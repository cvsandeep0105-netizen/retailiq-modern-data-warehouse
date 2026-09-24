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
    marts=[
        ("sales_orders","warehouse.fact_orders","order_id"),
        ("customer","warehouse.dim_customer","customer_sk"),
        ("product","warehouse.dim_product","product_sk"),
        ("seller_fulfillment","warehouse.dim_seller","seller_sk")
    ]
    all_reconciliation=True
    all_grain=True
    all_integrity=True

    for mart,source,key in marts:
        cur.execute(f"SELECT COUNT(*) FROM {source}")
        source_count=cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(*) FROM marts.{mart}")
        mart_count=cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(*) FROM (SELECT {key} FROM marts.{mart} GROUP BY {key} HAVING COUNT(*)>1) x")
        duplicates=cur.fetchone()[0]
        reconciliation="PASS" if source_count==mart_count else "FAIL"
        grain="PASS" if duplicates==0 else "FAIL"
        print(f"{mart}: SOURCE={source_count} MART={mart_count} RECONCILIATION={reconciliation} DUPLICATES={duplicates} GRAIN={grain}")
        all_reconciliation=all_reconciliation and reconciliation=="PASS"
        all_grain=all_grain and grain=="PASS"

    cur.execute("""SELECT COUNT(*) FROM marts.sales_orders WHERE sales_item_value<0 OR freight_value<0 OR total_order_value<0 OR payment_value<0 OR order_item_count<0 OR payment_count<0 OR review_count<0""")
    sales_invalid=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.customer WHERE sales_item_value<0 OR freight_value<0 OR total_spend<0 OR payment_value<0 OR order_count<0 OR order_item_count<0 OR payment_count<0 OR review_count<0""")
    customer_invalid=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.product WHERE sales_item_value<0 OR freight_value<0 OR total_item_value<0 OR product_order_count<0 OR order_item_count<0 OR seller_count<0 OR review_count<0""")
    product_invalid=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.seller_fulfillment WHERE sales_item_value<0 OR freight_value<0 OR total_item_value<0 OR order_count<0 OR order_item_count<0 OR customer_count<0 OR review_count<0""")
    seller_invalid=cur.fetchone()[0]

    print(f"SALES_ORDERS_INVALID_MEASURES={sales_invalid}")
    print(f"CUSTOMER_INVALID_MEASURES={customer_invalid}")
    print(f"PRODUCT_INVALID_MEASURES={product_invalid}")
    print(f"SELLER_INVALID_MEASURES={seller_invalid}")

    measure_pass=all(x==0 for x in [sales_invalid,customer_invalid,product_invalid,seller_invalid])
    print(f"MART_MEASURE_VALIDATION={'PASS' if measure_pass else 'FAIL'}")

    cur.execute("""SELECT COUNT(*) FROM marts.sales_orders s LEFT JOIN warehouse.dim_customer c ON s.customer_sk=c.customer_sk WHERE c.customer_sk IS NULL""")
    sales_orphans=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.customer m LEFT JOIN warehouse.dim_customer d ON m.customer_sk=d.customer_sk WHERE d.customer_sk IS NULL""")
    customer_orphans=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.product m LEFT JOIN warehouse.dim_product d ON m.product_sk=d.product_sk WHERE d.product_sk IS NULL""")
    product_orphans=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.seller_fulfillment m LEFT JOIN warehouse.dim_seller d ON m.seller_sk=d.seller_sk WHERE d.seller_sk IS NULL""")
    seller_orphans=cur.fetchone()[0]

    print(f"SALES_ORDERS_DIMENSION_ORPHANS={sales_orphans}")
    print(f"CUSTOMER_DIMENSION_ORPHANS={customer_orphans}")
    print(f"PRODUCT_DIMENSION_ORPHANS={product_orphans}")
    print(f"SELLER_DIMENSION_ORPHANS={seller_orphans}")

    all_integrity=all(x==0 for x in [sales_orphans,customer_orphans,product_orphans,seller_orphans])
    print(f"MART_DIMENSION_INTEGRITY={'PASS' if all_integrity else 'FAIL'}")

    cur.execute("""SELECT COUNT(*) FROM marts.sales_orders WHERE order_id IS NULL""")
    sales_null=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.customer WHERE customer_id IS NULL""")
    customer_null=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.product WHERE product_id IS NULL""")
    product_null=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(*) FROM marts.seller_fulfillment WHERE seller_id IS NULL""")
    seller_null=cur.fetchone()[0]

    print(f"SALES_ORDERS_NULL_GRAIN_KEYS={sales_null}")
    print(f"CUSTOMER_NULL_GRAIN_KEYS={customer_null}")
    print(f"PRODUCT_NULL_GRAIN_KEYS={product_null}")
    print(f"SELLER_NULL_GRAIN_KEYS={seller_null}")

    key_pass=all(x==0 for x in [sales_null,customer_null,product_null,seller_null])
    print(f"MART_GRAIN_KEY_VALIDATION={'PASS' if key_pass else 'FAIL'}")

    if all_reconciliation and all_grain and measure_pass and all_integrity and key_pass:
        print("PASS - COMPLETE BUSINESS DATA MART VALIDATION")
    else:
        raise RuntimeError("Business Data Mart validation failed")
finally:
    cur.close()
    conn.close()
