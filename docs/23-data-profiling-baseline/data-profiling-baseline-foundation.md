# Area 23.1 — Data Profiling Baseline Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the baseline profiling framework for measuring the structural, quality, completeness, uniqueness, distribution, temporal, relationship, and business characteristics of RetailIQ data before downstream analytical modeling.

## 2. Area 05 Source Profiling Dependency
The baseline shall build on the physical source profiling evidence established in Area 05 and shall not replace or contradict the accepted source observations.

## 3. Area 06 Relationship Dependency
Profiling shall preserve the relationship, key, cardinality, and exception boundaries established in Area 06.

## 4. Area 07 Contract Dependency
Profiling expectations shall remain consistent with the source schema, data types, nullability, and contract expectations established in Area 07.

## 5. Area 17 Raw Validation Dependency
Profiling shall distinguish accepted raw populations from rejected or quarantined populations established in Area 17.

## 6. Area 18 Staging Dependency
Profiling shall support validation of staging populations and transformations established in Area 18.

## 7. Area 19 Transformation Dependency
Profiling shall identify the measurable effects of approved staging transformations without treating expected changes as unexplained defects.

## 8. Area 20 Standardization Dependency
Profiling shall distinguish standardized representations from source representations while preserving business meaning.

## 9. Area 21 Deduplication Dependency
Profiling shall account for source duplicates, detected duplicates, resolved records, and preserved non-merge populations established in Area 21.

## 10. Area 22 Reconciliation Dependency
Profiling results shall support and remain consistent with the reconciliation controls, control totals, mappings, and exception framework established in Area 22.

## 11. Profiling Scope
The baseline shall cover source, staging, standardized, and applicable downstream analytical populations at their defined processing boundaries.

## 12. Structural Profiling
Structural profiling shall capture table or dataset presence, column presence, data types, field widths where relevant, record counts, and schema conformity.

## 13. Completeness Profiling
Completeness profiling shall measure null, missing, blank, and otherwise unavailable values for fields where completeness is analytically or contractually meaningful.

## 14. Uniqueness Profiling
Uniqueness profiling shall measure unique identifiers, duplicate populations, composite-key behavior, and entity-specific uniqueness expectations.

## 15. Validity Profiling
Validity profiling shall evaluate values against documented domains, formats, ranges, temporal boundaries, and contract expectations.

## 16. Distribution Profiling
Distribution profiling shall capture meaningful categorical frequencies, numeric ranges, central tendencies where useful, and materially skewed or sparse populations.

## 17. Temporal Profiling
Temporal profiling shall establish observed date ranges, missing temporal values, lifecycle intervals, and unexpected temporal boundaries.

## 18. Relationship Profiling
Relationship profiling shall measure parent-child coverage, orphan populations, relationship multiplicity, and documented boundary cases.

## 19. Business Profiling
Business profiling shall capture characteristics relevant to orders, customers, products, sellers, payments, reviews, and order items at their documented business grain.

## 20. Baseline Metrics
Each baseline metric shall have a defined name, population, field or entity scope, measurement rule, expected interpretation, and evidence location.

## 21. Baseline Versioning
Profiling baselines shall be versioned so future processing runs can distinguish legitimate data evolution from unexpected quality changes.

## 22. Exception Handling
Material deviations from established baseline expectations shall be classified, evidenced, investigated, and linked to the applicable reconciliation or quality control.

## 23. Evidence and Lineage
Profiling evidence shall identify the data boundary, execution context, metric definition, observed result, comparison baseline, exception state, and lineage information.

## 24. Technology-Neutral Boundary
This foundation defines logical profiling requirements without prescribing a specific warehouse, database, SQL engine, orchestration platform, or BI technology.

## 25. Acceptance Criteria
Area 23.1 is acceptable when profiling scope, structural, completeness, uniqueness, validity, distribution, temporal, relationship, business, baseline, versioning, exception, and lineage controls are explicitly defined and traceable to the frozen upstream Areas.

