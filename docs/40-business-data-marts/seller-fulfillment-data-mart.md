# Area 40.5 — Seller & Fulfillment Data Mart

Status: Accepted & Frozen

## 1. Purpose
Define the Seller & Fulfillment business data mart as a governed analytical product for seller identity, seller attributes, seller geography, item-level seller relationships, fulfillment performance, delivery timing, and seller operational analysis.

## 2. Area 40.4 Dependency
The Seller & Fulfillment mart shall remain compatible with the frozen Product mart while preserving seller and product grains and preventing uncontrolled multiplication of product or sales measures.

## 3. Area 40.3 Dependency
Customer relationships shall be consumed only through compatible analytical grains and shall not multiply seller or fulfillment measures.

## 4. Area 40.2 Dependency
Sales & Orders relationships shall provide governed order and order-item context while preserving seller-item grain and preventing order-level measure inflation.

## 5. Area 40.1 Dependency
The Seller & Fulfillment mart shall comply with the frozen Business Data Marts Foundation, including consumer, domain, grain, fact, dimension, measure, business-logic, quality, reconciliation, lineage, governance, BI-readiness, and performance boundaries.

## 6. Area 39 Dependency
The mart shall preserve the frozen Data Mart Architecture, including Seller and Fulfillment domain boundaries, grain, fact and dimension composition, business-logic ownership, cross-domain controls, quality, reconciliation, and double-counting prevention.

## 7. Area 38 Dependency
The mart shall follow the approved transformation dependency graph, execution ordering, lineage, failure handling, reconciliation, and recovery controls.

## 8. Area 37 Dependency
The mart shall comply with approved analytics engineering model contracts, naming, documentation, testing, ownership, regression, and controlled-change standards.

## 9. Area 36 Dependency
Seller and Fulfillment models shall consume governed Intermediate/Core transformations and shall not duplicate reusable enterprise transformation logic.

## 10. Area 35 Dependency
Incremental Seller and Fulfillment processing shall preserve approved model identity, key resolution, merge, idempotency, reconciliation, and recovery controls.

## 11. Area 34 Dependency
Full-refresh and incremental processing shall follow approved watermark, replay, backfill, late-arrival, and processing-mode escalation controls.

## 12. Area 33 Dependency
Seller and Fulfillment mart transformations shall remain within the approved ELT architecture.

## 13. Area 32 Dependency
Historical and late-arriving seller and fulfillment records shall preserve approved temporal semantics.

## 14. Area 31 Dependency
Seller historical attributes shall use approved SCD behavior where historical analysis requires versioned seller context.

## 15. Area 30 Dependency
Conformed and role-playing dimensions shall preserve consistent analytical meaning and key behavior.

## 16. Area 29 Dependency
Fulfillment facts and measures shall retain approved event grain and aggregation behavior.

## 17. Area 28 Dependency
Fact and dimension composition shall preserve approved architectural responsibilities.

## 18. Area 27 Dependency
Seller dimensions shall follow approved dimension architecture and attribute ownership.

## 19. Area 26 Dependency
Seller natural and surrogate key semantics shall remain consistent with approved key architecture.

## 20. Area 25 Dependency
Every Seller and Fulfillment model shall declare an explicit business grain.

## 21. Area 24 Dependency
Seller and fulfillment analytical models shall follow the approved dimensional modeling strategy.

## 22. Area 23 Dependency
Seller and Fulfillment outputs shall remain compatible with approved profiling baselines.

## 23. Area 22 Dependency
Seller populations, relationships, measures, and business totals shall reconcile at compatible grains.

## 24. Area 21 Dependency
Approved duplicate and record-resolution behavior shall remain preserved.

## 25. Area 20 Dependency
Seller and Fulfillment models shall consume standardized and normalized analytical inputs.

## 26. Business Purpose
The Seller & Fulfillment mart shall provide a governed analytical representation of sellers, seller geography, seller participation in order items, fulfillment timing, delivery performance, and seller operational metrics.

## 27. Primary Consumers
Primary consumers include seller operations, fulfillment analysis, marketplace operations, logistics analysis, business analysts, reporting workflows, semantic models, dashboards, and approved BI products.

## 28. Seller Business Grain
The core Seller model shall use one row per seller_id unless a separate model explicitly declares another grain.

## 29. Seller Identity
seller_id shall remain the governed seller business identifier. Seller identity shall not be duplicated or reassigned through downstream mart processing.

