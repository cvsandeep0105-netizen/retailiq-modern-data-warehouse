# Area 24.3 — Grain, Additivity & Measure Design Controls

Status: Accepted & Frozen

## 1. Purpose
Define formal grain, additivity, semi-additivity, non-additivity, and measure-design controls for RetailIQ dimensional modeling.

## 2. Area 24.1 Strategy Dependency
Measure design shall follow the grain-first dimensional modeling strategy established in Area 24.1.

## 3. Area 24.2 Candidate Mapping Dependency
Measure definitions shall remain aligned with the fact and dimension candidate mappings established in Area 24.2.

## 4. Area 03 Analytical Questions Dependency
Measures shall support documented analytical questions and shall not introduce unsupported business interpretations.

## 5. Area 06 Relationship Dependency
Measure aggregation shall respect source relationships, cardinalities, and documented multiplicity boundaries from Area 06.

## 6. Area 07 Contract Dependency
Measure data types, nullability, and source meanings shall remain traceable to Area 07 contracts.

## 7. Area 19 Transformation Dependency
Derived measures shall preserve approved transformation logic and business meaning from Area 19.

## 8. Area 20 Standardization Dependency
Measure units, numeric representations, categorical values, and standardized formats shall follow Area 20 controls.

## 9. Area 21 Deduplication Dependency
Measure populations shall account for duplicate detection and record-resolution outcomes established in Area 21.

## 10. Area 22 Reconciliation Dependency
Material measures shall be reconcilable using the control totals and measure reconciliation rules established in Area 22.

## 11. Area 23 Profiling Dependency
Measure design shall consider observed distributions, nullability, validity, and business characteristics identified in Area 23.

## 12. Order Grain
An order-level fact candidate shall represent one business order per fact row when that grain is selected. Order-level measures shall not be repeated across order-item rows.

## 13. Order Item Grain
An order-item fact candidate shall represent one order-item business line per fact row using the documented order_id and order_item_id identity.

## 14. Payment Grain
A payment fact candidate shall represent one payment event or payment sequence at its declared grain. Payment measures shall not be treated as order-level totals without explicit aggregation.

## 15. Review Grain
A review fact candidate shall use the documented review identity boundary and shall account for the observed repeated review_id behavior.

## 16. Additive Measures
Measures that can be safely summed across all relevant dimensions at their declared grain shall be classified as additive.

## 17. Semi-Additive Measures
Measures that can be aggregated across selected dimensions but not across time shall be classified as semi-additive with explicit aggregation rules.

## 18. Non-Additive Measures
Ratios, percentages, averages, scores, and other measures that cannot be safely summed shall be classified as non-additive and calculated from appropriate base measures where possible.

## 19. Derived Measures
Derived measures shall document their source measures, formula or calculation logic, grain, units, null behavior, and reconciliation expectations.

## 20. Monetary Measures
Price, freight, payment value, revenue-like measures, and other monetary values shall document currency assumptions, precision, grain, and aggregation behavior.

## 21. Quantity and Count Measures
Item counts, order counts, payment counts, review counts, and distinct-entity counts shall be defined separately to prevent accidental substitution or double counting.

## 22. Double-Counting Controls
Measures shall not be duplicated through joins between different grains. Order, item, payment, and review measures shall require explicit aggregation paths.

## 23. Measure Lineage and Reconciliation
Every material measure shall be traceable to source attributes, transformations, standardization, record-resolution behavior, and reconciliation controls.

## 24. Technology-Neutral Boundary
These measure-design controls define logical analytical behavior without prescribing a physical warehouse, SQL engine, cloud platform, orchestration system, or BI product.

## 25. Acceptance Criteria
Area 24.3 is acceptable when fact grain, measure grain, additive classification, derived measures, monetary and quantity controls, double-counting prevention, lineage, and reconciliation expectations are explicitly defined and traceable to frozen Areas 03, 06, 07, 19–23 and Areas 24.1–24.2.

