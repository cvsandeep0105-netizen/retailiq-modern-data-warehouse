# Area 42.2 — Semantic Model Structure, Entities, Dimensions & Relationships

Status: Accepted & Frozen

## 1. Purpose
Define the governed semantic model structure, business entities, dimensions, relationships, cardinality, keys, hierarchies, and analytical navigation boundaries for RetailIQ.

## 2. Area 42.1 Dependency
This artifact shall preserve the frozen Semantic / Business Layer Foundation, including business vocabulary, semantic entities, dimensions, measures, KPIs, relationships, aggregation, grain, governance, lineage, and BI boundaries.

## 3. Area 41 Dependency
Semantic model objects shall reference approved Business Metrics and KPI definitions without redefining their business meaning.

## 4. Area 40 Dependency
Semantic entities shall consume approved Business Data Marts and preserve their declared business grain and analytical responsibilities.

## 5. Area 39 Dependency
Semantic relationships shall follow the approved Data Mart Architecture and its fact, dimension, grain, business-logic, and double-counting boundaries.

## 6. Area 38 Dependency
Semantic dependencies shall follow the approved Transformation Dependency Graph.

## 7. Area 37 Dependency
Semantic models shall comply with approved analytics engineering model contracts, naming, documentation, testing, lineage, and change-control standards.

## 8. Area 36 Dependency
Reusable business transformations shall remain owned by the Intermediate/Core layer and shall not be unnecessarily duplicated here.

## 9. Area 35 Dependency
Semantic models shall preserve approved incremental model identity, merge, idempotency, reconciliation, and recovery behavior.

## 10. Area 34 Dependency
Semantic refresh shall remain compatible with approved full-refresh and incremental processing strategies.

## 11. Area 33 Dependency
Semantic structures shall remain within the approved ELT architecture.

## 12. Area 32 Dependency
Historical semantic relationships shall preserve approved late-arriving and historical record behavior.

## 13. Area 31 Dependency
Historical dimension exposure shall preserve approved SCD versioning and effective-dating semantics.

## 14. Area 30 Dependency
Semantic relationships shall use approved conformed and role-playing dimensions.

## 15. Area 29 Dependency
Semantic measures shall preserve approved fact grain and measure design.

## 16. Area 28 Dependency
Semantic entities shall respect approved fact and dimension responsibilities.

## 17. Area 27 Dependency
Dimension entities shall follow the approved Dimension Architecture.

## 18. Area 26 Dependency
Semantic relationships shall preserve approved natural-key and surrogate-key behavior.

## 19. Area 25 Dependency
Each semantic object shall preserve its declared business grain.

## 20. Area 24 Dependency
Semantic model structure shall follow the approved Dimensional Modeling Strategy.

## 21. Area 23 Dependency
Semantic structures shall remain compatible with the approved profiling baseline.

## 22. Area 22 Dependency
Semantic relationships and measures shall support approved reconciliation controls.

## 23. Area 21 Dependency
Semantic objects shall preserve approved duplicate and record-resolution behavior.

## 24. Area 20 Dependency
Semantic inputs shall consume approved standardized and normalized analytical data.

## 25. Semantic Model Topology
The semantic model shall provide a governed business-facing topology between approved business entities, dimensions, measures, KPIs, and analytical relationships.

## 26. Core Business Entities
Core semantic entities shall include Order, Customer, Product, Seller, Payment, Review, Date, and other approved business concepts required by analytical consumption.

## 27. Order Entity
Order shall represent the approved order business concept and shall preserve order-level grain, lifecycle semantics, customer relationship, dates, status, and approved order measures.

## 28. Customer Entity
Customer shall represent the approved customer business concept and shall preserve customer identity, geography, lifecycle, and approved customer-level analytical attributes.

## 29. Product Entity
Product shall represent the approved product business concept and shall preserve product identity, category, descriptive attributes, and approved product-level analytical attributes.

## 30. Seller Entity
Seller shall represent the approved seller business concept and shall preserve seller identity, geography, fulfillment context, and approved seller-level analytical attributes.

## 31. Payment Entity
Payment shall represent payment events and payment attributes without incorrectly attaching payment-grain measures directly to order-grain measures.

## 32. Review Entity
Review shall preserve the approved review identity and review-to-order relationship, including the documented repeated review_id boundary.

## 33. Date Entity
Date shall provide governed calendar context for approved business dates and shall support role-playing date relationships where required.

## 34. Dimension Structure
Dimensions shall expose approved descriptive attributes while preserving surrogate keys, natural keys, historical behavior, hierarchies, and unknown-member semantics.

## 35. Customer Dimension
Customer dimension attributes shall support customer identity, location, customer lifecycle context, and approved historical attributes without changing customer grain.

## 36. Product Dimension
Product dimension attributes shall support product identity, category, translated category where available, descriptive characteristics, and approved historical behavior.

## 37. Seller Dimension
Seller dimension attributes shall support seller identity, geography, fulfillment context, and approved historical behavior.

