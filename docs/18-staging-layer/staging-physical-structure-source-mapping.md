# Area 18.2 — Staging Physical Structure & Source Mapping

Status: Accepted & Frozen

## 1. Purpose
Define the physical organization and source-to-staging mapping responsibilities for the RetailIQ staging layer.

## 2. Staging Physical Organization
Staging structures must provide a controlled, consistent, and traceable representation of validated raw source data before intermediate and analytical transformations.

## 3. Source-Oriented Mapping
Each accepted raw source object must have an explicit mapping into its corresponding staging representation.

## 4. Olist Source Object Mapping
The staging boundary must account for all nine Olist source objects: customers, geolocation, order_items, order_payments, order_reviews, orders, products, sellers, and product_category_name_translation.

## 5. Source-to-Staging Identity
Source object identity, source record identifiers, and ingestion batch identity must remain traceable after staging.

## 6. Staging Naming Standards
Staging objects must follow the repository naming, schema naming, and artifact ownership standards established in Area 09 and the detailed repository engineering controls established in Area 14.

## 7. Staging Schema Boundary
Staging schemas must remain distinct from raw, intermediate, dimensional, fact, metric, and data-mart structures.

## 8. Source Column Mapping
Source columns must have an explicit mapping to staging columns, including controlled handling of renamed, typed, or standardized fields.

## 9. Data Type Mapping
Staging data types must provide reliable downstream processing while preserving source meaning and traceability.

## 10. Timestamp Mapping
Source date and timestamp fields must be mapped consistently into staging while preserving the original source semantics.

## 11. Nullability Mapping
Source nullability expectations must be preserved or explicitly documented when staging representation requires technical changes.

## 12. Identifier Mapping
Business identifiers and source identifiers must remain available for downstream relationship, reconciliation, and lineage controls.

## 13. Relationship Mapping
Source relationships established in Area 06 must remain representable within staging without inventing or silently repairing relationships.

## 14. Duplicate Boundary
Staging physical organization must distinguish source-observed duplicate conditions from duplicates introduced by processing.

## 15. Batch and Load Metadata
Staging records or load controls must retain sufficient metadata to associate staged data with its originating ingestion batch and raw source.

## 16. Processing State
Staging processing must provide controlled processing states such as received, processed, rejected, failed, or otherwise approved operational states where required.

## 17. Reconciliation Support
Physical staging organization must support reconciliation between accepted raw inputs and staged outputs.

## 18. Environment Separation
Staging structures must respect development, test, and production environment boundaries established in Area 08, together with the detailed environment controls established in Area 13.

## 19. Storage Architecture Dependency
Physical staging organization must follow the storage and schema responsibilities established in Area 10 and the detailed storage and schema implementation controls established in Area 15.

## 20. Repository Standards Dependency
Staging definitions, mappings, scripts, documentation, and configuration must follow repository ownership and engineering standards established in Areas 09 and 14.

## 21. Security Boundary
Staging structures and metadata must follow approved access, ownership, security, and artifact-hygiene controls.

## 22. Lineage Boundary
Source-to-staging mappings must support lineage from source acquisition through raw data, staging representation, and downstream processing.

## 23. Technology Evaluation Dependency
Physical implementation must remain consistent with the technology evaluation boundary established in Area 12 without prematurely selecting an implementation technology.

## 24. Technology-Neutral Boundary
This artifact defines physical organization and source-mapping responsibilities without selecting a specific warehouse, storage engine, cloud platform, orchestration tool, or transformation framework.

## 25. Next Step
After Area 18.2 validation and acceptance, proceed sequentially to the next approved Area 18 sub-area.



