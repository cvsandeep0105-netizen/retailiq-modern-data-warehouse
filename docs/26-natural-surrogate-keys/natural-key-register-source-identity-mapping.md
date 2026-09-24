# Area 26.2 — Natural Key Register & Source Identity Mapping

Status: Accepted & Frozen

## 1. Purpose
Create the formal natural-key register for RetailIQ and map each approved source identifier to its business entity, business grain, source object, uniqueness boundary, and downstream analytical role.

## 2. Area 26.1 Dependency
The register operationalizes the natural-key and surrogate-key foundation defined in Area 26.1.

## 3. Area 25 Dependency
Every natural key shall correspond to a documented business grain established in Area 25.

## 4. Area 06 Dependency
Source key uniqueness, composite-key boundaries, relationship cardinality, and known key exceptions from Area 06 shall be preserved.

## 5. Area 07 Dependency
Natural-key data types, nullability, structural expectations, and source contract definitions shall remain aligned with Area 07.

## 6. Area 19 Dependency
Transformation logic shall preserve the semantic identity of registered natural keys.

## 7. Area 20 Dependency
Identifier standardization shall normalize representation without changing the underlying business identity.

## 8. Area 21 Dependency
Natural-key registration shall use the approved record-identity and deduplication boundaries.

## 9. Area 22 Dependency
Natural-key populations shall remain reconcilable through source-to-target key counts and exception controls.

## 10. Area 23 Dependency
Profiling evidence shall support documented uniqueness, nullability, and multiplicity expectations.

## 11. Customer Natural-Key Mapping
customer_id is a source customer identifier and shall remain traceable. customer_unique_id is a distinct source identifier and shall not be silently substituted for customer_id without an explicit business-identity decision.

## 12. Order Natural-Key Mapping
order_id is the registered natural identifier for the order grain and shall be preserved across analytical transformations.

## 13. Order-Item Natural-Key Mapping
The order-item natural identity is the composite of order_id and order_item_id. The composite boundary shall remain intact throughout analytical processing.

## 14. Payment Natural-Key Mapping
The payment natural identity is the composite of order_id and payment_sequential. The sequential value alone is not a global identifier.

## 15. Review Natural-Key Mapping
Review identity shall follow the approved Area 06 boundary because repeated review_id values exist. review_id alone shall not be registered as a globally unique natural key.

## 16. Product Natural-Key Mapping
product_id is the registered source natural identifier for the product entity.

## 17. Seller Natural-Key Mapping
seller_id is the registered source natural identifier for the seller entity.

## 18. Category Natural-Key Mapping
product_category_name is the source category identifier used for category translation mapping. Unmatched translation values shall remain explicit exceptions.

## 19. Geographic Identifier Mapping
geolocation_zip_code_prefix and seller/customer zip-code prefixes shall retain their source meaning and shall not automatically be treated as unique geographic entities.

## 20. Natural-Key Uniqueness Boundary
Uniqueness shall be evaluated within the documented entity or composite-key boundary. A value that is unique in one source object shall not automatically be assumed globally unique.

## 21. Natural-Key Nullability Boundary
Required natural identifiers shall not be replaced with fabricated values. Missing identifiers shall be handled through documented exception and data-quality controls.

## 22. Source-to-Analytical Traceability
Every registered natural key shall have a traceable path from source object and source column through staging and transformations into its analytical representation.

## 23. Key Change and Drift Control
Changes to source identifier format, domain, uniqueness, or nullability shall be detected and assessed before altering analytical key behavior.

## 24. Register Governance
The natural-key register shall be version-controlled and changes shall require documented rationale, dependency impact analysis, reconciliation evidence, and controlled approval.

## 25. Acceptance Criteria
Area 26.2 is acceptable when all major RetailIQ natural identifiers and composite-key boundaries are registered, mapped to source identity and business grain, uniqueness and nullability expectations are documented, and traceability is established against Areas 06, 07, 19–25.

