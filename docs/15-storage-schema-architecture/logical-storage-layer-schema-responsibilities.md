# RetailIQ — Logical Storage Layer & Schema Responsibilities

## Status
- Status: Accepted & Frozen
- Area: 15.2
- Purpose: Define logical storage layers and schema responsibilities without prematurely binding the architecture to a specific technology.

## 1. Logical Layer Model
The RetailIQ platform uses controlled logical layers to separate source preservation, processing, analytical modeling, and business consumption responsibilities.

The logical flow is:
Source → Landing/Raw → Staging → Intermediate → Facts & Dimensions → Data Marts → Metrics/Semantic → BI Consumption

## 2. Source Boundary
The source boundary represents externally acquired operational data and its documented provenance.

Source data must remain distinguishable from transformed analytical data and must retain sufficient lineage to support traceability.

## 3. Landing / Raw Layer
The landing or raw layer preserves acquired source representations before analytical transformation.

Responsibilities include:
- Source preservation
- Ingestion traceability
- Replay support
- Acquisition metadata
- Basic structural validation

The raw layer must not become the primary business-facing analytical layer.

## 4. Staging Layer
The staging layer provides controlled structures for type normalization, naming normalization, structural validation, and source-oriented preparation.

Staging transformations must remain traceable to their source inputs.

Business metrics and final analytical definitions must not be embedded prematurely in staging structures.

## 5. Intermediate Layer
The intermediate layer contains reusable transformation structures that support analytical model construction.

Responsibilities include:
- Reusable joins
- Standardized business logic
- Intermediate calculations
- Transformation reuse
- Dependency isolation

Intermediate structures should avoid unnecessary duplication of business logic across downstream marts.

## 6. Fact Schema Responsibilities
Fact structures represent measurable business events at an explicitly defined grain.

Fact schemas must define:
- Business event
- Grain
- Measures
- Foreign-key relationships
- Additivity behavior
- Required dimensional context

Fact design will be formally defined in the dimensional modeling areas.

## 7. Dimension Schema Responsibilities
Dimension structures provide descriptive business context for analytical facts.

Dimensions must have documented business meaning, key strategy, attribute ownership, and historical behavior where applicable.

Surrogate-key and slowly-changing-dimension decisions will be established in later modeling areas.

## 8. Data Mart Layer
Data marts provide subject-oriented analytical structures designed around defined business consumption needs.

Each mart must have:
- Explicit business purpose
- Defined grain
- Documented source dependencies
- Governed metrics
- Known consumers
- Data quality expectations

Data marts must not silently redefine enterprise business metrics.

## 9. Metrics and Semantic Layer
The metrics and semantic layer provides governed business definitions and reusable analytical measures.

Metrics must be traceable to approved analytical structures and documented business definitions.

Metric definitions must remain consistent across BI products and analytical consumers.

## 10. BI Consumption Boundary
BI consumption structures expose governed analytical data products to reporting, dashboards, exploration, and other approved analytical consumers.

BI consumers should not depend directly on uncontrolled raw or staging structures for production reporting.

## 11. Schema Ownership
Every persistent logical schema or layer must have an accountable engineering or data ownership boundary.

Ownership includes purpose, change responsibility, validation responsibility, access responsibility, and documentation responsibility.

## 12. Schema Change Control
Schema changes must be version-controlled, documented, validated, and traceable.

Breaking changes require impact analysis and controlled downstream migration.

## 13. Cross-Layer Dependency Rules
Dependencies should flow toward progressively governed analytical structures.

Downstream business-facing layers must not create uncontrolled dependencies on temporary processing structures.

Cross-layer dependencies must be documented where they materially affect reliability, testing, or lineage.

## 14. Security and Access Responsibilities
Access must be aligned with layer purpose and least-privilege principles.

Source-preservation and technical-processing structures may require different access boundaries from business-facing analytical structures.

## 15. Performance Responsibilities
Each logical layer must have performance responsibilities appropriate to its workload.

Performance optimization must be based on measured workload characteristics and must not compromise correctness, lineage, or maintainability.

## 16. Lifecycle Responsibilities
Every logical layer must have documented retention, refresh, archival, and cleanup expectations where applicable.

Lifecycle decisions must preserve required analytical history and regulatory or governance obligations.

## 17. Technology-Neutral Boundary
This artifact defines logical storage and schema responsibilities only. It does not select a specific database, warehouse, cloud storage service, schema-management platform, or BI technology.

Technology implementation remains subject to the evidence-based technology evaluation established in Area 12.

## 18. Acceptance Boundary
The artifact is complete when every logical layer has an explicit responsibility, ownership boundary, dependency rule, access boundary, performance responsibility, lifecycle expectation, and technology-neutral definition.

## 19. Next Step
After 15.2 validation and acceptance, proceed to Area 15.3 — Storage Technology, Schema & Implementation Responsibilities.

