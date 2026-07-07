---
title: "Prerequisites"
type: reference
domain: openshift
slug: installing-4-22-ipi-install-prerequisites
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/ipi-install-prerequisites
version: 4.22
family: installing
documentKind: "Documentation"
---

# Prerequisites

[id="ipi-install-prerequisites"]
= Prerequisites

Installer-provisioned installation of OpenShift Container Platform requires:

. Three control plane nodes
. Baseboard management controller (BMC) access to each node
. At least one network:
.. One required routable network
.. One optional provisioning network
.. One optional management network

Before starting an installer-provisioned installation of OpenShift Container Platform, ensure the hardware environment meets the following requirements.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="node-requirements_{context}"]
= Node requirements

Installer-provisioned installation involves a number of hardware node requirements:

* *CPU architecture:* All nodes must use `x86_64`
or `aarch64`
CPU architecture.
* *Similar nodes:* Red Hat recommends nodes have an identical configuration per role. That is, Red Hat recommends nodes be the same brand and model with the same CPU, memory, and storage configuration.

* *Baseboard Management Controller:* The `provisioner` node must be able to access the baseboard management controller (BMC) of each OpenShift Container Platform cluster node. You may use IPMI, Redfish, or a proprietary protocol.

* *Latest generation:* Nodes must be of the most recent generation. Installer-provisioned installation relies on BMC protocols, which must be compatible across nodes. Additionally, {op-system-base} {op-system-version} ships with the most recent drivers for RAID controllers. Ensure that the nodes are recent enough to support {op-system-base} {op-system-version} for the `provisioner` node and {op-system} {op-system-version} for the control plane and worker nodes.
* *Latest generation:* Nodes must be of the most recent generation. Installer-provisioned installation relies on BMC protocols, which must be compatible across nodes. Additionally, {op-system-first} ships with the most recent drivers for RAID controllers. Ensure that the nodes are recent enough to support {op-system} for the `provisioner` node and {op-system} for the control plane and worker nodes.

* *Registry node:* (Optional) If setting up a disconnected mirrored registry, it is recommended the registry reside in its own node.

* *Provisioner node:* Installer-provisioned installation requires one `provisioner` node.

* *Control plane:* Installer-provisioned installation requires three control plane nodes for high availability. You can deploy an OpenShift Container Platform cluster with only three control plane nodes, making the control plane nodes schedulable as worker nodes. Smaller clusters are more resource efficient for administrators and developers during development, production, and testing.

* *Worker nodes:* While not required, a typical production cluster has two or more worker nodes.
+
[IMPORTANT]
====
Do not deploy a cluster with only one worker node, because the cluster will deploy with routers and ingress traffic in a degraded state.
====

* *Network interfaces:* Each node must have at least one network interface for the routable `baremetal` network. Each node must have one network interface for a `provisioning` network when using the `provisioning` network for deployment. Using the `provisioning` network is the default configuration.
+
[NOTE]
====
Only one network card (NIC) on the same subnet can route traffic through the gateway. By default, Address Resolution Protocol (ARP) uses the lowest numbered NIC. Use a single NIC for each node in the same subnet to ensure that network load balancing works as expected. When using multiple NICs for a node in the same subnet, use a single bond or team interface. Then add the other IP addresses to that interface in the form of an alias IP address. If you require fault tolerance or load balancing at the network interface level, use an alias IP address on the bond or team interface. Alternatively, you can disable a secondary NIC on the same subnet or ensure that it has no IP address.
====

* *Unified Extensible Firmware Interface (UEFI):* Installer-provisioned installation requires UEFI boot on all OpenShift Container Platform nodes when using IPv6 addressing on the `provisioning` network. In addition, UEFI Device PXE Settings must be set to use the IPv6 protocol on the `provisioning` network NIC, but omitting the `provisioning` network removes this requirement.
+
[IMPORTANT]
====
When starting the installation from virtual media such as an ISO image, delete all old UEFI boot table entries. If the boot table includes entries that are not generic entries provided by the firmware, the installation might fail.
====

