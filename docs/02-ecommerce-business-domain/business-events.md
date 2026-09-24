# RetailIQ — Business Events

## Document Status

- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Area: 02 — E-Commerce Business Domain
- Artifact: Business Events
- Status: Draft
- Purpose: Define observable business events and state changes within the e-commerce domain before physical warehouse and analytical model implementation.

## 1. Business Event Purpose

Business events represent observable occurrences, transactions, or state changes within the RetailIQ e-commerce domain. They connect business processes to measurable analytical activity.

Events documented here are conceptual. They do not represent physical event tables, Kafka topics, database tables, warehouse facts, or implementation-specific records.

## 2. Business Event Identification Principles

A business event should have a meaningful business occurrence, a triggering condition, participating business entities, an identifiable grain, and where possible an associated timestamp.

Events must be supported by source evidence before being implemented. A conceptual event must not be treated as available source data merely because it is logically expected in an e-commerce business.

## 3. Customer Established Event

### Business Meaning
Represents the establishment of a customer record or customer relationship within the platform.

### Trigger
A customer record is created or becomes available in the source system.

### Participating Entities
- Customer
- Geography, where available

### Expected Grain
One customer establishment event.

### Potential Timestamp
Customer creation or registration timestamp, if available.

### Analytical Relevance
Supports customer population, acquisition timing, geographic distribution, and customer lifecycle analysis.

### Source Verification
Verify whether the source contains a customer creation timestamp or only a customer master record.

## 4. Product Available Event

### Business Meaning
Represents a product or product listing becoming available within the marketplace.

### Trigger
A product or listing is recorded as available in the source system.

### Participating Entities
- Product
- Product Category
- Seller

### Expected Grain
One product availability event or product/listing record.

### Potential Timestamp
Product creation or availability timestamp, if available.

### Analytical Relevance
Supports assortment, product lifecycle, category, and seller analysis.

### Source Verification
Verify whether product creation or availability events exist. Do not infer availability dates from unrelated transaction timestamps.

## 5. Purchase Intent Event

### Business Meaning
Represents a customer interaction indicating potential purchase intent.

### Trigger
A customer adds, selects, saves, or otherwise interacts with a product for potential purchase.

### Participating Entities
- Customer
- Product
- Seller, where available

### Expected Grain
One customer-product interaction or intent event.

### Potential Timestamp
Interaction timestamp, if available.

### Analytical Relevance
Could support conversion and customer behavior analysis.

### Source Verification
Verify whether browsing, cart, wishlist, or interaction events exist. If absent, this event must remain conceptual.

## 6. Order Created Event

### Business Meaning
Represents the creation of a customer order.

### Trigger
A valid order identifier is created for a customer purchase.

### Participating Entities
- Customer
- Order
- Order Item

### Expected Grain
One order creation event.

### Potential Timestamp
Order creation timestamp.

### Analytical Relevance
Supports order volume, customer purchasing activity, order trends, and order lifecycle analysis.

### Source Verification
Verify order identifier uniqueness, order creation timestamp, customer relationship, and lifecycle semantics.

## 7. Order Item Recorded Event

### Business Meaning
Represents an individual product line being recorded within an order.

### Trigger
An order item record is associated with an order.

### Participating Entities
- Order
- Order Item
- Product
- Seller

### Expected Grain
One order item.

### Potential Timestamp
Order-item creation timestamp if available; otherwise the event may inherit carefully defined order context.

### Analytical Relevance
Supports units, product sales, seller sales, item-level revenue, and basket analysis.

### Source Verification
Verify item sequence, product identifier, seller identifier, price, freight, and quantity semantics.

## 8. Payment Recorded Event

### Business Meaning
Represents payment information being recorded against an order.

### Trigger
A payment record is associated with an order.

### Participating Entities
- Order
- Payment

### Expected Grain
One payment record or payment event.

### Potential Timestamp
Payment timestamp, if available.

