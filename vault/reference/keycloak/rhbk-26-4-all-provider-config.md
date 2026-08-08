---
title: "Chapter 22. All provider configuration - Red Hat build of Keycloak 26.4 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-all-provider-config
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/all-provider-config-
guide: server_configuration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Review provider configuration options. 22.1. authentication-sessions 22.1.1. infinispan Value spi-authentication-sessions--infinispan--auth-sessions-limit The maximum number of concurrent authentication sessions per RootAuthenticationSession. CLI: --spi-authentication-sessions--infinispan--auth-sessions-limit Env: KC_SPI_AUTHENTICATION_SESSIONS__INFINISPAN__AUTH_SESSIONS_LIMIT 300 (default) or any…"
---

# Chapter 22. All provider configuration - Red Hat build of Keycloak 26.4 Server Configuration Guide

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
22.3. cache-embedded
22.3.1. default
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
any |
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
any |
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
any |
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
any |
|
|
any |
22.4. cache-remote
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
any |
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
|
|
any |
|
|
any |
22.5. ciba-auth-channel
22.5.1. ciba-http-auth-channel
| Value | |
|---|---|
|
|
any |
22.6. connections-http-client
22.6.1. default
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
22.6.2. opentelemetry
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
22.7. connections-jpa
22.7.1. quarkus
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
22.8. credential
22.8.1. keycloak-password
| Value | |
|---|---|
|
|
|
22.9. crl-storage
22.9.1. infinispan
| Value | |
|---|---|
|
|
|
|
|
|
22.10. datastore
22.10.1. legacy
| Value | |
|---|---|
|
|
|
22.11. dblock
22.11.1. jpa
| Value | |
|---|---|
|
|
any |
22.12. device-representation
22.12.1. device-representation
| Value | |
|---|---|
|
|
|
22.13. events-listener
22.13.1. email
| Value | |
|---|---|
|
|
|
|
|
|
22.13.2. jboss-logging
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
22.14. export
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
|
|
|
|
22.14.2. single-file
| Value | |
|---|---|
|
|
any |
|
|
any |
22.15. group
22.15.1. jpa
| Value | |
|---|---|
|
|
|
|
|
any |
22.16. import
22.16.1. dir
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
22.16.2. single-file
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
22.17. jgroups-mtls
22.17.1. default
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
|
|
any |
|
|
any |
22.18. load-balancer-check
22.18.1. remote
| Value | |
|---|---|
|
|
|
22.19. login-protocol
22.19.1. openid-connect
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
22.19.2. saml
| Value | |
|---|---|
|
|
|
22.20. login-failure
22.20.1. remote
| Value | |
|---|---|
|
|
|
|
|
|
22.21. mapped-diagnostic-context
22.21.1. default
| Value | |
|---|---|
|
|
|
22.22. password-hashing
22.22.1. argon2
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
22.23. public-key-storage
22.23.1. infinispan
| Value | |
|---|---|
|
|
|
|
|
|
22.24. required-action
22.24.1. CONFIGURE_RECOVERY_AUTHN_CODES
| Value | |
|---|---|
|
|
|
|
|
|
22.24.2. CONFIGURE_TOTP
| Value | |
|---|---|
|
|
|
|
|
|
22.24.3. TERMS_AND_CONDITIONS
| Value | |
|---|---|
|
|
|
22.24.4. UPDATE_EMAIL
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
22.24.5. UPDATE_PASSWORD
| Value | |
|---|---|
|
|
|
22.24.6. UPDATE_PROFILE
| Value | |
|---|---|
|
|
|
22.24.7. VERIFY_EMAIL
| Value | |
|---|---|
|
|
|
|
|
|
22.24.8. VERIFY_PROFILE
| Value | |
|---|---|
|
|
|
22.24.9. delete_credential
| Value | |
|---|---|
|
|
|
22.24.10. idp_link
| Value | |
|---|---|
|
|
|
22.24.11. update_user_locale
| Value | |
|---|---|
|
|
|
22.24.12. webauthn-register
| Value | |
|---|---|
|
|
|
22.24.13. webauthn-register-passwordless
| Value | |
|---|---|
|
|
|
22.25. resource-encoding
22.25.1. gzip
| Value | |
|---|---|
|
|
|
22.26. security-profile
22.26.1. default
| Value | |
|---|---|
|
|
any |
22.27. single-use-object
22.27.1. infinispan
| Value | |
|---|---|
|
|
|
22.27.2. remote
| Value | |
|---|---|
|
|
|
22.28. sticky-session-encoder
22.28.1. infinispan
| Value | |
|---|---|
|
|
|
22.28.2. remote
| Value | |
|---|---|
|
|
|
22.29. storage
22.29.1. ldap
| Value | |
|---|---|
|
|
|
22.30. truststore
22.30.1. file
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
22.31. user-profile
22.31.1. declarative-user-profile
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
22.32. user-sessions
22.32.1. infinispan
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
|
|
|
22.32.2. remote
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
22.33. well-known
22.33.1. oauth-authorization-server
| Value | |
|---|---|
|
|
|
|
|
any |
22.33.2. openid-configuration
| Value | |
|---|---|
|
|
|
|
|
any |
