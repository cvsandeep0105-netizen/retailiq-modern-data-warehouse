# AREA 06.5 — Source Relationship Exceptions & Boundary Cases

## Document Status
- Status: Observed relationship exceptions and boundary cases documented
- Area: 06.5 — Source Relationship Exceptions & Boundary Cases
- Source basis: Locally acquired Olist source datasets
- This artifact documents observed source conditions only.

## Purpose

This artifact records source-level relationship exceptions, ambiguous relationship behavior, and boundary cases identified during Areas 05 and 06. It does not remediate, mutate, deduplicate, translate, or otherwise alter the source datasets.

## Exception Register

| ID | Source Area | Exception / Boundary Case | Observed Evidence | Engineering Boundary |
|---|---|---|---|---|
| EX-01 | Product / Category Translation | Unmatched product category translations | 32,328 of 32,341 non-null product category values matched; 13 did not match | Do not invent translations at source level; downstream treatment requires explicit rule |
| EX-02 | Reviews | Repeated review_id values | 99,224 review rows; 98,410 distinct review_id values; 814 duplicate rows by review_id | review_id cannot automatically be assumed to be a source-level unique business key |
| EX-03 | Reviews | Repeated review_id values span multiple orders | 789 duplicated review_id values were associated with multiple order_id values | Review grain and historical treatment require explicit modeling decision |
| EX-04 | Reviews | Review multiplicity | Maximum observed rows for one review_id = 3; maximum observed reviews per order = 3 | Do not collapse reviews into one order-level record without a defined aggregation rule |
| EX-05 | Geolocation | Repeated geographic records per zip-code prefix | geolocation_zip_code_prefix has 19,015 distinct values across 1,001,163 rows | Cannot automatically model zip-code prefix as a unique parent key |
| EX-06 | Orders / Items | Multiple items per order | Maximum 21 items per order; 9,803 orders have more than one item | Order and order-item grains must remain separate |
| EX-07 | Orders / Payments | Multiple payments per order | Maximum 29 payment records per order; 2,961 orders have more than one payment | Payment measures must not be joined naively at order grain |
| EX-08 | Orders / Reviews | Multiple reviews per order | Maximum 3 review rows per order; 547 orders have more than one review | Review grain must remain distinct from order grain unless an explicit aggregation is defined |
| EX-09 | Customers / Orders | Observed one-order-per-customer_id condition | 99,441 customer rows and 99,441 order rows; observed maximum orders per customer_id = 1 | This is a property of the acquired snapshot, not a universal business rule |

## EX-01 — Unmatched Product Category Translations

- Product dataset contains 32,341 non-null product_category_name values.
- 32,328 matched the category translation dataset.
- 13 non-null category values did not have a translation match.
- The unmatched values are retained as source exceptions.
- No translated English category value is invented in this area.
- Any fallback, unknown, preservation, or enrichment strategy is deferred to later transformation/modeling areas.

## EX-02 / EX-03 / EX-04 — Review Identifier Boundary

Observed review evidence:

- Total review rows: 99,224.
- Distinct review_id values: 98,410.
- Duplicate rows by review_id: 814.
- Duplicate review_id values: 789.
- Duplicate review_id values associated with multiple order_id values: 789.
- Duplicate review_id values with multiple review_score values: 0.
- Maximum rows associated with one review_id: 3.
- Exact full-row duplicates were not observed.
- Composite review_id + order_id duplicate rows: 0.

The evidence indicates that review_id alone must not automatically be treated as a unique source-level row identifier for analytical modeling.

## EX-05 — Geolocation Boundary

The geolocation dataset contains 1,001,163 rows and 19,015 distinct geolocation_zip_code_prefix values.

The repeated zip-code prefixes mean the source cannot automatically be interpreted as a one-row-per-zip lookup table. Geographic modeling requires additional aggregation, representative-location, or other explicitly governed treatment.

No geolocation record is removed or collapsed in this area.

## EX-06 / EX-07 / EX-08 — Multi-Child Relationship Boundary

Observed source cardinalities demonstrate that an order may have multiple child records:

- Order items: maximum 21 records per order.
- Payments: maximum 29 records per order.
- Reviews: maximum 3 records per order.

Joining these child datasets directly to an order-level dataset can create row multiplication and distort additive measures.

Downstream analytical models must therefore preserve fact grain and define aggregation boundaries explicitly.

## EX-09 — Customer / Order Boundary

The acquired snapshot contains 99,441 customer records and 99,441 order records. The observed customer_id relationship has a maximum of one order per customer_id.

This observation must not be interpreted as a permanent business rule. Future modeling must preserve the distinction between observed snapshot cardinality and general business cardinality.

## Source Preservation Rule

- Source CSV files must remain unchanged.
- No exception is resolved by deleting source rows.
- No duplicate review records are removed during source profiling.
- No missing category translation is invented during source profiling.
- No geolocation rows are collapsed during source profiling.
- Exception treatment must occur only in a documented downstream transformation or modeling layer.

## Engineering Decision Boundary

This artifact identifies conditions requiring downstream engineering decisions. It does not decide the final warehouse implementation.

Potential downstream decisions include:

- Review fact grain and review-event identity.
- Handling of repeated review_id values.
- Category translation fallback behavior.
- Geolocation dimensional grain.
- Aggregation boundaries for order items, payments, and reviews.
- Late-arriving and incomplete relationship handling.

These decisions are deferred to the appropriate later modeling and transformation areas.

## Assumptions

- The observations are based on the locally acquired source snapshot.
- Source-level identifiers retain their original representations.
- Observed cardinalities describe this dataset snapshot only.
- An exception is not automatically considered a data error.

## Unknowns

- The original source-system business rationale for repeated review_id values is unknown.
- The intended business interpretation of the 13 unmatched category translations is unknown.
- The appropriate representative geographic record for repeated zip-code prefixes is not established.
- Future source snapshots may have different cardinalities or exceptions.

## Physical Modeling Boundary

This artifact does not define warehouse tables, surrogate keys, fact grain, dimensions, SCD implementation, indexes, partitioning, clustering, or BI models. It records source exceptions that must be considered when those designs are created.

## Artifact Completion Criteria

- [x] Source relationship exceptions documented
- [x] Unmatched category translation exception documented
- [x] Review identifier exception documented
- [x] Review composite-key validation documented
- [x] Geolocation boundary documented
- [x] Multi-child relationship risks documented
- [x] Customer/order snapshot boundary documented
- [x] Source preservation rule documented
- [x] Engineering decision boundary documented
- [x] Assumptions documented
- [x] Unknowns documented
- [x] Physical modeling boundary documented

