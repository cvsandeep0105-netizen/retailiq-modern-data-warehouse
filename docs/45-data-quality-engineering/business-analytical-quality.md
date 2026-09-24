# Area 45.3 — Business & Analytical Quality

Status: Accepted & Frozen

## 1. Purpose
Define production-grade business and analytical data-quality controls for RetailIQ, ensuring that structurally valid data also remains analytically meaningful, correctly aggregated, reconciled, and fit for governed business use.

## 2. Area 45.2 Dependency
Business and analytical quality shall operate on structurally validated datasets and preserve all structural and schema controls established in Area 45.2.

## 3. Area 45.1 Dependency
Business and analytical quality shall implement the Data Quality Engineering foundation established in Area 45.1.

## 4. Area 44 Dependency
BI-ready metrics, KPIs, dimensions, datasets, contracts, quality controls, and consumption boundaries shall remain protected.

## 5. Area 43 Dependency
Analytical SQL and Advanced Business Analysis shall remain protected against incorrect grain, population, joins, calculations, interpretation, and aggregation.

## 6. Area 42 Dependency
Semantic and business-layer definitions shall remain authoritative for governed business meaning.

## 7. Area 41 Dependency
Business metrics and KPIs shall remain aligned with approved formulas, populations, targets, thresholds, periods, and directionality.

## 8. Area 40 Dependency
Business Data Marts shall remain the primary analytical serving boundary for business-quality reconciliation.

## 9. Area 39 Dependency
Data Mart architecture shall define approved analytical grain, fact, dimension, measure, and business-logic boundaries.

## 10. Area 38 Dependency
Business-quality validation shall respect the approved transformation dependency graph.

## 11. Area 37 Dependency
Analytics engineering standards shall remain preserved for model contracts, tests, lineage, documentation, ownership, and controlled change.

## 12. Area 36 Dependency
Intermediate/Core transformations shall remain subject to business-rule and analytical correctness controls.

## 13. Area 35 Dependency
Incremental model results shall preserve business identity, merge semantics, idempotency, and reconciliation.

## 14. Area 34 Dependency
Full-refresh and incremental processing shall preserve equivalent analytical meaning.

## 15. Area 33 Dependency
ELT transformations shall preserve approved business semantics across layers.

## 16. Area 32 Dependency
Historical and late-arriving records shall preserve business-effective temporal meaning.

## 17. Area 31 Dependency
SCD history shall preserve valid business attribute versions and temporal context.

## 18. Area 30 Dependency
Conformed and role-playing dimensions shall preserve consistent analytical meaning.

## 19. Area 29 Dependency
Fact grain and measure design shall remain the primary analytical-quality boundaries.

## 20. Area 28 Dependency
Fact architecture shall remain analytically valid.

## 21. Area 27 Dependency
Dimension architecture shall remain analytically valid.

## 22. Area 26 Dependency
Natural and surrogate key semantics shall remain consistent with analytical identity.

## 23. Area 25 Dependency
Business grain shall remain an explicit analytical quality invariant.

## 24. Area 24 Dependency
Dimensional-modeling principles shall remain preserved.

## 25. Area 23 Dependency
Profiling baselines shall provide analytical expectations and anomaly context.

## 26. Area 22 Dependency
Reconciliation controls shall remain the core evidence boundary for analytical correctness.

## 27. Area 21 Dependency
Duplicate and record-resolution boundaries shall remain preserved.

## 28. Area 20 Dependency
Standardized and normalized values shall remain the upstream analytical foundation.

## 29. Business Quality Definition
Business quality evaluates whether structurally valid data correctly represents the approved business concepts, rules, measures, populations, relationships, time context, and analytical outcomes.

## 30. Analytical Quality Definition
Analytical quality evaluates whether data produces correct results at the declared grain using approved populations, joins, aggregations, calculations, dimensions, time semantics, and business definitions.

## 31. Fitness-for-Analysis
Analytical data shall be evaluated against the specific question, consumer, grain, population, metric, and decision context for which it is intended.

## 32. Business Rule Validation
Approved business rules shall be explicitly tested rather than assumed from technically valid records.

## 33. Order Business Rules
Order lifecycle, status, purchase, approval, delivery, cancellation, and fulfillment semantics shall remain consistent with approved definitions.

## 34. Customer Business Rules
Customer-level analysis shall preserve customer identity, order relationships, purchase behavior, geography, and historical context.

## 35. Product Business Rules
Product analysis shall preserve product identity, category, item relationships, pricing, and product-level analytical boundaries.

## 36. Seller Business Rules
Seller analysis shall preserve seller identity, seller geography, product relationships, order-item relationships, and fulfillment context.

## 37. Payment Business Rules
Payment analysis shall preserve payment identity, payment type, installment semantics, payment amount, and order relationships.

## 38. Review Business Rules
Review analysis shall preserve review identity, score, creation and response timing, order relationship, and documented multiplicity.

