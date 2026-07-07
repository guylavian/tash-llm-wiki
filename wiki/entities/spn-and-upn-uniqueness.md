---
title: SPN and UPN Uniqueness
type: entity
domain: active-directory
slug: spn-and-upn-uniqueness
summary: The forest-wide constraint, enforced by Windows Server 2012 R2+ DCs, that each Service Principal Name and User Principal Name must be unique — duplicate values cause Kerberos authentication failures and Entra ID sync breaks.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/SPN-and-UPN-uniqueness (Microsoft Learn — SPN and UPN uniqueness, fetched 2026-06-18)
  - kb:ad-ds-spn-and-upn-uniqueness
provenance_extracted: 16
provenance_inferred: 3
provenance_ambiguous: 0
symptoms:
  - "8467"
  - "8648"
  - "0x21c7"
  - "0x21c8"
  - "ERROR_DS_SPN_VALUE_NOT_UNIQUE_IN_FOREST"
  - "ERROR_DS_UPN_VALUE_NOT_UNIQUE_IN_FOREST"
  - "event id 2974"
  - "Duplicate SPN found, aborting operation"
  - "the logon name you have chosen is already in use"
  - "excessive LSASS CPU"
tags: [ad-authn, security, directory-services, troubleshooting]
status: draft
updated: 2026-07-02
---

# SPN and UPN Uniqueness

**Windows Server 2012 R2 DCs enforce forest-wide uniqueness for Service Principal Names (SPNs) and User Principal Names (UPNs) — duplicate values are blocked at the write point and cause Kerberos auth failures or Entra ID sync breaks if they already exist.**

## Body

### Why uniqueness matters

| Attribute | Consequence of duplicates |
|-----------|--------------------------|
| **UPN** (`userPrincipalName`) | Breaks synchronization with Microsoft Entra ID / Office 365; users may be unable to log in to cloud services. |
| **SPN** (`servicePrincipalName`) | Kerberos mutual authentication requires an SPN to map to exactly one account; a duplicate means the KDC cannot resolve which secret to use — authentication fails and LSASS CPU spikes on the DC. |

### Enforcement (Windows Server 2012 R2+)

When a Windows Server 2012 R2 or later DC processes a write:

- **If the DC is a Global Catalog (GC):** the check queries the local forest-wide UPN/SPN index directly. Write is blocked if the value exists.
- **If the DC is not a GC:** the DC submits an LDAP query to the closest GC. If no GC is reachable, the check falls back to the local DIT only — a best-effort check that can still allow duplicates in degraded connectivity (inferred — stated as "best-effort" in the source).

Blocked writes produce:

| Code (decimal) | Hex | Symbolic | Meaning |
|---------------|-----|----------|---------|
| 8647 | `0x21C7` | `ERROR_DS_SPN_VALUE_NOT_UNIQUE_IN_FOREST` | Duplicate SPN blocked |
| 8648 | `0x21C8` | `ERROR_DS_UPN_VALUE_NOT_UNIQUE_IN_FOREST` | Duplicate UPN blocked |

**Event ID 2974** (`ActiveDirectory_DomainService`) is logged listing the blocked value and up to 10 conflicting objects.

### Tooling behavior

- **`setspn.exe -S`**: duplicate check built-in since Windows Server 2008.
- **`setspn.exe -A`**: bypasses the duplicate check — still blocked by a WS2012 R2 DC.
- **`ADSIEdit`, `PowerShell Set-ADUser`, `DSAC.exe`**: all return the same error codes when targeting a WS2012 R2 DC.

### SPN auto-update triggers

When the following attributes are modified, AD automatically deletes obsolete SPNs and reconstructs new ones; the new values are also subject to the uniqueness check:

- `dNSHostName`, `msDS-AdditionalDnsHostName`
- `sAMAccountName`, `msDS-AdditionalSamAccountName`
- `serverReferenceBL`, `userAccountControl`

### Finding and resolving duplicates

**Identify UPN in deleted objects:**
```
repadmin /showattr <DC> "CN=Deleted Objects,DC=..." /subtree /filter:"(msDS-LastKnownRDN=<NAME>)" /deleted /atts:userprincipalname
```

**Find all objects with a conflicting UPN:**
```
Get-ADObject -LdapFilter "(userPrincipalName=conflict@domain.com)" -IncludeDeletedObjects -SearchScope Subtree
```

To restore a deleted object whose UPN conflicts with a live object, null out the duplicate UPN on one of the live objects first; no event is logged when a restore fails silently due to UPN conflict — check manually.

### Relationship to Recycle Bin and object restore

When a deleted object in the [[ad-recycle-bin]] is reanimated, its SPN and UPN values are re-validated against the forest-wide index. If a live object acquired the same value after deletion, the restore fails. No event is logged for this path (inferred — the source notes the absence of an event log entry specifically for restore failure).

## Contradictions / caveats

- In a **mixed domain** (some DCs pre-2012 R2, some 2012 R2+), writes processed by down-level DCs bypass the uniqueness check entirely. Duplicates can accumulate until all DCs are upgraded — audit with `repadmin` or PowerShell proactively.
- In a **[[disjoint-namespace]]** environment, an SPN registered with the AD domain FQDN may not match the service's DNS-advertised FQDN in the disjoint zone, producing Kerberos auth failures even when no true duplicate exists — the root cause is a name mismatch, not a uniqueness violation.
- Reviewing Event ID 2974 regularly is the recommended proactive control; Microsoft recommends this as a monitoring practice.

## Reference notes
- [[ad-ds-spn-and-upn-uniqueness]]

## See also
- [[dns-for-ad-ds]]
- [[dc-locator]]
- [[disjoint-namespace]]
- [[ad-recycle-bin]]
- [[security-principals]]
- [[group-managed-service-accounts]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-spn-and-upn-uniqueness|SPN and UPN uniqueness]]
<!-- crosslink:end -->
