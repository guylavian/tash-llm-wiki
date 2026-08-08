---
title: "Uninstalling {ServerlessProductName} Knative Serving"
type: reference
domain: openshift
slug: serverless-4-22-uninstalling-knative-serving
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/uninstalling-knative-serving
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Uninstalling {ServerlessProductName} Knative Serving

[id="uninstalling-knative-serving"]
= Uninstalling {ServerlessProductName} Knative Serving

Before you can remove the {ServerlessOperatorName}, you must remove Knative Serving. To uninstall Knative Serving, you must remove the `KnativeServing` custom resource (CR) and delete the `knative-serving` namespace.

// Uninstalling Knative Serving
// Module included in the following assemblies:
//
// * serverless/install/removing-openshift-serverless.adoc

[id="serverless-uninstalling-knative-serving_{context}"]
= Uninstalling Knative Serving

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* Install the OpenShift CLI (`oc`).

.Procedure

. Delete the `KnativeServing` CR:
+
[source,terminal]
----
$ oc delete knativeservings.operator.knative.dev knative-serving -n knative-serving
----

. After the command has completed and all pods have been removed from the `knative-serving` namespace, delete the namespace:
+
[source,terminal]
----
$ oc delete namespace knative-serving
----
