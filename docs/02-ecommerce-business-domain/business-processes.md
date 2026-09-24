# RetailIQ — Business Processes

## Document Status

- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Area: 02 — E-Commerce Business Domain
- Artifact: Business Processes
- Status: Draft
- Purpose: Define the major e-commerce business processes, their sequence, participating entities, analytical relevance, business grain, dependencies, assumptions, and source-verification requirements.

## 1. Business Process Purpose

Business processes describe how business activity occurs across the RetailIQ e-commerce domain. They provide the operational and analytical context required before defining business events, warehouse facts, dimensions, transformations, and metrics.

Business processes in this document are conceptual. They do not represent physical database procedures, SQL models, orchestration jobs, or warehouse tables.

## 2. Process Identification Principles

A business process is identified by a meaningful business activity that involves one or more business entities and produces an operational outcome, state change, measurable activity, or analytical observation.

Each process is evaluated according to its business purpose, participating entities, sequence, expected grain, analytical relevance, dependencies, and source-verification requirements.

## 3. Customer Acquisition and Registration

### Business Meaning
This process represents the creation or establishment of a customer relationship with the e-commerce platform.

### Participating Entities
- Customer
- Geography, where available

### Process Flow
1. A customer enters the platform or marketplace.
2. Customer information is established in the source system.
3. A customer identifier is assigned or maintained.
4. Customer attributes may be associated with geographic information.

### Analytical Relevance
This process can support customer acquisition, customer population, geographic distribution, and customer lifecycle analysis when the source contains the necessary information.

### Expected Process Grain
One customer registration or customer establishment event, if such events are available.

### Source Verification
Verify whether the source contains registration timestamps, customer creation events, or only customer master records.

## 4. Product Discovery and Availability

### Business Meaning
This process represents products being available for discovery and purchase through the e-commerce platform.

### Participating Entities
- Product
- Product Category
- Seller

### Process Flow
1. A product or listing is available through the marketplace.
2. Product attributes and category information are associated with the product.
3. Seller information may be associated with the product or listing.
4. Customers may subsequently purchase the product.

### Analytical Relevance
Product discovery and availability provide context for product assortment, category distribution, seller participation, and product performance.

### Expected Process Grain
One product or product-listing availability record, if source data supports this concept.

### Source Verification
Verify whether the source represents product listings, product master data, seller-product relationships, inventory, or only products appearing in transactions.

## 5. Purchase Intent and Cart Activity

### Business Meaning
This process represents customer purchase intent before an order is formally created.

### Participating Entities
- Customer
- Product
- Seller

### Process Flow
1. A customer identifies one or more products.
2. Products may be selected for potential purchase.
3. Purchase intent may progress toward order placement.

### Analytical Relevance
Cart or pre-order behavior can support conversion analysis and customer behavior analysis if source events are available.

### Expected Process Grain
One customer-product interaction or cart event, if explicitly available in the source.

### Source Verification
Verify whether cart, browsing, clickstream, wishlist, or other pre-order events exist. If unavailable, this process remains a conceptual domain process and must not be fabricated in the warehouse.

## 6. Order Placement

### Business Meaning
Order placement represents the creation of a customer order for one or more products.

### Participating Entities
- Customer
- Order
- Order Item
- Product
- Seller

### Process Flow
1. A customer initiates a purchase.
2. One or more products become order items.
3. An order is created.
4. The order receives an identifier and lifecycle status.
5. Order-level and item-level attributes are recorded.

### Analytical Relevance
Order placement is central to sales volume, order count, customer activity, product performance, seller performance, and revenue-related analysis.

### Expected Process Grain
At order level: one business order.
At item level: one product line within an order.

### Source Verification
Verify order identifiers, customer relationships, order timestamps, item cardinality, status values, product relationships, seller relationships, and pricing fields.

## 7. Order Item Processing

### Business Meaning
Order item processing represents the detailed handling of each product line contained within an order.

### Participating Entities
- Order
- Order Item
- Product
- Seller

### Process Flow
1. An order contains one or more order items.
2. Each item references a product.
3. Seller information may be associated with the item.
4. Quantity, price, freight, or other item-level measures may be recorded.

### Analytical Relevance
This process provides the detailed transaction grain needed for units sold, item revenue, product performance, seller performance, and basket analysis.

### Expected Process Grain
One order item or order line.

### Source Verification
Verify item sequence, product identifier, seller identifier, quantity, price, freight value, and duplicate behavior.

## 8. Payment Processing

### Business Meaning
Payment processing represents the recording or application of payment information associated with an order.

### Participating Entities
- Order
- Payment

