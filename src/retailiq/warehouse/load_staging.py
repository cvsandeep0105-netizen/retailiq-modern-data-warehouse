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

mappings={
    "stg_customers":"olist_customers",
    "stg_geolocation":"olist_geolocation",
    "stg_orders":"olist_orders",
    "stg_order_items":"olist_order_items",
    "stg_order_payments":"olist_order_payments",
    "stg_order_reviews":"olist_order_reviews",
    "stg_products":"olist_products",
    "stg_sellers":"olist_sellers",
    "stg_category_translation":"product_category_name_translation"
}

try:
    for staging,raw in mappings.items():
        cur.execute(f'TRUNCATE TABLE staging."{staging}"')
        cur.execute(f'INSERT INTO staging."{staging}" SELECT * FROM raw."{raw}"')
        cur.execute(f'SELECT COUNT(*) FROM staging."{staging}"')
        count=cur.fetchone()[0]
        print(f"{staging}: ROW_COUNT={count} STATUS=PASS")
    conn.commit()
    print("PASS - STAGING DATA LOAD COMPLETE")
except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
