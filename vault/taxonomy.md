# Wiki tag taxonomy — controlled vocabulary

This is the **only** source of legal `tags:` values. `tags.py` and `lint.py` parse
this file (the backticked tokens under each facet heading) — keep tags from these
lists, kebab-case. Tags are navigation/faceting aids, not facts; they never replace
`sources:` or `provenance:`.

A page's `tags:` should carry **one or more `area`**, optionally **one `kind`**, and
optionally **version** tags when the page is version-specific. Example:

```yaml
tags: [federation, concept, v26.6]
```

## Areas
- `realm` — realms, realm settings, keys/rotation, import/export, localization
- `authn` — authentication flows, MFA/OTP/WebAuthn, passwords, brute force, step-up
- `authz` — Authorization Services: resources/scopes/policies/permissions, UMA, PEP/PDP
- `clients` — OIDC/SAML clients, client auth, scopes, protocol mappers, registration
- `tokens` — access/refresh tokens, sessions, lifespans, exchange, DPoP, logout
- `federation` — LDAP/AD user federation, user storage, mappers, Kerberos
- `brokering` — external OIDC/SAML/social identity providers, IdP mappers
- `users` — users, credentials, roles, groups, profile attributes
- `operator` — RHBK Operator, Keycloak CR, OLM, realm-import CR, OpenShift deploy
- `ha` — clustering, Infinispan caches, multi-site, load balancer, failover, sizing
- `observability` — health, metrics, tracing, OpenTelemetry, SLIs, dashboards
- `server-config` — kc.sh build/runtime, hostname, db, TLS, proxy, vault, features
- `migration` — RH-SSO→RHBK, version upgrades, adapter/provider/theme porting
- `spi` — SPI provider/factory model, custom providers, themes, scripts
- `iac` — Infrastructure-as-Code, the keycloak/keycloak Terraform provider
- `security` — hardening, FAPI/OAuth2.1, threat mitigation, production checklist
- `troubleshooting` — symptom→cause→fix pages, gated-KB pointers
<!-- active-directory areas (notes-first domain) -->
- `directory-services` — AD DS: forests, domains, trees, OUs, schema, the directory database (NTDS)
- `replication` — multi-master replication, the KCC, replication topology/latency, USN/tombstones
- `group-policy` — GPO processing, ADMX/ADML, GPO scope/precedence (LSDOU), loopback
- `ad-dns` — AD-integrated DNS, SRV/`_msdcs` records, locator process, scavenging
- `fsmo` — the five operations-master roles (Schema, Domain Naming, RID, PDC, Infrastructure)
- `trusts` — domain & forest trusts, trust direction/transitivity, SID filtering
- `sites-topology` — sites, subnets, site links, DC locator, replication topology
- `ad-certificate-services` — AD CS / PKI: CA roles, templates, enrollment, autoenrollment
- `ad-authn` — Kerberos & NTLM authentication, SPNs, delegation, tickets
- `deploy` — install/promote/demote lifecycle: DC promotion, adprep, capacity & placement planning
- `logical-design` — forest/domain/OU design models, namespace design, disjoint namespaces
- `virtualization` — virtualized DCs: VM-GenerationID, USN rollback, cloning, snapshot safety
<!-- cisco-ios-xe areas (notes-first domain) -->
- `routing-protocols` — dynamic IP routing: OSPF, BGP, EIGRP, IS-IS, RIP — adjacencies, metrics, path selection, authentication
- `ip-routing` — protocol-independent forwarding: static routes, RIB/FIB, administrative distance, route maps, PBR, redistribution, BFD
- `lan-switching` — VLANs, VTP, 802.1Q trunking, inter-VLAN routing, access/trunk ports
- `spanning-tree` — STP/RSTP/MST, root-bridge election, PortFast, BPDU guard/filter, loop prevention
- `etherchannel` — Layer-2/3 link aggregation, LACP/PAgP, load balancing, bundle consistency
<!-- openshift / kubernetes areas (notes-first domain; promote to corpus-backed once docs are harvested) -->
- `workloads` — pods, Deployments, StatefulSets, DaemonSets, Jobs/CronJobs, ReplicaSets, probes, scheduling, resource requests/limits
- `cluster-networking` — Services, Ingress, OpenShift Routes, NetworkPolicy, OVN-Kubernetes/CNI, cluster DNS, load balancers
- `cluster-storage` — PersistentVolumes/Claims, StorageClasses, CSI drivers, dynamic provisioning, volume modes
- `operators-olm` — Operators, Operator Lifecycle Manager (OLM), ClusterOperators, MachineConfig, day-2 cluster management
- `builds-images` — image streams, BuildConfigs, Source-to-Image (S2I), the internal registry, image pull/signature policy
- `cluster-auth` — RBAC (Roles/Bindings), ServiceAccounts, OpenShift OAuth, Security Context Constraints (SCC), identity providers
<!-- windows-server areas (corpus-backed: MicrosoftDocs/windowsserverdocs) -->
- `win-storage` — Storage Spaces (Direct), Storage Replica, Storage Migration Service, DFS namespaces/replication, ReFS, dedup, iSCSI, NFS, FSRM
- `failover-clustering` — failover clusters, quorum, cluster sets, CSV, cluster-aware updating
- `hyper-v` — Hyper-V hosts and VMs, checkpoints, live migration, virtual switches, nested virtualization
- `win-networking` — DNS Server role, SDN, BranchCache, Network ATC, NCSI, Windows Time Service
- `remote-services` — Remote Desktop Services, Remote Access (VPN/DirectAccess/RRAS), Web Application Proxy
- `win-administration` — Server Core, Server Manager, Windows Admin Center, WSUS, OpenSSH, windows-commands, performance tuning, Azure Arc, licensing/editions
- `win-authn` — Windows authentication stack: Kerberos, NTLM, credentials protection, TLS/Schannel, UAC, LAPS
<!-- sccm areas (corpus-backed: MicrosoftDocs/memdocs intune/configmgr + PDF set) -->
- `sccm-core` — site infrastructure, hierarchy, site systems, clients, collections, console, admin service/SDK
- `sccm-apps` — application management, deployments, Software Center, app model
- `sccm-osd` — operating system deployment, task sequences, boot images, MDT
- `sccm-updates` — software updates management, ADRs, WSUS integration, patching
- `sccm-compliance` — compliance settings, baselines, co-management, endpoint protection integration
<!-- powershell areas (corpus-backed: PowerShell 7.6 scripting PDF + office-docs-powershell cmdlet refs) -->
- `ps-language` — syntax, operators, pipelines, functions, scripting constructs, classes, error handling
- `ps-modules` — module system + per-product cmdlet reference docsets (server & online admin modules)
- `ps-remoting` — PowerShell remoting, sessions, WinRM/SSH transports, implicit remoting
<!-- exchange areas (corpus-backed: Exchange Server PDF docset) -->
- `exchange-mailflow` — transport pipeline, connectors, queues, routing, transport rules
- `exchange-recipients` — mailboxes, recipient types, address lists, permissions
- `exchange-ha` — DAGs, database copies, site resilience, backup/restore
<!-- sharepoint areas (corpus-backed: SharePoint Server PDF docset + SP PowerShell) -->
- `sp-farm` — farm topology, service applications, central administration, distributed cache
- `sp-content` — web applications, site collections, content databases, storage
- `sp-search` — search service application, crawling, index, query
<!-- checkpoint areas (notes-first; raw tier fed by the ONLINE scraper from support.checkpoint.com) -->
- `cp-gateway` — Security Gateway: inspection, blades, NAT, routing, acceleration (SecureXL/CoreXL)
- `cp-management` — Security Management Server / Multi-Domain, SmartConsole, database, upgrades
- `cp-policy` — access-control & threat-prevention policy, layers, rulebase, install-policy
- `cp-vpn` — site-to-site and remote-access VPN, communities, IKE/IPsec, Mobile Access
- `cp-clustering` — ClusterXL, VRRP, VSX, high availability, load sharing, sync network
<!-- rhel areas -->
- `rhel-system` — RHEL base OS: systemd units/targets, boot & GRUB, dnf/rpm packaging, subscription-manager, users & sudo
- `rhel-storage` — RHEL storage stack: LVM, filesystems (XFS/ext4), Stratis, VDO, multipath, NFS/Samba clients
- `rhel-networking` — RHEL networking: NetworkManager/nmcli, firewalld/nftables, bonding & teaming, chrony, hostname/DNS resolution
- `selinux` — SELinux: enforcing/permissive modes, contexts & labels, booleans, policy modules, audit2allow denials
- `rhel-kernel` — kernel & performance: sysctl tuning, tuned profiles, cgroups, kdump/crash, kernel modules, live patching
<!-- vmware-vsphere areas -->
- `vsphere-compute` — ESXi hosts, virtual machines, VM hardware & tools, DRS, vMotion, resource pools, clusters
- `vsphere-storage` — datastores, VMFS/NFS, vSAN, storage policies (SPBM), VMDK & disk modes, storage vMotion
- `vsphere-networking` — standard & distributed switches, port groups, VMkernel adapters, NIC teaming, VLANs on vSphere
- `vsphere-lifecycle` — vCenter Server, vLCM/Update Manager, upgrades & patching, certificates, SSO & permissions
<!-- vmware-nsx areas -->
- `nsx-switching` — NSX logical switching: segments, overlay/Geneve encapsulation, transport zones, VNIs, MAC/ARP tables
- `nsx-routing` — NSX logical routing: Tier-0/Tier-1 gateways, edge nodes & clusters, BGP/OSPF peering, NAT, service interfaces
- `nsx-security` — distributed firewall, gateway firewall, groups & tags, IDS/IPS, micro-segmentation policy
- `nsx-platform` — NSX Managers, transport nodes, host preparation, install/upgrade, backup & restore, federation
<!-- palo-alto areas -->
- `panos-policy` — PAN-OS security & NAT policy, App-ID, User-ID, security profiles, policy evaluation order
- `panos-networking` — interfaces & zones, virtual routers, VLAN/Layer-3 deployments, HA pairs, GlobalProtect & IPsec VPN
- `panos-threat` — threat prevention: antivirus, anti-spyware, vulnerability protection, WildFire, URL filtering, DNS security
- `panos-panorama` — Panorama management: device groups, templates & stacks, commit/push workflow, log collectors
<!-- juniper-junos areas -->
- `junos-platform` — Junos OS fundamentals: configuration hierarchy, candidate config & commit model, CLI operational mode, software upgrades, ZTP
- `junos-security` — SRX security: zones & security policies, screens, source/destination NAT, IPsec VPN, UTM
<!-- fortinet areas -->
- `fortios-policy` — FortiOS firewall policies, virtual IPs & NAT, security profiles (AV/IPS/web filter), policy lookup order
- `fortios-networking` — FortiGate interfaces & VDOMs, static/dynamic routing, SD-WAN rules, HA clusters (FGCP/FGSP)
- `fortios-vpn` — IPsec site-to-site and dial-up VPN, SSL-VPN portals & tunnels, ADVPN
- `fortios-platform` — FortiManager/FortiAnalyzer, firmware upgrade paths, licensing & entitlement, configuration backup
<!-- f5-big-ip areas -->
- `bigip-ltm` — BIG-IP LTM: virtual servers, pools & members, health monitors, persistence, SNAT, iRules, SSL profiles
- `bigip-apm-asm` — BIG-IP APM access policies & SSO, and ASM/Advanced WAF policies, signatures, learning & blocking modes
- `bigip-platform` — TMOS platform: HA device groups & traffic groups, config sync, upgrades & UCS archives, licensing, vCMP
<!-- commvault areas -->
- `backup-policy` — protection plans & storage policies, retention rules, schedules, SLA, auxiliary copy
- `backup-agents` — iDataAgents & the Virtual Server Agent: file system, database and hypervisor backups, application-aware protection
- `backup-infrastructure` — CommServe, MediaAgents, deduplication databases, disk & cloud libraries, index servers, network topologies
- `backup-restore` — restore & recovery: in-place/out-of-place restores, granular recovery, DR of the CommServe, replication & failover