* *Secure Boot:* Many production scenarios require nodes with Secure Boot enabled to verify the node only boots with trusted software, such as UEFI firmware drivers, EFI applications, and the operating system. You may deploy with Secure Boot manually or managed.
+
. *Manually:* To deploy an OpenShift Container Platform cluster with Secure Boot manually, you must enable UEFI boot mode and Secure Boot on each control plane node and each worker node. Red Hat supports Secure Boot with manually enabled UEFI and Secure Boot only when installer-provisioned installations use Redfish virtual media. See "Configuring nodes for Secure Boot manually" in the "Configuring nodes" section for additional details.
+
. *Managed:* To deploy an OpenShift Container Platform cluster with managed Secure Boot, you must set the `bootMode` value to `UEFISecureBoot` in the `install-config.yaml` file. Red Hat only supports installer-provisioned installation with managed Secure Boot on 10th generation HPE hardware and 13th generation Dell hardware running firmware version `2.75.75.75` or greater. Deploying with managed Secure Boot does not require Redfish virtual media. See "Configuring managed Secure Boot" in the "Setting up the environment for an OpenShift installation" section for details.
+
[NOTE]
====
Red Hat does not support managing self-generated keys, or other keys, for Secure Boot.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-restricted.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc
// * installing/installing_bare_metal_ipi/ipi-install-prerequisites.adoc
// * installing/installing_ibm_z/installing-ibm-z-reqs.adoc

[id="installation-minimum-resource-requirements_{context}"]
= Minimum resource requirements for cluster installation

[role="_abstract"]
Each created cluster must meet minimum requirements so that the cluster runs as expected.

.Minimum resource requirements
[cols="2,2,2,2,2,2",options="header"]
|===

|Machine
|Operating System
|vCPU ^[1]^
|vCPU
|Virtual RAM
|CPU ^[1]^
|RAM
|Storage
|Input/Output Per Second (IOPS)^[2]^
|Input/Output Per Second (IOPS)^[1]^
|Input/Output Per Second (IOPS)

|Bootstrap
|16 GB
|100 GB
|300
|N/A

|Control plane
|{op-system}
|16 GB
|100 GB
|300
|N/A

|Compute
|2
|8 GB
|100 GB
|300
|N/A

|Compute
|{op-system}
|2
|8 GB
|100 GB
|300
|N/A
|===
[.small]
--
1. One physical core (IFL) provides two logical cores (threads) when SMT-2 is enabled. The hypervisor can provide two or more vCPUs.
1. One CPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = CPUs.
1. One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
2. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.
3. As with all user-provisioned installations, if you choose to use {op-system-base} compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of {op-system-base} 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.
2. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.
1. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.
2. As with all user-provisioned installations, if you choose to use {op-system-base} compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of {op-system-base} 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.
--
[NOTE]
====
For OpenShift Container Platform version 4.22, {op-system} is based on {op-system-base} version 9.8, which has the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* IBM Power architecture requires Power 9 ISA
* s390x architecture requires z14 ISA

For more information, see Architectures ({op-system-base} documentation).
====

[IMPORTANT]
====
You are required to use Azure virtual machines that have the `premiumIO` parameter set to `true`.
====

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

[IMPORTANT]
====
Do not use memory ballooning in OpenShift Container Platform clusters. Memory ballooning can cause cluster-wide instabilities, service degradation, or other undefined behaviors.

* Control plane machines should have committed memory equal to or greater than the published minimum resource requirements for a cluster installation.

* Compute machines should have a minimum reservation equal to or greater than the published minimum resource requirements for a cluster installation.

These minimum CPU and memory requirements do not account for resources required by user workloads.

For more information, see the Red Hat Knowledgebase article Memory Ballooning and OpenShift.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/preparing-to-install-on-bare-metal.adoc
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="virt-planning-bare-metal-cluster-for-ocp-virt_{context}"]
= Bare-metal cluster installation requirements for {VirtProductName}

