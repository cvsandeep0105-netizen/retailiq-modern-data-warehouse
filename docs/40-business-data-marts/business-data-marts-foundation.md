# Area 40.1 — Business Data Marts Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the foundation for RetailIQ business data marts, including business consumption, analytical purpose, mart ownership, model boundaries, grain, measures, dimensions, dependencies, quality, reconciliation, governance, and BI readiness.

## 2. Area 39 Dependency
Business data marts shall implement the frozen Data Mart Architecture, including approved business-domain boundaries, model organization, grain, fact and dimension composition, business-logic ownership, quality, reconciliation, exception, lineage, performance, and governance controls.

## 3. Area 38 Dependency
Business marts shall follow the approved transformation dependency graph, execution ordering, lineage, failure handling, reconciliation, and recovery boundaries.

## 4. Area 37 Dependency
Business marts shall comply with the approved analytics engineering framework, including model standards, contracts, documentation, testing, ownership, regression, CI/CD, and controlled change.

## 5. Area 36 Dependency
Business marts shall consume governed Intermediate/Core models and shall not bypass approved transformation ownership boundaries.

## 6. Area 35 Dependency
Business marts shall preserve approved incremental model identity, key resolution, merge behavior, idempotency, reconciliation, and recovery controls.

## 7. Area 34 Dependency
Business mart processing shall support approved full-refresh, incremental, watermark, replay, backfill, and processing-mode escalation strategies.

## 8. Area 33 Dependency
Business mart construction shall remain within the approved ELT architecture and transformation-layer responsibilities.

## 9. Area 32 Dependency
Historical and late-arriving records shall retain approved temporal semantics when consumed by business marts.

## 10. Area 31 Dependency
SCD dimensions shall provide historically correct descriptive context where required by business mart analysis.

## 11. Area 30 Dependency
Conformed and role-playing dimensions shall retain consistent analytical meaning and key behavior across business marts.

## 12. Area 29 Dependency
Fact measures shall preserve approved business grain, measure definitions, and aggregation behavior.

## 13. Area 28 Dependency
Business mart facts and dimensions shall preserve approved fact and dimension architectural responsibilities.

## 14. Area 27 Dependency
Business mart dimensions shall follow approved dimension architecture, attribute ownership, relationship, and historical controls.

## 15. Area 26 Dependency
Business mart models shall preserve approved natural-key and surrogate-key semantics.

## 16. Area 25 Dependency
Each business mart model shall have an explicit business grain and shall prevent uncontrolled grain multiplication.

## 17. Area 24 Dependency
Business marts shall implement the approved dimensional modeling strategy.

## 18. Area 23 Dependency
Business mart outputs shall remain compatible with approved profiling baselines and analytical validation.

## 19. Area 22 Dependency
Business marts shall support approved population, key, measure, and business-total reconciliation.

## 20. Area 21 Dependency
Approved duplicate and record-resolution behavior shall remain preserved in business mart inputs.

## 21. Area 20 Dependency
Business marts shall consume standardized and normalized analytical data.

## 22. Business Data Mart Definition
A business data mart is a governed analytical data product organized around a defined business domain or cross-domain analytical purpose. It provides stable, documented, consumer-oriented data structures without replacing the enterprise warehouse architecture.

## 23. Business Consumer Boundary
Business marts shall be designed for analytical consumption by business users, analysts, reporting workflows, semantic models, dashboards, and approved downstream analytical products.

## 24. Business Domain Boundary
Each mart shall have an explicit business purpose and ownership boundary. Business marts shall not become uncontrolled collections of unrelated analytical models.

## 25. Initial RetailIQ Mart Domains
RetailIQ shall support governed business mart domains including Sales and Orders, Customer, Product, Seller and Fulfillment, Payment, Customer Experience, and approved cross-domain analytical marts.

## 26. Mart Model Boundary
Business marts shall expose stable analytical models while keeping reusable transformation logic in governed upstream layers.

## 27. Grain Boundary
Every business mart model shall declare its business grain and shall preserve that grain through joins, calculations, filtering, and aggregation.

## 28. Fact Boundary
Fact models shall represent measurable business events or approved analytical states and shall retain governed measures at the declared grain.

## 29. Dimension Boundary
Dimension models shall provide descriptive analytical context using approved natural-key, surrogate-key, conformed, role-playing, and SCD behavior.

## 30. Measure Boundary
Business measures shall have documented definitions, aggregation behavior, business meaning, source lineage, and ownership.

## 31. Business Logic Boundary
Enterprise-reusable business rules shall remain upstream in governed transformation layers. Business marts shall focus on domain-oriented analytical composition and approved business calculations.

## 32. Cross-Domain Boundary
Cross-domain marts shall document participating domains, grain compatibility, join relationships, measure behavior, and analytical purpose.

## 33. Data Quality Boundary
Business marts shall inherit and enforce approved structural, grain, key, measure, referential, reconciliation, and business-rule quality controls.

## 34. Reconciliation Boundary
Business mart populations and measures shall reconcile with compatible upstream models before being released as analytical data products.

## 35. Lineage Boundary
Each mart model shall maintain traceability to its upstream analytical models and ultimately to governed source data.

## 36. Governance Boundary
Business marts shall have defined ownership, documentation, access expectations, change controls, data-quality responsibilities, and operational accountability.

## 37. BI Readiness Boundary
Business marts shall provide stable analytical structures suitable for the later Business Metrics, Semantic Layer, BI-Ready Data Products, and BI Product stages.

## 38. Performance Boundary
Mart design shall support analytical workloads through appropriate model grain, joins, aggregations, access patterns, and reusable structures without sacrificing correctness.

## 39. Source Preservation
Business mart construction shall never modify, overwrite, or delete original source records.

## 40. Acceptance Criteria
Area 40.1 is accepted when the business mart purpose, consumer boundary, domain boundary, model boundary, grain, fact, dimension, measure, business-logic, cross-domain, quality, reconciliation, lineage, governance, BI-readiness, performance, and source-preservation boundaries are explicitly documented and validated.

