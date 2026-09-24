# Area 40.2 — Sales & Orders Data Mart

Status: Accepted & Frozen

## 1. Purpose
Define the Sales & Orders business data mart as a governed analytical product for order lifecycle, item-level sales, revenue, freight, fulfillment, and commercial performance analysis.

## 2. Area 40.1 Dependency
The Sales & Orders mart shall comply with the frozen Business Data Marts Foundation, including consumer, domain, grain, fact, dimension, measure, business-logic, quality, reconciliation, lineage, governance, BI-readiness, and performance boundaries.

## 3. Area 39 Dependency
The mart shall preserve the frozen Data Mart Architecture, including approved Sales and Orders domain boundaries, grain, fact and dimension composition, business-logic ownership, cross-domain controls, quality, reconciliation, and double-counting prevention.

## 4. Area 38 Dependency
The mart shall follow the approved transformation dependency graph and execution-order controls.

## 5. Area 37 Dependency
The mart shall comply with approved analytics engineering model contracts, naming, documentation, testing, ownership, regression, and controlled-change standards.

## 6. Area 36 Dependency
Sales and Orders models shall consume governed Intermediate/Core transformations and shall not duplicate reusable enterprise transformation logic.

## 7. Area 35 Dependency
Incremental processing shall preserve approved model identity, key resolution, merge, idempotency, reconciliation, and recovery controls.

## 8. Area 34 Dependency
Full-refresh and incremental processing shall follow approved watermark, replay, backfill, late-arrival, and escalation controls.

## 9. Area 33 Dependency
Sales and Orders mart transformations shall remain within the approved ELT architecture.

## 10. Area 32 Dependency
Historical and late-arriving order and sales records shall retain approved temporal semantics.

## 11. Area 31 Dependency
Customer, product, seller, and other applicable SCD dimensions shall provide historically correct context where required.

## 12. Area 30 Dependency
Conformed and role-playing dimensions shall retain consistent analytical meaning and key behavior.

## 13. Area 29 Dependency
Sales and order facts shall preserve approved event grain and measure aggregation behavior.

## 14. Area 28 Dependency
Fact and dimension composition shall preserve the approved architecture.

## 15. Area 27 Dependency
Dimensions shall follow approved dimension architecture.

## 16. Area 26 Dependency
Natural and surrogate key semantics shall remain consistent.

## 17. Area 25 Dependency
Each Sales & Orders model shall declare an explicit business grain.

## 18. Area 24 Dependency
Dimensional modeling shall follow the approved strategy.

## 19. Area 23 Dependency
Sales and Orders outputs shall remain compatible with profiling baselines.

## 20. Area 22 Dependency
Population, key, measure, and business-total reconciliation shall be preserved.

## 21. Area 21 Dependency
Approved duplicate and record-resolution behavior shall remain preserved.

## 22. Area 20 Dependency
Sales and Orders models shall consume standardized and normalized analytical inputs.

## 23. Business Purpose
The Sales & Orders mart shall provide a governed analytical view of customer orders, order items, commercial values, order lifecycle status, and fulfillment timing.

## 24. Primary Consumers
Primary consumers include sales analysts, business analysts, commercial reporting, operations analysts, finance-oriented analytical workflows, dashboards, semantic models, and approved BI products.

## 25. Order-Level Business Grain
The order-level model shall use one row per order. Order-level measures and attributes shall not be inflated by direct joins to lower-grain order-item or payment records.

## 26. Order-Item Business Grain
The sales-item model shall use one row per order-item identified by the approved composite order_id and order_item_id business key.

## 27. Order Lifecycle
Order lifecycle analysis shall support order status, purchase time, approval time, carrier handoff, customer delivery, and estimated delivery dates while preserving nulls that represent legitimate incomplete lifecycle states.

## 28. Sales Measures
Sales measures shall include governed item price and freight-related measures at the order-item grain, with order-level aggregations performed only through controlled aggregation logic.

## 29. Order Measures
Order-level analytical measures shall include order counts and lifecycle measures derived at order grain without duplicating orders through item or payment relationships.

## 30. Revenue Boundary
Revenue-related calculations shall use documented business definitions and shall distinguish item price from freight value and payment value rather than treating them as interchangeable measures.

## 31. Customer Dimension Boundary
Customer attributes may enrich Sales & Orders analysis through the approved customer key while preserving the order or order-item grain.

## 32. Product Dimension Boundary
Product attributes may enrich item-level sales analysis through product_id without changing the declared sales-item grain.

## 33. Seller Dimension Boundary
Seller attributes may enrich item-level fulfillment and sales analysis through seller_id without multiplying order-item records.

## 34. Date Dimension Boundary
Date analysis shall use approved role-playing date relationships where applicable, including purchase date, approval date, carrier date, delivery date, and estimated delivery date.

## 35. Payment Interaction Boundary
Payment data shall not be directly joined to order-item rows when calculating item-level sales measures unless payment allocation is explicitly governed. Order-level payment analysis shall remain at payment or order grain as appropriate.

## 36. Review Interaction Boundary
Review records shall not be directly joined to order-item rows for measure calculations without controlled aggregation because multiple reviews can exist for an order.

## 37. Fulfillment Analysis
The mart shall support delivery timing, carrier handoff, estimated-versus-actual delivery, order status, seller, and product-related fulfillment analysis where source data supports the calculation.

## 38. Commercial Analysis
The mart shall support analysis by order date, customer, product, category, seller, geography, order status, and other approved analytical dimensions.

## 39. Grain Protection
Known one-to-many relationships, including orders to items and orders to payments, shall be aggregated or modeled separately before being combined into a compatible analytical grain.

## 40. Double-Counting Prevention
Sales measures shall explicitly protect against inflation caused by multi-item orders, multiple payments, repeated reviews, seller relationships, and other many-to-one or one-to-many joins.

## 41. Data Quality
Quality controls shall validate order keys, order-item composite keys, dimension references, numeric measures, dates, status domains, null handling, and declared grain.

## 42. Reconciliation
Order counts shall reconcile to compatible upstream order populations. Order-item counts and item-level monetary measures shall reconcile to compatible upstream populations and aggregation levels.

## 43. Exception Handling
Unmatched keys, invalid lifecycle dates, unexpected statuses, duplicate business keys, measure anomalies, and reconciliation differences shall be classified and handled through approved exception controls.

## 44. Lineage
Each Sales & Orders model and governed measure shall retain traceability to upstream transformation models and source attributes.

## 45. BI Consumption
The mart shall provide stable order-level and sales-item analytical outputs for later KPI, semantic-layer, BI-ready, dashboard, and analytical SQL consumption.

## 46. Acceptance Criteria
Area 40.2 is accepted when Sales & Orders purpose, consumers, grains, lifecycle, measures, revenue boundary, dimension relationships, payment and review boundaries, fulfillment analysis, commercial analysis, grain protection, double-counting prevention, quality, reconciliation, exception handling, lineage, and BI consumption controls are explicitly documented and validated.

