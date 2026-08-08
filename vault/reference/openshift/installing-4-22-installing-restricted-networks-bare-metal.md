---
title: "Installing a user-provisioned bare metal cluster on a disconnected environment"
type: reference
domain: openshift
slug: installing-4-22-installing-restricted-networks-bare-metal
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-restricted-networks-bare-metal
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a user-provisioned bare metal cluster on a disconnected environment

[id="installing-restricted-networks-bare-metal"]
= Installing a user-provisioned bare metal cluster on a disconnected environment

In OpenShift Container Platform , you can install a cluster on
bare metal infrastructure that you provision in a restricted network.

[IMPORTANT]
====
While you might be able to follow this procedure to deploy a cluster on
virtualized or cloud environments, you must be aware of additional
considerations for non-bare metal platforms. Review the information in the
guidelines for deploying OpenShift Container Platform on non-tested platforms
before you attempt to install an OpenShift Container Platform cluster in such an environment.
====

== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You created a registry on your mirror host and obtained the `imageContentSources` data for your version of OpenShift Container Platform.
+
[IMPORTANT]
====
Because the installation media is on the mirror host, you can use that computer to complete all installation steps.
====
* You provisioned persistent storage for your cluster. To deploy a private image registry, your storage must provide ReadWriteMany access modes.
* If you use a firewall and plan to use the Telemetry service, you configured the firewall to allow the sites that your cluster requires access to.
+
[NOTE]
====
Be sure to also review this site list if you are configuring a proxy.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc

[id="installation-about-restricted-networks_{context}"]
= About installations in restricted networks

In OpenShift Container Platform , you can perform an installation that does not
require an active connection to the internet to obtain software components. Restricted network installations can be completed using installer-provisioned infrastructure or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

If you choose to perform a restricted network installation on a cloud platform, you
still require access to its cloud APIs. Some cloud functions, like
Amazon Web Service's Route 53 DNS and IAM services, require internet access.
//behind a proxy
Depending on your network, you might require less internet
access for an installation on bare metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that
mirrors the contents of the {product-registry} and contains the
installation media. You can create this registry on a mirror host, which can
access both the internet and your closed network, or by using other methods
that meet your restrictions.

[IMPORTANT]
====
Because of the complexity of the configuration for user-provisioned installations, consider completing a standard user-provisioned infrastructure installation before you attempt a restricted network installation using user-provisioned infrastructure. Completing this test installation might make it easier to isolate and troubleshoot any issues that might arise during your installation in a restricted network.
====

[id="required-internet-access-and-an-installation-host_{context}"]
== Required internet access and an installation host

You complete the installation using a bastion host or portable device that can access both the internet and your closed network. You must use a host with internet access to:

* Download the installation program, the OpenShift CLI (`oc`), and the CCO utility (`ccoctl`).
* Use the installation program to locate the {op-system-first} image and create the installation configuration file.
* Use `oc` to extract `ccoctl` from the CCO container image.
* Use `oc` and `ccoctl` to configure IAM for {ibm-cloud-name}.

[id="access-to-a-mirror-registry_{context}"]
== Access to a mirror registry

To complete a restricted network installation, you must create a registry that
mirrors the contents of the {product-registry} and contains the installation media.

You can create this registry on a mirror host, which can access both the internet and your restricted network, or by using other methods that meet your organization's security restrictions.

For more information on mirroring images for a disconnected installation, see "Additional resources".

[id="access-to-ibm-service-endpoints_{context}"]
== Access to IBM service endpoints

The installation program requires access to the following {ibm-cloud-name} service endpoints:

* Cloud Object Storage
* DNS Services
* Global Search
* Global Tagging
* Identity Services
* Resource Controller
* Resource Manager
* VPC

[NOTE]
====
If you are specifying an {ibm-name} Key Protect for {ibm-cloud-name} root key as part of the installation process, the service endpoint for Key Protect is also required.
====

By default, the public endpoint is used to access the service. If network restrictions limit access to public service endpoints, you can override the default behavior.

Before deploying the cluster, you can update the installation configuration file (`install-config.yaml`) to specify the URI of an alternate service endpoint. For more information on usage, see "Additional resources".

[id="installation-restricted-network-limits_{context}"]
== Additional limits

Clusters in restricted networks have the following additional limitations and restrictions:

* The `ClusterVersion` status includes an `Unable to retrieve available updates`
error.
//* The authentication Operator might randomly fail.
* By default, you cannot use the contents of the Developer Catalog because
 you cannot access the required image stream tags.
//* The `TelemeterClientDown` and `Watchdog` alerts from the monitoring Operator always display.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-network-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china-region.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_openstack/installing-openstack-user-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
// * architecture/architecture.adoc
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc

[id="cluster-entitlements_{context}"]
= Internet access for OpenShift Container Platform

[role="_abstract"]
In OpenShift Container Platform , you require access to the internet to
install
obtain the images that are necessary to install
your cluster.

You must have internet access to perform the following actions:

* Access {cluster-manager-url} to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

[IMPORTANT]
====
If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.
====

[id="installation-requirements-user-infra_{context}"]
== Requirements for a cluster with user-provisioned infrastructure

For a cluster that contains user-provisioned infrastructure, you must deploy all
of the required machines.

This section describes the requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z-reqs.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="installation-machine-requirements_{context}"]
= Required machines for cluster installation

[role="_abstract"]
You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

[IMPORTANT]
====
For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.
====

.Minimum required hosts
[options="header"]
|===

|Hosts |Description

|One temporary bootstrap machine
|The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster
on the three control plane machines. You can remove the bootstrap machine after
you install the cluster.

|Three control plane machines
|The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane.

|At least two compute machines, which are also known as worker machines.
|The workloads requested by OpenShift Container Platform users run on the compute machines.

|===

[NOTE]
====
As an exception, you can run zero compute machines in a bare metal cluster that consists of three control plane machines only. This provides smaller, more resource efficient clusters for cluster administrators and developers to use for testing, development, and production. Running one compute machine is not supported.
====

[IMPORTANT]
====
To improve high availability of your cluster, distribute the control plane machines over different hypervisor instances on at least two physical machines.
To maintain high availability of your cluster, use separate physical hosts for
these cluster machines.
====

The bootstrap and control plane machines must use {op-system-first} as the operating system. However, the compute machines can choose between {op-system-first}, {op-system-base-full} 8.6 and later.
The bootstrap, control plane, and compute machines must use {op-system-first} as the operating system.

Note that {op-system} is based on {op-system-base-full} 9.8 and inherits all of its hardware certifications and requirements.
See Red Hat Enterprise Linux technology capabilities and limits.

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

[role="_additional-resources"]
.Additional resources

* Optimizing storage

// Module included in the following assemblies:
//
// installing/installing_aws/installing-aws-user-infra.adoc
// installing/installing_aws/installing-restricted-networks-aws.adoc
// installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// installing/installing_azure/installing-azure-user-infra.adoc
// installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// installing/installing_bare_metal/upi/installing-bare-metal.adoc
// installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// installing/installing_gcp/installing-gcp-user-infra.adoc
// installing/installing_gcp/installing-restricted-networks-gcp.adoc
// installing/installing_ibm_power/installing-ibm-power.adoc
// installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// installing/installing_ibm_z/installing-ibm-z.adoc
// installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// machine_management/adding-rhel-compute.adoc
// machine_management/more-rhel-compute.adoc
// post_installation_configuration/node-tasks.adoc
// installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="csr-management_{context}"]
= Certificate signing requests management

[role="_abstract"]
On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

[role="_additional-resources"]
.Additional resources

* See Configuring a three-node cluster for details about deploying three-node clusters in bare metal environments.
* See Approving the certificate signing requests for your machines for more information about approving cluster certificate signing requests after installation.

// Networking requirements for user-provisioned infrastructure
// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="installation-network-user-infra_{context}"]
= Networking requirements for user-provisioned infrastructure

[role="_abstract"]
You must configure networking for all the {op-system-first} machines in `initramfs` during boot, so that they can fetch their Ignition config files.

[IMPORTANT]
====
Ensure you enable the `disk.EnableUUID` parameter on all virtual machines in your cluster.
====

During the initial boot, the machines require an HTTP or HTTPS server to
establish a network connection to download their Ignition config files.

The machines are configured with static IP addresses. No DHCP server is required. Ensure that the machines have persistent IP addresses and hostnames.
During the initial boot, the machines require an IP address configuration that is set either through a DHCP server or statically by providing the required boot options. After a network connection is established, the machines download their Ignition config files from an HTTP or HTTPS server. The Ignition config files are then used to set the exact state of each machine. The Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation.

[NOTE]
====
* Consider using a DHCP server for long-term management of the cluster machines. Ensure that the DHCP server is configured to provide persistent IP addresses, DNS server information, and hostnames to the cluster machines.

* If a DHCP service is not available for your user-provisioned infrastructure, you can instead provide the IP networking configuration and the address of the DNS server to the nodes at {op-system} install time. These can be passed as boot arguments if you are installing from an ISO image. See the _Installing {op-system} and starting the OpenShift Container Platform bootstrap process_ section for more information about static IP provisioning and advanced networking options.
====

The Kubernetes API server must be able to resolve the node names of the cluster machines. If the API servers and worker nodes are in different zones, you can configure a default DNS search zone to allow the API server to resolve the node names. Another supported approach is to always refer to hosts by their fully-qualified domain names in both the node objects and all DNS requests.

[id="installation-host-names-dhcp-user-infra_{context}"]
== Setting the cluster node hostnames through DHCP

On {op-system-first} machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

[id="installation-network-connectivity-user-infra_{context}"]
== Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

[IMPORTANT]
====
In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images
for platform containers and provide telemetry data to Red Hat.
====

[NOTE]
====
In a {op-system-base} KVM environment the host must be configured to use bridged networking in libvirt or MacVTap to connect the network to the virtual machines. The virtual machines must have access to the network, which is attached to the {op-system-base} KVM host. Virtual Networks, for example network address translation (NAT), within KVM are not a supported configuration.
====

.Ports used for all-machine to all-machine communications
[cols="2a,2a,5a",options="header"]
|===

|Protocol
|Port
|Description

|ICMP
|N/A
|Network reachability tests

.4+|TCP
|`1936`
|Metrics

|`9000`-`9999`
|Host level services, including the node exporter on ports `9100`-`9101` and
the Cluster Version Operator on port `9099`.

|`10250`-`10259`
|The default ports that Kubernetes reserves

|`22623`
|The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines.
.6+|UDP

|`6081`
|Geneve

|`9000`-`9999`
|Host level services, including the node exporter on ports `9100`-`9101`.

|`500`
|IPsec IKE packets

|`4500`
|IPsec NAT-T packets

|`123`
|Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`.

|TCP/UDP
|`30000`-`32767`
|Kubernetes node port

|ESP
|N/A
|IPsec Encapsulating Security Payload (ESP)

|===

.Ports used for all-machine to control plane communications
[cols="2a,2a,5a",options="header"]
|===

|Protocol
|Port
|Description

|TCP
|`6443`
|Kubernetes API

|===

.Ports used for control plane machine to control plane machine communications
[cols="2a,2a,5a",options="header"]
|===

|Protocol
|Port
|Description

|TCP
|`2379`-`2380`
|etcd server and peer ports

|===

== NTP configuration for user-provisioned infrastructure

OpenShift Container Platform clusters are configured to use a public Network Time Protocol (NTP) server by default. If you want to use a local enterprise NTP server, or if your cluster is being deployed in a disconnected network, you can configure the cluster to use a specific time server. For more information, see the documentation for _Configuring chrony time service_.

If a DHCP server provides NTP server information, the chrony time service on the {op-system-first} machines read the information and can sync the clock with the NTP servers.

[role="_additional-resources"]
.Additional resources

* Configuring chrony time service

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-network-customizations-user-infra.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="installation-dns-user-infra_{context}"]
= User-provisioned DNS requirements

[role="_abstract"]
In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

* The Kubernetes API
* The OpenShift Container Platform application wildcard
* The bootstrap and control plane machines
* The compute machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, and the control plane machines.

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because {op-system-first} uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

[NOTE]
====
It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the _DHCP recommendations for user-provisioned infrastructure_ section for more information.
====

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

.Required DNS records
[cols="1a,3a,5a",options="header"]
|===

|Component
|Record
|Description

.2+a|Kubernetes API
|`api.<cluster_name>.<base_domain>.`
|A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.

|`api-int.<cluster_name>.<base_domain>.`
|A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.
[IMPORTANT]
====
The API server must be able to resolve the worker nodes by the hostnames
that are recorded in Kubernetes. If the API server cannot resolve the node
names, then proxied API calls can fail, and you cannot retrieve logs from pods.
====

|Routes
|`*.apps.<cluster_name>.<base_domain>.`
|A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods.
By default, the Ingress Controller pods run on compute nodes. In cluster topologies without dedicated compute nodes, such as two-node or three-node clusters, the control plane nodes also carry the worker label, so the Ingress pods are scheduled on the control plane nodes.
The Ingress Controller pods run on the compute machines by default.
These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.

For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console.

|Bootstrap machine
|`bootstrap.<cluster_name>.<base_domain>.`
|A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap
machine. These records must be resolvable by the nodes within the cluster.

|Control plane machines
|`<control_plane><n>.<cluster_name>.<base_domain>.`
|DNS A/AAAA or CNAME records and DNS PTR records to identify each machine
for the control plane nodes. These records must be resolvable by the nodes within the cluster.

|Compute machines
|`<compute><n>.<cluster_name>.<base_domain>.`
|DNS A/AAAA or CNAME records and DNS PTR records to identify each machine
for the worker nodes. These records must be resolvable by the nodes within the cluster.

|===

[NOTE]
====
In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.
====

[TIP]
====
You can use the `dig` command to verify name and reverse name resolution. See the section on _Validating DNS resolution for user-provisioned infrastructure_ for detailed validation steps.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-network-customizations-user-infra.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="installation-dns-user-infra-example_{context}"]
= Example DNS configuration for user-provisioned clusters

[role="_abstract"]
Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

[NOTE]
====
In a two-node cluster with fencing, the control plane machines are also schedulable worker nodes. The DNS configuration must therefore include only the two control plane nodes. If you later add compute machines, provide corresponding A and PTR records for them as in a standard user-provisioned installation.
====

The following example is a BIND zone file that shows sample DNS A records for name resolution in a user-provisioned cluster.

[NOTE]
====
In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.
====

[source,text]
----
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
	IN	MX 10	smtp.example.com.
;
;
ns1.example.com.		IN	A	192.168.1.5
smtp.example.com.		IN	A	192.168.1.5
;
helper.example.com.		IN	A	192.168.1.5
helper.ocp4.example.com.	IN	A	192.168.1.5
;
api.ocp4.example.com.		IN	A	192.168.1.5
api-int.ocp4.example.com.	IN	A	192.168.1.5
;
*.apps.ocp4.example.com.	IN	A	192.168.1.5
;
bootstrap.ocp4.example.com.	IN	A	192.168.1.96
;
control-plane0.ocp4.example.com.	IN	A	192.168.1.97
control-plane1.ocp4.example.com.	IN	A	192.168.1.98
;
control-plane2.ocp4.example.com.	IN	A	192.168.1.99
;
compute0.ocp4.example.com.	IN	A	192.168.1.11
compute1.ocp4.example.com.	IN	A	192.168.1.7
;
;EOF
----

where:

`api.ocp4.example.com.`:: Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer.
`api-int.ocp4.example.com.`:: Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications.
`*.apps.ocp4.example.com.`:: Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods.
`bootstrap.ocp4.example.com`:: Provides name resolution for the bootstrap machine.
`control-plane0.ocp4.example.com`:: Provides name resolution for the control plane machines.
`compute0.ocp4.example.com.`:: Provides name resolution for the compute machines.

The following example BIND zone file shows sample PTR records for reverse name resolution in a user-provisioned cluster:

[source,text]
----
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
;
5.1.168.192.in-addr.arpa.	IN	PTR	api.ocp4.example.com.
5.1.168.192.in-addr.arpa.	IN	PTR	api-int.ocp4.example.com.
;
96.1.168.192.in-addr.arpa.	IN	PTR	bootstrap.ocp4.example.com.
;
97.1.168.192.in-addr.arpa.	IN	PTR	control-plane0.ocp4.example.com.
98.1.168.192.in-addr.arpa.	IN	PTR	control-plane1.ocp4.example.com.
;
99.1.168.192.in-addr.arpa.	IN	PTR	control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	compute1.ocp4.example.com.
;
;EOF
----

where:

`api.ocp4.example.com.`:: Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer.
`api-int.ocp4.example.com.`:: Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications.
`bootstrap.ocp4.example.com.`:: Provides reverse DNS resolution for the bootstrap machine.
`control-plane0.ocp4.example.com.`:: Provides rebootstrap.ocp4.example.com.verse DNS resolution for the control plane machines.
`compute0.ocp4.example.com.`:: Provides reverse DNS resolution for the compute machines.

[NOTE]
====
A PTR record is not required for the OpenShift Container Platform application wildcard.
====

[role="_additional-resources"]
.Additional resources

* Validating DNS resolution for user-provisioned infrastructure

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc

[id="installation-bare-metal-dns-record-type_{context}"]
= Configuring the dnsRecordsType parameter

[role="_abstract"]
During cluster installation, you can specify the `dnsRecordsType` parameter in the `install-config.yaml` file to set if the internal DNS service or an external source provides the necessary records for `api`, `api-int`, and `ingress` DNS records.

The `dnsRecordsType` parameter supports the following values:

* `Internal`: The default value. Setting this value causes the cluster infrastructure to automatically create and maintain the necessary DNS records.
* `External`: You can use this value only if you set the `loadBalancer.type` parameter to `UserManaged`. The cluster does not manage the DNS records. You must manually configure DNS records on an external DNS server.

.Prerequisites

* You created DNS records, such as `api`, `api-int`, or `*.apps`.
* You configured a user-managed load balancer for your cluster.
* If you intend on setting `dnsRecordsType.External` in the `infrastructure.config.openshift.io` CR, you must initially configure cluster nodes to use the specific external server for DNS resolution.

.Procedure

* In the `install-config.yaml` file during cluster installation, specify `TechPreviewNoUpgrade` for the `featureSet` parameter and specify `External` for the `dnsRecordsType` parameter:
+
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
metadata:
  name: dev-cluster
# ...
platform:
  baremetal:
# ...
    loadBalancer:
      type: UserManaged
    dnsRecordsType: External
# ...
featureSet: TechPreviewNoUpgrade
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
sshKey: 'ssh-ed25519 AAAA...'
# ...
----
+
where:
+
`type.UserManaged`:: Specifies an external load balancer for your cluster.
`dnsRecordsType.External`:: Specifies that the cluster does not create internal DNS records for the core infrastructure.
`featureSet.TechPreviewNoUpgrade`:: Specifies the enablement of non-default features for your cluster.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc

[id="installation-load-balancing-user-infra_{context}"]
= Load balancing requirements for user-provisioned infrastructure

[role="_abstract"]
Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

Before you install OpenShift Container Platform, you can provision your own API and application ingress load balancing infrastructure to use in place of the default, internal load balancing solution. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

[NOTE]
====
If you want to deploy the API and application Ingress load balancers with a {op-system-base-full} instance, you must purchase the {op-system-base} subscription separately.
====

The load balancing infrastructure must meet the following requirements:

* API load balancer: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions:

** Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.
** A stateless load balancing algorithm. The options vary based on the load balancer implementation.

[IMPORTANT]
====
Do not configure session persistence for an API load balancer. Configuring session persistence for a Kubernetes API server might cause performance issues from excess application traffic for your OpenShift Container Platform cluster and the Kubernetes API that runs inside the cluster.
====

Configure the following ports on both the front and back of the API load balancers:

[cols="2,5,^2,^2,2",options="header"]
|===

|Port
|Back-end machines (pool members)
|Internal
|External
|Description

|`6443`
|Bootstrap and control plane. You remove the bootstrap machine from the load
balancer after the bootstrap machine initializes the cluster control plane. You
must configure the `/readyz` endpoint for the API server health check probe.
|X
|X
|Kubernetes API server

|`22623`
|Bootstrap and control plane. You remove the bootstrap machine from the load
balancer after the bootstrap machine initializes the cluster control plane.
|X
|
|Machine config server

|===

[NOTE]
====
The load balancer must be configured to take a maximum of 30 seconds from the
time the API server turns off the `/readyz` endpoint to the removal of the API
server instance from the pool. Within the time frame after `/readyz` returns an
error or becomes healthy, the endpoint must have been removed or added. Probing
every 5 or 10 seconds, with two successful requests to become healthy and three
to become unhealthy, are well-tested values.
====

* Application Ingress load balancer: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. Configure the following conditions:

** Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.
** A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform.

[TIP]
====
If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption.
====

Configure the following ports on both the front and back of the load balancers:

.Application Ingress load balancer
[cols="2,5,^2,^2,2",options="header"]
|===

|Port
|Back-end machines (pool members)
|Internal
|External
|Description

|`443`
|The machines that run the Ingress Controller pods, compute, or worker, by default.
|X
|X
|HTTPS traffic

|`80`
|The machines that run the Ingress Controller pods, compute, or worker, by default.
|X
|X
|HTTP traffic

|===

[NOTE]
====
If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc

[id="installation-load-balancing-user-infra-example_{context}"]
= Example load balancer configuration for user-provisioned clusters

[role="_abstract"]
Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters.

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

= Example load balancer configuration for clusters that are deployed with user-managed load balancers

This section provides an example API and application Ingress load balancer configuration that meets the load balancing requirements for clusters that are deployed with user-managed load balancers. The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

[TIP]
====
If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.
====

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

[NOTE]
====
If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`.
====

