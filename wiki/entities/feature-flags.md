---
title: Feature flags (enabling & disabling features)
type: entity
domain: keycloak
slug: feature-flags
summary: "Optional, preview, and deprecated functionality is toggled with the build-time `features` / `features-disabled` options."
sources:
  - guide:server_configuration_guide
provenance: needs-review
tags: [server-config]
status: draft
updated: 2026-06-16
---

# Feature flags

**Optional, preview, and deprecated functionality is toggled with the build-time `features` / `features-disabled` options.**

## Enabling / disabling

```
bin/kc.sh build --features="docker,token-exchange"   # enable
bin/kc.sh build --features="preview"                 # enable ALL preview features
bin/kc.sh build --features-disabled="impersonation"  # disable a default-on feature
```

`features` is a **build option** — changes need a `build` (and a recreate rather than a rolling update for some features). A feature cannot appear in both lists. Disabling a feature disables all its versions.

## Versioned vs unversioned names

Names may be versioned (`feature:v1` — that exact version) or unversioned (`feature` — resolved at runtime). Unversioned resolution precedence: highest default-supported → highest non-default-supported → highest deprecated → highest preview → highest experimental version.

## Categories (RHBK 26.4)

- **Enabled by default (supported)**: `account:v3`, `admin:v2`, `admin-api:v1`, `admin-fine-grained-authz:v2`, `authorization:v1`, `ciba:v1`, `device-flow:v1`, `dpop:v1`, `hostname:v2`, `impersonation:v1`, `kerberos:v1`, `login:v2`, `opentelemetry:v1`, `organization:v1`, `par:v1`, `passkeys:v1`, `persistent-user-sessions:v1`, `recovery-codes:v1`, `rolling-updates:v1`, `step-up-authentication:v1`, `token-exchange-standard:v2`, `update-email:v1`, `user-event-metrics:v1`, `web-authn:v1`, and others.
- **Supported but disabled by default**: `docker:v1`, `fips:v1`, `multi-site:v1`.
- **Preview (not for production)**: `admin-fine-grained-authz:v1`, `client-auth-federated:v1`, `client-secret-rotation:v1`, `log-mdc:v1`, `rolling-updates:v2`, `scripts:v1`, `spiffe:v1`, `token-exchange:v1`.
- **Deprecated (off by default, will be removed)**: `instagram-broker:v1`, `login:v1`, `logout-all-sessions:v1`, `passkeys-conditional-ui-authenticator:v1`.

## Contradictions / caveats
- **These tables are version-specific.** The lists above are from **26.4**; default/preview/deprecated membership moves between 26.0/26.2/26.4/26.6 (e.g. token-exchange evolved from preview `token-exchange:v1` toward supported `token-exchange-standard:v2`). Always confirm against the matching guide.
- Preview features may change or be removed and are unsupported for production.
- `hostname:v2` is a default-on feature — see [[hostname-v2]].

## See also
- [[server-configuration]]
- [[build-vs-runtime-options]]
- [[tokens-and-sessions]]
- [[distributed-caches]]
- [[production-checklist]]
