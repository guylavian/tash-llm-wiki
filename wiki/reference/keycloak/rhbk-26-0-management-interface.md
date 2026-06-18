---
title: "Chapter 18. Configuring the Management Interface - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-management-interface
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/management-interface-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 18. Configuring the Management Interface - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 18. Configuring the Management Interface
The management interface allows accessing management endpoints via a different HTTP server than the primary one. It provides the possibility to hide endpoints like /metrics
or /health
from the outside world and, therefore, hardens the security. The most significant advantage might be seen in Kubernetes environments as the specific management port might not be exposed.
18.1. Management interface configuration
The management interface is turned on when something is exposed on it. Management endpoints such as /metrics
and /health
are exposed on the default management port 9000
when metrics and health are enabled. The management interface provides a set of options and is fully configurable.
If management interface properties are not explicitly set, their values are automatically inherited from the default HTTP server.
18.1.1. Port
In order to change the port for the management interface, you can use the Red Hat build of Keycloak option http-management-port
.
18.1.2. Relative path
You can change the relative path of the management interface, as the prefix path for the management endpoints can be different. You can achieve it via the Red Hat build of Keycloak option http-management-relative-path
.
For instance, if you set the CLI option --http-management-relative-path=/management
, the metrics, and health endpoints will be accessed on the /management/metrics
and /management/health
paths.
User is automatically redirected to the path where Red Hat build of Keycloak is hosted when the relative path is specified. It means when the relative path is set to /management
, and the user access localhost:9000/
, the page is redirected to localhost:9000/management
.
If you do not explicitly set the value for it, the value from the http-relative-path
property is used. For instance, if you set the CLI option --http-relative-path=/auth
, these endpoints are accessible on the /auth/metrics
and /auth/health
paths.
18.1.3. TLS support
When the TLS is set for the default Red Hat build of Keycloak server, the management interface will be accessible through HTTPS as well. The management interface can run only either on HTTP or HTTPS, not both as for the main server.
Specific Red Hat build of Keycloak management interface options with the prefix https-management-*
were provided for setting different TLS parameters for the management HTTP server. Their function is similar to their counterparts for the main HTTP server, for details see Configuring TLS. When these options are not explicitly set, the TLS parameters are inherited from the default HTTP server.
18.1.4. Disable Management interface
The management interface is automatically turned off when nothing is exposed on it. Currently, only health checks and metrics are exposed on the management interface regardless. If you want to disable exposing them on the management interface, set the Red Hat build of Keycloak property legacy-observability-interface
to true
.
Exposing health and metrics endpoints on the default server is not recommended for security reasons, and you should always use the management interface. Beware, the legacy-observability-interface
option is deprecated and will be removed in future releases. It only allows you to give more time for the migration.
18.2. Relevant options
| Value | |
|---|---|
|
| (default) |
| 🛠
| (default) |
|
| |
|
| |
| 🛠
|
|
|
| |
|
| (default) |
| 🛠
DEPRECATED. |
|