## 39. Fulfillment Business Rules
Delivery and fulfillment analysis shall preserve event ordering, delivery intervals, estimated dates, and valid temporal relationships.

## 40. Geography Business Rules
Customer and seller geography shall remain distinct analytical roles and shall not be incorrectly combined.

## 41. Category Business Rules
Product categories shall preserve source meaning and approved translation boundaries.

## 42. Metric Definition Quality
Every material metric shall be validated against its approved business definition, formula, grain, population, aggregation type, dimensional compatibility, and time basis.

## 43. KPI Definition Quality
Every material KPI shall be validated against numerator, denominator, target, threshold, directionality, period, population, and dimensional context.

## 44. Measure Grain
Measures shall be calculated at the correct declared grain before aggregation to higher analytical levels.

## 45. Additivity
Measures shall be validated for additive, semi-additive, non-additive, ratio, distinct-count, duration, and score behavior.

## 46. Distinct Count Quality
Distinct counts shall identify the correct business entity and shall not be inflated by lower-grain joins.

## 47. Ratio Quality
Ratios shall use compatible numerator and denominator populations and shall explicitly handle zero or missing denominators.

## 48. Average Quality
Averages shall preserve the correct numerator population, denominator population, grain, and weighting behavior.

## 49. Duration Quality
Duration measures shall use approved start and end events, units, temporal population, and valid interval semantics.

## 50. GMV Quality Boundary
GMV shall use its approved governed definition and shall not be silently substituted with payment_value or another measure.

## 51. Payment Value Quality Boundary
payment_value shall preserve payment semantics and shall not be interpreted as sales-item value without an explicit approved definition.

## 52. Sales Value Quality
Sales-item value shall preserve item-level pricing and quantity/grain semantics defined by the approved model.

## 53. Freight Quality
Freight value shall remain analytically distinct from sales-item value and payment value unless an approved metric explicitly combines them.

## 54. Order Count Quality
Order counts shall use order-level identity and shall not be multiplied by item, payment, or review joins.

## 55. Order Item Count Quality
Order-item counts shall use the declared (order_id, order_item_id) identity.

## 56. Customer Count Quality
Customer counts shall use the approved customer analytical identity and shall preserve the declared population.

## 57. Product Count Quality
Product counts shall use product-level identity and shall not be multiplied by seller, item, or order relationships.

## 58. Seller Count Quality
Seller counts shall use seller-level identity and shall not be multiplied by item or order relationships.

## 59. Review Count Quality
Review counts shall preserve the (review_id, order_id) identity boundary.

## 60. Population Quality
Every analytical result shall have an explicit population definition.

## 61. Inclusion Rules
Inclusion criteria shall be documented and consistently applied.

## 62. Exclusion Rules
Exclusions shall be explicit, justified, and consistent with the governed business definition.

## 63. Status Filtering
Lifecycle status filters shall use approved business semantics and shall not silently change metric populations.

## 64. Time-Basis Quality
Metrics shall identify whether time is based on purchase, approval, shipment, delivery, review, payment, or another governed business event.

## 65. Period Quality
Period boundaries shall be consistent across daily, weekly, monthly, quarterly, yearly, cohort, and comparative analysis.

## 66. Incomplete Period Quality
Incomplete periods shall be identified and shall not be compared as complete periods without an approved analytical treatment.

## 67. Historical Quality
Historical analytical results shall preserve the correct dimension version and business-effective context.

## 68. Late-Arriving Quality
Late-arriving facts and dimensions shall be incorporated without silently changing historical meaning.

## 69. Temporal Ordering
Business events shall respect valid chronological relationships where the source and business process require ordering.

## 70. Temporal Anomaly
Impossible or contradictory event sequences shall be detected and classified.

## 71. Join Quality
Analytical joins shall be validated for keys, cardinality, intended grain, population effects, and business meaning.

## 72. Join Multiplication
One-to-many and many-to-many relationships shall be tested for unintended row multiplication.

## 73. Many-to-Many Quality
Many-to-many relationships shall use explicit bridges, controlled pre-aggregation, or another governed strategy.

## 74. Double-Counting Prevention
Parent-level measures shall not be multiplied by child-level records.

## 75. Cross-Domain Quality
Cross-domain analysis shall combine domains only when their grains, populations, relationships, and business meanings are compatible.

## 76. Customer-Product Quality
Customer-product analysis shall prevent item, order, and customer grain from being mixed without explicit aggregation.

## 77. Customer-Seller Quality
Customer-seller analysis shall preserve order-item and seller relationships without multiplying customer-level measures.

## 78. Product-Seller Quality
Product-seller analysis shall preserve item-level and product-level grain boundaries.

## 79. Order-Payment Quality
Order-level payment analysis shall account for multiple payment records per order.

## 80. Order-Review Quality
Order-level review analysis shall account for multiple review records per order.

## 81. Order-Item Quality
Order-item analysis shall account for multiple items per order.

