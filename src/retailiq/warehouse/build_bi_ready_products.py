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
    views={
        "bi_sales_overview":"""
            CREATE OR REPLACE VIEW semantic.bi_sales_overview AS
            SELECT
                order_id,
                order_purchase_timestamp,
                order_status,
                order_item_count,
                sales_item_value,
                freight_value,
                total_order_value,
                payment_value,
                payment_count,
                review_count,
                average_review_score,
                delivery_duration_days,
                estimated_delivery_difference_days,
                is_delivered,
                is_on_time,
                is_late
            FROM semantic.sales_analysis
        """,
        "bi_customer_overview":"""
            CREATE OR REPLACE VIEW semantic.bi_customer_overview AS
            SELECT
                customer_id,
                customer_unique_id,
                customer_city,
                customer_state,
                order_count,
                order_item_count,
                sales_item_value,
                freight_value,
                total_spend,
                payment_value,
                payment_count,
                review_count,
                average_review_score,
                first_order_timestamp,
                last_order_timestamp,
                orders_per_customer
            FROM semantic.customer_analysis
        """,
        "bi_product_overview":"""
            CREATE OR REPLACE VIEW semantic.bi_product_overview AS
            SELECT
                product_id,
                product_category_name,
                product_category_name_english,
                product_order_count,
                order_item_count,
                seller_count,
                sales_item_value,
                freight_value,
                total_item_value,
                average_item_price,
                review_count,
                average_review_score
            FROM semantic.product_analysis
        """,
        "bi_seller_fulfillment":"""
            CREATE OR REPLACE VIEW semantic.bi_seller_fulfillment AS
            SELECT
                seller_id,
                seller_city,
                seller_state,
                order_count,
                order_item_count,
                customer_count,
                sales_item_value,
                freight_value,
                total_item_value,
                average_item_price,
                delivered_order_count,
                on_time_order_count,
                late_order_count,
                average_delivery_duration_days,
                review_count,
                average_review_score
            FROM semantic.seller_fulfillment_analysis
        """
    }

    for sql in views.values():
        cur.execute(sql)

    checks=[
        ("bi_sales_overview",99441,"order_id"),
        ("bi_customer_overview",99441,"customer_id"),
        ("bi_product_overview",32951,"product_id"),
        ("bi_seller_fulfillment",3095,"seller_id")
    ]

    passed=0
    for name,expected,key in checks:
        cur.execute(f"SELECT COUNT(*) FROM semantic.{name}")
        rows=cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(*) FROM (SELECT {key} FROM semantic.{name} GROUP BY {key} HAVING COUNT(*)>1) x")
        duplicates=cur.fetchone()[0]
        status="PASS" if rows==expected and duplicates==0 else "FAIL"
        print(f"{name}: ROWS={rows} EXPECTED={expected} DUPLICATES={duplicates} STATUS={status}")
        if status=="PASS": passed+=1

    cur.execute("""SELECT COUNT(*) FROM semantic.bi_sales_overview WHERE total_order_value<0 OR sales_item_value<0 OR freight_value<0""")
    sales_invalid=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM semantic.bi_customer_overview WHERE total_spend<0 OR sales_item_value<0 OR freight_value<0""")
    customer_invalid=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM semantic.bi_product_overview WHERE total_item_value<0 OR sales_item_value<0 OR freight_value<0""")
    product_invalid=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM semantic.bi_seller_fulfillment WHERE total_item_value<0 OR sales_item_value<0 OR freight_value<0""")
    seller_invalid=cur.fetchone()[0]

    print(f"BI_SALES_INVALID_VALUES={sales_invalid}")
    print(f"BI_CUSTOMER_INVALID_VALUES={customer_invalid}")
    print(f"BI_PRODUCT_INVALID_VALUES={product_invalid}")
    print(f"BI_SELLER_INVALID_VALUES={seller_invalid}")

    value_pass=all(x==0 for x in [sales_invalid,customer_invalid,product_invalid,seller_invalid])
    print(f"BI_VALUE_VALIDATION={'PASS' if value_pass else 'FAIL'}")
    print(f"BI_PRODUCT_COUNT={passed}")
    print(f"BI_READY_PRODUCT_STATUS={'PASS' if passed==4 and value_pass else 'FAIL'}")

    if passed==4 and value_pass:
        conn.commit()
        print("PASS - BI-READY DATA PRODUCTS CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("BI-ready validation failed")
finally:
    cur.close()
    conn.close()
