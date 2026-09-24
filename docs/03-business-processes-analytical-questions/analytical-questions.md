# RetailIQ — Analytical Questions Catalog

## Document Status

- Area: 03 — Business Processes & Analytical Questions
- Artifact: Analytical Questions Catalog
- Status: Draft
- Scope: Business-facing analytical requirements
- Source-specific implementation: Deferred until source discovery
- Physical warehouse design: Out of scope

## 1. Purpose

This document defines the analytical questions RetailIQ should be capable of answering from verified e-commerce data.

The questions are intentionally expressed as business questions rather than SQL queries or warehouse-table requirements.

They will later drive source discovery, data modeling, metric definition, data marts, testing, and BI-ready analytical products.

## 2. Question Design Principles

Each analytical question must:

- have a clear business purpose
- identify the relevant business process
- respect the underlying business grain
- identify relevant time context
- avoid unsupported source assumptions
- be measurable only when required source evidence exists
- avoid double counting
- remain independent of a specific physical warehouse design

## 3. Sales Questions

### AQ-SALES-001

**Business Process:** Order Placement

**Question:** How does order volume change over time?

**Purpose:** Understand commercial activity trends.

**Required Grain:** Order

**Potential Dimensions:** Date, geography, customer

**Potential Measures:** Order count

**Source Dependency:** Verified order records and timestamps.

### AQ-SALES-002

**Business Process:** Order Placement

**Question:** How does sales value change over time?

**Purpose:** Understand commercial revenue trends.

**Required Grain:** Order or order-item aggregation depending on source definition.

**Potential Dimensions:** Date, geography, product, category, seller

**Potential Measures:** Revenue or verified sales amount

**Source Dependency:** Verified monetary fields and business definition.

### AQ-SALES-003

**Business Process:** Order Item Processing

**Question:** Which product categories generate the greatest sales value?

**Purpose:** Understand category-level commercial performance.

**Required Grain:** Order item aggregated by category.

**Potential Dimensions:** Date, category

**Potential Measures:** Revenue

**Source Dependency:** Product-category relationship and monetary fields.

### AQ-SALES-004

**Business Process:** Order Item Processing

**Question:** Which products generate the greatest unit volume?

**Purpose:** Identify products with high purchasing volume.

**Required Grain:** Order item

**Potential Dimensions:** Product, category, date

**Potential Measures:** Units sold

**Source Dependency:** Verified quantity semantics.

## 4. Order Questions

### AQ-ORDER-001

**Business Process:** Order Placement

**Question:** How many orders are placed during each time period?

**Purpose:** Monitor commercial order activity.

**Required Grain:** Order

**Potential Dimensions:** Date, customer, geography, status

**Potential Measures:** Order count

### AQ-ORDER-002

**Business Process:** Order Placement

**Question:** What is the average order value?

**Purpose:** Understand the monetary value of a typical order.

**Required Grain:** Order

**Potential Measures:** Revenue and order count

**Analytical Rule:** AOV must be calculated from order-level aggregation rather than summing repeated order values across item rows.

### AQ-ORDER-003

**Business Process:** Order Completion

**Question:** What proportion of orders reach the defined completed state?

**Purpose:** Understand successful order completion.

**Required Grain:** Order

**Potential Dimensions:** Date, geography, seller

**Potential Measures:** Completed orders and qualifying orders

**Source Dependency:** Verified order-status semantics.

### AQ-ORDER-004

**Business Process:** Order Lifecycle

**Question:** How does order status distribution change over time?

**Purpose:** Understand the composition of the order lifecycle.

**Required Grain:** Order

**Potential Dimensions:** Date, order status

**Source Dependency:** Verified status values.

## 5. Customer Questions

### AQ-CUST-001

**Business Process:** Customer Establishment

**Question:** How many customers are represented in the verified source population?

**Purpose:** Establish the customer population available for analysis.

**Required Grain:** Customer

**Potential Measures:** Distinct customer count

