---
title: Behavior of KC_CACHE_EMBEDDED_MCAST_PORT with --cache=local
type: question
domain: keycloak
slug: kc-cache-embedded-mcast-port-behavior
summary: "KC_CACHE_EMBEDDED_MCAST_PORT is not a recognized Keycloak env var. It is silently ignored under any cache mode (including --cache=local) — no deprecation warning, no error."
sources:
  - guide:server_configuration_guide
  - guide:release_notes
provenance:
  extracted: 3
  inferred: 1
  ambiguous: 0
status: draft
updated: 2026-07-05
---

# Behavior of `KC_CACHE_EMBEDDED_MCAST_PORT` with `--cache=local`

**`KC_CACHE_EMBEDDED_MCAST_PORT` is not a known environment variable in any RHBK 26.x release. It is silently ignored whether the server runs with `--cache=local` or `--cache=ispn`.**

## Why it doesn't exist

RHBK's Quarkus-based configuration framework maps `KC_*` env vars to known CLI options. The naming convention is `KC_` + the CLI option name uppercased with underscores (e.g. `--cache-stack` → `KC_CACHE_STACK`, `--cache-embedded-network-bind-port` → `KC_CACHE_EMBEDDED_NETWORK_BIND_PORT`).

There is no CLI option `--cache-embedded-mcast-port` in the shipped config reference (`rhbk-26-4-all-config.md`), so no `KC_CACHE_EMBEDDED_MCAST_PORT` is recognized.

## The correct way to set the multicast port

The JGroups multicast port is a JGroups system property, not a Keycloak CLI option. Per `rhbk-26-4-caching.md` §10.4.1:

> By default, Red Hat build of Keycloak uses 239.6.7.8 as multicast address for `jgroups.mcast_addr` and **46655** for the multicast port `jgroups.mcast_port`. Use `-D<property>=<value>` to pass the properties via the `JAVA_OPTS_APPEND` environment variable or in the CLI command.

```bash
export JAVA_OPTS_APPEND="-Djgroups.mcast_port=46656"
```

## What happens with `--cache=local`

When running with `--cache=local` (or `KC_CACHE=local`, or via `start-dev` which implicitly sets it), the embedded Infinispan container uses **local-only** mode — no JGroups transport stack is initialized at all. The multicast port is irrelevant because there is no cluster to form.

## Result: silent ignore, not a warning

- `KC_CACHE_EMBEDDED_MCAST_PORT` → Keycloak's config layer doesn't recognise the key → the env var is **never read** → completely silent.
- No deprecation warning — there is no known option to deprecate.

The effect is the same under both `--cache=local` and `--cache=ispn`: the var is unclaimed and ignored.

## See also
- [[distributed-caches]]
- [[quarkus-config-migration]]
