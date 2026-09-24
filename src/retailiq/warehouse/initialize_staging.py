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

tables={
    "stg_customers":"""CREATE TABLE IF NOT EXISTS staging.stg_customers AS SELECT * FROM raw.olist_customers WITH NO DATA""",
    "stg_geolocation":"""CREATE TABLE IF NOT EXISTS staging.stg_geolocation AS SELECT * FROM raw.olist_geolocation WITH NO DATA""",
    "stg_orders":"""CREATE TABLE IF NOT EXISTS staging.stg_orders AS SELECT * FROM raw.olist_orders WITH NO DATA""",
    "stg_order_items":"""CREATE TABLE IF NOT EXISTS staging.stg_order_items AS SELECT * FROM raw.olist_order_items WITH NO DATA""",
    "stg_order_payments":"""CREATE TABLE IF NOT EXISTS staging.stg_order_payments AS SELECT * FROM raw.olist_order_payments WITH NO DATA""",
    "stg_order_reviews":"""CREATE TABLE IF NOT EXISTS staging.stg_order_reviews AS SELECT * FROM raw.olist_order_reviews WITH NO DATA""",
    "stg_products":"""CREATE TABLE IF NOT EXISTS staging.stg_products AS SELECT * FROM raw.olist_products WITH NO DATA""",
    "stg_sellers":"""CREATE TABLE IF NOT EXISTS staging.stg_sellers AS SELECT * FROM raw.olist_sellers WITH NO DATA""",
    "stg_category_translation":"""CREATE TABLE IF NOT EXISTS staging.stg_category_translation AS SELECT * FROM raw.product_category_name_translation WITH NO DATA"""
}

try:
    for name,sql in tables.items():
        cur.execute(sql)
        print(f"{name}: FOUNDATION=PASS")
    conn.commit()
    cur.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='staging' AND table_name LIKE 'stg_%'""")
    count=cur.fetchone()[0]
    print(f"STAGING_TABLE_COUNT={count}")
    print("PASS - STAGING FOUNDATION CREATED")
except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
