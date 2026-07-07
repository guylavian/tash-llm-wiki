---
title: "Installing the SR-IOV Network Operator"
type: reference
domain: openshift
slug: networking-4-22-installing-sriov-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/installing-sriov-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Installing the SR-IOV Network Operator

[id="installing-sriov-operator"]
= Installing the SR-IOV Network Operator

[role="_abstract"]
To manage SR-IOV network devices and network attachments on your cluster, install the Single Root I/O Virtualization (SR-IOV) Network Operator. By using this Operator, you can centralize the configuration and lifecycle management of your SR-IOV resources.

As a cluster administrator, you can install the Single Root I/O Virtualization (SR-IOV) Network Operator by using the OpenShift Container Platform CLI or the web console.

// Using the CLI to install the SR-IOV Network Operator
// Module included in the following assemblies:
//
// * networking/hardware_networks/installing-sriov-operator.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

[id="install-operator-cli_{context}"]
= Using the CLI to install the SR-IOV Network Operator

[role="_abstract"]
You can use the CLI to install the SR-IOV Network Operator. By using the CLI, you can deploy the Operator directly from your terminal to manage SR-IOV network devices and attachments without navigating the web console.

.Prerequisites

* You installed the {oc-first}.
* You have an account with `cluster-admin` privileges.
* You installed a cluster on bare-metal hardware, and you ensured that cluster nodes have hardware that supports SR-IOV.

.Procedure

. Create the `openshift-sriov-network-operator` namespace by entering the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-sriov-network-operator
  annotations:
    workload.openshift.io/allowed: management
EOF
----

. Create an `OperatorGroup` custom resource (CR) by entering the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: sriov-network-operators
  namespace: openshift-sriov-network-operator
spec:
  targetNamespaces:
  - openshift-sriov-network-operator
EOF
----

. Create a `Subscription` CR for the SR-IOV Network Operator by entering the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: sriov-network-operator-subscription
  namespace: openshift-sriov-network-operator
spec:
  channel: stable
  name: sriov-network-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
----

. Create an `SriovoperatorConfig` resource by entering the following command:
+
[source,terminal]
----
$ cat <<EOF | oc create -f -
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  enableInjector: true
  enableOperatorWebhook: true
  logLevel: 2
  disableDrain: false
EOF
----

.Verification

* To verify that the Operator is installed, enter the following command and then check that the output shows `Succeeded` for the Operator:
+
[source,terminal]
----
$ oc get csv -n openshift-sriov-network-operator \
  -o custom-columns=Name:.metadata.name,Phase:.status.phase
----

//
// Module included in the following assemblies:
//
// * networking/hardware_networks/installing-sriov-operator.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

[id="nw-sriov-installing-operator-web-console_{context}"]
= Using the web console to install the SR-IOV Network Operator

[role="_abstract"]
You can use the web console to install the SR-IOV Network Operator. By using the web console, you can deploy the Operator and manage SR-IOV network devices and attachments directly from a graphical interface without having to use the CLI.

.Prerequisites

* You have an account with `cluster-admin` privileges.
* You installed a cluster on bare-metal hardware, and you ensured that cluster nodes have hardware that supports SR-IOV.

.Procedure

. Install the SR-IOV Network Operator:
+
.. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.
+
.. Select *SR-IOV Network Operator* from the list of available Operators, and then click *Install*.
+
.. On the *Install Operator* page, under *Installed Namespace*, select *Operator recommended Namespace*.
+
.. Click *Install*.

.Verification

. Navigate to the *Ecosystem* -> *Installed Operators* page.

. Ensure that *SR-IOV Network Operator* is listed in the *openshift-sriov-network-operator* project with a *Status* of *InstallSucceeded*.
+
[NOTE]
====
During installation an Operator might display a *Failed* status. If the installation later succeeds with an *InstallSucceeded* message, you can ignore the *Failed* message.
====

. If the Operator does not show as installed, complete any of the following steps to troubleshoot the issue:
+
* Inspect the *Operator Subscriptions* and *Install Plans* tabs for any failure or errors under *Status*.
* Navigate to the *Workloads* -> *Pods* page and check the logs for pods in the `openshift-sriov-network-operator` project.
* Check the namespace of the YAML file. If the annotation is missing, you can add the annotation `workload.openshift.io/allowed=management` to the Operator namespace with the following command:
+
[source,terminal]
----
$ oc annotate ns/openshift-sriov-network-operator workload.openshift.io/allowed=management
----
+
[NOTE]
====
For {sno} clusters, the annotation `workload.openshift.io/allowed=management` is required for the namespace.
====

[role="_additional-resources_installing-sriov-operator.adoc"]
[id="additional-resources_{context}"]
== Additional resources

* Configuring the SR-IOV Network Operator