[role="_abstract"]
Configure your bare-metal cluster correctly during installation to support {VirtProductName}, as certain required settings cannot be changed after installation.

[id="virt-planning-bare-metal-cluster-for-ocp-virt-HA_{context}"]
== High availability requirements for {VirtProductName}

When discussing high availability (HA) features in the context of {VirtProductName}, this refers only to the replication model of the core cluster components, determined by the `controlPlaneTopology` and `infrastructureTopology` fields in the `Infrastructure` custom resource (CR).
Setting these fields to `HighlyAvailable` offers component redundancy, which is distinct from general cluster-wide application HA. Setting these fields to `SingleReplica` disables component redundancy, and therefore disables {VirtProductName} HA features.

If you plan to use {VirtProductName} HA features, you must have three control plane nodes at the time of cluster installation. The `controlPlaneTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`.

[NOTE]
====
You can install {VirtProductName} on a single-node cluster, but {sno} does not support HA features.
====

[id="virt-planning-bare-metal-cluster-for-ocp-virt-LM_{context}"]
== Live migration requirements for {VirtProductName}

* If you plan to use live migration, you must have multiple worker nodes. The `infrastructureTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`. A minimum of three worker nodes is recommended.
+
[NOTE]
====
You can install {VirtProductName} on a single-node cluster, but {sno} does not support live migration.
====
* Live migration requires shared storage. Storage for {VirtProductName} must support and use the ReadWriteMany (RWX) access mode.

[id="virt-planning-bare-metal-cluster-for-ocp-virt-SR-IOV_{context}"]
== SR-IOV requirements for {VirtProductName}

If you plan to use Single Root I/O Virtualization (SR-IOV), ensure that your network interface controllers (NICs) are supported by OpenShift Container Platform.

[role="_additional-resources"]
.Additional resources

* Preparing your cluster for {VirtProductName}
* About Single Root I/O Virtualization (SR-IOV) hardware networks
* Connecting a virtual machine to an SR-IOV network

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id='ipi-install-firmware-requirements-for-installing-with-virtual-media_{context}']
= Firmware requirements for installing with virtual media

[role="_abstract"]
The installation program for installer-provisioned OpenShift Container Platform clusters depends on the hardware and firmware compatibility with Redfish virtual media. The installation may not succeed if the node firmware is not compatible.

The following tables list the firmware versions tested and verified to work for installer-provisioned OpenShift Container Platform clusters deployed by using Redfish virtual media.

[NOTE]
====
Red Hat does not test every combination of firmware, hardware, or other third-party components. For further information about third-party support, see Red Hat third-party support policy. For information about updating the firmware, see the hardware documentation for the nodes or contact the hardware vendor.
====

.Firmware compatibility for HP hardware with Redfish virtual media
[cols="1,1,1",options="header"]
|====
| Model | Management | Firmware versions
| 11th Generation | iLO6 | 1.57 or later
| 10th Generation | iLO5 | 2.63 or later

|====

.Firmware compatibility for Dell hardware with Redfish virtual media
[cols="1,1,1",options="header"]
|====
| Model | Management | Firmware versions
| 17th Generation | iDRAC 10| v1.20.25.00, v1.20.60.50, and v1.20.70.50
| 16th Generation | iDRAC 9 | v7.10.70.00
| 15th Generation | iDRAC 9 | v6.10.30.00, v7.10.50.00, and v7.10.70.00
| 14th Generation | iDRAC 9 | v6.10.30.00

|====

.Firmware compatibility for Cisco UCS hardware with Redfish virtual media
[cols="1,1,1",options="header"]
|====
| Model | Management | Firmware versions
| UCS X-Series servers | Intersight Managed Mode  | 5.2(2) or later
| FI-Attached UCS C-Series servers | Intersight Managed Mode | 4.3 or later
| Standalone UCS C-Series servers | Standalone / Intersight | 4.3 or later
|====

[NOTE]
====
Always confirm that your server supports {op-system-first} on UCSHCL.
====

[role="_additional-resources"]
.Additional resources

Unable to discover new bare-metal hosts by using the BMC

