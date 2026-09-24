# Area 07 — Data Contracts & Schema Expectations

## Document Status
- Status: Accepted & Frozen
- Area: 07
- Step: 07.1 — Data Contract Foundation
- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform

## Purpose
Define the engineering contract framework that governs how source datasets are expected to behave before ingestion and downstream transformation.

## Data Contract Scope
The contracts will define expected structure, identity, data types, nullability, domain expectations, relationship expectations, temporal expectations, and controlled exceptions for source datasets.

## Contract Principles
1. Source contracts describe expectations; they do not modify source data.
2. Contracts must be traceable to observed physical source evidence.
3. Business rules must be distinguished from physical source observations.
4. Known source exceptions must be explicitly documented rather than silently corrected.
5. Schema changes must be detectable.
6. Key and relationship expectations must be explicit.
7. Nullability expectations must distinguish legitimate source nulls from unexpected data-quality failures.
8. Domain constraints must be testable.
9. Contract violations must be observable and actionable.
10. Downstream models must not silently redefine source meaning.

## Contract Layers
- Structural contract: columns, names, and physical data types.
- Identity contract: primary/business keys and uniqueness expectations.
- Nullability contract: required, optional, and conditionally nullable fields.
- Domain contract: permitted categorical and value ranges.
- Relationship contract: expected parent-child relationships.
- Temporal contract: date/time fields and valid temporal boundaries.
- Volume contract: expected record-volume behavior and anomaly detection.
- Semantic contract: documented meaning and grain of important fields.
- Exception contract: known and accepted source anomalies.

## Source Boundary
Contracts apply to the nine discovered Olist source datasets used by RetailIQ.

## Source Preservation
No contract implementation may mutate, deduplicate, overwrite, or otherwise alter the original source files.

## Traceability Requirement
Every contract expectation must be traceable to Area 05 physical profiling evidence, Area 06 relationship/dependency evidence, or an explicitly documented engineering decision.

## Acceptance Boundary
Step 07.1 is complete when the contract framework, contract layers, source boundary, preservation rules, and traceability requirements are documented.

## Next Step
Step 07.2 will define the source contract inventory and assign contract coverage to each source dataset.

