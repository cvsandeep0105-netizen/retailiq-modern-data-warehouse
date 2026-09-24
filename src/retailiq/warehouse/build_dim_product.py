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
    CREATE TABLE IF NOT EXISTS warehouse.dim_product (
        product_sk BIGSERIAL PRIMARY KEY,
        product_id TEXT NOT NULL UNIQUE,
        product_category_name TEXT,
        product_category_name_english TEXT,
        product_name_length DOUBLE PRECISION,
        product_description_length DOUBLE PRECISION,
        product_photos_qty DOUBLE PRECISION,
        product_weight_g INTEGER,
        product_length_cm INTEGER,
        product_height_cm INTEGER,
        product_width_cm INTEGER,
        record_source TEXT NOT NULL DEFAULT 'olist',
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("TRUNCATE TABLE warehouse.dim_product RESTART IDENTITY")

    cur.execute("""
    INSERT INTO warehouse.dim_product (
        product_id, product_category_name, product_category_name_english,
        product_name_length, product_description_length, product_photos_qty,
        product_weight_g, product_length_cm, product_height_cm, product_width_cm
    )
    SELECT
        p.product_id,
        p.product_category_name,
        t.product_category_name_english,
        p.product_name_lenght,
        p.product_description_lenght,
        p.product_photos_qty,
        p.product_weight_g,
        p.product_length_cm,
        p.product_height_cm,
        p.product_width_cm
    FROM intermediate.int_products p
    LEFT JOIN intermediate.int_category_translation t
      ON p.product_category_name=t.product_category_name
    WHERE p.product_id IS NOT NULL
    """)

    cur.execute("SELECT COUNT(*) FROM intermediate.int_products WHERE product_id IS NOT NULL")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM warehouse.dim_product")
    target_count=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM (
        SELECT product_id
        FROM warehouse.dim_product
        GROUP BY product_id
        HAVING COUNT(*) > 1
    ) d
    """)
    duplicate_keys=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.dim_product
    WHERE product_sk IS NULL OR product_id IS NULL
    """)
    invalid_required=cur.fetchone()[0]

    row_status="PASS" if source_count==target_count else "FAIL"
    key_status="PASS" if duplicate_keys==0 else "FAIL"
    required_status="PASS" if invalid_required==0 else "FAIL"

    print(f"SOURCE_PRODUCT_COUNT={source_count}")
    print(f"DIM_PRODUCT_COUNT={target_count}")
    print(f"ROW_RECONCILIATION_STATUS={row_status}")
    print(f"DUPLICATE_NATURAL_KEYS={duplicate_keys}")
    print(f"NATURAL_KEY_STATUS={key_status}")
    print(f"INVALID_REQUIRED_ATTRIBUTES={invalid_required}")
    print(f"REQUIRED_ATTRIBUTE_STATUS={required_status}")

    if row_status=="PASS" and key_status=="PASS" and required_status=="PASS":
        conn.commit()
        print("PASS - DIM_PRODUCT CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("dim_product validation failed")

except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
