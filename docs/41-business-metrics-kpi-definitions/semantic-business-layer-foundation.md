# Area 42.1 — Semantic / Business Layer Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the governed Semantic / Business Layer that presents approved metrics, KPIs, dimensions, business entities, analytical relationships, and business terminology consistently to downstream analytical and BI consumers.

## 2. Area 41 Dependency
The Semantic / Business Layer shall consume the frozen Business Metrics & KPI Definitions from Area 41 without silently redefining approved metric or KPI business meaning.

## 3. Area 40 Dependency
Semantic entities and measures shall consume approved Business Data Marts and preserve their declared grain, dimensions, facts, measures, reconciliation, and business boundaries.

## 4. Area 39 Dependency
Semantic structures shall follow the approved Data Mart Architecture, including domain organization, grain, fact-dimension relationships, business-logic boundaries, and double-counting controls.

## 5. Area 38 Dependency
Semantic dependencies shall follow the approved Transformation Dependency Graph.

## 6. Area 37 Dependency
Semantic models shall comply with Analytics Engineering Framework standards for model contracts, documentation, testing, ownership, lineage, reproducibility, and controlled change.

## 7. Area 36 Dependency
Reusable Intermediate/Core business transformations shall remain owned upstream and shall not be unnecessarily duplicated in the Semantic Layer.

## 8. Area 35 Dependency
Semantic outputs shall preserve incremental model identity, idempotency, merge, reconciliation, recovery, and replay behavior.

## 9. Area 34 Dependency
Semantic refresh behavior shall remain compatible with approved full-refresh and incremental processing strategies.

## 10. Area 33 Dependency
Semantic models shall remain within the approved ELT architecture and transformation boundaries.

## 11. Area 32 Dependency
Historical semantic interpretation shall preserve approved historical and late-arriving record behavior.

## 12. Area 31 Dependency
Historical dimension attributes exposed through the semantic layer shall preserve approved SCD behavior.

## 13. Area 30 Dependency
Semantic dimensions shall use approved conformed and role-playing dimension structures.

## 14. Area 29 Dependency
Semantic measures shall preserve approved fact grain and measure definitions.

## 15. Area 28 Dependency
Semantic relationships shall respect approved fact and dimension responsibilities.

## 16. Area 27 Dependency
Semantic dimensions shall follow the approved Dimension Architecture.

## 17. Area 26 Dependency
Semantic relationships shall preserve approved natural-key and surrogate-key semantics.

## 18. Area 25 Dependency
Every semantic measure shall retain a clearly defined business grain.

## 19. Area 24 Dependency
Semantic structures shall follow the approved Dimensional Modeling Strategy.

## 20. Area 23 Dependency
Semantic definitions shall remain compatible with approved Data Profiling Baselines.

## 21. Area 22 Dependency
Semantic values shall support approved reconciliation controls.

## 22. Area 21 Dependency
Semantic outputs shall preserve approved duplicate detection and record-resolution behavior.

## 23. Area 20 Dependency
Semantic inputs shall consume approved standardized and normalized analytical data.

## 24. Business Meaning
The Semantic / Business Layer shall translate technical warehouse structures into governed business concepts understandable by analysts, BI consumers, and business stakeholders.

## 25. Business Vocabulary
Business terms shall use approved terminology from the Business Domain, Business Glossary, Metric Catalog, KPI Catalog, and Data Mart definitions.

## 26. Semantic Entity
A semantic entity represents a governed business concept such as Order, Customer, Product, Seller, Payment, Review, Date, or another approved analytical subject.

## 27. Semantic Dimension
Dimensions shall expose approved descriptive attributes and shall preserve their declared business meaning, key semantics, hierarchy, and historical behavior.

## 28. Semantic Measure
Measures shall reference approved governed metrics and shall preserve calculation, grain, aggregation, unit, population, and dimensional compatibility.

## 29. Semantic KPI
KPIs shall reference the approved KPI definitions from Area 41 and shall expose their governed business meaning without redefining the underlying formula.

## 30. Semantic Relationship
Relationships between semantic entities shall explicitly define participating entities, keys, cardinality, relationship direction, and analytical purpose.

