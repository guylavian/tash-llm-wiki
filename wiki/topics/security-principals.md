---
title: Security Principals
type: topic
domain: active-directory
slug: security-principals
summary: A security principal is any entity the OS can authenticate — user, computer, or group — each represented by a unique SID and used throughout Windows authorization and access control.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-principals (Microsoft Learn — Security Principals, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups (Microsoft Learn — Active Directory Security Groups, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts (Microsoft Learn — Active Directory Accounts, fetched 2026-06-18)
provenance_extracted: 7
provenance_inferred: 2
provenance_ambiguous: 0
tags: [directory-services, concept]
status: draft
updated: 2026-06-18
---

# Security Principals

**A security principal is any entity that the operating system can authenticate — a user account, a computer account, or a security group — and each one is represented by a unique security identifier (SID).**

## Body
Security principals are the foundation of access control in Windows and Active Directory. Each is assigned a unique [[security-identifiers-sid]] at creation that it keeps for its entire lifetime and that is never reused. The authorization flow turns these SIDs into access decisions: at sign-in the Local Security Authority (LSA) builds an **access token** containing the user's SID, the SIDs of the groups they belong to, and their user rights; when a thread touches a securable object, the OS compares the token's SIDs against the access control entries (ACEs) in that object's **security descriptor** (its DACL for access, SACL for auditing).

Principals come in two storage scopes (inferred — drawn together from the principals and accounts sections): **domain** principals are Active Directory objects managed by AD tools and replicated among domain controllers, while **local** principals live in the Security Accounts Manager (SAM) database on a single computer (every Windows machine except domain controllers). The kinds of principal are:

- **User accounts** — identify and authenticate a person (or a dedicated service account), and carry the rights/permissions that authorize resource access. See [[default-user-accounts]] for the built-in ones.
- **Computer accounts** — let a domain-joined machine authenticate and act on the network even with no user signed in.
- **Security groups** — collect users, computers, and other groups so rights and permissions can be assigned once to a unit rather than per account; see [[security-groups]].

A distinct flavor, **special identity groups**, represents dynamic sets of principals (Everyone, Authenticated Users, etc.) whose membership the OS controls and you cannot edit — see [[special-identity-groups]].

Permissions (attached to objects, expressed as ACEs) are different from **user rights** (assigned to accounts/groups, e.g. "Back up files and directories"). Using a group SID rather than many individual user SIDs in an ACL also keeps ACLs small and speeds up access checks (inferred — this is the operational rationale the groups note gives for group-based access control).

## Contradictions / caveats
- Local vs. domain principals are managed by completely different stores (SAM vs. AD); a local account's SID is unique only to its computer, whereas a domain principal's SID is unique across the whole forest.
- Group *scope* (domain-local / global / universal) applies only to real security groups, **not** to special identity groups — their scope concept does not exist.

## Reference notes
- [[ad-ds-understand-security-principals]]
- [[ad-ds-understand-security-groups]]
- [[ad-ds-understand-default-user-accounts]]

## See also
- [[security-identifiers-sid]]
- [[security-groups]]
- [[special-identity-groups]]
- [[default-user-accounts]]
- [[securing-active-directory]]
- [[fsmo-roles]]
