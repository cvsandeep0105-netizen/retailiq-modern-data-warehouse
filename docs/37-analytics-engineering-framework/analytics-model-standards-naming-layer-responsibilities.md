# Area 37.2 — Analytics Model Standards, Naming & Layer Responsibilities

Status: Accepted & Frozen

## 1. Purpose
Define consistent standards for analytics model naming, structure, ownership, layering, dependencies, and transformation responsibilities.

## 2. Area 37.1 Dependency
This standard extends the Analytics Engineering Framework Foundation and preserves its requirements for modularity, contracts, testing, documentation, lineage, governance, reproducibility, and controlled change.

## 3. Area 36 Dependency
Analytics models shall consume Intermediate/Core outputs according to the approved transformation boundaries and shall not duplicate or bypass governed core business logic without documented justification.

## 4. Area 35 Dependency
Incremental analytical models shall preserve approved key, merge, change-application, idempotency, reconciliation, and recovery controls.

## 5. Area 34 Dependency
Model execution shall comply with approved full-refresh, incremental, watermark, replay, and backfill strategies.

## 6. Area 33 Dependency
All analytical models shall remain within the approved ELT dependency flow and transformation responsibilities.

## 7. Area 32 Dependency
Historical and late-arriving records shall retain their approved temporal and correction semantics when consumed by analytical models.

## 8. Area 31 Dependency
SCD-controlled dimensions shall preserve historical version, effective-date, and current-state semantics.

## 9. Area 30 Dependency
Conformed and role-playing dimensions shall retain consistent naming, identity, and analytical usage across downstream models.

## 10. Area 29 Dependency
Fact models shall preserve approved grain and measure semantics when exposed to analytical consumers.

## 11. Area 28 Dependency
Fact and dimension responsibilities shall remain separated according to the approved fact architecture.

## 12. Area 27 Dependency
Dimension models shall follow the approved dimension architecture and attribute ownership boundaries.

## 13. Area 26 Dependency
Natural-key and surrogate-key usage shall remain consistent with approved identity rules.

## 14. Area 25 Dependency
Every model shall explicitly identify its business grain and shall prevent accidental grain changes through joins, filters, or aggregations.

## 15. Area 24 Dependency
Model organization shall implement the approved dimensional modeling strategy.

## 16. Area 23 Dependency
Model standards shall support profiling, baseline comparison, anomaly detection, and regression analysis.

## 17. Area 22 Dependency
Model standards shall support population, key, measure, and reconciliation controls.

## 18. Area 21 Dependency
Resolved duplicate and record-identity decisions shall be preserved and not silently reintroduced downstream.

## 19. Area 20 Dependency
Models shall consume standardized and normalized data according to the approved transformation standards.

## 20. Layer Responsibility Standards
Raw and landing layers preserve source data. Staging prepares source-aligned structures. Intermediate/Core models implement reusable business transformations. Dimensions and facts implement analytical structures. Data marts organize business-consumption outputs. Metrics and semantic models expose governed business meaning. BI-ready outputs serve approved analytical consumers.

## 21. Naming Standards
Model names shall be descriptive, stable, deterministic, lowercase where technically supported, and consistent within the repository. Names shall communicate business meaning and model responsibility rather than implementation details. Abbreviations shall be controlled and documented.

## 22. Column Naming Standards
Column names shall use consistent business terminology, avoid ambiguous abbreviations, preserve approved key semantics, distinguish identifiers from measures, and use explicit names for dates, timestamps, status attributes, quantities, monetary values, and derived metrics.

## 23. Model Structure Standards
Each model shall have a clearly defined purpose, declared grain, inputs, outputs, keys, transformation responsibilities, quality expectations, owner, downstream dependencies, and documentation boundary.

## 24. Dependency and Reuse Standards
Models shall reference approved upstream models rather than duplicating transformation logic. Dependencies shall form an intentional directed graph with no unexplained circular dependencies. Reusable business logic shall have a single governed ownership location where practical.

## 25. Acceptance Criteria
Area 37.2 is accepted when layer responsibilities, model naming, column naming, model structure, business grain, dependency management, reusable logic, key semantics, historical behavior, and upstream dependency controls are explicitly documented and validated.

