# Area 36.4 — Intermediate/Core Transformation Quality, Reconciliation & Exception Controls

Status: Accepted & Frozen

## 1. Purpose
Define production-grade quality, reconciliation, exception, failure, recovery, and audit controls for the Intermediate/Core transformation layer.

## 2. Area 36.1 Dependency
Quality controls shall operate within the approved Intermediate/Core foundation and transformation boundaries.

## 3. Area 36.2 Dependency
Model structure, input/output contracts, grain, keys, joins, and transformation responsibilities shall be validated.

## 4. Area 36.3 Dependency
Core business transformations, reusable logic, business rules, calculations, joins, and aggregations shall be validated before downstream acceptance.

## 5. Area 35 Dependency
Incremental model outputs consumed by Intermediate/Core transformations shall retain approved quality, key, change-application, and idempotency controls.

## 6. Area 34 Dependency
Transformation validation shall respect incremental boundaries, watermark context, replay, recovery, and reconciliation controls.

## 7. Area 33 Dependency
Quality and reconciliation shall follow the approved ELT dependency flow.

## 8. Area 32 Dependency
Late-arriving records, historical corrections, and backfills shall remain distinguishable and traceable.

## 9. Area 31 Dependency
SCD historical context and effective-date integrity shall be validated where applicable.

## 10. Area 30 Dependency
Conformed and role-playing dimension relationships shall remain consistent after transformation.

## 11. Area 29 Dependency
Fact grain and measure preparation shall be validated before downstream fact construction.

## 12. Area 28 Dependency
Fact and dimension inputs shall remain structurally consistent with approved architecture.

## 13. Area 27 Dependency
Dimension transformation rules shall remain within approved ownership boundaries.

## 14. Area 26 Dependency
Natural-key and surrogate-key integrity shall be validated after transformation.

## 15. Area 25 Dependency
Business grain shall be validated before and after transformation.

## 16. Area 24 Dependency
Dimensional relationships shall remain valid after Intermediate/Core processing.

## 17. Area 23 Dependency
Transformation outputs shall be compared against profiling baselines for unexpected population, null, distribution, and value changes.

## 18. Area 22 Dependency
Layer-to-layer and source-to-target reconciliation shall validate transformation populations and analytical results.

## 19. Area 21 Dependency
Duplicate and record-resolution outcomes shall remain preserved through transformations.

## 20. Area 20 Dependency
Standardization and normalization assumptions shall be validated and shall not be silently reversed.

## 21. Structural and Contract Quality
Each Intermediate/Core model shall validate expected columns, data types, required fields, key relationships, nullability expectations, and output contract compatibility before downstream consumption.

## 22. Grain, Join and Business-Rule Quality
Each transformation shall validate declared grain, join cardinality, duplicate behavior, derived-field rules, aggregation logic, status mappings, date logic, and applicable business definitions.

## 23. Reconciliation and Analytical Quality
Transformation populations shall reconcile from controlled inputs to outputs. Applicable counts, quantities, monetary measures, and derived analytical measures shall reconcile at the declared grain and shall prevent double counting.

## 24. Exception, Recovery, Audit and Idempotency
Exceptions shall be classified by source, schema, key, grain, join, transformation, business-rule, reconciliation, or operational cause. Failed transformations shall support safe retry or controlled recovery without corrupting accepted states. Execution, exceptions, reconciliation results, lineage, and remediation shall remain auditable. Reprocessing the same governed input boundary shall be idempotent.

## 25. Acceptance Criteria
Area 36.4 is accepted when structural and contract quality, grain and join validation, business-rule validation, reconciliation, analytical quality, exception classification, recovery, audit, lineage, idempotency, and all required dependencies are explicitly governed.

