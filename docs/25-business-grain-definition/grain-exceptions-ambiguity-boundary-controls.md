# Area 25.4 — Grain Exceptions, Ambiguity & Boundary Controls

Status: Accepted & Frozen

## 1. Purpose
Define explicit controls for ambiguous, exceptional, incomplete, multi-valued, and boundary-case records that could affect RetailIQ business-grain interpretation.

## 2. Area 25.1 Dependency
Exceptions shall be evaluated against the approved grain-first definitions established in Area 25.1.

## 3. Area 25.2 Dependency
Every exception shall reference the affected registered grain and business process.

## 4. Area 25.3 Dependency
Exceptions shall preserve the approved additivity, aggregation, and double-counting rules from Area 25.3.

## 5. Area 06 Dependency
Known source relationship exceptions and cardinality boundaries from Area 06 shall be explicitly considered.

## 6. Area 07 Dependency
Schema and contract boundaries shall determine whether an unexpected record represents a valid source condition, contract exception, or data-quality failure.

## 7. Area 19 Dependency
Transformation behavior shall preserve the distinction between legitimate business exceptions and transformation defects.

## 8. Area 20 Dependency
Standardization and normalization shall not silently convert ambiguous values into a misleading business grain.

## 9. Area 21 Dependency
Deduplication and record-resolution outcomes shall be distinguished from legitimate repeated business events.

## 10. Area 22 Dependency
Exception populations shall remain reconcilable and separately measurable.

## 11. Area 23 Dependency
Profiling evidence shall be used to identify unusual multiplicity, nullability, frequency, and distribution patterns.

## 12. Area 24 Dependency
Dimensional modeling patterns shall provide the boundary for unknown, not-applicable, historical, late-arriving, and ambiguous dimension cases.

## 13. Repeated Review Identifier Boundary
Repeated review_id values shall not automatically be treated as duplicate business events. The documented review_id plus order_id boundary and Area 06 evidence shall be respected.

## 14. Multiple Payment Boundary
Multiple payment records associated with one order shall remain valid payment-grain records unless a documented business rule establishes otherwise.

## 15. Multiple Order Item Boundary
Multiple order-item records within one order shall remain distinct item-grain records and shall not be collapsed merely because they share an order_id.

## 16. Null and Unknown Boundary
Null, unknown, unavailable, and not-applicable values shall remain semantically distinct where the business meaning requires it. Missing values shall not automatically create or remove a business entity.

## 17. Translation Exception Boundary
Unmatched product-category translation values identified in Area 06 shall remain traceable exceptions. Missing translations shall not cause products to disappear from the analytical population.

## 18. Geolocation Boundary
Repeated geolocation rows and multiple observations for a postal-code prefix shall not be collapsed into a single business entity without an approved analytical rule.

## 19. Late and Incomplete Event Boundary
Orders, deliveries, approvals, reviews, and other events with incomplete timestamps shall retain their valid business grain while missing attributes are handled according to documented data-quality rules.

## 20. Ambiguous Grain Resolution
When available attributes cannot establish a unique grain, the record shall be quarantined, represented at a documented lower-confidence boundary, or retained with an explicit exception classification. The system shall not invent identity.

## 21. Cross-Grain Join Boundary
Joins between incompatible grains shall require explicit pre-aggregation, controlled bridge logic, or separate analytical facts. Direct joins that multiply measures shall be prohibited.

## 22. Exception Reconciliation
Exception populations shall have counts, identifiers where permitted, source references, reason codes, disposition, and reconciliation totals so their impact can be measured.

## 23. Exception Lineage and Audit
Every grain exception shall retain source lineage, transformation context, resolution decision, responsible control, and audit evidence sufficient to reproduce the decision.

## 24. Governance and Change Control
Changes to exception interpretation shall require documented impact analysis against business grain, measures, dimensional relationships, downstream marts, metrics, and BI outputs.

## 25. Acceptance Criteria
Area 25.4 is acceptable when known grain exceptions and ambiguity boundaries are explicitly documented, repeated events are not incorrectly deduplicated, null and unknown states remain meaningful, cross-grain joins are controlled, exceptions are reconcilable and traceable, and dependencies on Areas 06, 07, 19–24 are preserved.

