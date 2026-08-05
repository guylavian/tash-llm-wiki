---
title: "Event sources"
type: reference
domain: openshift
slug: serverless-4-22-knative-event-sources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/knative-event-sources
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Event sources

[id="knative-event-sources"]
= Event sources

A Knative _event source_ can be any Kubernetes object that generates or imports cloud events, and relays those events to another endpoint, known as a _sink_. Sourcing events is critical to developing a distributed system that reacts to events.

You can create and manage Knative event sources by using the *Developer* perspective in the OpenShift Container Platform web console, the Knative (`kn`) CLI, or by applying YAML files.

Currently, {ServerlessProductName} supports the following event source types:

API server source:: Brings Kubernetes API server events into Knative. The API server source sends a new event each time a Kubernetes resource is created, updated or deleted.

Ping source:: Produces events with a fixed payload on a specified cron schedule.

Kafka event source:: Connects an Apache Kafka cluster to a sink as an event source.

You can also create a custom event source.
