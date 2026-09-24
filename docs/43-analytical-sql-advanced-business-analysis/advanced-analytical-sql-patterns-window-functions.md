# Area 43.2 — Advanced Analytical SQL Patterns & Window Functions

Status: Accepted & Frozen

## 1. Purpose
Define governed advanced analytical SQL patterns for RetailIQ, including window functions, ranking, period comparison, rolling analysis, contribution analysis, conditional aggregation, distinct-count analysis, cohort analysis, and business segmentation.

## 2. Area 43.1 Dependency
This artifact extends the Analytical SQL and Business Analysis Foundation defined in Area 43.1.

## 3. Area 42 Dependency
Advanced analytical SQL shall consume the approved Semantic / Business Layer and preserve governed entities, dimensions, measures, KPIs, relationships, filters, and aggregation semantics.

## 4. Area 41 Dependency
Advanced calculations shall reuse governed metric and KPI definitions rather than silently redefining business formulas.

## 5. Area 40 Dependency
Queries shall consume approved Business Data Marts and preserve their declared grains.

## 6. Area 39 Dependency
Analytical patterns shall preserve approved data-mart composition, measure boundaries, and double-counting controls.

## 7. Area 38 Dependency
Query dependencies shall follow the approved transformation dependency graph.

## 8. Area 37 Dependency
Analytical models and SQL artifacts shall follow approved analytics engineering standards.

## 9. Area 36 Dependency
Reusable transformations shall remain upstream where appropriate and shall not be unnecessarily duplicated inside analytical queries.

## 10. Area 35 Dependency
Advanced analytical consumption shall remain compatible with incremental model identity and change-processing semantics.

## 11. Area 34 Dependency
Analytical queries shall respect approved full-refresh and incremental processing boundaries.

## 12. Area 33 Dependency
Analytical SQL shall consume the approved ELT layers rather than bypassing governed transformation responsibilities.

## 13. Area 32 Dependency
Historical and late-arriving data shall preserve approved temporal semantics.

## 14. Area 31 Dependency
Queries involving historical dimensions shall respect approved SCD versioning and effective-date controls.

## 15. Area 30 Dependency
Conformed and role-playing dimensions shall be used according to their approved analytical roles.

## 16. Area 29 Dependency
Window calculations and aggregations shall preserve approved fact grain and measure semantics.

## 17. Area 28 Dependency
Advanced analysis shall respect approved fact architecture.

## 18. Area 27 Dependency
Dimension attributes shall be consumed according to approved dimension architecture.

## 19. Area 26 Dependency
Joins shall preserve approved natural-key and surrogate-key semantics.

## 20. Area 25 Dependency
Every analytical calculation shall explicitly preserve its declared business grain.

## 21. Area 24 Dependency
Analytical patterns shall remain consistent with the approved dimensional model.

## 22. Area 23 Dependency
Analytical outputs shall remain compatible with profiling baselines.

## 23. Area 22 Dependency
Analytical results shall support approved reconciliation controls.

## 24. Area 21 Dependency
Duplicate and record-resolution boundaries shall be preserved.

## 25. Area 20 Dependency
Advanced SQL shall consume standardized and normalized analytical data.

## 26. Window Function Purpose
Window functions shall calculate analytical context without unintentionally changing the underlying row grain.

## 27. PARTITION BY
Partitioning shall define the business population within which a window calculation operates.

## 28. ORDER BY in Windows
Window ordering shall be deterministic and shall use business-relevant ordering columns.

## 29. Window Frame
Window frames shall explicitly define the rows or range included in calculations when default database behavior could produce ambiguity.

## 30. ROW_NUMBER
ROW_NUMBER shall be used for deterministic sequencing, latest-record selection, controlled deduplication, and business ranking where unique ordering is required.

## 31. RANK
RANK shall be used when tied observations should share the same ranking position and subsequent positions may contain gaps.

## 32. DENSE_RANK
DENSE_RANK shall be used when tied observations share ranking positions without gaps in subsequent rank values.

