---
title: "Using functions with Knative Eventing"
type: reference
domain: openshift
slug: serverless-4-22-serverless-functions-eventing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-functions-eventing
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Using functions with Knative Eventing

[id="serverless-functions-eventing"]
= Using functions with Knative Eventing

Functions are deployed as Knative services on an OpenShift Container Platform cluster. You can connect functions to Knative Eventing components so that they can receive incoming events.

// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-eventing.adoc

[id="serverless-connect-func-source-odc_{context}"]
= Connect an event source to a function using the Developer perspective

Functions are deployed as Knative services on an OpenShift Container Platform cluster. When you create an event source by using the OpenShift Container Platform web console, you can specify a deployed function that events are sent to from that source.

.Prerequisites

* The {ServerlessOperatorName}, Knative Serving, and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have logged in to the web console and are in the *Developer* perspective.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You have created and deployed a function.

.Procedure

. Create an event source of any type, by navigating to *+Add* -> *Event Source* and selecting the event source type that you want to create.

. In the *Sink* section of the *Create Event Source* form view, select your function in the *Resource* list.

. Click *Create*.

.Verification

You can verify that the event source was created and is connected to the function by viewing the *Topology* page.

. In the *Developer* perspective, navigate to *Topology*.

. View the event source and click the connected function to see the function details in the right panel.
