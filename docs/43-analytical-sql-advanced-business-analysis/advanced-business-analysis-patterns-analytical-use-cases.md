# Area 43.3 — Advanced Business Analysis Patterns & Analytical Use Cases

Status: Accepted & Frozen

## 1. Purpose
Define governed advanced business-analysis patterns for RetailIQ using approved semantic objects, business metrics, KPIs, data marts, dimensional models, and analytical SQL.

## 2. Area 43.2 Dependency
Business analysis patterns shall use the advanced analytical SQL controls defined in Area 43.2.

## 3. Area 42 Dependency
Business analysis shall consume the governed Semantic / Business Layer.

## 4. Area 41 Dependency
Business analysis shall reuse approved metrics and KPI definitions.

## 5. Area 40 Dependency
Business analysis shall consume approved business data marts.

## 6. Area 39 Dependency
Analytical use cases shall preserve approved mart grain, fact, dimension, measure, and business-logic boundaries.

## 7. Area 38 Dependency
Analytical dependencies shall follow the approved transformation dependency graph.

## 8. Area 37 Dependency
Analytical artifacts shall follow analytics engineering standards for documentation, testing, lineage, ownership, and controlled change.

## 9. Area 36 Dependency
Reusable business transformations shall remain governed upstream.

## 10. Area 35 Dependency
Analysis shall remain compatible with incremental model semantics.

## 11. Area 34 Dependency
Analysis shall remain compatible with full-refresh and incremental processing boundaries.

## 12. Area 33 Dependency
Analysis shall consume the approved ELT architecture.

## 13. Area 32 Dependency
Historical and late-arriving records shall retain approved temporal semantics.

## 14. Area 31 Dependency
Historical dimension analysis shall preserve SCD semantics.

## 15. Area 30 Dependency
Conformed and role-playing dimensions shall be used according to approved roles.

## 16. Area 29 Dependency
Analytical measures shall preserve approved fact grain.

## 17. Area 28 Dependency
Business analysis shall respect approved fact architecture.

## 18. Area 27 Dependency
Business analysis shall respect approved dimension architecture.

## 19. Area 26 Dependency
Analytical joins shall use approved natural and surrogate keys.

## 20. Area 25 Dependency
Every analysis shall explicitly declare its business grain.

## 21. Area 24 Dependency
Analysis shall preserve approved dimensional modeling semantics.

## 22. Area 23 Dependency
Analysis shall remain compatible with profiling baselines.

## 23. Area 22 Dependency
Analysis shall support reconciliation controls.

## 24. Area 21 Dependency
Duplicate and record-resolution controls shall remain preserved.

## 25. Area 20 Dependency
Analysis shall consume standardized and normalized data.

## 26. Business Analysis Framework
Each use case shall define business question, population, grain, dimensions, measures, time context, filters, assumptions, expected output, and interpretation boundary.

## 27. Executive Sales Analysis
Sales analysis shall examine approved commercial measures by governed time and dimensional contexts without inventing unsupported business outcomes.

## 28. Order Volume Analysis
Order-volume analysis shall use governed order_count and preserve one-order analytical grain where appropriate.

## 29. Order Value Analysis
Order-value analysis shall use approved sales, payment, or other governed measures and shall explicitly distinguish their business meanings.

## 30. Average Order Value
AOV analysis shall reuse the approved average-order-value definition and shall validate numerator and denominator compatibility.

## 31. Customer Purchase Frequency
Purchase-frequency analysis shall define customer population, observation period, qualifying orders, and aggregation grain.

## 32. Customer Value Analysis
Customer-value analysis shall use approved measures and shall avoid assuming unsupported lifetime-value or profitability semantics.

## 33. Customer Segmentation
Customer segmentation shall define population, segmentation attributes, threshold rules, effective period, and assignment logic.

## 34. Customer Cohort Analysis
Customer cohorts shall define the qualifying customer event, cohort period, observation period, and retained or active population.

## 35. Customer Retention
Retention analysis shall explicitly define retained behavior and denominator population rather than assuming a universal retention definition.

## 36. Customer Geographic Analysis
Customer geography analysis shall distinguish customer location from seller or fulfillment geography.

## 37. Product Performance
Product analysis shall preserve product grain and distinguish product-level measures from order-item events.

## 38. Product Category Performance
Category analysis shall preserve source category values and shall not fabricate translations.

## 39. Product Ranking
Product rankings shall define metric, population, period, ordering, N, and tie handling.

## 40. Product Mix
Product-mix analysis shall define the denominator population and ensure compatible product and item grains.

## 41. Seller Performance
Seller analysis shall preserve seller grain and distinguish seller attributes from item and order-event measures.

## 42. Seller Ranking
Seller ranking shall define the performance metric, population, time context, ordering, and ties.

## 43. Seller Fulfillment Analysis
Fulfillment analysis shall use approved delivery measures and eligible order populations.

## 44. Order Lifecycle Analysis
Order lifecycle analysis shall use governed order-status and lifecycle timestamps without treating missing lifecycle dates as completed events.

## 45. Delivery Performance
Delivery analysis shall use approved delivery-duration and estimated-delivery-difference definitions.

## 46. On-Time Delivery
On-time delivery analysis shall use the governed on-time definition and explicitly define eligible delivered orders.

## 47. Late Delivery
Late-delivery analysis shall use the governed late definition and compatible denominator population.

## 48. Payment Mix
Payment analysis shall preserve payment-event grain and aggregate payment rows before order-level analysis when required.

## 49. Payment Behavior
Payment behavior analysis shall distinguish payment events, payment values, payment types, and order populations.

