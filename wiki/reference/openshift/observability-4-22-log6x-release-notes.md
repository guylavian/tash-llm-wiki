---
title: "Logging 6.0.0"
type: reference
domain: openshift
slug: observability-4-22-log6x-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/log6x-release-notes
version: 4.22
family: observability
documentKind: "Documentation"
---

# Logging 6.0.0

[id="log6x-release-notes"]
= Logging 6.0.0

This release includes {logging-uc} {for} Bug Fix Release 6.0.0

.Upstream component versions
[options="header"]
|===

| {logging} Version 6+| Component Version

| Operator | `eventrouter` | `logfilemetricexporter` | `loki` | `lokistack-gateway` | `opa-openshift` | `vector`

|6.0 | 0.4 | 1.1 | 3.1.0 | 0.1 | 0.1 | 0.37.1

|===

[id="log6x-release-notes-6-0-0-removal-notice"]
== Removal notice

* With this release, {logging} no longer supports the `ClusterLogging.logging.openshift.io` and `ClusterLogForwarder.logging.openshift.io` custom resources. Refer to the product documentation for details on the replacement features. (LOG-5803)

* With this release, {logging} no longer manages or deploys log storage (such as Elasticsearch), visualization (such as Kibana), or Fluentd-based log collectors. (LOG-5368)

[NOTE]
====
In order to continue to use Elasticsearch and Kibana managed by the elasticsearch-operator, the administrator must modify those object's ownerRefs before deleting the ClusterLogging resource.
====

[id="log6x-release-notes-6-0-0-enhancements"]
== New features and enhancements

* This feature introduces a new architecture for {logging} {for} by shifting component responsibilities to their relevant Operators, such as for storage, visualization, and collection. It introduces the `ClusterLogForwarder.observability.openshift.io` API for log collection and forwarding. Support for the `ClusterLogging.logging.openshift.io` and `ClusterLogForwarder.logging.openshift.io` APIs, along with the Red Hat managed Elastic stack (Elasticsearch and Kibana), is removed. Users are encouraged to migrate to the Red Hat `LokiStack` for log storage. Existing managed Elasticsearch deployments can be used for a limited time. Automated migration for log collection is not provided, so administrators need to create a new ClusterLogForwarder.observability.openshift.io specification to replace their previous custom resources. Refer to the official product documentation for more details. (LOG-3493)

* With this release, the responsibility for deploying the {logging} view plugin shifts from the {clo} to the {coo-first}. For new log storage installations that need visualization, the {coo-full} and the associated `UIPlugin` resource must be deployed. For more information, see Visualization for logging. (LOG-5461)
+
--
--

* This enhancement sets default requests and limits for Vector collector deployments' memory and CPU usage based on Vector documentation recommendations. (LOG-4745)

* This enhancement updates Vector to align with the upstream version v0.37.1. (LOG-5296)

* This enhancement introduces an alert that triggers when log collectors buffer logs to a node's file system and use over 15% of the available space, indicating potential back pressure issues. (LOG-5381)

* This enhancement updates the selectors for all components to use common Kubernetes labels. (LOG-5906)

* This enhancement changes the collector configuration to deploy as a ConfigMap instead of a secret, allowing users to view and edit the configuration when the ClusterLogForwarder is set to Unmanaged. (LOG-5599)

* This enhancement adds the ability to configure the Vector collector log level using an annotation on the ClusterLogForwarder, with options including trace, debug, info, warn, error, or off. (LOG-5372)

* This enhancement adds validation to reject configurations where Amazon CloudWatch outputs use multiple AWS roles, preventing incorrect log routing. (LOG-5640)
* This enhancement removes the Log Bytes Collected and Log Bytes Sent graphs from the metrics dashboard. (LOG-5964)

* This enhancement updates the must-gather functionality to only capture information for inspecting Logging 6.0 components, including Vector deployments from ClusterLogForwarder.observability.openshift.io resources and the Red Hat managed LokiStack. (LOG-5949)

* This enhancement improves Azure storage secret validation by providing early warnings for specific error conditions. (LOG-4571)

[id="log6x-release-notes-6-0-0-technology-preview-features"]
== Technology Preview features

* This release introduces a Technology Preview feature for log forwarding using OpenTelemetry. A new output type,` OTLP`, allows sending JSON-encoded log records using the OpenTelemetry data model and resource semantic conventions. (LOG-4225)

[id="log6x-release-notes-6-0-0-bug-fixes"]
== Bug fixes

* Before this update, the `CollectorHighErrorRate` and `CollectorVeryHighErrorRate` alerts were still present. With this update, both alerts are removed in the {logging} 6.0 release but might return in a future release. (LOG-3432)

[id="log6x-release-notes-6-0-0-CVEs"]
== CVEs

* CVE-2024-34397
