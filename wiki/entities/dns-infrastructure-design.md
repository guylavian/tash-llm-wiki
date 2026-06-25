---
title: DNS Infrastructure Design
type: entity
domain: active-directory
slug: dns-infrastructure-design
summary: Design decisions for the DNS infrastructure supporting AD DS — AD-integrated zones, namespace selection, delegation, and forwarding topology.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Creating-a-DNS-Infrastructure-Design (Microsoft Learn — Creating a DNS Infrastructure Design, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Reviewing-DNS-Concepts (Microsoft Learn — Reviewing DNS Concepts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Integrating-AD-DS-into-an-Existing-DNS-Infrastructure (Microsoft Learn — Integrating AD DS into an Existing DNS Infrastructure, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/DNS-and-AD-DS (Microsoft Learn — DNS and AD DS, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Selecting-the-Forest-Root-Domain (Microsoft Learn — Selecting the Forest Root Domain, fetched 2026-06-18)
provenance_extracted: 17
provenance_inferred: 5
provenance_ambiguous: 0
tags: [ad-dns, logical-design, concept]
status: draft
updated: 2026-06-18
---

# DNS Infrastructure Design

**The DNS infrastructure design for AD DS determines the namespace, zone hosting strategy, delegation structure, and forwarding topology that allow domain controllers and clients to locate AD DS services.**

## Why DNS design precedes DC deployment

AD DS depends on DNS for DC Locator — every client and DC finds authentication services by querying SRV records in DNS zones that correspond to AD domains. A misconfigured DNS namespace or missing delegations cause domain join failures, replication errors, and authentication problems. (inferred)

## Namespace decisions

### Forest root domain name

The forest root DNS name is the forest name. Design rules:
- Use a **registered** Internet DNS suffix (e.g., `corp.contoso.com`) — registered names are globally unique and prevent namespace collisions on mergers/acquisitions
- Avoid **single-label names** (e.g., `corp`) — unsupported and cause DNS resolution failures across many platforms
- Avoid **unregistered suffixes** (e.g., `.local`) — causes issues with mDNS, certificate SANs, and future Internet connectivity
- Keep the prefix ≤15 characters so the NetBIOS name equals the DNS prefix

### Internal vs. external split DNS

Organizations often use a different DNS suffix internally than externally (e.g., `contoso.com` externally, `corp.contoso.com` internally). Both approaches are valid; the key is that the internal AD namespace be clearly defined and that DCs are authoritative for the internal zones. (inferred)

## AD-integrated DNS zones

AD DS–integrated DNS zones store zone data in the Active Directory database (domain or application partition) rather than flat zone files. Benefits:
- Zone data replicates via AD replication (multi-master, secure dynamic updates)
- DNS SRV records are automatically registered and updated by DCs
- Eliminates separate zone transfer configuration between DNS servers that are also DCs
- Supports fine-grained replication scoping (domain-wide vs. forest-wide application partition)

See [[ad-integrated-dns-zones]] for zone types and replication partition scoping.

## Delegation

For a regional domain model, each child domain's DNS zone must be delegated from the parent zone. A delegation record in the parent zone (NS + glue A record) points resolvers to the authoritative DNS servers for the child zone. Without delegation, clients outside a child domain cannot resolve names in that domain. (inferred)

Steps:
1. Identify parent zone owner (usually the forest root domain DNS owner)
2. Add NS and A (glue) records in the parent zone for each child domain's DNS servers
3. Verify delegation using `nslookup` or `Resolve-DnsName` from outside the delegated zone

## Forwarding topology

DNS servers within the AD forest should use one of:
- **Conditional forwarders** — forward queries for specific external domains to the appropriate external DNS servers, keeping internal resolution internal
- **Root hints** — for organizations with full internet DNS resolution; all non-authoritative queries resolve recursively from the root

For disjoint namespace environments (AD domain suffix differs from DNS suffix), conditional forwarders are essential. See [[disjoint-namespace]].

## DNS for site topology

The DC Locator uses DNS SRV records scoped by site name (e.g., `_ldap._tcp.<site>._sites.dc._msdcs.<domain>`). Correct subnet → site mapping ensures clients receive site-local DC referrals. Broken DNS delegation or missing SRV records prevent site-aware DC location and cause cross-site authentication traffic. (inferred)

## Contradictions / caveats

- AD-integrated zones are recommended but require the DNS server role to be co-hosted on DCs. In environments where DNS is managed separately from AD, file-backed zones with secure dynamic updates and careful delegation are still supported.
- The `_msdcs.<forest-root>` zone is a critical forest-wide DNS zone; it must be replicated to all DNS servers in the forest for cross-domain GC and KDC location. In Windows Server 2003+, this is hosted in the `ForestDnsZones` application partition automatically.

## Reference notes
- [[ad-ds-creating-a-dns-infrastructure-design]]
- [[ad-ds-reviewing-dns-concepts]]
- [[ad-ds-dns-and-ad-ds]]
- [[ad-ds-integrating-ad-ds-into-an-existing-dns-infrastructure]]
- [[ad-ds-selecting-the-forest-root-domain]]

## See also
- [[ad-logical-structure-design]]
- [[ad-integrated-dns-zones]]
- [[dc-locator]]
- [[disjoint-namespace]]
- [[dns-for-ad-ds]]