// Module included in the following assemblies:
//
// * installing/installing_bare_metal_ipi/ipi-install-prerequisites.adoc

[id="ncsi-hardware-requirements-for-bare-metal_{context}"]
= NC-SI hardware requirements for bare metal

To deploy OpenShift Container Platform 4.19 and later with a Network Controller Sideband Interface (NC-SI) on bare metal, you must use hardware with baseboard management controllers (BMCs) and network interface cards (NICs) that support NC-SI. NC-SI enables the BMC to share a system NIC with the host, requiring the `DisablePowerOff` feature to prevent loss of BMC connectivity during power-offs.

.Server compatibility for NC-SI
[cols="1,1,2,3",options="header"]
|====
| Vendor | Models | Generation | Management
| Dell | PowerEdge | 14th generation and later | iDRAC 9 and later (Redfish, IPMI, racadm, WS-MAN)
| HPE | ProLiant | 10th generation and later | iLO 5 and later (Redfish, IPMI, iLO RESTful API)
| Lenovo | ThinkSystem SR | 1st generation and later | XClarity Controller (Redfish, IPMI, proprietary APIs)
| Supermicro | SuperServer | X11 series and later | Supermicro BMC (Redfish, IPMI, proprietary web/CLI)
| Intel | Server Systems | S2600BP and later | Intel BMC (Redfish, IPMI, proprietary APIs)
| Fujitsu | PRIMERGY | M4 series and later | iRMC S5 and later (Redfish, IPMI, proprietary web/CLI)
| Cisco | UCS C-Series | M5 series and later | Cisco IMC (Redfish, IPMI, proprietary XML API)
|====

.Compatible Network Interface Cards (NICs) for NC-SI
[cols="1,2,2",options="header"]
|====
| Vendor | Models | Specifications
| Broadcom | NetXtreme BCM5720, BCM57416, BCM57504 | Gigabit and 10/25/100GbE, RMII sideband, supports Redfish, IPMI, and vendor protocols.
| Intel | I210, X710, XXV710, E810 | Gigabit to 100GbE, RMII and SMBus sideband, supports Redfish, IPMI, and vendor protocols.
| NVIDIA | ConnectX-5, ConnectX-6, ConnectX-7 | 25/50/100/200/400GbE, RMII sideband, supports Redfish, IPMI, and NVIDIA BMC APIs.
| NVIDIA | BlueField-2 and later | 200/400GbE, supports Redfish, IPMI, and NVIDIA BMC APIs.
| Marvell/Cavium | ThunderX CN88xx, FastLinQ QL41000 | 10/25/50GbE, RMII sideband, supports Redfish, IPMI, and vendor protocols.
| Mellanox (NVIDIA) | MCX4121A-ACAT, MCX512A-ACAT | 10/25/50GbE, RMII sideband, supports Redfish, IPMI, and Mellanox APIs.
|====

[NOTE]
====
Verify NC-SI support with vendor documentation, because compatibility depends on BMC, NIC, and firmware configurations. NC-SI NICs require a compatible BMC to enable shared NIC functionality.
====

[role="_additional-resources"]
.Additional resources
* Ironic NC-SI Specification
* DMTF: Network Controller Sideband Interface (NC-SI) Specification

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="network-requirements_{context}"]
= Network requirements

Installer-provisioned installation of OpenShift Container Platform involves multiple network requirements. First, installer-provisioned installation involves an optional non-routable `provisioning` network for provisioning the operating system on each bare-metal node. Second, installer-provisioned installation involves a routable `baremetal` network.

image::210_OpenShift_Baremetal_IPI_Deployment_updates_0122_2.png[Installer-provisioned networking]

[id="network-requirements-ensuring-required-ports-are-open_{context}"]
== Ensuring required ports are open

Certain ports must be open between cluster nodes for installer-provisioned installations to complete successfully. In certain situations, such as using separate subnets for far edge worker nodes, you must ensure that the nodes in these subnets can communicate with nodes in the other subnets on the following required ports.

