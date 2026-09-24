# RetailIQ — Source Candidate Register

## Document Status
- Area: 04 — Source Dataset Discovery
- Artifact: Source Candidate Register
- Status: Provisional Candidate Registered — Final Source Acceptance Pending
- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Physical Modeling Boundary: Deferred

## 1. Purpose

This register records the candidate source selected for RetailIQ and the objective discovery evidence used to determine whether the candidate should proceed to physical acquisition and profiling.

The register is a source-discovery control artifact. It does not replace physical source profiling, relationship validation, data-quality assessment, or final licensing review.

## 2. Registered Candidate

| Attribute | Candidate |
|---|---|
| Candidate ID | SRC-001 |
| Dataset | Brazilian E-Commerce Public Dataset by Olist |
| Publisher | Olist |
| Publication Platform | Kaggle |
| Source Type | Public historical e-commerce dataset |
| Historical Period | 2016–2018 |
| Documented Order Scale | Approximately 100,000 orders |
| Documented File Count | 9 |
| License | CC BY-NC-SA 4.0 |
| Current Status | Provisional Candidate |
| Physical Verification | Pending Area 05 |

## 3. Source Identity

Dataset title:

Brazilian E-Commerce Public Dataset by Olist

Primary source reference:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The source is published as a public historical Brazilian e-commerce dataset associated with Olist.

## 4. Candidate File Inventory

The documented candidate inventory contains:

- olist_customers_dataset.csv
- olist_geolocation_dataset.csv
- olist_order_items_dataset.csv
- olist_order_payments_dataset.csv
- olist_order_reviews_dataset.csv
- olist_orders_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv
- product_category_name_translation.csv

Physical file existence and physical schema remain subject to verification after acquisition.

## 5. Business-Domain Coverage

The candidate provides documented source subject areas corresponding to the RetailIQ business domain established in Areas 02 and 03.

| Business Domain | Candidate Evidence | Discovery Status |
|---|---|---|
| Customer | Customer dataset and order relationships | Documented |
| Product | Product and order-item datasets | Documented |
| Order | Order dataset and order items | Documented |
| Payment | Order payment dataset | Documented |
| Seller | Seller and order-item datasets | Documented |
| Delivery | Order delivery-related attributes | Documented |
| Review | Order review dataset | Documented |
| Geography | Customer, seller and geolocation information | Documented |

## 6. Analytical Requirement Coverage

The candidate maps to the analytical domains frozen in Area 03.

| Area 03 Analytical Domain | Candidate Source Coverage | Status |
|---|---|---|
| Sales | Orders, order items, products, sellers, payments | Candidate coverage identified |
| Orders | Orders and order items | Candidate coverage identified |
| Customers | Customers and orders | Candidate coverage identified |
| Products | Products, order items and category translation | Candidate coverage identified |
| Sellers | Sellers and order items | Candidate coverage identified |
| Payments | Order payments | Candidate coverage identified |
| Delivery | Orders and delivery-related attributes | Candidate coverage identified |
| Reviews | Order reviews | Candidate coverage identified |
| Geography | Customer, seller and geolocation information | Candidate coverage identified |
| Cross-Domain | Multiple source domains linked through source identifiers | Candidate coverage identified |

Coverage indicates discovery-level subject-matter alignment. It does not establish that every analytical question is physically answerable.

## 7. Candidate Evaluation Criteria

### 7.1 Business Relevance

Assessment: Candidate aligns with the e-commerce business processes and analytical domains defined for RetailIQ.

Status: PASS — Discovery evidence

### 7.2 Source Realism

Assessment: Publisher documentation describes the dataset as real Brazilian e-commerce data that has been anonymized.

Status: PASS — Publisher-documented

### 7.3 Historical Analytical Value

Assessment: The documented 2016–2018 historical period provides a defined time range for analytical engineering and historical reporting.

Status: PASS — Discovery evidence

### 7.4 Multi-Domain Coverage

Assessment: The documented source structure contains customer, order, item, product, seller, payment, review and geographic subject areas.

Status: PASS — Discovery evidence

### 7.5 Analytics Engineering Suitability

Assessment: The candidate contains multiple related source domains suitable for staging, transformation, dimensional modeling, fact construction, marts and governed analytical outputs.

Status: PROVISIONAL — Physical relationships require Area 05 and subsequent modeling validation

### 7.6 Historical Modeling Suitability

Assessment: The source contains time-oriented order and delivery information that can be evaluated for historical analytical modeling.

