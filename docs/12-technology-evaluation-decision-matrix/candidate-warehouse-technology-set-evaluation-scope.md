# Candidate Warehouse Technology Set & Evaluation Scope

## Document Status
- Status: Accepted & Frozen
- Area: 12.2

## Purpose
This document defines the candidate warehouse technology set and the evaluation scope for RetailIQ. Candidates are included for structured comparison against the approved evaluation framework. This document does not select a final technology.

## Candidate Selection Principles
- Candidates must support the core analytical warehouse requirements.
- Candidates must be relevant to dimensional modeling and ELT workloads.
- Candidates must have sufficient technical documentation for evidence-based evaluation.
- Candidates must be capable of supporting BI-oriented analytical workloads.
- Candidate inclusion does not imply preference or final selection.

## Candidate Technology Set
The initial candidate set is:
- PostgreSQL
- Microsoft SQL Server
- Snowflake
- Google BigQuery
- Amazon Redshift
- Databricks SQL Warehouse

## PostgreSQL Evaluation Scope
Evaluate PostgreSQL for relational warehouse modeling, SQL analytics, dimensional structures, ELT integration, local development, testing, performance, scalability, operational complexity, and BI connectivity.

## Microsoft SQL Server Evaluation Scope
Evaluate Microsoft SQL Server for enterprise relational warehousing, dimensional modeling, analytical SQL, ELT integration, workload management, security, governance, BI connectivity, operational management, and scalability.

## Snowflake Evaluation Scope
Evaluate Snowflake for cloud data warehousing, analytical SQL, dimensional modeling, workload isolation, scalability, ELT processing, governance, security, BI connectivity, operational management, and consumption patterns.

## Google BigQuery Evaluation Scope
Evaluate Google BigQuery for cloud analytical warehousing, SQL analytics, dimensional modeling, ELT workloads, large-scale analytical processing, scalability, governance, security, BI connectivity, and cost behavior.

## Amazon Redshift Evaluation Scope
Evaluate Amazon Redshift for cloud data warehousing, dimensional modeling, analytical SQL, workload management, scalability, ELT processing, governance, security, BI integration, and operational requirements.

## Databricks SQL Warehouse Evaluation Scope
Evaluate Databricks SQL Warehouse for analytical SQL, warehouse-style serving, lakehouse integration, dimensional modeling, ELT processing, scalability, governance, security, BI connectivity, and interoperability with broader data engineering workloads.

## Common Evaluation Scope
Every candidate must be evaluated using the same core dimensions:
- Functional warehouse capability.
- Dimensional modeling.
- SQL and analytical processing.
- ELT and transformation integration.
- Incremental processing.
- Historical data handling.
- Analytical performance.
- Scalability.
- Concurrency and workload isolation.
- Reliability and recovery.
- Security and access control.
- Governance, metadata, and lineage.
- Data quality and testing integration.
- Engineering and CI/CD integration.
- BI connectivity.
- Cost and operational complexity.
- Maintainability.
- Portability.
- Reproducibility.

## RetailIQ Workload Scope
Candidate evaluation must consider the actual RetailIQ workload profile:
- Approximately 100,000 historical ecommerce orders.
- Order-level analytical processing.
- Order-item analytical processing.
- Customer analysis.
- Product and category analysis.
- Seller analysis.
- Payment analysis.
- Review analysis.
- Delivery and fulfillment analysis.
- Dimensional modeling.
- Business data marts.
- Governed metrics and KPIs.
- BI-oriented analytical queries.
- Full-refresh and incremental ELT patterns.

## Development Environment Scope
Candidates must be assessed for practical development and testing in the user's Windows and VS Code engineering environment where applicable.

## Production Environment Scope
Candidates must be evaluated for production-oriented analytical workloads, including security, reliability, observability, scalability, operational ownership, and controlled deployment.

## BI Consumption Scope
Candidates must be evaluated for serving governed analytical datasets to BI consumers and supporting consistent metric definitions.

## Evidence Requirements
Each candidate evaluation must identify:
- Official technical documentation.
- Verified platform capabilities.
- Project-level validation where performed.
- Benchmark or measured evidence where available.
- Known limitations.
- Assumptions requiring further validation.

## Excluded Technology Scope
- Operational transactional databases are not automatically treated as analytical warehouse candidates.
- Streaming-first technologies are not treated as warehouse candidates solely because they can store or query data.
- A technology will not be included merely because it is familiar to the development team.

## Evaluation Boundary
This candidate set is an evaluation scope, not a ranking or final recommendation. Final technology selection requires the completed evidence-based decision matrix and architectural review.

## Change Control
Adding or removing a candidate after evaluation begins requires documented justification so that evaluation consistency is preserved.

## Evidence Source
- Evidence is derived from accepted Area 12.1 evaluation criteria and the accepted Areas 01–11 business, source, storage, environment, repository, and warehouse architecture artifacts.

## Acceptance Boundary
- Candidate technologies are explicitly identified.
- Each candidate has a defined evaluation scope.
- Common evaluation criteria apply across candidates.
- RetailIQ workload characteristics are included.
- Evidence requirements are defined.
- No candidate is selected or ranked by this artifact.

## Next Step
After validation and acceptance of this artifact, Area 12.3 will define the detailed candidate-by-criterion evaluation matrix structure.

## Artifact Completion Criteria
- Candidate technology set is documented.
- Individual candidate evaluation scopes are documented.
- Common evaluation criteria are defined.
- RetailIQ workload scope is documented.
- Development, production, BI, evidence, and change-control boundaries are defined.
- No final technology selection is made.
- Validation evidence is recorded before acceptance.

