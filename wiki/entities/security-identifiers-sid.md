---
title: Security Identifiers (SID)
type: entity
domain: active-directory
slug: security-identifiers-sid
summary: A SID is a variable-length binary value that uniquely identifies a security principal or group within Windows; it is created once, never reused, and embedded in every access token and ACE.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers (Microsoft Learn — Security Identifiers, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-principals (Microsoft Learn — Security Principals, fetched 2026-06-18)
  - kb:ad-ds-understand-security-identifiers
  - kb:ad-ds-understand-security-principals
provenance_extracted: 18
provenance_inferred: 3
provenance_ambiguous: 0
tags: [directory-services, ad-authn, concept]
status: draft
updated: 2026-07-02
---

# Security Identifiers (SID)

**A SID is a unique, immutable identifier issued by an authority (LSA for local accounts, a domain controller for domain accounts) that represents a security principal for the lifetime of that principal.**

## SID Structure

A SID is stored in binary but represented in string notation as:

```
S-R-X-Y1-Y2-Yn-1-Yn
```

| Component | Meaning |
|---|---|
| S | Literal "SID" marker |
| R | Revision level (always 1 today) |
| X | Identifier authority (e.g. 5 = NT Authority) |
| Y1…Yn-1 | Domain identifier — differentiates domains in a forest |
| Yn (RID) | Relative Identifier — uniquely identifies the account within a domain |

Example — built-in Administrators: `S-1-5-32-544`
- Revision 1, NT Authority (5), Builtin domain (32), RID 544.

Example — Domain Admins in a domain: `S-1-5-21-<domain>-512`
- Domain identifier `21-<three subauthority values>`, RID 512.

## RID Allocation and the RID Master

In a multi-DC domain, generating unique RIDs is a single-master operation. The [[fsmo-roles]] **RID Master** allocates blocks of RIDs to each domain controller; each DC consumes from its own block when creating new objects, then requests another block when running low. This prevents duplicate SIDs across DCs without locking. (inferred — synthesised from the description of the multi-master account database and the single-master RID allocation process.)

## SID History

When a user account moves between domains, a **new SID** is generated for the new domain and written to `ObjectSID`. The old SID is appended to the `SIDHistory` attribute. During Kerberos/NTLM authentication, all SIDs in `SIDHistory` are loaded into the access token, preserving resource access across the domain move without changing ACLs. (inferred — SIDHistory mechanics are described across the SID and principals reference notes but not summarised together in either one.)

## Well-Known SIDs

Well-known SIDs are constant across all Windows installations and identify generic users or groups. Key examples:

| SID | Name | Notes |
|---|---|---|
| S-1-1-0 | Everyone | Interactive, network, dial-up, and authenticated users |
| S-1-5-7 | Anonymous Logon | Not a member of Everyone (since Windows Server 2003) |
| S-1-5-11 | Authenticated Users | Any principal authenticated via a sign-in process; excludes Guest |
| S-1-5-18 | SYSTEM (LocalSystem) | OS processes; hidden member of Administrators |
| S-1-5-domain-500 | Administrator | Built-in admin account in every domain |
| S-1-5-domain-501 | Guest | Built-in guest account |
| S-1-5-domain-502 | KRBTGT | KDC service account, exists only on DCs |
| S-1-5-32-544 | Administrators (builtin) | Built-in Administrators local group |

See [[special-identity-groups]] for the full set of OS-managed special identity SIDs.

## GUIDs vs SIDs

Active Directory stores both. The `ObjectGUID` (128-bit, globally unique, never changes) is used for internal AD replication and object lookup. The `ObjectSID` can change when an object moves between domains. Searching by `ObjectGUID` is the most reliable way to locate an object when its SID or name may have changed. (inferred — neither source states this comparison explicitly in one place, but both establish the properties independently.)

## Capability SIDs

Windows 8 / Windows Server 2012 introduced capability SIDs (prefix `S-1-15-3-*`) that grant Universal Windows Applications access to specific resources. Stored in `HKLM\SOFTWARE\Microsoft\SecurityManager\CapabilityClasses\AllCachedCapabilities`.

## Contradictions / caveats
- A SID is unique within its scope: domain SIDs are unique enterprise-wide, local SIDs are unique only to the issuing machine.
- Deleted accounts' SIDs are never reused — a new account for the same person gets a new SID and inherits no prior ACL permissions unless `SIDHistory` is used.
- Starting with Windows Server 2008/Vista, `TrustedInstaller` (not LocalSystem) owns most OS files; a process running as LocalSystem or Administrators cannot auto-replace them.

## Reference notes
- [[ad-ds-understand-security-identifiers]]
- [[ad-ds-understand-security-principals]]

## See also
- [[security-principals]]
- [[security-groups]]
- [[fsmo-roles]]
- [[special-identity-groups]]
- [[securing-active-directory]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-understand-security-identifiers|Security Identifiers]]
- [[ad-ds-understand-security-principals|Security Principals]]
<!-- crosslink:end -->
