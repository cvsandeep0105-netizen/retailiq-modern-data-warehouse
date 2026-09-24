# Area 36.2 — Intermediate/Core Model Structure & Transformation Responsibilities

Status: Accepted & Frozen

## 1. Purpose
Define the logical structure of Intermediate/Core models and establish clear transformation responsibilities between staging inputs and downstream analytical models.

## 2. Area 36.1 Dependency
Model structure shall implement the approved Intermediate/Core foundation, including layer responsibility, transformation boundaries, business meaning, dependency execution, quality, reconciliation, idempotency, lineage, and preservation.

## 3. Area 35 Dependency
Intermediate/Core models shall consume governed incremental model outputs and preserve approved change-application and key-resolution behavior.

## 4. Area 34 Dependency
Model execution shall respect approved full-refresh, incremental, watermark, replay, recovery, and reconciliation controls.

## 5. Area 33 Dependency
Model structure shall remain consistent with the approved ELT architecture and dependency flow.

## 6. Area 32 Dependency
Model structure shall preserve late-arriving records, historical corrections, temporal context, and controlled backfills.

## 7. Area 31 Dependency
Historical dimension context and SCD version semantics shall remain available to transformations that require them.

## 8. Area 30 Dependency
Conformed and role-playing dimensions shall use consistent identity and relationship semantics.

## 9. Area 29 Dependency
Intermediate/Core models shall preserve fact grain and measure definitions before downstream fact construction.

## 10. Area 28 Dependency
Model structure shall provide governed inputs to approved fact and dimension structures without taking ownership of their final modeling responsibilities.

## 11. Area 27 Dependency
Dimension-related transformations shall respect approved dimension architecture and attribute ownership.

## 12. Area 26 Dependency
Natural-key and surrogate-key semantics shall remain consistent across Intermediate/Core models.

## 13. Area 25 Dependency
Every Intermediate/Core model shall declare its business grain and preserve that grain through transformation.

## 14. Area 24 Dependency
Model structures shall remain compatible with the approved dimensional modeling strategy.

## 15. Area 23 Dependency
Intermediate/Core model outputs shall remain measurable against established profiling baselines.

## 16. Area 22 Dependency
Model outputs shall support layer-to-layer and source-to-target reconciliation.

## 17. Area 21 Dependency
Resolved record identity and duplicate controls shall remain preserved across model boundaries.

## 18. Area 20 Dependency
Intermediate/Core transformations shall consume standardized and normalized inputs and shall not reintroduce uncontrolled source representations.

## 19. Model Structure
Intermediate/Core models shall be organized by reusable business transformation responsibility rather than by arbitrary technical convenience. Models may represent reusable joins, enriched entities, business-ready intermediate relationships, derived attributes, controlled aggregations, or reusable calculation foundations.

## 20. Input and Output Contracts
Each model shall define its upstream inputs, expected schemas, key relationships, business grain, transformation purpose, output structure, downstream consumers, and applicable quality expectations.

## 21. Transformation Responsibility
Intermediate/Core models shall perform reusable business transformations such as controlled joins, enrichment, derivation, normalization of analytical relationships, reusable calculations, and preparation of downstream dimensional or mart structures. Presentation-specific BI logic shall remain downstream.

## 22. Model Decomposition and Reusability
Complex transformations shall be decomposed into logically coherent models when separation improves dependency clarity, testing, reuse, lineage, or failure isolation. Excessive fragmentation that creates unnecessary dependencies shall be avoided.

## 23. Grain, Key and Join Controls
Each model shall explicitly document its grain and join cardinality. One-to-many joins shall be controlled to prevent accidental row multiplication, measure inflation, duplicate business entities, or loss of records.

## 24. Dependency, Quality and Change Controls
Model dependencies shall be acyclic and deterministic. Each model shall support quality validation, reconciliation, idempotent execution, lineage, auditability, and controlled change management. Changes shall preserve downstream contracts or trigger governed contract-impact assessment.

## 25. Acceptance Criteria
Area 36.2 is accepted when Intermediate/Core model structure, input/output contracts, transformation responsibilities, decomposition, reusability, grain and join controls, dependency execution, quality, reconciliation, lineage, idempotency, and change-control boundaries are explicitly governed.

