# Physical Schema Inventory

## Document Status

- Status: Active
- Area: 05 — Source Data Profiling
- Step: 05.6 — Physical Schema Inventory
- Evidence Basis: Actual local Olist CSV files
- Profiling Timestamp: 2026-09-19 12:02:11 +05:30

## Physical Schema Boundary

This artifact records the observed physical source schema. It does not define warehouse facts, dimensions, surrogate keys, business grain, or transformation-layer types.

## olist_customers_dataset.csv

| Column | Physical Type |
|---|---|
| customer_id | str |
| customer_unique_id | str |
| customer_zip_code_prefix | int64 |
| customer_city | str |
| customer_state | str |

## olist_geolocation_dataset.csv

| Column | Physical Type |
|---|---|
| geolocation_zip_code_prefix | int64 |
| geolocation_lat | float64 |
| geolocation_lng | float64 |
| geolocation_city | str |
| geolocation_state | str |

## olist_order_items_dataset.csv

| Column | Physical Type |
|---|---|
| order_id | str |
| order_item_id | int64 |
| product_id | str |
| seller_id | str |
| shipping_limit_date | str |
| price | float64 |
| freight_value | float64 |

## olist_order_payments_dataset.csv

| Column | Physical Type |
|---|---|
| order_id | str |
| payment_sequential | int64 |
| payment_type | str |
| payment_installments | int64 |
| payment_value | float64 |

## olist_order_reviews_dataset.csv

| Column | Physical Type |
|---|---|
| review_id | str |
| order_id | str |
| review_score | int64 |
| review_comment_title | str |
| review_comment_message | str |
| review_creation_date | str |
| review_answer_timestamp | str |

## olist_orders_dataset.csv

| Column | Physical Type |
|---|---|
| order_id | str |
| customer_id | str |
| order_status | str |
| order_purchase_timestamp | str |
| order_approved_at | str |
| order_delivered_carrier_date | str |
| order_delivered_customer_date | str |
| order_estimated_delivery_date | str |

## olist_products_dataset.csv

| Column | Physical Type |
|---|---|
| product_id | str |
| product_category_name | str |
| product_name_lenght | float64 |
| product_description_lenght | float64 |
| product_photos_qty | float64 |
| product_weight_g | int64 |
| product_length_cm | int64 |
| product_height_cm | int64 |
| product_width_cm | int64 |

## olist_sellers_dataset.csv

| Column | Physical Type |
|---|---|
| seller_id | str |
| seller_zip_code_prefix | int64 |
| seller_city | str |
| seller_state | str |

## product_category_name_translation.csv

| Column | Physical Type |
|---|---|
| product_category_name | str |
| product_category_name_english | str |

## Observed Physical Characteristics

- Identifier-like columns are physically represented as strings.
- Zip-code prefix columns are physically represented as int64.
- Monetary columns observed in the source include float64 values.
- Multiple date/time fields are physically represented as strings in the source.
- Product descriptive and measurement columns use both float64 and int64 physical types.
- Review text fields are physically represented as strings.

## Type Interpretation Boundary

Observed pandas physical types are source profiling evidence only. Analytical and warehouse-layer type conversions will be documented in later transformation and modeling areas.

## Key Interpretation Boundary

No primary-key, unique-key, foreign-key, or business-grain assertion is made by this artifact. Key behavior requires dedicated profiling evidence.

## Assumptions

- Physical types were observed using pandas against the downloaded local CSV files.
- The source files were not modified before profiling.

## Unknowns

- Column-level null rates have not yet been profiled.
- Duplicate rates have not yet been profiled.
- Key uniqueness has not yet been established.
- Cross-file relationship integrity has not yet been established.

## Physical Modeling Boundary

This artifact describes the source physical schema only. It does not establish the final warehouse schema or analytical model.

## Artifact Completion Criteria

- [x] All 9 source files inspected
- [x] Physical column names captured
- [x] Physical data types captured
- [x] Source schema boundary documented
- [x] Type interpretation boundary documented
- [x] Key interpretation boundary documented
- [x] Assumptions documented
- [x] Unknowns documented
- [x] Physical modeling boundary documented
