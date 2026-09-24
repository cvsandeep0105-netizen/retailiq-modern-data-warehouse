# RetailIQ — Business Entities

## Document Status

- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Area: 02 — E-Commerce Business Domain
- Artifact: Business Entities
- Status: Draft
- Purpose: Define the business entities, their meaning, relationships, analytical relevance, and expected business grain before physical warehouse modeling.

## 1. Business Entity Purpose

This document defines the major business entities within the RetailIQ e-commerce domain. The entities represent business concepts rather than physical database tables. Physical facts, dimensions, keys, schemas, and implementation structures will be designed in later areas.

## 2. Entity Identification Principles

Business entities are identified using their business meaning, operational role, identifying attributes, relationships, lifecycle, and analytical relevance.

Each entity definition distinguishes known business concepts from assumptions that require verification against the selected source dataset.

## 3. Customer

### Business Meaning
A customer represents a person or party that places or receives orders through the e-commerce platform.

### Business Purpose
The customer entity supports analysis of purchasing behavior, customer activity, order frequency, geographic distribution, and customer value.

### Identifying Concept
A customer is expected to be identifiable through a source-system customer identifier. The exact identifier and uniqueness behavior must be verified against the selected source.

### Relationships
- A customer may place multiple orders.
- An order is associated with a customer.
- A customer may be associated with geographic attributes.
- Customer activity may be analyzed across multiple dates and orders.

### Expected Cardinality
One customer to many orders is the expected business relationship, subject to source verification.

### Analytical Relevance
Customer analysis supports customer acquisition, retention, repeat purchasing, geographic analysis, and customer-value analysis.

### Potential Business Grain
One row representing one business customer.

### Source Verification Requirements
Verify customer identifier uniqueness, customer-to-order relationships, available geography, missing values, duplicate records, and whether customer attributes change historically.

## 4. Seller

### Business Meaning
A seller represents a merchant or business party responsible for selling products through the e-commerce platform.

### Business Purpose
The seller entity supports seller performance, sales contribution, fulfillment analysis, geographic analysis, and marketplace performance analysis.

### Identifying Concept
A seller is expected to have a source-system seller identifier. The identifier and uniqueness behavior require source verification.

### Relationships
- A seller may offer multiple products or product listings.
- A seller may be associated with multiple order items.
- Seller activity may contribute to order-level and item-level business outcomes.

### Expected Cardinality
One seller to many order items is expected where an order can contain products supplied by sellers.

### Analytical Relevance
Seller analysis supports seller revenue, units sold, order-item volume, geographic distribution, and seller-level operational performance.

### Potential Business Grain
One row representing one business seller.

### Source Verification Requirements
Verify seller identifiers, seller attributes, seller-to-item relationships, geographic information, duplicate records, and historical attribute behavior.

## 5. Product

### Business Meaning
A product represents a sellable product or product listing available through the e-commerce platform.

### Business Purpose
The product entity supports product sales, category analysis, product performance, pricing analysis, and product-level customer behavior.

### Identifying Concept
A product is expected to be identified by a source-system product identifier. The distinction between product and listing must be verified from source documentation and data.

### Relationships
- A product may be associated with a product category.
- A product may appear in multiple order items.
- A product may be associated with one or more sellers depending on source-system structure.

### Expected Cardinality
One product to many order items is expected.

### Analytical Relevance
Product analysis supports sales performance, product mix, category performance, pricing, volume, and customer purchasing analysis.

### Potential Business Grain
One row representing one business product or product listing, depending on source semantics.

### Source Verification Requirements
Verify product identifier uniqueness, category relationships, product attributes, seller relationships, missing attributes, and whether product attributes have historical versions.

## 6. Product Category

### Business Meaning
A product category groups products according to the classification supplied by the source or business domain.

### Business Purpose
Categories support product grouping and aggregated sales, volume, and customer analysis.

### Identifying Concept
A category should be identified through a source category identifier or a governed category value, depending on source structure.

### Relationships
- A category may contain multiple products.
- A product may belong to a category according to source-system rules.

### Expected Cardinality
One category to many products is expected.

### Analytical Relevance
Category-level analysis supports product mix, revenue distribution, demand analysis, and category performance.

### Potential Business Grain
One row representing one governed product category.

### Source Verification Requirements
Verify category identifiers, category names, translation mappings where applicable, and product-to-category cardinality.

