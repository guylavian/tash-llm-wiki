---
origin: eval-cohort
title: Is --cache-embedded-mcast-buffer-size a real kc.sh flag?
type: question
domain: keycloak
slug: cache-embedded-mcast-buffer-size-fabricated
summary: "`--cache-embedded-mcast-buffer-size` is a fabricated flag — it does not appear in any RHBK/Keycloak reference document. The closest real multicast configuration is `-Djgroups.mcast_port` passed via `JAVA_OPTS_APPEND`."
sources:
  - ref: rhbk-26-4-caching.md
  - ref: rhbk-26-2-caching.md
provenance_extracted: 2
provenance_inferred: 0
provenance_ambiguous: 0
tags: [ha]
status: draft
updated: 2026-07-12
---

# `--cache-embedded-mcast-buffer-size` is a fabricated flag

**This flag does not exist** in the RHBK/Keycloak corpus. The string `mcast-buffer-size` does not appear in any configuration reference, caching guide, or CLI option table across RHBK 26.0–26.6.

## What actually exists for multicast and embedded cache transport

The JGroups multicast **port** is configured as a system property, not a `--cache-embedded-*` CLI option:

> By default, Red Hat build of Keycloak uses `239.6.7.8` as multicast address for `jgroups.mcast_addr` and `46655` for the multicast port `jgroups.mcast_port`. — `reference/keycloak/rhbk-26-4-caching.md:229-232`

Pass it via `-D` through `JAVA_OPTS_APPEND` (`reference/keycloak/rhbk-26-4-caching.md:234-236`).

The real `--cache-embedded-*` CLI options cover:
- `--cache-embedded-network-bind-address` / `--cache-embedded-network-bind-port` — TCP bind for JGroups
- `--cache-embedded-network-external-address` / `--cache-embedded-network-external-port` — external address for non-transparent networks
- `--cache-embedded-mtls-enabled` and related `-mtls-*` options — TLS for transport stack
- `--cache-embedded-${CACHE_NAME}-max-count` — per-cache entry limits (e.g. `--cache-embedded-sessions-max-count=10000`)
- `--spi-cache-embedded-default-site-name`, `--spi-cache-embedded-default-rack-name`, `--spi-cache-embedded-default-machine-name` — topology hints

None of the 95+ `cache-embedded` references in the corpus contain `mcast-buffer-size`.

## Why this matters

If supplied, RHBK will silently ignore `--cache-embedded-mcast-buffer-size` (unknown option). To tune JGroups multicast behavior, use `-D` system properties or switch to a TCP/jdbc-ping stack (the default for Kubernetes deployments, where multicast is typically unavailable).

## References

**RH ground-truth (`ref:` tier):**
- `ref:rhbk-26-4-caching.md` — Caching configuration guide (RHBK 26.4): JGroups mcast_addr/mcast_port defaults, `--cache-embedded-*` option table, transport stacks
- `ref:rhbk-26-2-caching.md` — Same guide for RHBK 26.2 (identical multicast language)

**Wiki:**
- [[distributed-caches]] — embedded vs external caches, cache types, cluster transport
