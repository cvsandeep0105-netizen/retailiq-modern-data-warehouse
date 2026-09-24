# Area 41.3 — KPI Framework, Business Targets & Performance Definitions

Status: Accepted & Frozen

## 1. Purpose
Define the governed RetailIQ KPI framework, including KPI structure, performance periods, actual values, target references, variance, directionality, thresholds, dimensional context, ownership, and change controls.

## 2. Area 41.2 Dependency
KPI definitions shall consume the frozen Core Business Metric Catalog and shall preserve approved metric definitions, grain, population, calculation, aggregation, lineage, ownership, and change-control boundaries.

## 3. Area 41.1 Dependency
KPI definitions shall comply with the frozen Business Metrics & KPI Foundation.

## 4. Area 40 Dependency
KPI inputs shall consume approved Business Data Marts without changing their declared grain or business meaning.

## 5. Area 39 Dependency
KPI construction shall preserve the frozen Data Mart Architecture and its grain, fact, dimension, business-logic, reconciliation, and double-counting controls.

## 6. Area 38 Dependency
KPI dependencies shall follow the approved transformation dependency graph.

## 7. Area 37 Dependency
KPI models shall comply with approved analytics engineering contracts, testing, documentation, ownership, regression, and controlled-change standards.

## 8. Area 36 Dependency
KPI calculations shall consume governed upstream transformations rather than duplicating reusable enterprise business logic.

## 9. Area 35 Dependency
KPI processing shall preserve approved incremental model identity, merge, idempotency, reconciliation, and recovery behavior.

## 10. Area 34 Dependency
KPI refresh shall preserve approved full-refresh, incremental, watermark, replay, backfill, and escalation behavior.

## 11. Area 33 Dependency
KPI construction shall remain within the approved ELT architecture.

## 12. Area 32 Dependency
Historical KPI analysis shall preserve approved historical and late-arriving data semantics.

## 13. Area 31 Dependency
KPI analysis requiring historical dimensions shall preserve approved SCD behavior.

## 14. Area 30 Dependency
KPI dimensional slicing shall use approved conformed and role-playing dimensions.

## 15. Area 29 Dependency
KPI inputs shall preserve approved fact grain and measure behavior.

## 16. Area 28 Dependency
KPI inputs shall preserve approved fact and dimension responsibilities.

## 17. Area 27 Dependency
KPI dimensions shall follow approved dimension architecture.

## 18. Area 26 Dependency
KPI relationships shall use approved natural and surrogate key semantics.

## 19. Area 25 Dependency
Every KPI calculation shall have an explicit valid calculation grain.

## 20. Area 24 Dependency
KPI modeling shall follow the approved dimensional modeling strategy.

## 21. Area 23 Dependency
KPI outputs shall remain compatible with approved profiling baselines.

## 22. Area 22 Dependency
KPI values shall support approved population, key, measure, and business-total reconciliation.

## 23. Area 21 Dependency
KPI calculations shall preserve approved duplicate and record-resolution behavior.

## 24. Area 20 Dependency
KPI inputs shall consume standardized and normalized analytical data.

## 25. KPI Framework
A KPI shall consist of a governed metric, business objective or performance context, calculation definition, eligible population, time period, dimensional context, performance direction, and optional target or threshold reference.

## 26. KPI Identity
Each KPI shall have a stable unique identifier and human-readable name. Renaming shall not silently create a new business definition or alter historical interpretation.

## 27. KPI Business Objective
Each KPI shall document the business objective or performance question it is intended to represent.

## 28. KPI Base Metric
Each KPI shall reference one or more governed catalog metrics rather than independently redefining the underlying business measurement.

## 29. Actual Value
The actual KPI value shall be calculated using the approved metric definition and the declared population, time period, and dimensional context.

## 30. Target Reference
A target may be associated with a KPI when a governed business target exists. Target values shall be treated as external business-governance inputs unless they are explicitly sourced from an approved analytical system.

## 31. Target Governance
Targets shall have an owner, effective period, applicable population or dimension, unit, version, and approval status. A missing target shall not be interpreted as zero.

