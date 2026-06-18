---
title: "Chapter 16. Upgrading the Red Hat build of Keycloak Client Libraries - Red Hat build of Keycloak 26.2 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-upgrading-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/securing_applications_and_services_guide/upgrading-
guide: securing_applications_and_services_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "How to upgrade the Red Hat build of Keycloak Client Libraries. The client libraries are those artifacts: Java admin client - Maven artifact org.keycloak:keycloak-admin-client Java authorization client - Maven artifact org.keycloak:keycloak-authz-client Java policy enforcer - Maven artifact org.keycloak:keycloak-policy-enforcer Java common classes used by other client libraries above - Maven artifa…"
---

# Chapter 16. Upgrading the Red Hat build of Keycloak Client Libraries - Red Hat build of Keycloak 26.2 Securing Applications and Services Guide

Chapter 16. Upgrading the Red Hat build of Keycloak Client Libraries
How to upgrade the Red Hat build of Keycloak Client Libraries.
The client libraries are those artifacts:
-
Java admin client - Maven artifact
org.keycloak:keycloak-admin-client
-
Java authorization client - Maven artifact
org.keycloak:keycloak-authz-client
-
Java policy enforcer - Maven artifact
org.keycloak:keycloak-policy-enforcer
-
Java common classes used by other client libraries above - Maven artifact
org.keycloak:keycloak-client-common-synced
The last released client libraries are supported with all the supported Red Hat build of Keycloak server versions. The fact that client libraries are supported with more server versions makes the update easier, so you may not need to update the server at the same time when you update client libraries of your application.
It is possible that client libraries may work even with the older releases of the Red Hat build of Keycloak server, but it is not guaranteed and officially supported.
It may be needed to consult the javadoc of the client libraries like Java admin-client to see what endpoints and parameters are supported with which Red Hat build of Keycloak server version. For the admin client, see "Compatibility with Red Hat build of Keycloak server" in the Red Hat build of Keycloak admin client chapter for some additional notes.
