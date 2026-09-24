# Area 23.2 — Profiling Metrics & Measurement Rules

Status: Accepted & Frozen

## 1. Purpose
Define standardized profiling metrics and measurement rules for establishing a repeatable RetailIQ data-quality baseline.

## 2. Area 23.1 Foundation Dependency
All profiling metrics shall implement the baseline framework established in Area 23.1.

## 3. Area 05 Source Profiling Dependency
Metric definitions shall remain consistent with the physical source observations established in Area 05.

## 4. Area 06 Relationship Dependency
Relationship metrics shall respect approved keys, cardinalities, and documented exceptions from Area 06.

## 5. Area 07 Contract Dependency
Schema, type, nullability, and domain metrics shall reference the contracts established in Area 07.

## 6. Area 17 Raw Validation Dependency
Metrics shall distinguish accepted, rejected, and quarantined populations established in Area 17.

## 7. Area 18 Staging Dependency
Staging profiling shall measure populations and transformations within the boundaries established in Area 18.

## 8. Area 19 Transformation Dependency
Transformation effects shall be measurable and distinguishable from unexpected quality deviations.

## 9. Area 20 Standardization Dependency
Standardized values shall be profiled according to their normalized representation while retaining source lineage.

## 10. Area 21 Deduplication Dependency
Duplicate metrics shall distinguish source duplicates, detected duplicates, resolved records, and non-merge outcomes.

## 11. Area 22 Reconciliation Dependency
Profiling metrics shall align with the control totals, reconciliation rules, mappings, and exception framework established in Area 22.

## 12. Record Count Metrics
Record-count metrics shall capture total rows, accepted rows, rejected rows, and relevant population changes at defined processing boundaries.

## 13. Completeness Metrics
Completeness shall measure null rate, missing rate, blank rate where applicable, and population coverage for material fields.

## 14. Uniqueness Metrics
Uniqueness shall measure distinct counts, duplicate counts, duplicate rates, key uniqueness, and composite-key uniqueness where applicable.

## 15. Validity Metrics
Validity shall measure domain conformity, format conformity, numeric range conformity, date validity, and contract conformity.

## 16. Distribution Metrics
Distribution metrics shall include categorical frequency, minimum, maximum, and appropriate descriptive statistics for material numeric fields.

## 17. Temporal Metrics
Temporal metrics shall include minimum and maximum observed dates, null temporal values, lifecycle intervals, and boundary anomalies.

## 18. Relationship Metrics
Relationship metrics shall measure parent-child match rates, orphan counts, multiplicity, and documented relationship exceptions.

## 19. Business Metrics
Business profiling shall measure material characteristics of orders, customers, products, sellers, payments, reviews, and order items at approved grain.

## 20. Metric Calculation Standards
Each metric shall define population, numerator, denominator where applicable, calculation rule, grain, unit, expected range, and interpretation.

## 21. Threshold and Alert Rules
Thresholds shall be evidence-based and documented. A threshold breach shall create a reviewable profiling exception rather than automatically implying a processing defect.

## 22. Baseline Comparison
Current profiling results shall be compared with the approved baseline version and differences shall be classified as expected change, source change, processing change, or unexplained deviation.

## 23. Evidence and Reproducibility
Metric execution shall preserve definitions, input boundary, execution context, result values, baseline version, comparison result, and evidence location.

## 24. Technology-Neutral Boundary
These metric definitions specify logical measurement behavior without prescribing a specific warehouse, database, SQL engine, orchestration platform, or BI technology.

## 25. Acceptance Criteria
Area 23.2 is acceptable when profiling metrics, calculation rules, thresholds, baseline comparisons, evidence, and reproducibility controls are explicitly defined and traceable to frozen Areas 05–07, 17–22.