.Sample API and application Ingress load balancer configuration
[source,text]
----
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
----

where:

`listen api-server-6443`:: Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic.
`server bootstrap bootstrap.ocp4.example.com`:: The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete.
`listen machine-config-server`:: Port `22623` handles the machine config server traffic and points to the control plane machines.
`listen ingress-router-443`:: Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.
`listen ingress-router-80`:: Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.
+
[NOTE]
====
If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
====

// Creating a manifest object that includes a customized `br-ex` bridge
// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="creating-manifest-file-customized-br-ex-bridge_{context}"]
= Creating a manifest object that includes a customized br-ex bridge

[role="_abstract"]
By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on bare-metal nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, create a `MachineConfig` object that includes an NMState configuration file.

By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, use the Agent-based Installer to create a `MachineConfig` object that includes an NMState configuration file.

[IMPORTANT]
====
Customizations to the cluster made by additional manifests are not validated and not guaranteed to work. These manifests might result in a nonfunctional cluster.

For more information about an additional manifest file, see "Creating a directory to contain additional manifests".
====

Consider using the customized `br-ex` bridge configuration for any of the following tasks:

* You need to modify the `br-ex` bridge after you installed the cluster.
* You need to modify the maximum transmission unit (MTU) for your cluster.
* You need to update DNS values.
* You need to modify attributes for a different bond interface. Examples include MIImon (Media Independent Interface Monitor), bonding mode or Quality of Service (QoS).
* You need to enable Link Layer Discovery Protocol (LLDP) to discover and troubleshoot switch connectivity.

[NOTE]
====
Use the default OVS `br-ex` bridge for standard environments.

Use the default OVS `br-ex` bridge mechanism for single network interface controller (NIC) environments with default network settings.
====

After you install {op-system-first} and the system reboots, the Machine Config Operator injects Ignition configuration files into each node. This operation ensures that each node receives the `br-ex` bridge network configuration. To prevent configuration conflicts, the default OVS `br-ex` bridge mechanism is disabled.

[WARNING]
====
The following list of interface names are reserved and you cannot use the names with NMstate configurations:

* `br-ext`
* `br-int`
* `br-local`
* `br-nexthop`
* `br0`
* `ext-vxlan`
* `ext`
* `genev_sys_*`
* `int`
* `k8s-*`
* `ovn-k8s-*`
* `patch-br-*`
* `tun0`
* `vxlan_sys_*`
====

.Prerequisites
* Optional: You have installed the `nmstatectl` CLI tool to validate your NMState configuration.
* You checked that an `openshift` subdirectory exists in your installation directory. If the subdirectory does not exist, create the subdirectory.

.Procedure

. Create an NMState configuration file and define a customized `br-ex` bridge network configuration in the file:
+
.Example of an NMState configuration for a customized `br-ex` bridge network
[source,yaml]
----
interfaces:
- name: enp2s0
  type: ethernet
  state: up
  ipv4:
    enabled: false
  ipv6:
    enabled: false
- name: br-ex
  type: ovs-bridge
  state: up
  ipv4:
    enabled: false
    dhcp: false
  ipv6:
    enabled: false
    dhcp: false
  bridge:
    options:
      mcast-snooping-enable: true
    port:
    - name: enp2s0
    - name: br-ex
- name: br-ex
  type: ovs-interface
  state: up
  copy-mac-from: enp2s0
  ipv4:
    enabled: true
    dhcp: true
    auto-route-metric: 48
  ipv6:
    enabled: true
    dhcp: true
    auto-route-metric: 48
# ...
----
+
where:
+
`interfaces.name`:: Name of the interface.
`interfaces.type`:: The type of ethernet.
`interfaces.state`:: The requested state for the interface after creation.
`ipv4.enabled`:: Disables IPv4 and IPv6 in this example.
`port.name`:: The node NIC to which the bridge attaches.
`auto-route-metric`:: Set the parameter to `48` to ensure the `br-ex` default route always has the highest precedence (lowest metric). This configuration prevents routing conflicts with any other interfaces automatically configured by the `NetworkManager` service.

. Use the `cat` command to base64-encode the contents of the NMState configuration:
+
[source,terminal]
----
$ cat <nmstate_configuration>.yml | base64
----
+
where:
+
`<nmstate_configuration>`:: Replace `<nmstate_configuration>` with the name of your NMState resource YAML file.

. Create a `MachineConfig` manifest file and define a customized `br-ex` bridge network configuration analogous to the following example. The installation program automatically applies the updates from the `MachineConfig` object to your cluster.

. Create a `MachineConfig` file as an additional manifest file. Define a customized `br-ex` bridge network configuration analogous to the following example in the file. The Agent-based Installer automatically applies the updates from the `MachineConfig` object to your cluster.
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 10-br-ex-worker
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/worker-0.yml
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/worker-1.yml
# ...
----
+
where:
+
`metadata.name`:: Specifies the name of the policy.
`contents.source`:: Writes the encoded base64 information to the specified path.
`path`:: For each node in your cluster, specify the hostname path to your node and the base-64 encoded Ignition configuration file data for the machine type. The `worker` role is the default role for nodes in your cluster. Use the `.yml` extension for configuration files. For example, use `$(hostname -s).yml` when specifying the short hostname path for each node or all nodes in the `MachineConfig` manifest file.
+
You can apply a single global configuration to all nodes by using the `/etc/nmstate/openshift/cluster.yml` configuration file. In this case, you do not need to specify individual hostname paths for each node, such as `/etc/nmstate/openshift/<node_hostname>.yml`.
+
.Example /etc/nmstate/openshift/cluster.yml configuration file
[source,yaml]
----
# ...
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/cluster.yml
# ...
----

. Save the additional manifest file in the `openshift` subdirectory of your installation directory.
+
On completing other configuration inputs for your installation, such as encrypting the disk, you create the ISO image. After booting this image, the customized `br-ex` bridge configuration applies to each node in your cluster.

.Next steps

* Scaling compute nodes to apply the manifest object that includes a customized `br-ex` bridge to each compute node that exists in your cluster. For more information, see "Expanding the cluster" in the _Additional resources_ section.

[role="_additional-resources"]
.Additional resources

* Converting to a dual-stack cluster network

* Expanding the cluster

// Scale each machine set to compute nodes
// Module included in the following assemblies:
//
// IPI
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc
// UPI
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc

[id="creating-scaling-machine-sets-compute-nodes-networking_{context}"]
= Scaling each machine set to compute nodes

[role="_abstract"]
To scale each machine set to compute nodes, you must apply a customized `br-ex` bridge configuration to all compute nodes in your OpenShift Container Platform cluster. You must then edit your `MachineConfig` custom resource (CR) and modify its roles.

Additionally, you must create a `BareMetalHost` CR that defines information for your bare-metal machine, such as hostname, credentials, and your other required parameters. After you configure these resources, you must scale machine sets, so that the machine sets can apply the resource configuration to each compute node and reboot the nodes.

.Prerequisites

* You created a `MachineConfig` manifest object that includes a customized `br-ex` bridge configuration.

.Procedure

. Edit the `MachineConfig` CR by entering the following command:
+
[source,terminal]
----
$ oc edit mc <machineconfig_custom_resource_name>
----

. Add each compute node configuration to the CR, so that the CR can manage roles for each defined compute node in your cluster.

. Create a `Secret` object named `extraworker-secret` that has a minimal static IP configuration.

. Apply the `extraworker-secret` secret to each node in your cluster by entering the following command. This step provides each compute node access to the Ignition config file.
+
[source,terminal]
----
$ oc apply -f ./extraworker-secret.yaml
----

. Create a `BareMetalHost` resource and specify the network secret in the `preprovisioningNetworkDataName` parameter:
+
.Example `BareMetalHost` resource with an attached network secret
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
spec:
# ...
  preprovisioningNetworkDataName: ostest-extraworker-0-network-config-secret
# ...
----

. To manage the `BareMetalHost` object within the `openshift-machine-api` namespace of your cluster, change to the namespace by entering the following command:
+
[source,terminal]
----
$ oc project openshift-machine-api
----

. Get the machine sets:
+
[source,terminal]
----
$ oc get machinesets
----

. Scale each machine set by entering the following command. You must run this command for each machine set.
+
[source,terminal]
----
$ oc scale machineset <machineset_name> --replicas=<n>
----
* <n>: Where `<machineset_name>` is the name of the machine set and `<n>` is the number of compute nodes.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc

[id="installation-infrastructure-user-infra_{context}"]
= Preparing the user-provisioned infrastructure

[role="_abstract"]
Before you install OpenShift Container Platform on user-provisioned infrastructure, you must prepare the underlying infrastructure.

This section provides details about the high-level steps required to set up your cluster infrastructure in preparation for an OpenShift Container Platform installation. This includes configuring IP networking and network connectivity for your cluster nodes,
preparing a web server for the Ignition files,
enabling the required ports through your firewall, and setting up the required DNS and load balancing infrastructure.

After preparation, your cluster infrastructure must meet the requirements outlined in the _Requirements for a cluster with user-provisioned infrastructure_ section.

.Prerequisites

* You have reviewed the OpenShift Container Platform 4.x Tested Integrations page.
* You have reviewed the infrastructure requirements detailed in the _Requirements for a cluster with user-provisioned infrastructure_ section.

.Procedure

. Set up static IP addresses.

. Set up an HTTP or HTTPS server to provide Ignition files to the cluster nodes.

. If you are using DHCP to provide the IP networking configuration to your cluster nodes, configure your DHCP service.
+
.. Add persistent IP addresses for the nodes to your DHCP server configuration. In your configuration, match the MAC address of the relevant network interface to the intended IP address for each node.
+
.. When you use DHCP to configure IP addressing for the cluster machines, the machines also obtain the DNS server information through DHCP. Define the persistent DNS server address that is used by the cluster nodes through your DHCP server configuration.
+
[NOTE]
====
If you are not using a DHCP service, you must provide the IP networking configuration and the address of the DNS server to the nodes at {op-system} install time. These can be passed as boot arguments if you are installing from an ISO image. See the _Installing {op-system} and starting the OpenShift Container Platform bootstrap process_ section for more information about static IP provisioning and advanced networking options.
====
+
.. Define the hostnames of your cluster nodes in your DHCP server configuration. See the _Setting the cluster node hostnames through DHCP_ section for details about hostname considerations.
+
[NOTE]
====
If you are not using a DHCP service, the cluster nodes obtain their hostname through a reverse DNS lookup.
====
. Choose to perform either a fast track installation of {op-system-first} or a full installation of {op-system-first}. For the full installation, you must set up an HTTP or HTTPS server to provide Ignition files and install images to the cluster nodes. For the fast track installation an HTTP or HTTPS server is not required, however, a DHCP server is required. See sections “Fast-track installation: Creating {op-system-first} machines" and “Full installation: Creating {op-system-first} machines".

. Ensure that your network infrastructure provides the required network connectivity between the cluster components. See the _Networking requirements for user-provisioned infrastructure_ section for details about the requirements.

. Configure your firewall to enable the ports required for the OpenShift Container Platform cluster components to communicate. See _Networking requirements for user-provisioned infrastructure_ section for details about the ports that are required.
+
[IMPORTANT]
====
By default, port `1936` is accessible for an OpenShift Container Platform cluster, because each control plane node needs access to this port.

For ingress health check probes, the `/healthz/ready` endpoint is available on this port.

Avoid using the Ingress load balancer to expose this port, because doing so might result in the exposure of sensitive information, such as statistics and metrics, related to Ingress Controllers.
====

. Setup the required DNS infrastructure for your cluster.
+
.. Configure DNS name resolution for the Kubernetes API, the application wildcard, the bootstrap machine, the control plane machines, and the compute machines.
+
.. Configure reverse DNS resolution for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.
+
See the _User-provisioned DNS requirements_ section for more information about the OpenShift Container Platform DNS requirements.

. Validate your DNS configuration.
+
.. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses in the responses correspond to the correct components.
+
.. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names in the responses correspond to the correct components.
+
See the _Validating DNS resolution for user-provisioned infrastructure_ section for detailed DNS validation steps.

. Provision the required API and application ingress load balancing infrastructure. See the _Load balancing requirements for user-provisioned infrastructure_ section for more information about the requirements.
+
[NOTE]
====
Some load balancing solutions require the DNS name resolution for the cluster nodes to be in place before the load balancing is initialized.
====

[role="_additional-resources"]
.Additional resources

* Requirements for a cluster with user-provisioned infrastructure
* Installing {op-system} and starting the OpenShift Container Platform bootstrap process
* Setting the cluster node hostnames through DHCP
* Advanced RHCOS installation configuration
* Networking requirements for user-provisioned infrastructure
* User-provisioned DNS requirements
* Validating DNS resolution for user-provisioned infrastructure
* Load balancing requirements for user-provisioned infrastructure

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-network-customizations-user-infra.adoc
// * installing/installing_vmc/installing-vmc-user-infra.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc

[id="installation-user-provisioned-validating-dns_{context}"]
= Validating DNS resolution for user-provisioned infrastructure

[role="_abstract"]
To prevent network-related installation failures and ensure node connectivity in OpenShift Container Platform, validate your DNS configuration before deploying on user-provisioned infrastructure.

[IMPORTANT]
====
The validation steps detailed in this section must succeed before you install your cluster.
====

.Prerequisites

* You have configured the required DNS records for your user-provisioned infrastructure.

.Procedure

. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses contained in the responses correspond to the correct components.
+
.. Perform a lookup against the Kubernetes API record name. Check that the result points to the IP address of the API load balancer:
+
[source,terminal]
----
$ dig +noall +answer @<nameserver_ip> api.<cluster_name>.<base_domain>
----
Replace `<nameserver_ip>` with the IP address of the name server, `<cluster_name>` with your cluster name, and `<base_domain>` with your base domain name.
+
.Example output
[source,terminal]
----
api.ocp4.example.com.		604800	IN	A	192.168.1.5
----
+
.. Perform a lookup against the Kubernetes internal API record name. Check that the result points to the IP address of the API load balancer:
+
[source,terminal]
----
$ dig +noall +answer @<nameserver_ip> api-int.<cluster_name>.<base_domain>
----
+
.Example output
[source,terminal]
----
api-int.ocp4.example.com.		604800	IN	A	192.168.1.5
----
+
.. Test an example `*.apps.<cluster_name>.<base_domain>` DNS wildcard lookup. All of the application wildcard lookups must resolve to the IP address of the application ingress load balancer:
+
[source,terminal]
----
$ dig +noall +answer @<nameserver_ip> random.apps.<cluster_name>.<base_domain>
----
+
.Example output
[source,terminal]
----
random.apps.ocp4.example.com.		604800	IN	A	192.168.1.5
----
+
[NOTE]
====
In the example outputs, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.
====
+
You can replace `random` with another wildcard value. For example, you can query the route to the OpenShift Container Platform console:
+
[source,terminal]
----
$ dig +noall +answer @<nameserver_ip> console-openshift-console.apps.<cluster_name>.<base_domain>
----
+
.Example output
[source,terminal]
----
console-openshift-console.apps.ocp4.example.com. 604800 IN	A 192.168.1.5
----
+
.. Run a lookup against the bootstrap DNS record name. Check that the result points to the IP address of the bootstrap node:
+
[source,terminal]
----
$ dig +noall +answer @<nameserver_ip> bootstrap.<cluster_name>.<base_domain>
----
+
.Example output
[source,terminal]
----
bootstrap.ocp4.example.com.		604800	IN	A	192.168.1.96
----
+
.. Use this method to perform lookups against the DNS record names for the control plane and compute nodes. Check that the results correspond to the IP addresses of each node.

. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names contained in the responses correspond to the correct components.
+
.. Perform a reverse lookup against the IP address of the API load balancer. Check that the response includes the record names for the Kubernetes API and the Kubernetes internal API:
+
[source,terminal]
----
$ dig +noall +answer @<nameserver_ip> -x 192.168.1.5
----
+
.Example output
[source,terminal]
----
5.1.168.192.in-addr.arpa. 604800	IN	PTR	api-int.ocp4.example.com.
5.1.168.192.in-addr.arpa. 604800	IN	PTR	api.ocp4.example.com.
----
+
where:
+
`api-int.ocp4.example.com`:: Specifies the record name for the Kubernetes internal API.
`api.ocp4.example.com`:: Specifies the record name for the Kubernetes API.
+
[NOTE]
====
A PTR record is not required for the OpenShift Container Platform application wildcard. No validation step is needed for reverse DNS resolution against the IP address of the application ingress load balancer.
====
+
.. Perform a reverse lookup against the IP address of the bootstrap node. Check that the result points to the DNS record name of the bootstrap node:
+
[source,terminal]
----
$ dig +noall +answer @<nameserver_ip> -x 192.168.1.96
----
+
.Example output
[source,terminal]
----
96.1.168.192.in-addr.arpa. 604800	IN	PTR	bootstrap.ocp4.example.com.
----
+
.. Use this method to perform reverse lookups against the IP addresses for the control plane and compute nodes. Check that the results correspond to the DNS record names of each node.

[role="_additional-resources"]
.Additional resources

* User-provisioned DNS requirements
* Load balancing requirements for user-provisioned infrastructure

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-network-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc

[id="ssh-agent-using_{context}"]
= Generating a key pair for cluster node SSH access

[role="_abstract"]
During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to the {op-system-first} nodes through their Ignition config files and is used to authenticate SSH access to the nodes. The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication.

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the {op-system} nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user.

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes.

[IMPORTANT]
====
Do not skip this procedure in production environments, where disaster recovery and debugging is required.
====

[NOTE]
====
You must use a local key, not one that you configured with platform-specific approaches.
====

[NOTE]
====
On clusters running {op-system-first}, the SSH keys specified in the Ignition config files are written to the `/home/core/.ssh/authorized_keys.d/core` file. However, the Machine Config Operator manages SSH keys in the `/home/core/.ssh/authorized_keys` file and configures *sshd* to ignore the `/home/core/.ssh/authorized_keys.d/core` file.
As a result, newly provisioned OpenShift Container Platform nodes are not accessible using SSH until the Machine Config Operator reconciles the machine configs with the `authorized_keys` file. After you can access the nodes using SSH, you can delete the `/home/core/.ssh/authorized_keys.d/core` file.
====

.Procedure

. If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
----
Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory.
+
[NOTE]
====
If you plan to install an OpenShift Container Platform cluster that uses the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm.
====

. View the public SSH key:
+
[source,terminal]
----
$ cat <path>/<file_name>.pub
----
+
For example, run the following to view the `~/.ssh/id_ed25519.pub` public key:
+
[source,terminal]
----
$ cat ~/.ssh/id_ed25519.pub
----

. Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command.
+
[NOTE]
====
On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically.
====
+
.. If the `ssh-agent` process is not already running for your local user, start it as a background task:
+
[source,terminal]
----
$ eval "$(ssh-agent -s)"
----
+
.Example output
[source,terminal]
----
Agent pid 31874
----
+
[NOTE]
====
If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA.
====

