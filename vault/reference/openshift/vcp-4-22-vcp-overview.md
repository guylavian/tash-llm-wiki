---
title: "Understanding virtualized control planes"
type: reference
domain: openshift
slug: vcp-4-22-vcp-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/vcp/vcp-overview
version: 4.22
family: vcp
documentKind: "Documentation"
---

# Understanding virtualized control planes

[id="vcp-overview"]
= Understanding virtualized control planes

[role="_abstract"]
A virtualized control plane deployment is an OpenShift Container Platform cluster whose control plane nodes run as virtual machines (VMs) on a hosting cluster with {VirtProductName}.

This architecture is useful in the following example scenarios:

* Regulatory requirements mandate VM-level isolation for control plane components.
* You want to reduce hardware costs by consolidating multiple cluster control planes on shared infrastructure.
* You need faster provisioning of new clusters compared to physical bare metal.

In a virtualized control plane deployment, you have two clusters:

Hosting cluster:: An existing OpenShift Container Platform cluster running {VirtProductName} that hosts the control plane VMs.
Target cluster:: The OpenShift Container Platform cluster with control planes running on the VMs.

KubeVirt Redfish runs on the hosting cluster and exposes the VMs through the standard Redfish API endpoints.

With this approach, you can use installation workflows such as Agent-based Installer or {ztp-first}, to deploy virtualized control planes exactly like physical servers with baseboard management controllers (BMCs).

[NOTE]
====
Virtualized control planes differ from {hcp-capital}.
With virtualized control planes, the control plane runs as VMs with hypervisor-level isolation.
With {hcp-capital}, the control plane runs as pods with container-level isolation.
====

// Module included in the following assemblies:
//
// * vcp/vcp-overview.adoc

[id="con_virt-vcp-architecture_{context}"]
= Virtualized control plane architecture

[role="_abstract"]
A virtualized control plane deployment runs control plane components as VMs on a hosting cluster, providing hypervisor-level isolation between clusters.

A single hosting cluster can support multiple target clusters by running each cluster's control plane VMs in separate namespaces.
This consolidation reduces hardware costs while maintaining isolation.
The target cluster's worker nodes run on separate infrastructure, either physical servers or VMs on different hosts.

For high availability, distribute control plane VMs across different physical nodes on the hosting cluster.
This anti-affinity placement ensures that if a physical node fails, only one control plane VM is affected and the remaining nodes maintain etcd quorum.
Configure anti-affinity using pod anti-affinity rules or topology spread constraints in the VM specifications.

// Module included in the following assemblies:
//
// * vcp/vcp-overview.adoc

[id="con_virt-vcp-deployment-workflow_{context}"]
= Virtualized control plane deployment workflow

[role="_abstract"]
Deploy a virtualized control plane cluster by installing KubeVirt Redfish on your hosting cluster, configuring it to expose your VMs, and running your preferred installation method.

[NOTE]
====
Virtualized control planes require an OpenShift Container Platform cluster with {VirtProductName} installed and operational, which operates as the hosting cluster.
====

See the following high-level steps to deploy a virtualized control plane cluster:

. Install and configure KubeVirt Redfish on the hosting cluster. This includes defining which VMs to expose through the Redfish API, configuring authentication credentials, and creating a `Route` CR to expose the endpoint externally.

. Create the control plane VMs on the hosting cluster. Configure the VMs with appropriate resources and network settings, and ensure they remain powered off until the installation begins.

. Configure your installation method to use KubeVirt Redfish. In your configuration files, specify BMC addresses using the KubeVirt Redfish route URL for the virtualized control plane nodes, for example: `redfish-virtualmedia+https://<kubevirt_redfish_route>/redfish/v1/Systems/<vm_namespace>.<vm_name>`.

. Run the installation. The VMs boot from the installation media and communicate with each other to form the cluster. Depending on the installation method, this process is either fully automated or requires manual intervention to boot each node.

. After installation completes, a new OpenShift Container Platform cluster is deployed with its control plane running on VMs hosted by the original {VirtProductName} cluster.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Prerequisites for virtualized control planes
* Installing KubeVirt Redfish
* Configuring KubeVirt Redfish for VM management
* BMC addressing for installer-provisioned infrastructure
* Deploying far edge sites with ZTP
