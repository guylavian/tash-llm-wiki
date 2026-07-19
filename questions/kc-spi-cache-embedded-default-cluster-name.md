---
origin: eval-cohort
title: KC_SPI_CACHE_EMBEDDED_DEFAULT_CLUSTER_NAME does not exist
type: question
domain: keycloak
slug: kc-spi-cache-embedded-default-cluster-name
summary: "The environment variable KC_SPI_CACHE_EMBEDDED_DEFAULT_CLUSTER_NAME does not exist in Keycloak/RHBK; the real topology env vars are SITE_NAME, RACK_NAME, and MACHINE_NAME"
sources:
  - kb:rhbk-26-4-caching
provenance_extracted: 3
provenance_inferred: 0
provenance_ambiguous: 0
question_tier: conceptual
tags: [ha, spi]
status: draft
updated: 2026-07-12
---

# KC_SPI_CACHE_EMBEDDED_DEFAULT_CLUSTER_NAME does not exist

**The environment variable `KC_SPI_CACHE_EMBEDDED_DEFAULT_CLUSTER_NAME` does not exist in Red Hat build of Keycloak (RHBK).** Anyone who asks what this variable does is either asking about a typo or a fabrication. The real cache-topology environment variables follow the pattern `KC_SPI_CACHE_EMBEDDED__{section}__{key}` with double underscores as delimiters.

## Real topology env vars

The RHBK Server Configuration Guide documents three topology-hint environment variables for the embedded Infinispan cache (`reference/keycloak/rhbk-26-4-caching.md:156-177`):

| SPI option | Environment variable | Purpose |
|---|---|---|
| `spi-cache-embedded--default--site-name` | `KC_SPI_CACHE_EMBEDDED__DEFAULT__SITE_NAME` | Unique datacenter/site name for cross-datacenter deployments (extracted: `rhbk-26-4-caching.md:158-163`) |
| `spi-cache-embedded--default--rack-name` | `KC_SPI_CACHE_EMBEDDED__DEFAULT__RACK_NAME` | Unique rack name to spread replicas across physical racks (extracted: `rhbk-26-4-caching.md:164-170`) |
| `spi-cache-embedded--default--machine-name` | `KC_SPI_CACHE_EMBEDDED__DEFAULT__MACHINE_NAME` | Unique machine/physical-host name when multiple pods run on the same node (extracted: `rhbk-26-4-caching.md:171-178`) |

These set JGroups `TOPB` (topology) hints that Infinispan uses to scatter replicas across failure domains rather than consolidating them on the same site, rack, or machine.

The correct naming convention converts `spi-cache-embedded--default--{key}` to `KC_SPI_CACHE_EMBEDDED__DEFAULT__{KEY}` — each `--` in the SPI path becomes `__` in the env var, and the key part is uppercased. There is no `CLUSTER_NAME` key in this SPI family.

## References

### RH ground-truth
- `kb:rhbk-26-4-caching` — "Chapter 10. Configuring distributed caches" from the RHBK 26.4 Server Configuration Guide (`rhbk-26-4-caching.md:156-177`)

### Wiki
- [[distributed-caches]] — RHBK Infinispan cache model overview
- [[kc-spi-cache-embedded-default-cluster-name]] (this page)
