---
title: "Deleting {ServerlessProductName} custom resource definitions"
type: reference
domain: openshift
slug: serverless-4-22-deleting-serverless-crds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/deleting-serverless-crds
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Deleting {ServerlessProductName} custom resource definitions

[id="deleting-serverless-crds"]
= Deleting {ServerlessProductName} custom resource definitions

After uninstalling the {ServerlessProductName}, the Operator and API custom resource definitions (CRDs) remain on the cluster. You can use the following procedure to remove the remaining CRDs.

[IMPORTANT]
====
Removing the Operator and API CRDs also removes all resources that were defined by using them, including Knative services.
====

// deleting serverless CRDs
// Module included in the following assemblies:
//
//  * serverless/install/removing-openshift-serverless.adoc

[id="serverless-deleting-crds_{context}"]
= Removing {ServerlessProductName} Operator and API CRDs

Delete the Operator and API CRDs using the following procedure.

.Prerequisites

* Install the OpenShift CLI (`oc`).

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* You have uninstalled Knative Serving and removed the {ServerlessOperatorName}.

.Procedure

* To delete the remaining {ServerlessProductName} CRDs, enter the following command:
+
[source,terminal]
----
$ oc get crd -oname | grep 'knative.dev' | xargs oc delete
----
