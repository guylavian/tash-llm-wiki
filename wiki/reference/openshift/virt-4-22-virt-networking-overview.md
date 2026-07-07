---
title: "Networking overview"
type: reference
domain: openshift
slug: virt-4-22-virt-networking-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-networking-overview
version: 4.22
family: virt
documentKind: "Documentation"
---

# Networking overview

[id="virt-networking"]
= Networking overview

[role="_abstract"]
To connect virtual machines (VMs) to cluster networks, configure default and user-defined networking options in {VirtProductName}.

{VirtProductName} supports single-stack IPv6 clusters for VMs that are connected to an OVN-Kubernetes localnet network, Linux bridge Container Network Interface (CNI) plugin, and Single Root I/O Virtualization (SR-IOV) network devices.

The following figure illustrates the typical network setup of {VirtProductName}. Other configurations are also possible.

.{VirtProductName} networking overview
image::318_OpenShift_Virtualization_Networking_0423.png[{VirtProductName} networking architecture]

image:darkcircle-1.png[20,20] Pods and VMs run on the same network infrastructure so you can easily connect your containerized and virtualized workloads.

image:darkcircle-2.png[20,20] You can connect VMs to the default pod network and to any number of secondary networks.

image:darkcircle-3.png[20,20] The default pod network provides connectivity between all its members, service abstraction, IP management, micro segmentation, and other functionality.

image:darkcircle-4.png[20,20] Multus is a "meta" CNI plugin that enables a pod or virtual machine to connect to additional network interfaces by using other compatible CNI plugins.

image:darkcircle-5.png[20,20] The default pod network is overlay-based, tunneled through the underlying machine network.

image:darkcircle-6.png[20,20] You can define the machine network over a selected set of network interface controllers (NICs).

image:darkcircle-7.png[20,20] Secondary VM networks are typically bridged directly to a physical network, with or without VLAN encapsulation. It is also possible to create virtual overlay networks for secondary networks.

[IMPORTANT]
====
Connecting VMs directly to the underlay network is not supported on {product-rosa}, {azure-short},{dedicated}, {gcp-first}, or {oci-first}.
====

[NOTE]
====
Connecting VMs to user-defined networks with the `layer2` topology is recommended on public clouds.
====
image:darkcircle-8.png[20,20] Secondary VM networks can be defined on dedicated set of NICs, as shown in figure 1, or they can use the machine network.

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-pxe-booting.adoc
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc

[id="virt-networking-glossary_{context}"]
= {VirtProductName} networking glossary

[role="_abstract"]
The following terms are used throughout {VirtProductName} documentation.

Container Network Interface (CNI):: A Cloud Native Computing Foundation
project, focused on container network connectivity.
{VirtProductName} uses CNI plugins to build upon the basic Kubernetes networking functionality.

Multus:: A "meta" CNI plugin that allows multiple CNIs to exist so that a pod or virtual machine can use the interfaces it needs.

Custom resource definition (CRD):: A Kubernetes
API resource that allows you to define custom resources, or an object defined by using the CRD API resource.

`NetworkAttachmentDefinition`:: A CRD introduced by the Multus project that allows you to attach pods, virtual machines, and virtual machine instances to one or more networks.

`UserDefinedNetwork`:: A namespace-scoped CRD introduced by the user-defined network (UDN) API that can be used to create a tenant network that isolates the tenant namespace from other namespaces.

`ClusterUserDefinedNetwork`:: A cluster-scoped CRD introduced by the user-defined network API that cluster administrators can use to create a shared network across multiple namespaces.

`NodeNetworkConfigurationPolicy`:: A CRD introduced by the nmstate project, describing the requested network configuration on nodes.
You update the node network configuration, including adding and removing interfaces, by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-networking-overview.adoc

[id="virt-nw-overview-manage-overlay-nw_{context}"]
= Manage overlay networks

[role="_abstract"]
To ensure your virtual machines (VMs) connect reliably by using the standard OpenShift Container Platform networking model, configure the default pod network for cluster-wide connectivity.

Overlay networks provide a flexible, software-defined layer of connectivity on top of a physical network, enabling services like network segmentation, custom routing, and simplified management without altering the underlying hardware.

Connect a VM to the default pod network:: Each VM is connected by default to the default internal pod network. You can add or remove network interfaces by editing the VM specification.
+
You can access a virtual machine (VM) that is connected to the default internal pod network on a stable fully qualified domain name (FQDN) by using headless services.