## 33. Tie Handling
Every ranking analysis shall define how ties are handled and whether deterministic secondary ordering is required.

## 34. LAG
LAG shall support prior-period, prior-event, prior-order, and sequential comparison analysis where the ordering context is explicitly defined.

## 35. LEAD
LEAD shall support next-period, next-event, or future-state analysis where the business sequence is explicitly defined.

## 36. Running Totals
Running totals shall use deterministic ordering and an explicit frame to prevent unintended accumulation behavior.

## 37. Rolling Windows
Rolling calculations shall define window size, time basis, minimum observations, and treatment of missing periods.

## 38. Moving Average
Moving averages shall define numerator population, observation window, denominator behavior, and missing-period treatment.

## 39. Cumulative Contribution
Cumulative contribution analysis shall preserve the approved metric grain and denominator population.

## 40. Percent of Total
Percent-of-total calculations shall define numerator, denominator, partition context, and zero-denominator behavior.

## 41. Share of Category
Category-share analysis shall ensure numerator and denominator use compatible product, order-item, or sales grains.

## 42. Conditional Aggregation
Conditional aggregation shall use explicit business conditions and shall prevent incompatible populations from being combined.

## 43. Distinct Counts
Distinct-count analysis shall identify the business entity being counted and shall prevent lower-grain joins from inflating entity counts.

## 44. Conditional Distinct Counts
Conditional distinct counts shall document the condition, entity key, population, and dimensional context.

## 45. Ratio Calculations
Ratios shall use compatible numerator and denominator populations and shall explicitly handle zero or null denominators.

## 46. Percentage Calculations
Percentage calculations shall define units, numerator, denominator, rounding, and population scope.

## 47. Period-over-Period
Period-over-period analysis shall define current and comparison periods using a consistent governed date basis.

## 48. Year-over-Year
Year-over-year analysis shall compare compatible periods and shall document incomplete-period behavior.

## 49. Month-over-Month
Month-over-month analysis shall use consistent calendar boundaries and shall distinguish missing periods from zero activity.

## 50. Period Change
Absolute and percentage change shall be calculated separately and shall document denominator-zero behavior.

## 51. Top-N
Top-N analysis shall define ranking population, metric, N, dimensional scope, time period, and tie handling.

## 52. Bottom-N
Bottom-N analysis shall use equivalent population and ranking controls while reversing the ordering direction.

## 53. Top-N by Group
Grouped Top-N analysis shall partition the ranking by the approved business dimension before selecting the requested N.

## 54. Customer Ranking
Customer ranking shall preserve customer grain and use approved customer-related measures.

## 55. Product Ranking
Product ranking shall preserve product grain and shall distinguish product measures from item-level event counts.

## 56. Seller Ranking
Seller ranking shall preserve seller grain and shall distinguish seller measures from order-item and fulfillment event counts.

## 57. Order Analysis
Order-level analysis shall preserve one-row-per-order semantics where the selected mart or model declares order grain.

## 58. Order-Item Analysis
Order-item analysis shall preserve the composite order-item identity (order_id, order_item_id).

## 59. Payment Analysis
Payment analysis shall preserve payment-event grain and shall not interpret payment rows as orders without controlled aggregation.

## 60. Review Analysis
Review analysis shall preserve the documented review identity boundary because review_id alone is not unique.

## 61. Review Identity Control
The approved review identity boundary is (review_id, order_id); analytical queries shall not assume review_id alone is a unique business key.

## 62. Multi-Item Order Control
Order-level analysis shall account for orders containing multiple items; the observed source boundary permits up to 21 items per order.

## 63. Multi-Payment Order Control
Order-level payment analysis shall account for multiple payment rows; the observed source boundary permits up to 29 payments per order.

## 64. Multi-Review Order Control
Order-level review analysis shall account for multiple reviews; the observed source boundary permits up to 3 reviews per order.

## 65. Many-to-Many Protection
Queries combining multiple child-grain datasets shall aggregate each child population to the intended parent grain before combining measures.

