# Logical Warehouse Architecture & Analytical Schema Topology

## Document Status
- Status: Accepted & Frozen
- Area: 11.2

## Purpose
This document defines the logical warehouse topology for RetailIQ. It establishes how analytical schemas are separated, how data moves between warehouse layers, and how facts, dimensions, marts, metrics, and BI consumption are logically organized.

## Logical Warehouse Topology
- The warehouse follows a layered analytical architecture.
- Each layer has a defined responsibility and ownership boundary.
- Downstream layers consume governed outputs from upstream layers.
- Analytical consumers must not bypass governed warehouse layers.

## Staging Schema
- The staging schema contains source-aligned, technically standardized structures.
- Staging models retain traceability to the originating source.
- Staging is responsible for technical normalization and structural preparation.
- Staging is not the authoritative business-facing analytical layer.

## Intermediate / Core Schema
- The intermediate or core schema contains reusable business transformations.
- Core models provide stable inputs for dimensions, facts, and analytical products.
- Shared transformation logic should be centralized here rather than duplicated across marts.
- Core models must have documented grain and dependency relationships.

## Dimension Schema
- The dimension schema contains descriptive business entities.
- Dimensions provide reusable descriptive context for analytical facts.
- Dimension models must define natural keys and surrogate-key behavior where applicable.
- Historical behavior must follow the approved dimensional modeling strategy.

## Fact Schema
- The fact schema contains measurable business events.
- Each fact must have an explicitly documented grain.
- Measures must be valid at the declared grain.
- Fact relationships to dimensions must follow approved key and cardinality rules.

## Data Mart Schema
- The data mart schema contains business-oriented analytical products.
- Marts may combine facts, dimensions, and governed transformations for specific analytical domains.
- Mart models must remain traceable to authoritative warehouse models.
- Marts must not silently redefine governed business logic.

## Metrics / Semantic Schema
- The metrics or semantic layer contains governed business metrics and KPI definitions.
- Metric definitions must remain independent of individual BI reports where possible.
- Semantic structures provide a stable business interpretation of warehouse data.
- Changes to governed metrics require controlled change management.

## BI Consumption Boundary
- BI tools consume approved marts, semantic structures, or BI-ready data products.
- Direct reporting against raw or uncontrolled staging structures is outside the governed BI boundary.
- BI models must preserve the meaning of governed metrics.
- BI access must follow approved security and ownership controls.

## Logical Data Flow
SOURCE → RAW / LANDING → STAGING → INTERMEDIATE / CORE → DIMENSIONS + FACTS → DATA MARTS → METRICS / SEMANTIC → BI

## Dependency Direction
- Dependencies must flow from upstream data preparation toward downstream analytical consumption.
- Staging must not depend on final presentation models.
- Core transformations may depend on staging.
- Facts and dimensions may depend on approved core structures.
- Data marts may depend on facts, dimensions, and approved core models.
- Metrics and semantic structures may depend on governed analytical models.

## Schema Isolation
- Each schema must have a distinct analytical responsibility.
- Objects must not be placed in a schema merely for convenience.
- Cross-schema dependencies must be explicit and traceable.
- Schema boundaries must support testing, ownership, access control, and lifecycle management.

## Grain Boundary
- Every core, dimension, fact, and mart model must have an explicit grain.
- Grain must remain stable within a governed model.
- A transformation that changes grain must be explicitly documented.
- Aggregated models must not be mistaken for detailed fact models.

## Key Boundary
- Natural keys identify source or business entities where applicable.
- Surrogate keys support controlled dimensional relationships where required.
- Foreign keys must reference the intended analytical entity.
- Key transformations must remain traceable to upstream identifiers.

## Business Logic Boundary
- Reusable business rules belong in governed transformation models.
- Metric definitions belong in the metrics or semantic layer.
- BI presentation logic must not become the authoritative source of enterprise business definitions.
- Duplicate business calculations across marts must be minimized.

## Analytical Join Boundary
- Fact-to-dimension joins must follow documented relationships.
- Many-to-many relationships require explicit bridge or controlled modeling strategies where applicable.
- Joins must preserve intended fact grain.
- Analytical queries must avoid accidental row multiplication.

## Historical Data Boundary
- Historical facts must preserve required business events.
- Historical dimensions must follow the approved slowly changing dimension strategy.
- Late-arriving data must be handled according to the approved warehouse processing strategy.
- Historical corrections must remain auditable.

## Schema Evolution Boundary
- Schema changes require impact assessment.
- Breaking changes require controlled migration.
- Deprecated objects must have a documented retirement path.
- Downstream dependencies must be identified before structural changes are released.

## Security Boundary
- Access must be granted according to schema responsibility and user role.
- Engineering access and BI consumption access must remain appropriately separated.
- Sensitive data access must follow approved classification and authorization rules.
- Schema naming must not be treated as a substitute for access control.

## Performance Boundary
- Logical schema topology must support analytical query patterns.
- Physical optimization remains subject to technology selection and observed workload.
- Performance improvements must preserve analytical correctness.
- Aggregate or specialized models must remain traceable to authoritative sources.

## Technology-Neutral Boundary
- This logical topology does not prescribe a final physical warehouse technology.
- Physical schemas, databases, datasets, catalogs, or equivalent constructs will be mapped during technology evaluation.
- Technology-specific limitations must be documented before they affect the logical model.

## Evidence Source
- Evidence is derived from the accepted Area 10 storage architecture and Area 11.1 warehouse architecture foundation, together with the accepted business, source, contract, environment, and repository standards.

## Acceptance Boundary
- Logical warehouse schemas are explicitly defined.
- Analytical topology and data flow are documented.
- Dependency, grain, key, business logic, historical, security, and performance boundaries are defined.
- BI consumption is separated from uncontrolled source and staging access.
- Architecture remains technology-neutral pending formal technology evaluation.

## Next Step
After validation and acceptance of this artifact, Area 11.3 will define warehouse workload patterns, analytical access paths, and consumption architecture.

## Artifact Completion Criteria
- Logical schema topology is documented.
- Responsibilities for staging, core, dimensions, facts, marts, and semantic structures are defined.
- Dependency direction is explicit.
- Grain, key, join, historical, and schema evolution boundaries are documented.
- BI, security, and performance boundaries are documented.
- Technology-neutral architecture is preserved.
- Validation evidence is recorded before acceptance.

