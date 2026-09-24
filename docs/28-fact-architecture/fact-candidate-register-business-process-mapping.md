# Area 28.2 — Fact Candidate Register & Business Process Mapping

Status: Accepted & Frozen

## 1. Purpose
Create the formal RetailIQ fact candidate register and map each candidate fact to its business process, declared grain, source entities, event identity, dimensions, measures, and analytical responsibilities.

## 2. Area 28.1 Dependency
The fact register operationalizes the fact architecture foundation established in Area 28.1.

## 3. Area 24 Dependency
Fact candidates shall follow the dimensional modeling strategy and fact-design patterns established in Area 24.

## 4. Area 25 Dependency
Every fact candidate shall have an explicit and immutable business grain defined in Area 25.

## 5. Area 26 Dependency
Fact identities and dimension references shall follow the approved natural-key and surrogate-key strategy.

## 6. Area 27 Dependency
Fact candidates shall map to the approved conformed dimensions and role-playing relationships.

## 7. Area 03 Dependency
Each fact candidate shall support one or more documented business processes and analytical questions.

## 8. Area 06 Dependency
Source relationships, composite identifiers, cardinalities, and multiplicity shall constrain fact design.

## 9. Area 07 Dependency
Source identifiers, measures, timestamps, and structural attributes shall remain traceable to frozen source contracts.

## 10. Area 19 Dependency
Fact mappings shall preserve approved transformation semantics and business meaning.

## 11. Area 20 Dependency
Fact attributes and measures shall use standardized and normalized representations.

## 12. Area 21 Dependency
Fact populations shall use approved record-resolution outcomes without collapsing legitimate repeated business events.

## 13. Area 22 Dependency
Each fact candidate shall have defined reconciliation paths to upstream populations and control totals.

## 14. Area 23 Dependency
Profiling evidence shall support the documented fact grain, multiplicity, completeness, and measure assumptions.

## 15. Order Fact Register Entry
Order fact candidate: one customer order per row. Natural event identity is order_id. Candidate dimensions include customer and applicable date roles. Candidate measures shall remain strictly order-grain measures.

## 16. Order Item Fact Register Entry
Order-item fact candidate: one item line within one order per row. Natural event identity is the composite order_id and order_item_id. Candidate dimensions include customer, product, seller, and applicable dates. Price and freight are item-grain measures.

## 17. Payment Fact Register Entry
Payment fact candidate: one payment sequence associated with an order per row. Natural event identity is order_id plus payment_sequential. Payment value and payment-specific attributes remain at payment grain.

## 18. Review Fact Register Entry
Review fact candidate: one approved review business record per row at its documented review identity boundary. Candidate dimensions include customer and applicable date roles. Review score and review-event attributes remain at review grain.

## 19. Business Process Mapping
Order management maps to the order fact; merchandise and fulfillment line activity maps to the order-item fact; payment processing maps to the payment fact; customer feedback maps to the review fact.

## 20. Fact-to-Dimension Mapping
Each fact candidate shall identify its customer, product, seller, date, geography, and other applicable dimension relationships without introducing dimensions that violate fact grain.

## 21. Measure Register Boundary
Each candidate measure shall have a declared fact owner, source attribute, business definition, data type, unit or currency where applicable, additivity classification, and aggregation rule.

## 22. Event Timestamp Boundary
Each event timestamp shall remain associated with the business event that generated it. Multiple timestamp roles shall use explicit Date dimension role names.

## 23. Cross-Fact Boundary
Facts shall remain independent at their declared grains. Cross-fact analysis shall use conformed dimensions and controlled aggregation rather than direct measure-multiplying joins.

## 24. Register Governance
Any change to a fact candidate, grain, measure ownership, source mapping, dimension relationship, or business-process assignment shall require documented rationale, dependency review, reconciliation evidence, and controlled approval.

## 25. Acceptance Criteria
Area 28.2 is acceptable when order, order-item, payment, and review fact candidates are formally registered and mapped to business processes, grains, keys, dimensions, measures, timestamps, and reconciliation boundaries, with dependencies on Areas 03, 06, 07, 19–27 and 28.1 preserved.

