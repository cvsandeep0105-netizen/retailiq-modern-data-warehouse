# Area 30.2 — Conformed Dimension Register & Fact Mapping

Status: Accepted & Frozen

## 1. Purpose
Create the formal conformed-dimension register and map each approved dimension to compatible RetailIQ facts, business processes, grain, keys, analytical roles, and attribute responsibilities.

## 2. Area 30.1 Dependency
The conformed dimension register shall implement the foundation established in Area 30.1.

## 3. Area 29 Dependency
Dimension mappings shall preserve fact-grain, measure, aggregation, and analytical usage controls.

## 4. Area 28 Dependency
Fact-to-dimension relationships shall remain consistent with the frozen Fact Architecture.

## 5. Area 27 Dependency
Dimension mappings shall follow the approved dimension architecture and candidate register.

## 6. Area 26 Dependency
Dimension and fact relationships shall use the approved natural-key and surrogate-key strategy.

## 7. Area 25 Dependency
Mappings shall preserve business grain and shall not introduce incompatible grain relationships.

## 8. Area 24 Dependency
Mappings shall follow the approved dimensional modeling strategy.

## 9. Area 03 Dependency
Each dimension mapping shall support the business processes and analytical questions for which it is applicable.

## 10. Area 06 Dependency
Source relationship and cardinality evidence shall support each fact-to-dimension mapping.

## 11. Area 07 Dependency
Mapped keys and attributes shall remain traceable to the approved source contracts.

## 12. Area 19 Dependency
Mapped dimension attributes shall preserve approved transformation semantics.

## 13. Area 20 Dependency
Shared dimension attributes shall use standardized representations.

## 14. Area 21 Dependency
Dimension populations shall respect approved record-resolution and duplicate controls.

## 15. Area 22 Dependency
Dimension mappings shall support reconciliation of fact populations and analytical relationships.

## 16. Area 23 Dependency
Dimension mapping assumptions shall remain supported by profiling evidence.

## 17. Customer Dimension Register Entry
Customer dimension is conformed across compatible order, order-item, payment, and review facts. The customer surrogate key provides the shared analytical relationship while customer natural identity remains traceable.

## 18. Product Dimension Register Entry
Product dimension is conformed for order-item analysis and provides consistent product, category, and descriptive context. Product attributes shall retain one governed business meaning.

## 19. Seller Dimension Register Entry
Seller dimension is conformed for order-item analysis and provides governed seller identity, location, and descriptive context.

## 20. Date Dimension Register Entry
Date dimension is conformed across compatible facts. Multiple business timestamps shall map to explicit role-playing date relationships without changing the underlying Date dimension definition.

## 21. Geography Dimension Register Entry
Applicable geography context shall use governed geography semantics and key relationships. Geography shall only be mapped where the business meaning and grain are compatible.

## 22. Fact Mapping Matrix Boundary
Each fact shall explicitly identify applicable dimensions. Order fact may use customer and applicable date roles; order-item fact may use customer, product, seller, geography, and applicable date roles; payment fact may use customer and applicable payment/date context; review fact may use customer and applicable review/date context.

## 23. Role-Playing Date Mapping
Purchase, approval, carrier, delivery, estimated delivery, payment, review creation, and review answer timestamps shall map to explicit semantic date roles when included in analytical models.

## 24. Mapping Governance and Analytical Safety
Each mapping shall document expected cardinality, key relationship, applicable grain, unknown-member behavior, lineage, and prohibited analytical joins. Conformance shall not permit uncontrolled many-to-many fact joins.

## 25. Acceptance Criteria
Area 30.2 is acceptable when the customer, product, seller, date, and applicable geography dimensions are formally registered; fact mappings and role-playing date mappings are explicit; key, grain, lineage, reconciliation, and analytical safety controls are documented; and dependencies from Areas 03, 06, 07, 19–29 and 30.1 are preserved.

