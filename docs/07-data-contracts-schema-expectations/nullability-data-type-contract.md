# Area 07.3.3 — Nullability & Data-Type Contract

## Document Status

Status: Accepted & Frozen

## Purpose

This artifact defines the expected physical data types and nullability behavior for the nine Olist source datasets entering the RetailIQ platform.
The contract is based on the frozen Area 05 physical schema inventory and data profiling evidence.

## Contract Boundary

The contract describes the source interface as physically observed.
It does not mutate, clean, deduplicate, impute, or otherwise alter the source data.
Transformation-specific type changes belong to downstream staging, intermediate, dimensional, fact, and mart layers.

## Evidence Source

Primary evidence:
- Area 05 physical-schema-inventory.md
- Area 05 data-profile.md
- Area 06 source relationship and dependency evidence

## Nullability Classification

- NOT NULL: field was observed with zero null values in the physical source profile.
- NULLABLE: field was observed with one or more null values.
- Conditional / structural: nullability is governed by source lifecycle or business context and must not be converted into an artificial default.

## Dataset Contracts

### 1. customers

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| customer_id | string/object | NOT NULL | Primary source key |
| customer_unique_id | string/object | NOT NULL | Customer identity key |
| customer_zip_code_prefix | int64 | NOT NULL | Geographic reference |
| customer_city | string/object | NOT NULL | Descriptive attribute |
| customer_state | string/object | NOT NULL | Descriptive attribute |

Observed profile: no nulls in profiled customer fields.

### 2. geolocation

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| geolocation_zip_code_prefix | int64 | NOT NULL | Geographic reference key |
| geolocation_lat | float64 | NOT NULL | Latitude attribute |
| geolocation_lng | float64 | NOT NULL | Longitude attribute |
| geolocation_city | string/object | NOT NULL | Geographic attribute |
| geolocation_state | string/object | NOT NULL | Geographic attribute |

Observed profile: no nulls in profiled geolocation fields.
Geolocation is not treated as a one-row-per-zip dimension at this source-contract stage.

### 3. order_items

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| order_id | string/object | NOT NULL | Foreign key to orders |
| order_item_id | int64 | NOT NULL | Composite line-item key component |
| product_id | string/object | NOT NULL | Foreign key to products |
| seller_id | string/object | NOT NULL | Foreign key to sellers |
| shipping_limit_date | string/object | NOT NULL | Operational timestamp field |
| price | float64 | NOT NULL | Monetary measure |
| freight_value | float64 | NOT NULL | Monetary measure |

Composite source key: (order_id, order_item_id).

### 4. order_payments

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| order_id | string/object | NOT NULL | Foreign key to orders |
| payment_sequential | int64 | NOT NULL | Composite payment key component |
| payment_type | string/object | NOT NULL | Payment classification |
| payment_installments | int64 | NOT NULL | Payment attribute |
| payment_value | float64 | NOT NULL | Monetary measure |

Composite source key: (order_id, payment_sequential).

### 5. order_reviews

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| review_id | string/object | NOT NULL | Review identifier; not unique alone |
| order_id | string/object | NOT NULL | Foreign key to orders |
| review_score | int64 | NOT NULL | Review measure |
| review_comment_title | string/object | NULLABLE | Optional review attribute |
| review_comment_message | string/object | NULLABLE | Optional review attribute |
| review_creation_date | string/object | NOT NULL | Review timestamp field |
| review_answer_timestamp | string/object | NOT NULL | Review response timestamp |

Source evidence shows review_id alone is not unique.
Composite relationship key review_id + order_id is unique in the observed source profile.
Optional review text fields remain nullable and must not be replaced with fabricated values.

### 6. orders

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| order_id | string/object | NOT NULL | Primary source key |
| customer_id | string/object | NOT NULL | Foreign key to customers |
| order_status | string/object | NOT NULL | Order lifecycle attribute |
| order_purchase_timestamp | string/object | NOT NULL | Business event timestamp |
| order_approved_at | string/object | NULLABLE | Lifecycle timestamp |
| order_delivered_carrier_date | string/object | NULLABLE | Lifecycle timestamp |
| order_delivered_customer_date | string/object | NULLABLE | Lifecycle timestamp |
| order_estimated_delivery_date | string/object | NOT NULL | Delivery expectation timestamp |

Observed nullable lifecycle fields must remain nullable because missing values can represent incomplete or non-delivered order lifecycle states.

### 7. products

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| product_id | string/object | NOT NULL | Primary source key |
| product_category_name | string/object | NULLABLE | Product classification |
| product_name_lenght | float64 | NULLABLE | Product attribute |
| product_description_lenght | float64 | NULLABLE | Product attribute |
| product_photos_qty | float64 | NULLABLE | Product attribute |
| product_weight_g | int64 | NULLABLE | Physical attribute |
| product_length_cm | int64 | NULLABLE | Physical attribute |
| product_height_cm | int64 | NULLABLE | Physical attribute |
| product_width_cm | int64 | NULLABLE | Physical attribute |

Observed product descriptive fields contain source nulls.
Category translation is a separate source dataset and must not be assumed complete for every non-null product category.

### 8. sellers

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| seller_id | string/object | NOT NULL | Primary source key |
| seller_zip_code_prefix | int64 | NOT NULL | Geographic reference |
| seller_city | string/object | NOT NULL | Descriptive attribute |
| seller_state | string/object | NOT NULL | Descriptive attribute |

Observed profile: no nulls in seller fields.

### 9. product_category_name_translation

| Column | Physical Type | Nullability | Key Role |
|---|---|---|---|
| product_category_name | string/object | NOT NULL | Source category key |
| product_category_name_english | string/object | NOT NULL | Translation attribute |

Observed profile: no nulls in translation fields.

## Key Contract Controls

- Source primary and composite key fields must not be silently converted to nullable fields.
- Observed nullable fields must remain nullable at the source boundary.
- No default values may be invented to replace source nulls.
- Physical source types must be preserved at the contract boundary.
- Downstream canonical types may be defined separately during staging and standardization.
- review_id must not be treated as a unique source key by itself.
- order_items uses (order_id, order_item_id) as its observed composite key.
- order_payments uses (order_id, payment_sequential) as its observed composite key.

## Source Preservation Rule

The original source CSV files remain immutable.
This contract documents observed source characteristics and does not modify the source datasets.

## Acceptance Boundary

Area 07.3.3 is complete when all nine source datasets have documented physical data types, nullability expectations, key roles, and source-specific exceptions.

## Next Step

Step 07.3.4 will validate the nullability and data-type contract against the frozen Area 05 physical evidence.

## Artifact Completion Criteria

- All 9 source datasets represented.
- Physical data types documented.
- Nullability documented.
- Key roles documented.
- Source-specific exceptions documented.
- Source preservation rule present.
- Acceptance boundary present.

## Non-Nullable

Non-nullable fields are fields for which the Area 05 physical profile recorded no null values and which are treated as required at the source contract boundary unless a documented source-specific exception applies.

The non-nullable contract vocabulary is explicitly represented as NON-NULLABLE so downstream schema enforcement can distinguish required fields from observed nullable fields.

Representative non-nullable source fields include customer identifiers, order identifiers, order item identifiers, product identifiers, seller identifiers, payment identifiers, review identifiers, core status fields, core monetary fields, and other fields documented as having no observed nulls in Area 05.

This classification reflects the observed source profile and does not authorize mutation, imputation, or silent null replacement in the source data.


