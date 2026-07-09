---
title: What does KC_HOSTNAME_STRICT_BACKCHANNEL do?
type: question
question_tier: conceptual
domain: keycloak
slug: kc-hostname-strict-backchannel
summary: The Hostname v1 option that forced backchannel URLs to use the fixed frontend hostname; removed in v2 and replaced by `hostname-backchannel-dynamic`.
sources:
  - guide:upgrading_guide
provenance:
  extracted: 3
  inferred: 0
  ambiguous: 0
tags: [server-config]
status: draft
updated: 2026-07-07
---

# What does KC_HOSTNAME_STRICT_BACKCHANNEL do?

`KC_HOSTNAME_STRICT_BACKCHANNEL` (CLI: `--hostname-strict-backchannel`) is a **Hostname v1** option. When set to `true`, it forced the backchannel (server-to-server/API) URLs to use the same fixed hostname as the frontend, rather than resolving them dynamically from incoming request headers.

In Hostname v1, the default behavior was to dynamically resolve backchannel URLs from request headers. Setting `hostname-strict-backchannel=true` opted *out* of that dynamic resolution.

## Hostname v2 replacement

In RHBK 26.x (Hostname v2), this option was **removed**. The equivalent behavior (backchannel == frontchannel) is now the **default**: `--hostname-backchannel-dynamic` defaults to `false`. To get the old v1 default (dynamic backchannel), you now explicitly set `--hostname-backchannel-dynamic true` — the polarity is inverted.

| v1 (removed) | v2 equivalent |
|---|---|
| `--hostname-strict-backchannel=true` | default (no option needed) or `--hostname-backchannel-dynamic=false` |
| `--hostname-strict-backchannel=false` (default) | `--hostname-backchannel-dynamic=true` |

## Migration example

```bash
# Hostname v1
kc.sh start --hostname=mykeycloak.org --hostname-strict-backchannel=true

# Hostname v2 (same behavior — backchannel == frontchannel)
kc.sh start --hostname=https://mykeycloak.org --hostname-backchannel-dynamic=false
```

## References

### RH ground-truth
- `guide:upgrading_guide` (26.0) — hostname v1→v2 migration table and backchannel setting example

### Wiki
- [[hostname-v2]] — current Hostname v2 configuration model
