---
title: "Chapter 20. Enabling Red Hat build of Keycloak Metrics - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-configuration-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/configuration-metrics-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 20. Enabling Red Hat build of Keycloak Metrics - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 20. Enabling Red Hat build of Keycloak Metrics
Red Hat build of Keycloak has built in support for metrics. This chapter describes how to enable and configure server metrics.
20.1. Enabling Metrics
It is possible to enable metrics using the build time option metrics-enabled
:
bin/kc.[sh|bat] start --metrics-enabled=true
20.2. Querying Metrics
Red Hat build of Keycloak exposes metrics at the following endpoint on the management interface at:
-
/metrics
For more information about the management interface, see Configuring the Management Interface. The response from the endpoint uses a application/openmetrics-text
content type and it is based on the Prometheus (OpenMetrics) text format. The snippet below is an example of a response:
# HELP base_gc_total Displays the total number of collections that have occurred. This attribute lists -1 if the collection count is undefined for this collector.
# TYPE base_gc_total counter
base_gc_total{name="G1 Young Generation",} 14.0
# HELP jvm_memory_usage_after_gc_percent The percentage of long-lived heap pool used after the last GC event, in the range [0..1]
# TYPE jvm_memory_usage_after_gc_percent gauge
jvm_memory_usage_after_gc_percent{area="heap",pool="long-lived",} 0.0
# HELP jvm_threads_peak_threads The peak live thread count since the Java virtual machine started or peak was reset
# TYPE jvm_threads_peak_threads gauge
jvm_threads_peak_threads 113.0
# HELP agroal_active_count Number of active connections. These connections are in use and not available to be acquired.
# TYPE agroal_active_count gauge
agroal_active_count{datasource="default",} 0.0
# HELP base_memory_maxHeap_bytes Displays the maximum amount of memory, in bytes, that can be used for memory management.
# TYPE base_memory_maxHeap_bytes gauge
base_memory_maxHeap_bytes 1.6781410304E10
# HELP process_start_time_seconds Start time of the process since unix epoch.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.675188449054E9
# HELP system_load_average_1m The sum of the number of runnable entities queued to available processors and the number of runnable entities running on the available processors averaged over a period of time
# TYPE system_load_average_1m gauge
system_load_average_1m 4.005859375
...
20.3. Available Metrics
The table below summarizes the available metrics groups:
| Metric | Description |
|---|---|
| System | A set of system-level metrics related to CPU and memory usage. |
| JVM | A set of metrics from the Java Virtual Machine (JVM) related to GC, and heap. |
| Database | A set of metrics from the database connection pool, if using a database. |
| HTTP | A set of global and individual metrics from the HTTP endpoints |
| Cache | A set of metrics from Infinispan caches. See Configuring distributed caches for more details. |
20.4. Relevant options
| Value | |
|---|---|
|
Available only when metrics are enabled |
|
|
Available only when metrics are enabled |
|
|
Available only when metrics are enabled | |
| 🛠
|
|
