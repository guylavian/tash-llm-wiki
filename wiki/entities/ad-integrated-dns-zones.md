---
title: Active Directory-Integrated DNS Zones
type: entity
domain: active-directory
slug: ad-integrated-dns-zones
summary: DNS zones stored inside the directory and replicated by AD replication instead of zone transfers, giving multi-master updates and secure dynamic update.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Active-Directory-Integrated-DNS-Zones (Microsoft Learn — Active Directory-Integrated DNS Zones, fetched 2026-06-18)
provenance_extracted: 6
provenance_inferred: 2
provenance_ambiguous: 0
tags: [ad-dns, concept]
status: draft
updated: 2026-06-18
---

# Active Directory-Integrated DNS Zones

**A DNS zone whose data is stored in AD DS and replicated by Active Directory replication, so no separate DNS zone-transfer topology is needed.**

## Body

When a DNS server runs on a domain controller it can store its zones in AD DS
rather than in flat zone files. Because the zone records ride on AD replication,
there is no need to configure secondary zones or ordinary DNS zone transfers — zone
data is replicated automatically along with the rest of the directory.

Two advantages flow from this storage model:

- **Multi-master updates.** Every DC in the domain running the DNS Server service
  is authoritative and can write updates to the integrated zone. There is no single
  writable primary, so a DNS write succeeds at whichever DC the client reaches.
- **Secure dynamic update.** Because zone records are AD objects with ACLs, an
  administrator can control which computer may update which name and prevent an
  unauthorized computer from overwriting an existing record.

AD-integrated DNS stores zone data in **application directory partitions** (no
behavioral change from Windows Server 2003 integration). Two DNS application
partitions are created during AD DS installation:

- **ForestDnsZones** — a forest-wide partition (replicates to all DNS-running DCs
  in the forest).
- **DomainDnsZones** — a domain-wide partition per domain (replicates to DNS-running
  DCs in that domain).

The partition you place a zone in therefore sets its replication scope (inferred —
the source names the two partitions and that replication follows AD replication, so
partition choice governs reach). Microsoft recommends installing DNS during the AD DS
installation wizard so the DNS zone delegation is created automatically.

Because the records live in [[ad-integrated-dns-zones]]'s host partitions, DNS health
and [[ad-replication]] health are coupled: a replication backlog also delays DNS record
convergence (inferred).

## Contradictions / caveats

- Integrated zones are only available on a DNS server running on a domain controller;
  a member or standalone DNS server still uses file-backed zones and zone transfers.
- The convenience of "DNS rides on AD replication" is also the trap: replication
  latency or a [[knowledge-consistency-checker]] topology problem becomes a DNS
  staleness problem (inferred).

## Reference notes
- [[ad-ds-active-directory-integrated-dns-zones]]

## See also
- [[dns-for-ad-ds]]
- [[dc-locator]]
- [[ad-integrated-dns-zones]]
- [[ad-replication]]
