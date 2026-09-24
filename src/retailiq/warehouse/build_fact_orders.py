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
    CREATE TABLE IF NOT EXISTS warehouse.fact_orders (
        order_sk BIGSERIAL PRIMARY KEY,
        order_id TEXT NOT NULL UNIQUE,
        customer_sk BIGINT NOT NULL,
        purchase_date_sk INTEGER NOT NULL,
        approved_date_sk INTEGER NULL,
        delivered_carrier_date_sk INTEGER NULL,
        delivered_customer_date_sk INTEGER NULL,
        estimated_delivery_date_sk INTEGER NULL,
        order_status TEXT NOT NULL,
        order_purchase_timestamp TIMESTAMP NULL,
        order_approved_at TIMESTAMP NULL,
        order_delivered_carrier_date TIMESTAMP NULL,
        order_delivered_customer_date TIMESTAMP NULL,
        order_estimated_delivery_date DATE NULL,
        delivery_duration_days NUMERIC(12,2) NULL,
        estimated_delivery_difference_days NUMERIC(12,2) NULL,
        is_delivered BOOLEAN NOT NULL,
        is_on_time BOOLEAN NULL,
        is_late BOOLEAN NULL,
        record_source TEXT NOT NULL DEFAULT 'olist',
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT fk_fact_orders_customer FOREIGN KEY(customer_sk) REFERENCES warehouse.dim_customer(customer_sk),
        CONSTRAINT fk_fact_orders_purchase_date FOREIGN KEY(purchase_date_sk) REFERENCES warehouse.dim_date(date_sk),
        CONSTRAINT fk_fact_orders_approved_date FOREIGN KEY(approved_date_sk) REFERENCES warehouse.dim_date(date_sk),
        CONSTRAINT fk_fact_orders_carrier_date FOREIGN KEY(delivered_carrier_date_sk) REFERENCES warehouse.dim_date(date_sk),
        CONSTRAINT fk_fact_orders_customer_date FOREIGN KEY(delivered_customer_date_sk) REFERENCES warehouse.dim_date(date_sk),
        CONSTRAINT fk_fact_orders_estimated_date FOREIGN KEY(estimated_delivery_date_sk) REFERENCES warehouse.dim_date(date_sk)
    )
    """)

    cur.execute("TRUNCATE TABLE warehouse.fact_orders RESTART IDENTITY")

    cur.execute("""
    INSERT INTO warehouse.fact_orders (
        order_id, customer_sk, purchase_date_sk, approved_date_sk,
        delivered_carrier_date_sk, delivered_customer_date_sk,
        estimated_delivery_date_sk, order_status,
        order_purchase_timestamp, order_approved_at,
        order_delivered_carrier_date, order_delivered_customer_date,
        order_estimated_delivery_date, delivery_duration_days,
        estimated_delivery_difference_days, is_delivered, is_on_time, is_late
    )
    SELECT
        o.order_id,
        dc.customer_sk,
        TO_CHAR(o.order_purchase_timestamp,'YYYYMMDD')::INTEGER,
        CASE WHEN o.order_approved_at IS NOT NULL THEN TO_CHAR(o.order_approved_at,'YYYYMMDD')::INTEGER END,
        CASE WHEN o.order_delivered_carrier_date IS NOT NULL THEN TO_CHAR(o.order_delivered_carrier_date,'YYYYMMDD')::INTEGER END,
        CASE WHEN o.order_delivered_customer_date IS NOT NULL THEN TO_CHAR(o.order_delivered_customer_date,'YYYYMMDD')::INTEGER END,
        CASE WHEN o.order_estimated_delivery_date IS NOT NULL THEN TO_CHAR(o.order_estimated_delivery_date,'YYYYMMDD')::INTEGER END,
        o.order_status,
        o.order_purchase_timestamp,
        o.order_approved_at,
        o.order_delivered_carrier_date,
        o.order_delivered_customer_date,
        o.order_estimated_delivery_date,
        CASE
            WHEN o.order_delivered_customer_date IS NOT NULL
            THEN ROUND(EXTRACT(EPOCH FROM (o.order_delivered_customer_date-o.order_purchase_timestamp))/86400.0,2)
        END,
        CASE
            WHEN o.order_delivered_customer_date IS NOT NULL AND o.order_estimated_delivery_date IS NOT NULL
            THEN ROUND(EXTRACT(EPOCH FROM (o.order_delivered_customer_date-(o.order_estimated_delivery_date + INTERVAL '1 day')))/86400.0,2)
        END,
        o.order_status='delivered',
        CASE
            WHEN o.order_status='delivered' AND o.order_delivered_customer_date IS NOT NULL AND o.order_estimated_delivery_date IS NOT NULL
            THEN o.order_delivered_customer_date::DATE <= o.order_estimated_delivery_date
        END,
        CASE
            WHEN o.order_status='delivered' AND o.order_delivered_customer_date IS NOT NULL AND o.order_estimated_delivery_date IS NOT NULL
            THEN o.order_delivered_customer_date::DATE > o.order_estimated_delivery_date
        END
    FROM intermediate.int_orders o
    JOIN warehouse.dim_customer dc ON o.customer_id=dc.customer_id
    WHERE o.order_id IS NOT NULL
      AND o.order_purchase_timestamp IS NOT NULL
    """)

    cur.execute("SELECT COUNT(*) FROM intermediate.int_orders WHERE order_id IS NOT NULL AND order_purchase_timestamp IS NOT NULL")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM warehouse.fact_orders")
    fact_count=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM (
        SELECT order_id
        FROM warehouse.fact_orders
        GROUP BY order_id
        HAVING COUNT(*)>1
    ) d
    """)
    duplicate_grain=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.fact_orders f
    LEFT JOIN warehouse.dim_customer dc ON f.customer_sk=dc.customer_sk
    LEFT JOIN warehouse.dim_date dd ON f.purchase_date_sk=dd.date_sk
    WHERE dc.customer_sk IS NULL OR dd.date_sk IS NULL
    """)
    orphan_keys=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.fact_orders
    WHERE delivery_duration_days IS NOT NULL
      AND delivery_duration_days < 0
    """)
    invalid_duration=cur.fetchone()[0]

    row_status="PASS" if source_count==fact_count else "FAIL"
    grain_status="PASS" if duplicate_grain==0 else "FAIL"
    fk_status="PASS" if orphan_keys==0 else "FAIL"
    duration_status="PASS" if invalid_duration==0 else "FAIL"

    print(f"SOURCE_ORDER_COUNT={source_count}")
    print(f"FACT_ORDER_COUNT={fact_count}")
    print(f"ROW_RECONCILIATION_STATUS={row_status}")
    print(f"DUPLICATE_ORDER_GRAIN={duplicate_grain}")
    print(f"FACT_GRAIN_STATUS={grain_status}")
    print(f"ORPHAN_CUSTOMER_OR_DATE_KEYS={orphan_keys}")
    print(f"FOREIGN_KEY_STATUS={fk_status}")
    print(f"INVALID_NEGATIVE_DELIVERY_DURATION={invalid_duration}")
    print(f"DELIVERY_DURATION_STATUS={duration_status}")

    if row_status=="PASS" and grain_status=="PASS" and fk_status=="PASS" and duration_status=="PASS":
        conn.commit()
        print("PASS - FACT_ORDERS CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("fact_orders validation failed")

except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
