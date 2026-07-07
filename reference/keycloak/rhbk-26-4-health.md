---
title: "Chapter 1. Tracking instance status with health checks - Red Hat build of Keycloak 26.4 Observability Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-health
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/observability_guide/health-
guide: observability_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "Check if an instance has finished its start up and is ready to serve requests by calling its health REST endpoints. Red Hat build of Keycloak has built in support for health checks. This chapter describes how to enable and use the Red Hat build of Keycloak health checks. The Red Hat build of Keycloak health checks are exposed on the management port 9000 by default. For more details, see Configurin…"
---

# Chapter 1. Tracking instance status with health checks - Red Hat build of Keycloak 26.4 Observability Guide

Chapter 1. Tracking instance status with health checks
Check if an instance has finished its start up and is ready to serve requests by calling its health REST endpoints.
Red Hat build of Keycloak has built in support for health checks. This chapter describes how to enable and use the Red Hat build of Keycloak health checks. The Red Hat build of Keycloak health checks are exposed on the management port 9000
by default. For more details, see Configuring the Management Interface
When the http-management-health-enabled
option is false
the health endpoints will remain on the main HTTP(S) ports, rather than being exposed on the management port. When this option is false
you should block unwanted external traffic to /health
at your proxy.
1.1. Red Hat build of Keycloak health check endpoints
Red Hat build of Keycloak exposes 4 health endpoints:
-
/health/live
-
/health/ready
-
/health/started
-
/health
See the Quarkus SmallRye Health docs for information on the meaning of each endpoint.
These endpoints respond with HTTP status 200 OK
on success or 503 Service Unavailable
on failure, and a JSON object like the following:
Successful response for endpoints without additional per-check information:
{
"status": "UP",
"checks": []
}
Successful response for endpoints with information on the database connection:
{
"status": "UP",
"checks": [
{
"name": "Keycloak cluster health check",
"status": "UP"
},
{
"name": "Keycloak database connections async health check",
"status": "UP"
}
]
}
1.2. Enabling the health checks
It is possible to enable the health checks using the build time option health-enabled
:
bin/kc.[sh|bat] build --health-enabled=true
By default, no check is returned from the health endpoints.
1.3. Using the health checks
Due to security measures that remove curl
and other packages from the Red Hat build of Keycloak container image, you are not able to run checks against HTTPS endpoints from within the container.
If you are not using Red Hat build of Keycloak in a container, or if you are running the health checks outside of the container, use any tool to access the health check endpoints.
1.3.1. curl
You may use a simple HTTP HEAD request to determine the live
or ready
state of Red Hat build of Keycloak. curl
is a good HTTP client for this purpose.
If Red Hat build of Keycloak is deployed in a container, you must use a custom image or run this command from outside it due to the previously mentioned security measures. For example:
curl --head -fsS http://localhost:9000/health/ready
If the command returns with status 0, then Red Hat build of Keycloak is live
or ready
, depending on which endpoint you called. Otherwise there is a problem.
1.3.2. Kubernetes
Define a HTTP Probe so that Kubernetes may externally monitor the health endpoints. Do not use a liveness command.
If you configure mTLS with https-client-auth
set to required
, this configuration is inherited by the management interface. If you have not otherwise configured the usage of HTTP for the health endpoints, you will likely want to set https-management-client-auth
to request
or none
so that a valid client certificate is not required for probe requests.
1.3.3. HEALTHCHECK
The Containerfile HEALTHCHECK
instruction defines a command that will be periodically executed inside the container as it runs. While the Red Hat build of Keycloak container does not have any CLI HTTP clients installed, it is possible to leverage BASH support for redirects to TCP sockets and craft a simple HTTP request to the healthcheck endpoint:
{ printf 'HEAD /health/ready HTTP/1.0\r\n\r\n' >&0; grep 'HTTP/1.0 200'; } 0<>/dev/tcp/localhost/9000
The above code depends on the values of the Red Hat build of Keycloak options such as http-relative-path
(http-management-relative-path
) and http-management-port
. In case those are changed the code needs to be modified accordingly.
If you enable TLS as shown in Configuring TLS, the management interface will also use TLS. Depending upon how the management interface endpoints are intended to be used you can still have plain HTTP health checks if:
-
the management interface uses HTTP, not HTTPS, by setting
http-management-scheme
tohttp
. -
or the health checks are enabled for the main interface by setting
http-management-health-enabled
tofalse
and accessible via HTTP with settinghttp-enabled
totrue
. In this scenario external traffic to the HTTP port (defaults to 8080) or to the health endpoints (defaults to /health) should not be allowed by your proxy.
1.4. Available Checks
The table below shows the available checks.
| Check | Description | Requires Metrics |
|---|---|---|
| Database | Returns the status of the database connection pool. | Yes |
| Cluster | Returns the status of the cluster (network partitions). | No |
For some checks, you’ll need to also enable metrics as indicated by the Requires Metrics
column. To enable metrics use the metrics-enabled
option as follows:
bin/kc.[sh|bat] build --health-enabled=true --metrics-enabled=true
The cluster health check is only available for clustered setups when the cache transport stacks jdbc-ping
or jdbc-ping-udp
are used.
1.5. Relevant options
| Value | |
|---|---|
| 🛠
|
|
