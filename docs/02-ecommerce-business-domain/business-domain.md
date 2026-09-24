# RetailIQ — E-Commerce Business Domain

## Document Status

- Area: 02 — E-Commerce Business Domain
- Artifact: Business Domain Definition
- Status: Draft for Area 02 validation
- Project: Project 03

## 1. Business Domain Purpose

RetailIQ operates within the e-commerce analytics domain. The platform is intended to transform e-commerce operational data into reliable analytical data products that support business analysis across customers, orders, products, sellers, payments, delivery, reviews, geography, and related commercial activities.

The business domain definition establishes the business concepts that the engineering platform must understand before source-specific modeling decisions are finalized.

## 2. Domain Boundary

The primary domain boundary is the digital e-commerce transaction lifecycle:

Customer ? Product Discovery ? Order Placement ? Order Fulfillment ? Payment ? Delivery ? Customer Review

Supporting business entities such as sellers, geography, products, payments, and order status participate in this lifecycle.

The domain boundary is analytical rather than an assertion that every listed entity or process exists in the selected source dataset. Source availability will be verified in later areas.

## 3. Core Business Actors

### 3.1 Customer

A customer represents an individual or customer account participating in the e-commerce purchasing process.

Potential analytical concerns include:

- Customer identity
- Customer location
- Order behavior
- Purchase frequency
- Purchase value
- Repeat purchasing
- Customer experience

### 3.2 Seller

A seller represents a merchant or commercial participant responsible for offering products through the e-commerce marketplace.

Potential analytical concerns include:

- Seller identity
- Seller location
- Product assortment
- Order volume
- Sales value
- Fulfillment behavior
- Customer experience

### 3.3 Marketplace / E-Commerce Platform

The e-commerce platform provides the commercial environment in which customers, sellers, products, orders, payments, delivery processes, and reviews interact.

RetailIQ analyzes data produced by these business interactions rather than attempting to replace the underlying commerce platform.

## 4. Core Business Entities

The initial business-domain entity set includes:

- Customer
- Seller
- Product
- Product Category
- Order
- Order Item
- Payment
- Review
- Delivery
- Geography
- Order Status

These are business concepts, not yet final warehouse tables.

## 5. Customer Domain

The customer domain represents purchasing participants and their associated commercial activity.

Important business relationships include:

- A customer may place multiple orders.
- An order belongs to a customer.
- A customer may purchase multiple products through orders.
- A customer may provide reviews associated with purchased products or orders where the source supports that relationship.
- Customer geography may provide regional analytical context.

Customer-level analysis must distinguish customer identity from individual order and order-item transactions.

## 6. Product Domain

The product domain represents goods offered through the e-commerce marketplace.

Relevant concepts may include:

- Product identity
- Product category
- Product attributes
- Product dimensions
- Product availability where supported

Products participate in order-item transactions rather than directly representing an order.

## 7. Seller Domain

The seller domain represents merchants responsible for products and order fulfillment activities.

A seller may be associated with multiple products and multiple order items.

Seller-level analysis must distinguish seller attributes from individual commercial transactions.

## 8. Order Domain

An order represents a customer purchasing transaction or commercial order lifecycle.

An order may contain multiple order items.

Important order concepts may include:

- Order identifier
- Customer
- Order status
- Order creation
- Approval
- Shipment
- Delivery
- Completion
- Cancellation or exception where supported

An order is distinct from an order item. This distinction is essential because order-level and item-level measurements have different business grains.

## 9. Order Item Domain

An order item represents an individual product line within an order.

Potential business attributes include:

- Order
- Product
- Seller
- Item sequence
- Quantity where available
- Item price
- Freight or shipping value

Order-item analysis supports product, seller, quantity, revenue, and commercial performance analysis.

## 10. Payment Domain

The payment domain represents financial payment activity associated with commercial orders.

Potential concepts include:

- Payment method
- Payment sequence
- Payment value
- Payment installments where available
- Payment status where available

Payment-level analysis must preserve its own business grain because an order may potentially contain multiple payment records.

## 11. Delivery Domain

The delivery domain represents the movement of an order from fulfillment toward the customer.

Potential analytical concepts include:

- Estimated delivery date
- Actual delivery date
- Delivery duration
- Delivery delay
- Delivery completion

