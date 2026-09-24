# Area 29.1 — Fact Grain & Measure Design Foundation

Status: Accepted & Frozen

## 1. Purpose
Establish the detailed foundation for RetailIQ fact grain and measure design, building on the frozen fact architecture while defining precise measure ownership, aggregation behavior, and analytical boundaries.

## 2. Area 28 Dependency
This area implements the approved Fact Architecture established and frozen in Area 28.

## 3. Area 24 Dependency
Fact grain and measure design shall follow the dimensional modeling strategy established in Area 24.

## 4. Area 25 Dependency
Every fact and measure shall remain aligned with the approved business grain definitions and aggregation rules.

## 5. Area 26 Dependency
Fact identifiers and dimension references shall follow the approved natural-key and surrogate-key strategy.

## 6. Area 27 Dependency
Measure analysis shall use the approved dimension architecture, conformed dimensions, and role-playing relationships.

## 7. Area 28 Dependency
Fact grain, candidate facts, measure ownership, relationships, and analytical join controls shall remain consistent with Area 28.

## 8. Area 03 Dependency
Measure design shall support the documented business processes and analytical questions without changing their intended interpretation.

## 9. Area 06 Dependency
Source cardinality, multiplicity, composite identifiers, and relationship exceptions shall constrain measure and grain design.

## 10. Area 07 Dependency
Measure source attributes and identifiers shall remain traceable to the frozen source contracts and schema expectations.

## 11. Area 19 Dependency
Measure transformations shall preserve source meaning and approved transformation semantics.

## 12. Area 20 Dependency
Measure values shall follow approved standardization and normalization rules for numeric, monetary, temporal, categorical, and null values.

## 13. Area 21 Dependency
Measure populations shall respect approved deduplication and record-resolution outcomes while preserving legitimate repeated events.

## 14. Area 22 Dependency
Measures shall have reconciliation paths to upstream populations and control totals.

## 15. Area 23 Dependency
Measure ranges, completeness, distributions, multiplicity, and anomalies shall remain consistent with profiling evidence.

## 16. Order Fact Grain
The order fact grain is one customer order per row. Order-level measures shall be calculated only from attributes and events belonging to this grain.

## 17. Order Item Fact Grain
The order-item fact grain is one order-item line per row identified by order_id and order_item_id. Item-level price and freight measures belong to this grain.

## 18. Payment Fact Grain
The payment fact grain is one payment sequence per order identified by order_id and payment_sequential. Payment value belongs exclusively to this grain.

## 19. Review Fact Grain
The review fact shall preserve its approved review business-record grain. Review score and review-event attributes shall remain at review grain.

## 20. Measure Ownership
Every measure shall have one authoritative fact owner. A measure shall not be independently recreated in another fact unless a documented semantic and reconciliation boundary exists.

## 21. Additivity Foundation
Each measure shall be classified as additive, semi-additive, or non-additive before analytical consumption. Aggregation behavior shall be determined by business meaning and grain.

## 22. Derived Measure Foundation
Derived metrics such as averages, percentages, rates, conversion measures, and ratios shall be calculated from governed numerator and denominator populations rather than treated as additive stored measures.

## 23. Double-Counting Foundation
Measures from different fact grains shall not be combined through uncontrolled joins. Required cross-fact analysis shall establish an explicit aggregation boundary before measures are combined.

## 24. Lineage and Governance Foundation
Every measure shall have documented source lineage, business definition, grain ownership, transformation logic, data type, aggregation rule, quality expectation, and change-control requirements.

## 25. Acceptance Criteria
Area 29.1 is acceptable when the order, order-item, payment, and review grains are explicitly established; measure ownership and additivity are defined; derived-measure and double-counting boundaries are documented; and all dependencies from Areas 03, 06, 07, 19–28 are preserved.

