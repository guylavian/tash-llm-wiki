---
title: "Windows node updates"
type: reference
domain: openshift
slug: windows-containers-4-22-windows-node-upgrades
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/windows-node-upgrades
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Windows node updates

[id="windows-node-upgrades"]
= Windows node updates

[role="_abstract"]
You can ensure your Windows nodes have the latest updates by updating the Windows Machine Config Operator (WMCO).

You can update the WMCO in any of the following scenarios:

* Within the current version. for example, from <10.y.z> to <10.y.z+1>.
* To a new, contiguous version. For example, from <10.y> to <10.y+1>.
* From an EUS version to another EUS version by using a Control Plane Only update. For example, from <10.y> to <10.y+2>.

// Module included in the following assemblies:
//
// * windows_containers/windows-node-upgrades.adoc

[id="wmco-upgrades_{context}"]
= Windows Machine Config Operator updates

[role="_abstract"]
When a new version of the Windows Machine Config Operator (WMCO) is released that is compatible with the current cluster version, the Operator is updated based on the update channel and subscription approval strategy it was installed with when using the Operator Lifecycle Manager (OLM).

The WMCO update results in the Kubernetes components in the Windows machine being updated.

[NOTE]
====
If you are updating to a new version of the WMCO and want to use cluster monitoring, you must have the `openshift.io/cluster-monitoring=true` label present in the WMCO namespace. If you add the label to a pre-existing WMCO namespace, and there are already Windows nodes configured, restart the WMCO pod to allow monitoring graphs to display.
====

For a non-disruptive update, the WMCO terminates the Windows machines configured by the previous version of the WMCO and recreates them using the current version. This is done by deleting the `Machine` object, which results in the drain and deletion of the Windows node. To facilitate an update, the WMCO adds a version annotation to all the configured nodes. During an update, a mismatch in version annotation results in the deletion and recreation of a Windows machine. To have minimal service disruptions during an update, the WMCO only updates one Windows machine at a time.

After the update, it is recommended that you set the `spec.os.name.windows` parameter in your workload pods. The WMCO uses this field to authoritatively identify the pod operating system for validation and is used to enforce Windows-specific pod security context constraints (SCCs).

[IMPORTANT]
====
The WMCO is only responsible for updating Kubernetes components, not for Windows operating system updates. You provide the Windows image when creating the VMs; therefore, you are responsible for providing an updated image. You can provide an updated Windows image by changing the image configuration in the `MachineSet` spec.
====

// Module included in the following assemblies:
//
// * windows_containers/windows-node-upgrades.adoc

[id="wmco-upgrades-eus_{context}"]
= Windows Machine Config Operator Control Plane Only update

[role="_abstract"]
You can use the *Control Plane Only* process to update the OpenShift Container Platform from one EUS version to another EUS version of OpenShift Container Platform. After you update the cluster, the Windows nodes are updated the new EUS version.

During the update, the Windows workloads are kept in a healthy state with no disruptions.

[IMPORTANT]
====
This update was previously known as an *EUS-to-EUS* update and is now referred to as a *Control Plane Only* update. These updates are only viable between *even-numbered minor versions* of OpenShift Container Platform.
====

// Module included in the following assemblies:
//
// * windows_containers/windows-node-upgrades.adoc

[id="wmco-upgrades-eus-using-web-console_{context}"]
= WMCO Control Plane Only update by using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO).

.Prerequisites
* The cluster must be running on a supported EUS version of OpenShift Container Platform.
* All Windows nodes must be in a healthy state.
* All Windows nodes must be running on the same version of the WMCO.
* All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update."

.Procedure

. Uninstall WMCO operator by using the following the steps:
+
[IMPORTANT]
====
Delete the Operator only. Do not delete the Windows namespace or any Windows workloads.
====
+
.. Log in to the OpenShift Container Platform web console.
.. Navigate to *Ecosystem* -> *Software Catalog*.
.. Use the *Filter by keyword* box to search for `Red Hat Windows Machine Config Operator`.
.. Click the *Red Hat Windows Machine Config Operator* tile. The Operator tile indicates it is installed.
.. In the *Windows Machine Config Operator* descriptor page, click *Uninstall*.

. Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update."

. Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the web console."

// Module included in the following assemblies:
//
// * windows_containers/windows-node-upgrades.adoc

[id="wmco-upgrades-eus-using-cli_{context}"]
= WMCO Control Plane Only update by using the CLI

[role="_abstract"]
You can use the {oc-first} to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO).

.Prerequisites
* The cluster must be running on a supported EUS version of OpenShift Container Platform.
* All Windows nodes must be in a healthy state.
* All Windows nodes must be running on the same version of the WMCO.
* All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update."

.Procedure

. Uninstall the WMCO Operator from the cluster by following the steps in "Deleting Operators from a cluster using the CLI."
+
[IMPORTANT]
====
Delete the Operator only. Do not delete the Windows namespace or any Windows workloads.
====

. Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update."

. Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the CLI."

.Verification

* On the Verify that the *Status* shows *Succeeded* to confirm successful installation of the WMCO.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Updating installed Operators
* Performing a Control Plane Only update
* Installing the Windows Machine Config Operator using the CLI
* Deleting Operators from a cluster using the CLI
