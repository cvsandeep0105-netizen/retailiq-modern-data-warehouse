# Area 23.4 — Profiling Quality, Baseline Deviation & Exception Controls

Status: Accepted & Frozen

## 1. Purpose
Define quality controls for profiling results, baseline deviations, threshold breaches, exceptions, investigation, and auditability.

## 2. Area 23.1 Foundation Dependency
Quality controls shall implement the profiling baseline framework established in Area 23.1.

## 3. Area 23.2 Metrics Dependency
Quality evaluation shall use the profiling metrics and measurement rules established in Area 23.2.

## 4. Area 23.3 Mapping Dependency
Deviation interpretation shall use the business mappings and entity-grain controls established in Area 23.3.

## 5. Area 05 Source Profiling Dependency
Source-quality expectations shall remain grounded in the accepted physical observations from Area 05.

## 6. Area 06 Relationship Dependency
Relationship-quality deviations shall respect documented keys, cardinalities, and source exceptions from Area 06.

## 7. Area 07 Contract Dependency
Contract violations shall be evaluated against approved schema, type, nullability, and domain expectations.

## 8. Area 17 Raw Validation Dependency
Quality analysis shall distinguish raw accepted, rejected, and quarantined populations.

## 9. Area 18 Staging Dependency
Staging effects shall be considered when evaluating profiling deviations.

## 10. Area 19 Transformation Dependency
Approved transformation effects shall not automatically be classified as quality failures.

## 11. Area 20 Standardization Dependency
Approved normalization effects shall remain distinguishable from unexpected quality deviations.

## 12. Area 21 Deduplication Dependency
Duplicate and record-resolution effects shall be incorporated into profiling-quality evaluation.

## 13. Area 22 Reconciliation Dependency
Profiling deviations shall be cross-checked against reconciliation evidence, control totals, mappings, and exceptions from Area 22.

## 14. Completeness Quality
Unexpected changes in null, missing, blank, or population-coverage rates shall be identified and classified.

## 15. Uniqueness Quality
Unexpected changes in duplicate counts, distinct identifiers, or composite-key uniqueness shall generate reviewable deviations.

## 16. Validity Quality
Domain, format, range, temporal, and contract-validity deviations shall be measured against documented expectations.

## 17. Distribution Quality
Material distribution changes shall be identified using approved categorical and numeric profiling metrics.

## 18. Relationship Quality
Changes in parent-child coverage, orphan counts, and multiplicity shall be compared with approved relationship baselines.

## 19. Baseline Deviation Classification
Each deviation shall be classified as expected source evolution, expected transformation effect, expected standardization effect, expected deduplication effect, processing defect, contract deviation, or unexplained change.

## 20. Threshold and Severity
Thresholds shall have documented rationale. Severity shall reflect the impact and scope of the deviation rather than arbitrary numeric labels.

## 21. Exception Lifecycle
Profiling exceptions shall have detection, classification, ownership, investigation, disposition, evidence, and closure states.

## 22. Regression and Repeatability
Repeated profiling against unchanged inputs shall produce consistent results and shall support comparison with the approved baseline version.

## 23. Audit Evidence and Lineage
Each material deviation shall retain metric definition, population, baseline version, observed value, expected value or range, classification, evidence, and lineage.

## 24. Technology-Neutral Boundary
These controls define profiling-quality behavior independently of a specific warehouse, database, SQL engine, orchestration platform, or BI technology.

## 25. Acceptance Criteria
Area 23.4 is acceptable when completeness, uniqueness, validity, distribution, relationship, deviation, threshold, exception lifecycle, regression, audit, and lineage controls are explicitly defined and traceable to frozen Areas 05–07, 17–22 and Areas 23.1–23.3.

