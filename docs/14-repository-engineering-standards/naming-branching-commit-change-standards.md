# RetailIQ — Naming, Branching, Commit & Change Standards

## Status
- Status: Accepted & Frozen
- Area: 14.3
- Purpose: Define consistent standards for naming, branching, commits, pull requests, and engineering changes.

## 1. Naming Principles
- Names must be descriptive, consistent, predictable, and aligned with repository responsibilities.
- Names should communicate the purpose of the artifact without unnecessary abbreviations.
- Naming conventions must be applied consistently across related artifacts.

## 2. Directory Naming
Directories must use a predictable naming convention and should clearly represent their engineering responsibility.

Area-specific documentation directories must preserve the numbered project sequence where the project roadmap requires it.

## 3. File Naming
Files must use descriptive names that identify their purpose and artifact type.

File names should avoid spaces and ambiguous abbreviations where practical.

## 4. Branching Principles
Branches must represent a specific engineering purpose such as feature development, defect correction, documentation change, or controlled maintenance.

Long-lived branches should be minimized unless a documented engineering reason requires them.

## 5. Branch Naming
Branch names should communicate the change purpose and remain consistent across the repository.

Recommended branch naming patterns:
- feature/<short-purpose>
- fix/<short-purpose>
- docs/<short-purpose>
- chore/<short-purpose>

## 6. Commit Principles
Commits must represent a coherent engineering change.

Commits should avoid mixing unrelated features, fixes, refactoring, generated files, and documentation changes unless they form one inseparable change.

## 7. Commit Message Standard
Commit messages must clearly describe the engineering change.

Recommended commit message structure:
- <type>: <short imperative description>

Examples:
- feat: add customer dimension model
- fix: correct order revenue transformation
- docs: update warehouse architecture
- test: add order grain regression checks

## 8. Pull Request / Change Review
Material changes should be reviewed according to repository governance requirements.

A change review should identify the purpose, affected components, validation performed, data-impact considerations, and relevant documentation updates.

## 9. Change Scope
Changes must remain focused on the approved engineering objective.

Unrelated modifications must not be introduced merely because a file or component is being changed.

## 10. Breaking Changes
Changes that alter interfaces, schemas, contracts, analytical semantics, or downstream behavior must be explicitly identified and documented.

Breaking changes require appropriate downstream-impact validation before release.

## 11. Documentation Changes
Architecture, contracts, operational procedures, and other material documentation must be updated when implementation changes make existing documentation inaccurate.

## 12. Validation Before Commit
Before committing a material change, the responsible engineer should verify formatting, relevant tests, validation results, documentation consistency, and repository security hygiene.

## 13. Change Traceability
Material changes must be traceable from the implementation revision to the associated engineering requirement, issue, decision, or documented purpose where applicable.

## 14. Technology-Neutral Boundary
This artifact defines naming, branching, commit, and change-management standards. It does not mandate a specific Git hosting service, pull-request platform, issue tracker, or CI/CD product.

## 15. Acceptance Boundary
The artifact is complete when naming, directory and file conventions, branching, commit messages, review, change scope, breaking changes, documentation changes, validation, traceability, and technology-neutral boundaries are explicitly documented.

## 16. Next Step
After 14.3 validation and acceptance, proceed to Area 14.4.

