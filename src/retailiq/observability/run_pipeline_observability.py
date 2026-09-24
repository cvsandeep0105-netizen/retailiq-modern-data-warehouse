from pathlib import Path
import json
import time
import traceback
from datetime import datetime, timezone
import psycopg2

def read_env():
    d={}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k,v=line.split("=",1); d[k.strip()]=v.strip()
    return d

def utc_now():
    return datetime.now(timezone.utc).isoformat()

cfg=read_env()
conn=psycopg2.connect(host=cfg["POSTGRES_HOST"],port=int(cfg["POSTGRES_PORT"]),dbname=cfg["POSTGRES_DB"],user=cfg["POSTGRES_USER"],password=cfg["POSTGRES_PASSWORD"])
cur=conn.cursor()

steps=[
    ("raw","SELECT COUNT(*) FROM raw.olist_orders"),
    ("staging","SELECT COUNT(*) FROM staging.stg_orders"),
    ("intermediate","SELECT COUNT(*) FROM intermediate.int_orders"),
    ("warehouse","SELECT COUNT(*) FROM warehouse.fact_orders"),
    ("marts","SELECT COUNT(*) FROM marts.sales_orders"),
    ("semantic","SELECT COUNT(*) FROM semantic.sales_analysis")
]

run_id=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
started=utc_now()
results=[]
pipeline_status="PASS"

try:
    for name,sql in steps:
        step_started=time.perf_counter()
        step_start_utc=utc_now()
        try:
            cur.execute(sql)
            count=cur.fetchone()[0]
            elapsed_ms=round((time.perf_counter()-step_started)*1000,2)
            results.append({"step":name,"status":"PASS","row_count":count,"started_at":step_start_utc,"duration_ms":elapsed_ms})
        except Exception as exc:
            elapsed_ms=round((time.perf_counter()-step_started)*1000,2)
            results.append({"step":name,"status":"FAIL","error":str(exc),"started_at":step_start_utc,"duration_ms":elapsed_ms})
            pipeline_status="FAIL"
            break

    finished=utc_now()
    total_ms=round((datetime.fromisoformat(finished)-datetime.fromisoformat(started)).total_seconds()*1000,2)
    output={
        "run_id":run_id,
        "pipeline":"retailiq_local_warehouse_validation",
        "status":pipeline_status,
        "started_at":started,
        "finished_at":finished,
        "duration_ms":total_ms,
        "step_count":len(steps),
        "completed_step_count":len(results),
        "successful_step_count":sum(1 for r in results if r["status"]=="PASS"),
        "failed_step_count":sum(1 for r in results if r["status"]=="FAIL"),
        "retry_policy":"No automatic retry for deterministic validation checks; failures are captured and require targeted remediation.",
        "steps":results
    }
    out=Path("data/output/orchestration_observability")
    out.mkdir(parents=True,exist_ok=True)
    (out/"pipeline_execution_manifest.json").write_text(json.dumps(output,indent=2),encoding="utf-8")

    print(f"RUN_ID={run_id}")
    print(f"PIPELINE_STATUS={pipeline_status}")
    print(f"STEP_COUNT={len(steps)}")
    print(f"COMPLETED_STEP_COUNT={len(results)}")
    successful=sum(1 for r in results if r["status"]=="PASS"); print(f"SUCCESSFUL_STEP_COUNT={successful}")
    failed=sum(1 for r in results if r["status"]=="FAIL"); print(f"FAILED_STEP_COUNT={failed}")
    print(f"TOTAL_DURATION_MS={total_ms}")
    artifact_status="PASS" if (out/"pipeline_execution_manifest.json").exists() else "FAIL"; print(f"OBSERVABILITY_ARTIFACT_STATUS={artifact_status}")

    if pipeline_status!="PASS":
        raise RuntimeError("Pipeline validation failed")
    print("PASS - ORCHESTRATION RELIABILITY AND OBSERVABILITY VALIDATED")
finally:
    cur.close()
    conn.close()

