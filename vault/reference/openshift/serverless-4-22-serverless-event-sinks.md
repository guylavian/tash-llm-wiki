---
title: "Event sinks"
type: reference
domain: openshift
slug: serverless-4-22-serverless-event-sinks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-event-sinks
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Event sinks

[id="serverless-event-sinks"]
= Event sinks

Addressable objects receive and acknowledge an event delivered over HTTP to an address defined in their `status.address.url` field. As a special case, the core Kubernetes `Service` object also fulfills the addressable interface.

Callable objects are able to receive an event delivered over HTTP and transform the event, returning `0` or `1` new events in the HTTP response. These returned events may be further processed in the same way that events from an external event source are processed.

// Using --sink flag with kn (generic)
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-event-sinks.adoc
// * serverless/eventing/event-sources/serverless-apiserversource.adoc
// * serverless/eventing/event-sources/serverless-custom-event-sources.adoc
// * serverless/develop/serverless-kafka-developer.adoc
// * serverless/reference/kn-flags-reference.adoc

[id="specifying-sink-flag-kn_{context}"]
= Knative CLI sink flag

When you create an event source by using the Knative (`kn`) CLI, you can specify a sink where events are sent to from that resource by using the `--sink` flag. The sink can be any addressable or callable resource that can receive incoming events from other resources.

The following example creates a sink binding that uses a service, `\http://event-display.svc.cluster.local`, as the sink:

.Example command using the sink flag
[source,terminal]
----
$ kn source binding create bind-heartbeat \
  --namespace sinkbinding-example \
  --subject "Job:batch/v1:app=heartbeat-cron" \
  --sink http://event-display.svc.cluster.local \ <1>
  --ce-override "sink=bound"
----
<1> `svc` in `\http://event-display.svc.cluster.local` determines that the sink is a Knative service. Other default sink prefixes include `channel`, and `broker`.

[TIP]
====
You can configure which CRs can be used with the `--sink` flag for Knative (`kn`) CLI commands by Customizing `kn`.
====
