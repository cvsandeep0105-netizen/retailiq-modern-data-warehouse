# Area 34.2 — Incremental Change Detection & Watermark Controls

Status: Accepted & Frozen

## 1. Purpose
Define governed change-detection, watermark, cutoff, replay, and incremental eligibility controls for RetailIQ processing.

## 2. Area 34.1 Dependency
Change detection shall implement the approved full-refresh and incremental strategy foundation.

## 3. Area 33 Dependency
Incremental detection shall operate within the approved ELT architecture, dependency graph, quality boundaries, and transformation ownership.

## 4. Area 32 Dependency
Late-arriving records, historical corrections, and temporal backfills shall remain eligible for controlled incremental processing.

## 5. Area 31 Dependency
SCD historical changes shall use governed business-effective and processing-time boundaries.

## 6. Area 30 Dependency
Change detection shall preserve conformed and role-playing dimension semantics.

## 7. Area 29 Dependency
Incremental processing shall preserve fact grain and measure integrity.

## 8. Area 28 Dependency
Fact and dimension incremental processing shall follow approved analytical architecture.

## 9. Area 27 Dependency
Dimension change detection shall remain within approved dimension and attribute ownership boundaries.

## 10. Area 26 Dependency
Change detection shall use governed natural-key and surrogate-key relationships.

## 11. Area 25 Dependency
Incremental eligibility shall not alter declared business grain.

## 12. Area 24 Dependency
Change detection shall remain consistent with approved dimensional modeling patterns.

## 13. Area 23 Dependency
Profiling baselines shall support detection of unexpected incremental population and volume changes.

## 14. Area 22 Dependency
Incremental populations shall reconcile to source and upstream control totals.

## 15. Area 21 Dependency
Duplicate and record-resolution outcomes shall be applied before change detection where identity resolution is required.

## 16. Area 20 Dependency
Change comparison shall use standardized and normalized values to avoid representation-only changes.

## 17. Area 19 Dependency
Governed staging transformation outputs shall provide the inputs used by incremental detection.

## 18. Area 18 Dependency
Incremental processing shall consume approved staging outputs and preserve source-to-staging traceability.

## 19. Change Detection Signals
Incremental eligibility may be determined using governed source change timestamps, business-effective timestamps, source sequence values, explicit change indicators, controlled hashes, deterministic comparison, or other documented signals appropriate to the source and model.

## 20. Watermark Definition
A watermark represents the governed processing boundary used to identify source records eligible for an incremental run. Watermarks shall be associated with an explicit source field or change signal and processing context.

## 21. High-Watermark and Lower-Bound Controls
Incremental processing shall define both the prior committed boundary and the new processing cutoff where required. Boundary semantics shall specify inclusive or exclusive behavior to prevent gaps and unintended duplicate processing.

## 22. Overlap and Safety Window
Where source timing or delivery behavior can produce late records, incremental processing may use a controlled overlap or safety window. Reprocessing of the overlap must remain idempotent and reconciliation must distinguish legitimate replay from duplication.

## 23. Watermark Commit and Recovery
A new watermark shall be committed only after the associated incremental processing and required validation boundaries succeed. Failed processing shall not advance the committed watermark beyond unvalidated data.

## 24. Replay, Backfill, Audit and Preservation
Historical replay and backfill shall be able to process records outside the current watermark when explicitly authorized. Every watermark movement shall retain source boundary, previous value, new value, execution context, validation result, and audit evidence. Source data shall remain unchanged.

## 25. Acceptance Criteria
Area 34.2 is accepted when change-detection signals, watermark definitions, boundary semantics, overlap controls, commit/recovery rules, replay and backfill behavior, idempotency, reconciliation, auditability, and all required upstream dependencies are explicitly governed.