.Required ports
[options="header"]
|====
|Port|Description

|`67`,`68` | When using a provisioning network, cluster nodes access the `dnsmasq` DHCP server over their provisioning network interfaces using ports `67` and `68`.

| `69` | When using a provisioning network, cluster nodes communicate with the TFTP server on port `69` using their provisioning network interfaces. The TFTP server runs on the bootstrap VM. The bootstrap VM runs on the provisioner node.

| `80` | When not using the image caching option or when using virtual media, the provisioner node must have port `80` open on the `baremetal` machine network interface to stream the {op-system-first} image from the provisioner node to the cluster nodes.

| `123` | The cluster nodes must access the NTP server on port `123` using the `baremetal` machine network.

|`5050`| The Ironic Inspector API runs on the control plane nodes and listens on port `5050`. The Inspector API is responsible for hardware introspection, which collects information about the hardware characteristics of the bare-metal nodes.

|`5051`| Port `5050` uses port `5051` as a proxy.

|`6180`| When deploying with virtual media and not using TLS, the provisioner node and the control plane nodes must have port `6180` open on the `baremetal` machine network interface so that the baseboard management controller (BMC) of the worker nodes can access the {op-system} image. Starting with OpenShift Container Platform 4.13, the default HTTP port is `6180`.

|`6183`| When deploying with virtual media and using TLS, the provisioner node and the control plane nodes must have port `6183` open on the `baremetal` machine network interface so that the BMC of the worker nodes can access the {op-system} image.

|`6385`| The Ironic API server runs initially on the bootstrap VM and later on the control plane nodes and listens on port `6385`. The Ironic API allows clients to interact with Ironic for bare-metal node provisioning and management, including operations such as enrolling new nodes, managing their power state, deploying images, and cleaning the hardware.

|`6388`| Port `6385` uses port `6388` as a proxy.

|`8080`| When using image caching without TLS, port `8080` must be open on the provisioner node and accessible by the BMC interfaces of the cluster nodes.

|`8083`| When using the image caching option with TLS, port `8083` must be open on the provisioner node and accessible by the BMC interfaces of the cluster nodes.

|`9999`| By default, the Ironic Python Agent (IPA) listens on TCP port `9999` for API calls from the Ironic conductor service. Communication between the bare-metal node where IPA is running and the Ironic conductor service uses this port.

|====

[id="network-requirements-increase-mtu_{context}"]
== Increase the network MTU

Before deploying OpenShift Container Platform, increase the network maximum transmission unit (MTU) to 1500 or more. If the MTU is lower than 1500, the Ironic image that is used to boot the node might fail to communicate with the Ironic inspector pod, and inspection will fail. If this occurs, installation stops because the nodes are not available for installation.

[id="network-requirements-config-nics_{context}"]
== Configuring NICs

OpenShift Container Platform deploys with two networks:

- `provisioning`: The `provisioning` network is an optional non-routable network used for provisioning the underlying operating system on each node that is a part of the OpenShift Container Platform cluster. The network interface for the `provisioning` network on each cluster node must have the BIOS or UEFI configured to PXE boot.
+
The `provisioningNetworkInterface` configuration setting specifies the `provisioning` network NIC name on the control plane nodes, which must be identical on the control plane nodes. The `bootMACAddress` configuration setting provides a means to specify a particular NIC on each node for the `provisioning` network.
+
The `provisioning` network is optional, but it is required for PXE booting. If you deploy without a `provisioning` network, you must use a virtual media BMC addressing option such as `redfish-virtualmedia` or `idrac-virtualmedia`.

- `baremetal`: The `baremetal` network is a routable network. You can use any NIC to interface with the `baremetal` network provided the NIC is not configured to use the `provisioning` network.

[IMPORTANT]
====
When using a VLAN, each NIC must be on a separate VLAN corresponding to the appropriate network.
====

[id="network-requirements-dns_{context}"]
== DNS requirements

[id="network-requirements-dhcp-reqs_{context}"]
== Dynamic Host Configuration Protocol (DHCP) requirements

