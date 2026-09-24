# Area 39.1 — Data Mart Architecture Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the architectural foundation for RetailIQ Data Marts, including business-domain organization, analytical consumption boundaries, grain, source dependencies, metric readiness, reuse, governance, and BI consumption.

## 2. Area 38 Dependency
Data marts shall consume the approved Transformation Dependency Graph and preserve dependency direction, execution ordering, lineage, quality, reconciliation, failure handling, and controlled transformation boundaries.

## 3. Area 37 Dependency
Data marts shall comply with the frozen Analytics Engineering Framework, including model contracts, naming standards, layer responsibilities, testing, documentation, quality, lineage, CI/CD, and controlled change.

## 4. Area 36 Dependency
Data marts shall consume approved Intermediate/Core transformations and shall not bypass governed reusable business logic without documented architectural justification.

## 5. Area 35 Dependency
Incremental data marts shall preserve approved model identity, key matching, merge, change application, idempotency, reconciliation, and recovery behavior.

## 6. Area 34 Dependency
Data mart processing shall comply with approved full-refresh, incremental, watermark, replay, backfill, and escalation strategies.

## 7. Area 33 Dependency
Data marts shall occupy the approved downstream position in the ELT architecture after governed dimensions and facts where applicable.

## 8. Area 32 Dependency
Historical and late-arriving records shall preserve their approved temporal semantics when consumed by data marts.

## 9. Area 31 Dependency
SCD-controlled dimensions shall provide historically correct dimension context to data marts where historical analysis requires it.

## 10. Area 30 Dependency
Conformed and role-playing dimensions shall provide consistent analytical context across data marts.

## 11. Area 29 Dependency
Fact measures consumed by data marts shall retain their approved business grain, additive behavior, and aggregation semantics.

## 12. Area 28 Dependency
Fact and dimension architectural responsibilities shall remain preserved within data mart construction.

## 13. Area 27 Dependency
Dimension structures and attributes used by data marts shall follow approved dimension architecture.

## 14. Area 26 Dependency
Natural keys and surrogate keys shall retain their approved identity and relationship semantics in data mart models.

## 15. Area 25 Dependency
Every data mart shall have an explicitly documented business grain and shall prevent uncontrolled grain multiplication or aggregation drift.

## 16. Area 24 Dependency
Data mart architecture shall implement the approved dimensional modeling strategy for analytical consumption.

## 17. Area 23 Dependency
Data mart design shall support profiling baselines and measurable analytical quality expectations.

## 18. Area 22 Dependency
Data marts shall support reconciliation between upstream facts/dimensions and downstream business-facing populations and measures.

## 19. Area 21 Dependency
Data marts shall preserve approved duplicate and record-resolution behavior from upstream models.

## 20. Area 20 Dependency
Data marts shall consume standardized and normalized analytical inputs according to approved transformation standards.

## 21. Data Mart Definition
A data mart is a governed analytical data product organized around a defined business domain, analytical purpose, consumer population, grain, measures, dimensions, and documented business rules.

## 22. Business-Domain Organization
Data marts shall be organized around stable business analytical domains rather than individual source tables. Candidate domains include sales, orders, customers, products, sellers, payments, fulfillment, and customer experience.

## 23. Consumer Boundary
Each data mart shall identify its intended analytical consumers, primary use cases, expected access patterns, and supported analytical questions.

## 24. Grain Boundary
Each mart shall declare its business grain explicitly. Transformations, joins, aggregations, and derived measures shall preserve or intentionally change that grain only through documented rules.

## 25. Source Dependency Boundary
Data marts shall consume governed dimensions, facts, intermediate models, or other approved analytical products rather than directly depending on uncontrolled raw source structures.

## 26. Fact and Dimension Consumption
Data marts may combine approved facts and dimensions to answer domain-specific analytical questions while preserving measure definitions, dimension semantics, and relationship integrity.

## 27. Mart Reusability
Reusable business logic shall remain owned by the appropriate upstream model. Data marts shall focus on domain-specific analytical composition rather than duplicating common transformations.

## 28. Analytical Performance Boundary
Data marts shall be designed for predictable analytical access, appropriate aggregation, efficient filtering, controlled joins, and consumer-oriented query patterns.

## 29. Governance Boundary
Data marts shall have defined ownership, documentation, lineage, quality expectations, access boundaries, change-control requirements, and retention expectations where applicable.

## 30. BI Consumption Boundary
Data marts shall provide governed analytical inputs for metrics, semantic models, dashboards, reporting, self-service analysis, and BI-ready products without silently redefining authoritative business logic.

## 31. Acceptance Criteria
Area 39.1 is accepted when the data mart purpose, business-domain organization, consumer boundary, grain, source dependencies, fact/dimension consumption, reuse, performance, governance, BI boundary, and upstream dependencies are explicitly documented and validated.

