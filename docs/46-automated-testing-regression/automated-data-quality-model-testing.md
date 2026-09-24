# Area 46.3 — Automated Data Quality & Model Testing

Status: Accepted & Frozen

## 1. Purpose
Define automated validation for data quality rules, warehouse models, dimensions, facts, business marts, metrics, KPIs, relationships, grain, transformations, and analytical correctness.

## 2. Area 46.2 Dependency
Testing shall follow the test architecture, test types, coverage strategy, execution boundaries, and regression principles established in Area 46.2.

## 3. Area 46.1 Dependency
All model and data-quality tests shall preserve the automated testing and regression foundation.

## 4. Area 45 Dependency
Automated tests shall operationalize the approved Data Quality Engineering controls from Area 45.

## 5. Area 44 Dependency
BI-ready data products shall be protected by automated model and data-quality validation.

## 6. Area 43 Dependency
Analytical SQL results shall be validated for correctness, grain, aggregation, and business meaning.

## 7. Area 42 Dependency
Semantic-layer objects shall be validated against governed definitions.

## 8. Area 41 Dependency
Metrics and KPIs shall be automatically validated against approved definitions.

## 9. Area 40 Dependency
Business data marts shall have automated structural and analytical tests.

## 10. Area 39 Dependency
Data mart architecture shall determine applicable model tests.

## 11. Area 38 Dependency
Transformation dependency order shall determine test execution dependencies.

## 12. Area 37 Dependency
Analytics engineering models shall remain automatically testable.

## 13. Area 36 Dependency
Intermediate and core transformations shall have automated validation.

## 14. Area 35 Dependency
Incremental models shall be tested for incremental correctness and idempotency.

## 15. Area 34 Dependency
Full-refresh and incremental behavior shall have separate validation expectations.

## 16. Area 33 Dependency
ELT architecture boundaries shall remain testable.

## 17. Area 32 Dependency
Historical and late-arriving records shall be covered by automated tests.

## 18. Area 31 Dependency
SCD versioning and effective-dating behavior shall be automatically validated.

## 19. Area 30 Dependency
Conformed and role-playing dimensions shall have relationship and consistency tests.

## 20. Area 29 Dependency
Fact grain and measures shall have automated correctness tests.

## 21. Area 28 Dependency
Fact architecture shall have structural and relationship tests.

## 22. Area 27 Dependency
Dimension architecture shall have identity and relationship tests.

## 23. Area 26 Dependency
Natural and surrogate keys shall have automated uniqueness and identity tests.

## 24. Area 25 Dependency
Business grain shall remain a mandatory automated test invariant.

## 25. Area 24 Dependency
Dimensional-modeling behavior shall be covered by model tests.

## 26. Area 23 Dependency
Profiling baselines shall provide evidence for automated validation.

## 27. Area 22 Dependency
Reconciliation rules shall be represented in automated testing where deterministic.

## 28. Area 21 Dependency
Deduplication and record-resolution rules shall be automatically validated.

## 29. Area 20 Dependency
Standardization and normalization rules shall have automated tests.

## 30. Schema Tests
Automated schema tests shall validate required columns, unexpected columns, data types, nullability, precision, and approved schema evolution.

## 31. Column Tests
Critical columns shall have explicit validation for expected presence, type, meaning, and allowable nullability.

## 32. Nullability Tests
Required fields shall be tested for unexpected nulls while intentionally nullable fields shall not be incorrectly rejected.

## 33. Domain Tests
Categorical fields shall be tested against approved business and source domains.

## 34. Range Tests
Numeric, date, timestamp, and measurable attributes shall be tested against appropriate valid ranges.

## 35. Uniqueness Tests
Unique keys shall be tested according to their approved identity definitions.

## 36. Composite-Key Tests
Composite identities shall be tested as complete combinations rather than incorrectly testing individual columns in isolation.

## 37. Referential-Integrity Tests
Required parent-child relationships shall be automatically tested for orphan records.

## 38. Cardinality Tests
Expected relationship cardinality and known multiplicity boundaries shall be validated.

