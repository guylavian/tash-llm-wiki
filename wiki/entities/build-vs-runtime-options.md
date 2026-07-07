---
title: Build options vs runtime options (optimized image)
type: entity
domain: keycloak
slug: build-vs-runtime-options
summary: "Build options are persisted into an optimized RHBK image by `kc.sh build`; runtime (configuration) options are applied at `kc.sh start`."
sources:
  - guide:server_configuration_guide
provenance_extracted: 6
provenance_inferred: 1
provenance_ambiguous: 0
tags: [server-config]
status: draft
updated: 2026-07-02
---

# Build options vs runtime options

**Build options are persisted into an optimized RHBK image by `kc.sh build`; runtime (configuration) options are applied at `kc.sh start`.**

## The two classes

- **Build options** — marked with a 🛠 (tool icon) in *All configuration*. Applied with `bin/kc.sh build <build-options>` and baked into the server image via Quarkus re-augmentation. Examples: `db`, `features` / `features-disabled`, `health-enabled`, `metrics-enabled`, `vault`, `hostname:v2` feature gating. List them with `kc.sh build --help`.
- **Configuration / runtime options** — everything *not* marked with the tool icon. Applied at `kc.sh start`. Examples: `db-url-host`, `db-username`, `db-password`, `hostname`, `https-certificate-file`, `proxy-headers`.

Build options are stored in **plain text** inside the image. **Never** store sensitive data (passwords, secrets) as build options, and do not put build options in a Java KeyStore. Use the KeyStore config source for sensitive *runtime* options instead.

## Optimized startup flow (recommended)

```
bin/kc.sh build --db=postgres          # persist build options
bin/kc.sh start --optimized            # skip the implicit build at startup
```

`--optimized` tells RHBK to assume a pre-built image, so it does not check for or run a build at startup (faster start). Behavior when a build option also appears at `start`:
- same value as the built one → silently ignored.
- different value → a warning is logged and the **previously built value is used**; you must re-run `build` for the new value to take effect.

Without `--optimized`, `kc.sh start --db postgres ...` runs an implicit build first (slower, but no separate step).

## Why it matters

`build` performs a closed-world provider scan, pre-parses config files, and prepares DB-specific resources, so the server skips that work at each startup. For container/Operator images this is why a `RUN kc.sh build` line is added to the Containerfile (with `ENV KC_DB`, `ENV KC_HEALTH_ENABLED`, etc.).

## Contradictions / caveats
- The 🛠 build-time vs runtime split is stable across RHBK 26.0–26.6 (quoted from 26.4); the exact *set* of build options can grow between releases (inferred — only the 26.4 note was checked directly).
- Operator-managed custom images **must** be optimized (all build-time options set + `kc.sh build`). See [[rhbk-operator]].
- Changing certain build options (e.g. some features) requires a recreate rather than a rolling update — see the rolling-update compatibility chapter.

## See also
- [[server-configuration]]
- [[config-sources-precedence]]
- [[feature-flags]]
- [[database-configuration]]
- [[rhbk-operator]]
