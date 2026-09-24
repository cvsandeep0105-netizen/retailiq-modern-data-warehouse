from pathlib import Path
import json
import subprocess
import shutil
import platform
import os

def run(cmd):
    try:
        p=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
        return {"command":" ".join(cmd),"returncode":p.returncode,"stdout":p.stdout.strip(),"stderr":p.stderr.strip()}
    except Exception as e:
        return {"command":" ".join(cmd),"returncode":-1,"stdout":"","stderr":str(e)}

checks=[]
checks.append({"component":"platform","status":"PASS","detail":platform.platform()})
checks.append({"component":"python","status":"PASS","detail":platform.python_version()})
checks.append({"component":"docker","status":"PASS" if shutil.which("docker") else "FAIL","detail":run(["docker","--version"])})
checks.append({"component":"docker_compose","status":"PASS" if shutil.which("docker") else "FAIL","detail":run(["docker","compose","version"])})

docker_ps=run(["docker","ps","--filter","name=retailiq-postgres","--format","{{.Names}}|{{.Status}}|{{.Ports}}"])
checks.append({"component":"retailiq_postgres_container","status":"PASS" if docker_ps["returncode"]==0 and "retailiq-postgres" in docker_ps["stdout"] else "FAIL","detail":docker_ps})

volume=run(["docker","volume","inspect","retailiq_postgres_data","--format","{{.Name}}|{{.Mountpoint}}"])
checks.append({"component":"docker_storage_visibility","status":"PASS" if volume["returncode"]==0 else "FAIL","detail":volume})

gitignore=Path(".gitignore").read_text(encoding="utf-8") if Path(".gitignore").exists() else ""
data_policy=all(x in gitignore for x in ["data/processed/","data/intermediate/","data/output/"])
checks.append({"component":"generated_data_exclusion","status":"PASS" if data_policy else "FAIL","detail":"Generated processed/intermediate/output data excluded from Git"})

env_policy=all(x in gitignore for x in [".env",".env.*"])
checks.append({"component":"secret_exclusion","status":"PASS" if env_policy else "FAIL","detail":"Environment secret files excluded from Git"})

compose=Path("docker-compose.yml").read_text(encoding="utf-8") if Path("docker-compose.yml").exists() else ""
volume_policy="retailiq_postgres_data" in compose
checks.append({"component":"persistent_database_volume","status":"PASS" if volume_policy else "FAIL","detail":"Named PostgreSQL volume configured"})

cost_controls=[
    "Local PostgreSQL runtime isolates project infrastructure from the existing host PostgreSQL instance.",
    "Generated intermediate/output data is excluded from Git to prevent repository growth.",
    "Secrets are excluded from Git through .env rules.",
    "Named database volume avoids uncontrolled container-layer persistence.",
    "No cloud production cost is claimed because this implementation is local."
]

failed=[x for x in checks if x["status"]=="FAIL"]
evidence={"cost_engineering_scope":"Local development/runtime cost controls","cloud_cost_claim":False,"checks":checks,"cost_controls":cost_controls,"failed_check_count":len(failed)}
out=Path("data/output/cost")
out.mkdir(parents=True,exist_ok=True)
(out/"cost_engineering_evidence.json").write_text(json.dumps(evidence,indent=2),encoding="utf-8")

print(f"COST_CHECK_COUNT={len(checks)}")
print(f"COST_CHECK_FAILURE_COUNT={len(failed)}")
runtime_status="PASS" if not failed else "FAIL"; print(f"LOCAL_RUNTIME_COST_STATUS={runtime_status}")
print("CLOUD_PRODUCTION_COST_CLAIM=False")
artifact_status="PASS" if (out/"cost_engineering_evidence.json").exists() else "FAIL"; print(f"COST_ARTIFACT_STATUS={artifact_status}")
if failed:
    raise RuntimeError("Cost engineering validation failed")
print("PASS - COST ENGINEERING CONTROLS VALIDATED")