## 39. Grain Tests
Each model shall have automated validation for its declared grain.

## 40. Row-Count Tests
Material unexpected row-count changes shall be detectable against approved expectations or baselines.

## 41. Completeness Tests
Required populations, periods, entities, and records shall be tested for expected completeness.

## 42. Freshness Tests
Data availability shall be tested against governed freshness expectations where applicable.

## 43. Temporal Tests
Date and timestamp relationships shall be tested for valid ordering and business meaning.

## 44. Transformation Tests
Transformation logic shall be tested against representative expected outputs.

## 45. Standardization Tests
Standardized values, formats, categories, and normalization rules shall be automatically validated.

## 46. Deduplication Tests
Duplicate resolution shall be tested without removing legitimate business multiplicity.

## 47. Record-Resolution Tests
Identity resolution and survivorship rules shall be tested against deterministic expected behavior.

## 48. Dimension Tests
Dimension keys, attributes, uniqueness, relationships, effective dates, and historical behavior shall be validated.

## 49. Fact Tests
Fact keys, grain, foreign keys, measures, and additive behavior shall be validated.

## 50. Measure Tests
Measures shall be tested for correct calculation, population, grain, sign, units, and aggregation behavior.

## 51. Additivity Tests
Measures shall be tested for additive, semi-additive, or non-additive behavior according to their approved definition.

## 52. Distinct-Count Tests
Distinct-count metrics shall be tested to prevent accidental duplication caused by joins.

## 53. Ratio Tests
Ratios shall be tested for correct numerator, denominator, population, and zero-denominator handling.

## 54. Average Tests
Averages shall be tested against the correct population and aggregation grain.

## 55. Duration Tests
Delivery, processing, and other duration metrics shall be tested for valid temporal boundaries.

## 56. KPI Tests
KPIs shall be tested for numerator, denominator, population, period, and approved calculation definition.

## 57. Business-Rule Tests
Material business rules shall be automatically validated where deterministic evaluation is possible.

## 58. Status Tests
Order and other governed status values shall be validated against approved domains and business interpretation.

## 59. Customer Tests
Customer populations and customer-level measures shall be validated at their approved grain.

## 60. Product Tests
Product populations, categories, attributes, and product-level measures shall be validated.

## 61. Seller Tests
Seller identity, relationships, and seller-level measures shall be validated.

## 62. Payment Tests
Payment relationships, amounts, types, multiplicity, and payment-level measures shall be validated.

## 63. Review Tests
Review identity, scores, relationships, multiplicity, and review-level measures shall be validated.

## 64. Fulfillment Tests
Delivery and fulfillment timestamps, durations, estimates, and performance metrics shall be validated.

## 65. Geography Tests
Geographic attributes shall be validated without collapsing legitimate source-level geolocation multiplicity.

## 66. Category Tests
Product category relationships shall be tested while preserving the known 13 unmatched non-null translation values.

## 67. Known Review Identity Test
The approved review identity (review_id, order_id) shall be tested and review_id alone shall not be treated as universally unique.

## 68. Known Item Multiplicity Test
The observed maximum of 21 items per order shall remain a documented boundary rather than an automatic duplicate failure.

## 69. Known Payment Multiplicity Test
The observed maximum of 29 payment records per order shall remain a documented boundary.

## 70. Known Review Multiplicity Test
The observed maximum of 3 review records per order shall remain a documented boundary.

## 71. Category Translation Test
The 13 unmatched non-null product-category translation values shall remain visible as known exceptions and shall not receive fabricated translations.

## 72. Join Tests
Critical joins shall be tested for expected cardinality, population preservation, and accidental multiplication.

## 73. Double-Counting Tests
Automated tests shall detect measure multiplication caused by one-to-many and many-to-many joins.

## 74. Aggregation Tests
Aggregations shall be validated against approved lower-grain populations.

## 75. Mart Tests
Business marts shall be tested for model structure, grain, relationships, measures, dimensions, and consumer readiness.

## 76. Semantic Tests
Semantic objects shall be tested against governed metrics, dimensions, relationships, and business definitions.