### Analytical Relevance
Supports payment-method analysis, payment value, installment analysis, and reconciliation.

### Source Verification
Verify payment sequence, payment type, payment value, installments, identifiers, and order relationship.

## 9. Order Status Changed Event

### Business Meaning
Represents a change in the business state of an order.

### Trigger
An order transitions from one status to another.

### Participating Entities
- Order
- Order Status

### Expected Grain
One order-status transition.

### Potential Timestamp
Status-change timestamp.

### Analytical Relevance
Supports lifecycle analysis, cancellation analysis, fulfillment monitoring, and operational reporting.

### Source Verification
Verify whether status history exists. If the source only contains the latest order status, historical status-change events must not be fabricated.

## 10. Order Fulfillment Event

### Business Meaning
Represents an order progressing through fulfillment.

### Trigger
An order reaches a fulfillment-related state or event.

### Participating Entities
- Order
- Order Item
- Seller

### Expected Grain
One fulfillment event or order fulfillment lifecycle.

### Potential Timestamp
Fulfillment or shipment timestamp, if available.

### Analytical Relevance
Supports fulfillment performance and operational lifecycle analysis.

### Source Verification
Verify whether explicit fulfillment or shipment timestamps/events exist.

## 11. Delivery Expected Event

### Business Meaning
Represents the expected delivery commitment associated with an order.

### Trigger
An expected delivery date or delivery commitment is established.

### Participating Entities
- Order
- Customer
- Geography

### Expected Grain
One order-level expected delivery record.

### Potential Timestamp
Expected delivery date or timestamp.

### Analytical Relevance
Provides the reference point required for expected-versus-actual delivery analysis.

### Source Verification
Verify whether the source contains an estimated delivery date and its exact business meaning.

## 12. Delivery Completed Event

### Business Meaning
Represents completion of delivery for an order.

### Trigger
An actual delivery date or completed-delivery state is recorded.

### Participating Entities
- Order
- Customer
- Geography
- Delivery

### Expected Grain
One completed order delivery.

### Potential Timestamp
Actual delivery timestamp or date.

### Analytical Relevance
Supports delivery duration, delivery delay, geographic performance, and customer experience analysis.

### Source Verification
Verify actual delivery timestamps, missing values, cancellation behavior, and delivery semantics.

## 13. Customer Review Submitted Event

### Business Meaning
Represents a customer submitting feedback or a review.

### Trigger
A review record becomes available in the source system.

### Participating Entities
- Customer
- Review
- Order

### Expected Grain
One review record.

### Potential Timestamp
Review creation or submission timestamp, if available.

### Analytical Relevance
Supports review-score analysis, customer feedback, product analysis, and delivery-experience analysis.

### Source Verification
Verify review identifier, order relationship, score range, timestamps, and comment fields.

## 14. Order Cancelled Event

### Business Meaning
Represents an order entering a cancelled state.

### Trigger
An order receives a cancellation status or explicit cancellation event.

### Participating Entities
- Order
- Customer

### Expected Grain
One cancelled order event.

### Potential Timestamp
Cancellation timestamp, if available.

### Analytical Relevance
Supports cancellation rate and order lifecycle analysis.

### Source Verification
Verify whether cancellation is explicitly represented and whether the available status/timestamp can reliably identify the event.

## 15. Return or Refund Event

### Business Meaning
Represents a product or transaction being returned or refunded.

### Trigger
A return, refund, or equivalent exception is recorded.

### Participating Entities
- Order
- Order Item
- Payment

### Expected Grain
One return/refund event or affected order item, depending on source semantics.

### Analytical Relevance
Supports exception analysis, financial reconciliation, and operational quality analysis.

### Source Verification
Verify whether returns or refunds exist in the selected source. Do not derive them from assumptions about cancelled orders.

## 16. Business Event Dependency Chain

The principal conceptual event sequence is:

