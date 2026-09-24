# Area 30.4 — Conformed Dimension Quality, Reconciliation & Exception Controls

Status: Accepted & Frozen

## 1. Purpose
Define quality, reconciliation, exception, integrity, semantic-consistency, and audit controls for RetailIQ conformed and role-playing dimensions.

## 2. Area 30.1 Dependency
Quality controls shall validate the approved conformed and role-playing dimension foundation.

## 3. Area 30.2 Dependency
Quality validation shall cover the approved conformed-dimension register and fact mappings.

## 4. Area 30.3 Dependency
Role-playing date mappings and semantic controls shall be included in quality and exception validation.

## 5. Area 29 Dependency
Dimension quality shall preserve fact-grain, measure, aggregation, and analytical usage boundaries.

## 6. Area 28 Dependency
Dimension quality shall remain consistent with frozen fact relationships and analytical join controls.

## 7. Area 27 Dependency
Quality controls shall implement the approved dimension architecture and attribute relationships.

## 8. Area 26 Dependency
Dimension keys shall be validated against the approved natural-key and surrogate-key strategy.

## 9. Area 25 Dependency
Dimension relationships shall preserve business grain and prevent unintended measure multiplication.

## 10. Area 24 Dependency
Quality controls shall follow approved dimensional modeling patterns.

## 11. Area 03 Dependency
Dimension quality shall preserve the business meaning required by analytical questions.

## 12. Area 06 Dependency
Relationship cardinality and source multiplicity shall inform conformance validation.

## 13. Area 07 Dependency
Dimension identifiers and attributes shall remain traceable to source contracts.

## 14. Area 19 Dependency
Quality controls shall validate transformation and business meaning preservation.

## 15. Area 20 Dependency
Shared dimension attributes shall use standardized representations across consuming facts.

## 16. Area 21 Dependency
Dimension populations shall respect approved duplicate detection and record-resolution controls.

## 17. Area 22 Dependency
Conformed dimension populations and fact relationships shall support reconciliation to upstream controls.

## 18. Area 23 Dependency
Quality expectations shall consider profiling evidence for completeness, uniqueness, nullability, and value domains.

## 19. Key Integrity Controls
Customer, product, seller, date, and applicable geography dimension keys shall be checked for uniqueness, validity, referential integrity, unexpected nulls, and governed unknown or not-applicable members.

## 20. Semantic Consistency Controls
Shared dimension attributes shall retain identical business definitions, data meanings, units, and transformation semantics wherever the same conformed attribute is consumed across facts.

## 21. Role-Playing Date Quality
Each role-playing date relationship shall be checked for valid timestamp mapping, correct semantic role, null behavior, prohibited substitutions, and consistency with its consuming fact.

## 22. Cross-Fact Reconciliation
Shared dimension populations and fact-to-dimension relationships shall reconcile across compatible facts. Differences caused by legitimate fact-grain boundaries shall be documented rather than treated as defects.

## 23. Exception Classification
Exceptions shall be classified as missing dimension member, invalid key, duplicate dimension identity, semantic mismatch, role-mapping error, unexpected null, source anomaly, reconciliation variance, or unresolved business ambiguity.

## 24. Audit, Lineage and Remediation Controls
Every failed conformance check shall retain the validation rule, affected population, observed result, expected result, source lineage, disposition, remediation, and regression evidence. Corrections shall require controlled revalidation before acceptance.

## 25. Acceptance Criteria
Area 30.4 is acceptable when conformed dimensions and role-playing relationships have defined key-integrity, semantic-consistency, quality, reconciliation, exception, audit, lineage, and remediation controls, with dependencies from Areas 03, 06, 07, 19–29 and 30.1–30.3 preserved.

