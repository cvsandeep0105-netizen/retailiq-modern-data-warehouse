# RetailIQ — Business Process Analysis

## Document Status

- Area: 03 — Business Processes & Analytical Questions
- Artifact: Business Process Analysis
- Status: Draft
- Scope: Business-process and analytical-requirement definition
- Physical warehouse design: Out of scope
- Source-specific implementation: Deferred until source discovery and profiling
- Validation state: Initial creation

## 1. Purpose

This document converts the conceptual RetailIQ business domain into an analytical understanding of the major e-commerce business processes.

The objective is to establish how business activities occur, what business outcomes they produce, what analytical questions they support, and what information will eventually be required from verified source data.

This document does not define physical warehouse structures.

## 2. Business Process Inventory

RetailIQ recognizes the following major business processes:

1. Customer establishment and registration
2. Product discovery and availability
3. Purchase intent and cart activity
4. Order placement
5. Order item processing
6. Payment processing
7. Order fulfillment
8. Delivery execution
9. Order completion
10. Customer review and feedback
11. Cancellation, return, and refund handling
12. Seller activity and commercial fulfillment

These processes form a conceptual business lifecycle. Exact source representation must be verified during source discovery.

## 3. End-to-End Business Process Flow

The conceptual process flow is:

Customer Established
→ Product Discovery
→ Purchase Intent
→ Order Placement
→ Order Item Processing
→ Payment
→ Fulfillment
→ Delivery
→ Order Completion
→ Review / Feedback

Exception paths may include:

Order Placement
→ Cancellation

Order Completion / Delivery
→ Return / Refund

Payment
→ Payment Failure / Exception

The actual availability of these events and exception states is source-dependent.

## 4. Customer Establishment and Registration

### 4.1 Business Purpose

Establish a customer identity that can participate in marketplace transactions.

### 4.2 Primary Actor

Customer.

### 4.3 Core Business Entities

- Customer
- Geography

### 4.4 Business Outcome

A customer becomes identifiable for subsequent commercial activity.

### 4.5 Analytical Relevance

This process supports analysis of:

- customer population
- customer geography
- customer acquisition patterns where dates are available
- customer activity
- customer retention and repeat purchasing

### 4.6 Analytical Grain

Conceptual customer-level analysis.

### 4.7 Important Time Concepts

Potential timestamps include customer establishment or registration time if available.

### 4.8 Source Dependency

Customer creation timing and customer attributes must be verified against the selected source.

## 5. Product Discovery and Availability

### 5.1 Business Purpose

Enable customers to identify products that may be purchased.

### 5.2 Primary Actors

- Customer
- Seller
- Marketplace

### 5.3 Core Business Entities

- Product
- Product Category
- Seller

### 5.4 Business Outcome

Products become discoverable and commercially relevant to customers.

### 5.5 Analytical Relevance

Supports analysis of:

- product catalog composition
- category performance
- seller assortment
- product demand
- product-level commercial activity

### 5.6 Analytical Grain

Conceptually product-level or product-category-level analysis.

### 5.7 Source Dependency

Actual product availability, inventory state, discovery activity, and catalog history must not be assumed unless represented by the source.

## 6. Purchase Intent and Cart Activity

### 6.1 Business Purpose

Represent customer intent before confirmed order placement.

### 6.2 Analytical Relevance

Potential questions include:

- Which products generate purchase intent?
- How does purchase intent relate to completed orders?
- Which categories show strong customer interest?

### 6.3 Source Boundary

This process must be treated as source-dependent.

If cart, browsing, clickstream, or session data is not available, RetailIQ must not claim to measure purchase intent directly.

### 6.4 Physical Modeling Boundary

No cart or behavioral fact table is defined at this stage.

## 7. Order Placement

### 7.1 Business Purpose

Convert customer purchase intent into a commercial order.

### 7.2 Primary Actor

Customer.

### 7.3 Core Entities

- Customer
- Order
- Order Item
- Product
- Seller
- Payment

### 7.4 Business Outcome

An order is created containing one or more order items.

### 7.5 Analytical Grain

The process has at least two conceptual grains:

- order
- order item

These grains must not be combined without explicit aggregation rules.

### 7.6 Analytical Relevance

Supports:

- order volume
- sales analysis
- customer purchasing behavior
- product demand
- seller performance
- average order value

## 8. Order Item Processing

### 8.1 Business Purpose

Represent the individual products and commercial line items contained within an order.

### 8.2 Analytical Grain

One conceptual order item per purchased product line.

### 8.3 Analytical Relevance

Supports:

- units sold
- product sales
- category sales
- seller sales
- order composition
- basket analysis

