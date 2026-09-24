# Area 42.3 — Semantic Measures, KPI Exposure & Business Calculation Rules

Status: Accepted & Frozen

## 1. Purpose
Define governed semantic measures, KPI exposure, calculation rules, aggregation behavior, business filters, dimensional context, ratio handling, and analytical calculation boundaries.

## 2. Area 42.2 Dependency
Semantic measures and KPIs shall use the frozen semantic model structure, entities, dimensions, relationships, keys, cardinality, hierarchies, and grain controls established in Area 42.2.

## 3. Area 42.1 Dependency
Measure and KPI exposure shall preserve the frozen Semantic / Business Layer Foundation.

## 4. Area 41 Dependency
All exposed metrics and KPIs shall reference the frozen Business Metrics & KPI Definitions.

## 5. Area 40 Dependency
Measures shall consume approved Business Data Marts without changing their declared grain or business meaning.

## 6. Area 39 Dependency
Calculation rules shall preserve approved data-mart grain, fact, dimension, measure, reconciliation, and double-counting boundaries.

## 7. Area 38 Dependency
Measure dependencies shall follow the approved transformation dependency graph.

## 8. Area 37 Dependency
Semantic calculation models shall comply with analytics engineering contracts, documentation, testing, lineage, ownership, and controlled-change standards.

## 9. Area 36 Dependency
Reusable business transformations shall remain upstream and shall not be unnecessarily duplicated inside semantic calculations.

## 10. Area 35 Dependency
Measure and KPI processing shall preserve incremental identity, merge, idempotency, reconciliation, and recovery behavior.

## 11. Area 34 Dependency
Semantic calculation refresh shall remain compatible with approved full-refresh and incremental strategies.

## 12. Area 33 Dependency
Semantic calculations shall remain within the approved ELT architecture.

## 13. Area 32 Dependency
Historical measures shall preserve approved historical and late-arriving record semantics.

## 14. Area 31 Dependency
Historical dimension context shall preserve approved SCD behavior.

## 15. Area 30 Dependency
Measures shall use approved conformed and role-playing dimensions.

## 16. Area 29 Dependency
All measures shall preserve approved fact grain and measure semantics.

## 17. Area 28 Dependency
Calculation responsibility shall respect approved fact and dimension architecture.

## 18. Area 27 Dependency
Dimensional calculations shall use approved dimension structures.

## 19. Area 26 Dependency
Measure relationships shall use approved natural and surrogate key semantics.

## 20. Area 25 Dependency
Every measure and KPI shall have an explicit calculation grain.

## 21. Area 24 Dependency
Semantic calculations shall follow the approved dimensional modeling strategy.

## 22. Area 23 Dependency
Measure validation shall remain compatible with approved profiling baselines.

## 23. Area 22 Dependency
Measures and KPIs shall reconcile to approved upstream populations and values.

## 24. Area 21 Dependency
Calculation results shall preserve approved duplicate and record-resolution behavior.

## 25. Area 20 Dependency
Semantic calculations shall consume standardized and normalized analytical data.

## 26. Measure Identity
Every semantic measure shall have a stable unique identifier, business name, description, unit, owner, source metric, and calculation definition.

## 27. Measure Classification
Measures shall be classified as additive, semi-additive, non-additive, ratio, percentage, distinct-count, duration, score, or another governed type.

## 28. Additive Measure
Additive measures may be summed across approved dimensions where their business semantics and grain permit summation.

## 29. Semi-Additive Measure
Semi-additive measures shall document the dimensions across which aggregation is valid and the dimensions across which aggregation is prohibited.

## 30. Non-Additive Measure
Non-additive measures shall not be summed merely because they are exposed as numeric values.

## 31. Ratio Measure
Ratio measures shall preserve explicit numerator and denominator definitions and shall calculate the ratio from compatible populations.

## 32. Percentage Measure
Percentage measures shall use governed numerator and denominator populations and shall explicitly define zero-denominator behavior.

## 33. Distinct-Count Measure
Distinct-count measures shall preserve distinct entity semantics and shall not be incorrectly summed across overlapping groups.

## 34. Duration Measure
Duration measures shall document start event, end event, unit, null behavior, and invalid temporal boundary handling.

## 35. Score Measure
Score measures shall document scale, valid range, population, aggregation behavior, and missing-value semantics.

## 36. Core Order Measures
Order measures shall expose governed order_count, order-level populations, and other approved order metrics without multiplying orders through item, payment, or review joins.

## 37. Core Item Measures
Item measures shall preserve order-item grain and shall expose approved item counts, sales item value, freight value, and item price measures.

## 38. Customer Measures
Customer measures shall preserve customer grain and shall expose approved customer counts, orders per customer, purchase frequency, and related governed metrics.

## 39. Product Measures
Product measures shall preserve product grain and shall support approved product count, item sales, order participation, and category analysis.

## 40. Seller Measures
Seller measures shall preserve seller grain and shall support approved seller count, item sales, order participation, and fulfillment metrics.

## 41. Payment Measures
Payment measures shall preserve payment grain and shall not be directly summed with order-level measures without governed aggregation to a compatible grain.

## 42. Review Measures
Review measures shall preserve review population semantics and shall explicitly account for the documented repeated review_id behavior.

