---
title: "Getting started with {VirtProductName}"
type: reference
domain: openshift
slug: virt-4-22-virt-getting-started
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-getting-started
version: 4.22
family: virt
documentKind: "Documentation"
---

# Getting started with {VirtProductName}

[id="virt-getting-started"]
= Getting started with {VirtProductName}

[role="_abstract"]
Explore {VirtProductName} by taking guided tours, installing the Operator, and configuring a basic environment. Learn how to migrate from your current platform, then learn more about how to deploy and manage virtual machines (VMs) by following the additional resources links.

[NOTE]
====
Cluster configuration procedures require `cluster-admin` privileges.
====

// Module included in the following assemblies:
//
// * virt/getting_started/virt-getting-started.adoc

[id="virt-getting-started-tour_{context}"]
= Getting started tour

[role="_abstract"]
The *Getting started* tour introduces several key aspects of using {VirtProductName}. There are two ways to start the tour.

.Prerequisites

* You have access to the OpenShift Container Platform web console.

.Procedure

* If you see the *Welcome to {VirtProductName}* dialog, click *Start Tour*.
* Otherwise, go to *Virtualization* -> *Settings* -> *User* -> *Getting started resources* -> *Guided tour*.
// Module included in the following assemblies:
//
// * virt/getting_started/virt-getting-started.adoc

[id="virt-quick-starts_{context}"]
= Quick start tours

[role="_abstract"]
You can explore several {VirtProductName} capabilities by taking quick start tours in the web console.

.Prerequisites

* You have access to the OpenShift Container Platform web console.

.Procedure

. Click the *Help* icon *?* in the menu bar on the header of the OpenShift Container Platform web console.
. Select *Quick Starts*. You can filter the list of tours by entering the keyword `virtual` in the *Filter* field.
// Module included in the following assemblies:
//
// * virt/getting_started/virt-getting-started.adoc

[id="migrating-to-virt_{context}"]
= Migrating to {VirtProductName}

[role="_abstract"]
To migrate virtual machines from an external provider such as {vmw-first}, {rh-openstack-first}, Red Hat Virtualization, or another OpenShift Container Platform cluster, use the {mtv-first}. You can also migrate Open Virtual Appliance (OVA) files created by {vmw-full}.

[NOTE]
====
{mtv-full} is not part of {VirtProductName} and requires separate installation. For this reason, all links in this procedure lead outside of {VirtProductName} documentation.
====

.Prerequisites
* The {mtv-full} Operator is installed.

.Procedure

* Migrate virtual machines from {vmw-first}.
* Migrate virtual machines from {rh-openstack-first}.
* Migrate virtual machines from Red Hat Virtualization.
* Migrate virtual machines from {VirtProductName}.
* Migrate virtual machines from OVA files created by {vmw-full}.

[role="_additional-resources"]
== Additional resources
* Plan your bare-metal cluster for {VirtProductName}
* Prepare your cluster for {VirtProductName}
* Learn about storage volumes for VM disks
* Use a CSI-enabled storage provider
* Configure local storage for virtual machines
* Install the {VirtProductName} Operator
* Install the Kubernetes NMState Operator
* Specify nodes for virtual machines
* Install and use the `virtctl` command-line interface (CLI) tool
* Create a VM from a Red{nbsp}Hat image
* Create a VM from an instance type
* Import a custom image from a web page
* Upload an image from your local machine
* Clone a persistent volume claim (PVC)
* Connect a VM to a Linux bridge network
* Connect a VM to an Open Virtual Network (OVN)-Kubernetes secondary network
* Connect a VM to a Single Root I/O Virtualization (SR-IOV) network
* Connect to a virtual machine console
* SSH access for virtual machines
* Connect to the desktop viewer by using the web console
* Manage a VM by using the web console
* Export a VM
* Review post-installation configuration options
* Configure storage options and automatic boot source updates
* Learn about monitoring and health checks
* Learn about live migration
* Back up and restore VMs by using the {oadp-first}
* Tune and scale your cluster
