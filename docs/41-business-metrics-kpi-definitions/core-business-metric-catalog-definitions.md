# Area 41.2 — Core Business Metric Catalog & Definitions

Status: Accepted & Frozen

## 1. Purpose
Define the governed RetailIQ core business metric catalog, including orders, sales, customers, products, sellers, fulfillment, payments, reviews, monetary measures, counts, averages, ratios, and distinct-count measures.

## 2. Area 41.1 Dependency
All metrics shall comply with the frozen Business Metrics & KPI Foundation, including ownership, business meaning, calculation grain, additivity, aggregation, population, dimensional context, time basis, double-counting prevention, lineage, quality, and change control.

## 3. Area 40 Dependency
Metrics shall consume the frozen Business Data Marts and preserve their approved domain, grain, fact, dimension, measure, quality, reconciliation, and lineage boundaries.

## 4. Area 39 Dependency
Metric definitions shall preserve the approved Data Mart Architecture and its grain, composition, business-logic, cross-domain, reconciliation, and double-counting controls.

## 5. Area 38 Dependency
Metric dependencies shall follow the approved transformation dependency graph.

## 6. Area 37 Dependency
Metric definitions shall comply with analytics engineering contracts, documentation, testing, ownership, and controlled-change standards.

## 7. Area 36 Dependency
Reusable metric inputs shall consume governed Intermediate/Core transformations through approved downstream models.

## 8. Area 35 Dependency
Incrementally processed metric inputs shall preserve approved change, merge, idempotency, reconciliation, and recovery behavior.

## 9. Area 34 Dependency
Metric refresh shall preserve approved full-refresh, incremental, watermark, replay, backfill, and escalation strategies.

## 10. Area 33 Dependency
Metric construction shall remain within the approved ELT architecture.

## 11. Area 32 Dependency
Historical and late-arriving data shall preserve approved temporal semantics.

## 12. Area 31 Dependency
Historical metric interpretation shall use approved SCD behavior where required.

## 13. Area 30 Dependency
Metric dimensions shall use approved conformed and role-playing dimensions.

## 14. Area 29 Dependency
Metrics shall preserve approved fact grain and measure behavior.

## 15. Area 28 Dependency
Metric inputs shall preserve approved fact and dimension responsibilities.

## 16. Area 27 Dependency
Dimension attributes used by metrics shall follow approved dimension architecture.

## 17. Area 26 Dependency
Metric relationships shall use approved natural and surrogate key semantics.

## 18. Area 25 Dependency
Every metric shall declare its valid calculation grain.

## 19. Area 24 Dependency
Metric modeling shall follow the approved dimensional modeling strategy.

## 20. Area 23 Dependency
Metric outputs shall remain compatible with approved profiling baselines.

## 21. Area 22 Dependency
Metric values shall support approved population, key, measure, and business-total reconciliation.

## 22. Area 21 Dependency
Metric calculations shall preserve approved duplicate and record-resolution behavior.

## 23. Area 20 Dependency
Metric inputs shall consume standardized and normalized analytical data.

## 24. Metric Catalog Standard
Every governed metric shall have a unique metric name, business definition, technical definition, owner, calculation grain, source mart, source measure, population, time basis, dimensional context, aggregation behavior, and validation rule.

## 25. Order Count
Metric name: order_count. Definition: count of distinct orders within the declared analytical population and time context. Grain: order. Aggregation: additive across mutually exclusive populations, but distinct-count behavior shall be preserved when combining lower-grain datasets.

## 26. Order Item Count
Metric name: order_item_count. Definition: count of governed order-item records within the declared population. Grain: order-item. It shall not be substituted for order_count.

## 27. Customer Count
Metric name: customer_count. Definition: count of distinct governed customers within the declared population and time context. Grain: customer. Re-aggregation of customer_count across overlapping populations shall not be treated as additive.

## 28. Product Count
Metric name: product_count. Definition: count of distinct governed products within the declared population. Grain: product. The metric shall preserve distinct-count semantics.

## 29. Seller Count
Metric name: seller_count. Definition: count of distinct governed sellers within the declared population. Grain: seller. Overlapping populations shall not be summed as if they were mutually exclusive.

## 30. Sales Item Value
Metric name: sales_item_value. Definition: governed sum of order-item price values at the compatible order-item population. Grain: order-item. Freight shall remain separate.

## 31. Freight Value
Metric name: freight_value. Definition: governed sum of order-item freight values at compatible order-item grain. It shall not be silently combined with item price.

