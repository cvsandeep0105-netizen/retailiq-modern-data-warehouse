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
    cur.execute("""CREATE TABLE IF NOT EXISTS warehouse.fact_reviews (review_sk BIGSERIAL PRIMARY KEY, review_id TEXT NOT NULL, order_id TEXT NOT NULL, customer_sk BIGINT NOT NULL, review_score INTEGER NOT NULL, review_comment_title TEXT NULL, review_comment_message TEXT NULL, review_creation_timestamp TIMESTAMP NULL, review_answer_timestamp TIMESTAMP NULL, review_creation_date_sk INTEGER NULL, record_source TEXT NOT NULL DEFAULT 'olist', created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, CONSTRAINT uq_fact_review UNIQUE(review_id,order_id), CONSTRAINT fk_review_customer FOREIGN KEY(customer_sk) REFERENCES warehouse.dim_customer(customer_sk), CONSTRAINT fk_review_date FOREIGN KEY(review_creation_date_sk) REFERENCES warehouse.dim_date(date_sk), CONSTRAINT chk_review_score CHECK(review_score BETWEEN 1 AND 5))""")
    cur.execute("TRUNCATE TABLE warehouse.fact_reviews RESTART IDENTITY")
    cur.execute("""INSERT INTO warehouse.fact_reviews (review_id,order_id,customer_sk,review_score,review_comment_title,review_comment_message,review_creation_timestamp,review_answer_timestamp,review_creation_date_sk) SELECT r.review_id,r.order_id,dc.customer_sk,r.review_score,r.review_comment_title,r.review_comment_message,r.review_creation_date,r.review_answer_timestamp,TO_CHAR(r.review_creation_date,'YYYYMMDD')::INTEGER FROM intermediate.int_order_reviews r JOIN intermediate.int_orders o ON r.order_id=o.order_id JOIN warehouse.dim_customer dc ON o.customer_id=dc.customer_id""")
    cur.execute("SELECT COUNT(*) FROM intermediate.int_order_reviews")
    source_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM warehouse.fact_reviews")
    fact_count=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT review_id,order_id FROM warehouse.fact_reviews GROUP BY review_id,order_id HAVING COUNT(*)>1) d""")
    duplicate_grain=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_reviews f LEFT JOIN warehouse.dim_customer dc ON f.customer_sk=dc.customer_sk WHERE dc.customer_sk IS NULL""")
    orphan_customer_keys=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_reviews WHERE review_score < 1 OR review_score > 5""")
    invalid_scores=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_reviews f LEFT JOIN warehouse.dim_date d ON f.review_creation_date_sk=d.date_sk WHERE f.review_creation_date_sk IS NOT NULL AND d.date_sk IS NULL""")
    orphan_date_keys=cur.fetchone()[0]
    print(f"SOURCE_REVIEW_COUNT={source_count}")
    print(f"FACT_REVIEW_COUNT={fact_count}")
    print(f"ROW_RECONCILIATION_STATUS={'PASS' if source_count==fact_count else 'FAIL'}")
    print(f"DUPLICATE_REVIEW_GRAIN={duplicate_grain}")
    print(f"REVIEW_GRAIN_STATUS={'PASS' if duplicate_grain==0 else 'FAIL'}")
    print(f"ORPHAN_CUSTOMER_KEYS={orphan_customer_keys}")
    print(f"CUSTOMER_FOREIGN_KEY_STATUS={'PASS' if orphan_customer_keys==0 else 'FAIL'}")
    print(f"INVALID_REVIEW_SCORES={invalid_scores}")
    print(f"REVIEW_SCORE_STATUS={'PASS' if invalid_scores==0 else 'FAIL'}")
    print(f"ORPHAN_REVIEW_DATE_KEYS={orphan_date_keys}")
    print(f"REVIEW_DATE_STATUS={'PASS' if orphan_date_keys==0 else 'FAIL'}")
    if source_count==fact_count and duplicate_grain==0 and orphan_customer_keys==0 and invalid_scores==0 and orphan_date_keys==0:
        conn.commit()
        print("PASS - FACT_REVIEWS CREATED AND VALIDATED")
    else:
        conn.rollback()
        raise RuntimeError("fact_reviews validation failed")
except Exception:
    conn.rollback()
    raise
finally:
    cur.close()
    conn.close()