### Process Flow
1. An order is associated with one or more payment records where supported.
2. Payment method and monetary value are recorded.
3. Installment information may be recorded.
4. Payment information can be reconciled against order activity where source semantics permit.

### Analytical Relevance
Payment analysis supports payment-method distribution, payment value, installment behavior, transaction analysis, and reconciliation.

### Expected Process Grain
One payment record or payment event.

### Source Verification
Verify payment cardinality, payment type domain, payment value, installments, payment identifiers, and relationship to orders.

## 9. Order Fulfillment

### Business Meaning
Order fulfillment represents the operational progression of an accepted order toward shipment and delivery.

### Participating Entities
- Order
- Order Item
- Seller
- Delivery

### Process Flow
1. An order progresses through its lifecycle.
2. Order items are prepared or processed.
3. Fulfillment activity progresses toward shipment or delivery.
4. Operational status and timestamps may be recorded.

### Analytical Relevance
Fulfillment analysis supports operational performance, order lifecycle analysis, seller performance, and delivery analysis.

### Expected Process Grain
One order fulfillment lifecycle, or one fulfillment event where source events exist.

### Source Verification
Verify whether shipment or fulfillment events are explicitly available and whether the source provides only final order status and delivery timestamps.

## 10. Delivery

### Business Meaning
Delivery represents the movement of an order toward its customer and the completion of the delivery lifecycle.

### Participating Entities
- Order
- Customer
- Geography
- Delivery

### Process Flow
1. An order progresses toward delivery.
2. An estimated delivery date may be recorded.
3. An actual delivery date may be recorded.
4. Delivery performance can be evaluated against the expected timeline.

### Analytical Relevance
Delivery analysis supports delivery duration, delay rate, geographic performance, fulfillment analysis, and customer experience analysis.

### Expected Process Grain
One order delivery lifecycle, if the source supports order-level delivery analysis.

### Source Verification
Verify estimated delivery dates, actual delivery dates, order timestamps, cancellation behavior, missing dates, and whether multiple delivery events exist.

## 11. Order Completion and Lifecycle Closure

### Business Meaning
Order completion represents the progression of an order toward a terminal or completed business state.

### Participating Entities
- Order
- Order Item
- Payment
- Delivery

### Process Flow
1. The order progresses through its lifecycle.
2. Fulfillment and delivery outcomes are recorded where available.
3. The order reaches a terminal status or otherwise exits active processing.

### Analytical Relevance
Lifecycle closure supports completed-order analysis, cancellation analysis, fulfillment performance, delivery performance, and operational reporting.

### Expected Process Grain
One order lifecycle.

### Source Verification
Verify source order-status values, terminal states, timestamps, cancellation semantics, and whether status history is available.

## 12. Customer Review and Feedback

### Business Meaning
This process represents customer feedback associated with an order or transaction.

### Participating Entities
- Customer
- Review
- Order
- Product, indirectly where source relationships permit

### Process Flow
1. A customer provides feedback.
2. A review record is associated with an order or transaction where supported.
3. A review score and other feedback attributes may be recorded.

### Analytical Relevance
Review analysis supports customer satisfaction analysis, product performance, order experience analysis, and relationships between delivery outcomes and customer feedback.

### Expected Process Grain
One review record.

### Source Verification
Verify review identifiers, order relationships, score ranges, review timestamps, comment availability, and whether product-level relationships are directly available.

## 13. Returns and Exceptions

### Business Meaning
Returns and exceptions represent situations where normal order fulfillment or completion does not occur as expected.

### Participating Entities
- Order
- Order Item
- Payment
- Delivery

### Analytical Relevance
Returns, cancellations, failed deliveries, and other exceptions can support operational quality and exception-rate analysis.

### Source Boundary
This process must only be implemented if the selected source dataset contains reliable evidence of returns, refunds, cancellations, failed delivery events, or comparable exception states.

### Expected Process Grain
One exception event or one affected order/item, depending on source semantics.

### Source Verification
Verify whether exception events exist and whether they can be distinguished from normal lifecycle statuses.

## 14. Process Dependency Chain

The conceptual e-commerce process dependency chain is:

Customer Establishment → Product Availability → Purchase Intent → Order Placement → Order Item Processing → Payment Processing → Order Fulfillment → Delivery → Order Completion → Customer Review

Returns and exceptions may occur at multiple points in the lifecycle and therefore are treated as cross-cutting exception processes rather than a mandatory sequential step.

## 15. Process-to-Entity Relationship

