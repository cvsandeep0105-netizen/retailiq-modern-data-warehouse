from pathlib import Path
import json
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

checks=[
    ("raw_orders","SELECT COUNT(*) FROM raw.olist_orders",99441),
    ("staging_orders","SELECT COUNT(*) FROM staging.stg_orders",99441),
    ("intermediate_orders","SELECT COUNT(*) FROM intermediate.int_orders",99441),
    ("fact_orders","SELECT COUNT(*) FROM warehouse.fact_orders",99441),
    ("fact_order_items","SELECT COUNT(*) FROM warehouse.fact_order_items",112650),
    ("fact_payments","SELECT COUNT(*) FROM warehouse.fact_payments",103886),
    ("fact_reviews","SELECT COUNT(*) FROM warehouse.fact_reviews",99224),
    ("sales_orders_mart","SELECT COUNT(*) FROM marts.sales_orders",99441),
    ("customer_mart","SELECT COUNT(*) FROM marts.customer",99441),
    ("product_mart","SELECT COUNT(*) FROM marts.product",32951),
    ("seller_mart","SELECT COUNT(*) FROM marts.seller_fulfillment",3095),
    ("semantic_kpi","SELECT COUNT(*) FROM semantic.kpi_summary",1),
    ("semantic_sales","SELECT COUNT(*) FROM semantic.sales_analysis",99441),
    ("bi_sales","SELECT COUNT(*) FROM semantic.bi_sales_overview",99441),
    ("bi_customer","SELECT COUNT(*) FROM semantic.bi_customer_overview",99441),
    ("bi_product","SELECT COUNT(*) FROM semantic.bi_product_overview",32951),
    ("bi_seller","SELECT COUNT(*) FROM semantic.bi_seller_fulfillment",3095)
]
results=[]
for name,sql,expected in checks:
    cur.execute(sql)
    actual=cur.fetchone()[0]
    status="PASS" if actual==expected else "FAIL"
    results.append({"check":name,"expected":expected,"actual":actual,"status":status})

failed=[r for r in results if r["status"]=="FAIL"]

file_checks=[
    "data/output/lineage/lineage_catalog.json",
    "data/output/orchestration_observability/pipeline_execution_manifest.json",
    "data/output/performance/performance_benchmark.json",
    "data/output/scalability/scalability_workload_test.json",
    "data/output/cost/cost_engineering_evidence.json",
    "data/output/ci_cd/ci_validation_evidence.json",
    "data/output/data_quality/data_quality_execution.json"
]
file_results=[{"artifact":p,"status":"PASS" if Path(p).exists() else "FAIL"} for p in file_checks]
missing=[r for r in file_results if r["status"]=="FAIL"]

overall="PASS" if not failed and not missing else "FAIL"
evidence={
    "validation":"RetailIQ end-to-end platform validation",
    "status":overall,
    "database_checks":results,
    "database_check_count":len(results),
    "database_failure_count":len(failed),
    "evidence_artifacts":file_results,
    "missing_artifact_count":len(missing),
    "pipeline_path":"raw -> staging -> intermediate -> warehouse -> marts -> semantic -> BI"
}
out=Path("data/output/end_to_end")
out.mkdir(parents=True,exist_ok=True)
(out/"end_to_end_validation.json").write_text(json.dumps(evidence,indent=2),encoding="utf-8")

print(f"END_TO_END_DATABASE_CHECK_COUNT={len(results)}")
print(f"END_TO_END_DATABASE_FAILURE_COUNT={len(failed)}")
print(f"END_TO_END_ARTIFACT_CHECK_COUNT={len(file_results)}")
print(f"END_TO_END_MISSING_ARTIFACT_COUNT={len(missing)}")
print(f"END_TO_END_STATUS={overall}")
artifact_status="PASS" if (out/"end_to_end_validation.json").exists() else "FAIL"
print(f"END_TO_END_ARTIFACT_STATUS={artifact_status}")
if failed or missing:
    raise SystemExit(1)
print("PASS - END-TO-END PLATFORM VALIDATION")

cur.close()
conn.close()
