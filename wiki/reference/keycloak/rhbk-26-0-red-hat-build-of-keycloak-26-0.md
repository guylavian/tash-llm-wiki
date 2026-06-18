---
title: "Chapter 1. Red Hat build of Keycloak 26.0 - Red Hat build of Keycloak 26.0 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-0-red-hat-build-of-keycloak-26-0
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/release_notes/red_hat_build_of_keycloak_26_0
guide: release_notes
version: 26.0
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 1. Red Hat build of Keycloak 26.0 - Red Hat build of Keycloak 26.0 Release Notes

Chapter 1. Red Hat build of Keycloak 26.0
1.1. Overview
Red Hat build of Keycloak is based on the Keycloak project, which enables you to secure your web applications by providing Web SSO capabilities based on popular standards such as OpenID Connect, OAuth 2.0, and SAML 2.0. The Red Hat build of Keycloak server acts as an OpenID Connect or SAML-based identity provider (IdP), allowing your enterprise user directory or third-party IdP to secure your applications by using standards-based security tokens.
While preserving the power and functionality of Red Hat Single Sign-on, Red Hat build of Keycloak is faster, more flexible, and efficient. Red Hat build of Keycloak is an application built with Quarkus, which provides developers with flexibility and modularity. Quarkus provides a framework that is optimized for a container-first approach and provides many features for developing cloud-native applications.
1.2. Updates for 26.0.17
This release contains several fixed issues.
1.3. Updates for 26.0.16
This release contains several fixed issues and a change related to OIDC authentication requests.
1.3.1. OIDC authentication request
When the OIDC authentication request (or OAuth2 authorization request) is sent, a limit now exists for the maximum length of every standard OIDC/OAuth2 parameter. The maximum length of each standard parameter is 4,000 characters, which is a large number for backwards compatibility. The only exception is the login_hint
parameter, which has a maximum length of 255 characters. This change is aligned with the maximum length for the username
and email
attributes, which are configured in the default user profile configuration.
If you want to increase or decrease that number, you can start the server with the req-params-default-max-size
option for the default maximum length of the standard OIDC/OAuth2 parameters. Alternatively, you can use something such as req-params-max-size
for one specific parameter. For more details, see the login-protocol
provider configuration under All provider configuration.
1.4. Updates for 26.0.15
This release contains several fixed issues.
1.5. Updates for 26.0.14
This release contains several fixed issues.
1.6. Updates for 26.0.13
This release contains several fixed issues and a change to how verifying an account by email is executed.
1.6.1. Verify existing account by Email is only executed for the email and username sent by the identity provider
The execution Verify Existing Account By Email is one of the alternatives that the First Login Flow has to allow a brokering account to be linked to an existing Red Hat build of Keycloak user. This step is executed when the user logs in into Red Hat build of Keycloak through the broker for the first time, and the identity provider account is already present in Red Hat build of Keycloak. The execution sends an email to the current Red Hat build of Keycloak address in order to confirm the user controls that account.
Since this release, the Verify Existing Account By Email execution is only attempted in the First Login Flow if the linking attributes (email and username) sent by the external identity provider are not modified by the user during the review process. This new behavior avoids sending verification emails to an existing Red Hat build of Keycloak account that can inadvertently accept the linking.
In case the provider needs to modify the information sent by the identity provider (because emails or usernames are different in the broker), only the other alternative Verify Existing Account By Re-authentication is available to link the new account to the existing Red Hat build of Keycloak user.
If the data received from the identity provider is mandatory and cannot be modified, the Review Profile step in the First Login Flow can be disabled to avoid any user intervention.
For more information, see the First login flow section of the Server Administration Guide.
1.7. Updates for 26.0.12
This release contains several fixed issues.
1.8. Updates for 26.0.11
This release contains several fixed issues, CVE fixes, and a change for JWT client authentication.
1.8.1. CVE fixes
- CVE-2025-2559 JWT Token Cache Exhaustion Leading to Denial of Service (DoS) in Keycloak. A trusted client with long-lived JWT tokens can cause memory exhaustion in Keycloak due to unbounded token caching.
- CVE-2025-3501 Hostname verification issue that causes the trust store to trust all certificates. By setting the verification policy to 'ALL' not only the hostname check is skipped, but also the trust store certificate verification, which is an unintended side effect.
CVE-2025-3910 Two factor authentication bypass. AIA (Application-initiated actions) could be used to circumvent required actions configured by an administrator to be performed by a user upon signing in. This could lead to the user circumventing requirements such as setting up 2FA.
- A user account that has been required by an administrator to perform a required action.
- The same user passing in a URL parameter during the sign in process.
1.8.2. Change for JWT client authentication
When a client is configured to authenticate using the Signed JWT or Signed JWT with Client Secret type, Red Hat build of Keycloak now enforces a maximum expiration for the token. As a result, although the exp
(expiration) claim in the token may be much later, Red Hat build of Keycloak does not accept tokens issued before that max expiration time. The default value is 60 seconds.
Note that JWT tokens should be issued right before being sent for authentication. This provides the client with a one-minute window to send the token for login. You can adjust this expiration by using the Max expiration configuration option in the client Credentials tab. For more details, see Confidential client credentials.
1.9. Updates for 26.0.10
This release contains several fixed issues, CVE fixes, and a change for Send Reset Email.
1.9.1. CVE fixes
- CVE-2025-0604 Authentication Bypass Due to Missing LDAP Bind After Password Reset in Keycloak
- CVE-2025-1391 Keycloak could allow incorrect assignment of an organization to a user
1.9.2. Change for Send Reset Email
In previous releases, the reset credentials flow (forgot password feature) keeps the user logged in after the reset credentials if the same authentication session (same browser) was used. For federated user providers, this behavior can be a security issue. Imagine a provider implementation that detects the user as enabled, performs a successful password change, but the validation of the user password somehow fails. In this scenario, the reset credentials flow allowed a user to log in after a successful password change that would have been disallowed to log in using the normal browser flow. This scenario is an uncommon case, but it should be avoided by default.
In the current release, the authenticator reset-credential-email
(Send Reset Email) has a new configuration option called force-login
(Force login after reset) with three possible values:
-
true
- always force the login -
false
- the previous behavior that keeps the user logged in if the same authentication session is used -
only-federated
- the default value that forces federated users to authenticate again and keeps the previous behavior for users stored in Red Hat build of Keycloak’s internal database
For more details about changing this option, see Enable forgot password.
1.10. Updates for 26.0.9
This release contains several fixed issues.
1.11. Updates for 26.0.8
This release contains several fixed issues and CVE fixes.
1.11.1. CVE fixes
CVE-2024-11734 Unrestricted admin use of system and environment variables
A security vulnerability has been identified that could enable administrative users to access sensitive data if certain configurations are set, potentially revealing internal details from the server environment.
CVE-2024-11736 Denial of Service in Red Hat build of Keycloak Server via Security Headers
A potential Denial of Service (DoS) vulnerability has been identified in Red Hat build of Keycloak. An administrative user with the ability to modify realm settings could exploit this issue to cause service disruptions. If triggered, it may prevent users from accessing applications that rely on Keycloak or using its management consoles within the affected realm.
1.11.2. Deprecating using system variables in the realm configuration
To favor a more secure server runtime and avoid to accidentally expose system variables, you are now forced to specify which system variables you want to expose by using the spi-admin-allowed-system-variables
configuration option when starting the server.
In future releases, this capability will be removed in favor of preventing any usage of system variables in the realm configuration.
1.12. Updates for 26.0.7
This release contains several fixed issues and these additional updates.
1.12.1. Container images use OpenJDK 21
With this release, the container images use OpenJDK 21, which provides better performance than OpenJDK 17.
1.12.2. getAll() methods deprecated in certain APIs
getAll()
methods in Organizations
and OrganizationMembers
APIs are now deprecated and will be removed in the next major release. Instead, use corresponding list(first, max)
methods in Organizations
and OrganizationMembers
APIs.
1.13. Updates for 26.0.6
This release contains several fixed issues and the following additional changes.
1.13.1. CVE fixes
- CVE-2024-10451 Sensitive Data Exposure in Keycloak Build Process
- CVE-2024-10270 Keycloak Denial of Service
- CVE-2024-10492 Keycloak path traversal
- CVE-2024-9666 Keycloak proxy header handling Denial-of-Service [DoS] vulnerability
- CVE-2024-10039 Keycloak TLS passthrough
1.13.2. Updated documentation for X.509 client certificate lookup by proxy
Potential vulnerable configurations have been identified in the X.509 client certificate lookup when using a reverse proxy. If you have configured the client certificate lookup by a proxy header, additional configuration steps might be required. For more detail, see Enabling client certificate lookup.
1.13.3. Admin events might include more details
In this release, admin events might hold additional details about the context when the event is fired. After the upgrade, you find the database schema has a new column DETAILS_JSON
in the ADMIN_EVENT_ENTITY
table.
1.13.4. Security improvements for the key resolvers
While using the REALM_FILESEPARATOR_KEY
key resolver, Red Hat build of Keycloak now restricts access to FileVault secrets outside of its realm. Characters that could cause path traversal when specifying the expression placeholder in the Administration Console are now prohibited.
Additionally, the KEY_ONLY
key resolver now escapes the _
character to prevent reading secrets that would otherwise be linked to another realm when the REALM_UNDERSCORE_KEY
resolver is used. The escaping simply replaces _
with __
, so, for example, ${vault.my_secret}
now looks for a file named my__secret
. Because this is a breaking change, a warning is logged to ease the transition.
1.14. New features and enhancements
The following release notes apply to Red Hat build of Keycloak 26.0.5, the first 26.0 release of the product.
1.14.1. Java support
Red Hat build of Keycloak now supports OpenJDK 21. OpenJDK 17 support is deprecated and will be removed in a following release in favor of OpenJDK 21.
1.14.2. Keycloak JavaScript adapter now standalone
Keycloak JavaScript adapter is now a standalone library and is therefore no longer served statically from the Red Hat build of Keycloak server. The goal is to de-couple the library from the Red Hat build of Keycloak server, so that it can be refactored independently, simplifying the code and making it easier to maintain in the future. Additionally, the library is now free of third-party dependencies, which makes it more lightweight and easier to use in different environments.
For a complete breakdown of the changes consult the Upgrading Guide.
1.14.3. Organizations, multi-tenancy, and Customer Identity and Access Management
This release introduces organizations. The feature leverages the existing Identity and Access Management (IAM) capabilities of Red Hat build of Keycloak to address Customer Identity and Access Management (CIAM) use cases like Business-to-Business (B2B) and Business-to-Business-to-Consumer (B2B2C) integrations. By using the existing capabilities from a realm, the first release of this feature provides the very core capabilities to allow a realm to integrate with business partners and customers:
- Manage Organizations
- Manage Organization Member
- Onboard members using different strategies such as invitation links and brokering
- Decorate tokens with additional metadata about the organization that the subject belongs to
For more details, see Managing organizations.
1.14.4. Using organizations for multiple instances of a social broker in a realm
You can now have multiple instances of the same social broker in a realm.
Normally, a realm does not need multiple instances of the same social broker. However, with the organization
feature, you can link different instances of the same social broker to different organizations.
When creating a social broker, provide an Alias
and optionally a Display name
just like any other broker.
1.14.5. Identity Providers no longer available from the realm representation
To help with scaling realms and organizations with many identity providers, the realm representation no longer holds the list of identity providers. However, they are still available from the realm representation when exporting a realm.
For more details, see Identity providers.
1.14.6. User sessions persisted by default
Previous versions of Red Hat build of Keycloak stored only offline user and offline client sessions in the databases. The new feature, persistent-user-sessions, stores online user sessions and online client sessions in both memory and the database. As a result, a user can stay logged in even if all instances of Red Hat build of Keycloak are restarted or upgraded.
For more details, see Persistent user sessions.
This feature is enabled by default. If you want to disable it, see the Volatile user sessions
procedure in the Configuring distributed caches chapter for more details.
1.14.7. Account Console and Admin Console changes
1.14.7.1. New Admin Console default login theme
A new version of the keycloak
login theme exists. The v2
version provides an improved look and feel, including support for switching automatically to a dark theme based on user preferences. The previous version (v1
) is deprecated, and will be removed in a future release.
The default login theme for all new realms will be keycloak.v2
. Also, existing realms that never explicitly set a login theme will be switched to keycloak.v2
.
1.14.7.2. PatternFly 5 for Admin and Account Consoles
In Red Hat build of Keycloak 24, the Welcome page wss updated to use PatternFly 5, the latest version of the design system that underpins the user interface of Red Hat build of Keycloak. In this release, the Admin Console and Account Console are also updated to use PatternFly 5. If you want to extend and customize the Admin Console and Account Console, review the changes in PatternFly 5 and update your customizations accordingly.
1.14.9. You are already logged in message
The Red Hat build of Keycloak 24 release provided improvements for when a user is authenticated in parallel in multiple browser tabs. However, this improvement did not address the case when an authentication session expired. In this release, when a user is already logged in to one browser tab and an authentication session expired in another browser tab, Red Hat build of Keycloak redirects back to the client application with an OIDC/SAML error. As a result, the client application can immediately retry authentication, which should usually automatically log in the application because of the SSO session.
Note that the message You are already logged in does not appear to the end user when an authentication session expires and user is already logged-in. You may consider updating your applications to handle this error.
For more details, see authentication sessions.
1.14.10. Searching by user attribute is now case sensitive
When searching for users by user attribute, Red Hat build of Keycloak no longer searches for user attribute names forcing lower case comparisons. The goal of this change was to speed up searches by using the Red Hat build of Keycloak native index on the user attribute table. If your database collation is case-insensitive, your search results will stay the same. If your database collation is case-sensitive, you might see fewer search results than before.
1.14.11. Password policy for check if password contains Username
Red Hat build of Keycloak supports a new password policy that allows you to deny user passwords which contains the user username.
1.14.12. Required actions improvements
In the Admin Console, you can now configure some actions in the Required actions tab of a particular realm. Currently, the Update password is the only built-in configurable required action. It supports setting Maximum Age of Authentication, which is the maximum time users can update their password by the kc_action
parameter (used for instance for a password update in the Account Console) without re-authentication.
The sorting of required actions is also improved. When multiple actions are required during authentication, all actions are sorted together regardless of whether those are actions set during authentication (for instance by the kc_action
parameter) or actions added to the user account manually by an administrator.
1.14.13. Default client profile for SAML
The default client profile for secured SAML clients was added. When browsing through client policies of a realm in the Admin Console, you see a new client profile saml-security-profile
. When it is used, there are security best practices applied for SAML clients. For example, signatures are enforced, SAML Redirect binding is disabled, and wildcard redirect URLs are prohibited.
1.14.14. Improving performance for deletion of user consents
When a client scope or the full realm is deleted, the associated user consents should also be removed. A new index over the table USER_CONSENT_CLIENT_SCOPE
has been added to increase the performance.
Note that, if the table contains more than 300,000 entries, Red Hat build of Keycloak skips the creation of the indexes during the automatic schema migration and logs the SQL statements to the console instead. The statements must be run manually in the database after Red Hat build of Keycloak startup.
1.14.15. New generalized event types for credentials
Generalized events now exist for updating (UPDATE_CREDENTIAL
) and removing (REMOVE_CREDENTIAL
) a credential. The credential type is described in the credential_type
attribute of the events. The new event types are supported by the Email Event Listener.
The following event types are now deprecated and will be removed in a future version: UPDATE_PASSWORD
, UPDATE_PASSWORD_ERROR
, UPDATE_TOTP
, UPDATE_TOTP_ERROR
, REMOVE_TOTP
, REMOVE_TOTP_ERROR
.
1.14.16. Management port for metrics and health endpoints
Metrics and health checks endpoints are no longer accessible through the standard Red Hat build of Keycloak server port. As these endpoints should be hidden from the outside world, they can be accessed on a separate default management port 9000
.
Using a separate port prevents exposure to the users as standard Red Hat build of Keycloak endpoints in Kubernetes environments. The new management interface provides a new set of options, which you can configure.
The Red Hat build of Keycloak Operator assumes the management interface is enabled by default. For more details, see Configuring the Management Interface.
1.14.16.1. Metrics for embedded caches enabled by default
Metrics for the embedded caches are now enabled by default. To enable histograms for latencies, set the option cache-metrics-histograms-enabled
to true
.
1.14.16.2. Metrics for HTTP endpoints enabled by default
The metrics provided by Red Hat build of Keycloak now include HTTP server metrics starting with http_server
. See below for some examples.
http_server_active_requests 1.0
http_server_requests_seconds_count{method="GET",outcome="SUCCESS",status="200",uri="/realms/{realm}/protocol/{protocol}/auth"} 1.0
http_server_requests_seconds_sum{method="GET",outcome="SUCCESS",status="200",uri="/realms/{realm}/protocol/{protocol}/auth"} 0.048717142
Use the new options http-metrics-histograms-enabled
and http-metrics-slos
to enable default histogram buckets or specific buckets for service level objectives (SLOs). Read more about histograms in the Prometheus documentation about histograms on how to use the additional metrics series provided in http_server_requests_seconds_bucket
.
1.14.17. Client libraries updates
1.14.17.1. Dedicated release cycle for the client libraries
Starting at this release, some Red Hat build of Keycloak client libraries will have release cycles independent of the Red Hat build of Keycloak server release cycle. The 26.0 release may be the last one when the client libraries are released together with the Red Hat build of Keycloak server. From now on, the client libraries may be released at a different time than the Red Hat build of Keycloak server.
The client libraries are these artifacts:
-
Java admin client - Maven artifact
org.keycloak:keycloak-admin-client
-
Java authorization client - Maven artifact
org.keycloak:keycloak-authz-client
-
Java policy enforcer - Maven artifact
org.keycloak:keycloak-policy-enforcer
1.14.17.2. Compatibility of the client libraries with the server
Starting at this release, client libraries are tested and supported with the same server version and a few previous major server versions.
For details about supported versions of client libraries with server versions, see the Upgrading Guide.
1.14.18. Cookie updates
1.14.18.1. SameSite attribute set for all cookies
Previously, the following cookies did not set the SameSite
attribute, which in recent browser versions results in these cookies defaulting to SameSite=Lax
:
-
KC_STATE_CHECKER
now setsSameSite=Strict
-
KC_RESTART
now setsSameSite=None
-
KEYCLOAK_LOCALE
now setsSameSite=None
-
KEYCLOAK_REMEMBER_ME
now setsSameSite=None
The default value SameSite=Lax
causes issues with POST based bindings, which is mostly applicable to SAML, but it is also used in some OpenID Connect / OAuth 2.0 flows.
1.14.18.2. Removing KC_AUTH_STATE cookie
The cookie KC_AUTH_STATE
is removed and it is no longer set by the Red Hat build of Keycloak server as this server no longer needs this cookie.
1.14.19. Lightweight access tokens
1.14.19.1. Lightweight access token to be even more lightweight
In previous releases, the support for lightweight access token was added. In this release, the even more built-in claims are removed from the lightweight access token. The claims are added by protocol mappers. Some affect even the regular access tokens or ID tokens as they were not strictly required by the OIDC specification.
-
Claims
sub
andauth_time
are added by protocol mappers now, which are configured by default on the new client scopebasic
, which is added automatically to all the clients. The claims are still added to the ID token and access token as before, but not to the lightweight access token. -
Claim
nonce
is added only to the ID token now. It is not added to a regular access token or lightweight access token. For backwards compatibility, you can add this claim to an access token by protocol mapper, which needs to be explicitly configured. -
Claim
session_state
is not added to any token now. You can still add it by protocol mapper. The other dedicated claimsid
is still supported by the specification, which was available in previous versions and has exactly the same value.
For more details, see New default client scope basic.
1.14.19.2. Lightweight access tokens for Admin REST API
Lightweight access tokens can now be used on the admin REST API. The security-admin-console
and admin-cli
clients are now using lightweight access tokens by default, so “Always Use Lightweight Access Token” and “Full Scope Allowed” are now enabled on these two clients. However, the behavior in the Admin Console should effectively remain the same. Be cautious if you have made changes to these two clients and if you are using them for other purposes.
1.14.20. Support for application/jwt media-type in token introspection endpoint
You can use the HTTP Header Accept: application/jwt
when invoking a token introspection endpoint. When enabled for a particular client, it returns a claim jwt
from the token introspection endpoint with the full JWT access token, which can be useful especially when the client calling introspection endpoint used a lightweight access token.
1.14.21. Password changes
1.14.21.1. Argon2 password hashing
Argon2 is now the default password hashing algorithm used by Red Hat build of Keycloak in a non-FIPS environment.
Argon2 was the winner of the 2015 password hashing competition and is the recommended hashing algorithm by OWASP.
In Red Hat build of Keycloak 24, the default hashing iterations for PBKDF2 were increased from 27.5K to 210K, resulting in a more than 10 times increase in the amount of CPU time required to generate a password hash. With Argon2, you can achieve better security with almost the same CPU time as with previous releases of Red Hat build of Keycloak. One downside is Argon2 requires more memory, which is a requirement to be resistant against GPU attacks. The defaults for Argon2 in Red Hat build of Keycloak require 7MB per-hashing request.
To prevent excessive memory and CPU usage, the parallel computation of hashes by Argon2 is by default limited to the number of cores available to the JVM. To support the memory intensive nature of Argon2, the default GC is updated from ParallelGC to G1GC for a better heap utilization.
Note that Argon2 is not compliant with FIPS 140-2. So if you are in the FIPS environment, the default algorithm will be still PBKDF2. Also note that if you are on non-FIPS environment and you plan to migrate to the FIPS environment, consider changing the password policy to a FIPS compliant algorithm such as pbkdf2-sha512
at the outset. Otherwise, users will not be able to log in after they switch to the FIPS environment.
1.14.21.2. Password policy for check if password contains Username
Red Hat build of Keycloak supports a new password policy that allows you to deny a user password that contains the user username.
1.14.22. Passkeys improvements (preview)
The support for Passkeys conditional UI was added. When this preview feature is enabled, a dedicated authenticator is available. You can select from a list of available passkeys accounts and authenticate a user based on that.
1.14.23. Authenticator for override existing IDP link during first-broker-login
A new authenticator Confirm override existing link
exists. This authenticator allows you to override the linked IDP username for the Red Hat build of Keycloak user, which was previously linked to different IDP identity. For more details, see override existing broker link.
1.14.24. Authorization changes
1.14.24.1. Breaking fix in authorization client library
For users of the keycloak-authz-client
library, calling AuthorizationResource.getPermissions(…)
now correctly returns a List<Permission>
. Previously, it would return a List<Map>
at runtime, even though the method declaration advertised List<Permission>
.
This fix will break code that relied on casting the List or its contents to List<Map>
.
1.14.24.2. IDs are no longer set when exporting authorization settings for a client
When exporting the authorization settings for a client, the IDs for resources, scopes, and policies are no longer set. As a result, you can now import the settings from one client to another client.
1.14.26. Configuring the LDAP Connection Pool
In this release, the LDAP connection pool configuration relies solely on system properties.
For more details, see Configuring the connection pool.
1.14.27. New LDAP users are enabled by default when using Microsoft Active Directory
If you are using Microsoft AD and creating users through the administrative interfaces, the user will created as enabled by default.
In previous versions, it was only possible to update the user status after setting a (non-temporary) password to the user. This behavior was not consistent with other built-in user storages as well as not consistent with others LDAP vendors supported by the LDAP provider.
1.14.28. The java-keystore key provider supports more algorithms and vault secrets
The java-keystore
key provider, which allows loading a realm key from an external java keystore file, has been modified to manage all Red Hat build of Keycloak algorithms. Also, the keystore and key secrets, which are needed to retrieve the actual key from the store, can be configured using the vault. Therefore, a Red Hat build of Keycloak realm can externalize any key to the encrypted file without sensitive data stored in the database.
For more information about this subject, see Configuring realm keys.
1.14.29. Small changes in session lifespan and idle calculations
In previous versions, the session max lifespan and idle timeout calculation was slightly different when validating if a session was still valid. Now that validation uses the same code as the rest of the project.
If the session is using the remember me feature, the idle timeout and max lifespan are the maximum value between the common SSO and the remember me configuration values.
1.14.30. New Hostname options
Due to the complexity of the hostname configuration settings, this release includes Hostname v2 options. The original host name options have been removed. If you have custom hostname settings, you should migrate to the new options. Note that the behavior behind these options has also changed.
For more details, see New hostname options.
1.14.31. Logging enhancements
1.14.31.1. Syslog for remote logging
Red Hat build of Keycloak now supports the Syslog protocol for remote logging based on the protocol defined in RFC 5424. If you enable the syslog handler, it sends all log events to a remote syslog server.
For more information, see Configuring logging.
1.14.31.2. Different log levels for log handlers
You can now specify log levels for all available log handlers, such as console
, file
, or syslog
. This more fine-grained approach means that you can control logging over the whole application to match your specific needs.
For more information, see Configuring logging.
1.14.32. All cache options are runtime
You can now specify the cache
, cache-stack
, and cache-config-file
options during runtime. This change eliminates the need to execute the build phase and rebuild your image with these options.
For more details, see Specify cache options at runtime.
1.14.33. Improvements for highly available multi-site deployments
Red Hat build of Keycloak 26 introduces significant improvements to the recommended high availability multi-site architecture, most notably:
- Red Hat build of Keycloak deployments are now able to handle user requests simultaneously in both sites.
- Active monitoring of the connectivity between the sites is now required to update the replication between the sites in case of a failure.
- The loadbalancer blueprint has been updated to use the AWS Global Accelerator as this avoids prolonged fail-over times caused by DNS caching by clients.
- Persistent user sessions are now a requirement of the architecture. Consequently, user sessions will be kept on Red Hat build of Keycloak or Data Grid upgrades.
For details on implementation, see Highly available multi-site deployments.
1.14.34. Method getExp added to SingleUseObjectKeyModel
As a consequence of the removal of deprecated methods from AccessToken
, IDToken
, and JsonWebToken
, the SingleUseObjectKeyModel
also changed to keep consistency with the method names related to expiration values.
For more details, see SingleUseObjectKeyModel.
1.14.35. Support for PostgreSQL 16
The supported and tested databases now include PostgreSQL 16.
1.14.36. Infinispan marshalling changes to Infinispan Protostream
Marshalling is the process of converting Java objects into bytes to send them across the network between Red Hat build of Keycloak servers. With Red Hat build of Keycloak 26, the marshalling format is changed from JBoss Marshalling to Infinispan Protostream.
JBoss Marshalling and Infinispan Protostream are not compatible with each other and incorrect usage may lead to data loss. Consequently, all caches are cleared when upgrading to this version.
Infinispan Protostream is based on Protocol Buffers (proto 3), which has the advantage of backwards/forwards compatibility.
1.14.37. Keycloak CR changes
1.14.37.1. Keycloak CR supports standard scheduling options
The Keycloak CR now exposes first class properties for controlling the scheduling of your Keycloak Pods. The scheduling stanza exposes optional standard Kubernetes affinity, tolerations, topology spread constraints, and the priority class name to fine tune the scheduling and placement of your server Pods.
For more details, see Scheduling.
1.14.37.2. KeycloakRealmImport CR supports placeholder replacement
The KeycloakRealmImport CR now exposes spec.placeholders
to create environment variables for placeholder replacement in the import.
For more details, see Realm import.
1.14.38. Admin Bootstrapping and Recovery
In previous releases, regaining access to a Red Hat build of Keycloak instance when all admin users were locked out was a challenging process. However, Red Hat build of Keycloak now offers new methods to bootstrap a temporary admin account and recover lost admin access.
You can now run the start
or start-dev
commands with specific options to create a temporary admin account. Also, a new dedicated command is introduced, allowing users to quickly regain admin access.
Consequently, the environment variables KEYCLOAK_ADMIN
and KEYCLOAK_ADMIN_PASSWORD
have been deprecated. You should use KC_BOOTSTRAP_ADMIN_USERNAME
and KC_BOOTSTRAP_ADMIN_PASSWORD
instead. These are also general options, so they may be specified via the cli or other config sources, for example --bootstrap-admin-username=admin
.
For more information, see the temporary admin account.
1.14.39. OpenTelemetry Tracing Preview feature
The underlying Quarkus support for OpenTelemetry Tracing has been exposed to Red Hat build of Keycloak and allows you to obtain application traces for better observability. This feature includes the ability to locate performance bottlenecks, determine the cause of application failures, and trace a request through the distributed system.
For more information, see Enabling tracing.
1.14.40. DPoP improvements
The DPoP (OAuth 2.0 Demonstrating Proof-of-Possession) preview feature has improvements. The DPoP is now supported for all grant types. With previous releases, this feature was supported only for the authorization_code
grant type. Support also exists for the DPoP token type on the UserInfo endpoint.
1.14.41. Adding support for ECDH-ES encryption key management algorithms
Now Red Hat build of Keycloak allows configuring ECDH-ES, ECDH-ES+A128KW, ECDH-ES+A192KW or ECDH-ES+A256KW as the encryption key management algorithm for clients. The Key Agreement with Elliptic Curve Diffie-Hellman Ephemeral Static (ECDH-ES) specification introduces three new header parameters for the JWT: epk
, apu
and apv
. Currently Red Hat build of Keycloak implementation only manages the compulsory epk
while the other two (which are optional) are never added to the header. For more information about those algorithms please refer to the JSON Web Algorithms (JWA).
Also, a new key provider, ecdh-generated
, is available to generate realm keys and support for ECDH algorithms is added into the Java KeyStore provider.
1.14.42. Persisting revoked access tokens across restarts
In this release, revoked access tokens are written to the database and reloaded when the cluster is restarted by default when using the embedded caches.
For more details, see Persisting removed access tokens.
1.14.43. Client Attribute condition in Client Policies
The condition based on the client-attribute was added into Client Policies. You can use this condition to specify for the clients with the specified client attribute having a specified value. Use either an AND or OR condition when evaluating this condition as mentioned in the documentation for client policies.
1.14.44. Adding support for ECDH-ES encryption key management algorithms
Now Red Hat build of Keycloak allows configuring ECDH-ES, ECDH-ES+A128KW, ECDH-ES+A192KW or ECDH-ES+A256KW as the encryption key management algorithm for clients. The Key Agreement with Elliptic Curve Diffie-Hellman Ephemeral Static (ECDH-ES) specification introduces three new header parameters for the JWT: epk
, apu
and apv
. Currently, Red Hat build of Keycloak implementation only manages the compulsory epk
while the other two (which are optional) are never added to the header. For more information about those algorithms, see the JSON Web Algorithms (JWA).
Also, a new key provider, ecdh-generated
, is available to generate realm keys and support for ECDH algorithms is added into the Java KeyStore provider.
1.14.45. Option proxy-trusted-addresses added
The proxy-trusted-addresses
can be used when the proxy-headers
option is set to specify an allowlist of trusted proxy addresses. If the proxy address for a given request is not trusted, then the respective proxy header values will not be used. For details, see Trusted Proxies.
1.14.46. Option proxy-protocol-enabled added
The proxy-protocol-enabled
option controls whether the server should use the HA PROXY protocol when serving requests from behind a proxy. When set to true, the remote address returned will be the one from the actual connecting client. For details, see Proxy Protocol.
1.14.47. Option to reload trust and key material added
The https-certificates-reload-period
option can be set to define the reloading period of key store, trust store, and certificate files referenced by https-* options. Use -1 to disable reloading. Defaults to 1h (one hour). For details, see Certificate and Key Reloading.
1.14.48. Options to configure cache max-count added
The --cache-embedded-${CACHE_NAME}-max-count=
can be set to define an upper bound on the number of cache entries in the specified cache.
1.14.49. The https-trust-store-* options have been undeprecated
Based on the community feedback, we decided to undeprecate https-trust-store-*
options to allow better granularity in trusted certificates.
1.15. Adapter support
At this version of Red Hat build of Keycloak, the following adapters are supported:
- JavaScript adapter: 26.0.12
- Node.js adapter: 26.0.11
- JBoss EAP OpenID Connect adapter: 8.0
- Keycloak SAML Adapter RPM for JBoss EAP: 8.0
1.16. Deprecated features
In previous sections, some features have already been mentioned as deprecated. The following sections provide details on other deprecated features.
1.16.1. Resteasy util class is deprecated
org.keycloak.common.util.Resteasy
has been deprecated. You should use the org.keycloak.util.KeycloakSessionUtil
to obtain the KeycloakSession
instead.
It is highly recommended to avoid obtaining the KeycloakSession
by means other than when creating your custom provider.
1.16.2. Property origin in the UserRepresentation is deprecated
The origin
property in the UserRepresentation
is deprecated and planned to be removed in a future release.
Instead, prefer using the federationLink
property to obtain the provider to which a user is linked with.
1.16.3. Deprecations in keycloak-common module
The following items have been deprecated for removal in upcoming Red Hat build of Keycloak versions with no replacement:
-
org.keycloak.common.util.reflections.Reflections.newInstance(java.lang.Class<T>)
-
org.keycloak.common.util.reflections.Reflections.newInstance(java.lang.Class<?>, java.lang.String)
-
org.keycloak.common.util.reflections.SetAccessiblePrivilegedAction
-
org.keycloak.common.util.reflections.UnSetAccessiblePrivilegedAction
1.16.4. Deprecations in keycloak-services module
The class UserSessionCrossDCManager
is deprecated and planned to be removed in a future version of Red Hat build of Keycloak. Read the UserSessionCrossDCManager
Javadoc for the alternative methods to use.
1.16.5. Deprecated Account REST endpoint for removing credential
The Account REST endpoint for removing the credential of the user is deprecated. Starting at this version, the Account Console no longer uses this endpoint. It is replaced by the Delete Credential
application-initiated.
1.16.6. Deprecated keycloak login Theme
The keycloak
login theme has been deprecated in favor of the new keycloak.v2
and will be removed in a future version. While it remains the default for the new realms for compatibility reasons, it is strongly recommended to switch all the realm themes to keycloak.v2
.
1.16.7. Method encode deprecated on PasswordHashProvider
Method String encode(String rawPassword, int iterations)
on the interface org.keycloak.credential.hash.PasswordHashProvider
is deprecated. The method will be removed in one of the future Red Hat build of Keycloak releases.
1.16.8. Deprecated theme variables
The following variables were deprecated in the Admin theme and will be removed in a future version:
-
authServerUrl
. UseserverBaseUrl
instead. -
authUrl
. UseadminBaseUrl
instead.
The following variables were deprecated in the Account theme and will be removed in a future version:
-
authServerUrl
. UseserverBaseUrl
instead, noteserverBaseUrl
does not include trailing slash. -
authUrl
. UseserverBaseUrl
instead, noteserverBaseUrl
does not include trailing slash.
1.16.9. Methods to get and set current refresh token in client session are now deprecated
The methods String getCurrentRefreshToken()
, void setCurrentRefreshToken(String currentRefreshToken)
, int getCurrentRefreshTokenUseCount()
, and void setCurrentRefreshTokenUseCount(int currentRefreshTokenUseCount)
in the interface org.keycloak.models.AuthenticatedClientSessionModel
are deprecated. They have been replaced by similar methods that require an identifier as a parameter such as getRefreshToken(String reuseId)
to manage multiple refresh tokens within a client session. The methods will be removed in one of the future Red Hat build of Keycloak releases.
1.17. Removed features
In previous sections, some features have already been mentioned as removed. The following sections provide details on other removed features.
1.17.1. Support for the UMD distribution removed
The UMD distribution Universal Module Definition of the Keycloak JS library has been removed. This means that the library is no longer exposed as a global variable, and instead must be imported as a module. This change is in line with modern JavaScript development practices, and allows for a more consitent experience between browsers and build tooling, and generally results in more predictable code with less side-effects.
If you are using a bundler such as Vite or Webpack nothing changes, you’ll have the same experience as before. If you are using the library directly in the browser, you’ll need to update your code to import the library as a module:
<!-- Before -->
<script src="/path/to/keycloak.js"></script>
<script>
const keycloak = new Keycloak();
</script>
<!-- After -->
<script type="module">
import Keycloak from '/path/to/keycloak.js';
const keycloak = new Keycloak();
</script>
You can also opt to use an import map make the import of the library less verbose:
<script type="importmap">
{
"imports": {
"keycloak-js": "/path/to/keycloak.js"
}
}
</script>
<script type="module">
// The library can now be imported without specifying the full path, providing a similar experience as with a bundler.
import Keycloak from 'keycloak-js';
const keycloak = new Keycloak();
</script>
If you are using TypeScript you may need to update your tsconfig.json
to be able to resolve the library:
{
"compilerOptions": {
"moduleResolution": "Bundler"
}
}
1.17.2. CollectionUtil intesection method removed
The method org.keycloak.common.util.CollectionUtil.intersection
has been removed. You should use the 'java.util.Collection.retainAll' instead on an existing collection.
1.17.3. Account Console v2 theme removed
The Account Console v2 theme has been removed from Red Hat build of Keycloak. This theme was deprecated in Red Hat build of Keycloak 24 and replaced by the Account Console v3 theme. If you are still using this theme, you should migrate to the Account Console v3 theme.
1.17.4. Original host name options were removed
These options were replaced by new options referred to as Hostname v2. For more details, see Configuring the hostname (v2) and New hostname options.
1.17.5. Proxy option removed
The proxy
option was deprecated in Red Hat build of Keycloak 24 and was replaced by the proxy-headers
option in combination with hostname options as needed. For more details, see Using a reverse proxy.
1.17.6. Most Java adapters removed
Most Java adapters are now removed from the Red Hat build of Keycloak codebase and downloads pages.
-
For OAuth 2.0/OIDC, this includes removal of the EAP adapter, Servlet Filter adapter,
KeycloakInstalled
desktop adapter, thejaxrs-oauth-client
adapter, JAAS login modules, Spring adapter and SpringBoot adapters. - For SAML, this includes removal of the Servlet filter adapter. SAML adapters are still supported with JBoss EAP.
- The generic Authorization Client library is still supported. You can use it in combination with any other OAuth 2.0 or OpenID Connect libraries. You can check the quickstarts for some examples where this authorization client library is used together with the 3rd party Java adapters like Elytron OIDC or SpringBoot. You can check the quickstarts also for the example of SAML adapter used with WildFly.
1.17.7. OSGi metadata removed
Since all of the Java adapters that used OSGi metadata have been removed, OSGi metadata are no longer generated for our jars.
1.17.8. Legacy cookies removed
Red Hat build of Keycloak no longer sends _LEGACY
cookies, which where introduced as a work-around to older browsers not supporting the SameSite
flag on cookies.
The _LEGACY
cookies also served another purpose, which was to allow login from an insecure context. Although an insecure context is never recommended in production deployments of Red Hat build of Keycloak, it is fairly frequent to access Red Hat build of Keycloak over http
outside of localhost
. As an alternative to the _LEGACY
cookies, Red Hat build of Keycloak no longer sets the secure
flag; but it does set SameSite=Lax
instead of SameSite=None
when it detects an insecure context is used.
1.17.9. EnvironmentDependentProviderFactory removed
The method EnvironmentDependentProviderFactory.isSupported()
was deprecated for several releases and has now been removed.
Instead, implement isSupported(Config.Scope config)
.
1.17.10. Support for legacy redirect_uri parameter and SPI options are removed
Previous versions of Red Hat build of Keycloak had supported automatic logout of the user and redirecting to the application by opening logout endpoint URL such as http(s)://example-host/auth/realms/my-realm-name/protocol/openid-connect/logout?redirect_uri=encodedRedirectUri
. This functionality was deprecated in Red Hat build of Keycloak 18 and has been removed in this version in favor of following the OpenID Connect specification.
As part of this change the following related configuration options for the SPI have been removed:
-
--spi-login-protocol-openid-connect-legacy-logout-redirect-uri
-
--spi-login-protocol-openid-connect-suppress-logout-confirmation-screen
If you were still making use these options or the redirect_uri
parameter for logout you should implement the OpenID Connect RP-Initiated Logout specification instead.
1.17.11. org.keycloak:keycloak-model-legacy removed
The module org.keycloak:keycloak-model-legacy
module was deprecated in a previous release and is removed in this release. Use the org.keycloak:keycloak-model-storage
module instead.
1.17.12. Offline session preloading removed
The old behavior to preload offline sessions at startup is now removed after it has been deprecated in the previous release.
1.17.13. setOrCreateChild() method removed from JavaScript Admin Client
The groups.setOrCreateChild()
method has been removed from that JavaScript-based Admin Client. If you are still using this method, start using the createChildGroup()
or updateChildGroup()
methods instead.
1.17.14. Removed session_state claim
The session_state
claim, which contains the same value as the sid
claim, is now removed from all tokens as it is not required according to the OpenID Connect Front-Channel Logout and OpenID Connect Back-Channel Logout specifications. The session_state
claim remains present in the Access Token Response in accordance with OpenID Connect Session Management specification.
Note that the setSessionState()
method is also removed from the IDToken
class in favor of the setSessionId()
method, and the getSessionState()
method is now deprecated.
A new Session State (session_state)
mapper is also included and can be assigned to client scopes (for instance basic
client scope) to revert to the old behavior.
If an old version of the JS adapter is used, the Session State (session_state)
mapper should also be used by using client scopes as described above.
1.17.15. Grace period for idle sessions removed when persistent sessions are enabled
Previous versions of Red Hat build of Keycloak added a grace period of two minutes to idle times of user and client sessions. This was added due to a previous architecture where session refresh times were replicated asynchronously in a cluster. With persistent user sessions, this is no longer necessary, and therefore the grace period is now removed.
To keep the old behavior, update your realm configuration and extend the session and client idle times by two minutes.
1.17.16. Adapter and misc BOM files removed
The org.keycloak.bom:keycloak-adapter-bom
and org.keycloak.bom:keycloak-misc-bom
BOM files are removed. The adapter BOM was no longer useful because most of the Java adapters are removed. The misc BOM had contained only one artifact, keycloak-test-helper
, and that artifact is also removed in this release.
1.17.17. keycloak-test-helper removed
The maven artifact org.keycloak:keycloak-test-helper
is removed in this release. The artifact provided a few helper methods for dealing with a Java admin client. If you use the helper methods, it is possible to fork them into your application if needed.
1.17.18. JEE admin-client removed
The JEE admin-client is removed in this release, however, the Jakarta admin-client is still supported.
1.17.19. Deprecated methods from certain classes removed
The following methods were removed from the AccessToken
class:
-
expiration
. Use theexp
method instead. -
notBefore
. Use thenbf
method instead. -
issuedAt
. Use theiat
method instead.
The following methods were removed from the IDToken
class:
-
getAuthTime
andsetAuthTime
. Use thegetAuth_time
andsetAuth_time
methods, respectively. -
notBefore
. Use thenbf
method instead. -
issuedAt
. Use theiat
method instead. -
setSessionState
. Use thesetSessionId
method instead (See the details above in the section aboutsession_state
claim)
The following methods were removed from the JsonWebToken
class:
-
expiration
. Use theexp
method instead. -
notBefore
. Use thenbf
method instead. -
issuedAt
. Use theiat
method instead.
You should also expect both exp
and nbf
claims not set in tokens as they are optional. Previously, these claims were being set with a value of 0
what does not make mush sense because their value should be a valid NumericDate
.
1.17.20. Deprecated cookie methods removed
The following APIs for setting custom cookies have been removed:
-
ServerCookie
- replaced byNewCookie.Builder
-
LocaleSelectorProvider.KEYCLOAK_LOCALE
- replaced byCookieType.LOCALE
-
HttpCookie
- replaced byNewCookie.Builder
-
HttpResponse.setCookieIfAbsent(HttpCookie cookie)
- replaced byHttpResponse.setCookieIfAbsent(NewCookie cookie)
1.17.21. Deprecated LinkedIn provider removed
In version 22.0, the OAuh 2.0 social provider for LinkedIn was replaced by a new OpenId Connect implementation. The legacy provider was deprecated but not removed, just in case it was still functional in some existing realms. Red Hat build of Keycloak 26 is removing the old provider and its associated linkedin-oauth
feature. From now on, the default LinkedIn
social provider is the only option available.
1.18. Fixed issues
Each release includes fixed issues:
- Red Hat build of Keycloak 26.0.17 fixed Issues
- Red Hat build of Keycloak 26.0.16 fixed Issues
- Red Hat build of Keycloak 26.0.15 fixed Issues
- Red Hat build of Keycloak 26.0.14 fixed Issues
- Red Hat build of Keycloak 26.0.13 fixed Issues
- Red Hat build of Keycloak 26.0.12 fixed Issues
- Red Hat build of Keycloak 26.0.11 fixed Issues
- Red Hat build of Keycloak 26.0.10 fixed Issues
- Red Hat build of Keycloak 26.0.9 fixed Issues
- Red Hat build of Keycloak 26.0.8 fixed Issues
- Red Hat build of Keycloak 26.0.7 fixed Issues
- Red Hat build of Keycloak 26.0.6 fixed Issues
- Red Hat build of Keycloak 26.0.x fixed issues.
1.19. Supported configurations
For the supported configurations for Red Hat build of Keycloak 26.0, see Supported configurations.
1.20. Component details
For the list of supported component versions for Red Hat build of Keycloak 26.0, see Component details.
