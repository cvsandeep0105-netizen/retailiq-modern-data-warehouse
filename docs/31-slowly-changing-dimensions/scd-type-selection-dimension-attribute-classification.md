# Area 31.2 — SCD Type Selection & Dimension Attribute Classification

Status: Accepted & Frozen

## 1. Purpose
Define the SCD type-selection framework and classify RetailIQ dimension attributes according to their historical significance, change behavior, analytical purpose, and preservation requirements.

## 2. Area 31.1 Dependency
SCD type selection shall implement the foundation established in Area 31.1.

## 3. Area 30 Dependency
SCD decisions shall remain compatible with conformed and role-playing dimension architecture.

## 4. Area 29 Dependency
Historical dimension behavior shall preserve fact-grain and measure interpretation.

## 5. Area 28 Dependency
SCD behavior shall remain compatible with frozen fact relationships and analytical joins.

## 6. Area 27 Dependency
Attribute classification shall extend the approved dimension architecture and attribute ownership.

## 7. Area 26 Dependency
SCD versions shall use the approved natural-key and surrogate-key strategy.

## 8. Area 25 Dependency
Attribute changes shall not alter the declared business grain of the dimension or consuming facts.

## 9. Area 24 Dependency
SCD type selection shall follow approved dimensional modeling patterns.

## 10. Area 23 Dependency
Observed profiling evidence shall inform attribute stability, nullability, and change-detection expectations.

## 11. Area 22 Dependency
Historical dimension populations shall remain reconcilable to upstream source populations.

## 12. Area 21 Dependency
Duplicate and record-resolution controls shall precede SCD version creation.

## 13. Area 20 Dependency
Attribute standardization shall occur before change detection to prevent representation-only changes from becoming false historical changes.

## 14. Area 19 Dependency
Attribute transformation shall preserve business meaning before SCD comparison.

## 15. Area 07 Dependency
Attribute classification shall remain traceable to frozen source contracts and physical schemas.

## 16. SCD Type 1 Boundary
SCD Type 1 shall be used where only the current attribute state is analytically required and historical changes do not need to be preserved for the attribute's business purpose.

## 17. SCD Type 2 Boundary
SCD Type 2 shall be used where historical attribute states materially affect analysis and historical facts must retain the dimension context that existed during the relevant period.

## 18. SCD Type 0 Boundary
SCD Type 0 shall apply only to attributes whose values are intended to remain fixed after initial establishment, subject to explicit business justification.

## 19. Type Selection Principle
SCD type shall be selected per attribute rather than automatically per dimension. One dimension may legitimately contain attributes with different historical behaviors.

## 20. Customer Attribute Classification
Customer identity attributes shall preserve governed entity identity. Customer descriptive or geographic attributes shall be evaluated individually for historical significance, with historical customer context preserved where required by analytical use cases.

## 21. Product Attribute Classification
Product identity attributes shall remain stable business identifiers. Product descriptive and category-related attributes shall be evaluated for whether historical product classification or description changes need analytical preservation.

## 22. Seller Attribute Classification
Seller identity shall remain stable through the natural-key boundary. Seller descriptive and geographic attributes shall be evaluated for historical significance and analytical requirements.

## 23. Geography Attribute Classification
Geographic attributes shall be classified according to whether historical location meaning must be preserved. Source ambiguity shall not be converted into artificial historical changes.

## 24. Change Detection and Governance Controls
Change detection shall compare standardized, governed attributes using the approved natural key. Every SCD classification shall document business rationale, selected SCD behavior, affected attributes, source lineage, effective dating expectations, reconciliation requirements, and change-control ownership.

## 25. Acceptance Criteria
Area 31.2 is acceptable when SCD Type 0, Type 1, and Type 2 boundaries are defined; selection is attribute-specific; customer, product, seller, and geography attributes have classification principles; standardized change detection is governed; and dependencies from Areas 07, 19–30 and 31.1 are preserved.

