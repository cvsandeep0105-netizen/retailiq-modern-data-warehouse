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
    CREATE TABLE IF NOT EXISTS marts.product (
        product_sk BIGINT PRIMARY KEY,
        product_id TEXT NOT NULL UNIQUE,
        product_category_name TEXT,
        product_category_name_english TEXT,
        product_weight_g INTEGER,
        product_length_cm INTEGER,
        product_height_cm INTEGER,
        product_width_cm INTEGER,
        product_order_count INTEGER NOT NULL,
        order_item_count INTEGER NOT NULL,
        seller_count INTEGER NOT NULL,
        sales_item_value NUMERIC(18,2) NOT NULL,
        freight_value NUMERIC(18,2) NOT NULL,
        total_item_value NUMERIC(18,2) NOT NULL,
        average_item_price NUMERIC(18,2) NULL,
        review_count INTEGER NOT NULL,
        average_review_score NUMERIC(10,2) NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("TRUNCATE TABLE marts.product")

    cur.execute("""
    INSERT INTO marts.product (
        product_sk,product_id,product_category_name,product_category_name_english,
        product_weight_g,product_length_cm,product_height_cm,product_width_cm,
        product_order_count,order_item_count,seller_count,
        sales_item_value,freight_value,total_item_value,average_item_price,
        review_count,average_review_score
    )
    SELECT
        dp.product_sk,
        dp.product_id,
        dp.product_category_name,
        dp.product_category_name_english,
        dp.product_weight_g,
        dp.product_length_cm,
        dp.product_height_cm,
        dp.product_width_cm,
        COALESCE(i.product_order_count,0),
        COALESCE(i.order_item_count,0),
        COALESCE(i.seller_count,0),
        COALESCE(i.sales_item_value,0),
        COALESCE(i.freight_value,0),
        COALESCE(i.sales_item_value,0)+COALESCE(i.freight_value,0),
        i.average_item_price,
        COALESCE(r.review_count,0),
        r.average_review_score
    FROM warehouse.dim_product dp
    LEFT JOIN (
        SELECT product_sk,
               COUNT(DISTINCT order_id) AS product_order_count,
               COUNT(*) AS order_item_count,
               COUNT(DISTINCT seller_sk) AS seller_count,
               SUM(item_price) AS sales_item_value,
               SUM(freight_value) AS freight_value,
               AVG(item_price)::NUMERIC(18,2) AS average_item_price
        FROM warehouse.fact_order_items
        GROUP BY product_sk
    ) i ON dp.product_sk=i.product_sk
    LEFT JOIN (
        SELECT foi.product_sk,
               COUNT(fr.review_sk) AS review_count,
               AVG(fr.review_score)::NUMERIC(10,2) AS average_review_score
        FROM warehouse.fact_order_items foi
        JOIN warehouse.fact_reviews fr ON foi.order_id=fr.order_id
        GROUP BY foi.product_sk
    ) r ON dp.product_sk=r.product_sk
    """)

    cur.execute("SELECT COUNT(*) FROM warehouse.dim_product")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM marts.product")
    mart_count=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT product_sk FROM marts.product GROUP BY product_sk HAVING COUNT(*)>1) x""")
    duplicate_products=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.product WHERE product_order_count<0 OR order_item_count<0 OR seller_count<0 OR sales_item_value<0 OR freight_value<0 OR total_item_value<0 OR review_count<0""")
    invalid_measures=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.product WHERE average_review_score IS NOT NULL AND (average_review_score<1 OR average_review_score>5)""")
    invalid_reviews=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.product m LEFT JOIN warehouse.dim_product d ON m.product_sk=d.product_sk WHERE d.product_sk IS NULL""")
    orphan_products=cur.fetchone()[0]

    print(f"SOURCE_PRODUCT_COUNT={source_count}")
    print(f"MART_PRODUCT_COUNT={mart_count}")
    print(f"ROW_RECONCILIATION_STATUS={'PASS' if source_count==mart_count else 'FAIL'}")
    print(f"DUPLICATE_PRODUCT_GRAIN={duplicate_products}")
    print(f"PRODUCT_GRAIN_STATUS={'PASS' if duplicate_products==0 else 'FAIL'}")
    print(f"INVALID_PRODUCT_MEASURES={invalid_measures}")
    print(f"MEASURE_STATUS={'PASS' if invalid_measures==0 else 'FAIL'}")
    print(f"INVALID_PRODUCT_REVIEW_RATINGS={invalid_reviews}")
    print(f"REVIEW_RATING_STATUS={'PASS' if invalid_reviews==0 else 'FAIL'}")
    print(f"ORPHAN_PRODUCT_KEYS={orphan_products}")
    print(f"PRODUCT_DIMENSION_LINK_STATUS={'PASS' if orphan_products==0 else 'FAIL'}")

    if source_count==mart_count and duplicate_products==0 and invalid_measures==0 and invalid_reviews==0 and orphan_products==0:
        conn.commit()
        print("PASS - PRODUCT MART CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("product mart validation failed")
finally:
    cur.close()
    conn.close()
