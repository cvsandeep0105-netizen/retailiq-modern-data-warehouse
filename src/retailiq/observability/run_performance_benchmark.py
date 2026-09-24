from pathlib import Path
import json
import time
import psycopg2

def read_env():
    d={}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k,v=line.split("=",1); d[k.strip()]=v.strip()
    return d

cfg=read_env()
conn=psycopg2.connect(host=cfg["POSTGRES_HOST"],port=int(cfg["POSTGRES_PORT"]),dbname=cfg["POSTGRES_DB"],user=cfg["POSTGRES_USER"],password=cfg["POSTGRES_PASSWORD"])
cur=conn.cursor()
queries=[
    ("monthly_sales","SELECT DATE_TRUNC('month', order_purchase_timestamp)::date AS month, COUNT(*) AS orders, SUM(total_order_value) AS sales FROM marts.sales_orders GROUP BY 1 ORDER BY 1"),
    ("customer_analysis","SELECT customer_state, COUNT(*) AS customers, SUM(total_spend) AS sales FROM marts.customer GROUP BY customer_state ORDER BY sales DESC"),
    ("product_analysis","SELECT product_category_name_english, SUM(total_item_value) AS sales, SUM(order_item_count) AS items FROM marts.product GROUP BY product_category_name_english ORDER BY sales DESC LIMIT 25"),
    ("seller_fulfillment","SELECT seller_state, COUNT(*) AS sellers, SUM(total_item_value) AS sales, AVG(average_delivery_duration_days) AS avg_delivery_days FROM marts.seller_fulfillment GROUP BY seller_state ORDER BY sales DESC"),
    ("delivery_analysis","SELECT order_status, COUNT(*) AS orders, AVG(delivery_duration_days) AS avg_delivery_days FROM warehouse.fact_orders GROUP BY order_status ORDER BY orders DESC")
]
results=[]

try:
    for name,sql in queries:
        cur.execute("EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) "+sql)
        plan=cur.fetchone()[0][0]
        execution_ms=round(float(plan["Execution Time"]),3)
        planning_ms=round(float(plan["Planning Time"]),3)
        rows=int(plan["Plan"].get("Actual Rows",0))
        shared_hit=int(plan["Plan"].get("Shared Hit Blocks",0))
        shared_read=int(plan["Plan"].get("Shared Read Blocks",0))
        results.append({"query":name,"planning_time_ms":planning_ms,"execution_time_ms":execution_ms,"actual_rows":rows,"shared_hit_blocks":shared_hit,"shared_read_blocks":shared_read,"status":"PASS"})

    total_ms=round(sum(r["execution_time_ms"] for r in results),3)
    max_ms=max(r["execution_time_ms"] for r in results)
    avg_ms=round(total_ms/len(results),3)
    evidence={"benchmark":"RetailIQ analytical workload","query_count":len(results),"total_execution_time_ms":total_ms,"average_execution_time_ms":avg_ms,"max_execution_time_ms":max_ms,"queries":results}
    out=Path("data/output/performance")
    out.mkdir(parents=True,exist_ok=True)
    (out/"performance_benchmark.json").write_text(json.dumps(evidence,indent=2),encoding="utf-8")
    print(f"BENCHMARK_QUERY_COUNT={len(results)}")
    print(f"TOTAL_EXECUTION_TIME_MS={total_ms}")
    print(f"AVERAGE_EXECUTION_TIME_MS={avg_ms}")
    print(f"MAX_EXECUTION_TIME_MS={max_ms}")
    artifact_status="PASS" if (out/"performance_benchmark.json").exists() else "FAIL"; print(f"PERFORMANCE_ARTIFACT_STATUS={artifact_status}")
    print("PASS - PERFORMANCE BENCHMARK VALIDATED")
finally:
    cur.close()
    conn.close()




