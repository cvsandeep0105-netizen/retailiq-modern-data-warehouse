# Area 06.7 — Customer/Seller Geolocation Dependency Analysis

## Document Status
- Status: Draft — Evidence Captured
- Area: 06.7
- Purpose: Establish ZIP-prefix coverage and multiplicity between customer/seller source records and the geolocation source.
- Sources: customers, sellers, geolocation

## 1. Customer ZIP Coverage

| Metric | Verified Result |
|---|---:|
| Distinct customer ZIP prefixes | 14,994 |
| Customer ZIP prefixes found in geolocation | 14,837 |
| Customer ZIP prefixes missing from geolocation | 157 |
| Customer ZIP coverage | 98.9529% |

## 2. Seller ZIP Coverage

| Metric | Verified Result |
|---|---:|
| Distinct seller ZIP prefixes | 2,246 |
| Seller ZIP prefixes found in geolocation | 2,239 |
| Seller ZIP prefixes missing from geolocation | 7 |
| Seller ZIP coverage | 99.6883% |

## 3. Customer ZIP → Geolocation Multiplicity

| Metric | Verified Result |
|---|---:|
| Customer ZIP prefixes represented in geolocation | 14,837 |
| Maximum geolocation rows for a customer ZIP | 1,146 |
| Customer ZIPs with more than 1 geolocation row | 14,715 |
| Customer ZIPs with exactly 1 geolocation row | 122 |

## 4. Seller ZIP → Geolocation Multiplicity

| Metric | Verified Result |
|---|---:|
| Seller ZIP prefixes represented in geolocation | 2,239 |
| Maximum geolocation rows for a seller ZIP | 965 |
| Seller ZIPs with more than 1 geolocation row | 2,230 |
| Seller ZIPs with exactly 1 geolocation row | 9 |

## 5. Relationship Interpretation

Customer ZIP prefixes do not have complete coverage in the geolocation source. Of 14,994 distinct customer ZIP prefixes, 157 are not represented in geolocation.

Seller ZIP prefixes also do not have complete coverage. Of 2,246 distinct seller ZIP prefixes, 7 are not represented in geolocation.

For ZIP prefixes that are represented, the relationship is strongly one-to-many. Customer ZIP prefixes can map to as many as 1,146 geolocation rows, while seller ZIP prefixes can map to as many as 965 geolocation rows.

Therefore, neither customer ZIP prefix nor seller ZIP prefix may be treated as a unique geolocation key.

## 6. Engineering Implications

- Geographic enrichment must account for one-to-many ZIP-prefix relationships.
- Missing customer ZIP prefixes must remain visible as an explicit coverage exception.
- Missing seller ZIP prefixes must remain visible as an explicit coverage exception.
- Downstream enrichment must not silently duplicate customer or seller records through uncontrolled geolocation joins.
- A final geographic representation requires an explicit downstream modeling strategy.
- Source geolocation records must not be arbitrarily collapsed to one row per ZIP prefix.

## 7. Source Preservation Rule

- Preserve all source customer records.
- Preserve all source seller records.
- Preserve all source geolocation records.
- Do not invent geographic mappings for missing ZIP prefixes.
- Do not select an arbitrary geolocation row solely to force one-to-one cardinality.
- Do not silently discard geolocation multiplicity.

## 8. Assumptions

- ZIP-prefix values are compared using their observed numeric representation.
- Coverage is measured at the distinct ZIP-prefix level.
- Multiplicity is measured using physical geolocation rows associated with represented ZIP prefixes.

## 9. Unknowns

- The correct analytical geographic assignment for a ZIP prefix with multiple geolocation records is not yet defined.
- The treatment of the 157 missing customer ZIP prefixes remains a downstream modeling decision.
- The treatment of the 7 missing seller ZIP prefixes remains a downstream modeling decision.
- The appropriate geographic grain for BI reporting remains outside this analysis.

## 10. Modeling Boundary

This artifact establishes source relationship behavior only.

It does not define the final dimension structure, surrogate-key strategy, bridge design, geographic aggregation logic, or BI semantic-layer behavior.

Those decisions must be addressed during the dimensional modeling and warehouse design phases.

## 11. Acceptance Evidence

- Customer ZIP coverage measured.
- Seller ZIP coverage measured.
- Customer ZIP multiplicity measured.
- Seller ZIP multiplicity measured.
- Missing customer ZIP coverage quantified.
- Missing seller ZIP coverage quantified.
- One-to-many geographic relationship documented.

## Artifact Completion Criteria

- [x] Customer ZIP coverage measured.
- [x] Seller ZIP coverage measured.
- [x] Customer ZIP multiplicity measured.
- [x] Seller ZIP multiplicity measured.
- [x] Missing ZIP prefixes quantified.
- [x] One-to-many relationship documented.
- [x] Source preservation rule documented.
- [x] Modeling boundary documented.

## Document Control

- No source data was modified.
- No source rows were deleted.
- No geographic mappings were invented.
- No one-to-many geolocation relationships were collapsed.
