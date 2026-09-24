# Area 41.4 — KPI Target, Threshold & Performance Classification Controls

Status: Accepted & Frozen

## 1. Purpose
Define governed controls for KPI targets, thresholds, performance classification, comparison periods, target applicability, directionality, variance interpretation, exceptions, and downstream analytical consumption.

## 2. Area 41.3 Dependency
This artifact shall preserve the KPI framework, actual-value, target, variance, directionality, performance-period, dimensional-context, ownership, lineage, and change-control definitions established in Area 41.3.

## 3. Area 41.2 Dependency
Target and threshold controls shall reference only governed core business metrics and shall not redefine frozen metric calculations.

## 4. Area 41.1 Dependency
All target and classification controls shall comply with the frozen Business Metrics & KPI Foundation.

## 5. Area 40 Dependency
KPI performance classifications shall consume approved Business Data Marts without changing mart grain or business meaning.

## 6. Area 39 Dependency
Performance comparison shall preserve approved data-mart grain, fact, dimension, measure, reconciliation, and double-counting boundaries.

## 7. Area 38 Dependency
Target and KPI classification dependencies shall follow the approved transformation dependency graph.

## 8. Area 37 Dependency
Target and classification models shall follow analytics-engineering contracts, testing, documentation, ownership, lineage, and controlled-change standards.

## 9. Area 36 Dependency
Reusable upstream business transformations shall not be duplicated inside KPI classification logic.

## 10. Area 35 Dependency
Incremental processing shall preserve target and KPI classification idempotency, merge, reconciliation, and recovery behavior.

## 11. Area 34 Dependency
Target and KPI refresh shall remain compatible with approved full-refresh, incremental, watermark, replay, and backfill strategies.

## 12. Area 33 Dependency
Target and classification processing shall remain within the approved ELT architecture.

## 13. Area 32 Dependency
Historical target and KPI interpretation shall preserve approved historical and late-arriving record behavior.

## 14. Area 31 Dependency
Dimension-based target applicability shall preserve approved slowly changing dimension behavior.

## 15. Area 30 Dependency
Target applicability and performance classification shall use approved conformed and role-playing dimensions.

## 16. Area 29 Dependency
Performance comparisons shall preserve approved fact grain and measure definitions.

## 17. Area 28 Dependency
Target comparisons shall respect approved fact and dimension responsibilities.

## 18. Area 27 Dependency
Dimension-specific targets shall follow approved dimension architecture.

## 19. Area 26 Dependency
Target and KPI joins shall use approved natural and surrogate key semantics.

## 20. Area 25 Dependency
Performance classification shall preserve the declared KPI calculation grain.

## 21. Area 24 Dependency
Target and performance models shall follow the approved dimensional modeling strategy.

## 22. Area 23 Dependency
Performance classifications shall remain compatible with approved profiling baselines.

## 23. Area 22 Dependency
Target comparisons shall support population, measure, and analytical reconciliation.

## 24. Area 21 Dependency
Target and classification results shall preserve approved record-resolution behavior.

## 25. Area 20 Dependency
Target and KPI classification inputs shall consume standardized and normalized data.

## 26. Target Definition
A target is a governed expected KPI value or performance objective for a defined population, dimensional context, unit, and effective period.

## 27. Target Types
Supported target types shall be explicitly classified, including fixed target, percentage target, rate target, count target, range target, benchmark target, threshold target, and externally supplied business target.

## 28. Target Ownership
Every target shall identify an accountable business target owner. Technical ownership shall also be recorded where the target is implemented in analytical infrastructure.

## 29. Target Version
Targets shall be versioned. A revised target shall not silently overwrite the historical meaning of a previously effective target.

## 30. Target Effective Dates
Every governed target shall have an effective start date and, where applicable, an effective end date.

## 31. Target Applicability
Target applicability shall identify the KPI, population, business unit or dimensional scope, geography where applicable, and performance period.

## 32. Target Unit Compatibility
Actual and target values shall use compatible units, scale, currency treatment, rate definitions, and calculation semantics.

## 33. Target Population Compatibility
An actual KPI shall only be compared with a target when the eligible populations are compatible or an explicit governed adjustment exists.

## 34. Target Time Compatibility
Actual and target periods shall align according to the approved calendar, fiscal, rolling-window, or business-period definition.

## 35. Target Missingness
A missing target shall remain missing or not applicable. It shall never be silently converted to zero.

## 36. Unsupported Target Control
No target value shall be fabricated, inferred, estimated, or presented as an approved business target without documented governance or an explicitly labeled analytical assumption.

## 37. Baseline Definition
Where baseline performance is used, the baseline period, population, calculation method, and source shall be explicitly documented.

