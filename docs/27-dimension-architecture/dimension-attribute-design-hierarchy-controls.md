# Area 27.3 — Dimension Attribute Design & Hierarchy Controls

Status: Accepted & Frozen

## 1. Purpose
Define dimensional attribute design, hierarchy, descriptive semantics, drill-down paths, attribute ownership, and analytical usability controls for RetailIQ.

## 2. Area 27.1 Dependency
Attribute and hierarchy design shall implement the approved dimension architecture foundation.

## 3. Area 27.2 Dependency
All dimensional attributes shall originate from the approved candidate register and source-to-business mappings.

## 4. Area 24 Dependency
Attribute and hierarchy design shall follow the dimensional patterns established in Area 24.

## 5. Area 25 Dependency
Attributes shall remain aligned with the declared business grain of each dimension.

## 6. Area 26 Dependency
Dimension identifiers shall use the approved natural and surrogate key strategy.

## 7. Area 19 Dependency
Transformed attributes shall preserve source business meaning.

## 8. Area 20 Dependency
Attribute values shall use approved standardized and normalized representations.

## 9. Area 21 Dependency
Dimension attributes shall reflect approved record-resolution and survivorship outcomes.

## 10. Area 22 Dependency
Dimension attribute populations shall remain reconcilable to upstream populations.

## 11. Area 23 Dependency
Profiling evidence shall guide completeness, cardinality, domain, and distribution expectations for dimensional attributes.

## 12. Customer Attribute Design
Customer attributes shall support analytical segmentation by approved customer identity and location characteristics. Descriptive attributes shall remain at customer grain and shall not contain order-level or transaction-level measures.

## 13. Product Attribute Design
Product attributes shall support category, translated category, physical characteristics, descriptive metadata, and other approved product-level analytical groupings while remaining at product grain.

## 14. Seller Attribute Design
Seller attributes shall support seller identity and approved geographic descriptors while remaining at seller grain.

## 15. Date Attribute Design
Date attributes shall support year, quarter, month, week, day, weekday, and other governed calendar classifications needed for time-based analysis.

## 16. Geography Attribute Design
Geographic attributes shall use an explicit hierarchy where supported, such as state, city, and governed postal-code representation. Source postal-code observations shall not be treated as unique geographic entities without evidence.

## 17. Hierarchy Definition
A hierarchy is an ordered analytical path from a broader dimensional level to a more detailed level. Each hierarchy shall have explicit levels, keys, relationship assumptions, and aggregation behavior.

## 18. Customer Geography Hierarchy
Customer geography may support governed state-to-city-to-postal representation where the source data and business semantics support that hierarchy. Ambiguous postal-code relationships shall remain explicitly controlled.

## 19. Seller Geography Hierarchy
Seller geography may support governed state-to-city-to-postal representation, subject to the source relationship and uniqueness boundaries already established.

## 20. Product Category Hierarchy
Product category analysis shall distinguish source category values from translated English category values. Unmatched translations shall remain traceable exceptions and shall not be silently invented.

## 21. Attribute Naming and Semantic Consistency
Attribute names shall communicate business meaning consistently across dimensions. Equivalent concepts shall use consistent terminology and shall not be duplicated under conflicting semantic definitions.

## 22. Drill-Down and Roll-Up Controls
Every hierarchy shall define valid drill-down and roll-up paths. Analytical users shall not aggregate across a hierarchy level unless the relationship supports the intended interpretation.

## 23. Derived and Display Attributes
Derived calendar labels, categories, flags, and display attributes shall have documented derivation rules and shall not replace the underlying governed business attributes.

## 24. Attribute Quality, Lineage and Governance
Each dimensional attribute shall have documented source lineage, transformation logic, standardization behavior, null handling, quality expectations, ownership, and change-control requirements.

## 25. Acceptance Criteria
Area 27.3 is acceptable when customer, product, seller, date, and geography attributes have explicit design rules; valid hierarchies and drill-down paths are defined; product category translation boundaries are preserved; and attribute semantics remain aligned with Areas 19–26 and 27.1–27.2.