Connect a VM to a custom primary overlay network:: Configure a primary user-defined network (UDN) that supports multi-namespace connectivity to provide isolated and flexible traffic paths for your workloads.
+
Cluster administrators can configure a primary `UserDefinedNetwork` CRD to create a tenant network that isolates the tenant namespace from other namespaces without requiring network policies. Additionally, cluster administrators can use the `ClusterUserDefinedNetwork` CRD to create a shared OVN layer 2 network across multiple namespaces.
+
User-defined networks with the layer 2 overlay topology are useful for VM workloads, and a good alternative to secondary networks in environments where physical network access is limited, such as the public cloud. The layer 2 topology enables seamless migration of VMs without the need for Network Address Translation (NAT), and also provides persistent IP addresses that are preserved between reboots and during live migration.

Connect a VM to a custom secondary overlay network:: Configure a secondary UDN with layer 2 topology to create a private isolated communication channel between a group of VMs across different nodes. A layer 2 topology connects workloads by a cluster-wide logical switch. The OVN-Kubernetes CNI plugin uses the Geneve (Generic Network Virtualization Encapsulation) protocol to create an overlay network between nodes. You can use this overlay network to connect VMs on different nodes, without having to configure any additional physical networking infrastructure.

Configure external ingress by exposing a VM as a service:: You can expose a VM within the cluster or outside the cluster by creating a `Service` object. For on-premise clusters, you can configure a load balancing service by using the MetalLB Operator. You can install the MetalLB Operator by using the OpenShift Container Platform web console or the CLI.

Configure external ingress by exposing a VM as a service:: You can expose a VM within the cluster or outside the cluster by creating a `Service` object.

Add a VM to a {SMProductShortName}:: {VirtProductName} is integrated with {SMProductName}. You can monitor, visualize, and control traffic between pods and virtual machines on the default pod network with IPv4.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-networking-overview.adoc

[id="virt-nw-overview-connect-vm-to-physical-nw_{context}"]
= Connect to the provider's physical network

[role="_abstract"]
To give virtual machines (VMs) access to the internet or other physical devices, you configure the node network, define the secondary network, and attach the VM to the secondary network.

Connect a VM to the physical network by using an Open vSwitch bridge:: You can connect a VM to the physical network infrastructure by configuring an OVN-Kubernetes secondary user-defined network (UDN) with the localnet topology.
+
A localnet topology connects the secondary network to the physical underlay. This enables both east-west cluster traffic and access to services running outside the cluster, but it requires additional configuration of the underlying Open vSwitch (OVS) bridge on cluster nodes.
+
Cluster administrators can use the following steps to configure the localnet UDN:

. Install the Kubernetes NMState Operator which provides a state-driven network configuration across cluster nodes.
. Use the `NodeNetworkConfigurationPolicy` custom resource (CR) to configure OVS bridges and add the appropriate bridge mappings on the nodes.
. Use the `ClusterUserDefinedNetwork` CR from the UDN API to attach their workload to the underlay network through the OVS bridges configured in the previous step.

// Hiding from ROSA/OSD as Linux Bridge not supported
Connect a VM to the physical network by using a Linux bridge:: Install the Kubernetes NMState Operator to configure Linux bridges, VLANs, and bonding for your secondary networks. The OVN-Kubernetes `localnet` topology is the recommended way of connecting a VM to the underlying physical network, but {VirtProductName} also supports Linux bridge networks.
+
[NOTE]
====
You cannot directly attach to the default machine network when using Linux bridge networks.
====
+
You can create a Linux bridge network and attach a VM to the network by performing the following steps:

. Prepare the node network by creating a Linux bridge node network configuration policy (NNCP).
. Define the secondary Linux bridge network by creating a network attachment definition (NAD).
. Attach the VM to the Linux bridge network.

// Hiding from ROSA/OSD as SR-IOV not supported
Connect a VM to the physical network by using an SR-IOV device:: You can use Single Root I/O Virtualization (SR-IOV) network devices with additional networks on your OpenShift Container Platform cluster installed on bare metal or {rh-openstack-first} infrastructure for applications that require high bandwidth or low latency.
+
You must install the SR-IOV Network Operator on your cluster to manage SR-IOV network devices and network attachments.
+
You can connect a VM to an SR-IOV network by performing the following steps:

. Configure an SR-IOV physical network device by creating a `SriovNetworkNodePolicy` CR.
. Define the SR-IOV secondary network by creating an `SriovNetwork` object.
. Connect the VM to the SR-IOV network by including the network details in the VM configuration.

// Hiding in ROSA/OSD as not supported
Connect a VM to the physical network by using DPDK drivers with SR-IOV hardware:: The Data Plane Development Kit (DPDK) provides a set of libraries and drivers for fast packet processing. You can configure clusters and VMs to run DPDK workloads over SR-IOV networks by performing the following steps:

. Configure the node hardware.
. Configure the VM namespace for DPDK.
. Configure the VM and guest OS to run DPDK applications.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-networking-overview.adoc

[id="virt-nw-overview-comparing-localnet-linuxbridge_{context}"]
= Comparing Linux bridge CNI and OVN-Kubernetes localnet topology

// Hiding from ROSA/OSD as Linux Bridge is not supported

