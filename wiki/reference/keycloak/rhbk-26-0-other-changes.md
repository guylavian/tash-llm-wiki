---
title: "Chapter 9. Other notable changes - Red Hat build of Keycloak 26.0 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-other-changes
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/migration_guide/other-changes
guide: migration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 9. Other notable changes - Red Hat build of Keycloak 26.0 Migration Guide

Chapter 9. Other notable changes
9.1. Javascript engine available by default on the classpath
In the previous version, when Keycloak was used on Java 17 with Javascript providers (Script authenticator, Javascript authorization policy or Script protocol mappers for OIDC and SAML clients), it was needed to copy the javascript engine to the distribution. This is no longer needed as Nashorn javascript engine is available in Red Hat build of Keycloak server by default. When you deploy script providers, it is recommended to not copy Nashorn’s script engine and its dependencies into the Red Hat build of Keycloak distribution.
9.2. Renamed Keycloak Admin client artifacts
After the upgrade to Jakarta EE, artifacts for Keycloak Admin clients were renamed to more descriptive names with consideration for long-term maintainability. However, two separate Keycloak Admin clients still exist: one with Jakarta EE and the other with Java EE support.
The org.keycloak:keycloak-admin-client-jakarta
artifact is no longer released. The default one for the Keycloak Admin client with Jakarta EE support is org.keycloak:keycloak-admin-client
(since version 26.0.0).
The new artifact with Java EE support is org.keycloak:keycloak-admin-client-jee
.
9.2.1. Jakarta EE support
The new artifact with Java EE support is org.keycloak:keycloak-admin-client-jee
. Jakarta EE support
Before migration:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-admin-client-jakarta</artifactId>
<version>18.0.0.redhat-00001</version>
</dependency>
After migration:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-admin-client</artifactId>
<version>22.0.0.redhat-00001</version>
</dependency>
9.2.2. Java EE support
Before migration:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-admin-client</artifactId>
<version>18.0.0.redhat-00001</version>
</dependency>
After migration:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-admin-client-jee</artifactId>
<version>22.0.0.redhat-00001</version>
</dependency>
9.3. Never expires option removed from client advanced settings combos
The option Never expires
is now removed from all the combos of the Advanced Settings client tab. This option was misleading because the different lifespans or idle timeouts were never infinite, but limited by the general user session or realm values. Therefore, this option is removed in favor of the other two remaining options: Inherits from the realm settings
(the client uses general realm timeouts) and Expires in
(the value is overridden for the client). Internally the Never expires
was represented by -1
. Now that value is shown with a warning in the Admin Console and cannot be set directly by the administrator.
9.4. New email rules and limits validation
Red Hat build of Keycloak has new rules on email creation to allow ASCII characters during the email creation. Also, a new limit of 64 characters on exists on local email part (before the @). So, a new parameter --spi-user-profile-declarative-user-profile-max-email-local-part-length
is added to set max email local part length taking backwards compatibility into consideration. The default value is 64.
kc.sh start --spi-user-profile-declarative-user-profile-max-email-local-part-length=100