## 66. Double-Counting Prevention
Analytical SQL shall prevent measure multiplication caused by joining multiple one-to-many or many-to-many relationships at incompatible grains.

## 67. Grain Transition
Every intentional grain transition shall be documented before aggregation or window calculation.

## 68. Pre-Aggregation
Child-level measures shall be pre-aggregated when required to preserve parent-level analytical correctness.

## 69. Conditional Business Logic
CASE expressions shall use governed business definitions and shall document classification boundaries.

## 70. NULL Semantics
NULL shall not automatically be interpreted as zero, unknown, not-applicable, or absence of an event.

## 71. Zero Denominator
Division-by-zero shall be explicitly prevented and the resulting semantic treatment shall be documented.

## 72. Missing Data
Missing observations shall be distinguished from true zero values and from unavailable source information.

## 73. Cohort Construction
Cohort assignment shall use a clearly defined qualifying event, cohort period, and entity population.

## 74. Retention Analysis
Retention analysis shall define the retained population, observation periods, qualifying activity, and denominator.

## 75. Frequency Analysis
Frequency calculations shall define the event, entity, period, and aggregation grain.

## 76. Customer Value Analysis
Customer value analysis shall reuse governed sales, payment, order, or other approved measures and shall not invent unsupported financial semantics.

## 77. Delivery Analysis
Delivery analysis shall use approved delivery and estimated-delivery measures and shall explicitly define eligible orders.

## 78. Review Analysis Patterns
Review-score analysis may include averages, distributions, counts, dimensional comparisons, and time trends while preserving the approved review population.

## 79. Product Category Analysis
Category analysis shall preserve source category values and shall not fabricate English translations for the 13 unmatched non-null product-category values identified during source profiling.

## 80. Geographic Analysis
Geographic analysis shall define whether geography represents customer location, seller location, or another approved role.

## 81. Analytical SQL Layering
Complex analysis shall be decomposed into readable stages such as population selection, normalization, aggregation, window calculation, ranking, and final presentation.

## 82. CTE Usage
Common Table Expressions may be used to make analytical stages explicit, improve readability, and isolate grain transitions.

## 83. Reusable Analytical Logic
Repeated governed business logic should be implemented in approved upstream models or semantic definitions when appropriate rather than copied across queries.

## 84. Query Safety
Analytical queries shall avoid accidental Cartesian joins, uncontrolled row multiplication, unbounded scans, ambiguous grouping, and unsafe dynamic filtering.

## 85. Performance
Performance review shall consider predicate selectivity, join cardinality, aggregation strategy, window partitions, sorting, repeated scans, and reusable analytical structures.

## 86. Regression Testing
Advanced SQL changes shall be tested against approved expected results, population checks, grain checks, and reconciliation controls.

## 87. Reconciliation
Analytical outputs shall reconcile to governed metric and KPI values where the same population and dimensional context are used.

## 88. Lineage
Analytical SQL shall preserve traceability from the analytical result through semantic objects, marts, models, and approved upstream dependencies.

## 89. Documentation
Each advanced analytical pattern shall document purpose, input grain, output grain, population, calculation, filters, joins, ordering, window frame, assumptions, and interpretation.

## 90. BI Boundary
Analytical SQL may prepare governed analytical datasets for BI consumption but shall not silently replace the semantic/business layer.

## 91. Source Preservation
Analytical SQL shall never mutate or overwrite original source records.

## 92. Technology-Neutral Boundary
These analytical SQL patterns define logical behavior and are not tied to a specific warehouse or BI vendor.

## 93. Acceptance Criteria
Area 43.2 is accepted when advanced analytical SQL patterns, window functions, ranking, tie handling, period comparison, rolling calculations, contribution analysis, conditional aggregation, distinct counts, ratios, segmentation, cohort analysis, entity-specific analysis, grain transitions, many-to-many protection, double-counting prevention, null and denominator handling, query safety, performance, reconciliation, regression, lineage, documentation, BI boundaries, source preservation, and technology-neutral controls are explicitly documented and validated.

