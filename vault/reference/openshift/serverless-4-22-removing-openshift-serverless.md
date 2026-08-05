---
title: "Removing {ServerlessProductName} overview"
type: reference
domain: openshift
slug: serverless-4-22-removing-openshift-serverless
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/removing-openshift-serverless
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Removing {ServerlessProductName} overview

[id="removing-openshift-serverless"]
= Removing {ServerlessProductName} overview

If you need to remove {ServerlessProductName} from your cluster, you can do so by manually removing the {ServerlessOperatorName} and other {ServerlessProductName} components. Before you can remove the {ServerlessOperatorName}, you must remove Knative Serving and Knative Eventing.

After uninstalling the {ServerlessProductName}, you can remove the Operator and API custom resource definitions (CRDs) that remain on the cluster.

The steps for fully removing {ServerlessProductName} are detailed in the following procedures:

* Uninstalling Knative Eventing.
* Uninstalling Knative Serving.
* Removing the {ServerlessOperatorName}.
* Deleting {ServerlessProductName} custom resource definitions.
