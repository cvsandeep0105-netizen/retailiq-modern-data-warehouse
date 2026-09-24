# Area 32.3 — Late-Arriving Fact Handling & Historical Backfill Controls

Status: Accepted & Frozen

## 1. Purpose
Define controlled handling of fact records that arrive after their expected analytical processing point, including historical date assignment, dimension-key resolution, backfill, reconciliation, and idempotent reprocessing.

## 2. Area 32.1 Dependency
Late-arriving fact handling shall implement the historical-data and late-arriving-record foundation established in Area 32.1.

## 3. Area 32.2 Dependency
Fact processing shall use the approved late-arriving dimension and key-resolution controls from Area 32.2.

## 4. Area 31 Dependency
Historical fact handling shall remain compatible with SCD versioning and effective-dating controls.

## 5. Area 30 Dependency
Fact backfill shall preserve conformed and role-playing dimension semantics.

## 6. Area 29 Dependency
Backfilled facts shall preserve approved fact grain, measure ownership, additivity, and aggregation behavior.

## 7. Area 28 Dependency
Late-arriving facts shall remain consistent with approved fact architecture and fact-to-dimension relationships.

## 8. Area 27 Dependency
Dimension relationships required by late-arriving facts shall remain within approved dimension architecture.

## 9. Area 26 Dependency
Fact records shall use governed natural-key and surrogate-key resolution rules.

## 10. Area 25 Dependency
Backfill shall not alter the declared business grain of the affected fact.

## 11. Area 24 Dependency
Late-arriving fact processing shall follow approved dimensional modeling patterns.

## 12. Area 23 Dependency
Profiling baselines shall support detection of unexpected fact timing, population, and historical-period changes.

## 13. Area 22 Dependency
Late-arriving facts shall reconcile to upstream source populations, control totals, and affected analytical populations.

## 14. Area 21 Dependency
Duplicate and record-resolution controls shall be applied before fact insertion or historical backfill.

## 15. Area 20 Dependency
Fact matching and comparison shall operate on standardized source values.

## 16. Area 19 Dependency
Transformation logic shall preserve the original business meaning and declared fact grain before backfill.

## 17. Area 18 Dependency
Late-arriving facts shall remain traceable to governed staging records and staging transformation outputs.

## 18. Area 07 Dependency
Fact acceptance shall remain aligned with the frozen source contracts, schema expectations, and source identity rules.

## 19. Late-Arriving Fact Detection
A fact shall be classified as late-arriving when a valid business event becomes available after its expected analytical processing point or after dependent dimension context has already been processed.

## 20. Business-Effective Date Assignment
The fact shall use the appropriate business-effective event timestamp or date for analytical period assignment. Technical ingestion or processing time shall not replace the business event time unless explicitly governed by the metric definition.

## 21. Historical Dimension Context Resolution
Late-arriving facts shall resolve dimension surrogate keys according to the business-effective context. Where Type 2 history applies, the dimension version valid for the fact's effective context shall be selected rather than automatically using the current dimension version.

## 22. Historical Backfill Controls
Backfill shall insert or correct the affected fact population without changing the approved fact grain or measure values. Existing analytical results affected by the backfill shall be identifiable and reconcilable.

## 23. Duplicate, Correction and Ambiguity Controls
A late-arriving fact shall not be inserted twice. Existing matching records shall be classified as duplicate, correction, replacement, or other governed outcome. Ambiguous identity or historical context shall produce an explicit exception rather than an arbitrary resolution.

## 24. Reconciliation, Lineage, Idempotency and Audit
Each late-arriving fact shall retain source identity, business-effective time, processing time, resolved dimension keys, backfill status, source-to-target lineage, reconciliation evidence, and audit information. Reprocessing the same source event shall be deterministic and shall not create duplicate facts.

## 25. Acceptance Criteria
Area 32.3 is acceptable when late-arriving fact detection, business-effective dating, historical dimension context resolution, backfill, duplicate/correction handling, ambiguity controls, reconciliation, lineage, idempotency, auditability, and all required upstream dependencies are explicitly governed.

