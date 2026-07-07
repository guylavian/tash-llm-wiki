---
title: What is Active Directory Domain Services and what are its fundamental concepts?
type: question
domain: active-directory
slug: active-directory-domain-services-fundamentals
summary: "AD DS is Microsoft's directory service — a hierarchical, multi-master-replicated store of users, computers, and policy, hard-wired to DNS for locating DCs and to Kerberos/NTLM for authentication. Its fundamental concepts are: forest/domain/OU hierarchy, multi-master replication with five FSMO single-master roles, the security principal model (users/computers/groups with SIDs), Group Policy, DNS integration, and site topology for replication efficiency."
sources:
  - note:_sources/active-directory/_raw/identity/ad-ds/get-started/virtual-dc/Active-Directory-Domain-Services-Overview.md
  - note:_sources/active-directory/_raw/identity/ad-ds/get-started/replication/Active-Directory-Replication-Concepts.md
provenance:
  extracted: 8
  inferred: 3
  ambiguous: 0
status: draft
updated: 2026-07-07
---

# What is Active Directory Domain Services and what are its fundamental concepts?

**Active Directory Domain Services (AD DS) is Microsoft's directory service: a hierarchical, distributed store of objects (users, computers, groups, printers, policy) organized into a forest–domain–OU tree, replicated among domain controllers via multi-master replication, and dependent on DNS for service location and on Kerberos/NTLM for authentication.**

## Body

### What AD DS is

AD DS is the directory service that ships with Windows Server. A domain controller (DC) hosts the NTDS.dit database and authenticates users, enforces security policy, and maintains the directory. All DCs in a domain accept writes and converge changes through **multi-master replication** — any DC can process an update, which then propagates to all other DCs.

### Fundamental concepts

**Forest–Domain–OU hierarchy:**
- **Forest** — the outermost security and replication boundary. All domains in a forest share a common schema, configuration, and global catalog. The first domain in a forest is the forest root domain. ([[active-directory-overview]], [[forest-design-models]])
- **Domain** — a security boundary and replication partition. Domains in a forest are linked by transitive trusts. Each domain has its own security policy (password rules, lockout). ([[domain-design]])
- **Organizational Unit (OU)** — a container inside a domain for grouping objects. OUs are the unit of **Group Policy application** and **delegation** (administrative authority can be assigned at the OU level). ([[organizational-unit-design]])

**Multi-master replication + FSMO roles:**
AD replicates changes between DCs automatically (pull-based using connection objects built by the **Knowledge Consistency Checker**). Five operations are exceptions that require a **single-master** holder — the **FSMO roles** ([[fsmo-roles]]):
- Forest-wide: **Schema Master**, **Domain Naming Master**
- Per-domain: **RID Master** (SID uniqueness), **PDC Emulator** (time + password processing), **Infrastructure Master** (cross-domain references)

**Security principals and SIDs:**
A **security principal** is any entity the OS can authenticate — a user, computer, or group. Each principal is identified by a globally unique **Security Identifier (SID)**, issued when the object is created and never reused. ([[security-principals]], [[security-identifiers-sid]])

**Security groups** collect principals into manageable units. Three scopes — **Domain Local**, **Global**, **Universal** — governed by the AGDLP nesting pattern. ([[security-groups]])

**Group Policy:**
Group Policy centrally configures computer and user settings. A **GPO** (Group Policy Object) has two parts: an AD container and a SYSVOL template. It is scoped by linking to a site, domain, or OU, and applied by client-side extensions at startup/sign-in. ([[group-policy]])

**DNS dependency:**
AD DS is hard-wired to DNS. Clients locate a DC via **SRV records** under `_msdcs.<forest-root>` — the **DC Locator** algorithm. **AD-integrated DNS zones** store zone data in the directory and replicate with AD, eliminating zone transfers. A disjoint namespace (AD domain != client's primary DNS suffix) is supported but complex. ([[dns-for-ad-ds]])

**Site topology and replication:**
AD uses **sites** (sets of well-connected subnets), **site links** (with cost/interval/schedule), and the **KCC** to build an efficient replication topology. Intra-site replication is frequent/uncompressed; inter-site uses configurable cost and schedule to trade convergence speed against WAN load. The **Global Catalog** is a DC that holds a partial read replica of every domain in the forest, enabling forest-wide searches. ([[ad-replication]], [[global-catalog]])

**Time synchronization:**
Kerberos authentication requires clock skew under 5 minutes. The **PDC Emulator** in the forest root domain is the authoritative time source; the **Windows Time Service (W32Time)** propagates it down the domain hierarchy. ([[windows-time-service]])

## Contradictions / caveats

- Most "AD is broken" tickets trace to broken DNS or time skew, not the directory engine itself (inferred — recurring pattern observed across troubleshooting references).
- Sites and subnets affect both replication efficiency **and** client DC location; misconfigured site topology causes logon delays even when replication appears healthy. (inferred)

## References

### RH ground-truth (`note:` raw tier)
- [[ad-ds-active-directory-domain-services-overview|Overview of Active Directory Domain Services]] (reference note in `reference/active-directory/`)
- [[ad-ds-active-directory-replication-concepts|Active Directory Replication Concepts]]
- [[ad-ds-understand-security-principals|Security Principals]]
- [[ad-ds-understand-security-identifiers|Security Identifiers]]
- [[ad-ds-understand-security-groups|Active Directory Security Groups]]
- [[ad-ds-group-policy-overview|Group Policy overview for Windows Server]]
- [[ad-ds-dns-and-ad-ds|DNS and AD DS]]
- [[ad-ds-forest-design-models|Forest Design Models]]

### Wiki (`[[slug]]` pages)
- [[active-directory-overview]] — the spine for this domain
- [[fsmo-roles]] — the five single-master roles
- [[ad-replication]] — multi-master replication and site topology
- [[domain-design]] — single vs. regional domain forest models
- [[forest-design-models]] — organizational/resource/restricted-access models
- [[group-policy]] — GPO structure and application
- [[dns-for-ad-ds]] — DNS as the AD locator service
- [[security-principals]] — users, computers, and groups
- [[security-identifiers-sid]] — SID structure and well-known SIDs
- [[security-groups]] — group scopes and AGDLP nesting
