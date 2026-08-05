---
title: "Installing OpenShift KubeFed"
type: reference
domain: openshift
slug: kubefed-4-22-installing-kubefed
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/kubefed/installing-kubefed
version: 4.22
family: kubefed
documentKind: "Documentation"
---

# Installing OpenShift KubeFed

[id="installing-kubefed"]
= Installing OpenShift KubeFed

To get started with {KubeFedProductName}, you must create the `openshift-federation-system` namespace, install the Operator in this namespace, and then create the required custom resources (CRs) for your deployment.

NOTE: {KubeFedProductName} can be deployed as either a namespace-scoped or a cluster-scoped deployment, but not both, as this causes conflicts when both deployments attempt to manage the same set of resources.

[id="creating-federation-namespace_{context}"]
== Creating the namespace

You must create the `openshift-federation-system` namespace before installing any other {KubeFedProductName} components.

.Procedure

* Use the following command to create the namespace.
+
----
$ oc create ns openshift-federation-system
----

[id="installing-kubefed-operator_{context}"]
== Installing the {KubeFedProductName} Operator

You can install the {KubeFedProductName} Operator in the host cluster by following the OpenShift Container Platform instructions on installing an Operator.

For details, see the OpenShift Container Platform documentation on adding Operators to a cluster.

// Module included in the following assemblies:
//
// * kubefed/installing-kubefed.adoc

[id="creating-kubefed-CRs_{context}"]
= Creating KubeFed custom resources

You must create the `KubeFedWebHook` and `KubeFed` custom resources (CRs) for {KubeFedProductShortName} deployment.
The {KubeFedProductName} Operator creates the required custom resource definitions (CRDs) for these CRs automatically.

.Prerequisites
* You must have the `oc` CLI tool installed.

.Procedure

. Create a `KubeFedWebHook` resource to instantiate an admission webhook controller for {KubeFedProductShortName}. The namespace for this CR is `openshift-federation-system`.
+
----
$ cat <<-EOF | oc apply -n <namespace> -f -
 ---
 apiVersion: operator.kubefed.io/v1alpha1
 kind: KubeFedWebHook
 metadata:
   name: kubefed-webhook-resource
 spec:
---
----

. Create a `KubeFed` resource to drive the installation of {KubeFedProductShortName}. If you are planning to federate a cluster-scoped resource type, for example `StorageClass`, create this CR with `scope: Cluster`.
+
The namespace for this CR is `openshift-federation-system`, unless you are deploying namespace-scoped {KubeFedProductShortName}, in which case you can use the namespace(s) that you want to deploy {KubeFedProductShortName} to.
+
----
$ cat <<-EOF | oc apply -n <namespace> -f -
---
apiVersion: operator.kubefed.io/v1alpha1
kind: KubeFed
metadata:
  name: kubefed-resource
spec:
  scope: Cluster
---
----

[id="deleting-kubefed-operator_{context}"]
== Deleting the {KubeFedProductName} Operator

You can remove the {KubeFedProductName} Operator from the host cluster by following the OpenShift Container Platform instructions on deleting an Operator.

For details, see the OpenShift Container Platform documentation on deleting Operators from a cluster.
