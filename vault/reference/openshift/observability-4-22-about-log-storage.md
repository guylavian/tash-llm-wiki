---
title: "About log storage"
type: reference
domain: openshift
slug: observability-4-22-about-log-storage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/about-log-storage
version: 4.22
family: observability
documentKind: "Documentation"
---

# About log storage

[id="about-log-storage"]
= About log storage

You can use an internal Loki or Elasticsearch log store on your cluster for storing logs, or you can use a `ClusterLogForwarder` custom resource (CR) to forward logs to an external store.

[id="log-storage-overview-types"]
== Log storage types

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging.adoc

[id="cluster-logging-about-es-logstore_{context}"]
= About the Elasticsearch log store

The {logging} Elasticsearch instance is optimized and tested for short term storage, approximately seven days. If you want to retain your logs over a longer term, it is recommended you move the data to a third-party storage system.

Elasticsearch organizes the log data from Fluentd into datastores, or _indices_, then subdivides each index into multiple pieces called _shards_, which it spreads across a set of Elasticsearch nodes in an Elasticsearch cluster. You can configure Elasticsearch to make copies of the shards, called _replicas_, which Elasticsearch also spreads across the Elasticsearch nodes. The `ClusterLogging` custom resource (CR) allows you to specify how the shards are replicated to provide data redundancy and resilience to failure. You can also specify how long the different types of logs are retained using a retention policy in the `ClusterLogging` CR.

[NOTE]
====
The number of primary shards for the index templates is equal to the number of Elasticsearch data nodes.
====

The Red Hat OpenShift Logging Operator and companion OpenShift Elasticsearch Operator ensure that each Elasticsearch node is deployed using a unique deployment that includes its own storage volume.
You can use a `ClusterLogging` custom resource (CR) to increase the number of Elasticsearch nodes, as needed.
See the Elasticsearch documentation for considerations involved in configuring storage.

[NOTE]
====
A highly-available Elasticsearch environment requires at least three Elasticsearch nodes, each on a different host.
====

Role-based access control (RBAC) applied on the Elasticsearch indices enables the controlled access of the logs to the developers. Administrators can access all logs and developers can access only the logs in their projects.

[id="log-storage-overview-querying"]
== Querying log stores

You can query Loki by using the LogQL log query language.

[role="_additional-resources"]
[id="additional-resources_log-storage-overview"]
== Additional resources
* Loki components documentation
* Loki Object Storage documentation
