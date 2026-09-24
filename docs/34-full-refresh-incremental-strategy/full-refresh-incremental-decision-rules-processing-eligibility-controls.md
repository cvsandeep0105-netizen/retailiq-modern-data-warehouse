# Area 34.3 — Full Refresh vs Incremental Decision Rules & Processing Eligibility Controls

Status: Accepted & Frozen

## 1. Purpose
Define deterministic rules for selecting full-refresh or incremental processing and establish eligibility controls before execution.

## 2. Area 34.1 Dependency
Processing-mode decisions shall implement the approved full-refresh and incremental strategy.

## 3. Area 34.2 Dependency
Incremental eligibility shall use the approved change-detection, watermark, cutoff, overlap, replay, and recovery controls.

## 4. Area 33 Dependency
Processing-mode selection shall remain within the approved ELT architecture and transformation ownership boundaries.

## 5. Area 32 Dependency
Historical corrections and late-arriving records shall remain eligible for controlled backfill or replay regardless of the normal incremental path.

## 6. Area 31 Dependency
SCD requirements shall influence processing eligibility whenever historical dimension changes require version creation or correction.

## 7. Area 30 Dependency
Conformed and role-playing dimension dependencies shall be considered before incremental execution.

## 8. Area 29 Dependency
Fact-grain and measure dependencies shall be validated before selecting an incremental processing path.

## 9. Area 28 Dependency
Fact and dimension architecture shall determine model-specific processing eligibility.

## 10. Area 27 Dependency
Dimension ownership and attribute-change rules shall be respected when determining incremental eligibility.

## 11. Area 26 Dependency
Natural-key and surrogate-key requirements shall be satisfied before records enter incremental processing.

## 12. Area 25 Dependency
Processing decisions shall preserve the approved business grain and shall not introduce grain changes.

## 13. Area 24 Dependency
Dimensional modeling dependencies shall be evaluated before processing dependent analytical models.

## 14. Area 23 Dependency
Profiling baselines shall be used to identify abnormal source volume, schema, nullability, or distribution conditions that may require full refresh or controlled recovery.

## 15. Area 22 Dependency
Source and target reconciliation controls shall determine whether incremental processing is eligible to continue.

## 16. Area 21 Dependency
Record identity and duplicate-resolution outcomes shall be stable before incremental processing is accepted.

## 17. Area 20 Dependency
Standardization and normalization outputs shall be stable before processing eligibility is evaluated.

## 18. Area 19 Dependency
Approved staging transformation outputs shall be available before downstream incremental processing begins.

## 19. Full Refresh Eligibility Rules
Full refresh shall be considered for initial model population, controlled rebuilds, structural model changes, unreliable or reset watermarks, major historical corrections, approved recovery events, or situations where incremental correctness cannot be demonstrated.

## 20. Incremental Eligibility Rules
Incremental processing shall require a valid committed watermark or approved initial-incremental baseline, valid change-detection signals, stable source and transformation contracts, available dependencies, and successful pre-execution validation.

## 21. Processing-Mode Decision Matrix
Processing mode shall be selected using deterministic model-specific rules rather than operator preference. The decision shall consider initial-load state, source change availability, watermark validity, schema changes, historical corrections, dependency readiness, reconciliation state, and recovery requirements.

## 22. Automatic Escalation to Full Refresh
If required incremental controls cannot establish complete and correct change coverage, processing shall be escalated to full refresh or controlled backfill. Examples include invalid watermark state, incompatible structural change, missing change signal, unreconciled prior execution, or unbounded historical correction.

## 23. Pre-Execution Eligibility Gate
Before execution, the model shall pass source availability, schema contract, dependency readiness, watermark state, change-window validity, duplicate controls, data-quality prerequisites, reconciliation state, and configuration validation. A failed gate shall prevent uncontrolled incremental execution.

## 24. Post-Execution Validation and Audit
Processing-mode selection, eligibility evidence, source boundaries, watermark values, row counts, reconciliation results, exceptions, execution outcome, and any escalation to full refresh shall be auditable and traceable. Successful completion shall not be inferred solely from job completion.

## 25. Acceptance Criteria
Area 34.3 is accepted when deterministic full-refresh and incremental decision rules, model-specific eligibility controls, escalation conditions, pre-execution gates, post-execution validation, auditability, idempotency, historical preservation, and all required dependencies are explicitly governed.

