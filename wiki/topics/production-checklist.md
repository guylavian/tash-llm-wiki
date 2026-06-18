---
title: RHBK production configuration checklist
type: topic
domain: keycloak
slug: production-checklist
summary: "Going to production with `kc.sh start` means satisfying RHBK's secure-by-default requirements: TLS, an explicit hostname, a real database, a proxy/cluster topology, and observability kept internal."
sources:
  - guide:server_configuration_guide
provenance: needs-review
tags: [concept]
status: draft
updated: 2026-06-16
---

# RHBK production configuration checklist

**Going to production with `kc.sh start` means satisfying RHBK's secure-by-default requirements: TLS, an explicit hostname, a real database, a proxy/cluster topology, and observability kept internal.**

`kc.sh start` (production mode) is secure-by-default: HTTP is disabled, a hostname is expected, and HTTPS/TLS is expected — without these it refuses to start. The general production areas:

1. **TLS** — enable HTTPS; never expose plain HTTP endpoints. Provide PEM or keystore certs and avoid plaintext keystore passwords. See [[tls-configuration]].
2. **Hostname** — set an explicit `hostname` (or `hostname-strict false`) so URLs aren't derived from request headers. Best practice: expose the Admin REST API/Console on a separate hostname/context-path and block admin paths at the proxy. See [[hostname-v2]].
3. **Reverse proxy** — set `proxy-headers` correctly (`forwarded`/`xforwarded`), restrict with `proxy-trusted-addresses`, proxy only `8443`/`8080` (never `9000`), and expose only the recommended paths. See [[reverse-proxy-configuration]].
4. **Load shedding** — set `http-max-queued-requests` (no limit by default; over-threshold requests get `503`). Implement load shedding at the LB too.
5. **Production database** — replace the dev-only `dev-file` DB with a supported vendor. See [[database-configuration]].
6. **Cluster** — run 2+ nodes on JGroups/Infinispan (TLS-encrypted node comms by default); open the required firewall ports. See [[distributed-caches]] and [[ha-cross-site]].
7. **IPv4/IPv6** — select the stack via `JAVA_OPTS_APPEND` (`-Djava.net.preferIPv4Stack=true`, or the IPv6 pair) so cluster discovery binds correctly.
8. **Observability** — enable health (`health-enabled`) and metrics (`metrics-enabled`) and keep them on the internal [[management-interface]] (port 9000), not the public port.
9. **Secrets** — keep passwords out of plaintext config: use the KeyStore config source for sensitive runtime options ([[config-sources-precedence]]) and/or a [[keycloak-vault]].
10. **Optimized image** — pre-bake build options (`db`, `features`, `health-enabled`, `metrics-enabled`, `vault`) with `kc.sh build`, then run `kc.sh start --optimized`. See [[build-vs-runtime-options]].
11. **First admin** — bootstrap a temporary admin (`KC_BOOTSTRAP_ADMIN_USERNAME`/`PASSWORD` or `kc.sh bootstrap-admin`) and replace it with a real account. See [[kc-bootstrap-admin]].

## Contradictions / caveats
- Steps are framed from the RHBK **26.4** *Configuring for production* chapter and apply equally to containerized, on-premise, GitOps, and Ansible deployments; option names hold across 26.0–26.6 but feature availability varies — see [[feature-flags]].
- On OpenShift, the [[rhbk-operator]] enforces much of this (optimized images, hostname, TLS secrets) declaratively via the Keycloak CR.
- `multi-site:v1` is a supported-but-default-off feature; cross-site HA has its own prerequisites — see [[ha-cross-site]].

## See also
- [[server-configuration]]
- [[tls-configuration]]
- [[hostname-v2]]
- [[reverse-proxy-configuration]]
- [[database-configuration]]
- [[management-interface]]
- [[feature-flags]]
- [[keycloak-vault]]
- [[build-vs-runtime-options]]
- [[distributed-caches]]
- [[ha-cross-site]]
- [[kc-bootstrap-admin]]
- [[rhbk-operator]]
