---
title: "Listing event source types from the command line"
type: reference
domain: openshift
slug: serverless-4-22-list-event-source-types-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/list-event-source-types-cli
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Listing event source types from the command line

[id="list-event-source-types-cli"]
= Listing event source types from the command line

Using the Knative (`kn`) CLI provides a streamlined and intuitive user interface to view available event source types on your cluster.

// Module included in the following assemblies:
//
// * serverless/develop/serverless-listing-event-sources.adoc

[id="serverless-list-source-types-kn_{context}"]
= Listing available event source types by using the Knative CLI

You can list event source types that can be created and used on your cluster by using the `kn source list-types` CLI command.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

. List the available event source types in the terminal:
+
[source,terminal]
----
$ kn source list-types
----
+
.Example output
[source,terminal]
----
TYPE              NAME                                            DESCRIPTION
ApiServerSource   apiserversources.sources.knative.dev            Watch and send Kubernetes API events to a sink
PingSource        pingsources.sources.knative.dev                 Periodically send ping events to a sink
SinkBinding       sinkbindings.sources.knative.dev                Binding for connecting a PodSpecable to a sink
----

. Optional: You can also list the available event source types in YAML format:
+
[source,terminal]
----
$ kn source list-types -o yaml
----
// optional step not allowed yet for OSD due to upstream https://github.com/knative/client/issues/1385