. Add your SSH private key to the `ssh-agent`:
+
[source,terminal]
----
$ ssh-add <path>/<file_name>
----
Specifies the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`
+
.Example output
[source,terminal]
----
Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
----

.Next steps

* When you install OpenShift Container Platform, provide the SSH public key to the installation program.
If you install a cluster on infrastructure that you provision, you must provide the key to the installation program.

[role="_additional-resources"]
.Additional resources

* Verifying node health

//You extract the installation program from the mirrored content.

//You can install the CLI on the mirror host.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc

[id="installation-initializing-manual_{context}"]
= Manually creating the installation configuration file

[role="_abstract"]
Installing the cluster requires that you manually create the installation configuration file.

[IMPORTANT]
====
The Cloud Controller Manager Operator performs a connectivity check on a provided hostname or IP address. Ensure that you specify a hostname or an IP address to a reachable vCenter server. If you provide metadata to a non-existent vCenter server, installation of the cluster fails at the bootstrap stage.
====

.Prerequisites

* You have uploaded a custom RHCOS AMI.
* You have an SSH public key on your local machine for use with the installation program. You can use the key for SSH authentication onto your cluster nodes for debugging and disaster recovery.
* You have obtained the OpenShift Container Platform installation program and the pull secret for your
cluster.
* Obtain the `imageContentSources` section from the output of the command to
mirror the repository.
* Obtain the contents of the certificate for your mirror registry.
* You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry.
* You have obtained the contents of the certificate for your mirror registry.

.Procedure

. Create an installation directory to store your required installation assets in:
+
[source,terminal]
----
$ mkdir <installation_directory>
----
+
[IMPORTANT]
====
You must create a directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
====

. Edit the `install-config.yaml` file to set the `publish: Internal` parameter.
. Edit the `install-config.yaml` file to set the parameters necessary for installation into an existing VPC.
.. Define the network and subnets for the VPC to install the cluster in under the parent `platform.gcp` field:
+
[source,yaml]
----
platform:
  gcp:
    network: <existing_vpc>
    controlPlaneSubnet: <control_plane_subnet>
    computeSubnet: <compute_subnet>
----
+
For the `platform.gcp.network` parameter, specify the name for the existing Google VPC. For the `platform.gcp.controlPlaneSubnet` and `platform.gcp.computeSubnet` parameters, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
. Edit the `install-config.yaml` file to set the parameters necessary for installation into a shared VPC.
.. Define the network, subnets, and project names for the shared VPC:
+
[source,yaml]
----
# ...
platform:
  gcp:
    computeSubnet: <shared_vpc_compute_subnet>
    controlPlaneSubnet: <shared_vpc_control_plane_subnet>
    network: <shared_vpc_name>
    networkProjectID: <host_project_name>
    projectID: <service_project_name>
----
where:

`<shared_vpc_compute_subnet>`:: Specifies the name of the subnet in the shared VPC for compute machines to use.
`<shared_vpc_control_plane_subnet>`:: Specifies the name of the subnet in the shared VPC for control plane machines to use.
`<shared_vpc_name>`:: Specifies the name of the shared VPC.
`<host_project_name>`:: Specifies the name of the host project where the shared VPC exists.
`<service_project_name>`:: Specifies the name of the project where you want to install the cluster.

. Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.
.. Edit the `install-config.yaml` file to set the `publish: Internal` parameter.
.. If you use your own outbound routing to connect to the internet, set the `outboundType: UserDefinedRouting` parameter.
.. Edit the `install-config.yaml` file so that the value of the `platform.azure.cloudName` parameter is `AzureUSGovernmentCloud`.
+
[NOTE]
====
You must name this configuration file `install-config.yaml`.
====
+
When customizing the sample template, be sure to provide the information that is required for an installation in a restricted network:
+
.. Update the `pullSecret` value to contain the authentication information for your registry:
+
[source,yaml]
----
pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
----
+
For `<mirror_host_name>`, specify the registry domain name that you specified in the certificate for your mirror registry, and for `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
+
.. Add the `additionalTrustBundle` parameter and value.
+
[source,yaml]
----
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
----
+
The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry.
+
.. Define the network and subnets for the VPC to install the cluster in under the parent `platform.ibmcloud` field:
+
[source,yaml]
----
vpcName: <existing_vpc>
controlPlaneSubnets: <control_plane_subnet>
computeSubnets: <compute_subnet>
----
+
For `platform.ibmcloud.vpcName`, specify the name for the existing {ibm-cloud-title} Virtual Private Cloud (VPC) network. For `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
+
.. Add the image content resources, which resemble the following YAML excerpt:
+
[source,yaml]
----
imageContentSources:
- mirrors:
  - <mirror_host_name>:5000/<repo_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <mirror_host_name>:5000/<repo_name>/release
  source: registry.redhat.io/ocp/release
----
+
For these values, use the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.
+
.. If network restrictions limit the use of public endpoints to access the required {ibm-cloud-name} services, add the `serviceEndpoints` stanza to `platform.ibmcloud` to specify an alternate service endpoint.
+
[NOTE]
====
You can specify only one alternate service endpoint for each service.
====
+
.Example of using alternate services endpoints
[source,yaml]
----
# ...
serviceEndpoints:
  - name: IAM
    url: <iam_alternate_endpoint_url>
  - name: VPC
    url: <vpc_alternate_endpoint_url>
  - name: ResourceController
    url: <resource_controller_alternate_endpoint_url>
  - name: ResourceManager
    url: <resource_manager_alternate_endpoint_url>
  - name: DNSServices
    url: <dns_services_alternate_endpoint_url>
  - name: COS
    url: <cos_alternate_endpoint_url>
  - name: GlobalSearch
    url: <global_search_alternate_endpoint_url>
  - name: GlobalTagging
    url: <global_tagging_alternate_endpoint_url>
# ...
----
+
.. Optional: Set the publishing strategy to `Internal`:
+
[source,yaml]
----
publish: Internal
----
+
By setting this option, you create an internal Ingress Controller and a private load balancer.
+
[NOTE]
====
If you use the default value of `External`, your network must be able to access the public endpoint for {ibm-cloud-name} Internet Services (CIS). CIS is not enabled for Virtual Private Endpoints.
====
+
[NOTE]
====
You must name this configuration file `install-config.yaml`.
====

+
** Unless you use a registry that {op-system} trusts by default, such as `docker.io`, you must provide the contents of the certificate for your mirror repository in the `additionalTrustBundle` section. In most cases, you must provide the certificate for your mirror.
** You must include the `imageContentSources` section from the output of the command to
mirror the repository.
+
[IMPORTANT]
====
** The `ImageContentSourcePolicy` file is generated as an output of `oc mirror` after the mirroring process is finished.
** The `oc mirror` command generates an `ImageContentSourcePolicy` file which contains the YAML needed to define `ImageContentSourcePolicy`.
Copy the text from this file and paste it into your `install-config.yaml` file.
** You must run the 'oc mirror' command twice. The first time you run the `oc mirror` command, you get a full `ImageContentSourcePolicy` file. The second time you run the `oc mirror` command, you only get the difference between the first and second run.
Because of this behavior, you must always keep a backup of these files in case you need to merge them into one complete `ImageContentSourcePolicy` file. Keeping a backup of these two output files ensures that you have a complete `ImageContentSourcePolicy` file.
====

+
Make the following modifications for Azure Stack Hub:
+
.. Set the `replicas` parameter to `0` for the `compute` pool:
+
[source,yaml]
----
compute:
- hyperthreading: Enabled
  name: worker
  platform: {}
  replicas: 0
----
* `replicas`: Set to `0`.
+
The compute machines will be provisioned manually later.
+
.. Update the `platform.azure` section of the `install-config.yaml` file to configure your Azure Stack Hub configuration:
+
[source,yaml]
----
platform:
  azure:
    armEndpoint: <azurestack_arm_endpoint>
    baseDomainResourceGroupName: <resource_group>
    cloudName: AzureStackCloud
    region: <azurestack_region>
----
+
where:
+
`<azurestack_arm_endpoint>`:: Specifies the Azure Resource Manager endpoint of your Azure Stack Hub environment, like `\https://management.local.azurestack.external`.
`<resource_group>`:: Specifies the name of the resource group that contains the DNS zone for your base domain.
`cloudName`:: Specifies the Azure Stack Hub environment, which is used to configure the Azure SDK with the appropriate Azure API endpoints.
`region`:: Specifies the name of your Azure Stack Hub region.

+
Make the following modifications:
+
.. Specify the required installation parameters.
+
.. Update the `platform.azure` section to specify the parameters that are specific to Azure Stack Hub.
+
.. Optional: Update one or more of the default configuration parameters to customize the installation.
+
For more information about the parameters, see "Installation configuration parameters".

. If you are installing a three-node cluster or a cluster with user-provisioned infrastructure, set the `compute.replicas` parameter to `0`. In a three-node cluster, this ensures that the cluster's control planes are schedulable. For more information, see "Installing a three-node cluster". In a cluster with user-provisioned infrastructure, you must manually deploy compute machines before you finish installing OpenShift Container Platform.

. Back up the `install-config.yaml` file so that you can use it to install many clusters.
+
[IMPORTANT]
====
Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.
====

[role="_additional-resources"]
.Additional resources
* Installation configuration parameters for bare metal

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc

[id="installation-bare-metal-config-yaml_{context}"]
= Sample install-config.yaml file for bare metal
= Sample install-config.yaml file for {ibm-z-title}
= Sample install-config.yaml file for {ibm-power-title}
= Sample install-config.yaml file for other platforms

[role="_abstract"]
You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster platform or modify the values of the required parameters.

[source,yaml,subs="attributes+"]
----
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  replicas: 0
  architecture: s390x
  architecture: ppc64le
controlPlane:
  hyperthreading: Enabled
  name: master
  replicas: 3
  architecture: s390x
  architecture: ppc64le
metadata:
  name: test
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: 192.168.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
fips: false
pullSecret: '{"auths": ...}'
pullSecret: '{"auths": ...}'
sshKey: 'ssh-ed25519 AAAA...'
sshKey: 'ssh-ed25519 AAAA...'
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
sshKey: 'ssh-ed25519 AAAA...'
sshKey: 'ssh-ed25519 AAAA...'
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----

where:

`baseDomain`:: Specifies the base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.
`compute`:: Specifies the `compute` node configurations, which is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`.
`controlPlane`:: Specifies the `controlPlane` node configurations, which is a single mapping. To meet the requirements of the different data structures, the first line of the `controlPlane` section must not. Only one control plane pool is used.
`hyperthreading`:: Specifies whether to enable or disable simultaneous multithreading (SMT), or hyperthreading. By default, SMT is enabled to increase the performance of the cores in your machines. You can disable it by setting the parameter value to `Disabled`. If you disable SMT, you must disable it in all cluster machines; this includes both control plane and compute machines.
`hyperthreading`:: Specifies simultaneous multithreading (SMT), which you configure as a post-installation task.

[NOTE]
====
Simultaneous multithreading (SMT) is enabled by default. If SMT is not enabled in your BIOS settings, the `hyperthreading` parameter has no effect.
====

[IMPORTANT]
====
If you disable `hyperthreading`, whether in the BIOS or in the `install-config.yaml` file, ensure that your capacity planning accounts for the dramatically decreased machine performance.
====

[NOTE]
====
Simultaneous multithreading (SMT) is enabled by default. If SMT is not available on your OpenShift Container Platform nodes, the `hyperthreading` parameter has no effect.
====

[IMPORTANT]
====
If you disable `hyperthreading`, whether on your OpenShift Container Platform nodes or in the `install-config.yaml` file, ensure that your capacity planning accounts for the dramatically decreased machine performance.
====

`compute.replicas`:: Specifies the number of compute machines that the cluster creates and manages for you on installer-provisioned installations. You must set this value to `0` when you install OpenShift Container Platform on user-provisioned infrastructure. Additionally for user-provisioned installations, you must manually deploy the compute machines before you finish installing the cluster.

[NOTE]
====
If you are installing a three-node cluster, do not deploy any compute machines when you install the {op-system-first} machines.
====

`controlPlane.replicas`:: Specifies the number of control plane machines that you add to the cluster. Because the cluster uses these values as the number of etcd endpoints in the cluster, the value must match the number of control plane machines that you deploy.
`metadata.name`:: Specifies the cluster name that you specified in your DNS records.
`networking.clusterNetwork.cidr`:: Specifies a block of IP addresses from which pod IP addresses are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the pod network. If you need to access the pods from an external network, you must configure load balancers and routers to manage the traffic.

[NOTE]
====
Class E CIDR range is reserved for a future use. To use the Class E CIDR range, you must ensure your networking environment accepts the IP addresses within the Class E CIDR range.
====

`networking.cidr.hostPrefix`:: Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.
`networking.networkType`:: Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.
`networking.serviceNetwork`:: Specifies the IP address pool to use for service IP addresses. You can enter only one IP address pool. This block must not overlap with existing physical networks. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.
`platform`:: Specifies the platform. You must set the platform to `none`. You cannot provide additional platform configuration variables for

[IMPORTANT]
====
Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.
====
`fips`:: Specifies either enabling or disabling FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.

--
--

`pullSecret`:: Specifies the {cluster-manager-url-pull}. This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.
`pullSecret`:: Specifies the {cluster-manager-url-pull}. This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.
`pullSecret`:: Specifies the registry domain name for `<local_registry>`, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:5000`. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
`pullSecret`:: Specifies the registry domain name for `<local_registry>`, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:5000`. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
`sshKey`:: Specifies the SSH public key for the `core` user in {op-system-first}.
`sshKey`:: Specifies the SSH public key for the `core` user in {op-system-first}.

[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====

`additionalTrustBundle`:: Specifies the contents of the certificate file that you used for your mirror registry.
`additionalTrustBundle`:: Specifies the contents of the certificate file that you used for your mirror registry.
`additionalTrustBundle`:: Specifies the `additionalTrustBundle` parameter and value. The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry.
`imageContentSources`:: Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository.

[IMPORTANT]
====
* When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
* When using `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
* `ImageContentSourcePolicy` is deprecated. For more information see _Configuring image registry repository mirroring_.
====
`imageContentSources`:: Specifies the `imageContentSources` section from the output of the command to mirror the repository.

[role="_additional-resources"]
.Additional resources

* See Load balancing requirements for user-provisioned infrastructure for more information on the API and application ingress load balancing requirements.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing_aws-customizations.adoc
// * installing/installing_aws/installing_aws-private.adoc
// * installing/installing_aws/installing_aws-vpc.adoc
// * installing/installing_aws/installing_aws-china.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/
//installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * networking/configuring-a-custom-pki.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-configure-proxy_{context}"]
= Configuring the cluster-wide proxy during installation

[role="_abstract"]
Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform
cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

[NOTE]
====
For bare-metal installations, if you do not assign node IP addresses from the range that is specified in the `networking.machineNetwork[].cidr` field in the `install-config.yaml` file, you must include them in the `proxy.noProxy` field.
====

.Prerequisites
* You have an existing `install-config.yaml` file.

* You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, all cluster egress traffic is proxied, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object's `spec.noProxy` field to bypass the proxy if necessary.
+
[NOTE]
====
The `Proxy` object `status.noProxy` field is populated with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.

For installations on Amazon Web Services (AWS), {gcp-first}, Microsoft Azure, and {rh-openstack-first}, the `Proxy` object `status.noProxy` field is also populated with the instance metadata endpoint (`169.254.169.254`).
====

.Procedure

. Edit your `install-config.yaml` file and add the proxy settings. For example:
+
[source,yaml]
----
apiVersion: v1
baseDomain: my.domain.com
proxy:
  httpProxy: http://<username>:<pswd>@<ip>:<port>
  httpsProxy: https://<username>:<pswd>@<ip>:<port>
  noProxy: example.com
  noProxy: ec2.<aws_region>.amazonaws.com,elasticloadbalancing.<aws_region>.amazonaws.com,s3.<aws_region>.amazonaws.com
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
# ...
----
+
where:
+
`proxy.httpProxy`:: Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.
`proxy.httpsProxy`:: Specifies a proxy URL to use for creating HTTPS connections outside the cluster.
`proxy.noProxy`:: Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.
If you have added the Amazon `EC2`, `Elastic Load Balancing`, and `S3` VPC endpoints to your VPC, you must add these endpoints to the `noProxy` field.
You must include vCenter's IP address and the IP range that you use for its machines.
`additionalTrustBundle`:: If provided, the installation program generates a config map that is named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you provide `additionalTrustBundle` and at least one proxy setting, the `Proxy` object is configured to reference the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the {op-system} trust bundle. The `additionalTrustBundle` field is required unless the proxy's identity certificate is signed by an authority from the {op-system} trust bundle.
`additionalTrustBundlePolicy`:: Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when `http/https` proxy is configured. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.
+
[NOTE]
====
The installation program does not support the proxy `readinessEndpoints` field.
====
+
[NOTE]
====
If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:

[source,terminal]
----
$ ./openshift-install wait-for install-complete --log-level debug
----
====

. Save the file and reference it when installing OpenShift Container Platform.
+
The installation program creates a cluster-wide proxy that is named `cluster` that uses the proxy settings in the provided `install-config.yaml` file. If no proxy settings are provided, a `cluster` `Proxy` object is still created, but it will have a nil `spec`.
+
[NOTE]
====
Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc [Eventually]
// * installing/installing_azure/installing-azure-user-infra.adoc [Eventually]
// * installing/installing_gcp/installing-gcp-user-infra.adoc [Eventually]
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc [Eventually]
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc [Eventually]
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc [Eventually]
// * installing/installing_vsphere/installing-vsphere.adoc [Eventually]
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-three-node-cluster_{context}"]
= Configuring a three-node cluster

[role="_abstract"]
To create smaller, resource-efficient clusters for testing and production, deploy a bare-metal cluster with zero compute machines. This optional configuration uses only three control plane machines, optimizing infrastructure resources for administrators and developers.
To create smaller, resource-efficient clusters for testing and production, deploy a bare-metal cluster with zero compute machines in a minimal three-node cluster. This optional configuration uses only three control plane machines, optimizing infrastructure resources for testing, development, and production purposes.

In three-node OpenShift Container Platform environments, the three control plane machines are schedulable, which means that your application workloads are scheduled to run on them.

.Prerequisites

* You have an existing `install-config.yaml` file.

.Procedure

* Ensure that the number of compute replicas is set to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:
+
[source,yaml]
----
compute:
- name: worker
  platform: {}
  replicas: 0
# ...
----
+
[NOTE]
====
You must set the value of the `replicas` parameter for the compute machines to `0` when you install OpenShift Container Platform on user-provisioned infrastructure, regardless of the number of compute machines you are deploying. In installer-provisioned installations, the parameter controls the number of compute machines that the cluster creates and manages for you. This does not apply to user-provisioned installations, where the compute machines are deployed manually.
====
+
[NOTE]
====
The preferred resource for control plane nodes is six vCPUs and 21 GB. For three control plane nodes this is the memory + vCPU equivalent of a minimum five-node cluster. You should back the three nodes, each installed on a 120 GB disk, with three IFLs that are SMT2 enabled. The minimum tested setup is three vCPUs and 10 GB on a 120 GB disk for each control plane node.
====
.Next steps

For three-node cluster installations, follow these next steps:

* If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the _Load balancing requirements for user-provisioned infrastructure_ section for more information.

* When you create the Kubernetes manifest files in the following procedure, ensure that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file is set to `true`. This enables your application workloads to run on the control plane nodes.

* Do not deploy any compute nodes when you create the {op-system-first} machines.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-user-infra-generate-k8s-manifest-ignition_{context}"]
= Creating the Kubernetes manifest and Ignition config files

[role="_abstract"]
To customize cluster definitions and manually start machines, generate the Kubernetes manifest and Ignition config files.

The installation configuration file transforms into the Kubernetes manifests. The manifests wrap into the Ignition configuration files, which are later used to configure the cluster machines.

[IMPORTANT]
====
* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

[NOTE]
====
The installation program that generates the manifest and Ignition files is architecture specific and can be obtained from the
client image mirror. The Linux version of the installation program runs on s390x only. This installer program is also available as a macOS version.
====
[NOTE]
====
The installation program that generates the manifest and Ignition files is architecture specific and can be obtained from the
client image mirror. The Linux version of the installation program (without an architecture postfix) runs on ppc64le only. This installer program is also available as a macOS version.
====

.Prerequisites

* You obtained the OpenShift Container Platform installation program.
For a restricted network installation, these files are on your mirror host.
* You created the `install-config.yaml` installation configuration file.

.Procedure

. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
+
where
+
`<installation_directory>`:: Specifies the installation directory that contains the `install-config.yaml` file you created.

. Remove the Kubernetes manifest files that define the control plane machines:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
----
+
By removing these files, you prevent the cluster from automatically generating control plane machines.

. Remove the Kubernetes manifest files that define the control plane machine set:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
----

