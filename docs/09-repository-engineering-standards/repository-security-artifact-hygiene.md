# RetailIQ — Repository Security, Ignore Rules, Artifact Hygiene & Sensitive-File Protection

Document Status: Accepted & Frozen

## Purpose

Define repository security, ignore rules, artifact hygiene, sensitive-file protection, and source-control safeguards for the RetailIQ engineering repository.

## Repository Security Principles

- Repository contents must follow least-exposure principles.
- Sensitive information must never be committed to source control.
- Repository artifacts must have a defined engineering purpose.
- Temporary, generated, and local-only artifacts must remain outside authoritative source boundaries.
- Security-impacting changes must receive appropriate review and validation.

## Sensitive Information Boundary

The following must not be committed to the repository:
- Passwords
- API keys
- Access tokens
- Private keys
- Connection secrets
- Credential files
- Production secret values
- Personal authentication material

Sensitive values must be supplied through approved environment configuration or secret-management mechanisms.

## Ignore Rules

The repository must use appropriate ignore rules to prevent accidental inclusion of local-only and generated artifacts.

Ignore rules should cover applicable categories such as:
- Local environment files
- Secret files
- Runtime logs
- Caches
- Temporary files
- Build outputs
- IDE-specific files
- Operating-system metadata
- Large generated datasets where not explicitly approved

Ignore rules must not be used to hide authoritative source files, required tests, or required project documentation.

## Environment File Protection

Environment-specific secret files must remain outside source control.

Safe configuration templates may be committed when they contain placeholders rather than real credentials or secrets.

## Data Protection

Source and generated datasets must follow the project's approved data and licensing boundaries.

Original source data must not be unintentionally modified or replaced by generated outputs.

Sensitive or restricted datasets must not be committed without explicit approval.

## Artifact Hygiene

Repository contents must remain clean and purposeful.

Temporary debugging files, local exports, caches, generated logs, and obsolete artifacts must not accumulate inside authoritative repository boundaries.

Generated artifacts must be clearly distinguishable from source-controlled engineering assets.

## Secret Scanning

The repository should use secret-detection or equivalent validation mechanisms where available.

Potential secret exposure must be investigated before a change is accepted.

Removing a secret from the current working tree does not by itself establish that the secret was never exposed through repository history.

## Access Protection

Repository access must follow the environment access and permission boundaries defined in Area 08.

Repository permissions should be granted according to role and required responsibility.

## Branch Protection

The approved/default branch should be protected according to repository capabilities and project governance.

Direct uncontrolled changes to the protected branch should be avoided.

## Security Incident Boundary

If sensitive information is committed or exposed, the event must be treated as a security issue.

The response must include containment, credential rotation or revocation where applicable, impact assessment, repository remediation, and appropriate documentation.

## Review Requirements

Security-sensitive repository changes require review appropriate to their impact.

Review should consider secret exposure, dependency risk, data exposure, permission changes, and unintended repository artifacts.

## Evidence Source

Evidence sources include Area 08 access boundaries, Area 09.1–09.4 repository standards, repository configuration, ignore rules, security validation results, and approved engineering requirements.

## Acceptance Boundary

This artifact is accepted only when repository security, sensitive-file protection, ignore rules, data protection, artifact hygiene, secret scanning, access protection, branch protection, security incident handling, and review requirements are explicitly documented.

## Next Step

After acceptance, Area 09.6 will define repository documentation, README, contribution, and engineering handoff standards.

## Artifact Completion Criteria

- Repository security principles documented
- Sensitive information boundary documented
- Ignore rules documented
- Environment file protection documented
- Data protection documented
- Artifact hygiene documented
- Secret scanning documented
- Access protection documented
- Branch protection documented
- Security incident boundary documented
- Review requirements documented
- Acceptance boundary documented

