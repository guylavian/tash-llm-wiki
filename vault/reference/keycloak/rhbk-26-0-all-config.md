---
title: "Chapter 24. All configuration - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-all-config
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/all-config-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "24.1. Cache Value cache Defines the cache mechanism for high-availability. By default in production mode, a ispn cache is used to create a cluster between multiple server nodes. By default in development mode, a local cache disables clustering and is intended for development and testing purposes. CLI: --cache Env: KC_CACHE ispn (default), local cache-config-file Defines the file from which cache c…"
---

# Chapter 24. All configuration - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 24. All configuration
24.1. Cache
| Value | |
|---|---|
|
CLI: |
|
|
CLI: | |
|
CLI: | |
|
CLI: Available only when embedded Infinispan clusters configured | |
|
CLI: | |
|
CLI: |
|
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: Available only when embedded Infinispan clusters configured | |
|
CLI: Available only when embedded Infinispan clusters configured | |
|
CLI: | |
|
CLI: Available only when embedded Infinispan clusters configured | |
|
CLI: | |
|
CLI: Available only when metrics are enabled |
|
|
CLI: | |
|
CLI: Available only when remote host is set | |
|
CLI: Available only when remote host is set | (default) |
|
CLI: Available only when remote host is set |
|
|
CLI: Available only when remote host is set | |
|
CLI: |
|
24.2. Config
| Value | |
|---|---|
|
CLI: | |
|
CLI: | |
|
CLI: | (default) |
24.3. Database
| Value | |
|---|---|
| 🛠
CLI: |
|
| 🛠
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: | (default) |
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: |
24.4. Transaction
| Value | |
|---|---|
| 🛠
CLI: |
|
24.5. Feature
| Value | |
|---|---|
| 🛠
CLI: |
|
| 🛠
CLI: |
|
24.6. Hostname v2
| Value | |
|---|---|
|
CLI: Available only when hostname:v2 feature is enabled | |
|
CLI: Available only when hostname:v2 feature is enabled | |
|
CLI: Available only when hostname:v2 feature is enabled |
|
|
CLI: Available only when hostname:v2 feature is enabled |
|
|
CLI: Available only when hostname:v2 feature is enabled |
|
24.7. HTTP(S)
| Value | |
|---|---|
|
CLI: |
|
|
CLI: | (default) |
|
CLI: | |
|
CLI: Available only when metrics are enabled |
|
|
CLI: Available only when metrics are enabled | |
|
CLI: | |
|
CLI: | (default) |
| 🛠
CLI: | (default) |
|
CLI: | |
|
CLI: | |
|
CLI: | (default) |
|
CLI: | |
| 🛠
CLI: |
|
|
CLI: | |
|
CLI: | (default) |
|
CLI: | |
|
CLI: | (default) |
|
CLI: | (default) |
|
CLI: | |
|
CLI: | |
|
CLI: |
24.8. Health
| Value | |
|---|---|
| 🛠
CLI: |
|
24.9. Management
| Value | |
|---|---|
|
CLI: | (default) |
| 🛠
CLI: | (default) |
|
CLI: | |
|
CLI: | |
| 🛠
CLI: |
|
|
CLI: | |
|
CLI: | (default) |
| 🛠
CLI: DEPRECATED. |
|
24.10. Metrics
| Value | |
|---|---|
| 🛠
CLI: |
|
24.11. Proxy
| Value | |
|---|---|
|
CLI: |
|
|
CLI: |
|
|
CLI: |
24.12. Vault
| Value | |
|---|---|
| 🛠
CLI: |
|
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: | (default) |
24.13. Logging
| Value | |
|---|---|
|
CLI: |
|
|
CLI: Available only when Console log handler is activated |
|
|
CLI: Available only when Console log handler is activated | (default) |
|
CLI: Available only when Console log handler and Tracing is activated |
|
|
CLI: Available only when Console log handler is activated |
|
|
CLI: Available only when Console log handler is activated |
|
|
CLI: Available only when File log handler is activated | (default) |
|
CLI: Available only when File log handler is activated | (default) |
|
CLI: Available only when File log handler and Tracing is activated |
|
|
CLI: Available only when File log handler is activated |
|
|
CLI: Available only when File log handler is activated |
|
|
CLI: | (default) |
|
CLI: Available only when Syslog is activated | (default) |
|
CLI: Available only when Syslog is activated | (default) |
|
CLI: Available only when Syslog is activated | (default) |
|
CLI: Available only when Syslog handler and Tracing is activated |
|
|
CLI: Available only when Syslog is activated |
|
|
CLI: Available only when Syslog is activated | |
|
CLI: Available only when Syslog is activated |
|
|
CLI: Available only when Syslog is activated |
|
|
CLI: Available only when Syslog is activated |
|
24.14. Tracing (Preview)
| Value | |
|---|---|
|
CLI: Available only when 'opentelemetry' feature and Tracing is enabled |
|
| 🛠
CLI: Available only when 'opentelemetry' feature is enabled |
|
|
CLI: Available only when 'opentelemetry' feature and Tracing is enabled | (default) |
| 🛠
CLI: Available only when 'opentelemetry' feature and Tracing is enabled |
|
|
CLI: Available only when 'opentelemetry' feature and Tracing is enabled |
|
|
CLI: Available only when 'opentelemetry' feature and Tracing is enabled | |
|
CLI: Available only when 'opentelemetry' feature and Tracing is enabled | (default) |
| 🛠
CLI: Available only when 'opentelemetry' feature and Tracing is enabled |
|
|
CLI: Available only when 'opentelemetry' feature and Tracing is enabled | (default) |
24.15. Truststore
| Value | |
|---|---|
|
CLI:
STRICT and WILDCARD have been deprecated, use DEFAULT instead. Deprecated values: |
|
|
CLI: |
24.16. Security
| Value | |
|---|---|
| 🛠
CLI: |
|
24.17. Export
| Value | |
|---|---|
|
CLI: | |
|
CLI: | |
|
CLI: | |
|
CLI: |
|
|
CLI: | (default) |
24.18. Import
| Value | |
|---|---|
|
CLI: | |
|
CLI: | |
|
CLI: |
|
24.19. Bootstrap Admin
| Value | |
|---|---|
|
CLI: | (default) |
|
CLI: | |
|
CLI: | |
|
CLI: | (default) |
