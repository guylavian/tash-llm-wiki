---
title: "Installing {VirtProductName}"
type: reference
domain: openshift
slug: virt-4-22-installing-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/installing-virt
version: 4.22
family: virt
documentKind: "Documentation"
---

# Installing {VirtProductName}

[id="installing-virt"]
= Installing {VirtProductName}

[role="_abstract"]
Install {VirtProductName} to add virtualization functionality to your OpenShift Container Platform cluster.

[IMPORTANT]
====
If you install {VirtProductName} in a restricted environment with no internet connectivity, you must configure {olm-first} for a disconnected environment.

If you have limited internet connectivity, you can configure proxy support in {olm} to access the software catalog.
====

// Module included in the following assemblies:
//
// * virt/install/installing-virt.adoc

[id="virt-installing-virt-operator_{context}"]
= Installing the {VirtProductName} Operator by using the web console

[role="_abstract"]
You can deploy the {VirtProductName} Operator by using the OpenShift Container Platform web console.

.Prerequisites

* Install OpenShift Container Platform  on your cluster.
* Log in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.
// required for ROSA/OSD
* Create a machine pool based on a bare metal compute node instance type. For more information, see "Creating a machine pool" in the Additional resources of this section.

.Procedure

. From the *Administrator* perspective, click *Ecosystem* -> *Software Catalog*.

. In the *Filter by keyword* field, type *Virtualization*.

. Select the *{CNVOperatorDisplayName}* tile with the *Red Hat* source label.

. Read the information about the Operator and click *Install*.

. On the *Install Operator* page:

.. Select *stable* from the list of available *Update Channel* options. This ensures that you install the version of {VirtProductName} that is compatible with your OpenShift Container Platform version.

.. For *Installed Namespace*, ensure that the *Operator recommended namespace* option is selected. This installs the Operator in the mandatory `{CNVNamespace}` namespace, which is automatically created if it does not exist.
+
[WARNING]
====
Attempting to install the {VirtProductName} Operator in a namespace other than `{CNVNamespace}` causes the installation to fail.
====

.. For *Approval Strategy*, it is highly recommended that you select *Automatic*, which is the default value, so that {VirtProductName} automatically updates when a new version is available in the *stable* update channel.
+
Selecting the *Manual* approval strategy is not recommended, as it poses a high risk to cluster support and functionality. Only select *Manual* if you fully understand these risks and cannot use *Automatic*.
+
[WARNING]
====
Because {VirtProductName} is only supported when used with the corresponding OpenShift Container Platform version, missing {VirtProductName} updates can cause your cluster to become unsupported.
====

. Click *Install* to make the Operator available to the `{CNVNamespace}` namespace.

. When the Operator installs successfully, click *Create HyperConverged*.

. Optional: Configure *Infra* and *Workloads* node placement options for {VirtProductName} components.

. Click *Create* to launch {VirtProductName}.

.Verification

* Navigate to the *Workloads* -> *Pods* page and monitor the {VirtProductName} pods until they are all *Running*. After all the pods display the *Running* state, you can use {VirtProductName}.
// Module included in the following assemblies:
//
// * virt/install/installing-virt.adoc

[id="virt-subscribing-cli_{context}"]
= Subscribing to the {VirtProductName} catalog by using the CLI

[role="_abstract"]
Before you install {VirtProductName}, you must subscribe to the {VirtProductName} catalog. Subscribing gives the `{CNVNamespace}` namespace access to the {VirtProductName} Operators.

To subscribe, configure `Namespace`, `OperatorGroup`, and `Subscription` objects by applying a single manifest to your cluster.

.Prerequisites

* Install OpenShift Container Platform  on your cluster.
* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a YAML file that contains the following manifest:
//Note that there are two versions of the following YAML file; the first one is for openshift-enterprise and the second is for openshift-origin (aka OKD).
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Namespace
metadata:
  name: {CNVNamespace}
  labels:
    openshift.io/cluster-monitoring: "true"
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: kubevirt-hyperconverged-group
  namespace: {CNVNamespace}
spec:
  targetNamespaces:
    - {CNVNamespace}
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: hco-operatorhub
  namespace: {CNVNamespace}
spec:
  source: {CNVSubscriptionSpecSource}
  sourceNamespace: openshift-marketplace
  name: {CNVSubscriptionSpecName}
  startingCSV: kubevirt-hyperconverged-operator.v{HCOVersion}
  channel: "stable"
