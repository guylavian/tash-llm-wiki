---
title: "What does windows-server-identity.pdf cover that the AD brain is missing?"
type: question
domain: active-directory
slug: windows-server-identity-coverage-gaps
summary: Gap analysis of the active-directory wiki brain against the full Microsoft Learn "Windows Server identity" doc set (4,163-page PDF). Of the in-scope pillars, Windows LAPS, AD CS, and the Solutions/Scenario guides are absent from the vault corpus entirely (AD FS is deliberately out of scope); within the one pillar present (AD DS) only FSMO has a synthesis page — ~221 reference notes are un-synthesized.
sources:
  - note:_sources/active-directory/fsmo-roles.md
  - web:https://learn.microsoft.com/windows-server/identity/ (Microsoft Learn — "windows-server identity", PDF export 4,163 pp / 451 articles, fetched 2026-06-18)
provenance_extracted: 6
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, migration, troubleshooting]
status: reviewed
updated: 2026-06-18
---

# What does windows-server-identity.pdf cover that the AD brain is missing?

**The PDF is the complete Microsoft Learn _Windows Server identity_ doc set (4,163
pages, ~451 articles) spanning four pillars — AD DS, Windows LAPS, AD CS, AD FS —
plus Solutions/Scenario guides. The wiki's `active-directory` brain currently
covers only AD DS, and even that only at the reference tier: three of the four
pillars are absent from the vault entirely, and the synthesis layer is three pages.**

## Body

### What the PDF contains (4 pillars + scenarios)
1. **Active Directory Domain Services (AD DS)** — overview, functional levels,
   deployment/design, replication & topology, DNS, FSMO, RODC, virtualized DCs,
   forest recovery, Group Policy, securing AD, service accounts, security
   principals.
2. **Windows LAPS** (Local Administrator Password Solution) — what it is, key
   concepts, get-started for AD and for Entra ID, policy settings, migrate from
   legacy LAPS, event logs, passwords/passphrases.
3. **Active Directory Certificate Services (AD CS)** — what AD CS is, CA Web
   Enrollment, certificate templates, renew root CA, export cert + private key,
   certificates & trust in Windows, migrate the CA, TPM key attestation.
4. **Active Directory Federation Services (AD FS)** — overview, design & deployment
   guides, operations, troubleshooting, **OpenID Connect/OAuth concepts**,
   **SAML 2.0 interop**, the claims engine/pipeline/rule language, federation
   server farms (WID/SQL), Web Application Proxy, device registration, MFA,
   conditional access, token-signing/decrypting/service certificates.
5. **Solutions / Scenario guides** — **Dynamic Access Control** (Central Access
   Policy, File Access Auditing, Access-Denied Assistance), Workplace Join / device
   registration, Conditional Access, advanced audit policy.

(AD FS alone is ~3,500 keyword hits across the PDF — the single largest section.)

### What the wiki AD brain has today
- **Reference tier** (`reference/active-directory/`): **221 content notes, all
  `ad-ds-*`** — i.e. the AD DS pillar only. A grep of the bodies finds **no
  dedicated LAPS, AD FS, or AD CS notes** (only incidental cross-mentions).
- **Synthesis tier**: **3 pages** — `[[active-directory-overview]]`,
  `[[active-directory-implementation-review]]` (the MOC), and one entity
  `[[fsmo-roles]]`.

### Gap A — three whole pillars + scenarios are absent from the vault (corpus gap)
The harvest that became `reference/active-directory/` ingested only the AD DS
section of the identity doc set. Missing from the vault entirely:

- **Windows LAPS** — no coverage of local-admin password rotation, the area most
  adjacent to the `security` area already declared in the taxonomy.
- **AD CS** — no PKI / certificate-template / enrollment coverage, despite AD CS
  underpinning LDAPS and smartcard auth.
- **Solutions/Scenario guides** — Dynamic Access Control, Workplace Join,
  Conditional Access.

> **AD FS is explicitly out of scope** for this brain (owner decision,
> 2026-06-18) — not relevant even though the PDF carries the largest section on it.
> Do not harvest or ingest AD FS material; treat its absence as intentional.
> The taxonomy still declares `ad-certificate-services` as an area, so AD CS is
> **in-scope by design but un-ingested**. (extracted from `_meta/taxonomy.md`.)

### Gap B — AD DS reference is present but ~99% un-synthesized
Only FSMO has an entity page. Major AD DS themes with rich reference coverage and
**zero synthesis page** (each is a strong INGEST candidate):

