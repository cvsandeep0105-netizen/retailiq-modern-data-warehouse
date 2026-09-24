from pathlib import Path
import csv
import os
import psycopg2

BASE=Path("data/raw")

TABLES={
    "olist_geolocation_dataset.csv":("olist_geolocation",[("geolocation_zip_code_prefix","INTEGER"),("geolocation_lat","DOUBLE PRECISION"),("geolocation_lng","DOUBLE PRECISION"),("geolocation_city","TEXT"),("geolocation_state","TEXT")]),
    "olist_orders_dataset.csv":("olist_orders",[("order_id","TEXT"),("customer_id","TEXT"),("order_status","TEXT"),("order_purchase_timestamp","TEXT"),("order_approved_at","TEXT"),("order_delivered_carrier_date","TEXT"),("order_delivered_customer_date","TEXT"),("order_estimated_delivery_date","TEXT")]),
    "olist_order_items_dataset.csv":("olist_order_items",[("order_id","TEXT"),("order_item_id","INTEGER"),("product_id","TEXT"),("seller_id","TEXT"),("shipping_limit_date","TEXT"),("price","DOUBLE PRECISION"),("freight_value","DOUBLE PRECISION")]),
    "olist_order_payments_dataset.csv":("olist_order_payments",[("order_id","TEXT"),("payment_sequential","INTEGER"),("payment_type","TEXT"),("payment_installments","INTEGER"),("payment_value","DOUBLE PRECISION")]),
    "olist_order_reviews_dataset.csv":("olist_order_reviews",[("review_id","TEXT"),("order_id","TEXT"),("review_score","INTEGER"),("review_comment_title","TEXT"),("review_comment_message","TEXT"),("review_creation_date","TEXT"),("review_answer_timestamp","TEXT")]),
    "olist_products_dataset.csv":("olist_products",[("product_id","TEXT"),("product_category_name","TEXT"),("product_name_lenght","DOUBLE PRECISION"),("product_description_lenght","DOUBLE PRECISION"),("product_photos_qty","DOUBLE PRECISION"),("product_weight_g","INTEGER"),("product_length_cm","INTEGER"),("product_height_cm","INTEGER"),("product_width_cm","INTEGER")]),
    "olist_sellers_dataset.csv":("olist_sellers",[("seller_id","TEXT"),("seller_zip_code_prefix","INTEGER"),("seller_city","TEXT"),("seller_state","TEXT")]),
    "product_category_name_translation.csv":("product_category_name_translation",[("product_category_name","TEXT"),("product_category_name_english","TEXT")])
}

def env_file():
    values={}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        line=line.strip()
        if line and not line.startswith("#") and "=" in line:
            k,v=line.split("=",1)
            values[k.strip()]=v.strip()
    return values

cfg=env_file()
conn=psycopg2.connect(host=cfg["POSTGRES_HOST"],port=int(cfg["POSTGRES_PORT"]),dbname=cfg["POSTGRES_DB"],user=cfg["POSTGRES_USER"],password=cfg["POSTGRES_PASSWORD"])
conn.autocommit=False
cur=conn.cursor()

try:
    for filename,(table,columns) in TABLES.items():
        path=BASE/filename
        names=", ".join(f"""\"{n}\"""" for n,_ in columns)
        definitions=", ".join(f"""\"{n}\" {t}""" for n,t in columns)
        cur.execute(f"""CREATE TABLE IF NOT EXISTS raw."{table}" ({definitions})""")
        cur.execute(f"""TRUNCATE TABLE raw."{table}" """)
        copy_sql=f"""COPY raw."{table}" ({names}) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, NULL '', ENCODING 'UTF8')"""
        with path.open("r",encoding="utf-8-sig",newline="") as fh:
            cur.copy_expert(copy_sql,fh)
        cur.execute(f"""SELECT COUNT(*) FROM raw."{table}" """)
        db_count=cur.fetchone()[0]
        with path.open("r",encoding="utf-8-sig",newline="") as fh:
            source_count=sum(1 for _ in csv.DictReader(fh))
        status="PASS" if db_count==source_count else "FAIL"
        print(f"{table}: SOURCE={source_count} DATABASE={db_count} STATUS={status}")
        if status=="FAIL": raise RuntimeError(f"Row-count mismatch for {table}")
    conn.commit()
    print("PASS - BULK RAW LOAD COMPLETE")
except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
