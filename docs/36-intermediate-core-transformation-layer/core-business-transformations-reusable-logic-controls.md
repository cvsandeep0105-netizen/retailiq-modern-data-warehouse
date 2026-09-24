# Area 36.3 — Core Business Transformations & Reusable Logic Controls

Status: Accepted & Frozen

## 1. Purpose
Define governed business transformations and reusable analytical logic within the Intermediate/Core layer while preserving business meaning, grain, keys, measures, lineage, and downstream contracts.

## 2. Area 36.1 Dependency
Business transformations shall operate within the approved Intermediate/Core responsibilities and transformation boundaries.

## 3. Area 36.2 Dependency
Reusable logic shall follow the approved model structure, input/output contracts, decomposition, grain, key, and join controls.

## 4. Area 35 Dependency
Transformations shall consume governed incremental model outputs and preserve approved change-application and idempotency behavior.

## 5. Area 34 Dependency
Transformation execution shall respect approved incremental boundaries, watermarks, replay, recovery, and reconciliation controls.

## 6. Area 33 Dependency
Business transformations shall remain within the approved ELT dependency flow.

## 7. Area 32 Dependency
Late-arriving and historical records shall retain their correct business-effective context through transformations.

## 8. Area 31 Dependency
SCD historical context shall be preserved when transformations use dimension attributes or historical versions.

## 9. Area 30 Dependency
Conformed and role-playing dimensions shall retain consistent business identity and relationship semantics.

## 10. Area 29 Dependency
Derived measures shall preserve the approved fact grain and measure definitions.

## 11. Area 28 Dependency
Core transformations shall prepare governed inputs for facts and dimensions without taking over their final model ownership.

## 12. Area 27 Dependency
Dimension-related business logic shall respect approved attribute ownership and dimension architecture.

## 13. Area 26 Dependency
Natural-key and surrogate-key semantics shall remain stable throughout reusable transformations.

## 14. Area 25 Dependency
Every transformation shall preserve or explicitly document its resulting business grain.

## 15. Area 24 Dependency
Business transformations shall remain consistent with approved dimensional modeling principles.

## 16. Area 23 Dependency
Transformation outputs shall remain measurable against profiling baselines.

## 17. Area 22 Dependency
Reusable transformations shall support layer-to-layer reconciliation and controlled exception handling.

## 18. Area 21 Dependency
Resolved record identity and duplicate controls shall remain preserved through reusable business logic.

## 19. Area 20 Dependency
Transformations shall consume standardized and normalized inputs and shall produce consistently governed outputs.

## 20. Core Business Transformation Categories
Core transformations may include governed entity enrichment, controlled joins, business classifications, derived attributes, reusable date and status logic, standardized analytical flags, controlled aggregations, relationship resolution, and reusable measure preparation.

## 21. Reusable Logic Principles
Reusable logic shall have one authoritative definition where practical. Repeated business rules shall not be independently reimplemented across downstream models when centralization improves consistency, testing, lineage, and change control.

## 22. Business Rule and Calculation Controls
Each reusable rule or calculation shall have a documented business definition, input fields, output fields, null behavior, boundary conditions, applicable grain, and expected behavior for invalid or exceptional inputs.

## 23. Join, Aggregation and Grain Controls
Joins shall have explicit cardinality expectations. Aggregations shall occur only at a declared grain. Many-to-many relationships shall be resolved through governed intermediate logic before measures are calculated to prevent duplication and inflation.

## 24. Quality, Lineage, Idempotency and Change Control
Reusable transformations shall be testable, deterministic, traceable to their inputs, and idempotent for the same governed input boundary. Changes shall undergo impact assessment, regression validation, reconciliation, and controlled documentation updates.

## 25. Acceptance Criteria
Area 36.3 is accepted when core business transformation categories, reusable logic principles, business-rule definitions, calculation controls, join and aggregation boundaries, grain preservation, quality, lineage, idempotency, reconciliation, and change-control requirements are explicitly governed.

