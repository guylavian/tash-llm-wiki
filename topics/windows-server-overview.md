---
title: Windows Server — Overview
type: topic
domain: windows-server
slug: windows-server-overview
summary: The spine of the windows-server brain — the server OS's core pillars (storage/HCI, failover clustering, Hyper-V virtualization, networking/DNS, remote/RDS, administration tooling, the Windows authentication stack) and how they compose into a hyperconverged or traditional datacenter deployment.
sources:
  - kb:virtualization-overview
  - kb:storage-storage-spaces-direct-overview
  - kb:failover-clustering-failover-clustering-overview
  - kb:storage-dfs-replication-overview
  - kb:storage-storage-replica-overview
  - kb:administration-windows-server-update-services-wsus
  - kb:remote-rds-roles
  - kb:administration-what-is-server-core
  - kb:manage-overview-2
  - kb:networking-dns-overview
  - kb:security-kerberos-authentication-overview
  - kb:security-credentials-protection-and-management
provenance:
  extracted: 11
  inferred: 3
  ambiguous: 0
tags: [win-storage, failover-clustering, hyper-v, win-networking, remote-services, win-administration, win-authn]
status: draft
updated: 2026-07-23
graph_community: "Windows Server — Overview"
---

# Windows Server — Overview

**Windows Server is Microsoft's server operating system: a set of installable
roles/features (storage, virtualization, networking, remote access,
identity/authentication) that compose into anything from a single file server to
a multi-site hyperconverged datacenter.**

## Body

### Installation footprint: Server Core vs. Desktop Experience

Every deployment starts with a choice of install option. **[[server-core]]** is the
minimal option (no GUI shell) available on Standard/Datacenter editions, chosen for
a smaller attack surface and disk footprint; Server with Desktop Experience installs
the full GUI stack. Not every role runs on Server Core — most notably, the **Remote
Desktop Session Host role service is excluded from Server Core** (extracted: it does
not appear in the Server Core role/role-service table), so session-based RDS
deployments need Desktop Experience or a client-OS-based host.

### Storage and hyperconverged infrastructure

The storage pillar layers four technologies:

- **[[storage-spaces-direct]]** pools local, direct-attached drives across 2–16
  clustered servers into a single software-defined storage pool — the foundation of
  hyperconverged infrastructure (HCI), where the same cluster runs Hyper-V compute
  and storage together.
- **[[failover-cluster-quorum]]** (Failover Clustering) is the underlying
  high-availability mechanism Storage Spaces Direct, Hyper-V, and Scale-Out File
  Server all depend on — nodes vote on quorum to avoid split-brain, and losing more
  than half the votes stops the cluster.
- **[[dfs-replication]]** and **[[storage-replica]]** both keep data synchronized
  across servers/sites, but at different layers and for different purposes:
  DFS Replication is file-level (and also replicates AD's `sysvol`), while Storage
  Replica is block-level, storage-agnostic, and offers zero-data-loss synchronous
  replication for disaster recovery (inferred — DFS Replication's file-close/
  throttling design makes it a poor DR substitute for Storage Replica, per the
  Storage Replica overview's own comparison).

### Virtualization

**[[hyper-v]]** is the built-in type-1 hypervisor. It composes directly with
Failover Clustering (live migration, Cluster Shared Volumes) and with Storage
Spaces Direct (hyperconverged deployments run Hyper-V VMs directly on S2D volumes).

### Networking

**[[windows-server-dns-role]]** is the DNS Server role — the name-resolution
backbone for both plain Windows networks and Active Directory Domain Services
(AD DS uses DNS as the domain-controller location mechanism). DNS sits alongside
other networking building blocks not yet broken into their own entity pages here
(BranchCache, SDN/Network Controller, DHCP) — see `reference/windows-server/networking-*`
for the full reference set.

### Remote access and administration

**[[remote-desktop-services]]** (RDS) is the session/VDI hosting role — Session
Host, Connection Broker, Gateway, Web Access, and Licensing roles compose into a
farm. **[[wsus]]** (Windows Server Update Services) centralizes patch distribution
and is **deprecated** (no new features, but still supported and serviced).
**[[windows-admin-center]]** is the modern browser-based management surface that
replaces/augments Server Manager and MMC snap-ins for day-to-day administration,
including of Storage Spaces Direct, failover clusters, and Hyper-V hosts (it is a
free download with no extra licensing cost).

### Authentication and credential protection

Windows Server's authentication stack is built on **[[windows-server-kerberos-auth-stack]]**
(Kerberos v5 is the default domain protocol; NTLM is the legacy fallback), backed by
the domain controller's Active Directory database via the KDC. On top of the
protocol layer, **[[windows-server-credential-protection]]** covers OS-level
credential-theft mitigations (Restricted Admin mode, LSA protection, the Protected
Users group, Authentication Policies/Silos) that reduce what a compromised host can
harvest — this is the credential-hardening layer immediately adjacent to (but
distinct from) AD's own [[windows-laps]] local-admin-password rotation, which lives
in the `active-directory` domain.

## Contradictions / caveats

WSUS is explicitly called out as deprecated in its own overview note ("no longer
adding new features... continues to be supported... receives security and quality
updates") — treat any WSUS-based patch pipeline as a maintenance-mode component,
not a growth area. Storage Spaces Direct and Storage Replica overlap in the
hyperconverged-disaster-recovery space; the Storage Spaces Direct disaster-recovery
guidance explicitly recommends Storage Replica (cluster-to-cluster) or Hyper-V
Replica over trying to stretch a single hyperconverged cluster across sites, since
losing two nodes in an HCI cluster takes the whole cluster down (inferred summary of
the disaster-recovery note's stretch-cluster caveat).

## See also
- [[storage-spaces-direct]]
- [[failover-cluster-quorum]]
- [[hyper-v]]
- [[dfs-replication]]
- [[storage-replica]]
- [[wsus]]
- [[remote-desktop-services]]
- [[server-core]]
- [[windows-admin-center]]
- [[windows-server-dns-role]]
- [[windows-server-kerberos-auth-stack]]
- [[windows-server-credential-protection]]
- [[windows-server-implementation-review]]
- [[windows-server-identity-coverage-gaps]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[virtualization-overview|Hyper-V virtualization in Windows Server and Windows]]
- [[storage-storage-spaces-direct-overview|Storage Spaces Direct overview]]
- [[failover-clustering-failover-clustering-overview|Failover Clustering]]
- [[storage-dfs-replication-overview|Distributed File System (DFS) Replication]]
- [[storage-storage-replica-overview|Storage Replica Overview]]
- [[administration-windows-server-update-services-wsus|Windows Server Update Services (WSUS) Overview]]
- [[remote-rds-roles|Remote Desktop Services roles]]
- [[administration-what-is-server-core|What is Server Core?]]
- [[manage-overview-2|Windows Admin Center overview]]
- [[networking-dns-overview|Domain Name System (DNS) in Windows and Windows Server]]
- [[security-kerberos-authentication-overview|Kerberos authentication overview in Windows Server]]
- [[security-credentials-protection-and-management|Credentials Protection and Management]]
<!-- crosslink:end -->
