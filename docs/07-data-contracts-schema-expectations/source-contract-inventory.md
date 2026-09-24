# Area 07.2 — Source Contract Inventory

## Document Status
- Status: Accepted & Frozen
- Area: 07
- Step: 07.2 — Source Contract Inventory

## Purpose
Establish the contract inventory for every discovered Olist source dataset and define the contract dimensions that must be enforced or monitored.

## Source Contract Inventory

| Source Dataset | Contract Coverage | Primary Contract Focus |
|---|---|---|
| olist_customers_dataset.csv | Required | Customer identity, attributes, ZIP geography, nullability |
| olist_geolocation_dataset.csv | Required | ZIP-prefix geography, multiplicity, coordinate fields, coverage |
| olist_order_items_dataset.csv | Required | Order-item grain, composite identity, product/seller relationships, measures |
| olist_order_payments_dataset.csv | Required | Order-payment grain, payment sequence, payment domain, measures |
| olist_order_reviews_dataset.csv | Required | Review identity, review/order relationship, review score, nullable comments |
| olist_orders_dataset.csv | Required | Order identity, customer relationship, lifecycle status, timestamps |
| olist_products_dataset.csv | Required | Product identity, category, physical attributes, nullable attributes |
| olist_sellers_dataset.csv | Required | Seller identity, seller geography, ZIP coverage |
| product_category_name_translation.csv | Required | Category translation key, translation coverage, uniqueness |

## Contract Dimensions

Each source contract will address the following dimensions where applicable:

- Structural schema
- Data types
- Required fields
- Nullable fields
- Primary or natural identity
- Composite keys
- Domain constraints
- Relationship constraints
- Cardinality expectations
- Temporal constraints
- Geographic expectations
- Volume expectations
- Known exceptions
- Source preservation requirements

## Evidence Sources

Contract definitions must use evidence from:

- Area 05 — Physical source profiling
- Area 06 — Source relationships and data dependencies
- Documented source exceptions
- Explicit engineering decisions

## Known Contract-Sensitive Exceptions

- Review identifiers require composite interpretation because review_id alone is not unique.
- Product category translation has documented unmatched non-null source category values.
- Geolocation contains repeated ZIP-prefix records and must not be collapsed without an explicit modeling decision.
- Customer and seller ZIP prefixes have documented geolocation coverage exceptions.
- Source nullable fields must not automatically be converted into invalid defaults.

## Contract Ownership Boundary

The source contract describes the expected source interface entering the RetailIQ platform. Transformation-specific rules belong to downstream staging, intermediate, dimensional, and mart layers.

## Source Preservation Rule

Contract validation must observe the source data without mutating the original source files.

## Acceptance Boundary

Step 07.2 is complete when all nine source datasets are represented in the inventory and each has an explicit contract coverage classification and primary contract focus.

## Next Step

Step 07.3 will define the detailed structural schema contract for the source datasets.

