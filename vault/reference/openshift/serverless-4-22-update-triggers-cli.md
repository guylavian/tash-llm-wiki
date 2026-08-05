---
title: "Updating triggers from the command line"
type: reference
domain: openshift
slug: serverless-4-22-update-triggers-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/update-triggers-cli
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Updating triggers from the command line

[id="update-triggers-cli"]
= Updating triggers from the command line

Using the Knative (`kn`) CLI to update triggers provides a streamlined and intuitive user interface.

// Module included in the following assemblies:
//
// * /serverless/develop/serverless-triggers.adoc

[id="kn-trigger-update_{context}"]
= Updating a trigger by using the Knative CLI

You can use the `kn trigger update` command with certain flags to update attributes for a trigger.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Update a trigger:
+
[source,terminal]
----
$ kn trigger update <trigger_name> --filter <key=value> --sink <sink_name> [flags]
----
** You can update a trigger to filter exact event attributes that match incoming events. For example, using the `type` attribute:
+
[source,terminal]
----
$ kn trigger update <trigger_name> --filter type=knative.dev.event
----
** You can remove a filter attribute from a trigger. For example, you can remove the filter attribute with key `type`:
+
[source,terminal]
----
$ kn trigger update <trigger_name> --filter type-
----
** You can use the `--sink` parameter to change the event sink of a trigger:
+
[source,terminal]
----
$ kn trigger update <trigger_name> --sink ksvc:my-event-sink
----