## Kinds
- `concept` — broad synthesis / how-something-works (usually topics/)
- `config-option` — a single config key / flag / setting
- `cli` — a command-line tool or command (kcadm.sh, kcreg.sh, kc.sh)
- `cr-field` — a Keycloak Custom Resource field/section
- `provider` — an SPI provider / built-in component
- `endpoint` — an HTTP endpoint or protocol surface
- `profile` — a client/security policy profile (FAPI, OAuth 2.1)
- `procedure` — a step-by-step task
- `how-to` — alias of `procedure` used by the active-directory import (prefer `procedure` for new pages)
- `troubleshooting` — a diagnosis/fix page
- `anti-pattern` — a page centered on a common wrong implementation (paired with the rule it violates); used by the upstream SSO-dev best-practice pages (Rule / Anti-pattern / Symptom framing)
- `failure-mode` — a page centered on the observable fault/symptom a wrong implementation produces (the ticket you'd actually see)

## Versions
- `v26.0`
- `v26.2`
- `v26.4`
- `v26.6`

## Domains
The `domain:` **frontmatter facet** (required on every page) partitions the wiki by
technology. It is *not* a tag — it lives in frontmatter, and `lint.py` validates each
page's `domain:` against the domains declared below (parsed from the `- domain: <name>`
lines). `index.py` reads each block to build that domain's `index.<domain>.md`. The
per-domain `areas:` are a subset of the `## Areas` vocabulary above; when you add a
domain that needs a *new* area, add it to `## Areas` too (areas are a flat union).

