# Area 26.3 — Surrogate Key Strategy & Generation Controls

Status: Accepted & Frozen

## 1. Purpose
Define the RetailIQ surrogate-key strategy, generation rules, uniqueness controls, historical behavior, unknown-member handling, and operational boundaries.

## 2. Area 26.1 Dependency
Surrogate-key strategy shall implement the foundation established in Area 26.1.

## 3. Area 26.2 Dependency
Every surrogate key shall map to a registered natural identity and business grain from Area 26.2.

## 4. Area 25 Dependency
Surrogate keys shall never redefine the business grain established in Area 25.

## 5. Area 24 Dependency
Surrogate-key design shall support the dimensional patterns and historical modeling boundaries established in Area 24.

## 6. Area 21 Dependency
Record-resolution outcomes shall be established before surrogate keys are assigned to analytical entities.

## 7. Area 22 Dependency
Surrogate-key populations shall reconcile to approved natural-key populations and exception counts.

## 8. Area 23 Dependency
Key-generation assumptions shall remain consistent with observed source uniqueness and multiplicity evidence.

## 9. Surrogate Key Purpose
Surrogate keys provide warehouse-local analytical identity for dimensions and other structures where stable technical references are required independently of source business identifiers.

## 10. Surrogate Key Independence
Surrogate keys shall not encode business meaning, source-system semantics, geographic meaning, dates, categories, or mutable descriptive attributes.

## 11. Dimension Surrogate Keys
Customer, product, seller, date, geography, and other applicable dimensions shall use warehouse-local surrogate keys where required by the dimensional architecture.

## 12. Fact Foreign-Key Strategy
Fact records shall reference the applicable dimension surrogate keys while retaining approved natural identifiers where needed for traceability and reconciliation.

## 13. Natural-to-Surrogate Mapping
Each dimension surrogate key shall maintain a controlled mapping to its natural business identifier or approved composite identity.

## 14. Determinism and Reproducibility
Surrogate-key generation shall produce controlled, collision-free identifiers. Reprocessing shall not unintentionally create conflicting identities for the same governed dimensional version.

## 15. Uniqueness Control
Each surrogate key shall be unique within its defined dimensional entity and analytical environment.

## 16. Collision Prevention
Generation mechanisms shall prevent key collisions and shall include validation capable of detecting duplicate surrogate keys before analytical publication.

## 17. Historical Version Boundary
When a dimension supports historical versions, separate surrogate keys may represent separate valid versions of the same natural entity. The natural identifier remains the business identity while the surrogate key identifies the analytical version.

## 18. Unknown Member Strategy
A governed surrogate-key representation shall exist for records whose dimension relationship is unknown at fact-load time. This prevents uncontrolled null foreign keys while preserving analytical row counts.

## 19. Not-Applicable Strategy
Where a dimension relationship is genuinely not applicable, a distinct governed surrogate-key representation may be used rather than conflating not-applicable with unknown.

## 20. Late-Arriving Dimension Strategy
Facts arriving before their corresponding dimension record shall use the governed temporary or unknown-member approach and shall be reconciled when the dimension becomes available.

## 21. Key Reprocessing Control
Reprocessing the same approved natural identity shall preserve the intended surrogate identity and shall not generate uncontrolled duplicate dimension members.

## 22. Referential Integrity
Published fact foreign keys shall resolve to valid dimension surrogate keys or approved unknown/not-applicable members according to the dimensional contract.

## 23. Key Lineage and Audit
Surrogate-key generation shall retain lineage to the source natural key, generation process, dimensional version, load context, and validation evidence.

## 24. Technology-Neutral Generation Boundary
The conceptual strategy is independent of a specific warehouse engine. Physical key-generation implementation shall be selected and documented during implementation without changing the approved business-key semantics.

## 25. Acceptance Criteria
Area 26.3 is acceptable when surrogate-key purpose, generation, uniqueness, collision prevention, historical versioning, unknown/not-applicable handling, late-arriving dimensions, referential integrity, and lineage controls are explicitly defined and traceable to Areas 21, 22, 23, 24, 25, and 26.1–26.2.

