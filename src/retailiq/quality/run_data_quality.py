from pathlib import Path
import psycopg2
import json

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
    checks=[]

    reconciliation=[
        ("orders", "intermediate.int_orders", "warehouse.fact_orders"),
        ("order_items", "intermediate.int_order_items", "warehouse.fact_order_items"),
        ("payments", "intermediate.int_order_payments", "warehouse.fact_payments"),
        ("reviews", "intermediate.int_order_reviews", "warehouse.fact_reviews"),
        ("customers", "warehouse.dim_customer", "marts.customer"),
        ("products", "warehouse.dim_product", "marts.product"),
        ("sellers", "warehouse.dim_seller", "marts.seller_fulfillment")
    ]

    for name,source,target in reconciliation:
        cur.execute(f"SELECT COUNT(*) FROM {source}")
        s=cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(*) FROM {target}")
        t=cur.fetchone()[0]
        checks.append((f"reconciliation_{name}",s==t,s,t))

    grain_queries={
        "fact_orders_grain":"SELECT COUNT(*) FROM (SELECT order_id FROM warehouse.fact_orders GROUP BY order_id HAVING COUNT(*)>1)x",
        "fact_order_items_grain":"SELECT COUNT(*) FROM (SELECT order_id,order_item_id FROM warehouse.fact_order_items GROUP BY order_id,order_item_id HAVING COUNT(*)>1)x",
        "fact_payments_grain":"SELECT COUNT(*) FROM (SELECT order_id,payment_sequential FROM warehouse.fact_payments GROUP BY order_id,payment_sequential HAVING COUNT(*)>1)x",
        "fact_reviews_grain":"SELECT COUNT(*) FROM (SELECT review_id,order_id FROM warehouse.fact_reviews GROUP BY review_id,order_id HAVING COUNT(*)>1)x",
        "customer_mart_grain":"SELECT COUNT(*) FROM (SELECT customer_sk FROM marts.customer GROUP BY customer_sk HAVING COUNT(*)>1)x",
        "product_mart_grain":"SELECT COUNT(*) FROM (SELECT product_sk FROM marts.product GROUP BY product_sk HAVING COUNT(*)>1)x",
        "seller_mart_grain":"SELECT COUNT(*) FROM (SELECT seller_sk FROM marts.seller_fulfillment GROUP BY seller_sk HAVING COUNT(*)>1)x"
    }

    for name,sql in grain_queries.items():
        cur.execute(sql)
        value=cur.fetchone()[0]
        checks.append((name,value==0,value,0))

    quality_queries={
        "invalid_review_scores":"SELECT COUNT(*) FROM warehouse.fact_reviews WHERE review_score NOT BETWEEN 1 AND 5",
        "negative_item_measures":"SELECT COUNT(*) FROM warehouse.fact_order_items WHERE item_price<0 OR freight_value<0 OR total_item_value<0",
        "negative_payment_values":"SELECT COUNT(*) FROM warehouse.fact_payments WHERE payment_value<0",
        "negative_delivery_duration":"SELECT COUNT(*) FROM warehouse.fact_orders WHERE delivery_duration_days<0",
        "sales_negative_values":"SELECT COUNT(*) FROM marts.sales_orders WHERE sales_item_value<0 OR freight_value<0 OR total_order_value<0 OR payment_value<0",
        "customer_negative_values":"SELECT COUNT(*) FROM marts.customer WHERE sales_item_value<0 OR freight_value<0 OR total_spend<0 OR payment_value<0",
        "product_negative_values":"SELECT COUNT(*) FROM marts.product WHERE sales_item_value<0 OR freight_value<0 OR total_item_value<0",
        "seller_negative_values":"SELECT COUNT(*) FROM marts.seller_fulfillment WHERE sales_item_value<0 OR freight_value<0 OR total_item_value<0",
        "bi_sales_negative_values":"SELECT COUNT(*) FROM semantic.bi_sales_overview WHERE sales_item_value<0 OR freight_value<0 OR total_order_value<0",
        "bi_customer_negative_values":"SELECT COUNT(*) FROM semantic.bi_customer_overview WHERE sales_item_value<0 OR freight_value<0 OR total_spend<0",
        "bi_product_negative_values":"SELECT COUNT(*) FROM semantic.bi_product_overview WHERE sales_item_value<0 OR freight_value<0 OR total_item_value<0",
        "bi_seller_negative_values":"SELECT COUNT(*) FROM semantic.bi_seller_fulfillment WHERE sales_item_value<0 OR freight_value<0 OR total_item_value<0"
    }

    for name,sql in quality_queries.items():
        cur.execute(sql)
        value=cur.fetchone()[0]
        checks.append((name,value==0,value,0))

    required_queries={
        "fact_orders_required_keys":"SELECT COUNT(*) FROM warehouse.fact_orders WHERE order_id IS NULL OR customer_sk IS NULL OR purchase_date_sk IS NULL",
        "fact_items_required_keys":"SELECT COUNT(*) FROM warehouse.fact_order_items WHERE order_id IS NULL OR order_item_id IS NULL OR customer_sk IS NULL OR product_sk IS NULL OR seller_sk IS NULL OR order_date_sk IS NULL",
        "fact_payments_required_keys":"SELECT COUNT(*) FROM warehouse.fact_payments WHERE order_id IS NULL OR payment_sequential IS NULL OR customer_sk IS NULL",
        "fact_reviews_required_keys":"SELECT COUNT(*) FROM warehouse.fact_reviews WHERE review_id IS NULL OR order_id IS NULL OR customer_sk IS NULL",
        "sales_required_keys":"SELECT COUNT(*) FROM marts.sales_orders WHERE order_id IS NULL OR customer_sk IS NULL",
        "customer_required_keys":"SELECT COUNT(*) FROM marts.customer WHERE customer_id IS NULL OR customer_sk IS NULL",
        "product_required_keys":"SELECT COUNT(*) FROM marts.product WHERE product_id IS NULL OR product_sk IS NULL",
        "seller_required_keys":"SELECT COUNT(*) FROM marts.seller_fulfillment WHERE seller_id IS NULL OR seller_sk IS NULL"
    }

    for name,sql in required_queries.items():
        cur.execute(sql)
        value=cur.fetchone()[0]
        checks.append((name,value==0,value,0))

    total=len(checks)
    passed=sum(1 for x in checks if x[1])
    failed=total-passed

    print(f"DATA_QUALITY_CHECK_COUNT={total}")
    print(f"DATA_QUALITY_PASS_COUNT={passed}")
    print(f"DATA_QUALITY_FAIL_COUNT={failed}")

    for name,status,actual,expected in checks:
        print(f"{name}: ACTUAL={actual} EXPECTED={expected} STATUS={'PASS' if status else 'FAIL'}")

    result={
        "check_count":total,
        "pass_count":passed,
        "fail_count":failed,
        "status":"PASS" if failed==0 else "FAIL"
    }
    out=Path("data/output/data_quality")
    out.mkdir(parents=True,exist_ok=True)
    (out/"data_quality_execution.json").write_text(json.dumps(result,indent=2),encoding="utf-8")

    if failed==0:
        conn.commit()
        print("PASS - DATA QUALITY ENGINEERING EXECUTION VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("Data quality execution failed")
finally:
    cur.close()
    conn.close()
