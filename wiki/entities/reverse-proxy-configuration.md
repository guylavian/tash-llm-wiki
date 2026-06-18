---
title: Reverse proxy configuration
type: entity
domain: keycloak
slug: reverse-proxy-configuration
summary: "Behind a proxy/load balancer, RHBK must be told which forwarding headers to trust via `proxy-headers`; misconfiguration causes 403s or opens spoofing vulnerabilities."
sources:
  - guide:server_configuration_guide
provenance: needs-review
tags: [server-config]
status: draft
updated: 2026-06-16
---

# Reverse proxy configuration

**Behind a proxy/load balancer, RHBK must be told which forwarding headers to trust via `proxy-headers`; misconfiguration causes 403s or opens spoofing vulnerabilities.**

## Ports

- `8443` (or `8080` with `--http-enabled=true`) serves Admin UI, Account Console, SAML/OIDC endpoints, and Admin REST API. **Proxy only this port.**
- `9000` is the [[management-interface]] (health/metrics). **Do not proxy 9000** — keep it internal.

## proxy-headers

`--proxy-headers` accepts:
- *(unset, default)* — no proxy headers parsed; use for no-proxy or **HTTPS passthrough**. With a non-passthrough proxy and no setting, origin-checked requests return **403 Forbidden**.
- `forwarded` — parse RFC 7239 `Forwarded`.
- `xforwarded` — parse `X-Forwarded-For/Proto/Host/Port`. `X-Forwarded-Port` wins over a port in `X-Forwarded-Host`.

Never use `forwarded`/`xforwarded` with HTTPS passthrough. The proxy must set/overwrite these headers, or rogue clients can spoof the client IP. Restrict trust with `--proxy-trusted-addresses=192.168.0.32,127.0.0.0/8` (IPs/CIDRs). For edge TLS termination, also set `--http-enabled true`.

## Other modes

- **PROXY protocol**: `--proxy-protocol-enabled true` for an HA-PROXY-compatible passthrough proxy; cannot be combined with `proxy-headers`.
- **Context path**: RHBK assumes the same path on the proxy. Use a full-URL `--hostname=https://host/auth`, or change RHBK's own path with `http-relative-path`.
- **Client cert lookup**: with a TLS-termination proxy, client cert info is forwarded via headers; configure the lookup per proxy (e.g. NGINX provider rebuilds the chain from the truststore).

## Sticky sessions

Sticky sessions are recommended (not mandatory) so Infinispan session owners are local. RHBK encodes the owner node into the `AUTH_SESSION_ID` cookie (`<session-id>.<node>`); configure the LB to stick on that cookie. If the proxy does affinity without reading backend cookies, set `spi-sticky-session-encoder--infinispan--should-attach-route=false` (default `true`).

## Exposed-path recommendations

Expose: `/realms/`, `/resources/`, `/.well-known/`. Do **not** expose: `/`, `/admin/`, `/metrics`, `/health`. With `http-relative-path` set, map `/.well-known/` (unprefixed) to the prefixed path for RFC 8414 discovery.

## Contradictions / caveats
- Behavior consistent across RHBK 26.0–26.6 (quoted from 26.4). This is part of hostname **v2** thinking — the legacy `proxy` mode option (`edge`/`reencrypt`/`passthrough`) of older versions is replaced by `proxy-headers` + passthrough/PROXY-protocol settings.

## See also
- [[server-configuration]]
- [[hostname-v2]]
- [[tls-configuration]]
- [[management-interface]]
- [[distributed-caches]]
- [[production-checklist]]
