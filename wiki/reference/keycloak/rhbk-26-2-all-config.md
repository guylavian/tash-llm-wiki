---
title: "Chapter 21. All configuration - Red Hat build of Keycloak 26.2 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-all-config
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/all-config-
guide: server_configuration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 21. All configuration - Red Hat build of Keycloak 26.2 Server Configuration Guide

Chapter 21. All configuration
Review build options and configuration for Red Hat build of Keycloak.
21.1. Cache
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
CLI: | |
|
CLI: Available only when a TCP based cache-stack is used |
|
|
CLI: Available only when property 'cache-embedded-mtls-enabled' is enabled | |
|
CLI: Available only when property 'cache-embedded-mtls-enabled' is enabled | |
|
CLI: Available only when property 'cache-embedded-mtls-enabled' is enabled | (default) |
|
CLI: Available only when property 'cache-embedded-mtls-enabled' is enabled | |
|
CLI: Available only when property 'cache-embedded-mtls-enabled' is enabled | |
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
CLI: Available only when 'cache' type is set to 'ispn'
Use 'jdbc-ping' instead by leaving it unset Deprecated values: |
|
21.2. Config
| Value | |
|---|---|
|
CLI: | |
|
CLI: | |
|
CLI: | (default) |
21.3. Database
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
21.4. Transaction
| Value | |
|---|---|
| 🛠
CLI: |
|
21.5. Feature
| Value | |
|---|---|
| 🛠
CLI: |
|
| 🛠
CLI: |
|
21.6. Hostname v2
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
21.7. HTTP(S)
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
CLI: |
|
|
CLI: | |
|
CLI: | |
|
CLI: |
21.8. Health
| Value | |
|---|---|
| 🛠
CLI: |
|
21.9. Management
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
|
CLI: | (default) |
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
21.10. Metrics
| Value | |
|---|---|
| 🛠
CLI: |
|
21.11. Proxy
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
21.12. Vault
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
21.13. Logging
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
CLI: Available only when Console log handler is activated and output is set to 'json' |
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
CLI: Available only when File log handler is activated and output is set to 'json' |
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
CLI: Available only when Syslog is activated and output is set to 'json' |
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
21.14. Tracing
| Value | |
|---|---|
|
CLI: Available only when Tracing is enabled |
|
| 🛠
CLI: Available only when 'opentelemetry' feature is enabled |
|
|
CLI: Available only when Tracing is enabled | (default) |
| 🛠
CLI: Available only when Tracing is enabled |
|
|
CLI: Available only when Tracing is enabled |
|
|
CLI: Available only when Tracing is enabled | |
|
CLI: Available only when Tracing is enabled | (default) |
| 🛠
CLI: Available only when Tracing is enabled |
|
|
CLI: Available only when Tracing is enabled | (default) |
21.15. Events
| Value | |
|---|---|
| 🛠
CLI: Available only when metrics are enabled and feature user-event-metrics is enabled |
|
|
CLI: Available only when user event metrics are enabled
Use |
|
|
CLI: Available only when user event metrics are enabled |
|
21.16. Truststore
| Value | |
|---|---|
|
CLI:
STRICT and WILDCARD have been deprecated, use DEFAULT instead. Deprecated values: |
|
|
CLI: |
21.17. Security
| Value | |
|---|---|
| 🛠
CLI: |
|
21.18. Export
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
21.19. Import
| Value | |
|---|---|
|
CLI: | |
|
CLI: | |
|
CLI: |
|
21.20. Bootstrap Admin
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
