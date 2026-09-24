# Area 07.3.4 — Physical Schema Contract Validation

## Document Status

Status: Accepted & Frozen

## Purpose

Validate the Area 07.3.3 nullability and data-type contract against the frozen Area 05 physical schema evidence.

## Evidence Sources

- Area 05 physical-schema-inventory.md
- Area 05 data-profile.md
- Area 07.3.3 nullability-data-type-contract.md

## Validation Scope

The validation covers all nine source datasets.

Validation dimensions:

- Dataset representation
- Column representation
- Physical data type alignment
- Nullability alignment
- Key-role alignment
- Source-specific exceptions

## Dataset Validation Register

| Dataset | Area 05 Physical Evidence | 07.3.3 Contract | Validation Status |
|---|---|---|---|
| customers | Present | Present | Pending execution |
| geolocation | Present | Present | Pending execution |
| order_items | Present | Present | Pending execution |
| order_payments | Present | Present | Pending execution |
| order_reviews | Present | Present | Pending execution |
| orders | Present | Present | Pending execution |
| products | Present | Present | Pending execution |
| sellers | Present | Present | Pending execution |
| product_category_name_translation | Present | Present | Pending execution |

## Physical Data-Type Validation

The physical data types recorded in Area 05 are the authoritative source evidence.

The contract must not invent, silently convert, or overwrite the observed source types.

## Nullability Validation

Nullability must reflect the actual Area 05 profiling evidence.

Known nullable fields include documented operational timestamps, review text fields, and product attributes where nulls were physically observed.

## Key Validation

Primary and composite key roles must remain consistent with Area 06 relationship and cardinality evidence.

Review identity requires special treatment because review_id alone is not unique in the source data.

## Source-Specific Exceptions

The validation must preserve documented exceptions rather than normalize them away.

Examples include repeated review_id values, unmatched product-category translations, and geolocation one-to-many zip-prefix relationships.

## Acceptance Boundary

Area 07.3.4 is accepted only when the structural contract agrees with the frozen Area 05 physical evidence and documented Area 06 relationship evidence.

## Source Preservation Rule

Validation is observational only. Original source files must not be mutated.

## Next Step

Step 07.3.4.2 will execute the actual column-level validation against the Area 05 evidence.

## Artifact Completion Criteria

- All 9 datasets validated.
- Physical data types reconciled.
- Nullability reconciled.
- Key roles reconciled.
- Source-specific exceptions reconciled.
- No source data mutation.
- Validation evidence recorded.