**Source tiers as a coverage axis (for the QUERY Confidence gate).** Beyond *shape*,
each domain declares `- tiers-covered:` — the coarse knowledge-tiers actually ingested,
from this fixed, deliberately tiny set (do **not** grow it into an ontology):
- `conceptual` — how it works: product docs / guides / MS Learn.
- `support-kb` — break-fix / known-issue / patch knowledge: support KB & Solution articles.
- `scenarios` — end-to-end deployment & operations playbooks.
A QUERY classifies the question's tier; if the routed domain does not cover it, the
**Confidence gate** (`CLAUDE.md`, Operation: QUERY) fires `Out of corpus coverage`.
This is the high-precision signal that catches a *faithful extraction from an incomplete
tier* — the failure `provenance_*` counts cannot see.

### keycloak
- domain: keycloak
- areas: [realm, authn, authz, clients, tokens, federation, brokering, users, operator, ha, observability, server-config, migration, spi, iac, security, troubleshooting]
- shape: corpus-backed
- sources: [corpora/keycloak/, _sources/keycloak/]
- review-moc: sso-implementation-review
- tiers-covered: [conceptual, support-kb]   # product guides + RH KB Solution notes (documentKind: Solution)

### active-directory
- domain: active-directory
- areas: [directory-services, replication, group-policy, ad-dns, fsmo, trusts, sites-topology, ad-certificate-services, ad-authn, users, security, troubleshooting, migration]
- shape: corpus-backed
- sources: [reference/active-directory/, corpora/active-directory/, _sources/active-directory/]
- review-moc: active-directory-implementation-review
- tiers-covered: [conceptual]   # MS Learn conceptual docs only — NO support-kb/break-fix tier (the gap behind cross-site-split-brain-pac-signing)

