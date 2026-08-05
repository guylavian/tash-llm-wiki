---
title: "Manage virtual machine instances"
type: reference
domain: openshift
slug: virt-4-22-virt-manage-vmis
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-manage-vmis
version: 4.22
family: virt
documentKind: "Documentation"
---

# Manage virtual machine instances

[id="virt-manage-vmis"]
= Manage virtual machine instances

[role="_abstract"]
Manage standalone virtual machine instances (VMIs) that were created independently outside of the {VirtProductName} environment through the web console by using `oc` or `virtctl` commands from the command-line interface (CLI).

The `virtctl` command provides more virtualization options than the `oc` command. For example, you can use `virtctl` to pause a VM or expose a port.

// Module included in the following assembly:
//
// * virt/virtual_machines/virt-manage-vmis.adoc
//

[id="virt-about-vmis_{context}"]
= About virtual machine instances

[role="_abstract"]
A virtual machine instance (VMI) is a representation of a running virtual machine (VM). When a VMI is owned by a VM or by another object, you manage it through its owner in the web console or by using the `oc` command-line interface (CLI).

A standalone VMI is created and started independently with a script, through automation, or by using other methods in the CLI. In your environment, you might have standalone VMIs that were developed and started outside of the {VirtProductName} environment. You can continue to manage those standalone VMIs by using the CLI. You can also use the web console for specific tasks associated with standalone VMIs:

* List standalone VMIs and their details.

* Edit labels and annotations for a standalone VMI.

* Delete a standalone VMI.

When you delete a VM, the associated VMI is automatically deleted. You delete a standalone VMI directly because it is not owned by VMs or other objects.

[NOTE]
====
Before you uninstall {VirtProductName}, list and view the standalone VMIs by using the CLI or the web console. Then, delete any outstanding VMIs.
====

When you edit a VM, some settings might be applied to the VMIs dynamically and without the need for a restart. Any change made to a VM object that cannot be applied to the VMIs dynamically will trigger the `RestartRequired` VM condition. Changes are effective on the next reboot, and the condition is removed.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-manage-vmis.adoc

[id="virt-listing-vmis-cli_{context}"]
= Listing all virtual machine instances using the CLI

[role="_abstract"]
You can list all virtual machine instances (VMIs) in your cluster, including standalone VMIs and those owned by virtual machines, by using the {oc-first}.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* List all VMIs by running the following command:
+
[source,terminal]
----
$ oc get vmis -A
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-manage-vmis-web.adoc

[id="virt-listing-vmis-web_{context}"]
= Listing standalone virtual machine instances using the web console

[role="_abstract"]
Using the web console, you can list and view standalone virtual machine instances (VMIs) in your cluster that are not owned by virtual machines (VMs).

[NOTE]
====
VMIs that are owned by VMs or other objects are not displayed in the web console. The web console displays only standalone VMIs. If you want to list all VMIs in your cluster, you must use the CLI.
====

.Procedure

* Click *Virtualization* -> *VirtualMachines* from the side menu.
+
You can identify a standalone VMI by a dark colored badge next to its name.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-manage-vmis.adoc

[id="virt-searching-vmis-web_{context}"]
= Searching for standalone virtual machine instances by using the web console

[role="_abstract"]
You can search for virtual machine instances (VMIs) by using the search bar on the *VirtualMachines* page. Use the advanced search to apply additional filters.

.Procedure

. In the OpenShift Container Platform console, click *Virtualization* → *VirtualMachines* from the side menu.

. In the search bar at the top of the page, type a VM name, label, or IP address.

. In the suggestions list, choose one of the following options:
* Click a VM name to open its details page.
* Click *All search results found for ...* to view results on a dedicated page.
* Click a related suggestion to prefill search filters.

. Optional: To open advanced search options, click the sliders icon next to the search bar. Expand the **Details** section and specify one or more of the available filters: *Name*, *Project*, *Description*, *Labels*, *Date created*, *vCPU*, and *Memory*.

. Optional: Expand the **Network** section and enter an IP address to filter by.

. Click *Search*.

. Optional: If Advanced Cluster Management (ACM) is installed, use the *Cluster* dropdown to search across multiple clusters.

. Optional: Click the *Save search* icon to store your search in the `kubevirt-user-settings` ConfigMap.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-manage-vmis.adoc

[id="virt-editing-vmis-web_{context}"]
= Editing a standalone virtual machine instance using the web console

[role="_abstract"]
You can edit the annotations and labels of a standalone virtual machine instance (VMI) using the web console. Other fields are not editable.

.Procedure

. In the OpenShift Container Platform console, click *Virtualization* -> *VirtualMachines* from the side menu.

. Select a standalone VMI to open the *VirtualMachineInstance details* page.

. On the *Details* tab, click the pencil icon beside *Annotations* or *Labels*.

. Make the relevant changes and click *Save*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-deleting-vmis-cli.adoc

[id="virt-deleting-vmis-cli_{context}"]

= Deleting a standalone virtual machine instance using the CLI

[role="_abstract"]
You can delete a standalone virtual machine instance (VMI) by using the `oc` command-line interface (CLI).

.Prerequisites

* Identify the name of the VMI that you want to delete.
* You have installed the {oc-first}.

.Procedure

* Delete the VMI by running the following command:
+
[source,terminal]
----
$ oc delete vmi <vmi_name>
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-manage-vmis.adoc

[id="virt-deleting-vmis-web_{context}"]
= Deleting a standalone virtual machine instance using the web console

[role="_abstract"]
You can delete a standalone virtual machine instance (VMI) from the web console.

.Procedure

. In the OpenShift Container Platform web console, click *Virtualization* -> *VirtualMachines* from the side menu.

. Click *Actions* -> *Delete VirtualMachineInstance*.

. In the confirmation pop-up window, click *Delete* to permanently delete the standalone VMI.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Using the CLI tools
