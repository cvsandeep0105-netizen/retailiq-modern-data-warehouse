# RetailIQ — Raw / Landing Physical Structure & Source Ingestion Organization

## Status
- Status: Accepted & Frozen
- Area: 16.2
- Purpose: Define the physical organization of raw and landing data and the controlled organization of source ingestion without prematurely binding the design to a specific platform.

## 1. Physical Organization Principles
Raw and landing storage must be organized so that source identity, ingestion events, processing state, and preserved source data remain distinguishable.

Physical organization must support traceability, replayability, validation, lifecycle management, and controlled downstream consumption.

## 2. Source-Oriented Organization
Source data should be organized using stable source identifiers and source-object identifiers rather than relying only on ingestion timestamps.

For the Olist dataset, each of the nine source files must remain individually identifiable within the raw / landing organization.

## 3. Source Object Boundaries
The source objects are:
- olist_customers_dataset.csv
- olist_geolocation_dataset.csv
- olist_order_items_dataset.csv
- olist_order_payments_dataset.csv
- olist_order_reviews_dataset.csv
- olist_orders_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv
- product_category_name_translation.csv

Each source object must retain its source identity through ingestion and downstream lineage.

## 4. Landing Intake Organization
Landing intake should provide a controlled location or logical namespace for newly received source inputs before acceptance into the preserved raw representation.

Unvalidated or failed inputs must remain distinguishable from accepted raw data.

## 5. Accepted Raw Organization
Accepted raw data should be organized separately from transient landing inputs.

The organization must make it possible to identify the source object, ingestion event, processing status, and applicable source version or acquisition identity.

## 6. Ingestion Batch Identity
Every ingestion execution must have a distinguishable batch or execution identity.

Batch identity must support correlation between source input, ingestion metadata, validation results, rejected inputs, and downstream processing.

## 7. File and Object Identity
Physical source objects must retain sufficient identity information to distinguish different acquisitions of the same logical source object.

File names or equivalent object identifiers must not be the sole mechanism for lineage when repeated acquisitions are possible.

## 8. Ingestion Metadata Organization
Technical metadata should be maintained in a controlled structure associated with each ingestion event.

At minimum, metadata should support source identity, source object identity, ingestion timestamp, batch identifier, processing status, record or file outcome, and error information where applicable.

## 9. Processing State Organization
Processing state must distinguish at least the concepts of received, accepted, rejected, processed, and failed where those states are applicable to the implementation.

State transitions must be traceable and must not silently overwrite the history of an ingestion event.

## 10. Rejected Input Organization
Rejected source inputs must be isolated from accepted raw data while remaining available for controlled investigation and reprocessing.

Rejection records should identify the source object, ingestion event, rejection reason, and processing outcome.

## 11. Replay Organization
Replay processing must use identifiable source inputs and execution identities.

A replay must not silently appear as a new business source acquisition.

Downstream processing must be able to distinguish replay activity from ordinary ingestion activity where required for auditability.

## 12. Source Preservation Organization
Preserved raw data must remain as close as reasonably practical to the acquired source representation.

Transformations such as business enrichment, deduplication, dimensional modeling, and analytical calculations must not be performed in the preserved raw representation.

## 13. Partitioning and Physical Segmentation
Where the selected technology supports physical partitioning or equivalent segmentation, it may be used to organize data by source, ingestion period, batch, or another justified access pattern.

Partitioning decisions must be based on measured workload, data volume, operational behavior, and lifecycle requirements rather than assumed performance benefits.

## 14. Schema Organization
Raw and landing schemas or equivalent namespaces must remain distinct from staging, intermediate, dimensional, mart, semantic, and BI consumption namespaces.

Namespace organization must remain consistent with the logical layer responsibilities established in Area 15.2.

## 15. Environment Organization
Development, validation/test, and production raw / landing structures must remain appropriately isolated.

Environment-specific configuration and access must follow the environment boundaries established in Area 13.

## 16. Access Organization
Access to raw and landing structures must follow least-privilege principles.

Technical ingestion identities should receive only the permissions required for ingestion and metadata operations.

Business-facing consumers should not receive unnecessary direct access to raw / landing structures.

## 17. Lifecycle Organization
Landing and raw objects must have documented lifecycle behavior covering retention, archival, cleanup, and controlled deletion where applicable.

Lifecycle operations must preserve required replay, reconciliation, lineage, and auditability capabilities.

## 18. Storage and Metadata Separation
Source data and ingestion-control metadata may be physically separated when this improves ownership, security, performance, or operational clarity.

Physical separation must not break the logical relationship between source data and its ingestion metadata.

## 19. Technology Evaluation Dependency
Physical implementation choices must remain consistent with the evidence-based technology evaluation established in Area 12.

Technology-specific implementation details must be documented after the applicable technology decision is established.

## 20. Validation Requirements
The physical organization must be validated for source completeness, source-object identity, ingestion traceability, state handling, rejection isolation, replayability, access boundaries, and lifecycle behavior.

Validation evidence must be retained as part of the project's engineering evidence.

## 21. Technology-Neutral Boundary
This artifact defines physical organization and ingestion-organization responsibilities. It does not select a specific database, warehouse, cloud storage service, object-storage product, ingestion platform, or partitioning technology.

## 22. Acceptance Boundary
The artifact is complete when physical source organization, source-object boundaries, landing intake, accepted raw organization, batch identity, object identity, metadata, processing states, rejection handling, replay, preservation, segmentation, schemas, environments, access, lifecycle, metadata separation, technology dependency, and validation requirements are explicitly defined.

## 23. Next Step
After 16.2 validation and acceptance, proceed to Area 16.3 — Raw Ingestion Metadata, Batch Control & Traceability.