By default, installer-provisioned installation deploys `ironic-dnsmasq` with DHCP enabled for the `provisioning` network. No other DHCP servers should be running on the `provisioning` network when the `provisioningNetwork` configuration setting is set to `managed`, which is the default value. If you have a DHCP server running on the `provisioning` network, you must set the `provisioningNetwork` configuration setting to `unmanaged` in the `install-config.yaml` file.

Network administrators must reserve IP addresses for each node in the OpenShift Container Platform cluster for the `baremetal` network on an external DHCP server.

[id="network-requirements-reserving-ip-addresses_{context}"]
== Reserving IP addresses for nodes with the DHCP server

For the `baremetal` network, a network administrator must reserve several IP addresses, including:

. Two unique virtual IP addresses.
+
- One virtual IP address for the API endpoint.
- One virtual IP address for the wildcard ingress endpoint.
+
. One IP address for the provisioner node.
. One IP address for each control plane node.
. One IP address for each worker node, if applicable.

[IMPORTANT]
.Reserving IP addresses so they become static IP addresses
====
Some administrators prefer to use static IP addresses so that each node's IP address remains constant in the absence of a DHCP server. To configure static IP addresses with NMState, see "(Optional) Configuring node network interfaces" in the "Setting up the environment for an OpenShift installation" section.
====

[IMPORTANT]
.Networking between external load balancers and control plane nodes
====
External load balancing services and the control plane nodes must run on the same L2 network, and on the same VLAN when using VLANs to route traffic between the load balancing services and the control plane nodes.
====

[IMPORTANT]
====
The storage interface requires a DHCP reservation or a static IP.
====

The following table provides an exemplary embodiment of fully qualified domain names. The API and name server addresses begin with canonical name extensions. The hostnames of the control plane and worker nodes are exemplary, so you can use any host naming convention you prefer.

[width="100%", cols="3,5,2", options="header"]
|=====
| Usage | Host Name | IP
| API | `api.<cluster_name>.<base_domain>` | `<ip>`
| Ingress LB (apps) |  `*.apps.<cluster_name>.<base_domain>`  | `<ip>`
| Provisioner node | `provisioner.<cluster_name>.<base_domain>` | `<ip>`
| Control-plane-0 | `openshift-control-plane-0.<cluster_name>.<base_domain>` | `<ip>`
| Control-plane-1 | `openshift-control-plane-1.<cluster_name>-.<base_domain>` | `<ip>`
| Control-plane-2 | `openshift-control-plane-2.<cluster_name>.<base_domain>` | `<ip>`
| Worker-0 | `openshift-worker-0.<cluster_name>.<base_domain>` | `<ip>`
| Worker-1 | `openshift-worker-1.<cluster_name>.<base_domain>` | `<ip>`
| Worker-n | `openshift-worker-n.<cluster_name>.<base_domain>` | `<ip>`
|=====

[NOTE]
====
If you do not create DHCP reservations, the installation program requires reverse DNS resolution to set the hostnames for the Kubernetes API node, the provisioner node, the control plane nodes, and the worker nodes.
====

[id="network-requirements-provisioner_{context}"]
== Provisioner node requirements

You must specify the MAC address for the provisioner node in your installation configuration. The `bootMacAddress` specification is typically associated with PXE network booting. However, the Ironic provisioning service also requires the `bootMacAddress` specification to identify nodes during the inspection of the cluster, or during node redeployment in the cluster.

The provisioner node requires layer 2 connectivity for network booting, DHCP and DNS resolution, and local network communication. The provisioner node requires layer 3 connectivity for virtual media booting.

[id="network-requirements-ntp_{context}"]
== Network Time Protocol (NTP)

Each OpenShift Container Platform node in the cluster must have access to an NTP server. OpenShift Container Platform nodes use NTP to synchronize their clocks. For example, cluster nodes use SSL/TLS certificates that require validation, which might fail if the date and time between the nodes are not in sync.

[IMPORTANT]
====
Define a consistent clock date and time format in each cluster node's BIOS settings, or installation might fail.
====

