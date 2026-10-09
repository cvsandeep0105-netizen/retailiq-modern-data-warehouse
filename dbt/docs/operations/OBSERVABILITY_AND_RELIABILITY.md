# RetailIQ — Observability & Reliability Engineering

## 1. Purpose

RetailIQ treats pipeline reliability and data observability as first-class engineering concerns.

The platform provides validation at multiple stages:

RAW ? STAGING ? INTERMEDIATE ? WAREHOUSE ? MARTS ? SEMANTIC

Each downstream layer depends on validated upstream data.

## 2. Pipeline Health Signals

Primary health signals include:

- dbt parse success
- dbt model execution status
- dbt test status
- snapshot execution status
- incremental model execution
- row-count reconciliation
- uniqueness validation
- null validation
- referential-integrity validation
- business-rule validation
- semantic KPI validation
- dbt manifest generation
- dbt catalog generation

## 3. Current Validated Evidence

The latest complete local dbt build completed successfully:

- 36 models
- 1 snapshot
- 132 data tests
- 9 sources
- 477 macros
- 169 executable nodes
- 169/169 PASS
- 0 WARN
- 0 ERROR
- 0 SKIP
- Total execution time: approximately 4 minutes 36 seconds

The build included 30 views, 5 table models, 1 incremental model, 1 snapshot, and 132 data tests.

### Incremental-model defect recovery

The daily order metrics model previously accumulated duplicate date keys under its original append-based implementation. The model was changed to use dbt's native `delete+insert` incremental strategy with `date_sk` as its unique key.

Validated evidence after the change:

- Full-refresh result: 634 rows
- Distinct date keys after repeated incremental executions: 634
- Duplicate date-key count: 0
- Incremental-model tests: 9/9 PASS
- Daily-sales mart tests: 3/3 PASS
- Complete dbt build: 169/169 PASS

Repeated incremental runs reported `INSERT 0 2`. The resulting table retained 634 rows and 634 distinct date keys. The complete build subsequently executed the incremental model and passed its unique-date test.

This validates row-count stability and key uniqueness. A complete metric-by-metric comparison against a full-refresh result has not yet been documented as a separate test.

### Cross-layer reconciliation

Previously validated reconciliation evidence:

- Fact orders: 99,441 rows
- Customer 360: 99,441 rows
- Fact order items: 112,650 rows
- Product performance: 112,650 rows
- Seller performance: 112,650 rows
- Fact reviews: 99,224 rows
- Review performance: 99,224 rows

The daily incremental model and daily-sales mart each contain 634 date-level rows. Their aggregated `total_orders` measure is 99,441. These are different measurements and must not be represented as identical row counts.
## 4. Data Quality Monitoring

The project validates:

### Structural quality

- Not-null constraints
- Unique business keys
- Unique surrogate keys
- Valid dimensional keys
- Required source attributes

### Referential quality

Foreign-key relationships are tested between:

- Facts and customers
- Facts and products
- Facts and sellers
- Facts and dates

### Business quality

Business-rule tests verify:

- Delivered orders do not exceed total orders
- Late orders do not exceed delivered orders
- On-time orders do not exceed delivered orders
- Delivery rates remain between 0 and 100
- On-time and late rates remain between 0 and 100

## 5. Incremental Reliability

The daily order metrics model uses:

- Incremental materialization
- `date_sk` as the unique key
- dbt's native `delete+insert` strategy
- A seven-calendar-day lookback
- Actual calendar-date comparisons rather than integer date-key arithmetic

The model reprocesses the configured date window and replaces matching date-key records rather than relying on append-only insertion.

### Validated recovery evidence

After replacing the previous append-based implementation:

1. A full refresh produced 634 rows.
2. Two consecutive incremental executions each reported `INSERT 0 2`.
3. A database query confirmed 634 total rows, 634 distinct `date_sk` keys, and zero duplicate rows.
4. All 9 incremental-model tests passed.
5. All 3 daily-sales mart tests passed.
6. The subsequent complete dbt build passed all 169 executable nodes.

This confirms the observed duplicate-key defect is resolved for the tested dataset and execution sequence.

The seven-day lookback supports reprocessing within that window. Changes older than the configured window require a separate backfill or full-refresh procedure. Metric-level equivalence between incremental and full-refresh results remains a distinct validation task.
## 6. SCD Type 2 Reliability

Customer history is maintained through a dbt snapshot.

The snapshot:

- Uses `customer_id` as the business key
- Uses check-based change detection
- Tracks customer attribute changes
- Preserves historical versions
- Remains stable when source data is unchanged

Repeated execution against unchanged source data produced no additional snapshot records.

## 7. Failure Handling

If a dbt model fails:

1. Stop downstream consumption.
2. Identify the failed model.
3. Inspect the dbt error output.
4. Check upstream dependencies.
5. Run the affected model independently.
6. Run the model's associated tests.
7. Perform reconciliation.
8. Resume the downstream build only after validation passes.

## 8. Recovery Strategy

For a failed incremental transformation:

1. Validate the source data.
2. Inspect the incremental lookback window.
3. Re-run the affected incremental model.
4. Execute associated tests.
5. Reconcile the resulting metrics against upstream facts.
6. Resume downstream marts and semantic models.

For a snapshot issue:

1. Inspect source changes.
2. Validate the snapshot configuration.
3. Check historical/current records.
4. Re-run the snapshot.
5. Validate row counts and current-record status.

## 9. Observability Artifacts

dbt generates:

- `manifest.json`
- `catalog.json`
- `run_results.json`

These artifacts provide metadata about:

- Model dependencies
- Test execution
- Execution status
- Model timing
- Database relations
- Column metadata

## 10. Monitoring Architecture for Production

The current project is validated locally.

A production implementation can connect dbt execution to:

- CI/CD pipelines
- Cloud scheduler/orchestrator
- Centralized logs
- Metrics platform
- Alerting system
- Incident-management workflow

Example flow:

Scheduler
? dbt execution
? test results
? metrics/logs
? alerting
? engineering response

## 11. Alert Conditions

Recommended production alerts include:

### Critical

- dbt build failure
- data-quality test failure
- referential-integrity failure
- unexpected row-count drop
- snapshot failure
- incremental model failure

### Warning

- abnormal model runtime
- unusual row-count growth
- freshness degradation
- increasing rejected records
- unexpected metric movement

## 12. Reliability Principles

RetailIQ follows:

1. Validate before downstream consumption
2. Fail fast on critical data-quality errors
3. Preserve deterministic transformations
4. Support controlled reprocessing
5. Reconcile important analytical outputs
6. Maintain lineage
7. Separate development and production environments
8. Keep recovery procedures documented
9. Avoid silent data loss
10. Make operational evidence reproducible

## 13. Production Boundary

The current implementation demonstrates the engineering patterns locally using PostgreSQL and dbt Core.

Cloud monitoring, production alerting and managed orchestration are architectural targets unless separately implemented and validated.

No production monitoring capability is claimed without implementation evidence.
