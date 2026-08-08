---
title: "Deleting triggers from the command line"
type: reference
domain: openshift
slug: serverless-4-22-delete-triggers-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/delete-triggers-cli
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Deleting triggers from the command line

[id="delete-triggers-cli"]
= Deleting triggers from the command line

Using the Knative (`kn`) CLI to delete a trigger provides a streamlined and intuitive user interface.

// Module included in the following assemblies:
//
// * /serverless/eventing/triggers/delete-triggers-cli.adoc

[id="delete-kn-trigger_{context}"]
= Deleting a trigger by using the Knative CLI

You can use the `kn trigger delete` command to delete a trigger.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Delete a trigger:
+
[source,terminal]
----
$ kn trigger delete <trigger_name>
----

.Verification

. List existing triggers:
+
[source,terminal]
----
$ kn trigger list
----

. Verify that the trigger no longer exists:
+
.Example output
[source,terminal]
----
No triggers found.
----
