---
title: "Chapter 3. Technology preview features - Red Hat build of Keycloak 26.6 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-6-techpreview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/release_notes/techpreview
guide: release_notes
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 3. Technology preview features - Red Hat build of Keycloak 26.6 Release Notes

Chapter 3. Technology preview features
The following new features are in a Technology Preview status:
3.1. Enhanced HTTP performance
You can now enable a more efficient way to handle JSON data in the HTTP layer. This change increases throughput by approximately five percent, stabilizes response times, and reduces system resource usage.
In order to apply it, you need to explicitly enable the feature http-optimized-serializers
.
For more details, see Configuring Red Hat build of Keycloak for production.
3.2. OpenTelemetry Logs
Red Hat build of Keycloak now supports exporting logs to OpenTelemetry collectors, enabling centralized log management. This preview feature allows you to export Red Hat build of Keycloak logs to any OpenTelemetry-compatible backend and use the same OpenTelemetry collector for logs, metrics and traces.
For more details, see OpenTelemetry.
3.3. Identity Brokering APIs V2
A new preview version 2 for the Identity Brokering APIs is introduced in this release.
When brokering is used during the authentication process, Red Hat build of Keycloak allows you to store tokens and responses issued by the external Identity Provider. Applications call a specific endpoint to retrieve those tokens, which can be used to get extra user information or invoke endpoints in the external trust domain.
The new version improves the token retrieval endpoint to substitute the internal to external Token Exchange (use case for the legacy Token Exchange V1).
For more details, see Identity Brokering APIs.
3.4. Step-up authentication for SAML
The feature step-up-authentication-saml
extends the step-up authentication to include the SAML protocol and clients. For more details, see Step-up authentication for SAML.
