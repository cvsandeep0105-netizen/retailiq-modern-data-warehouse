# Storage Schema Naming, Namespace & Physical Implementation Standards

## Document Status
- Status: Accepted & Frozen
- Area: 10.4

## Purpose
This document defines the naming, namespace, and physical implementation standards for RetailIQ storage schemas. The standard ensures that storage structures remain consistent, discoverable, maintainable, and aligned with the approved logical architecture.

## Naming Principles
- Names must be clear, deterministic, and business-readable.
- Naming must remain consistent across environments.
- Names must communicate the responsibility of the storage object.
- Ambiguous abbreviations must be avoided unless formally standardized.
- Naming conventions must support automated validation and discoverability.

## Namespace Architecture
- Raw / Landing objects belong to the raw namespace.
- Staging objects belong to the staging namespace.
- Intermediate / Core objects belong to the intermediate or core namespace.
- Dimensions belong to the dimension namespace.
- Facts belong to the fact namespace.
- Data marts belong to the mart namespace.
- Metrics and semantic objects belong to the metrics or semantic namespace.

## Schema Naming Standard
- Schema names must be lowercase unless the selected physical technology requires another convention.
- Schema names must use stable functional names rather than environment-specific names.
- Environment separation must be implemented through approved environment boundaries rather than inconsistent schema naming.
- Schema names must map clearly to their logical storage responsibility.

## Table Naming Standard
- Table names must be lowercase and descriptive.
- Table names must identify the business entity, event, or analytical product they represent.
- Fact tables must use a consistent fact naming convention.
- Dimension tables must use a consistent dimension naming convention.
- Data mart tables must communicate their business domain or analytical purpose.

## Column Naming Standard
- Column names must be lowercase and descriptive.
- Multi-word column names must use snake_case.
- Technical identifiers must use consistent suffix and prefix conventions.
- Date and timestamp columns must use explicit names that communicate their meaning.
- Measure names must communicate the business quantity represented.

## Key Naming Standard
- Natural keys must preserve source business identifiers where required.
- Surrogate keys must use a consistent naming convention.
- Foreign keys must clearly identify the referenced business entity.
- Composite keys must have explicitly documented component columns.

## Fact and Dimension Naming
- Dimension objects must use a consistent dim_<entity> convention where supported by the selected physical technology.
- Fact objects must use a consistent fact_<business_process> convention where supported by the selected physical technology.
- Naming must not imply a grain that differs from the documented model.

## Data Mart Naming
- Data mart schemas or namespaces must identify the business domain.
- Mart tables must represent governed analytical products rather than raw operational copies.
- Naming must support BI discovery and business-user interpretation.

## Metrics and Semantic Naming
- Metric names must be business-readable.
- KPI names must have one authoritative definition.
- Semantic objects must distinguish governed metrics from physical storage structures.
- Metric naming must remain stable across downstream BI consumption.

## Environment Naming Boundary
- Development, test, validation, and production environments must remain distinguishable through approved environment configuration.
- Environment identifiers must not create inconsistent business object names.
- Promotion between environments must preserve logical object identity.

## Physical Implementation Boundary
- Logical names must be mapped to physical objects through documented implementation rules.
- Physical technology limitations may require controlled naming adaptations.
- Any adaptation must preserve semantic meaning and traceability.
- Vendor-specific naming requirements must not override the logical ownership boundary without documented justification.

## Reserved Names and Ambiguity Control
- Reserved words of the selected physical technology must not be used as unqualified object names.
- Duplicate or near-duplicate names must be avoided.
- Names differing only by capitalization must not be treated as separate business concepts.
- Deprecated names must not be reused for different business meanings.

## Schema Evolution Naming
- Renaming a governed object requires impact assessment.
- Deprecated objects must have a documented migration or retirement path.
- Breaking name changes require explicit change control.
- Historical documentation must preserve traceability to previous names.

## Automated Naming Validation
- Schema names must be validated against the approved naming standard.
- Table names must be checked for naming consistency.
- Column names must be checked for naming consistency.
- Key naming must be checked against documented model rules.
- Naming validation results must be retained as engineering evidence.

## Security Boundary
- Object names must not expose secrets, credentials, tokens, or sensitive configuration values.
- Sensitive data classification must be documented separately from naming conventions.
- Access-control boundaries must be enforced independently of object naming.

## Evidence Source
- Evidence is derived from the accepted Area 10.1 storage architecture, Area 10.2 logical schema responsibilities, Area 10.3 technology boundary responsibilities, and Areas 08–09 environment and repository standards.

## Acceptance Boundary
- Naming standards cover schemas, tables, columns, keys, facts, dimensions, marts, and metrics.
- Namespace responsibilities are explicit.
- Environment and physical implementation boundaries are documented.
- Schema evolution and automated naming validation requirements are defined.

## Next Step
After validation and acceptance of this artifact, Area 10.5 will define storage security, retention, lifecycle, and operational ownership standards.

## Artifact Completion Criteria
- Namespace standards are documented.
- Schema, table, column, and key naming standards are documented.
- Fact, dimension, mart, and metric naming standards are documented.
- Environment and physical implementation boundaries are defined.
- Naming validation and schema evolution controls are documented.
- Security naming boundaries are documented.
- Validation evidence is recorded before acceptance.

