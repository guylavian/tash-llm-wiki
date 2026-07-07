---
title: "Chapter 22. All provider configuration - Red Hat build of Keycloak 26.2 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-all-provider-config
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/all-provider-config-
guide: server_configuration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "Review provider configuration options. 22.1. authentication-sessions 22.1.1. infinispan Value spi-authentication-sessions-infinispan-auth-sessions-limit The maximum number of concurrent authentication sessions per RootAuthenticationSession. CLI: --spi-authentication-sessions-infinispan-auth-sessions-limit Env: KC_SPI_AUTHENTICATION_SESSIONS_INFINISPAN_AUTH_SESSIONS_LIMIT 300 (default) or any int 2…"
---

# Chapter 22. All provider configuration - Red Hat build of Keycloak 26.2 Server Configuration Guide

Chapter 22. All provider configuration
Review provider configuration options.
22.1. authentication-sessions
22.1.1. infinispan
| Value | |
|---|---|
|
|
|
22.1.2. remote
| Value | |
|---|---|
|
|
|
|
|
|
|
|
|
22.2. brute-force-protector
22.2.1. default-brute-force-detector
| Value | |
|---|---|
|
|
|
22.3. ciba-auth-channel
22.3.1. ciba-http-auth-channel
| Value | |
|---|---|
|
|
any |
22.4. connections-http-client
22.4.1. default
| Value | |
|---|---|
|
|
|
|
|
any |
|
|
any |
|
|
any |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
any |
|
|
|
|
|
|
22.4.2. opentelemetry
| Value | |
|---|---|
|
|
|
|
|
any |
|
|
any |
|
|
any |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
any |
|
|
|
|
|
|
22.5. connections-infinispan
22.5.1. quarkus
| Value | |
|---|---|
|
|
any |
22.6. connections-jpa
22.6.1. quarkus
| Value | |
|---|---|
|
|
|
|
|
any |
|
|
|
22.7. credential
22.7.1. keycloak-password
| Value | |
|---|---|
|
|
|
22.8. crl-storage
22.8.1. infinispan
| Value | |
|---|---|
|
|
|
|
|
|
22.9. datastore
22.9.1. legacy
| Value | |
|---|---|
|
|
|
22.10. dblock
22.10.1. jpa
| Value | |
|---|---|
|
|
any |
22.11. events-listener
22.11.1. email
| Value | |
|---|---|
|
|
|
|
|
|
22.11.2. jboss-logging
| Value | |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
22.12. export
22.12.1. dir
| Value | |
|---|---|
|
|
any |
|
|
any |
|
|
|
|
|
|
22.12.2. single-file
| Value | |
|---|---|
|
|
any |
|
|
any |
22.13. group
22.13.1. jpa
| Value | |
|---|---|
|
|
|
|
|
any |
22.14. import
22.14.1. dir
| Value | |
|---|---|
|
|
any |
|
|
any |
|
|
any |
22.14.2. single-file
| Value | |
|---|---|
|
|
any |
|
|
any |
|
|
any |
22.15. load-balancer-check
22.15.1. remote
| Value | |
|---|---|
|
|
|
22.16. login-protocol
22.16.1. openid-connect
| Value | |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
any |
22.17. login-failure
22.17.1. remote
| Value | |
|---|---|
|
|
|
|
|
|
22.18. password-hashing
22.18.1. argon2
| Value | |
|---|---|
|
|
any |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
22.19. public-key-storage
22.19.1. infinispan
| Value | |
|---|---|
|
|
|
|
|
|
22.20. required-action
22.20.1. UPDATE_PASSWORD
| Value | |
|---|---|
|
|
|
22.21. resource-encoding
22.21.1. gzip
| Value | |
|---|---|
|
|
|
22.22. security-profile
22.22.1. default
| Value | |
|---|---|
|
|
any |
22.23. single-use-object
22.23.1. infinispan
| Value | |
|---|---|
|
|
|
22.23.2. remote
| Value | |
|---|---|
|
|
|
22.24. sticky-session-encoder
22.24.1. infinispan
| Value | |
|---|---|
|
|
|
22.24.2. remote
| Value | |
|---|---|
|
|
|
22.25. storage
22.25.1. ldap
| Value | |
|---|---|
|
|
|
22.26. truststore
22.26.1. file
| Value | |
|---|---|
|
|
any |
|
|
|
|
|
any |
|
|
any |
22.27. user-profile
22.27.1. declarative-user-profile
| Value | |
|---|---|
|
|
any |
|
|
any |
|
|
any |
22.28. user-sessions
22.28.1. infinispan
| Value | |
|---|---|
|
|
|
|
|
any |
|
|
any |
|
|
|
22.28.2. remote
| Value | |
|---|---|
|
|
|
|
|
|
|
|
|
22.29. well-known
22.29.1. oauth-authorization-server
| Value | |
|---|---|
|
|
|
|
|
any |
22.29.2. openid-configuration
| Value | |
|---|---|
|
|
|
|
|
any |
