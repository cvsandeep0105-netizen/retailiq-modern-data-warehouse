# RetailIQ — Governance & Security Engineering

## 1. Purpose

RetailIQ separates ingestion, transformation, analytical modeling, semantic consumption, and operational controls into explicit layers.

The governance design is intended to support secure, traceable and maintainable analytical data engineering.

## 2. Environment Separation

Development uses:

- Local PostgreSQL
- dbt Core
- Docker
- Environment variables
- `dbt_dev` development schema

Production deployment is intentionally separated from the local development environment.

Production credentials must never be committed to source control.

## 3. Secret Management

Database credentials are supplied through environment variables.

The local `.env` file contains development credentials and is excluded from Git through `.gitignore`.

No passwords, API keys, tokens or connection secrets are stored in:

- SQL models
- dbt YAML files
- Git history
- documentation
- README files
- portfolio pages

Production environments should use a managed secret store such as:

- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager
- equivalent enterprise secret-management services

## 4. Data Layer Governance

### RAW

Purpose:
- Preserve source data
- Maintain source-level traceability
- Support replay and investigation

Controls:
- Source ownership
- Schema awareness
- Controlled write access

### STAGING

Purpose:
- Standardize source structures
- Normalize types
- Apply basic structural quality checks

Controls:
- Source tests
- Not-null validation
- Uniqueness checks where applicable

### INTERMEDIATE

Purpose:
- Create reusable transformation contracts
- Isolate business transformation logic

Controls:
- Explicit model dependencies
- Deterministic transformations
- Reconciliation against source structures

### WAREHOUSE

Purpose:
- Provide governed dimensional analytical structures

Controls:
- Surrogate keys
- Defined grain
- Referential integrity
- SCD Type 2 snapshot strategy
- Data-quality tests

### MARTS

Purpose:
- Provide business-oriented analytical products

Controls:
- Business grain
- Metric definitions
- Reconciliation to warehouse facts
- Controlled access patterns

### SEMANTIC

Purpose:
- Provide consistent analytical metrics and business concepts

Controls:
- Centralized KPI definitions
- Rate validation
- Metric consistency
- BI-ready views

## 5. Customer Data

Customer-related fields are treated as controlled analytical data.

The project avoids unnecessary exposure of personally identifying information.

Analytical models use customer identifiers required for joins and business analysis while avoiding unnecessary publication of sensitive source attributes.

## 6. Access Control

The target production architecture follows least privilege.

Recommended role separation:

- Ingestion role — source/raw write access
- Transformation role — staging/intermediate/warehouse write access
- Analytics role — mart/semantic read access
- BI role — semantic and approved mart read access
- Platform administrator — infrastructure and security administration

Users should receive only the permissions required for their responsibilities.

## 7. Auditability

RetailIQ maintains traceability through:

- `record_source`
- `created_at`
- dbt model dependencies
- dbt test results
- dbt manifest/catalog artifacts
- deterministic surrogate-key generation
- snapshot history for SCD Type 2

## 8. Data Quality as a Governance Control

Data quality is treated as an operational control rather than only a development feature.

The current implementation contains:

- 132 dbt data tests
- structural validation
- uniqueness validation
- not-null validation
- relationship validation
- business-rule tests
- cross-layer reconciliation

The final full dbt build achieved:

- 169/169 PASS
- 0 WARN
- 0 ERROR

## 9. Development / Production Boundary

The current implementation is a local engineering and portfolio environment.

The architecture does not claim production cloud deployment.

For production deployment, the same governance principles would be implemented using cloud-native identity, networking, encryption, secret management, logging and policy controls.

## 10. Security Principles

RetailIQ follows:

1. Least privilege
2. Secret isolation
3. Environment separation
4. Data minimization
5. Explicit ownership
6. Traceability
7. Validation before downstream consumption
8. No credentials in source control
9. Controlled analytical access
10. Reproducible transformations

## 11. Interview Boundary

The project demonstrates hands-on governance and security engineering at the local PostgreSQL/dbt implementation level.

Cloud security services are architectural targets unless separately implemented and validated.

No production-security capability is claimed without implementation evidence.