### 8.4 Double-Counting Risk

Order-level measures must not be summed directly across order-item rows without appropriate aggregation.

For example, an order total repeated across multiple order-item rows can cause inflated revenue if summed at item grain.

## 9. Payment Processing

### 9.1 Business Purpose

Record financial payment activity associated with commercial orders.

### 9.2 Core Entities

- Order
- Payment

### 9.3 Analytical Grain

Payment records may have a different grain from orders.

The source must determine whether multiple payment records can exist for a single order.

### 9.4 Analytical Relevance

Potential analysis includes:

- payment method usage
- payment transaction volume
- payment amounts
- payment behavior by customer
- payment behavior by order

### 9.5 Source Dependency

Payment semantics, status, sequence, and amount definitions must be verified from the source.

## 10. Order Fulfillment

### 10.1 Business Purpose

Process confirmed orders toward shipment and delivery.

### 10.2 Primary Actors

- Seller
- Marketplace
- Logistics provider where represented

### 10.3 Analytical Relevance

Supports:

- fulfillment volume
- seller operational activity
- order status analysis
- fulfillment timing

### 10.4 Source Dependency

The exact fulfillment lifecycle depends on source status fields and timestamps.

## 11. Delivery Execution

### 11.1 Business Purpose

Move an order from fulfillment toward customer receipt.

### 11.2 Core Entities

- Order
- Customer
- Geography
- Seller
- Delivery

### 11.3 Analytical Relevance

Potential analysis includes:

- delivery duration
- estimated versus actual delivery
- delivery delay
- geography-level delivery performance
- seller-level delivery performance

### 11.4 Time Concepts

Potential timestamps include:

- order purchase timestamp
- estimated delivery date
- actual delivery date

Exact fields require source verification.

## 12. Order Completion

### 12.1 Business Purpose

Represent the successful completion of the commercial order lifecycle.

### 12.2 Analytical Relevance

Supports:

- completed order volume
- completed sales
- customer activity
- delivery performance
- downstream review analysis

### 12.3 Source Dependency

Completion must be derived from verified source status and lifecycle fields.

## 13. Customer Review and Feedback

### 13.1 Business Purpose

Capture customer feedback following the commercial experience.

### 13.2 Core Entities

- Review
- Customer
- Order
- Product

### 13.3 Analytical Grain

One conceptual review record or review event.

### 13.4 Analytical Relevance

Supports:

- average review score
- review volume
- product satisfaction patterns
- seller-related customer feedback where supported
- relationship between delivery and customer feedback

### 13.5 Source Dependency

The relationship between review, order, product, and seller must be verified.

## 14. Cancellation, Return, and Refund Handling

### 14.1 Business Purpose

Represent commercial exceptions occurring before or after successful order completion.

### 14.2 Analytical Relevance

Potential analysis includes:

- cancellation volume
- return volume
- refund amounts
- exception rates
- product or seller exception patterns

### 14.3 Source Boundary

These capabilities must not be claimed unless the source contains sufficient information.

### 14.4 Physical Modeling Boundary

No return, refund, or exception fact is defined until source availability is verified.

## 15. Seller Commercial Activity

### 15.1 Business Purpose

Represent seller participation in the marketplace and fulfillment of commercial demand.

### 15.2 Core Entities

- Seller
- Product
- Order Item
- Order

### 15.3 Analytical Relevance

Supports:

- seller revenue
- seller order-item volume
- seller product assortment
- seller delivery performance
- seller customer feedback

### 15.4 Analytical Grain

Seller-level analysis must be distinguished from order-item-level analysis.

## 16. Process Dependency Model

The major dependency chain is:

Customer
→ Product Discovery
→ Purchase Intent
→ Order
→ Order Item
→ Payment
→ Fulfillment
→ Delivery
→ Completion
→ Review

Exception paths:

Order
→ Cancellation

Delivery / Completion
→ Return / Refund

Payment
→ Payment Exception

Not every process or exception path is guaranteed to exist in the selected source.

## 17. Process-to-Entity Relationship Summary

| Process | Primary Entities | Analytical Grain |
|---|---|---|
| Customer Establishment | Customer, Geography | Customer |
| Product Discovery | Product, Category, Seller | Product |
| Purchase Intent | Customer, Product | Event/session if available |
| Order Placement | Customer, Order | Order |
| Order Item Processing | Order, Order Item, Product, Seller | Order Item |
| Payment | Order, Payment | Payment |
| Fulfillment | Order, Seller | Order / fulfillment event |
| Delivery | Order, Customer, Geography | Order / delivery lifecycle |
| Completion | Order | Order |
| Review | Review, Customer, Product, Order | Review |
| Cancellation | Order | Order / event |
| Return / Refund | Order, Order Item, Payment | Exception/event |
| Seller Activity | Seller, Order Item, Product | Seller / order item |

