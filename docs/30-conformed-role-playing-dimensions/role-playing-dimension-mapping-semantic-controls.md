# Area 30.3 — Role-Playing Dimension Mapping & Semantic Controls

Status: Accepted & Frozen

## 1. Purpose
Define detailed role-playing dimension mappings and semantic controls for RetailIQ, ensuring that one governed dimension can support multiple business contexts without creating ambiguous analytical meaning.

## 2. Area 30.1 Dependency
Role-playing mappings shall implement the conformed and role-playing dimension foundation.

## 3. Area 30.2 Dependency
Role-playing relationships shall extend the approved conformed-dimension register and fact mapping.

## 4. Area 29 Dependency
Role-playing relationships shall preserve approved fact grain, measure ownership, aggregation, and analytical usage boundaries.

## 5. Area 28 Dependency
Role-playing mappings shall remain consistent with frozen fact architecture and analytical join controls.

## 6. Area 27 Dependency
Dimension roles shall follow the approved dimension architecture and role-playing controls.

## 7. Area 26 Dependency
Role-playing relationships shall use governed surrogate keys and preserve natural-key traceability.

## 8. Area 25 Dependency
Every role shall preserve the business grain of the consuming fact.

## 9. Area 24 Dependency
Role-playing implementation shall follow approved dimensional modeling patterns.

## 10. Area 03 Dependency
Semantic roles shall correspond to documented business events and analytical questions.

## 11. Area 06 Dependency
Role mappings shall respect source event relationships, cardinality, and multiplicity.

## 12. Area 07 Dependency
Business timestamps and identifiers used by role-playing relationships shall remain traceable to source contracts.

## 13. Area 19 Dependency
Timestamp and role transformations shall preserve approved source business meaning.

## 14. Area 20 Dependency
Role-playing attributes shall use standardized temporal and identifier representations.

## 15. Area 21 Dependency
Role mappings shall not recreate duplicate records or alter approved record-resolution outcomes.

## 16. Area 22 Dependency
Role-playing relationships shall support reconciliation of fact populations by business event.

## 17. Area 23 Dependency
Role selection and timestamp behavior shall remain consistent with profiling evidence and observed completeness.

## 18. Purchase Date Role
Purchase date shall represent the business date associated with order purchase activity. It shall be distinct semantically from approval, carrier, delivery, and estimated delivery roles.

## 19. Approval Date Role
Approval date shall represent the approved order event timestamp when available. Missing approval timestamps shall remain governed by the applicable null or unknown-date policy rather than being silently substituted.

## 20. Carrier Date Role
Carrier date shall represent the order event associated with carrier handoff or delivery-to-carrier activity. It shall remain distinct from customer delivery and estimated delivery dates.

## 21. Customer Delivery Date Role
Customer delivery date shall represent the actual customer delivery event. It shall not be substituted with estimated delivery when the actual event is unavailable.

## 22. Estimated Delivery Date Role
Estimated delivery date shall represent the expected delivery date supplied by the source business process. It shall remain semantically distinct from actual delivery.

## 23. Payment and Review Date Roles
Payment date and review-related dates shall use explicit semantic roles when represented in the analytical model. Review creation and review answer timestamps shall not be treated as interchangeable events.

## 24. Semantic, Join and Governance Controls
Every role-playing relationship shall document role name, source timestamp, business meaning, consuming fact, grain, key relationship, null behavior, lineage, and prohibited substitutions. Role-playing dates shall not be joined together as independent business events merely because they originate from the same order.

## 25. Acceptance Criteria
Area 30.3 is acceptable when all approved role-playing date contexts have explicit semantic definitions, source mappings, consuming facts, null behavior, key relationships, lineage, and substitution controls, with dependencies from Areas 03, 06, 07, 19–29 and 30.1–30.2 preserved.

