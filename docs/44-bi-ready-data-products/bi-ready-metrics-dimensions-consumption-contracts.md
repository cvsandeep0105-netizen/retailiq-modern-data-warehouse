# Area 44.3 — BI-Ready Metrics, Dimensions & Consumption Contracts

Status: Accepted & Frozen

## 1. Purpose
Define governed contracts for metrics, KPIs, dimensions, fields, relationships, filters, grain, and analytical consumption within RetailIQ BI-ready data products.

## 2. Area 44.2 Dependency
BI-ready contracts shall extend the approved dataset structures and analytical access patterns defined in Area 44.2.

## 3. Area 44.1 Dependency
All consumption contracts shall preserve the BI-ready data product foundation.

## 4. Area 43 Dependency
Exposed analytical measures and datasets shall preserve approved Analytical SQL and Advanced Business Analysis definitions.

## 5. Area 42 Dependency
Semantic and business-layer definitions remain authoritative for reusable business meaning.

## 6. Area 41 Dependency
Metrics, KPIs, targets, thresholds, populations, periods, and calculation definitions shall remain governed.

## 7. Area 40 Dependency
Consumption contracts shall preserve Business Data Mart grain and responsibilities.

## 8. Area 39 Dependency
Data-mart architecture shall remain the structural foundation for BI-ready contracts.

## 9. Area 38 Dependency
Dataset dependencies shall remain aligned with the approved transformation dependency graph.

## 10. Area 37 Dependency
Contracts shall follow analytics engineering standards for naming, documentation, testing, lineage, ownership, and controlled change.

## 11. Area 36 Dependency
Reusable business transformations shall remain upstream of consumption contracts.

## 12. Area 35 Dependency
Consumption outputs shall remain compatible with incremental model identity and idempotency.

## 13. Area 34 Dependency
Refresh behavior shall remain compatible with approved full-refresh and incremental processing.

## 14. Area 33 Dependency
Contracts shall consume the approved ELT architecture.

## 15. Area 32 Dependency
Historical and late-arriving record semantics shall remain preserved.

## 16. Area 31 Dependency
SCD behavior shall remain preserved where historical dimensions are exposed.

## 17. Area 30 Dependency
Conformed and role-playing dimension semantics shall remain preserved.

## 18. Area 29 Dependency
Fact grain and measure definitions shall remain unchanged.

## 19. Area 28 Dependency
Fact architecture shall remain authoritative for fact-based consumption.

## 20. Area 27 Dependency
Dimension architecture shall remain authoritative for dimensional consumption.

## 21. Area 26 Dependency
Natural and surrogate key semantics shall remain traceable.

## 22. Area 25 Dependency
Every contract shall explicitly declare its business grain.

## 23. Area 24 Dependency
Dimensional-modeling semantics shall remain preserved.

## 24. Area 23 Dependency
Profiling expectations shall remain available for contract validation.

## 25. Area 22 Dependency
Reconciliation controls shall remain applicable.

## 26. Area 21 Dependency
Duplicate and record-resolution boundaries shall remain preserved.

## 27. Area 20 Dependency
Contracts shall consume standardized and normalized analytical data.

## 28. Consumption Contract Definition
A BI-ready consumption contract defines the approved meaning, structure, grain, population, calculation, dimensional context, refresh expectation, quality requirements, and usage boundary of an exposed analytical object.

## 29. Contract Identity
Each material metric, KPI, dimension, field, or dataset contract shall have a unique governed identity.

## 30. Business Definition
Every exposed analytical object shall have a clear business definition understandable to its intended consumers.

## 31. Technical Definition
Every exposed object shall identify its technical source, model, field, calculation, or transformation lineage.

## 32. Grain Contract
Every metric and dataset shall declare its intended grain and shall document any required aggregation before consumption.

## 33. Population Contract
Every metric and KPI shall define its eligible population, inclusion rules, exclusions, and status treatment.

## 34. Time Contract
Time-based metrics shall define date role, period basis, timezone assumptions where applicable, incomplete-period behavior, and historical context.

## 35. Aggregation Contract
Each measure shall identify whether it is additive, semi-additive, non-additive, a ratio, a distinct count, a duration, or a score.

## 36. Metric Formula Contract
Metric formulas shall match the approved Area 41 and Area 42 definitions.

## 37. KPI Contract
KPIs shall preserve numerator, denominator, target, threshold, directionality, performance period, and dimensional applicability.

## 38. GMV Boundary
GMV shall retain its governed definition and shall not be silently treated as equivalent to payment_value or another measure.

## 39. Payment Value Boundary
payment_value shall retain its approved payment semantics and shall not be substituted for sales-item value without an explicit governed definition.

## 40. Average Metric Contract
Average measures shall document numerator, denominator, population, zero-denominator behavior, and rounding boundary.

## 41. Distinct Count Contract
Distinct counts shall identify the business entity being counted and protect against lower-grain join multiplication.

## 42. Ratio Contract
Ratios shall document numerator, denominator, population compatibility, zero-denominator behavior, and percentage representation.

## 43. Duration Contract
Duration measures shall document start event, end event, unit, eligible population, null behavior, and temporal validity.

## 44. Dimension Contract
Each dimension shall document identity, attributes, hierarchy, key, relationship, role, filter behavior, and historical semantics.

## 45. Customer Dimension Contract
Customer attributes shall preserve customer grain and approved customer identity semantics.

## 46. Product Dimension Contract
Product attributes shall preserve product grain, category semantics, and documented unmatched translation behavior.

## 47. Seller Dimension Contract
Seller attributes shall preserve seller grain and seller geography semantics.

## 48. Date Dimension Contract
Date attributes shall support approved calendar periods, date roles, period comparison, and time-based analysis.

