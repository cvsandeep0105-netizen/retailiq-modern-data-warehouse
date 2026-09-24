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
    CREATE TABLE IF NOT EXISTS warehouse.fact_payments (
        payment_sk BIGSERIAL PRIMARY KEY,
        order_id TEXT NOT NULL,
        payment_sequential INTEGER NOT NULL,
        customer_sk BIGINT NOT NULL,
        payment_type TEXT NOT NULL,
        payment_installments INTEGER NOT NULL,
        payment_value NUMERIC(18,2) NOT NULL,
        payment_date_sk INTEGER NOT NULL,
        record_source TEXT NOT NULL DEFAULT 'olist',
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT uq_fact_payment UNIQUE(order_id,payment_sequential),
        CONSTRAINT fk_payment_customer FOREIGN KEY(customer_sk) REFERENCES warehouse.dim_customer(customer_sk),
        CONSTRAINT fk_payment_date FOREIGN KEY(payment_date_sk) REFERENCES warehouse.dim_date(date_sk)
    )
    """)

    cur.execute("TRUNCATE TABLE warehouse.fact_payments RESTART IDENTITY")

    cur.execute("""
    INSERT INTO warehouse.fact_payments (
        order_id, payment_sequential, customer_sk, payment_type,
        payment_installments, payment_value, payment_date_sk
    )
    SELECT
        p.order_id,
        p.payment_sequential,
        dc.customer_sk,
        p.payment_type,
        p.payment_installments,
        ROUND(p.payment_value::NUMERIC,2),
        fo.purchase_date_sk
    FROM intermediate.int_order_payments p
    JOIN intermediate.int_orders o
      ON p.order_id=o.order_id
    JOIN warehouse.dim_customer dc
      ON o.customer_id=dc.customer_id
    JOIN warehouse.fact_orders fo
      ON p.order_id=fo.order_id
    """)

    cur.execute("SELECT COUNT(*) FROM intermediate.int_order_payments")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM warehouse.fact_payments")
    fact_count=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM (
        SELECT order_id,payment_sequential
        FROM warehouse.fact_payments
        GROUP BY order_id,payment_sequential
        HAVING COUNT(*)>1
    ) d
    """)
    duplicate_grain=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.fact_payments fp
    LEFT JOIN warehouse.dim_customer dc ON fp.customer_sk=dc.customer_sk
    LEFT JOIN warehouse.dim_date dd ON fp.payment_date_sk=dd.date_sk
    WHERE dc.customer_sk IS NULL OR dd.date_sk IS NULL
    """)
    orphan_keys=cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM warehouse.fact_payments
    WHERE payment_value < 0
       OR payment_installments < 0
    """)
    invalid_measures=cur.fetchone()[0]

    row_status="PASS" if source_count==fact_count else "FAIL"
    grain_status="PASS" if duplicate_grain==0 else "FAIL"
    fk_status="PASS" if orphan_keys==0 else "FAIL"
    measure_status="PASS" if invalid_measures==0 else "FAIL"

    print(f"SOURCE_PAYMENT_COUNT={source_count}")
    print(f"FACT_PAYMENT_COUNT={fact_count}")
    print(f"ROW_RECONCILIATION_STATUS={row_status}")
    print(f"DUPLICATE_PAYMENT_GRAIN={duplicate_grain}")
    print(f"FACT_GRAIN_STATUS={grain_status}")
    print(f"ORPHAN_CUSTOMER_OR_DATE_KEYS={orphan_keys}")
    print(f"FOREIGN_KEY_STATUS={fk_status}")
    print(f"INVALID_PAYMENT_MEASURES={invalid_measures}")
    print(f"PAYMENT_MEASURE_STATUS={measure_status}")

    if row_status=="PASS" and grain_status=="PASS" and fk_status=="PASS" and measure_status=="PASS":
        conn.commit()
        print("PASS - FACT_PAYMENTS CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("fact_payments validation failed")

except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
