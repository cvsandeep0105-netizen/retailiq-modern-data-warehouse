# AREA 06.4 — Source Dependency Direction

## Document Status
- Status: Evidence captured and dependency direction documented
- Area: 06.4 — Source Dependency Direction
- Source basis: Locally acquired Olist source datasets
- This artifact records observed source-level dependency direction only.

## Dependency Direction

| Parent / Referenced Dataset | Child / Dependent Dataset | Dependency Key | Observed Coverage |
|---|---|---|---:|
| olist_customers_dataset.csv | olist_orders_dataset.csv | customer_id | 99,441 / 99,441 |
| olist_orders_dataset.csv | olist_order_items_dataset.csv | order_id | 112,650 / 112,650 |
| olist_orders_dataset.csv | olist_order_payments_dataset.csv | order_id | 103,886 / 103,886 |
| olist_orders_dataset.csv | olist_order_reviews_dataset.csv | order_id | 99,224 / 99,224 |
| olist_products_dataset.csv | olist_order_items_dataset.csv | product_id | 112,650 / 112,650 |
| olist_sellers_dataset.csv | olist_order_items_dataset.csv | seller_id | 112,650 / 112,650 |
| product_category_name_translation.csv | olist_products_dataset.csv | product_category_name | 32,328 / 32,341 non-null product categories |

## Source Dependency Interpretation

The observed dependency graph is:

customers -> orders -> order_items
                    |
                    +-> payments
                    +-> reviews

order_items -> products -> category_translation
order_items -> sellers

The arrows represent observed source-level dependency direction and join-key availability. They do not yet represent final warehouse foreign keys, dimensional relationships, or physical warehouse implementation.

## Source Node Inventory

| Dataset | Observed Rows | Dependency Role |
|---|---:|---|
| olist_customers_dataset.csv | 99,441 | Customer reference / order parent |
| olist_orders_dataset.csv | 99,441 | Order transaction parent |
| olist_order_items_dataset.csv | 112,650 | Order-line dependent dataset |
| olist_order_payments_dataset.csv | 103,886 | Order payment dependent dataset |
| olist_order_reviews_dataset.csv | 99,224 | Order review dependent dataset |
| olist_products_dataset.csv | 32,951 | Product reference dataset |
| olist_sellers_dataset.csv | 3,095 | Seller reference dataset |
| product_category_name_translation.csv | 71 | Category translation/reference dataset |
| olist_geolocation_dataset.csv | 1,001,163 | Geographic reference/supporting dataset; dependency direction requires separate key-level treatment |

## Dependency Coverage Findings

- All observed order rows matched a customer_id in the customer dataset.
- All observed order-item rows matched an order_id in the orders dataset.
- All observed payment rows matched an order_id in the orders dataset.
- All observed review rows matched an order_id in the orders dataset.
- All observed order-item rows matched a product_id in the products dataset.
- All observed order-item rows matched a seller_id in the sellers dataset.
- 32,328 of 32,341 non-null product category values matched the category translation dataset.
- 13 non-null product category values did not have a translation match.
- The 13 unmatched category values are retained as a source-level exception for downstream standardization and modeling decisions.

## Geolocation Dependency Boundary

olist_geolocation_dataset.csv is not assigned a definitive parent-child dependency direction in this artifact. Its zip-code prefix relationship requires dedicated key-level validation because the source contains repeated geographic records per prefix and therefore cannot be treated as a simple unique-key parent without further analysis.

## Join and Multiplication Risk Boundary

- One order can contain multiple order items.
- One order can contain multiple payment records.
- One order can contain multiple review rows according to observed source data.
- Joining multiple child datasets directly at order grain can multiply rows and distort measures.
- Analytical models must therefore preserve the documented grain of each downstream fact or intermediate model.
- No aggregation strategy is finalized in this artifact.

## Interpretation Boundary

- Dependency direction is based on observed source keys and local coverage checks.
- Coverage does not prove business semantics beyond the observed key relationship.
- A successful key match does not establish that the relationship is logically one-to-one.
- Final warehouse relationship types, surrogate keys, fact grain, dimension grain, and conformed dimensions are deferred to later modeling areas.

## Assumptions

- The locally acquired CSV files represent the source snapshot being profiled.
- Column values used for dependency checks were evaluated using their observed source representations.
- Non-null product category values were used when measuring translation coverage.
- The source relationship graph is treated as an engineering dependency graph, not a claim about the original operational database implementation.

## Unknowns

- The historical source-system foreign-key enforcement mechanism is unknown.
- The business reason for the 13 unmatched product category translations is not established.
- The appropriate analytical treatment of repeated review_id values is not finalized here.
- Geolocation zip-code dependency semantics require additional key-level analysis.
- Final warehouse relationship implementation is not defined in this artifact.

## Physical Modeling Boundary

This artifact records source-level dependency direction and observed coverage only. It does not define warehouse tables, surrogate keys, dimensional relationships, fact grain, SCD behavior, physical indexes, partitioning, clustering, or final BI models.

## Artifact Completion Criteria

- [x] Source dependency directions documented
- [x] Dependency keys documented
- [x] Coverage evidence documented
- [x] Source node inventory documented
- [x] Geolocation boundary documented
- [x] Join multiplication risk documented
- [x] Interpretation boundary documented
- [x] Assumptions documented
- [x] Unknowns documented
- [x] Physical modeling boundary documented