You can reconfigure the control plane nodes to act as NTP servers on disconnected clusters, and reconfigure worker nodes to retrieve time from the control plane nodes.

[id="network-requirements-out-of-band_{context}"]
== Port access for the out-of-band management IP address

The out-of-band management IP address is on a separate network from the node. To ensure that the out-of-band management can communicate with the provisioner node during installation, the out-of-band management IP address must be granted access to port `6180` on the provisioner node and on the OpenShift Container Platform control plane nodes. TLS port `6183` is required for virtual media installation, for example, by using Redfish.

[role="_additional-resources"]
.Additional resources

* Using DNS forwarding

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="configuring-nodes_{context}"]
= Configuring nodes

== Configuring nodes when using the `provisioning` network

Each node in the cluster requires the following configuration for proper installation.

[WARNING]
====
A mismatch between nodes will cause an installation failure.
====

While the cluster nodes can contain more than two NICs, the installation process only focuses on the first two NICs. In the following table, NIC1 is a non-routable network (`provisioning`) that is only used for the installation of the OpenShift Container Platform cluster.

[options="header"]
|===
|NIC |Network |VLAN
| NIC1 | `provisioning` | `<provisioning_vlan>`
| NIC2 | `baremetal` | `<baremetal_vlan>`
|===

[options="header"]
|===
|PXE |Boot order
| NIC1 PXE-enabled `provisioning` network | 1
| NIC2 `baremetal` network. PXE-enabled is optional. | 2
|===

[NOTE]
====
Ensure PXE is disabled on all other NICs.
====

Configure the control plane and worker nodes as follows:

[options="header"]
|===
|PXE | Boot order
| NIC1 PXE-enabled (provisioning network) | 1
|===

== Configuring nodes without the `provisioning` network

The installation process requires one NIC:

[options="header"]
|===
|NIC |Network |VLAN
| NICx | `baremetal` | `<baremetal_vlan>`
|===

NICx is a routable network (`baremetal`) that is used for the installation of the OpenShift Container Platform cluster, and routable to the internet.

[IMPORTANT]
====
The `provisioning` network is optional, but it is required for PXE booting. If you deploy without a `provisioning` network, you must use a virtual media BMC addressing option such as `redfish-virtualmedia` or `idrac-virtualmedia`.
====

[id="configuring-nodes-for-secure-boot_{context}"]

== Configuring nodes for Secure Boot manually

Secure Boot prevents a node from booting unless it verifies the node is using only trusted software, such as UEFI firmware drivers, EFI applications, and the operating system.

[NOTE]
====
Red Hat only supports manually configured Secure Boot when deploying with Redfish virtual media.
====

To enable Secure Boot manually, refer to the hardware guide for the node and execute the following:

.Procedure
. Boot the node and enter the BIOS menu.
. Set the node's boot mode to `UEFI Enabled`.
. Enable Secure Boot.

[IMPORTANT]
====
Red Hat does not support Secure Boot with self-generated keys.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="out-of-band-management_{context}"]
= Out-of-band management

Nodes typically have an additional NIC used by the baseboard management controllers (BMCs). These BMCs must be accessible from the provisioner node.

Each node must be accessible via out-of-band management. When using an out-of-band management network, the provisioner node requires access to the out-of-band management network for a successful OpenShift Container Platform installation.

The out-of-band management setup is out of scope for this document. Using a separate management network for out-of-band management can enhance performance and improve security. However, using the provisioning network or the bare metal network are valid options.

[NOTE]
====
The bootstrap VM features a maximum of two network interfaces. If you configure a separate management network for out-of-band management, and you are using a provisioning network, the bootstrap VM requires routing access to the management network through one of the network interfaces. In this scenario, the bootstrap VM can then access three networks:

* the bare metal network
* the provisioning network
* the management network routed through one of the network interfaces
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="required-data-for-installation_{context}"]
= Required data for installation

Prior to the installation of the OpenShift Container Platform cluster, gather the following information from all cluster nodes:

