---
title: "What is Keycloak / RHBK? (overview)"
type: question
domain: keycloak
slug: what-is-keycloak
summary: "Keycloak (productized as Red Hat build of Keycloak) is a standalone single sign-on server that secures web apps and REST services over OIDC/OAuth2/SAML: apps redirect users to it, never see credentials, and receive signed tokens; it adds LDAP/AD federation, identity brokering, fine-grained authorization, and SPI-based extensibility, running on Quarkus with an OpenShift operator."
sources:
  - kb:red_hat_build_of_keycloak_features_and_concepts
  - guide:server_administration_guide
  - guide:securing_applications_and_services_guide
  - guide:server_configuration_guide
  - guide:migration_guide
  - guide:operator_guide
  - guide:high_availability_guide
  - guide:server_developer_guide
  - guide:authorization_services_guide
provenance_extracted: 16
provenance_inferred: 2
provenance_ambiguous: 0
question_tier: conceptual
tags: [realm, clients, tokens, concept]
status: draft
updated: 2026-07-09
---

# What is Keycloak / RHBK?

**Q: "Tell me about Keycloak."**

**Keycloak — shipped by Red Hat as Red Hat build of Keycloak (RHBK) — is a single
sign-on solution for web apps and RESTful web services**, whose stated goal is to
make security simple by providing out-of-the-box, tailorable security features and
customizable user-facing UIs for login, registration, administration, and account
management (`reference/keycloak/rhbk-26-4-red-hat-build-of-keycloak-features-and-concepts.md:19`).

## How it operates

It is a **separate server you manage on your network**; applications are configured
to point to it and be secured by it, using **open protocol standards — OpenID
Connect or SAML 2.0**. Browser apps redirect the user to the Keycloak login page, so
**users are isolated from applications and applications never see a user's
credentials** — they receive a cryptographically signed identity token or assertion
instead, carrying profile and permission data
(`reference/keycloak/rhbk-26-4-red-hat-build-of-keycloak-features-and-concepts.md:41`).

## Core building blocks

- **Realm** — manages a set of users, credentials, roles, and groups; a user belongs
  to and logs into a realm, and realms are isolated from one another
  (`...features-and-concepts.md:72-73`). The **master realm** is created at first
  start and should be used only to create/manage other realms — put end users
  elsewhere (`topics/realm-administration.md:25-31`).
- **Client** — an entity (usually an app/service) that requests Keycloak to
  authenticate a user (`...features-and-concepts.md:74-75`). Clients split into
  **confidential** (server-side, can hold a secret) and **public** (SPA/native,
  PKCE-hardened redirect flows) (`topics/securing-apps-oidc-saml.md:56-65`); every
  client has a built-in **service account** for machine-to-machine tokens
  (`...features-and-concepts.md:92-93`).
- **Tokens & sessions** — short-lived JWT access tokens, refresh tokens bounded by
  SSO session idle/max lifespans; resource servers validate by JWKS (offline) or
  introspection (online) (`topics/tokens-and-sessions.md:25-32`).

## Feature areas (the map)

- **Protocols & flows** — OIDC is the recommended protocol for new apps; SAML 2.0
  mainly for existing enterprise SPs (`topics/securing-apps-oidc-saml.md:34-43`).
  Authorization Code + PKCE is the recommended flow; Implicit and Direct Grant are
  discouraged/removed in OAuth 2.1 (`topics/securing-apps-oidc-saml.md:80-85`).
- **User federation** — built-in LDAP/Active Directory provider (on the User
  Storage SPI): import vs on-demand storage modes, READ_ONLY/WRITABLE/UNSYNCED edit
  modes, LDAP mappers (`topics/ldap-user-federation.md:27-43`).
- **Identity brokering & social login** — delegates authentication to external
  OIDC/SAML/social IdPs (Google, GitHub, Facebook, Microsoft, …) and then issues
  its own token; the client never sees the external protocol
  (`topics/identity-brokering.md:22-41`).
- **Fine-grained authorization** — Authorization Services turn a confidential
  client into a central policy decision point (resources, scopes, policies,
  permissions; UMA 2.0-based) beyond plain RBAC
  (`topics/fine-grained-authorization.md:26-40`).
- **Extensibility** — everything user-facing is themeable
  (`...features-and-concepts.md:116-117`), and server behavior is customized via
  SPIs: a `Provider` + `ProviderFactory` in a JAR under `providers/`, activated by
  `kc.sh build` (`topics/spi-provider-model.md:24-32`).

