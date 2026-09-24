# Area 31.3 — SCD Historical Versioning & Effective-Dating Controls

Status: Accepted & Frozen

## 1. Purpose
Define controlled historical versioning and effective-dating rules for Slowly Changing Dimensions without changing the frozen source data or previously approved dimensional grain.

## 2. Area 31.1 Dependency
Historical versioning shall implement the SCD foundation defined in Area 31.1.

## 3. Area 31.2 Dependency
Historical version creation shall follow the attribute-level SCD type classifications defined in Area 31.2.

## 4. Area 30 Dependency
Historical dimension versions shall remain compatible with conformed and role-playing dimension behavior.

## 5. Area 29 Dependency
Dimension versioning shall preserve approved fact-grain and measure interpretation.

## 6. Area 28 Dependency
Historical dimension rows shall maintain approved fact-to-dimension relationship semantics.

## 7. Area 27 Dependency
Versioned attributes shall remain within the approved dimension ownership and architecture boundaries.

## 8. Area 26 Dependency
Each historical version shall retain the approved natural-key identity and receive a governed surrogate-key identity.

## 9. Area 25 Dependency
Historical versioning shall not alter the declared business grain of the dimension or consuming facts.

## 10. Area 24 Dependency
Effective dating shall follow the dimensional modeling patterns approved in Area 24.

## 11. Area 23 Dependency
Profiling evidence shall be used to identify nullability, stability, and source-quality considerations without inferring historical changes from a static snapshot.

## 12. Area 22 Dependency
Historical version populations and transitions shall remain reconcilable to governed upstream records.

## 13. Area 21 Dependency
Record identity and duplicate resolution shall be completed before historical version creation.

## 14. Area 20 Dependency
Historical comparisons shall operate on standardized values so formatting-only changes do not create false SCD versions.

## 15. Area 19 Dependency
Transformation rules shall preserve business meaning before historical change detection.

## 16. Area 07 Dependency
Historical versioning shall remain traceable to the frozen source schema and data contract.

## 17. Historical Version Identity
Each Type 2 historical version shall be uniquely identifiable through its governed surrogate key while retaining the source natural key for business identity and traceability.

## 18. Effective Start and End Dating
Type 2 records shall use governed effective-start and effective-end boundaries. The effective interval shall represent the period during which the dimension version is valid.

## 19. Current-Version Control
Each Type 2 natural-key entity shall have a controlled current-version indicator. At most one version shall be designated current for a given natural key.

## 20. Non-Overlapping Version Intervals
Historical versions for the same natural key shall not contain overlapping effective intervals. A newly detected version shall close the preceding applicable version according to the approved effective-date rule.

## 21. Change Event Date and Load Date
Business-effective change timing and technical ingestion/load timing shall remain distinct. A technical load timestamp shall not automatically be treated as the business-effective date.

## 22. Unknown and Not-Applicable Members
Unknown and not-applicable dimension members shall remain distinct governed states and shall not be represented as historical versions of an identified business entity.

## 23. Late-Arriving and Out-of-Order Changes
Late-arriving or out-of-order historical changes shall be handled through controlled version adjustment, reconciliation, lineage, and audit procedures. Detailed late-arriving record processing remains within Area 32.

## 24. Reprocessing, Idempotency and Preservation
Repeated processing of the same source state shall not create duplicate historical versions. Reprocessing shall preserve deterministic version identity, source traceability, reconciliation evidence, and the original source data.

## 25. Acceptance Criteria
Area 31.3 is acceptable when historical version identity, effective-start and effective-end dating, current-version controls, non-overlapping intervals, business-effective versus technical timestamps, unknown/not-applicable handling, late-arriving boundaries, idempotency, reconciliation, lineage, and source preservation are explicitly governed and all required upstream dependencies are preserved.