* Out-of-band management IP
** Examples
*** Dell (iDRAC) IP
*** HP (iLO) IP
*** Fujitsu (iRMC) IP

.When using the `provisioning` network

* NIC (`provisioning`) MAC address
* NIC (`baremetal`) MAC address

.When omitting the `provisioning` network

* NIC (`baremetal`) MAC address

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="validation-checklist-for-nodes_{context}"]
= Validation checklist for nodes

.When using the `provisioning` network

* [ ] NIC1 VLAN is configured for the `provisioning` network.
* [ ] NIC1 for the `provisioning` network is PXE-enabled on the provisioner, control plane, and worker nodes.
* [ ] NIC2 VLAN is configured for the `baremetal` network.
* [ ] PXE has been disabled on all other NICs.
* [ ] DNS is configured with API and Ingress endpoints.
* [ ] Control plane and worker nodes are configured.
* [ ] All nodes accessible via out-of-band management.
* [ ] (Optional) A separate management network has been created.
* [ ] Required data for installation.

.When omitting the `provisioning` network

* [ ] NIC1 VLAN is configured for the `baremetal` network.
* [ ] DNS is configured with API and Ingress endpoints.
* [ ] Control plane and worker nodes are configured.
* [ ] All nodes accessible via out-of-band management.
* [ ] (Optional) A separate management network has been created.
* [ ] Required data for installation.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-prerequisites.adoc

[id="installation-overview_{context}"]
= Installation overview

The installation program supports interactive mode. However, you can prepare an `install-config.yaml` file containing the provisioning details for all of the bare-metal hosts, and the relevant cluster details, in advance.

The installation program loads the `install-config.yaml` file and the administrator generates the manifests and verifies all prerequisites.

The installation program performs the following tasks:

* Enrolls all nodes in the cluster
* Starts the bootstrap virtual machine (VM)
* Starts the metal platform components as `systemd` services, which have the following containers:

** Ironic-dnsmasq: The DHCP server responsible for handing over the IP addresses to the provisioning interface of various nodes on the provisioning network. Ironic-dnsmasq is only enabled when you deploy an OpenShift Container Platform cluster with a provisioning network.
** Ironic-httpd: The HTTP server that is used to ship the images to the nodes.
** Image-customization
** Ironic
** Ironic-inspector (available in OpenShift Container Platform 4.16 and earlier)
** Ironic-ramdisk-logs
** Extract-machine-os
** Provisioning-interface
** Metal3-baremetal-operator

The nodes enter the validation phase, where each node moves to a _manageable_ state after Ironic validates the credentials to access the Baseboard Management Controller (BMC).

When the node is in the manageable state, the _inspection_ phase starts. The inspection phase ensures that the hardware meets the minimum requirements needed for a successful deployment of OpenShift Container Platform.

The `install-config.yaml` file details the provisioning network. On the bootstrap VM, the installation program uses the Pre-Boot Execution Environment (PXE) to push a live image to every node with the Ironic Python Agent (IPA) loaded. When using virtual media, it connects directly to the BMC of each node to virtually attach the image.

When using PXE boot, all nodes reboot to start the process:

* The `ironic-dnsmasq` service running on the bootstrap VM provides the IP address of the node and the TFTP boot server.
* The first-boot software loads the root file system over HTTP.
* The `ironic` service on the bootstrap VM receives the hardware information from each node.

The nodes enter the cleaning state, where each node must clean all the disks before continuing with the configuration.

After the cleaning state finishes, the nodes enter the available state and the installation program moves the nodes to the deploying state.

IPA runs the `coreos-installer` command to install the {op-system-first} image on the disk defined by the `rootDeviceHints` parameter in the `install-config.yaml` file. The node boots by using {op-system}.

After the installation program configures the control plane nodes, it moves control from the bootstrap VM to the control plane nodes and deletes the bootstrap VM.

The Bare-Metal Operator continues the deployment of the workers, storage, and infra nodes.

After the installation completes, the nodes move to the active state. You can then proceed with postinstallation configuration and other Day 2 tasks.
