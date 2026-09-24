# Area 44.2 — BI-Ready Dataset Structure, Consumption Models & Analytical Access Patterns

Status: Accepted & Frozen

## 1. Purpose
Define the logical structure, consumption models, access patterns, dimensional behavior, analytical usability, and governed serving boundaries for RetailIQ BI-ready datasets.

## 2. Area 44.1 Dependency
BI-ready dataset structures shall extend the approved BI-ready data product foundation.

## 3. Area 43 Dependency
Analytical access patterns shall consume approved Analytical SQL and Advanced Business Analysis outputs.

## 4. Area 42 Dependency
Dataset structures shall preserve the governed Semantic / Business Layer.

## 5. Area 41 Dependency
Exposed metrics and KPIs shall retain approved definitions.

## 6. Area 40 Dependency
BI-ready structures shall consume approved Business Data Marts.

## 7. Area 39 Dependency
Data-mart grain and composition shall remain preserved.

## 8. Area 38 Dependency
Dataset dependencies shall follow the approved transformation dependency graph.

## 9. Area 37 Dependency
Analytics engineering model standards shall govern dataset naming, contracts, testing, documentation, and lineage.

## 10. Area 36 Dependency
Reusable transformation responsibilities shall remain upstream of BI-serving structures.

## 11. Area 35 Dependency
Incremental model behavior shall remain compatible with BI-ready dataset refresh and consumption.

## 12. Area 34 Dependency
Full-refresh and incremental processing semantics shall remain preserved.

## 13. Area 33 Dependency
BI-ready datasets shall consume the approved ELT architecture.

## 14. Area 32 Dependency
Historical and late-arriving record behavior shall remain preserved.

## 15. Area 31 Dependency
SCD historical dimension semantics shall remain preserved.

## 16. Area 30 Dependency
Conformed and role-playing dimensions shall remain consistent across consumption models.

## 17. Area 29 Dependency
Fact grain and measure definitions shall remain unchanged.

## 18. Area 28 Dependency
Fact architecture shall remain the analytical foundation.

## 19. Area 27 Dependency
Dimension architecture shall remain the analytical foundation.

## 20. Area 26 Dependency
Key semantics shall remain traceable.

## 21. Area 25 Dependency
Each dataset shall declare its primary analytical grain.

## 22. Area 24 Dependency
Dimensional-modeling semantics shall remain preserved.

## 23. Area 23 Dependency
Profiling expectations shall remain available for validation.

## 24. Area 22 Dependency
Reconciliation controls shall remain applicable.

## 25. Area 21 Dependency
Duplicate and record-resolution boundaries shall remain preserved.

## 26. Area 20 Dependency
Standardized and normalized data shall remain the governed analytical input.

## 27. Dataset Serving Definition
A BI-ready dataset is a governed serving structure optimized for a defined analytical consumption pattern while preserving approved business definitions and grain.

## 28. Dataset Grain Declaration
Every BI-ready dataset shall declare exactly one primary output grain and identify any intentionally nested or secondary-grain structures.

## 29. Dataset Purpose
Each dataset shall identify the business questions and analytical workflows it is designed to support.

## 30. Consumer Model
Each dataset shall identify whether its primary consumers are dashboards, reports, analytical SQL users, semantic models, exports, or controlled self-service users.

## 31. Wide Analytical Dataset Boundary
A wide BI-ready dataset may combine commonly consumed dimensions and measures only when grain and measure compatibility are explicitly controlled.

## 32. Dimensional Consumption Model
Dimensional consumption shall preserve fact-to-dimension relationships and allow governed slicing, filtering, grouping, and aggregation.

## 33. Aggregate Consumption Model
Pre-aggregated datasets may be used where a stable business grain and reusable aggregation definition are established.

## 34. Detail Consumption Model
Detailed datasets may expose lower-grain analytical records where consumers require drill-down or investigation.

## 35. Summary Consumption Model
Summary datasets shall clearly document aggregation grain and shall not be mistaken for source-level detail.

## 36. Metric Consumption Model
Metric-serving structures shall expose governed measures and KPIs without redefining their business logic.

## 37. Time-Series Consumption
Time-series datasets shall provide governed date context and consistent period definitions.

## 38. Snapshot Consumption
Snapshot structures shall document snapshot date, business state, grain, and historical interpretation.

