# Area 31.4 — SCD Quality, Reconciliation & Exception Controls

Status: Accepted & Frozen

## 1. Purpose
Define quality, reconciliation, exception, audit, and failure controls for Slowly Changing Dimension processing while preserving source truth and approved dimensional semantics.

## 2. Area 31.1 Dependency
SCD quality controls shall implement the historical-dimension foundation defined in Area 31.1.

## 3. Area 31.2 Dependency
Quality validation shall enforce the approved attribute-level SCD type classifications.

## 4. Area 31.3 Dependency
Historical version quality shall validate effective dating, current-version controls, and version interval integrity.

## 5. Area 30 Dependency
SCD quality shall preserve conformed and role-playing dimension consistency.

## 6. Area 29 Dependency
SCD validation shall protect fact-grain, measure ownership, and aggregation semantics.

## 7. Area 28 Dependency
Dimension version changes shall not introduce invalid fact-to-dimension relationships.

## 8. Area 27 Dependency
Quality controls shall cover the approved dimension architecture and attribute ownership boundaries.

## 9. Area 26 Dependency
Natural-key and surrogate-key mappings shall remain unique, stable, and traceable across historical versions.

## 10. Area 25 Dependency
SCD quality processing shall preserve the declared business grain.

## 11. Area 24 Dependency
Validation shall conform to the approved dimensional modeling and historical modeling patterns.

## 12. Area 23 Dependency
Profiling baselines shall provide reference measurements for detecting unexpected SCD population or attribute behavior.

## 13. Area 22 Dependency
SCD populations and historical transitions shall reconcile to governed upstream records and control totals.

## 14. Area 21 Dependency
Duplicate and record-resolution controls shall prevent duplicate business identities from generating invalid historical versions.

## 15. Area 20 Dependency
Quality comparisons shall operate on standardized values and distinguish true business changes from representation-only differences.

## 16. Area 19 Dependency
Transformation outputs shall preserve business meaning before SCD quality validation.

## 17. Area 07 Dependency
Validation shall remain traceable to the frozen source schema, data types, nullability expectations, and source contracts.

## 18. Historical Version Integrity Controls
Validate natural-key presence, surrogate-key uniqueness, one current version per natural key, valid effective dates, non-overlapping historical intervals, and consistent historical version identity.

## 19. Attribute Change Quality Controls
Validate that only attributes classified for historical tracking can create Type 2 versions. Type 1 or Type 0 changes shall not incorrectly create historical versions.

## 20. Reconciliation Controls
Reconcile source business identities to dimension identities, version counts, current-record counts, historical-record counts, and applicable control totals. Differences shall be explainable and evidenced.

## 21. Referential Integrity Controls
Validate that fact foreign keys resolve to valid dimension surrogate keys, including governed unknown or not-applicable members where appropriate.

## 22. Exception Classification
Classify exceptions including missing natural keys, duplicate current versions, overlapping effective intervals, invalid dates, missing surrogate mappings, unexpected attribute changes, unresolved members, and reconciliation differences.

## 23. Failure and Remediation Controls
SCD failures shall be isolated from accepted processing where feasible. Failed records or batches shall retain reason codes, evidence, lineage, ownership, remediation status, and reprocessing eligibility.

## 24. Audit, Lineage, Regression and Preservation
Every historical change decision shall be auditable to its source identity, comparison inputs, selected SCD behavior, resulting version, effective dates, and processing evidence. Regression and idempotency checks shall prevent repeated processing from creating unintended versions. Original source data shall remain unchanged.

## 25. Acceptance Criteria
Area 31.4 is acceptable when historical-version integrity, attribute-change controls, reconciliation, referential integrity, exception classification, failure remediation, auditability, lineage, regression, idempotency, and source-preservation controls are explicitly defined and all required upstream dependencies are preserved.

