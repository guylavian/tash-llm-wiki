---
title: Windows Server — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: windows-server
slug: windows-server-implementation-review
summary: The evaluation lens and Map of Content for the windows-server brain — a rule → anti-pattern → symptom checklist across storage/HCI, failover clustering, Hyper-V, remote/administration, and the authentication stack, plus a symptom → likely-cause reverse index.
sources:
  - kb:storage-storage-spaces-direct-overview
  - kb:storage-storage-spaces-direct-hardware-requirements
  - kb:storage-storage-spaces-direct-disaster-recovery
  - kb:failover-clustering-what-is-quorum-witness
  - kb:failover-clustering-recover-failover-cluster-without-quorum
  - kb:storage-dfs-replication-overview
  - kb:storage-storage-replica-overview
  - kb:administration-windows-server-update-services-wsus
  - kb:administration-plan-your-wsus-deployment
  - kb:administration-server-core-roles-and-services
  - kb:remote-rds-roles
  - kb:security-credentials-protection-and-management
provenance:
  extracted: 5
  inferred: 26
  ambiguous: 0
tags: [win-storage, failover-clustering, hyper-v, remote-services, win-administration, win-authn, troubleshooting]
status: draft
updated: 2026-07-23
graph_community: "Windows Server — Overview"
---

# Windows Server — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `windows-server` domain.** It
indexes windows-server health pages into a forward checklist (rule → anti-pattern →
symptom) and a reverse index (symptom → likely cause), mirroring
[[active-directory-implementation-review]]; grow it as pages land via INGEST.

---

## How to use this page

