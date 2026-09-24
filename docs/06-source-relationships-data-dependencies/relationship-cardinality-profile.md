# Relationship Cardinality & Key Profile

## Document Status
- Status: Accepted for Area 06.3
- Evidence Basis: Local Olist source data
- Scope: Source key uniqueness, composite-key uniqueness, and observed relationship cardinality

## Key Uniqueness Findings
| Source Entity | Key | Duplicate Rows | Interpretation |
|---|---|---:|---|
| Customer | customer_id | 0 | Unique in source |
| Order | order_id | 0 | Unique in source |
| Product | product_id | 0 | Unique in source |
| Seller | seller_id | 0 | Unique in source |
| Review | review_id | 814 | Not unique in source |
| Order Item | order_id + order_item_id | 0 | Unique composite key |
| Payment | order_id + payment_sequential | 0 | Unique composite key |
| Category Translation | product_category_name | 0 | Unique in source |
| Review | review_id + order_id | 0 | Unique composite key |

## Review Key Finding
The source review dataset contains 99,224 rows and 98,410 distinct review_id values. There are 814 duplicate rows when review_id is evaluated alone, affecting 789 review_id values. Exact duplicate rows are zero.

Further investigation established that all 789 duplicated review_id values occur across multiple order_id values, while no duplicated review_id has multiple review_score values. The maximum number of source rows for one review_id is three.

The composite key review_id + order_id has zero duplicate rows and exactly 99,224 distinct pairs across 99,224 review rows.

Therefore review_id must not be treated as a standalone source primary key. The source relationship evidence supports review_id + order_id as the observed unique composite key.

## Observed Cardinality
| Relationship | Observed Maximum | Additional Evidence |
|---|---:|---|
| Customer → Orders by customer_id | 1 | 0 customers with more than one order |
| Order → Order Items | 21 | 9,803 orders have more than one item |
| Order → Payments | 29 | 2,961 orders have more than one payment |
| Order → Reviews | 3 | 547 orders have more than one review row |
| Seller → Distinct Products represented in order items | 399 | 3,095 sellers represented in order items |

## Interpretation Boundary
Observed cardinalities describe the physical source data and are not yet warehouse dimensional-model decisions.

The customer_id relationship is a physical source relationship. The presence of customer_unique_id requires separate analytical interpretation before customer grain is finalized.

Multiple order items, payments, and reviews must not be collapsed into a single order-level record without explicit aggregation rules.

## Assumptions
- Source keys are interpreted from observed physical values only.
- No source rows were modified during profiling.
- Cardinality results represent the acquired Olist dataset version used for this project.

## Unknowns
- Final warehouse surrogate-key strategy is deferred to the modeling phase.
- Final fact grain is deferred to Areas 24–32.
- Review business semantics and historical treatment require downstream modeling decisions.

## Physical Modeling Boundary
This artifact records source-level uniqueness and cardinality evidence only. It does not establish the final warehouse schema, fact grain, dimension grain, surrogate keys, or SCD strategy.

## Artifact Completion Criteria
- [x] Source key uniqueness assessed
- [x] Composite-key uniqueness assessed
- [x] Review duplicate behavior investigated
- [x] Review composite key validated
- [x] Relationship cardinalities measured
- [x] Interpretation boundaries documented
- [x] Assumptions documented
- [x] Unknowns documented
- [x] Physical modeling boundary documented
