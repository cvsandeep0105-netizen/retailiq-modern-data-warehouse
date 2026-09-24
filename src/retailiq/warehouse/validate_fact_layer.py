from pathlib import Path
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
    checks=[
        ("fact_orders","intermediate.int_orders","order_id","order_id"),
        ("fact_order_items","intermediate.int_order_items","order_id","order_id"),
        ("fact_payments","intermediate.int_order_payments","order_id","order_id"),
        ("fact_reviews","intermediate.int_order_reviews","order_id","order_id")
    ]
    all_pass=True
    for fact,source,fk,source_key in checks:
        cur.execute(f"SELECT COUNT(*) FROM {source}")
        source_count=cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(*) FROM warehouse.{fact}")
        fact_count=cur.fetchone()[0]
        status="PASS" if source_count==fact_count else "FAIL"
        print(f"{fact}: SOURCE={source_count} FACT={fact_count} ROW_RECONCILIATION={status}")
        all_pass=all_pass and status=="PASS"

    cur.execute("""SELECT COUNT(*) FROM (SELECT order_id FROM warehouse.fact_orders GROUP BY order_id HAVING COUNT(*)>1) x""")
    orders_dup=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT order_id,order_item_id FROM warehouse.fact_order_items GROUP BY order_id,order_item_id HAVING COUNT(*)>1) x""")
    items_dup=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT order_id,payment_sequential FROM warehouse.fact_payments GROUP BY order_id,payment_sequential HAVING COUNT(*)>1) x""")
    payments_dup=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM (SELECT review_id,order_id FROM warehouse.fact_reviews GROUP BY review_id,order_id HAVING COUNT(*)>1) x""")
    reviews_dup=cur.fetchone()[0]

    print(f"FACT_ORDERS_DUPLICATE_GRAIN={orders_dup}")
    print(f"FACT_ORDER_ITEMS_DUPLICATE_GRAIN={items_dup}")
    print(f"FACT_PAYMENTS_DUPLICATE_GRAIN={payments_dup}")
    print(f"FACT_REVIEWS_DUPLICATE_GRAIN={reviews_dup}")

    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_order_items WHERE item_price < 0 OR freight_value < 0 OR total_item_value < 0""")
    negative_items=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_payments WHERE payment_value < 0""")
    negative_payments=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_reviews WHERE review_score NOT BETWEEN 1 AND 5""")
    invalid_reviews=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_orders WHERE delivery_duration_days < 0""")
    negative_delivery=cur.fetchone()[0]

    print(f"NEGATIVE_ORDER_ITEM_MEASURES={negative_items}")
    print(f"NEGATIVE_PAYMENT_MEASURES={negative_payments}")
    print(f"INVALID_REVIEW_SCORES={invalid_reviews}")
    print(f"NEGATIVE_DELIVERY_DURATION={negative_delivery}")

    grain_pass=all(x==0 for x in [orders_dup,items_dup,payments_dup,reviews_dup])
    measure_pass=all(x==0 for x in [negative_items,negative_payments,invalid_reviews,negative_delivery])
    print(f"FACT_GRAIN_VALIDATION={'PASS' if grain_pass else 'FAIL'}")
    print(f"FACT_MEASURE_VALIDATION={'PASS' if measure_pass else 'FAIL'}")

    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_order_items f LEFT JOIN warehouse.dim_customer c ON f.customer_sk=c.customer_sk LEFT JOIN warehouse.dim_product p ON f.product_sk=p.product_sk LEFT JOIN warehouse.dim_seller s ON f.seller_sk=s.seller_sk LEFT JOIN warehouse.dim_date d ON f.order_date_sk=d.date_sk WHERE c.customer_sk IS NULL OR p.product_sk IS NULL OR s.seller_sk IS NULL OR d.date_sk IS NULL""")
    item_orphans=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_orders f LEFT JOIN warehouse.dim_customer c ON f.customer_sk=c.customer_sk WHERE c.customer_sk IS NULL""")
    order_orphans=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_payments f LEFT JOIN warehouse.dim_customer c ON f.customer_sk=c.customer_sk WHERE c.customer_sk IS NULL""")
    payment_orphans=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM warehouse.fact_reviews f LEFT JOIN warehouse.dim_customer c ON f.customer_sk=c.customer_sk WHERE c.customer_sk IS NULL""")
    review_orphans=cur.fetchone()[0]

    print(f"FACT_ORDER_ITEMS_DIMENSION_ORPHANS={item_orphans}")
    print(f"FACT_ORDERS_DIMENSION_ORPHANS={order_orphans}")
    print(f"FACT_PAYMENTS_DIMENSION_ORPHANS={payment_orphans}")
    print(f"FACT_REVIEWS_DIMENSION_ORPHANS={review_orphans}")

    fk_pass=all(x==0 for x in [item_orphans,order_orphans,payment_orphans,review_orphans])
    print(f"FACT_DIMENSION_INTEGRITY={'PASS' if fk_pass else 'FAIL'}")

    if all_pass and grain_pass and measure_pass and fk_pass:
        conn.commit()
        print("PASS - COMPLETE FACT LAYER VALIDATION")
    else:
        raise RuntimeError("Complete fact-layer validation failed")
finally:
    cur.close()
    conn.close()
