# RetailIQ — Source Dataset Discovery

## Document Status
- Area: 04 — Source Dataset Discovery
- Artifact: Source Discovery
- Status: Discovery Verified — Candidate Pending Local Acquisition and Use-License Review
- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Primary Engineering Identity: Data Engineering
- Physical Modeling Boundary: Deferred to later areas

## 1. Purpose

This document records the discovery-level evaluation of the candidate source dataset for the RetailIQ modern data warehouse and analytics engineering platform.

The purpose of this artifact is to establish source identity, provenance, publisher context, documented dataset scope, expected source structure, source capabilities, limitations, licensing information, and traceability to the analytical requirements established in Area 03.

This document does not establish physical data-quality results. Actual row counts, null rates, duplicate rates, cardinalities, value distributions, schema verification, and relationship validation require acquisition of the source files and are deferred to Area 05 — Source Data Profiling.

## 2. Candidate Source Dataset

### Dataset
- Dataset name: Brazilian E-Commerce Public Dataset by Olist
- Publisher: Olist
- Primary discovery source: Kaggle
- Dataset URL: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Dataset type: Public historical e-commerce dataset
- Historical period documented by the publisher: 2016–2018
- Dataset-level description: Approximately 100,000 orders with product, customer, payment, seller, delivery and review-related information
- Current Kaggle data explorer metadata: 9 files are exposed by the dataset

### Discovery Assessment

The Olist Brazilian E-Commerce Public Dataset is a suitable provisional source candidate for RetailIQ because its documented subject areas cover the principal e-commerce domains required by the Area 03 analytical-question catalogue.

Candidate status is intentionally not treated as final source acceptance at this stage. Local acquisition, file integrity verification, physical profiling, relationship validation, and licensing/use review must be completed before the source is frozen as the implementation source.

## 3. Publisher and Provenance

The dataset is published as the Brazilian E-Commerce Public Dataset by Olist through Kaggle.

The publisher describes the dataset as real Brazilian e-commerce data that has been anonymized. The documented dataset context covers orders and associated customer, product, seller, payment, delivery and review information.

The source represents historical e-commerce activity rather than a live operational feed. The documented historical period is 2016–2018.

Source provenance chain:

Olist → Kaggle public dataset publication → RetailIQ source acquisition → Raw/Landing layer → Staging → Intermediate transformations → Warehouse facts and dimensions → Data marts → Governed metrics → BI-ready data products

## 4. Documented Source File Inventory

The current dataset publication exposes the following nine source files:

1. olist_customers_dataset.csv
2. olist_geolocation_dataset.csv
3. olist_order_items_dataset.csv
4. olist_order_payments_dataset.csv
5. olist_order_reviews_dataset.csv
6. olist_orders_dataset.csv
7. olist_products_dataset.csv
8. olist_sellers_dataset.csv
9. product_category_name_translation.csv

These filenames represent the documented source structure discovered during Area 04.

Physical file existence, file size, encoding, column names, row counts, data types, nullability, duplicate behavior, key uniqueness, and relationship integrity will be verified from the acquired files in Area 05.

## 5. Documented Source Domains

Based on the publisher's documented dataset description and source file structure, the candidate source covers the following conceptual domains:

- Customers
- Orders
- Order items
- Payments
- Products
- Sellers
- Reviews
- Product category translation
- Geographic reference information

These domains provide source evidence for the principal RetailIQ analytical areas defined in Area 03.

## 6. Expected Source-Level Grain

The following are discovery-level conceptual expectations derived from the documented source structure. They are not yet physical-model assertions.

| Source Dataset | Expected Conceptual Grain | Physical Verification |
|---|---|---|
| olist_customers_dataset.csv | One customer record per source customer identifier | Area 05 |
| olist_geolocation_dataset.csv | Geographic reference record associated with source geographic information | Area 05 |
| olist_order_items_dataset.csv | One order-item / seller line associated with an order | Area 05 |
| olist_order_payments_dataset.csv | One payment record associated with an order/payment sequence | Area 05 |
| olist_order_reviews_dataset.csv | One review record associated with an order/review event | Area 05 |
| olist_orders_dataset.csv | One source order record per order identifier | Area 05 |
| olist_products_dataset.csv | One product record per source product identifier | Area 05 |
| olist_sellers_dataset.csv | One seller record per source seller identifier | Area 05 |
| product_category_name_translation.csv | One source category-name translation mapping where represented | Area 05 |

Important boundary: these grains are discovery hypotheses based on documented source structure. They must not be treated as validated warehouse grain.

## 7. Source Capabilities Relevant to RetailIQ

The candidate source can support discovery of analytical requirements involving:

- Order activity
- Order-item sales activity
- Product analysis
- Customer analysis
- Seller analysis
- Payment analysis
- Delivery lifecycle analysis
- Review and customer-feedback analysis
- Geography-related analysis
- Cross-domain e-commerce analysis

The source therefore provides a reasonable foundation for the analytical domains and business questions established in Area 03.

## 8. Source Limitations and Boundaries

The source is historical rather than a live production operational source.

The documented dataset covers a historical period and therefore cannot by itself establish current e-commerce market conditions or current Olist operational behavior.

The dataset is anonymized. Direct real-world customer or seller identity reconstruction is outside the intended analytical boundary.

