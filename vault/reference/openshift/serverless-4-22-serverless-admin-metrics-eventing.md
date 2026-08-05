---
title: "Knative Eventing metrics"
type: reference
domain: openshift
slug: serverless-4-22-serverless-admin-metrics-eventing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-admin-metrics-eventing
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Knative Eventing metrics

[id="serverless-admin-metrics-eventing"]
= Knative Eventing metrics

Cluster administrators can view the following metrics for Knative Eventing components.

By aggregating the metrics from HTTP code, events can be separated into two categories; successful events (2xx) and failed events (5xx).

// Module included in the following assemblies:
//
// * serverless/observability/admin-metrics/serverless-admin-metrics.adoc

[id="serverless-broker-ingress-metrics_{context}"]
= Broker ingress metrics

You can use the following metrics to debug the broker ingress, see how it is performing, and see which events are being dispatched by the ingress component.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`event_count`
|Number of events received by a broker.
|Counter
|`broker_name`, `event_type`, `namespace_name`, `response_code`, `response_code_class`, `unique_name`
|Integer (no units)

|`event_dispatch_latencies`
|The time taken to dispatch an event to a channel.
|Histogram
|`broker_name`, `event_type`, `namespace_name`, `response_code`, `response_code_class`, `unique_name`
|Milliseconds
|===
// Module included in the following assemblies:
//
// * serverless/observability/admin-metrics/serverless-admin-metrics.adoc

[id="serverless-broker-filter-metrics_{context}"]
= Broker filter metrics

You can use the following metrics to debug broker filters, see how they are performing, and see which events are being dispatched by the filters. You can also measure the latency of the filtering action on an event.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`event_count`
|Number of events received by a broker.
|Counter
|`broker_name`, `container_name`, `filter_type`, `namespace_name`, `response_code`, `response_code_class`, `trigger_name`, `unique_name`
|Integer (no units)

|`event_dispatch_latencies`
|The time taken to dispatch an event to a channel.
|Histogram
|`broker_name`, `container_name`, `filter_type`, `namespace_name`, `response_code`, `response_code_class`, `trigger_name`, `unique_name`
|Milliseconds

|`event_processing_latencies`
|The time it takes to process an event before it is dispatched to a trigger subscriber.
|Histogram
|`broker_name`, `container_name`, `filter_type`, `namespace_name`, `trigger_name`, `unique_name`
|Milliseconds
|===
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-admin-metrics.adoc

[id="serverless-inmemory-dispatch-metrics_{context}"]
= InMemoryChannel dispatcher metrics

You can use the following metrics to debug `InMemoryChannel` channels, see how they are performing, and see which events are being dispatched by the channels.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`event_count`
|Number of events dispatched by `InMemoryChannel` channels.
|Counter
|`broker_name`, `container_name`, `filter_type`, `namespace_name`, `response_code`, `response_code_class`, `trigger_name`, `unique_name`
|Integer (no units)

|`event_dispatch_latencies`
|The time taken to dispatch an event from an `InMemoryChannel` channel.
|Histogram
|`broker_name`, `container_name`, `filter_type`, `namespace_name`, `response_code`, `response_code_class`, `trigger_name`, `unique_name`
|Milliseconds
|===
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-admin-metrics.adoc

[id="serverless-event-source-metrics_{context}"]
= Event source metrics

You can use the following metrics to verify that events have been delivered from the event source to the connected event sink.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`event_count`
|Number of events sent by the event source.
|Counter
|`broker_name`, `container_name`, `filter_type`, `namespace_name`, `response_code`, `response_code_class`, `trigger_name`, `unique_name`
|Integer (no units)

|`retry_event_count`
|Number of retried events sent by the event source after initially failing to be delivered.
|Counter
|`event_source`, `event_type`, `name`, `namespace_name`, `resource_group`, `response_code`, `response_code_class`, `response_error`, `response_timeout` |Integer (no units)
|===
