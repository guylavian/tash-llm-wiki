---
title: "Creating channels"
type: reference
domain: openshift
slug: serverless-4-22-serverless-creating-channels
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-creating-channels
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Creating channels

[id="serverless-creating-channels"]
= Creating channels

// Channel
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-cluster-admin-eventing.adoc

[id="serverless-creating-channel-admin-web-console_{context}"]
= Creating a channel by using the Administrator perspective

After Knative Eventing is installed on your cluster, you can create a channel by using the Administrator perspective.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.

* You have logged in to the web console and are in the *Administrator* perspective.

* You have cluster administrator permissions for OpenShift Container Platform.

* You have cluster or dedicated administrator permissions for OpenShift Container Platform.

.Procedure

. In the *Administrator* perspective of the OpenShift Container Platform web console, navigate to *Serverless* -> *Eventing*.
. In the *Create* list, select *Channel*. You will be directed to the *Channel* page.
. Select the type of `Channel` object that you want to create in the *Type* list.
+
[NOTE]
====
Currently only `InMemoryChannel` channel objects are supported by default. Knative channels for Apache Kafka are available if you have installed the Knative broker implementation for Apache Kafka on {ServerlessProductName}.
====
. Click *Create*.
// Module included in the following assemblies:
//
//  * /serverless/develop/serverless-creating-channels.adoc

[id="serverless-create-channel-odc_{context}"]
= Creating a channel by using the Developer perspective

Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create a channel. After Knative Eventing is installed on your cluster, you can create a channel by using the web console.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. In the *Developer* perspective, navigate to *+Add* -> *Channel*.
. Select the type of `Channel` object that you want to create in the *Type* list.
. Click *Create*.

.Verification

* Confirm that the channel now exists by navigating to the *Topology* page.
+
image::verify-channel-odc.png[View the channel in the Topology view]
// Module included in the following assemblies:
//
//  * /serverless/develop/serverless-creating-channels.adoc

[id="serverless-create-channel-kn_{context}"]
= Creating a channel by using the Knative CLI

Using the Knative (`kn`) CLI to create channels provides a more streamlined and intuitive user interface than modifying YAML files directly. You can use the `kn channel create` command to create a channel.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Create a channel:
+
[source,terminal]
----
$ kn channel create <channel_name> --type <channel_type>
----
+
The channel type is optional, but where specified, must be given in the format `Group:Version:Kind`.
For example, you can create an `InMemoryChannel` object:
+
[source,terminal]
----
$ kn channel create mychannel --type messaging.knative.dev:v1:InMemoryChannel
----
+
.Example output
[source,terminal]
----
Channel 'mychannel' created in namespace 'default'.
----

.Verification

* To confirm that the channel now exists, list the existing channels and inspect the output:
+
[source,terminal]
----
$ kn channel list
----
+
.Example output
[source,terminal]
----
kn channel list
NAME        TYPE              URL                                                     AGE   READY   REASON
mychannel   InMemoryChannel   http://mychannel-kn-channel.default.svc.cluster.local   93s   True
----

.Deleting a channel
// split into own module, out of scope for this PR
* Delete a channel:
+
[source,terminal]
----
$ kn channel delete <channel_name>
----
// Module included in the following assemblies:
//
//  * /serverless/develop/serverless-creating-channels.adoc

[id="serverless-create-default-channel-yaml_{context}"]
= Creating a default implementation channel by using YAML

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe channels declaratively and in a reproducible manner. To create a serverless channel by using YAML, you must create a YAML file that defines a `Channel` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. Create a `Channel` object as a YAML file:
+
[source,yaml]
----
apiVersion: messaging.knative.dev/v1
kind: Channel
metadata:
  name: example-channel
  namespace: default
----

. Apply the YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----
// Module included in the following assemblies:
//
//  * serverless/develop/serverless-creating-channels.adoc
//  * serverless/develop/serverless-kafka-developer.adoc

[id="serverless-create-kafka-channel-yaml_{context}"]
= Creating a channel for Apache Kafka by using YAML

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe channels declaratively and in a reproducible manner. You can create a Knative Eventing channel that is backed by Kafka topics by creating a Kafka channel. To create a Kafka channel by using YAML, you must create a YAML file that defines a `KafkaChannel` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource are installed on your OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. Create a `KafkaChannel` object as a YAML file:
+
[source,yaml]
----
apiVersion: messaging.knative.dev/v1beta1
kind: KafkaChannel
metadata:
  name: example-channel
  namespace: default
spec:
  numPartitions: 3
  replicationFactor: 1
----
+
[IMPORTANT]
====
Only the `v1beta1` version of the API for `KafkaChannel` objects on {ServerlessProductName} is supported. Do not use the `v1alpha1` version of this API, as this version is now deprecated.
====

. Apply the `KafkaChannel` YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----

[id="next-steps_serverless-creating-channels"]
== Next steps

* After you have created a channel, you can connect the channel to a sink so that the sink can receive events.
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See Examples of configuring event delivery parameters.
