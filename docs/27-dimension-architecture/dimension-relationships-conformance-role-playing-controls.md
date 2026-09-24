# Area 27.4 — Dimension Relationships, Conformance & Role-Playing Controls

Status: Accepted & Frozen

## 1. Purpose
Define dimension relationships, conformed-dimension behavior, role-playing dimensions, relationship cardinality, shared analytical semantics, and cross-fact consistency controls for RetailIQ.

## 2. Area 27.1 Dependency
Relationship design shall implement the approved dimension architecture foundation.

## 3. Area 27.2 Dependency
Dimension relationships shall use the registered candidate dimensions, attributes, and source mappings.

## 4. Area 27.3 Dependency
Relationships and hierarchies shall preserve the approved attribute semantics and drill-down boundaries.

## 5. Area 24 Dependency
Conformance and role-playing behavior shall follow the dimensional modeling patterns established in Area 24.

## 6. Area 25 Dependency
Relationships shall preserve the declared grain of each dimension and associated fact.

## 7. Area 26 Dependency
Dimension relationships shall use governed surrogate keys and approved natural-key traceability.

## 8. Area 06 Dependency
Source cardinalities and relationship boundaries shall constrain analytical relationships.

## 9. Area 22 Dependency
Dimension relationships shall remain reconcilable through controlled key populations and relationship counts.

## 10. Area 23 Dependency
Profiling evidence shall support expected relationship cardinality, completeness, and multiplicity assumptions.

## 11. Conformed Dimension Definition
A conformed dimension provides consistent business definitions, keys, attributes, and semantics across multiple analytical facts or data marts.

## 12. Customer Conformance
The Customer dimension shall use one governed definition of customer identity and shared customer attributes wherever customer analysis is required across RetailIQ facts and marts.

## 13. Product Conformance
The Product dimension shall provide one governed product identity and consistent product-category semantics across order-item, sales, and related analytical facts.

## 14. Seller Conformance
The Seller dimension shall provide one governed seller identity and consistent seller attributes wherever seller analysis is required.

## 15. Date Conformance
The Date dimension shall be reusable across all applicable facts and business events. Date relationships shall use explicit role names rather than creating separate physical date dimensions for every event.

## 16. Geography Conformance
Where geography is shared across customer, seller, or other analytical contexts, the governed geographic semantics shall remain consistent. Distinct source geographic roles shall not be conflated.

## 17. Role-Playing Date Relationships
Order purchase date, approval date, carrier delivery date, customer delivery date, review creation date, review response date, and estimated delivery date shall use controlled role-playing relationships to the reusable Date dimension.

## 18. Role Naming Convention
Every role-playing relationship shall have an explicit business name identifying the event represented by the date relationship, preventing ambiguity when the same dimension is referenced multiple times.

## 19. Fact-to-Dimension Relationship
Each fact-to-dimension relationship shall identify the fact grain, dimension grain, foreign-key path, expected cardinality, null or unknown behavior, and analytical purpose.

## 20. Dimension-to-Dimension Relationship
Direct dimension-to-dimension relationships shall be used only where the business relationship is explicit and analytically governed. Convenience joins that create ambiguous paths shall be avoided.

## 21. Conformed Attribute Consistency
Shared attributes such as customer identity, product category, seller identity, calendar classifications, and governed geography shall retain consistent definitions across all consuming models.

## 22. Cross-Fact Consistency
Conformed dimensions shall allow comparable analysis across multiple facts without changing the meaning of the shared dimension or introducing incompatible grain relationships.

## 23. Referential Integrity and Unknown Members
All dimension relationships shall resolve through approved surrogate keys or governed unknown/not-applicable members. Uncontrolled orphan relationships shall not be published.

## 24. Relationship Lineage and Governance
Every dimension relationship shall document its source lineage, key path, cardinality, grain compatibility, business meaning, ownership, validation controls, and change-management requirements.

## 25. Acceptance Criteria
Area 27.4 is acceptable when conformed dimensions, role-playing dates, fact-to-dimension relationships, dimension-to-dimension boundaries, cross-fact consistency, referential integrity, cardinality, lineage, and governance controls are explicitly defined and traceable to Areas 22–26 and 27.1–27.3.

