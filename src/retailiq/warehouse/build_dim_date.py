from pathlib import Path
import psycopg2

def load_env():
    values={}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        line=line.strip()
        if line and not line.startswith("#") and "=" in line:
            k,v=line.split("=",1)
            values[k.strip()]=v.strip()
    return values

cfg=load_env()
conn=psycopg2.connect(host=cfg["POSTGRES_HOST"],port=int(cfg["POSTGRES_PORT"]),dbname=cfg["POSTGRES_DB"],user=cfg["POSTGRES_USER"],password=cfg["POSTGRES_PASSWORD"])
cur=conn.cursor()

try:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS warehouse.dim_date (
        date_sk INTEGER PRIMARY KEY,
        calendar_date DATE NOT NULL UNIQUE,
        calendar_year INTEGER NOT NULL,
        calendar_quarter INTEGER NOT NULL,
        calendar_month INTEGER NOT NULL,
        month_name TEXT NOT NULL,
        calendar_week INTEGER NOT NULL,
        day_of_month INTEGER NOT NULL,
        day_of_week INTEGER NOT NULL,
        day_name TEXT NOT NULL,
        is_weekend BOOLEAN NOT NULL
    )
    """)

    cur.execute("TRUNCATE TABLE warehouse.dim_date")

    cur.execute("""
    INSERT INTO warehouse.dim_date
    SELECT
        TO_CHAR(d,'YYYYMMDD')::INTEGER AS date_sk,
        d::DATE AS calendar_date,
        EXTRACT(YEAR FROM d)::INTEGER,
        EXTRACT(QUARTER FROM d)::INTEGER,
        EXTRACT(MONTH FROM d)::INTEGER,
        TO_CHAR(d,'FMMonth'),
        EXTRACT(WEEK FROM d)::INTEGER,
        EXTRACT(DAY FROM d)::INTEGER,
        EXTRACT(ISODOW FROM d)::INTEGER,
        TO_CHAR(d,'FMDay'),
        EXTRACT(ISODOW FROM d)::INTEGER IN (6,7)
    FROM generate_series(
        DATE '2016-01-01',
        DATE '2018-12-31',
        INTERVAL '1 day'
    ) d
    """)

    cur.execute("SELECT COUNT(*) FROM warehouse.dim_date")
    date_count=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM (
        SELECT calendar_date,
               calendar_date - (ROW_NUMBER() OVER (ORDER BY calendar_date))::INTEGER AS grp
        FROM warehouse.dim_date
    ) x
    GROUP BY grp
    HAVING COUNT(*) > 0
    """)
    continuity_groups=cur.rowcount

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.dim_date
    WHERE date_sk IS NULL
       OR calendar_date IS NULL
       OR calendar_year IS NULL
       OR calendar_month IS NULL
    """)
    invalid_required=cur.fetchone()[0]

    cur.execute("SELECT MIN(calendar_date), MAX(calendar_date) FROM warehouse.dim_date")
    min_date,max_date=cur.fetchone()

    count_status="PASS" if date_count==1096 else "FAIL"
    required_status="PASS" if invalid_required==0 else "FAIL"
    range_status="PASS" if str(min_date)=="2016-01-01" and str(max_date)=="2018-12-31" else "FAIL"

    print(f"DIM_DATE_COUNT={date_count}")
    print(f"EXPECTED_DATE_COUNT=1096")
    print(f"DATE_COUNT_STATUS={count_status}")
    print(f"DATE_RANGE={min_date} TO {max_date}")
    print(f"DATE_RANGE_STATUS={range_status}")
    print(f"INVALID_REQUIRED_ATTRIBUTES={invalid_required}")
    print(f"REQUIRED_ATTRIBUTE_STATUS={required_status}")

    if count_status=="PASS" and range_status=="PASS" and required_status=="PASS":
        conn.commit()
        print("PASS - DIM_DATE CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("dim_date validation failed")

except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