## Running it

- **Runtime & config** — RHBK is built on **Quarkus** (RH-SSO 7.6 ran JBoss EAP)
  (`topics/rhsso-to-rhbk-migration.md:41-44`); configured from four ordered sources
  (CLI > env > `conf/keycloak.conf` > keystore) with build-time vs runtime options
  (`topics/server-configuration.md:23-30,36-41`). `kc.sh start-dev` is for dev;
  `kc.sh start` is secure-by-default production and refuses to start without
  hostname/TLS (`topics/server-configuration.md:45-46`).
- **OpenShift** — deploy via the RHBK Operator (OLM): a `Keycloak` CR is reconciled
  into a StatefulSet/Service/Ingress (`topics/operator-deployment.md:27-29`).
- **HA** — two documented shapes: single OpenShift cluster with embedded Infinispan,
  or two-site Active/Passive with an external Data Grid; the guide prioritizes
  consistency over availability (`topics/rhbk-ha-architectures.md:26-29`).

## Product lineage & versions

RHBK is the rebased successor to legacy **RH-SSO 7.x** (last line 7.6)
(`topics/rhsso-to-rhbk-migration.md:41-44`); RHBK and upstream OSS Keycloak are the
same server with minimal differences from Keycloak 22+ — Red Hat artifacts, no
bundled Oracle/MSSQL drivers (`topics/rhsso-to-rhbk-migration.md:69-73`). RHBK ships
as the **26.0 / 26.2 / 26.4 / 26.6** minor streams (`topics/realm-administration.md:65-66`).
Practically, "Keycloak the project" is what you extend and follow upstream, while
"RHBK the product" is the supported snapshot you run (inferred — framing across the
migration guide, not stated verbatim in one source).

## References

**RH ground-truth (kb: / guide:)**
- kb:red_hat_build_of_keycloak_features_and_concepts — Chapter 1. Red Hat build of Keycloak features and concepts (Server Administration Guide 26.4)
- kb:configuring-realms — Chapter 3. Configuring realms (via [[realm-administration]])
- kb:oidc-layers- / kb:overview- — Securing applications with OpenID Connect / Authorization services overview (via [[securing-apps-oidc-saml]])
- kb:user-storage-federation — Chapter 4. Using external storage (via [[ldap-user-federation]])
- kb:identity_broker — Chapter 9. Integrating identity providers (via [[identity-brokering]])
- kb:migrating-server / kb:migrating-keycloak — Migration Guide chapters (via [[rhsso-to-rhbk-migration]])
- kb:operator_guide/installation- / basic-deployment- — Operator Guide chapters (via [[operator-deployment]])
- kb:multi-cluster-introduction / kb:single-cluster-introduction — High Availability Guide chapters (via [[rhbk-ha-architectures]])
- kb:…/server_developer_guide/providers — Chapter 4. Service Provider Interfaces (via [[spi-provider-model]])
- kb:authorization_services_guide/overview — Authorization services overview (via [[fine-grained-authorization]])
- guide:server_configuration_guide (via [[server-configuration]])

**Wiki**
- [[keycloak-overview]] · [[securing-apps-oidc-saml]] · [[realm-administration]] ·
  [[tokens-and-sessions]] · [[server-configuration]] · [[rhsso-to-rhbk-migration]] ·
  [[ldap-user-federation]] · [[identity-brokering]] · [[fine-grained-authorization]] ·
  [[spi-provider-model]] · [[operator-deployment]] · [[rhbk-ha-architectures]]

## See also
- [[keycloak-overview]]
- [[production-checklist]]
- [[sso-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-4-red-hat-build-of-keycloak-features-and-concepts|Chapter 1. Red Hat build of Keycloak features and concepts]]
- [[_ref-keycloak-server_administration_guide|keycloak reference — server_administration_guide]]
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
- [[_ref-keycloak-server_configuration_guide|keycloak reference — server_configuration_guide]]
- [[_ref-keycloak-migration_guide|keycloak reference — migration_guide]]
- [[_ref-keycloak-operator_guide|keycloak reference — operator_guide]]
- [[_ref-keycloak-high_availability_guide|keycloak reference — high_availability_guide]]
- [[_ref-keycloak-server_developer_guide|keycloak reference — server_developer_guide]]
- [[_ref-keycloak-authorization_services_guide|keycloak reference — authorization_services_guide]]
<!-- crosslink:end -->
