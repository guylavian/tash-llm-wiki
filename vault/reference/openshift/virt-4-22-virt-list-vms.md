---
title: "List virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-list-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-list-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# List virtual machines

[id="virt-list-vms"]
= List virtual machines

[role="_abstract"]
Use the web console or {oc-first} to list your virtual machines (VMs). From the list, you can filter and search for specific VMs.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-list-vms.adoc

[id="virt-listing-vms-cli_{context}"]
= List virtual machines by using the CLI

[role="_abstract"]
You can either list all of the virtual machines (VMs) in your cluster or limit the list to VMs in a specified namespace by using the {oc-first}.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* List all of the VMs in your cluster by running the following command:
+
[source,terminal]
----
$ oc get vms -A
----

* List all of the VMs in a specific namespace by running the following command:
+
[source,terminal]
----
$ oc get vms -n <namespace>
----

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-list-vms.adoc

[id="virt-listing-vms-web_{context}"]
= List virtual machines by using the web console

[role="_abstract"]
You can list all of the virtual machines (VMs) in your cluster by using the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu to access the tree view of all projects and VMs in your cluster.

. Optional: Enable the *Show only projects with VirtualMachines* option above the tree view to limit the displayed projects.

. Click the *Virtual machines* tab.

. Optional: Click the *Search virtual machines* text box and begin to type the name of a virtual machine. A list of filtered virtual machine names will appear and change as you type.

. Optional: Click the *Advanced search* button next to the search bar to use more search options.

.. Use the fields provided to further filter your virtual machine search.
+
[cols="1,1a", options="header"]
|===
|Field |Description

| Name
| The virtual machine name.

| Project
| A project that is part of your deployment.

| Description
| Text in the description of the virtual machine.

| Status
| The status of the virtual machine.

| Operating system
| The operating system of the virtual machine.

| vCPU
| The number of vCPUs alotted to the virtual machine. Select a modifying expression and enter a value to search on.

| Memory
| The amount of memory alotted to the virtual machine. Select a modifying expression, enter a value to search on, and select what that value represents.

| Storage class
| The storage class the virtual machine uses.

| Hardware devices
| The type of hardware device assocaited with the virtual machine.

| Date created
| The date range the virtual machine was created in.

| Labels
| The labels associated with the virtual machine.

| Scheduling
| The scheduling logic associated with the virtual machine.

| Nodes
| The nodes associated with the virtual machine.

| IP address
| The IP address of the virtual machine.

| Network Attachment Definitions
| Select the appropriate definition.

|===

.. Click *Search*.

.. Optional: Click *Clear all* to clear all search criteria.

. Optional: Click *Save search* to save the current for reuse later.

. Optional: Select a saved search from the *Saved searches* list to reuse.

. Optional: Filter the list of virtual machines by project using the *Project* list.

. Optional: Filter the list of virtual machines by status using the *Status* list.

. Optional: Filter the list of virtual machines by operating system using the *Operating system* list.

. Optional: Filter the list of virtual machines by name using the *Search by name* field.

. Optional: Use the *Selection* list to quickly select or deselect a group of virtual machines.

. Optional: Use the *Actions* list to perform an action on all selected virtual machines.

. Optional: Click the *More actions* icon beside an individual virtual machine listing to perform an action on that virtual machine.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-list-vms.adoc

[id="virt-organize-vms-web_{context}"]
= Organize virtual machines by using the web console

[role="_abstract"]
In addition to creating virtual machines (VMs) in different projects, you can use the tree view to further organize them in folders.

[IMPORTANT]
====
Enabling folders in the virtual machine tree is a Technology Preview feature only. Technology Preview features are not supported with Red{nbsp}Hat production service level agreements (SLAs) and might not be functionally complete. Red{nbsp}Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red{nbsp}Hat Technology Preview features, see Technology Preview Features Support Scope.
====

[NOTE]
====
{VirtProductName} does not enable folders in the virtual machine tree by default. To enable folders, go to *Virtualization* -> *Settings*. In the *Preview features* tab, select *Enable folders in Virtual Machines tree view*.
====

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu to access the tree view with all projects and VMs in your cluster.

. Perform one of the following actions depending on your use case:

* To move the VM to a new folder in the same project:

.. Right-click the name of the VM in the tree view.
.. Select *Move to folder* from the menu.
.. Type the name of the folder to create in the "Search folder" bar.
.. Click *Create folder* in the drop-down list.
.. Click *Save*.

* To move the VM to an existing folder in the same project:

** Click the name of the VM in the tree view and drag it to a folder in the same project. A highlight is displayed on the folder for permitted operations.

* To move the VM from a folder to the project:

** Click the name of the VM in the tree view and drag it on the project name. A highlight is displayed on the folder for permitted operations.
