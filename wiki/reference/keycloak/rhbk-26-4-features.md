---
title: "Chapter 14. Enabling and disabling features - Red Hat build of Keycloak 26.4 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-features
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/features-
guide: server_configuration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 14. Enabling and disabling features - Red Hat build of Keycloak 26.4 Server Configuration Guide

Chapter 14. Enabling and disabling features
Configure Red Hat build of Keycloak to use optional features.
Red Hat build of Keycloak has packed some functionality in features, including some disabled features, such as Technology Preview and deprecated features. Other features are enabled by default, but you can disable them if they do not apply to your use of Red Hat build of Keycloak.
14.1. Enabling features
Some supported features, and all preview features, are disabled by default. To enable a feature, enter this command:
bin/kc.[sh|bat] build --features="<name>[,<name>]"
For example, to enable docker
and token-exchange
, enter this command:
bin/kc.[sh|bat] build --features="docker,token-exchange"
To enable all preview features, enter this command:
bin/kc.[sh|bat] build --features="preview"
Enabled feature may be versioned, or unversioned. If you use a versioned feature name, e.g. feature:v1, that exact feature version will be enabled as long as it still exists in the runtime. If you instead use an unversioned name, e.g. just feature, the selection of the particular supported feature version may change from release to release according to the following precedence:
- The highest default supported version
- The highest non-default supported version
- The highest deprecated version
- The highest preview version
- The highest experimental version
14.2. Disabling features
To disable a feature that is enabled by default, enter this command:
bin/kc.[sh|bat] build --features-disabled="<name>[,<name>]"
For example to disable impersonation
, enter this command:
bin/kc.[sh|bat] build --features-disabled="impersonation"
It is not allowed to have a feature in both the features-disabled
list and the features
list.
When a feature is disabled all versions of that feature are disabled.
14.3. Supported features
The following list contains supported features that are enabled by default, and can be disabled if not needed.
| Feature | Description |
|---|---|
| account-api:v1 | Account Management REST API |
| account:v3 | Account Console version 3 |
| admin-api:v1 | Admin API |
| admin-fine-grained-authz:v2 | Fine-Grained Admin Permissions version 2 |
| admin:v2 | New Admin Console |
| authorization:v1 | Authorization Service |
| ciba:v1 | OpenID Connect Client Initiated Backchannel Authentication (CIBA) |
| client-policies:v1 | Client configuration policies |
| device-flow:v1 | OAuth 2.0 Device Authorization Grant |
| dpop:v1 | OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer |
| hostname:v2 | Hostname Options V2 |
| impersonation:v1 | Ability for admins to impersonate users |
| kerberos:v1 | Kerberos |
| login:v2 | New Login Theme |
| opentelemetry:v1 | OpenTelemetry Tracing |
| organization:v1 | Organization support within realms |
| par:v1 | OAuth 2.0 Pushed Authorization Requests (PAR) |
| passkeys:v1 | Passkeys |
| persistent-user-sessions:v1 | Persistent online user sessions across restarts and upgrades |
| recovery-codes:v1 | Recovery codes |
| rolling-updates:v1 | Rolling Updates |
| step-up-authentication:v1 | Step-up Authentication |
| token-exchange-standard:v2 | Standard Token Exchange version 2 |
| update-email:v1 | Update Email Action |
| user-event-metrics:v1 | Collect metrics based on user events |
| web-authn:v1 | W3C Web Authentication (WebAuthn) |
14.3.1. Disabled by default
The following list contains supported features that are disabled by default, and can be enabled if needed.
| Feature | Description |
|---|---|
| docker:v1 | Docker Registry protocol |
| fips:v1 | FIPS 140-2 mode |
| multi-site:v1 | Multi-site support |
14.4. Preview features
Preview features are disabled by default and are not recommended for use in production. These features may change or be removed at a future release.
| Feature | Description |
|---|---|
| admin-fine-grained-authz:v1 | Fine-Grained Admin Permissions |
| client-auth-federated:v1 | Authenticates client based on assertions issued by identity provider |
| client-secret-rotation:v1 | Client Secret Rotation |
| log-mdc:v1 | Mapped Diagnostic Context (MDC) information in logs |
| rolling-updates:v2 | Rolling Updates for patch releases |
| scripts:v1 | Write custom authenticators using JavaScript |
| spiffe:v1 | SPIFFE trust relationship provider |
| token-exchange:v1 | Token Exchange Service |
14.5. Deprecated features
The following list contains deprecated features that will be removed in a future release. These features are disabled by default.
| Feature | Description |
|---|---|
| instagram-broker:v1 | Instagram Identity Broker |
| login:v1 | Legacy Login Theme |
| logout-all-sessions:v1 | Logout all sessions logs out only regular sessions |
| passkeys-conditional-ui-authenticator:v1 | Passkeys conditional UI authenticator |
14.6. Relevant options
| Value | |
|---|---|
| 🛠
|
|
| 🛠
|
|
