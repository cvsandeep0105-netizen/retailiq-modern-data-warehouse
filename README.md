# RetailIQ — Modern Data Warehouse & Analytics Engineering Platform

## Project 03 — Production-Style Modern Data Warehouse + Analytics Engineering Platform

RetailIQ is an end-to-end modern data warehouse and analytics engineering platform built around the Olist Brazilian E-Commerce Public Dataset.

## Engineering Focus

- Modern Data Warehousing
- ELT and Analytics Engineering
- Dimensional Modeling
- Fact and Dimension Design
- Slowly Changing Dimensions
- Incremental Processing
- Data Quality Engineering
- Automated Testing
- Business Data Marts
- Semantic / Business Layer
- Analytical SQL
- BI-Ready Data Products
- Data Lineage and Documentation
- Governance and Security
- Observability
- Performance and Scalability
- CI/CD
- Streamlit BI Dashboard

## Architecture

`	ext
Olist Source Data
      |
      v
RAW / LANDING
      |
      v
STAGING
      |
      v
INTERMEDIATE / CORE
      |
      v
DIMENSIONAL DATA WAREHOUSE
      |
      v
BUSINESS DATA MARTS
      |
      v
SEMANTIC / BUSINESS LAYER
      |
      v
BI-READY DATA PRODUCTS
      |
      v
RETAILIQ STREAMLIT DASHBOARD
`

## Validated Source Data

| Dataset | Records |
|---|---:|
| Customers | 99,441 |
| Geolocation | 1,000,163 |
| Orders | 99,441 |
| Order Items | 112,650 |
| Payments | 103,886 |
| Reviews | 99,224 |
| Products | 32,951 |
| Sellers | 3,095 |
| Translation | 71 |

Original source CSV files are intentionally excluded from this repository.

## Dimensional Warehouse Model

### Dimensions

- dim_customer
- dim_product
- dim_seller
- dim_date

### Facts

- act_orders
- act_order_items
- act_payments
- act_reviews

## Business Data Marts

- Sales
- Customer
- Product
- Seller / Fulfillment

## Semantic Layer

- KPI Summary
- Business KPIs
- Sales Analysis
- Customer Analysis
- Product Analysis
- Seller / Fulfillment Analysis

## Analytical SQL

- Monthly Sales
- Category Performance
- Customer Segmentation
- Seller Fulfillment
- Delivery Analysis
- Payment Analysis
- Review Analysis
- Window-function analysis

## Data Quality

`	ext
DATA_QUALITY_CHECKS=34
DATA_QUALITY_FAILURES=0
`

## Validation Evidence

`	ext
CI_STATUS=PASS
E2E_STATUS=PASS
SCALABILITY_FAILURES=0
LOCAL_PRODUCTION_STYLE_VALIDATION=PASS
PERFORMANCE_QUERIES=5
PERFORMANCE_AVG_MS=2405.857
PERFORMANCE_MAX_MS=6057.035
SCALABILITY_EXECUTIONS=15
SCALABILITY_FAILURES=0
SCALABILITY_QPS=1.27
`

## RetailIQ Dashboard

The Streamlit BI product contains six pages:

1. Executive Overview
2. Sales Analytics
3. Customer Analytics
4. Product Analytics
5. Seller & Fulfillment
6. Platform Health

Run the complete demonstration:

`powershell
.\\scripts\\demo.ps1
`

The demonstration validates the platform and automatically launches the dashboard.

Dashboard URL:

http://127.0.0.1:8501/

## Technology Stack

Python, SQL, PostgreSQL, Pandas, SQLAlchemy, psycopg2, Pytest, Streamlit, Git, GitHub, PowerShell, Docker and CI/CD validation.

## Engineering Principles

- Preserve source-data integrity.
- Separate raw, staging, core, warehouse, mart, semantic and BI layers.
- Define business grain before implementation.
- Use explicit keys and documented relationships.
- Make transformations reproducible.
- Validate every major engineering layer.
- Treat data quality as an engineering requirement.
- Keep secrets and source datasets outside version control.
- Prefer measurable evidence over unsupported claims.

## Project Status

`	ext
AREAS 01-50: FROZEN
LOCAL VALIDATION: PASS
DATA QUALITY: PASS
INTEGRATION TESTING: PASS
E2E VALIDATION: PASS
DASHBOARD: PASS
CLOUD PRODUCTION DEPLOYMENT: NOT CLAIMED
GITHUB PUBLICATION: IN PROGRESS
ENGINEERING REPORT: PENDING
PORTFOLIO INTEGRATION: PENDING
`

## Portfolio Projects

- Project 01 — Enterprise AI-Powered Real-Time EV Fleet Data Platform
- Project 02 — Cloud-Native Lakehouse, CDC & AI-Ready Data Platform
- Project 03 — RetailIQ Modern Data Warehouse & Analytics Engineering Platform

## Source Data Notice

The original Olist dataset remains subject to its published source license. Original source CSV files are intentionally excluded from this repository.

---

**Professional Focus:** Data Engineering + Cloud Data Platforms + Analytics Engineering + AI-enabled Data Systems


---

## Author

**Sandeep Reddy**

Data Engineer | Modern Data Warehousing | Analytics Engineering

GitHub: https://github.com/cvsandeep0105-netizen
