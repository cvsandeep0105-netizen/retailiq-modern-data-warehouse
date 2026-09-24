# Area 25.1 — Business Grain Definition Foundation

Status: Accepted & Frozen

## 1. Purpose
Define the formal business-grain framework for RetailIQ so every fact, dimension, measure, relationship, and analytical output has an explicit and defensible level of detail.

## 2. Area 03 Business Process Dependency
Business grain definitions shall originate from the documented business processes and analytical questions established in Area 03.

## 3. Area 06 Relationship Dependency
Grain definitions shall respect the source relationships, cardinalities, composite keys, and documented relationship exceptions established in Area 06.

## 4. Area 07 Contract Dependency
Grain definitions shall remain traceable to source contracts, schema expectations, identifiers, data types, and nullability established in Area 07.

## 5. Area 19 Transformation Dependency
Grain definitions shall preserve the business meaning of approved transformations established in Area 19.

## 6. Area 20 Standardization Dependency
Grain definitions shall use approved standardized identifiers, values, dates, numeric representations, and categorical meanings established in Area 20.

## 7. Area 21 Deduplication Dependency
Grain definitions shall account for duplicate detection, record identity, survivorship, and non-merge outcomes established in Area 21.

## 8. Area 22 Reconciliation Dependency
Grain definitions shall remain measurable and reconcilable using the control totals, mappings, and exception controls established in Area 22.

## 9. Area 23 Profiling Dependency
Grain decisions shall use profiling evidence concerning uniqueness, multiplicity, distributions, completeness, and entity relationships established in Area 23.

## 10. Area 24 Dimensional Strategy Dependency
Business grain shall be the primary design constraint for the fact and dimension strategy established in Area 24.

## 11. Definition of Business Grain
Business grain is the precise statement of what one row represents within an analytical entity, fact, dimension, snapshot, event, or derived dataset.

## 12. Grain-First Rule
No physical fact or analytical model shall be implemented until its business grain is explicitly documented and approved.

## 13. Order Grain
Order grain represents one customer order per row. Order-level measures shall be calculated and stored only at this grain unless an explicit downstream aggregation is defined.

## 14. Order Item Grain
Order-item grain represents one item line within one customer order, identified by the approved order_id and order_item_id combination.

## 15. Payment Grain
Payment grain represents one payment record or payment sequence associated with an order at its explicitly defined payment grain. Multiple payment records per order must remain supported.

## 16. Review Grain
Review grain represents one approved review business record at the documented review identity boundary. review_id alone shall not be assumed to define uniqueness because Area 06 established repeated review_id behavior.

## 17. Product and Seller Grain
Product and seller dimensions shall represent one analytical entity per row at their respective entity grains, subject to the historical strategy defined by the dimensional model.

## 18. Customer Grain
Customer grain shall explicitly distinguish the operational customer_id from customer_unique_id and shall document which identifier defines the analytical entity.

## 19. Date and Geography Grain
Reusable Date and Geography dimensions shall each have explicit row-level grain and shall not be duplicated unnecessarily for different analytical roles.

## 20. Measure Grain Alignment
Every measure shall be defined at the same grain as its fact or have an explicit aggregation path. Measures shall not be repeated across a finer-grain join without controlled aggregation.

## 21. Multi-Grain Interaction
Order, order-item, payment, and review populations shall not be directly combined as though they share the same grain. Cross-grain analysis shall use controlled aggregation or appropriate fact structures.

## 22. Grain and Double-Counting Control
Any join or aggregation that can multiply rows shall be identified and controlled before analytical consumption. Grain compatibility shall be validated before measures are combined.

## 23. Grain Documentation and Lineage
Each grain definition shall document its business process, row meaning, identifying attributes, source lineage, transformation dependencies, measure implications, and reconciliation controls.

## 24. Technology-Neutral Boundary
This foundation defines business-grain requirements independently of a specific warehouse, database, SQL engine, cloud provider, orchestration platform, or BI product.

## 25. Acceptance Criteria
Area 25.1 is acceptable when business grain is explicitly defined for major RetailIQ entities and analytical processes, grain-first rules are established, multi-grain and double-counting risks are controlled, and all definitions are traceable to frozen Areas 03, 06, 07, 19–24.