Customer Established → Product Available → Purchase Intent → Order Created → Order Item Recorded → Payment Recorded → Fulfillment → Delivery Expected → Delivery Completed → Review Submitted

Order Status Changed can occur throughout the order lifecycle.

Order Cancellation and Return/Refund events are exception events and may occur at different points in the lifecycle.

## 17. Event-to-Process Mapping

| Business Event | Related Process | Expected Grain | Source Verification |
|---|---|---|---|
| Customer Established | Customer Acquisition and Registration | Customer event | Required |
| Product Available | Product Discovery and Availability | Product/listing | Required |
| Purchase Intent | Purchase Intent and Cart Activity | Interaction/event | Required |
| Order Created | Order Placement | Order | Required |
| Order Item Recorded | Order Item Processing | Order item | Required |
| Payment Recorded | Payment Processing | Payment record | Required |
| Order Status Changed | Order Completion / Lifecycle | Status transition | Required |
| Order Fulfillment | Order Fulfillment | Fulfillment event/lifecycle | Required |
| Delivery Expected | Delivery | Order delivery | Required |
| Delivery Completed | Delivery | Order delivery | Required |
| Customer Review Submitted | Customer Review and Feedback | Review | Required |
| Order Cancelled | Returns and Exceptions | Cancelled order | Required |
| Return or Refund | Returns and Exceptions | Return/refund event | Required |

## 18. Event Grain and Double-Counting Risk

Business events operate at different grains. An order-created event is not equivalent to an order-item event. A payment record is not equivalent to an order. A review is not equivalent to a customer.

Analytical models must preserve these distinctions. Joining event populations without controlling grain can multiply records and produce incorrect order counts, revenue, units, payment values, or review statistics.

Future warehouse models must therefore define explicit grain before combining event-derived information.

## 19. Event Timestamp Requirements

Where an event is implemented analytically, the relevant source timestamp must be identified and its business meaning documented.

Potential timestamps include creation time, payment time, fulfillment time, estimated delivery date, actual delivery date, review submission time, cancellation time, or other source-defined event timestamps.

Dates must not be substituted for timestamps without documenting the loss of time precision and the business implications.

## 20. Source Availability Classification

Business events will eventually be classified into three categories:

- Confirmed: directly supported by verified source records.
- Derived: calculated from verified source attributes according to an explicit documented rule.
- Conceptual: logically valid business event but not supported by available source evidence.

No conceptual event may be presented as confirmed source data.

## 21. Derived Event Boundaries

Some events may be derived from source data. For example, a delivery-delay condition may be derived from expected and actual delivery dates.

Derived events require:

- Verified source fields.
- A documented calculation rule.
- Explicit business semantics.
- Data-quality validation.
- Clear distinction from directly captured source events.

## 22. Assumptions

- Orders represent meaningful customer purchase activity.
- Order items represent detailed product lines.
- Payment records represent payment-related business activity where available.
- Delivery dates can support delivery analysis when their semantics are verified.
- Reviews represent customer feedback.
- Some logically expected events may not exist in the selected source dataset.

## 23. Known Unknowns

- Exact event timestamps have not yet been verified against the source.
- Customer creation events may not exist.
- Product availability events may not exist.
- Purchase-intent events may not exist.
- Explicit order-status history may not exist.
- Fulfillment/shipment events may not exist.
- Cancellation timestamps may not exist.
- Return/refund events may not exist.

## 24. Physical Modeling Boundary

This document does not define event tables, fact tables, dimension tables, surrogate keys, SQL transformations, streaming topics, warehouse schemas, indexes, partitions, orchestration jobs, or BI implementation.

Physical implementation decisions belong to later engineering areas after source discovery, profiling, architecture, and dimensional modeling.

## 25. Area 02 Artifact Completion

This artifact defines the conceptual business events and state changes associated with RetailIQ processes, including event meaning, triggers, participating entities, grain, timestamps, analytical relevance, dependencies, and source-verification requirements.

Status: Draft — validation required before acceptance.
