---
title: "Chapter 2. New features and enhancements - Red Hat build of Keycloak 26.6 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-6-newfeatures
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/release_notes/newfeatures
guide: release_notes
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "This release features new capabilities for users and administrators of Red Hat build of Keycloak. The highlights of this release are: JWT Authorization Grant, enabling external-to-internal token exchange using externally signed JWT assertions Federated client authentication, eliminating the need to manage individual client secrets in Red Hat build of Keycloak Workflows, enabling administrators to …"
---

# Chapter 2. New features and enhancements - Red Hat build of Keycloak 26.6 Release Notes

Chapter 2. New features and enhancements
This release features new capabilities for users and administrators of Red Hat build of Keycloak. The highlights of this release are:
- JWT Authorization Grant, enabling external-to-internal token exchange using externally signed JWT assertions
- Federated client authentication, eliminating the need to manage individual client secrets in Red Hat build of Keycloak
- Workflows, enabling administrators to automate realm administrative tasks such as user and client lifecycle management
- Zero-downtime patch releases, allowing rolling updates within a minor release stream without service downtime
- Instructions for using Red Hat build of Keycloak as an authorization server for Model Context Protocol (MCP) servers
- Authenticating clients with Kubernetes service account tokens to avoid static client secrets
- The addition of the UI Customization Guide, which includes details on creating themes for the Admin Console, Account Console, and Login page.
Read on to learn more about each new feature. If you are upgrading from a previous release, also review the changes listed in the Upgrading Guide.
2.1. Security and Standards
2.1.1. JWT Authorization Grant
This release introduces JWT Authorization Grant, a new feature that adds support for RFC 7523 to use external signed JWT assertions to request OAuth 2.0 access tokens.
To accept signed JWT assertions, a trust relationship must be established between the external provider and Red Hat build of Keycloak. This trust relationship can be configured through an identity provider in a dedicated section of the OpenID Connect v1.0 identity provider, or through the new JWT Authorization Grant identity provider.
JWT Authorization Grant is recommended as an alternative to External to internal token exchange V1. For more details, see JWT Authorization Grant.
2.1.2. Federated client authentication
Federated client authentication allows clients to leverage existing credentials once a trust relationship with another issuer exists. It eliminates the need to assign and manage individual secrets for each client in Red Hat build of Keycloak.
This feature includes support for client assertions issued by external OpenID Connect identity providers and Kubernetes Service Accounts. For details, see Kubernetes identity providers.
2.1.3. Red Hat build of Keycloak as an authorization server for MCP servers
Using Red Hat build of Keycloak as an authorization server for Model Context Protocol (MCP) servers is becoming popular, so this release ships additional documentation on how to do this.
For more details, see Integrating with Model Context Protocol.
2.1.4. New instructions for Demonstrating Proof-of-Possession
The Securing applications and Services guide includes more information about OAuth 2.0 Demonstrating Proof-of-Possession (DPoP). It provides information on how to mitigate the risk of stolen tokens by making tokens sender-constrained.
For more details, see Securing applications with DPoP.
2.1.5. CORS enhancements
Cross Origin Resource Sharing (CORS) is a browser security feature that controls how web pages on one domain can request resources from a different domain.
- For the OpenID Connect Dynamic Client Registration, you can now specify which CORS headers are allowed by the client registration access policies.
-
For the overall CORS configuration, you can now allow environment specific headers by using the SPI option
spi-cors--default--allowed-headers
.
2.1.6. Logout confirmation page
The client logout configuration now includes an option to show a logout confirmation page. By enabling this option, “You are logged out” appears upon successful logout.
2.1.7. Hiding OpenID Connect scopes from the discovery endpoint
Previously, all scopes of an OpenID Connect client were advertised in the discovery endpoint.
In some situations, you might want to avoid it as the calling client. For example, an MCP server might not support it, or you might prefer to hide some scopes to prevent their discovery by public APIs. In this situation, you can disable Include in OpenID Provider Metadata.
2.2. Administration
2.2.1. Organization invitation management
Organization administrators can now manage organization invitations through both the Admin Console and REST API:
- View all sent invitations with their current status (Pending, Expired)
- Resend pending invitations to recipients
- Delete invitation records from the system
- Filter invitations by status for easier management
All invitations are now persistently stored in the database, providing better tracking and management capabilities.
The invitation management features are available in the Invitations tab when managing an organization in the Admin Console, and through the Organizations REST API endpoints under /admin/realms/{realm}/orgs/{orgId}/invitations
.
2.2.2. New event USER_SESSION_DELETED
For each expired user session, a new user event, USER_SESSION_DELETED
, is fired. This event is published approximately three to ten minutes after the session has expired depending on job scheduling and load on the system. By default, this event is not persisted.
2.2.3. Workflows
In this release, Workflows is promoted to supported. Workflows allow administrators to automate and orchestrate realm administrative tasks, bringing key capabilities of Identity Governance and Administration (IGA) to Red Hat build of Keycloak. By defining workflows in YAML format, you can automate the lifecycle of realm resources such as users and clients based on events, conditions, and schedules.
For more details, see Managing workflows.
2.2.4. Organization groups
Organizations now support isolated group hierarchies, allowing each organization to manage its own teams and departments without naming conflicts across the realm. This update includes Identity Provider mappers to automatically assign federated users to organization groups based on external claims. Group membership is automatically included in OIDC tokens and SAML assertions when an organization context is requested.
For more details, see Managing organization groups.
2.2.5. New Groups scope for user membership changes
Fine-Grained Admin Permissions (FGAP) now includes a new Groups
scope: manage-membership-of-members
.
This scope is now used as the group-side bridge for evaluating user-side manage-group-membership
permissions based on a user’s current group memberships. The existing manage-membership
scope keeps its current behavior for target group membership management operations.
2.2.6. Looking up client secrets by the Vault SPI
You can now look up and manage secrets for clients by using the Vault SPI.
2.2.7. Forcing password change for LDAP users
There is now initial support for LDAP password policy control. The support is limited to prompting users to update their password when the LDAP server indicates that the password must be changed. Previously, Red Hat build of Keycloak let the user in and ignored the mandatory password reset. To enable this capability, use the new Enable LDAP password policy setting under under LDAP advanced settings.
2.3. Configuring and Running
2.3.1. Improved server response times
Authentication, user, and client sessions are now created on the respective Red Hat build of Keycloak node and avoid extra remote calls to neighbors when reading or writing them to the embedded caches. When you have sticky sessions enabled in your load balancer, you benefit from this feature automatically, and you should see reduced response times when authenticating users.
Expired user sessions are now deleted from the database in small batches, instead of delete statements that affect the whole table. The goal is to provide better response times when many sessions exist in the table.
2.3.2. Configure retry behavior for outgoing HTTP requests
Red Hat build of Keycloak now provides increased flexibility for configuring the retrying of outgoing HTTP requests. This change is useful for handling transient network errors or temporary unavailability of the service where Red Hat build of Keycloak needs to send HTTP requests. Retry behavior is disabled by default and must be explicitly enabled. For more details, see Outgoing HTTP requests documentation.
2.3.3. Enable/disable features by a single option
You can now enable or disable individual features using the feature-<name>
option such as feature-spiffe=enabled
.
This change provides a more fine-grained way to manage features and eliminates the need to maintain long lists of enabled or disabled features. The feature-<name>
option takes precedence over both features
and features-disabled
.
For more details, see Enabling and disabling features.
2.3.4. Client certificate lookup compliant with RFC 9440
You can now use a new client certificate lookup provider that is compliant with RFC 9440. This change enables native support such as for Caddy and other reverse proxies that follow the RFC. For more details, see Enabling Client Certificate Lookup.
2.3.5. Running Red Hat build of Keycloak as a Windows service
Red Hat build of Keycloak can now be installed and run as a Windows service using Apache Commons Daemon (Procrun). The new tools windows-service
CLI subcommand simplifies service installation and uninstallation.
The service runs kc.bat start
as an external process, ensuring all environment variables and configuration files are respected. This provides seamless integration with the Windows Services management console and enables automatic startup on system boot without requiring a user to be logged on.
For more details, see Running Red Hat build of Keycloak as a Windows Service.
2.3.6. Java 25 support
Red Hat build of Keycloak now supports running with OpenJDK 25. The server container image continues to use OpenJDK 21 for now to support FIPS mode. For details, see FIPS 140-2 support.
2.3.7. Zero-downtime patch releases
Zero-downtime patch releases is now supported. You can perform rolling updates when upgrading to a newer patch version within the same major.minor
release stream without service downtime. When using the Red Hat build of Keycloak Operator, set the update strategy to Auto
to use this functionality.
For more details on the Operator configuration, see Avoiding downtime with rolling updates.
2.3.8. Graceful shutdown of HTTP stack
To allow rolling updates for configuration changes or version updates, a graceful shutdown of Red Hat build of Keycloak nodes prevents users from seeing error responses when logging in or refreshing their tokens when nodes shut down.
Starting with this version, Red Hat build of Keycloak supports a graceful shutdown of the HTTP stack. This change includes delaying a shutdown after receiving a termination signal, connection draining for HTTP/1.1 and HTTP/2 connections during that period, and a shutdown timeout to finish ongoing requests.
The defaults are a shutdown delay and a shutdown timeout of one second each. These defaults work well when the reverse proxy is using TLS edge termination or re-encryption and the reverse proxy is notified about the Red Hat build of Keycloak node shutting down at the same time as the Red Hat build of Keycloak node. This setup is common in Kubernetes environments.
You can adjust those values depending on your proxy setup. For more details, see Graceful HTTP shutdown.
2.3.9. Installation instructions for CloudNativePG
If you are running Red Hat build of Keycloak on Kubernetes, you can use new instructions for a CloudNativePG Operator. You can deploy a PostgreSQL database on Kubernetes by using the CloudNativePG Operator and connect Red Hat build of Keycloak to the database.
For more details, see Deploying CloudNativePG in multiple availability zones.
2.3.10. Simplified database operations
This release includes new command line options that simplify database operations for Red Hat build of Keycloak and remove the need to use raw JDBC connection options:
- Configuring TLS for the database connection
- Database connection timeouts
- Transaction timeouts with production-ready defaults
These options also verify the correct UTF-8 character encoding of the database at startup and print a warning if this is not the case.
When running on orchestrators such as Kubernetes, the startup and liveness probes return UP during database migrations, simplifying upgrades by removing the need to adjust the probes during upgrades.
See the Upgrading Guide for additional details on each aspect.
2.3.11. New KCRAW_ prefix for environment variables to preserve literal values
Red Hat build of Keycloak now supports a KCRAW_
prefix for environment variables to preserve values containing $
characters exactly as written, without expression evaluation.
When using the standard KC_
prefix, Red Hat build of Keycloak (by SmallRye Config) evaluates expressions in values (for example, ${some_key}
is resolved and $$
is collapsed to $
). This can silently modify passwords or secrets injected by a secrets manager or orchestration tool where manual escaping is not feasible.
Setting KCRAW_<KEY>
instead of KC_<KEY>
preserves the value exactly as provided.
For more details, see Preserving literal values with the KCRAW_ prefix.
2.3.12. Automatic reload of lists with disallowed passwords
When a list of disallowed passwords (also called blacklist) changes, that list is automatically reloaded. This feature avoids the need for a server restart when the list changes.
2.3.13. Automatic truststore initialization on Kubernetes and OpenShift
Red Hat build of Keycloak now automatically discovers and trusts cluster certificate authorities when running on Kubernetes or OpenShift, without requiring the Operator to preconfigure the truststore.
The following certificates are added to the system truststore at startup if they are found in the container filesystem:
-
/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
(Kubernetes service account CA) -
/var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt
(OpenShift service CA)
This behavior is enabled by default and can be controlled with the server option --truststore-kubernetes-enabled=true|false
(default: true
).
Most deployments do not require any action. If you relied on the Operator to manage these truststore entries previously, the server now performs the same function directly.
2.3.14. Client certificate lookup providers for Traefik and Envoy
You can now use new client certificate lookup providers for Traefik and Envoy proxies. For more details, see Enabling Client Certificate Lookup.
2.3.15. Configurable Kubernetes Service name and port in the Operator
The Red Hat build of Keycloak Operator now supports overriding the name and port of the Kubernetes Service that it creates for a Red Hat build of Keycloak deployment.
Previously, the Service name was always derived as <cr-name>-service
and the Service port always matched the container port. You can now use the spec.http.serviceName
, spec.http.serviceHttpsPort
, and spec.http.serviceHttpPort
fields to configure these independently.
For more details, see Advanced configuration.
2.3.16. Sensitive information is not displayed in the HTTP Access log
If you are using the HTTP Access logging capability, sensitive information is omitted. This means that tokens in the Authorization
HTTP header and specific sensitive cookies are not shown.
For more details, see Configuring HTTP access logging.
2.3.17. HTTP access logs in a dedicated file
HTTP access logs can now be written to a dedicated file, separate from the server logs. This change makes it easier to process and archive access logs independently for security auditing and compliance monitoring.
For more details, see Configuring HTTP access logging.
2.3.18. Configurable log file rotation
You can now configure log file rotation when using Red Hat build of Keycloak’s built-in file logging handler. This feature includes a simple option to fully disable log rotation, which is useful when using an external log rotation solution such as logrotate
.
To disable log file rotation:
bin/kc.sh start --log="console,file" --log-file-rotation-enabled=false
For more details, see File logging.
2.3.19. Customizable service fields in JSON log output
Red Hat build of Keycloak now provides native options to customize the service.name
and service.environment
fields in JSON log output across all log handlers: console, file, and syslog.
Previously, when using the ECS format, service.name
and service.environment
could not be overridden through Red Hat build of Keycloak configuration. This limitation made it difficult to align JSON log fields with OpenTelemetry resource attributes.
You can now set these fields using log-service-name
and log-service-environment
.
For more details, see Configuring logging.
2.3.20. Right-to-left language support in the Account Console
At a previous release, support for right-to-left (RTL) languages was added to the Login page, Admin Console, and email templates. This release adds initial RTL support to the Account Console, which completes this effort.
2.4. Observability
2.4.1. Export traces with custom request headers
It is now possible to set request headers for exporting traces by OpenTelemetry Protocol (OTLP). It is mainly useful for providing tokens in the request. You can specify these headers by the tracing-header-<header>
wildcard option, accepting any custom header name.
For more details, see Root cause analysis with tracing.
2.4.2. MDC logging
The log-mdc:v1
feature is now supported feature. MDC enables Red Hat build of Keycloak to enrich log entries with contextual information such as realm, client, user ID and IP address, significantly improving debugging and observability.
For more details, see Adding context for log messages.
2.4.3. New centralized OpenTelemetry options
Red Hat build of Keycloak now provides centralized telemetry configuration options that can be shared across all telemetry (OpenTelemetry) components - traces and logs, with future support planned for metrics. Individual components can override these global settings when needed.
The new options are telemetry-endpoint
, telemetry-protocol
, telemetry-service-name
, and telemetry-resource-attributes
.
Deprecation: The tracing-service-name
and tracing-resource-attributes
options are now deprecated in favor of telemetry-service-name
and telemetry-resource-attributes
.
For more details, see OpenTelemetry.
2.4.4. Telemetry configuration by the Keycloak CR
Red Hat build of Keycloak now supports configuring the OpenTelemetry properties by the Keycloak CR when using the Operator. These properties are shared among the available OpenTelemetry components - logs, metrics, and traces.
For more details, see OpenTelemetry.
2.4.5. Custom request headers for OpenTelemetry
It is now possible to set request headers for exporting telemetry by OpenTelemetry Protocol (OTLP). This feature is mainly useful for providing tokens in the request.
You can specify these headers by the telemetry-header-<header>
wildcard option, which accepts any custom header name. Alternatively, use telemetry-logs-header-<header>
for OpenTelemetry Logs or telemetry-metrics-header-<header>
for OpenTelemetry Metrics.
For more details, see OpenTelemetry.
2.4.6. Service Monitor annotations and labels by the Keycloak CR
You can now configure service monitor labels and annotations by the Keycloak CR when using the Operator.
For more details, see ServiceMonitor.
