# Area 39.3 — Data Mart Grain, Fact/Dimension Composition & Business Logic Boundaries

Status: Accepted & Frozen

## 1. Purpose
Define data mart grain, fact and dimension composition, aggregation boundaries, business-logic ownership, join controls, and analytical measure preservation for RetailIQ.

## 2. Area 39.2 Dependency
This artifact extends the frozen Data Mart Domain Structure & Model Organization and preserves its business-domain, model-organization, grain, cross-domain, dependency, and reusable-model boundaries.

## 3. Area 39.1 Dependency
Data mart composition shall comply with the approved Data Mart Architecture Foundation, including consumer boundaries, analytical purpose, source dependencies, performance, governance, and BI consumption.

## 4. Area 38 Dependency
Data mart composition shall preserve the approved transformation dependency graph, execution order, lineage, quality, reconciliation, and failure controls.

## 5. Area 37 Dependency
Data mart models shall comply with approved analytics engineering contracts, naming, testing, documentation, quality, ownership, and controlled-change standards.

## 6. Area 36 Dependency
Approved Intermediate/Core transformations shall remain the governed source of reusable business logic consumed by marts.

## 7. Area 35 Dependency
Incremental mart processing shall preserve approved model identity, key matching, merge, idempotency, reconciliation, and recovery controls.

## 8. Area 34 Dependency
Mart refresh behavior shall preserve approved full-refresh, incremental, watermark, replay, backfill, and escalation strategies.

## 9. Area 33 Dependency
Mart transformations shall remain within the approved ELT architecture and downstream transformation boundaries.

## 10. Area 32 Dependency
Historical and late-arriving data shall retain approved temporal semantics within mart outputs.

## 11. Area 31 Dependency
SCD dimensions shall provide historically correct dimensional context where mart analysis requires historical state.

## 12. Area 30 Dependency
Conformed and role-playing dimensions shall retain consistent keys and analytical meaning across marts.

## 13. Area 29 Dependency
Fact measures shall preserve approved business grain, additive behavior, and aggregation semantics.

## 14. Area 28 Dependency
Fact and dimension composition shall preserve their approved architectural responsibilities.

## 15. Area 27 Dependency
Dimension attributes and relationships shall follow approved dimension architecture.

## 16. Area 26 Dependency
Natural and surrogate keys shall retain their approved identity and relationship semantics.

## 17. Area 25 Dependency
Every mart model shall declare a precise business grain and prevent accidental grain multiplication or reduction.

## 18. Area 24 Dependency
Mart composition shall implement the approved dimensional modeling strategy.

## 19. Area 23 Dependency
Mart outputs shall support profiling and analytical baseline validation.

## 20. Area 22 Dependency
Mart composition shall support population, key, measure, and business-total reconciliation.

## 21. Area 21 Dependency
Approved duplicate and record-resolution behavior shall remain preserved in mart inputs.

## 22. Area 20 Dependency
Mart models shall consume standardized and normalized analytical inputs.

## 23. Mart Grain Definition
Every mart model shall have one explicit declared business grain. The grain shall describe what one row represents in business terms and shall be documented before measure or aggregation logic is finalized.

## 24. Grain Preservation
Joins, filters, unions, aggregations, and derived transformations shall preserve the declared grain unless an intentional grain transition is explicitly documented.

## 25. Fact Composition
Facts shall provide measurable business events or periodic analytical states appropriate to the mart use case. Fact composition shall retain approved measures, event relationships, and additive behavior.

## 26. Dimension Composition
Dimensions shall provide descriptive analytical context for facts and mart consumers. Dimension joins shall use approved keys and preserve relationship integrity.

## 27. Fact-to-Dimension Join Controls
Fact-to-dimension joins shall validate key compatibility, expected cardinality, surrogate-key behavior, unknown-member handling, and absence of unintended row multiplication.

## 28. Multiple-Fact Composition
When a mart combines multiple fact sources, each fact's grain shall be documented separately. Direct joins between incompatible fact grains shall be avoided unless a controlled bridge, aggregation, or other approved mechanism preserves analytical correctness.

## 29. Measure Aggregation Boundary
Measures shall document whether they are additive, semi-additive, or non-additive and shall define valid aggregation dimensions and restrictions.

## 30. Derived Measure Boundary
Derived measures shall use governed upstream measures or documented business rules. Equivalent business calculations shall not be independently reimplemented across marts without controlled ownership.

## 31. Business Logic Ownership
Reusable enterprise business rules shall remain owned by Intermediate/Core or another explicitly governed layer. Mart-specific business logic shall be limited to domain-specific analytical composition and documented calculations.

## 32. Cross-Domain Composition
Cross-domain marts shall explicitly document domain joins, relationship cardinality, grain compatibility, filtering, aggregation, and business purpose before combining data.

## 33. Double-Counting Prevention
Mart design shall explicitly identify repeated-event risks, multi-payment orders, multi-item orders, repeated reviews, many-to-many relationships, and other conditions capable of inflating measures.

## 34. Acceptance Criteria
Area 39.3 is accepted when mart grain, grain preservation, fact composition, dimension composition, join controls, multiple-fact boundaries, measure aggregation, derived measures, business-logic ownership, cross-domain composition, and double-counting prevention are explicitly documented and validated.