## 7. Order

### Business Meaning
An order represents a customer purchase transaction or order lifecycle initiated through the e-commerce platform.

### Business Purpose
The order entity provides the central business context for order volume, order status, customer activity, fulfillment, payment, delivery, and revenue-related analysis.

### Identifying Concept
An order is expected to have a source-system order identifier that identifies the order business event or lifecycle.

### Relationships
- An order belongs to a customer.
- An order may contain multiple order items.
- An order may have one or more payment records depending on source behavior.
- An order may have review information depending on source behavior.
- An order has lifecycle and delivery-related dates where available.

### Expected Cardinality
One order to many order items is expected. Other relationships require source verification.

### Analytical Relevance
Order analysis supports order volume, order status, customer activity, revenue analysis, fulfillment, delivery, and operational performance.

### Potential Business Grain
One row representing one business order.

### Source Verification Requirements
Verify order identifier uniqueness, customer relationship, item cardinality, payment cardinality, status values, timestamps, and lifecycle semantics.

## 8. Order Item

### Business Meaning
An order item represents an individual product line within an order.

### Business Purpose
Order items provide the detailed transaction grain required for product, seller, quantity, price, and item-level sales analysis.

### Identifying Concept
An order item may require a composite business identity such as order identifier plus item sequence, depending on the source model.

### Relationships
- An order item belongs to an order.
- An order item references a product.
- An order item may reference a seller.
- An order may contain multiple order items.

### Expected Cardinality
One order to many order items is expected.

### Analytical Relevance
Order-item analysis supports units sold, item revenue, product performance, seller performance, basket composition, and detailed sales analysis.

### Potential Business Grain
One row representing one product line within one order.

### Source Verification Requirements
Verify order-item identifier behavior, item sequence semantics, product relationship, seller relationship, quantity availability, pricing fields, and freight or item-level charges.

## 9. Payment

### Business Meaning
A payment represents a payment transaction or payment record associated with an order.

### Business Purpose
Payment information supports payment-method analysis, payment value analysis, installment analysis where available, and reconciliation with order-level business activity.

### Identifying Concept
A payment may require an order identifier combined with a payment sequence or source payment identifier, depending on source structure.

### Relationships
- A payment is associated with an order.
- An order may have multiple payment records if supported by the source.

### Expected Cardinality
One order to one or many payment records must be verified from the source.

### Analytical Relevance
Payment analysis supports payment-method distribution, payment value, transaction counts, and reconciliation.

### Potential Business Grain
One row representing one source payment record or payment event.

### Source Verification Requirements
Verify payment identifier availability, order relationship, payment sequence behavior, payment type, value, installments, duplicates, and reconciliation rules.

## 10. Delivery

### Business Meaning
Delivery represents the fulfillment and delivery lifecycle associated with an order.

### Business Purpose
Delivery information supports fulfillment performance, delivery duration, delivery delays, estimated-versus-actual delivery analysis, and operational performance.

### Identifying Concept
Delivery may be represented by an order-level lifecycle rather than an independent source entity. This must be determined from source data.

### Relationships
- Delivery is associated with an order.
- Delivery may contain estimated and actual delivery dates.
- Delivery outcomes may be analyzed alongside customer geography and order attributes.

### Expected Cardinality
An order is expected to have zero or one primary delivery lifecycle record in the analytical model if source semantics support that representation.

### Analytical Relevance
Delivery analysis supports delivery duration, delay rate, fulfillment performance, and geographic delivery analysis.

### Potential Business Grain
One row representing one order delivery lifecycle.

### Source Verification Requirements
Verify delivery-related timestamps, order relationship, missing dates, cancellation behavior, and whether multiple delivery events exist.

## 11. Review

### Business Meaning
A review represents customer feedback associated with a completed or otherwise reviewable order or transaction.

### Business Purpose
Reviews support customer satisfaction, product performance, order experience, and relationships between operational outcomes and customer feedback.

### Identifying Concept
A review may be identified through a source review identifier, with an associated order identifier where supported.

### Relationships
- A review may be associated with an order.
- Review information may indirectly support product and customer analysis through order relationships.

### Expected Cardinality
Review-to-order cardinality must be verified from the source.

### Analytical Relevance
Review analysis supports rating distributions, customer feedback, product performance, and delivery or fulfillment outcome analysis.

