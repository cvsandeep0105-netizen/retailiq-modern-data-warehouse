# Area 24.2 — Business Process & Fact/Dimension Candidate Mapping

Status: Accepted & Frozen

## 1. Purpose
Map approved RetailIQ business processes to candidate analytical facts and dimensions before physical dimensional implementation.

## 2. Area 24.1 Strategy Dependency
Candidate mappings shall follow the grain-first dimensional modeling strategy established in Area 24.1.

## 3. Area 03 Business Process Dependency
Candidate facts shall originate from the business processes and analytical questions documented in Area 03.

## 4. Area 06 Relationship Dependency
Candidate relationships shall respect the source relationship and cardinality evidence established in Area 06.

## 5. Area 07 Contract Dependency
Candidate entities shall remain traceable to the approved source contracts and schemas established in Area 07.

## 6. Area 18 Staging Dependency
Candidate analytical structures shall consume approved staging boundaries established in Area 18.

## 7. Area 19 Transformation Dependency
Candidate structures shall preserve approved transformation meaning established in Area 19.

## 8. Area 20 Standardization Dependency
Candidate attributes and measures shall use standardized representations established in Area 20.

## 9. Area 21 Deduplication Dependency
Candidate populations shall respect duplicate and record-resolution outcomes established in Area 21.

## 10. Area 22 Reconciliation Dependency
Candidate fact and dimension populations shall remain reconcilable using Area 22 controls.

## 11. Area 23 Profiling Dependency
Candidate structures shall use profiling evidence to identify completeness, uniqueness, validity, distribution, and business-grain considerations.

## 12. Customer Business Process
Customer analysis shall use a customer-oriented dimension candidate while preserving customer_id and customer_unique_id distinctions established in the source evidence.

## 13. Order Business Process
Order analysis shall use an order-oriented fact candidate at an explicitly declared order grain and shall not mix order-level and item-level measures.

## 14. Order Item Business Process
Order-item analysis shall use a candidate fact at the order-item grain with product, seller, customer/order context, and applicable measures.

## 15. Payment Business Process
Payment analysis shall use a payment-oriented candidate fact because multiple payment records can exist for one order.

## 16. Review Business Process
Review analysis shall preserve the documented review identity boundary and support review-level analytical measures without assuming review_id alone is unique.

## 17. Product and Seller Entities
Product and seller entities shall be modeled as candidate descriptive dimensions where their attributes provide reusable analytical context.

## 18. Date and Time Entity
A reusable date dimension candidate shall support consistent temporal analysis across order, payment, review, delivery, and other applicable business events.

## 19. Geography Entity
Geographical attributes shall be evaluated as dimension candidates while preserving the documented geolocation repetition and source boundaries.

## 20. Fact Candidate Classification
Candidate facts shall be classified as transaction/event facts, periodic snapshots, or other documented analytical fact types only when their grain and business process justify the classification.

## 21. Dimension Candidate Classification
Candidate dimensions shall provide descriptive context and shall be evaluated for reuse across multiple business processes.

## 22. Measure Candidate Classification
Measures shall be classified as additive, semi-additive, or non-additive according to their business behavior and declared grain.

## 23. Business Grain and Double-Counting Control
No candidate mapping shall permit combining order, order-item, payment, or review populations without explicit grain alignment and aggregation controls.

## 24. Technology-Neutral Boundary
This candidate mapping defines logical analytical structures without prescribing a physical warehouse implementation, SQL engine, cloud platform, or BI product.

## 25. Acceptance Criteria
Area 24.2 is acceptable when business processes are mapped to candidate facts, dimensions, dates, geography, and measures; grain and double-counting controls are explicit; and all mappings remain traceable to frozen Areas 03, 06, 07, 18–23 and Area 24.1.

