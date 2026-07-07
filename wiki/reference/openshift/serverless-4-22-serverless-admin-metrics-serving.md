---
title: "Knative Serving metrics"
type: reference
domain: openshift
slug: serverless-4-22-serverless-admin-metrics-serving
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-admin-metrics-serving
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Knative Serving metrics

[id="serverless-admin-metrics-serving"]
= Knative Serving metrics

Cluster administrators can view the following metrics for Knative Serving components.

// Module included in the following assemblies:
//
// * serverless/observability/admin-metrics/serverless-admin-metrics.adoc

[id="serverless-activator-metrics_{context}"]
= Activator metrics

You can use the following metrics to understand how applications respond when traffic passes through the activator.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`request_concurrency`
|The number of concurrent requests that are routed to the activator, or average concurrency over a reporting period.
|Gauge
|`configuration_name`, `container_name`, `namespace_name`, `pod_name`, `revision_name`, `service_name`
|Integer (no units)

|`request_count`
|The number of requests that are routed to activator. These are requests that have been fulfilled from the activator handler.
|Counter
|`configuration_name`, `container_name`, `namespace_name`, `pod_name`, `response_code`, `response_code_class`, `revision_name`, `service_name`, |Integer (no units)

|`request_latencies`
|The response time in milliseconds for a fulfilled, routed request.
|Histogram
|`configuration_name`, `container_name`, `namespace_name`, `pod_name`, `response_code`, `response_code_class`, `revision_name`, `service_name`
|Milliseconds
|===
// Module included in the following assemblies:
//
// * serverless/observability/admin-metrics/serverless-admin-metrics.adoc

[id="serverless-autoscaler-metrics_{context}"]
= Autoscaler metrics

The autoscaler component exposes a number of metrics related to autoscaler behavior for each revision. For example, at any given time, you can monitor the targeted number of pods the autoscaler tries to allocate for a service, the average number of requests per second during the stable window, or whether the autoscaler is in panic mode if you are using the Knative pod autoscaler (KPA).

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`desired_pods`
|The number of pods the autoscaler tries to allocate for a service.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`excess_burst_capacity`
|The excess burst capacity served over the stable window.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`stable_request_concurrency`
|The average number of requests for each observed pod over the stable window.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`panic_request_concurrency`
|The average number of requests for each observed pod over the panic window.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`target_concurrency_per_pod`
|The number of concurrent requests that the autoscaler tries to send to each pod.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`stable_requests_per_second`
|The average number of requests-per-second for each observed pod over the stable window.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`panic_requests_per_second`
|The average number of requests-per-second for each observed pod over the panic window.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`target_requests_per_second`
|The number of requests-per-second that the autoscaler targets for each pod.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`panic_mode`
|This value is `1` if the autoscaler is in panic mode, or `0` if the autoscaler is not in panic mode.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`requested_pods`
|The number of pods that the autoscaler has requested from the Kubernetes cluster.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`actual_pods`
|The number of pods that are allocated and currently have a ready state.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`not_ready_pods`
|The number of pods that have a not ready state.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`pending_pods`
|The number of pods that are currently pending.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)

|`terminating_pods`
|The number of pods that are currently terminating.
|Gauge
|`configuration_name`, `namespace_name`, `revision_name`, `service_name`
|Integer (no units)
|===
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-admin-metrics.adoc

[id="serverless-go-metrics_{context}"]
= Go runtime metrics

Each Knative Serving control plane process emits a number of Go runtime memory statistics (MemStats).

[NOTE]
====
The `name` tag for each metric is an empty tag.
====

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`go_alloc`
|The number of bytes of allocated heap objects. This metric is the same as `heap_alloc`.
|Gauge
|`name`
|Integer (no units)

|`go_total_alloc`
|The cumulative bytes allocated for heap objects.
|Gauge
|`name`
|Integer (no units)

|`go_sys`
|The total bytes of memory obtained from the operating system.
|Gauge
|`name`
|Integer (no units)

|`go_lookups`
|The number of pointer lookups performed by the runtime.
|Gauge
|`name`
|Integer (no units)

|`go_mallocs`
|The cumulative count of heap objects allocated.
|Gauge
|`name`
|Integer (no units)

|`go_frees`
|The cumulative count of heap objects that have been freed.
|Gauge
|`name`
|Integer (no units)

|`go_heap_alloc`
|The number of bytes of allocated heap objects.
|Gauge
|`name`
|Integer (no units)

|`go_heap_sys`
|The number of bytes of heap memory obtained from the operating system.
|Gauge
|`name`
|Integer (no units)

|`go_heap_idle`
|The number of bytes in idle, unused spans.
|Gauge
|`name`
|Integer (no units)

|`go_heap_in_use`
|The number of bytes in spans that are currently in use.
|Gauge
|`name`
|Integer (no units)

|`go_heap_released`
|The number of bytes of physical memory returned to the operating system.
|Gauge
|`name`
|Integer (no units)

|`go_heap_objects`
|The number of allocated heap objects.
|Gauge
|`name`
|Integer (no units)

|`go_stack_in_use`
|The number of bytes in stack spans that are currently in use.
|Gauge
|`name`
|Integer (no units)

|`go_stack_sys`
|The number of bytes of stack memory obtained from the operating system.
|Gauge
|`name`
|Integer (no units)

|`go_mspan_in_use`
|The number of bytes of allocated `mspan` structures.
|Gauge
|`name`
|Integer (no units)

|`go_mspan_sys`
|The number of bytes of memory obtained from the operating system for `mspan` structures.
|Gauge
|`name`
|Integer (no units)

|`go_mcache_in_use`
|The number of bytes of allocated `mcache` structures.
|Gauge
|`name`
|Integer (no units)

|`go_mcache_sys`
|The number of bytes of memory obtained from the operating system for `mcache` structures.
|Gauge
|`name`
|Integer (no units)

|`go_bucket_hash_sys`
|The number of bytes of memory in profiling bucket hash tables.
|Gauge
|`name`
|Integer (no units)

|`go_gc_sys`
|The number of bytes of memory in garbage collection metadata.
|Gauge
|`name`
|Integer (no units)

|`go_other_sys`
|The number of bytes of memory in miscellaneous, off-heap runtime allocations.
|Gauge
|`name`
|Integer (no units)

|`go_next_gc`
|The target heap size of the next garbage collection cycle.
|Gauge
|`name`
|Integer (no units)

|`go_last_gc`
|The time that the last garbage collection was completed in _Epoch_ or Unix time.
|Gauge
|`name`
|Nanoseconds

|`go_total_gc_pause_ns`
|The cumulative time in garbage collection _stop-the-world_ pauses since the program started.
|Gauge
|`name`
|Nanoseconds

|`go_num_gc`
|The number of completed garbage collection cycles.
|Gauge
|`name`
|Integer (no units)

|`go_num_forced_gc`
|The number of garbage collection cycles that were forced due to an application calling the garbage collection function.
|Gauge
|`name`
|Integer (no units)

|`go_gc_cpu_fraction`
|The fraction of the available CPU time of the program that has been used by the garbage collector since the program started.
|Gauge
|`name`
|Integer (no units)
|===
