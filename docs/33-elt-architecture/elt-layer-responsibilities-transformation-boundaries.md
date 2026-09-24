# Area 33.2 — ELT Layer Responsibilities & Transformation Boundaries

Status: Accepted & Frozen

## 1. Purpose
Define explicit responsibilities, transformation ownership, input/output boundaries, and prohibited responsibilities for each RetailIQ ELT layer.

## 2. Area 33.1 Dependency
This artifact implements the logical ELT flow and transformation boundaries established in Area 33.1.

## 3. Area 32 Dependency
Historical and late-arriving record controls shall remain applicable across all ELT layers.

## 4. Area 31 Dependency
SCD processing shall remain a governed downstream responsibility and shall not be duplicated inconsistently across layers.

## 5. Area 30 Dependency
Conformed and role-playing dimension semantics shall be preserved through every transformation boundary.

## 6. Area 29 Dependency
Fact-grain and measure definitions shall not be changed implicitly by upstream transformations.

## 7. Area 28 Dependency
Fact and dimension construction shall remain within the approved analytical modeling boundary.

## 8. Area 27 Dependency
Dimension attribute ownership shall remain aligned with the approved dimension architecture.

## 9. Area 26 Dependency
Natural-key and surrogate-key responsibilities shall remain explicit and traceable.

## 10. Area 25 Dependency
Business grain shall remain stable across transformations unless an explicitly documented model changes the grain.

## 11. Area 24 Dependency
Dimensional modeling rules shall govern analytical structures rather than being redefined inside individual transformation steps.

## 12. Area 23 Dependency
Profiling baselines shall support validation at appropriate transformation boundaries.

## 13. Area 22 Dependency
Control totals and reconciliation shall be preserved between major ELT layers.

## 14. Area 21 Dependency
Duplicate and record-resolution logic shall have an explicit ownership boundary and shall not be silently repeated.

## 15. Area 20 Dependency
Standardization and normalization responsibilities shall be distinguishable from analytical business transformations.

## 16. Area 19 Dependency
Staging transformation rules shall remain upstream inputs to reusable analytical transformations.

## 17. Area 18 Dependency
Staging remains the governed boundary for source mapping and controlled staging outputs.

## 18. Raw and Landing Responsibility
The Raw/Landing layer preserves source data and ingestion evidence. It shall not contain irreversible business transformations that prevent source reconstruction.

## 19. Staging Responsibility
The Staging layer performs controlled source mapping, structural alignment, standardization, normalization, and source-oriented validation. It shall preserve source meaning and remain close to source structure.

## 20. Intermediate/Core Responsibility
The Intermediate/Core layer contains reusable business transformations, cross-source integration, governed derived attributes, reusable joins, and analytical preparation. It shall not become an uncontrolled collection of presentation-specific logic.

## 21. Dimension and Fact Responsibility
Dimension models establish governed analytical entities and historical behavior. Fact models establish approved business grains and measures. These models shall consume governed upstream transformations rather than embedding unrelated ingestion logic.

## 22. Data Mart Responsibility
Data marts shall organize approved facts and dimensions into consumption-oriented business structures. Mart logic shall remain aligned with declared business metrics and shall not redefine core business meaning without governance.

## 23. Metrics, Semantic and BI-Ready Responsibility
Metrics and semantic structures shall expose governed business definitions, dimensions, measures, filters, and analytical relationships. BI-ready products shall optimize consumption without bypassing governed analytical models.

## 24. Cross-Layer Controls and Prohibited Leakage
Each layer shall have explicit input/output contracts, ownership, lineage, quality checks, reconciliation expectations, and failure boundaries. Raw ingestion logic shall not leak into marts; presentation-specific logic shall not redefine core facts; and identical business logic shall not be independently reimplemented across layers without an approved reason.

## 25. Acceptance Criteria
Area 33.2 is accepted when responsibilities for Raw/Landing, Staging, Intermediate/Core, Dimensions/Facts, Data Marts, Metrics/Semantic, and BI-Ready layers are explicitly defined; transformation leakage is controlled; upstream/downstream boundaries are traceable; and all required dependencies are preserved.

