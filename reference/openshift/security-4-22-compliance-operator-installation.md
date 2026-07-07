---
title: "Installing the Compliance Operator"
type: reference
domain: openshift
slug: security-4-22-compliance-operator-installation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/compliance-operator-installation
version: 4.22
family: security
documentKind: "Documentation"
---

# Installing the Compliance Operator

[id="compliance-operator-installation"]
= Installing the Compliance Operator

Before you can use the Compliance Operator, you must ensure it is deployed in the cluster.

[IMPORTANT]
====
All cluster nodes must have the same release version in order for this Operator to function properly.
As an example, for nodes running {op-system}, all nodes must have the same {op-system} version.
====

[IMPORTANT]
====
The Compliance Operator might report incorrect results on managed platforms, such as OpenShift Dedicated, Red{nbsp}Hat OpenShift Service on AWS Classic, and Microsoft Azure Red{nbsp}Hat OpenShift. For more information, see the Knowledgebase article Compliance Operator reports incorrect results on Managed Services.
====

[IMPORTANT]
====
Before deploying the Compliance Operator, you are required to define persistent storage in your cluster to store the raw results output. For more information, see Persistent storage overview and Managing the default storage class.
====

// Module included in the following assemblies:
//
// * security/compliance_operator/co-management/compliance-operator-installation.adoc

[id="installing-compliance-operator-web-console_{context}"]
= Installing the Compliance Operator through the web console

.Prerequisites

* You must have `admin` privileges.
* You must have a `StorageClass` resource configured.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.
. Search for the Compliance Operator, then click *Install*.
. Keep the default selection of *Installation mode* and *namespace* to ensure that the Operator will be installed to the `openshift-compliance` namespace.
. Click *Install*.

.Verification

To confirm that the installation is successful:

. Navigate to the *Ecosystem* -> *Installed Operators* page.
. Check that the Compliance Operator is installed in the `openshift-compliance` namespace and its status is `Succeeded`.

If the Operator is not installed successfully:

. Navigate to the *Ecosystem* -> *Installed Operators* page and inspect the `Status` column for any errors or failures.
. Navigate to the *Workloads* -> *Pods* page and check the logs in any pods in the `openshift-compliance` project that are reporting issues.

[IMPORTANT]
====
If the `restricted` Security Context Constraints (SCC) have been modified to contain the `system:authenticated` group or has added `requiredDropCapabilities`, the Compliance Operator may not function properly due to permissions issues.

You can create a custom SCC for the Compliance Operator scanner pod service account. For more information, see Creating a custom SCC for the Compliance Operator.
====

// Module included in the following assemblies:
//
// * security/compliance_operator/co-management/compliance-operator-installation.adoc

[id="installing-compliance-operator-cli_{context}"]
= Installing the Compliance Operator using the CLI

.Prerequisites

* You must have `admin` privileges.
* You must have a `StorageClass` resource configured.

.Procedure

. Define a `Namespace` object:
+
.Example `namespace-object.yaml`
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged <1>
  name: openshift-compliance
----
<1> In OpenShift Container Platform , the pod security label must be set to `privileged` at the namespace level.

. Create the `Namespace` object:
+
[source,terminal]
----
$ oc create -f namespace-object.yaml
----

. Define an `OperatorGroup` object:
+
.Example `operator-group-object.yaml`
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: compliance-operator
  namespace: openshift-compliance
spec:
  targetNamespaces:
  - openshift-compliance
----

. Create the `OperatorGroup` object:
+
[source,terminal]
----
$ oc create -f operator-group-object.yaml
----

. Define a `Subscription` object:
+
.Example `subscription-object.yaml`
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: compliance-operator-sub
  namespace: openshift-compliance
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: compliance-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----
. Create the `Subscription` object:
+
[source,terminal]
----
$ oc create -f subscription-object.yaml
----

[NOTE]
====
If you are setting the global scheduler feature and enable `defaultNodeSelector`, you must create the namespace manually and update the annotations of the `openshift-compliance` namespace, or the namespace where the Compliance Operator was installed, with `openshift.io/node-selector: “”`. This removes the default node selector and prevents deployment failures.
====

.Verification

. Verify the installation succeeded by inspecting the CSV file:
+
[source,terminal]
----
$ oc get csv -n openshift-compliance
----

. Verify that the Compliance Operator is up and running:
+
[source,terminal]
----
$ oc get deploy -n openshift-compliance
----

