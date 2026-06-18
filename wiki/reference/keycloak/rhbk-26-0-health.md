---
title: "Chapter 19. Enabling Red Hat build of Keycloak Health checks - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-health
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/health-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 19. Enabling Red Hat build of Keycloak Health checks - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 19. Enabling Red Hat build of Keycloak Health checks
Red Hat build of Keycloak has built in support for health checks. This chapter describes how to enable and use the Red Hat build of Keycloak health checks. The Red Hat build of Keycloak health checks are exposed on the management port 9000
by default. For more details, see Configuring the Management Interface
19.1. Red Hat build of Keycloak health check endpoints
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
"name": "Keycloak database connections health check",
"status": "UP"
}
]
}
19.2. Enabling the health checks
It is possible to enable the health checks using the build time option health-enabled
:
bin/kc.[sh|bat] build --health-enabled=true
By default, no check is returned from the health endpoints.
19.3. Using the health checks
It is recommended that the health endpoints be monitored by external HTTP requests. Due to security measures that remove curl
and other packages from the Red Hat build of Keycloak container image, local command-based monitoring will not function easily.
If you are not using Red Hat build of Keycloak in a container, use whatever you want to access the health check endpoints.
19.3.1. curl
You may use a simple HTTP HEAD request to determine the live
or ready
state of Red Hat build of Keycloak. curl
is a good HTTP client for this purpose.
If Red Hat build of Keycloak is deployed in a container, you must run this command from outside it due to the previously mentioned security measures. For example:
curl --head -fsS http://localhost:9000/health/ready
If the command returns with status 0, then Red Hat build of Keycloak is live
or ready
, depending on which endpoint you called. Otherwise there is a problem.
19.3.2. Kubernetes
Define a HTTP Probe so that Kubernetes may externally monitor the health endpoints. Do not use a liveness command.
19.3.3. HEALTHCHECK
The Containerfile HEALTHCHECK
instruction defines a command that will be periodically executed inside the container as it runs. The Red Hat build of Keycloak container does not have any CLI HTTP clients installed. Consider installing curl
as an additional RPM, as detailed by the Running Red Hat build of Keycloak in a container chapter. Note that your container may be less secure because of this.
19.4. Available Checks
The table below shows the available checks.
| Check | Description | Requires Metrics |
|---|---|---|
| Database | Returns the status of the database connection pool. | Yes |
For some checks, you’ll need to also enable metrics as indicated by the Requires Metrics
column. To enable metrics use the metrics-enabled
option as follows:
bin/kc.[sh|bat] build --health-enabled=true --metrics-enabled=true
19.5. Relevant options
| Value | |
|---|---|
| 🛠
|
|