## 77. BI-Ready Tests
BI-ready outputs shall be tested for schema, grain, completeness, metric correctness, and consumer usability.

## 78. Reconciliation Tests
Equivalent populations and measures shall be automatically reconciled where deterministic comparison is possible.

## 79. Regression Tests
Previously accepted results shall be protected against unintended changes.

## 80. Baseline Comparison
Approved baselines shall be used to detect material unexpected changes in population, distribution, measures, and quality.

## 81. Drift Tests
Material schema, distribution, relationship, business, metric, and KPI drift shall be detectable.

## 82. Incremental Tests
Incremental processing shall validate inserts, updates, late arrivals, overlap, duplicate prevention, and repeated execution.

## 83. Full-Refresh Tests
Full refresh shall validate completeness and consistency with equivalent approved inputs.

## 84. Idempotency Tests
Repeated execution shall not create unintended duplicates or inconsistent analytical results.

## 85. Historical Tests
Historical dimension and fact behavior shall preserve effective dates, versions, and business meaning.

## 86. Late-Arriving Tests
Late-arriving records shall be validated for correct historical integration.

## 87. Negative Tests
Invalid records shall produce the expected validation, rejection, quarantine, or exception behavior.

## 88. Exception Tests
Expected exceptions shall be classified correctly and shall not silently disappear.

## 89. Quality-Gate Tests
Blocking and non-blocking quality gates shall produce their approved outcomes.

## 90. Failure-Recovery Tests
Retry, recovery, reprocessing, and rollback behavior shall be tested where applicable.

## 91. Test Evidence
Automated test execution shall retain meaningful test name, scope, version, environment, timestamp, result, and failure evidence.

## 92. Failure Isolation
Failures shall identify the affected test, model, rule, dataset, or dependency without unnecessary changes to unrelated passing components.

## 93. Reproducibility
Material failures shall be reproducible using controlled inputs, code version, configuration, and environment.

## 94. Test Stability
Critical automated tests shall produce stable outcomes under equivalent conditions.

## 95. Flaky Test Management
Flaky tests shall be identified, investigated, corrected, quarantined under controlled policy, or replaced rather than ignored.

## 96. CI/CD Integration
Automated data-quality and model tests shall be executable within controlled CI/CD workflows.

## 97. Promotion Gate
Critical test failures shall prevent affected model or data-product promotion.

## 98. Certification Gate
Certified analytical products shall require applicable automated tests to pass.

## 99. No Silent Bypass
Critical tests shall not be silently disabled or skipped to obtain a passing state.

## 100. No Fabricated Results
Automated test evidence shall represent actual execution results.

## 101. Source Preservation
Testing shall never modify original source records.

## 102. Lineage
Material test failures shall remain traceable to the affected data product and transformation dependency.

## 103. Documentation
Tests shall document purpose, expected behavior, ownership, scope, limitations, and failure interpretation.

## 104. Security
Test execution and evidence shall follow governed access controls and minimize unnecessary sensitive-data exposure.

## 105. Consumer Protection
Materially invalid data shall not be certified as consumer-ready.

## 106. Technology-Neutral Boundary
These automated data-quality and model-testing requirements define logical behavior independently of a specific warehouse, testing framework, orchestration platform, or BI technology.

## 107. Acceptance Criteria
Area 46.3 is accepted when automated schema, column, nullability, domain, range, uniqueness, composite-key, referential, cardinality, grain, completeness, freshness, temporal, transformation, standardization, deduplication, identity, dimension, fact, measure, KPI, business-rule, domain, join, aggregation, reconciliation, regression, baseline, drift, incremental, full-refresh, idempotency, historical, negative, exception, quality-gate, recovery, evidence, failure-isolation, reproducibility, stability, CI/CD, promotion, certification, security, lineage, documentation, consumer-protection, source-preservation, and technology-neutral controls are explicitly validated.

## 108. Freeze Rule
After acceptance, Area 46.3 shall be frozen and changed only for a verified defect, dependency correction, or formally approved engineering change.

