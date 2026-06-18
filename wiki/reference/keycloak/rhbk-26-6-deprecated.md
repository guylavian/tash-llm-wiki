---
title: "Chapter 5. Deprecated features - Red Hat build of Keycloak 26.6 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-6-deprecated
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/release_notes/deprecated
guide: release_notes
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "The following sections provide details on deprecated features. 5.1. Fine-Grained Admin Permissions (FGAP) v1 Fine-Grained Admin Permissions (FGAP) v1 is deprecated. This version no longer receives enhancements and improvements and will be removed in a future release. To ensure continued support, migrate to FGAP v2. 5.2. AuthenticationManager.AuthResult is now a record The inner class Authenticatio…"
---

# Chapter 5. Deprecated features - Red Hat build of Keycloak 26.6 Release Notes

Chapter 5. Deprecated features
The following sections provide details on deprecated features.
5.1. Fine-Grained Admin Permissions (FGAP) v1
Fine-Grained Admin Permissions (FGAP) v1 is deprecated. This version no longer receives enhancements and improvements and will be removed in a future release. To ensure continued support, migrate to FGAP v2.
5.2. AuthenticationManager.AuthResult is now a record
The inner class AuthenticationManager.AuthResult
in the keycloak-services
module is now a record. The getter methods like getSession()
have been deprecated in favor of the session()
accessors.
5.3. Methods for removing expired authentication sessions from AuthenticationSessionProvider
The methods removeAllExpired()
and removeExpired(RealmModel realm)
are annotated with the @Deprecated
annotation. They have been deprecated for some time as the built-in implementations now use their own internal cleanup mechanisms. If you are providing a custom implementation of this provider, implement an internal mechanism to delete expired sessions.
5.4. Methods for removing expired user sessions from UserSessionProvider
The methods removeAllExpired()
and removeExpired(RealmModel realm)
are deprecated. A new internal cleanup mechanism has been implemented to automatically remove expired sessions from the database. If you are providing a custom implementation of this provider, implement an internal mechanism to delete expired sessions.
5.5. Cluster scheduled task ClearExpiredUserSessions
As AuthenticationSessionProvider
and UserSessionProvider
now have an internal mechanism to delete expired entries, the scheduled task ClearExpiredUserSessions
has been deprecated. It is still triggered in this Red Hat build of Keycloak version, but will be removed in a future release.
5.6. Specific tracing properties in Keycloak CR
The tracing.serviceName
, and tracing.resourceAttributes
fields of the Keycloak CR, are deprecated. You should use the new telemetry.serviceName
, and telemetry.resourceAttributes
fields that are shared among all OpenTelemetry components - logs, metrics, and traces.
The service name and resource attributes are not directly related to the OpenTelemetry Tracing itself, but to the whole OpenTelemetry settings.
The deprecated options will continue to work, but the new telemetry options take precedence.
Migration path:
tracing-service-name --> telemetry-service-name
tracing-resource-attributes --> telemetry-resource-attributes
5.7. Tracing span attributes for HTTP requests
The OpenTelemetry tracing span attributes code.function
and code.namespace
are deprecated for the HTTP request spans when tracing is enabled. These attributes will be removed in the next major release, and only the fully qualified code.function.name
span attribute will stay.
5.8. Legacy Token Exchange
Legacy token exchange V1 is deprecated. It will be removed in a future version, when its functionality can be totally or partially replaced by the supported version 2 and other features.
5.9. Certain UserSessionProvider methods
The following methods are deprecated for removal: getUserSessionsStream(RealmModel realm, ClientModel client)
, getUserSessionsStream(RealmModel realm, ClientModel client, Integer firstResult, Integer maxResults)
, and getOfflineUserSessionsStream(RealmModel realm, ClientModel client, Integer firstResult, Integer maxResults)
. They are replaced with read-only alternatives to reduce memory consumption. See the UserSessionProvider
API changes section in the Upgrading Guide for further information.
5.10. Non-UTF-8 database character encoding
Running Red Hat build of Keycloak on a database that is not using UTF-8 as a charset is deprecated.
In the current version, Red Hat build of Keycloak will log a warning if the database is not configured to use UTF-8 encoding. Future versions might refuse to work with database that is not configured to use UTF-8 encoding.
5.11. Keycloak and KeycloakRealmImport CRDs v2beta1 version
To better capture the maturity of Operator CRDs for the Keycloak
and KeycloakRealmImport
, the resources now include a v2beta1
version. The previous v2alpha1
version for these resources is deprecated but still served. You can keep using it but we recommend upgrading to v2beta1
at your earliest convenience. There are currently no differences in the schema between the two versions, so you will just need to update the relevant apiVersion
references.
