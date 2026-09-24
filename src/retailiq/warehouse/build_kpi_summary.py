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
    cur.execute("""
    CREATE SCHEMA IF NOT EXISTS semantic
    """)

    cur.execute("""
    CREATE OR REPLACE VIEW semantic.kpi_summary AS
    SELECT
        COUNT(DISTINCT so.order_id)::BIGINT AS order_count,
        COALESCE(SUM(so.order_item_count),0)::BIGINT AS order_item_count,
        COUNT(DISTINCT so.customer_sk)::BIGINT AS customer_count,
        (SELECT COUNT(*) FROM marts.product)::BIGINT AS product_count,
        (SELECT COUNT(*) FROM marts.seller_fulfillment)::BIGINT AS seller_count,
        COALESCE(SUM(so.sales_item_value),0)::NUMERIC(18,2) AS sales_item_value,
        COALESCE(SUM(so.freight_value),0)::NUMERIC(18,2) AS freight_value,
        COALESCE(SUM(so.total_order_value),0)::NUMERIC(18,2) AS gmv_boundary_value,
        COALESCE(SUM(so.payment_value),0)::NUMERIC(18,2) AS payment_value,
        CASE WHEN COUNT(DISTINCT so.order_id)>0
             THEN ROUND(SUM(so.total_order_value)/COUNT(DISTINCT so.order_id),2)
             ELSE 0 END::NUMERIC(18,2) AS average_order_value,
        CASE WHEN COUNT(DISTINCT so.customer_sk)>0
             THEN ROUND(COUNT(DISTINCT so.order_id)::NUMERIC/COUNT(DISTINCT so.customer_sk),2)
             ELSE 0 END::NUMERIC(18,2) AS orders_per_customer,
        CASE WHEN COUNT(DISTINCT so.order_id)>0
             THEN ROUND(SUM(so.order_item_count)::NUMERIC/COUNT(DISTINCT so.order_id),2)
             ELSE 0 END::NUMERIC(18,2) AS items_per_order,
        ROUND(AVG(so.delivery_duration_days),2)::NUMERIC(18,2) AS average_delivery_duration_days,
        ROUND(AVG(so.estimated_delivery_difference_days),2)::NUMERIC(18,2) AS average_estimated_delivery_difference_days,
        CASE WHEN SUM(CASE WHEN so.is_delivered THEN 1 ELSE 0 END)>0
             THEN ROUND(100.0*SUM(CASE WHEN so.is_on_time THEN 1 ELSE 0 END)/SUM(CASE WHEN so.is_delivered THEN 1 ELSE 0 END),2)
             ELSE 0 END::NUMERIC(18,2) AS on_time_delivery_rate_pct,
        CASE WHEN SUM(CASE WHEN so.is_delivered THEN 1 ELSE 0 END)>0
             THEN ROUND(100.0*SUM(CASE WHEN so.is_late THEN 1 ELSE 0 END)/SUM(CASE WHEN so.is_delivered THEN 1 ELSE 0 END),2)
             ELSE 0 END::NUMERIC(18,2) AS late_delivery_rate_pct,
        (SELECT ROUND(AVG(average_review_score),2) FROM marts.customer WHERE average_review_score IS NOT NULL)::NUMERIC(18,2) AS average_review_score,
        (SELECT COALESCE(SUM(review_count),0) FROM marts.customer)::BIGINT AS review_count,
        (SELECT COALESCE(SUM(payment_count),0) FROM marts.customer)::BIGINT AS payment_count,
        CASE WHEN COUNT(DISTINCT so.customer_sk)>0
             THEN ROUND(COUNT(DISTINCT so.order_id)::NUMERIC/COUNT(DISTINCT so.customer_sk),2)
             ELSE 0 END::NUMERIC(18,2) AS customer_purchase_frequency
    FROM marts.sales_orders so
    """)

    cur.execute("SELECT COUNT(*) FROM semantic.kpi_summary")
    row_count=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM semantic.kpi_summary WHERE order_count<0 OR order_item_count<0 OR customer_count<0 OR product_count<0 OR seller_count<0 OR sales_item_value<0 OR freight_value<0 OR payment_value<0 OR review_count<0 OR payment_count<0""")
    invalid_values=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM semantic.kpi_summary WHERE on_time_delivery_rate_pct<0 OR on_time_delivery_rate_pct>100 OR late_delivery_rate_pct<0 OR late_delivery_rate_pct>100""")
    invalid_rates=cur.fetchone()[0]

    cur.execute("SELECT * FROM semantic.kpi_summary")
    row=cur.fetchone()

    print(f"KPI_SUMMARY_ROWS={row_count}")
    print(f"KPI_INVALID_VALUES={invalid_values}")
    print(f"KPI_INVALID_RATE_VALUES={invalid_rates}")
    print(f"KPI_VIEW_STATUS={'PASS' if row_count==1 else 'FAIL'}")
    print(f"KPI_VALUE_STATUS={'PASS' if invalid_values==0 else 'FAIL'}")
    print(f"KPI_RATE_STATUS={'PASS' if invalid_rates==0 else 'FAIL'}")

    if row_count==1 and invalid_values==0 and invalid_rates==0:
        conn.commit()
        print("PASS - KPI SUMMARY LAYER CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("KPI validation failed")
finally:
    cur.close()
    conn.close()
