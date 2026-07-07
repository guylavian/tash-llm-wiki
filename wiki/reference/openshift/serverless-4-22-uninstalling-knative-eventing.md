---
title: "Uninstalling {ServerlessProductName} Knative Eventing"
type: reference
domain: openshift
slug: serverless-4-22-uninstalling-knative-eventing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/uninstalling-knative-eventing
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Uninstalling {ServerlessProductName} Knative Eventing

[id="uninstalling-knative-eventing"]
= Uninstalling {ServerlessProductName} Knative Eventing

Before you can remove the {ServerlessOperatorName}, you must remove Knative Eventing. To uninstall Knative Eventing, you must remove the `KnativeEventing` custom resource (CR) and delete the `knative-eventing` namespace.

// Uninstalling Knative Eventing
// Module included in the following assemblies:
//
// * serverless/removing/uninstalling-knative-eventing.adoc

[id="serverless-uninstalling-knative-eventing_{context}"]
= Uninstalling Knative Eventing

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* Install the OpenShift CLI (`oc`).

.Procedure

. Delete the `KnativeEventing` CR:
+
[source,terminal]
----
$ oc delete knativeeventings.operator.knative.dev knative-eventing -n knative-eventing
----

. After the command has completed and all pods have been removed from the `knative-eventing` namespace, delete the namespace:
+
[source,terminal]
----
$ oc delete namespace knative-eventing
----