## 38. Date Dimension
Date dimension shall provide reusable calendar attributes such as date, day, week, month, quarter, year, and other governed calendar attributes.

## 39. Role-Playing Date Dimensions
Purchase date, approval date, carrier delivery date, customer delivery date, estimated delivery date, review creation date, and other approved date roles shall be represented through governed role-playing relationships where applicable.

## 40. Fact Relationship Boundary
Fact entities shall remain the authoritative source for quantitative event-level measures. Semantic dimensions shall provide descriptive context without duplicating fact measures.

## 41. Primary Relationship
Each semantic relationship shall identify the parent entity, child entity, join key, cardinality, and analytical purpose.

## 42. Key Relationship
Semantic joins shall use approved surrogate or natural keys according to the governed model design and shall not rely on ambiguous descriptive attributes.

## 43. Cardinality
Relationship cardinality shall explicitly identify one-to-one, one-to-many, many-to-one, or controlled many-to-many behavior.

## 44. Referential Integrity
Semantic relationships shall preserve approved referential integrity and shall identify expected unknown or unmatched members.

## 45. Many-to-Many Relationship Control
Many-to-many relationships shall be isolated, explicitly documented, and protected from measure multiplication.

## 46. Bridge Boundary
Where a bridge structure is required, its grain, keys, relationship purpose, and aggregation implications shall be explicitly documented.

## 47. Hierarchy Structure
Approved hierarchies shall document levels, parent-child relationships, ordering, and valid drill paths.

## 48. Customer Geography Hierarchy
Customer geography may expose governed state and city attributes while preserving the underlying customer grain and avoiding geographic duplication.

## 49. Seller Geography Hierarchy
Seller geography may expose governed state and city attributes while preserving seller grain.

## 50. Product Category Hierarchy
Product category shall preserve source category semantics and shall not invent translations for the 13 unmatched category values identified during source profiling.

## 51. Order Lifecycle Navigation
Order status and approved lifecycle dates shall support governed analytical navigation without changing the source lifecycle definitions.

## 52. Filter Propagation
Filter propagation between semantic entities shall be deterministic and shall not unintentionally multiply or remove measure populations.

## 53. Relationship Direction
Relationship direction shall be explicitly documented wherever the semantic implementation supports directional filter behavior.

## 54. Ambiguous Relationship Prevention
Multiple competing paths between semantic entities shall be identified and controlled to prevent ambiguous analytical results.

## 55. Circular Relationship Prevention
Circular semantic relationships shall not be introduced unless a specific governed implementation pattern explicitly supports them.

## 56. Grain Protection
Adding dimensions or relationships to a semantic query shall not silently change the declared grain of a measure or KPI.

## 57. Measure Multiplication Protection
Relationships shall be tested for measure multiplication caused by one-to-many and many-to-many joins.

## 58. KPI Context
KPIs shall expose only dimensions and relationships that are compatible with their approved calculation population and grain.

## 59. Business-Friendly Navigation
Semantic objects shall support intuitive navigation using business terminology rather than requiring consumers to understand physical warehouse structures.

## 60. Technical Traceability
Every semantic entity, attribute, relationship, and hierarchy shall remain traceable to its governed warehouse object and business definition.

## 61. Security Boundary
Semantic relationships and objects shall respect approved access-control and governance boundaries.

## 62. Documentation
Each semantic object shall document purpose, grain, keys, relationships, attributes, measures, filters, hierarchy, ownership, lineage, and known limitations.

## 63. Testing
Semantic model validation shall test relationship cardinality, referential integrity, filter propagation, grain preservation, measure multiplication, KPI compatibility, and reconciliation.

## 64. Reconciliation
Semantic model outputs shall reconcile to the corresponding approved marts, facts, dimensions, metrics, and KPIs.

## 65. Lineage
Semantic relationships shall maintain lineage to upstream analytical models, metrics, dimensions, facts, and source structures.

## 66. Change Control
Changes to semantic entities, attributes, relationships, hierarchies, keys, or navigation behavior shall require documented impact analysis, approval, regression testing, and version history.

## 67. BI Boundary
The semantic model shall provide governed structures suitable for later BI-ready data products and analytical consumption.

## 68. Source Preservation
Semantic modeling shall never mutate, overwrite, delete, or alter original source data.

## 69. Technology-Neutral Boundary
The semantic model shall remain independent of a specific BI visualization product unless a later approved implementation decision establishes such a dependency.

## 70. Acceptance Criteria
Area 42.2 is accepted when semantic topology, business entities, dimensions, facts, keys, cardinality, referential integrity, many-to-many boundaries, bridge structures, hierarchies, role-playing dates, filter propagation, relationship direction, ambiguity prevention, circular relationship prevention, grain protection, measure multiplication protection, KPI compatibility, business navigation, technical traceability, security, documentation, testing, reconciliation, lineage, change control, BI boundaries, and source preservation are explicitly documented and validated.

