from pathlib import Path
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
try:
    for schema,table in [("marts","sales_orders"),("marts","customer"),("marts","product"),("marts","seller_fulfillment")]:
        cur.execute("""SELECT column_name,data_type FROM information_schema.columns WHERE table_schema=%s AND table_name=%s ORDER BY ordinal_position""",(schema,table))
        print(f"TABLE={schema}.{table}")
        for name,dtype in cur.fetchall():
            print(f"  {name} | {dtype}")
finally:
    cur.close()
    conn.close()
