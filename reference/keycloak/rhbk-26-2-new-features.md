---
title: "Chapter 14. New features and enhancements - Red Hat build of Keycloak 26.2 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-2-new-features
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/release_notes/new_features
guide: release_notes
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "The following release notes apply to Red Hat build of Keycloak 26.2. This release includes several key features such as new support for fine-grained admin permissions and token exchange, rolling update, and many other features and improvements. 14.1. Fine-grained admin permissions This release introduces support for a new version of Fine-Grained Admin Permissions. Version 2 (V2) provides enhanced …"
---

# Chapter 14. New features and enhancements - Red Hat build of Keycloak 26.2 Release Notes

Chapter 15. New features and enhancements
The following release notes apply to Red Hat build of Keycloak 26.2. This release includes several key features such as new support for fine-grained admin permissions and token exchange, rolling update, and many other features and improvements.
15.1. Fine-grained admin permissions
This release introduces support for a new version of Fine-Grained Admin Permissions. Version 2 (V2) provides enhanced flexibility and control over administrative access within realms. With this feature, administrators can define permissions for administering users, groups, clients, and roles without relying on broad administrative roles. V2 offers the same level of access control over realm resources as the previous version, with plans to extend its capabilities in future versions. Some key points follow:
- Centralized Admin Console Management - New Permissions section was introduced to allow management from a single place without having to navigate to different places in the Admin Console.
- Resource-Specific and Global Permissions – Permissions can be defined for individual resources (such as, specific users or groups), or entire resource types (such as., all users or all groups).
- Explicit Operation Scoping – Permissions are now independent, removing hidden dependencies between operations. Administrators must assign each scope explicitly, making it easier to see what is granted without needing prior knowledge of implicit relationships.
- Per-Realm Enablement – Fine-Grained Admin Permissions can be enabled on a per-realm basis, allowing greater control over adoption and configuration.
For more details, see Fine-Grained Admin Permissions. For more information about migration, see the Upgrading Guide.
15.2. Standard token exchange support
This release introduces basic support for the standard token exchange. This feature is currently limited to exchanging the Internal token to internal token compliant with the Token exchange specification. Support is being planned to cover other use cases related to identity brokering or subject impersonation.
For more details, see Standard token exchange.
For information on how to upgrade from the legacy token exchange used in previous Red Hat build of Keycloak versions, see the Upgrading Guide.
15.3. JWT Client authentication and the latest OIDC specification
The latest version of the OpenID Connect Core Specification tightened the rules for audience validation in JWT client assertions for the Client Authentication methods private_key_jwt
and client_secret_jwt
. Red Hat build of Keycloak now enforces by default that there is a single audience in the JWT token used for client authentication.
For more details on the changed audience validation in JWT Client authentication Red Hat build of Keycloak versions, see the Upgrading Guide.
15.4. Operator enhancements
These updates are relevant to topics covered in the Operator Guide.
15.4.1. Rolling updates for optimized and customized images
When using an optimized or customized image, the Red Hat build of Keycloak Operator can now perform a rolling update for a new image if the old and the new image contain the same version of Red Hat build of Keycloak. For example, this option is helpful when you want to roll out an updated theme or provider without downtime.
To use the functionality in the Operator, enable the Auto
update strategy and the Operator will briefly start up the old and new images to determine if a rolling update without downtime is possible. For more details, see Managing Rolling Updates.
The checks to determine if a rolling update is possible are also available on the command line. You can use them in your deployment pipeline. For more details, see the Update Compatibility Tool.
15.4.2. Operator creates NetworkPolicies to restrict traffic
The Red Hat build of Keycloak Operator now creates a NetworkPolicy to restrict traffic to internal ports used for Red Hat build of Keycloak’s distributed caches. These Network Policies improve the security of your Kubernetes deployment. They strengthen a secure-by-default setup and minimize the configuration steps of new setups.
You can add more restrictions on the access to the management and HTTP endpoints further using the Kubernetes NetworkPolicies rule syntax. You define network policies in your Keycloak CR. The Operator accepts the ingress rules, which define where the traffic is allowed to come from, and it automatically creates the necessary Network Policies.
For more details, see Operator Advanced configuration.
15.4.3. ARM architecture
Red Hat build of Keycloak now supports OpenShift on ARM architecture.
15.5. Observability enhancements
These updates are relevant to topics covered in the Observability Guide, a new guide at this release.
15.5.1. Metrics and Grafana dashboards
In addition to the list of useful metric names, this guide also contains details on how to display these metrics in Grafana. It includes details on these two dashboards.
- Troubleshooting dashboard - show metrics related to service level indicators and troubleshooting.
- Capacity planning dashboard - shows metrics related to estimating the load handled by Red Hat build of Keycloak.
15.5.2. OpenTelemetry Tracing supported
The OpenTelemetry Tracing feature is fully supported now and the opentelemetry
feature is enabled by default. The tracing capabilities feature has these improvements:
- Configuration by Keycloak CR in Red Hat build of Keycloak Operator
Custom spans for:
- Incoming/outgoing HTTP requests including Identity Providers brokerage
- Database operations and connections
- LDAP requests
- Time-consuming operations (passwords hashing, persistent sessions operations, and so on)
For more information, see Enabling tracing.
15.5.3. Metrics on user activities
Event metrics provide administrators an aggregated view of the different user activities in a Red Hat build of Keycloak instance. In this release, metrics for user events are captured. For example, you can monitor the number of logins, login failures, or token refreshes performed.
For more details, see Monitoring user activities with event metrics.
15.5.4. Metrics on password hashing
A new password hashing metric was added to count how many password validations were performed by Red Hat build of Keycloak. Therefore, you can better assess where CPU resources are used, which feeds into your sizing calculations.
For more details, see Keycloak metrics and Concepts for sizing CPU and memory resources.
15.6. Transport stack jdbc-ping as new default
Red Hat build of Keycloak now uses its database to discover other nodes of the same cluster, which removes the need of additional network related configurations especially for cloud providers. It is also a default that will work without modification in cloud environments. Previous versions of Red Hat build of Keycloak used UDP multicast as a default to discover other nodes to form a cluster and to synchronize the replicated caches of Red Hat build of Keycloak. This required multicast to be available and to be configured correctly, which is usually not the case in cloud environments.
Starting with this version, the default changes to the jdbc-ping
configuration which uses Red Hat build of Keycloak’s database to discover other nodes. This change removes the need for multicast network capabilities and UDP and no longer uses dynamic ports for the TCP-based failure detection; this simplification is a drop-in replacement for environments that used the previous default. To enable the previous behavior, choose the transport stack udp,
which is now deprecated.
The Red Hat build of Keycloak Operator will continue to configure kubernetes
as a transport stack.
See Configuring distributed caches for more information.
15.7. Virtual Threads enabled for Infinispan and JGroups thread pools
Starting from this release, Red Hat build of Keycloak automatically enables the virtual thread pool support in both the embedded Infinispan and JGroups when running on OpenJDK 21 for environments with at least 2 CPU cores available. This change removes the need to configure the JGroups thread pool and the need to align the JGroups thread pool with the HTTP worker thread pool; it also reduces the overall memory footprint.
15.8. Infinispan default XML configuration location
Previous releases ignored any change to conf/cache-ispn.xml
if the --cache-config-file
option was not provided.
Starting from this release, when --cache-config-file
is not set, the default Infinispan XML configuration file is conf/cache-ispn.xml
as this is both the expected behavior and the implied behavior given the documentation of the current and previous releases.
15.9. Individual options for category-specific log levels
It is now possible to set category-specific log levels as individual log-level-category
options.
For more details, see Configuring levels as individual options.
15.10. Logs support ECS format
All available log handlers now support ECS (Elastic Common Schema) JSON format. It helps to improve Red Hat build of Keycloak’s observability story and centralized logging.
For more details, see Logging.
15.11. Minimum ACR Value for the client
The option Minimum ACR value is added as a configuration option on the realm OIDC clients. This addition is an enhancement related to step-up authentication, which makes it possible to enforce a minimum ACR level when logging in to the particular client.
15.12. Support for prompt=create
Support now exists for the Initiating user registration standard, which allows OIDC clients to initiate the login request with the parameter prompt=create
to notify Red Hat build of Keycloak that a new user should be registered rather than an existing user authenticated. Initiating user registration was already supported in Red Hat build of Keycloak with the use of dedicated endpoint /realms/<realm>/protocol/openid-connect/registrations
. However, this endpoint is now deprecated in favor of the standard way as it was a proprietary solution specific to Red Hat build of Keycloak.
15.13. Option to create certificates for generated EC keys
A new option, Generate certificate, exists for EC-DSA and Ed-DSA key providers. When the generated key is created by a realm administrator, a certificate might be generated for this key. The certificate information is available in the Admin Console and in the JWK representation of this key, which is available from JWKS endpoint with the realm keys.
15.14. Authorization Code Binding to a DPoP Key
Support now exists for Authorization Code Binding to a DPoP Key including support for the DPoP with Pushed Authorization Requests.
15.15. Maximum count and length parameters for OIDC authentication requests
The OIDC authentication request supports a limited number of additional custom parameters of maximum length. The additional parameters can be used for custom purposes (for example, adding the claims into the token with the use of the protocol mappers). In previous versions, the maximum count of the parameters was hardcoded to 5 and the maximum length of the parameters was hardcoded to 2000. Now both values are configurable. Additionally it can be possible to configure if additional parameters cause a request to fail or if parameters are ignored.
15.16. New LDAP users enabled by default for Microsoft Active Directory
If you are using Microsoft AD and creating users through the administrative interfaces, the user will be created as enabled by default.
In previous versions, it was only possible to update the user status after setting a (non-temporary) password to the user. This behavior was inconsistent with other built-in user storages and other LDAP vendors supported by the LDAP provider.
15.17. Option to reload trust and key material for the management interface
The https-management-certificates-reload-period
option can be set to define the reloading period of key store, trust store, and certificate files referenced by https-management-*
options for the management interface. Use -1 to disable reloading, which defaults to https-certificates-reload-period
, which is 1h (one hour).
For more information, see Configuring the Management Interface.
15.18. Zero-configuration secure cluster communication
For clustering multiple nodes, Red Hat build of Keycloak uses distributed caches. Starting with this release for all TCP-based transport stacks, the communication between the nodes is encrypted with TLS and secured with automatically generated ephemeral keys and certificates.
This strengthens a secure-by-default setup and minimizes the configuration steps of new setups.
If you are not using a TCP-based transport stack, it is recommended to migrate to the jdbc-ping
transport stack to benefit from the simplified configuration and enhanced security.
If you provided your own keystore and truststore to secure the TCP transport stack communication in previous releases, it is now recommended to migrate to the automatically generated ephemeral keys and certificates to benefit from the simplified setup.
If you are using a custom transport stack, this default behavior can be disabled by setting the option cache-embedded-mtls-enabled
to false
.
For more information, see Securing Transport Stacks.
15.19. New cache for CRLs loaded for the X.509 authenticator
The Certificate Revocation Lists (CRL), that are used to validate certificates in the X.509 authenticator, are now cached inside a new infinispan cache called crl
. Caching improves the validation performance and decreases the memory consumption because just one CRL is maintained per source.
Check the crl-storage
section in the All provider configuration chapter to know the options for the new cache provider.
15.20. New conditional authenticators
The Condition - sub-flow executed and Condition - client scope are new conditional authenticators in Red Hat build of Keycloak. The condition Condition - sub-flow executed checks if a previous sub-flow was executed (or not executed) successfully during the authentication flow execution. The condition Condition - client scope checks if a configured client scope is present as a client scope of the client requesting authentication. For more details, see Conditions in conditional flows.
15.21. Defining dependencies between provider factories
When developing extensions for Red Hat build of Keycloak, developers can now specify dependencies between provider factories classes by implementing the method dependsOn()
in the ProviderFactory
interface. See the Javadoc for a detailed description.
15.22. Dark mode enabled for the welcome theme
Dark mode support is now enabled for all the keycloak
themes. This feature was previously present in the Admin Console, Account Console, and login page, and is now also available on the welcome page. If a user indicates a preference through an operating system setting (such as light or dark mode) or a user agent setting, the theme automatically follows that preference.
If you are using a custom theme that extends a keycloak
theme and you are not ready to support dark mode, or you have styling conflicts that prevent you from implementing dark mode, you can disable support by adding the following property to your theme:
darkMode=false
Alternatively, you can disable dark mode support for the built-in Keycloak themes on a per-realm basis by turning off the Dark mode setting under the Theme tab in the realm settings.
15.23. Signing out active sessions now removes all sessions
In previous versions, clicking on Sign out all active sessions in the Admin Console resulted in the removal of regular sessions only. Offline sessions would still be displayed despite being effectively invalidated.
This approach has changed. Now all sessions, regular and offline, are removed when signing out of all active sessions.
15.24. Dedicated releases for Node.js and JavaScript adapters
From this release onwards, the Red Hat build of Keycloak JavaScript adapter and Red Hat build of Keycloak Node.js adapter will have a release cycle independent of the Red Hat build of Keycloak server release cycle. The 26.2.0 release may be the last one where these adapters are released together with the Red Hat build of Keycloak server, but from now on, these adapters may be released at a different time than the Red Hat build of Keycloak server.
15.25. Updated format of KEYCLOAK_SESSION cookie and AUTH_SESSION_ID cookie
The format of the KEYCLOAK_SESSION
cookie was updated to omit any private data in plain text. Until now, the format of the cookie was realmName/userId/userSessionId
. Now the cookie contains the user session ID, which is hashed by SHA-256 and URL encoded.
The format of the AUTH_SESSION_ID
cookie was updated to include a signature of the auth session id to ensure its integrity through signature verification. The new format is base64(auth_session_id.auth_session_id_signature)
. With this update, the old format will no longer be accepted, meaning that old auth sessions will no longer be valid. This change has no impact on user sessions.
These changes can affect you when you implement your own providers and you are relying on the format of internal Keycloak cookies.
15.26. Imported key providers check and passivate keys with an expired certificate
The key providers that allow you to import externally generated keys (rsa
and java-keystore
factories) now check the validity of the associated certificate if present. Therefore, a key with a certificate that is expired can no longer be imported in Red Hat build of Keycloak. If the certificate expires at runtime, the key is converted into a passive key (enabled but not active). A passive key is not used for new tokens, but it is still valid for validating previous issued tokens.
The default generated
key providers generate a certificate valid for 10 years (the types that have or can have an associated certificate). Because of the long validity and the recommendation to rotate keys frequently, the generated providers do not perform this check.
15.27. Admin events might include more context details
In this release, admin events might hold additional details about the context when the event is fired. During upgrade, you should expect the database schema being updated to add a new column DETAILS_JSON
to the ADMIN_EVENT_ENTITY
table.
15.28. More query parameters in Admin Events API
The Admin Events API now supports filtering for events based on Epoc timestamps in addition to the previous yyyy-MM-dd
format. This provides more fine-grained control of the window of events to retrieve.
A direction
query parameter was also added, allowing controlling the order of returned items as asc
or`desc`. In previous versions, the events were always returned in desc
order (most recent events first).
Finally, the returned event representations now also include the id
, which provides a unique identifier for an event.
15.29. New abort option in X.509 authenticator
The X.509 authenticator has a new option x509-cert-auth-crl-abort-if-non-updated
(CRL abort if non updated in the Admin Console). This option aborts the login if a CRL is configured to validate the certificate and the CRL is not updated in the time specified in the next update field. The new option defaults to true
in the Admin Console. For more details about the CRL next update field, see RFC5280, Section-5.1.2.5.
The value false
is maintained for compatibility with the previous behavior. Note that existing configurations will not have the new option and will act as if this option was set to false
, but the Admin Console will add the default value true
on edit.
15.30. New option to force a login in Send Reset Email
The reset-credential-email
(Send Reset Email) is the authenticator used in the reset credentials flow (forgot password feature) for sending the email to the user with the reset credentials token link. This authenticator now has a new option force-login
(Force login after reset). When this option is set to true
, the authenticator terminates the session and forces a new login.
The default value is only-federated
, which supports the secure-by-default policy. This value means that the force login is true for federated users and false for the internal database users. Therefore, all users managed by user federation providers, whose implementation can be not so tightly integrated with Red Hat build of Keycloak, are forced to login again after the reset credentials flow to avoid any issue.
For more information, see Enable forgot password.
15.31. Dynamic Authentication Flow selection
You can now dynamically select authentication flows based on conditions such as requested scopes, ACR (Authentication Context Class Reference) and others. This can be achieved using Client Policies by combining the new AuthenticationFlowSelectorExecutor
with conditions like the new ACRCondition
. For more details, see the Server Administration Guide.
15.32. Federated credentials available when fetching user credentials
Until now, querying user credentials using the User API will not return credentials managed by user storage providers and, as a consequence, prevent fetching additional metadata associated with federated credentials like the last time a credential was updated.
In this release, we are adding a new method getCredentials(RealmModel, UserModel)
to the org.keycloak.credential.CredentialInputUpdater
interface so that user storage providers can return the credentials they manage for a specific user in a realm. By doing this, user storage providers can indicate whether the credential is linked to it as well as provide additional metadata so that additional information can be shown when managing users through the administration console.
For LDAP, it should be possible now to see the last time the password was updated based on the standard pwdChangedTime
attribute or, if using Microsoft AD, based on the pwdLastSet
attribute.
In order to check if a credential is local - managed by Red Hat build of Keycloak - or federated, you can check the federationLink
property available from both CredentialRepresentation
and CredentialModel
types. If set, the federationLink
property holds the UUID of the component model associated with a given user storage provider.
15.33. Token based authentication for SMTP (XOAUTH2)
The Red Hat build of Keycloak outgoing SMTP mail configuration now supports token authentication (XOAUTH2). Many service providers, such as Microsoft and Google, are moving towards SMTP OAuth authentication, ending the support for basic authentication. The token is gathered using the Client Credentials Grant.
15.34. New client configuration for access token header type
A new admin setting has been added: Clients
If enabled, access tokens will get the header type at+jwt
in compliance with rfc9068#section-2.1. Otherwise, the access token header type will be JWT
.
This setting is turned off by default.
