# Area 07.3 — Structural Schema Contract

## Document Status

Status: Accepted & Frozen

## Purpose

This document defines the structural schema expectations for the nine RetailIQ source datasets. The contract captures expected column names, physical data types, key roles, nullability expectations, and structural constraints derived from the verified Area 05 physical schema inventory.

## Contract Boundary

The contract applies to the source interface entering the RetailIQ platform. It defines structural expectations only. Business transformations, dimensional modeling, deduplication, normalization, and analytical semantics are outside this contract.

## Source Preservation Rule

Schema validation must observe the original source files without mutating, renaming, deleting, deduplicating, or otherwise altering source records.

## Dataset Contract Register

| Dataset | Primary Structural Key | Key Role | Structural Notes |
|---|---|---|---|
| olist_customers_dataset.csv | customer_id | Primary identifier | customer_id expected non-null and unique |
| olist_geolocation_dataset.csv | geolocation_zip_code_prefix + location attributes | Reference / non-unique geographic records | Zip prefix may have multiple geographic rows |
| olist_order_items_dataset.csv | order_id + order_item_id | Composite row identifier | order_id and order_item_id expected non-null; composite uniqueness observed |
| olist_order_payments_dataset.csv | order_id + payment_sequential | Composite row identifier | Multiple payment records may exist per order |
| olist_order_reviews_dataset.csv | review_id + order_id | Composite review identifier | review_id alone is not unique in the physical source |
| olist_orders_dataset.csv | order_id | Primary identifier | order_id expected non-null and unique |
| olist_products_dataset.csv | product_id | Primary identifier | product_id expected non-null and unique |
| olist_sellers_dataset.csv | seller_id | Primary identifier | seller_id expected non-null and unique |
| product_category_name_translation.csv | product_category_name | Reference identifier | Translation key expected unique; unmatched source categories require exception handling |

## Physical Type Expectations

### Customers

| Column | Expected Type | Nullability |
|---|---|---|
| customer_id | string | NOT NULL |
| customer_unique_id | string | NOT NULL |
| customer_zip_code_prefix | integer | NOT NULL |
| customer_city | string | NOT NULL |
| customer_state | string | NOT NULL |

### Geolocation

| Column | Expected Type | Nullability |
|---|---|---|
| geolocation_zip_code_prefix | integer | NOT NULL |
| geolocation_lat | float | NOT NULL |
| geolocation_lng | float | NOT NULL |
| geolocation_city | string | NOT NULL |
| geolocation_state | string | NOT NULL |

### Order Items

| Column | Expected Type | Nullability |
|---|---|---|
| order_id | string | NOT NULL |
| order_item_id | integer | NOT NULL |
| product_id | string | NOT NULL |
| seller_id | string | NOT NULL |
| shipping_limit_date | string / date-time candidate | NOT NULL |
| price | float | NOT NULL |
| freight_value | float | NOT NULL |

### Order Payments

| Column | Expected Type | Nullability |
|---|---|---|
| order_id | string | NOT NULL |
| payment_sequential | integer | NOT NULL |
| payment_type | string | NOT NULL |
| payment_installments | integer | NOT NULL |
| payment_value | float | NOT NULL |

### Order Reviews

| Column | Expected Type | Nullability |
|---|---|---|
| review_id | string | NOT NULL |
| order_id | string | NOT NULL |
| review_score | integer | NOT NULL |
| review_comment_title | string | NULLABLE |
| review_comment_message | string | NULLABLE |
| review_creation_date | string / date-time candidate | NOT NULL |
| review_answer_timestamp | string / date-time candidate | NOT NULL |

### Orders

| Column | Expected Type | Nullability |
|---|---|---|
| order_id | string | NOT NULL |
| customer_id | string | NOT NULL |
| order_status | string | NOT NULL |
| order_purchase_timestamp | string / date-time candidate | NOT NULL |
| order_approved_at | string / date-time candidate | NULLABLE |
| order_delivered_carrier_date | string / date-time candidate | NULLABLE |
| order_delivered_customer_date | string / date-time candidate | NULLABLE |
| order_estimated_delivery_date | string / date-time candidate | NOT NULL |

### Products

| Column | Expected Type | Nullability |
|---|---|---|
| product_id | string | NOT NULL |
| product_category_name | string | NULLABLE |
| product_name_lenght | float | NULLABLE |
| product_description_lenght | float | NULLABLE |
| product_photos_qty | float | NULLABLE |
| product_weight_g | integer | NULLABLE |
| product_length_cm | integer | NULLABLE |
| product_height_cm | integer | NULLABLE |
| product_width_cm | integer | NULLABLE |

### Sellers

| Column | Expected Type | Nullability |
|---|---|---|
| seller_id | string | NOT NULL |
| seller_zip_code_prefix | integer | NOT NULL |
| seller_city | string | NOT NULL |
| seller_state | string | NOT NULL |

### Category Translation

| Column | Expected Type | Nullability |
|---|---|---|
| product_category_name | string | NOT NULL |
| product_category_name_english | string | NOT NULL |

## Structural Constraints

- Required source columns must be present before downstream processing.
- Primary identifiers must not be silently renamed or dropped at ingestion.
- Composite identifiers must be evaluated at their declared grain.
- Nullable fields must remain explicitly nullable until downstream rules define treatment.
- Physical source types must be validated before transformation.
- Date-time candidate fields require parsing validation before analytical use.
- Numeric measures require numeric type validation.
- Reference datasets must not be assumed to provide universal coverage.

## Known Structural Exceptions

- review_id is not unique by itself; review_id + order_id is the validated composite identifier.
- Geolocation zip-code prefixes can map to multiple geographic records and must not be collapsed at source-contract validation.
- product category translation does not cover every non-null product category value.
- Nullable operational timestamps in the orders dataset are valid structural conditions and require downstream treatment rather than source mutation.

## Evidence Source

Primary evidence: Area 05 physical-schema-inventory.md and data-profile.md.

## Acceptance Boundary

Area 07.3 structural contract acceptance requires all nine datasets to be represented, all verified physical columns to be represented, structural key roles to be documented, nullable fields to be identified, and known structural exceptions to be explicitly recorded.

## Next Step

Step 07.3.2 will validate this contract against the actual Area 05 physical schema evidence before the artifact is accepted and frozen.

