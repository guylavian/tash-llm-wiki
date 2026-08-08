---
title: "Installing {kueue-name}"
type: reference
domain: openshift
slug: ai-workloads-4-22-install-kueue
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/install-kueue
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Installing {kueue-name}

[id="install-kueue"]
= Installing {kueue-name}

You can install {kueue-name} by using the {kueue-op} in OperatorHub.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/install-kueue.adoc
// * ai_workloads/kueue/install-disconnected.adoc
// * ai_workloads/kueue/release-notes.adoc

[id="compatible-environments_{context}"]
= Compatible environments

Before you install {kueue-name}, review this section to ensure that your cluster meets the requirements.

[id="compatible-environments-arch_{context}"]
== Supported architectures

{kueue-name} version 1.1 and later is supported on the following architectures:

* ARM64
* 64-bit x86
* ppc64le ({ibm-power-name})
* s390x ({ibm-z-name})

[id="compatible-environments-platforms_{context}"]
== Supported platforms

{kueue-name} version 1.1 and later is supported on the following platforms:

* OpenShift Container Platform
* {hcp-capital} for OpenShift Container Platform

[IMPORTANT]
====
Currently, {kueue-name} is not supported on {ms}.
====

// Module included in the following assemblies:
//
// * ai_workloads/kueue/install-kueue.adoc
// * ai_workloads/kueue/install-disconnected.adoc

[id="install-kueue-operator_{context}"]
= Installing the {kueue-op}

You can install the {kueue-op} on a OpenShift Container Platform cluster by using the OperatorHub in the web console.

.Prerequisites

* You have administrator permissions on a OpenShift Container Platform cluster.
* You have access to the OpenShift Container Platform web console.
* You have installed and configured the {cert-manager-operator} for your cluster.

.Procedure

. In the OpenShift Container Platform web console, click *Operators* -> *OperatorHub*.
. Choose *{kueue-op}* from the list of available Operators, and click *Install*.
. Select *Enable Operator recommended cluster monitoring on this Namespace*.
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the Namespace object.
You must select this option to ensure that cluster monitoring scrapes the `openshift-kueue-operator` namespace.
. Click *Install*.
+
[NOTE]
====
Alternatively, if you are creating the `Namespace` object by using YAML, ensure that you include the `openshift.io/cluster-monitoring: "true"` label:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
  name: openshift-kueue-operator
----
====

.Verification

* Go to *Operators* -> *Installed Operators* and confirm that the *{kueue-op}* is listed with *Status* as *Succeeded*.

[role="_additional-resources"]
.Additional resources
* Installing the {cert-manager-operator}

// Module included in the following assemblies:
//
// * ai_workloads/kueue/install-disconnected.adoc
// * ai_workloads/kueue/install-kueue.adoc

[id="upgrading-kueue_{context}"]
= Upgrading {kueue-name}

[role="_abstract"]
If you have previously installed {kueue-name}, you must manually upgrade your deployment to the latest version to use the latest bug fixes and feature enhancements.

.Prerequisites

* You have installed a previous version of {kueue-name}.
* You are logged in to the OpenShift Container Platform web console with cluster administrator permissions.

.Procedure

. In the OpenShift Container Platform web console, click *Operators* -> *Installed Operators*, then select *{kueue-name}* from the list.

. From the *Actions* drop-down menu, select *Uninstall Operator*.

. The *Uninstall Operator?* dialog box opens. Click *Uninstall*.
+
[IMPORTANT]
====
Selecting the *Delete all operand instances for this operator* checkbox before clicking *Uninstall* deletes all existing resources from the cluster, including:

* The `Kueue` CR
* Any cluster queues, local queues, or resource flavors that you have created

Leave this box unchecked when upgrading your cluster to retain your created resources.
====

. In the OpenShift Container Platform web console, click *Operators* -> *OperatorHub*.

. Choose *{kueue-op}* from the list of available Operators, and click *Install*.

.Verification

. Go to *Operators* -> *Installed Operators*.

. Confirm that the *{kueue-op}* is listed with *Status* as *Succeeded*.

. Confirm that the version shown under the Operator name in the list is the latest version.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/install-kueue.adoc
// * ai_workloads/kueue/install-disconnected.adoc

[id="create-kueue-cr_{context}"]
= Creating a Kueue custom resource

After you have installed the {kueue-op}, you must create a `Kueue` custom resource (CR) to configure your installation.

.Prerequisites

.Procedure

. In the OpenShift Container Platform web console, click *Operators* -> *Installed Operators*.
. In the *Provided APIs* table column, click *Kueue*. This takes you to the *Kueue* tab of the *Operator details* page.
. Click *Create Kueue*. This takes you to the *Create Kueue* YAML view.
. Enter the details for your `Kueue` CR.
+
.Example `Kueue` CR
[source,yaml]
----
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  labels:
    app.kubernetes.io/name: kueue-operator
    app.kubernetes.io/managed-by: kustomize
  name: cluster # <1>
  namespace: openshift-kueue-operator
spec:
  managementState: Managed
  config:
    integrations:
      frameworks: # <2>
      - BatchJob
    preemption:
      preemptionPolicy: Classical # <3>
# ...
----
<1> The name of the `Kueue` CR must be `cluster`.
<2> If you want to configure {kueue-name} for use with other workload types, add those types here.
The default configuration is `BatchJob`. Additional types are `Pod`, `Deployment`, and `StatefulSet`.
<3> Optional: If you want to configure fair sharing for {kueue-name}, set the `preemptionPolicy` value to `FairSharing`.
The default setting in the `Kueue` CR is `Classical` preemption.
// Once conceptual docs are added mention those docs here. "For more information about X, see..."

. Click *Create*.

.Verification

* After you create the `Kueue` CR, the web console brings you to the *Operator details* page, where you can see the CR in the list of *Kueues*.
* Optional: If you have the {oc-first} installed, you can run the following command and observe the output to confirm that your `Kueue` CR has been created successfully:
+
[source,terminal]
----
$ oc get kueue
----
+
.Example output
[source,terminal]
----
NAME      	AGE
cluster   	4m
----

// Module included in the following assemblies:
//
// * ai_workloads/kueue/install-kueue.adoc
// * ai_workloads/kueue/install-disconnected.adoc

[id="label-namespaces_{context}"]
= Labeling namespaces to allow {kueue-name} to manage jobs

The {kueue-name} Operator uses an opt-in webhook mechanism to ensure that policies are only enforced for the jobs and namespaces that it is expected to target.

You must label the namespaces where you want {kueue-name} to manage jobs with the `kueue.openshift.io/managed=true` label.

.Prerequisites

* You have cluster administrator permissions.
* The {kueue-name} Operator is installed on your cluster, and you have created a `Kueue` custom resource (CR).
* You have installed the {oc-first}.

.Procedure

* Add the `kueue.openshift.io/managed=true` label to a namespace by running the following command:
+
[source,terminal]
----
$ oc label namespace <namespace> kueue.openshift.io/managed=true
----

When you add this label, you instruct the {kueue-name} Operator that the namespace is managed by its webhook admission controllers. As a result, any {kueue-name} resources within that namespace are properly validated and mutated.
