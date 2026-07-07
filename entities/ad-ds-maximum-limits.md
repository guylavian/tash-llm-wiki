---
title: Active Directory DS Maximum Limits and Scalability
type: entity
domain: active-directory
slug: ad-ds-maximum-limits
summary: AD DS imposes hard limits on objects (≈2.15 billion DNTs per DC lifetime), SIDs (≈2.15 billion RIDs per domain), group members (~5,000 pre-LVR; virtually unlimited post-LVR), and various name lengths that administrators must plan for.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/active-directory-domain-services-maximum-limits (Microsoft Learn — Active Directory Domain Services Maximum Limits and Scalability, fetched 2026-06-18)
  - kb:ad-ds-active-directory-domain-services-maximum-limits
  - kb:ad-ds-how-ldap-server-cookies-are-handled
provenance_extracted: 24
provenance_inferred: 4
provenance_ambiguous: 1
symptoms:
  - "000020EF: SvcErr: DSID-0208044C, problem 5012 (DIR_ERROR), data -1076 — DNT limit reached on DC"
  - "Event ID 16656 (Directory-Services-SAM) — RID pool within 1% of global RID space"
  - "0x00000b: LDAP_ADMIN_LIMIT_EXCEEDED — nonlinked attribute limit exceeded on an object"
  - "Error <49>: ldap_simple_bind_s() failed: Invalid Credentials — DN exceeds 255 chars in simple bind"
tags: [directory-services, troubleshooting, concept]
status: draft
updated: 2026-07-02
---

# Active Directory DS Maximum Limits and Scalability

**AD DS has hard and recommended limits across objects, identifiers, names, groups, and policy objects that planners and operators must track to avoid production failures.**

## Object limit (DNTs)

Each DC can create at most **2,147,483,393** objects (2^31 − 255) over its lifetime. Distinguished Name Tags (DNTs) are DC-local, monotonically increasing identifiers; deleted objects free their DNT but it is never reused. The limit applies to the aggregate across all partitions hosted on the DC (domain, configuration, schema, application).

When the DNT limit is reached:
```
Error: Add: Operations Error. <1> Server error: 000020EF: SvcErr: DSID-0208044C, problem 5012 (DIR_ERROR), data -1076.
```

Check headroom via `approximateHighestInternalObjectID` on rootDSE (requires Windows Server 2012+). Workarounds: permanently delete objects, or promote a new DC that replicates remaining objects (do not use IFM — it inherits DNT values from the source DC).

## RID / SID limit

The global RID pool per domain holds at most **2,147,483,647 RIDs**. RIDs are not reused after deletion. When available RIDs drop to **10% remaining**, DCs begin preparing an artificial throttle; at **1% remaining**, Event ID 16656 appears in the System log. RIDs are allocated in blocks of 500 from the RID Master.

Demoted DCs leave their unused allocated RIDs stranded — those RIDs cannot return to the pool.

## Group membership — the 5,000 caveat

**Windows 2000 forests:** Recommended maximum of **5,000 members** per group. This is a database transaction size limit for non-linked multivalued attributes (all group member values must fit in one database record page per write).

**Windows Server 2003 forest functional level and higher:** Linked Value Replication (LVR) was introduced. LVR stores each group membership link as a separate replicable unit, removing the 5,000-member ceiling. Production environments have exceeded **4 million members**; Microsoft scalability testing reached **500 million members**. (inferred) The 5,000-member warning persists in some tooling documentation and is commonly misquoted as an absolute limit — it is not, once LVR is active.

Important caveat: members added **before** raising the functional level to Windows Server 2003+ must be removed and re-added to become LVR-enabled. Mixed membership (some LVR, some not) is allowed.

## ACL / DACL entries

The maximum entries in a DACL or SACL on an AD object is constrained by a 64 KB ACL size limit. Because ACEs can include GUIDs, the practical maximum is **1,100 to 1,820 entries**.

## Security principal group membership (token)

A security principal can be a member of at most **1,015 groups**. This is an access token size limit, not a database limit, and is not affected by group nesting. Kerberos tickets also have a recommended maximum of **48,000 bytes** (`MaxTokenSize`); large group memberships bloat the PAC and can exceed token limits, causing authentication failures — see [[securing-active-directory]].

## GPO limit per user/computer

A user or computer account can have at most **999 GPOs** applied. This is a processing performance guard, not a raw object count limit.

## Trust path depth

Kerberos clients can traverse at most **10 trust links** to reach a resource in another domain. Performance degrades noticeably beyond **2,400 Trusted Domain Objects (TDOs)** in a forest.

## Nonlinked attribute values per object

- Pre-Windows Server 2025 forests: ~**1,200 nonlinked attribute values** per object.
- Windows Server 2025 forests: up to ~**3,200 values** (with 32k page format); the nonlinked attribute record limit also rises to ~3,000 under Windows Server 2025 functional level.

Error when the limit is hit: `LDAP_ADMIN_LIMIT_EXCEEDED (0x00000b)`.

## Name length limits

| Name type | Limit |
|---|---|
| FQDN (total) | 64 characters |
| NetBIOS computer / domain name | 15 characters |
| DNS host name | 24 characters |
| OU name | 64 characters |
| Display name (schema) | 256 characters |
| Common name (schema) | 64 characters |
| SAM-Account-Name (effective) | 20 characters (users) |
| LDAP simple bind DN | 255 characters |
| File paths (NTDS.dit, SYSVOL) | 260 characters (MAX_PATH) |

## LDAP transaction / paged search

Recommended maximum: **5,000 operations per LDAP transaction**. Exceeding this risks resource timeouts and full transaction rollback.

The LDAP server cookie pool (paged search) defaults: MinResultSets=4, MaxResultSetSize=262,144 bytes, MaxResultSetsPerConn=10. Events 2898 and 2899 fire when limits are hit.

## Contradictions / caveats

- The 5,000 group membership warning is widely misunderstood. It is a **soft recommendation** for pre-LVR (Windows 2000 forest functional level) and has no hard limit under LVR — but it appears in Microsoft documentation in both contexts, which causes confusion. (ambiguous — the source itself qualifies: "recommended maximum" in Windows 2000, then states LVR removes the limit)
- The DNT limit is per-DC, not per-forest. A new DC has its full DNT range regardless of how many objects exist.
- The recommended maximum of 1,200 domain controllers per domain is a SYSVOL recovery constraint, not a technical hard limit.

## Reference notes
- [[ad-ds-active-directory-domain-services-maximum-limits]]
- [[ad-ds-how-ldap-server-cookies-are-handled]]

## See also
- [[active-directory-overview]]
- [[ad-database-and-32k-pages]]
- [[rid-issuance-management]]
- [[security-groups]]
- [[securing-active-directory]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-active-directory-domain-services-maximum-limits|Active Directory Domain Services Maximum Limits and Scalability]]
- [[ad-ds-how-ldap-server-cookies-are-handled|How LDAP server cookies are handled]]
<!-- crosslink:end -->
