---
title: "Chapter 3. Monitoring user activities with event metrics - Red Hat build of Keycloak 26.4 Observability Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-event-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/observability_guide/event-metrics-
guide: observability_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "Event metrics provide an aggregated view of user activities in a Red Hat build of Keycloak instance. For now, only metrics for user events are captured. For example, you can monitor the number of logins, login failures, or token refreshes performed. The metrics are exposed using the standard metrics endpoint, and you can use it in your own metrics collection system to create dashboards and alerts.…"
---

# Chapter 3. Monitoring user activities with event metrics - Red Hat build of Keycloak 26.4 Observability Guide

Chapter 3. Monitoring user activities with event metrics
Event metrics provide an aggregated view of user activities in a Red Hat build of Keycloak instance.
For now, only metrics for user events are captured. For example, you can monitor the number of logins, login failures, or token refreshes performed.
The metrics are exposed using the standard metrics endpoint, and you can use it in your own metrics collection system to create dashboards and alerts.
The metrics are reported as counters per Red Hat build of Keycloak instance. The counters are reset on the restart of the instance. If you have multiple instances running in a cluster, you will need to collect the metrics from all instances and aggregate them to get per a cluster view.
3.1. Enable event metrics
To start collecting event metrics, enable metrics and enable the metrics for user events.
The following shows the required startup parameters:
bin/kc.[sh|bat] start --metrics-enabled=true --event-metrics-user-enabled=true ...
By default, there is a separate metric for each realm. To break down the metric by client and identity provider, you can add those metrics dimension using the configuration option event-metrics-user-tags
. This can be useful on installations with a small number of clients and IDPs. This is not recommended for installations with a large number of clients or IDPs as it will increase the memory usage of Red Hat build of Keycloak and as it will increase the load on your monitoring system.
The following shows how to configure Red Hat build of Keycloak to break down the metrics by all three metrics dimensions:
bin/kc.[sh|bat] start ... --event-metrics-user-tags=realm,idp,clientId ...
You can limit the events for which Red Hat build of Keycloak will expose metrics. See the Server Administration Guide on event types for an overview of the available events.
The following example limits the events collected to LOGIN
and LOGOUT
events:
bin/kc.[sh|bat] start ... --event-metrics-user-events=login,logout ...
See Self-provided metrics for a description of the metrics collected.
3.2. Relevant options
| Value | |
|---|---|
| 🛠
|
|
| 🛠
Available only when metrics are enabled and feature user-event-metrics is enabled |
|
|
Available only when user event metrics are enabled
Use |
|
|
Available only when user event metrics are enabled |
|
