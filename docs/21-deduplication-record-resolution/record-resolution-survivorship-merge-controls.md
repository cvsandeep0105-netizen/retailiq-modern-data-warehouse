# Area 21.3 — Record Resolution, Survivorship & Merge Controls

Status: Accepted & Frozen

## 1. Purpose
Define deterministic controls for resolving duplicate records, selecting survivorship outcomes, preserving source evidence, and controlling any approved record consolidation.

## 2. Area 21.1 Foundation Dependency
Area 21.3 depends on the complete and frozen Area 21.1 Deduplication & Record Resolution Foundation.

## 3. Area 21.2 Detection Dependency
Area 21.3 depends on the complete and frozen Area 21.2 Duplicate Detection & Classification Rules.

## 4. Area 20 Standardization Dependency
Area 21.3 depends on the complete and frozen Area 20 Data Standardization & Normalization.

## 5. Area 19 Transformation Dependency
Area 21.3 depends on the complete and frozen Area 19 Staging Transformations.

## 6. Area 06 Relationship Dependency
Record resolution must preserve the approved source relationships, keys, cardinality boundaries, and documented duplicate evidence established in Area 06.

## 7. Area 07 Contract Dependency
Resolution outcomes must remain consistent with source contracts and schema expectations established in Area 07.

## 8. Resolution Eligibility
Only duplicate conditions that satisfy an approved deterministic resolution rule may proceed to resolution. Unclassified or ambiguous conditions must remain unresolved.

## 9. Resolution Group Formation
Records may be grouped for resolution only when they satisfy the documented entity-specific identity and matching criteria.

## 10. Survivorship Criteria
Survivorship must use deterministic, documented criteria such as trusted source precedence, completeness, validity, recency, or other approved evidence appropriate to the entity.

## 11. Attribute-Level Survivorship
Attribute-level survivorship may select values independently only when the rule preserves business meaning and does not create an invalid combination of attributes.

## 12. Source Precedence
Where multiple source representations exist, source precedence must be explicitly documented. No source may be treated as authoritative solely by assumption.

## 13. Recency and Completeness
Recency and completeness may be used as resolution evidence only when their meaning is appropriate to the affected business entity and the rule is deterministic.

## 14. Merge Eligibility
Records may be merged only when approved identity evidence establishes that they represent the same intended business entity or record boundary.

## 15. Merge Prohibition
Records must not be merged solely because values are similar, names match, identifiers partially overlap, or a probabilistic similarity score exceeds an undocumented threshold.

## 16. Non-Merge Outcomes
Valid outcomes include retain-separately, resolve-to-survivor, link-as-related, quarantine-for-review, or unresolved-exception according to the approved entity-specific rule.

## 17. Source Preservation
Original source records must remain preserved and traceable even when a downstream resolution or consolidation outcome is created.

## 18. Business Meaning Preservation
Resolution and survivorship must preserve business meaning, event history, financial measures, relationship semantics, and source identity.

## 19. Reconciliation and Resolution Evidence
Resolution processing must reconcile input records, resolution groups, survivor records, non-survivor records, unresolved records, excluded records, identifiers, relationships, and applicable control totals.

## 20. Lineage, Audit and Rollback
Every resolution decision must retain source-record references, matching evidence, rule version, survivor selection, decision timestamp or processing context, and sufficient evidence to reproduce or reverse the downstream resolution outcome.

## 21. Environment and Repository Dependencies
Area 21.3 explicitly depends on Area 08 Environment Architecture, Area 09 Repository & Engineering Standards, Area 13 Environment Architecture, and Area 14 Repository & Engineering Standards.

## 22. Storage and Technology Dependencies
Area 21.3 explicitly depends on Area 10 Storage & Schema Architecture, Area 12 Technology Evaluation & Decision Matrix, and Area 15 Storage & Schema Architecture.

## 23. Downstream Modeling Boundary
Record resolution produces controlled resolved-record inputs but does not define final fact-table grain, dimension architecture, surrogate-key implementation, slowly changing dimensions, or final data marts.

## 24. Technology-Neutral Boundary
This artifact defines record-resolution, survivorship, and merge requirements without selecting a specific warehouse, database, SQL engine, transformation framework, matching library, orchestration platform, cloud service, or BI technology.

## 25. Acceptance Criteria
Area 21.3 may be accepted only when resolution eligibility, grouping, survivorship, attribute selection, source precedence, recency and completeness rules, merge eligibility, merge prohibitions, non-merge outcomes, preservation, reconciliation, lineage, audit, rollback, dependencies, and technology-neutral boundaries are documented and validated.