## 32. Gross Merchandise Value Boundary
If a governed GMV-style metric is introduced, its definition shall explicitly state whether it represents item price only or another approved commercial value. It shall not be assumed equivalent to payment_value.

## 33. Payment Value
Metric name: payment_value. Definition: governed sum of payment_value at payment grain or a compatible aggregated order grain. Multiple payments for an order shall be aggregated before joining to order-item or customer-level measures.

## 34. Average Order Value
Metric name: average_order_value. Definition: governed order-level monetary value divided by the compatible distinct order population. The numerator and denominator must use compatible populations and time context.

## 35. Average Item Price
Metric name: average_item_price. Definition: governed average of order-item price values at the declared item population. The averaging method shall be documented and shall not be substituted with an incompatible order-level average.

## 36. Orders Per Customer
Metric name: orders_per_customer. Definition: compatible order population divided by compatible distinct customer population. It is a ratio and shall not be summed across dimensions.

## 37. Items Per Order
Metric name: items_per_order. Definition: compatible order-item population divided by compatible distinct order population. It is a ratio and shall not be summed.

## 38. Customer Purchase Frequency
Metric name: customer_purchase_frequency. Definition: governed measure of order activity per customer over a declared time period. The denominator and eligible customer population shall be explicitly defined.

## 39. Delivery Duration
Metric name: delivery_duration. Definition: governed elapsed time between approved delivery lifecycle timestamps. Records missing required timestamps shall not receive fabricated durations.

## 40. Estimated Delivery Difference
Metric name: estimated_delivery_difference. Definition: governed difference between actual delivery timing and estimated delivery timing where both timestamps are valid and available.

## 41. On-Time Delivery Rate
Metric name: on_time_delivery_rate. Definition: compatible on-time delivery population divided by compatible eligible delivery population. It is a percentage and shall not be summed.

## 42. Late Delivery Rate
Metric name: late_delivery_rate. Definition: compatible late-delivery population divided by compatible eligible delivery population. It is a percentage and shall not be summed.

## 43. Review Score Average
Metric name: average_review_score. Definition: governed average review_score over the declared review population. The review population and treatment of repeated review identifiers shall follow approved review-grain controls.

## 44. Review Count
Metric name: review_count. Definition: count of governed review records at the declared review grain. It shall not be confused with distinct orders or distinct review_id values.

## 45. Payment Count
Metric name: payment_count. Definition: count of governed payment records at payment grain. Multiple payments for an order shall remain multiple payment records unless an order-level aggregation is explicitly defined.

## 46. Metric Type Classification
Count, distinct count, sum, average, ratio, percentage, duration, and derived metrics shall be explicitly classified so consumers understand valid aggregation behavior.

## 47. Null and Missing-Data Rules
Null, missing, invalid, and unavailable source values shall follow governed metric-specific rules. Missing lifecycle timestamps shall not be interpreted as zero duration or successful completion.

## 48. Status Filtering
Metrics involving order lifecycle shall explicitly document which order_status values are included or excluded. No universal delivered-only rule shall be assumed across every metric.

## 49. Time Basis
Every time-based metric shall identify the governing event timestamp or date, such as order purchase, approval, delivery, review creation, or another documented business event.

## 50. Dimension Compatibility
Metrics shall identify valid dimensional slicing. A metric shall not be exposed through a dimension whose relationship can multiply its underlying population.

## 51. Double-Counting Controls
Core metrics shall explicitly protect against multi-item orders, multiple payments, repeated reviews, multiple sellers, many-to-many relationships, and incompatible fact joins.

## 52. Reconciliation Controls
Core metric results shall reconcile to compatible upstream mart populations and measures at the declared grain and aggregation level.

## 53. Metric Lineage
Every catalog metric shall identify its originating mart, model, source measure or columns, transformation dependency, and calculation definition.

## 54. Metric Ownership
Every catalog metric shall have a named business owner and technical owner, with responsibility for definition, validation, change approval, and downstream impact.

## 55. Change Control
Changing a metric definition, population, grain, formula, time basis, or aggregation behavior shall require impact analysis, owner approval, regression validation, and documented version/change history.

## 56. Acceptance Criteria
Area 41.2 is accepted when the core metric catalog contains governed definitions for orders, order items, customers, products, sellers, sales value, freight, payments, averages, ratios, fulfillment metrics, review metrics, metric types, null rules, status rules, time basis, dimensional compatibility, double-counting, reconciliation, lineage, ownership, and change control.

