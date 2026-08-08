---
title: "Broker types"
type: reference
domain: openshift
slug: serverless-4-22-serverless-broker-types
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-broker-types
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Broker types

[id="serverless-broker-types"]
= Broker types

Cluster administrators can set the default broker implementation for a cluster. When you create a broker, the default broker implementation is used, unless you provide set configurations in the `Broker` object.

[id="serverless-broker-types-default_{context}"]
== Default broker implementation for development purposes

Knative provides a default, channel-based broker implementation. This channel-based broker can be used for development and testing purposes, but does not provide adequate event delivery guarantees for production environments. The default broker is backed by the `InMemoryChannel` channel implementation by default.

If you want to use Apache Kafka to reduce network hops, use the Knative broker implementation for Apache Kafka. Do not configure the channel-based broker to be backed by the `KafkaChannel` channel implementation.

[id="serverless-broker-types-production_{context}"]
== Production-ready Knative broker implementation for Apache Kafka