## 49. Geography Dimension Contract
Geography shall explicitly identify customer versus seller location and shall not blur their analytical roles.

## 50. Category Dimension Contract
Category values shall preserve source meaning and shall not invent translations for the 13 unmatched non-null source categories.

## 51. Role-Playing Date Contract
Role-playing dates shall explicitly identify the business event represented by each date role.

## 52. Relationship Contract
Every exposed relationship shall define participating entities, keys, expected cardinality, filter behavior, and analytical purpose.

## 53. Many-to-Many Contract
Many-to-many relationships shall require explicit handling such as controlled bridges or pre-aggregation where appropriate.

## 54. Filter Contract
Filters shall use governed business values and shall document whether they operate at row, entity, aggregate, or KPI level.

## 55. Status Contract
Order-status and other lifecycle filters shall use approved status semantics and shall not silently reinterpret missing states.

## 56. Null Contract
NULL shall remain distinct from zero, unknown, unavailable, and not-applicable states.

## 57. Unknown Member Contract
Unknown or unresolved members shall have explicit governed semantics.

## 58. Field Contract
Every exposed field shall define name, meaning, type, grain, nullability expectation, lineage, and consumer purpose.

## 59. Naming Contract
Business-facing names shall be consistent, readable, unambiguous, and traceable to technical names.

## 60. Measure Exposure Contract
Measures shall be exposed only where their aggregation and dimensional compatibility are understood and documented.

## 61. KPI Exposure Contract
KPIs shall be exposed only when their definitions, targets, thresholds, populations, and periods are governed.

## 62. Certified Metric Boundary
Certified metrics shall not be redefined downstream by dashboards, reports, or self-service calculations.

## 63. Provisional Metric Boundary
Provisional analytical objects shall be explicitly labeled and shall not be represented as certified business definitions.

## 64. Deprecated Object Boundary
Deprecated objects shall have documented replacement or retirement behavior and shall not silently remain the preferred consumption path.

## 65. Dashboard Contract
Dashboard-facing datasets shall define supported dimensions, metrics, filters, time context, and expected grain.

## 66. Report Contract
Reporting datasets shall define stable fields, metric semantics, reporting period, and expected population.

## 67. Self-Service Contract
Self-service consumers shall receive governed objects that reduce the need for independent metric reconstruction.

## 68. Export Contract
Exported analytical data shall preserve field definitions, grain, metric meaning, and applicable governance restrictions.

## 69. Drill-Down Contract
Drill-down paths shall document how summary measures connect to lower-grain analytical records.

## 70. Drill-Through Contract
Drill-through behavior shall preserve originating filters and business context where technically supported.

## 71. Performance Contract
BI-ready contracts shall define expected analytical access behavior and shall avoid requiring consumers to repeatedly reconstruct expensive transformations.

## 72. Freshness Contract
Each material dataset shall define expected freshness and the evidence used to determine currentness.

## 73. Availability Contract
BI-ready products shall define expected availability and publication behavior.

## 74. Quality Contract
Required structural, business-rule, reconciliation, and analytical quality checks shall pass before certified publication.

## 75. Reconciliation Contract
Exposed measures shall reconcile to approved semantic, mart, and upstream values where equivalent populations exist.

## 76. Regression Contract
Changes shall be tested for schema, grain, population, metric, KPI, relationship, and reconciliation regressions.

## 77. Lineage Contract
Every exposed metric, KPI, dimension, and field shall be traceable to approved upstream objects.

## 78. Ownership Contract
Each governed object shall have accountable ownership for definition, quality, access, and change.

## 79. Documentation Contract
Contracts shall document business meaning, technical meaning, calculation, grain, population, filters, refresh, limitations, lineage, and owner.

## 80. Change Contract
Changes shall be assessed for semantic, analytical, schema, downstream BI, performance, and consumer impact.

## 81. Version Contract
Breaking changes shall use controlled versioning where compatibility cannot be preserved.

## 82. Security Contract
Consumption shall enforce approved access, least privilege, sensitive-data boundaries, and authorization.

## 83. Audit Contract
Contract changes and certification decisions shall retain auditable evidence.

## 84. Known Multiplicity Contract
Contracts involving order-level analysis shall explicitly account for up to 21 observed order items, up to 29 payment records, and up to 3 review records per order.

## 85. Review Identity Contract
Review identity shall preserve (review_id, order_id) because review_id alone is not unique.

## 86. Double-Counting Contract
Consumption contracts shall prevent incompatible child-grain relationships from multiplying parent-level measures.

## 87. Reproducibility Contract
Governed analytical objects shall be reproducible from approved definitions, models, processing versions, filters, and time context.

## 88. Observability Contract
Contracted datasets shall support freshness, availability, schema, quality, and reconciliation monitoring.

## 89. Failure Contract
Failed contract validation shall prevent invalid or uncertified publication.

## 90. Recovery Contract
Recovery shall restore valid consumption structures without modifying original source records.

## 91. Source Preservation
BI-ready contract generation shall never mutate, overwrite, delete, or alter original source data.

## 92. Technology-Neutral Boundary
These contracts define logical business and analytical behavior and are independent of a specific warehouse or BI vendor.

## 93. Acceptance Criteria
Area 44.3 is accepted when metric, KPI, dimension, field, grain, population, time, aggregation, formula, relationship, filter, null, unknown, naming, dashboard, report, self-service, export, drill-down, performance, freshness, availability, quality, reconciliation, regression, lineage, ownership, documentation, change, versioning, security, audit, known multiplicity, review identity, double-counting, reproducibility, observability, failure, recovery, source-preservation, and technology-neutral consumption contracts are explicitly documented and validated.

