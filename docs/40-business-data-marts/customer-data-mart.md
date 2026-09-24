# Area 40.3 — Customer Data Mart

Status: Accepted & Frozen

## 1. Purpose
Define the Customer business data mart as a governed analytical product for customer identity, customer attributes, customer order behavior, customer value, geography, lifecycle analysis, and approved customer-level analytical metrics.

## 2. Area 40.2 Dependency
The Customer mart shall remain compatible with the frozen Sales & Orders mart while avoiding uncontrolled duplication of order-level and item-level measures.

## 3. Area 40.1 Dependency
The Customer mart shall comply with the frozen Business Data Marts Foundation, including consumer, domain, grain, fact, dimension, measure, business-logic, quality, reconciliation, lineage, governance, BI-readiness, and performance boundaries.

## 4. Area 39 Dependency
The mart shall preserve the frozen Data Mart Architecture, including approved Customer domain boundaries, grain, fact and dimension composition, business-logic ownership, cross-domain controls, quality, reconciliation, and double-counting prevention.

## 5. Area 38 Dependency
The mart shall follow the approved transformation dependency graph, execution ordering, lineage, failure handling, reconciliation, and recovery controls.

## 6. Area 37 Dependency
The mart shall comply with approved analytics engineering model contracts, naming, documentation, testing, ownership, regression, and controlled-change standards.

## 7. Area 36 Dependency
Customer models shall consume governed Intermediate/Core transformations and shall not duplicate reusable enterprise transformation logic.

## 8. Area 35 Dependency
Incremental Customer processing shall preserve approved model identity, key resolution, merge, idempotency, reconciliation, and recovery controls.

## 9. Area 34 Dependency
Full-refresh and incremental processing shall follow approved watermark, replay, backfill, late-arrival, and processing-mode escalation controls.

## 10. Area 33 Dependency
Customer mart transformations shall remain within the approved ELT architecture.

## 11. Area 32 Dependency
Historical and late-arriving customer records shall preserve approved temporal semantics.

## 12. Area 31 Dependency
Customer historical attributes shall use approved SCD behavior where historical analysis requires versioned customer context.

## 13. Area 30 Dependency
Customer dimensions shall preserve conformed and role-playing dimension semantics where applicable.

## 14. Area 29 Dependency
Customer-related facts and measures shall retain approved grain and aggregation behavior.

## 15. Area 28 Dependency
Fact and dimension composition shall preserve approved architectural responsibilities.

## 16. Area 27 Dependency
Customer dimensions shall follow approved dimension architecture and attribute ownership.

## 17. Area 26 Dependency
Customer natural and surrogate key semantics shall remain consistent with approved key architecture.

## 18. Area 25 Dependency
Every Customer mart model shall declare an explicit business grain.

## 19. Area 24 Dependency
Customer analytical models shall follow the approved dimensional modeling strategy.

## 20. Area 23 Dependency
Customer outputs shall remain compatible with approved profiling baselines.

## 21. Area 22 Dependency
Customer population, key, measure, and business-total reconciliation shall be preserved.

## 22. Area 21 Dependency
Approved duplicate and record-resolution behavior shall remain preserved.

## 23. Area 20 Dependency
Customer models shall consume standardized and normalized analytical inputs.

## 24. Business Purpose
The Customer mart shall provide a governed analytical representation of customers and their approved customer-level relationships, characteristics, activity, purchasing behavior, and analytical value.

## 25. Primary Consumers
Primary consumers include customer analytics, marketing analysis, business analysts, customer-experience analysis, retention analysis, reporting workflows, semantic models, dashboards, and approved BI products.

## 26. Customer Business Grain
The core customer model shall use one row per customer_id unless a separate model explicitly declares another grain.

## 27. Customer Identity
customer_id shall remain the operational customer identifier for source relationship analysis. customer_unique_id shall be retained as an approved analytical identity attribute where appropriate and shall not be treated as interchangeable with customer_id without documented business rules.

## 28. Customer Attribute Boundary
Customer city, state, postal-prefix information, and other approved descriptive attributes shall remain descriptive customer attributes and shall not silently become transactional measures.

## 29. Customer Geography
Customer geography shall support customer-state, city, and postal-prefix analysis using approved source relationships and standardized geography logic.

## 30. Customer Order Relationship
Customer-to-order relationships shall be modeled through the approved customer key. Order-level measures shall be aggregated before being attached to customer grain.

## 31. Customer Purchase Metrics
Customer-level analytical metrics may include order count, item count, gross item value, freight value, payment value, average order value, purchase frequency, and other governed metrics where definitions are explicitly documented.

## 32. Measure Aggregation Boundary
Customer measures shall be calculated from compatible order, item, payment, or other source grains before aggregation to customer grain.

## 33. Payment Boundary
Multiple payments per order shall not inflate customer purchase metrics. Payment measures shall be aggregated at the appropriate order or payment grain before customer-level aggregation.

## 34. Order-Item Boundary
Multiple items per order shall not cause order counts to be multiplied. Item-level measures shall be intentionally aggregated before being associated with customer grain.

## 35. Review Boundary
Multiple reviews associated with an order shall not directly multiply customer metrics. Review metrics shall be separately aggregated at a compatible grain before customer-level use.

## 36. Customer Lifecycle
Customer lifecycle analysis shall preserve available order activity and temporal information without inventing customer states that are not supported by governed source data.

## 37. Customer Historical Context
Where customer attributes change over time and historical analysis requires the previous state, approved SCD controls shall preserve effective periods and historical versions.

## 38. Customer Value Boundary
Customer value calculations shall distinguish item value, freight value, payment value, order counts, and other measures rather than treating them as a single undifferentiated revenue concept.

## 39. Customer Segmentation Boundary
Segmentation attributes or derived customer groups shall be based on documented business rules and governed analytical measures. Segmentation shall not overwrite source customer attributes.

## 40. Data Quality
Quality controls shall validate customer keys, identity attributes, expected uniqueness, nullability, geography domains, relationship integrity, metric validity, and declared grain.

## 41. Reconciliation
Customer population shall reconcile to compatible upstream customer populations. Customer order counts and other measures shall reconcile at compatible grains and aggregation levels.

## 42. Exception Handling
Duplicate identities, unmatched relationships, invalid geography values, unexpected nulls, metric anomalies, and reconciliation differences shall be classified and handled through approved exception controls.

## 43. Lineage
Customer attributes and governed customer metrics shall retain traceability to upstream transformation models and source fields.

## 44. BI Consumption
The Customer mart shall provide stable customer-level analytical outputs for KPI definitions, semantic models, customer dashboards, retention analysis, segmentation, and BI-ready products.

## 45. Performance
Customer-level analytical access shall be supported through appropriate model grain, pre-aggregation, key design, and query patterns without compromising correctness.

## 46. Source Preservation
Customer mart processing shall never mutate, overwrite, or delete original source records.

## 47. Acceptance Criteria
Area 40.3 is accepted when customer grain, identity, attributes, geography, order relationships, customer metrics, aggregation boundaries, payment and item controls, review boundaries, lifecycle, historical context, customer value, segmentation, quality, reconciliation, exceptions, lineage, BI consumption, performance, and source-preservation controls are explicitly documented and validated.

