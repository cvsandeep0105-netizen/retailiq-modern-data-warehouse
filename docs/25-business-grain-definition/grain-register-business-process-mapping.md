# Area 25.2 — Grain Register & Business Process Mapping

Status: Accepted & Frozen

## 1. Purpose
Create the formal RetailIQ grain register and map each analytical grain to its business process, source entities, identifying attributes, dimensional role, and downstream analytical use.

## 2. Area 25.1 Dependency
This register operationalizes the grain-first foundation defined in Area 25.1.

## 3. Area 03 Dependency
Business-process mapping shall use the analytical processes and questions established in Area 03.

## 4. Area 06 Dependency
Source relationships, cardinalities, composite keys, and relationship exceptions from Area 06 shall constrain every grain definition.

## 5. Area 07 Dependency
Source contracts and schema expectations from Area 07 shall provide the structural boundary for grain identifiers.

## 6. Area 18 Dependency
Staging-layer structures shall provide the controlled source-to-staging boundary for grain mapping.

## 7. Area 19 Dependency
Approved staging transformations shall preserve the documented business meaning of each grain.

## 8. Area 20 Dependency
Standardized and normalized attributes shall be used when defining analytical grain identifiers.

## 9. Area 21 Dependency
Deduplication and record-resolution rules shall determine which records are eligible for analytical grain representation.

## 10. Area 22 Dependency
Reconciliation controls shall support validation of row counts, keys, and measures at each registered grain.

## 11. Area 23 Dependency
Profiling evidence shall inform uniqueness, multiplicity, nullability, and distribution expectations for registered grains.

## 12. Area 24 Dependency
Dimensional modeling strategy shall determine how registered grains participate in fact and dimension architecture.

## 13. Customer Grain Register Entry
Customer grain: one analytical customer entity per row. Candidate identifying attributes include customer_unique_id and customer_id, with the final analytical identifier governed by the approved dimensional key strategy.

## 14. Order Grain Register Entry
Order grain: one customer order per row, identified by order_id. Order-level measures must not be multiplied by item, payment, or review joins.

## 15. Order Item Grain Register Entry
Order-item grain: one item line within an order per row, identified by the composite order_id and order_item_id boundary established in Area 06.

## 16. Payment Grain Register Entry
Payment grain: one payment sequence associated with an order per row, identified by order_id and payment_sequential. Multiple payments for an order must remain independently represented.

## 17. Review Grain Register Entry
Review grain: one review business record per row at the documented review identity boundary. review_id alone shall not be treated as a universally unique analytical key.

## 18. Product Grain Register Entry
Product grain: one product entity per row identified by product_id, subject to historical and dimensional treatment defined by later modeling areas.

## 19. Seller Grain Register Entry
Seller grain: one seller entity per row identified by seller_id, subject to historical and dimensional treatment defined by later modeling areas.

## 20. Date and Geography Register Entries
Date grain shall represent one calendar date per row. Geography grain shall represent the approved geographic entity level and shall not collapse source geolocation observations without an explicit business rule.

## 21. Business Process Mapping
Customer management maps primarily to customer grain; order management maps to order grain; fulfillment and merchandise activity map to order-item grain; payment activity maps to payment grain; customer feedback maps to review grain.

## 22. Grain Compatibility Matrix
Compatible joins shall be defined through declared keys and controlled aggregation. Incompatible direct combinations, particularly order-to-payment, order-to-review, and order-to-item measure joins, require explicit aggregation or separate fact treatment.

## 23. Grain Validation Controls
Every register entry shall have an explicit row meaning, business process, identifier, source lineage, expected multiplicity, aggregation behavior, and reconciliation method.

## 24. Grain Register Governance
Changes to a registered grain shall require documented business justification, impact assessment, dependency review, reconciliation evidence, and controlled approval. Existing frozen grain definitions shall not be silently modified.

## 25. Acceptance Criteria
Area 25.2 is acceptable when all major RetailIQ analytical grains are registered, mapped to business processes and source boundaries, associated with explicit identifiers and multiplicity rules, protected against double counting, and traceable to Areas 03, 06, 07, 18–24.

