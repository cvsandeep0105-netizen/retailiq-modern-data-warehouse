from pathlib import Path
import subprocess
import json
import os

root=Path(".")
env=os.environ.copy()
env["PYTHONPATH"]=str(root/"src")
checks=[
    ("python_compile",["-m","compileall","-q","src"]),
    ("pytest_regression",["-m","pytest","-q","tests/integration/test_platform_regression.py"])
]
results=[]

for name,args in checks:
    p=subprocess.run(["python"]+args,capture_output=True,text=True,env=env)
    results.append({
        "check":name,
        "status":"PASS" if p.returncode==0 else "FAIL",
        "returncode":p.returncode,
        "stdout":p.stdout[-4000:],
        "stderr":p.stderr[-4000:]
    })

failed=[r for r in results if r["status"]=="FAIL"]
ci_status="PASS" if not failed else "FAIL"

workflow={
    "workflow":"RetailIQ local CI validation",
    "checks":results,
    "check_count":len(results),
    "failed_check_count":len(failed),
    "status":ci_status,
    "ci_scope":"Local reproducible validation; remote CI execution deferred until repository publication."
}

out=Path("data/output/ci_cd")
out.mkdir(parents=True,exist_ok=True)
(out/"ci_validation_evidence.json").write_text(json.dumps(workflow,indent=2),encoding="utf-8")

print(f"CI_CHECK_COUNT={len(results)}")
print(f"CI_FAILED_CHECK_COUNT={len(failed)}")
print(f"CI_STATUS={ci_status}")
artifact_status="PASS" if (out/"ci_validation_evidence.json").exists() else "FAIL"
print(f"CI_ARTIFACT_STATUS={artifact_status}")

if failed:
    for r in failed:
        print("FAILED_CHECK="+r["check"])
    raise SystemExit(1)

print("PASS - CI/CD VALIDATION WORKFLOW EXECUTED")
