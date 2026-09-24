from pathlib import Path
import os
import psycopg2

def load_env():
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k,v=line.split("=",1)
            os.environ[k.strip()]=v.strip()

load_env()
conn=psycopg2.connect(host=os.environ["POSTGRES_HOST"],port=int(os.environ["POSTGRES_PORT"]),dbname=os.environ["POSTGRES_DB"],user=os.environ["POSTGRES_USER"],password=os.environ["POSTGRES_PASSWORD"])
cur=conn.cursor()
try:
    schemas=("raw","staging","intermediate","warehouse","marts","semantic")
    for schema in schemas:
        cur.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=%s",(schema,))
        print(f"{schema.upper()}_OBJECTS={cur.fetchone()[0]}")
finally:
    cur.close()
    conn.close()
