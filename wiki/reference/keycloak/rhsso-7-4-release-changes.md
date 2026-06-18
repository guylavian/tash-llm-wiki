---
title: "Chapter 2. Changes - Red Hat Single Sign-On 7.4 Upgrading Guide"
type: reference
domain: keycloak
slug: rhsso-7-4-release-changes
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.4/html/upgrading_guide/release_changes
guide: upgrading_guide
version: 7.4
family: rhsso
documentKind: "Documentation"
---

# Chapter 2. Changes - Red Hat Single Sign-On 7.4 Upgrading Guide

Chapter 2. Changes
Review these changes carefully before upgrading.
2.1. RH SSO 7.4
The following changes have occurred from Red Hat Single Sign-On 7.3 to Red Hat Single Sign-On 7.4.
2.1.1. Upgrade to EAP 7.3
The Red Hat Single Sign-On server was upgraded to use EAP 7.3 as the underlying container. This change does not directly involve any specific Red Hat Single Sign-On server functionality, but a few changes relate to the migration.
2.1.1.1. Dependency updates
The dependencies were updated to the versions used by EAP 7.3 server. For example, the Infinispan component version is now 9.3.1.Final.
2.1.1.2. Configuration changes
There are a few configuration changes in the standalone(-ha).xml and domain.xml files. Follow the Upgrading the Red Hat Single Sign-On server section to handle the migration of configuration files automatically.
2.1.1.3. Cross-Datacenter replication changes
You will need to upgrade RHDG to version 7.3. The older version may still work, but it is not tested so it is not guaranteed to work.
2.1.2. Authentication flows changes
We did some refactoring and improvements related to the authentication flows, which requires attention during migration.
2.1.2.1. REQUIRED and ALTERNATIVE executions not supported at same authentication flow
Previously, it was possible to have REQUIRED and ALTERNATIVE executions in the same authentication flow at the same level. There were some issues with this approach and we did the refactoring in the Authentication SPI, which means that this is no longer valid. If ALTERNATIVE and REQUIRED executions are configured at the same level, the ALTERNATIVE executions are considered disabled.
So when migrating to this version, your existing authentication flows will be migrated but retain the behavior of the previous version. If an authentication flow contains ALTERNATIVE executions at the same level as REQUIRED executions, the ALTERNATIVE executions are added to the separate REQUIRED subflow.
This strategy should ensure the same or similar behavior of the each authentication flow as in the previous version. However, you may review the configuration of your authentication flow and double check that it works as expected. This recommendation applies in particular for customized authentication flows with custom authenticator implementations.
2.1.2.2. OPTIONAL execution requirement removed
Regarding migration, the most important change is removing support for the OPTIONAL requirement from authentication executions and replacing it with the CONDITIONAL requirement, which allows more flexibility.
OPTIONAL authenticators configured in the previous version are replaced with the CONDITIONAL subflows. These subflows have the Condition - User Configured condition configured as first execution, and the previously OPTIONAL authenticator (for example OTP Form) as second execution. For the user, the behavior during authentication matches the behavior of the previous version.
2.1.2.3. SPI Changes
Some changes exist in the Java Authentication SPI and Credential Provider SPI.
The interface Authenticator is not changed, but you may be affected if you develop advanced authenticators that introduce some new credential types (subclasses of CredentialModel). Changes exist on the CredentialProvider interface and introduction of some new interfaces such as CredentialValidator.
Also, you may be affected if your authenticator supported the OPTIONAL execution requirement. It is recommended that you double check the latest authentication examples in the server development guide for more details.
2.1.2.4. Freemarker template changes
Changes exist in the freemarker templates. You may be affected if you have your own theme with custom freemarker templates for login forms or some account forms, especially for the forms related to OTP. We recommend that you review the changes in the Freemarker templates in this version and align your templates according to it.
2.1.3. Duplicated top level groups
This release fixes a problem that could create duplicated top level groups in the realm. Nevertheless the existence of previous duplicated groups makes the upgrade process fail. The Red Hat Single Sign-On server can be affected by this issue if it is using a H2, MariaDB, MySQL or PostgreSQL database. Before launching the upgrade, check if the server contains duplicated top level groups. For example the following SQL query can be executed at database level to list them:
SELECT REALM_ID, NAME, COUNT(*) FROM KEYCLOAK_GROUP WHERE PARENT_GROUP is NULL GROUP BY REALM_ID, NAME HAVING COUNT(*) > 1;
Only one top level group can exist in each realm with the same name. Duplicates should be reviewed and deleted before the upgrade. The error in the upgrade contains the message Change Set META-INF/jpa-changelog-9.0.1.xml::9.0.1- KEYCLOAK-12579-add-not-null-constraint::keycloak failed.
2.1.4. User credentials changes
We added more flexibility around storing user credentials. Among other things, every user can have multiple credentials of the same type, such as multiple OTP credentials. Some changes exist in the database schema in relation to that, however the credentials from the previous version are updated to the new format. Users can still log in with the passwords or OTP credentials defined in the previous version.
2.1.5. New optional client scope
We have added a microprofile-jwt optional client scope to handle the claims defined in the MicroProfile/JWT Auth Specification. This new client scope defines protocol mappers to set the username of the authenticated user to the upn claim and to set the realm roles to the groups claim.
2.1.6. Improved handling of user locale
A number of improvements have been made to how the locale for the login page is selected, as well as when the locale is updated for a user. See the Server Administration Guide for more details.
2.1.7. Legacy promise in JavaScript adapter
You no longer need to set promiseType in the JavaScript adapter, and both are available at the same time. It is recommended to update applications to use native promise API (then and catch) as soon as possible, as the legacy API (success and error) will be removed at some point.
2.1.8. Deploying Scripts to the Server
Until now, administrators were allowed to upload scripts to the server through the Red Hat Single Sign-On Admin Console and the RESTful Admin API. This capability is now disabled. Users should deploy scripts directly to the server. For more details, review the JavaScript Providers.
2.1.9. Client Credentials in the JavaScript adapter
In the previous releases, developers were allowed to provide client credentials to the JavaScript adapter. For now on, this capability was removed, because client-side apps are not safe to keep secrets. Ability to propagate prompt=none to default IDP
We have added a switch in the OIDC identity provider configuration named Accepts prompt=none forward from client to identify IDPs that are able to handle forwarded requests that include the prompt=none query parameter.
Until now, when receiving an auth request with prompt=none, a realm would return a login_required error if the user is not authenticated in the realm without checking if the user has been authenticated by an IDP. From now on, if a default IDP can be determined for the auth request (either by the use of the kc_idp_hint query param or by setting up a default IDP for the realm) and if the Accepts prompt=none forward from client switch has been enabled for the IDP, the auth request is forwarded to the IDP to check if the user has been authenticated there.
It is important to note that this switch is only taken into account if a default IDP is specified, in which case we know where to forward the auth request without having to prompt the user to select an IDP. If a default IDP cannot be determined, we cannot assume which one will be used to fulfill the auth request so the request forwarding is not performed.
2.1.10. New Default Hostname provider
The request and fixed hostname providers have been replaced with a new default hostname provider. The request and fixed hostname providers are now deprecated and we recommend that you switch to the default hostname provider as soon as possible.
2.1.11. Deprecated or removed features
Certain features have a change in status.
2.1.11.1. Deprecated methods in token representation Java classes
In the year 2038, an int is no longer able to hold the value of seconds since 1970, as such we are working on updating these to long values. In token representation there is a further issue. An int will by default result in 0 in the JSON representation, while it should not be included.
See the JavaDocs Documentation for further details on exact methods that have been deprecated and replacement methods.
2.1.11.2. Uploading scripts
Upload of scripts through admin rest endpoints/console is deprecated. It will be removed at a future release.
2.1.12. Authorization Services Drools Policy
The Authorization Services Drools Policy has been removed.
2.1.13. Changes of default configuration values
- Reduced default HTTP socket read timeout
- The default read timeout for the HTTP and HTTPS listeners has been reduced from 120 to 30 seconds.
- Increased default JDBC connection pool size
- The default connection pool size of the default H2 JDBC datasource has been increased from 20 to 100 connections. It is recommended to set a sufficient pool size for the production datasource as well.
2.1.13.1. Upgrading Configuration
The configuration changes affect standalone(-ha).xml and domain.xml files. Follow the Upgrading the Red Hat Single Sign-On server section to handle the migration of configuration files automatically.
2.1.13.2. Client Credentials Grant without refresh token by default
From this Red Hat Single Sign-On version, the OAuth2 Client Credentials Grant endpoint does not issue refresh tokens by default. This behavior is aligned with the OAuth2 specification. As a side-effect of this change, there is no user session created on the Red Hat Single Sign-On server side after successful Client Credentials authentication, which results in improved performance and memory consumption. Clients that use Client Credentials Grant are encouraged to stop using refresh tokens and instead always authenticate at every request with grant_type=client_credentials
instead of using refresh_token
as grant type. In relation to this situation, Red Hat Single Sign-On has support for revocation of access tokens in the OAuth2 Revocation Endpoint, hence clients are allowed to revoke individual access tokens if needed.
For the backwards compatibility, there is a possibility to stick to the behavior of old versions. When this option is used, the refresh token will be still issued after a successful authentication with the Client Credentials Grant and also the user session will be created. This capability can be enabled for the particular client in the Red Hat Single Sign-On admin console, in client details in the section with OpenID Connect Compatibility Modes
with the switch Use Refresh Tokens For Client Credentials Grant
.
2.1.13.3. Valid Request URIs
If you use the OpenID Connect parameter request_uri
, a requirement exists that your client needs to have Valid Request URIs
configured. This parameter can be configured through the admin console on the client details page or through the admin REST API or client registration API. Valid Request URIs need to contain the list of Request URI values that are permitted for the particular client. This is to avoid SSRF attacks. There is a possibility to use wildcards or relative paths similarly such as the Valid Redirect URIs
option, however for security purposes, we typically recommend to use as specific value as possible.
2.2. RH-SSO 7.3
The following changes have occurred from RH-SSO 7.2 to RH-SSO 7.3.
2.2.1. Changes to Authorization Services
We added support for UMA 2.0. This version of the UMA specification introduced some important changes on how permissions are obtained from the server.
Here are the main changes introduced by UMA 2.0 support. See Authorization Services Guide for details.
- Authorization API was removed
- Prior to UMA 2.0 (UMA 1.0), client applications were using the Authorization API to obtain permissions from the server in the format of a RPT. The new version of UMA specification has removed the Authorization API which was also removed from Red Hat Single Sign-On. In UMA 2.0, RPTs can now be obtained from the token endpoint by using a specific grant type. See Authorization Services Guide for details.
- Entitlement API was removed
- With the introduction of UMA 2.0, we decided to leverage the token endpoint and UMA grant type to allow obtaining RPTs from Red Hat Single Sign-On and avoid having different APIs. The functionality provided by the Entitlement API was kept the same and is still possible to obtain permissions for a set of one or more resources and scopes or all permissions from the server in case no resource or scope is provided. See Authorization Services Guide for details.
- Changes to UMA Discovery Endpoint
- UMA Discovery document changed, see Authorization Services Guide for details.
- Changes to Red Hat Single Sign-On Authorization JavaScript Adapter
The Red Hat Single Sign-On Authorization JavaScript Adapter (keycloak-authz.js) changed in order to comply with the changes introduced by UMA 2.0 while keeping the same behavior as before. The main change is on how you invoke both
authorization
andentitlement
methods which now expect a specific object type representing an authorization request. This new object type provides more flexibility on how permissions can be obtained from the server by supporting the different parameters supported by the UMA grant type. See Authorization Services Guide for details.One of the main changes introduced by this release is that you are no longer required to exchange access tokens with RPTs in order to access resources protected by a resource server (when not using UMA). Depending on how the policy enforcer is configured on the resource server side, you can just send regular access tokens as a bearer token and permissions will still be enforced.
- Changes to Red Hat Single Sign-On Authorization Client Java API
-
When upgrading to the new version of Red Hat Single Sign-On Authorization Client Java API, you’ll notice that some representation classes were moved to a different package in
org.keycloak:keycloak-core
.
2.2.2. Client Templates changed to Client Scopes
We added support for Client Scopes, which requires some attention during migration.
- Client Templates changed to Client Scopes
- Client Templates were changed to Client Scopes. If you had any Client Templates, their protocol mappers and role scope mappings will be preserved.
- Spaces replaced in the names
-
Client templates with the space character in the name were renamed by replacing spaces with an underscore, because spaces are not allowed in the name of client scopes. For example, a client template
my template
will be changed to client scopemy_template
. - Linking Client Scopes to Clients
-
For clients which had the client template, the corresponding client scope is now added as
Default Client Scope
to the client. So protocol mappers and role scope mappings will be preserved on the client. - Realm Default Client Scopes not linked with existing clients
-
During the migration, the list of built-in client scopes is added to each realm as well as list of
Realm Default Client Scopes
. However, existing clients are NOT upgraded and new client scopes are NOT automatically added to them. Also all the protocol mappers and role scope mappings are kept on existing clients. In the new version, when you create a new client, it automatically has Realm Default Client Scopes attached to it and it does not have any protocol mappers attached to it. We did not change existing clients during migration as it would be impossible to properly detect customizations, which you will have for protocol mappers of the clients, for example. If you want to update existing clients (remove protocol mappers from them and link them with client scopes), you will need to do it manually. - Consents need to be confirmed again
- The client scopes change required the refactoring of consents. Consents now point to client scopes, not to roles or protocol mappers. Because of this change, the previously confirmed persistent consents by users are not valid anymore and users need to confirm the consent page again after the migration.
- Some configuration switches removed
-
The switch
Scope Param Required
was removed from Role Detail. The switchesConsent Required
andConsent Text
were removed from the Protocol Mapper details. Those switches were replaced by the Client Scope feature.
2.2.3. New default client scopes
We have added new realm default client scopes roles
and web-origins
. These client scopes contain protocol mappers to add the roles of the user and allowed web origins to the token. During migration, these client scopes should be automatically added to all the OpenID Connect clients as default client scopes. Hence no setup should be required after database migration is finished.
2.2.3.1. Protocol mapper SPI addition
Related to this, there is a small addition in the (unsupported) Protocol Mappers SPI. You can be affected only if you implemented a custom ProtocolMapper. There is a new getPriority()
method on the ProtocolMapper interface. The method has the default implementation set to return 0. If your protocol mapper implementation relies on the roles in the access token realmAccess
or resourceAccess
properties, you may need to increase the priority of your mapper.
2.2.3.2. Audience resolving
Audiences of all the clients, for which authenticated user has at least one client role in the token, are automatically added to the aud
claim in the access token now. On the other hand, an access token may not automatically contain the audience of the frontend client, for which it was issued. Read the Server Administration Guide for more details.
2.2.4. Upgrade to EAP 7.2
The Red Hat Single Sign-On server was upgraded to use EAP 7.2 as the underlying container. This does not directly involve any specific Red Hat Single Sign-On server functionality, but there are few changes related to the migration, which worth mentioning.
- Dependency updates
- The dependencies were updated to the versions used by EAP 7.2 server. For example, Infinispan is now 9.3.1.Final.
- Configuration changes
-
There are few configuration changes in the
standalone(-ha).xml
anddomain.xml
files. You should follow the Section 3.1.2, “Upgrading Red Hat Single Sign-On server” section to handle the migration of configuration files automatically. - Cross-Datacenter Replication changes
- You will need to upgrade RHDG server to version 7.3. The older version may still work, but it is not guaranteed as we don’t test it anymore.
-
There is a need to add
protocolVersion
property with the value2.6
to the configuration of theremote-store
element in the Red Hat Single Sign-On configuration. This is required as there is a need to downgrade the version of HotRod protocol to be compatible with the version used by RHDG 7.3.
2.2.5. Hostname configuration
In previous versions it was recommended to use a filter to specify permitted hostnames. It is now possible to set a fixed hostname which makes it easier to make sure the valid hostname is used and also allows internal applications to invoke Red Hat Single Sign-On through an alternative URL, for example an internal IP address. It is recommended that you switch to this approach in production.
2.2.6. JavaScipt Adapter Promise
To use native JavaScript promise with the JavaScript adapter it is now required to set promiseType
to native
in the init options.
In the past if native promise was available a wrapper was returned that provided both the legacy Keycloak promise and the native promise. This was causing issues as the error handler was not always set prior to the native error event, which resulted in Uncaught (in promise)
error.
2.2.7. Microsoft Identity Provider updated to use the Microsoft Graph API
The Microsoft Identity Provider implementation in Red Hat Single Sign-On used to rely on the Live SDK endpoints for authorization and obtaining the user profile. From November 2018 onwards, Microsoft is removing support for the Live SDK API in favor of the new Microsoft Graph API. The Red Hat Single Sign-On identity provider has been updated to use the new endpoints so if this integration is in use make sure you upgrade to the latest Red Hat Single Sign-On version.
Legacy client applications registered under "Live SDK applications" won’t work with the Microsoft Graph endpoints due to changes in the id format of the applications. If you run into an error saying that the application identifier was not found in the directory, you will have to register the client application again in the Microsoft Application Registration portal to obtain a new application id.
2.2.8. Google Identity Provider updated to use Google Sign-in authentication system
The Google Identity Provider implementation in Red Hat Single Sign-On used to rely on the Google+ API endpoints endpoints for authorization and obtaining the user profile. From March 2019 onwards, Google is removing support for the Google+ API in favor of the new Google Sign-in authentication system. The Red Hat Single Sign-On identity provider has been updated to use the new endpoints so if this integration is in use make sure you upgrade to the latest Red Hat Single Sign-On version.
If you run into an error saying that the application identifier was not found in the directory, you will have to register the client application again in the Google API Console portal to obtain a new application id and secret.
It is possible that you will need to adjust custom mappers for non-standard claims that were provided by Google+ user information endpoint and are provided under different name by Google Sign-in API. Please consult Google documentation for the most up-to-date information on available claims.
2.2.9. LinkedIn Social Broker Updated to Version 2 of LinkedIn APIs
Accordingly with LinkedIn, all developers need to migrate to version 2.0 of their APIs and OAuth 2.0. As such, we have updated our LinkedIn Social Broker.
Existing deployments using this broker may start experiencing errors when fetching user’s profile using version 2 of LinkedIn APIs. This error may be related with the lack of permissions granted to the client application used to configure the broker which may not be authorized to access the Profile API or request specific OAuth2 scopes during the authentication process.
Even for newly created LinkedIn client applications, you need to make sure that the client is able to request the r_liteprofile
and r_emailaddress
OAuth2 scopes, at least, as well that the client application can fetch current member’s profile from the https://api.linkedin.com/v2/me
endpoint.
Due to these privacy restrictions imposed by LinkedIn in regards to access to member’s information and the limited set of claims returned by the current member’s Profile API, the LinkedIn Social Broker is now using the member’s email address as the default username. That means that the r_emailaddress
is always set when sending authorization requests during the authentication.
2.3. RH-SSO 7.2
The following changes have occurred from RH-SSO 7.1 to RH-SSO 7.2.
2.3.1. New Password Hashing algorithms
We have added two new password hashing algorithms (pbkdf2-sha256 and pbkdf2-sha512). New realms will use the pbkdf2-sha256 hashing algorithm with 27500 hashing iterations. Since pbkdf2-sha256 is slightly faster than pbkdf2 the iterations was increased to 27500 from 20000.
Existing realms are upgraded if the password policy contains the default value for the hashing algorithm (not specified) and iteration (20000). If you have changed the hashing iterations, you need to manually change to pbkdf2-sha256 if you’d like to use the more secure hashing algorithm.
2.3.2. ID Token requires scope=openid
In RH-SSO 7.0, the ID Token was returned regardless if scope=openid
query parameter was present or not in authorization request. This is incorrect according to the OpenID Connect specification.
In RH-SSO 7.1, we added this query parameter to adapters, but left the old behavior to accommodate migration.
In RH-SSO 7.2, this behavior has changed and the scope=openid
query parameter is now required to mark the request as an OpenID Connect request. If this query parameter is omitted the ID Token will not be generated.
2.3.3. Microsoft SQL Server requires extra dependency
Microsoft JDBC Driver 6.0 requires additional dependency added to the JDBC driver module. If you observe an NoClassDefFoundError
error when using Microsoft SQL Server please add the following dependency to your JDBC driver module.xml
file:
<module name="javax.xml.bind.api"/>
2.3.4. Added session_state parameter to OpenID Connect Authentication Response
The OpenID Connect Session Management specification requires that the parameter session_state
is present in the OpenID Connect Authentication Response.
In RH-SSO 7.1, we did not have this parameter, but now Red Hat Single Sign-On adds this parameter by default, as required by the specification.
However, some OpenID Connect / OAuth2 adapters, and especially older Red Hat Single Sign-On adapters (such as RH-SSO 7.1 and older), may have issues with this new parameter.
For example, the parameter will be always present in the browser URL after successful authentication to the client application. If you use RH-SSO 7.1 or a legacy OAuth2 / OpenID Connect adapter, it may be useful to disable adding the session_state
parameter to the authentication response. This can be done for the particular client in the Red Hat Single Sign-On admin console, in client details in the section with OpenID Connect Compatibility Modes
, described in Section 4.1, “Compatibility with older adapters”. There is the Exclude Session State From Authentication Response
switch, which can be turned on to prevent adding the session_state
parameter to the Authentication Response.
2.3.5. Microsoft Identity Provider updated to use the Microsoft Graph API
The Microsoft Identity Provider implementation in Red Hat Single Sign-On up to version 7.2.4 relies on the Live SDK endpoints for authorization and obtaining the user profile. From November 2018 onwards, Microsoft is removing support for the Live SDK API in favor of the new Microsoft Graph API. The Red Hat Single Sign-On identity provider has been updated to use the new endpoints so if this integration is in use make sure you upgrade to Red Hat Single Sign-On version 7.2.5 or later.
Legacy client applications registered under "Live SDK applications" won’t work with the Microsoft Graph endpoints due to changes in the id format of the applications. If you run into an error saying that the application identifier was not found in the directory, you will have to register the client application again in the Microsoft Application Registration portal to obtain a new application id.
2.3.6. Google Identity Provider updated to use Google Sign-in authentication system
The Google Identity Provider implementation in Red Hat Single Sign-On up to version 7.2.5 relies on the Google+ API endpoints endpoints for authorization and obtaining the user profile. From March 2019 onwards, Google is removing support for the Google+ API in favor of the new Google Sign-in authentication system. The Red Hat Single Sign-On identity provider has been updated to use the new endpoints so if this integration is in use make sure you upgrade to Red Hat Single Sign-On version 7.2.6 or later.
If you run into an error saying that the application identifier was not found in the directory, you will have to register the client application again in the Google API Console portal to obtain a new application id and secret.
It is possible that you will need to adjust custom mappers for non-standard claims that were provided by Google+ user information endpoint and are provided under different name by Google Sign-in API. Please consult Google documentation for the most up-to-date information on available claims.
2.3.7. LinkedIn Social Broker Updated to Version 2 of LinkedIn APIs
Accordingly with LinkedIn, all developers need to migrate to version 2.0 of their APIs and OAuth 2.0. As such, we have updated our LinkedIn Social Broker so if this integration is in use make sure you upgrade to Red Hat Single Sign-On version 7.2.6 or later.
Existing deployments using this broker may start experiencing errors when fetching user’s profile using version 2 of LinkedIn APIs. This error may be related with the lack of permissions granted to the client application used to configure the broker which may not be authorized to access the Profile API or request specific OAuth2 scopes during the authentication process.
Even for newly created LinkedIn client applications, you need to make sure that the client is able to request the r_liteprofile
and r_emailaddress
OAuth2 scopes, at least, as well that the client application can fetch current member’s profile from the https://api.linkedin.com/v2/me
endpoint.
Due to these privacy restrictions imposed by LinkedIn in regards to access to member’s information and the limited set of claims returned by the current member’s Profile API, the LinkedIn Social Broker is now using the member’s email address as the default username. That means that the r_emailaddress
is always set when sending authorization requests during the authentication.
2.4. RH-SSO 7.1
The following changes have occurred from RH-SSO 7.0 to RH-SSO 7.1.
2.4.1. Realm Keys
For RH-SSO 7.0, only one set of keys could be associated with a realm. This meant that when changing the keys, all current cookies and tokens would be invalidated and all users would have to re-authenticate. For RH-SSO 7.1, support for multiple keys for one realm has been added. At any given time, one set of keys is the active set used for creating signatures, but there can be multiple keys used to verify signatures. This means that old cookies and tokens can be verified, then refreshed with the new signatures, allowing users to remain authenticated when keys are changed. There are also some changes to how keys are managed through the Admin Console and Admin REST API; for more details see Realm Keys in the Server Administration Guide.
To allow seamless key rotation you must remove hard-coded keys from client adapters. The client adapters will automatically retrieve keys from the server as long as the realm key is not specified. Client adapters will also retrieve new keys automatically when keys are rotated.
2.4.2. Client Redirect URI Matching
For RH-SSO 7.0, query parameters are ignored when matching valid redirect URIs for a client. For RH-SSO 7.1, query parameters are no longer ignored. If you need to include query parameters in the redirect URI you must specify the query parameters in the valid redirect URI for the client (for example, https://hostname/app/login?foo=bar) or use a wildcard (for example, https://hostname/app/login/*). Fragments are also no longer permitted in Valid Redirect URIs (that is, https://hostname/app#fragment).
2.4.3. Automatically Redirect to Identity Provider
For RH-SSO 7.1, identity providers cannot be set as the default authentication provider. To automatically redirect to an identity provider for RH-SSO 7.1, you must now configure the identity provider redirector. For more information see Default Identity Provider in the Server Administration Guide. If you previously had an identity provider with the default authentication provider option set, this value is automatically used as the value for the identity provider redirector when the server is upgraded to RH-SSO 7.1.
2.4.4. Admin REST API
For RH-SSO 7.0, paginated endpoints in the Admin REST API return all results if the maxResults query parameter was not specified. This could cause issues with a temporary high load and requests timing out when a large number of results were returned (for example, users). For RH-SSO 7.1, a maximum of 100 results are returned if a value for maxResults is not specified. You can return all results by specifying maxResults as -1.
2.4.5. Server Configuration
For RH-SSO 7.0, server configuration is split between the keycloak-server.json file and the standalone/domain.xml or domain.xml file. For RH-SSO 7.1, the keycloak-server.json file has been removed and all server configuration is done through the standalone.xml or domain.xml file. The upgrading procedure for RH-SSO 7.1 automatically migrates the server configuration from the keycloak-server.json file to the standalone.xml or domain.xml file.
2.4.6. Key Encryption Algorithm in SAML Assertions
For RH-SSO 7.1, keys in SAML assertions and documents are now encrypted using the RSA-OAEP encryption scheme. To use encrypted assertions, ensure your service providers support this encryption scheme. In the event that you have service providers that do not support RSA-OAEP, RH-SSO can be configured to use the legacy RSA-v1.5 encryption scheme by starting the server with the system property "keycloak.saml.key_trans.rsa_v1.5" set to true. If you do this, you should upgrade your service providers as soon as possible to be able to revert to the more secure RSA-OAEP encryption scheme.