### Potential Business Grain
One row representing one source review record.

### Source Verification Requirements
Verify review identifier uniqueness, order relationship, score range, comment availability, timestamps, duplicates, and missing records.

## 12. Geography

### Business Meaning
Geography represents geographic attributes associated with customers, sellers, delivery locations, or other business parties.

### Business Purpose
Geographic information supports regional sales, customer distribution, seller distribution, delivery performance, and location-based analysis.

### Identifying Concept
Geography may be represented through postal-code prefixes, cities, states, regions, coordinates, or governed geographic keys depending on source availability.

### Relationships
- Customers may be associated with geography.
- Sellers may be associated with geography.
- Orders or deliveries may reference customer delivery geography.

### Expected Cardinality
Geographic relationships depend on the level and quality of source location data.

### Analytical Relevance
Geographic analysis supports regional sales, customer distribution, seller concentration, and delivery performance.

### Potential Business Grain
One row representing one governed geographic entity at a defined geographic level.

### Source Verification Requirements
Verify available geographic attributes, granularity, postal-code behavior, coordinate availability, data quality, and mapping requirements.

## 13. Order Status

### Business Meaning
Order status represents a business state in the order lifecycle.

### Business Purpose
Order status supports lifecycle analysis, operational monitoring, cancellation analysis, fulfillment analysis, and order-state reporting.

### Identifying Concept
Status is expected to be represented by a controlled source value rather than an independently assumed business identifier.

### Relationships
- An order has one or more status values across its lifecycle depending on source history availability.

### Expected Cardinality
The analytical representation of status history must be determined from source data and historical availability.

### Analytical Relevance
Status analysis supports order lifecycle and operational performance analysis.

### Potential Business Grain
One governed status value, or one order-status event if historical status events are available.

### Source Verification Requirements
Verify the complete status domain, lifecycle sequence, timestamp availability, cancellation semantics, and whether status history exists.

## 14. Entity Relationship Summary

| Entity | Primary Business Relationship | Expected Analytical Grain | Source Verification Required |
|---|---|---|---|
| Customer | Customer places orders | One customer | Yes |
| Seller | Seller supplies order items | One seller | Yes |
| Product | Product appears in order items | One product/listing | Yes |
| Product Category | Category groups products | One category | Yes |
| Order | Customer places order | One order | Yes |
| Order Item | Order contains product lines | One order line | Yes |
| Payment | Order has payment record(s) | One payment record | Yes |
| Delivery | Order has delivery lifecycle | One order delivery lifecycle | Yes |
| Review | Review relates to order/transaction | One review | Yes |
| Geography | Business party/order linked to location | One governed geography | Yes |
| Order Status | Order lifecycle state | One status/event | Yes |

## 15. Business Grain Summary

The principal business grains identified at this stage are customer, seller, product, category, order, order item, payment, delivery lifecycle, review, geography, and order status.

These grains are conceptual only. Physical fact and dimension grain definitions will be established later during the dimensional modeling phase.

## 16. Assumptions

- The domain represents an e-commerce marketplace or platform.
- Customers, sellers, products, orders, order items, payments, reviews, delivery, and geography are relevant business concepts.
- The exact relationships and cardinalities must be validated against the selected source dataset.
- The source may not contain complete historical records for every business concept.
- Source-specific terminology may differ from the conceptual terminology used here.

## 17. Known Unknowns

- Exact source identifiers have not yet been finalized.
- Exact source cardinalities have not yet been validated.
- Historical attribute behavior is not yet confirmed.
- Delivery event structure is not yet confirmed.
- Payment cardinality is not yet confirmed.
- Review-to-order and review-to-product relationships require source verification.
- Geographic granularity and normalization requirements require source profiling.

## 18. Physical Modeling Boundary

This document intentionally does not define final fact tables, dimension tables, surrogate keys, warehouse schemas, indexes, partitions, clustering, materializations, or SQL implementations.

Those decisions belong to later engineering areas after source discovery, profiling, and dimensional modeling.

## 19. Area 02 Artifact Completion

This artifact establishes the conceptual business entities required for RetailIQ and documents their business meaning, relationships, expected cardinality, analytical relevance, potential grain, assumptions, and source-verification requirements.

Status: Draft — validation required before acceptance.
