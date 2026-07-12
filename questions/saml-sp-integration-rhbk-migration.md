---
origin: eval-cohort
title: How do SAML service-provider apps integrate with RHBK and what survives migration?
type: question
domain: keycloak
slug: saml-sp-integration-rhbk-migration
summary: "SAML SPs integrate with RHBK as a SAML 2.0 IdP via entity descriptor exchange, metadata files, or protocol bindings; on RH-SSO 7.6→RHBK migration: the EAP 8 SAML feature pack and mod_auth_mellon survive, but RH-SSO 7.6 SAML adapters for EAP 6.x/7.x do not"
sources:
  - guide:migration_guide
  - guide:server_administration_guide
  - guide:securing_applications_and_services_guide
  - kb:migrating-applications
  - ref:securing-apps-oidc-saml.md
  - ref:migration-upgrading.md
provenance_extracted: 10
provenance_inferred: 2
provenance_ambiguous: 0
question_tier: conceptual
status: draft
updated: 2026-07-12
---

# How do SAML service-provider apps integrate with RHBK and what survives migration?

RHBK is a full SAML 2.0 Identity Provider. SAML SPs register as **clients** in a realm and exchange SAML assertions over browser-redirect/POST bindings.

## Integration methods

- **SAML entity descriptor**: export the SP's metadata XML and import it into RHBK, or configure manually in the Admin Console. RHBK also exposes its IdP metadata at `.../realms/<realm>/protocol/saml/descriptor` for the SP to consume. (`saml-clients-and-migration.md:28-34`, extracted)
- **[[mod-auth-mellon]]**: the Apache HTTPD SAML module turns httpd into a SAML SP, securing apps behind the proxy without embedding adapters. RHBK acts as IdP; the integration is file-based SP/IdP metadata exchange. (`mod-auth-mellon.md:24-30`, extracted)
- **EAP 8 SAML Galleon feature pack / RPM**: the supported in-app SAML adapter for JBoss EAP 8.x. (`saml-clients-and-migration.md:39-40`, extracted)
- **Framework-native SAML**: e.g. Spring Security SAML consuming RHBK's SP/IdP metadata directly. (`saml-clients-and-migration.md:43-44`, extracted)
- **Generic SAML SP**: any SAML 2.0-compliant SP can integrate — integration is metadata-file exchange, making it air-gap friendly (export/import files, no network). (`saml-clients-and-migration.md:69-73`, extracted)

## What survives RH-SSO 7.6 → RHBK migration

The SAML adapter story differs from OIDC — **not all adapters are dropped**:

| Adapter | Survives? | Detail |
|---|---|---|
| **EAP 8 SAML feature pack / RPM** | ✅ Supported | The target for EAP-hosted SAML SPs migrating to RHBK (`saml-clients-and-migration.md:39-40`) |
| **[[mod-auth-mellon]]** (Apache module) | ✅ Supported | Clean air-gap fit; works with RHBK as IdP (`saml-clients-and-migration.md:41-42`) |
| **Framework-native SAML** (e.g. Spring Security) | ✅ Supported | Consumes RHBK metadata, no Keycloak adapter needed (`saml-clients-and-migration.md:43-44`) |
| **RH-SSO 7.6 SAML adapter (EAP 7.x)** | 🔴 Not released for RHBK | Must re-platform to EAP 8 feature pack, mod_auth_mellon, or framework-native SAML (`saml-clients-and-migration.md:45-48`) |
| **RH-SSO 7.6 SAML adapter (EAP 6.x)** | 🔴 EOL | Unsupported by both products (`adapter-migration.md:41`) |

**Bridge guarantee:** RH-SSO 7.6 SAML adapters remain *supported in combination with* an RHBK 26.x server even though they are no longer released — migrate the server first, re-platform SPs after. (`adapter-migration.md:44-46`, extracted; `rhsso-to-rhbk-migration.md:96-98`, extracted)

## SAML-specific changes on migration

- **SP metadata exposes only encryption realm keys** (algorithm-tagged: `rsa-oaep-mgf1p` for RSA-OAEP, `rsa-1_5` for RSA1_5). (`references/migration-upgrading.md:147`, extracted)
- **`RSA_SHA1` / `DSA_SHA1` deprecated** — fail verification on Java 17+. (`references/migration-upgrading.md:147`, extracted)
- **SAML `SubjectConfirmationData` bearer check** in RHBK 26.6 — allow sufficient clock skew. (`references/migration-upgrading.md:207`, extracted)
- **SAML REDIRECT inflate cap** — 128KB default (`--spi-login-protocol--saml--max-inflating-size=`). (`references/migration-upgrading.md:213`, extracted)
- **Token exchange does not support SAML clients/IdPs** — SAML SPs cannot participate in OAuth2 token-exchange flows. (`securing-apps-oidc-saml.md:41-43`, extracted; `mod-auth-mellon.md:52-53`, extracted)

## Air-gap friendliness

SAML integration is metadata-file exchange — export the IdP descriptor and SP descriptor as files, import each side manually. No internet, no metadata-URL polling needed. (`saml-clients-and-migration.md:69-73`, extracted)

## Contradictions / caveats

- Adapter support combinations are version-sensitive — confirm the exact SP-adapter ↔ RHBK-server combination in `ref:rhbk-platform-support.md`. (`saml-clients-and-migration.md:76-77`, extracted)
- SAML wording is stable across RHBK 26.0–26.6; the "fully supported = EAP 8 SAML feature pack/RPM" statement appears consistently in the migration guides. (`saml-clients-and-migration.md:78-79`, extracted)

## See also
- [[saml-clients-and-migration]]
- [[adapter-migration]]
- [[mod-auth-mellon]]
- [[securing-apps-oidc-saml]]
- [[rhsso-to-rhbk-migration]]
- [[client-libraries-by-stack]]
- [[air-gapped-client-integration]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-migration_guide|keycloak reference — migration_guide]]
- [[_ref-keycloak-server_administration_guide|keycloak reference — server_administration_guide]]
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
- [[rhbk-26-6-migrating-applications|Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6]]
- [[references/securing-apps-oidc-saml|Securing Applications & Services with RHBK 26.6 (OIDC & SAML)]]
- [[references/migration-upgrading|Migration & Upgrading — RH-SSO 7.6 → RHBK and RHBK version upgrades — 26.6 (Offline Reference)]]
<!-- crosslink:end -->
