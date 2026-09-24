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
    CREATE TABLE IF NOT EXISTS marts.customer (
        customer_sk BIGINT PRIMARY KEY,
        customer_id TEXT NOT NULL UNIQUE,
        customer_unique_id TEXT NOT NULL,
        customer_city TEXT,
        customer_state TEXT,
        order_count INTEGER NOT NULL,
        order_item_count INTEGER NOT NULL,
        sales_item_value NUMERIC(18,2) NOT NULL,
        freight_value NUMERIC(18,2) NOT NULL,
        total_spend NUMERIC(18,2) NOT NULL,
        payment_value NUMERIC(18,2) NOT NULL,
        payment_count INTEGER NOT NULL,
        review_count INTEGER NOT NULL,
        average_review_score NUMERIC(10,2) NULL,
        first_order_timestamp TIMESTAMP NULL,
        last_order_timestamp TIMESTAMP NULL,
        orders_per_customer NUMERIC(10,2) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("TRUNCATE TABLE marts.customer")

    cur.execute("""
    INSERT INTO marts.customer (
        customer_sk,customer_id,customer_unique_id,customer_city,customer_state,
        order_count,order_item_count,sales_item_value,freight_value,total_spend,
        payment_value,payment_count,review_count,average_review_score,
        first_order_timestamp,last_order_timestamp,orders_per_customer
    )
    SELECT
        dc.customer_sk,
        dc.customer_id,
        dc.customer_unique_id,
        dc.customer_city,
        dc.customer_state,
        COALESCE(o.order_count,0),
        COALESCE(i.order_item_count,0),
        COALESCE(i.sales_item_value,0),
        COALESCE(i.freight_value,0),
        COALESCE(i.sales_item_value,0)+COALESCE(i.freight_value,0),
        COALESCE(p.payment_value,0),
        COALESCE(p.payment_count,0),
        COALESCE(r.review_count,0),
        r.average_review_score,
        o.first_order_timestamp,
        o.last_order_timestamp,
        COALESCE(o.order_count,0)::NUMERIC(10,2)
    FROM warehouse.dim_customer dc
    LEFT JOIN (
        SELECT customer_sk,COUNT(*) AS order_count,
               MIN(order_purchase_timestamp) AS first_order_timestamp,
               MAX(order_purchase_timestamp) AS last_order_timestamp
        FROM warehouse.fact_orders
        GROUP BY customer_sk
    ) o ON dc.customer_sk=o.customer_sk
    LEFT JOIN (
        SELECT customer_sk,COUNT(*) AS order_item_count,
               SUM(item_price) AS sales_item_value,
               SUM(freight_value) AS freight_value
        FROM warehouse.fact_order_items
        GROUP BY customer_sk
    ) i ON dc.customer_sk=i.customer_sk
    LEFT JOIN (
        SELECT customer_sk,SUM(payment_value) AS payment_value,COUNT(*) AS payment_count
        FROM warehouse.fact_payments
        GROUP BY customer_sk
    ) p ON dc.customer_sk=p.customer_sk
    LEFT JOIN (
        SELECT customer_sk,COUNT(*) AS review_count,AVG(review_score)::NUMERIC(10,2) AS average_review_score
        FROM warehouse.fact_reviews
        GROUP BY customer_sk
    ) r ON dc.customer_sk=r.customer_sk
    """)

    cur.execute("SELECT COUNT(*) FROM warehouse.dim_customer")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM marts.customer")
    mart_count=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT customer_sk FROM marts.customer GROUP BY customer_sk HAVING COUNT(*)>1) x""")
    duplicate_customers=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.customer WHERE order_count<0 OR order_item_count<0 OR sales_item_value<0 OR freight_value<0 OR total_spend<0 OR payment_value<0 OR payment_count<0 OR review_count<0""")
    invalid_measures=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.customer WHERE order_count>0 AND orders_per_customer<>order_count""")
    invalid_frequency=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.customer m LEFT JOIN warehouse.dim_customer d ON m.customer_sk=d.customer_sk WHERE d.customer_sk IS NULL""")
    orphan_customers=cur.fetchone()[0]

    print(f"SOURCE_CUSTOMER_COUNT={source_count}")
    print(f"MART_CUSTOMER_COUNT={mart_count}")
    print(f"ROW_RECONCILIATION_STATUS={'PASS' if source_count==mart_count else 'FAIL'}")
    print(f"DUPLICATE_CUSTOMER_GRAIN={duplicate_customers}")
    print(f"CUSTOMER_GRAIN_STATUS={'PASS' if duplicate_customers==0 else 'FAIL'}")
    print(f"INVALID_CUSTOMER_MEASURES={invalid_measures}")
    print(f"MEASURE_STATUS={'PASS' if invalid_measures==0 else 'FAIL'}")
    print(f"INVALID_ORDER_FREQUENCY_ROWS={invalid_frequency}")
    print(f"ORDER_FREQUENCY_STATUS={'PASS' if invalid_frequency==0 else 'FAIL'}")
    print(f"ORPHAN_CUSTOMER_KEYS={orphan_customers}")
    print(f"CUSTOMER_DIMENSION_LINK_STATUS={'PASS' if orphan_customers==0 else 'FAIL'}")

    if source_count==mart_count and duplicate_customers==0 and invalid_measures==0 and invalid_frequency==0 and orphan_customers==0:
        conn.commit()
        print("PASS - CUSTOMER MART CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("customer mart validation failed")
finally:
    cur.close()
    conn.close()
