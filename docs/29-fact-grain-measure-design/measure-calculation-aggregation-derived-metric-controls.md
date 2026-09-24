# Area 29.3 — Measure Calculation, Aggregation & Derived Metric Controls

Status: Accepted & Frozen

## 1. Purpose
Define controlled calculation, aggregation, derivation, null handling, denominator handling, and analytical consistency rules for RetailIQ measures.

## 2. Area 29.1 Dependency
Calculation rules shall implement the approved fact-grain and measure-design foundation.

## 3. Area 29.2 Dependency
All calculations shall use the approved measure register, business definitions, metadata, and ownership.

## 4. Area 28 Dependency
Calculations shall preserve the frozen fact architecture, fact grains, relationships, and analytical join boundaries.

## 5. Area 25 Dependency
Aggregation shall respect the approved business grain and measure additivity rules.

## 6. Area 26 Dependency
Calculation populations shall use governed fact and dimension keys and shall not create duplicate identities.

## 7. Area 27 Dependency
Measure calculations shall respect dimension relationships, conformed dimensions, and role-playing date boundaries.

## 8. Area 03 Dependency
Calculated metrics shall preserve the business meaning of the analytical questions they support.

## 9. Area 06 Dependency
Calculations shall account for source multiplicity and relationship cardinality.

## 10. Area 07 Dependency
Calculation inputs shall remain traceable to contracted source attributes and schemas.

## 11. Area 19 Dependency
Calculation transformations shall preserve approved transformation semantics.

## 12. Area 20 Dependency
Calculation inputs shall use standardized numeric, monetary, temporal, categorical, and null representations.

## 13. Area 21 Dependency
Calculation populations shall use resolved records and shall not reintroduce duplicate source records.

## 14. Area 22 Dependency
Calculated measures shall remain reconcilable to their underlying fact populations and source control totals.

## 15. Area 23 Dependency
Calculation rules shall account for profiled value ranges, missingness, distributions, and observed multiplicity.

## 16. Order Measure Calculation
Order-level measures shall calculate only from the order fact population. Order counts shall count order-grain rows or explicitly distinct order identities according to the registered metric definition.

## 17. Order Item Measure Calculation
Item price and freight shall be calculated from order-item rows. Item-level sums shall not be used as order-level measures without an explicit aggregation from item grain to order grain.

## 18. Payment Measure Calculation
Payment value shall be summed from payment-grain rows. Payment totals shall be calculated before any analytical combination with item or review populations when those populations contain multiple rows per order.

## 19. Review Measure Calculation
Review metrics shall use review-grain populations. Average review score shall be calculated as an appropriate review-level aggregation and shall not be summed or averaged again after an uncontrolled many-to-many join.

## 20. Additive Aggregation Controls
Additive measures may be summed across compatible dimensions when each fact row contributes exactly once to the requested analytical population.

## 21. Semi-Additive Aggregation Controls
Semi-additive measures shall identify the dimensions across which aggregation is prohibited or restricted. The calculation must follow the registered business definition.

## 22. Non-Additive Aggregation Controls
Ratios, percentages, averages, rates, and similar non-additive metrics shall be recalculated from governed underlying populations rather than summed across groups.

## 23. Null and Zero Controls
Null values shall not automatically become zero unless the measure definition explicitly permits that interpretation. Zero denominators shall have an explicit governed outcome rather than producing invalid calculations.

## 24. Double-Counting and Reconciliation Controls
Every calculation shall preserve fact grain, prevent many-to-many measure multiplication, document aggregation boundaries, and support reconciliation from derived result to underlying fact population.

## 25. Acceptance Criteria
Area 29.3 is acceptable when order, order-item, payment, and review calculations are explicitly controlled; additive, semi-additive, and non-additive aggregation behavior is enforced; derived metrics, nulls, zero denominators, double-counting, and reconciliation are governed; and all dependencies remain traceable.

