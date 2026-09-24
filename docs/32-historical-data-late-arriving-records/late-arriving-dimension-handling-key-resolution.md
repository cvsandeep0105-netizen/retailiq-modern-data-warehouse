# Area 32.2 — Late-Arriving Dimension Handling & Key Resolution

Status: Accepted & Frozen

## 1. Purpose
Define controlled handling of dimension records that arrive after dependent analytical processing, including natural-key resolution, surrogate-key assignment, unknown-member handling, and historical correction.

## 2. Area 32.1 Dependency
Late-arriving dimension handling shall implement the historical and late-arriving record foundation established in Area 32.1.

## 3. Area 31 Dependency
Dimension arrival and correction shall remain consistent with Slowly Changing Dimension versioning and effective-dating controls.

## 4. Area 30 Dependency
Late-arriving dimension resolution shall preserve conformed and role-playing dimension semantics.

## 5. Area 29 Dependency
Key resolution shall preserve fact grain and measure interpretation.

## 6. Area 28 Dependency
Resolved dimension keys shall maintain approved fact-to-dimension relationships.

## 7. Area 27 Dependency
Dimension resolution shall remain within approved dimension ownership and attribute boundaries.

## 8. Area 26 Dependency
Natural-key matching and surrogate-key assignment shall follow the approved key strategy.

## 9. Area 25 Dependency
Late-arriving dimension handling shall not alter the declared business grain.

## 10. Area 24 Dependency
Resolution behavior shall follow approved dimensional modeling patterns.

## 11. Area 23 Dependency
Profiling evidence shall provide baseline expectations for dimension populations, nullability, and key completeness.

## 12. Area 22 Dependency
Dimension resolution shall support reconciliation between source identities, dimension identities, and dependent facts.

## 13. Area 21 Dependency
Duplicate resolution shall precede natural-key matching and surrogate-key creation.

## 14. Area 20 Dependency
Natural-key comparison shall use standardized values and governed normalization rules.

## 15. Area 19 Dependency
Transformation logic shall preserve business identity and meaning before key resolution.

## 16. Area 18 Dependency
Late-arriving dimension records shall be traceable to governed staging outputs.

## 17. Area 07 Dependency
Key resolution shall remain aligned with the frozen source contracts and schema expectations.

## 18. Late-Arriving Dimension Detection
A dimension record shall be classified as late-arriving when its valid business context becomes available after a dependent fact or analytical record has already been processed without that dimension context.

## 19. Natural-Key Resolution
Resolution shall first identify the governed natural key and determine whether a matching dimension entity already exists. Natural-key matching shall be deterministic and shall not rely on descriptive similarity when the governed identity is unavailable.

## 20. Surrogate-Key Resolution
When a valid dimension entity exists, the dependent fact shall resolve to the appropriate surrogate key for the business-effective context. Historical Type 2 context shall be respected when effective dating is applicable.

## 21. Unknown and Temporary Member Handling
When dimension context is genuinely unavailable at fact-processing time, a governed unknown or temporary handling strategy shall prevent invalid foreign-key relationships. Temporary handling shall not be treated as proof of a permanent unknown business entity.

## 22. Historical Backfill and Correction
When the late dimension record subsequently becomes available, affected dependent records shall be eligible for controlled key correction or historical backfill. Corrections shall preserve fact grain, measure values, source identity, audit evidence, and historical meaning.

## 23. Multiple Matches and Ambiguous Resolution
If a natural key maps to multiple incompatible dimension states or cannot be resolved deterministically, processing shall produce an explicit exception rather than selecting an arbitrary surrogate key.

## 24. Reconciliation, Lineage, Idempotency and Audit
Every late-arriving resolution shall retain source natural key, resolved surrogate key, dimension version where applicable, effective context, processing timestamps, resolution status, exception reason where applicable, and lineage. Reprocessing the same record shall not create duplicate entities or duplicate corrections.

## 25. Acceptance Criteria
Area 32.2 is acceptable when late-arriving dimension detection, natural-key resolution, surrogate-key resolution, unknown/temporary handling, historical correction, ambiguity handling, reconciliation, lineage, idempotency, auditability, and all required upstream dependencies are explicitly governed.

