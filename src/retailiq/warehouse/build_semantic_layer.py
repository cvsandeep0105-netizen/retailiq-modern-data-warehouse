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
        "business_kpis":"""
            CREATE OR REPLACE VIEW semantic.business_kpis AS
            SELECT
                order_count AS total_orders,
                order_item_count AS total_order_items,
                customer_count AS total_customers,
                product_count AS total_products,
                seller_count AS total_sellers,
                sales_item_value AS sales_value,
                freight_value AS freight_value,
                gmv_boundary_value AS gmv_boundary_value,
                payment_value AS total_payment_value,
                average_order_value AS aov,
                orders_per_customer,
                items_per_order,
                customer_purchase_frequency,
                average_delivery_duration_days,
                average_estimated_delivery_difference_days,
                on_time_delivery_rate_pct,
                late_delivery_rate_pct,
                average_review_score,
                review_count AS total_reviews,
                payment_count AS total_payments
            FROM semantic.kpi_summary
        """,
        "sales_analysis":"""
            CREATE OR REPLACE VIEW semantic.sales_analysis AS
            SELECT
                order_id,
                customer_sk,
                purchase_date_sk,
                order_status,
                order_purchase_timestamp,
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
            FROM marts.sales_orders
        """,
        "customer_analysis":"""
            CREATE OR REPLACE VIEW semantic.customer_analysis AS
            SELECT
                customer_sk,
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
            FROM marts.customer
        """,
        "product_analysis":"""
            CREATE OR REPLACE VIEW semantic.product_analysis AS
            SELECT
                product_sk,
                product_id,
                product_category_name,
                product_category_name_english,
                product_weight_g,
                product_length_cm,
                product_height_cm,
                product_width_cm,
                product_order_count,
                order_item_count,
                seller_count,
                sales_item_value,
                freight_value,
                total_item_value,
                average_item_price,
                review_count,
                average_review_score
            FROM marts.product
        """,
        "seller_fulfillment_analysis":"""
            CREATE OR REPLACE VIEW semantic.seller_fulfillment_analysis AS
            SELECT
                seller_sk,
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
            FROM marts.seller_fulfillment
        """
    }

    for name,sql in views.items():
        cur.execute(sql)

    cur.execute("""
    SELECT table_name
    FROM information_schema.views
    WHERE table_schema='semantic'
      AND table_name IN (
        'kpi_summary',
        'business_kpis',
        'sales_analysis',
        'customer_analysis',
        'product_analysis',
        'seller_fulfillment_analysis'
      )
    ORDER BY table_name
    """)
    found=[r[0] for r in cur.fetchall()]
    expected=["business_kpis","customer_analysis","kpi_summary","product_analysis","sales_analysis","seller_fulfillment_analysis"]

    cur.execute("SELECT COUNT(*) FROM semantic.business_kpis")
    kpi_rows=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM semantic.sales_analysis")
    sales_rows=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM semantic.customer_analysis")
    customer_rows=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM semantic.product_analysis")
    product_rows=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM semantic.seller_fulfillment_analysis")
    seller_rows=cur.fetchone()[0]

    print(f"SEMANTIC_VIEW_COUNT={len(found)}")
    print(f"SEMANTIC_VIEW_SET_STATUS={'PASS' if found==expected else 'FAIL'}")
    print(f"BUSINESS_KPIS_ROWS={kpi_rows}")
    print(f"SALES_ANALYSIS_ROWS={sales_rows}")
    print(f"CUSTOMER_ANALYSIS_ROWS={customer_rows}")
    print(f"PRODUCT_ANALYSIS_ROWS={product_rows}")
    print(f"SELLER_FULFILLMENT_ANALYSIS_ROWS={seller_rows}")

    if found==expected and kpi_rows==1 and sales_rows==99441 and customer_rows==99441 and product_rows==32951 and seller_rows==3095:
        conn.commit()
        print("PASS - SEMANTIC BUSINESS LAYER CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("semantic business layer validation failed")
finally:
    cur.close()
    conn.close()