## 31. Relationship Cardinality
One-to-one, one-to-many, many-to-one, and many-to-many relationships shall be explicitly documented where relevant.

## 32. Many-to-Many Boundary
Many-to-many relationships shall not be exposed in a way that silently causes measure multiplication or double-counting.

## 33. Measure Aggregation
Every semantic measure shall declare whether it is additive, semi-additive, non-additive, ratio-based, distinct-count, or another governed type.

## 34. Default Aggregation
Default aggregation behavior shall be explicitly governed and shall never be inferred solely from the physical data type.

## 35. Metric Reuse
Equivalent business metrics shall be defined once and reused rather than recreated independently across semantic consumers.

## 36. KPI Reuse
Approved KPIs shall have a single governed semantic definition and shall not receive conflicting downstream formulas.

## 37. Business Filters
Common business filters such as order status, date range, customer state, seller state, product category, and payment type shall use governed definitions.

## 38. Status Semantics
Order and other business status values shall retain documented source and analytical meanings. Semantic labels shall not silently change source classifications.

## 39. Date Semantics
Semantic date attributes shall distinguish relevant business dates such as purchase, approval, delivery, estimated delivery, review, and other approved date roles.

## 40. Time Context
Time-based metrics shall explicitly identify the date role and performance-period semantics used for analysis.

## 41. Currency Semantics
Currency-valued measures shall document their source currency context, unit, and any approved conversion boundary.

## 42. Null Semantics
Null values shall retain their documented meaning. The semantic layer shall not convert unknown, unavailable, or not-applicable values into misleading business values.

## 43. Unknown Member Semantics
Approved unknown or not-applicable dimension members shall retain their governed interpretation.

## 44. Business-Friendly Naming
Semantic names shall be understandable to business consumers while remaining traceable to governed technical definitions.

## 45. Technical-to-Business Mapping
Semantic attributes shall retain mappings to their underlying technical fields, models, metrics, or dimensions.

## 46. Grain Protection
Semantic exposure shall not change the underlying grain of facts, dimensions, metrics, or KPIs.

## 47. Double-Counting Protection
Semantic relationships and measures shall prevent inflated results caused by multiple items, payments, reviews, sellers, or other one-to-many relationships.

## 48. Filter Context
Filter behavior shall be deterministic and shall not unexpectedly alter populations used by governed measures or KPIs.

## 49. Security Boundary
Semantic access shall respect approved governance, security, ownership, and access-control boundaries.

## 50. Governance
Every semantic entity, measure, KPI, relationship, and business definition shall have an identifiable owner and documented change-control responsibility.

## 51. Documentation
Semantic objects shall document business meaning, technical source, grain, relationships, aggregation, filters, ownership, and known limitations.

## 52. Lineage
Semantic objects shall maintain lineage to approved metrics, marts, transformations, dimensions, facts, and upstream source structures.

## 53. Testing
Semantic objects shall be validated for relationship correctness, measure correctness, grain preservation, aggregation behavior, filtering, reconciliation, and regression.

## 54. Reconciliation
Semantic measures and KPIs shall reconcile to their governed upstream metric and mart values.

## 55. Change Control
Changes to semantic definitions, relationships, measures, KPIs, filters, or business terminology shall require documented impact analysis, approval, regression validation, and version history.

## 56. BI Consumption Boundary
The Semantic / Business Layer shall provide governed business-facing structures for downstream BI-ready data products and analytical consumption.

## 57. Source Preservation
Semantic modeling shall never mutate, overwrite, delete, or alter original source records.

## 58. Technology-Neutral Boundary
The semantic design shall remain independent of a specific BI vendor or visualization tool unless a later implementation decision explicitly establishes such a dependency.

## 59. Acceptance Criteria
Area 42.1 is accepted when semantic purpose, business vocabulary, entities, dimensions, measures, KPIs, relationships, cardinality, many-to-many protection, aggregation, metric reuse, filters, status semantics, date semantics, time context, currency, nulls, unknown members, naming, technical mappings, grain, double-counting, governance, documentation, lineage, testing, reconciliation, change control, BI consumption, source preservation, and technology-neutral boundaries are explicitly documented and validated.