## 43. GMV Exposure
GMV shall only be exposed using the governed Area 41 definition. GMV shall not be assumed to equal payment_value unless the approved metric definition explicitly establishes that relationship.

## 44. Payment Value Exposure
payment_value shall retain its payment-domain meaning and shall not be silently substituted for order-level commercial value.

## 45. Average Order Value
Average order value shall use a compatible order-level numerator and order-count denominator and shall not be calculated from incompatible payment or item populations.

## 46. Average Item Price
Average item price shall preserve item-level numerator and item-count denominator semantics.

## 47. Orders Per Customer
Orders per customer shall use compatible customer and order populations and shall explicitly define the eligible customer population.

## 48. Items Per Order
Items per order shall use compatible item and order populations and shall preserve order-item grain.

## 49. Customer Purchase Frequency
Purchase frequency shall document the customer population, order event definition, observation period, and time basis.

## 50. Delivery Duration
Delivery duration shall use approved purchase, carrier, or customer-delivery timestamps according to the governed metric definition.

## 51. Estimated Delivery Difference
Estimated delivery difference shall preserve the approved actual-versus-estimated date semantics and invalid-date handling.

## 52. On-Time Delivery Rate
On-time delivery rate shall define eligible delivered orders, numerator, denominator, comparison rule, and missing delivery-date behavior.

## 53. Late Delivery Rate
Late delivery rate shall use a governed eligible population and shall remain mathematically and semantically compatible with on-time delivery classification.

## 54. Average Review Score
Average review score shall preserve review population, valid score range, and aggregation behavior.

## 55. Review Count
Review count shall document whether it represents review rows, distinct review identifiers, or another governed review population.

## 56. Payment Count
Payment count shall preserve payment-event grain and shall not be interpreted as order count.

## 57. KPI Exposure
KPIs shall expose the approved KPI identity, actual value, target where available, variance, directionality, performance period, dimensional context, and classification where governed.

## 58. Target Exposure
Target values shall retain target version, effective period, applicability, unit, and ownership metadata where exposed.

## 59. Variance Exposure
Variance shall expose only when actual and target values are compatible and shall preserve the governed variance definition.

## 60. Percentage Variance
Percentage variance shall explicitly handle missing or zero targets and shall never fabricate a percentage.

## 61. Performance Classification
Performance classifications shall use governed thresholds and directionality and shall not modify the underlying actual KPI value.

## 62. Business Filter Rules
Business filters shall use governed values and definitions for order status, payment type, review score, geography, category, seller, product, and date.

## 63. Date Filter Context
Every time-sensitive measure shall document which date role controls its time filtering.

## 64. Dimensional Filter Context
Measures shall document valid dimensions and prevent unsupported dimensional slicing from producing misleading results.

## 65. Filter Propagation
Filter propagation shall preserve intended populations and shall not introduce measure multiplication.

## 66. Null Handling
Null, unknown, unavailable, and not-applicable values shall retain governed semantics and shall not silently become zero.

## 67. Zero-Denominator Handling
Division by zero shall produce a controlled null or not-applicable result according to the governed metric rule.

## 68. Currency Handling
Currency measures shall preserve source currency and unit semantics. Any conversion shall require an explicitly governed conversion rule.

## 69. Rounding
Rounding shall occur only at the approved presentation or calculation boundary and shall not alter underlying analytical precision unnecessarily.

## 70. Double-Counting Protection
Measure calculations shall explicitly prevent inflation from order-item, payment, review, seller, and other one-to-many or many-to-many relationships.

## 71. Calculation Reconciliation
Every exposed measure and KPI shall reconcile to its governed upstream metric or mart at compatible grain and population.

## 72. Testing
Measure and KPI tests shall cover formula correctness, aggregation, filters, dimensions, null handling, zero denominators, relationship behavior, and expected reconciliation.

## 73. Regression
Changes to calculations, relationships, dimensions, filters, or upstream metrics shall trigger regression validation for affected semantic outputs.

## 74. Lineage
Every exposed measure and KPI shall maintain lineage to its governed Area 41 definition and upstream analytical models.

## 75. Documentation
Every semantic calculation shall document business meaning, formula, grain, unit, aggregation, population, filters, dimensions, ownership, and limitations.

## 76. Change Control
Changes to semantic calculations shall require impact assessment, approval, versioning, regression evidence, and documented effective date.

## 77. BI Boundary
Semantic measures and KPIs shall be exposed in a form suitable for downstream BI-ready data products and analytical consumption.

## 78. Source Preservation
Semantic calculation logic shall never mutate, overwrite, delete, or alter original source records.

## 79. Technology-Neutral Boundary
Calculation definitions shall remain independent of a specific BI visualization product unless a later approved implementation decision establishes such dependency.

## 80. Acceptance Criteria
Area 42.3 is accepted when measure identity, classification, aggregation, core business measures, GMV, payment value, averages, ratios, counts, fulfillment metrics, review metrics, KPI exposure, target and variance exposure, performance classification, business filters, date context, dimensional context, null handling, zero-denominator handling, currency, rounding, double-counting, reconciliation, testing, regression, lineage, documentation, change control, BI, source preservation, and technology-neutral boundaries are explicitly documented and validated.

