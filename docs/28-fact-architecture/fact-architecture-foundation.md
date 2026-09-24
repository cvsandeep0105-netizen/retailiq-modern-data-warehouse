# Area 28.1 — Fact Architecture Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the foundational fact architecture for RetailIQ, establishing fact responsibilities, business-process alignment, fact grain, event boundaries, measure ownership, dimensional relationships, and analytical consumption rules.

## 2. Area 24 Dependency
Fact architecture shall implement the dimensional modeling strategy established and frozen in Area 24.

## 3. Area 25 Dependency
Every fact shall have an explicit business grain consistent with the Business Grain Definition established in Area 25.

## 4. Area 26 Dependency
Fact identities and dimension references shall use the approved natural-key and surrogate-key strategy established in Area 26.

## 5. Area 27 Dependency
Fact-to-dimension relationships shall use the approved dimension architecture established in Area 27.

## 6. Area 03 Dependency
Fact structures shall support the business processes and analytical questions documented in Area 03.

## 7. Area 06 Dependency
Fact design shall respect source relationships, cardinalities, composite keys, multiplicity, and documented relationship exceptions.

## 8. Area 07 Dependency
Fact source attributes and event identifiers shall remain consistent with the frozen source contracts and schema expectations.

## 9. Area 19 Dependency
Fact measures and event attributes shall preserve the approved transformation and business meaning rules.

## 10. Area 20 Dependency
Fact attributes and measures shall use approved standardized and normalized representations.

## 11. Area 21 Dependency
Fact populations shall use approved record-resolution outcomes while preserving legitimate repeated business events.

## 12. Area 22 Dependency
Fact populations and measures shall remain reconcilable to controlled upstream populations and source totals.

## 13. Area 23 Dependency
Fact grain and measure assumptions shall remain supported by profiling evidence for multiplicity, completeness, uniqueness, and distributions.

## 14. Order Fact Candidate
The order fact candidate shall represent one customer order per row at order grain. It shall contain only order-grain measures and event attributes appropriate to that grain.

## 15. Order Item Fact Candidate
The order-item fact candidate shall represent one order-item line per row using the approved order_id and order_item_id grain. Item-level measures such as price and freight shall belong at this grain.

## 16. Payment Fact Candidate
The payment fact candidate shall represent one payment sequence per order at payment grain. Payment value and payment-specific attributes shall remain at payment grain.

## 17. Review Fact Candidate
The review fact candidate shall represent one review business record at its approved review grain. Review score and review-event attributes shall remain at review grain.

## 18. Fact Grain Independence
Each fact shall maintain one explicit grain. Facts shall not combine order, item, payment, and review records into one physical grain merely for convenience.

## 19. Measure Ownership
Every measure shall belong to the fact whose grain and business process naturally own that measure. Measures shall not be duplicated across facts without an explicit semantic reason.

## 20. Additivity Boundary
Fact measures shall follow the additive, semi-additive, and non-additive rules established in Area 25. Measures shall not be aggregated across incompatible grains.

## 21. Degenerate and Event Identifiers
Business event identifiers such as order_id may remain available within appropriate facts as degenerate or traceability attributes when required, while dimensional relationships use governed surrogate keys.

## 22. Fact-to-Dimension Relationships
Each fact shall explicitly define its dimension foreign keys, expected cardinality, role-playing date relationships, unknown-member behavior, and analytical purpose.

## 23. Multi-Fact Analytical Boundary
Cross-fact analysis shall use conformed dimensions, controlled aggregation, or explicitly governed relationships. Direct joins between incompatible fact grains shall not be used to multiply measures.

## 24. Governance, Lineage and Reconciliation
Every fact shall have documented source lineage, business-process ownership, grain definition, measure definitions, dimension relationships, quality expectations, reconciliation controls, and change-management requirements.

## 25. Acceptance Criteria
Area 28.1 is acceptable when order, order-item, payment, and review fact candidates are explicitly defined by business process and grain; measure ownership and additivity are controlled; fact-to-dimension and cross-fact boundaries are defined; and the architecture remains traceable to Areas 03, 06, 07, 19–27.

