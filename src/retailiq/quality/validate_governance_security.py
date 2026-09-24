from pathlib import Path
import json
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
    cur.execute("SELECT current_user")
    current_user=cur.fetchone()[0]
    cur.execute("SELECT current_database()")
    current_db=cur.fetchone()[0]
    cur.execute("""SELECT rolname,rolsuper,rolcanlogin FROM pg_roles WHERE rolname=%s""",(current_user,))
    role=cur.fetchone()

    schemas=["raw","staging","intermediate","warehouse","marts","semantic"]
    schema_results=[]
    for schema in schemas:
        cur.execute("""SELECT COUNT(*) FROM information_schema.schemata WHERE schema_name=%s""",(schema,))
        exists=cur.fetchone()[0]==1
        schema_results.append({"schema":schema,"exists":exists})

    env_exists=Path(".env").exists()
    gitignore=Path(".gitignore").read_text(encoding="utf-8") if Path(".gitignore").exists() else ""
    env_ignored=(".env" in gitignore and ".env.*" in gitignore)
    env_example_exists=Path(".env.example").exists()

    cur.execute("""SELECT COUNT(*) FROM information_schema.role_table_grants WHERE grantee=%s AND table_schema IN ('raw','staging','intermediate','warehouse','marts','semantic')""",(current_user,))
    grant_count=cur.fetchone()[0]

    cur.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_schema IN ('raw','staging','intermediate','warehouse','marts','semantic')""")
    table_count=cur.fetchone()[0]

    role_status="PASS" if role and role[2] else "FAIL"
    schema_status="PASS" if all(x["exists"] for x in schema_results) else "FAIL"
    secret_status="PASS" if env_exists and env_ignored else "FAIL"
    grant_status="PASS" if grant_count>0 else "FAIL"

    print(f"DATABASE={current_db}")
    print(f"CURRENT_ROLE={current_user}")
    print(f"ROLE_LOGIN_STATUS={role_status}")
    print(f"SCHEMA_COUNT={len(schema_results)}")
    print(f"SCHEMA_BOUNDARY_STATUS={schema_status}")
    print(f"DATABASE_OBJECT_COUNT={table_count}")
    print(f"ACTIVE_ROLE_GRANT_COUNT={grant_count}")
    print(f"ROLE_GRANT_STATUS={grant_status}")
    print(f"ENV_FILE_PRESENT={env_exists}")
    print(f"ENV_SECRET_EXCLUSION_STATUS={secret_status}")
    print(f"ENV_EXAMPLE_PRESENT={env_example_exists}")

    evidence={
        "database":current_db,
        "role":current_user,
        "role_login_status":role_status,
        "schemas":schema_results,
        "database_object_count":table_count,
        "active_role_grant_count":grant_count,
        "env_file_present":env_exists,
        "env_secret_exclusion_status":secret_status,
        "env_example_present":env_example_exists
    }
    out=Path("data/output/governance_security")
    out.mkdir(parents=True,exist_ok=True)
    (out/"governance_security_evidence.json").write_text(json.dumps(evidence,indent=2),encoding="utf-8")

    if role_status=="PASS" and schema_status=="PASS" and secret_status=="PASS" and grant_status=="PASS":
        conn.commit()
        print("PASS - GOVERNANCE SECURITY ACCESS CONTROL VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("Governance/security validation failed")
finally:
    cur.close()
    conn.close()
