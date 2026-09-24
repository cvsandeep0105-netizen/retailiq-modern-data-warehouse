# Area 28.4 — Fact Relationships, Conformance & Analytical Join Controls

Status: Accepted & Frozen

## 1. Purpose
Define controlled relationships between RetailIQ facts and dimensions, conformed analytical paths, role-playing dimensions, cross-fact joins, referential integrity, and measure-preserving analytical access.

## 2. Area 28.1 Dependency
Fact relationships shall implement the approved fact architecture foundation.

## 3. Area 28.2 Dependency
Fact relationships shall remain consistent with the approved fact candidate register and business-process mappings.

## 4. Area 28.3 Dependency
Analytical joins shall preserve the approved grain, measure ownership, additivity, and double-counting controls.

## 5. Area 24 Dependency
Relationships shall follow the dimensional modeling patterns established in Area 24.

## 6. Area 25 Dependency
All joins shall respect the declared business grain and aggregation boundaries.

## 7. Area 26 Dependency
Fact-to-dimension relationships shall use governed surrogate-key mappings while retaining natural identifiers where required for traceability.

## 8. Area 27 Dependency
Dimension relationships shall use the conformed and role-playing dimension architecture established in Area 27.

## 9. Area 03 Dependency
Analytical join paths shall support documented business processes and analytical questions without changing their intended grain.

## 10. Area 06 Dependency
Source cardinality and relationship multiplicity shall inform fact relationship constraints.

## 11. Area 07 Dependency
Relationship keys and source identifiers shall remain consistent with frozen data contracts.

## 12. Area 19 Dependency
Join attributes shall preserve transformation and business meaning rules.

## 13. Area 20 Dependency
Join keys and analytical attributes shall use standardized representations.

## 14. Area 21 Dependency
Resolved records shall not be re-expanded through uncontrolled joins that recreate duplicate business events.

## 15. Area 22 Dependency
Relationship paths shall support reconciliation of fact populations and measures.

## 16. Area 23 Dependency
Observed source cardinalities and multiplicities shall inform relationship and join controls.

## 17. Order Fact Relationships
The order fact shall relate to applicable customer and date dimensions through governed keys. Order-grain measures shall not be multiplied by joining directly to multi-row item, payment, or review facts.

## 18. Order Item Fact Relationships
The order-item fact shall relate to customer, product, seller, and applicable date dimensions. Product and seller relationships shall remain at item grain.

## 19. Payment Fact Relationships
The payment fact shall relate to customer, order-related analytical context, and applicable date dimensions through controlled keys. Payment measures shall not be multiplied by item or review relationships.

## 20. Review Fact Relationships
The review fact shall relate to applicable customer and date dimensions. Review measures shall remain independent of item and payment multiplicity unless an explicit aggregation boundary is applied.

## 21. Conformed Dimension Controls
Customer, product, seller, date, and applicable geography dimensions shall provide shared analytical context across compatible facts. Conformance shall not imply that every dimension applies to every fact.

## 22. Role-Playing Date Controls
Multiple business timestamps shall use explicitly named role-playing Date relationships such as purchase date, approval date, carrier date, delivery date, estimated delivery date, payment date, and review date where applicable.

## 23. Referential Integrity Controls
Every dimension foreign key shall resolve to an approved dimension member or governed unknown/not-applicable member. Orphan fact records shall be detected and reconciled.

## 24. Analytical Join and Lineage Controls
Approved analytical join paths shall document join keys, expected cardinality, grain before and after the join, aggregation boundary, measure-preservation rule, and lineage. Uncontrolled many-to-many fact joins shall be prohibited.

## 25. Acceptance Criteria
Area 28.4 is acceptable when order, order-item, payment, and review fact relationships are defined; conformed and role-playing dimensions are controlled; referential integrity is addressed; cross-fact joins preserve measures and grain; and analytical join lineage and reconciliation controls are documented.

