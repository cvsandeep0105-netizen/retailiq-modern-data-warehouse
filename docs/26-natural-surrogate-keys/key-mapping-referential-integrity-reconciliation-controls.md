# Area 26.4 — Key Mapping, Referential Integrity & Reconciliation Controls

Status: Accepted & Frozen

## 1. Purpose
Define controls for mapping natural keys to surrogate keys, validating referential integrity, reconciling key populations, and detecting key failures before analytical publication.

## 2. Area 26.1 Dependency
Key mapping shall follow the approved natural and surrogate key foundation.

## 3. Area 26.2 Dependency
Natural-key mappings and source identity boundaries shall provide the reference population for reconciliation.

## 4. Area 26.3 Dependency
Surrogate-key generation, uniqueness, historical, unknown-member, and late-arriving controls shall be enforced during key mapping.

## 5. Area 25 Dependency
Key mappings shall preserve the business grains defined in Area 25.

## 6. Area 24 Dependency
Key mappings shall remain consistent with the dimensional architecture and fact/dimension relationships defined in Area 24.

## 7. Area 06 Dependency
Source relationships and composite-key boundaries shall remain intact during analytical key conversion.

## 8. Area 21 Dependency
Only approved record-resolution outcomes shall participate in analytical key assignment.

## 9. Area 22 Dependency
Key reconciliation shall use established control-total and exception-reconciliation principles.

## 10. Area 23 Dependency
Key validation shall account for observed uniqueness, multiplicity, nullability, and distribution characteristics.

## 11. Natural-to-Surrogate Mapping Control
Every approved analytical entity shall have a controlled mapping between its natural identity and its surrogate identity where surrogate keys are used.

## 12. Composite Natural-Key Mapping
Composite identities such as order-item and payment identities shall be mapped using the complete approved composite key rather than any individual component.

## 13. Customer Mapping
Customer analytical identity shall preserve the documented distinction between customer_id and customer_unique_id and shall use the approved business identity consistently.

## 14. Order Mapping
order_id shall remain traceable from source order through analytical order representations and any associated fact relationships.

## 15. Product and Seller Mapping
product_id and seller_id shall map to their respective analytical dimension identities without losing source traceability.

## 16. Review Mapping
Review mapping shall respect the documented review identity boundary and shall not collapse repeated review_id values merely because the identifier repeats.

## 17. Unknown and Not-Applicable Mapping
Unknown and not-applicable dimension references shall use governed surrogate representations and shall be separately identifiable in reconciliation results.

## 18. Referential Integrity Validation
Every published fact foreign key shall resolve to an existing dimension surrogate key or an explicitly governed unknown/not-applicable member.

## 19. Orphan Detection
Key validation shall identify fact records whose foreign keys do not resolve to an approved dimension record and shall prevent uncontrolled publication of orphan relationships.

## 20. Key Population Reconciliation
Distinct natural-key counts, surrogate-key counts, mapped records, unmapped records, unknown-member records, and exception populations shall be reconciled.

## 21. Duplicate Mapping Detection
A natural identity shall not map simultaneously to conflicting active surrogate identities unless historical versioning explicitly permits multiple dimensional versions.

## 22. Historical Mapping Validation
When historical versions exist, effective dates or equivalent version boundaries shall ensure that a fact resolves to the correct dimensional version for its business event.

## 23. Regression and Reprocessing Validation
Repeated processing of the same governed input shall not create uncontrolled surrogate-key changes, duplicate mappings, or referential-integrity failures.

## 24. Audit, Lineage and Failure Handling
Mapping failures shall retain source identifiers, attempted surrogate references, failure reason, affected population, reconciliation impact, and resolution status. All mapping logic shall remain auditable.

## 25. Acceptance Criteria
Area 26.4 is acceptable when natural-to-surrogate mappings, composite-key mappings, referential integrity, orphan detection, population reconciliation, duplicate mapping, historical resolution, reprocessing, and failure-lineage controls are explicitly defined and traceable to Areas 06, 21–25, and 26.1–26.3.

