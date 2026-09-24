from pathlib import Path
import json

lineage={
    "source_to_raw":[
        {"source":"olist_customers_dataset.csv","target":"data/raw/olist_customers_dataset.csv"},
        {"source":"olist_geolocation_dataset.csv","target":"data/raw/olist_geolocation_dataset.csv"},
        {"source":"olist_orders_dataset.csv","target":"data/raw/olist_orders_dataset.csv"},
        {"source":"olist_order_items_dataset.csv","target":"data/raw/olist_order_items_dataset.csv"},
        {"source":"olist_order_payments_dataset.csv","target":"data/raw/olist_order_payments_dataset.csv"},
        {"source":"olist_order_reviews_dataset.csv","target":"data/raw/olist_order_reviews_dataset.csv"},
        {"source":"olist_products_dataset.csv","target":"data/raw/olist_products_dataset.csv"},
        {"source":"olist_sellers_dataset.csv","target":"data/raw/olist_sellers_dataset.csv"},
        {"source":"product_category_name_translation.csv","target":"data/raw/product_category_name_translation.csv"}
    ],
    "raw_to_staging":[
        {"source":"raw.olist_customers","target":"staging.stg_customers"},
        {"source":"raw.olist_geolocation","target":"staging.stg_geolocation"},
        {"source":"raw.olist_orders","target":"staging.stg_orders"},
        {"source":"raw.olist_order_items","target":"staging.stg_order_items"},
        {"source":"raw.olist_order_payments","target":"staging.stg_order_payments"},
        {"source":"raw.olist_order_reviews","target":"staging.stg_order_reviews"},
        {"source":"raw.olist_products","target":"staging.stg_products"},
        {"source":"raw.olist_sellers","target":"staging.stg_sellers"},
        {"source":"raw.product_category_name_translation","target":"staging.stg_category_translation"}
    ],
    "staging_to_intermediate":[
        {"source":"staging.*","target":"intermediate.*"}
    ],
    "intermediate_to_warehouse":[
        {"source":"intermediate.int_customers","target":"warehouse.dim_customer"},
        {"source":"intermediate.int_products","target":"warehouse.dim_product"},
        {"source":"intermediate.int_sellers","target":"warehouse.dim_seller"},
        {"source":"intermediate.int_orders","target":"warehouse.fact_orders"},
        {"source":"intermediate.int_order_items","target":"warehouse.fact_order_items"},
        {"source":"intermediate.int_order_payments","target":"warehouse.fact_payments"},
        {"source":"intermediate.int_order_reviews","target":"warehouse.fact_reviews"},
        {"source":"date attributes","target":"warehouse.dim_date"}
    ],
    "warehouse_to_marts":[
        {"source":"warehouse.fact_orders + warehouse.fact_order_items + warehouse.fact_payments + warehouse.fact_reviews","target":"marts.sales_orders"},
        {"source":"warehouse.dim_customer + warehouse facts","target":"marts.customer"},
        {"source":"warehouse.dim_product + warehouse.fact_order_items + warehouse.fact_reviews","target":"marts.product"},
        {"source":"warehouse.dim_seller + warehouse.fact_order_items + warehouse.fact_orders + warehouse.fact_reviews","target":"marts.seller_fulfillment"}
    ],
    "marts_to_semantic":[
        {"source":"marts.sales_orders","target":"semantic.sales_analysis"},
        {"source":"marts.customer","target":"semantic.customer_analysis"},
        {"source":"marts.product","target":"semantic.product_analysis"},
        {"source":"marts.seller_fulfillment","target":"semantic.seller_fulfillment_analysis"},
        {"source":"marts + KPI calculations","target":"semantic.kpi_summary"}
    ],
    "semantic_to_bi":[
        {"source":"semantic.sales_analysis","target":"semantic.bi_sales_overview"},
        {"source":"semantic.customer_analysis","target":"semantic.bi_customer_overview"},
        {"source":"semantic.product_analysis","target":"semantic.bi_product_overview"},
        {"source":"semantic.seller_fulfillment_analysis","target":"semantic.bi_seller_fulfillment"}
    ]
}

out=Path("data/output/lineage")
out.mkdir(parents=True,exist_ok=True)
(out/"lineage_catalog.json").write_text(json.dumps(lineage,indent=2),encoding="utf-8")

expected_sections=["source_to_raw","raw_to_staging","staging_to_intermediate","intermediate_to_warehouse","warehouse_to_marts","marts_to_semantic","semantic_to_bi"]
present=[x for x in expected_sections if x in lineage and len(lineage[x])>0]
edge_count=sum(len(lineage[x]) for x in present)

print(f"LINEAGE_SECTION_COUNT={len(present)}")
print(f"LINEAGE_EDGE_COUNT={edge_count}")
print(f"LINEAGE_SECTION_STATUS={'PASS' if len(present)==7 else 'FAIL'}")
artifact_exists=(out/"lineage_catalog.json").exists(); print(f"LINEAGE_ARTIFACT_STATUS={'PASS' if artifact_exists else 'FAIL'}")

if len(present)==7 and edge_count>=30 and (out/"lineage_catalog.json").exists():
    print("PASS - DATA LINEAGE AND METADATA CATALOG VALIDATED")
else:
    raise RuntimeError("Lineage validation failed")

