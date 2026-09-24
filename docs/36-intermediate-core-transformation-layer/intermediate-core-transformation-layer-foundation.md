# Area 36.1 — Intermediate / Core Transformation Layer Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the architecture, responsibilities, transformation boundaries, dependencies, quality controls, and engineering standards for the Intermediate / Core transformation layer of RetailIQ.

## 2. Area 35 Dependency
Intermediate/Core models shall consume governed incremental model outputs and preserve approved key, grain, change-application, reconciliation, recovery, and idempotency controls.

## 3. Area 34 Dependency
Intermediate/Core processing shall respect the approved full-refresh and incremental strategy, including change detection, watermarks, processing eligibility, replay, recovery, and reconciliation.

## 4. Area 33 Dependency
The Intermediate/Core layer shall implement the approved ELT architecture and remain within its documented transformation responsibility.

## 5. Area 32 Dependency
Historical records, late-arriving records, temporal corrections, and backfills shall remain traceable through the Intermediate/Core layer.

## 6. Area 31 Dependency
SCD-related historical context shall be preserved when Intermediate/Core transformations consume dimension history.

## 7. Area 30 Dependency
Conformed and role-playing dimension relationships shall remain consistent across Intermediate/Core transformations.

## 8. Area 29 Dependency
Intermediate/Core transformations shall preserve fact grain and measure semantics before downstream fact construction.

## 9. Area 28 Dependency
The Intermediate/Core layer shall prepare governed inputs for approved fact and dimension structures without duplicating their ownership responsibilities.

## 10. Area 27 Dependency
Dimension-specific transformation logic shall respect approved dimension ownership and attribute classification.

## 11. Area 26 Dependency
Natural-key and surrogate-key semantics shall remain stable throughout Intermediate/Core transformations.

## 12. Area 25 Dependency
Intermediate/Core transformations shall explicitly preserve the approved business grain and prevent unintended row multiplication.

## 13. Area 24 Dependency
Transformation logic shall remain consistent with the approved dimensional modeling strategy.

## 14. Area 23 Dependency
Intermediate/Core outputs shall remain measurable against established profiling baselines.

## 15. Area 22 Dependency
Transformation outputs shall support source-to-target and layer-to-layer reconciliation.

## 16. Area 21 Dependency
Duplicate and record-resolution outcomes shall be preserved and shall not be silently reversed by Intermediate/Core transformations.

## 17. Area 20 Dependency
Intermediate/Core models shall consume standardized and normalized data and shall not reintroduce uncontrolled representation differences.

## 18. Layer Responsibility
The Intermediate/Core layer shall combine, enrich, derive, reshape, and prepare governed business-ready analytical structures between staging and downstream facts, dimensions, and data marts.

## 19. Transformation Boundary
Source acquisition, raw preservation, basic staging standardization, final dimensional modeling, business data marts, and BI presentation logic shall remain outside the Intermediate/Core layer unless explicitly assigned by the approved architecture.

## 20. Model Design Principles
Intermediate/Core models shall be modular, deterministic, reusable, dependency-aware, testable, traceable, and aligned with declared business grain. Logic shall avoid unnecessary duplication and shall expose reusable business transformations to downstream models.

## 21. Business Meaning Preservation
Transformations shall preserve business definitions, keys, measures, timestamps, statuses, relationships, and analytical meaning. Derived fields shall have documented definitions and deterministic calculation rules.

## 22. Dependency and Execution Controls
Intermediate/Core models shall execute only after required upstream inputs and quality gates succeed. Dependency ordering shall prevent circular references and consumption of incomplete upstream states.

## 23. Quality, Reconciliation and Idempotency
Intermediate/Core models shall define structural, key, grain, nullability, referential-integrity, transformation, and applicable business-rule validations. Reprocessing the same governed source boundary shall produce an idempotent result unless an approved correction changes the expected state.

## 24. Audit, Lineage, Change Control and Preservation
Intermediate/Core transformations shall retain model identity, source dependencies, transformation ownership, processing context, lineage, quality outcomes, reconciliation evidence, exceptions, and change history. Upstream source and accepted historical states shall not be silently mutated.

## 25. Acceptance Criteria
Area 36.1 is accepted when the Intermediate/Core layer purpose, responsibilities, transformation boundaries, business meaning, dependency execution, quality, reconciliation, idempotency, audit, lineage, change control, historical preservation, and all required upstream dependencies are explicitly governed.