. Optional: If you do not want the cluster to provision compute machines, remove
the Kubernetes manifest files that define the worker machines:
. Remove the Kubernetes manifest files that define the worker machines:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
----
+
[IMPORTANT]
====
If you disabled the `MachineAPI` capability when installing a cluster on user-provisioned infrastructure, you must remove the Kubernetes manifest files that define the worker machines. Otherwise, your cluster fails to install.
====
+
Because you create and manage the worker machines yourself, you do not need to initialize these machines.

. Remove the Kubernetes manifest files that define the control plane machines, compute machine sets, and control plane machine sets:
+
[source,terminal]
----
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
----
+
Because you create and manage these resources yourself, you do not have to initialize them. You can preserve the compute machine set files to create compute machines by using the machine API, but you must update references to them to match your environment.
+
[WARNING]
====
If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.
====
+
[IMPORTANT]
====
When you configure control plane nodes from the default unschedulable to schedulable, additional subscriptions are required. This is because control plane nodes then become compute nodes.
====

. Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:
+
.. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
+
.. Locate the `mastersSchedulable` parameter and ensure that it is set to `false`.
+
.. Save and exit the file.

. Optional: If you do not want
the Ingress Operator
to create DNS records on your behalf, remove the `privateZone` and `publicZone`
sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:
. Remove the `privateZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: DNS
metadata:
  creationTimestamp: null
  name: cluster
spec:
  baseDomain: example.openshift.com
  privateZone:
    id: mycluster-100419-private-zone
  publicZone: <1>
    id: example.openshift.com
status: {}
----
`spec.privateZone`: Remove this section completely.
+
If you do so, you must add ingress DNS records manually in a later step.

. Configure the cloud provider for your VPC.
+
.. Open the `<installation_directory>/manifests/cloud-provider-config.yaml` file.
+
.. Add the `network-project-id` parameter and set its value to the ID of project that hosts the shared VPC network.
+
.. Add the `network-name` parameter and set its value to the name of the shared VPC network that hosts the OpenShift Container Platform cluster.
+
.. Replace the value of the `subnetwork-name` parameter with the value of the shared VPC subnet that hosts your compute machines.
+
The contents of the `<installation_directory>/manifests/cloud-provider-config.yaml` resemble the following example:
+
[source,yaml]
----
config: |+
  [global]
  project-id      = example-project
  regional        = true
  multizone       = true
  node-tags       = opensh-ptzzx-master
  node-tags       = opensh-ptzzx-worker
  node-instance-prefix = opensh-ptzzx
  external-instance-groups-prefix = opensh-ptzzx
  network-project-id = example-shared-vpc
  network-name    = example-network
  subnetwork-name = example-worker-subnet
----

. If you deploy a cluster that is not on a private network, open the `<installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml` file and replace the value of the `scope` parameter with `External`. The contents of the file resemble the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
    type: LoadBalancerService
status:
  availableReplicas: 0
  domain: ''
  selector: ''
----

. Optional: If your Azure Stack Hub environment uses an internal certificate authority (CA), you must update the `.spec.trustedCA.name` field in the `<installation_directory>/manifests/cluster-proxy-01-config.yaml` file to use `user-ca-bundle`:
+
[source,yaml]
----
...
spec:
  trustedCA:
    name: user-ca-bundle
...
----
+
Later, you must update your bootstrap ignition to include the CA.

. When configuring Azure on user-provisioned infrastructure, you must export
some common variables defined in the manifest files to use later in the Azure
Resource Manager (ARM) templates:
+
.. Export the infrastructure ID by using the following command:
+
[source,terminal]
----
$ export INFRA_ID=<infra_id>
----
+
where:
+
`<infra_id>`:: Specifies that the OpenShift Container Platform cluster has been assigned an identifier (`INFRA_ID`) in the form of `<cluster_name>-<random_string>`. This identifier is used as the base name for most resources created using the provided ARM templates. This is the value of the `.status.infrastructureName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.
+
.. Export the resource group by using the following command:
+
[source,terminal]
----
$ export RESOURCE_GROUP=<resource_group>
----
+
where:
+
`<resource_group>`:: All resources created in this Azure deployment exists as part of a resource group. The resource group name is also based on the `INFRA_ID`, in the form of `<cluster_name>-<random_string>-rg`. This is the value of the `.status.platformStatus.azure.resourceGroupName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.

. Manually create your cloud credentials.
+
.. From the directory that contains the installation program, obtain details of the OpenShift Container Platform release image that your `openshift-install` binary is built to use:
+
[source,terminal]
----
$ openshift-install version
----
+
.Example output
[source,text]
----
release image quay.io/openshift-release-dev/ocp-release:4.y.z-x86_64
----
+
.. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
+
.. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \//
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \//
  --to=<path_to_directory_for_credentials_requests>
----
+
where:
+
`--included`::  Specifies to include only the manifests that your specific cluster configuration requires.
`<path_to_directory_with_installation_configuration>`:: Specifies the location of the `install-config.yaml` file.
`<path_to_directory_for_credentials_requests>`:: Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
+
This command creates a YAML file for each `CredentialsRequest` object.
+
.Sample `CredentialsRequest` object
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  labels:
    controller-tools.k8s.io: "1.0"
  name: openshift-image-registry-azure
  namespace: openshift-cloud-credential-operator
spec:
  secretRef:
    name: installer-cloud-credentials
    namespace: openshift-image-registry
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
----
+
.. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object. The format for the secret data varies for each cloud provider.
+
.Sample `secrets.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
    name: ${secret_name}
    namespace: ${secret_namespace}
stringData:
  azure_subscription_id: ${subscription_id}
  azure_client_id: ${app_id}
  azure_client_secret: ${client_secret}
  azure_tenant_id: ${tenant_id}
  azure_resource_prefix: ${cluster_name}
  azure_resourcegroup: ${resource_group}
  azure_region: ${azure_region}
----
+
.. Create a `cco-configmap.yaml` file in the manifests directory with the Cloud Credential Operator (CCO) disabled:
+
.Sample `ConfigMap` object
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
name: cloud-credential-operator-config
namespace: openshift-cloud-credential-operator
  annotations:
    release.openshift.io/create-only: "true"
data:
  disabled: "true"
----

. To create the Ignition configuration files, run the following command from the directory that contains the installation program:
+
[source,terminal]
----
$ ./openshift-install create ignition-configs --dir <installation_directory>
----
+
where:
+
`<installation_directory>`:: Specifies the same installation directory.
+
Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory. The `kubeadmin-password` and `kubeconfig` files are created in the `./<installation_directory>/auth` directory:
+
----
.
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
├── bootstrap.ign
├── master.ign
├── metadata.json
└── worker.ign
----

. Export the metadata file's `infraID` key as an environment variable:
+
[source,terminal]
----
$ export INFRA_ID=$(jq -r .infraID metadata.json)
----
+
[TIP]
Extract the `infraID` key from `metadata.json` and use it as a prefix for all of the {rh-openstack} resources that you create. By doing so, you avoid name conflicts when making multiple deployments in the same project.

[role="_additional-resources"]
.Additional resources

* See Recovering from expired control plane certificates for more information about recovering kubelet certificates.

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * machine_configuration/machine-configs-configure.adoc

[id="installation-special-config-chrony_{context}"]
= Configuring chrony time service

[role="_abstract"]
You
set the time server and related settings used by the chrony time service (`chronyd`)
by modifying the contents of the `chrony.conf` file and passing those contents
to your nodes as a machine config.

.Procedure

. Create a Butane config including the contents of the `chrony.conf` file. For example, to configure chrony on worker nodes, create a `99-worker-chrony.bu` file.
+
[NOTE]
====
====
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 99-worker-chrony
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  files:
  - path: /etc/chrony.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        pool 0.rhel.pool.ntp.org iburst
        driftfile /var/lib/chrony/drift
        makestep 1.0 3
        rtcsync
        logdir /var/log/chrony
----
+
--
* `name: 99-worker-chrony` - Specify a name for the machine config file. On control plane nodes, substitute `master` for `worker`.
* `machineconfiguration.openshift.io/role: worker` - On control plane nodes, substitute `master` for `worker`.
* `mode: 0644` - Specify an octal value mode for the `mode` field in the machine config file. After creating the file and applying the changes, the `mode` is converted to a decimal value. You can check the YAML file with the command `oc get mc <mc-name> -o yaml`.
* `pool 0.rhel.pool.ntp.org iburst` - Specify any valid, reachable time source, such as the one provided by your DHCP server.
--

+
[NOTE]
====
For all-machine to all-machine communication, the Network Time Protocol (NTP) on UDP is port `123`. If an external NTP time server is configured, you must open UDP port `123`.
====

. Use Butane to generate a `MachineConfig` object file, `99-worker-chrony.yaml`, containing the configuration to be delivered to the nodes:
+
[source,terminal]
----
$ butane 99-worker-chrony.bu -o 99-worker-chrony.yaml
----

. Apply the configurations in one of two ways:
+
* If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
+
* If the cluster is already running, apply the file:
+
[source,terminal]
----
$ oc apply -f ./99-worker-chrony.yaml
----

For more information on chrony best practices, see the following resources:

* https://access.redhat.com/solutions/3073261[Configuring chrony]
* https://access.redhat.com/solutions/778603[Best practices for NTP]
* https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/troubleshooting_guide/basic-chrony-NTP-troubleshooting_diag#basic-chrony-NTP-troubleshooting_diag[Basic chrony NTP troubleshooting]

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc

[id="creating-machines-bare-metal_{context}"]
= Installing {op-system} and starting the OpenShift Container Platform bootstrap process

[role="_abstract"]
To install OpenShift Container Platform on bare-metal infrastructure that you provision, install {op-system-first} by using the generated Ignition config files. Providing these files ensures the bootstrap process begins automatically after the machines reboot.

If you have configured suitable networking, DNS, and load balancing infrastructure, the OpenShift Container Platform bootstrap process begins automatically after the {op-system} machines have rebooted.

To install {op-system} on the machines, follow either the steps to use an ISO image or network PXE booting.

[NOTE]
====
The compute node deployment steps included in this installation document are {op-system}-specific. If you choose instead to deploy {op-system-base}-based compute nodes, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Only {op-system-base} 8 compute machines are supported.
====

You can configure {op-system} during ISO and PXE installations by using the following methods:

* Kernel arguments: You can use kernel arguments to provide installation-specific information. For example, you can specify the locations of the {op-system} installation files that you uploaded to your HTTP server and the location of the Ignition config file for the type of node you are installing. For a PXE installation, you can use the `APPEND` parameter to pass the arguments to the kernel of the live installer. For an ISO installation, you can interrupt the live installation boot process to add the kernel arguments. In both installation cases, you can use special `coreos.inst.*` arguments to direct the live installer, as well as standard installation boot arguments for turning standard kernel services on or off.

* Ignition configs: OpenShift Container Platform Ignition config files (`*.ign`) are specific to the type of node you are installing. You pass the location of a bootstrap, control plane, or compute node Ignition config file during the {op-system} installation so that it takes effect on first boot. In special cases, you can create a separate, limited Ignition config to pass to the live system. That Ignition config could do a certain set of tasks, such as reporting success to a provisioning system after completing installation. This special Ignition config is consumed by the `coreos-installer` to be applied on first boot of the installed system. Do not provide the standard control plane and compute node Ignition configs to the live ISO directly.

* `coreos-installer`: You can boot the live ISO installer to a shell prompt, which allows you to prepare the permanent system in a variety of ways before first boot. In particular, you can run the `coreos-installer` command to identify various artifacts to include, work with disk partitions, and set up networking. In some cases, you can configure features on the live system and copy them to the installed system.
+
[NOTE]
====
As of version `0.17.0-3`, `coreos-installer` requires {op-system-base} 9 or later to run the program. You can still use older versions of `coreos-installer` to customize {op-system} artifacts of newer OpenShift Container Platform releases and install metal images to disk. You can download older versions of the `coreos-installer` binary from the `coreos-installer` image mirror page.
====

Whether to use an ISO or PXE install depends on your situation. A PXE install requires an available DHCP service and more preparation, but can make the installation process more automated. An ISO install is a more manual process and can be inconvenient if you are setting up more than a few machines.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc

[id="installation-user-infra-machines-iso_{context}"]
= Installing {op-system} by using an ISO image

[role="_abstract"]
To provision physical or virtual machines, install {op-system} by using a bootable ISO image.

.Prerequisites

* You have created the Ignition config files for your cluster.
* You have configured a suitable network, DNS, and load balancing infrastructure.
* You have an HTTP server that can be accessed from your computer, and from the machines that you create.
* You have reviewed the _Advanced {op-system} installation configuration_ section for different ways to configure features, such as networking and disk partitioning.

.Procedure

. Obtain the SHA512 digest for each of your Ignition config files. For example, you can use the following on a system running Linux to get the SHA512 digest for your `bootstrap.ign` Ignition config file:
+
[source,terminal]
----
$ sha512sum <installation_directory>/bootstrap.ign
----
+
The digests are provided to the `coreos-installer` in a later step to validate the authenticity of the Ignition config files on the cluster nodes.

. Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files.
+
[IMPORTANT]
====
You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
====

. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:
+
[source,terminal]
----
$ curl -k http://<HTTP_server>/bootstrap.ign
----
* <HTTP_server>: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.
+
.Example output
[source,terminal]
----
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
----

. Although it is possible to obtain the {op-system} images that are required for your preferred method of installing operating system instances from the
{op-system} image mirror
{op-system}
{op-system} image mirror
page, the recommended way to obtain the correct version of your {op-system} images are from the output of `openshift-install` command:
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | grep '\.iso[^.]'
----
+
.Example output
[source,terminal]
----
"location": "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live.aarch64.iso",
"location": "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live.ppc64le.iso",
"location": "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live.s390x.iso",
"location": "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live.x86_64.iso",
----
+
[source,terminal]
----
"location": "<url>/prod/streams/stable/builds/<release>/x86_64/fedora-coreos-<release>-live.x86_64.iso",
----
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. Use only ISO images for this procedure. {op-system} qcow2 images are not supported for this installation type.
====
+
ISO file names resemble the following example:
+
`rhcos-<version>-live.<architecture>.iso`
`fedora-coreos-<version>-live.<architecture>.iso`

. Use the ISO to start the {op-system} installation. Use one of the following installation options:
** Burn the ISO image to a disk and boot it directly.
** Use ISO redirection by using a lights-out management (LOM) interface.

. Boot the {op-system} ISO image without specifying any options or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the {op-system} live environment.
+
[NOTE]
====
It is possible to interrupt the {op-system} installation boot process to add kernel arguments. However, for this ISO procedure you should use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments.
====

. Run the `coreos-installer` command and specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to:
+
[source,terminal]
----
$ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> \
--ignition-hash=sha512-<digest> --offline
----
[source,terminal]
----
$ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> \
--ignition-hash=sha512-<digest>
----
* `<device>`: You must run the `coreos-installer` command by using `sudo`, because the `core` user does not have the required root privileges to perform the installation.
* `<digest>`: The `--ignition-hash` option is required when the Ignition config file is obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node. `<digest>` is the Ignition config file SHA512 digest obtained in a preceding step.
+
[NOTE]
====
If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`.
====
+
The following example initializes a bootstrap node installation to the `/dev/sda` device. The Ignition config file for the bootstrap node is obtained from an HTTP web server with the IP address 192.168.1.2:
+
[source,terminal]
----
$ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/bootstrap.ign /dev/sda \
--ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b \
--offline
----
[source,terminal]
----
$ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/bootstrap.ign /dev/sda \
--ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
----

. Monitor the progress of the {op-system} installation on the console of the machine.
+
[IMPORTANT]
====
Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of {op-system} installation issues that might arise.
====

. After {op-system} installs, you must reboot the system. During the system reboot, it applies the Ignition config file that you specified.

. Check the console output to verify that Ignition ran.
+
.Example command
[source,terminal]
----
Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
Ignition: user-provided config was applied
----

. Continue to create the other machines for your cluster.
+
[IMPORTANT]
====
You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install OpenShift Container Platform.
====
+
If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the {op-system} nodes have rebooted.
+
[NOTE]
====
{op-system} nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running {op-system} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc

[id="installation-user-infra-machines-pxe_{context}"]
= Installing {op-system} by using PXE or iPXE booting
= Installing {op-system} by using PXE booting

[role="_abstract"]
You can use PXE or iPXE booting to install {op-system} on the machines.
You can use PXE booting to install {op-system} on the machines.

.Prerequisites

* You have created the Ignition config files for your cluster.
* You have configured a suitable network, DNS and load balancing infrastructure.
* You have configured suitable PXE or iPXE infrastructure.
* You have configured suitable PXE infrastructure.
* You have an HTTP server that can be accessed from your computer, and from the machines that you create.
* You have reviewed the _Advanced {op-system} installation configuration_ section for different ways to configure features, such as networking and disk partitioning.

.Procedure

. Upload the bootstrap, control plane, and compute node Ignition config files that the
installation program created to your HTTP server. Note the URLs of these files.
+
[IMPORTANT]
====
You can add or change configuration settings in your Ignition configs
before saving them to your HTTP server.
If you plan to add more compute machines to your cluster after you finish
installation, do not delete these files.
====

. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:
+
[source,terminal]
----
$ curl -k http://<HTTP_server>/bootstrap.ign
----
+
* `<HTTP_server>`: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.
+
.Example output
[source,terminal]
----
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
----

. Although it is possible to obtain the {op-system} `kernel`, `initramfs` and `rootfs`
files that are required for your preferred method of installing operating system instances from the
{op-system} image mirror
{op-system}
{op-system} image mirror
page, the recommended way to obtain the correct version of your {op-system} files are
from the output of `openshift-install` command:
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | grep -Eo '"https.*(kernel-|initramfs.|rootfs.)\w+(\.img)?"'
----
+
.Example output
[source,terminal]
----
"<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-kernel-aarch64"
"<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-initramfs.aarch64.img"
"<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-rootfs.aarch64.img"
"<url>/art/storage/releases/rhcos-4.22-ppc64le/49.84.202110081256-0/ppc64le/rhcos-<release>-live-kernel-ppc64le"
"<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-initramfs.ppc64le.img"
"<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-rootfs.ppc64le.img"
"<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-kernel-s390x"
"<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-initramfs.s390x.img"
"<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-rootfs.s390x.img"
"<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-kernel-x86_64"
"<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-initramfs.x86_64.img"
"<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-rootfs.x86_64.img"
----
----
"<url>/prod/streams/stable/builds/<release>/x86_64/fedora-coreos-<release>-live-kernel-x86_64"
"<url>/prod/streams/stable/builds/<release>/x86_64/fedora-coreos-<release>-live-initramfs.x86_64.img"
"<url>/prod/streams/stable/builds/<release>/x86_64/fedora-coreos-<release>-live-rootfs.x86_64.img"
----
+
[IMPORTANT]
====
The {op-system} artifacts might not change with every release of OpenShift Container Platform.
You must download images with the highest version that is less than or equal
to the OpenShift Container Platform version that you install. Only use
the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described below
for this procedure.
{op-system} QCOW2 images are not supported for this installation type.
====
+
The file names contain the OpenShift Container Platform version number. They resemble the following examples:
+
** `kernel`: `rhcos-<version>-live-kernel-<architecture>`
** `initramfs`: `rhcos-<version>-live-initramfs.<architecture>.img`
** `rootfs`: `rhcos-<version>-live-rootfs.<architecture>.img`
** `kernel`: `fedora-coreos-<version>-live-kernel-<architecture>`
** `initramfs`: `fedora-coreos-<version>-live-initramfs.<architecture>.img`
** `rootfs`: `fedora-coreos-<version>-live-rootfs.<architecture>.img`

. Upload the `rootfs`, `kernel`, and `initramfs` files
to your HTTP server.
+
[IMPORTANT]
====
If you plan to add more compute machines to your cluster after you finish
installation, do not delete these files.
====

. Configure the network boot infrastructure so that the machines boot from their
local disks after {op-system} is installed on them.

. Configure PXE or iPXE installation for the {op-system} images and begin the installation.
. Configure PXE installation for the {op-system} images and begin the installation.
+
. Modify one of the following example menu entries for your environment and verify that the image and Ignition files are properly accessible:
. Modify the following example menu entry for your environment and verify that the image and Ignition files are properly accessible:
** For PXE (`x86_64`):
+
----
DEFAULT pxeboot
TIMEOUT 20
PROMPT 0
LABEL pxeboot
    KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
    APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
----
+
where:
+
`kernel`:: Specify the location of the live `kernel` file that you uploaded to your HTTP server. The URL must be HTTP, TFTP, or FTP; HTTPS and NFS are not supported.
`initrd=main`:: If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`. Specify the locations of the {op-system} files that you uploaded to your HTTP server. The `initrd` parameter value is the location of the `initramfs` file, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. You can also add more kernel arguments to the `APPEND` line to configure networking or other boot options.
+
[NOTE]
====
This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information, see How does one set up a serial terminal and/or console in Red Hat Enterprise Linux? and "Enabling the serial console for PXE and ISO installation" in the "Advanced {op-system} installation configuration" section.
====

