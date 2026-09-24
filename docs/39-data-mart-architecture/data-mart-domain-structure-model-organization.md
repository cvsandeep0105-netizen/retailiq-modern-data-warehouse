# Area 39.2 — Data Mart Domain Structure & Model Organization

Status: Accepted & Frozen

## 1. Purpose
Define how RetailIQ data marts are organized by business domain, analytical purpose, model responsibility, grain, reusable inputs, and downstream consumption.

## 2. Area 39.1 Dependency
This artifact extends the frozen Data Mart Architecture Foundation and preserves its business-domain, consumer, grain, source-dependency, fact/dimension, reuse, performance, governance, and BI-consumption boundaries.

## 3. Area 38 Dependency
Data mart organization shall preserve the approved Transformation Dependency Graph, including dependency direction, execution ordering, lineage, quality, reconciliation, and failure controls.

## 4. Area 37 Dependency
Data mart models shall comply with Analytics Engineering naming, contracts, documentation, testing, quality, ownership, lineage, CI/CD, and change-control standards.

## 5. Area 36 Dependency
Data mart inputs shall come from approved Intermediate/Core transformations and shall not duplicate governed reusable business logic unnecessarily.

## 6. Area 35 Dependency
Incremental mart models shall preserve approved model identity, merge, change detection, idempotency, reconciliation, and recovery controls.

## 7. Area 34 Dependency
Mart refresh behavior shall comply with approved full-refresh, incremental, watermark, replay, backfill, and escalation strategies.

## 8. Area 33 Dependency
Mart organization shall remain within the approved ELT architecture and downstream transformation boundaries.

## 9. Area 32 Dependency
Historical and late-arriving data behavior shall remain consistent with approved temporal and correction rules.

## 10. Area 31 Dependency
SCD dimension dependencies shall preserve historical context and effective-date semantics where required.

## 11. Area 30 Dependency
Conformed and role-playing dimensions shall remain consistently usable across applicable marts.

## 12. Area 29 Dependency
Fact measures shall retain approved grain, additive behavior, and aggregation semantics when consumed by marts.

## 13. Area 28 Dependency
Fact and dimension responsibilities shall remain consistent with the approved architecture.

## 14. Area 27 Dependency
Dimension attributes and relationships shall follow approved dimension ownership.

## 15. Area 26 Dependency
Natural-key and surrogate-key behavior shall remain consistent across mart relationships.

## 16. Area 25 Dependency
Each mart model shall explicitly declare its business grain and protect against unintended grain changes.

## 17. Area 24 Dependency
Mart organization shall implement the approved dimensional modeling strategy.

## 18. Area 23 Dependency
Mart structures shall support profiling and baseline validation.

## 19. Area 22 Dependency
Mart outputs shall support upstream-to-downstream reconciliation.

## 20. Area 21 Dependency
Approved duplicate and record-resolution behavior shall remain preserved in mart inputs.

## 21. Area 20 Dependency
Mart inputs shall retain approved standardization and normalization semantics.

## 22. Business Domain Structure
RetailIQ marts shall be organized around stable analytical domains rather than raw source-table ownership. Domain boundaries shall reflect business questions and consumer needs.

## 23. Sales and Orders Domain
The sales and orders domain may organize order-level and order-item analytical outputs, including order activity, sales value, item volume, order status, and related dimensions. Each model shall declare its specific grain.

## 24. Customer Domain
Customer-oriented marts shall organize customer behavior, order activity, customer value, geography, and related analytical attributes without redefining authoritative customer identity.

## 25. Product Domain
Product-oriented marts shall organize product performance, category analysis, pricing, item volume, and product attributes while preserving approved product keys and dimensional semantics.

## 26. Seller and Fulfillment Domain
Seller and fulfillment marts shall support seller performance, shipping, delivery, logistics, and fulfillment analysis while preserving approved order-item and order relationships.

## 27. Payment Domain
Payment-oriented marts shall support payment-method, payment-value, installment, and transaction analysis while preserving payment grain and avoiding double counting across multi-payment orders.

## 28. Customer Experience Domain
Customer-experience marts shall support review, score, response, and service-quality analysis while preserving the approved review identity and review-to-order relationships.

## 29. Cross-Domain Mart Boundary
Cross-domain marts may combine multiple governed domains when a defined analytical use case requires them. Such marts shall explicitly document join keys, grain compatibility, relationship cardinality, and business purpose.

## 30. Model Organization Standards
Each mart shall have a clear model naming convention, domain ownership, purpose, declared grain, upstream dependencies, dimensions, measures, business rules, quality expectations, and downstream consumers.

## 31. Reusable Model Boundary
Common business logic shall remain in governed upstream models. Domain marts shall primarily compose approved analytical structures rather than independently implementing the same transformation logic.

## 32. Acceptance Criteria
Area 39.2 is accepted when business-domain organization, domain boundaries, cross-domain controls, model organization, grain declarations, upstream dependencies, reusable-logic ownership, and consumer-oriented structure are explicitly documented and validated.

