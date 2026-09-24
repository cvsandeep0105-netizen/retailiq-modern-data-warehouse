# RetailIQ — Repository Security & Artifact Hygiene

## Status
- Status: Accepted & Frozen
- Area: 14.5
- Purpose: Define repository security controls and artifact-hygiene standards.

## 1. Repository Security Principles
- Repository content must be treated as controlled engineering assets.
- Security-sensitive material must not be committed.
- Access must follow least-privilege principles.
- Security controls must apply throughout the development lifecycle.

## 2. Secret Protection
Passwords, API keys, access tokens, private keys, certificates containing private material, and other secrets must never be committed to the repository.

Secrets must be supplied through protected environment or runtime mechanisms.

## 3. Sensitive Data Protection
Personal, confidential, regulated, or otherwise sensitive data must not be committed unless its inclusion is explicitly authorized and appropriately protected.

Production datasets must not be copied into the repository as ordinary development artifacts.

## 4. Source Dataset Hygiene
Source datasets must remain subject to their applicable license, provenance, security, and distribution restrictions.

Only permitted sample or derived data should be versioned when required for engineering reproducibility.

## 5. Generated Artifact Hygiene
Temporary files, local caches, build outputs, logs containing sensitive information, compiled artifacts, and uncontrolled generated files must not be committed.

Generated artifacts may be versioned only when they are explicitly designated as project deliverables.

## 6. Repository Ignore Controls
Repository ignore rules should exclude operating-system files, local environment files, caches, temporary outputs, secrets, and other non-versioned artifacts.

Ignore rules must not be used to conceal required production artifacts or security issues.

## 7. Credential Exposure Prevention
Before committing material changes, repository content should be checked for accidental credential or secret exposure.

If a credential is exposed, it must be treated as compromised and handled through the applicable security response process.

## 8. Dependency Artifact Hygiene
Dependency definitions and lock artifacts must be reviewed for unauthorized or unexpected changes.

Downloaded packages, local dependency caches, and environment-specific package directories must not be committed unless explicitly required.

## 9. Data and License Compliance
Repository artifacts derived from external datasets must preserve appropriate provenance and applicable usage constraints.

License requirements must be documented where relevant to project distribution or reuse.

## 10. Access and Repository Permissions
Repository access must follow the project's documented ownership and least-privilege principles.

Write or administrative permissions must be limited to authorized identities.

## 11. Security Incident Boundary
If sensitive information is accidentally committed, further distribution must stop and the affected material must be handled according to the applicable incident-response process.

Simply deleting the visible file is not sufficient if sensitive material has already entered version history.

## 12. Artifact Review
Material repository changes should be reviewed for unintended secrets, sensitive data, prohibited generated artifacts, unexpected dependencies, and license concerns.

## 13. Technology-Neutral Boundary
This artifact defines repository security and artifact-hygiene requirements. It does not mandate a specific secret scanner, security platform, Git provider, repository-hosting service, or compliance product.

## 14. Acceptance Boundary
The artifact is complete when repository security, secret protection, sensitive-data protection, dataset hygiene, generated-artifact hygiene, ignore controls, credential exposure prevention, dependency hygiene, license compliance, access permissions, incident handling, artifact review, and technology-neutral boundaries are explicitly documented.

## 15. Next Step
After 14.5 validation and acceptance, proceed to Area 14.6.