| Theme | Reference notes present | Synthesis |
|---|---|---|
| Replication & site topology (KCC, site links, cost/interval/schedule) | many | none |
| DNS for AD DS (AD-integrated zones, `_msdcs` SRV, disjoint namespace) | yes | none |
| Forest / domain / OU / site **design** | full design set | none |
| **Group Policy** (processing, scope, preferences, GPMC, modeling) | ~8 notes | none |
| **Securing AD / privileged access** (tiered admin, attack surface, credential theft, secure admin hosts, monitoring, appendices B–M) | ~20 notes | none |
| Service accounts: **gMSA / dMSA**, KDS root key, SPN/UPN | yes | none |
| Security principals: **SIDs, security groups, special identities**, default accounts | yes | none |
| Fine-grained password policies | yes | none |
| Functional levels, adprep, schema updates, upgrades | yes | none |
| **RODC** | yes | none |
| Virtualized DC / cloning | full set | none |
| **Forest recovery** (full step procedures) | full set | none |
| LDAP signing / channel binding / LDAP server cookies | yes | none |
| Windows Time Service / Kerberos time skew | yes | partial (overview only) |
| **Trusts** (declared area) | **no dedicated note** — only `reset-trust` in forest-recovery + incidental | none |

`trusts` is a declared area but, like AD FS/CS/LAPS, has **no dedicated reference
note** in the current harvest — flag it for the next harvest.

## Recommendation (what to do about it)
1. **Re-harvest the in-scope missing pillars** into `reference/active-directory/`
   — **Windows LAPS, AD CS**, and the Solutions/DAC guides — via
   `corpus_to_vault.py --domain active-directory`. The PDF itself is the source.
   **AD FS is excluded** (owner decision — not relevant).
2. **Add a dedicated `trusts` reference note** (and a Domain/Forest Trusts entity)
   — declared area, currently unbacked.
3. **INGEST the high-value AD DS themes** from Gap B into synthesis pages, starting
   with the ones the review-MOC already needs: **replication**, **DNS for AD DS**,
   **Group Policy**, **securing-AD / tiered-admin**, **gMSA/service accounts**,
   **forest recovery**. Each turns a cluster of un-linked reference notes into a
   cited topic + entities.
4. **Reconcile the shape label**: `[[active-directory-overview]]` calls this a
   "notes-first domain" in its body, but `_meta/taxonomy.md` declares
   `shape: corpus-backed` (221 reference notes exist). Fix one so they agree.

## Status update (2026-06-18 — first pass done)

A first pass closed the highest-value gaps (AD FS still excluded):
- **New pillars distilled + synthesized** (notes-first, paraphrased from the PDF):
  Windows LAPS → `_sources/active-directory/windows-laps.md` + [[windows-laps]] /
  [[laps-password-encryption]]; AD CS → `_sources/active-directory/ad-certificate-services.md`
  + [[ad-certificate-services]] / [[certification-authority-types]] / [[certificate-templates]].
- **AD DS themes synthesized** from the existing reference tier: [[ad-replication]],
  [[dns-for-ad-ds]], [[group-policy]], [[securing-active-directory]],
  [[group-managed-service-accounts]], [[ad-forest-recovery]],
  [[fine-grained-password-policies]].

### Second pass (2026-06-18) — AD DS fully synthesized

A multi-agent workflow (11 theme-cluster drafters + verifiers + an MOC rebuild) then
synthesized the **entire AD DS reference tier** into ~52 more pages — the
`active-directory` brain is now **66 synthesis pages** and `lint.py` reports **no
broken links, no orphans, no errors** for the domain. New AD DS coverage: logical
design (forest/domain/OU/site/DNS design + capacity/placement), deployment & upgrade
(install/promote, functional levels, adprep/schema, demote/remove), security
(tiered admin, secure admin hosts, credential theft, AdminSDHolder/protected groups,
monitoring, advanced audit, SRP, attack-surface), security principals (SIDs, groups,
special identities, default accounts), replication internals (KCC, site links, global
catalog, UG caching), DNS internals (AD-integrated zones, DC locator, disjoint
namespace, SPN/UPN), service accounts (gMSA/dMSA/KDS root key), virtualized DCs
(cloning, VM-GenerationID), directory internals (LDAP signing/channel binding, Recycle
Bin, NTDS/32k pages, max limits), RODC, Windows Time Service, RID issuance, admin
tools, krbtgt reset & metadata cleanup. The `active-directory-implementation-review`
MOC was rebuilt to a 30-row rule→symptom checklist + a 29-row symptom→cause reverse
index + a full domain map.

**AD DS is now treated as complete.** Remaining (other pillars, lower priority):
the Solutions/Scenario guides (Dynamic Access Control, Workplace Join), a dedicated
`trusts` reference note, and full doc-body harvests of LAPS/AD CS (currently distilled
summaries only). AD FS stays out of scope.

## References

**Ground truth — Microsoft Learn (corpus tier for this domain)**
- `reference/active-directory/` — 221 `ad-ds-*` notes (the AD DS pillar; the
  authority for what's already in the vault).
- `web:` Microsoft Learn *Windows Server identity* — the PDF, 4,163 pp / 451
  articles, fetched 2026-06-18 (the authority for what the full doc set covers).
- `_meta/taxonomy.md` — declares the domain's in-scope areas (incl.
  `ad-certificate-services`, `ad-authn`, `trusts`).

**Wiki**
- [[active-directory-overview]] — current spine (AD DS only)
- [[active-directory-implementation-review]] — review MOC (the synthesis target for Gap B)
- [[fsmo-roles]] — the one existing entity

## See also
- [[active-directory-overview]]
- [[active-directory-implementation-review]]
