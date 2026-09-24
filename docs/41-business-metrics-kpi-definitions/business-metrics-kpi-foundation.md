# Area 41.1 — Business Metrics & KPI Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the foundation for governed RetailIQ business metrics and KPIs, including metric ownership, business meaning, grain, calculation boundaries, dimensional context, aggregation behavior, lineage, reconciliation, quality, semantic consumption, and controlled change.

## 2. Area 40 Dependency
Business metrics shall consume approved Business Data Marts and shall preserve their declared grains, facts, dimensions, measures, quality controls, reconciliation boundaries, lineage, and business-domain ownership.

## 3. Area 39 Dependency
Metrics shall preserve the frozen Data Mart Architecture, including grain, fact and dimension composition, business-logic ownership, cross-domain controls, quality, reconciliation, and double-counting prevention.

## 4. Area 38 Dependency
Metric dependencies shall follow the approved transformation dependency graph and preserve execution, lineage, failure, reconciliation, and recovery controls.

## 5. Area 37 Dependency
Metric definitions shall comply with approved analytics engineering contracts, documentation, testing, ownership, regression, and controlled-change standards.

## 6. Area 36 Dependency
Reusable metric inputs shall consume governed Intermediate/Core transformations through approved downstream models rather than duplicating upstream business logic.

## 7. Area 35 Dependency
Metrics based on incrementally processed models shall preserve approved model identity, change application, idempotency, reconciliation, and recovery behavior.

## 8. Area 34 Dependency
Metric refresh behavior shall preserve approved full-refresh, incremental, watermark, replay, backfill, and escalation strategies.

## 9. Area 33 Dependency
Metric construction shall remain within the approved ELT architecture and downstream analytical transformation boundaries.

## 10. Area 32 Dependency
Metrics requiring historical or late-arriving data shall preserve approved temporal semantics.

## 11. Area 31 Dependency
Historical metrics shall use approved SCD behavior where historical dimension context affects metric interpretation.

## 12. Area 30 Dependency
Metrics shall use conformed and role-playing dimensions consistently across analytical domains.

## 13. Area 29 Dependency
Metric calculations shall preserve approved fact grain, measure definitions, additive behavior, and aggregation semantics.

## 14. Area 28 Dependency
Metric inputs shall preserve approved fact and dimension architectural responsibilities.

## 15. Area 27 Dependency
Dimension attributes used for KPI slicing shall follow approved dimension architecture.

## 16. Area 26 Dependency
Metric relationships shall use approved natural and surrogate key semantics.

## 17. Area 25 Dependency
Every metric shall declare the grain at which its calculation is valid.

## 18. Area 24 Dependency
Metrics shall implement the approved dimensional modeling strategy.

## 19. Area 23 Dependency
Metric outputs shall remain compatible with approved profiling baselines.

## 20. Area 22 Dependency
Metric populations and values shall support approved reconciliation controls.

## 21. Area 21 Dependency
Metric calculations shall preserve approved duplicate and record-resolution behavior.

## 22. Area 20 Dependency
Metric inputs shall consume standardized and normalized analytical data.

## 23. Business Metric Definition
A business metric is a governed quantitative or categorical measurement with an explicit business meaning, calculation definition, grain, source lineage, dimensional context, owner, and validation expectation.

## 24. KPI Definition
A KPI is a governed business indicator selected to represent a defined business objective or performance dimension. KPI designation shall not change the underlying metric definition or calculation semantics.

## 25. Metric Ownership
Every governed metric shall have a defined business owner and technical owner. Ownership shall include responsibility for definition, validation, change approval, and downstream impact assessment.

## 26. Business Meaning
Each metric shall have a concise business definition that explains what is being measured, what population is included, what population is excluded, and what the value represents.

## 27. Calculation Definition
Each metric shall document its calculation logic, required inputs, filters, joins, aggregation level, treatment of nulls, treatment of invalid records, and any applicable business rules.

## 28. Grain Definition
Each metric shall explicitly state its calculation grain and the grain at which the final value may safely be consumed.

## 29. Additivity Classification
Metrics shall be classified as additive, semi-additive, non-additive, ratio, percentage, count, distinct count, duration, or another documented metric type as appropriate.

## 30. Aggregation Boundary
Metrics shall define valid aggregation dimensions and shall prevent invalid re-aggregation of ratios, percentages, averages, distinct counts, or other non-additive measures.

## 31. Population Boundary
Every metric shall define its eligible population, exclusion rules, status filters, date boundaries, and treatment of incomplete or exceptional records.

## 32. Dimensional Context
Metrics shall identify approved dimensions through which they may be sliced, including date, customer, product, seller, geography, order status, and other compatible dimensions.

## 33. Time Context
Time-based metrics shall identify the relevant business date or timestamp, such as purchase date, approval date, delivery date, or another governed event time.

## 34. Double-Counting Prevention
Metric definitions shall explicitly prevent inflation caused by multi-item orders, multiple payments, repeated reviews, multiple sellers, many-to-many relationships, and incompatible joins.

## 35. Metric Dependency
Each metric shall identify its upstream mart model, required measures, dimensions, filters, and dependent calculations.

## 36. Derived Metric Boundary
Derived metrics shall reuse governed base metrics where appropriate and shall not create competing definitions of the same business concept without documented ownership and change control.

## 37. KPI Boundary
KPI designation shall identify business importance without changing the governed underlying calculation, grain, population, or aggregation semantics.

## 38. Reconciliation
Metrics shall reconcile to compatible upstream measures and populations at the declared grain and aggregation level.

## 39. Quality
Metric validation shall include input completeness, valid domains, calculation correctness, grain integrity, aggregation correctness, null handling, and expected-value checks where appropriate.

## 40. Lineage
Every governed metric shall retain traceability from the published metric through its mart model, transformation dependencies, and source data.

## 41. Documentation
Metric definitions shall be documented in a consistent format containing name, business definition, owner, grain, calculation, population, dimensions, time basis, aggregation behavior, lineage, quality rules, and change history.

## 42. Change Control
Changes to an established metric definition shall require documented impact analysis, owner approval, downstream dependency review, regression validation, and version-aware communication.

## 43. Semantic Layer Boundary
Business metrics defined in this area shall become governed inputs to the later Semantic / Business Layer and shall not be silently redefined there.

## 44. BI Boundary
Published metrics shall provide stable definitions for later BI-ready data products, dashboards, analytical SQL, and reporting consumption.

## 45. Source Preservation
Metric calculation and publication shall never mutate, overwrite, or delete original source records.

## 46. Acceptance Criteria
Area 41.1 is accepted when business metric and KPI definitions, ownership, business meaning, calculation, grain, additivity, aggregation, population, dimensions, time context, double-counting, dependencies, derived metrics, reconciliation, quality, lineage, documentation, change control, semantic-layer, BI, and source-preservation boundaries are explicitly documented and validated.

