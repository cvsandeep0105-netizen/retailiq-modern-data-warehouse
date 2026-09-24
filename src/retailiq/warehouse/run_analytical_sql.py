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

queries={
    "monthly_sales":"""
        SELECT DATE_TRUNC('month',order_purchase_timestamp)::date AS month,
               COUNT(*) AS order_count,
               SUM(order_item_count) AS item_count,
               ROUND(SUM(total_order_value),2) AS total_value
        FROM semantic.sales_analysis
        GROUP BY 1 ORDER BY 1
    """,
    "category_performance":"""
        SELECT COALESCE(product_category_name_english,product_category_name,'unknown') AS category,
               COUNT(DISTINCT product_id) AS product_count,
               SUM(order_item_count) AS item_count,
               ROUND(SUM(sales_item_value),2) AS sales_value
        FROM semantic.product_analysis
        GROUP BY 1 ORDER BY sales_value DESC
    """,
    "customer_segments":"""
        SELECT
            CASE
                WHEN order_count=0 THEN 'no_orders'
                WHEN order_count=1 THEN 'one_order'
                WHEN order_count BETWEEN 2 AND 3 THEN 'repeat_2_3'
                ELSE 'repeat_4_plus'
            END AS customer_segment,
            COUNT(*) AS customer_count,
            ROUND(AVG(total_spend),2) AS average_spend
        FROM semantic.customer_analysis
        GROUP BY 1 ORDER BY 1
    """,
    "seller_fulfillment":"""
        SELECT seller_id,seller_state,order_count,delivered_order_count,
               on_time_order_count,late_order_count,
               average_delivery_duration_days,average_review_score,
               RANK() OVER (ORDER BY sales_item_value DESC) AS sales_rank
        FROM semantic.seller_fulfillment_analysis
        ORDER BY sales_rank
        LIMIT 20
    """,
    "delivery_analysis":"""
        SELECT order_status,
               COUNT(*) AS order_count,
               ROUND(AVG(delivery_duration_days),2) AS avg_delivery_days,
               ROUND(AVG(estimated_delivery_difference_days),2) AS avg_estimated_difference
        FROM semantic.sales_analysis
        GROUP BY order_status
        ORDER BY order_count DESC
    """,
    "payment_analysis":"""
        SELECT payment_count,
               COUNT(*) AS order_count,
               ROUND(AVG(payment_value),2) AS average_payment_value
        FROM semantic.sales_analysis
        GROUP BY payment_count
        ORDER BY payment_count
    """,
    "monthly_sales_window":"""
        SELECT month,monthly_value,
               ROUND(SUM(monthly_value) OVER (ORDER BY month),2) AS cumulative_value,
               ROUND(monthly_value-LAG(monthly_value) OVER (ORDER BY month),2) AS month_change
        FROM (
            SELECT DATE_TRUNC('month',order_purchase_timestamp)::date AS month,
                   SUM(total_order_value)::numeric AS monthly_value
            FROM semantic.sales_analysis
            GROUP BY 1
        ) x
        ORDER BY month
    """,
    "review_analysis":"""
        SELECT average_review_score,
               COUNT(*) AS customer_count,
               ROUND(AVG(total_spend),2) AS average_customer_spend
        FROM semantic.customer_analysis
        WHERE average_review_score IS NOT NULL
        GROUP BY average_review_score
        ORDER BY average_review_score DESC
    """
}

try:
    output=Path("data/output/analytical_sql")
    output.mkdir(parents=True,exist_ok=True)
    passed=0

    for name,sql in queries.items():
        cur.execute(sql)
        rows=cur.fetchall()
        columns=[d[0] for d in cur.description]
        file=output/f"{name}.csv"
        lines=[",".join(columns)]
        for row in rows:
            values=[]
            for value in row:
                if value is None: values.append("")
                else: values.append('"' + str(value).replace('"','""') + '"' )
            lines.append(",".join(values))
        file.write_text("\\n".join(lines)+"\\n",encoding="utf-8")
        status="PASS" if len(rows)>0 else "FAIL"
        print(f"{name}: ROWS={len(rows)} STATUS={status}")
        if status=="PASS": passed+=1

    print(f"ANALYTICAL_QUERY_COUNT={len(queries)}")
    print(f"ANALYTICAL_QUERY_PASS_COUNT={passed}")
    print(f"ANALYTICAL_SQL_STATUS={'PASS' if passed==len(queries) else 'FAIL'}")

    if passed==len(queries):
        conn.commit()
        print("PASS - ANALYTICAL SQL AND BUSINESS ANALYSIS VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("Analytical SQL validation failed")
finally:
    cur.close()
    conn.close()
