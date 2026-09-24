from pathlib import Path
import psycopg2

def load_env():
    values={}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        line=line.strip()
        if line and not line.startswith("#") and "=" in line:
            k,v=line.split("=",1)
            values[k.strip()]=v.strip()
    return values

cfg=load_env()
conn=psycopg2.connect(host=cfg["POSTGRES_HOST"],port=int(cfg["POSTGRES_PORT"]),dbname=cfg["POSTGRES_DB"],user=cfg["POSTGRES_USER"],password=cfg["POSTGRES_PASSWORD"])
cur=conn.cursor()

try:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS warehouse.fact_order_items (
        order_item_sk BIGSERIAL PRIMARY KEY,
        order_id TEXT NOT NULL,
        order_item_id INTEGER NOT NULL,
        customer_sk BIGINT NOT NULL,
        product_sk BIGINT NOT NULL,
        seller_sk BIGINT NOT NULL,
        order_date_sk INTEGER NOT NULL,
        shipping_limit_date TIMESTAMP NULL,
        item_price NUMERIC(18,2) NOT NULL,
        freight_value NUMERIC(18,2) NOT NULL,
        total_item_value NUMERIC(18,2) NOT NULL,
        record_source TEXT NOT NULL DEFAULT 'olist',
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT uq_fact_order_item UNIQUE(order_id,order_item_id),
        CONSTRAINT fk_fact_customer FOREIGN KEY(customer_sk) REFERENCES warehouse.dim_customer(customer_sk),
        CONSTRAINT fk_fact_product FOREIGN KEY(product_sk) REFERENCES warehouse.dim_product(product_sk),
        CONSTRAINT fk_fact_seller FOREIGN KEY(seller_sk) REFERENCES warehouse.dim_seller(seller_sk),
        CONSTRAINT fk_fact_date FOREIGN KEY(order_date_sk) REFERENCES warehouse.dim_date(date_sk)
    )
    """)

    cur.execute("TRUNCATE TABLE warehouse.fact_order_items RESTART IDENTITY")

    cur.execute("""
    INSERT INTO warehouse.fact_order_items (
        order_id, order_item_id, customer_sk, product_sk, seller_sk,
        order_date_sk, shipping_limit_date, item_price, freight_value,
        total_item_value
    )
    SELECT
        oi.order_id,
        oi.order_item_id,
        dc.customer_sk,
        dp.product_sk,
        ds.seller_sk,
        TO_CHAR(o.order_purchase_timestamp,'YYYYMMDD')::INTEGER,
        oi.shipping_limit_date,
        ROUND(oi.price::NUMERIC,2),
        ROUND(oi.freight_value::NUMERIC,2),
        ROUND((oi.price + oi.freight_value)::NUMERIC,2)
    FROM intermediate.int_order_items oi
    JOIN intermediate.int_orders o
      ON oi.order_id=o.order_id
    JOIN warehouse.dim_customer dc
      ON o.customer_id=dc.customer_id
    JOIN warehouse.dim_product dp
      ON oi.product_id=dp.product_id
    JOIN warehouse.dim_seller ds
      ON oi.seller_id=ds.seller_id
    WHERE o.order_purchase_timestamp IS NOT NULL
    """)

    cur.execute("SELECT COUNT(*) FROM intermediate.int_order_items")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM warehouse.fact_order_items")
    fact_count=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*) FROM (
        SELECT order_id,order_item_id
        FROM warehouse.fact_order_items
        GROUP BY order_id,order_item_id
        HAVING COUNT(*)>1
    ) d
    """)
    duplicate_grain=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.fact_order_items f
    LEFT JOIN warehouse.dim_customer d ON f.customer_sk=d.customer_sk
    LEFT JOIN warehouse.dim_product p ON f.product_sk=p.product_sk
    LEFT JOIN warehouse.dim_seller s ON f.seller_sk=s.seller_sk
    LEFT JOIN warehouse.dim_date dt ON f.order_date_sk=dt.date_sk
    WHERE d.customer_sk IS NULL
       OR p.product_sk IS NULL
       OR s.seller_sk IS NULL
       OR dt.date_sk IS NULL
    """)
    orphan_keys=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.fact_order_items
    WHERE item_price < 0 OR freight_value < 0 OR total_item_value < 0
    """)
    invalid_measures=cur.fetchone()[0]

    row_status="PASS" if source_count==fact_count else "FAIL"
    grain_status="PASS" if duplicate_grain==0 else "FAIL"
    fk_status="PASS" if orphan_keys==0 else "FAIL"
    measure_status="PASS" if invalid_measures==0 else "FAIL"

    print(f"SOURCE_ORDER_ITEM_COUNT={source_count}")
    print(f"FACT_ORDER_ITEM_COUNT={fact_count}")
    print(f"ROW_RECONCILIATION_STATUS={row_status}")
    print(f"DUPLICATE_FACT_GRAIN={duplicate_grain}")
    print(f"FACT_GRAIN_STATUS={grain_status}")
    print(f"ORPHAN_DIMENSION_KEYS={orphan_keys}")
    print(f"FOREIGN_KEY_STATUS={fk_status}")
    print(f"INVALID_NEGATIVE_MEASURES={invalid_measures}")
    print(f"MEASURE_STATUS={measure_status}")

    if row_status=="PASS" and grain_status=="PASS" and fk_status=="PASS" and measure_status=="PASS":
        conn.commit()
        print("PASS - FACT_ORDER_ITEMS CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("fact_order_items validation failed")

except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
