---
title: "Listing event source types from the Developer perspective"
type: reference
domain: openshift
slug: serverless-4-22-list-event-source-types-odc
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/list-event-source-types-odc
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Listing event source types from the Developer perspective

[id="list-event-source-types-odc"]
= Listing event source types from the Developer perspective

It is possible to view a list of all available event source types on your cluster. Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to view available event source types.

// Module included in the following assemblies:
//
// * serverless/eventing/discovery/list-event-sources.adoc

[id="serverless-list-source-types-odc_{context}"]
= Viewing available event source types within the Developer perspective

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* The {ServerlessOperatorName} and Knative Eventing are installed on your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

. Access the *Developer* perspective.
. Click *+Add*.
. Click *Event Source*.
. View the available event source types.
