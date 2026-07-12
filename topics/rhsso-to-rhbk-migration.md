---
title: RH-SSO 7.x → Red Hat Build of Keycloak Migration
type: topic
domain: keycloak
slug: rhsso-to-rhbk-migration
summary: "Moving from legacy Red Hat Single Sign-On 7.6 to Red Hat Build of Keycloak (RHBK), the supported successor product — and, by the same machinery, upgrading between RHBK versions"
sources:
  - guide:migration_guide
  - ref:migration-upgrading.md
  - ref:rhbk-platform-support.md
  - kb:migrating-server
  - kb:migrating-operator
  - kb:migrating-applications
  - kb:migrating-providers
  - kb:migrating-themes
  - kb:migrating-keycloak
  - kb:other-changes
source_notes:
  - "[[rhbk-26-6-migrating-server]]"
  - "[[rhbk-26-6-migrating-operator]]"
  - "[[rhbk-26-6-migrating-applications]]"
  - "[[rhbk-26-6-migrating-providers]]"
  - "[[rhbk-26-6-migrating-themes]]"
  - "[[rhbk-26-6-migrating-keycloak]]"
  - "[[rhbk-26-6-other-changes]]"
provenance_extracted: 10
provenance_inferred: 4
provenance_ambiguous: 0
tags: [migration, concept]
status: draft
updated: 2026-07-02
---

# RH-SSO 7.x → Red Hat Build of Keycloak Migration

**Moving from legacy Red Hat Single Sign-On 7.6 to Red Hat Build of Keycloak
(RHBK), the supported successor product — and, by the same machinery, upgrading
between RHBK versions.**

## Body
RHBK is the rebased successor to RH-SSO 7.x (the last RH-SSO line is **7.6**).
The single biggest architectural change is the runtime: RH-SSO 7.6 ran on
**JBoss EAP**, while RHBK is built on **Quarkus**, so the whole configuration
model changes (see [[quarkus-config-migration]]). Migration spans several
surfaces:

- **Server** — stand up RHBK on OpenJDK 21, map the EAP `standalone.xml`
  datasource/TLS/cache/hostname/vault config to `kc.sh` options, then point it at
  the existing database. Covered in [[server-config-migration]] and
  [[database-auto-migration]]. RHBK auto-migrates the DB schema on first start.
- **Operator** — RH-SSO Operator → RHBK [[rhbk-operator]]; the `Keycloak` CR is
  a complete rewrite and is **not** backward compatible. See
  [[operator-cr-migration]].
- **Apps / adapters** — several legacy RH-SSO Java adapters are no longer
  released; re-platform clients onto standard OIDC/SAML. See
  [[adapter-migration]].
- **Custom providers / themes / templates** — recompile SPIs against RHBK
  (Jakarta EE 10, removed APIs), port themes; OpenShift Templates give way to the
  operator CRs. See [[custom-provider-migration]] and [[keycloak-themes]].

### Two migration directions
This guide actually folds in **three** source→target paths, all of which funnel
through the same Quarkus/DB-migration machinery (inferred — this three-way
framing is this page's own synthesis across the migration-guide chapters, not
stated as such in any one source):

1. **RH-SSO 7.6 → RHBK** — the largest jump (EAP→Quarkus, new Operator, dropped
   adapters). The bulk of this page.
2. **Upstream Keycloak → RHBK** — minimal differences from Keycloak 22+. Match
   the Keycloak version to the target RHBK version first, then swap distribution
   artifacts; Operator CRs are compatible. Differences: artifacts come from the
   Red Hat customer portal, Oracle/MSSQL drivers are **not** bundled, and the
   GELF log handler is absent. (kb:migrating-keycloak)
3. **RHBK x.y → RHBK x.z (version upgrade)** — same product; just review the
   per-version release notes and let [[database-auto-migration]] run. The
   `recreate` upgrade strategy (operator) and manual SQL export apply here too.

## Downstream-product impact
- **3scale:** 3scale 2.14 still requires RH-SSO **7.6**, not RHBK — RHBK becomes
  the supported 3scale IdP only in a future 3scale release (inferred — not found
  in this page's cited sources; verify against the 3scale supported-config matrix
  before relying on it). See
  [[3scale-rhsso-support]]. Sequence the migration so a 3scale dependency doesn't
  strand you on RH-SSO (inferred).

## Contradictions / caveats
- Confirm supported source/target versions and feature parity in
  `ref:rhbk-platform-support.md` for the exact RHBK version — preview features in
  RH-SSO may have different status in RHBK.
- Check each dependent product's (3scale, OpenShift, etc.) own supported-config
  page; the IdP migration is not automatically "supported" just because RHBK runs.
- **Version drift in transport stacks:** the default JGroups stack is
  `jdbc-ping` from 26.2; all stacks except `kubernetes` were deprecated in 26.2,
  and `kubernetes` itself was deprecated in 26.4. Plan cache config accordingly —
  see [[server-config-migration]] and [[distributed-caches]].
- RH-SSO 7.6 adapters remain *supported in combination with* an RHBK 26.x server
  even though those adapters are no longer released — useful as a bridge. See
  [[adapter-migration]].

## See also
- [[server-config-migration]]
- [[quarkus-config-migration]]
- [[database-auto-migration]]
- [[operator-cr-migration]]
- [[adapter-migration]]
- [[custom-provider-migration]]
- [[rhbk-operator]]
- [[3scale-rhsso-support]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-migration_guide|keycloak reference — migration_guide]]
- [[references/migration-upgrading|Migration & Upgrading — RH-SSO 7.6 → RHBK and RHBK version upgrades — 26.6 (Offline Reference)]]
- [[references/rhbk-platform-support|RHBK Platform & Support — Offline Reference]]
- [[rhbk-26-6-migrating-server|Chapter 2. Migrating a Red Hat Single Sign-On 7.6 server]]
- [[rhbk-26-6-migrating-operator|Chapter 3. Migrating Operator deployments on Openshift]]
- [[rhbk-26-6-migrating-applications|Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6]]
- [[rhbk-26-6-migrating-providers|Chapter 6. Migrating custom providers]]
- [[rhbk-26-6-migrating-themes|Chapter 7. Migrating custom themes]]
- [[rhbk-26-6-migrating-keycloak|Chapter 8. Migrating upstream Keycloak to Red Hat build of Keycloak 26.6]]
- [[rhbk-26-6-other-changes|Chapter 9. Other notable changes]]
<!-- crosslink:end -->