### cisco-ios-xe
- domain: cisco-ios-xe
- areas: [routing-protocols, ip-routing, lan-switching, spanning-tree, etherchannel, security, troubleshooting]
- shape: corpus-backed
- sources: [reference/cisco-ios-xe/, _sources/cisco-ios-xe/]
- review-moc: cisco-ios-xe-implementation-review
- tiers-covered: [conceptual]   # config guides only

### openshift
- domain: openshift
- areas: [workloads, cluster-networking, cluster-storage, operators-olm, builds-images, cluster-auth, observability, security, troubleshooting, migration]
- shape: corpus-backed
- sources: [reference/openshift/, corpora/openshift/, _sources/openshift/]   # 3,813 doc bodies: 1,602 Kubernetes (kubernetes/website) + 2,211 OpenShift 4.22 assemblies (openshift/openshift-docs, via adoc_to_corpus)
- review-moc: openshift-implementation-review
- tiers-covered: [conceptual]         # Kubernetes + OpenShift conceptual docs (4.22). Older OCP 4.8–4.21 + release-notes/known-issues history: re-run adoc_to_corpus per branch (see _meta/ADD-DOMAIN.md)

### windows-server
- domain: windows-server
- areas: [win-storage, failover-clustering, hyper-v, win-networking, remote-services, win-administration, win-authn, security, troubleshooting]
- shape: corpus-backed
- sources: [reference/windows-server/, corpora/windows-server/, _sources/windows-server/]   # MicrosoftDocs/windowsserverdocs minus identity/ad-{ds,fs,rms} (ad-ds lives in active-directory; ad-fs/ad-rms/windows-defender excluded by owner decision 2026-07-23)
- review-moc: windows-server-implementation-review
- tiers-covered: [conceptual]   # MS Learn conceptual docs

### sccm
- domain: sccm
- areas: [sccm-core, sccm-apps, sccm-osd, sccm-updates, sccm-compliance, ps-modules, security, troubleshooting]
- shape: corpus-backed
- sources: [reference/sccm/, corpora/sccm/, _sources/sccm/]   # memdocs intune/configmgr markdown + intune-configmgr-* / troubleshoot-mem-configmgr / powershell-sccm PDF set
- review-moc: sccm-implementation-review
- tiers-covered: [conceptual, support-kb]   # troubleshoot-mem-configmgr PDF is the break-fix tier

### powershell
- domain: powershell
- areas: [ps-language, ps-modules, ps-remoting, security, troubleshooting]
- shape: corpus-backed
- sources: [reference/powershell/, corpora/powershell/, _sources/powershell/]   # PowerShell 7.6 scripting PDF + office-docs-powershell + OfficeDocs-SharePoint-PowerShell cmdlet refs
- review-moc: powershell-implementation-review
- tiers-covered: [conceptual]

