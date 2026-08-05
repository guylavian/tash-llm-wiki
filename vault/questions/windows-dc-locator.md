---
title: How Windows clients locate a suitable domain controller
type: question
domain: active-directory
slug: windows-dc-locator
summary: Windows clients use the DC locator algorithm (Netlogon/DsGetDcName) — primarily DNS-based SRV record discovery with LDAP UDP pings, falling back to NetBIOS/WINS only when necessary and explicitly allowed.
sources:
  - kb:ad-ds-dc-locator
  - kb:ad-ds-dc-locator-performance-counters
provenance:
  extracted: 18
  inferred: 1
tags: [clients]
question_tier: conceptual
status: draft
updated: 2026-07-18
graph_community: "Active Directory — Implementation Review (Evaluation-Lens MOC)"
---

# How Windows clients locate a suitable domain controller

Windows clients locate a domain controller through the **DC locator algorithm**, implemented by the local **Netlogon service** via the `DsGetDcName` API. The process has two modes: **DNS-based discovery** (primary/recommended) and **NetBIOS-based discovery** (legacy, restricted as of Windows Server 2025).

## DNS-based discovery (default)

1. A client application calls `DsGetDcName`, which invokes the local Netlogon service via RPC (`ad-ds-dc-locator.md:81-83`).
2. Netlogon queries DNS for SRV records in the format `_<service>._<protocol>.<DnsDomainName>` — e.g. `_ldap._tcp.contoso.com` (`ad-ds-dc-locator.md:87-91`).
3. The DNS response returns a list of candidate domain controllers (via A/AAAA records).
4. Netlogon sends an LDAP UDP datagram ("LDAP ping") to each candidate (`ad-ds-dc-locator.md:93-95`).
5. The **first domain controller to respond** is returned to the caller (`ad-ds-dc-locator.md:97`)(`extracted`).
6. The result is **cached** by Netlogon so subsequent requests reuse the same DC (`ad-ds-dc-locator.md:99`)(`extracted`).

DC locator supports different SRV record types per capability: LDAP, Global Catalog (GC), Kerberos KDC, and PDC (`ad-ds-dc-locator.md:41`)(`extracted`).

## NetBIOS-based discovery (legacy)

When a client specifies a **short NetBIOS-style domain name**, DC locator first attempts to map it to a DNS domain name from: cached lookups, all domains in the forest, trusting forest trusts, configured mappings (WS2025+), and local sign-in sessions (`ad-ds-dc-locator.md:50-66`)(`extracted`). If no mapping succeeds, it falls back to NetBIOS-based discovery via **WINS** or **mailslot broadcasts** (`ad-ds-dc-locator.md:45,66-67`).

WINS was deprecated in Windows Server 2022 and mailslots in Windows Server 2025 (`ad-ds-dc-locator.md:116`)(`extracted`).

## Closest site detection

After establishing an LDAP connection, the domain controller tells the client which **Active Directory site** it belongs to, based on the client's IP subnet. If the responding DC is not in the client's optimal site, the client re-queries DNS for site-specific SRV records (`_ldap._tcp.<site>._sites.<DnsDomainName>`) (`ad-ds-dc-locator.md:146-149`)(`extracted`). The cache is flushed after 15 minutes if the DC is in a suboptimal site (`ad-ds-dc-locator.md:150`)(`extracted`).

## Windows Server 2025: BlockNetBIOSDiscovery

Starting with Windows Server 2025, the `BlockNetBIOSDiscovery` Group Policy setting (default **TRUE**) blocks NetBIOS-based DC location entirely. This is located under **Computer Configuration > Administrative Templates > System > Net Logon > DC Locator DNS Records** (`ad-ds-dc-locator.md:128-135`)(`extracted`). The policy enforces a secure-by-default posture; disable only temporarily while pursuing other mitigations (`ad-ds-dc-locator.md:134-135`)(`extracted`).

## Observability (Windows Server 2025+)

Beginning with Windows Server 2025, DC locator performance can be monitored via Performance Monitor (`perfmon.exe`) using three counter sets: **DC Locator (Client)**, **DC Locator (DC)**, and **DC Locator (Netlogon)** (`ad-ds-dc-locator-performance-counters.md:23-27`)(`extracted`). Key counters include `Requests: Failures/sec` (number of failed requests per second, on the client-side set) and, on the Netlogon set, `Cache: Hits/sec` and `DNS Query Failures/sec` (`ad-ds-dc-locator-performance-counters.md:54,82,84`)(`extracted`).

## Contradictions / caveats

- Windows Server 2025 changes the default behavior significantly — NetBIOS discovery is now blocked by default, and forest-level domain name mappings are a new feature (`ad-ds-dc-locator.md:58-62,68`)(`inferred`). These changes do not apply to earlier versions.

## See also
- [[ad-dns]]
- [[sites-topology]]
- [[dc-locator]]
- [[dns-for-ad-ds]]
- [[ad-integrated-dns-zones]]
- [[disjoint-namespace]]
- [[global-catalog]]

## References

**RH ground-truth (reference tier):**
- `ad-ds-dc-locator.md` — Locating Active Directory Domain Controllers in Windows and Windows Server (Microsoft Learn, folded into reference/)
- `ad-ds-dc-locator-performance-counters.md` — Active Directory DC Locator performance counters in Windows Server (Microsoft Learn, folded into reference/)

**Wiki:**
- [[ad-dns]] — AD-integrated DNS, SRV records, the locator process
- [[sites-topology]] — sites, subnets, site links, DC locator
- [[dc-locator]] — DsGetDcName, DNS-based vs. NetBIOS discovery
- [[dns-for-ad-ds]] — why DNS is essential to AD DS
- [[ad-integrated-dns-zones]] — AD-integrated DNS zones
- [[disjoint-namespace]] — disjoint namespace DC locator behavior
- [[global-catalog]] — Global Catalog SRV record type

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-dc-locator|Locating Active Directory Domain Controllers in Windows and Windows Server]]
- [[ad-ds-dc-locator-performance-counters|Active Directory DC Locator performance counters in Windows Server]]
<!-- crosslink:end -->
