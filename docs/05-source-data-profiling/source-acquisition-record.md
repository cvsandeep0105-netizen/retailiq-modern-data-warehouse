# Source Acquisition Record

## Document Status

- Status: Active
- Area: 05 — Source Data Profiling
- Step: 05.5 — Source Acquisition Record
- Record Type: Source acquisition and provenance evidence

## Source Dataset

- Dataset: Brazilian E-Commerce Public Dataset by Olist
- Kaggle Dataset Identifier: `olistbr/brazilian-ecommerce`
- Source Platform: Kaggle
- Acquisition Method: Kaggle CLI
- Local Source Path: `data/source/olist`
- Acquisition Timestamp: 2026-09-19 11:52:09 +05:30
- License Reported During Acquisition: CC-BY-NC-SA 4.0

## Acquisition Validation

- Kaggle CLI installation: PASS
- Kaggle authentication: PASS
- Kaggle dataset access verification: PASS
- Dataset download: PASS
- Extraction: PASS
- Expected CSV file count: 9
- Actual CSV file count: 9
- Unexpected non-CSV files: 0
- Total local CSV size: 120.34 MB

## Source Preservation Controls

- Original downloaded CSV files are preserved under `data/source/olist`.
- Source files are not modified, cleaned, renamed, or transformed at this stage.
- Source data is kept separate from derived warehouse and transformation artifacts.
- Physical schema, row counts, null rates, duplicate analysis, key analysis, and relationship analysis are established separately during Area 05 profiling.

## Provenance Boundary

The dataset is treated as externally sourced historical data acquired through Kaggle. Source facts are distinguished from project-derived profiling findings.

## License Boundary

The acquisition output reported the dataset license as CC-BY-NC-SA 4.0. Project documentation must preserve attribution and must not represent the source as unrestricted data. Any redistribution or external publication of source data requires separate license/use review.

## Assumptions

- The files present in `data/source/olist` are the files extracted by the Kaggle CLI acquisition step.
- The local files are treated as immutable source inputs for the profiling phase.

## Unknowns

- Actual physical schemas and data-quality characteristics have not yet been established in this artifact.
- Row-level profiling and relationship validation are deferred to subsequent Area 05 steps.

## Physical Modeling Boundary

No warehouse fact, dimension, staging, or analytical model is defined by this acquisition record. This artifact records source acquisition only.

## Artifact Completion Criteria

- [x] Source dataset identified
- [x] Acquisition method recorded
- [x] Local source path recorded
- [x] Acquisition validation recorded
- [x] Expected source file count recorded
- [x] Actual source file count captured from local directory
- [x] Local source size captured
- [x] Source preservation controls documented
- [x] License boundary documented
- [x] Area 05 profiling boundary preserved