### exchange
- domain: exchange
- areas: [exchange-mailflow, exchange-recipients, exchange-ha, ps-modules, security, troubleshooting, migration]
- shape: corpus-backed
- sources: [reference/exchange/, corpora/exchange/, _sources/exchange/]   # Exchange Server docset PDF (exchange-servertoc)
- review-moc: exchange-implementation-review
- tiers-covered: [conceptual]

### sharepoint
- domain: sharepoint
- areas: [sp-farm, sp-content, sp-search, ps-modules, security, troubleshooting, migration]
- shape: corpus-backed
- sources: [reference/sharepoint/, corpora/sharepoint/, _sources/sharepoint/]   # SharePoint Server docset PDF (sharepoint-spstoc) + SP PowerShell refs
- review-moc: sharepoint-implementation-review
- tiers-covered: [conceptual]

### checkpoint
- domain: checkpoint
- areas: [cp-gateway, cp-management, cp-policy, cp-vpn, cp-clustering, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/checkpoint/]   # seeded by the ONLINE scraper: support.checkpoint.com is on vault/scrape-sources.json (match: prefix) -> _sources/checkpoint/_raw/web/ -> reference/checkpoint/
- review-moc: checkpoint-implementation-review
- tiers-covered: [conceptual]   # NOTHING INGESTED YET. Keep it at `conceptual` until real
                                # content lands: a support-kb/scenarios claim here would be the
                                # Confidence gate's H1 arm silently NOT firing on break-fix
                                # questions the vault cannot actually answer.

### rhel
- domain: rhel
- areas: [rhel-system, rhel-storage, rhel-networking, selinux, rhel-kernel, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/rhel/]
- review-moc: rhel-implementation-review
- tiers-covered: [conceptual]

### vmware-vsphere
- domain: vmware-vsphere
- areas: [vsphere-compute, vsphere-storage, vsphere-networking, vsphere-lifecycle, ha, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/vmware-vsphere/]
- review-moc: vmware-vsphere-implementation-review
- tiers-covered: [conceptual]

### vmware-nsx
- domain: vmware-nsx
- areas: [nsx-switching, nsx-routing, nsx-security, nsx-platform, ha, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/vmware-nsx/]
- review-moc: vmware-nsx-implementation-review
- tiers-covered: [conceptual]

### palo-alto
- domain: palo-alto
- areas: [panos-policy, panos-networking, panos-threat, panos-panorama, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/palo-alto/]
- review-moc: palo-alto-implementation-review
- tiers-covered: [conceptual]

### juniper-junos
- domain: juniper-junos
- areas: [junos-platform, junos-security, routing-protocols, ip-routing, lan-switching, security, troubleshooting]
- shape: notes-first
- sources: [_sources/juniper-junos/]
- review-moc: juniper-junos-implementation-review
- tiers-covered: [conceptual]

### fortinet
- domain: fortinet
- areas: [fortios-policy, fortios-networking, fortios-vpn, fortios-platform, security, troubleshooting]
- shape: notes-first
- sources: [_sources/fortinet/]
- review-moc: fortinet-implementation-review
- tiers-covered: [conceptual]

### f5-big-ip
- domain: f5-big-ip
- areas: [bigip-ltm, bigip-apm-asm, bigip-platform, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/f5-big-ip/]
- review-moc: f5-big-ip-implementation-review
- tiers-covered: [conceptual]

### commvault
- domain: commvault
- areas: [backup-policy, backup-agents, backup-infrastructure, backup-restore, security, troubleshooting]
- shape: notes-first
- sources: [_sources/commvault/]
- review-moc: commvault-implementation-review
- tiers-covered: [conceptual]

<!-- Template — copy per new technology (placeholders are ignored by lint/index):
### <domain>
- domain: <domain>
- areas: [...]                       # also add any NEW area to ## Areas above
- shape: notes-first | corpus-backed
- sources: [_sources/<domain>/]      # + corpora/<domain>/ if corpus-backed
- review-moc: <domain>-implementation-review
- tiers-covered: [conceptual]        # coarse tiers ingested: conceptual | support-kb | scenarios
-->

## Synonyms (normalized away by `tags.py --normalize`)
- `auth` -> `authn`
- `authentication` -> `authn`
- `authorization` -> `authz`
- `oidc` -> `clients`
- `saml` -> `clients`
- `ldap` -> `federation`
- `infinispan` -> `ha`
- `cache` -> `ha`
- `metrics` -> `observability`
- `tracing` -> `observability`
- `telemetry` -> `observability`
- `terraform` -> `iac`
- `session` -> `tokens`
- `sessions` -> `tokens`
- `hardening` -> `security`
