# Area 21.2 — Duplicate Detection & Classification Rules

Status: Accepted & Frozen

## 1. Purpose
Define deterministic duplicate-detection and duplicate-classification rules for the RetailIQ analytical data foundation while preserving source evidence and business meaning.

## 2. Area 21.1 Foundation Dependency
Area 21.2 depends on the complete and frozen Area 21.1 Deduplication & Record Resolution Foundation.

## 3. Area 20 Standardization Dependency
Area 21.2 depends on the complete and frozen Area 20 Data Standardization & Normalization.

## 4. Area 19 Transformation Dependency
Area 21.2 depends on the complete and frozen Area 19 Staging Transformations.

## 5. Area 06 Relationship Dependency
Duplicate rules must preserve the relationship, key, cardinality, and duplicate evidence established in Area 06.

## 6. Area 07 Contract Dependency
Duplicate detection must remain consistent with the structural schema and uniqueness expectations established in Area 07.

## 7. Exact Duplicate Rule
An exact duplicate is identified when the complete approved comparison attribute set is identical. Exact equality must be defined against the applicable entity and documented comparison boundary.

## 8. Key-Based Duplicate Rule
Key-based duplicates are identified when a documented natural key or composite business key occurs more than once where uniqueness is expected.

## 9. Composite-Key Rule
Composite-key duplicate detection must evaluate the complete approved key combination rather than assuming uniqueness from an individual attribute.

## 10. Review Duplicate Rule
Review records must respect the documented review identity boundary. Review ID alone must not be assumed unique where Area 06 evidence demonstrates repeated review IDs.

## 11. Order Item Duplicate Rule
Order-item identity must respect the approved composite order_id and order_item_id boundary.

## 12. Payment Duplicate Rule
Payment identity must respect the approved composite order_id and payment_sequential boundary.

## 13. Source Duplicate Rule
Observed source duplicates must be classified and preserved as source conditions unless an explicit downstream resolution rule is approved.

## 14. Near-Duplicate Rule
Near-duplicate detection may only be performed using documented matching attributes and deterministic thresholds. Similarity alone does not establish record identity.

## 15. Duplicate Classification
Each detected duplicate condition must be classified as exact duplicate, key-based duplicate, composite-key duplicate, source-observed duplicate, near-duplicate candidate, or other approved category.

## 16. Ambiguity Classification
Records that cannot be deterministically classified must be marked ambiguous and routed to controlled exception handling rather than automatically merged or deleted.

## 17. Cross-Entity Boundary
Duplicate rules must not merge records across different business entities merely because identifiers or attribute values appear similar.

## 18. Business Meaning Preservation
Duplicate detection must not alter source business meaning, event history, financial values, relationship semantics, or approved record identity.

## 19. Reconciliation Controls
Duplicate detection results must reconcile input record counts, duplicate groups, retained records, unresolved records, identifiers, and applicable relationships.

## 20. Evidence and Lineage
Every duplicate classification must retain evidence identifying the source records, comparison rule, affected attributes, classification result, processing version, and downstream disposition.

## 21. Environment and Repository Dependencies
Area 21.2 explicitly depends on Area 08 Environment Architecture, Area 09 Repository & Engineering Standards, Area 13 Environment Architecture, and Area 14 Repository & Engineering Standards.

## 22. Storage and Technology Dependencies
Area 21.2 explicitly depends on Area 10 Storage & Schema Architecture, Area 12 Technology Evaluation & Decision Matrix, and Area 15 Storage & Schema Architecture.

## 23. Downstream Modeling Boundary
Duplicate classification provides controlled inputs for later record resolution and modeling but does not define final dimension, fact, surrogate-key, slowly changing dimension, or data-mart implementation.

## 24. Technology-Neutral Boundary
This artifact defines duplicate detection and classification rules without selecting a specific warehouse, database, SQL engine, transformation framework, matching library, orchestration platform, cloud service, or BI technology.

## 25. Acceptance Criteria
Area 21.2 may be accepted only when exact, key-based, composite-key, source, near-duplicate, ambiguity, cross-entity, preservation, reconciliation, evidence, lineage, dependency, and technology-neutral controls are documented and validated.

