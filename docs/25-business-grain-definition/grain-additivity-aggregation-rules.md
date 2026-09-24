# Area 25.3 — Grain, Additivity & Aggregation Rules

Status: Accepted & Frozen

## 1. Purpose
Define formal aggregation and additivity rules so RetailIQ measures remain mathematically valid when queried across their declared business grains.

## 2. Area 25.1 Dependency
All aggregation rules shall originate from the approved business-grain definitions established in Area 25.1.

## 3. Area 25.2 Dependency
Every measure shall reference a registered grain and business process from the Area 25.2 grain register.

## 4. Area 03 Dependency
Aggregation behavior shall support the analytical questions and business processes documented in Area 03.

## 5. Area 06 Dependency
Source cardinalities and one-to-many relationships shall be considered before combining measures across entities.

## 6. Area 19 Dependency
Transformation logic shall not alter measure meaning or aggregation behavior without explicit documentation.

## 7. Area 20 Dependency
Standardized numeric, monetary, temporal, and categorical representations shall be used consistently in measure calculations.

## 8. Area 21 Dependency
Deduplicated and resolved records shall be the approved analytical population before measure aggregation.

## 9. Area 22 Dependency
Aggregated results shall remain reconcilable to approved control totals and source-to-target mappings.

## 10. Area 23 Dependency
Profiling evidence shall inform expected distributions, multiplicity, null behavior, and aggregation boundaries.

## 11. Area 24 Dependency
Dimensional modeling strategy shall govern fact grain, dimension relationships, and measure placement.

## 12. Additive Measures
Measures that can be summed across all relevant dimensions shall be explicitly classified as additive only when their business meaning supports unrestricted summation.

## 13. Semi-Additive Measures
Measures that can be aggregated across some dimensions but not across time shall be classified as semi-additive, with the valid aggregation dimensions explicitly documented.

## 14. Non-Additive Measures
Ratios, percentages, averages, rates, scores, and other derived measures shall not be blindly summed. They shall be recalculated from appropriate base measures at the requested grain.

## 15. Order-Level Aggregation
Order-level measures shall be aggregated from the order grain. Joining order measures directly to multiple order-item, payment, or review rows shall be prohibited unless controlled aggregation is performed first.

## 16. Order-Item Aggregation
Order-item measures such as item count, item price totals, and freight totals shall be calculated at order-item grain and aggregated upward only through declared business rules.

## 17. Payment Aggregation
Payment measures shall remain at payment grain until intentionally aggregated to order or another compatible analytical grain. Multiple payment rows must not be interpreted as multiple orders.

## 18. Review Aggregation
Review measures such as review count and review score shall be aggregated from review grain. Review multiplication caused by joins must be prevented.

## 19. Quantity and Count Rules
Counts shall identify the entity being counted. COUNT of orders, customers, items, payments, and reviews shall not be interchanged merely because the records are joined.

## 20. Monetary Measure Rules
Monetary values shall retain their declared currency and business meaning. Revenue, item price, freight, payment value, and related measures shall not be treated as interchangeable metrics.

## 21. Average and Ratio Rules
Average order value, average review score, conversion-style rates, percentages, and ratios shall be calculated from appropriate numerators and denominators rather than averaged or summed across incompatible grains.

## 22. Double-Counting Prevention
Any one-to-many join capable of multiplying a measure must use pre-aggregation, distinct entity counting where appropriate, or an explicitly designed fact relationship.

## 23. Reconciliation and Validation
Aggregation outputs shall be validated using row counts, distinct business keys, control totals, expected ranges, and source-to-target reconciliation evidence.

## 24. Analytical Query Governance
Every production analytical metric shall document its grain, source measure, aggregation rule, dimensional scope, denominator where applicable, and known limitations.

## 25. Acceptance Criteria
Area 25.3 is acceptable when additive, semi-additive, and non-additive behavior is explicitly defined; order, item, payment, and review aggregation boundaries are controlled; monetary and ratio calculations are protected from double counting; and all rules remain traceable to Areas 03, 06, 19–24.

