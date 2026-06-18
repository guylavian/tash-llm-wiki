---
title: "Chapter 12. New features and enhancements - Red Hat build of Keycloak 26.4 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-4-newfeatures
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/newfeatures
guide: release_notes
version: 26.4
family: rhbk
documentKind: "Documentation"
---

# Chapter 12. New features and enhancements - Red Hat build of Keycloak 26.4 Release Notes

Chapter 12. New features and enhancements
The following release notes apply to version 26.4.11 of Red Hat build of Keycloak. This release features new capabilities focused on security enhancements, deeper integration, and improved server administration. The highlights of this release are:
- Passkeys for seamless, passwordless authentication of users.
- Simplified experiences for application developers with streamlined WebAuthn/Passkey registration and simplified account linking to identity providers via application initiated actions.
- Federated Client Authentication to use SPIFFE or Kubernetes service account tokens for client authentication.
- Simplified deployments across multiple availability zones to boost availability.
- FAPI 2 Final: the final specifications of FAPI 2.0 Security Profile and FAPI 2.0 Message Signing.
- DPoP: The OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP) is now fully supported. Improvements include the ability to bind only refresh tokens for public clients, and securing all Keycloak endpoints with DPoP tokens.
- Account recovery with 2FA recovery codes, protecting users from lockout. Broader connectivity with the ability to broker with any OAuth 2.0 compliant authorization server, and enhanced trusted email verification for OpenID Connect providers.
- Asynchronous logging for higher throughput and lower latency, ensuring more efficient deployments.
Read on to learn more about each new feature. If you are upgrading from a previous release, also review the changes listed in the Upgrading Guide.
12.1. Security and Standards
12.1.1. Passkeys integration is now supported
Passkeys are now seamlessly integrated in the Red Hat build of Keycloak login forms using both conditional and modal UIs. To activate the integration in the realm, go to Authentication, Policies, Webauthn Passwordless Policy and switch Enable Passkeys to enabled.
For more information, see Passkeys.
12.1.2. FAPI 2 Final is now supported
Red Hat build of Keycloak has support for the latest versions of FAPI 2 specifications. Specifications FAPI 2.0 Security Profile and FAPI 2.0 Message Signing are already promoted to Final and Red Hat build of Keycloak supports them. Red Hat build of Keycloak client policies support the final versions and corresponding client profiles for FAPI 2 are passing the FAPI conformance test suite.
Apart from some very minor polishing of existing policies, Red Hat build of Keycloak has new client profiles (fapi-2-dpop-security-profile
and fapi-2-dpop-message-signing
) for the clients that use DPoP and are intended to be FAPI 2 compliant.
For more details, see FAPI Support.
12.1.3. DPoP is now supported
Red Hat build of Keycloak has support for OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP), which was previously a preview feature. Also, the supported version includes some improvements and minor capabilities of the DPoP feature such as the following:
- Possibility to make only refresh tokens of a public client to be DPoP bound and omit the binding of an access token.
- All Red Hat build of Keycloak endpoints that are secured by bearer token can now handle DPoP tokens. This includes, for example, the Admin REST API and Account REST API.
-
Possibility to require the
dpop_jkt
parameter in the OIDC authentication request.
For more information, see the DPoP section in the documentation.
12.1.4. FIPS 140-2 mode now supports EdDSA
With the upgrade to Bouncy Castle 2.1.x, the algorithm EdDSA can now be used.
12.2. Integration
12.2.1. Automatic certificate management for SAML clients
The SAML clients can now be configured to automatically download the signing and encrypting certificates from the SP entity metadata descriptor endpoint. In order to use this new feature, in the client Settings tab, section Signature and Encryption, configure the Metadata descriptor URL option (the URL where the SP metadata information with the certificates is published) and activate Use metadata descriptor URL. The certificates will be automatically downloaded and cached in the public-key-storage
SPI from that URL. This also allows for seamless rotation of certificates.
For more information, see Creating a SAML client.
12.2.2. Serving as an authorization server in MCP
MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems. Using MCP, AI applications can connect to data sources, tools and workflows enabling them to access key information and perform tasks.
To comply with MCP specification, this version provides its OAuth 2.0 Server Metadata via a well-known URI whose format complies with RFC 8414 OAuth 2.0 Authorization Server Metadata specification. Therefore, Keycloak users can now use Keycloak as an authorization server for MCP.
The latest MCP specification 2025-06-18 additionally requires support for resource indicators which are currently not implemented in Red Hat build of Keycloak.
12.2.3. Simplified linking of user accounts to an identity provider
Client-initiated linking a user account to the identity provider is now based on application-initiated action (AIA) implementation. This functionality aligns configuring this functionality, simplifies the error handling in calling the client application, which makes it more useful for a broader audience.
The custom protocol, which was previously used for client-initiated account linking, is now deprecated.
12.2.4. Brokering with OAuth v2 compliant authorization servers
In previous releases, Red Hat build of Keycloak already supported federation with other OpenID Connect and SAML providers, as well as with several Social Providers like GitHub and Google, which are based on OAuth 2.0.
The new OAuth 2.0 broker now closes the gap to federate with any OAuth 2.0 provider. As a result of this change, you can federate with Amazon or other providers. As this is a generic provider, you need to specify the different claims and a user info endpoint in the provider’s configuration.
For more information, see OAuth v2 identity providers.
12.2.5. Trusted email verification when brokering OpenID Connect Providers
Until now, the OpenID Connect broker did not support the standard email_verified
claim available from the ID Tokens issued by OpenID Connect Providers.
Starting with this release, Red Hat build of Keycloak supports this standard claim as defined by the OpenID Connect Core Specification for federation.
Whenever users are federated for the first time or when they re-authenticate and the Trust email setting is enabled, Sync Mode is set to FORCE
and the provider sends the email_verified
claim, the user account will have their email marked according to the email_verified
claim. If the provider does not send the claim, it defaults to the original behavior and sets the email as verified.
12.3. Administration
12.3.1. Update Email Workflow is now supported
Users can now update their email addresses in a more secure and consistent flow. Accounts are forced to both re-authenticate and verify their emails before any account updates.
For more information, see Update Email Workflow.
12.3.2. Optional email domain for organizations
In earlier versions, each organization required at least one email domain, which was a limitation for some scenarios. Starting with this release, an email domain is optional.
When no domain is specified, organization members will not be validated against domain restrictions during authentication and profile validation.
12.3.3. Hiding identity providers from the Account Console
You can now control which identity providers appear in the Account Console based on different options using the Show in Account console
setting. You can choose to show only those linked with a user or hide them completely.
For more information, see General configuration.
12.3.4. Enforce recovery codes setup after setting up OTP
If you have enabled OTPs and recovery codes as a second factor for authentication, you can configure the OTP required action to ask users to set up recovery codes once they set up an OTP.
12.3.5. New conditional authenticator
The Conditional - credential is a new authenticator that checks if a specific credential type has been used (or not used) during the authentication process. This condition is related to the Passkeys feature. It is added by Red Hat build of Keycloak to the default browser flow to skip 2FA in case a passkey was used to log in as the primary credential.
For more information about conditional flows, see Conditions in conditional flows.
12.3.6. Recovering an account after losing 2FA credentials
Users can get locked out of their accounts when they lose their 2FA credentials. For example, a user may have smart phone with a one-time-password (OTP) generator as a second factor for authentication. That user might lose his phone and be locked out.
To work around this issue, users can print a set of recovery codes as an additional second factor. The recovery codes become an alternative 2FA in the login flow. As a result, the user can gain access without using the OTP generated passwords.
With this release, the recovery codes feature is promoted from preview to a supported feature. For newly created realms, the browser flow now includes the Recovery Authentication Code Form as Disabled, and it can be switched to Alternative by admins if they want to use this feature.
For more information about this 2FA method, see Recovery Codes.
12.3.7. Simplified registration for WebAuthn and Passkeys
Both WebAuthn Register actions (webauthn-register
and webauthn-register-passwordless
), which are also used for Passkeys, now support a skip_if_exists
parameter when initiated by the application (AIA).
This change should make it more convenient to use the AIA in scenarios where a user has already set up WebAuthn or Passkeys. The parameter allows skipping the action if the user already has a credential of that type.
For more information, see Registering WebAuthn credentials using AIA.
12.4. Configuring and Running
12.4.1. Enhancements for single-cluster and multi-cluster setups
This release renamed multi-site to multi-cluster. The updated documentation describes how Red Hat build of Keycloak clusters can be optionally distributed across multiple availability-zones within a region for increased availability. The Red Hat build of Keycloak Operator now deploys Red Hat build of Keycloak across multiple availability zones within a Kubernetes cluster by default. Red Hat build of Keycloak also detects split-brains within a cluster.
This change should provide better availability for users who are running Red Hat build of Keycloak in Kubernetes clusters that span multiple availability zones.
12.4.2. Support for additional databases and versions
With this release, we added support for the following new database vendors:
- EnterpriseDB (EDB) Advanced 17.6
- Azure SQL Database and Azure SQL Managed Instance
Where the previous documentation stated only tested database version, it now states all the supported database versions as well.
12.4.3. Expose management interface by HTTP
Previous versions exposed the management endpoint only by HTTPS when the main interface was using HTTPS.
Set the new option http-management-scheme
to http
to have the management interface use HTTP rather than inheriting the HTTPS settings of the main interface. This change allows monitoring those endpoints in environments where no TLS client is available.
12.4.4. Expose health endpoints on the main HTTP(S) port
With health-enabled
set to true, you may set the http-management-health-enabled
to false
to indicate that health endpoints should be exposed on the main HTTP(s) port instead of the management port. When this option is false
you should block unwanted external traffic to /health
at your proxy.
This allows using the health endpoints in environments where the load balancer might need access to those ports to direct traffic to the correct nodes.
12.4.5. Ability to specify a tlsSecret on the Keycloak CR ingress spec
To support basic TLS termination (edge) deployments by the operator, you may now set the Keycloak CR spec.ingress.tlsSecret
field to a TLS Secret name in the namespace.
12.4.6. Additional datasources configuration
Some Red Hat build of Keycloak use cases like User Federation might require connecting to additional databases. This was possible only through specifying unsupported raw Quarkus properties in previous Red Hat build of Keycloak versions. In this release, there are now dedicated server options for additional datasources. This allows users to leverage additional databases in their extensions in a supported and user-friendly way.
For more details, see Configure multiple datasources.
12.4.7. Asynchronous logging for higher throughput and lower latency
All available log handlers now support asynchronous logging capabilities. Asynchronous logging helps deployments that require high throughput and low latency.
For more details on this feature, see Asynchronous logging.
12.4.8. HTTP access logging of incoming HTTP requests
Red Hat build of Keycloak supports HTTP access logging to record details of incoming HTTP requests. While access logs are often used for debugging and traffic analysis, they are also important for security auditing and compliance monitoring.
For more details, see HTTP Access Logging.
12.4.9. Performance improvements: import, export, and migration
The time it takes to run imports, exports or migrations involving a large number of realms has been improved. A cumulative performance degradation for each additional realm processed is no longer an issue.
12.5. Observability
12.5.1. Operator creates a ServiceMonitor automatically
The Operator now includes a ServiceMonitor
for the management endpoint if metrics are enabled and the monitoring.coreos.com/v1:ServiceMonitor
Custom Resource Definition is present on the Kubernetes cluster. The specification of the ServiceMonitor
takes into account the various management endpoint configurations, to ensure that metrics can be scraped without any additional configuration. If you do not want a ServiceMonitor
to be created, you can disable this by setting spec.serviceMonitor.enabled: false
. For more details, see the Operator Guide. == HTTP access logging of incoming HTTP requests
Red Hat build of Keycloak supports HTTP access logging to record details of incoming HTTP requests. While access logs are often used for debugging and traffic analysis, they are also important for security auditing and compliance monitoring.
For more information, see Configuring logging.