[role="_abstract"]
The following table provides a comparison of features available when using the Linux bridge CNI compared to the localnet topology for an OVN-Kubernetes plugin.

.Linux bridge CNI compared to an OVN-Kubernetes localnet topology
[cols="1,1,1",options="header"]
|===
|Feature
|Available on Linux bridge CNI
|Available on OVN-Kubernetes localnet

|Layer 2 access to the underlay native network
|Only on secondary network interface controllers (NICs)
|Yes

|Layer 2 access to underlay VLANs
|Yes
|Yes

|Layer 2 trunk access
|Yes
|No

|Network policies
|No
|Yes

|MAC spoof filtering
|Yes
|Yes (Always on)

|===

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-networking-overview.adoc

[id="virt-nw-overview-manage-vm-nw-config_{context}"]
= Manage VM network interface configuration

[role="_abstract"]
Manage virtual machine (VM) network configuration to scale connectivity without incurring application downtime, troubleshoot network latency, define and automate management of MAC address pools, configure IP addresses, and isolate live migration traffic.

Hot plug secondary network interfaces:: You can add or remove secondary network interfaces without stopping your VM. {VirtProductName} supports hot plugging and hot unplugging for secondary interfaces that use bridge binding and the VirtIO device driver. {VirtProductName} also supports hot plugging secondary interfaces that use the SR-IOV binding.

Hot plug secondary network interfaces:: You can add or remove secondary network interfaces without stopping your VM. {VirtProductName} supports hot plugging and hot unplugging for secondary interfaces that use bridge binding and the OVN-Kubernetes `layer2` topology.

Access a VM by using its external FQDN:: You can access a virtual machine (VM) that is attached to a secondary network interface from outside the cluster by using its fully qualified domain name (FQDN). To connect to a VM by using its external FQDN, you must configure the DNS server, retrieve the cluster FQDN, and then connect to the VM by using the `ssh` command.

Manage the link state of a VM network interface:: You can manage the link state of a primary or secondary VM network interface by using the OpenShift Container Platform web console or the command line. By specifying the link state, you can logically connect or disconnect the virtual network interface controller (vNIC) from a network.
+
[NOTE]
====
{VirtProductName} does not support link state management for Single Root I/O Virtualization (SR-IOV) secondary network interfaces and their link states are not reported.
====

Configure and view VM IP address:: You can configure the IP address of a secondary network interface when you create a VM. The IP address is provisioned with cloud-init. You can view the IP address of a VM by using the OpenShift Container Platform web console or the command line. The network information is collected by the QEMU guest agent.

Manage MAC address pools for VM network interfaces:: The KubeMacPool component allocates MAC addresses for VM network interfaces from a shared MAC address pool. This ensures that each network interface is assigned a unique MAC address. A virtual machine instance created from that VM retains the assigned MAC address across reboots.

Configure a dedicated network for live migration:: You can configure a dedicated Multus network for live migration. A dedicated network minimizes the effects of network saturation on tenant workloads during live migration.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-networking-overview.adoc

[id="virt-nw-overview-vm-ssh-config_{context}"]
= Configure VM SSH access

[role="_abstract"]
You can use SSH to securely access your virtual machines (VMs) from the command line.

To set up your SSH configuration, use one of the following methods:

Use the `virtctl ssh` command:: You create an SSH key pair, add the public key to a VM, and connect to the VM by running the `virtctl ssh` command with the private key.
+
You can add public SSH keys to {op-system-base-full} 9 VMs at runtime or at first boot to VMs with guest operating systems that can be configured by using a cloud-init data source.

Use the `virtctl port-forward` command:: You add the `virtctl port-foward` command to your `.ssh/config` file and connect to the VM by using OpenSSH.

Service:: You create a service, associate the service with the VM, and connect to the IP address and port exposed by the service.

Secondary network:: You configure a secondary network, attach a VM to the secondary network interface, and connect to its allocated IP address.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Connect a virtual machine to the default pod network
* Connect a virtual machine to a custom primary overlay network
* Connect a VM to a custom secondary overlay network
* Configure external ingress by exposing a VM as a service
* Add a VM to a Service Mesh
* Connect a VM to the physical network by using an Open vSwitch bridge
* Access a virtual machine by using its internal FQDN
* Installing the MetalLB Operator
* Connect a virtual machine to the physical network by using a Linux bridge
* Install the Kubernetes NMState Operator
* Connect a VM to the physical network by using an SR-IOV device
* Install the SR-IOV Network Operator
* Connect a VM to the physical network by using DPDK drivers with SR-IOV hardware
* Configure a dedicated network for live migration
* Access a VM by using its external FQDN
* Manage the link state of a virtual machine interface
* Hot plugging secondary network interfaces
* Configure and view VM IP address
* Manage MAC address pools for network interfaces
* SSH access for virtual machines
