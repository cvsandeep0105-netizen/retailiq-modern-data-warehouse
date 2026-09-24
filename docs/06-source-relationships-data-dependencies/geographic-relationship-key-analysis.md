# Area 06.6 — Geographic Relationship Key Analysis

## Document Status
- Status: Draft — Evidence Captured
- Area: 06.6
- Purpose: Establish the physical relationship behavior of the geolocation ZIP-prefix key before downstream modeling decisions.
- Source: data/source/olist/olist_geolocation_dataset.csv",
",


## 1. Verified Physical Row Count

The geolocation source contains 1,001,163 physical data rows.

Independent verification:
- Pandas profiling result: 1,001,163 data rows
- Physical CSV line count including header: 1,000,164
- Physical CSV data rows excluding header: 1,001,163
- Canonical verified row count: 1,001,163

## 2. Geographic Key Profile

| Metric | Verified Result |
|---|---:|
| Total geolocation rows | 1,001,163 |
| Distinct ZIP prefixes | 19,015 |
| Duplicate ZIP-prefix rows | 981,148 |
| Maximum rows per ZIP prefix | 1,146 |
| ZIP prefixes with more than 1 row | 17,972 |
| ZIP prefixes with exactly 1 row | 1,043 |

## 3. Geographic Attribute Multiplicity

| Attribute behavior | Verified Result |
|---|---:|
| ZIP prefixes with multiple latitude values | 17,781 |
| ZIP prefixes with multiple longitude values | 17,780 |
| ZIP prefixes with multiple city values | 8,556 |
| ZIP prefixes with multiple state values | 8 |
| Maximum states represented by one ZIP prefix | 2 |

## 4. Relationship Interpretation

The geolocation ZIP-code prefix is not a unique source key.

The source contains substantial one-to-many behavior from a ZIP prefix to geolocation records. Most ZIP prefixes have multiple physical records, and many ZIP prefixes contain multiple latitude, longitude, or city values.

State multiplicity is much less common than coordinate and city multiplicity, but it is present. Eight ZIP prefixes contain multiple state values, with a maximum of two states represented by a single ZIP prefix.

Therefore, geolocation_zip_code_prefix must not be treated as a unique geolocation dimension key without an explicit downstream modeling strategy.

## 5. Source Preservation Rule

- Preserve all source geolocation records.
- Do not deduplicate the source based on ZIP prefix.
- Do not arbitrarily select one coordinate for a ZIP prefix.
- Do not collapse multiple cities into one city without a documented business rule.
- Do not overwrite source geographic attributes.
- Any downstream geographic dimension or bridge structure must explicitly account for ZIP-prefix multiplicity.

## 6. Engineering Decision Boundary

This analysis establishes physical source behavior only.

It does not yet define the final warehouse geography dimension, surrogate-key strategy, geographic aggregation rule, or BI semantic behavior.

Those decisions require downstream modeling analysis and must preserve the documented source multiplicity.

## 7. Assumptions

- The locally acquired CSV is the source artifact being profiled.
- The header is excluded when calculating physical data-row count.
- ZIP-prefix multiplicity is treated as an observed source characteristic rather than a data-quality error.

## 8. Unknowns

- The final analytical meaning of multiple geolocation records for one ZIP prefix is not yet established.
- A final rule for assigning a single geographic representation to customers or sellers has not yet been defined.
- The appropriate warehouse representation for one-to-many ZIP-prefix geography remains a downstream modeling decision.

## 9. Acceptance Evidence

- Geographic source row count independently verified: 1,001,163.
- ZIP-prefix uniqueness tested.
- ZIP-prefix multiplicity quantified.
- Coordinate multiplicity quantified.
- City multiplicity quantified.
- State multiplicity quantified.
- Source preservation boundary documented.

## Artifact Completion Criteria

- [x] Physical row count independently verified.
- [x] ZIP-prefix cardinality measured.
- [x] ZIP-prefix multiplicity measured.
- [x] Geographic attribute multiplicity measured.
- [x] Engineering interpretation documented.
- [x] Source preservation rule documented.
- [x] Modeling decision boundary documented.

## Document Control

- This artifact records observed source behavior.
- No source data was modified.
- No source rows were deleted.
- No geographic values were invented.
- Final warehouse modeling decisions remain outside this artifact.


