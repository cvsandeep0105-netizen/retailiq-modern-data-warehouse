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
    CREATE TABLE IF NOT EXISTS marts.sales_orders (
        order_id TEXT PRIMARY KEY,
        customer_sk BIGINT NOT NULL,
        purchase_date_sk INTEGER NOT NULL,
        order_status TEXT NOT NULL,
        order_purchase_timestamp TIMESTAMP NOT NULL,
        order_approved_at TIMESTAMP NULL,
        order_delivered_carrier_date TIMESTAMP NULL,
        order_delivered_customer_date TIMESTAMP NULL,
        order_estimated_delivery_date DATE NULL,
        order_item_count INTEGER NOT NULL,
        sales_item_value NUMERIC(18,2) NOT NULL,
        freight_value NUMERIC(18,2) NOT NULL,
        total_order_value NUMERIC(18,2) NOT NULL,
        payment_value NUMERIC(18,2) NOT NULL,
        payment_count INTEGER NOT NULL,
        review_count INTEGER NOT NULL,
        average_review_score NUMERIC(10,2) NULL,
        delivery_duration_days NUMERIC(10,2) NULL,
        estimated_delivery_difference_days NUMERIC(10,2) NULL,
        is_delivered BOOLEAN NOT NULL,
        is_on_time BOOLEAN NULL,
        is_late BOOLEAN NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("TRUNCATE TABLE marts.sales_orders")

    cur.execute("""
    INSERT INTO marts.sales_orders (
        order_id,customer_sk,purchase_date_sk,order_status,
        order_purchase_timestamp,order_approved_at,
        order_delivered_carrier_date,order_delivered_customer_date,
        order_estimated_delivery_date,order_item_count,
        sales_item_value,freight_value,total_order_value,
        payment_value,payment_count,review_count,average_review_score,
        delivery_duration_days,estimated_delivery_difference_days,
        is_delivered,is_on_time,is_late
    )
    SELECT
        fo.order_id,
        fo.customer_sk,
        fo.purchase_date_sk,
        fo.order_status,
        fo.order_purchase_timestamp,
        fo.order_approved_at,
        fo.order_delivered_carrier_date,
        fo.order_delivered_customer_date,
        fo.order_estimated_delivery_date,
        COALESCE(oi.order_item_count,0),
        COALESCE(oi.sales_item_value,0),
        COALESCE(oi.freight_value,0),
        COALESCE(oi.sales_item_value,0)+COALESCE(oi.freight_value,0),
        COALESCE(p.payment_value,0),
        COALESCE(p.payment_count,0),
        COALESCE(r.review_count,0),
        r.average_review_score,
        fo.delivery_duration_days,
        fo.estimated_delivery_difference_days,
        fo.is_delivered,
        fo.is_on_time,
        fo.is_late
    FROM warehouse.fact_orders fo
    LEFT JOIN (
        SELECT order_id,COUNT(*) AS order_item_count,
               SUM(item_price) AS sales_item_value,
               SUM(freight_value) AS freight_value
        FROM warehouse.fact_order_items
        GROUP BY order_id
    ) oi ON fo.order_id=oi.order_id
    LEFT JOIN (
        SELECT order_id,SUM(payment_value) AS payment_value,COUNT(*) AS payment_count
        FROM warehouse.fact_payments
        GROUP BY order_id
    ) p ON fo.order_id=p.order_id
    LEFT JOIN (
        SELECT order_id,COUNT(*) AS review_count,AVG(review_score)::NUMERIC(10,2) AS average_review_score
        FROM warehouse.fact_reviews
        GROUP BY order_id
    ) r ON fo.order_id=r.order_id
    """)

    cur.execute("SELECT COUNT(*) FROM warehouse.fact_orders")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM marts.sales_orders")
    mart_count=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT order_id FROM marts.sales_orders GROUP BY order_id HAVING COUNT(*)>1) x""")
    duplicate_orders=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.sales_orders WHERE sales_item_value<0 OR freight_value<0 OR total_order_value<0 OR payment_value<0""")
    invalid_measures=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.sales_orders s LEFT JOIN warehouse.dim_customer c ON s.customer_sk=c.customer_sk WHERE c.customer_sk IS NULL""")
    orphan_customers=cur.fetchone()[0]

    print(f"SOURCE_ORDER_COUNT={source_count}")
    print(f"MART_ORDER_COUNT={mart_count}")
    print(f"ROW_RECONCILIATION_STATUS={'PASS' if source_count==mart_count else 'FAIL'}")
    print(f"DUPLICATE_ORDER_GRAIN={duplicate_orders}")
    print(f"ORDER_GRAIN_STATUS={'PASS' if duplicate_orders==0 else 'FAIL'}")
    print(f"INVALID_MART_MEASURES={invalid_measures}")
    print(f"MEASURE_STATUS={'PASS' if invalid_measures==0 else 'FAIL'}")
    print(f"ORPHAN_CUSTOMER_KEYS={orphan_customers}")
    print(f"CUSTOMER_LINK_STATUS={'PASS' if orphan_customers==0 else 'FAIL'}")

    if source_count==mart_count and duplicate_orders==0 and invalid_measures==0 and orphan_customers==0:
        conn.commit()
        print("PASS - SALES ORDERS MART CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("sales_orders mart validation failed")
finally:
    cur.close()
    conn.close()