**Source Dependency:** Verified customer identifier.

### AQ-CUST-002

**Business Process:** Order Placement

**Question:** How many orders does each customer place?

**Purpose:** Understand purchasing frequency.

**Required Grain:** Customer aggregated from orders.

**Potential Measures:** Order count

### AQ-CUST-003

**Business Process:** Order Placement

**Question:** What is the distribution of customer purchasing activity?

**Purpose:** Understand customer purchasing behavior.

**Required Grain:** Customer

**Potential Measures:** Order count, revenue, units purchased

### AQ-CUST-004

**Business Process:** Repeat Purchasing

**Question:** What proportion of qualifying customers place more than one order?

**Purpose:** Analyze repeat customer behavior.

**Required Grain:** Customer

**Potential Measures:** Repeat customers and qualifying customers

**Source Dependency:** Verified customer and order relationship.

### AQ-CUST-005

**Business Process:** Customer Activity

**Question:** Which customer geographies generate the greatest commercial activity?

**Purpose:** Understand geographic distribution of customers and transactions.

**Required Grain:** Customer or order depending on question definition.

**Potential Dimensions:** Geography

**Potential Measures:** Customer count, order count, revenue

**Source Dependency:** Verified geography mapping.

## 6. Product Questions

### AQ-PROD-001

**Business Process:** Product Discovery / Order Item Processing

**Question:** Which products generate the highest revenue?

**Purpose:** Identify commercially significant products.

**Required Grain:** Order item aggregated to product.

**Potential Measures:** Revenue

### AQ-PROD-002

**Business Process:** Order Item Processing

**Question:** Which products generate the highest unit volume?

**Purpose:** Understand product demand.

**Required Grain:** Order item aggregated to product.

**Potential Measures:** Units sold

### AQ-PROD-003

**Business Process:** Order Item Processing

**Question:** Which product categories have the highest order-item volume?

**Purpose:** Understand category demand.

**Required Grain:** Order item.

**Potential Measures:** Order-item count or units sold, depending on verified source semantics.

### AQ-PROD-004

**Business Process:** Review

**Question:** Which products have the highest review activity?

**Purpose:** Understand products receiving significant customer feedback.

**Required Grain:** Review.

**Potential Measures:** Review count

### AQ-PROD-005

**Business Process:** Review

**Question:** How do review scores vary across products or categories?

**Purpose:** Analyze customer feedback patterns.

**Required Grain:** Review aggregated by product/category.

**Potential Measures:** Average review score, review count

**Source Dependency:** Verified review score semantics.

## 7. Seller Questions

### AQ-SELLER-001

**Business Process:** Seller Activity

**Question:** Which sellers generate the greatest sales value?

**Purpose:** Understand seller commercial contribution.

**Required Grain:** Order item aggregated to seller.

**Potential Measures:** Revenue

### AQ-SELLER-002

**Business Process:** Seller Activity

**Question:** Which sellers process the greatest order-item volume?

**Purpose:** Understand seller commercial activity.

**Required Grain:** Order item.

**Potential Measures:** Units sold, order-item count

### AQ-SELLER-003

**Business Process:** Seller Activity

**Question:** How does seller performance vary across product categories?

**Purpose:** Compare seller activity by assortment category.

**Required Grain:** Order item aggregated by seller and category.

**Potential Measures:** Revenue, units sold

### AQ-SELLER-004

**Business Process:** Delivery

**Question:** How does delivery performance vary across sellers?

**Purpose:** Understand seller-associated delivery outcomes where source relationships permit.

**Required Grain:** Delivery/order.

**Potential Measures:** Delivery duration, delayed deliveries

**Source Dependency:** Verified delivery and seller relationship.

## 8. Payment Questions

### AQ-PAY-001

**Business Process:** Payment

**Question:** What payment methods are used most frequently?

**Purpose:** Understand payment-method distribution.

**Required Grain:** Payment.

**Potential Measures:** Payment record count, order count where appropriate.

