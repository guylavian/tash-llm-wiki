---
title: "Chapter 2. Release-specific changes - Red Hat build of Keycloak 26.2 Upgrading Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-migration-changes
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/upgrading_guide/migration-changes
guide: upgrading_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "2.1. Breaking changes at version 26.2.x At version 26.2.x, some breaking changes exist. Breaking changes are identified as requiring changes from existing users to their configurations. 2.1.1. Changes to port behavior with the X-Forwarded-Host header The X-Forwarded-Host header can optionally also contain the port. In previous versions when the port was omitted from the header, Red Hat build of Ke…"
---

# Chapter 2. Release-specific changes - Red Hat build of Keycloak 26.2 Upgrading Guide

Chapter 2. Release-specific changes
2.1. Breaking changes at version 26.2.x
At version 26.2.x, some breaking changes exist. Breaking changes are identified as requiring changes from existing users to their configurations.
2.1.1. Changes to port behavior with the X-Forwarded-Host header
The X-Forwarded-Host
header can optionally also contain the port. In previous versions when the port was omitted from the header, Red Hat build of Keycloak fell back to the actual request port. For example if Red Hat build of Keycloak was listening on port 8080 and the request contained X-Forwarded-Host: example.com
header, the resolved URL was http://example.com:8080
.
This is now changed and omitting the port results in removing it from the resolved URL. The resolved URL from the previous example would now be http://example.com
.
To mitigate that, either make your reverse proxy include the port in the X-Forwarded-Host
header or configure it to set the X-Forwarded-Port
header with the desired port.
2.1.2. Changes to installing Oracle JDBC driver
The required JAR for the Oracle JDBC driver that needs to be explicitly added to the distribution has changed. Instead of providing ojdbc11
JAR, use ojdbc17
JAR as stated in Installing the Oracle Database driver.
2.1.3. H2 Credentials
With this version, the default H2 based dev-file
database changed its credentials. While migrating from an instance using this dev only database is not supported, you may be able to continue to use your existing H2 database if you explicitly provide the old defaults for the database username and password. For example in the keycloak.conf
specify:
db-username=sa
db-password=password
2.1.4. JWT Client authentication aligned with the latest OIDC specification
The latest draft version of the OpenID Connect core specification changed the rules for audience validation in JWT client assertions for the Client Authentication methods private_key_jwt
and client_secret_jwt
.
Previously, the aud
claim of a JWT client assertion was loosely defined as The Audience SHOULD be the URL of the Authorization Server’s Token Endpoint
, which did not exclude the usage of other URLs.
The revised OIDC Core specification uses a stricter audience check: The Audience value MUST be the OP’s Issuer Identifier passed as a string, and not a single-element array.
.
We adapted the JWT client authentication authenticators of both private_key_jwt
and client_secret_jwt
to allow only a single audience in the token by default. For now, the audience can be the issuer, token endpoint, introspection endpoint or some other OAuth/OIDC endpoint, which is used by client JWT authentication. However since there is single audience allowed now, it means that it is not possible to use other unrelated audience values, which is to make sure that JWT token is really only useful by the Red Hat build of Keycloak for client authentication.
This strict audience check can be reverted to the previous more lenient check with a new option of OIDC login protocol SPI. It will be still allowed to use multiple audiences in JWT if server is started with the option:
--spi-login-protocol-openid-connect-allow-multiple-audiences-for-jwt-client-authentication=true
Note that this option might be removed in the future. Possibly in Red Hat build of Keycloak 27. So it is highly recommended to update your clients to use a single audience instead of using this option. It is also recommended that your clients use the issuer URL for the audience when sending JWT for client authentication as that is going to be compatible with the future version of OIDC specification.
2.1.5. Changes involving newly supported features
At version 26.2.x, the following changes are major improvements that provide new support for existing features.
2.1.6. Standard token exchange
In this release, Red Hat build of Keycloak added support for the Standard token exchange (Feature token-exchange-standard:v2
). In the past Red Hat build of Keycloak releases, Red Hat build of Keycloak had only a preview token exchange feature, which is now referred to as Legacy token exchange (Feature token-exchange:v1
). The legacy token exchange is still in preview and it works the same way as in previous releases. If you used the internal-internal token exchange,consider migrating to the new standard token exchange.
If you prefer to continue using the legacy token exchange, no need exists to disable the standard token exchange feature. Your clients will use the standard token exchange only if it is enabled on the Red Hat build of Keycloak client. However, migration to the standard token exchange is recommended. It is the officially supported method and the priority for enhancements.
Consider the following notes as you plan for migration to the new standard token exchange:
-
The feature
token-exchange-standard
, which represents the new Standard token exchange, is enabled by default. It is recommended to disable thetoken-exchange
feature, which represents the Legacy token exchange, to make sure that requests will be served by the new standard token exchange. You can have both the standard and legacy token exchange features enabled, which can be useful if you need to cover standard use cases (internal-internal) together with the other token exchange use cases that are implemented only by legacy token exchange. For instance, external to internal token exchange is implemented only by the legacy token exchange. In this case, Red Hat build of Keycloak serves the standard internal-to-internal requests preferably by the standard token exchange while the other requests are served by the legacy token exchange. The choice of standard or legacy token exchange is determined based on the parameters of the particular request. For example, requests containing non-standard parameters such as
requested_issuer
orrequested_subject
are considered legacy.If you still need the legacy token exchange feature, you also need Fine-grained admin permissions version 1 enabled (FGAP:v1) because version 2 (FGAP:v2) does not have support for token exchange permissions. This is on purpose because token-exchange is conceptually not really an "admin" permission and therefore token exchange permissions were not added to FGAP:v2.
- Standard token exchange requires enabling a switch on the client. See How to enable token exchange.
Consider these additional changes in the behavior of the two types of token exchange:
- Fine-grained admin permissions are no longer needed or supported for the standard token exchange.
-
The most notable change regarding the behavior of scopes and audiences is that the applied client scopes are based on the client triggering the token exchange request rather than the "target" client specified by the
audience
parameter. Support exists for multiple values of theaudience
parameter as mentioned in the specification. See How to enable token exchange. -
Public clients are no longer allowed to send the token exchange requests. Legacy token exchange allowed public clients to exchange tokens with themselves to downscope the original token. This use case can instead be covered by using the refresh token grant, in which the
scope
parameter can be used to downscope the refreshed access token, as mentioned in the OAuth2 specification. -
Exchanging an access token for a SAML assertion is not supported in this release. In other words, using
requested_token_type=urn:ietf:params:oauth:token-type:saml2
is not supported. - Exchanging an access token for a refresh token is allowed only if it is explicitly enabled on the client as mentioned in How to enable token exchange.
Currently, it is not supported to request offline tokens or exchange a refresh token when the subject token was issued from an offline session. The recommended approach is to exchange for access tokens instead of a refresh token when possible.
2.1.7. Fine-grained admin permissions
Red Hat build of Keycloak introduces fine-grained admin permissions V2, offering an improved and more flexible authorization model for administrative permissions.
- FGAP:V2 feature is enabled by default.
-
FGAP:V1 feature remains in preview and can be enabled using
--features=admin-fine-grained-authz:v1
. However, V1 may be deprecated and removed in a future release.
2.1.7.1. Migration from V1 to V2
Due to fundamental changes in the permission model, automatic migration from V1 to V2 is not available. To simplify the transition:
- A new admin-permissions client is introduced. This client is created when you enable the capability for the realm. The client holds the authorization model for FGAP:V2.
- The existing FGAP:V1 authorization model remains unchanged within the realm-management client.
- Administrators must recreate permissions and policies using the new model, which can be configured in the updated Permissions section of the Admin Console.
2.1.7.2. Key Differences Between FGAP:V1 and FGAP:V2
Realm-level enablement:
- FGAP:V2 can be enabled for a realm using the new Admin Permissions switch in Realm Settings.
Centralized management:
- The resource-specific Permissions tabs (for users, groups, clients, and roles) have been removed.
- A new Permissions section provides centralized management for all administrative permissions from a single place in the Admin Console.
Explicit operation scoping:
- Transitive dependencies between permissions have been removed.
- Administrators must now explicitly assign each required permission.
- Example: To both view and manage a resource, both view and manage scopes for a permission must be assigned separately.
Permission model changes:
- The user-impersonated user permission has been removed.
- The configure client permission has been removed. With the introduction of explicit operation scoping in V2, the distinction between manage and configure became ambiguous. Permissions to manage-members of a group do not allow a realm administrator to unassign members from groups. The reason for that restriction is that V1 allowed a member of a group to become a regular realm user, and workaround permissions to create users in a realm. Future releases may provide additional scopes to allow deletion of members from groups.
Flexible resource scoping:
- Unlike V1, where permissions were granted either to a single resource (for clients, groups, and roles) or all resources (for users), V2 introduces greater flexibility.
Administrators can now define permissions for:
- A specific resource
- A set of selected resources
- All resources of a given type
- This applies to all resource types: clients, users,groups, and roles.
Notable changes where an internal behavior changed to prevent common misconfigurations, fix bugs or simplify running Red Hat build of Keycloak.
2.2. Notable changes at version 26.2.15
2.2.1. Maximum length of the parameters in the OIDC token endpoint
When the OIDC token endpoint request (or OAuth2 token endpoint request) is sent, a new limit exists for the maximum length of every OIDC/OAuth2 parameter. The maximum length of each parameter is 4,000 characters, which is aligned with the same limit, which already exists for the parameters sent to OIDC/OAuth authentication request.
If you want to increase or lower those numbers, start the server with the option req-params-default-max-size
for the default maximum length of the OIDC/OAuth2 parameters or you can use something such as req-params-max-size
for one specific parameter.
For more details, see login protocol.
2.3. Notable changes at version 26.2.13
2.3.1. Usage of virtual threads for embedded caches
Previously virtual threads were used when at least two CPU cores were available. Starting with this version, virtual threads are only used when at least four CPU cores are available. This change should prevent deadlocks due to pinned virtual threads.
2.4. Notable changes at version 26.2.11
2.4.1. Change to user sessions created with "Remember Me"
When the "Remember Me" option is disabled in the realm settings, all user sessions previously created with the "Remember Me" flag are now considered invalid. Users will be required to log in again, and any associated refresh tokens will no longer be usable. User sessions created without selecting "Remember Me" are not affected.
2.4.2. New database indexes on OFFLINE_CLIENT_SESSION table
This change adds new indexes on the OFFLINE_CLIENT_SESSION
table to improve performance when retrieving or deleting client sessions.
If those tables contain more than 300,000 entries, Red Hat build of Keycloak skips the index creation during the automatic schema migration. Instead, the migration displays the required SQL statement to be applied manually after startup of Red Hat build of Keycloak. For details on configuring a different limit, see Migrating the database.
2.4.3. Filtering of LDAP referrals
This release adds filtering of LDAP referrals by default. This change enhances security and aligns with best practices for LDAP configurations. If this change is unacceptable, you can disable LDAP referrals in all LDAP providers in all realms.
2.4.4. Deprecated: Filtering of LDAP referrals
The option spi-storage-ldap-secure-referral
to disable filtering referrals is deprecated. When this feature is removed in a future release, filtering will be enforced.
2.5. Notable changes at version 26.2.10
2.5.1. serverinfo endpoint
The serverinfo
endpoint is used by the Admin Console to obtain general information of the Red Hat build of Keycloak installation. Starting with this version, the serverinfo
endpoint only returns the system information for administrators in the Master realm. This change was done for security reasons.
If an administrator in a common realm needs to access the systemInfo
, cpuInfo
or memoryInfo
fields of the serverinfo
response, create a view-system role and assign it to that administrator.
- In the affected realm, select the management client realm-management.
- In the Roles tab, create a role called view-system.
Select Users and perform the following actions:
- Select the administrator account.
- Click the Role mapping tab.
- Assign the view-system client role to that account.
The previous workaround is marked as deprecated and it can be removed in a future version of Red Hat build of Keycloak.
2.6. Notable changes at version 26.2.9
Notable changes where an internal behavior changed to prevent common misconfigurations, fix bugs or simplify running Red Hat build of Keycloak.
2.6.1. Maximum length of the parameters in the OIDC authentication request
When the OIDC authentication request (or OAuth2 authorization request) is sent, there is now limit for the maximum length of every standard OIDC/OAuth2 parameter. The maximum length of each standard parameter is 4000 characters, which is very big number and can be lowered in the future releases. For now, it is kept big for the backwards compatibility. The only exception is the login_hint
parameter, which is limited to the maximum length of 255 characters. This is aligned with the maximum length for the username
and email
attributes configured in the default user profile configuration.
If you want to make those number higher or lower, you can start the server with the option req-params-default-max-size
for the default maximum length of the standard OIDC/OAuth2 parameters, or you can use something like req-params-max-size
for one specific parameter. See the login-protocol
provider configuration.
2.7. Notable changes at version 26.2.8
Notable changes where an internal behavior changed to prevent common misconfigurations, fix bugs or simplify running Red Hat build of Keycloak.
2.7.1. UTF-8 management in the email sender
Since this release, Red Hat build of Keycloak adds a new option allowutf8
for the realm SMTP configuration (Allow UTF-8 field inside the Email tab in the Realm settings section of the Admin Console). For more information about email configuration, see the Configuring email for a realm chapter in the Server Administration Guide.
Enabling the option encodes email addresses in UTF-8 when sending them, but it depends on the SMTP server to also supports UTF-8 via the SMTPUTF8 extension. If Allow UTF-8 is disabled, Red Hat build of Keycloak will encode the domain part of the email address (second part after @
) using punycode if non-ASCII characters are used, and will reject email addresses that use non-ASCII characters in the local part.
If you have an SMTP server configured for your realm, perform the following migration after the upgrade:
If your SMTP server supports SMTPUTF8:
- Enable the Allow UTF-8 option.
If your SMTP server does not support SMTPUTF8:
- Keep the Allow UTF-8 option disabled.
- Verify that no email addresses of users have non-ASCII characters in the local part of the email address.
-
Update the validation of email addresses to prevent allow non-ASCII characters in the local part of the email address, for example, by adding a regex pattern validation in the user profile for the email address field similar to
\p{ASCII}*@.*
with an error message similar toLocal part of the address must contain only ASCII characters
.
2.8. Notable changes at version 26.2.6
Notable changes concern an internal behavior that is changed to prevent common misconfigurations, bug fixes, or a simplification to running Red Hat build of Keycloak.
2.8.1. Upgrade procedure changed for the distribution
If you are upgrading Red Hat build of Keycloak by downloading the distribution, the upgrade procedure has been changed. Previously, that procedure recommended copying over the contents of the conf/
folder from the old to the new installation. The new procedure recommends that you re-apply any changes to cache-ispn.xml
or a custom cache configuration based on the file included in the new version.
This step prevents you from accidentally downgrading functionality, for example, by using an old cache-ispn.xml
file from a previous version.
2.8.2. Problematic cache configurations ignored
Previous versions of Red Hat build of Keycloak warned about problematic configurations, for example, if a wrong number of owners was configured or a cache size was set when it should not have been set when enabling volatile user sessions. The docs also stated to update the cache-ispn.xml
configuration file for volatile user sessions.
The current version will always use safe settings for the number of owners and maximum cache size for the affected user and client session caches, and will log only an INFO message. With this behavior, there is no need any more to update the cache-ispn.xml
configuration file. If you previously used a custom cache-ispn.xml
in order to use volatile user sessions, we recommend reverting those changes and use the standard configuration file.
2.8.3. Verify existing account by Email is only executed for the email and username sent by the identity provider
The execution Verify Existing Account By Email is one of the alternatives that the First Login Flow has to allow a brokering account to be linked to an existing Red Hat build of Keycloak user. This step is executed when the user logs in into Red Hat build of Keycloak through the broker for the first time, and the identity provider account is already present in Red Hat build of Keycloak. The execution sends an email to the current Red Hat build of Keycloak address in order to confirm the user controls that account.
Since this release, the Verify Existing Account By Email execution is only attempted in the First Login Flow if the linking attributes (email and username) sent by the external identity provider are not modified by the user during the review process. This new behavior avoids sending verification emails to an existing Red Hat build of Keycloak account that can inadvertently accept the linking.
In case the provider needs to modify the information sent by the identity provider (because emails or usernames are different in the broker), only the other alternative Verify Existing Account By Re-authentication is available to link the new account to the existing Red Hat build of Keycloak user.
If the data received from the identity provider is mandatory and cannot be modified, then the Review Profile step in the First Login Flow can be disabled to avoid any user intervention.
For more information, see the First login flow section of the Server Administration Guide.
2.8.4. Updates to the user-profile-commons.ftl theme template
The user-profile-commons.ftl
changed to improve support for localization. As a result of this change, pages might start displaying a locale
field if you extend this template. To avoid that situation, update the theme template with the changes aforementioned.
2.9. Additional changes at version 26.2.x
The following changes concern internal behavior changes to prevent common misconfigurations, changes to address issues, and other changes that simplify running of Red Hat build of Keycloak.
2.9.1. Zero-configuration secure cluster communication
For clustering multiple nodes, Red Hat build of Keycloak uses distributed caches. Starting with this release for all TCP-based transport stacks, the communication between the nodes is encrypted with TLS and secured with automatically generated ephemeral keys and certificates.
If you are not using a TCP-based transport stack, it is recommended to migrate to the jdbc-ping
transport stack to benefit from the simplified configuration and enhanced security.
If you provided your own keystore and truststore to secure the TCP transport stack communication in previous releases, it is now recommended to migrate to the automatically generated ephemeral keys and certificates to benefit from the simplified setup.
If you are using a custom transport stack, this default behavior can be disabled by setting the option cache-embedded-mtls-enabled
to false
.
If you are using a service mesh, configure it to allow direct mTLS communication between the Red Hat build of Keycloak Pods.
For more details, see Securing Transport Stacks.
2.9.2. LDAP provider now can store new users, groups, and roles in a sub-DN of the base DN
When adding new users, groups, or roles, the LDAP provider would always store them in the same base DN configured for the searches. However, in some deployments admins may want to configure a broader DN with subtree
scope to fetch users (or groups/roles) from multiple sub-DNs, but they do not want new users (or groups/roles) to be stored in this base DN in LDAP. Instead, they would like to choose one of the sub-DNs for that.
It is now possible to control where new users, groups, or roles will be created using the new Relative User Creation DN
config option in the LDAP provider and also in the LDAP group and role mappers. For more details, see LDAP admin
2.9.3. proxy-trusted-addresses enforced for built-in X509 client certificate lookup providers
Built-in X.509 client certificate lookup providers now reflect the proxy-trusted-addresses
config option. A certificate provided through the HTTP headers will now be processed only if the proxy is trusted, or proxy-trusted-addresses
is unset.
2.9.4. Operator creates NetworkPolicies to restrict traffic
The Red Hat build of Keycloak Operator now creates by default a NetworkPolicy to restrict traffic to internal ports used for Red Hat build of Keycloak’s distributed caches.
This strengthens a secure-by-default setup and minimizes the configuration steps of new setups. This change is intended to be backwards compatible to existing deployment, so no additional steps are necessary at the time of the upgrade. You can return to the previous behavior by disabling the creation of NetworkPolicies in the Keycloak CR.
If your deployment scripts add explicit NetworkPolicies for Red Hat build of Keycloak, consider removing those and migrate to the new functionality provided in the Keycloak CR as a follow-up to the upgrade.
For more details, see Operator Advanced configuration.
2.9.5. Send Reset Email force login again for federated users after reset credentials
Previously the reset credentials flow (forgot password feature) kept the user logged in after the reset credentials if the same authentication session (same browser) was used. For federated user providers, this behavior can be a security issue. Consider a scenario where a provider implementation detects the user as enabled and performs the password change successfully, but somehow the validation of the user password fails. In this scenario, the reset credentials flow allowed a user to log in after the successful password change; however, that login would have been denied using the normal browser flow. This is not a common scenario, but it should be avoided by default.
For this reason, now the authenticator reset-credential-email
(Send Reset Email) has a new configuration option called force-login
(Force login after reset) with values true
(always force the login), false
(previous behavior that keeps the user logged in if the same authentication session is used), and only-federated
(default value that forces federated users to authenticate again and keeps the previous behavior for users stored in Red Hat build of Keycloak’s internal database).
For more information about changing this option, see Enable forgot password.
2.9.6. Offline access removes the associated online session if the offline_scope is requested in the initial exchange
Any offline session in Red Hat build of Keycloak is created from an online session. When the offline_access
scope is requested, the current online session is used to create the associated offline session for the client. Therefore, any offline_access
request finished, until now, created two sessions: one online and one offline. This situation leads to unreliable behavior. For example, when just the login with scope=offline_access
was requested, an unused online session could be created. This session is useless in most cases and causes unnecessary consumption of server resources.
Starting with this version, Red Hat build of Keycloak removes the initial online session if the offline_scope
is directly requested as the first interaction for the session. The client retrieves the offline token after the code to token exchange that is associated to the offline session, but the previous online session is removed. If the online session has been used before the offline_scope
request, by the same or another client, the online session remains active as today. This situation also means that the SSO session is not created in the browser if the login request with scope=offline_access
is used and the user was not already authenticated in the SSO beforehand. Although the new behavior makes sense because the client application is just asking for an offline token, it can affect some scenarios that rely on having the online session still active after the initial offline_scope
token request.
2.9.7. New client scope service_account for client_credentials grant mappers
Red Hat build of Keycloak introduces a new client scope at the realm level called service_account
. This scope is in charge of adding the specific claims for the client_credentials
grant (client_id
, clientHost
and clientAddress
) by using protocol mappers. This scope will be automatically assigned to and unassigned from the client when the serviceAccountsEnabled
option is set or unset in the client configuration.
Previously, the three mappers (Client Id
, Client Host
and Client IP Address
) were added directly to the dedicated scope when the client was configured to enable service accounts, and they were never removed.
The behavior should be effectively the same for most Red Hat build of Keycloak deployments because claims in the token are effectively the same as before. You might be affected in cases when you are using a client credentials grant and you are preparing the Red Hat build of Keycloak environment by some tooling that is manually removing or updating the three protocol mappers mentioned above. For instance, if you use an admin CLI script to enable a service-account for a client and then remove the built-in service-account protocol mappers, you may adjust your CLI to instead remove the assignment of the service_account
client scope from the client instead of removing protocol mappers.
2.9.8. JWT client authentication defines a new max expiration option for the token
When a client is configured to authenticate using the Signed JWT or Signed JWT with Client Secret type, Red Hat build of Keycloak now enforces a maximum expiration for the token. This means that, although the exp
(expiration) claim in the token may be much later, Red Hat build of Keycloak will not accept tokens issued before that max expiration time. The default value is 60 seconds. Note that JWT tokens should be issued right before being sent for authentication. As a result, the client has a one minute window to send the token for login. Nevertheless this expiration can be tuned using the Max expiration configuration option on the client Credentials tab. For more details, see Confidential client credentials.
2.9.9. Removed and deprecated features
At version 26.2.x, certain features have been removed and other features have been marked as deprecated for removal at a later release. For details on these changes, see the Release Notes.