The source documentation does not by itself establish every business rule required by the RetailIQ warehouse. Business rules, fact grain, dimensional behavior, metric definitions, and derived analytical logic must be established through later engineering areas.

Actual source completeness, consistency, duplicate behavior, relationship integrity, timestamp quality, and other data-quality characteristics remain unknown until physical profiling is performed.

## 9. Area 03 Analytical Requirement Coverage

The source candidate provides documented subject areas corresponding to the following Area 03 analytical domains:

| Area 03 Domain | Candidate Source Evidence | Verification Status |
|---|---|---|
| Sales | Orders, order items, products, sellers, payments | Discovery-level coverage identified |
| Orders | Orders and order items | Discovery-level coverage identified |
| Customers | Customers and orders | Discovery-level coverage identified |
| Products | Products, order items, category translation | Discovery-level coverage identified |
| Sellers | Sellers and order items | Discovery-level coverage identified |
| Payments | Order payments | Discovery-level coverage identified |
| Delivery | Orders and delivery-related order attributes | Discovery-level coverage identified |
| Reviews | Order reviews | Discovery-level coverage identified |
| Geography | Customer, seller and geolocation information | Discovery-level coverage identified |
| Cross-Domain | Relationships among orders, customers, products, sellers, payments, delivery and reviews | Discovery-level coverage identified |

Coverage in this table means that the source documentation indicates relevant subject matter exists. It does not mean that every Area 03 analytical question has already been physically verified as answerable.

## 10. Source Verification Boundary

Area 04 establishes:

- Source identity
- Publisher
- Dataset provenance
- Documented historical scope
- Documented file inventory
- Discovery-level conceptual domains
- Discovery-level expected grain
- Source capabilities
- Source limitations
- Licensing information
- Initial traceability to Area 03 requirements

Area 04 does not establish:

- Actual local row counts
- Actual local file sizes
- Actual column definitions
- Actual data types
- Actual null percentages
- Actual duplicate counts
- Actual key uniqueness
- Actual cardinalities
- Actual referential integrity
- Actual value distributions
- Actual data-quality defects
- Final warehouse grain
- Final fact or dimension design
- Final SCD strategy
- Final metric implementation

Those controls begin with physical acquisition and profiling in Area 05 and subsequent modeling areas.

## 11. Licensing and Use Constraint

The Kaggle publication currently identifies the dataset license as Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

License reference: https://creativecommons.org/licenses/by-nc-sa/4.0/

The license requires attribution, restricts commercial use, and includes ShareAlike requirements for adaptations as described by Creative Commons.

Because RetailIQ is intended as a professional portfolio project, the practical use and publication implications of the license must be reviewed and documented before final source acceptance.

No conclusion is made here about the legal status of any particular portfolio, employment, commercial, or deployment use. The project must preserve attribution and clearly document the source license and any applicable use constraints.

## 12. Discovery Decision

Current decision:

PROVISIONAL CANDIDATE — DISCOVERY VERIFIED

The Olist Brazilian E-Commerce Public Dataset is retained as the primary candidate source for the next source-engineering stage.

Final source acceptance remains pending:

1. Local acquisition of the published source files.
2. Physical file and schema verification.
3. Source profiling.
4. Relationship and dependency verification.
5. Data-quality assessment.
6. Confirmation that the source supports the required analytical questions.
7. Documented review of the CC BY-NC-SA 4.0 licensing constraints for the intended portfolio use.

## 13. Assumptions

- The Kaggle publication is the discovery reference for the candidate dataset.
- The documented historical period is treated as 2016–2018 until physical source metadata confirms the relevant date fields.
- The nine currently documented source files are treated as the discovery inventory.
- Expected grains are hypotheses and require physical validation.
- Source documentation is not treated as proof of physical data quality.
- Analytical requirements remain those frozen in Area 03.

## 14. Unknowns

- Exact locally acquired row counts.
- Exact locally acquired file sizes.
- Exact physical schema and data types.
- Null and missing-value behavior.
- Duplicate behavior.
- Key uniqueness.
- Referential integrity.
- Actual source cardinalities.
- Actual timestamp coverage.
- Actual business-value distributions.
- Which source records require transformation or reconciliation.
- Final source-to-warehouse mappings.
- Final implications of the dataset license for the intended portfolio distribution model.

## 15. Physical Modeling Boundary

No physical warehouse schema is finalized by this document.

Facts, dimensions, surrogate keys, natural keys, SCD behavior, staging models, intermediate models, marts, metrics, and BI-ready structures will be designed only after source profiling and dependency validation.

## 16. Artifact Completion Criteria

This artifact is complete when:

- Source identity is documented.
- Publisher and provenance are documented.
- Source URL is documented.
- Historical scope is documented.
- Documented source files are inventoried.
- Discovery-level conceptual domains are documented.
- Expected source grain is explicitly marked as unverified.
- Source capabilities and limitations are documented.
- Area 03 analytical coverage is mapped.
- Licensing information is documented.
- Source verification boundaries are explicit.
- Assumptions and unknowns are explicit.
- Physical modeling is explicitly deferred.

## 17. References

- Kaggle — Brazilian E-Commerce Public Dataset by Olist: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Creative Commons — CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/
- Olist official website: https://olist.com/

## Document Control

- Created for: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Area: 04
- Artifact: source-discovery.md
- Status: Discovery Verified — Candidate Pending Local Acquisition and Use-License Review
- Next dependency: Area 05 — Source Data Profiling