** For iPXE (`x86_64`
+ `aarch64`
):
+
----
kernel http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture> initrd=main coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
initrd --name main http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img
boot
----
`kernel`:: Specify the locations of the {op-system} files that you uploaded to your HTTP server. The `kernel` parameter value is the location of the `kernel` file, the `initrd=main` argument is needed for booting on UEFI systems, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. If you use multiple NICs, specify a single interface in the `ip` option.
For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`.
`initrd`:: Specify the location of the `initramfs` file that you uploaded to your HTTP server.
+
[NOTE]
====
This configuration does not enable serial console access on machines with a graphical console.  To configure a different console, add one or more `console=` arguments to the `kernel` line.  For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console.  For more information, see How does one set up a serial terminal and/or console in Red Hat Enterprise Linux? and "Enabling the serial console for PXE and ISO installation" in the "Advanced {op-system} installation configuration" section.
====
+
[NOTE]
====
To network boot the CoreOS `kernel` on `aarch64` architecture, you need to use a version of iPXE build with the `IMAGE_GZIP` option enabled. See `IMAGE_GZIP` option in iPXE.
====
** For PXE (with UEFI and Grub as second stage) on `aarch64`:
+
----
menuentry 'Install CoreOS' {
    linux rhcos-<version>-live-kernel-<architecture>  coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
    initrd rhcos-<version>-live-initramfs.<architecture>.img
}
----
+
where:
+
`coreos.live.rootfs_url`:: Specify the locations of the {op-system} files that you uploaded to your HTTP/TFTP server.
`kernel`:: The `kernel` parameter value is the location of the `kernel` file on your TFTP server. The `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file on your HTTP Server. If you use multiple NICs, specify a single interface in the `ip` option.
For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`.
`initrd rhcos`:: Specify the location of the `initramfs` file that you uploaded to your TFTP server.

. Monitor the progress of the {op-system} installation on the console of the machine.
+
[IMPORTANT]
====
Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of {op-system} installation issues that might arise.
====

. After {op-system} installs, the system reboots. During reboot, the system applies the Ignition config file that you specified.

. Check the console output to verify that Ignition ran.
+
.Example command
[source,terminal]
----
Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
Ignition: user-provided config was applied
----

. Continue to create the machines for your cluster.
+
[IMPORTANT]
====
You must create the bootstrap and control plane machines at this time. If the
control plane machines are not made schedulable, also
create at least two compute machines before you install the cluster.
====
+
If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the {op-system} nodes have rebooted.
+
[NOTE]
====
{op-system} nodes do not include a default password for the  `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running {op-system} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="installation-user-infra-machines-advanced_{context}"]
= Advanced {op-system} installation configuration

[role="_abstract"]
To apply advanced configurations unavailable through default installation methods, manually provision {op-system-first} nodes for OpenShift Container Platform.

This approach enables granular control over the node infrastructure to meet specific deployment requirements.

* Passing kernel arguments to the live installer
* Running `coreos-installer` manually from the live system
* Customizing a live ISO or PXE boot image

The advanced configuration topics for manual {op-system-first} installations detailed in this section relate to disk partitioning, networking, and configuring Ignition in different ways.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="installation-user-infra-machines-advanced_network_{context}"]
= Using advanced networking options for PXE and ISO installations

[role="_abstract"]
Networking for OpenShift Container Platform nodes uses DHCP by default to gather all necessary configuration settings. You can set up static IP addresses or configure special settings.

To set up static IP addresses or configure special settings, such as bonding, you can do one of the following:

* Pass special kernel parameters when you boot the live installer.

* Use a machine config to copy networking files to the installed system.

* Configure networking from a live installer shell prompt, then copy those settings to the installed system so that they take effect when the installed system first boots.

To configure a PXE or iPXE installation, use one of the following options:

* See the "coreos-installer and boot options for ISO and PXE installations" tables.

* Use a machine config to copy networking files to the installed system.

To configure an ISO installation, use the following procedure.

.Procedure

. Boot the ISO installer.

. From the live system shell prompt, configure networking for the live system by using available RHEL tools, such as `nmcli` or `nmtui`.

. Run the `coreos-installer` command to install the system, adding the `--copy-network` option to copy networking configuration. For example:
+
[source,terminal]
----
$ sudo coreos-installer install --copy-network \
     --ignition-url=http://host/worker.ign /dev/disk/by-id/scsi-<serial_number>
----
[source,terminal]
----
$ sudo coreos-installer install --copy-network \
--ignition-url=http://host/worker.ign \
--offline \
/dev/disk/by-id/scsi-<serial_number>
----
+
[IMPORTANT]
====
The `--copy-network` option only copies networking configuration found under `/etc/NetworkManager/system-connections`. In particular, it does not copy the system hostname.
====

. Reboot into the installed system.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="installation-user-infra-machines-advanced-disk_{context}"]
= Disk partitioning

[role="_abstract"]
Disk partitions are created on OpenShift Container Platform cluster nodes during the {op-system-first} installation. Each {op-system} node of a particular architecture uses the same partition layout, unless you override the default partitioning configuration.

During the {op-system} installation, the size of the root file system is increased to use any remaining available space on the target device.

[IMPORTANT]
====
The use of a custom partition scheme on your node might result in OpenShift Container Platform not monitoring or alerting on some node partitions. For more information on monitoring host file systems when using custom partitioning, see Understanding OpenShift File System Monitoring (eviction conditions).
====

OpenShift Container Platform monitors the following two filesystem identifiers:

* `nodefs`, which is the filesystem that contains `/var/lib/kubelet`.
* `imagefs`, which is the filesystem that contains `/var/lib/containers`.

For the default partition scheme, `nodefs` and `imagefs` monitor the same root filesystem, `/`.

To override the default partitioning when installing {op-system} on an OpenShift Container Platform cluster node, you must create separate partitions. Consider a situation where you want to add a separate storage partition for your containers and container images. For example, by mounting `/var/lib/containers` in a separate partition, the kubelet separately monitors `/var/lib/containers` as the `imagefs` directory and the root file system as the `nodefs` directory.

[IMPORTANT]
====
If you have resized your disk size to host a larger file system, consider creating a separate `/var/lib/containers` partition. Consider resizing a disk that has an `xfs` format to reduce CPU time issues caused by a high number of allocation groups.
====
[id="installation-user-infra-machines-advanced-disk_{context}"]
= Creating disk partitions