## 32. Variance Definition
KPI variance shall have an explicit definition appropriate to the KPI type. Where both actual and target exist, absolute and/or relative variance may be defined according to governed business rules.

## 33. Directionality
Each KPI shall document whether higher, lower, or a context-specific value represents the desired direction. Directionality shall not be inferred solely from the metric name.

## 34. Threshold Boundary
Thresholds may classify KPI performance when governed thresholds exist. Thresholds shall be explicitly versioned and effective-dated.

## 35. Threshold Independence
Threshold classifications shall not alter the underlying metric or actual KPI value. They are interpretive attributes applied after calculation.

## 36. Performance Period
Each KPI shall define its performance period, such as daily, weekly, monthly, quarterly, annual, rolling period, or another governed period.

## 37. Period Boundary
Period calculations shall use explicit calendar or business-period definitions. Period boundaries shall be consistent across the KPI and its target where comparison is performed.

## 38. Actual-versus-Target Compatibility
Actual and target values shall use compatible units, populations, dimensional context, time periods, and calculation semantics before variance is calculated.

## 39. KPI Units
Each KPI shall declare its unit, such as currency, count, percentage, rate, duration, score, or another documented unit.

## 40. Ratio and Percentage KPIs
Ratio and percentage KPIs shall preserve their numerator and denominator definitions. Numerators and denominators shall be calculated from compatible populations before division.

## 41. Distinct-Count KPI Boundary
Distinct-count KPIs shall preserve distinct-count semantics and shall not be summed across overlapping populations.

## 42. Average KPI Boundary
Average-based KPIs shall preserve compatible numerator and denominator populations and shall not be averaged across periods unless that operation is explicitly governed.

## 43. Dimensional Context
KPI definitions shall identify valid dimensions such as date, customer, product, seller, geography, order status, category, and other approved analytical dimensions.

## 44. Cross-Domain KPI Boundary
Cross-domain KPIs shall explicitly document participating domains, compatible grains, joins, populations, measures, and aggregation rules.

## 45. Double-Counting Prevention
KPI calculations shall explicitly prevent inflation from multi-item orders, multiple payments, repeated reviews, multiple sellers, many-to-many relationships, and incompatible joins.

## 46. Missing and Exceptional Data
Missing, invalid, quarantined, or incomplete records shall follow KPI-specific population rules. They shall not be silently converted to valid zero values unless explicitly defined.

## 47. KPI Reconciliation
KPI actual values shall reconcile to compatible underlying metrics and mart populations at the declared grain and performance period.

## 48. KPI Quality
KPI validation shall include formula correctness, unit consistency, population completeness, numerator/denominator validity, grain integrity, target compatibility, and expected-value checks where appropriate.

## 49. KPI Lineage
Each KPI shall retain lineage to its base metric, source mart, transformation dependencies, and source attributes.

## 50. KPI Ownership
Each KPI shall have a business owner and technical owner responsible for definition, target governance where applicable, validation, change approval, and downstream impact assessment.

## 51. KPI Change Control
Changes to KPI formula, base metric, population, grain, target semantics, threshold, directionality, or performance period shall require documented impact analysis, approval, regression validation, and change history.

## 52. Historical Comparability
KPI versions shall preserve sufficient metadata to determine whether values from different periods remain directly comparable after definition or target changes.

## 53. Semantic Layer Boundary
KPI definitions established here shall become governed inputs to the later Semantic / Business Layer and shall not be silently redefined downstream.

## 54. BI Consumption Boundary
KPI outputs shall be suitable for BI-ready datasets, dashboards, scorecards, analytical SQL, and approved reporting products.

## 55. Source Preservation
KPI processing shall never mutate, overwrite, or delete original source records.

## 56. Acceptance Criteria
Area 41.3 is accepted when KPI framework, identity, objective, base metric, actual, target, variance, directionality, threshold, performance period, units, ratio, distinct-count, average, dimensional, cross-domain, double-counting, missing-data, reconciliation, quality, lineage, ownership, change control, historical comparability, semantic-layer, BI, and source-preservation controls are explicitly documented and validated.