## 50. Review Analysis
Review analysis shall preserve review population semantics and the documented review identity boundary.

## 51. Review Score Distribution
Review-score analysis shall examine score distributions without assuming causal explanations for observed ratings.

## 52. Review Trend Analysis
Review trends shall define the review date basis and treatment of incomplete periods.

## 53. Customer Experience Analysis
Customer-experience analysis may combine governed order, delivery, and review measures only after compatible grains and populations are established.

## 54. Cross-Domain Analysis
Cross-domain analysis shall document every domain join and demonstrate that measures remain compatible.

## 55. Sales and Customer Analysis
Sales-by-customer analysis shall aggregate item-level commercial measures to customer grain before combining customer attributes.

## 56. Sales and Product Analysis
Sales-by-product analysis shall preserve product grain and aggregate item-level measures appropriately.

## 57. Sales and Seller Analysis
Sales-by-seller analysis shall preserve seller grain and prevent duplicated order-level measures.

## 58. Sales and Geography
Geographic sales analysis shall declare whether geography represents customer or seller location.

## 59. Payment and Sales Analysis
Payment and sales comparisons shall not assume payment_value is identical to sales-item value or GMV.

## 60. Delivery and Customer Experience
Delivery and review analysis shall define the shared order population and prevent review multiplicity from inflating delivery measures.

## 61. Product and Review Analysis
Product-review analysis shall aggregate reviews to the intended product grain before combining with product measures.

## 62. Seller and Review Analysis
Seller-review analysis shall establish the correct order-item and review relationships before aggregation.

## 63. Trend and Seasonality Boundary
Trend patterns shall be descriptive unless a separately governed analytical method supports stronger inference.

## 64. Comparative Analysis
Comparisons shall use compatible periods, populations, dimensional contexts, and metric definitions.

## 65. Benchmark Analysis
Benchmark analysis shall document the reference population and shall not imply an external benchmark when none is defined.

## 66. Variance Analysis
Variance shall distinguish absolute difference from percentage difference and handle zero or null denominators explicitly.

## 67. Contribution Analysis
Contribution analysis shall define how each entity or segment contributes to the approved total.

## 68. Pareto-Style Analysis
Pareto-style analysis may identify cumulative contribution patterns but shall document the selected population and threshold rather than assuming a universal 80/20 rule.

## 69. Exception Analysis
Exception analysis shall identify records or groups that violate approved analytical conditions and shall preserve traceability.

## 70. Data Quality Analysis
Business analysis shall be able to surface nulls, missing values, invalid temporal relationships, unresolved categories, and other governed exceptions.

## 71. Source Boundary Awareness
Known source boundaries shall remain visible during analysis, including 13 unmatched non-null product-category translations.

## 72. Review Identity Boundary
Because review_id alone is not unique, review analysis shall use the approved composite identity boundary (review_id, order_id) where record identity is required.

## 73. Order Item Multiplicity
Order-level analysis shall account for orders containing multiple items, with the observed source maximum of 21 items per order.

## 74. Payment Multiplicity
Order-level payment analysis shall account for multiple payment records, with the observed source maximum of 29 payments per order.

## 75. Review Multiplicity
Order-level review analysis shall account for multiple reviews, with the observed source maximum of 3 reviews per order.

## 76. Double-Counting Control
Cross-domain analysis shall pre-aggregate lower-grain populations when multiple one-to-many relationships could multiply measures.

## 77. Null and Zero Handling
Null values, zero values, unavailable values, and not-applicable values shall retain their governed meanings.

## 78. Interpretation Boundary
Analytical findings shall distinguish observed descriptive patterns from assumptions, causal explanations, forecasts, or recommendations.

## 79. No Unsupported Business Outcomes
Documentation shall not claim actual business performance, rankings, trends, or causal findings until the corresponding analytical SQL is executed against governed data.

## 80. Reconciliation
Each material business analysis shall reconcile to governed metrics or marts where equivalent populations and definitions exist.

## 81. Validation
Use cases shall validate grain, population, joins, calculations, filters, dimensional context, time context, and expected output structure.

## 82. Regression
Changes to analytical use cases shall be regression-tested against approved baselines and business controls.

## 83. Lineage
Every material analysis shall retain lineage to semantic definitions, data marts, models, and upstream dependencies.

## 84. Documentation
Business analysis artifacts shall document business question, method, data population, grain, metrics, filters, assumptions, limitations, and interpretation.

## 85. Performance
Advanced use cases shall use governed reusable structures and avoid unnecessary repeated scans, joins, sorting, or aggregation.

## 86. BI Consumption
Analytical outputs may feed BI products but shall remain consistent with the governed semantic/business layer.

## 87. Security
Business analysis shall respect approved access, least-privilege, sensitive-data, ownership, and governance controls.

## 88. Reproducibility
Business analyses shall be reproducible using documented definitions, inputs, filters, periods, model versions, and query logic.

## 89. Source Preservation
Business analysis shall never modify original source records.

## 90. Technology-Neutral Boundary
Business-analysis patterns describe logical analytical behavior and remain independent of a specific warehouse or BI vendor.

## 91. Acceptance Criteria
Area 43.3 is accepted when advanced business-analysis patterns, customer, product, seller, order, sales, fulfillment, payment, review, geographic, cohort, retention, segmentation, trend, ranking, contribution, variance, cross-domain, data-quality, grain, population, reconciliation, validation, regression, lineage, documentation, performance, BI, security, reproducibility, source-preservation, and technology-neutral controls are explicitly documented and validated.