[role="_abstract"]
In general, you must use the default disk partitioning that is created during the {op-system} installation. However, there are cases where you might want to create a separate partition for a directory that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` directory or a subdirectory of `/var`. For example:

* `/var/lib/containers`: Holds container-related content that can grow
as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.
+
[IMPORTANT]
====
For disk sizes larger than 100GB, and especially larger than 1TB, create a separate `/var` partition.
====

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date to keep that data intact. This method eliminates the need to re-pull containers or copy large log files during system updates.

The use of a separate partition for the `/var` directory or a subdirectory of `/var` also prevents data growth in the partitioned directory from filling up the root file system.

The following procedure sets up a separate `/var` partition by adding a machine config manifest that is wrapped into the Ignition config file for a node type during the preparation phase of an installation.

.Prerequisites
* You have created an `openshift` subdirectory within your installation directory.

.Procedure

. On your installation host, change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ openshift-install create manifests --dir <installation_directory>
----

. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 98-var-partition
storage:
  disks:
  - device: /dev/disk/by-id/<device_name>
    partitions:
    - label: var
      start_mib: <partition_start_offset>
      size_mib: <partition_size>
      number: 5
  filesystems:
    - device: /dev/disk/by-partlabel/var
      path: /var
      format: xfs
      mount_options: [defaults, prjquota]
      with_mount_unit: true
----
+
where:
+
`<device_name>`:: Specifies the storage device name of the disk that you want to partition.
`<partition_start_offset>`:: Specifies the minimum offset value for the boot disk. For best performance, specify a minimum offset value of 25000 mebibytes. The root file system is automatically resized to fill all available space up to the specified offset. If no offset value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of {op-system} might overwrite the beginning of the data partition.
`<partition_size>`:: Specifies the size of the data partition in mebibytes.
`mount_options`:: The `prjquota` mount option must be enabled for filesystems used for container storage.
+
[NOTE]
====
When creating a separate `/var` partition, you cannot use different instance types for compute nodes, if the different instance types do not have the same device name.
====

. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:
+
[source,terminal]
----
$ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
----

. Create the Ignition config files by running the following command:
+
[source,terminal]
----
$ openshift-install create ignition-configs --dir <installation_directory>
----
+
where:
+
`<installation_directory>`:: Specifies the name of the installation directory.
+
Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory:
+
----
.
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
├── bootstrap.ign
├── master.ign
├── metadata.json
└── worker.ign
----
+
The files in the `<installation_directory>/manifest` and `<installation_directory>/openshift` directories are wrapped into the Ignition config files, including the file that contains the `98-var-partition` custom `MachineConfig` object.

. Optional: You can apply the custom disk partitioning by referencing the Ignition config files during the {op-system} installations.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="installation-user-infra-machines-advanced-retain-disk_{context}"]
= Examples of retaining existing partitions

[role="_abstract"]
For an ISO installation, you can add options to the `coreos-installer` command that causes the installation program to maintain one or more existing partitions. For a PXE installation, you can add `coreos.inst.*` options to the `APPEND` parameter to preserve partitions.

Saved partitions might be data partitions from an existing OpenShift Container Platform system. You can identify the disk partitions you want to keep either by partition label or by number.

[NOTE]
====
If you save existing partitions, and those partitions do not leave enough space for {op-system}, the installation fails without damaging the saved partitions.
====

The following examples preserve any existing partition during an ISO installation in which the partition label begins with `data` (`data*`):

[source,terminal]
----
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partlabel 'data*' \
/dev/disk/by-id/scsi-<serial_number>
----

[source,terminal]
----
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partlabel 'data*' \
--offline \
/dev/disk/by-id/scsi-<serial_number>
----

The following example runs the `coreos-installer` in a way that preserves
the sixth (6) partition on the disk:

[source,terminal]
----
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partindex 6 /dev/disk/by-id/scsi-<serial_number>
----

[source,terminal]
----
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partindex 6 \
--offline \
/dev/disk/by-id/scsi-<serial_number>
----

The following example preserves partitions 5 and higher:

[source,terminal]
----
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partindex 5- /dev/disk/by-id/scsi-<serial_number>
----

[source,terminal]
----
# coreos-installer install --ignition-url http://10.0.2.2:8080/user.ign \
--save-partindex 5- \
--offline \
/dev/disk/by-id/scsi-<serial_number>
----

In the earlier examples where partition saving is used, `coreos-installer` recreates the partition immediately.

The following examples preserve existing partitions during a PXE installation. The following `APPEND` option preserves any partition in which the partition label begins with 'data' ('data*').

[source,terminal]
----
coreos.inst.save_partlabel=data*
----

The following `APPEND` option preserves partitions 5 and higher:

[source,terminal]
----
coreos.inst.save_partindex=5-
----

The following `APPEND` option preserves partition 6:

[source,terminal]
----
coreos.inst.save_partindex=6
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="installation-user-infra-machines-advanced-ignition_{context}"]
= Identifying Ignition configs

[role="_abstract"]
When doing an {op-system} manual installation, there are two types of Ignition configs that you can provide: Permanent install Ignition config and live install Ignition config.

When manually installing {op-system}, you can provide the following two types of Ignition configs:

* **Permanent install Ignition config**: Every manual {op-system} installation needs to pass one of the Ignition config files generated by `openshift-installer`, such as `bootstrap.ign`, `master.ign` and `worker.ign`, to carry out the installation.

[IMPORTANT]
====
Do not modify these Ignition config files directly. You can update the manifest files that are wrapped into the Ignition config files, as outlined in examples in the preceding sections.
====

For PXE installations, you can pass the Ignition configs on the `APPEND` line using the `coreos.inst.ignition_url=` option. For ISO installations, after the ISO boots to the shell prompt, you must identify the Ignition config on the `coreos-installer` command line with the `--ignition-url=` option. In both cases, only HTTP and HTTPS protocols are supported.

* **Live install Ignition config**: This type can be created by using the `coreos-installer` `customize` subcommand of `coreos-installer` and its various options. With this method, the Ignition config passes to the live install medium, runs immediately upon booting, and performs setup tasks before or after the {op-system} system installs to disk. This method must be only used for performing tasks that must be done once and not applied again later, such as with advanced partitioning that cannot be done using a machine config.

For PXE or ISO boots, you can create the Ignition config and `APPEND` the `ignition.config.url=` option to identify the location of the Ignition config. You also need to append `ignition.firstboot ignition.platform.id=metal` else the `ignition.config.url` option is ignored.

[role="_additional-resources"]
.Additional resources

* Getting started with nmcli
* Getting started with nmtui

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-console-configuration_{context}"]
= Default console configuration

[role="_abstract"]
{op-system-first} nodes installed from an OpenShift Container Platform  boot image use a default console that is meant to accomodate most virtualized and bare metal setups. Different cloud and virtualization platforms may use different default settings depending on the chosen architecture.

Bare-metal installations use the kernel default settings which typically means the graphical console is the primary console and the serial console is disabled.

The default consoles may not match your specific hardware configuration or you might have specific needs that require you to adjust the default console. For example:

* You want to access the emergency shell on the console for debugging purposes.
* Your cloud platform does not provide interactive access to the graphical console, but provides a serial console.
* You want to enable multiple consoles.

Console configuration is inherited from the boot image. This means that new nodes in existing clusters are unaffected by changes to the default console.

You can configure the console for bare metal installations in the following ways:

* Using `coreos-installer` manually on the command line.
* Using the `coreos-installer iso customize` or `coreos-installer pxe customize` subcommands with the `--dest-console` option to create a custom image that automates the process.

[NOTE]
====
For advanced customization, perform console configuration using the `coreos-installer iso` or `coreos-installer pxe` subcommands, and not kernel arguments.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-enabling-serial-console_{context}"]
= Enabling the serial console for PXE and ISO installations

[role="_abstract"]
By default, the {op-system-first} serial console is disabled and all output is written to the graphical console. You can enable the serial console for PXE and ISO installations.

.Procedure

. Boot the ISO installer.

. Run the `coreos-installer` command to install the system, adding the `--console` option once to specify the graphical console, and a second time to specify the serial console:
+
[source,terminal]
----
$ coreos-installer install \
--console=tty0 \
--console=ttyS0,<options> \
--ignition-url=http://host/worker.ign /dev/disk/by-id/scsi-<serial_number>
----
[source,terminal]
----
$ coreos-installer install \
--console=tty0 \
--console=ttyS0,<options> \
--ignition-url=http://host/worker.ign \
--offline \
/dev/disk/by-id/scsi-<serial_number>
----
+
where:
+
`--console=tty0`:: The desired secondary console. In this case, the graphical console. Omitting this option will disable the graphical console.
`--console=ttyS0`:: The desired primary console. In this case, the serial console. The `options` field defines the baud rate and other settings. A common value for this field is `115200n8`. If no options are provided, the default kernel value of `9600n8` is used. For more information on the format of this option, see Linux kernel serial console documentation.

. Reboot into the installed system.
+
[NOTE]
====
A similar outcome can be obtained by using the `coreos-installer install --append-karg` option, and specifying the console with `console=`. However, this will only set the console for the kernel and not the bootloader.
====
+
To configure a PXE installation, make sure the `coreos.inst.install_dev` kernel command-line option is omitted, and use the shell prompt to run `coreos-installer` manually using the above ISO installation procedure.

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-customizing-iso-or-pxe_{context}"]
= Customizing a live {op-system} ISO or PXE install

[role="_abstract"]
You can use the live ISO image or PXE environment to install {op-system} by injecting an Ignition config file directly into the image. This creates a customized image that you can use to provision your system.

For an ISO image, the mechanism to do this is the `coreos-installer iso customize` subcommand, which modifies the `.iso` file with your configuration. Similarly, the mechanism for a PXE environment is the `coreos-installer pxe customize` subcommand, which creates a new `initramfs` file that includes your customizations.

The `customize` subcommand is a general-purpose tool that can embed other types of customizations as well. The following tasks are examples of some of the more common customizations:

* Inject custom CA certificates for when corporate security policy requires their use.
* Configure network settings without the need for kernel arguments.
* Embed arbitrary pre-install and post-install scripts or binaries.

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-customizing-live-{boot}_{context}"]
= Customizing a live {op-system} {boot-media}

[role="_abstract"]
You can customize a live {op-system} {boot-media} directly with the
`coreos-installer iso customize`
`coreos-installer pxe customize`
subcommand. When you boot the {boot-media}, the customizations are applied automatically. You can use this feature to configure the {boot-media} to automatically install {op-system}.

.Procedure

. Download the `coreos-installer` binary from the `coreos-installer` image mirror page.

. Retrieve the {op-system} ISO image from the {op-system} image mirror page and the Ignition config file, and then run the following command to inject the Ignition config directly into the ISO image:
+
[source,terminal]
----
$ coreos-installer iso customize rhcos-<version>-live.x86_64.iso \
    --dest-ignition bootstrap.ign \
    --dest-device /dev/disk/by-id/scsi-<serial_number>
----
+
where:
+
`--dest-ignition`:: Specifies the Ignition config file that is generated from the `openshift-installer` installation program.
`--dest-device`:: When you specify this option, the {boot-media} automatically runs an installation. Otherwise, the image remains configured for installation, but does not install automatically unless you specify the `coreos.inst.install_dev` kernel argument.

. Optional: To remove the {boot-media} customizations and return the image to its pristine state, run:
+
[source,terminal]
----
$ coreos-installer iso reset rhcos-<version>-live.x86_64.iso
----
+
You can now re-customize the live {boot-media} or use it in its pristine state.

. Retrieve the {op-system} `kernel`, `initramfs`, and `rootfs` files from the {op-system} image mirror page and the Ignition config file, and then run the following command to create a new `initramfs` file that contains the customizations from your Ignition config:
+
[source,terminal]
----
$ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
    --dest-ignition bootstrap.ign \
    --dest-device /dev/disk/by-id/scsi-<serial_number> \
    -o rhcos-<version>-custom-initramfs.x86_64.img
----
+
where:
+
`--dest-ignition`:: Specifies the Ignition config file that is generated from `openshift-installer`.
`<serial_number>`:: When you specify this option, the {boot-media} automatically runs an install. Otherwise, the image remains configured for installation, but does not do so automatically unless you specify the `coreos.inst.install_dev` kernel argument.
`<version>`:: Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.
+
Applying your customizations affects every subsequent boot of {op-system}.

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-customizing-live-{boot}-serial-console_{context}"]
= Modifying a live install {boot-media} to enable the serial console

[role="_abstract"]
To redirect system output from the default graphical interface, enable the serial console by modifying the live install {boot-media}. This configuration ensures access to boot messages on OpenShift Container Platform 4.12 and later clusters.

.Procedure

. Download the `coreos-installer` binary from the `coreos-installer` image mirror page.

. Retrieve the {op-system} ISO image from the {op-system} image mirror page and run the following command to customize the ISO image to enable the serial console to receive output:
+
[source,terminal]
----
$ coreos-installer iso customize rhcos-<version>-live.x86_64.iso \
  --dest-ignition <path> \
  --dest-console tty0 \
  --dest-console ttyS0,<options> \
  --dest-device /dev/disk/by-id/scsi-<serial_number>
----
+
where:
+
`<path>`:: The location of the Ignition config to install.
`tty0`:: The desired secondary console. In this case, the graphical console. Omitting this option will disable the graphical console.
`<options>`:: The desired primary console. In this case, the serial console. The `options` field defines the baud rate and other settings. A common value for this field is `115200n8`. If no options are provided, the default kernel value of `9600n8` is used. For more information on the format of this option, see the Linux kernel serial console documentation.
`<serial_number>`:: The specified disk to install to. If you omit this option, the {boot-media} automatically runs the installation program which will fail unless you also specify the `coreos.inst.install_dev` kernel argument.
+
[NOTE]
====
The `--dest-console` option affects the installed system and not the live ISO system. To modify the console for a live ISO system, use the `--live-karg-append` option and specify the console with `console=`.
====
+
Your customizations are applied and affect every subsequent boot of the {boot-media}.

. Optional: To remove the {boot-media} customizations and return the image to its original state, run the following command:
+
[source,terminal]
----
$ coreos-installer iso reset rhcos-<version>-live.x86_64.iso
----
+
You can now recustomize the live {boot-media} or use it in its original state.

. Retrieve the {op-system} `kernel`, `initramfs`, and `rootfs` files from the {op-system} image mirror page and the Ignition config file, and then run the following command to create a new customized `initramfs` file that enables the serial console to receive output:
+
[source,terminal]
----
$ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
  --dest-ignition <path> \
  --dest-console tty0 \
  --dest-console ttyS0,<options> \
  --dest-device /dev/disk/by-id/scsi-<serial_number> \
  -o rhcos-<version>-custom-initramfs.x86_64.img
----
+
where:
+
`<path>`:: The location of the Ignition config to install.
`tty0`:: The desired secondary console. In this case, the graphical console. Omitting this option will disable the graphical console.
`<options>`:: The desired primary console. In this case, the serial console. The `options` field defines the baud rate and other settings. A common value for this field is `115200n8`. If no options are provided, the default kernel value of `9600n8` is used. For more information on the format of this option, see the Linux kernel serial console documentation.
`<serial_number>`:: The specified disk to install to. If you omit this option, the {boot-media} automatically runs the installation program which will fail unless you also specify the `coreos.inst.install_dev` kernel argument.
`<version>`:: Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.
+
Your customizations are applied and affect every subsequent boot of the {boot-media}.

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-customizing-live-{boot}-ca-certs_{context}"]
= Modifying a live install {boot-media} to use a custom certificate authority

[role="_abstract"]
You can provide certificate authority (CA) certificates to Ignition with the `--ignition-ca` flag of the `customize` subcommand. You can use the CA certificates during both the installation boot and when provisioning the installed system.

[NOTE]
====
Custom CA certificates affect how Ignition fetches remote resources, but they do not affect the certificates installed onto the system.
====

.Procedure

. Download the `coreos-installer` binary from the `coreos-installer` image mirror page.

. Retrieve the {op-system} ISO image from the {op-system} image mirror page, and run the following command to customize the ISO image for use with a custom CA:
+
[source,terminal]
----
$ coreos-installer iso customize rhcos-<version>-live.x86_64.iso --ignition-ca cert.pem
----

. Retrieve the {op-system} `kernel`, `initramfs`, and `rootfs` files from the {op-system} image mirror page, and run the following command to create a new customized `initramfs` file for use with a custom CA:
+
[source,terminal]
----
$ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
    --ignition-ca cert.pem \
    -o rhcos-<version>-custom-initramfs.x86_64.img
----

. Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.
+
[IMPORTANT]
====
The `coreos.inst.ignition_url` kernel parameter does not work with the `--ignition-ca` flag.
You must use the `--dest-ignition` flag to create a customized image for each cluster.
====
+
Applying your custom CA certificate affects every subsequent boot of {op-system}.

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-customizing-live-{boot}_network_keyfile_{context}"]
= Modifying a live install {boot-media} with customized network settings

[role="_abstract"]
You can embed a NetworkManager keyfile into the live {boot-media} and pass it through to the installed system with the `--network-keyfile` flag of the `customize` subcommand.

[WARNING]
====
When creating a connection profile, you must use a `.nmconnection` filename extension in the filename of the connection profile. If you do not use a `.nmconnection` filename extension, the cluster will apply the connection profile to the live environment, but it will not apply the configuration when the cluster first boots up the nodes, resulting in a setup that does not work.
====

.Procedure

. Download the `coreos-installer` binary from the `coreos-installer` image mirror page.

. Create a connection profile for a bonded interface. For example, create the `bond0.nmconnection` file in your local directory with the following content:
+
[source,terminal,subs="quotes,verbatim"]
----
/[connection]
id=bond0
type=bond
interface-name=bond0
multi-connect=1

/[bond]
miimon=100
mode=active-backup

/[ipv4]
method=auto

/[ipv6]
method=auto
----

. Create a connection profile for a secondary interface to add to the bond. For example, create the `bond0-proxy-em1.nmconnection` file in your local directory with the following content:
+
[source,terminal,subs="quotes,verbatim"]
----
/[connection]
id=em1
type=ethernet
interface-name=em1
master=bond0
multi-connect=1
slave-type=bond
----

. Create a connection profile for a secondary interface to add to the bond. For example, create the `bond0-proxy-em2.nmconnection` file in your local directory with the following content:
+
[source,terminal,subs="quotes,verbatim"]
----
/[connection]
id=em2
type=ethernet
interface-name=em2
master=bond0
multi-connect=1
slave-type=bond
----

. Retrieve the {op-system} ISO image from the {op-system} image mirror page and run the following command to customize the ISO image with your configured networking:
+
[source,terminal]
----
$ coreos-installer iso customize rhcos-<version>-live.x86_64.iso \
    --network-keyfile bond0.nmconnection \
    --network-keyfile bond0-proxy-em1.nmconnection \
    --network-keyfile bond0-proxy-em2.nmconnection
----

. Retrieve the {op-system} `kernel`, `initramfs`, and `rootfs` files from the {op-system} image mirror page and run the following command to create a new customized `initramfs` file that contains your configured networking:
+
[source,terminal]
----
$ coreos-installer pxe customize rhcos-<version>-live-initramfs.x86_64.img \
    --network-keyfile bond0.nmconnection \
    --network-keyfile bond0-proxy-em1.nmconnection \
    --network-keyfile bond0-proxy-em2.nmconnection \
    -o rhcos-<version>-custom-initramfs.x86_64.img
----

. Use the customized `initramfs` file in your PXE configuration. Add the `ignition.firstboot` and `ignition.platform.id=metal` kernel arguments if they are not already present.
+
Network settings are applied to the live system and are carried over to the destination system.

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-customizing-live-{boot}-iscsi-manual_{context}"]
= Customizing a live install {boot-media} for an iSCSI boot device

[role="_abstract"]
You can set the iSCSI target and initiator values for automatic mounting, booting and configuration by using a customized version of the live {op-system} image.

.Prerequisites
. You have an iSCSI target you want to install {op-system} on.

.Procedure

. Download the `coreos-installer` binary from the `coreos-installer` image mirror page.

. Retrieve the {op-system} ISO image from the {op-system} image mirror page and run the following command to customize the ISO image with the following information:
+
[source,text]
----
$ coreos-installer iso customize \
    --pre-install mount-iscsi.sh \
    --post-install unmount-iscsi.sh \
    --dest-device /dev/disk/by-path/<IP_address>:<port>-iscsi-<target_iqn>-lun-<lun> \
    --dest-ignition config.ign \
    --dest-karg-append rd.iscsi.initiator=<initiator_iqn> \
    --dest-karg-append netroot=<target_iqn> \
    -o custom.iso rhcos-<version>-live.x86_64.iso
----
+
where:
+
`mount-iscsi.sh`:: Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target and any commands enabling multipathing.
`unmount-iscsi.sh`:: Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.
`<target_iqn>`:: Specifies the location of the destination system. You must provide the IP address of the target portal, the associated port number, the target iSCSI node in IQN format, and the iSCSI logical unit number (LUN).
`config.ign`:: Specifies the Ignition configuration for the destination system.
`<initiator_iqn>`::Specifies the iSCSI initiator, or client, name in IQN format. The initiator forms a session to connect to the iSCSI target.
`<target_iqn>`::Specifies the iSCSI target, or server, name in IQN format.

. Retrieve the {op-system} `kernel`, `initramfs`, and `rootfs` files from the {op-system} image mirror page and run the following command to create a new customized `initramfs` file with the following information:
+
[source,text]
----
$ coreos-installer pxe customize \
    --pre-install mount-iscsi.sh \
    --post-install unmount-iscsi.sh \
    --dest-device /dev/disk/by-path/<IP_address>:<port>-iscsi-<target_iqn>-lun-<lun> \
    --dest-ignition config.ign \
    --dest-karg-append rd.iscsi.initiator=<initiator_iqn> \
    --dest-karg-append netroot=<target_iqn> \
    -o custom.img rhcos-<version>-live-initramfs.x86_64.img
----
+
where:
+
`mount-iscsi.sh`:: Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target and any commands enabling multipathing.
`unmount-iscsi.sh`:: Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.
`<target_iqn>`:: Specifies the location of the destination system. You must provide the IP address of the target portal, the associated port number, the target iSCSI node in IQN format, and the iSCSI logical unit number (LUN).
`config.ign`:: Specifies the Ignition configuration for the destination system.
`<initiator_iqn>`:: Specifies the iSCSI initiator, or client, name in IQN format. The initiator forms a session to connect to the iSCSI target.
`<target_iqn>`:: Specifies the iSCSI target, or server, name in IQN format.
+
For more information about the iSCSI options supported by `dracut`, see the `dracut.cmdline` manual page.

[role="_additional-resources"]
.Additional resources

* `dracut.cmdline` manual page

// Module included in the following assemblies
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc

[id="installation-user-infra-machines-advanced-customizing-live-{boot}-iscsi-ibft_{context}"]
= Customizing a live install {boot-media} for an iSCSI boot device with iBFT

[role="_abstract"]
You can set the iSCSI target and initiator values for automatic mounting, booting and configuration using a customized version of the live {op-system} image.

.Prerequisites
. You have an iSCSI target you want to install {op-system} on.
. Optional: You have multipathed your iSCSI target.

.Procedure

. Download the `coreos-installer` binary from the `coreos-installer` image mirror page.

. Retrieve the {op-system} ISO image from the {op-system} image mirror page and run the following command to customize the ISO image with the following information:
+
[source,text]
----
$ coreos-installer iso customize \
    --pre-install mount-iscsi.sh \
    --post-install unmount-iscsi.sh \
    --dest-device /dev/mapper/mpatha \
    --dest-ignition config.ign \
    --dest-karg-append rd.iscsi.firmware=1 \
    --dest-karg-append rd.multipath=default \
    -o custom.iso rhcos-<version>-live.x86_64.iso
----
+
where:
+
`mount-iscsi.sh`:: Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target and any commands enabling multipathing.
`unmount-iscsi.sh`:: Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.
`/dev/mapper/mpatha`:: Specifies the path to the device. If you are using multipath, the multipath device, `/dev/mapper/mpatha`, If there are multiple multipath devices connected, or to be explicit, you can use the World Wide Name (WWN) symlink available in `/dev/disk/by-path`.
`config.ign`:: Specifies the Ignition configuration for the destination system.
`rd.iscsi.firmware=1`::Specifies the iSCSI parameter is read from the BIOS firmware.
`rd.multipath=default`:: Specifies if you want to enable multipathing. Optional parameter.

. Retrieve the {op-system} `kernel`, `initramfs`, and `rootfs` files from the {op-system} image mirror page and run the following command to create a new customized `initramfs` file with the following information:
+
[source,text]
----
$ coreos-installer pxe customize \
    --pre-install mount-iscsi.sh \
    --post-install unmount-iscsi.sh \
    --dest-device /dev/mapper/mpatha \
    --dest-ignition config.ign \
    --dest-karg-append rd.iscsi.firmware=1 \
    --dest-karg-append rd.multipath=default \
    -o custom.img rhcos-<version>-live-initramfs.x86_64.img
----
+
where:
+
`mount-iscsi.sh`:: Specifies the script that gets run before installation. It should contain the `iscsiadm` commands for mounting the iSCSI target.
`unmount-iscsi.sh`:: Specifies the script that gets run after installation. It should contain the command `iscsiadm --mode node --logout=all`.
`/dev/mapper/mpatha`:: Specifies the path to the device. If you are using multipath, the multipath device, `/dev/mapper/mpatha`, If there are multiple multipath devices connected, or to be explicit, you can use the World Wide Name (WWN) symlink available in `/dev/disk/by-path`.
`config.ign`:: Specifies the Ignition configuration for the destination system.
`rd.iscsi.firmware=1`:: Specifies the iSCSI parameter is read from the BIOS firmware.
`rd.multipath=default`:: Specifies if you want to enable multipathing. Optional parameter.
+
For more information about see the `dracut.cmdline` manual page.

[role="_additional-resources"]
.Additional resources

* `dracut.cmdline` manual page

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="installation-user-infra-machines-routing-bonding_{context}"]
= Networking and bonding options for ISO installations
= Networking options for ISO installations

[role="_abstract"]
You can configure advanced options so that you can modify the {op-system-first} manual installation process. The subsequent sections show examples of networking options for an ISO installation.

If you install {op-system} from an ISO image, you can add kernel arguments manually when you boot the image to configure networking for a node. If no networking arguments are specified, DHCP is activated in the initramfs when {op-system} detects that networking is required to fetch the Ignition config file.

[IMPORTANT]
====
When adding networking arguments manually, you must also add the `rd.neednet=1` kernel argument to bring the network up in the initramfs.
====

The following information provides examples for configuring networking and bonding on your {op-system} nodes for ISO installations. The examples describe how to use the `ip=`, `nameserver=`, and `bond=` kernel arguments.

[NOTE]
====
Ordering is important when adding the kernel arguments: `ip=`, `nameserver=`, and then `bond=`.
====

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see `dracut.cmdline` manual page.

The following information provides examples for configuring networking on your {op-system} nodes for ISO installations. The examples describe how to use the `ip=` and `nameserver=` kernel arguments.

[NOTE]
====
Ordering is important when adding the kernel arguments: `ip=` and `nameserver=`.
====

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see the `dracut.cmdline` manual page.

[role="_additional-resources"]
.Additional resources

* `dracut.cmdline` manual page

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-dhcp-or-static-ip-addresses_{context}"]
= Configuring DHCP or static IP addresses

[role="_abstract"]
You can configure an IP address by using either DHCP or an individual static IP address. If you set a static IP, you must then identify the DNS server IP address on each node.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node's IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The hostname to `core0.example.com`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

.Procedure

. Enter a command like the following command to configure a static IP address:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
nameserver=4.4.4.41
----

. Enter a command like the following command to configure a DHCP IP address:
+
[source,terminal]
----
ip=enp1s0:dhcp
----
+
[NOTE]
====
When you use DHCP to configure IP addressing for the {op-system} machines, the machines also obtain the DNS server information through DHCP. For DHCP-based deployments, you can define the DNS server address that is used by the {op-system} nodes through your DHCP server configuration.
====

. If two or more network interfaces and only one interface exists, disable DHCP on a single interface. In the example, the `enp1s0` interface has a static networking configuration and DHCP is disabled for `enp2s0`, which is not used:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
ip=::::core0.example.com:enp2s0:none
----

. If you need to combine DHCP and static IP configurations on systems with multiple network interfaces, run the following example command:
+
[source,terminal]
----
ip=enp1s0:dhcp
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-ip-address-without-static-hostname_{context}"]
= Configuring an IP address without a static hostname

[role="_abstract"]
You can configure an IP address without assigning a static hostname. If a static hostname is not set by the user, the static hostname gets picked up and automatically set by a reverse DNS lookup.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node's IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

.Procedure

* To configure an IP address without a static hostname, enter a command like the following command:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0::enp1s0:none
nameserver=4.4.4.41
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="specifying-multiple-network-interfaces_{context}"]
= Specifying multiple network interfaces and DNS servers

[role="_abstract"]
You can specify multiple network interfaces by setting multiple `ip=` entries. You can provide multiple DNS servers by adding a `nameserver=` entry for each server,

.Procedure

* To specify multiple network interfaces for your interfaces, you can enter a command like the following command:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
ip=10.10.10.3::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
----

* To provide multiple DNS servers by adding a `nameserver=` entry for each server, enter a command like the following command:
+
[source,terminal]
----
nameserver=1.1.1.1
nameserver=8.8.8.8
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-default-gateway-route_{context}"]
= Configuring default gateway and route

[role="_abstract"]
As an optional task, you can configure routes to additional networks by setting an `rd.route=` value.

[NOTE]
====
When you configure one or multiple networks, one default gateway is required. If the additional network gateway is different from the primary network gateway, the default gateway must be the primary network gateway.
====

.Procedure

* To configure the default gateway, enter the following command:
+
[source,terminal]
----
ip=::10.10.10.254::::
----

* To configure the route for an additional network, enter the following command:
+
[source,terminal]
----
rd.route=20.20.20.0/24:20.20.20.254:enp2s0
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-vlans-individual-interfaces_{context}"]
= Configuring VLANs on individual interfaces

[role="_abstract"]
As an optional task, you can configure VLANs on individual interfaces by using the `vlan=` parameter.

.Procedure

* To configure a VLAN on a network interface and use a static IP address, run the following command:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0.100:none
vlan=enp2s0.100:enp2s0
----

* To configure a VLAN on a network interface and to use DHCP, run the following command:
+
[source,terminal]
----
ip=enp2s0.100:dhcp
vlan=enp2s0.100:enp2s0
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="bonding-multiple-network-interfaces-to-single-interface_{context}"]
= Bonding multiple network interfaces to a single interface

[role="_abstract"]
As an optional task, you can bond multiple network interfaces to a single interface by using the `bond=` option.

The following example demonstrates editing the `/etc/config/network` file and specifying the following syntax for bonding multiple network interfaces to a single interface:

[source,terminal]
----
bond=<name>[:<network_interfaces>][:<options>]
----
* `<name>`: Specifies the bonding device name, for example `bond0`.
* `<network_interfaces>`: Specifies a comma-separated list of physical (ethernet) interfaces, such as `em1,em2`.
* `<options>: Specifies a comma-separated list of bonding options. Enter the `modinfo bonding` command to see available options.

When you create a bonded interface using the `bond=` command, you must specify how the IP address is assigned and other information for the bonded interface.

.Procedure

* To configure the bonded interface to use DHCP, edit the `/etc/config/network` file by setting the IP address for the bond to `dhcp`. For example:
+
[source,terminal]
----
ip=bond0:dhcp
----

* To configure the bonded interface to use a static IP address, edit the `/etc/config/network` file entering the specific IP address you want and related information. For example:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
----
[source,terminal]
----
bond=bond0:em1,em2:mode=active-backup
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none::AA:BB:CC:DD:EE:FF ip=em1:none::AA:BB:CC:DD:EE:FF
ip=em2:none::AA:BB:CC:DD:EE:FF
----
+
{ibm-z-title} supports value `1` for the `fail_over_mac` parameter, so always set the `fail_over_mac=1` option in active-backup mode to avoid problems when shared OSA/RoCE cards are used.

* You can configure VLANs on bonded interfaces by editing the `/etc/config/network` file and specifying the `vlan=` parameter to use DHCP. For example:
+
[source,terminal]
----
ip=bond0.100:dhcp
bond=bond0:em1,em2:mode=active-backup
vlan=bond0.100:bond0
----

* To configure the bonded interface with a VLAN, edit the `/etc/config/network` file and specify a static IP address. For example:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0.100:none
bond=bond0:em1,em2:mode=active-backup
vlan=bond0.100:bond0
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="bonding-multiple-sriov-network-interfaces-to-dual-port_{context}"]
= Bonding multiple SR-IOV network interfaces to a dual port NIC interface
= Using network teaming

[role="_abstract"]
You can bond multiple SR-IOV network interfaces to a dual port NIC interface by using the `bond=` option. Ensure you apply the procedure tasks to each node.
You can use network teaming as an alternative to bonding by using the `team=` parameter.

.Procedure

. Create the SR-IOV virtual functions (VFs) following the guidance in Managing SR-IOV devices. Follow the procedure in the "Attaching SR-IOV networking devices to virtual machines" section.
. Create the SR-IOV virtual functions (VFs).

. Create the bond, attach the desired VFs to the bond and set the bond link state up following the guidance in Configuring network bonding. Follow any of the described procedures to create the bond.
+
The following examples illustrate the syntax you must use:
+
* The syntax for configuring a bonded interface is `bond=<name>[:<network_interfaces>][:options]`.
+
`<name>` is the bonding device name (`bond0`), `<network_interfaces>` represents the virtual functions (VFs) by their known name in the kernel and shown in the output of the `ip link` command(`eno1f0`, `eno2f0`), and _options_ is a comma-separated list of bonding options. Enter `modinfo bonding` to see available options.
+
* When you create a bonded interface using `bond=`, you must specify how the IP address is assigned and other information for the bonded interface.
+
** To configure the bonded interface to use DHCP, set the bond's IP address to `dhcp`. For example:
+
[source,terminal]
----
bond=bond0:eno1f0,eno2f0:mode=active-backup
ip=bond0:dhcp::AA:BB:CC:DD:EE:FF
ip=eno1f0:none::AA:BB:CC:DD:EE:FF
ip=eno2f0:none::AA:BB:CC:DD:EE:FF
----
+
** To configure the bonded interface to use a static IP address, enter the specific IP address you want and related information. For example:
+
[source,terminal]
----
bond=bond0:eno1f0,eno2f0:mode=active-backup
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
----

