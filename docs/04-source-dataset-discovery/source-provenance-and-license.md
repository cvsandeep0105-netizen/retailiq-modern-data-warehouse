# RetailIQ — Source Provenance and License

## Document Status
- Area: 04 — Source Dataset Discovery
- Artifact: Source Provenance and License
- Status: Discovery Control — License Constraint Documented; Final Use Review Pending
- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Candidate ID: SRC-001
- Physical Modeling Boundary: Deferred

## 1. Purpose

This document establishes the provenance record and licensing control for the RetailIQ source dataset candidate.

The objective is to ensure that source origin, publisher attribution, publication location, documented license, required license controls, intended engineering use, and unresolved use questions are explicitly recorded before physical source acquisition and later portfolio publication.

This document is not legal advice and does not determine whether a specific commercial, employment, portfolio, hosting, or distribution scenario is legally permitted.

## 2. Source Provenance

| Provenance Attribute | Recorded Value |
|---|---|
| Candidate ID | SRC-001 |
| Dataset | Brazilian E-Commerce Public Dataset by Olist |
| Publisher | Olist |
| Publication Platform | Kaggle |
| Historical Period | 2016–2018 |
| Dataset Type | Public historical e-commerce dataset |
| Discovery Source | Kaggle dataset publication |
| License Identified | CC BY-NC-SA 4.0 |

Primary dataset reference:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

License reference:

https://creativecommons.org/licenses/by-nc-sa/4.0/

## 3. Provenance Chain

The documented provenance chain for RetailIQ is:

Olist source publication

→ Kaggle public dataset publication

→ RetailIQ source acquisition

→ Raw / Landing layer

→ Staging

→ Intermediate transformations

→ Warehouse facts and dimensions

→ Data marts

→ Governed metrics

→ BI-ready analytical data products

→ Engineering documentation and portfolio presentation

The RetailIQ engineering layers are derived analytical processing performed by this project. They must not be represented as the original source publication.

## 4. Publisher Context

The candidate dataset is associated with Olist and is published through Kaggle as the Brazilian E-Commerce Public Dataset by Olist.

The dataset describes historical Brazilian e-commerce activity and is presented as anonymized data.

Current Olist company information is treated separately from the historical dataset context. The current Olist website is not treated as evidence that the historical dataset represents current operational data.

Official Olist website:

https://olist.com/

## 5. Historical Scope

The publisher documentation identifies the dataset as covering activity from 2016 through 2018.

This historical scope is important for RetailIQ because analytical outputs must be described as analysis of the supplied historical source rather than current market or current operational reporting.

Any later analytical date coverage must be verified from the acquired source files during profiling.

## 6. License Identification

The Kaggle publication identifies the dataset license as:

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

Short form:

CC BY-NC-SA 4.0

Official Creative Commons license reference:

https://creativecommons.org/licenses/by-nc-sa/4.0/

## 7. License Controls Identified

Based on the Creative Commons license documentation, the following controls are recorded:

### Attribution

Attribution is required when using the licensed material.

RetailIQ must preserve clear attribution to the source dataset and provide an appropriate reference to the applicable license.

### NonCommercial

The license contains a non-commercial-use condition.

RetailIQ must therefore distinguish technical portfolio development from any use or distribution scenario that could constitute commercial use.

### ShareAlike

The license contains a ShareAlike condition for adaptations as described by the license.

Any adaptation or modified material must be evaluated against the applicable ShareAlike requirements before distribution.

### Changes

Where applicable, changes to the licensed material must be indicated as required by the license.

## 8. RetailIQ Attribution Control

The project documentation should identify the source using a statement equivalent in substance to:

Source: Brazilian E-Commerce Public Dataset by Olist, published through Kaggle. Licensed under CC BY-NC-SA 4.0.

The exact attribution presentation can be refined during final documentation and portfolio integration.

## 9. Intended Engineering Use

The candidate source is intended to support engineering activities including:

- Data ingestion experimentation.
- Raw and landing-layer design.
- Staging transformation.
- Data standardization.
- Deduplication and reconciliation.
- Dimensional modeling.
- Fact and dimension construction.
- Slowly changing dimension engineering.
- ELT and analytics engineering.
- Data marts.
- Governed analytical metrics.
- Data quality testing.
- Analytical SQL.
- BI-ready data products.
- Engineering documentation.
- Portfolio demonstration, subject to applicable license constraints.

## 10. Source Versus Derived Material

RetailIQ must distinguish between original source material and project-generated derived artifacts.

Examples of project-generated engineering artifacts include:

- Warehouse schemas.
- Transformation logic.
- Data models.
- Tests.
- Data-quality rules.
- Analytical SQL.
- Data marts.
- Metric definitions.
- Documentation.
- Architecture diagrams.
- Orchestration logic.
- Observability logic.
- Performance measurements.