----
+
Using the `stable` channel ensures that you install the version of
{VirtProductName} that is compatible with your OpenShift Container Platform version.

. Create a YAML file that contains the following manifest:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Namespace
metadata:
  name: {CNVNamespace}
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: kubevirt-hyperconverged-group
  namespace: {CNVNamespace}
spec: {}
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: hco-operatorhub
  namespace: {CNVNamespace}
spec:
  source: {CNVSubscriptionSpecSource}
  sourceNamespace: openshift-marketplace
  name: {CNVSubscriptionSpecName}
  startingCSV: kubevirt-hyperconverged-operator.v{HCOVersion}
  channel: "stable"
----
+
Using the `stable` channel ensures that you install the version of
{VirtProductName} that is compatible with your OpenShift Container Platform version.

. Create the required `Namespace`, `OperatorGroup`, and `Subscription` objects
for {VirtProductName} by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

You must verify that the subscription creation was successful before you can proceed with installing {VirtProductName}.

. Check that the `ClusterServiceVersion` (CSV) object was created successfully. Run the following command and verify the output:
+
[source,terminal,subs="attributes+"]
----
$ oc get csv -n {CNVNamespace}
----
+
If the CSV was created successfully, the output shows an entry that contains a `NAME` value of `kubevirt-hyperconverged-operator-*`, a `DISPLAY` value of `{VirtProductName}`, and a `PHASE` value of `Succeeded`, as shown in the following example output:
+
Example output:
+
[source,terminal,subs="attributes+"]
----
NAME                                       DISPLAY                    VERSION   REPLACES                                   PHASE
kubevirt-hyperconverged-operator.v{HCOVersion}   {VirtProductName}   {HCOVersion}    kubevirt-hyperconverged-operator.v{HCOVersionPrev}   Succeeded
----

. Check that the `HyperConverged` custom resource (CR) has the correct version. Run the following command and verify the output:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} -n {CNVNamespace} kubevirt-hyperconverged -o json | jq .status.versions
----
+
Example output:
+
[source,terminal,subs="attributes+"]
----
{
"name": "operator",
"version": "{HCOVersion}"
}
----

. Verify the `HyperConverged` CR conditions. Run the following command and check the output:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} -o json | jq -r '.status.conditions[] | {type,status}'
----
+
Example output:
+
[source,terminal]
----
{
  "type": "ReconcileComplete",
  "status": "True"
}
{
  "type": "Available",
  "status": "True"
}
{
  "type": "Progressing",
  "status": "False"
}
{
  "type": "Degraded",
  "status": "False"
}
{
  "type": "Upgradeable",
  "status": "True"
}
----
// Module included in the following assemblies:
//
// * virt/install/installing-virt.adoc

[id="virt-deploying-operator-cli_{context}"]
= Deploying the {VirtProductName} Operator by using the CLI

[role="_abstract"]
You can deploy the {VirtProductName} Operator by using the `oc` CLI.

.Prerequisites

* Install the {oc-first}.
* Subscribe to the {VirtProductName} catalog in the `{CNVNamespace}` namespace.
* Log in as a user with `cluster-admin` privileges.
// required for ROSA/OSD
* Create a machine pool based on a bare metal compute node instance type.

.Procedure

. Create a YAML file that contains the following manifest:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
----

. Deploy the {VirtProductName} Operator by running the following command:
+
[source,terminal]
----
$ oc apply -f <file_name>.yaml
----

.Verification

* Ensure that {VirtProductName} deployed successfully by watching the `PHASE` of the cluster service version (CSV) in the `{CNVNamespace}` namespace. Run the following command:
+
[source,terminal,subs="attributes+"]
----
$ watch oc get csv -n {CNVNamespace}
----
+
The following output displays if deployment was successful:
+
[source,terminal,subs="attributes+"]
----
NAME                                      DISPLAY                    VERSION   REPLACES   PHASE
kubevirt-hyperconverged-operator.v{HCOVersion}   {VirtProductName}   {HCOVersion}                Succeeded
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Using Operator Lifecycle Manager in disconnected environments
* Configuring proxy support in Operator Lifecycle Manager
* Self validation checkup
* Creating a machine pool
* Creating a machine pool
* Configure certificate rotation
* Creating a hostpath provisioner with a basic storage pool