### AQ-PAY-002

**Business Process:** Payment

**Question:** How does payment activity vary over time?

**Purpose:** Understand financial transaction activity.

**Required Grain:** Payment.

**Potential Dimensions:** Date, payment method.

**Potential Measures:** Payment amount, payment count.

### AQ-PAY-003

**Business Process:** Payment

**Question:** What is the relationship between payment activity and order activity?

**Purpose:** Identify differences between order and payment grains.

**Required Grain:** Order and payment.

**Source Dependency:** Verified payment cardinality.

## 9. Delivery Questions

### AQ-DEL-001

**Business Process:** Delivery

**Question:** What is the average delivery duration?

**Purpose:** Understand delivery performance.

**Required Grain:** Order/delivery lifecycle.

**Potential Measures:** Delivery duration.

**Source Dependency:** Verified order and delivery timestamps.

### AQ-DEL-002

**Business Process:** Delivery

**Question:** What proportion of qualifying deliveries are delayed?

**Purpose:** Measure delivery exceptions.

**Required Grain:** Delivery/order.

**Potential Measures:** Delayed deliveries and qualifying deliveries.

**Source Dependency:** Verified estimated and actual delivery dates.

### AQ-DEL-003

**Business Process:** Delivery

**Question:** How does delivery performance vary by geography?

**Purpose:** Identify geographic delivery patterns.

**Required Grain:** Delivery/order aggregated by geography.

**Potential Measures:** Average delivery duration, delay rate.

### AQ-DEL-004

**Business Process:** Delivery

**Question:** How does delivery performance vary over time?

**Purpose:** Identify changes in operational delivery performance.

**Required Grain:** Delivery/order.

**Potential Dimensions:** Date.

## 10. Review Questions

### AQ-REV-001

**Business Process:** Customer Review

**Question:** What is the average review score over time?

**Purpose:** Monitor customer feedback trends.

**Required Grain:** Review.

**Potential Measures:** Average review score.

### AQ-REV-002

**Business Process:** Customer Review

**Question:** Which products receive the greatest review volume?

**Purpose:** Identify products generating substantial customer feedback.

**Required Grain:** Review.

**Potential Measures:** Review count.

### AQ-REV-003

**Business Process:** Customer Review / Delivery

**Question:** Is review performance different for orders with different delivery outcomes?

**Purpose:** Explore the relationship between delivery experience and customer feedback.

**Required Grain:** Review joined to verified order/delivery context.

**Source Dependency:** Valid review-to-order relationship and delivery attributes.

This is an analytical relationship, not a causal claim.

## 11. Geography Questions

### AQ-GEO-001

**Business Process:** Order Placement

**Question:** Which customer geographies generate the greatest order volume?

**Required Grain:** Order aggregated by customer geography.

**Potential Measures:** Order count.

### AQ-GEO-002

**Business Process:** Order Item Processing

**Question:** Which geographies generate the greatest sales value?

**Required Grain:** Order item aggregated by customer geography.

**Potential Measures:** Revenue.

### AQ-GEO-003

**Business Process:** Delivery

**Question:** Which geographies experience the greatest delivery delay rate?

**Required Grain:** Delivery/order.

**Potential Measures:** Delayed deliveries, qualifying deliveries.

**Source Dependency:** Verified geography and delivery fields.

## 12. Cross-Domain Questions

### AQ-CROSS-001

**Question:** How does customer geography relate to sales activity?

**Domains:** Customer, Geography, Orders, Order Items

### AQ-CROSS-002

**Question:** How does product category relate to seller sales performance?

**Domains:** Product, Category, Seller, Order Items

### AQ-CROSS-003

**Question:** How does delivery performance vary with seller activity?

**Domains:** Seller, Orders, Delivery

### AQ-CROSS-004

**Question:** How does review performance vary across product categories?

**Domains:** Product, Category, Review

### AQ-CROSS-005

**Question:** How do payment methods vary across order activity?

