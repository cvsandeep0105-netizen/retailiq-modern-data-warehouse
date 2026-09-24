# RetailIQ — Environment Access, Permissions & Operational Ownership Boundaries

Document Status: Accepted & Frozen

## Purpose

Define the access, permission, ownership, and operational responsibility boundaries for Development, Test/Validation, and Production environments.

## Access Principles

- Access must follow least privilege.
- Environment access must be separated by purpose.
- Production access must be more restricted than Development access.
- Human and service identities must be distinguishable.
- Access must be auditable and attributable.
- Permissions must not be embedded directly in application code.

## Development Access Boundary

Development is the primary engineering workspace for implementation, debugging, local validation, and controlled experimentation.

Expected access:
- Developers: read/write development resources required for implementation.
- Data Engineering: read/write development data and transformation artifacts.
- BI Development: read development analytical outputs.
- Platform/Operations: administrative access when required for environment maintenance.

Development access must not provide unrestricted Production permissions.

## Test / Validation Access Boundary

The Test/Validation environment is used for controlled validation of schemas, transformations, data quality, analytical outputs, and release candidates.

Expected access:
- Data Engineering: controlled read/write access for validation workloads.
- QA/Data Quality: read access to validation outputs and controlled execution of validation checks.
- BI/Analytics: read access to validation datasets and reports.
- Platform/Operations: environment administration.

Test data and permissions must remain isolated from Production resources.

## Production Access Boundary

Production contains operational analytical data products consumed by approved business and BI workloads.

Expected access:
- Runtime service identities: only the permissions required to execute approved workloads.
- Data Engineering: controlled operational access based on assigned responsibility.
- BI/Analytics: read-only access to approved analytical products.
- Platform/Operations: controlled administrative access.
- Direct manual modification of production analytical data is prohibited unless explicitly authorized through an operational change process.

## Identity Boundary

Human identities and service identities must use separate authentication and authorization mechanisms where supported.

Service identities must not rely on individual developer credentials for production execution.

## Permission Model

Permissions must be assigned according to role, environment, resource, and required operation.

Representative permission categories:
- Read
- Write
- Execute
- Administer
- Deploy
- Monitor

Permissions must be reviewed when responsibilities, environments, or system components change.

## Operational Ownership

Data Engineering owns data models, transformation logic, data quality rules, and analytical data products within the approved project boundary.

Platform/Operations owns environment availability, runtime infrastructure, deployment mechanisms, and operational controls within the approved project boundary.

BI/Analytics owns consumption-layer requirements, analytical interpretation, and approved BI/reporting usage.

Security/Governance owns applicable access-control, governance, and compliance requirements.

Business stakeholders own business definitions and approval of business-facing analytical requirements.

## Deployment Boundary

Production deployment must occur through a controlled release mechanism.

Development users must not bypass the approved deployment path to modify Production resources directly.

## Auditability

Environment access, privileged operations, deployments, and material configuration changes should produce auditable records where supported by the selected technology.

## Access Review

Access should be reviewed periodically and whenever a user changes role, responsibility, or environment assignment.

## Evidence Source

Evidence sources are the Area 08 environment architecture artifacts and the project's approved engineering requirements.

## Acceptance Boundary

This artifact is accepted only when access boundaries, permission principles, identity separation, operational ownership, deployment restrictions, and auditability requirements are explicitly documented.

## Next Step

After acceptance, Area 08.5 will define environment-level access and ownership evidence requirements.

## Artifact Completion Criteria

- Environment access boundaries documented
- Permission principles documented
- Identity boundaries documented
- Operational ownership documented
- Deployment restrictions documented
- Auditability requirements documented
- Acceptance boundary documented