## 39. Historical Consumption
Historical datasets shall preserve approved SCD and effective-date semantics.

## 40. Current-State Consumption
Current-state datasets shall clearly identify current-record semantics and shall not be interpreted as historical versions.

## 41. Dashboard Access Pattern
Dashboard-serving datasets shall support predictable filtering, grouping, KPI retrieval, and commonly required dimensional slicing.

## 42. Reporting Access Pattern
Reporting datasets shall support repeatable business reporting with stable definitions and documented time context.

## 43. Drill-Down Access Pattern
Drill-down paths shall move from summary to lower-grain detail without changing business meaning.

## 44. Drill-Through Boundary
Drill-through datasets shall preserve relationships between the originating analytical context and detailed records.

## 45. Slice-and-Dice Pattern
Dimensional slicing shall use governed dimensions and shall not produce incompatible metric populations.

## 46. Filtering Pattern
Filters shall operate on governed attributes and shall document whether they apply before or after aggregation.

## 47. Grouping Pattern
Grouping shall preserve the declared analytical grain and shall not accidentally mix incompatible dimensions.

## 48. Sorting Pattern
Sorting shall be deterministic where ranking or reproducible presentation is required.

## 49. Ranking Access
Ranking datasets shall expose governed ranking measures and documented tie behavior where ranking is material.

## 50. Top-N Access
Top-N consumption shall preserve the approved population, metric, period, N, and tie semantics.

## 51. Period Comparison Access
Comparison datasets shall provide compatible current and comparison periods using governed date semantics.

## 52. Trend Access
Trend datasets shall preserve complete period definitions and distinguish missing periods from true zero activity.

## 53. Cohort Access
Cohort datasets shall expose cohort assignment, observation period, population, and approved retention or activity measures.

## 54. Customer Access
Customer-oriented datasets shall preserve customer grain and approved customer measures.

## 55. Product Access
Product-oriented datasets shall preserve product grain and distinguish product attributes from order-item measures.

## 56. Seller Access
Seller-oriented datasets shall preserve seller grain and distinguish seller measures from order-item and fulfillment events.

## 57. Order Access
Order-oriented datasets shall preserve order grain when order-level analysis is intended.

## 58. Order-Item Access
Order-item datasets shall preserve (order_id, order_item_id) identity.

## 59. Payment Access
Payment-oriented datasets shall preserve payment-event semantics and shall not treat payment rows as orders without governed aggregation.

## 60. Review Access
Review-oriented datasets shall preserve the approved (review_id, order_id) identity boundary.

## 61. Geography Access
Geographic access shall explicitly identify customer geography versus seller geography.

## 62. Category Access
Category access shall preserve source category values and shall not invent translations for unmatched categories.

## 63. Cross-Domain Dataset
Cross-domain datasets shall explicitly document each domain join, grain transition, population compatibility rule, and measure aggregation boundary.

## 64. Multi-Fact Dataset
Datasets combining multiple fact populations shall pre-aggregate or otherwise isolate each fact population before combining measures.

## 65. Many-to-Many Protection
BI-ready structures shall prevent uncontrolled many-to-many relationships from multiplying measures.

## 66. Double-Counting Protection
Dataset design shall prevent repeated order, item, payment, or review records from inflating unrelated measures.

## 67. Known Multiplicity — Items
The observed source boundary permits up to 21 order items per order; BI-ready structures shall preserve this fact and control order-level aggregation.

## 68. Known Multiplicity — Payments
The observed source boundary permits up to 29 payment records per order; payment measures shall be aggregated deliberately before order-level consumption.

## 69. Known Multiplicity — Reviews
The observed source boundary permits up to 3 review records per order; review measures shall be aggregated deliberately before order-level consumption.

## 70. Null Handling
Null, unknown, unavailable, and not-applicable values shall remain semantically distinct.

## 71. Zero Handling
Zero shall represent a valid zero value only where the business definition supports that interpretation.

## 72. Missing Period Handling
Missing time periods shall not automatically be converted into zero activity.

## 73. Unknown Member Handling
Unknown dimensional members shall use documented governed semantics.

## 74. Field Selection
Only fields required for supported analytical consumption should be exposed in a BI-ready dataset, subject to traceability and governance requirements.

