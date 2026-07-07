---
title: "Event delivery"
type: reference
domain: openshift
slug: serverless-4-22-serverless-event-delivery
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-event-delivery
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Event delivery

[id="serverless-event-delivery"]
= Event delivery

You can configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. Configuring event delivery parameters, including a dead letter sink, ensures that any events that fail to be delivered to an event sink are retried. Otherwise, undelivered events are dropped.

// event delivery behavior of different component types, e.g. kafka
// Module included in the following assemblies:
//
// serverless/develop/serverless-event-delivery.adoc

[id="serverless-event-delivery-component-behaviors_{context}"]
= Event delivery behavior patterns for channels and brokers

Different channel and broker types have their own behavior patterns that are followed for event delivery.

[id="serverless-event-delivery-component-behaviors-kafka_{context}"]
== Knative channels and brokers for Apache Kafka

If an event is successfully delivered to a Kafka channel or broker receiver, the receiver responds with a `202` status code, which means that the event has been safely stored inside a Kafka topic and is not lost.

If the receiver responds with any other status code, the event is not safely stored, and steps must be taken by the user to resolve the issue.

// event delivery configurable parameters
// Module included in the following assemblies:
//
// serverless/develop/serverless-event-delivery.adoc

[id="serverless-event-delivery-parameters_{context}"]
= Configurable event delivery parameters

The following parameters can be configured for event delivery:

Dead letter sink:: You can configure the `deadLetterSink` delivery parameter so that if an event fails to be delivered, it is stored in the specified event sink. Undelivered events that are not stored in a dead letter sink are dropped. The dead letter sink be any addressable object that conforms to the Knative Eventing sink contract, such as a Knative service, a Kubernetes service, or a URI.

Retries:: You can set a minimum number of times that the delivery must be retried before the event is sent to the dead letter sink, by configuring the `retry` delivery parameter with an integer value.

Back off delay:: You can set the `backoffDelay` delivery parameter to specify the time delay before an event delivery retry is attempted after a failure. The duration of the `backoffDelay` parameter is specified using the https://en.wikipedia.org/wiki/ISO_8601#Durations[ISO 8601] format. For example, `PT1S` specifies a 1 second delay.

Back off policy:: The `backoffPolicy` delivery parameter can be used to specify the retry back off policy. The policy can be specified as either `linear` or `exponential`. When using the `linear` back off policy, the back off delay is equal to `backoffDelay * <numberOfRetries>`. When using the `exponential` backoff policy, the back off delay is equal to `backoffDelay*2^<numberOfRetries>`.

// configuring parameters examples
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-event-delivery.adoc

[id="serverless-configuring-event-delivery-examples_{context}"]
= Examples of configuring event delivery parameters

You can configure event delivery parameters for `Broker`, `Trigger`, `Channel`, and `Subscription` objects. If you configure event delivery parameters for a broker or channel, these parameters are propagated to triggers or subscriptions created for those objects. You can also set event delivery parameters for triggers or subscriptions to override the settings for the broker or channel.

.Example `Broker` object
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Broker
metadata:
...
spec:
  delivery:
    deadLetterSink:
      ref:
        apiVersion: eventing.knative.dev/v1alpha1
        kind: KafkaSink
        name: <sink_name>
    backoffDelay: <duration>
    backoffPolicy: <policy_type>
    retry: <integer>
...
----

.Example `Trigger` object
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Trigger
metadata:
...
spec:
  broker: <broker_name>
  delivery:
    deadLetterSink:
      ref:
        apiVersion: serving.knative.dev/v1
        kind: Service
        name: <sink_name>
    backoffDelay: <duration>
    backoffPolicy: <policy_type>
    retry: <integer>
...
----

.Example `Channel` object
[source,yaml]
----
apiVersion: messaging.knative.dev/v1
kind: Channel
metadata:
...
spec:
  delivery:
    deadLetterSink:
      ref:
        apiVersion: serving.knative.dev/v1
        kind: Service
        name: <sink_name>
    backoffDelay: <duration>
    backoffPolicy: <policy_type>
    retry: <integer>
...
----

.Example `Subscription` object
[source,yaml]
----
apiVersion: messaging.knative.dev/v1
kind: Subscription
metadata:
...
spec:
  channel:
    apiVersion: messaging.knative.dev/v1
    kind: Channel
    name: <channel_name>
  delivery:
    deadLetterSink:
      ref:
        apiVersion: serving.knative.dev/v1
        kind: Service
        name: <sink_name>
    backoffDelay: <duration>
    backoffPolicy: <policy_type>
    retry: <integer>
...
----

// event delivery ordering
// Module included in the following assemblies:
//
// * /serverless/develop/serverless-triggers.adoc

[id="trigger-event-delivery-config_{context}"]
= Configuring event delivery ordering for triggers

If you are using a Kafka broker, you can configure the delivery order of events from triggers to event sinks.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and Knative broker implementation for Apache Kafka are installed on your OpenShift Container Platform cluster.
* Kafka broker is enabled for use on your cluster, and you have created a Kafka broker.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have installed the OpenShift (`oc`) CLI.

.Procedure

. Create or modify a `Trigger` object and set the `kafka.eventing.knative.dev/delivery.order` annotation:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Trigger
metadata:
  name: <trigger_name>
  annotations:
     kafka.eventing.knative.dev/delivery.order: ordered
...
----
+
The supported consumer delivery guarantees are:
+
`unordered`:: An unordered consumer is a non-blocking consumer that delivers messages unordered, while preserving proper offset management.
+
`ordered`:: An ordered consumer is a per-partition blocking consumer that waits for a successful response from the CloudEvent subscriber before it delivers the next message of the partition.
+
The default ordering guarantee is `unordered`.

. Apply the `Trigger` object:
+
[source,terminal]
----
$ oc apply -f <filename>
----
