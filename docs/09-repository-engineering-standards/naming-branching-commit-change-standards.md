# RetailIQ — Repository Naming, Branching, Commit & Change-Management Standards

Document Status: Accepted & Frozen

## Purpose

Define consistent naming, branching, commit, pull-request, review, and change-management practices for the RetailIQ repository.

## Naming Principles

- Names must be descriptive, predictable, and consistent.
- Names must communicate the purpose of the artifact.
- Avoid ambiguous abbreviations and temporary names in accepted artifacts.
- Naming conventions must remain consistent across related directories and files.

## Directory Naming

Documentation directories must preserve the numbered Area convention established by the project.

Implementation directories should use lowercase, descriptive names and avoid unnecessary nesting.

## File Naming

Documentation files should use descriptive lowercase names with hyphens where appropriate.

Source-code filenames should follow the conventions of the selected programming language or framework.

Temporary files must not be presented as authoritative project artifacts.

## Branching Standard

Git branches must represent a defined unit of engineering work.

Branch names should communicate the purpose of the change and avoid personal or ambiguous naming.

The default branch represents the approved repository baseline.

Direct changes to the protected/default branch should be controlled according to repository policy.

## Branch Scope

A branch should contain a coherent and reviewable change.

Unrelated feature changes should not be combined into the same branch without an explicit reason.

## Commit Standard

Commits must represent meaningful engineering changes.

Commit messages should clearly communicate the change and its purpose.

Commits should avoid including unrelated temporary changes.

## Commit Traceability

Material engineering changes should be traceable from the repository history to the relevant requirement, issue, area, or engineering decision where applicable.

## Pull Request / Review Standard

Material repository changes should be reviewed before integration when the repository workflow supports pull requests.

Review should consider correctness, scope, testing, security, maintainability, and compatibility with accepted architecture.

## Change Classification

Changes should be classified according to their impact.

Representative categories include:
- Documentation-only
- Bug fix
- Data-model change
- Transformation change
- Configuration change
- Test change
- Infrastructure or deployment change
- Security or access-control change

## Frozen-Area Protection

Accepted and frozen project areas must not be modified as part of unrelated work.

A frozen area may be reopened only when a concrete defect, dependency, factual inconsistency, or approved change requirement is established.

## Change Validation

Changes must be validated against the affected engineering boundary before acceptance.

Validation must include appropriate regression checks when a change can affect previously accepted functionality.

## Release Boundary

Only validated and approved repository changes may enter a release or production deployment path.

Development-only experiments must not be promoted as production-ready artifacts without validation.

## Rollback Consideration

Material changes should have a practical rollback or recovery strategy appropriate to their impact.

## Evidence Source

Evidence sources include Git repository practices, accepted Area 09.1 and 09.2 standards, Area 08 environment boundaries, and approved project engineering requirements.

## Acceptance Boundary

This artifact is accepted only when naming, branching, commit, review, change classification, frozen-area protection, validation, release, and rollback standards are explicitly documented.

## Next Step

After acceptance, Area 09.4 will define repository dependency, environment configuration, and reproducibility standards.

## Artifact Completion Criteria

- Naming principles documented
- Directory naming documented
- File naming documented
- Branching standard documented
- Branch scope documented
- Commit standard documented
- Commit traceability documented
- Review standard documented
- Change classification documented
- Frozen-area protection documented
- Change validation documented
- Release boundary documented
- Rollback consideration documented
- Acceptance boundary documented

