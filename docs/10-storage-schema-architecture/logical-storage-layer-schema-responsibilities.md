# RetailIQ — Logical Storage-Layer Architecture & Schema Responsibilities

Document Status: Accepted & Frozen

## Purpose

Define the logical storage layers, schema responsibilities, ownership boundaries, and permitted data movement for the RetailIQ analytical warehouse.

## Logical Architecture

The logical data flow is:

Source → Raw / Landing → Staging → Intermediate / Core → Facts & Dimensions → Data Marts → Metrics / Semantic → BI

Each layer represents a controlled transformation boundary and must have a distinct responsibility.

## Raw / Landing Schema

The Raw / Landing schema represents source-aligned data preserved for traceability, replay, and downstream validation.

Responsibilities:
- Preserve source-level attributes.
- Preserve source relationships required for downstream processing.
- Maintain traceability to source datasets.
- Prevent uncontrolled business transformations.

The Raw / Landing schema is not a business-facing analytical schema.

## Staging Schema

The Staging schema provides controlled structures for structural normalization and preparation.

Responsibilities:
- Standardize data types.
- Normalize source representations.
- Apply structural validation.
- Prepare data for reusable transformations.

Staging must not become an uncontrolled replacement for the governed analytical model.

## Intermediate / Core Schema

The Intermediate / Core schema contains reusable transformation logic and business-aligned structures used by downstream warehouse models.

Responsibilities:
- Centralize reusable business transformations.
- Resolve common transformation logic.
- Provide stable inputs to facts, dimensions, and analytical models.
- Reduce duplicated transformation logic.

## Dimension Schema

The Dimension schema contains governed descriptive entities used to provide analytical context.

Candidate dimensions include customer, product, seller, date, geography, and other approved business entities.

Final dimension structures, keys, history strategy, and attributes will be defined in the dimensional-modeling areas.

## Fact Schema

The Fact schema contains measurable business events at explicitly defined grains.

Candidate fact domains include orders, order items, payments, reviews, and other approved analytical events.

Final fact grains, measures, keys, and relationships will be defined in the dimensional-modeling areas.

## Data Mart Schema

The Data Mart schema provides business-oriented analytical structures derived from governed facts and dimensions.

Data marts must be organized around approved analytical domains and consumption requirements.

Data marts must not independently redefine core business logic without governance.

## Metrics / Semantic Schema

The Metrics / Semantic layer provides governed business metrics, KPI definitions, analytical relationships, and consumption-oriented structures.

Metrics must reference approved business definitions and governed analytical models.

## BI Consumption Boundary

BI tools consume approved data marts, metrics, or semantic structures.

BI dashboards must not directly modify warehouse data or establish uncontrolled business definitions.

## Schema Naming Responsibility

Schema names must clearly communicate the lifecycle layer and ownership purpose.

Naming must remain consistent across environments and must follow the repository naming standards.

## Data Movement Rules

Data should move downstream through controlled transformation boundaries.

Upstream source layers must not depend on downstream business-facing models.

Circular dependencies between storage layers are prohibited.

## Ownership Boundary

Data Engineering owns the technical schemas, transformation structures, facts, dimensions, and governed analytical data products.

Business stakeholders own approved business definitions.

BI and Analytics consume approved structures according to access controls.

## Schema Evolution Boundary

Changes to logical schemas must be evaluated for downstream impact.

Breaking changes require explicit migration or compatibility planning.

## Security Boundary

Schema access must follow the environment and permission boundaries defined in Area 08.

Raw, staging, core, warehouse, mart, and semantic schemas must not receive broader access than required for their intended use.

## Evidence Source

Evidence sources include Area 10.1, accepted Areas 01–09, source profiling, source relationships, data contracts, environment architecture, and approved RetailIQ analytical requirements.

## Acceptance Boundary

This artifact is accepted only when each logical storage layer has an explicit schema responsibility, ownership boundary, data movement rule, security boundary, and downstream consumption role.

## Next Step

After acceptance, Area 10.3 will define schema naming, namespace, and object-organization standards.

## Artifact Completion Criteria

- Logical architecture documented
- Raw / Landing schema documented
- Staging schema documented
- Intermediate / Core schema documented
- Dimension schema documented
- Fact schema documented
- Data Mart schema documented
- Metrics / Semantic schema documented
- BI consumption boundary documented
- Schema naming responsibility documented
- Data movement rules documented
- Ownership boundary documented
- Schema evolution boundary documented
- Security boundary documented
- Acceptance boundary documented

