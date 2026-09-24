from pathlib import Path
import psycopg2
import pytest

def env():
    d={}
    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k,v=line.split("=",1); d[k.strip()]=v.strip()
    return d

@pytest.fixture(scope="module")
def conn():
    c=env()
    connection=psycopg2.connect(host=c["POSTGRES_HOST"],port=int(c["POSTGRES_PORT"]),dbname=c["POSTGRES_DB"],user=c["POSTGRES_USER"],password=c["POSTGRES_PASSWORD"])
    yield connection
    connection.close()

def scalar(cur,sql):
    cur.execute(sql)
    return cur.fetchone()[0]

def test_required_schemas_exist(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM information_schema.schemata WHERE schema_name IN ('raw','staging','intermediate','warehouse','marts','semantic')")==6

def test_fact_counts(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_orders")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_order_items")==112650
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_payments")==103886
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_reviews")==99224

def test_dimension_counts(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.dim_customer")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.dim_product")==32951
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.dim_seller")==3095
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.dim_date")==1096

def test_mart_counts(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM marts.sales_orders")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM marts.customer")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM marts.product")==32951
    assert scalar(cur,"SELECT COUNT(*) FROM marts.seller_fulfillment")==3095

def test_semantic_counts(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.kpi_summary")==1
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.sales_analysis")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.customer_analysis")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.product_analysis")==32951
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.seller_fulfillment_analysis")==3095

def test_bi_counts(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.bi_sales_overview")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.bi_customer_overview")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.bi_product_overview")==32951
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.bi_seller_fulfillment")==3095

def test_fact_grains(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM (SELECT order_id FROM warehouse.fact_orders GROUP BY order_id HAVING COUNT(*)>1)x")==0
    assert scalar(cur,"SELECT COUNT(*) FROM (SELECT order_id,order_item_id FROM warehouse.fact_order_items GROUP BY order_id,order_item_id HAVING COUNT(*)>1)x")==0
    assert scalar(cur,"SELECT COUNT(*) FROM (SELECT order_id,payment_sequential FROM warehouse.fact_payments GROUP BY order_id,payment_sequential HAVING COUNT(*)>1)x")==0
    assert scalar(cur,"SELECT COUNT(*) FROM (SELECT review_id,order_id FROM warehouse.fact_reviews GROUP BY review_id,order_id HAVING COUNT(*)>1)x")==0

def test_core_quality_rules(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_reviews WHERE review_score NOT BETWEEN 1 AND 5")==0
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_order_items WHERE item_price<0 OR freight_value<0 OR total_item_value<0")==0
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_payments WHERE payment_value<0")==0
    assert scalar(cur,"SELECT COUNT(*) FROM warehouse.fact_orders WHERE delivery_duration_days<0")==0

def test_analytical_outputs(conn):
    cur=conn.cursor()
    assert scalar(cur,"SELECT COUNT(*) FROM semantic.bi_sales_overview")==99441
    assert scalar(cur,"SELECT COUNT(*) FROM (SELECT DATE_TRUNC('month',order_purchase_timestamp)::date FROM semantic.sales_analysis GROUP BY 1)x")==25


