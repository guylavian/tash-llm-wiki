---
title: "Chapter 17. Deprecated features - Red Hat build of Keycloak 26.2 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-2-deprecated-features
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/release_notes/deprecated_features
guide: release_notes
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 17. Deprecated features - Red Hat build of Keycloak 26.2 Release Notes

Chapter 18. Deprecated features
In previous sections, some features have already been mentioned as deprecated. The following sections provide details on other deprecated features.
18.1. Disabling filtering of LDAP referrals
The option spi-storage—ldap—secure-referral
to disable filtering referrals is deprecated. When this feature is removed in a future release, filtering will then be enforced.
18.2. Default db option for production
In previous releases, the db
option defaulted to dev-file
both in production (start
) and development (start-dev
) modes while dev-file
has never been supported in the production mode. In this release, we have deprecated this behavior and in some future release the db
option will not default to dev-file
in production mode. For build
or non-optimized start
and non-server commands import
, export
, or bootstrap-admin
in the production profile, a value should be explicitly supplied.
This change is to prevent the unintentional usage of the dev-file
(H2) database in a production environment, which is typically indicative of a misconfiguration.
18.3. APIs for JavaScript Authorization client
The following APIs for the JavaScript Authorization client are deprecated and will be removed in the next major release:
-
The
ready
property on theKeycloakAuthorization
instance. -
The
init()
method on theKeycloakAuthorization
instance.
These APIs are no longer needed as initialization is done automatically on demand when calling methods on the KeycloakAuthorization
instance. You can safely remove any code that depends on these APIs.
18.4. Endpoint for initiate registration from OIDC client
The /realms/<realm>/protocol/openid-connect/registrations
endpoint, which was used for initiating registration by OIDC client, is now deprecated because a standard way exists to initiate registration from the OIDC client. This way is now supported by Red Hat build of Keycloak. It uses the parameter prompt=create
.
18.5. getAll() methods in Organizations and OrganizationMembers APIs
getAll()
methods in Organizations
and OrganizationMembers
APIs are now deprecated and will be removed in the next major release. Instead, use corresponding list(first, max)
methods in Organizations
and OrganizationMembers
APIs.
18.6. Transport stacks for distributed caches
The udp
, jdbc-ping-udp
, tcp
, azure
, ec2
and google
transport stacks have been deprecated. Users should use the TCP based jdbc-ping
stack as a direct replacement.