| Business Process | Primary Entities | Primary Analytical Grain |
|---|---|---|
| Customer Acquisition and Registration | Customer, Geography | Customer/event |
| Product Discovery and Availability | Product, Category, Seller | Product/listing |
| Purchase Intent and Cart Activity | Customer, Product, Seller | Interaction/event |
| Order Placement | Customer, Order, Order Item, Product, Seller | Order / order item |
| Order Item Processing | Order Item, Order, Product, Seller | Order item |
| Payment Processing | Order, Payment | Payment record |
| Order Fulfillment | Order, Order Item, Seller, Delivery | Order fulfillment |
| Delivery | Order, Customer, Geography, Delivery | Delivery lifecycle |
| Order Completion | Order, Delivery, Payment | Order lifecycle |
| Customer Review and Feedback | Customer, Review, Order | Review |
| Returns and Exceptions | Order, Order Item, Payment, Delivery | Exception/event |

## 16. Process-to-Analytical Questions

### Sales
- How many orders are placed over time?
- What is the sales value associated with order items?
- How many units are sold?
- How does sales activity vary by product, category, seller, customer, and geography?

### Customers
- How many customers place orders?
- How frequently do customers purchase?
- What proportion of customers are repeat customers?
- How does customer activity vary geographically?

### Products
- Which products contribute to sales and unit volume?
- How does performance vary by product category?
- How do product-level outcomes vary across sellers?

### Sellers
- How much transaction activity is associated with each seller?
- How does seller performance vary by geography and product category?

### Payments
- Which payment methods are used?
- What payment value is associated with orders?
- Can payment records be reconciled with order activity?

### Delivery
- How long does delivery take?
- How frequently are deliveries later than expected?
- How does delivery performance vary geographically?

### Reviews
- What is the distribution of review scores?
- How does customer feedback relate to product and delivery outcomes?

These questions are analytical examples and will be formally governed as metrics and analytical definitions in later areas.

## 17. Process Grain Awareness

Different processes operate at different grains. Customer processes may operate at customer or customer-event grain. Order processes operate at order grain. Order-item processing operates at order-item grain. Payment processing operates at payment-record grain. Reviews operate at review grain. Delivery may operate at order-delivery lifecycle grain.

Combining these grains without explicit modeling would create double-counting risks. Later dimensional modeling must preserve the original business grain of each measurable process.

## 18. Process Dependencies

Key dependencies include:

- Customer context is required for customer-level order analysis.
- Product and seller context is required for order-item analysis.
- Order context is required for order-item, payment, delivery, and review relationships.
- Order-item context is required for detailed product and seller sales analysis.
- Delivery timestamps are required for reliable delivery-duration and delay calculations.
- Review relationships are required before connecting customer feedback to orders or products.

## 19. Operational Versus Analytical Process Perspective

Operational processes describe how the e-commerce business executes activities. Analytical processes describe how those activities are transformed into reliable, governed information for reporting and decision support.

RetailIQ must preserve this distinction. A source operational record must not automatically be treated as an analytical fact without validating its business meaning, grain, relationships, and measurement semantics.

## 20. Source-Dependent Processes

Some conceptual processes may not be directly represented by the selected source dataset.

Examples include customer registration, cart activity, browsing behavior, inventory activity, shipment events, returns, refunds, and detailed status history.

These processes must not be fabricated. If source evidence does not exist, the process remains documented as a domain concept but is excluded from implemented analytical models unless another legitimate source is introduced.

## 21. Assumptions

- The project represents an e-commerce marketplace or comparable retail transaction domain.
- Orders contain one or more order items where source semantics support that relationship.
- Payment records are associated with orders.
- Delivery outcomes may be analyzed when sufficient timestamps are available.
- Customer reviews represent customer feedback associated with an order or transaction.
- Some business processes may not have direct event-level source data.

## 22. Known Unknowns

- Exact process timestamps must be verified from the selected source.
- Exact order lifecycle states must be verified.
- Fulfillment and shipment event availability is not yet confirmed.
- Cart and browsing activity availability is not yet confirmed.
- Returns and refund information is not yet confirmed.
- Review-to-product relationships require source verification.
- The distinction between source master data and transactional events requires profiling.

## 23. Physical Modeling Boundary

This document does not define physical fact tables, dimension tables, surrogate keys, SQL transformations, warehouse schemas, indexes, partitions, clustering, orchestration jobs, or BI implementation.

Those engineering decisions belong to later areas after source discovery, profiling, modeling, and architecture validation.

## 24. Area 02 Artifact Completion

This artifact defines the conceptual business processes of the RetailIQ e-commerce domain, their participating entities, process dependencies, analytical relevance, process grains, assumptions, unknowns, and source-verification requirements.

Status: Draft — validation required before acceptance.
