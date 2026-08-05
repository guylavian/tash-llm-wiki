---
title: "Configuring physical networks"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-physical-networks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-physical-networks
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring physical networks

[id="configuring-physical-networks"]
= Configuring physical networks

[role="_abstract"]
As an OpenShift administrator, you can create or configure a physical network in the OpenShift Container Platform web console without using the node network configuration policy (NNCP) page. The *Physical networks* page is available when the NMState console plugin is installed. When you use the *Physical networks* page in the web console, the NNCP is generated automatically. If you need more flexibility or require complex settings, use the NNCP page.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-physical-networks.adoc
[id="creating-a-physical-network_{context}"]
= Creating a physical network by using the OpenShift Container Platform web console

[role="_abstract"]
You can create physical networks for {VirtProductName} using the OpenShift Container Platform web console to create a network with direct layer 2 connectivity to your data center.

.Prerequisites
* You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

.Procedure
. In the OpenShift Container Platform web console, go to *Networking* -> *Physical networks*.
. Click *Create network*. The *Network configuration wizard* is displayed.
. On the *Network identity* page, enter a name for your network.
. On the *Nodes configuration* page, select either *Apply to all nodes on the cluster* or *Apply to specific subsets of nodes using the nodes selector*.
+
[NOTE]
====
If you select specific nodes to apply the network to, you can view the matching nodes list to ensure the selection is correct. A validation error is displayed if the selected nodes overlap with another configuration associated with the same network.
====
. On the *Uplink connection* page, select the network interface that you want to connect to the physical network:
+
Default node network:: Uses the default node network to access the outside physical network.
A single interface:: Select a specific physical network interface from the list.
+
[WARNING]
====
If the selected secondary interface has an IP address on some of the nodes, using it removes the IP address and might disrupt network services.
====
Bonding interface:: Configures bonded network interfaces to achieve resilience and higher throughput.
+
.. Enter a *Bonding name*.
.. Select the *Network interfaces* to bond.
.. Select the *Aggregation mode* from the drop-down menu.
. On the *Settings* page, enter a *Bridge name* and set the *Maximum Transmission Unit (MTU)*.
. Review the configuration details.
. Click *Create*.

.Verification
. In the OpenShift Container Platform web console, go to *Networking* -> *Physical networks*.
. Locate your new network in the list.
. Expand the network row to view the associated configurations. Verify that the *Enactment state* is *Available* and that the *Nodes* count matches your expectation.
// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-physical-networks.adoc
[id="expanding-physical-network_{context}"]
= Expanding a OpenShift Container Platform physical network to include new nodes

[role="_abstract"]
You can add one or more OpenShift Container Platform worker nodes to an existing physical network if you want to expand access to that network.
Expanding a physical network creates a new configuration under the same logical physical network.

.Prerequisites
* You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

.Procedure
. In the OpenShift Container Platform web console, go to *Networking* -> *Physical networks*.
. Click the Options menu {kebab} next to the network that you want to edit.
. Click *Configure nodes*. The *Network configuration wizard* is displayed.
+
[NOTE]
====
The *Physical network name* is predefined. You cannot edit it during this process.
====
. Click *Next*.
. On the *Nodes configuration* page, select either *Apply to all nodes on the cluster* or *Apply to specific subsets of nodes using the nodes selector*.
+
[NOTE]
====
If you select specific nodes, you can view the matching nodes list to ensure the selection is correct. A validation error is displayed if the selected nodes overlap with another configuration associated with the same network.
====
. On the *Uplink connection* page, select the network interface to connect to the physical network:
+
Default node network:: Uses the default node network to access the outside physical network.
A single interface:: Select a specific physical network interface from the list.
+
[WARNING]
====
If the selected secondary interface has an IP address on some of the nodes, using removes the IP address and might disrupt network services.
====
Bonding interface:: Configures bonded network interfaces to achieve resilience and higher throughput.
.. Enter a *Bonding name*.
.. Select the *Network interfaces* to bond.
+
[NOTE]
====
The system displays only the interfaces that all nodes have in common.
====
.. Select the *Aggregation mode* from the drop down options.
. On the *Settings* page, enter a *Bridge name* and set the *Maximum Transmission Unit (MTU)*.
. Review the configuration details.
. Click *Create*.
// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-physical-networks.adoc
[id="creating-vm-network-localnet_{context}"]
= Creating a virtual machine network from a physical network

[role="_abstract"]
If your use case does not permit the use of network address translation (NAT), you can give VMs direct layer 2 access by creating a VM network that uses a physical network.

.Prerequisites
* You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

.Procedure
. In the OpenShift Container Platform web console, go to *Networking* -> *Physical networks*.
. Click the Options menu {kebab} next to the network that you want to edit.
. Click *Create a virtual machines network using this physical network*. The *Create virtual machine network* wizard is displayed with the network name populated.
. Select a *Physical network*.
. Optional: Select *VLAN tagging* and enter a *VLAN ID*.
. On the *Project mapping* page, define which projects can access this network.
. Click *Create*.