## 30. Seller Attribute Boundary
Seller city, state, postal-prefix information, and other approved descriptive attributes shall remain descriptive seller attributes and shall not silently become transactional measures.

## 31. Seller Geography
Seller geography shall support seller-state, city, and postal-prefix analysis using approved source relationships and standardized geography logic.

## 32. Seller Order-Item Relationship
Seller performance shall be derived through the approved seller_id relationship to order-item data. Seller-level measures shall be aggregated from order-item or fulfillment-compatible grains before being attached to seller grain.

## 33. Seller Product Relationship
A seller may participate in sales of multiple products. Product relationships shall not be collapsed into a single product attribute at seller grain unless a governed aggregation or bridge model is explicitly defined.

## 34. Seller Order Count
Seller order counts shall count distinct compatible orders when the business definition requires orders. Multiple items from the same seller within one order shall not inflate distinct order counts.

## 35. Seller Item Count
Seller item counts shall use the approved order-item grain and shall remain distinct from order counts.

## 36. Seller Sales Measures
Governed seller measures may include item quantity, item sales value, freight value, distinct order count, average item price, and other documented seller-performance measures.

## 37. Fulfillment Grain
Fulfillment analytical models shall explicitly declare whether their grain is order, order-item, seller-order, seller-order-item, delivery event, or another approved grain. No implicit grain transition is permitted.

## 38. Delivery Timing
Fulfillment analysis shall support available carrier handoff, customer delivery, purchase, approval, and estimated delivery timestamps while preserving legitimate missing lifecycle values.

## 39. Delivery Performance
Governed delivery metrics may include delivery duration, estimated-versus-actual delivery difference, on-time or late classification, and other documented measures where source timestamps support the calculation.

## 40. Invalid Temporal Boundary
Delivery metrics shall not fabricate durations when required timestamps are unavailable or invalid. Missing lifecycle timestamps shall remain explicit exceptions or unavailable states.

## 41. Multi-Seller Order Boundary
Orders containing items from multiple sellers shall not be treated as a single-seller fulfillment event. Seller-level analysis shall remain based on the seller's participating order-item relationships.

## 42. Product Interaction Boundary
Product-level relationships shall be aggregated or modeled separately before being combined with seller-level measures to avoid seller-product join multiplication.

## 43. Customer Interaction Boundary
Customer relationships shall be aggregated to a compatible seller grain before customer-derived measures are attached to seller-level models.

## 44. Sales Interaction Boundary
Order-level sales measures shall not be directly joined to seller-item rows without controlled aggregation because one order may contain multiple sellers and multiple items.

## 45. Fulfillment Quality
Quality controls shall validate seller keys, order-item relationships, timestamps, delivery calculations, status domains, measure validity, expected uniqueness, and declared grain.

## 46. Reconciliation
Seller populations shall reconcile to compatible upstream seller populations. Seller item counts and seller sales measures shall reconcile to compatible order-item populations and aggregation levels.

## 47. Fulfillment Reconciliation
Delivery and fulfillment metrics shall reconcile to compatible populations of orders or order-items with the required timestamps and shall distinguish unavailable timestamps from actual operational outcomes.

## 48. Exception Handling
Unmatched sellers, invalid seller attributes, missing or inconsistent lifecycle timestamps, impossible delivery intervals, duplicate business keys, measure anomalies, and reconciliation differences shall be classified and handled through approved exception controls.

## 49. Lineage
Seller attributes, seller metrics, fulfillment measures, and delivery classifications shall retain traceability to upstream transformation models and source fields.

## 50. BI Consumption
The Seller & Fulfillment mart shall provide stable seller-level and fulfillment-level analytical outputs for KPI definitions, semantic models, operational dashboards, marketplace analysis, analytical SQL, and BI-ready products.

## 51. Performance
Seller and fulfillment analytical access shall be supported through appropriate grain, aggregation, key design, and query patterns without compromising correctness.

## 52. Source Preservation
Seller and Fulfillment mart processing shall never mutate, overwrite, or delete original source records.

## 53. Acceptance Criteria
Area 40.5 is accepted when seller grain, identity, attributes, geography, seller-order-item relationships, product and customer boundaries, sales measures, fulfillment grain, delivery timing, delivery performance, temporal exceptions, multi-seller handling, quality, reconciliation, exception handling, lineage, BI consumption, performance, and source-preservation controls are explicitly documented and validated.

