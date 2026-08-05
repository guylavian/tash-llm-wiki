---
title: "Event source in the Administrator perspective"
type: reference
domain: openshift
slug: serverless-4-22-event-source-admin-perspective
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/event-source-admin-perspective
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Event source in the Administrator perspective

[id="event-source-admin-perspective"]
= Event source in the Administrator perspective

Sourcing events is critical to developing a distributed system that reacts to events.

// Event sources
// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-cluster-admin-eventing.adoc

[id="serverless-creating-event-source-admin-web-console_{context}"]
= Creating an event source by using the Administrator perspective

A Knative _event source_ can be any Kubernetes object that generates or imports cloud events, and relays those events to another endpoint, known as a _sink_.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.

* You have logged in to the web console and are in the *Administrator* perspective.

* You have cluster administrator permissions for OpenShift Container Platform.

* You have cluster or dedicated administrator permissions for OpenShift Container Platform.

.Procedure

. In the *Administrator* perspective of the OpenShift Container Platform web console, navigate to *Serverless* -> *Eventing*.
. In the *Create* list, select *Event Source*. You will be directed to the *Event Sources* page.
. Select the event source type that you want to create.
