---
title: "Webhook metrics"
type: reference
domain: openshift
slug: serverless-4-22-serverless-webhook-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-webhook-metrics
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Webhook metrics

[id="serverless-webhook-metrics"]
= Webhook metrics

Webhook metrics report useful information about operations. For example, if a large number of operations fail, this might indicate an issue with a user-created resource.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`request_count`
|The number of requests that are routed to the webhook.
|Counter
|`admission_allowed`, `kind_group`, `kind_kind`, `kind_version`, `request_operation`, `resource_group`, `resource_namespace`, `resource_resource`, `resource_version`
|Integer (no units)

|`request_latencies`
|The response time for a webhook request.
|Histogram
|`admission_allowed`, `kind_group`, `kind_kind`, `kind_version`, `request_operation`, `resource_group`, `resource_namespace`, `resource_resource`, `resource_version`
|Milliseconds
|===
