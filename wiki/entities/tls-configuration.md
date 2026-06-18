---
title: TLS / HTTPS configuration
type: entity
domain: keycloak
slug: tls-configuration
summary: "RHBK serves HTTPS on port 8443 using either PEM cert/key files or a Java keystore; production must never expose plain HTTP endpoints."
sources:
  - guide:server_configuration_guide
provenance: needs-review
tags: [server-config]
status: draft
updated: 2026-06-16
---

# TLS / HTTPS configuration

**RHBK serves HTTPS on port 8443 using either PEM cert/key files or a Java keystore; production must never expose plain HTTP endpoints.**

## Providing certificates

- **PEM**: `--https-certificate-file=/path/cert.pem --https-certificate-key-file=/path/key.pem`. RHBK builds an in-memory keystore from them.
- **Keystore**: `--https-key-store-file=/path/keystore`. If no keystore is configured and `http-enabled=false`, RHBK looks for `conf/server.keystore`. Recognized extensions: `.p12`/`.pkcs12`/`.pfx` (PKCS12), `.jks`/`.keystore` (JKS), `.key`/`.crt`/`.pem` (PEM). Set `https-key-store-type` if the extension doesn't match.
- When both PEM and keystore are configured, **PEM takes precedence**.

## Password and other options

- `--https-key-store-password=<value>` — defaults to `password` if unset. Avoid plaintext: use a vault/mounted secret (see [[keycloak-vault]]).
- `--https-protocols=TLSv1.3[,...]` — deprecated protocols are off by default.
- `--https-port=<port>` — default `8443`.
- `https-certificates-reload-period` — certs/keys/keystores under `https-*` reload **every hour** by default without restart; accepts a `java.time.Duration`, seconds, or `<n>[ms|s|m|h|d]` (must be > 30s); `-1` disables.

## Edge / termination

For an edge TLS-termination proxy, enable HTTP on the backend (`--http-enabled true`) and set the public scheme via [[hostname-v2]] (`--hostname https://...`). The [[management-interface]] inherits TLS from the main server by default but can be forced to HTTP with `http-management-scheme=http`, or tuned separately via `https-management-*`.

## Contradictions / caveats
- PEM-over-keystore precedence and the hourly reload are consistent across RHBK 26.0–26.6 (quoted from 26.4).
- mTLS / X.509 client authentication is a separate concern (trusted-certs / mutual-tls chapter), not the server-side HTTPS listener covered here.

## See also
- [[server-configuration]]
- [[hostname-v2]]
- [[reverse-proxy-configuration]]
- [[management-interface]]
- [[keycloak-vault]]
- [[production-checklist]]
