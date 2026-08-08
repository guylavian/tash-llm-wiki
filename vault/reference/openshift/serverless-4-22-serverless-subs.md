---
title: "Creating subscriptions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-subs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-subs
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Creating subscriptions

[id="serverless-subs"]
= Creating subscriptions

After you have created a channel and an event sink, you can create a subscription to enable event delivery. Subscriptions are created by configuring a `Subscription` object, which specifies the channel and the sink (also known as a _subscriber_) to deliver events to.

// Subscription
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-cluster-admin-eventing.adoc

[id="serverless-creating-subscription-admin-web-console_{context}"]
= Creating a subscription by using the Administrator perspective

After you have created a channel and an event sink, also known as a _subscriber_, you can create a subscription to enable event delivery. Subscriptions are created by configuring a `Subscription` object, which specifies the channel and the subscriber to deliver events to. You can also specify some subscriber-specific options, such as how to handle failures.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.

* You have logged in to the web console and are in the *Administrator* perspective.

* You have cluster administrator permissions for OpenShift Container Platform.

* You have cluster or dedicated administrator permissions for OpenShift Container Platform.

* You have created a Knative channel.

* You have created a Knative service to use as a subscriber.

.Procedure

. In the *Administrator* perspective of the OpenShift Container Platform web console, navigate to *Serverless* -> *Eventing*.
. In the *Channel* tab, select the Options menu {kebab} for the channel that you want to add a subscription to.
. Click *Add Subscription* in the list.
. In the *Add Subscription* dialogue box, select a *Subscriber* for the subscription. The subscriber is the Knative service that receives events from the channel.
. Click *Add*.
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

[id="serverless-creating-subscriptions-odc_{context}"]
= Creating a subscription by using the Developer perspective

After you have created a channel and an event sink, you can create a subscription to enable event delivery. Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to create a subscription.

.Prerequisites

* The {ServerlessOperatorName}, Knative Serving, and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have logged in to the web console.
* You have created an event sink, such as a Knative service, and a channel.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. In the *Developer* perspective, navigate to the *Topology* page.

. Create a subscription using one of the following methods:

.. Hover over the channel that you want to create a subscription for, and drag the arrow. The *Add Subscription* option is displayed.
+
image::create-sub-ODC.png[Create a subscription for the channel]
+
... Select your sink in the *Subscriber* list.
... Click *Add*.
.. If the service is available in the *Topology* view under the same namespace or project as the channel, click on the channel that you want to create a subscription for, and drag the arrow directly to a service to immediately create a subscription from the channel to that service.

.Verification

* After the subscription has been created, you can see it represented as a line that connects the channel to the service in the *Topology* view:
+
image::verify-subscription-odc.png[Subscription in the Topology view]
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

[id="serverless-creating-subscriptions-yaml_{context}"]
= Creating a subscription by using YAML

After you have created a channel and an event sink, you can create a subscription to enable event delivery. Creating Knative resources by using YAML files uses a declarative API, which enables you to describe subscriptions declaratively and in a reproducible manner. To create a subscription by using YAML, you must create a YAML file that defines a `Subscription` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on the cluster.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Create a `Subscription` object:
** Create a YAML file and copy the following sample code into it:
+
[source,yaml]
----
apiVersion: messaging.knative.dev/v1beta1
kind: Subscription
metadata:
  name: my-subscription <1>
  namespace: default
spec:
  channel: <2>
    apiVersion: messaging.knative.dev/v1beta1
    kind: Channel
    name: example-channel
  delivery: <3>
    deadLetterSink:
      ref:
        apiVersion: serving.knative.dev/v1
        kind: Service
        name: error-handler
  subscriber: <4>
    ref:
      apiVersion: serving.knative.dev/v1
      kind: Service
      name: event-display
----
+
<1> Name of the subscription.
<2> Configuration settings for the channel that the subscription connects to.
<3> Configuration settings for event delivery. This tells the subscription what happens to events that cannot be delivered to the subscriber. When this is configured, events that failed to be consumed are sent to the `deadLetterSink`. The event is dropped, no re-delivery of the event is attempted, and an error is logged in the system. The `deadLetterSink` value must be a Destination.
<4> Configuration settings for the subscriber. This is the event sink that events are delivered to from the channel.
** Apply the YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

[id="serverless-creating-subscriptions-kn_{context}"]
= Creating a subscription by using the Knative CLI

After you have created a channel and an event sink, you can create a subscription to enable event delivery. Using the Knative (`kn`) CLI to create subscriptions provides a more streamlined and intuitive user interface than modifying YAML files directly. You can use the `kn subscription create` command with the appropriate flags to create a subscription.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Create a subscription to connect a sink to a channel:
+
[source,terminal]
----
$ kn subscription create <subscription_name> \
  --channel <group:version:kind>:<channel_name> \ <1>
  --sink <sink_prefix>:<sink_name> \ <2>
  --sink-dead-letter <sink_prefix>:<sink_name> <3>
----
<1> `--channel` specifies the source for cloud events that should be processed. You must provide the channel name. If you are not using the default `InMemoryChannel` channel that is backed by the `Channel` custom resource, you must prefix the channel name with the `<group:version:kind>` for the specified channel type. For example, this will be `messaging.knative.dev:v1beta1:KafkaChannel` for an Apache Kafka backed channel.
<2> `--sink` specifies the target destination to which the event should be delivered. By default, the `<sink_name>` is interpreted as a Knative service of this name, in the same namespace as the subscription. You can specify the type of the sink by using one of the following prefixes:
`ksvc`:: A Knative service.
`channel`:: A channel that should be used as destination. Only default channel types can be referenced here.
`broker`:: An Eventing broker.
<3> Optional: `--sink-dead-letter` is an optional flag that can be used to specify a sink which events should be sent to in cases where events fail to be delivered. For more information, see the {ServerlessProductName} _Event delivery_ documentation.
+
.Example command
[source,terminal]
----
$ kn subscription create mysubscription --channel mychannel --sink ksvc:event-display
----
+
.Example output
[source,terminal]
----
Subscription 'mysubscription' created in namespace 'default'.
----

.Verification

* To confirm that the channel is connected to the event sink, or _subscriber_, by a subscription, list the existing subscriptions and inspect the output:
+
[source,terminal]
----
$ kn subscription list
----
+
.Example output
[source,terminal]
----
NAME            CHANNEL             SUBSCRIBER           REPLY   DEAD LETTER SINK   READY   REASON
mysubscription   Channel:mychannel   ksvc:event-display                              True
----

.Deleting a subscription
// move to own procedure, out of scope for this PR
* Delete a subscription:
+
[source,terminal]
----
$ kn subscription delete <subscription_name>
----

[id="next-steps_serverless-subs"]
== Next steps
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See Examples of configuring event delivery parameters.
