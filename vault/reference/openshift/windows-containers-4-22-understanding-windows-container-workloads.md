---
title: "Understanding Windows container workloads"
type: reference
domain: openshift
slug: windows-containers-4-22-understanding-windows-container-workloads
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/understanding-windows-container-workloads
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Understanding Windows container workloads

[id="understanding-windows-container-workloads"]
= Understanding Windows container workloads

[role="_abstract"]
You can use the Windows Machine Config Operator (WMCO) to run Microsoft Windows Server containers on OpenShift Container Platform.

For those that administer heterogeneous environments with a mix of Linux and Windows workloads, OpenShift Container Platform allows you to deploy Windows workloads running on Windows Server containers while also providing traditional Linux workloads hosted on {op-system-first} or {op-system-base-full}.

[NOTE]
====
Multi-tenancy for clusters that have Windows nodes is not supported. Clusters are considered _multi-tenant_ when multiple workloads operate on shared infrastructure and resources. If one or more workloads running on an infrastructure cannot be trusted, the multi-tenant environment is considered _hostile_.

Hostile multi-tenant clusters introduce security concerns in all Kubernetes environments. Additional security features like pod security policies, or more fine-grained role-based access control (RBAC) for nodes, make exploiting your environment more difficult. However, if you choose to run hostile multi-tenant workloads, a hypervisor is the only security option you should use. The security domain for Kubernetes encompasses the entire cluster, not an individual node. For these types of hostile multi-tenant workloads, you should use physically isolated clusters.

Windows Server Containers provide resource isolation using a shared kernel but are not intended to be used in hostile multitenancy scenarios.
====

// Module included in the following assemblies:
//
// * windows_containers/understanding-windows-container-workloads.adoc

[id="windows-workload-management_{context}"]
= Windows workload management

[role="_abstract"]
To run Windows workloads in your cluster, you must install the Windows Machine Config Operator (WMCO).

The WMCO is a Linux-based Operator that runs on the Linux-based control plane and compute nodes. The WMCO orchestrates the process of deploying and managing Windows workloads on a cluster.

.WMCO design
image::wmco-design.png[WMCO workflow]

Before deploying Windows workloads, you must create a Windows compute node and have it join the cluster. The Windows node hosts the Windows workloads in a cluster, and can run alongside other Linux-based compute nodes. You can create a Windows compute node by creating a Windows compute machine set to host Windows Server compute machines. You must apply a Windows-specific label to the compute machine set that specifies a Windows OS image.

The WMCO watches for machines with the Windows label. After a Windows compute machine set is detected and its respective machines are provisioned, the WMCO configures the underlying Windows virtual machine (VM) so that it can join the cluster as a compute node.

.Mixed Windows and Linux workloads
image::mixed-windows-linux-workloads.png[Mixed Windows and Linux workloads]

The WMCO expects a predetermined secret in its namespace containing a private key that is used to interact with the Windows instance. WMCO checks for this secret during boot up time and creates a user data secret which you must reference in the Windows `MachineSet` object that you created. Then the WMCO populates the user data secret with a public key that corresponds to the private key. With this data in place, the cluster can connect to the Windows VM using an SSH connection.

After the cluster establishes a connection with the Windows VM, you can manage the Windows node using similar practices as you would a Linux-based node.

[NOTE]
====
The OpenShift Container Platform web console provides most of the same monitoring capabilities for Windows nodes that are available for Linux nodes. However, the ability to monitor workload graphs for pods running on Windows nodes is not available at this time.
====

Scheduling Windows workloads to a Windows node can be done with typical pod scheduling practices like taints, tolerations, and node selectors; alternatively, you can differentiate your Windows workloads from Linux workloads and other Windows-versioned workloads by using a `RuntimeClass` object.

// Module included in the following assemblies:
//
// * windows_containers/understanding-windows-container-workloads.adoc

[id="windows-node-services_{context}"]
= Windows node services

[role="_abstract"]
By default, the installation process installs several Windows-specific services on each Windows node.

[cols="1,2",options="header"]
|===

|Service
|Description

|kubelet
|Registers the Windows node and manages its status.

|Container Network Interface (CNI) plugins
|Exposes networking for Windows nodes.

|Windows Instance Config Daemon (WICD)
|Maintains the state of all services running on the Windows instance to ensure the instance functions as a worker node.

|Windows Exporter
|Exports Prometheus metrics from Windows nodes

|Kubernetes Cloud Controller Manager (CCM)
|Interacts with the underlying Azure cloud platform.

|hybrid-overlay
|Creates the OpenShift Container Platform Host Network Service (HNS).

|kube-proxy
|Maintains network rules on nodes allowing outside communication.

|containerd container runtime
|Manages the complete container lifecycle.

|CSI Proxy
|Enables CSI drivers to perform storage operations on the node, which allows containerized CSI drivers to run on Windows nodes.

|===

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Pod Security Policies (Kubernetes Documentation)
* Configuring hybrid networking with OVN-Kubernetes