. Optional: You can use network teaming as an alternative to bonding by using the `team=` parameter.
+
* The syntax for configuring a team interface is: `team=name[:network_interfaces]`
+
_name_ is the team device name (`team0`) and _network_interfaces_ represents a comma-separated list of physical (ethernet) interfaces (`em1, em2`).
+
[NOTE]
====
Teaming is planned to be deprecated when {op-system} switches to an upcoming version of {op-system-base}. For more information, see this https://access.redhat.com/solutions/6509691[Red Hat Knowledgebase Article].
====
+
Use the following example to configure a network team:
+
[source,terminal]
----
team=team0:em1,em2
ip=team0:dhcp
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="installation-user-infra-machines-coreos-installer-options_{context}"]
= `coreos-installer` and boot options for ISO and PXE installations

[role="_abstract"]
You can install {op-system} by running `coreos-installer install <options> <device>` at the command prompt, after booting into the {op-system} live environment from an ISO image.

The following table shows the subcommands, options, and arguments you can pass to the `coreos-installer` command.

.`coreos-installer` subcommands, command-line options, and arguments
|===

2+|*coreos-installer install subcommand*

|*_Subcommand_* |*_Description_*

a|`$ coreos-installer install <options> <device>`
a|Embed an Ignition config in an ISO image.

2+|*coreos-installer install subcommand options*

|*_Option_* |*_Description_*

a| `-u`, `--image-url <url>`
a|Specify the image URL manually.

a| `-f`, `--image-file <path>`
a|Specify a local image file manually. Used for debugging.

a|`-i,` `--ignition-file <path>`
a|Embed an Ignition config from a file.

a|`-I`, `--ignition-url <URL>`
a|Embed an Ignition config from a URL.

a|`--ignition-hash <digest>`
a|Digest `type-value` of the Ignition config.

a|`-p`, `--platform <name>`
a|Override the Ignition platform ID for the installed system.

a|`--console <spec>`
a|Set the kernel and boot loader console for the installed system. For more information about the format of `<spec>`, see the Linux kernel serial console documentation.

a|`--append-karg <arg>...`
a|Append a default kernel argument to the installed system.

a|`--delete-karg <arg>...`
a|Delete a default kernel argument from the installed system.

a|`-n`, `--copy-network`
a|Copy the network configuration from the install environment.

[IMPORTANT]
====
The `--copy-network` option only copies networking configuration found under `/etc/NetworkManager/system-connections`. In particular, it does not copy the system hostname.
====

a|`--network-dir <path>`
a|For use with `-n`. Default is `/etc/NetworkManager/system-connections/`.

a|`--save-partlabel <lx>..`
a|Save partitions with this label glob.

a|`--save-partindex <id>...`
a|Save partitions with this number or range.

a|`--insecure`
a|Skip {op-system} image signature verification.

a|`--insecure-ignition`
a|Allow Ignition URL without HTTPS or hash.

a|`--architecture <name>`
a|Target CPU architecture. Valid values are `x86_64` and `aarch64`.

a|`--preserve-on-error`
a|Do not clear partition table on error.

a|`-h`, `--help`
a|Print help information.

2+|*coreos-installer install subcommand argument*

|*_Argument_* |*_Description_*

a|`<device>`
a|The destination device.

2+|*coreos-installer ISO subcommands*

|*_Subcommand_* |*_Description_*

a|`$ coreos-installer iso customize <options> <ISO_image>`
a|Customize a {op-system} live ISO image.

a|`coreos-installer iso reset <options> <ISO_image>`
|Restore a {op-system} live ISO image to default settings.

a|`coreos-installer iso ignition remove <options> <ISO_image>`
a|Remove the embedded Ignition config from an ISO image.

2+|*coreos-installer ISO customize subcommand options*

|*_Option_* |*_Description_*

a|`--dest-ignition <path>`
a|Merge the specified Ignition config file into a new configuration fragment for the destination system.

a|`--dest-console <spec>`
a|Specify the kernel and boot loader console for the destination system.

a|`--dest-device <path>`
a|Install and overwrite the specified destination device.

a|`--dest-karg-append <arg>`
a|Add a kernel argument to each boot of the destination system.

a|`--dest-karg-delete <arg>`
a|Delete a kernel argument from each boot of the destination system.

a|`--network-keyfile <path>`
a|Configure networking by using the specified NetworkManager keyfile for live and destination systems.

a|`--ignition-ca <path>`
a|Specify an additional TLS certificate authority to be trusted by Ignition.

a|`--pre-install <path>`
a|Run the specified script before installation.

a|`--post-install <path>`
a|Run the specified script after installation.

a|`--installer-config <path>`
a|Apply the specified installer configuration file.

a|`--live-ignition <path>`
a|Merge the specified Ignition config file into a new configuration fragment for the live environment.

a|`--live-karg-append <arg>`
a|Add a kernel argument to each boot of the live environment.

a|`--live-karg-delete <arg>`
a|Delete a kernel argument from each boot of the live environment.

a|`--live-karg-replace <k=o=n>`
a|Replace a kernel argument in each boot of the live environment, in the form `key=old=new`.

a|`-f`, `--force`
a|Overwrite an existing Ignition config.

a|`-o`, `--output <path>`
a|Write the ISO to a new output file.

a|`-h`, `--help`
a|Print help information.

2+|*coreos-installer PXE subcommands*

|*_Subcommand_* |*_Description_*

2+|Note that not all of these options are accepted by all subcommands.

a|`coreos-installer pxe customize <options> <path>`
a|Customize a {op-system} live PXE boot config.

a|`coreos-installer pxe ignition wrap <options>`
a|Wrap an Ignition config in an image.

a|`coreos-installer pxe ignition unwrap <options> <image_name>`
a|Show the wrapped Ignition config in an image.

2+|*coreos-installer PXE customize subcommand options*

|*_Option_* |*_Description_*

2+|Note that not all of these options are accepted by all subcommands.

a|`--dest-ignition <path>`
a|Merge the specified Ignition config file into a new configuration fragment for the destination system.

a|`--dest-console <spec>`
a|Specify the kernel and boot loader console for the destination system.

a|`--dest-device <path>`
a|Install and overwrite the specified destination device.

a|`--network-keyfile <path>`
a|Configure networking by using the specified NetworkManager keyfile for live and destination systems.

a|`--ignition-ca <path>`
a|Specify an additional TLS certificate authority to be trusted by Ignition.

a|`--pre-install <path>`
a|Run the specified script before installation.

a|`post-install <path>`
a|Run the specified script after installation.

a|`--installer-config <path>`
a|Apply the specified installer configuration file.

a|`--live-ignition <path>`
a|Merge the specified Ignition config file into a new configuration fragment for the live environment.

a|`-o,` `--output <path>`
a|Write the initramfs to a new output file.

[NOTE]
====
This option is required for PXE environments.
====

a|`-h`, `--help`
a|Print help information.

|===

You can automatically start `coreos-installer` options at boot time by passing `coreos.inst` boot arguments to the {op-system} live installer. These are provided in addition to the standard boot arguments.

* For ISO installations, the `coreos.inst` options can be added by interrupting the automatic boot at the boot loader menu. You can interrupt the automatic boot by pressing `TAB` while the *RHEL CoreOS (Live)* menu option is highlighted.

* For PXE or iPXE installations, the `coreos.inst` options must be added to the `APPEND` line before the {op-system} live installer is booted.

The following table shows the {op-system} live installer `coreos.inst` boot options for ISO and PXE installations.

.`coreos.inst` boot options
|===
|Argument |Description

a|`coreos.inst.install_dev`

a|Required. The block device on the system to install to.

[NOTE]
====
It is recommended to use the full path, such as `/dev/sda`, although `sda` is allowed.
====

a|`coreos.inst.ignition_url`

a|Optional: The URL of the Ignition config to embed into the installed system. If no URL is specified, no Ignition config is embedded. Only HTTP and HTTPS protocols are supported.

a|`coreos.inst.save_partlabel`

a|Optional: Comma-separated labels of partitions to preserve during the install. Glob-style wildcards are permitted. The specified partitions do not need to exist.

a|`coreos.inst.save_partindex`

a|Optional: Comma-separated indexes of partitions to preserve during the install. Ranges `m-n` are permitted, and either `m` or `n` can be omitted. The specified partitions do not need to exist.

a|`coreos.inst.insecure`

a|Optional: Permits the OS image that is specified by `coreos.inst.image_url` to be unsigned.

a|`coreos.inst.image_url`

a|Optional: Download and install the specified {op-system} image.

* This argument should not be used in production environments and is intended for debugging purposes only.

* While this argument can be used to install a version of {op-system} that does not match the live media, it is recommended that you instead use the media that matches the version you want to install.

* If you are using `coreos.inst.image_url`, you must also use `coreos.inst.insecure`. This is because the bare-metal media are not GPG-signed for OpenShift Container Platform.

* Only HTTP and HTTPS protocols are supported.

a|`coreos.inst.skip_reboot`

a|Optional: The system will not reboot after installing. After the install finishes, you will receive a prompt that allows you to inspect what is happening during installation. This argument should not be used in production environments and is intended for debugging purposes only.

a|`coreos.inst.platform_id`

a| Optional: The Ignition platform ID of the platform the {op-system} image is being installed on. Default is `metal`. This option determines whether or not to request an Ignition config from the cloud provider, such as VMware. For example: `coreos.inst.platform_id=vmware`.

a|`ignition.config.url`

a|Optional: The URL of the Ignition config for the live boot. For example, this can be used to customize how `coreos-installer` is invoked, or to run code before or after the installation. This is different from `coreos.inst.ignition_url`, which is the Ignition config for the installed system.
|===

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc

[id="rhcos-enabling-multipath_{context}"]
= Enabling multipathing with kernel arguments on {op-system}

[role="_abstract"]
{op-system} supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability.

You can enable multipathing at installation time for nodes that were provisioned in OpenShift Container Platform 4.8 or later. While postinstallation support is available by activating multipathing through the machine config, Red{nbsp}Hat recommends enabling multipathing during installation.

In setups where any I/O to non-optimized paths results in I/O system errors, you must enable multipathing at installation time.

[IMPORTANT]
====
On {ibm-z-name} and {ibm-linuxone-name}, you can enable multipathing only if you configured your cluster for it during installation. For more information, see "Installing {op-system} and starting the OpenShift Container Platform bootstrap process" in _Installing a cluster with z/VM on {ibm-z-name} and {ibm-linuxone-name}_.
====

The following procedure enables multipath at installation time and appends kernel arguments to the `coreos-installer install` command so that the installed system itself will use multipath beginning from the first boot.

[NOTE]
====
OpenShift Container Platform does not support enabling multipathing as a day-2 activity on nodes that have been upgraded from 4.6 or earlier.
====

.Prerequisites

* You have created the Ignition config files for your cluster.

* You have reviewed _Installing {op-system} and starting the OpenShift Container Platform bootstrap process_.

.Procedure

. To enable multipath and start the `multipathd` daemon, run the following command on the installation host:
+
[source,terminal]
----
$ mpathconf --enable && systemctl start multipathd.service
----
+
.. Optional: If booting the PXE or ISO, you can instead enable multipath by adding `rd.multipath=default` from the kernel command line.

. Append the kernel arguments by invoking the `coreos-installer` program:
+
* If there is only one multipath device connected to the machine, the device should be available at path `/dev/mapper/mpatha`. For example:
+
[source,terminal]
----
$ coreos-installer install /dev/mapper/mpatha \
--ignition-url=http://host/worker.ign \
--append-karg rd.multipath=default \
--append-karg root=/dev/disk/by-label/dm-mpath-root \
--append-karg rw
----
[source,terminal]
----
$ coreos-installer install /dev/mapper/mpatha \
--ignition-url=http://host/worker.ign \
--append-karg rd.multipath=default \
--append-karg root=/dev/disk/by-label/dm-mpath-root \
--append-karg rw \
--offline
----
+
--
* `/dev/mapper/mpatha`: Indicates the path of the single multipathed device.
--
+
* If there are multiple multipath devices connected to the machine, instead of using `/dev/mapper/mpatha`, Red{nbsp}Hat recommends using the World Wide Name (WWN) symlink. The symlink is available in `/dev/disk/by-id`. For example:
+
[source,terminal]
----
$ coreos-installer install /dev/disk/by-id/wwn-<wwn_ID> \
--ignition-url=http://host/worker.ign \
--append-karg rd.multipath=default \
--append-karg root=/dev/disk/by-label/dm-mpath-root \
--append-karg rw
----
[source,terminal]
----
$ coreos-installer install /dev/disk/by-id/wwn-<wwn_ID> \
--ignition-url=http://host/worker.ign \
--append-karg rd.multipath=default \
--append-karg root=/dev/disk/by-label/dm-mpath-root \
--append-karg rw \
--offline
----
+
where:
+
* `<wwn_ID>`:: Indicates the WWN ID of the target multipathed device. For example, `0xx194e957fcedb4841`.
+
This symlink can also be used as the `coreos.inst.install_dev` kernel argument when using special `coreos.inst.*` arguments to direct the live installer. For more information, see "Installing {op-system} and starting the OpenShift Container Platform bootstrap process".

. Reboot into the installed system.

. Check that the kernel arguments worked by going to one of the worker nodes and listing the kernel command-line arguments (in `/proc/cmdline` on the host):
+
[source,terminal]
----
$ oc debug node/ip-10-0-141-105.ec2.internal
----
+
.Example output
[source,terminal]
----
Starting pod/ip-10-0-141-105ec2internal-debug ...
To use host binaries, run `chroot /host`

sh-4.2# cat /host/proc/cmdline
...
rd.multipath=default root=/dev/disk/by-label/dm-mpath-root
...

sh-4.2# exit
----
+
You should see the added kernel arguments.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc

[id="rhcos-multipath-secondary-disk_{context}"]
= Enabling multipathing on secondary disks

[role="_abstract"]
{op-system} also supports multipathing on a secondary disk. Instead of kernel arguments, you use Ignition to enable multipathing for the secondary disk at installation time.

.Prerequisites

* You have read the section _Disk partitioning_.
* You have read _Enabling multipathing with kernel arguments on {op-system}_.
* You have installed the Butane utility.

.Procedure

. Create a Butane config with information similar to the following:
+
.Example `multipath-config.bu`
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
systemd:
  units:
    - name: mpath-configure.service
      enabled: true
      contents: |
        [Unit]
        Description=Configure Multipath on Secondary Disk
        ConditionFirstBoot=true
        ConditionPathExists=!/etc/multipath.conf
        Before=multipathd.service
        DefaultDependencies=no

        [Service]
        Type=oneshot
        ExecStart=/usr/sbin/mpathconf --enable

        [Install]
        WantedBy=multi-user.target
    - name: mpath-var-lib-container.service
      enabled: true
      contents: |
        [Unit]
        Description=Set Up Multipath On /var/lib/containers
        ConditionFirstBoot=true
        Requires=dev-mapper-mpatha.device
        After=dev-mapper-mpatha.device
        After=ostree-remount.service
        Before=kubelet.service
        DefaultDependencies=no

        [Service]
        Type=oneshot
        ExecStart=/usr/sbin/mkfs.xfs -L containers -m reflink=1 /dev/mapper/mpatha
        ExecStart=/usr/bin/mkdir -p /var/lib/containers

        [Install]
        WantedBy=multi-user.target
    - name: var-lib-containers.mount
      enabled: true
      contents: |
        [Unit]
        Description=Mount /var/lib/containers
        After=mpath-var-lib-containers.service
        Before=kubelet.service

        [Mount]
        What=/dev/disk/by-label/dm-mpath-containers
        Where=/var/lib/containers
        Type=xfs

        [Install]
        WantedBy=multi-user.target
----
+
where:
+
`Before=multipathd.service`:: Specifies that the configuration must be set before launching the multipath daemon.
`ExecStart=/usr/sbin/mpathconf`:: Specifies starting the `mpathconf` utility.
`ConditionFirstBoot=true`:: Set to the value `true`.
`[Service]`:: Specifies the creation of the filesystem and directory `/var/lib/containers`.
`Before=kubelet.service`:: Specifies that the device must be mounted before starting any nodes.
`[Mount]`:: Specifies to mount the device to the `/var/lib/containers` mount point. This location cannot be a symlink.

. Create the Ignition configuration by running the following command:
+
[source,terminal]
----
$ butane --pretty --strict multipath-config.bu > multipath-config.ign
----

. Continue with the rest of the first boot {op-system} installation process.
+
[IMPORTANT]
====
Do not add the `rd.multipath` or `root` kernel arguments on the CLI during installation unless the primary disk is also multipathed.
====

//iscsi using `coreos-installer install`
// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc

[id="rhcos-install-iscsi-manual_{context}"]
= Installing {op-system} manually on an iSCSI boot device

[role="_abstract"]
You can manually install {op-system} on an iSCSI target.

.Prerequisites
. You are in the {op-system} live environment.
. You have an iSCSI target that you want to install {op-system} on.

.Procedure

. Mount the iSCSI target from the live environment by running the following command:
+
[source,text]
----
$ iscsiadm \
    --mode discovery \
    --type sendtargets
    --portal <IP_address> \
    --login
----
+
where:
+
`<IP_address>`:: Specifies the IP address of the target portal.

. Install {op-system} onto the iSCSI target by running the following command and using the necessary kernel arguments, for example:
+
[source,text]
----
$ coreos-installer install \
/dev/disk/by-path/ip-<IP_address>:<port>-iscsi-<target_iqn>-lun-<lun> \
--append-karg rd.iscsi.initiator=<initiator_iqn> \
--append.karg netroot=<target_iqn> \
--console ttyS0,115200n8
--ignition-file <path_to_file>
$ coreos-installer install \
/dev/disk/by-path/ip-<IP_address>:<port>-iscsi-<target_iqn>-lun-<lun> \
--append-karg rd.iscsi.initiator=<initiator_iqn> \
--append.karg netroot=<target_iqn> \
--console ttyS0,115200n8 \
--ignition-file <path_to_file> \
--offline
----
+
where:
+
`/dev/disk/by-path/ip`:: Specifies the installation location. You must provide the IP address of the target portal, the associated port number, the target iSCSI node in IQN format, and the iSCSI logical unit number (LUN).
`<initiator_iqn>`:: Specifies the iSCSI initiator, or client, name in IQN format. The initiator forms a session to connect to the iSCSI target.
`<target_iqn>`:: Specifies the iSCSI target, or server, name in IQN format.
+
For more information about the iSCSI options supported by `dracut`, see the `dracut.cmdline` manual page.

. Unmount the iSCSI disk with the following command:
+
[source,text]
----
$ iscsiadm --mode node --logoutall=all
----
+
This procedure can also be performed using the `coreos-installer iso customize` or `coreos-installer pxe customize` subcommands.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc

[id="rhcos-install-iscsi-ibft_{context}"]
= Installing {op-system} on an iSCSI boot device using iBFT

[role="_abstract"]
On a completely diskless machine, the iSCSI target and initiator values can be passed through iBFT. iSCSI multipathing is also supported.

.Prerequisites

. You are in the {op-system} live environment.
. You have an iSCSI target you want to install {op-system} on.
. Optional: You have configured multipathing for your iSCSI target.

.Procedure

. Mount the iSCSI target from the live environment by running the following command:
+
[source,text]
----
$ iscsiadm \
    --mode discovery \
    --type sendtargets
    --portal <IP_address> \
    --login
----
+
where:
+
`<IP_address>`:: Specifies the IP address of the target portal.

. Optional: enable multipathing and start the daemon with the following command:
+
[source,text]
----
$ mpathconf --enable && systemctl start multipathd.service
----

. Install {op-system} onto the iSCSI target by running the following command and using the necessary kernel arguments, for example:
+
[source,text]
----
$ coreos-installer install \
    /dev/mapper/mpatha \
    --append-karg rd.iscsi.firmware=1 \
    --append-karg rd.multipath=default \
    --console ttyS0 \
    --ignition-file <path_to_file>
$ coreos-installer install \
    /dev/mapper/mpatha \
    --append-karg rd.iscsi.firmware=1 \
    --append-karg rd.multipath=default \
    --console ttyS0 \
    --ignition-file <path_to_file> \
    --offline
