---
title: "Chapter 5. Upgrading the Red Hat build of Keycloak Client Libraries - Red Hat build of Keycloak 26.0 Upgrading Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-upgrading-the-red-hat-build-of-keycloak-client-libraries
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/upgrading_guide/upgrading_the_red_hat_build_of_keycloak_client_libraries
guide: upgrading_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 5. Upgrading the Red Hat build of Keycloak Client Libraries - Red Hat build of Keycloak 26.0 Upgrading Guide

Chapter 5. Upgrading the Red Hat build of Keycloak Client Libraries
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
The client libraries are supported with all the supported Red Hat build of Keycloak server versions. The fact that client libraries are supported with more server versions makes the update easier, so you may not need to update the server at the same time when you update client libraries of your application.
It is possible that client libraries may work even with the older releases of the Red Hat build of Keycloak server, but it is not guaranteed and officially supported.
It may be needed to consult the javadoc of the client libraries like Java admin-client to see what endpoints and parameters are supported with which Red Hat build of Keycloak server version.