## 82. Known Item Multiplicity
Quality controls shall preserve the observed maximum of 21 order items per order.

## 83. Known Payment Multiplicity
Quality controls shall preserve the observed maximum of 29 payment records per order.

## 84. Known Review Multiplicity
Quality controls shall preserve the observed maximum of 3 review records per order.

## 85. Review Identity
Review quality shall use (review_id, order_id) where review identity is required because review_id alone is not unique.

## 86. Category Translation Quality
The 13 unmatched non-null product-category translation values shall remain explicitly identified and shall not receive invented translations.

## 87. Null Analytical Semantics
NULL shall remain distinct from zero, unknown, unavailable, and not-applicable values.

## 88. Zero Denominator
Analytical calculations shall define behavior for zero denominators rather than producing uncontrolled errors or misleading results.

## 89. Missing Period
Missing analytical periods shall be distinguished from periods with a measured zero.

## 90. Outlier Quality
Potential outliers shall be investigated against business context and shall not be removed merely because they appear unusual.

## 91. Anomaly Quality
Anomalies shall be classified using evidence and shall not automatically be treated as data errors.

## 92. Reconciliation Framework
Business and analytical outputs shall reconcile across equivalent populations and definitions.

## 93. Population Reconciliation
Equivalent populations shall reconcile between upstream and downstream analytical layers.

## 94. Count Reconciliation
Equivalent order, item, customer, product, seller, payment, and review counts shall reconcile where grain and population are identical.

## 95. Measure Reconciliation
Equivalent sales, freight, payment, delivery, and review measures shall reconcile under identical definitions and populations.

## 96. KPI Reconciliation
KPI results shall reconcile to governed metric and semantic definitions.

## 97. Dimensional Reconciliation
Aggregations by customer, product, seller, geography, category, status, and date shall preserve compatible populations and grain.

## 98. Time Reconciliation
Period totals shall reconcile to lower-grain records when equivalent time definitions are used.

## 99. Cross-Domain Reconciliation
Cross-domain analytical outputs shall reconcile each contributing domain before combined interpretation.

## 100. Regression Quality
Business and analytical quality results shall be compared against approved baselines and expected changes.

## 101. Idempotency Quality
Repeated processing of unchanged inputs shall preserve equivalent analytical results.

## 102. Reproducibility Quality
Analytical results shall be reproducible from the same governed definitions, inputs, model versions, filters, and execution context.

## 103. Exception Classification
Business and analytical exceptions shall be classified as rule, population, metric, KPI, grain, join, temporal, reconciliation, multiplicity, or interpretation exceptions as appropriate.

## 104. Critical Analytical Failure
Failures that materially change business interpretation or certified metrics shall be capable of blocking publication.

## 105. Remediation
Analytical defects shall be corrected at the appropriate model, transformation, metric, or business-rule layer rather than by modifying source records.

## 106. Quality Evidence
Analytical quality evidence shall retain rule, population, grain, expected result, observed result, affected scope, execution context, and status.

## 107. Lineage
Business and analytical quality results shall remain traceable to metrics, models, transformations, and sources.

## 108. Documentation
Every material business-quality rule shall document its business purpose, calculation boundary, expected condition, owner, severity, and remediation.

## 109. Ownership
Business and technical owners shall remain accountable for analytical definitions and quality outcomes.

## 110. Consumer Protection
Business and analytical quality controls shall protect semantic models, dashboards, reports, analytical SQL, exports, and self-service consumers.

## 111. Security
Analytical quality evidence shall respect approved access and sensitive-data controls.

## 112. Observability
Business-quality failures, metric drift, KPI drift, population changes, reconciliation failures, and analytical anomalies shall be observable.

## 113. CI/CD Integration
Business and analytical quality rules shall be suitable for automated validation in controlled engineering workflows.

## 114. Change Impact
Changes to business rules, metrics, KPIs, dimensions, facts, joins, populations, or analytical definitions shall undergo impact assessment.

## 115. Source Preservation
Business and analytical quality processing shall never modify, delete, overwrite, or mutate original source records.

## 116. Technology-Neutral Boundary
These business and analytical quality controls define logical expectations independently of a specific database, warehouse, orchestration, testing, or BI technology.

## 117. Acceptance Criteria
Area 45.3 is accepted when business rules, domain-specific rules, metric and KPI definitions, grain, additivity, distinct counts, ratios, averages, durations, GMV, payment, sales, freight, entity counts, populations, inclusion and exclusion rules, status filters, time basis, periods, historical and late-arriving semantics, temporal ordering, joins, many-to-many relationships, double-counting, cross-domain analysis, known multiplicity, review identity, category translation, null and zero semantics, anomalies, reconciliation, regression, idempotency, reproducibility, exceptions, remediation, evidence, lineage, documentation, ownership, consumer protection, security, observability, CI/CD, change impact, source preservation, and technology-neutral boundaries are explicitly documented and validated.