The presence of project-generated engineering artifacts does not remove the need to evaluate the license obligations associated with the underlying source material.

## 11. Portfolio Publication Control

Before final public portfolio publication, the project must verify:

1. Source attribution is visible.
2. The dataset license is identified.
3. The license reference is available.
4. The historical nature of the dataset is accurately described.
5. The project does not describe the source as unrestricted.
6. Any distributed source-derived material is reviewed against the license terms.
7. Any transformed or adapted material is reviewed for applicable ShareAlike requirements.
8. Any commercial context is separately reviewed before publication or distribution.

## 12. Unresolved Use Questions

The following questions remain open until the intended distribution model is finalized:

- Whether the exact planned portfolio hosting arrangement qualifies as non-commercial under the applicable license terms.
- Whether any source files or transformed source-derived files will be redistributed publicly.
- Whether repository publication will contain original source data, subsets, extracts, or only code and documentation.
- Whether generated BI outputs contain source-derived material requiring additional license consideration.
- Whether any future commercial use of the project changes the applicable licensing analysis.

These questions are deliberately recorded rather than answered through unsupported assumptions.

## 13. Recommended Repository Data Boundary

For engineering control, the project should maintain a clear distinction between:

### Source Data

Downloaded source files obtained under the dataset's applicable license.

### Project Code

RetailIQ-owned ingestion, transformation, testing, orchestration and application code.

### Project Documentation

RetailIQ-owned engineering documentation containing appropriate source attribution and license references.

### Derived Analytical Data

Warehouse and mart outputs generated from the source. Their distribution must be evaluated against the applicable source-license requirements.

The repository should not silently include the original source dataset unless the intended distribution has been reviewed against the license terms.

## 14. Evidence Hierarchy

Source and license decisions should use the following evidence hierarchy:

1. Official Creative Commons license text and license deed for license terms.
2. Primary Kaggle dataset publication for dataset identity, publisher attribution, documented scope and license metadata.
3. Official Olist information for publisher/company context.
4. Secondary sources only when primary evidence is unavailable or requires corroboration.

Secondary sources must not override the primary source or license documentation.

## 15. Provenance Verification Boundary

Verified during Area 04:

- Candidate identity.
- Publisher identity as documented by the dataset publication.
- Kaggle publication reference.
- Historical dataset context.
- Documented nine-file inventory.
- License identification.
- Attribution requirement.
- Non-commercial condition.
- ShareAlike condition.
- Portfolio-use questions requiring later review.

Not yet verified during Area 04:

- Physical file hashes.
- Downloaded file integrity.
- Actual local file metadata.
- Physical schema.
- Actual row counts.
- Actual data quality.
- Actual source relationships.
- Actual transformation requirements.
- Final repository data-distribution decision.

## 16. Assumptions

- Kaggle is treated as the primary discovery publication for the candidate.
- Creative Commons official documentation is treated as the primary license reference.
- The dataset license identified on the publication is treated as a material project constraint.
- The source remains historical data rather than a live operational feed.
- Final legal/use conclusions are outside the scope of this engineering artifact.

## 17. Unknowns

- Exact final portfolio distribution model.
- Whether original source files will be redistributed.
- Whether derived analytical outputs will be publicly distributed.
- Whether any future commercial use will occur.
- Exact license treatment required for each planned distribution mechanism.

## 18. Physical Modeling Boundary

This document does not define:

- Warehouse facts.
- Warehouse dimensions.
- Fact grain.
- Surrogate-key strategy.
- SCD implementation.
- Data marts.
- Metric implementation.
- Physical data-quality results.

Those concerns remain governed by later project areas.

## 19. Artifact Completion Criteria

This artifact is complete when:

- Source provenance is documented.
- Publisher context is documented.
- Historical scope is documented.
- Primary source reference is documented.
- License is identified.
- Attribution requirements are documented.
- Non-commercial condition is documented.
- ShareAlike condition is documented.
- Portfolio publication controls are documented.
- Unresolved licensing/use questions are explicitly recorded.
- Source and derived-material boundaries are documented.
- Evidence hierarchy is documented.
- Physical verification remains deferred.

## 20. References

- Kaggle — Brazilian E-Commerce Public Dataset by Olist: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Creative Commons — CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/
- Olist official website: https://olist.com/

## Document Control

- Project: RetailIQ — Modern Data Warehouse & Analytics Engineering Platform
- Area: 04
- Artifact: source-provenance-and-license.md
- Status: Discovery Control — License Constraint Documented; Final Use Review Pending
- Previous accepted artifacts: source-discovery.md; source-candidate-register.md
- Next dependency: Area 05 — Source Data Profiling