## 18. Process-to-Analytical-Question Mapping

| Process | Primary Analytical Themes |
|---|---|
| Customer Establishment | Customer population and geography |
| Product Discovery | Catalog and product/category activity |
| Purchase Intent | Behavioral demand where source-supported |
| Order Placement | Orders, customers, sales |
| Order Item Processing | Product, category, seller and unit analysis |
| Payment | Payment methods and payment activity |
| Fulfillment | Operational processing |
| Delivery | Delivery duration and delay |
| Completion | Completed commercial activity |
| Review | Customer feedback and product experience |
| Cancellation | Order exceptions |
| Return / Refund | Commercial exceptions |
| Seller Activity | Seller commercial performance |

## 19. Analytical Grain Rules

RetailIQ must explicitly distinguish:

- customer grain
- seller grain
- product grain
- order grain
- order-item grain
- payment grain
- review grain
- delivery grain
- event grain

Measures must only be aggregated at compatible grains.

A measure originating at order grain must not be multiplied by order-item, payment, or review joins without explicit aggregation controls.

## 20. Time Analysis Requirements

Potential analytical time dimensions include:

- order date
- order purchase timestamp
- payment timestamp
- shipment timestamp
- delivery date
- review creation date

The source must determine which timestamps are actually available.

Time-based analysis may eventually support:

- daily trends
- weekly trends
- monthly trends
- year-over-year analysis where sufficient history exists
- delivery duration
- operational latency
- customer activity trends

## 21. Cross-Domain Analytical Requirements

RetailIQ should support analytical relationships such as:

- Customer × Orders
- Customer × Revenue
- Product × Units Sold
- Product × Revenue
- Category × Revenue
- Seller × Revenue
- Seller × Delivery Performance
- Payment Method × Order Activity
- Geography × Sales
- Geography × Delivery
- Review × Product
- Review × Delivery Experience

These are analytical requirements, not physical table definitions.

## 22. Double-Counting Controls

The project must explicitly protect against:

- order totals repeated across order-item rows
- payment records multiplied through order-item joins
- review records multiplied through product or order joins
- seller totals duplicated through many-to-many analytical joins
- customer totals duplicated across orders
- delivery measures duplicated through status-event relationships

Future warehouse and semantic-layer implementation must preserve the intended grain of every measure.

## 23. Source-Dependent Process Classification

### Conceptually Required

- Customer
- Product
- Order
- Order Item
- Seller
- Payment
- Delivery
- Review

### Source-Dependent

- Cart activity
- Product availability history
- Fulfillment events
- Cancellation events
- Return events
- Refund events
- Detailed delivery events
- Customer acquisition timing

### Not Assumed

RetailIQ will not claim that a process is measurable merely because it is conceptually meaningful.

## 24. Business Requirements Boundary

This artifact establishes business-process requirements for subsequent source discovery and data engineering.

It does not establish:

- final source tables
- final source columns
- final warehouse tables
- final facts
- final dimensions
- surrogate-key strategy
- SCD implementation
- SQL transformations
- physical indexes
- partitions
- clustering
- BI implementation

## 25. Assumptions

- Orders represent commercial transactions.
- Orders may contain multiple order items.
- Payment records may have a different grain from orders.
- Reviews may have a different grain from orders.
- Delivery represents a lifecycle that may contain multiple dates or states.
- Seller and product relationships require source validation.
- Business processes may not map one-to-one to source tables.

## 26. Unknowns

The following remain unresolved until source discovery:

- Exact source process representation
- Exact source timestamps
- Exact source status semantics
- Actual payment cardinality
- Actual review cardinality
- Availability of returns and refunds
- Availability of cart or behavioral events
- Availability of detailed fulfillment events
- Historical changes to business entities
- Completeness of geography

## 27. Artifact Completion Criteria

This artifact is complete when:

1. Major business processes are documented.
2. Process dependencies are documented.
3. Process grains are identified conceptually.
4. Analytical relevance is documented.
5. Process-to-entity relationships are documented.
6. Analytical question themes are mapped.
7. Double-counting risks are documented.
8. Source-dependent boundaries are explicit.
9. Physical warehouse design remains outside scope.
10. Assumptions and unknowns are explicit.

## 28. Status

This artifact is currently **Draft**.

It must be validated against the companion analytical-question catalog before Area 03 acceptance.
