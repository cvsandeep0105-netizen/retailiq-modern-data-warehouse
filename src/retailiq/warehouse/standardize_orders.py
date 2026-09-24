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
    CREATE TABLE IF NOT EXISTS intermediate.int_orders (
        order_id TEXT NOT NULL,
        customer_id TEXT NOT NULL,
        order_status TEXT NOT NULL,
        order_purchase_timestamp TIMESTAMP NULL,
        order_approved_at TIMESTAMP NULL,
        order_delivered_carrier_date TIMESTAMP NULL,
        order_delivered_customer_date TIMESTAMP NULL,
        order_estimated_delivery_date DATE NULL
    )
    """)

    cur.execute("TRUNCATE TABLE intermediate.int_orders")

    cur.execute("""
    INSERT INTO intermediate.int_orders
    SELECT
        TRIM(order_id),
        TRIM(customer_id),
        LOWER(TRIM(order_status)),
        NULLIF(TRIM(order_purchase_timestamp), '')::TIMESTAMP,
        NULLIF(TRIM(order_approved_at), '')::TIMESTAMP,
        NULLIF(TRIM(order_delivered_carrier_date), '')::TIMESTAMP,
        NULLIF(TRIM(order_delivered_customer_date), '')::TIMESTAMP,
        NULLIF(TRIM(order_estimated_delivery_date), '')::DATE
    FROM staging.stg_orders
    """)

    cur.execute("SELECT COUNT(*) FROM staging.stg_orders")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM intermediate.int_orders")
    target_count=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM intermediate.int_orders
    WHERE order_id IS NULL
       OR customer_id IS NULL
       OR order_status IS NULL
    """)
    invalid_keys=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM intermediate.int_orders
    WHERE order_status NOT IN (
        'delivered','shipped','canceled','unavailable',
        'invoiced','processing','created','approved'
    )
    """)
    invalid_status=cur.fetchone()[0]

    row_status="PASS" if source_count==target_count else "FAIL"
    key_status="PASS" if invalid_keys==0 else "FAIL"
    domain_status="PASS" if invalid_status==0 else "FAIL"

    print(f"SOURCE_ROW_COUNT={source_count}")
    print(f"STANDARDIZED_ROW_COUNT={target_count}")
    print(f"ROW_COUNT_STATUS={row_status}")
    print(f"INVALID_REQUIRED_KEYS={invalid_keys}")
    print(f"REQUIRED_KEY_STATUS={key_status}")
    print(f"INVALID_ORDER_STATUS_VALUES={invalid_status}")
    print(f"ORDER_STATUS_DOMAIN_STATUS={domain_status}")

    if row_status=="PASS" and key_status=="PASS" and domain_status=="PASS":
        conn.commit()
        print("PASS - ORDERS STANDARDIZATION COMPLETE")
    else:
        conn.rollback()
        raise RuntimeError("Orders standardization validation failed")

except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
