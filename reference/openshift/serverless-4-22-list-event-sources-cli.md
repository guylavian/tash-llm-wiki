---
title: "Listing event sources from the command line"
type: reference
domain: openshift
slug: serverless-4-22-list-event-sources-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/list-event-sources-cli
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Listing event sources from the command line

[id="list-event-sources-cli"]
= Listing event sources from the command line

Using the Knative (`kn`) CLI provides a streamlined and intuitive user interface to view existing event sources on your cluster.

// move ODC to own section?
// Module included in the following assemblies:
//
// * serverless/eventing/discovery/list-event-sources-cli.adoc

[id="serverless-list-source-cli_{context}"]
= Listing available event sources by using the Knative CLI

You can list existing event sources by using the `kn source list` command.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

. List the existing event sources in the terminal:
+
[source,terminal]
----
$ kn source list
----
+
.Example output
[source,terminal]
----
NAME   TYPE              RESOURCE                               SINK         READY
a1     ApiServerSource   apiserversources.sources.knative.dev   ksvc:eshow2   True
b1     SinkBinding       sinkbindings.sources.knative.dev       ksvc:eshow3   False
p1     PingSource        pingsources.sources.knative.dev        ksvc:eshow1   True
----

. Optional: You can list event sources of a specific type only, by using the `--type` flag:
+
[source,terminal]
----
$ kn source list --type <event_source_type>
----
+
.Example command
[source,terminal]
----
$ kn source list --type PingSource
----
+
.Example output
[source,terminal]
----
NAME   TYPE              RESOURCE                               SINK         READY
p1     PingSource        pingsources.sources.knative.dev        ksvc:eshow1   True
----
