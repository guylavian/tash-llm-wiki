---
title: How do you turn Keycloak's optional or preview features on or off?
type: question
question_tier: conceptual
domain: keycloak
slug: feature-flags-enable-disable
summary: Optional/preview/deprecated features are toggled with the build-time `features`/`features-disabled` options; changes require `kc.sh build`.
sources:
  - guide:server_configuration_guide
  - ref:rhbk-26-4-features.md
provenance:
  extracted: 6
  inferred: 1
  ambiguous: 0
tags: [server-config]
status: draft
updated: 2026-07-07
---

# How do you turn Keycloak's optional or preview features on or off?

**Use the build-time `features` and `features-disabled` options with `kc.sh build`.** Feature flags are a build option, not a runtime option, so toggling them requires a rebuild (and often a recreate rather than a rolling update).

## Enable a feature

```bash
bin/kc.sh build --features="docker,token-exchange"
```

Enable all preview features at once:

```bash
bin/kc.sh build --features="preview"
```

## Disable a default-on feature

```bash
bin/kc.sh build --features-disabled="impersonation"
```

A feature cannot appear in both `features` and `features-disabled`. Disabling a feature disables all its versions.

## Versioned vs unversioned names

You can target a specific version (`feature:v1`) or let the server resolve the unversioned name (`feature`) at runtime. Unversioned resolution uses: highest default-supported → highest non-default-supported → highest deprecated → highest preview → highest experimental version.

## Categories (RHBK 26.4)

- **Enabled by default (supported)**: `account:v3`, `admin:v2`, `admin-api:v1`, `admin-fine-grained-authz:v2`, `authorization:v1`, `ciba:v1`, `device-flow:v1`, `dpop:v1`, `hostname:v2`, `impersonation:v1`, `kerberos:v1`, `login:v2`, `opentelemetry:v1`, `organization:v1`, `par:v1`, `passkeys:v1`, `persistent-user-sessions:v1`, `recovery-codes:v1`, `rolling-updates:v1`, `step-up-authentication:v1`, `token-exchange-standard:v2`, `update-email:v1`, `user-event-metrics:v1`, `web-authn:v1`, and others.
- **Supported but disabled by default**: `docker:v1`, `fips:v1`, `multi-site:v1`.
- **Preview (not for production)**: `admin-fine-grained-authz:v1`, `client-auth-federated:v1`, `client-secret-rotation:v1`, `log-mdc:v1`, `rolling-updates:v2`, `scripts:v1`, `spiffe:v1`, `token-exchange:v1`.
- **Deprecated (off by default, will be removed)**: `instagram-broker:v1`, `login:v1`, `logout-all-sessions:v1`, `passkeys-conditional-ui-authenticator:v1`.

> **These tables are version-specific.** The lists above are from RHBK 26.4 — default/preview/deprecated membership moves between 26.0/26.2/26.4/26.6. Always confirm against the matching guide.

## References

**RH ground-truth:**
- `guide:server_configuration_guide` — Server Configuration Guide, Chapter 14 "Enabling and disabling features" (`_ref-keycloak-server_configuration_guide.md`)
- `ref:rhbk-26-4-features.md` — RHBK 26.4 Server Configuration Guide, Chapter 14, with the full feature category tables
- `ref:rhbk-26-6-techpreview.md` — RHBK 26.6 technology preview additions

**Wiki:**
- [[feature-flags]] — The entity page with detailed category tables and caveats
- [[build-vs-runtime-options]] — Why features need a build (not a runtime toggle)
- [[server-configuration]] — The overall config model
- [[multi-site-feature-flag]] — Multi-site requires a specific feature flag