## 75. Field Naming
Field names shall be consistent, business-readable, unambiguous, and traceable to approved technical definitions.

## 76. Field Documentation
Every exposed field shall have a documented business meaning, data type, grain, source or model lineage, and applicable quality constraints.

## 77. Measure Metadata
Measures shall document additivity, calculation, population, time basis, dimensional compatibility, and aggregation behavior.

## 78. Dimension Metadata
Dimensions shall document hierarchy, key, relationship, role, and filter behavior.

## 79. KPI Metadata
KPIs shall document formula, target, threshold, period, directionality, population, and dimensional applicability.

## 80. Certification Boundary
Only datasets that satisfy defined quality, reconciliation, documentation, lineage, and ownership requirements may be certified for governed consumption.

## 81. Consumption Status
Dataset status shall distinguish certified, provisional, deprecated, restricted, and failed-quality states.

## 82. Schema Stability
BI-ready schemas shall maintain predictable field meaning and controlled structural changes.

## 83. Versioning
Breaking schema or semantic changes shall use a controlled versioning strategy where backward compatibility cannot be maintained.

## 84. Backward Compatibility
Non-breaking changes shall preserve existing field meanings and consumer expectations.

## 85. Query Safety
Serving structures shall reduce the risk of accidental Cartesian joins, uncontrolled aggregations, ambiguous relationships, and unsupported calculations.

## 86. Performance
BI-ready structures shall support predictable access through appropriate grain, aggregation, filtering, and reusable analytical structures.

## 87. Refresh Compatibility
Dataset refresh behavior shall align with approved full-refresh or incremental processing semantics.

## 88. Freshness Metadata
Datasets shall expose or document refresh timestamp, processing state, and freshness expectation where operationally required.

## 89. Completeness Metadata
Where applicable, datasets shall expose evidence of population completeness and processing completion.

## 90. Reconciliation Metadata
Material BI-ready datasets shall retain evidence of applicable reconciliation checks.

## 91. Lineage Metadata
Datasets shall retain lineage from serving fields through semantic objects, marts, transformations, and approved sources.

## 92. Access Governance
Consumption access shall follow approved ownership, authorization, least-privilege, and sensitive-data controls.

## 93. Export Boundary
Exportable datasets shall retain business definitions, field meaning, grain, and applicable governance restrictions.

## 94. Self-Service Boundary
Self-service users shall consume governed structures and shall not redefine certified metrics without controlled governance.

## 95. Analytical SQL Boundary
BI-ready access structures may simplify consumption but shall not duplicate or contradict governed analytical SQL definitions.

## 96. Semantic Boundary
Serving structures shall remain aligned with the semantic/business layer as the authoritative business-definition boundary.

## 97. Observability
BI-ready serving structures shall support monitoring of freshness, availability, completeness, schema stability, quality, and reconciliation.

## 98. Failure Handling
Failed dataset generation shall prevent publication of invalid or partially processed BI-ready products.

## 99. Recovery
Recovery shall restore a valid serving state without modifying original source records.

## 100. Reproducibility
Dataset generation shall be reproducible from approved upstream models, definitions, processing state, and configuration.

## 101. Change Impact
Dataset changes shall assess impact on dashboards, reports, semantic models, analytical SQL, metrics, KPIs, and downstream consumers.

## 102. Security
BI-ready access shall enforce approved data-access and sensitive-attribute boundaries.

## 103. Source Preservation
BI-ready serving structures shall never mutate, overwrite, delete, or alter original source records.

## 104. Technology-Neutral Boundary
These logical consumption models are independent of a specific warehouse or BI visualization vendor.

## 105. Acceptance Criteria
Area 44.2 is accepted when BI-ready dataset structure, grain, consumer models, detail and summary models, metric and dimensional consumption, dashboard and reporting access, drill-down, filtering, grouping, ranking, period comparison, trend, cohort, entity-specific access, cross-domain and multi-fact controls, known multiplicity, null and zero semantics, field and metric metadata, certification, schema stability, versioning, query safety, performance, refresh, freshness, completeness, reconciliation, lineage, access governance, export, self-service, semantic alignment, observability, failure handling, recovery, reproducibility, change impact, security, source preservation, and technology-neutral boundaries are explicitly documented and validated.

