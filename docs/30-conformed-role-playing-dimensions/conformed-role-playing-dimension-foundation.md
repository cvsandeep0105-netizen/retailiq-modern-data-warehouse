# Area 30.1 — Conformed & Role-Playing Dimension Foundation

Status: Accepted & Frozen

## 1. Purpose
Establish the foundation for conformed and role-playing dimensions across RetailIQ facts, ensuring shared analytical meaning, consistent keys, controlled date roles, and reliable cross-fact analysis.

## 2. Area 29 Dependency
Dimension conformance shall support the approved fact grains, measures, aggregation rules, and analytical usage boundaries established in Area 29.

## 3. Area 28 Dependency
Dimension relationships shall implement the frozen fact architecture and its approved analytical join controls.

## 4. Area 27 Dependency
This area extends the approved dimension architecture, conformance rules, and role-playing relationships defined in Area 27.

## 5. Area 26 Dependency
Conformed dimensions shall use the approved natural-key and surrogate-key strategy.

## 6. Area 25 Dependency
Dimension relationships shall preserve the business grain and shall not introduce measure multiplication across facts.

## 7. Area 24 Dependency
Conformance shall follow the dimensional modeling strategy and approved dimension patterns.

## 8. Area 03 Dependency
Conformed dimensions shall support consistent answers to analytical questions across compatible business processes.

## 9. Area 06 Dependency
Source relationship and cardinality evidence shall constrain dimension conformance and cross-fact relationships.

## 10. Area 07 Dependency
Dimension identifiers and attributes shall remain traceable to approved source contracts.

## 11. Area 19 Dependency
Conformed attributes shall preserve approved transformation and business meaning rules.

## 12. Area 20 Dependency
Shared dimension attributes shall use standardized representations across analytical facts.

## 13. Area 21 Dependency
Dimension populations shall preserve approved record-resolution outcomes and shall not recreate duplicate entities.

## 14. Area 22 Dependency
Conformed dimensions shall support reconciliation of shared analytical populations and relationships.

## 15. Area 23 Dependency
Conformance decisions shall remain supported by profiling evidence for identifiers, attributes, nullability, and value domains.

## 16. Customer Conformed Dimension
The customer dimension shall provide a shared customer analytical context for compatible order, order-item, payment, and review facts. Its surrogate key shall be consistent across all applicable facts.

## 17. Product Conformed Dimension
The product dimension shall provide shared product context for applicable order-item analysis. Product attributes and category relationships shall retain consistent business meaning across analytical consumers.

## 18. Seller Conformed Dimension
The seller dimension shall provide shared seller context for applicable order-item analysis and shall retain governed seller identity and descriptive attributes.

## 19. Date Role-Playing Dimension
The Date dimension shall support multiple business-event roles without creating separate physical date dimensions unnecessarily. Each role shall have an explicit semantic name.

## 20. Approved Date Roles
Potential date roles include purchase date, approval date, carrier handoff date, customer delivery date, estimated delivery date, payment date, review creation date, and review answer date where applicable to the analytical model.

## 21. Geography Conformance
Where geography is used across compatible facts or dimensions, geographic meaning, key strategy, hierarchy, and source lineage shall remain consistent. Source geography ambiguity shall not be silently resolved.

## 22. Conformance Rules
A dimension is conformed only when its business definition, grain, key strategy, attribute semantics, unknown-member behavior, and analytical interpretation are consistent across the facts that consume it.

## 23. Role-Playing Rules
A role-playing dimension shall retain one governed dimension definition while exposing multiple semantic roles through explicit relationships or aliases. Each role must identify its originating business timestamp or context.

## 24. Cross-Fact Analytical Boundary
Conformed dimensions may provide shared analytical context across compatible facts, but conformance does not authorize direct many-to-many fact joins. Fact grain and measure-preservation controls from Areas 28 and 29 remain mandatory.

## 25. Acceptance Criteria
Area 30.1 is acceptable when customer, product, seller, date, and applicable geography conformance principles are defined; role-playing date controls are explicit; key and semantic consistency are established; and dependencies from Areas 03, 06, 07, 19–29 are preserved.

