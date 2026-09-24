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
    CREATE TABLE IF NOT EXISTS warehouse.dim_customer (
        customer_sk BIGSERIAL PRIMARY KEY,
        customer_id TEXT NOT NULL UNIQUE,
        customer_unique_id TEXT NOT NULL,
        customer_zip_code_prefix INTEGER,
        customer_city TEXT,
        customer_state TEXT,
        record_source TEXT NOT NULL DEFAULT 'olist',
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("TRUNCATE TABLE warehouse.dim_customer RESTART IDENTITY")

    cur.execute("""
    INSERT INTO warehouse.dim_customer (
        customer_id,
        customer_unique_id,
        customer_zip_code_prefix,
        customer_city,
        customer_state
    )
    SELECT DISTINCT ON (customer_id)
        customer_id,
        customer_unique_id,
        customer_zip_code_prefix,
        customer_city,
        customer_state
    FROM intermediate.int_customers
    WHERE customer_id IS NOT NULL
    ORDER BY customer_id
    """)

    cur.execute("SELECT COUNT(*) FROM intermediate.int_customers WHERE customer_id IS NOT NULL")
    source_count=cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM warehouse.dim_customer")
    target_count=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM (
        SELECT customer_id
        FROM warehouse.dim_customer
        GROUP BY customer_id
        HAVING COUNT(*) > 1
    ) d
    """)
    duplicate_keys=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.dim_customer
    WHERE customer_sk IS NULL
       OR customer_id IS NULL
       OR customer_unique_id IS NULL
    """)
    invalid_required=cur.fetchone()[0]

    row_status="PASS" if source_count==target_count else "FAIL"
    key_status="PASS" if duplicate_keys==0 else "FAIL"
    required_status="PASS" if invalid_required==0 else "FAIL"

    print(f"SOURCE_CUSTOMER_COUNT={source_count}")
    print(f"DIM_CUSTOMER_COUNT={target_count}")
    print(f"ROW_RECONCILIATION_STATUS={row_status}")
    print(f"DUPLICATE_NATURAL_KEYS={duplicate_keys}")
    print(f"NATURAL_KEY_STATUS={key_status}")
    print(f"INVALID_REQUIRED_ATTRIBUTES={invalid_required}")
    print(f"REQUIRED_ATTRIBUTE_STATUS={required_status}")

    if row_status=="PASS" and key_status=="PASS" and required_status=="PASS":
        conn.commit()
        print("PASS - DIM_CUSTOMER CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("dim_customer validation failed")

except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
