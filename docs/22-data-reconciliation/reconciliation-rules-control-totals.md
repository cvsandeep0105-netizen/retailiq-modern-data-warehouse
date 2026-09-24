# Area 22.2 — Reconciliation Rules & Control Totals

Status: Accepted & Frozen

## 1. Purpose
Define detailed reconciliation rules and control-total standards for validating data movement and transformation across RetailIQ processing layers.

## 2. Area 22.1 Foundation Dependency
Rules shall implement the reconciliation foundation defined in Area 22.1.

## 3. Area 06 Relationship Dependency
Relationship reconciliation shall respect the approved keys, cardinalities, and documented exceptions from Area 06.

## 4. Area 07 Contract Dependency
Reconciliation rules shall validate against approved source contracts and schema expectations from Area 07.

## 5. Area 17 Raw Validation Dependency
Raw-layer control totals shall use the accepted and rejected populations established through Area 17.

## 6. Area 18 Staging Dependency
Staging reconciliation shall compare expected source-to-staging populations and approved structural mappings.

## 7. Area 19 Transformation Dependency
Transformation reconciliation shall distinguish expected transformations from unexplained record or measure differences.

## 8. Area 20 Standardization Dependency
Standardization effects shall be reconciled without treating approved representation changes as data loss.

## 9. Area 21 Deduplication Dependency
Deduplication reconciliation shall distinguish source duplicates, resolved records, preserved records, and intentionally non-merged records.

## 10. Row Count Reconciliation
Row counts shall be captured at defined processing boundaries and compared using explicit expected-difference rules.

## 11. Distinct Key Reconciliation
Distinct business and technical key counts shall be compared where the key remains valid across the processing boundary.

## 12. Composite Key Reconciliation
Composite keys shall be reconciled where entity grain requires multiple attributes for record identity.

## 13. Relationship Reconciliation
Foreign-key and relationship populations shall be reconciled against their approved parent populations and documented exceptions.

## 14. Control Total Definition
Each material reconciliation shall identify source total, target total, expected adjustment, actual difference, tolerance, and final reconciliation state.

## 15. Financial Measure Reconciliation
Applicable monetary measures including price, freight, payment value, and derived financial quantities shall be reconciled at their documented grain.

## 16. Quantity Reconciliation
Item and order quantities shall be reconciled at the appropriate business grain without incorrectly equating order counts with item counts.

## 17. Temporal Reconciliation
Date and timestamp populations shall be reconciled for valid records, nullability, boundary dates, and expected lifecycle differences.

## 18. Nullability Reconciliation
Null counts shall be compared where nullability is contractually or analytically meaningful, while approved transformation-generated nulls remain explainable.

## 19. Duplicate Reconciliation
Duplicate populations shall be reconciled against Area 21 detection and resolution outcomes so legitimate source duplicates are not silently interpreted as processing defects.

## 20. Tolerance Rules
Every tolerance shall have an explicit business or engineering rationale. Unexplained differences shall not be hidden through arbitrary tolerances.

## 21. Exception Classification
Reconciliation differences shall be classified as expected transformation, source exception, contract exception, processing defect, unresolved difference, or accepted boundary condition.

## 22. Evidence Capture
Each reconciliation execution shall retain control identifiers, source and target populations, totals, differences, tolerance, result, exception classification, and execution evidence.

## 23. Idempotency and Repeatability
Repeated reconciliation of unchanged inputs shall produce consistent control results and shall not mutate source data.

## 24. Technology-Neutral Boundary
These reconciliation rules define logical controls and do not prescribe a specific database, warehouse engine, orchestration platform, or BI technology.

## 25. Acceptance Criteria
Area 22.2 is acceptable when row counts, keys, relationships, measures, temporal fields, nullability, duplicates, tolerances, exceptions, evidence, and repeatability rules are explicitly defined and traceable to the frozen upstream Areas.