Delivery metrics must be derived only when the source provides the required dates or status information.

## 12. Review Domain

The review domain represents customer feedback associated with completed or relevant commercial interactions.

Potential concepts include:

- Review identifier
- Review score
- Review creation date
- Review response
- Review message
- Associated order or product where supported

Review analysis may provide customer-experience context but must not be assumed to represent all customer sentiment or all customers.

## 13. Geography Domain

The geography domain provides location context for customers, sellers, or other business entities.

Potential analytical levels include:

- Customer location
- Seller location
- City
- State or region
- Postal-code-derived geography
- Geographic coordinates where legitimately available

Geographic attributes must be handled according to the actual source structure and privacy considerations.

## 14. Business Lifecycle

The initial business lifecycle is:

1. Customer exists within the marketplace.
2. Customer interacts with products and sellers.
3. Customer places an order.
4. Order contains one or more order items.
5. Payment activity is associated with the order.
6. Order moves through fulfillment and delivery stages.
7. Delivery reaches the customer where applicable.
8. Customer may provide a review.
9. Resulting data becomes available for analytical processing.

This lifecycle is a conceptual business model. The verified source dataset will determine which lifecycle stages and attributes can actually be observed.

## 15. Business Grain Awareness

RetailIQ must distinguish multiple business grains.

Examples include:

- Customer grain — one business entity per customer
- Order grain — one business transaction per order
- Order-item grain — one product line within an order
- Payment grain — one payment record or payment event
- Review grain — one review record or review event
- Seller grain — one business entity per seller
- Product grain — one product entity per product

These grains are business concepts only at this stage. Final warehouse grain definitions will be established after source profiling and dimensional-modeling analysis.

## 16. Operational Versus Analytical Perspective

Operational systems record business transactions and events required to operate the e-commerce business.

Analytical systems reorganize those records so that business questions can be answered consistently and efficiently.

RetailIQ therefore separates:

- Operational source representation
- Raw source preservation
- Analytical transformation
- Warehouse structures
- Business data marts
- Governed metrics
- BI consumption

## 17. Primary Analytical Domains

The business domain supports analytical investigation across:

- Sales
- Customers
- Products
- Sellers
- Orders
- Payments
- Delivery
- Reviews
- Geography

Final analytical questions will be derived from verified source capabilities and business requirements in subsequent areas.

## 18. Domain Assumptions

The following are initial conceptual assumptions:

- Customers can be distinguished as business entities.
- Orders represent commercial transactions.
- Orders may contain multiple order items.
- Products are distinct from order items.
- Sellers are distinct from products.
- Payment records may have a different grain from orders.
- Reviews may have a different grain from orders.
- Delivery information may represent a lifecycle rather than a single instantaneous event.

These assumptions must be verified against the selected source dataset before they become implementation rules.

## 19. Domain Unknowns

The following must remain open until source discovery and profiling:

- Exact source entity names
- Exact source keys
- Actual cardinalities
- Whether all business entities are present
- Whether product categories are complete
- Whether historical attribute changes are observable
- Whether payment records are one-to-one or one-to-many with orders
- Whether reviews map directly to products, orders, or both
- Whether delivery events are sufficiently detailed
- Whether geographic attributes are complete

Unknowns must not be replaced with invented source behavior.

## 20. Domain-to-Engineering Implications

The business domain indicates that RetailIQ will need to handle multiple business grains, relational dependencies, transaction-level analysis, entity-level analysis, historical considerations, and cross-domain analytical relationships.

These implications will guide later source discovery, data profiling, dimensional modeling, fact-grain definition, and metric design.

They do not constitute final physical warehouse design.


## 20.1 Physical Modeling Boundary

This document defines the conceptual business domain only.

It does not define final physical warehouse tables, schemas, fact tables, dimension tables, surrogate-key structures, physical storage layouts, indexes, partitions, clustering strategies, or implementation-specific transformation logic.

Physical warehouse design will be established only after source discovery, source profiling, relationship validation, grain definition, dimensional modeling, and technology evaluation in subsequent areas.

The business concepts documented here must therefore be treated as domain-level definitions rather than final database structures.

## 21. Area 02 Artifact Completion

This artifact is complete for its current scope when the business-domain boundary, core actors, core entities, lifecycle, grain awareness, assumptions, and unknowns are documented and validated.

