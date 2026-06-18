---
title: "Chapter 4. Monitoring performance with Service Level Indicators - Red Hat build of Keycloak 26.2 Observability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-keycloak-service-level-indicators
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/observability_guide/keycloak-service-level-indicators-
guide: observability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 4. Monitoring performance with Service Level Indicators - Red Hat build of Keycloak 26.2 Observability Guide

Chapter 4. Monitoring performance with Service Level Indicators
Track performance and reliability as perceived by users with Service Level Indicators (SLIs) and Service Level Objectives (SLOs).
Service Level Indicators (SLIs) and Service Level Objectives (SLOs) are essential components in monitoring and maintaining the performance and reliability of Red Hat build of Keycloak in production environments.
The Google Site Reliability Engineering book defines this as follows:
- A Service Level Indicator (SLI) is a carefully defined quantitative measure of some aspect of the level of service that is provided.
- A Service level objective (SLO) is a target value or range of values for a service level that is measured by an SLI.
By agreeing those with the stakeholders and tracking these, service owners can ensure that deployments are aligned with user’s expectations and that they neither over- nor under-deliver on the service they provide.
4.1. Prerequisites
-
Metrics need to be enabled for Red Hat build of Keycloak, and the
http-metrics-slos
option needs to be set to latency to be measured for the SLO defined below. Follow Gaining insights with metrics chapter for more details. - A monitoring system collecting the metrics. The following paragraphs assume Prometheus or a similar system is used that supports the PromQL query language.
4.2. Definition of the service delivered
The following service definition is used in the next steps to identify the appropriate SLIs and SLOs. It should capture the behavior observed by its users.
As a Red Hat build of Keycloak user,
- I want to be able to log in,
- refresh my token and
- log out,
so that I can use the applications that use Red Hat build of Keycloak for authentication.
4.3. Definition of SLI and SLO
The following provides example SLIs and SLOs based on the service description above and the metrics available in Red Hat build of Keycloak.
While these SLOs are independent of the actual load the system, this is expected as a single user does not care about the system load if they get slow responses.
At the same time, if you enter a Service Level Agreement (SLA) with stakeholders, you as the one running Red Hat build of Keycloak have an interest to define limits of the traffic Red Hat build of Keycloak receives, as response times will be prolonged and error rates might increase as the load of the system increases and scaling thresholds are reached.
| Characteristic | Service Level Indicator | Service Level Objective* | Metric Source |
|---|---|---|---|
| Availability | Percentage of the time Red Hat build of Keycloak is able to answer requests as measured by the monitoring system | Red Hat build of Keycloak should be available 99.9% of the time within a month (44 minutes unavailability per month). |
Use the Prometheus |
| Latency | Response time for authentication related HTTP requests as measured by the server | 95% of all authentication related requests should be faster than 250 ms within 30 days. |
Red Hat build of Keycloak server-side metrics to track latency for specific endpoints along with Response Time Distribution using |
| Errors | Failed authentication requests due to server problems as measured by the server | The rate of errors due to server problems for authentication requests should be less than 0.1% within 30 days. |
Identify server side error by filtering the metric |
* These SLO target values are an example and should be tailored to fit your use case and deployment.
4.4. PromQL queries
These are example queries created in a Kubernetes environment and are used with Prometheus as a monitoring tool. They are provided as blueprints, and you will need to adapt them for a different runtime or monitoring environment.
For a production environment, you might want to replace those queries or subqueries with a recording rule to make sure they do not use too many resources if you want to use them for alerting or live dashboards.
4.4.1. Availability
This metric will have a value of at least one if the Red Hat build of Keycloak instances is available and responding to Prometheus scrape requests, and 0 if the service is down or unreachable.
Then use a tool like Grafana to show a 30-day time range and let it calculate the average of the metric in that time window.
count_over_time(
sum (up{
container="keycloak",
namespace="$namespace"
} > 0)[30d:15s]
)
/
count_over_time(vector(1)[30d:15s])
In Grafana you can replace value 30d:15s
with $range:$interval
to compute availability SLI in the time range selected for the dashboard.
4.4.2. Latency of authentication requests
This Prometheus query calculates the percentage of authentication requests that completed within 0.25 seconds relative to all authentication requests for specific Red Hat build of Keycloak endpoints, targeting a particular namespace and pod, over the past 30 days.
This example requires the Red Hat build of Keycloak configuration http-metrics-slos
to contain value 250
indicating that buckets for requests faster and slower than 250 ms should be recorded. Setting http-metrics-histograms-enabled
to true
would capture additional buckets which can help with performance troubleshooting.
sum(
rate(
http_server_requests_seconds_bucket{
uri=~"/realms/{realm}/protocol/{protocol}.*|/realms/{realm}/login-actions.*",
le="0.25",
container="keycloak",
namespace="$namespace"}
[30d]
)
) without (le,uri,status,outcome,method,pod,instance)
/
sum(
rate(
http_server_requests_seconds_count{
uri=~"/realms/{realm}/protocol/{protocol}.*|/realms/{realm}/login-actions.*",
container="keycloak",
namespace="$namespace"}
[30d]
)
) without (le,uri,status,outcome,method,pod,instance)
In Grafana, you can replace value 30d
with $__range
to compute latency SLI in the time range selected for the dashboard.
4.4.3. Errors for authentication requests
This Prometheus query calculates the percentage of authentication requests that returned a server side error for all authentication requests, targeting a particular namespace, over the past 30 days.
sum(
rate(
http_server_requests_seconds_count{
uri=~"/realms/{realm}/protocol/{protocol}.*|/realms/{realm}/login-actions.*",
outcome="SERVER_ERROR",
container="keycloak",
namespace="$namespace"}
[30d]
)
) without (le,uri,status,outcome,method,pod,instance)
/
sum(
rate(
http_server_requests_seconds_count{
uri=~"/realms/{realm}/protocol/{protocol}.*|/realms/{realm}/login-actions.*",
container="keycloak",
namespace="$namespace"}
[30d]
)
) without (le,uri,status,outcome,method,pod,instance)
In Grafana, you can replace value 30d
with $__range
to compute errors SLI in the time range selected for the dashboard.
