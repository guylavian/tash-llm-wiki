---
title: "Uninstalling the SR-IOV Network Operator"
type: reference
domain: openshift
slug: networking-4-22-uninstalling-sriov-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/uninstalling-sriov-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Uninstalling the SR-IOV Network Operator

[id="uninstalling-sriov-operator"]
= Uninstalling the SR-IOV Network Operator

[role="_abstract"]
To uninstall the SR-IOV Network Operator, you must delete any running SR-IOV workloads, uninstall the Operator, and delete the webhooks that the Operator used.

// Module included in the following assemblies:
//
// * networking/hardware_networks/uninstalling-sriov-operator.adoc

[id="nw-sriov-operator-uninstall_{context}"]
= Uninstalling the SR-IOV Network Operator

[role="_abstract"]
You can remove the SR-IOV Network Operator from your cluster by uninstalling the Operator. This ensures that the Operator and its associated resources are deleted when you no longer need to manage SR-IOV network devices.

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have the SR-IOV Network Operator installed.

.Procedure

. Delete all SR-IOV custom resources (CRs):
+
[source,terminal]
----
$ oc delete sriovnetwork -n openshift-sriov-network-operator --all
----
+
[source,terminal]
----
$ oc delete sriovnetworknodepolicy -n openshift-sriov-network-operator --all
----
+
[source,terminal]
----
$ oc delete sriovibnetwork -n openshift-sriov-network-operator --all
----
+
[source,terminal]
----
$ oc delete sriovoperatorconfigs -n openshift-sriov-network-operator --all
----

. Follow the instructions in the "Deleting Operators from a cluster" section to remove the SR-IOV Network Operator from your cluster.

. Delete the SR-IOV custom resource definitions that remain in the cluster after the SR-IOV Network Operator is uninstalled:
+
[source,terminal]
----
$ oc delete crd sriovibnetworks.sriovnetwork.openshift.io
----
+
[source,terminal]
----
$ oc delete crd sriovnetworknodepolicies.sriovnetwork.openshift.io
----
+
[source,terminal]
----
$ oc delete crd sriovnetworknodestates.sriovnetwork.openshift.io
----
+
[source,terminal]
----
$ oc delete crd sriovnetworkpoolconfigs.sriovnetwork.openshift.io
----
+
[source,terminal]
----
$ oc delete crd sriovnetworks.sriovnetwork.openshift.io
----
+
[source,terminal]
----
$ oc delete crd sriovoperatorconfigs.sriovnetwork.openshift.io
----

. Delete the SR-IOV Network Operator namespace:
+
[source,terminal]
----
$ oc delete namespace openshift-sriov-network-operator
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Deleting Operators from a cluster
