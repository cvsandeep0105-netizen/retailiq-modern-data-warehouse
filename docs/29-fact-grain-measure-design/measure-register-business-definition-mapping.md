# Area 29.2 — Measure Register & Business Definition Mapping

Status: Accepted & Frozen

## 1. Purpose
Create the formal RetailIQ measure register and map each measure to its fact owner, business definition, grain, source attribute, transformation logic, unit, additivity classification, and analytical usage.

## 2. Area 29.1 Dependency
The measure register shall implement the fact-grain and measure-design foundation established in Area 29.1.

## 3. Area 28 Dependency
Measure ownership and analytical behavior shall remain consistent with the frozen Fact Architecture in Area 28.

## 4. Area 25 Dependency
Every measure shall be explicitly aligned with its approved business grain and aggregation boundary.

## 5. Area 26 Dependency
Measure records shall retain traceability to the approved natural-key and surrogate-key architecture where identifiers participate in calculations or grouping.

## 6. Area 27 Dependency
Measure definitions shall identify the dimensions and analytical contexts in which the measure is valid.

## 7. Area 03 Dependency
Measures shall map to documented business processes and analytical questions.

## 8. Area 06 Dependency
Measure definitions shall respect source cardinality, multiplicity, composite identifiers, and relationship exceptions.

## 9. Area 07 Dependency
Source fields used by measures shall remain traceable to the frozen source contracts and physical schema expectations.

## 10. Area 19 Dependency
Measure transformations shall preserve approved source semantics and business meaning.

## 11. Area 20 Dependency
Measure values shall follow standardized numeric, monetary, temporal, categorical, and null-handling conventions.

## 12. Area 21 Dependency
Measure populations shall use approved record-resolution outcomes and shall not recreate duplicate source records.

## 13. Area 22 Dependency
Every measure shall have an identifiable reconciliation path to appropriate upstream control totals.

## 14. Area 23 Dependency
Measure definitions shall be consistent with profiling evidence for completeness, distributions, ranges, and multiplicity.

## 15. Order Measure Register
Order fact measures shall include explicitly defined order counts and other approved order-grain metrics. Each measure shall identify its order-level grain, source lineage, business meaning, and aggregation behavior.

## 16. Order Item Measure Register
Order-item measures shall include price and freight at order-item grain. Item measures shall be eligible for aggregation only when the analytical grouping preserves item-row uniqueness.

## 17. Payment Measure Register
Payment value shall be registered as a payment-grain monetary measure. Payment totals shall be aggregated from payment rows and shall not be summed after uncontrolled joins to multi-item or multi-review populations.

## 18. Review Measure Register
Review score shall be registered as a review-grain measure. Average review score shall be derived from the appropriate review population and shall not be treated as an additive measure.

## 19. Measure Business Definition
Every measure shall have a precise business definition describing what is counted, summed, averaged, or derived and what population is included or excluded.

## 20. Measure Metadata
Every registered measure shall define measure name, business definition, fact owner, grain, source attribute or derivation, data type, unit, currency where applicable, null behavior, and default aggregation behavior.

## 21. Additivity Register
Every measure shall explicitly declare additive, semi-additive, or non-additive behavior. Aggregation shall be restricted to dimensions and contexts for which the classification is valid.

## 22. Derived Metric Register
Derived metrics shall document numerator, denominator, population filters, grain alignment, null handling, zero-denominator behavior, and calculation logic.

## 23. Analytical Usage Boundary
Each measure shall document valid analytical dimensions, approved aggregation paths, prohibited joins, and known double-counting risks.

## 24. Lineage, Reconciliation and Change Control
Each measure shall have source-to-target lineage, reconciliation evidence, quality expectations, and controlled change requirements. Any modification to a measure definition or aggregation rule shall require dependency review and regression validation.

## 25. Acceptance Criteria
Area 29.2 is acceptable when the RetailIQ measure register contains explicit business definitions, fact ownership, grain, source lineage, metadata, additivity classification, derived-metric rules, analytical usage boundaries, reconciliation controls, and change-management requirements for the approved fact measures.

