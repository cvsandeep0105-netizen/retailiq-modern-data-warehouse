# Area 35.2 — Incremental Model Key & Merge Strategy Controls

Status: Accepted & Frozen

## 1. Purpose
Define deterministic key-resolution, matching, merge, update, insert, and historical-preservation controls for incremental analytical models.

## 2. Area 35.1 Dependency
Key and merge behavior shall implement the incremental model engineering foundation, including model identity, processing boundaries, change application semantics, dependency execution, idempotency, quality, and lineage.

## 3. Area 34 Dependency
Key and merge operations shall respect the approved watermark, change-detection, processing eligibility, replay, recovery, and reconciliation controls.

## 4. Area 32 Dependency
Late-arriving records, historical corrections, and backfills shall use controlled key resolution without destroying previously established historical context.

## 5. Area 31 Dependency
SCD-enabled dimensions shall preserve historical versions and shall not overwrite historical identity through uncontrolled merge behavior.

## 6. Area 30 Dependency
Conformed and role-playing dimensions shall use consistent key semantics across dependent analytical models.

## 7. Area 29 Dependency
Fact merge behavior shall preserve the declared fact grain and prevent duplicate measures caused by incorrect matching.

## 8. Area 28 Dependency
Merge strategy shall follow the approved fact and dimension architecture.

## 9. Area 27 Dependency
Dimension-specific key and merge rules shall respect approved dimension ownership and attribute-change classification.

## 10. Area 26 Dependency
Natural-key and surrogate-key definitions shall remain the authoritative identity boundary for incremental matching.

## 11. Area 25 Dependency
Merge operations shall preserve the declared business grain and shall not create unintended one-to-many expansion.

## 12. Area 24 Dependency
Key behavior shall remain consistent with the dimensional modeling strategy and approved analytical relationships.

## 13. Area 23 Dependency
Key populations and merge outcomes shall be measurable against established profiling baselines.

## 14. Area 22 Dependency
Merge results shall support source-to-target reconciliation, accepted/rejected populations, and controlled exception handling.

## 15. Area 21 Dependency
Duplicate and record-resolution rules shall be applied before a source record is treated as a unique incremental business change.

## 16. Area 20 Dependency
Key comparison shall operate on standardized and normalized values to prevent representation differences from producing false matches or changes.

## 17. Natural-Key Matching
Incremental models shall define the natural business identifier used to match incoming records to existing records. Natural-key matching shall be deterministic, documented, and appropriate to the declared business grain.

## 18. Surrogate-Key Resolution
Where surrogate keys are used, incoming records shall resolve to the correct existing or newly created surrogate key through controlled natural-key lookup and applicable historical-effective-date rules.

## 19. Composite-Key Controls
Models requiring multiple attributes for identity shall define the complete composite key, attribute order or canonical representation where relevant, null handling, normalization rules, and uniqueness expectations.

## 20. Insert, Update and No-Change Semantics
Each incremental model shall explicitly distinguish new records, changed records, unchanged records, corrections, and invalid records. No-change records shall not generate unnecessary updates or historical versions.

## 21. Merge Conflict Controls
Multiple incoming records resolving to the same target identity shall be treated as a controlled condition. The model shall apply deterministic ordering, source precedence, or quarantine rules rather than relying on nondeterministic merge behavior.

## 22. SCD and Historical Merge Controls
For historical dimensions, merge behavior shall respect effective dates, current-row indicators, non-overlapping validity intervals, and approved SCD type rules. Historical records shall never be silently replaced when historical preservation is required.

## 23. Idempotency, Duplicate Prevention and Reprocessing
Repeated processing of the same source boundary shall resolve to the same target state. Merge operations shall prevent duplicate inserts, duplicate fact measures, repeated dimension versions, and unintended updates during replay.

## 24. Reconciliation, Audit and Exception Controls
Merge results shall retain inserted, updated, unchanged, rejected, quarantined, and conflicted populations where applicable. Key-resolution decisions, merge outcomes, source boundaries, target identities, exceptions, and remediation shall remain auditable and traceable.

## 25. Acceptance Criteria
Area 35.2 is accepted when natural-key matching, surrogate-key resolution, composite-key handling, insert/update/no-change semantics, conflict handling, SCD historical behavior, idempotency, duplicate prevention, reconciliation, auditability, exception handling, and all required dependencies are explicitly governed.