**Domains:** Payment, Orders

### AQ-CROSS-006

**Question:** How does order activity vary across customer geographies and time?

**Domains:** Customer, Geography, Orders, Date

## 13. Analytical Question Grain Rules

The following grain controls apply:

| Question Type | Primary Grain |
|---|---|
| Customer population | Customer |
| Order volume | Order |
| Revenue from line items | Order Item |
| Units sold | Order Item |
| Payment activity | Payment |
| Review activity | Review |
| Delivery performance | Delivery / Order |
| Seller performance | Seller / Order Item |
| Product performance | Product / Order Item |
| Geography sales | Order / Order Item |
| Repeat customer analysis | Customer |

Grain must be explicitly resolved before implementation.

## 14. Analytical Evidence Requirements

Analytical questions may require:

- business identifiers
- dates and timestamps
- entity relationships
- monetary measures
- quantity measures
- status values
- geography attributes
- payment attributes
- delivery dates
- review scores
- product/category relationships
- seller relationships

The actual availability of these fields must be established during source discovery and profiling.

## 15. Unsupported-Question Rule

If the selected source does not contain sufficient evidence to answer a question, RetailIQ must not fabricate the result.

The question must instead be classified as:

- Source Supported
- Partially Supported
- Source Unsupported
- Requires Derived Logic

The classification will be finalized after source discovery.

## 16. Double-Counting Protection

Analytical implementation must prevent:

- order-level revenue being multiplied by order items
- payment amounts being multiplied through order joins
- review counts being multiplied through product or order joins
- customer measures being duplicated across transactions
- delivery measures being duplicated across lifecycle records

Every implemented metric must preserve its declared grain.

## 17. Question-to-Later-Engineering Traceability

Analytical questions will later trace to:

Analytical Question
→ Source Evidence
→ Data Contract
→ Staging Attribute
→ Intermediate Transformation
→ Fact / Dimension
→ Data Mart
→ Governed Metric
→ BI Data Product
→ Test

This traceability will be established progressively in later areas.

## 18. Source Verification Boundary

No question in this document should be interpreted as confirmation that the selected dataset supports the required evidence.

Source verification begins in Area 04.

## 19. Physical Modeling Boundary

This catalog does not define:

- fact tables
- dimension tables
- physical schemas
- surrogate keys
- SCD implementation
- SQL transformations
- indexes
- partitions
- clustering
- materializations
- BI dashboards

Those decisions belong to later engineering areas.

## 20. Assumptions

- Orders represent commercial transactions.
- Order items represent lower-grain commercial activity than orders.
- Customers can be related to orders.
- Products can be related to order items.
- Sellers can be related to commercial activity.
- Payment and review records may have different grains.
- Delivery performance can only be measured if required timestamps exist.

## 21. Unknowns

- Exact source fields
- Exact source grain
- Exact revenue definition
- Exact quantity definition
- Exact payment semantics
- Exact review semantics
- Exact delivery semantics
- Exact status semantics
- Availability of returns/refunds
- Availability of behavioral data
- Availability of historical attributes

## 22. Initial Question Inventory

The current catalog contains analytical questions covering:

- Sales
- Orders
- Customers
- Products
- Sellers
- Payments
- Delivery
- Reviews
- Geography
- Cross-domain analysis

The catalog is intentionally source-independent until Area 04.

## 23. Artifact Completion Criteria

This artifact is complete when:

1. Analytical questions cover the major business domains.
2. Questions are linked to business processes.
3. Questions have explicit conceptual grain.
4. Required analytical evidence is documented.
5. Source dependencies are explicit.
6. Double-counting risks are documented.
7. Unsupported-question handling is defined.
8. Physical modeling remains outside scope.
9. Assumptions and unknowns are explicit.
10. Questions can later be traced to implemented analytical products.

## 24. Status

This artifact is currently **Draft**.

It must be validated together with `process-analysis.md` before Area 03 acceptance.