## 38. Baseline Stability
Baseline changes shall be versioned and shall preserve the ability to explain historical performance comparisons.

## 39. Threshold Definition
A threshold defines a governed boundary used to classify KPI performance or trigger an analytical condition.

## 40. Threshold Types
Thresholds may include minimum acceptable value, maximum acceptable value, warning boundary, target boundary, tolerance boundary, or multi-band performance boundary.

## 41. Threshold Directionality
Threshold evaluation shall respect KPI directionality. Higher-is-better and lower-is-better KPIs shall not use identical classification logic without explicit justification.

## 42. Threshold Inclusivity
Each threshold shall define whether its boundary is inclusive or exclusive. Boundary behavior shall be deterministic.

## 43. Multi-Band Classification
Where multiple performance bands exist, their order, boundaries, labels, and applicability shall be explicitly defined.

## 44. Classification Labels
Performance labels shall be governed semantic classifications and shall not alter the underlying numeric KPI value.

## 45. Actual-versus-Target Variance
Absolute variance shall be calculated as actual minus target where that convention is appropriate and documented.

## 46. Percentage Variance
Percentage variance shall use a governed denominator. Division by zero or unavailable targets shall produce a controlled non-applicable result rather than an invented percentage.

## 47. Favorable and Unfavorable Direction
Favorable or unfavorable interpretation shall be derived from documented KPI directionality and shall not be assumed from the sign of variance alone.

## 48. Tolerance Controls
Where tolerance is defined, the tolerance amount or percentage, unit, direction, effective period, and owner shall be documented.

## 49. Performance Period Controls
Performance periods shall be deterministic and shall use approved date and time boundaries.

## 50. Comparative Period Controls
Prior-period, year-over-year, month-over-month, or rolling comparisons shall document the comparison basis and population compatibility.

## 51. Dimensional Target Controls
Targets scoped by customer, product, seller, geography, category, or other dimensions shall have explicit dimensional applicability.

## 52. Hierarchical Target Controls
Targets at different hierarchy levels shall not be mixed without an explicit aggregation or allocation rule.

## 53. Target Aggregation Boundary
Targets shall not be summed, averaged, or otherwise aggregated unless the target's mathematical and business semantics permit that operation.

## 54. KPI Grain Protection
Performance classification shall not change the KPI's declared grain or create duplicate KPI records.

## 55. Double-Counting Protection
Target joins and classification joins shall be validated so that one KPI observation does not receive multiple target records unless the model explicitly supports that structure.

## 56. Target Join Integrity
Every target join shall define its key, effective-date logic, dimensional scope, and expected cardinality.

## 57. Overlapping Target Control
Overlapping effective target records for the same KPI and applicability scope shall be detected and treated as an exception.

## 58. Target Gaps
Unexpected gaps in required target coverage shall be identified and reported rather than silently filled.

## 59. Exception Classification
Target exceptions shall distinguish missing target, overlapping target, invalid target, incompatible unit, incompatible population, incompatible period, and unsupported target.

## 60. Reconciliation
Actual KPI values, targets, variances, and classification counts shall reconcile to their governed upstream populations and metric definitions.

## 61. Quality Controls
Validation shall cover target completeness, uniqueness, effective dating, unit compatibility, population compatibility, threshold boundaries, directionality, variance calculations, and classification determinism.

## 62. Regression Controls
Changes to targets, thresholds, formulas, periods, or classification rules shall trigger regression validation for affected KPI outputs.

## 63. Historical Preservation
Historical KPI classifications shall preserve the target and threshold version applicable to the historical performance period.

## 64. Lineage
Every performance classification shall retain lineage to the KPI, actual metric, target version, threshold version, dimensional context, and effective period.

## 65. Auditability
Target and threshold changes shall be auditable through ownership, version, approval status, effective dates, change reason, and change timestamp.

## 66. Semantic Layer Boundary
Target, threshold, variance, and classification semantics defined here shall become governed inputs to the later Semantic / Business Layer.

## 67. BI Boundary
BI-ready outputs may expose actual, target, variance, variance percentage, performance classification, target version, and applicable period when governed.

## 68. Source Preservation
Target and KPI classification processing shall never mutate or overwrite original source records.

## 69. Acceptance Criteria
Area 41.4 is accepted when target definition, target types, ownership, versioning, effective dates, applicability, unit compatibility, population compatibility, missing-target handling, unsupported-target controls, baselines, thresholds, directionality, multi-band classification, variance, tolerance, performance periods, comparative periods, dimensional scope, target joins, overlap/gap controls, exceptions, reconciliation, quality, regression, historical preservation, lineage, auditability, semantic-layer, BI, and source-preservation controls are explicitly documented and validated.

