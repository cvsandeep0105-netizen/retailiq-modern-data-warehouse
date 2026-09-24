# Area 26.1 — Natural & Surrogate Key Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the foundation for natural keys, business identifiers, surrogate keys, key stability, and key-management boundaries across the RetailIQ dimensional model.

## 2. Area 25 Dependency
Key design shall preserve the business grains formally defined and frozen in Area 25.

## 3. Area 24 Dependency
Natural and surrogate key decisions shall support the dimensional modeling strategy established in Area 24.

## 4. Area 06 Dependency
Source relationship evidence, key uniqueness, composite keys, and documented exceptions from Area 06 shall constrain key design.

## 5. Area 07 Dependency
Source contract definitions shall establish the structural and data-type expectations for natural identifiers.

## 6. Area 19 Dependency
Transformation logic shall preserve identifier meaning and shall not silently redefine business identity.

## 7. Area 20 Dependency
Standardization shall produce consistent representations of identifiers without changing their business identity.

## 8. Area 21 Dependency
Deduplication and record resolution shall establish the approved identity boundary before analytical keys are assigned.

## 9. Area 22 Dependency
Key populations shall remain reconcilable between source, staging, intermediate, and dimensional representations.

## 10. Area 23 Dependency
Profiling evidence shall support uniqueness, nullability, cardinality, and stability assumptions for candidate natural keys.

## 11. Natural Key Definition
A natural key is a source or business identifier whose value has meaning within the originating business domain and can identify the corresponding business entity or event.

## 12. Surrogate Key Definition
A surrogate key is an analytical identifier generated independently of the source business identifier and used to provide stable dimensional references within the warehouse model.

## 13. Natural Key Preservation
Approved natural keys shall be retained as business-reference attributes even when surrogate keys are introduced, subject to security and governance requirements.

## 14. Customer Key Boundary
customer_id and customer_unique_id shall remain distinct source identifiers. The analytical customer identity shall not be inferred solely from naming; the selected business identity must remain explicitly documented.

## 15. Order Key Boundary
order_id is the documented natural business identifier for the order grain and shall remain traceable through all analytical layers.

## 16. Order Item Composite Key Boundary
Order-item identity shall respect the composite order_id and order_item_id boundary established in Area 06. order_item_id alone shall not be treated as globally unique.

## 17. Payment Composite Key Boundary
Payment identity shall respect order_id and payment_sequential. payment_sequential alone shall not be treated as a global payment identifier.

## 18. Review Key Boundary
review_id alone shall not be assumed to be globally unique because Area 06 documented repeated review_id values. The approved review identity boundary shall remain explicitly represented.

## 19. Product and Seller Keys
product_id and seller_id are source business identifiers for their respective entities and shall remain traceable when surrogate dimension keys are introduced.

## 20. Surrogate Key Purpose
Surrogate keys shall support dimensional joins, historical versioning, unknown-member handling, late-arriving dimensions, and warehouse-local identity without replacing business identifiers.

## 21. Key Stability
Surrogate keys shall remain stable within their defined analytical environment and shall not depend on mutable descriptive attributes.

## 22. Key Generation Boundary
Key-generation logic shall be deterministic or operationally controlled according to the target platform. Key generation shall prevent unintended collisions and shall be reproducible within the governed environment.

## 23. Unknown and Not-Applicable Keys
Dimensional models shall reserve governed representations for unknown, unavailable, and not-applicable dimension relationships rather than using arbitrary null handling that can break referential integrity.

## 24. Key Governance and Lineage
Every analytical key shall document its source natural key or business identity, generation rule, uniqueness expectation, historical behavior, lineage, reconciliation method, and downstream ownership.

## 25. Acceptance Criteria
Area 26.1 is acceptable when natural and surrogate key concepts are explicitly defined, major RetailIQ source identifiers and composite-key boundaries are documented, key stability and generation controls are established, and the design remains traceable to Areas 06, 07, 19–25.

