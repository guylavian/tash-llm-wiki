---
title: "Chapter 4. Upgrading Red Hat build of Keycloak adapters - Red Hat build of Keycloak 26.2 Upgrading Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-upgrading-red-hat-build-of-keycloak-adapters
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/upgrading_guide/upgrading_red_hat_build_of_keycloak_adapters
guide: upgrading_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "After upgrading the Red Hat build of Keycloak server, you upgrade the adapters. Versions of adapters and Red Hat build of Keycloak are now decoupled, meaning that they are released on different schedules. Therefore, use these rules to determine which adapters you upgrade: Earlier versions of an adapter might work with later versions of the Red Hat build of Keycloak server. Earlier versions of the …"
---

# Chapter 4. Upgrading Red Hat build of Keycloak adapters - Red Hat build of Keycloak 26.2 Upgrading Guide

Chapter 4. Upgrading Red Hat build of Keycloak adapters
After upgrading the Red Hat build of Keycloak server, you upgrade the adapters. Versions of adapters and Red Hat build of Keycloak are now decoupled, meaning that they are released on different schedules. Therefore, use these rules to determine which adapters you upgrade:
- Earlier versions of an adapter might work with later versions of the Red Hat build of Keycloak server.
- Earlier versions of the Red Hat build of Keycloak server might not work with later versions of an adapter.
Each adapter upgrade section provides details on supported adapter versions.
4.1. Upgrading the JBoss EAP SAML adapter
As of Red Hat build of Keycloak 26.0, the JBoss EAP SAML adapter is no longer released with Red Hat build of Keycloak. If you deployed an application with version 6.x or 7.x of that adapter, it is not supported by Red Hat build of Keycloak. Those versions of the adapter are only supported to be used in combination with Red Hat Single Sign-On 7.6.
The fully supported adapter for SAML is the Keycloak SAML Adapter feature pack or RPM for JBoss EAP 8.0.
To upgrade a JBoss EAP SAML adapter that has been copied to your web application, perform the following procedure.
Procedure
-
Remove the previous adapter modules by deleting the
EAP_HOME/modules/system/add-ons/keycloak/
directory. - Install the new version of the adapter. For full details, see Installing JBoss EAP by using the RPM installation method.
4.2. Upgrading the JBoss EAP OpenID connect adapter
As of Red Hat build of Keycloak 26.0, the JBoss EAP OpenID connect (OIDC) adapter is no longer released with Red Hat build of Keycloak. This adapter has reached end of life and it is only supported to be used in combination with Red Hat Single Sign-On 7.6. The supported adapter for OIDC is supplied by JBoss EAP 8.0.
To upgrade a JBoss EAP OIDC adapter that has been copied to your web application, perform the following procedure.
Procedure
-
Remove the previous adapter modules by deleting the
EAP_HOME/modules/system/add-ons/keycloak/
directory. - Install the OIDC client supplied by JBoss EAP 8.0. For details, see Securing Applications with OIDC.
4.3. Upgrading the JavaScript adapter
The previous version of the JavaScript adapter is 26.0.11. For this release of Red Hat build of Keycloak, the supported version of this adapter is 26.2.0.
To upgrade a JavaScript adapter that has been copied to your web application, perform the following procedure.
Procedure
- Remove the previous version of the JavaScript adapter.
Use these NPM commands to install the 26.2.0 version of the adapter:
npm config set @redhat:registry https://npm.registry.redhat.com install: npm install @redhat/keycloak-js@latest
4.4. Upgrading the Node.js adapter
The previous version of the Node.js adapter is 26.0.11. For this release of Red Hat build of Keycloak, the supported version of this adapter is 26.1.1.
To upgrade a Node.js adapter that has been copied to your web application, perform the following procedure.
Procedure
- Remove the previous version of the Node.js adapter.
Use these NPM commands to install the 26.1.1 version of the Node.js adapter:
npm config set @redhat:registry https://npm.registry.redhat.com npm install @redhat/keycloak-connect@latest
-
Change the dependency for keycloak-connect in the
package.json
of your application.
