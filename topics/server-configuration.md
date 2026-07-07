---
title: RHBK Server Configuration — sources, build vs runtime, precedence
type: topic
domain: keycloak
slug: server-configuration
summary: "Red Hat build of Keycloak is configured from four ordered sources and distinguishes build-time options (baked into an optimized image) from runtime options (applied at `start`)."
sources:
  - guide:server_configuration_guide
provenance_extracted: 13
provenance_inferred: 1
provenance_ambiguous: 0
tags: [server-config, concept]
status: draft
updated: 2026-07-02
---

# RHBK Server Configuration

**Red Hat build of Keycloak is configured from four ordered sources and distinguishes build-time options (baked into an optimized image) from runtime options (applied at `start`).**

## Configuration sources and precedence

RHBK loads configuration from four sources, applied in this order (first wins):

1. **Command-line parameters** — `--<key-with-dashes>=<value>` (some have a `-<abbr>` shorthand).
2. **Environment variables** — `KC_<KEY_WITH_UNDERSCORES>=<value>`.
3. **Config file** — `conf/keycloak.conf` (or a file named with `[-cf|--config-file]`), `<key-with-dashes>=<value>`.
4. **Java KeyStore file** — `kc.<key-with-dashes>`, value is a password stored in the KeyStore (lowest priority; intended for sensitive options). Loaded via `--config-keystore` / `--config-keystore-password` (`--config-keystore-type` defaults to `PKCS12`).

So a CLI `--db-url=cliValue` overrides `KC_DB_URL=envVarValue`, which overrides `db-url=confFileValue`, which overrides the KeyStore value. See [[config-sources-precedence]].

The config file supports `${ENV_VAR}` placeholders with a `${ENV_VAR:fallback}` colon fallback. Non-alphanumeric chars in a key map to `_` in the env-var form; logging categories are an exception (`_` maps back to `.`), which is why ambiguous logging keys may need `KC_...`/`KCKEY_...` env-var pairs or a `keycloak.conf` indirection.

## Build options vs configuration (runtime) options

RHBK separates two classes of options (see [[build-vs-runtime-options]]):

- **Build options** (tool icon in *All configuration*) are persisted into an optimized image by `kc.sh build` — e.g. `db`, `features`, `health-enabled`, `metrics-enabled`, `vault`. They are stored in **plain text**, so never store secrets as build options.
- **Configuration (runtime) options** are applied at `start` — e.g. `db-url-host`, `db-password`, `hostname`, `https-certificate-file`.

The recommended optimized flow is `kc.sh build` followed by `kc.sh start --optimized`. With `--optimized`, RHBK skips the implicit build at startup. A build option re-specified at start with the *same* value is silently ignored; a *different* value logs a warning and the previously built value is used until you re-run `build`. Raw Quarkus properties go in `conf/quarkus.properties`; a build-time Quarkus property (lock icon in Quarkus docs) also requires `build`. RHBK config values take precedence over equivalent mapped Quarkus properties.

## Dev vs production startup mode

- `kc.sh start-dev` — development: HTTP enabled, `hostname-strict` effectively off, local (non-distributed) cache, theme/template caching disabled.
- `kc.sh start` — production, secure-by-default: HTTP disabled, a hostname **must** be configured, and an HTTPS/TLS setup is expected. Starting `start` without these fails on purpose.

## Going to production

Production hardening pulls together the per-area chapters (inferred — this
grouping/framing is this page's own synthesis across chapters, not a single
source's structure): [[tls-configuration]] for HTTPS, [[hostname-v2]] for public URLs, [[reverse-proxy-configuration]] for load balancers, [[database-configuration]] for a real DB (the default `dev-file` is dev-only), and [[distributed-caches]] for clustering. Other production knobs: `http-max-queued-requests` (load shedding; no limit by default → returns `503` over threshold) and IPv4/IPv6 stack selection via `JAVA_OPTS_APPEND` (`-Djava.net.preferIPv4Stack=true`, etc.). See the consolidated [[production-checklist]].

## Contradictions / caveats

- Hostname **v2** is the model in RHBK 26.x (`hostname:v2` feature, enabled by default); v1 was removed earlier. See [[hostname-v2]].
- `spi-admin--allowed-system-variables` (system/env variable references in realm config) is documented as a transitional capability that will be removed in a future release.
- These chapters are quoted from the **26.4** primary corpus; option names are stable across 26.0/26.2/26.4/26.6 but the *features* tables (preview/deprecated) shift per release — see [[feature-flags]].

## See also
- [[config-sources-precedence]]
- [[build-vs-runtime-options]]
- [[production-checklist]]
- [[hostname-v2]]
- [[tls-configuration]]
- [[reverse-proxy-configuration]]
- [[database-configuration]]
- [[management-interface]]
- [[feature-flags]]
- [[keycloak-vault]]
- [[kc-bootstrap-admin]]
- [[distributed-caches]]
