# Project 03 — Microsoft Fabric + dbt + Architecture Extension

## Document Status

- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Extension: Microsoft Fabric + dbt + System Design / Architecture
- Base Project Status: FINAL / FROZEN
- Extension Branch: `feature/fabric-dbt-architecture-extension`
- Extension Status: DESIGN PHASE
- Original Project 03 implementation: MUST NOT be modified destructively
- Purpose: Extend the existing RetailIQ platform with validated modern data-platform capabilities without weakening the original implementation.

---

# 1. Extension Objective

The purpose of this controlled extension is to demonstrate how the existing RetailIQ modern data warehouse and analytics engineering platform can be extended toward a Microsoft Fabric-oriented architecture while introducing dbt-based analytics engineering practices and strengthening system-design and data-architecture capabilities.

The extension must remain materially connected to the existing RetailIQ platform.

The extension is not intended to replace the original architecture.

The extension is intended to demonstrate:

1. Microsoft Fabric architecture understanding.
2. OneLake and Fabric Lakehouse concepts.
3. Fabric data ingestion and orchestration concepts.
4. Fabric Spark / PySpark data engineering.
5. Fabric Warehouse analytical serving.
6. Semantic and BI-oriented architecture.
7. dbt-based analytics engineering.
8. Modern ELT architecture.
9. Data modeling and transformation discipline.
10. System design and architecture decision-making.
11. Data quality and validation.
12. Production-oriented engineering practices.
13. Clear separation between implemented capabilities and architectural capabilities.

---

# 2. Architectural Boundary

The original RetailIQ implementation is considered the baseline system.

The extension must preserve the existing:

- RAW layer
- STAGING layer
- dimensional models
- fact tables
- dimension tables
- SCD implementation
- incremental models
- data marts
- business metrics
- data-quality framework
- integration testing
- database validation
- dashboard
- documentation
- CI/CD practices

The extension must not introduce destructive changes to the original implementation.

The extension must be developed independently on:

`feature/fabric-dbt-architecture-extension`

The original `main` branch remains the stable baseline.

---

# 3. Existing RetailIQ Logical Architecture

The existing platform follows a modern warehouse and analytics-engineering pattern:

```text
Source Data
    |
    v
RAW / Landing
    |
    v
STAGING
    |
    v
Source-to-Staging Transformations
    |
    v
Intermediate / Transformation Layer
    |
    v
Dimensional Model
    |
    +------------------+
    |                  |
    v                  v
Dimensions           Facts
    |                  |
    +--------+---------+
             |
             v
        Data Marts
             |
             v
    Business Metrics /
     Semantic Layer
             |
             v
       BI / Dashboard