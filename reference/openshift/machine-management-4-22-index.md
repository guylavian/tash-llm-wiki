---
title: "Overview of machine management"
type: reference
domain: openshift
slug: machine-management-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/index
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Overview of machine management

[id="overview-of-machine-management"]
= Overview of machine management

[role="_abstract"]
You can use machine management to flexibly work with underlying infrastructure such as Amazon Web Services (AWS), Microsoft Azure, {gcp-first}, {rh-openstack-first}, and VMware vSphere to manage the OpenShift Container Platform cluster.
You can control the cluster and perform auto-scaling, such as scaling up and down the cluster based on specific workload policies.

It is important to have a cluster that adapts to changing workloads. The OpenShift Container Platform cluster can horizontally scale up and down when the load increases or decreases.

Machine management is implemented as a custom resource definition (CRD).
A CRD object defines a new unique object `Kind` in the cluster and enables the Kubernetes API server to handle the object's entire lifecycle.

The Machine API Operator provisions the following resources:

* `MachineSet`
* `Machine`
* `ClusterAutoscaler`
* `MachineAutoscaler`
* `MachineHealthCheck`

// Module included in the following assemblies:
//
// * machine_management/index.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-osp.adoc
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-aws.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-azure.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-gcp.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-nutanix.adoc

[id="machine-api-overview_{context}"]
= Machine API overview

[role="_abstract"]
The Machine API performs all node host provisioning management actions after the cluster installation finishes. Because of this system, OpenShift Container Platform offers an elastic, dynamic provisioning method on top of public or private cloud infrastructure.

The Machine API is a combination of primary resources that are based on the upstream Cluster API project and custom OpenShift Container Platform resources.

The two primary resources are:

Machines:: A fundamental unit that describes the host for a node. A machine has a `providerSpec` specification, which describes the types of compute nodes that are offered for different cloud platforms. For example, a machine type for a compute node might define a specific machine type and required metadata.

Machine sets:: `MachineSet` resources are groups of compute machines. Compute machine sets are to compute machines as replica sets are to pods. If you need more compute machines or must scale them down, you change the `replicas` field on the `MachineSet` resource to meet your compute need.
+
[WARNING]
====
Control plane machines cannot be managed by compute machine sets.

Control plane machine sets provide management capabilities for supported control plane machines that are similar to what compute machine sets provide for compute machines.

For more information, see “Managing control plane machines".
====

The following custom resources add more capabilities to your cluster:

Machine autoscaler:: The `MachineAutoscaler` resource automatically scales compute machines in a cloud. You can set the minimum and maximum scaling boundaries for nodes in a specified compute machine set, and the machine autoscaler maintains that range of nodes.
+
The `MachineAutoscaler` object takes effect after a `ClusterAutoscaler` object exists. Both `ClusterAutoscaler` and `MachineAutoscaler` resources are made available by the `ClusterAutoscalerOperator` object.

Cluster autoscaler:: This resource is based on the upstream cluster autoscaler project. In the OpenShift Container Platform implementation, it is integrated with the Machine API by extending the compute machine set API. You can use the cluster autoscaler to manage your cluster in the following ways:
+
* Set cluster-wide scaling limits for resources such as cores, nodes, memory, and GPU
* Set the priority so that the cluster prioritizes pods and new nodes are not brought online for less important pods
* Set the scaling policy so that you can scale up nodes but not scale them down

Machine health check:: The `MachineHealthCheck` resource detects when a machine is unhealthy, deletes it, and, on supported platforms, makes a new machine.

// Should this paragraph still be in here in 2022? Or at least should it be rephrased to avoid comparing to 3.11?
In OpenShift Container Platform version 3.11, you could not roll out a multi-zone architecture easily because the cluster did not manage machine provisioning. Beginning with OpenShift Container Platform version 4.1, this process is easier. Each compute machine set is scoped to a single zone, so the installation program sends out compute machine sets across availability zones on your behalf. And then because your compute is dynamic, and in the face of a zone failure, you always have a zone for when you must rebalance your machines. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability. The autoscaler provides best-effort balancing over the life of a cluster.

[role="_additional-resources"]
.Additional resources
* Machine phases and lifecycle

// Module included in the following assemblies:
//
// * machine_management/index.adoc
//
// This file is a navigation file - xrefs are allowed in this type of module, but it must only ever be included from one location

[id="machine-mgmt-intro-managing-compute_{context}"]
= Compute machine management

[role="_abstract"]
As a cluster administrator, you can manage the compute machines in your OpenShift Container Platform cluster.

For example, you can perform the following actions:

* Create a compute machine set for the following cloud providers:

** AWS

** Azure

** Azure Stack Hub

** {gcp-short}

** IBM Cloud

** IBM Power Virtual Server

** Nutanix

** {rh-openstack}

** vSphere

* Create a machine set for a bare metal deployment: Creating a compute machine set on bare metal

* Manually scale a compute machine set by adding or removing a machine from the compute machine set.

* Modify a compute machine set through the `MachineSet` YAML configuration file.

* Delete a machine.

* Create infrastructure compute machine sets.

* Configure and deploy a machine health check to automatically fix damaged machines in a machine pool.

[NOTE]
====
When creating a new machine set, you should specify the latest image to use for the boot image. For more information about updating the boot image on your cluster, see "Manually updating the boot image" and "Boot image management". The method to update or specify the image varies by platform.
====

[role="_additional-resources"]
.Additional resources
* Manually updating the boot image
* Boot image management

// Module included in the following assemblies:
//
// * machine_management/index.adoc
//
// This file is a navigation file - xrefs are allowed in this type of module, but it must only ever be included from one location

[id="machine-mgmt-intro-managing-control-plane_{context}"]
= Control plane machine management

[role="_abstract"]
As a cluster administrator, you can manage the control plane machines in your OpenShift Container Platform cluster.

For example, you can perform the following actions:

* Update your control plane configuration with a control plane machine set for the following cloud providers:

** {aws-full}

** {gcp-full}

** {azure-full}

** Nutanix

** {rh-openstack-first}

** {vmw-full}

* Configure and deploy a machine health check to automatically recover unhealthy control plane machines.

// Module included in the following assemblies:
//
// * machine_management/index.adoc
//
// This file is a navigation file - xrefs are allowed in this type of module, but it must only ever be included from one location

[id="machine-mgmt-intro-autoscaling_{context}"]
= Cluster autoscaling

[role="_abstract"]
You can automatically scale your OpenShift Container Platform cluster to ensure flexibility for changing workloads.

To autoscale your cluster, you must first deploy a cluster autoscaler, and then deploy a machine autoscaler for each compute machine set.

* The _cluster autoscaler_ increases and decreases the size of the cluster based on deployment needs.

* The _machine autoscaler_ adjusts the number of machines in the compute machine sets that you deploy in your OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * machine_management/index.adoc

[id="machine-mgmt-intro-add-for-upi_{context}"]
= Compute machine creation on user-provisioned infrastructure

[role="_abstract"]
User-provisioned infrastructure is an environment where you can deploy infrastructure such as compute, network, and storage resources that host the OpenShift Container Platform. You can add compute machines to a cluster on user-provisioned infrastructure during or after the installation process.

[role="_additional-resources"]
.Additional resources
* Adding compute machines to clusters with user-provisioned infrastructure manually
