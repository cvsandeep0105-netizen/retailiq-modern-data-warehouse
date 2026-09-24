# Area 40.4 — Product Data Mart

Status: Accepted & Frozen

## 1. Purpose
Define the Product business data mart as a governed analytical product for product identity, category, product attributes, catalog analysis, sales performance, and product-level analytical consumption.

## 2. Area 40.3 Dependency
The Product mart shall remain compatible with the frozen Customer mart while preserving its own product-domain grain and avoiding uncontrolled duplication of customer or sales measures.

## 3. Area 40.2 Dependency
The Product mart shall consume compatible Sales & Orders outputs where product sales performance is required, while preserving product and sales-item grains.

## 4. Area 40.1 Dependency
The Product mart shall comply with the frozen Business Data Marts Foundation, including consumer, domain, grain, fact, dimension, measure, business-logic, quality, reconciliation, lineage, governance, BI-readiness, and performance boundaries.

## 5. Area 39 Dependency
The mart shall preserve the frozen Data Mart Architecture, including Product domain boundaries, grain, fact and dimension composition, business-logic ownership, cross-domain controls, quality, reconciliation, and double-counting prevention.

## 6. Area 38 Dependency
The mart shall follow the approved transformation dependency graph, execution ordering, lineage, failure handling, reconciliation, and recovery controls.

## 7. Area 37 Dependency
The mart shall comply with approved analytics engineering model contracts, naming, documentation, testing, ownership, regression, and controlled-change standards.

## 8. Area 36 Dependency
Product models shall consume governed Intermediate/Core transformations and shall not duplicate reusable enterprise transformation logic.

## 9. Area 35 Dependency
Incremental Product processing shall preserve approved model identity, key resolution, merge, idempotency, reconciliation, and recovery controls.

## 10. Area 34 Dependency
Full-refresh and incremental processing shall follow approved watermark, replay, backfill, late-arrival, and processing-mode escalation controls.

## 11. Area 33 Dependency
Product mart transformations shall remain within the approved ELT architecture.

## 12. Area 32 Dependency
Historical and late-arriving product records shall preserve approved temporal semantics.

## 13. Area 31 Dependency
Product historical attributes shall use approved SCD behavior where historical analysis requires versioned product context.

## 14. Area 30 Dependency
Product dimensions shall preserve conformed and role-playing dimension semantics where applicable.

## 15. Area 29 Dependency
Product-related facts and measures shall retain approved grain and aggregation behavior.

## 16. Area 28 Dependency
Fact and dimension composition shall preserve approved architectural responsibilities.

## 17. Area 27 Dependency
Product dimensions shall follow approved dimension architecture and attribute ownership.

## 18. Area 26 Dependency
Product natural and surrogate key semantics shall remain consistent with approved key architecture.

## 19. Area 25 Dependency
Every Product mart model shall declare an explicit business grain.

## 20. Area 24 Dependency
Product analytical models shall follow the approved dimensional modeling strategy.

## 21. Area 23 Dependency
Product outputs shall remain compatible with approved profiling baselines.

## 22. Area 22 Dependency
Product population, key, measure, and business-total reconciliation shall be preserved.

## 23. Area 21 Dependency
Approved duplicate and record-resolution behavior shall remain preserved.

## 24. Area 20 Dependency
Product models shall consume standardized and normalized analytical inputs.

## 25. Business Purpose
The Product mart shall provide a governed analytical representation of the product catalog, product attributes, product categories, translated category labels, and approved product performance metrics.

## 26. Primary Consumers
Primary consumers include product analytics, merchandising analysis, category analysis, sales analysis, business analysts, reporting workflows, semantic models, dashboards, and approved BI products.

## 27. Product Business Grain
The core Product model shall use one row per product_id unless a separate model explicitly declares another grain.

## 28. Product Identity
product_id shall remain the governed product business identifier. Product identity shall not be duplicated or reassigned through downstream mart processing.

## 29. Product Attribute Boundary
Product category, descriptive lengths, photo quantity, weight, length, height, and width shall remain descriptive product attributes unless an explicitly governed analytical metric derives from them.

## 30. Product Category Boundary
product_category_name shall retain its source-domain meaning. Category transformations shall preserve the original category value and shall not silently replace it.

## 31. Category Translation Boundary
product_category_name_english may provide an analytical English representation where a valid translation exists. The translation relationship shall remain explicit and unmatched source categories shall not receive invented translations.

## 32. Unmatched Category Handling
Known unmatched product category translation values shall be represented through approved unknown, untranslated, or exception handling rather than fabricated category labels.

## 33. Product Sales Relationship
Product sales performance shall use the approved product_id relationship to order-item data. Product-level measures shall be aggregated from the order-item grain before being attached to product grain.

## 34. Product Sales Measures
Governed product measures may include item quantity, item sales value, freight value, order count, average item price, and other documented product-performance measures.

## 35. Order Count Boundary
Product order counts shall count distinct compatible orders rather than order-item rows when the business definition requires orders. Multiple items for the same product/order combination shall not inflate order counts.

## 36. Item Count Boundary
Product item counts shall be based on the approved order-item grain and shall not be confused with distinct order counts.

## 37. Seller Relationship Boundary
Products may be associated with multiple sellers through order-item relationships. Seller analysis shall not be collapsed into the core product grain unless a documented aggregation or bridge model is used.

## 38. Customer Relationship Boundary
Customer-level analysis shall not be directly joined to product grain for measure calculations unless customer behavior has first been aggregated to a compatible product grain.

## 39. Category Performance
Category-level performance shall be derived through the governed product-category relationship and shall preserve product and category aggregation semantics.

## 40. Product Lifecycle and History
Where product attributes change over time and historical analysis requires prior values, approved SCD controls shall preserve historical versions and effective periods.

## 41. Data Quality
Quality controls shall validate product keys, attribute domains, category relationships, translation coverage, numeric attributes, expected uniqueness, null handling, and declared grain.

## 42. Reconciliation
Product population shall reconcile to compatible upstream product populations. Product sales measures shall reconcile to compatible order-item populations and aggregation levels.

## 43. Exception Handling
Duplicate products, invalid product attributes, unmatched category translations, invalid measures, relationship anomalies, and reconciliation differences shall be classified and handled through approved exception controls.

## 44. Lineage
Product attributes, category mappings, and governed product metrics shall retain traceability to upstream transformation models and source fields.

## 45. BI Consumption
The Product mart shall provide stable product-level and category-level analytical outputs for KPI definitions, semantic models, product dashboards, merchandising analysis, analytical SQL, and BI-ready products.

## 46. Performance
Product analytical access shall be supported through appropriate product grain, category relationships, pre-aggregation, key design, and query patterns without compromising correctness.

## 47. Source Preservation
Product mart processing shall never mutate, overwrite, or delete original product or translation source records.

## 48. Acceptance Criteria
Area 40.4 is accepted when product grain, identity, attributes, category handling, translation handling, sales relationships, seller and customer boundaries, product measures, order and item count definitions, category performance, historical behavior, quality, reconciliation, exceptions, lineage, BI consumption, performance, and source-preservation controls are explicitly documented and validated.

