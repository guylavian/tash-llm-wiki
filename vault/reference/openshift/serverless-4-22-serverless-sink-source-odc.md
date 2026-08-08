---
title: "Connecting an event source to a sink using the Developer perspective"
type: reference
domain: openshift
slug: serverless-4-22-serverless-sink-source-odc
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-sink-source-odc
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Connecting an event source to a sink using the Developer perspective

[id="serverless-sink-source-odc"]
= Connecting an event source to a sink using the Developer perspective

When you create an event source by using the OpenShift Container Platform web console, you can specify a sink that events are sent to from that source. The sink can be any addressable or callable resource that can receive incoming events from other resources.

// Connect sinks to sources in ODC
// Module included in the following assemblies:
//
// * serverless/eventing/event-sources/serverless-sink-source-odc.adoc

[id="serverless-connect-sink-source-odc_{context}"]
= Connect an event source to a sink using the Developer perspective

.Prerequisites

* The {ServerlessOperatorName}, Knative Serving, and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have logged in to the web console and are in the *Developer* perspective.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have created a sink, such as a Knative service, channel or broker.

.Procedure

. Create an event source of any type, by navigating to *+Add* -> *Event Source* and selecting the event source type that you want to create.

. In the *Sink* section of the *Create Event Source* form view, select your sink in the *Resource* list.

. Click *Create*.

.Verification

You can verify that the event source was created and is connected to the sink by viewing the *Topology* page.

. In the *Developer* perspective, navigate to *Topology*.

. View the event source and click the connected sink to see the sink details in the right panel.
