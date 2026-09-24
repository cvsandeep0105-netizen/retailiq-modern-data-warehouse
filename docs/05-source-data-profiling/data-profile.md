# RetailIQ — Source Data Profile

## Document Status
Status: In Progress — Area 05

## Profiling Boundary
This document consolidates observed physical profiling evidence from the acquired Olist source files. It records observed characteristics only and does not define the final warehouse model.

## Source File Coverage
- 9 Olist CSV source files profiled.
- Source acquisition verified before profiling.
- Physical column names and observed data types captured.
- Row counts captured for all source files.

## Observed Row Counts
| Source File | Rows | Columns |
|---|---:|---:|
| olist_customers_dataset.csv | 99,441 | 5 |
| olist_geolocation_dataset.csv | 1,001,163 | 5 |
| olist_order_items_dataset.csv | 112,650 | 7 |
| olist_order_payments_dataset.csv | 103,886 | 5 |
| olist_order_reviews_dataset.csv | 99,224 | 7 |
| olist_orders_dataset.csv | 99,441 | 8 |
| olist_products_dataset.csv | 32,951 | 9 |
| olist_sellers_dataset.csv | 3,095 | 4 |
| product_category_name_translation.csv | 71 | 2 |

## Null Profile Findings
- Customer dataset key columns contain no observed nulls.
- Orders contain missing values in approval and delivery lifecycle timestamps.
- Product dataset contains missing product-category and descriptive/physical attributes.
- Review title and message fields contain substantial missing values.
- Payment and order-item core fields contain no observed nulls in the captured profile.

## Duplicate Profile
- All nine source files were checked for complete-row duplicates.
- Complete-row duplicates were observed in olist_geolocation_dataset.csv.
- The remaining eight source files showed zero complete-row duplicates in the captured profile.
- Geolocation duplicates require business-key analysis before any deduplication decision.

## Categorical Domain Findings
- order_status contains 8 observed values.
- payment_type contains 5 observed values, including not_defined.
- review_score contains values 1 through 5.
- Customer and geolocation state domains contain 27 observed states.
- Seller state domain contains 23 observed states.
- order_item_id ranges from 1 through 21.

## Relationship Integrity
- Orders to customers: zero orphan rows observed.
- Order items to orders: zero orphan rows observed.
- Order items to products: zero orphan rows observed.
- Order items to sellers: zero orphan rows observed.
- Payments to orders: zero orphan rows observed.
- Reviews to orders: zero orphan rows observed.
- Product-category translation profiling identified 3 unmatched source-category rows requiring explicit handling.

## Date Boundary Findings
- Order purchase timestamps span September 2016 through October 2018.
- Review timestamps span October 2016 through October 2018.
- Delivery-related timestamp columns contain missing values.
- Date parsing produced no invalid non-null date values in the profiled columns.

## Physical Modeling Boundary
Observed source characteristics are evidence for later warehouse modeling decisions. This document does not define fact grain, dimension grain, surrogate keys, SCD behavior, or final warehouse relationships.

## Assumptions
- Profiling results represent the acquired local source files.
- Nulls in lifecycle timestamps may represent legitimately incomplete business processes.
- Complete-row duplication does not automatically mean a source record is invalid.

## Unknowns
- Business meaning of every duplicate geolocation row is not yet fully resolved.
- Treatment of unmatched product categories requires downstream transformation policy.
- Final analytical grain remains deferred to the dimensional modeling phase.

## Artifact Completion Criteria
- [x] All source files profiled
- [x] Row counts documented
- [x] Null findings documented
- [x] Duplicate findings documented
- [x] Categorical findings documented
- [x] Relationship integrity findings documented
- [x] Date findings documented
- [x] Physical modeling boundary documented
