# Area 43.1 — Analytical SQL & Business Analysis Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the governed Analytical SQL and Advanced Business Analysis foundation for RetailIQ, covering analytical query patterns, business analysis, metric consumption, dimensional analysis, time analysis, ranking, segmentation, trend analysis, and controlled analytical interpretation.

## 2. Area 42 Dependency
Analytical SQL shall consume the frozen Semantic / Business Layer and shall preserve approved business definitions, measures, KPIs, dimensions, relationships, grain, filters, and aggregation semantics.

## 3. Area 41 Dependency
Analytical queries shall use approved Business Metrics and KPI Definitions rather than redefining governed metrics or KPIs.

## 4. Area 40 Dependency
Analytical SQL shall consume approved Business Data Marts and preserve their declared grains and business responsibilities.

## 5. Area 39 Dependency
Analytical queries shall preserve approved data-mart architecture, fact, dimension, measure, reconciliation, and double-counting boundaries.

## 6. Area 38 Dependency
Analytical SQL dependencies shall follow the approved Transformation Dependency Graph.

## 7. Area 37 Dependency
Analytical SQL artifacts shall follow analytics engineering standards for naming, documentation, testing, lineage, ownership, reproducibility, and controlled change.

## 8. Area 36 Dependency
Reusable business transformations shall remain owned upstream and shall not be unnecessarily duplicated in analytical queries.

## 9. Area 35 Dependency
Analytical outputs shall remain compatible with approved incremental model identity, idempotency, reconciliation, and recovery behavior.

## 10. Area 34 Dependency
Analytical consumption shall remain compatible with approved full-refresh and incremental processing semantics.

## 11. Area 33 Dependency
Analytical SQL shall consume the approved ELT architecture and shall not bypass governed transformation layers without documented justification.

## 12. Area 32 Dependency
Historical analysis shall preserve approved historical and late-arriving record semantics.

## 13. Area 31 Dependency
Historical dimension analysis shall preserve approved SCD behavior.

## 14. Area 30 Dependency
Analytical SQL shall use approved conformed and role-playing dimensions.

## 15. Area 29 Dependency
Analytical calculations shall preserve approved fact grain and measure definitions.

## 16. Area 28 Dependency
Analytical queries shall respect approved fact and dimension responsibilities.

## 17. Area 27 Dependency
Dimension-based analysis shall use approved dimension architecture.

## 18. Area 26 Dependency
Analytical joins shall use approved natural and surrogate key semantics.

## 19. Area 25 Dependency
Every analytical query shall explicitly preserve the business grain required by the analysis.

## 20. Area 24 Dependency
Analytical SQL shall follow the approved dimensional modeling strategy.

## 21. Area 23 Dependency
Analytical analysis shall remain compatible with approved profiling baselines.

## 22. Area 22 Dependency
Analytical outputs shall support approved reconciliation controls.

## 23. Area 21 Dependency
Analytical queries shall preserve approved duplicate detection and record-resolution behavior.

## 24. Area 20 Dependency
Analytical SQL shall consume standardized and normalized analytical data.

## 25. Analytical SQL Purpose
Analytical SQL shall transform governed semantic and mart data into reproducible business analysis without changing the underlying governed definitions.

## 26. Business Question First
Every analytical query shall begin with a clearly stated business question or analytical objective.

## 27. Analysis Scope
Each analysis shall document population, time period, dimensional scope, filters, exclusions, and relevant business assumptions.

## 28. Grain Declaration
Each analytical query shall declare its intended output grain before joins, aggregations, rankings, or window calculations are applied.

## 29. Population Definition
Analytical populations shall explicitly identify eligible records and exclusion rules.

## 30. Metric Reuse
Approved metrics shall be reused from governed semantic definitions rather than independently recreated with potentially conflicting formulas.

## 31. KPI Reuse
Approved KPIs shall be consumed according to their governed definitions, targets, thresholds, directionality, and performance periods.

## 32. Join Discipline
Every analytical join shall have an identified business purpose, join key, expected cardinality, and grain impact.

## 33. Join Safety
Analytical SQL shall prevent accidental Cartesian products, uncontrolled many-to-many joins, and measure multiplication.

## 34. Aggregation Discipline
Aggregations shall occur at the appropriate business grain and shall preserve additive, semi-additive, non-additive, ratio, and distinct-count semantics.

## 35. Filtering Discipline
Filters shall use governed business values and shall be applied at a level that does not unintentionally alter metric populations.

## 36. Date Analysis
Time-based analysis shall use the correct governed date role and explicit period boundaries.

## 37. Period Comparisons
Prior-period, month-over-month, year-over-year, rolling-period, and other comparative analyses shall document the comparison basis.

## 38. Trend Analysis
Trend analysis shall identify the metric, observation period, dimensional context, and treatment of incomplete periods.

