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
    CREATE TABLE IF NOT EXISTS intermediate.int_customers AS
    SELECT TRIM(customer_id) AS customer_id,
           TRIM(customer_unique_id) AS customer_unique_id,
           customer_zip_code_prefix,
           TRIM(customer_city) AS customer_city,
           UPPER(TRIM(customer_state)) AS customer_state
    FROM staging.stg_customers WITH NO DATA
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS intermediate.int_geolocation AS
    SELECT geolocation_zip_code_prefix,
           geolocation_lat, geolocation_lng,
           TRIM(geolocation_city) AS geolocation_city,
           UPPER(TRIM(geolocation_state)) AS geolocation_state
    FROM staging.stg_geolocation WITH NO DATA
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS intermediate.int_order_items AS
    SELECT TRIM(order_id) AS order_id, order_item_id,
           TRIM(product_id) AS product_id,
           TRIM(seller_id) AS seller_id,
           NULLIF(TRIM(shipping_limit_date), '')::TIMESTAMP AS shipping_limit_date,
           price, freight_value
    FROM staging.stg_order_items WITH NO DATA
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS intermediate.int_order_payments AS
    SELECT TRIM(order_id) AS order_id, payment_sequential,
           LOWER(TRIM(payment_type)) AS payment_type,
           payment_installments, payment_value
    FROM staging.stg_order_payments WITH NO DATA
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS intermediate.int_order_reviews AS
    SELECT TRIM(review_id) AS review_id,
           TRIM(order_id) AS order_id,
           review_score,
           NULLIF(TRIM(review_comment_title), '') AS review_comment_title,
           NULLIF(TRIM(review_comment_message), '') AS review_comment_message,
           NULLIF(TRIM(review_creation_date), '')::TIMESTAMP AS review_creation_date,
           NULLIF(TRIM(review_answer_timestamp), '')::TIMESTAMP AS review_answer_timestamp
    FROM staging.stg_order_reviews WITH NO DATA
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS intermediate.int_products AS
    SELECT TRIM(product_id) AS product_id,
           NULLIF(TRIM(product_category_name), '') AS product_category_name,
           product_name_lenght, product_description_lenght,
           product_photos_qty, product_weight_g,
           product_length_cm, product_height_cm, product_width_cm
    FROM staging.stg_products WITH NO DATA
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS intermediate.int_sellers AS
    SELECT TRIM(seller_id) AS seller_id,
           seller_zip_code_prefix,
           TRIM(seller_city) AS seller_city,
           UPPER(TRIM(seller_state)) AS seller_state
    FROM staging.stg_sellers WITH NO DATA
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS intermediate.int_category_translation AS
    SELECT NULLIF(TRIM(product_category_name), '') AS product_category_name,
           NULLIF(TRIM(product_category_name_english), '') AS product_category_name_english
    FROM staging.stg_category_translation WITH NO DATA
    """)

    mappings={
        "int_customers":"stg_customers",
        "int_geolocation":"stg_geolocation",
        "int_order_items":"stg_order_items",
        "int_order_payments":"stg_order_payments",
        "int_order_reviews":"stg_order_reviews",
        "int_products":"stg_products",
        "int_sellers":"stg_sellers",
        "int_category_translation":"stg_category_translation"
    }

    statements={
        "int_customers":"""INSERT INTO intermediate.int_customers SELECT TRIM(customer_id),TRIM(customer_unique_id),customer_zip_code_prefix,TRIM(customer_city),UPPER(TRIM(customer_state)) FROM staging.stg_customers""",
        "int_geolocation":"""INSERT INTO intermediate.int_geolocation SELECT geolocation_zip_code_prefix,geolocation_lat,geolocation_lng,TRIM(geolocation_city),UPPER(TRIM(geolocation_state)) FROM staging.stg_geolocation""",
        "int_order_items":"""INSERT INTO intermediate.int_order_items SELECT TRIM(order_id),order_item_id,TRIM(product_id),TRIM(seller_id),NULLIF(TRIM(shipping_limit_date),'')::TIMESTAMP,price,freight_value FROM staging.stg_order_items""",
        "int_order_payments":"""INSERT INTO intermediate.int_order_payments SELECT TRIM(order_id),payment_sequential,LOWER(TRIM(payment_type)),payment_installments,payment_value FROM staging.stg_order_payments""",
        "int_order_reviews":"""INSERT INTO intermediate.int_order_reviews SELECT TRIM(review_id),TRIM(order_id),review_score,NULLIF(TRIM(review_comment_title),''),NULLIF(TRIM(review_comment_message),''),NULLIF(TRIM(review_creation_date),'')::TIMESTAMP,NULLIF(TRIM(review_answer_timestamp),'')::TIMESTAMP FROM staging.stg_order_reviews""",
        "int_products":"""INSERT INTO intermediate.int_products SELECT TRIM(product_id),NULLIF(TRIM(product_category_name),''),product_name_lenght,product_description_lenght,product_photos_qty,product_weight_g,product_length_cm,product_height_cm,product_width_cm FROM staging.stg_products""",
        "int_sellers":"""INSERT INTO intermediate.int_sellers SELECT TRIM(seller_id),seller_zip_code_prefix,TRIM(seller_city),UPPER(TRIM(seller_state)) FROM staging.stg_sellers""",
        "int_category_translation":"""INSERT INTO intermediate.int_category_translation SELECT NULLIF(TRIM(product_category_name),''),NULLIF(TRIM(product_category_name_english),'') FROM staging.stg_category_translation"""
    }

    for table in mappings:
        cur.execute(f'TRUNCATE TABLE intermediate."{table}"')
        cur.execute(statements[table])
        cur.execute(f'SELECT COUNT(*) FROM intermediate."{table}"')
        target=cur.fetchone()[0]
        staging=mappings[table]
        cur.execute(f'SELECT COUNT(*) FROM staging."{staging}"')
        source=cur.fetchone()[0]
        status="PASS" if source==target else "FAIL"
        print(f"{table}: SOURCE={source} STANDARDIZED={target} STATUS={status}")
        if status=="FAIL":
            raise RuntimeError(f"Row-count mismatch for {table}")

    conn.commit()
    print("PASS - REMAINING INTERMEDIATE STANDARDIZATION COMPLETE")
except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
