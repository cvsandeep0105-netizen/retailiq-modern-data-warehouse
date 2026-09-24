from pathlib import Path
import psycopg2

def env():
    d={}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k,v=line.split("=",1); d[k.strip()]=v.strip()
    return d

c=env()
conn=psycopg2.connect(host=c["POSTGRES_HOST"],port=int(c["POSTGRES_PORT"]),dbname=c["POSTGRES_DB"],user=c["POSTGRES_USER"],password=c["POSTGRES_PASSWORD"])
cur=conn.cursor()

try:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS marts.seller_fulfillment (
        seller_sk BIGINT PRIMARY KEY,
        seller_id TEXT NOT NULL UNIQUE,
        seller_city TEXT,
        seller_state TEXT,
        order_count INTEGER NOT NULL,
        order_item_count INTEGER NOT NULL,
        customer_count INTEGER NOT NULL,
        sales_item_value NUMERIC(18,2) NOT NULL,
        freight_value NUMERIC(18,2) NOT NULL,
        total_item_value NUMERIC(18,2) NOT NULL,
        average_item_price NUMERIC(18,2) NULL,
        delivered_order_count INTEGER NOT NULL,
        on_time_order_count INTEGER NOT NULL,
        late_order_count INTEGER NOT NULL,
        average_delivery_duration_days NUMERIC(10,2) NULL,
        review_count INTEGER NOT NULL,
        average_review_score NUMERIC(10,2) NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("TRUNCATE TABLE marts.seller_fulfillment")

    cur.execute("""
    INSERT INTO marts.seller_fulfillment (
        seller_sk,seller_id,seller_city,seller_state,
        order_count,order_item_count,customer_count,
        sales_item_value,freight_value,total_item_value,average_item_price,
        delivered_order_count,on_time_order_count,late_order_count,
        average_delivery_duration_days,review_count,average_review_score
    )
    SELECT
        ds.seller_sk,
        ds.seller_id,
        ds.seller_city,
        ds.seller_state,
        COALESCE(i.order_count,0),
        COALESCE(i.order_item_count,0),
        COALESCE(i.customer_count,0),
        COALESCE(i.sales_item_value,0),
        COALESCE(i.freight_value,0),
        COALESCE(i.sales_item_value,0)+COALESCE(i.freight_value,0),
        i.average_item_price,
        COALESCE(f.delivered_order_count,0),
        COALESCE(f.on_time_order_count,0),
        COALESCE(f.late_order_count,0),
        f.average_delivery_duration_days,
        COALESCE(r.review_count,0),
        r.average_review_score
    FROM warehouse.dim_seller ds
    LEFT JOIN (
        SELECT seller_sk,
               COUNT(DISTINCT order_id) AS order_count,
               COUNT(*) AS order_item_count,
               COUNT(DISTINCT customer_sk) AS customer_count,
               SUM(item_price) AS sales_item_value,
               SUM(freight_value) AS freight_value,
               AVG(item_price)::NUMERIC(18,2) AS average_item_price
        FROM warehouse.fact_order_items
        GROUP BY seller_sk
    ) i ON ds.seller_sk=i.seller_sk
    LEFT JOIN (
        SELECT foi.seller_sk,
               COUNT(DISTINCT CASE WHEN fo.is_delivered THEN fo.order_id END) AS delivered_order_count,
               COUNT(DISTINCT CASE WHEN fo.is_on_time THEN fo.order_id END) AS on_time_order_count,
               COUNT(DISTINCT CASE WHEN fo.is_late THEN fo.order_id END) AS late_order_count,
               AVG(CASE WHEN fo.delivery_duration_days IS NOT NULL THEN fo.delivery_duration_days END)::NUMERIC(10,2) AS average_delivery_duration_days
        FROM warehouse.fact_order_items foi
        JOIN warehouse.fact_orders fo ON foi.order_id=fo.order_id
        GROUP BY foi.seller_sk
    ) f ON ds.seller_sk=f.seller_sk
    LEFT JOIN (
        SELECT foi.seller_sk,
               COUNT(DISTINCT fr.review_sk) AS review_count,
               AVG(fr.review_score)::NUMERIC(10,2) AS average_review_score
        FROM warehouse.fact_order_items foi
        JOIN warehouse.fact_reviews fr ON foi.order_id=fr.order_id
        GROUP BY foi.seller_sk
    ) r ON ds.seller_sk=r.seller_sk
    """)

    cur.execute("SELECT COUNT(*) FROM warehouse.dim_seller")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM marts.seller_fulfillment")
    mart_count=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT seller_sk FROM marts.seller_fulfillment GROUP BY seller_sk HAVING COUNT(*)>1) x""")
    duplicate_sellers=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.seller_fulfillment WHERE order_count<0 OR order_item_count<0 OR customer_count<0 OR sales_item_value<0 OR freight_value<0 OR total_item_value<0 OR delivered_order_count<0 OR on_time_order_count<0 OR late_order_count<0 OR review_count<0""")
    invalid_measures=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.seller_fulfillment WHERE delivered_order_count>order_count OR on_time_order_count>delivered_order_count OR late_order_count>delivered_order_count""")
    invalid_fulfillment=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.seller_fulfillment WHERE average_review_score IS NOT NULL AND (average_review_score<1 OR average_review_score>5)""")
    invalid_reviews=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.seller_fulfillment m LEFT JOIN warehouse.dim_seller d ON m.seller_sk=d.seller_sk WHERE d.seller_sk IS NULL""")
    orphan_sellers=cur.fetchone()[0]

    print(f"SOURCE_SELLER_COUNT={source_count}")
    print(f"MART_SELLER_COUNT={mart_count}")
    print(f"ROW_RECONCILIATION_STATUS={'PASS' if source_count==mart_count else 'FAIL'}")
    print(f"DUPLICATE_SELLER_GRAIN={duplicate_sellers}")
    print(f"SELLER_GRAIN_STATUS={'PASS' if duplicate_sellers==0 else 'FAIL'}")
    print(f"INVALID_SELLER_MEASURES={invalid_measures}")
    print(f"MEASURE_STATUS={'PASS' if invalid_measures==0 else 'FAIL'}")
    print(f"INVALID_FULFILLMENT_RELATIONSHIPS={invalid_fulfillment}")
    print(f"FULFILLMENT_STATUS={'PASS' if invalid_fulfillment==0 else 'FAIL'}")
    print(f"INVALID_SELLER_REVIEW_RATINGS={invalid_reviews}")
    print(f"REVIEW_RATING_STATUS={'PASS' if invalid_reviews==0 else 'FAIL'}")
    print(f"ORPHAN_SELLER_KEYS={orphan_sellers}")
    print(f"SELLER_DIMENSION_LINK_STATUS={'PASS' if orphan_sellers==0 else 'FAIL'}")

    if source_count==mart_count and duplicate_sellers==0 and invalid_measures==0 and invalid_fulfillment==0 and invalid_reviews==0 and orphan_sellers==0:
        conn.commit()
        print("PASS - SELLER FULFILLMENT MART CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("seller fulfillment mart validation failed")
finally:
    cur.close()
    conn.close()
