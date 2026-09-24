# Area 17.2 — Raw Structural & Schema Validation Controls

Status: Accepted & Frozen

## 1. Purpose
Define controlled structural and schema validation rules for raw data before downstream processing.

## 2. Validation Scope
Validation covers source objects, files or objects, columns, identifiers, data types, schema structure, and documented source-contract expectations.

## 3. Source Object Validation
Each expected Olist source object must be identifiable and validated against the approved source inventory.

## 4. File and Object Presence
Expected source files or objects must be checked for presence, identity, accessibility, and association with the correct ingestion batch.

## 5. Column Presence Validation
Required columns must be present according to the structural schema contract established in Area 07.

## 6. Unexpected Column Detection
Unexpected columns must be detected and recorded as schema exceptions rather than silently incorporated into the accepted contract.

## 7. Missing Column Detection
Missing required columns must cause a validation exception and prevent uncontrolled downstream processing.

## 8. Column Data Type Validation
Observed column data types must be compared with the approved physical schema expectations.

## 9. Identifier Validation
Required source identifiers must be present and must satisfy the applicable structural expectations.

## 10. Nullability Validation
Nullability must be evaluated according to the approved source contract. Observed nulls must not be changed merely to satisfy validation.

## 11. Schema Drift Detection
Structural changes between expected and observed source schemas must be detected, classified, recorded, and controlled before downstream use.

## 12. Source Contract Dependency
Validation rules must remain aligned with Area 07 data contracts and schema expectations.

## 13. Source Preservation Boundary
Validation must inspect source data without modifying, deduplicating, normalizing, enriching, or replacing source values.

## 14. Validation Result Classification
Validation results must distinguish successful validation, warning conditions, recoverable exceptions, and blocking validation failures.

## 15. Exception Traceability
Every structural or schema exception must be traceable to the source object, ingestion batch, affected field or structure, and applicable validation rule.

## 16. Acceptance Boundary
Blocking structural or schema failures must prevent the affected input from entering the accepted downstream processing boundary.

## 17. Quarantine Dependency
Inputs requiring investigation must follow the quarantine controls established in Area 16.

## 18. Validation Evidence
Validation execution must produce evidence sufficient to demonstrate expected schema, observed schema, validation result, exceptions, and processing decision.

## 19. Reconciliation Boundary
Schema validation results must remain reconcilable with ingestion batch identity, accepted inputs, rejected inputs, and downstream handoff.

## 20. Lineage Boundary
Structural validation outcomes must remain connected to source identity, batch identity, raw representation, and downstream processing context.

## 21. Operational Monitoring
Schema failures, drift events, exception counts, and validation status must be observable through operational controls.

## 22. Technology Evaluation Dependency
Implementation must remain within the technology evaluation boundary established in Area 12.

## 23. Security Boundary
Validation must operate under the project's approved access, ownership, security, and artifact-hygiene controls.

## 24. Technology-Neutral Boundary
This control defines structural and schema validation responsibilities without selecting a specific warehouse, storage, ingestion, orchestration, or cloud technology.

## 25. Next Step
After Area 17.2 validation and acceptance, proceed sequentially to the next approved Area 17 sub-area.

