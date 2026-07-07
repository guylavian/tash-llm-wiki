---
title: "Creating triggers"
type: reference
domain: openshift
slug: serverless-4-22-create-triggers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/create-triggers
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Creating triggers

[id="create-triggers"]
= Creating triggers

// Trigger
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-cluster-admin-eventing.adoc
// * serverless/eventing/triggers/create-trigger-admin.adoc

[id="serverless-creating-trigger-admin-web-console_{context}"]
= Creating a trigger by using the Administrator perspective

Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create a trigger. After Knative Eventing is installed on your cluster and you have created a broker, you can create a trigger by using the web console.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.

* You have logged in to the web console and are in the *Administrator* perspective.

* You have cluster administrator permissions for OpenShift Container Platform.

* You have cluster or dedicated administrator permissions for OpenShift Container Platform.

* You have created a Knative broker.

* You have created a Knative service to use as a subscriber.

.Procedure

. In the *Administrator* perspective of the OpenShift Container Platform web console, navigate to *Serverless* -> *Eventing*.
. In the *Broker* tab, select the Options menu {kebab} for the broker that you want to add a trigger to.
. Click *Add Trigger* in the list.
. In the *Add Trigger* dialogue box, select a *Subscriber* for the trigger. The subscriber is the Knative service that will receive events from the broker.
. Click *Add*.

// ODC
// Module included in the following assemblies:
//
// * /serverless/eventing/triggers/create-trigger-odc.adoc

[id="serverless-create-trigger-odc_{context}"]
= Creating a trigger by using the Developer perspective

Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create a trigger. After Knative Eventing is installed on your cluster and you have created a broker, you can create a trigger by using the web console.

.Prerequisites

* The {ServerlessOperatorName}, Knative Serving, and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have logged in to the web console.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have created a broker and a Knative service or other event sink to connect to the trigger.

.Procedure

. In the *Developer* perspective, navigate to the *Topology* page.
. Hover over the broker that you want to create a trigger for, and drag the arrow. The *Add Trigger* option is displayed.
. Click *Add Trigger*.
. Select your sink in the *Subscriber* list.
. Click *Add*.

.Verification

* After the subscription has been created, you can view it in the *Topology* page, where it is represented as a line that connects the broker to the event sink.

.Deleting a trigger
// should be a separate module; out of scope for this PR

. In the *Developer* perspective, navigate to the *Topology* page.
. Click on the trigger that you want to delete.
. In the *Actions* context menu, select *Delete Trigger*.

// kn trigger
// Module included in the following assemblies:
//
// * /serverless/eventing/triggers/create-trigger-cli.adoc

[id="serverless-create-kn-trigger_{context}"]
= Creating a trigger by using the Knative CLI

You can use the `kn trigger create` command to create a trigger.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Create a trigger:
+
[source,terminal]
----
$ kn trigger create <trigger_name> --broker <broker_name> --filter <key=value> --sink <sink_name>
----
+
Alternatively, you can create a trigger and simultaneously create the `default` broker using broker injection:
+
[source,terminal]
----
$ kn trigger create <trigger_name> --inject-broker --filter <key=value> --sink <sink_name>
----
+
By default, triggers forward all events sent to a broker to sinks that are subscribed to that broker.
Using the `--filter` attribute for triggers allows you to filter events from a broker, so that subscribers will only receive a subset of events based on your defined criteria.