// Module included in the following assemblies:
//
// * security/compliance_operator/co-management/compliance-operator-installation.adoc

[id="installing-compliance-operator-rosa_{context}"]
= Installing the Compliance Operator on ROSA hosted control planes (HCP)

As of the Compliance Operator 1.5.0 release, the Operator is tested against {product-rosa} using {hcp-capital}.

{product-rosa} {hcp-capital} clusters have restricted access to the control plane, which is managed by Red{nbsp}Hat. By default, the Compliance Operator will schedule to nodes within the `master` node pool, which is not available in {product-rosa} {hcp-capital} installations. This requires you to configure the `Subscription` object in a way that allows the Operator to schedule on available node pools. This step is necessary for a successful installation on {product-rosa} {hcp-capital} clusters.

.Prerequisites

* You must have `admin` privileges.
* You must have a `StorageClass` resource configured.

.Procedure

. Define a `Namespace` object:
+
.Example `namespace-object.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged <1>
  name: openshift-compliance
----
<1> In OpenShift Container Platform , the pod security label must be set to `privileged` at the namespace level.

. Create the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc create -f namespace-object.yaml
----

. Define an `OperatorGroup` object:
+
.Example `operator-group-object.yaml` file
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: compliance-operator
  namespace: openshift-compliance
spec:
  targetNamespaces:
  - openshift-compliance
----

. Create the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc create -f operator-group-object.yaml
----

. Define a `Subscription` object:
+
.Example `subscription-object.yaml` file
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: compliance-operator-sub
  namespace: openshift-compliance
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: compliance-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  config:
    nodeSelector:
      node-role.kubernetes.io/worker: "" <1>
----
<1> Update the Operator deployment to deploy on `worker` nodes.

. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc create -f subscription-object.yaml
----

.Verification

. Verify that the installation succeeded by running the following command to inspect the cluster service version (CSV) file:
+
[source,terminal]
----
$ oc get csv -n openshift-compliance
----

. Verify that the Compliance Operator is up and running by using the following command:
+
[source,terminal]
----
$ oc get deploy -n openshift-compliance
----

[IMPORTANT]
====
If the `restricted` Security Context Constraints (SCC) have been modified to contain the `system:authenticated` group or has added `requiredDropCapabilities`, the Compliance Operator may not function properly due to permissions issues.

You can create a custom SCC for the Compliance Operator scanner pod service account. For more information, see Creating a custom SCC for the Compliance Operator.
====

// only applies to 4.11+
// Module included in the following assemblies:
//
// * security/compliance_operator/co-management/compliance-operator-installation.adoc

[id="installing-compliance-operator-hcp_{context}"]
= Installing the Compliance Operator on Hypershift {hcp}

The Compliance Operator can be installed in {hcp} using the software catalog by creating a `Subscription` file.

.Prerequisites

* You must have `admin` privileges.

.Procedure

. Define a `Namespace` object similar to the following:
+
.Example `namespace-object.yaml`
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged <1>
  name: openshift-compliance
----
<1> In OpenShift Container Platform , the pod security label must be set to `privileged` at the namespace level.

. Create the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc create -f namespace-object.yaml
----

. Define an `OperatorGroup` object:
+
.Example `operator-group-object.yaml`
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: compliance-operator
  namespace: openshift-compliance
spec:
  targetNamespaces:
  - openshift-compliance
----

. Create the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc create -f operator-group-object.yaml
----

. Define a `Subscription` object:
+
.Example `subscription-object.yaml`
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: compliance-operator-sub
  namespace: openshift-compliance
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: compliance-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  config:
    nodeSelector:
      node-role.kubernetes.io/worker: ""
    env:
    - name: PLATFORM
      value: "HyperShift"
----

. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc create -f subscription-object.yaml
----

.Verification

. Verify the installation succeeded by inspecting the CSV file by running the following command:
+
[source,terminal]
----
$ oc get csv -n openshift-compliance
----

. Verify that the Compliance Operator is up and running by running the following command:
+
[source,terminal]
----
$ oc get deploy -n openshift-compliance
----

[role="_additional-resources"]
.Additional resources

// 4.13+
// * {hcp-capital} overview
//
// 4.11-4.12, commenting out of 4.13-main
//* Overview of {hcp} (Technology Preview)

[id="additional-resources-installing-the-compliance-operator"]
[role="_additional-resources"]
== Additional resources

* Using Operator Lifecycle Manager in disconnected environments
