---
title: "Chapter 15. Deprecated features - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-deprecated
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/deprecated
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
---

# Chapter 15. Deprecated features - Red Hat build of Keycloak 26.4 Release Notes

Chapter 15. Deprecated features
The following sections provide details on deprecated features.
15.1. Disabling filtering of LDAP referrals
The option spi-storage—ldap—secure-referral
to disable filtering referrals is deprecated. When this feature is removed in a future release, filtering will then be enforced.
15.2. SPI options separating the provider with a single dash
SPI options ending in -enabled
, -provider-default
, or -provider
are treated as build-time options. However, in some instances, this was not correct as a provider could have a configuration property ending in one of those suffixes as well.
To resolve this ambiguity, and any potential ambiguity involving SPI and provider names, a new SPI option format was introduced where the scopes and suffix are separated by --
(double dash) instead of -
(dash). The new format then reads as spi-<spi-name>--<provider-name>--...
.
An SPI property ending in -enabled
, -provider-default
, or -provider
should use the new format or else a warning will be emitted. For example spi-<spi-name>--<provider-name>--enabled
will be recognized as a build-time option without a warning.
For instance, the correct way to reference your custom email template is: --spi-email-template--mycustomprovider--enabled
(not --spi-email-template-mycustomprovider-enabled
).
Options using the legacy format and ending in -enabled
, -provider-default
, or -provider
will still be treated as a build-time option, but may not be in future releases.
15.3. Kubernetes cache stack
The kubernetes
cache stack has been deprecated and will be removed in a future release. Users should transition to the jdbc-ping
stack.
Consequently, the Keycloak Operator now uses the jdbc-ping
cache stack by default.
15.4. method RequiredActionProvider.getMaxAuthAge()
The method RequiredActionProvider.getMaxAuthAge()
is deprecated. It is effectively not used now. Please use the method RequiredActionProvider.getMaxAuthAge(KeycloakSession session)
instead. This is due to enable individual configuration for required actions.
15.5. spi-connections-infinispan-quarkus-site-name
The option spi-connections-infinispan-quarkus-site-name
is deprecated and no longer used for multi-site setups, and it will be removed in the future. Use spi-cache-embedded-default-site-name
instead in setups when running with embedded distributed caches. See All provider configuration for more details on these options.
15.6. Proprietary protocol for client initiated linking to the identity provider account
When you want the user, who is authenticated to your client application, to link his or her account to a specific identity provider, consider using the Application initiated action (AIA) based mechanism with the action idp_link
. The proprietary custom protocol for client initiated account linking is deprecated now and might be removed in the future versions. For more information, see the Client initiated account link section of the Server Developer Guide.
15.7. Instagram Identity Broker
In this release, the Instagram Identity Broker is deprecated for removal and is not enabled by default. If you are using this broker, it is recommended to use the Facebook Identity Broker instead.
If you are using the Instagram Identity Broker and want to re-enable it, you can do it by enabling the instagram-broker
feature using the features
server option:
--features=instagram-broker
15.8. Local admin
UrlType.LOCAL_ADMIN
and the corresponding welcome theme variable localAdminUrl
have been deprecated for eventual removal. The default welcome resource will now simply mention localhost rather than providing a URL when an admin user has yet to be created.
15.9. Password policy Recovery Codes Warning Threshold
In relation to supported Recovery codes, we deprecated the password policy Recovery Codes Warning Threshold
. This password policy might be removed in the future major version of Red Hat build of Keycloak. This password policy was not related to passwords at all, but was related to recovery codes, and hence using password policy is an inappropriate way to configure this threshold. It is better to use the Warning Threshold configuration option of the Recovery Authentication Codes required action. For more details, see Recovery Codes.
15.10. Scope.getPropertyNames
The org.keycloak.Config.Scope.getPropertyNames
method has been deprecated for removal.
15.11. displayTest field in ConsentScopeRepresentation
The displayTest
field in the ConsentScopeRepresentation
class returned by the Account REST service has been deprecated due to a typo in its name. A new field displayText
with the correct spelling has been added to replace it. The old field will be removed in Red Hat build of Keycloak 27.0. The Typescript code ConsentScopeRepresentation
for the Account Console already contains only the new field.
15.12. Lifetime of offline session caches
The options --spi-user-sessions--infinispan--offline-session-cache-entry-lifespan-override
and --spi-user-sessions--infinispan--offline-client-session-cache-entry-lifespan-override
are now deprecated for removal.
Instead use the options cache-embedded-offline-sessions-max-count
and cache-embedded-offline-client-sessions-max-count
to limit the memory usage if the default of 10000 cache offline user and client sessions does not work in your scenario.
15.13. Passkeys Conditional UI Authenticator
The authenticator Passkeys Conditional UI Authenticator is deprecated and disabled by default. It now requires the feature passkeys_conditional_ui_authenticator
to be explicitly enabled during server startup. This allows administrators to start the server and re-configure authentication flows for passkeys authentication in a recommended way as described in the Passkeys chapter in the Server Administration Guide. A future major version will remove the feature and the Passkeys Conditional UI Authenticator.
15.14. Modifying default cache configurations in the cache config file
All Red Hat build of Keycloak default cache configurations have been removed from conf/cache-ispn.xml
. Configuration of the default cache configurations in conf/cache-ispn.xml
, or in a custom file via --cache-config-file
, without specifying --cache-config-mutate=true
is now deprecated and will log a warning.
In a future major release, the start-up will fail if default cache configurations are stated in those files and the option is not specified.
15.15. Simplified API for UserSessionProvider
In order to retrieve a client session via UserSessionProvider#getClientSession
, you no longer need to pass in the client session ID. The old methods have been deprecated and will be removed in a future release. You should also review the other methods that are deprecated for removal in this class.
15.16. Simplified API for AuthenticatedClientSessionModel
The clientId
note in the authenticated client session is an internal note present only when using the embedded caches, and is now deprecated for removal. Instead, use the getClient()
method.
15.17. Sending OpenID Connect client secret by basic authentication without URL encoding
In a scenario where Red Hat build of Keycloak acts as a broker and connects by OpenID Connect to another identity provider, you can choose to send the client secret as Client secret sent as HTTP Basic authentication without URL encoding (client_secret_basic_unencoded). While this violates RFC6749, it can be used to keep the default behavior of earlier versions of Red Hat build of Keycloak.
