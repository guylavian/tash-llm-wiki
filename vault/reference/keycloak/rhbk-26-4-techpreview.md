---
title: "Chapter 13. Technology preview features - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-techpreview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/techpreview
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "The following new features are in a Technology Preview status: 13.1. Federated client authentication and SPIFFE trust relationship provider Identity providers are now able to federate client authentication. This allows clients to authenticate with SPIFFE JWT SVIDs, Kubernetes service accounts, or tokens issued by a OpenID Connect identity provider. 13.2. Rolling updates for patch releases for mini…"
---

# Chapter 13. Technology preview features - Red Hat build of Keycloak 26.4 Release Notes

Chapter 13. Technology preview features
The following new features are in a Technology Preview status:
13.1. Federated client authentication and SPIFFE trust relationship provider
Identity providers are now able to federate client authentication. This allows clients to authenticate with SPIFFE JWT SVIDs, Kubernetes service accounts, or tokens issued by a OpenID Connect identity provider.
13.2. Rolling updates for patch releases for minimized downtime
In the previous release, the Keycloak Operator was enhanced to support performing rolling updates of the Keycloak image if both images contain the same version. This is useful, for example, when switching to an optimized image, changing a theme or a provider source code.
In this release, we extended this capability to perform a rolling update when the new image contains a future patch release from the same major.minor
release stream as a preview feature. This can reduce the service’s downtime even further, as downtime is only needed when upgrading from a different minor or major version.
For more details, see Rolling updates.
13.3. Showing context information in log messages
You can now add context information via the mapped diagnostic context (MDC) to each log message like the realm or the client that initiated the request. This helps you to track down a warning or error message in the log to a specific caller or environment
For more details on this feature, see Adding context for log messages.
13.4. Existing technology preview features
Also, the following existing features remain in a technology preview status:
- Client Secret Rotation
- JavaScript support to write custom authenticators