Status: PROVISIONAL — Physical timestamp behavior requires Area 05 verification

### 7.7 Data Quality Suitability

Assessment: No positive or negative physical data-quality conclusion is made during discovery.

Status: PENDING — Area 05

### 7.8 Source Accessibility

Assessment: The dataset is publicly discoverable through Kaggle.

Status: PASS — Discovery evidence

### 7.9 Licensing

Assessment: The dataset is currently identified as CC BY-NC-SA 4.0.

Status: CONSTRAINT IDENTIFIED — Intended portfolio use requires documented license review

## 8. Candidate Strengths

Discovery-level strengths include:

- Broad e-commerce business-domain coverage.
- Multiple related source datasets.
- Historical order and transaction context.
- Product, customer and seller subject areas.
- Payment and review information.
- Delivery-related information.
- Geographic information.
- Public discoverability.
- Anonymized dataset context.
- Suitable subject matter for warehouse and analytics engineering experimentation.

These observations are source-discovery characteristics and are not a final assessment of physical data quality.

## 9. Candidate Limitations

Known discovery-level limitations include:

- Historical rather than live operational data.
- Limited historical period documented by the publisher.
- Anonymized source data.
- Physical source quality has not yet been profiled.
- Physical relationships have not yet been independently verified.
- Current local file contents have not yet been validated.
- Licensing imposes attribution, non-commercial and ShareAlike requirements.

## 10. License Control

The source publication currently identifies the dataset as CC BY-NC-SA 4.0.

License reference:

https://creativecommons.org/licenses/by-nc-sa/4.0/

Required controls identified during discovery:

- Attribution must be preserved.
- Commercial use restrictions must be considered.
- ShareAlike requirements must be considered for adaptations.
- Portfolio publication and distribution must be reviewed against the applicable license terms.

This register records the license constraint but does not provide legal advice or make a legal determination about a particular use case.

## 11. Verification Dependencies

Final source acceptance depends on:

1. Successful acquisition of the source files.
2. File integrity verification.
3. Physical schema discovery.
4. Source data profiling.
5. Key and relationship verification.
6. Data-quality assessment.
7. Analytical-question coverage validation.
8. Source-to-warehouse dependency mapping.
9. Licensing/use review for the intended portfolio distribution.

## 12. Candidate Decision

Decision:

PROVISIONAL CANDIDATE — PROCEED TO PHYSICAL SOURCE ACQUISITION AND PROFILING

Rationale:

The documented source structure aligns with the RetailIQ e-commerce business domain and the analytical requirements established in Area 03. The source contains multiple related business domains required for modern warehouse and analytics engineering.

Final acceptance is intentionally deferred until physical acquisition, profiling, relationship verification and licensing/use review are completed.

## 13. Assumptions

- Kaggle remains the primary discovery reference for the candidate dataset.
- Publisher-documented source characteristics are treated as discovery evidence until independently verified.
- The nine documented files constitute the current discovery inventory.
- Physical characteristics are unknown until acquisition and profiling.
- Area 03 analytical requirements remain frozen.

## 14. Unknowns

- Actual local row counts.
- Actual local file sizes.
- Physical column definitions.
- Physical data types.
- Null behavior.
- Duplicate behavior.
- Key uniqueness.
- Relationship integrity.
- Actual timestamp coverage.
- Actual analytical-question coverage after profiling.
- Final license implications for the exact portfolio distribution approach.

## 15. Physical Modeling Boundary

This register does not establish final warehouse facts, dimensions, grains, surrogate keys, natural keys, SCD strategies, marts or metrics.

Those decisions require evidence from physical source profiling and subsequent modeling areas.

## 16. Artifact Completion Criteria

This artifact is complete when:

- Candidate identity is recorded.
- Candidate provenance is recorded.
- Candidate file inventory is recorded.
- Business-domain coverage is mapped.
- Area 03 analytical coverage is mapped.
- Candidate evaluation criteria are documented.
- Strengths and limitations are documented without unsupported quality claims.
- Licensing constraints are recorded.
- Verification dependencies are explicit.
- Candidate decision is explicitly provisional.
- Physical modeling remains deferred.

## 17. References

- Kaggle — Brazilian E-Commerce Public Dataset by Olist: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Creative Commons — CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/
- Olist official website: https://olist.com/

## Document Control

- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Area: 04
- Artifact: source-candidate-register.md
- Status: Provisional Candidate Registered — Final Source Acceptance Pending
- Previous accepted artifact: source-discovery.md
- Next artifact: source-provenance-and-license.md