----
+
where:
+
`/dev/mapper/mpatha`:: Specifies the path of a single multipathed device. If there are multiple multipath devices connected, or to be explicit, you can use the World Wide Name (WWN) symlink available in `/dev/disk/by-path`.
`rd.iscsi.firmware=1`:: Specifies that the iSCSI parameter is read from the BIOS firmware.
`rd.multipath=default`:: Specifies to enable multipathing. Optional parameter.
+
For more information about the iSCSI options supported by `dracut`, see the `dracut.cmdline` manual page.

. Unmount the iSCSI disk:
+
[source,text]
----
$ iscsiadm --mode node --logout=all
----
+
You can also perform this procedure by using the `coreos-installer iso customize` or `coreos-installer pxe customize` subcommands.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-installing-bare-metal_{context}"]
= Waiting for the bootstrap process to complete

[role="_abstract"]
The OpenShift Container Platform bootstrap process begins after the cluster nodes first boot into the persistent {op-system} environment that has been installed to disk. The configuration information provided through the Ignition config files is used to initialize the bootstrap process and install OpenShift Container Platform on the machines. You must wait for the bootstrap process to complete.

.Prerequisites

* You have created the Ignition config files for your cluster.
* You have configured suitable network, DNS, and load balancing infrastructure.
* You have obtained the installation program and generated the Ignition config files for your cluster.
* You installed {op-system} on your cluster machines and provided the Ignition config files that the OpenShift Container Platform installation program generated.
* Your machines have direct internet access or have an HTTP or HTTPS proxy available.

.Procedure

. Monitor the bootstrap process:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> wait-for bootstrap-complete \
    --log-level=info
----
+
where:
+
`<installation_directory>`:: Specifies the path to the directory that stores the installation files.
`--log-level=info`:: Specifies `warn`, `debug`, or `error` instead of `info` to view different installation details.
+
.Example output
[source,terminal]
----
INFO Waiting up to 30m0s for the Kubernetes API at https://api.test.example.com:6443...
INFO API v1.35.4 up
INFO Waiting up to 30m0s for bootstrapping to complete...
INFO It is now safe to remove the bootstrap resources
----
+
The command succeeds when the Kubernetes API server signals that it has been
bootstrapped on the control plane machines.

. After the bootstrap process is complete, remove the bootstrap machine from the
load balancer.
+
[IMPORTANT]
====
You must remove the bootstrap machine from the load balancer at this point. You
can also remove or reformat the bootstrap machine itself.
====

[role="_additional-resources"]
.Additional resources

* See Monitoring installation progress for more information about monitoring the installation logs and retrieving diagnostic data if installation issues arise.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp_user_infra/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="cli-logging-in-kubeadmin_{context}"]
= Logging in to the cluster by using the CLI

[role="_abstract"]
To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and is created during OpenShift Container Platform installation.

.Prerequisites
* You deployed an OpenShift Container Platform cluster.
* You installed the {oc-first}.
* Ensure the bootstrap process completed successfully.

.Procedure

. Export the `kubeadmin` credentials by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
----
+
where:
+
`<installation_directory>`:: Specifies the path to the directory that stores the installation files.

. Verify you can run `oc` commands successfully using the exported configuration by running the following command:
+
[source,terminal]
----
$ oc whoami
----
+
.Example output
[source,terminal]
----
system:admin
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-restricted-networks.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * machine_management/adding-rhel-compute.adoc
// * machine_management/more-rhel-compute.adoc
// * machine_management/user_provisioned/adding-aws-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-bare-metal-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-vsphere-compute-user-infra.adoc
// * post_installation_configuration/node-tasks.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-power.adoc

[id="installation-approve-csrs_{context}"]
= Approving the certificate signing requests for your machines

[role="_abstract"]
When you add machines to a cluster, two pending certificate signing requests (CSRs) are generated for each machine that you added. You must confirm that these CSRs are approved or, if necessary, approve them yourself. The client requests must be approved first, followed by the server requests.

.Prerequisites

* You added machines to your cluster.

.Procedure

. Confirm that the cluster recognizes the machines:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  63m  v1.35.4
master-1  Ready     master  63m  v1.35.4
master-2  Ready     master  64m  v1.35.4
----
+
The output lists all of the machines that you created.
+
[NOTE]
====
The preceding output might not include the compute nodes, also known as worker nodes, until some CSRs are approved.
====

. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
...
----
+
In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
[source,terminal]
----
$ oc get csr
----
+
[source,terminal]
.Example output
----
NAME        AGE   REQUESTOR                                   CONDITION
csr-mddf5   20m   system:node:master-01.example.com   Approved,Issued
csr-z5rln   16m   system:node:worker-21.example.com   Approved,Issued
----

. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:
+
[NOTE]
====
You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates will rotate, and more than two certificates will be present for each node. You must approve all of these certificates. After the client CSR is approved, the Kubelet creates a secondary CSR for the serving certificate, which requires manual approval. Then, subsequent serving certificate renewal requests are automatically approved by the `machine-approver` if the Kubelet requests a new certificate with identical parameters.
====
+
[NOTE]
====
For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If a request is not approved, then the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because a serving certificate is required when the API server connects to the kubelet. Any operation that contacts the Kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the CSR was submitted by the `node-bootstrapper` service account in the `system:node` or `system:admin` groups, and confirm the identity of the node.
====
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
----
+
[NOTE]
====
Some Operators might not become available until some CSRs are approved.
Each node submits two CSRs, so you may need to run the command to approve CSRs multiple times.
====

. Now that your client requests are approved, you must review the server requests for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
...
----

. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
----

. After all client and server CSRs have been approved, the machines have the `Ready` status. Verify this by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
[source,terminal]
----
$ oc get nodes -o wide
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  73m  v1.35.4
master-1  Ready     master  73m  v1.35.4
master-2  Ready     master  74m  v1.35.4
worker-0  Ready     worker  11m  v1.35.4
worker-1  Ready     worker  11m  v1.35.4
----
.Example output
[source,terminal]
----
NAME               STATUS   ROLES                  AGE   VERSION   INTERNAL-IP      EXTERNAL-IP   OS-IMAGE                                                       KERNEL-VERSION                  CONTAINER-RUNTIME
worker-0-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.21   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.20   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-0-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.38      10.248.0.38   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-1-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.39      10.248.0.39   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-2-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.40      10.248.0.40   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-0-x86       Ready    worker                 75d   v1.35.4   10.248.0.43      10.248.0.43   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-x86       Ready    worker                 75d   v1.35.4   10.248.0.44      10.248.0.44   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
----
+
[NOTE]
====
It can take a few minutes after approval of the server CSRs for the machines to transition to the `Ready` status.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-operators-config_{context}"]
= Initial Operator configuration

[role="_abstract"]
After the control plane initializes, you must immediately configure some Operators so that they all become available.

.Prerequisites

* Your control plane has initialized.

.Procedure

. Watch the cluster components come online:
+
[source,terminal]
----
$ watch -n5 oc get clusteroperators
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             .0    True        False         False      19m
baremetal                                  .0    True        False         False      37m
cloud-credential                           .0    True        False         False      40m
cluster-autoscaler                         .0    True        False         False      37m
config-operator                            .0    True        False         False      38m
console                                    .0    True        False         False      26m
csi-snapshot-controller                    .0    True        False         False      37m
dns                                        .0    True        False         False      37m
etcd                                       .0    True        False         False      36m
image-registry                             .0    True        False         False      31m
ingress                                    .0    True        False         False      30m
insights                                   .0    True        False         False      31m
kube-apiserver                             .0    True        False         False      26m
kube-controller-manager                    .0    True        False         False      36m
kube-scheduler                             .0    True        False         False      36m
kube-storage-version-migrator              .0    True        False         False      37m
machine-api                                .0    True        False         False      29m
machine-approver                           .0    True        False         False      37m
machine-config                             .0    True        False         False      36m
marketplace                                .0    True        False         False      37m
monitoring                                 .0    True        False         False      29m
network                                    .0    True        False         False      38m
node-tuning                                .0    True        False         False      37m
openshift-apiserver                        .0    True        False         False      32m
openshift-controller-manager               .0    True        False         False      30m
openshift-samples                          .0    True        False         False      32m
operator-lifecycle-manager                 .0    True        False         False      37m
operator-lifecycle-manager-catalog         .0    True        False         False      37m
operator-lifecycle-manager-packageserver   .0    True        False         False      32m
service-ca                                 .0    True        False         False      38m
storage                                    .0    True        False         False      37m
----

. Configure the Operators that are not available.

[role="_additional-resources"]
.Additional resources

* See Gathering logs from a failed installation for details about gathering data in the event of a failed OpenShift Container Platform installation.
* See Troubleshooting Operator issues for steps to check Operator pod health across the cluster and gather Operator logs for diagnosis.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * operators/admin/olm-restricted-networks.adoc
// * operators/admin/olm-managing-custom-catalogs.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="olm-restricted-networks-operatorhub_{context}"]
= Disabling the default software catalog sources

Operator catalogs that source content provided by Red Hat and community projects are configured for the software catalog by default during an OpenShift Container Platform installation.
In a restricted network environment, you must disable the default catalogs as a cluster administrator.
You can then configure the OperatorHub custom resource definition (CRD) to use local catalog sources for the software catalog.
As a cluster administrator, you can disable the set of default catalogs.

.Procedure

* Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:
+
[source,terminal]
----
$ oc patch OperatorHub cluster --type json \
    -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
----

[TIP]
====
Alternatively, you can use the web console to manage catalog sources. From the *Administration* -> *Cluster Settings* -> *Configuration* -> *OperatorHub* page, click the *Sources* tab, where you can create, update, delete, disable, and enable individual sources.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="installation-registry-storage-config_{context}"]
= Image registry storage configuration

[role="_abstract"]
Amazon Web Services provides default storage, which means the Image Registry Operator is available after installation. However, if the Registry Operator cannot create an S3 bucket and automatically configure storage, you must manually configure registry storage.
[role="_abstract"]
The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="registry-change-management-state_{context}"]
= Changing the image registry's management state

[role="_abstract"]
To start the image registry, you must change the Image Registry Operator configuration's `managementState` from `Removed` to `Managed`.

.Procedure

* Change `managementState` Image Registry Operator configuration from `Removed` to `Managed`. For example:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"managementState":"Managed"}}'
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="registry-configuring-storage-baremetal_{context}"]
= Configuring registry storage for bare metal and other manual installations

= Configuring registry storage for {ibm-z-title}

= Configuring registry storage for {ibm-power-title}

[role="_abstract"]
As a cluster administrator, following installation you must configure your registry to use storage.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have a cluster
* You have provisioned persistent storage for your cluster, such as {rh-storage-first}.
+
[IMPORTANT]
====
OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.
====
+
* You must have a system with at least 100Gi capacity.

.Procedure

. To configure your registry to use storage, change the `spec.storage.pvc` in
the `configs.imageregistry/cluster` resource.
+
[NOTE]
====
When you use shared storage, review your security settings to prevent outside access.
====

. Verify that you do not have a registry pod:
+
[source,terminal]
----
$ oc get pod -n openshift-image-registry -l docker-registry=default
----
+
.Example output
[source,terminal]
----
No resources found in openshift-image-registry namespace
----
+
[NOTE]
=====
If you do have a registry pod in your output, you do not need to continue with this procedure.
=====
. Check the registry configuration:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io
----
+
.Example output
[source,yaml]
----
storage:
  pvc:
    claim:
----
+
Leave the `claim` field blank to allow the automatic creation of an
`image-registry-storage` PVC.
+
. Check the `clusteroperator` status:
+
[source,terminal]
----
$ oc get clusteroperator image-registry
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME             VERSION              AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
image-registry                    True        False         False      6h50m
----
+
. Ensure that your registry is set to managed to enable building and pushing of images.
+
* Run:
+
----
$ oc edit configs.imageregistry/cluster
----
+
Then, change the line
+
----
managementState: Removed
----
+
to
+
----
managementState: Managed
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-registry-storage-non-production_{context}"]
= Configuring storage for the image registry in non-production clusters

[role="_abstract"]
You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory. If you do so, all images are lost if you restart the registry.

.Procedure

* To set the image registry storage to an empty directory:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
----
+
[WARNING]
====
Configure this option only for non-production clusters.
====
+
If you run this command before the Image Registry Operator initializes its
components, the `oc patch` command fails with the following error:
+
[source,terminal]
----
Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
----
+
Wait a few minutes and run the command again.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_baremetal/installing-bare-metal-network-customizations.adoc
// * installing/installing_baremetal/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc

[id="installation-registry-storage-block-recreate-rollout-bare-metal_{context}"]
= Configuring block registry storage for bare metal

[role="_abstract"]
To allow the image registry to use block storage types during upgrades as a cluster administrator, you can use the `Recreate` rollout strategy.

[IMPORTANT]
====
Block storage volumes, or block persistent volumes, are supported but not recommended for use with the image registry on production clusters. An installation where the registry is configured on block storage is not highly available because the registry cannot have more than one replica.

If you choose to use a block storage volume with the image registry, you must use a filesystem persistent volume claim (PVC).
====

.Procedure

. Enter the following command to set the image registry storage as a block storage type, patch the registry so that it uses the `Recreate` rollout strategy, and runs with only one (`1`) replica:
+
[source,terminal]
----
$ oc patch config.imageregistry.operator.openshift.io/cluster --type=merge -p '{"spec":{"rolloutStrategy":"Recreate","replicas":1}}'
----

. Provision the PV for the block storage device, and create a PVC for that volume. The requested block volume uses the ReadWriteOnce (RWO) access mode.
.. Create a `pvc.yaml` file with the following contents to define a VMware vSphere `PersistentVolumeClaim` object:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: image-registry-storage
  namespace: openshift-image-registry
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
----
+
where:
+
--
`metadata.name`:: Specifies a unique name that represents the `PersistentVolumeClaim` object.
`metadata.namespace`:: Specifies the `namespace` for the `PersistentVolumeClaim` object, which is `openshift-image-registry`.
`spec.accessModes`:: Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.
`spec.resources.requests.storage`:: The size of the persistent volume claim.
--

.. Enter the following command to create the `PersistentVolumeClaim` object from the file:
+
[source,terminal]
----
$ oc create -f pvc.yaml -n openshift-image-registry
----

+
. Enter the following command to edit the registry configuration so that it references the correct PVC:
+
[source,terminal]
----
$ oc edit config.imageregistry.operator.openshift.io -o yaml
----
+
.Example output
[source,yaml]
----
storage:
  pvc:
    claim:
----
+
By creating a custom PVC, you can leave the `claim` field blank for the default automatic creation of an `image-registry-storage` PVC.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-complete-user-infra_{context}"]
= Completing installation on user-provisioned infrastructure

[role="_abstract"]
To finalize the installation on user-provisioned infrastructure, complete the cluster deployment after configuring the Operators. This ensures the cluster is fully operational on the infrastructure that you provide.

.Prerequisites

* Your control plane has initialized.
* You have completed the initial Operator configuration.

.Procedure

. Confirm that all the cluster components are online with the following command:
+
[source,terminal]
----
$ watch -n5 oc get clusteroperators
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             .0    True        False         False      19m
baremetal                                  .0    True        False         False      37m
cloud-credential                           .0    True        False         False      40m
cluster-autoscaler                         .0    True        False         False      37m
config-operator                            .0    True        False         False      38m
console                                    .0    True        False         False      26m
csi-snapshot-controller                    .0    True        False         False      37m
dns                                        .0    True        False         False      37m
etcd                                       .0    True        False         False      36m
image-registry                             .0    True        False         False      31m
ingress                                    .0    True        False         False      30m
insights                                   .0    True        False         False      31m
kube-apiserver                             .0    True        False         False      26m
kube-controller-manager                    .0    True        False         False      36m
kube-scheduler                             .0    True        False         False      36m
kube-storage-version-migrator              .0    True        False         False      37m
machine-api                                .0    True        False         False      29m
machine-approver                           .0    True        False         False      37m
machine-config                             .0    True        False         False      36m
marketplace                                .0    True        False         False      37muser
monitoring                                 .0    True        False         False      29m
network                                    .0    True        False         False      38m
node-tuning                                .0    True        False         False      37m
openshift-apiserver                        .0    True        False         False      32muser
openshift-controller-manager               .0    True        False         False      30m
openshift-samples                          .0    True        False         False      32m
operator-lifecycle-manager                 .0    True        False         False      37m
operator-lifecycle-manager-catalog         .0    True        False         False      37m
operator-lifecycle-manager-packageserver   .0    True        False         False      32m
service-ca                                 .0    True        False         False      38m
storage                                    .0    True        False         False      37m
----
+
Alternatively, the following command notifies you when all of the clusters are available. The command also retrieves and displays credentials:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> wait-for install-complete
----
+
where:
+
`<installation_directory>`:: Specifies the path to the directory that you
stored the installation files in.
+
.Example output
[source,terminal]
----
INFO Waiting up to 30m0s for the cluster to initialize...
----
+
The command succeeds when the Cluster Version Operator finishes deploying the
OpenShift Container Platform cluster from Kubernetes API server.
+
[IMPORTANT]
====
* The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

. Confirm that the Kubernetes API server is communicating with the pods.
+
.. To view a list of all pods, use the following command:
+
[source,terminal]
----
$ oc get pods --all-namespaces
----
+
.Example output
[source,terminal]
----
NAMESPACE                         NAME                                            READY   STATUS      RESTARTS   AGE
openshift-apiserver-operator      openshift-apiserver-operator-85cb746d55-zqhs8   1/1     Running     1          9m
openshift-apiserver               apiserver-67b9g                                 1/1     Running     0          3m
openshift-apiserver               apiserver-ljcmx                                 1/1     Running     0          1m
openshift-apiserver               apiserver-z25h4                                 1/1     Running     0          2m
openshift-authentication-operator authentication-operator-69d5d8bf84-vh2n8        1/1     Running     0          5m
----
+
.. View the logs for a pod that is listed in the output of the previous command by using the following command:
+
[source,terminal]
----
$ oc logs <pod_name> -n <namespace>
----
+
where:
+
`<namespace>`:: Specifies the pod name and namespace, as shown in the output of an earlier command.
+
If the pod logs display, the Kubernetes API server can communicate with the cluster machines.

. For an installation with Fibre Channel Protocol (FCP), additional steps are required to enable multipathing. Do not enable multipathing during installation.
. Additional steps are required to enable multipathing. Do not enable multipathing during installation.
+
See "Enabling multipathing with kernel arguments on {op-system}" in the _Postinstallation machine configuration tasks_ documentation for more information.

. Register your cluster on the Cluster registration page.

.Verification

If you have enabled secure boot during the OpenShift Container Platform bootstrap process, the following verification steps are required:

. Debug the node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----
+
.Example output
[source,terminal]
----
chroot /host
----

. Confirm that secure boot is enabled by running the following command. Example output states `1` if secure boot is enabled and `0` if secure boot is not enabled.
+
[source,terminal]
----
$ cat /sys/firmware/ipl/secure
----

. List the re-IPL configuration by running the following command:
+
[source,terminal]
----
# lsreipl
----
+
.Example output for an FCP disk
[source,terminal,subs="attributes+"]
----
Re-IPL type: fcp
WWPN: 0x500507630400d1e3
LUN: 0x4001400e00000000
Device: 0.0.810e
bootprog: 0
br_lba: 0
Loadparm: ""
Bootparms: ""
clear: 0
----
+
.Example output for a DASD disk
[source,terminal,subs="attributes+"]
----
for DASD output:
Re-IPL type: ccw
Device: 0.0.525d
Loadparm: ""
clear: 0
----

. Shut down the node by running the following command:
+
[source,terminal]
----
sudo shutdown -h
----

. Initiate a boot from LPAR from the Hardware Management Console (HMC). See Initiating a secure boot from an LPAR in IBM documentation.

. When the node is back, check the secure boot status again.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_openstack/installing-openstack-user-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="cluster-telemetry_{context}"]
= Telemetry access for OpenShift Container Platform

[role="_abstract"]
To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to {cluster-manager-url}.

After you confirm that your {cluster-manager-url} inventory is correct, either maintained automatically by Telemetry or manually by using {cluster-manager},use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat's subscription services" in the _Additional resources_ section.

[role="_additional-resources"]
.Additional resources

* See About remote health monitoring for more information about the Telemetry service

== Next steps

* Validating an installation.
* Customize your cluster.
* Configure image streams for the Cluster Samples Operator and the `must-gather` tool.
* Learn how to use Operator Lifecycle Manager in disconnected environments.
* If the mirror registry that you used to install your cluster has a trusted CA, add it to the cluster by configuring additional trust stores.
* If necessary, you can
Remote health reporting.
* If necessary, see Registering your disconnected cluster
