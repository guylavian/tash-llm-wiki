---
title: "Knative Eventing"
type: reference
domain: openshift
slug: serverless-4-22-about-knative-eventing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/about-knative-eventing
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Knative Eventing

[id="about-knative-eventing"]
= Knative Eventing

Knative Eventing on OpenShift Container Platform enables developers to use an event-driven architecture with serverless applications. An event-driven architecture is based on the concept of decoupled relationships between event producers and event consumers.

Event producers create events, and event _sinks_, or consumers, receive events. Knative Eventing uses standard HTTP POST requests to send and receive events between event producers and sinks. These events conform to the CloudEvents specifications, which enables creating, parsing, sending, and receiving events in any programming language.

Knative Eventing supports the following use cases:

Publish an event without creating a consumer:: You can send events to a broker as an HTTP POST, and use binding to decouple the destination configuration from your application that produces events.

Consume an event without creating a publisher:: You can use a trigger to consume events from a broker based on event attributes. The application receives events as an HTTP POST.

To enable delivery to multiple types of sinks, Knative Eventing defines the following generic interfaces that can be implemented by multiple Kubernetes resources:

Addressable resources:: Able to receive and acknowledge an event delivered over HTTP to an address defined in the `status.address.url` field of the event. The Kubernetes `Service` resource also satisfies the addressable interface.

Callable resources:: Able to receive an event delivered over HTTP and transform it, returning `0` or `1` new events in the HTTP response payload. These returned events may be further processed in the same way that events from an external event source are processed.

// Module is included in the following assemblies:
//
// serverless/about/about-knative-eventing.adoc

[id="serverless-kafka-developer_{context}"]
= Using the Knative broker for Apache Kafka

THe Knative broker implementation for Apache Kafka provides integration options for you to use supported versions of the Apache Kafka message streaming platform with {ServerlessProductName}. Kafka provides options for event source, channel, broker, and event sink capabilities.

// OCP
[NOTE]
====
The Knative broker implementation for Apache Kafka is not currently supported for {ibm-z-name} and {ibm-power-name}.
====

Knative broker for Apache Kafka provides additional options, such as:

* Kafka source
* Kafka channel
* Kafka broker
* Kafka sink

[id="additional-resources_about-knative-eventing"]
[role="_additional-resources"]
== Additional resources
* Installing the `KnativeKafka` custom resource.
* Red Hat AMQ Streams documentation
* Red Hat AMQ Streams TLS and SASL on Apache Kafka documentation
* Event delivery
