# Area 31.1 — Slowly Changing Dimension Foundation

Status: Accepted & Frozen

## 1. Purpose
Establish the Slowly Changing Dimension (SCD) foundation for RetailIQ, defining how dimension attribute changes, historical preservation, effective periods, current-state representation, and analytical history shall be governed.

## 2. Area 30 Dependency
SCD design shall operate within the frozen conformed and role-playing dimension architecture established in Area 30.

## 3. Area 29 Dependency
Historical dimension behavior shall preserve fact-grain, measure, aggregation, and analytical interpretation defined in Area 29.

## 4. Area 28 Dependency
SCD behavior shall remain compatible with the frozen fact architecture and fact-to-dimension relationships.

## 5. Area 27 Dependency
SCD implementation shall extend the approved dimension architecture, attribute ownership, key strategy, and historical boundaries.

## 6. Area 26 Dependency
Dimension history shall use the approved natural-key and surrogate-key strategy, with surrogate keys identifying dimension versions where historical tracking is required.

## 7. Area 25 Dependency
Historical dimension records shall preserve the declared business grain and shall not change fact-grain semantics.

## 8. Area 24 Dependency
SCD decisions shall follow the approved dimensional modeling strategy and historical modeling patterns.

## 9. Area 23 Dependency
Historical modeling decisions shall consider profiling evidence for attribute completeness, stability, uniqueness, and observed source behavior.

## 10. Area 22 Dependency
Dimension changes and historical populations shall remain reconcilable to upstream source populations.

## 11. Area 21 Dependency
SCD processing shall respect approved duplicate detection and record-resolution outcomes before creating historical dimension versions.

## 12. Area 20 Dependency
Dimension attributes shall be standardized before historical change detection so equivalent representations do not create false changes.

## 13. Area 19 Dependency
Historical attributes shall preserve approved transformation semantics and business meaning.

## 14. Area 07 Dependency
Change-detection attributes shall remain traceable to approved source contracts and schema expectations.

## 15. SCD Purpose Boundary
SCD controls shall distinguish between attributes whose historical changes matter analytically and attributes where current-state representation is sufficient. Not every dimension attribute requires historical versioning.

## 16. Historical Change Principle
When an analytically significant dimension attribute changes, the model shall preserve the applicable historical state according to the selected SCD behavior rather than silently overwriting historical context.

## 17. Natural Key and Surrogate Key Principle
The natural business identifier shall identify the underlying entity, while the surrogate key shall identify the applicable dimension version when historical versioning is required.

## 18. Effective Dating Principle
Historically versioned records shall have governed effective-start and effective-end semantics and an explicit current-version indicator where applicable.

## 19. Current-State Principle
Current-state reporting shall identify the active dimension version without destroying prior historical versions required for historical analysis.

## 20. Attribute Change Classification
Dimension attributes shall be classified as historically significant, current-state-only, derived, descriptive, operational, or otherwise governed before an SCD strategy is assigned.

## 21. Candidate Dimension Scope
Customer, product, seller, and applicable geography dimensions shall be evaluated for SCD behavior based on business meaning, source change characteristics, analytical requirements, and historical usefulness.

## 22. Date Dimension Boundary
The Date dimension is governed primarily as a calendar reference dimension. It shall not be treated as an ordinary entity SCD merely because business facts contain multiple date roles.

## 23. Unknown and Not-Applicable Members
Unknown, not-applicable, and unresolved dimension members shall be governed explicitly and shall not be confused with historical versions of legitimate entities.

## 24. Governance, Lineage and Change Control
Every SCD decision shall document the attribute, business rationale, selected historical behavior, source lineage, key behavior, effective dating rules, reconciliation expectations, and change-control requirements.

## 25. Acceptance Criteria
Area 31.1 is acceptable when the SCD foundation defines historical-change principles, key and effective-dating behavior, current-state handling, attribute classification, candidate dimension scope, unknown-member boundaries, and governance controls, with dependencies from Areas 07, 19–30 preserved.

