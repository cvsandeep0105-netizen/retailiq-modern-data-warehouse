# RetailIQ — Scalability & Cost Engineering

## 1. Purpose

RetailIQ is designed so that analytical workloads can scale without requiring a complete redesign of the logical data architecture.

The current implementation uses PostgreSQL and dbt Core locally.

The scalability design separates:

- ingestion
- transformation
- storage
- analytical serving
- semantic consumption

This allows the logical model to migrate to managed cloud infrastructure when required.

## 2. Current Workload

The validated RetailIQ dataset contains:

- 99,441 orders
- 112,650 order items
- 103,886 payments
- 99,224 reviews
- 32,951 products
- 3,095 sellers
- 1,000,163 geolocation records
- 99,441 customers

The current workload is small enough for local PostgreSQL while still providing realistic dimensional and analytical engineering characteristics.

## 3. Scaling Principles

RetailIQ follows these principles:

1. Process incrementally where possible.
2. Avoid unnecessary full-table transformations.
3. Separate reusable transformation layers.
4. Materialize business-facing marts.
5. Keep semantic logic lightweight.
6. Push filtering and aggregation toward the data engine.
7. Use deterministic keys and explicit grains.
8. Optimize high-frequency access paths.
9. Separate storage and compute in cloud architectures.
10. Monitor workload growth before scaling infrastructure.

## 4. Incremental Processing

The daily order metrics model uses incremental processing.

Configuration:

- Incremental materialization
- `date_sk` unique key
- Delete-and-insert strategy
- Seven-calendar-day lookback

The lookback allows controlled reprocessing for late-arriving or corrected records without rebuilding the complete historical dataset.

This reduces unnecessary compute as the dataset grows.

## 5. Data Volume Growth

For larger workloads, scaling should occur by layer.

### Staging

Use partition-aware ingestion and incremental extraction where supported.

### Intermediate

Reuse standardized models and avoid repeated source scans.

### Warehouse

Partition large fact tables by business date where supported.

Potential partition candidates:

- order purchase date
- payment date
- review creation date

### Marts

Keep business-facing marts focused on analytical access patterns.

Frequently consumed aggregates should be materialized rather than recomputed repeatedly.

### Semantic Layer

Keep semantic models lightweight and derived from governed marts.

## 6. Cloud Storage Strategy

For a cloud-scale implementation, storage and compute should be separated where supported.

A target architecture can use object storage for durable analytical data and a managed SQL/warehouse engine for serving.

Examples include:

- Amazon S3
- Azure Data Lake Storage / OneLake
- Google Cloud Storage

The exact service depends on deployment requirements.

## 7. Compute Scaling

As workload increases, compute can scale independently from storage.

Potential strategies:

- Increase warehouse compute for heavy transformation windows.
- Use distributed Spark processing for large transformations.
- Schedule expensive transformations during controlled execution windows.
- Separate transformation workloads from BI-serving workloads.
- Use workload-specific compute where the platform supports it.

## 8. Concurrency

BI and analytical workloads can create different access patterns.

The architecture should separate:

- transformation workloads
- interactive analytical queries
- scheduled reporting
- ad-hoc exploration

Where supported, workload isolation prevents heavy transformations from degrading BI query performance.

## 9. Query Optimization

The current implementation includes targeted indexes on high-value mart access paths:

- `mart_customer_360.customer_id`
- `mart_customer_360.customer_state`
- `mart_product_performance.product_id`
- `mart_product_performance.product_category_name`
- `mart_seller_performance.seller_id`
- `mart_daily_sales.date_sk`

The indexes support common filtering and lookup patterns without changing analytical business logic.

## 10. Materialization Strategy

RetailIQ uses different materialization strategies according to workload:

### Views

Used where lightweight derived logic is appropriate.

### Tables

Used for business-facing marts where repeated analytical access benefits from persisted results.

### Incremental

Used where repeated full-history recomputation would be unnecessary.

### Snapshot

Used where historical dimension changes must be preserved.

This prevents using one materialization strategy for every workload.

## 11. Cost Engineering

Cost controls should focus on avoiding unnecessary compute.

Recommended controls:

- Incremental processing
- Partition pruning
- Predicate pushdown
- Reusable intermediate models
- Appropriate materialization
- Scheduled transformation windows
- Workload isolation
- Query monitoring
- Retention policies
- Storage lifecycle policies

## 12. Development Cost Control

The current project intentionally uses local PostgreSQL and dbt Core for development.

This avoids unnecessary cloud consumption while allowing the engineering patterns to be validated locally.

Cloud infrastructure should be introduced when the workload or deployment requirement justifies it.

## 13. Production Cost Controls

A production deployment should monitor:

- compute utilization
- storage growth
- query execution time
- scan volume
- failed/retried jobs
- concurrency
- idle resources
- data retention
- pipeline frequency

Cost anomalies should be treated as operational signals.

## 14. Performance vs Cost Trade-offs

RetailIQ recognizes that maximum performance is not always the lowest-cost architecture.

Examples:

- Persisting every transformation increases storage usage.
- Recomputing everything increases compute usage.
- Excessive indexing increases write and storage overhead.
- Excessive concurrency can increase infrastructure cost.
- Over-partitioning can increase metadata and planning overhead.

Architecture decisions should therefore balance:

Performance
+
Reliability
+
Maintainability
+
Cost

## 15. Scalability Target Architecture

A cloud-scale implementation can follow:

Source Systems
? Ingestion
? Object Storage / Lakehouse
? Distributed Transformation
? Governed Warehouse
? Data Marts
? Semantic Layer
? BI / Analytics

The logical model remains consistent while infrastructure scales underneath it.

## 16. Current Implementation Boundary

The current project demonstrates scalability principles using:

- PostgreSQL
- dbt Core
- incremental processing
- dimensional modeling
- persisted marts
- targeted indexing
- reconciliation
- data-quality testing

The project does not claim production-scale cloud capacity.

Cloud services and distributed compute are architectural targets unless separately implemented and validated.

## 17. Interview Boundary

The defensible claim is:

"Designed and validated a scalable analytics-engineering architecture with incremental processing, dimensional modeling, persisted marts, targeted query optimization, reconciliation and documented cloud-scale migration patterns."

Production cloud cost savings or production throughput figures are not claimed without corresponding implementation evidence.
