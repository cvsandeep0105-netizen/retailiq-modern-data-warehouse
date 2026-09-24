# Area 27.2 — Dimension Candidate Register & Attribute Mapping

Status: Accepted & Frozen

## 1. Purpose
Create the formal RetailIQ dimension candidate register and map each dimension to its business entity, grain, natural identity, surrogate-key requirement, source attributes, descriptive attributes, and analytical responsibilities.

## 2. Area 27.1 Dependency
The candidate register operationalizes the dimension architecture foundation established in Area 27.1.

## 3. Area 24 Dependency
Dimension candidates shall follow the dimensional modeling strategy and design patterns established in Area 24.

## 4. Area 25 Dependency
Every candidate dimension shall have an explicit business grain defined in Area 25.

## 5. Area 26 Dependency
Each candidate dimension shall use the approved natural-key and surrogate-key boundaries established in Area 26.

## 6. Area 06 Dependency
Candidate relationships and attribute ownership shall respect source relationships, cardinalities, uniqueness, and documented exceptions.

## 7. Area 07 Dependency
Candidate attributes shall remain traceable to the frozen source contracts and physical schema expectations.

## 8. Area 19 Dependency
Attribute mappings shall preserve the approved transformation and business-meaning rules.

## 9. Area 20 Dependency
Candidate attributes shall use approved standardized and normalized representations.

## 10. Area 21 Dependency
Dimension populations shall use approved record-resolution outcomes and preserve legitimate repeated events.

## 11. Area 22 Dependency
Candidate dimension populations shall remain reconcilable to upstream controlled populations.

## 12. Area 23 Dependency
Profiling evidence shall inform attribute completeness, uniqueness, cardinality, and quality expectations.

## 13. Customer Dimension Candidate
Customer dimension candidate: one analytical customer entity per row. Candidate attributes include customer identity, customer location, city, state, and approved source-reference attributes.

## 14. Product Dimension Candidate
Product dimension candidate: one analytical product entity per row. Candidate attributes include product category, translated category where available, product descriptive measurements, dimensions, weight, photos quantity, and governed source-reference attributes.

## 15. Seller Dimension Candidate
Seller dimension candidate: one analytical seller entity per row. Candidate attributes include seller identity, postal-code prefix, city, state, and approved source-reference attributes.

## 16. Date Dimension Candidate
Date dimension candidate: one calendar date per row. Candidate attributes include calendar date, year, quarter, month, week, day, weekday, and other governed calendar attributes required by analytical use cases.

## 17. Geography Dimension Candidate
Geography dimension candidate: one governed geographic entity per row at an explicitly selected grain. Postal-code prefixes, cities, and states shall not be conflated without a documented geographic hierarchy.

## 18. Role-Playing Attribute Mapping
Order purchase, approval, carrier delivery, customer delivery, review creation, review response, estimated delivery, and other date roles shall map to the reusable Date dimension through controlled role-playing relationships.

## 19. Attribute Classification
Every candidate attribute shall be classified as identifier, descriptive attribute, analytical grouping attribute, derived attribute, operational reference, or excluded implementation detail.

## 20. Attribute Source Mapping
Each retained dimensional attribute shall identify its source object and source column, transformation or standardization dependency, business meaning, and downstream ownership.

## 21. Null and Unknown Attribute Handling
Nullable descriptive attributes shall retain documented semantic meaning. Unknown, unavailable, and not-applicable conditions shall not be silently converted into misleading descriptive values.

## 22. Attribute Change Classification
Candidate attributes shall be classified according to expected change behavior so later historical modeling can distinguish stable, slowly changing, and derived attributes.

## 23. Dimension Exclusion Boundary
Measures, transactional event records, payment events, order-item events, review events, and other fact-level records shall not be incorrectly embedded as dimension attributes merely for convenience.

## 24. Candidate Register Governance
Any change to a dimension candidate, attribute ownership, grain, key boundary, or source mapping shall require documented rationale, impact analysis, lineage review, reconciliation evidence, and controlled approval.

## 25. Acceptance Criteria
Area 27.2 is acceptable when customer, product, seller, date, and geography dimension candidates are formally registered, their grains and keys are mapped, major attributes have source and business mappings, role-playing date usage is defined, fact-versus-dimension boundaries are controlled, and dependencies on Areas 06, 07, 19–26 and 27.1 are preserved.