Read each row left to right: the **Rule** column states what a healthy deployment
must do; **Anti-pattern** states the common misconfiguration; **Symptom** names the
observable ticket it produces; **Page** links the cause page. To diagnose, jump to
the [Reverse index](#reverse-index--symptom--likely-cause).

---

## Health checklist

### Storage / hyperconverged infrastructure

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Keep an odd number of total quorum votes; add a witness on an even node count | 2-node or 4-node Storage Spaces Direct cluster deployed with no witness | Cluster stops on a single node reboot/failure because remaining votes are exactly half | [[failover-cluster-quorum]], [[storage-spaces-direct]] |
| Use only supported drive topologies (direct-attached, one server each) | Shared SAS enclosure or any MPIO path attached to Storage Spaces Direct | Cluster validation wizard / `Test-Cluster` fails storage tests; drives not eligible for pool | [[storage-spaces-direct]] |
| Provision 4 GB RAM per TB of cache-drive capacity in addition to workload RAM | Cache drives sized without the S2D metadata RAM overhead accounted for | Pool/cluster performance degradation or metadata pressure under load | [[storage-spaces-direct]] |
| Use cluster-to-cluster [[storage-replica]] or Hyper-V Replica for hyperconverged DR across sites | Attempting a stretch-cluster topology for a hyperconverged (S2D) cluster | Unsupported configuration; DR plan fails validation or design review | [[storage-spaces-direct]], [[storage-replica]] |
| Use [[storage-replica]] (block-level) for zero-data-loss DR; don't rely on [[dfs-replication]] as a DR substitute | DFS Replication used as the sole DR mechanism for latency-sensitive or open-file workloads | Large recovery-point deltas (hours/days); hottest files not yet replicated at failure time | [[dfs-replication]], [[storage-replica]] |
| Size Storage Replica log volumes faster than data volumes and dedicate them to logging only | Log volume shared with another workload or slower than the data volume | Elevated write latency; synchronous replication round-trip exceeds the ~5 ms target | [[storage-replica]] |

### Failover clustering and quorum

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Investigate root cause before force-starting a cluster without quorum | Force-starting (`-ForceQuorum`) as the default response to any cluster outage | Event ID 1177 logged repeatedly; recurring quorum loss never actually diagnosed | [[failover-cluster-quorum]] |
| Start remaining nodes with `-PreventQuorum` after a force-start | Remaining nodes started normally after a force-start on another node | Split cluster — two competing cluster instances form | [[failover-cluster-quorum]] |
| Remember a Storage Spaces Direct cluster tolerates at most two node failures, even with dynamic quorum | Assuming dynamic quorum makes an HCI cluster tolerant of any number of sequential failures | Cluster (and all VMs/volumes on it) goes down after a third node failure | [[failover-cluster-quorum]], [[storage-spaces-direct]] |
| Use a file share witness (not a disk witness) for clusters with no shared disks | Attempting a disk witness on a Storage Spaces Direct / SQL AG / Exchange DAG cluster | Witness configuration fails — no shared disk exists to host it | [[failover-cluster-quorum]] |

### Hyper-V and virtualization

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use Generation 2 VMs with Shielded VM / Host Guardian Service for sensitive workloads | Generation 1 VMs run for sensitive data with no Shielded VM protection | A compromised host administrator can access VM disk/memory contents unimpeded | [[hyper-v]] |
| Size Hyper-V Replica RPO to the workload's tolerance (as low as 30s) rather than defaulting blindly | Replica frequency left at a default that doesn't match the workload's actual RPO requirement | Unexpected data loss window during failover larger than the business expects | [[hyper-v]] |

### Remote / administration

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Deploy RD Session Host on Server with Desktop Experience, not Server Core | Attempting to add the RD Session Host role service on a Server Core install | Role service unavailable / not installable on Server Core | [[remote-desktop-services]], [[server-core]] |
| Install matching, CA-issued certificates on RD Gateway / RD Web Access and clients before production release | Self-signed certificates left in place after moving from test to production | Users blocked by certificate trust errors when connecting from the internet | [[remote-desktop-services]] |
| Treat WSUS as a maintenance-mode component; plan its long-term replacement | New automation or scaling investment built on WSUS as if it were still actively developed | Feature gaps vs. modern update tooling; UUP MIME-type workaround needed for Windows 11 22H2+ clients | [[wsus]] |
| Register the `.wim`/`.msu` MIME types (or apply the required cumulative update) before Windows 11 22H2+ clients sync | WSUS server left unpatched/unconfigured for UUP | Windows 11, version 22H2+ clients fail to install updates from WSUS | [[wsus]] |
| Keep a WSUS hierarchy shallow (avoid deep nesting) | WSUS servers chained more than a few levels deep | Update propagation delay compounds across each hierarchy level | [[wsus]] |

### Authentication and credential protection

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Never add service or computer accounts to the Protected Users group | Service/computer account added to Protected Users expecting extra protection | Authentication fails ("user name or password is incorrect") for that service/computer | [[windows-server-credential-protection]] |
| Use Restricted Admin mode for RDP to hosts that may be compromised | Standard RDP admin logon used to hosts of uncertain trust | Credentials harvestable from a compromised RDP target during the initial connection | [[windows-server-credential-protection]] |
| Configure encryption types via Group Policy on Windows Server 2025+, not the legacy registry key | `SupportedEncryptionTypes` registry key relied on for Kerberos encryption-type control after upgrading to Windows Server 2025 | Registry key silently ignored; encryption-type policy doesn't take effect | [[windows-server-kerberos-auth-stack]] |

---

## Reverse index — symptom → likely cause

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| `Event ID 1177` (cluster service stopped — quorum lost) | Insufficient active quorum votes; missing witness on an even-node cluster | [[failover-cluster-quorum]] |
| Cluster (and hosted VMs/volumes) down after losing a third Storage Spaces Direct node | S2D's dynamic-quorum tolerance ceiling (max 2 node failures) exceeded | [[failover-cluster-quorum]], [[storage-spaces-direct]] |
| Split cluster / two competing cluster instances after a force-start | Remaining nodes started without `-PreventQuorum` after a force-start | [[failover-cluster-quorum]] |
| `Test-Cluster` / cluster validation storage test failure on Storage Spaces Direct | Unsupported drive topology — shared SAS enclosure or MPIO path | [[storage-spaces-direct]] |
| DR failover shows large recovery-point gap; hottest files stale on the replica | DFS Replication used for latency-sensitive/open-file DR instead of Storage Replica | [[dfs-replication]], [[storage-replica]] |
| Destination volume inaccessible during Storage Replica replication (Windows Server 2016) | Expected behavior — the destination is dismounted while replicating; use `Test-Failover` for read-write access | [[storage-replica]] |
| RD Session Host role service unavailable to install | Target server is running Server Core, which excludes RD Session Host | [[remote-desktop-services]], [[server-core]] |
| Certificate trust error connecting to RD Gateway / RD Web Access from the internet | Self-signed certificate left in place for a production deployment | [[remote-desktop-services]] |
| Windows 11, version 22H2+ client fails to install updates from WSUS | UUP MIME types (`.wim`/`.msu`) not registered / required cumulative update missing on WSUS server | [[wsus]] |
| WSUS update propagation is slow across branch offices | WSUS hierarchy nested too deeply instead of hub-and-spoke | [[wsus]] |
| Service/computer account fails authentication with "user name or password is incorrect" | Account was added to the Protected Users security group | [[windows-server-credential-protection]] |
| `SupportedEncryptionTypes` registry key has no effect on Kerberos behavior | Server is Windows Server 2025+, where the key is no longer honored — use Group Policy instead | [[windows-server-kerberos-auth-stack]] |
| DC location / logon failure traced to Windows-Server-role DNS (non-AD-specific) | DNS Server role misconfigured or unreachable — see [[windows-server-dns-role]] for the generic role; AD-specific `_msdcs`/SRV troubleshooting is in the `active-directory` domain | [[windows-server-dns-role]] |

---

## Domain map — pages by area

### Storage and HCI
- [[storage-spaces-direct]] — hyperconverged pooled storage
- [[dfs-replication]] — file-level replication, `sysvol`
- [[storage-replica]] — block-level DR replication

### Failover clustering
- [[failover-cluster-quorum]] — quorum voting, witnesses, force-start recovery

### Virtualization
- [[hyper-v]] — the built-in hypervisor

### Networking
- [[windows-server-dns-role]] — the DNS Server role

### Remote and administration
- [[remote-desktop-services]] — RDS role family
- [[wsus]] — update distribution
- [[server-core]] — minimal install option
- [[windows-admin-center]] — browser-based management

### Authentication
- [[windows-server-kerberos-auth-stack]] — Kerberos v5 implementation
- [[windows-server-credential-protection]] — Restricted Admin, LSA protection, Protected Users, Authentication Policies

## See also
- [[active-directory-implementation-review]] — Active Directory domain's equivalent MOC
- [[windows-server-overview]] — domain primer
- [[windows-server-identity-coverage-gaps]] — cross-domain identity gap analysis

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[storage-storage-spaces-direct-overview|Storage Spaces Direct overview]]
- [[storage-storage-spaces-direct-hardware-requirements|Storage Spaces Direct Hardware Requirements in Windows Server]]
- [[storage-storage-spaces-direct-disaster-recovery|Disaster Recovery Scenarios for Storage Spaces Direct in Windows Server]]
- [[failover-clustering-what-is-quorum-witness|What is a failover cluster quorum witness in Windows Server?]]
- [[failover-clustering-recover-failover-cluster-without-quorum|Recover a failover cluster without quorum in Windows Server]]
- [[storage-dfs-replication-overview|Distributed File System (DFS) Replication]]
- [[storage-storage-replica-overview|Storage Replica Overview]]
- [[administration-windows-server-update-services-wsus|Windows Server Update Services (WSUS) Overview]]
- [[administration-plan-your-wsus-deployment|Plan Your WSUS Deployment]]
- [[administration-server-core-roles-and-services|Roles, Role Services, and Features included in Windows Server]]
- [[remote-rds-roles|Remote Desktop Services roles]]
- [[security-credentials-protection-and-management|Credentials Protection and Management]]
<!-- crosslink:end -->
