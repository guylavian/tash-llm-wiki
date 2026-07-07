---
title: "List triggers from the command line"
type: reference
domain: openshift
slug: serverless-4-22-list-triggers-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/list-triggers-cli
version: 4.22
family: serverless
documentKind: "Documentation"
---

# List triggers from the command line

[id="list-triggers-cli"]
= List triggers from the command line

Using the Knative (`kn`) CLI to list triggers provides a streamlined and intuitive user interface.

// Module included in the following assemblies:
//
// * /serverless/eventing/triggers/list-triggers-cli.adoc

[id="kn-trigger-list_{context}"]
= Listing triggers by using the Knative CLI

You can use the `kn trigger list` command to list existing triggers in your cluster.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

. Print a list of available triggers:
+
[source,terminal]
----
$ kn trigger list
----
+
.Example output
[source,terminal]
----
NAME    BROKER    SINK           AGE   CONDITIONS   READY   REASON
email   default   ksvc:edisplay   4s    5 OK / 5     True
ping    default   ksvc:edisplay   32s   5 OK / 5     True
----

. Optional: Print a list of triggers in JSON format:
+
[source,terminal]
----
$ kn trigger list -o json
----
//example output?
