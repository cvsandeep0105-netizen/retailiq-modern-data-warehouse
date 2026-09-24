from pathlib import Path
import json
import time
import statistics
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
    "SELECT COUNT(*),SUM(total_order_value),AVG(delivery_duration_days) FROM marts.sales_orders",
    "SELECT customer_state,COUNT(*),SUM(total_spend) FROM marts.customer GROUP BY customer_state",
    "SELECT product_category_name_english,COUNT(*),SUM(total_item_value) FROM marts.product GROUP BY product_category_name_english",
    "SELECT seller_state,COUNT(*),SUM(total_item_value),AVG(average_delivery_duration_days) FROM marts.seller_fulfillment GROUP BY seller_state",
    "SELECT order_status,COUNT(*),AVG(delivery_duration_days) FROM warehouse.fact_orders GROUP BY order_status"
]
repetitions=3
runs=[]

try:
    for iteration in range(1,repetitions+1):
        started=time.perf_counter()
        successful=0
        failed=0
        query_times=[]
        for sql in queries:
            qstart=time.perf_counter()
            try:
                cur.execute(sql)
                cur.fetchall()
                successful+=1
            except Exception:
                failed+=1
                conn.rollback()
            query_times.append(round((time.perf_counter()-qstart)*1000,3))
        total_ms=round((time.perf_counter()-started)*1000,3)
        runs.append({"iteration":iteration,"successful_queries":successful,"failed_queries":failed,"total_time_ms":total_ms,"query_times_ms":query_times})

    totals=[r["total_time_ms"] for r in runs]
    successful=sum(r["successful_queries"] for r in runs)
    failed=sum(r["failed_queries"] for r in runs)
    total_time=sum(totals)
    throughput=round(successful/(total_time/1000),3) if total_time else 0
    evidence={"workload":"RetailIQ controlled analytical workload","query_count_per_iteration":len(queries),"repetitions":repetitions,"total_query_executions":successful+failed,"successful_query_executions":successful,"failed_query_executions":failed,"total_elapsed_ms":round(total_time,3),"average_iteration_ms":round(statistics.mean(totals),3),"min_iteration_ms":min(totals),"max_iteration_ms":max(totals),"queries_per_second":throughput,"runs":runs}
    out=Path("data/output/scalability")
    out.mkdir(parents=True,exist_ok=True)
    (out/"scalability_workload_test.json").write_text(json.dumps(evidence,indent=2),encoding="utf-8")
    print(f"ITERATION_COUNT={repetitions}")
    print(f"QUERY_COUNT_PER_ITERATION={len(queries)}")
    print(f"TOTAL_QUERY_EXECUTIONS={successful+failed}")
    print(f"SUCCESSFUL_QUERY_EXECUTIONS={successful}")
    print(f"FAILED_QUERY_EXECUTIONS={failed}")
    print(f"AVERAGE_ITERATION_MS={round(statistics.mean(totals),3)}")
    print(f"MIN_ITERATION_MS={min(totals)}")
    print(f"MAX_ITERATION_MS={max(totals)}")
    print(f"THROUGHPUT_QUERIES_PER_SECOND={throughput}")
    artifact_status="PASS" if (out/"scalability_workload_test.json").exists() else "FAIL"; print(f"SCALABILITY_ARTIFACT_STATUS={artifact_status}")
    if failed==0:
        print("PASS - SCALABILITY WORKLOAD TEST VALIDATED")
    else:
        raise RuntimeError("Scalability workload contained failed queries")
finally:
    cur.close()
    conn.close()

