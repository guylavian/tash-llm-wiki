---
title: "Prerequisites for virtualized control planes"
type: reference
domain: openshift
slug: vcp-4-22-vcp-prerequisites
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/vcp/vcp-prerequisites
version: 4.22
family: vcp
documentKind: "Documentation"
---

# Prerequisites for virtualized control planes

[id="vcp-prerequisites"]
= Prerequisites for virtualized control planes

[role="_abstract"]
Before deploying a virtualized control plane cluster, ensure your environment meets the following requirements.

// Module included in the following assemblies:
//
// * vcp/vcp-prerequisites.adoc

[id="con_virt-vcp-hosting-cluster-requirements_{context}"]
= Hosting cluster requirements

[role="_abstract"]
The hosting cluster runs the virtualized control plane VMs and manages their lifecycle through KubeVirt Redfish.

The hosting cluster requires the following components:

* OpenShift Container Platform installed and operational.
* {VirtProductName} installed and configured.
* Sufficient compute resources to host control plane VMs.
* At least three physical nodes to enable anti-affinity placement, ensuring control plane VMs are spread across different physical hosts.

// Module included in the following assemblies:
//
// * vcp/vcp-prerequisites.adoc

[id="con_virt-vcp-storage-requirements_{context}"]
= Storage requirements

[role="_abstract"]
The hosting cluster must have a storage solution that supports VM disk images and meets the latency requirements of `etcd`.

The hosting cluster must have one of the following storage solutions:

* {odf-first} provides VM live migration. When you install {odf-short} on a cluster where {VirtProductName} is running, the `ocs-storagecluster-ceph-rbd-virtualization` storage class is created automatically. This storage class is optimized for KubeVirt workloads.
* {lvms-first}, backed by NVMe drives, provides predictable, low-latency disk I/O but does not support VM live migration.

Consider the following when choosing a storage solution:

* {odf-short} replicates data across multiple storage nodes for durability. This replication can cause unpredictable latency spikes during synchronization, which might affect `etcd` performance. Monitor `etcd` disk latency in production and ensure the underlying storage nodes use NVMe disks.
* {lvms} writes directly to local disks without replication, providing consistent low latency. However, data is not replicated across nodes.

// Module included in the following assemblies:
//
// * vcp/vcp-prerequisites.adoc

[id="con_virt-vcp-network-requirements_{context}"]
= Network requirements

[role="_abstract"]
Virtualized control plane deployments require specific network connectivity between VMs, worker nodes, and external services.

Configure networking to meet the following requirements:

* L2 network connectivity between control plane VMs. The OpenShift Container Platform installation program requires all control plane nodes to share the same L2 network segment.
* L3 connectivity without network address translation (NAT) between the control plane VMs and worker nodes. Worker nodes must be able to route traffic directly to the control plane VMs. During installation, the bootstrap VM also requires L3 connectivity to the control plane.
* External access to the cluster API.
* Access to container image registries.
* DNS resolution for cluster components.

You can use either dynamic or static IP addressing for the control plane VMs:

* For deployments that use DHCP, configure static MAC addresses on the primary network interfaces of the VMs and create DHCP reservations for each MAC address. This ensures consistent IP assignment across VM restarts.
* For deployments that use static IP addressing, define the network configuration in your `install-config.yaml` or Agent-based installation manifests.

// Module included in the following assemblies:
//
// * vcp/vcp-prerequisites.adoc

[id="con_virt-vcp-control-plane-vm-requirements_{context}"]
= Control plane VM requirements

[role="_abstract"]
Each control plane VM must meet minimum resource requirements to run the OpenShift Container Platform control plane components reliably.

Each control plane VM requires the following minimum resources:

* 8 vCPUs
* 16 GiB RAM
* 120 GiB storage

// Module included in the following assemblies:
//
// * vcp/vcp-prerequisites.adoc

[id="con_virt-vcp-kubevirt-redfish-requirements_{context}"]
= KubeVirt Redfish requirements

[role="_abstract"]
KubeVirt Redfish exposes VMs through the Redfish API.

You need the following to use KubeVirt Redfish:

* Network access from the installation workstation to the KubeVirt Redfish route.
* Credentials configured in KubeVirt Redfish for API authentication.
* VMs labeled to be exposed through the Redfish API.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Recommended resources for the agent-based installer
* Effects of disk latency on etcd
