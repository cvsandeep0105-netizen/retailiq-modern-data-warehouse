# Area 28.3 — Fact Grain, Additivity & Measure Design Controls

Status: Accepted & Frozen

## 1. Purpose
Define detailed fact-grain, measure ownership, additivity, aggregation, and double-counting controls for the RetailIQ fact architecture.

## 2. Area 28.1 Dependency
Fact measure design shall implement the approved fact architecture foundation.

## 3. Area 28.2 Dependency
Measure ownership and business-process mapping shall remain consistent with the fact candidate register.

## 4. Area 24 Dependency
Measure design shall follow the dimensional modeling strategy and measure-design principles.

## 5. Area 25 Dependency
Every measure shall be evaluated against its declared business grain and aggregation rules.

## 6. Area 26 Dependency
Fact and dimension key relationships shall follow the approved natural-key and surrogate-key strategy.

## 7. Area 27 Dependency
Measures shall be associated with the correct dimension relationships and conformed analytical structures.

## 8. Area 03 Dependency
Measure definitions shall support documented business processes and analytical questions.

## 9. Area 06 Dependency
Measure design shall respect source cardinality, multiplicity, composite identifiers, and relationship boundaries.

## 10. Area 07 Dependency
Measure source attributes shall remain consistent with source schema and data-contract expectations.

## 11. Area 19 Dependency
Measure transformations shall preserve approved source meaning and transformation semantics.

## 12. Area 20 Dependency
Measures shall use standardized numeric, monetary, categorical, temporal, and null-handling conventions.

## 13. Area 21 Dependency
Duplicate detection and record-resolution rules shall be applied before measures are treated as analytical facts.

## 14. Area 22 Dependency
Fact measures shall support reconciliation against upstream control totals and source populations.

## 15. Area 23 Dependency
Profiling evidence shall inform completeness, range, distribution, multiplicity, and anomaly controls for measures.

## 16. Order Fact Measure Controls
Order-grain measures shall be calculated only from order-grain attributes. Order counts may be additive across compatible dimensions, while order-level monetary measures shall not be duplicated through order-item, payment, or review joins.

## 17. Order Item Fact Measure Controls
Order-item price and freight measures shall remain at order-item grain. They may be summed across compatible dimensions when the underlying rows are unique at item grain.

## 18. Payment Fact Measure Controls
Payment value shall remain a payment-grain measure. Payment totals shall not be joined directly to order-item rows without an aggregation boundary because multiple payments and multiple items can create measure multiplication.

## 19. Review Fact Measure Controls
Review score shall be treated as a review-grain measure. Average review score is non-additive and shall be calculated using the review population appropriate to the analytical question.

## 20. Additive Measure Classification
Measures shall be explicitly classified as additive, semi-additive, or non-additive. Additive measures may be summed across valid dimensions; semi-additive measures require restricted aggregation; non-additive measures require derived calculations such as averages, ratios, or percentages.

## 21. Count and Distinct-Count Controls
Row counts shall count the declared fact grain. Distinct business-event counts shall use the appropriate natural business identifier and shall not substitute for row counts without an explicit definition.

## 22. Monetary and Ratio Controls
Monetary measures shall retain their source currency semantics and aggregation boundary. Ratios, percentages, averages, and rates shall be recalculated from appropriate numerator and denominator populations rather than summed.

## 23. Double-Counting Prevention
Analytical joins shall aggregate each fact to the required business grain before combining measures from facts with different grains. Direct many-to-many fact joins that multiply measures shall be prohibited unless explicitly controlled.

## 24. Measure Lineage and Reconciliation
Every production measure shall have source lineage, business definition, grain ownership, transformation rule, aggregation rule, quality expectation, and reconciliation control. Changes shall preserve traceability and regression evidence.

## 25. Acceptance Criteria
Area 28.3 is acceptable when fact-grain and measure ownership are explicit; order, order-item, payment, and review measures have documented aggregation behavior; additive, semi-additive, and non-additive controls are defined; double-counting prevention is established; and measure lineage and reconciliation are preserved.