## 39. Ranking Analysis
Ranking analysis shall define the ranking metric, population, ordering direction, tie behavior, and requested ranking grain.

## 40. Top-N Analysis
Top-N analysis shall define N, ranking population, tie behavior, dimensional scope, and time period.

## 41. Bottom-N Analysis
Bottom-N analysis shall use the same explicit population, metric, ordering, tie, and period controls as Top-N analysis.

## 42. Window Functions
Window functions shall document partitioning, ordering, frame boundaries, and intended business interpretation.

## 43. Running Totals
Running totals shall use deterministic ordering and shall not double-count repeated business events.

## 44. Moving Averages
Moving averages shall define the observation window, minimum observations, missing-period treatment, and aggregation semantics.

## 45. Percent-of-Total
Percent-of-total analysis shall define the numerator population, denominator population, partition context, and denominator-zero behavior.

## 46. Contribution Analysis
Contribution analysis shall distinguish absolute contribution from percentage contribution and preserve compatible populations.

## 47. Segmentation
Customer, product, seller, order, or other segmentation shall define segmentation population, attributes, thresholds, and assignment rules.

## 48. Cohort Analysis
Cohort analysis shall define cohort assignment event, cohort period, observation period, population, and retention or value measure.

## 49. Customer Analysis
Customer analysis shall use governed customer grain, purchase behavior, order relationships, frequency, value, geography, and lifecycle context.

## 50. Product Analysis
Product analysis shall preserve product grain and shall distinguish product-level attributes from order-item-level measures.

## 51. Seller Analysis
Seller analysis shall preserve seller grain and shall distinguish seller-level attributes from fulfillment and item-level measures.

## 52. Sales Analysis
Sales analysis shall use governed sales measures and shall explicitly define the applicable commercial population and time basis.

## 53. Fulfillment Analysis
Fulfillment analysis shall use governed delivery measures and shall document eligible order populations and temporal boundaries.

## 54. Payment Analysis
Payment analysis shall preserve payment grain and shall not treat payment events as orders without governed aggregation.

## 55. Review Analysis
Review analysis shall preserve review population semantics and the documented review_id repetition boundary.

## 56. Geography Analysis
Geographic analysis shall use approved customer and seller geography dimensions and shall preserve the relevant entity grain.

## 57. Category Analysis
Product-category analysis shall preserve source category semantics and shall not invent translations for unmatched category values.

## 58. Null Handling
Null, unknown, unavailable, and not-applicable values shall retain governed semantics during analytical calculations.

## 59. Outlier Treatment
Outlier handling shall be explicitly documented and shall not silently remove valid business records.

## 60. Missing Periods
Missing periods shall be distinguished from periods with genuine zero activity.

## 61. Statistical Interpretation
Analytical summaries shall distinguish descriptive calculations from causal or predictive conclusions.

## 62. Business Interpretation
Analytical results shall distinguish observed data patterns from assumptions or interpretations.

## 63. Reconciliation
Analytical results shall reconcile to approved semantic measures, KPIs, marts, and populations where an equivalent governed value exists.

## 64. Validation
Analytical SQL shall be validated for syntax, data types, grain, joins, filters, aggregations, expected population, and business-rule correctness.

## 65. Regression
Changes to analytical SQL shall be regression-tested against approved baseline results or expected business controls.

## 66. Reproducibility
Analytical results shall be reproducible from the same governed inputs, definitions, filters, time context, and model versions.

## 67. Lineage
Analytical SQL shall document upstream semantic objects, marts, metrics, dimensions, and relevant source dependencies.

## 68. Documentation
Each analytical query shall document business question, assumptions, grain, population, metric definitions, joins, filters, calculations, and expected interpretation.

## 69. Performance Awareness
Analytical SQL shall avoid unnecessary scans, repeated transformations, uncontrolled joins, and inefficient calculation patterns where governed architecture provides reusable structures.

## 70. Security
Analytical SQL shall respect approved data-access, ownership, least-privilege, and sensitive-attribute boundaries.

## 71. Source Preservation
Analytical SQL shall never mutate, overwrite, delete, or alter original source data.

## 72. Technology-Neutral Boundary
Analytical SQL definitions shall remain independent of a specific BI or visualization product unless a later approved implementation explicitly establishes such dependency.

## 73. Acceptance Criteria
Area 43.1 is accepted when analytical purpose, business-question definition, scope, grain, population, metric and KPI reuse, join discipline, aggregation, filtering, date analysis, period comparison, trend, ranking, Top-N, Bottom-N, window functions, running totals, moving averages, percent-of-total, contribution, segmentation, cohort, customer, product, seller, sales, fulfillment, payment, review, geography, category, null, outlier, missing-period, statistical, business interpretation, reconciliation, validation, regression, reproducibility, lineage, documentation, performance, security, source-preservation, and technology-neutral controls are explicitly documented and validated.

