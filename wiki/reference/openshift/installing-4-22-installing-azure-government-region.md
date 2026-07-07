---
title: "Installing a cluster on Azure into a government region"
type: reference
domain: openshift
slug: installing-4-22-installing-azure-government-region
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-azure-government-region
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on Azure into a government region

[id="installing-azure-government-region"]
= Installing a cluster on Azure into a government region

In OpenShift Container Platform version , you can install a cluster on
Microsoft Azure into a government region. To configure the government region,
you modify parameters in the `install-config.yaml` file before you install the
cluster.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-government-region.adoc

[id="installation-azure-about-government-region_{context}"]
= Azure government regions

OpenShift Container Platform supports deploying a cluster to
Microsoft Azure Government (MAG)
regions. MAG is specifically designed for US government agencies at the federal,
state, and local level, as well as contractors, educational institutions, and
other US customers that must run sensitive workloads on Azure. MAG is composed
of government-only data center regions, all granted an
Impact Level 5 Provisional Authorization.

Installing to a MAG region requires manually configuring the Azure Government
dedicated cloud instance and region in the `install-config.yaml` file. You must
also update your service principal to reference the appropriate government
environment.

[NOTE]
====
The Azure government region cannot be selected using the guided terminal prompts
from the installation program. You must define the region manually in the
`install-config.yaml` file. Remember to also set the dedicated cloud instance,
like `AzureUSGovernmentCloud`, based on the region specified.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc

[id="private-clusters-default_{context}"]
= Private clusters

You can deploy a private OpenShift Container Platform cluster that does not expose external endpoints. Private clusters are accessible from only an internal network and are not visible to the internet.

[NOTE]
====
Public zones are not supported in Route 53 in {aws-short} Government, Secret, and Top Secret regions. Therefore, clusters must be private if they are deployed to one of these regions.
====

By default, OpenShift Container Platform is provisioned to use publicly-accessible DNS and endpoints. A private cluster sets the DNS, Ingress Controller, and API server to private when you deploy your cluster. This means that the cluster resources are only accessible from your internal network and are not visible to the internet.

To deploy a private cluster, you must:

* Use existing networking that meets your requirements. Your cluster resources might be shared between other clusters on the network.
* Use existing networking that meets your requirements.
* Create a DNS zone using {ibm-cloud-name} DNS Services and specify it as the base domain of the cluster. For more information, see "Using {ibm-cloud-name} DNS Services to configure DNS resolution".
* Deploy from a machine that has access to:
** The API services for the cloud to which you provision.
** The hosts on the network that you provision.
** The internet to obtain installation media.

You can use any machine that meets these access requirements and follows your company's guidelines. For example, this machine can be a bastion host on your cloud network.

[NOTE]
====
AWS China does not support a VPN connection between the VPC and your network. For more information about the Amazon VPC service in the Beijing and Ningxia regions, see Amazon Virtual Private Cloud in the AWS China documentation.
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc

[id="private-clusters-about-azure_{context}"]
= Private clusters in Azure

To create a private cluster on Microsoft Azure, you must provide an existing private VNet and subnets to host the cluster. The installation program must also be able to resolve the DNS records that the cluster requires. The installation program configures the Ingress Operator and API server for only internal traffic.

Depending how your network connects to the private VNET, you might need to use a DNS forwarder to resolve the cluster's private DNS records. The cluster's machines use `168.63.129.16` internally for DNS resolution. For more information, see What is Azure Private DNS? and What is IP address 168.63.129.16? in the Azure documentation.

The cluster still requires access to internet to access the Azure APIs.

The following items are not required or created when you install a private cluster:

* A `BaseDomainResourceGroup`, since the cluster does not create public records
* Public IP addresses
* Public DNS records
* Public endpoints

 The cluster is configured so that the Operators do not create public records for the cluster and all cluster machines are placed in the private subnets that you specify.

[id="private-clusters-limitations-azure_{context}"]
== Limitations

Private clusters on Azure are subject to only the limitations that are associated with the use of an existing VNet.

Is this also valid in Azure?

The ability to add public functionality to a private cluster is limited.

* You cannot make the Kubernetes API endpoints public after installation without taking additional actions, including creating public subnets in the VNet for each availability zone in use, creating a public load balancer, and configuring the control plane security groups to allow traffic from the internet on 6443 (Kubernetes API port).

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

[id="installation-azure-user-defined-routing_{context}"]
= User-defined outbound routing

In OpenShift Container Platform, you can choose your own outbound routing for a cluster to connect to the internet. This allows you to skip the creation of public IP addresses and the public load balancer.

You can configure user-defined routing by modifying parameters in the `install-config.yaml` file before installing your cluster. A pre-existing VNet is required to use outbound routing when installing a cluster; the installation program is not responsible for configuring this.

When configuring a cluster to use user-defined routing, the installation program does not create the following resources:

* Outbound rules for access to the internet.
* Public IPs for the public load balancer.
* Kubernetes Service object to add the cluster machines to the public load balancer for outbound requests.

You must ensure the following items are available before setting user-defined
routing:

* Egress to the internet is possible to pull container images, unless using an
{product-registry} mirror.
* The cluster can access Azure APIs.
* Various allowlist endpoints are configured. You can reference these endpoints in the _Configuring your firewall_ section.

There are several pre-existing networking setups that are supported for internet access using user-defined routing.

== Restricted cluster with Azure Firewall

You can use Azure Firewall to restrict the outbound routing for the Virtual Network (VNet) that is used to install the OpenShift Container Platform cluster. For more information, see providing user-defined routing with Azure Firewall. You can create a OpenShift Container Platform cluster in a restricted network by using VNet with Azure Firewall and configuring the user-defined routing.

[IMPORTANT]
====
If you are using Azure Firewall for restricting internet access, you must set the `publish` field to `Internal` in the `install-config.yaml` file. This is because Azure Firewall does not work properly with Azure public load balancers.
====

== Private cluster with network address translation

You can use Azure VNET network address translation (NAT) to provide outbound internet access for the subnets in your cluster. You can reference Create a NAT gateway using Azure CLI in the Azure documentation for configuration instructions.

When using a VNet setup with Azure NAT and user-defined routing configured, you can create a private cluster with no public endpoints.

== Private cluster with Azure Firewall

You can use Azure Firewall to provide outbound routing for the VNet used to install the cluster. You can learn more about providing user-defined routing with Azure Firewall in the Azure documentation.

When using a VNet setup with Azure Firewall and user-defined routing configured, you can create a private cluster with no public endpoints.

== Private cluster with a proxy configuration

You can use a proxy with user-defined routing to allow egress to the internet. You must ensure that cluster Operators do not access Azure APIs using a proxy; Operators must have access to Azure APIs outside of the proxy.

When using the default route table for subnets, with `0.0.0.0/0` populated automatically by Azure, all Azure API requests are routed over Azure's internal network even though the IP addresses are public. As long as the Network Security Group rules allow egress to Azure API endpoints, proxies with user-defined routing configured allow you to create private clusters with no public endpoints.

== Private cluster with no internet access

You can install a private network that restricts all access to the internet, except the Azure API. This is accomplished by mirroring the release image registry locally. Your cluster must have access to the following:

* An {product-registry} mirror that allows for pulling container images
* Access to Azure APIs

With these requirements available, you can use user-defined routing to create private clusters with no public endpoints.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

[id="installation-about-custom-azure-vnet_{context}"]
= About reusing a VNet for your OpenShift Container Platform cluster

In OpenShift Container Platform , you can deploy a cluster into an existing Azure Virtual Network (VNet) in Microsoft Azure. If you do, you must also use existing subnets within the VNet and routing rules.

By deploying OpenShift Container Platform into an existing Azure VNet, you might be able to avoid service limit constraints in new accounts or more easily abide by the operational constraints that your company's guidelines set. This is a good option to use if you cannot obtain the infrastructure creation permissions that are required to create the VNet.

[id="installation-about-custom-azure-vnet-requirements_{context}"]
== Requirements for using your VNet

When you deploy a cluster by using an existing VNet, you must perform additional network configuration before you install the cluster. In installer-provisioned infrastructure clusters, the installer usually creates the following components, but it does not create them when you install into an existing VNet:

* Subnets
* Route tables
* VNets
* Network Security Groups

If you use a custom VNet, you must correctly configure it and its subnets for the installation program and the cluster to use. The installation program cannot subdivide network ranges for the cluster to use, set route tables for the subnets, or set VNet options like DHCP, so you must do so before you install the cluster.

The cluster must be able to access the resource group that contains the existing VNet and subnets. While all of the resources that the cluster creates are placed in a separate resource group that it creates, some network resources are used from a separate group. Some cluster Operators must be able to access resources in both resource groups. For example, the Machine API controller attaches NICS for the virtual machines that it creates to subnets from the networking resource group.

Your VNet must meet the following characteristics:

* The VNet's CIDR block must contain the `Networking.MachineCIDR` range, which is the IP address pool for cluster machines.
* The VNet and its subnets must belong to the same resource group, and the subnets must be configured to use Azure-assigned DHCP IP addresses instead of static IP addresses.

You must provide two subnets within your VNet, one for the control plane machines and one for the compute machines. Because Azure distributes machines in different availability zones within the region that you specify, your cluster will have high availability by default.

[NOTE]
====
By default, if you specify availability zones in the `install-config.yaml` file, the installation program distributes the control plane machines and the compute machines across these availability zones
within a region. To ensure high availability for your cluster, select a region with at least three availability zones. If your region contains fewer than three availability zones, the installation program places more than one control plane machine in the available zones.
====

To ensure that the subnets that you provide are suitable, the installation program confirms the following data:

* All the specified subnets exist.
* There are two private subnets, one for the control plane machines and one for the compute machines.
* The subnet CIDRs belong to the machine CIDR that you specified. Machines are not provisioned in availability zones that you do not provide private subnets for.
If required, the installation program creates public load balancers that manage the control plane and worker nodes, and Azure allocates a public IP address to them.

[NOTE]
====
If you destroy a cluster that uses an existing VNet, the VNet is not deleted.
====

[id="installation-about-custom-azure-vnet-nsg-requirements_{context}"]
=== Network security group requirements

The network security groups for the subnets that host the compute and control plane machines require specific access to ensure that the cluster communication is correct. You must create rules to allow access to the required cluster communication ports.

[IMPORTANT]
====
The network security group rules must be in place before you install the cluster. If you attempt to install a cluster without the required access, the installation program cannot reach the Azure APIs, and installation fails.
====

.Required ports
[options="header",cols="1,3,1,1"]
|===

|Port
|Description
|Control plane
|Compute

|`80`
|Allows HTTP traffic
|
|x

|`443`
|Allows HTTPS traffic
|
|x

|`6443`
|Allows communication to the control plane machines
|x
|

|`22623`
|Allows internal communication to the machine config server for provisioning machines
|x
|

|`*`
a|Allows connections to Azure APIs. You must set a Destination Service Tag to `AzureCloud`. ^[1]^
|x
|x

|`*`
a|Denies connections to the internet. You must set a Destination Service Tag to `Internet`. ^[1]^
|x
|x
|===
[.small]
--
1. If you are using Azure Firewall to restrict the internet access, then you can configure Azure Firewall to allow the Azure APIs. A network security group rule is not needed. For more information, see "Configuring your firewall" in "Additional resources".
--

Because cluster components do not modify the user-provided network security groups, which the Kubernetes controllers update, a pseudo-network security group is created for the Kubernetes controller to modify without impacting the rest of the environment.

.Ports used for all-machine to all-machine communications
[cols="2a,2a,5a",options="header"]
|===

|Protocol
|Port
|Description

|ICMP
|N/A
|Network reachability tests

.3+|TCP
|`1936`
|Metrics

|`9000`-`9999`
|Host level services, including the node exporter on ports `9100`-`9101` and
the Cluster Version Operator on port `9099`.

|`10250`-`10259`
|The default ports that Kubernetes reserves

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
|Network Time Protocol (NTP) on UDP port `123`. If you configure an external NTP time server, you must open UDP port `123`.

|TCP/UDP
|`30000`-`32767`
|Kubernetes node port

|ESP
|N/A
|IPsec Encapsulating Security Payload (ESP)

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

[id="installation-about-custom-azure-permissions_{context}"]
== Division of permissions

Starting with OpenShift Container Platform 4.3, you do not need all of the permissions that are required for an installation program-provisioned infrastructure cluster to deploy a cluster. This change mimics the division of permissions that you might have at your company: some individuals can create different resources in your clouds than others. For example, you might be able to create application-specific items, like instances, storage, and load balancers, but not networking-related components such as VNets, subnet, or ingress rules.

The Azure credentials that you use when you create your cluster do not need the networking permissions that are required to make VNets and core networking components within the VNet, such as subnets, routing tables, internet gateways, NAT, and VPN. You still need permission to make the application resources that the machines within the cluster require, such as load balancers, security groups, storage accounts, and nodes.

[id="installation-about-custom-azure-vnet-isolation_{context}"]
== Isolation between clusters

Because the cluster is unable to modify network security groups in an existing subnet, there is no way to isolate clusters from each other on the VNet.
These are some of the details from the AWS version, and if any of them are relevant to Azure, they can be included.
If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is reduced in the following ways:

* You can install multiple OpenShift Container Platform clusters in the same VNet.
* ICMP ingress is allowed to entire network.
* TCP 22 ingress (SSH) is allowed to the entire network.
* Control plane TCP 6443 ingress (Kubernetes API) is allowed to the entire network.
* Control plane TCP 22623 ingress (MCS) is allowed to the entire network.

[role="_additional-resources"]
.Additional resources

* About the OVN-Kubernetes network plugin

* Configuring your firewall

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
* Installation configuration parameters for Azure

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
// installing/installing_azure/installing-azure-customizations.adoc
// installing/installing_azure/installing-azure-government-region.adoc
// installing/installing_azure/installing-azure-private.adoc
// installing/installing_azure/installing-azure-user-infra.adoc
// installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-tested-machine-types_{context}"]
= Tested instance types for Azure

[role="_abstract"]
There are several Microsoft Azure instance types tested with OpenShift Container Platform. Choose a listed instance type when you install a cluster on 64-bit x86 infrastructure.

.Machine types based on 64-bit x86 architecture
[%collapsible]
====

====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-network-customizations

[id="installation-azure-trusted-launch_{context}"]
= Enabling trusted launch for Azure VMs

[role="_abstract"]
To enable trusted launch on Azure virtual machines for your OpenShift Container Platform cluster, you can configure secure boot and virtualized Trusted Platform Modules in the `install-config.yaml` file. Apply the settings to control plane nodes, compute nodes, or all nodes as needed.

For more information about the sizes of virtual machines that support the trusted launch features, secure boot, and virtualized Trusted Platform Modules, see the Additional resources section.

.Prerequisites

* You have created an `install-config.yaml` file.

.Procedure

* Edit the `install-config.yaml` file before deploying your cluster:

** Enable trusted launch only on control plane by adding the following stanza:
+
[source,yaml]
----
controlPlane:
  platform:
    azure:
      settings:
        securityType: TrustedLaunch
        trustedLaunch:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
----

** Enable trusted launch only on compute node by adding the following stanza:
+
[source,yaml]
----
compute:
  platform:
    azure:
      settings:
        securityType: TrustedLaunch
        trustedLaunch:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
----

**  Enable trusted launch on all nodes by adding the following stanza:
+
[source,yaml]
----
platform:
  azure:
    settings:
      securityType: TrustedLaunch
      trustedLaunch:
        uefiSettings:
          secureBoot: Enabled
          virtualizedTrustedPlatformModule: Enabled
----

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-network-customizations

[id="installation-azure-confidential-vms_{context}"]
= Enabling confidential VMs

[role="_abstract"]
To enable confidential VMs on Azure for your OpenShift Container Platform cluster, you can configure the `install-config.yaml` file before deployment. Apply the settings to control plane nodes, compute nodes, or all nodes as needed.

//commenting out the second encryption option until https://issues.redhat.com/browse/OCPBUGS-18379 is resolved
Confidential VMs can operate in two modes:

* Only encrypting the virtual machine guest state storage, which contains the security state of the virtual machine
* Encrypting the virtual machine guest state storage and the operating system storage

If you encrypt the operating system storage, you can use a platform-managed encryption key or a key you manage.

You can use confidential VMs with the following VM sizes:

* DCasv5-series
* DCadsv5-series
* ECasv5-series
* ECadsv5-series
* DCesv5-series
* DCedsv5-series
* ECesv5-series
* ECedsv5-series
* NCCads_H100_v5

[IMPORTANT]
====
Confidential VMs are currently not supported on 64-bit ARM architectures.
====

.Prerequisites

* You have created an `install-config.yaml` file.

.Procedure

* Edit the `install-config.yaml` file before deploying your cluster:

** Enable confidential VMs only on control plane by adding the following stanza:
+
[source,yaml]
----
controlPlane:
  platform:
    azure:
      settings:
        securityType: ConfidentialVM
        confidentialVM:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
      osDisk:
        securityProfile:
          securityEncryptionType: VMGuestStateOnly
----

**  Enable confidential VMs only on compute nodes by adding the following stanza:
+
[source,yaml]
----
compute:
  platform:
    azure:
      settings:
        securityType: ConfidentialVM
        confidentialVM:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
      osDisk:
        securityProfile:
          securityEncryptionType: VMGuestStateOnly
----

**  Enable confidential VMs on all nodes by adding the following stanza:
+
[source,yaml]
----
platform:
  azure:
    defaultMachinePlatform:
      settings:
        securityType: ConfidentialVM
        confidentialVM:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
      osDisk:
        securityProfile:
          securityEncryptionType: VMGuestStateOnly
----

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-network-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc

[id="installation-azure-config-yaml-simple_{context}"]
= Sample customized install-config.yaml file for Azure

[role="_abstract"]
You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster's platform or modify the values of the required parameters.

[IMPORTANT]
====
This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.
For a full list and description of all installation configuration parameters, see _Installation configuration parameters for Azure_.
====

.Sample `install-config.yaml` file for {azure-short}
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
metadata:
  name: example-cluster
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    azure:
      type: Standard_D8s_v3
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    azure:
      type: Standard_D2s_v3
  replicas: 3
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  azure:
    baseDomainResourceGroupName: example-basedomain-resourcegroup-name
    region: centralus
----
where:

`controlPlane`:: Specifies parameters that apply to control plane machines.
`compute`:: Specifies parameters that apply to compute machines.
`networking`:: Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.
`platform`:: Specifies parameters that apply to the infrastructure platform that hosts the cluster.

[role="_additional-resources"]
.Additional resources

* Installation configuration parameters for Azure

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

[role="_additional-resources"]
.Additional resources

* For more details about Accelerated Networking, see Accelerated Networking for Microsoft Azure VMs.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-specialized-region.adoc
// * installing/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-ibm-cloud-customizations.adoc
// * installing/installing_gcp/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// If you use this module in any other assembly, you must update the ifeval
// statements.

[id="installation-launching-installer_{context}"]
= Deploying the cluster

[role="_abstract"]
To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

[IMPORTANT]
====
You can run the `create cluster` command of the installation program only once, during initial installation.
====

.Prerequisites

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
+
If the {op-system-first} image is available locally, the host running the installation program does not require internet access.
* You have an Azure subscription ID and tenant ID.
* You have the application ID and password of a service principal.
* If you are installing the cluster using a service principal, you have its application ID and password.
* If you are installing the cluster using a system-assigned managed identity, you have enabled it on the virtual machine that you will run the installation program from.
* If you are installing the cluster using a user-assigned managed identity, you have met these prerequisites:
** You have its client ID.
** You have assigned it to the virtual machine that you will run the installation program from.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.
* Optional: Before you create the cluster, you configured an external load balancer in place of the default load balancer.
+
[IMPORTANT]
====
You do not need to specify API and Ingress static addresses for your installation program. If you choose this configuration, you must take additional actions to define network targets that accept an IP address from each referenced vSphere subnet. See the section "Configuring a user-managed load balancer".
====

.Procedure
. Remove any existing {gcp-short} credentials that do not use the service account key
for the {gcp-short} account that you configured for your cluster and that are stored in the
following locations:
** The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON`
environment variables
** The `~/.gcp/osServiceAccount.json` file
** The `gcloud cli` default credentials

. Optional: If you have run the installation program on this computer before, and want to use an alternative service principal, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.
+
Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.
. Optional: If you have run the installation program on this computer before, and want to use an alternative service principal or managed identity, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.
+
Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.
. Export the `OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE` variable to specify the location of the {op-system-first} image by running the following command:
+
[source,terminal]
----
$ export OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE="<path_to_image>/rhcos-<image_version>-ibmcloud.x86_64.qcow2.gz"
----
. In the directory that contains the installation program, initialize the cluster deployment by running the following command:
* In the directory that contains the installation program, initialize the cluster deployment by running the following command:
+
[source,terminal]
----
$ ./openshift-install create cluster --dir <installation_directory> \
    --log-level=info
----
+
** For `<installation_directory>`, specify the
location of your customized `./install-config.yaml` file.
directory name to store the files that the installation program creates.
** To view different installation details, specify `warn`, `debug`, or
`error` instead of `info`.

+
If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.
. Enter the following Azure parameter values for your subscription:
** *azure subscription id*: Enter the subscription ID to use for the cluster.
** *azure tenant id*: Enter the tenant ID.
. Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client id*:
** If you are using a service principal, enter its application ID.
** If you are using a system-assigned managed identity, leave this value blank.
** If you are using a user-assigned managed identity, specify its client ID.
. Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client secret*:
** If you are using a service principal, enter its password.
** If you are using a system-assigned managed identity, leave this value blank.
** If you are using a user-assigned managed identity,leave this value blank.
+
[NOTE]
====
If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.
====

+
When specifying the directory:
* Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
* Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

. Provide values at the prompts:

.. Optional: Select an SSH key to use to access your cluster machines.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
.. Select *aws* as the platform to target.
.. If you do not have an Amazon Web Services (AWS) profile stored on your computer, enter the AWS access key ID and secret access key for the user that you configured to run the
installation program.
+
[NOTE]
====
The AWS access key ID and secret access key are stored in `~/.aws/credentials` in the home directory of the current user on the installation host. You are prompted for the credentials by the installation program if the credentials for the exported profile are not present in the file. Any credentials that you provide to the installation program are stored in the file.
====
.. Select the AWS region to deploy the cluster to.
.. Select the base domain for the Route 53 service that you configured for your cluster.
.. Select *azure* as the platform to target.
+
If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.
.. Specify the following Azure parameter values for your subscription and service principal:
*** *azure subscription id*: Enter the subscription ID to use for the cluster.
*** *azure tenant id*: Enter the tenant ID.
*** *azure service principal client id*: Enter its application ID.
*** *azure service principal client secret*: Enter its password.
.. Select the region to deploy the cluster to.
.. Select the base domain to deploy the cluster to. The base domain corresponds to the Azure DNS Zone that you created for your cluster.
.. Select *gcp* as the platform to target.
.. If you have not configured the service account key for your {gcp-short} account on
your host, you must obtain it from {gcp-short} and paste the contents of the file
or enter the absolute path to the file.
.. Select the project ID to provision the cluster in. The default value is
specified by the service account that you configured.
.. Select the region to deploy the cluster to.
.. Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
.. test
.. Select *openstack* as the platform to target.
.. Specify the {rh-openstack-first} external network name to use for installing the cluster.
.. Specify the Floating IP address to use for external access to the OpenShift API.
.. Specify the {rh-openstack} flavor with at least 16 GB RAM to use for control plane
and compute nodes.
.. Select the base domain to deploy the cluster to. All DNS records will be
sub-domains of this base and will also include the cluster name.
.. Select *vsphere* as the platform to target.
.. Specify the name of your vCenter instance.
.. Specify the user name and password for the vCenter account that has the required permissions to create the cluster.
+
The installation program connects to your vCenter instance.
+
[IMPORTANT]
====
Some VMware vCenter Single Sign-On (SSO) environments with Active Directory (AD) integration might primarily require you to use the traditional login method, which requires the `<domain>\` construct.

To ensure that vCenter account permission checks complete properly, consider using the User Principal Name (UPN) login method, such as `<username>@<fully_qualified_domainname>`.
====

.. Select the data center in your vCenter instance to connect to.
.. Select the default vCenter datastore to use.
+
[NOTE]
====
Datastore and cluster names cannot exceed 60 characters; therefore, ensure the combined string length does not exceed the 60 character limit.
====
.. Select the vCenter cluster to install the OpenShift Container Platform cluster in. The installation program uses the root resource pool of the vSphere cluster as the default resource pool.
.. Select the network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.
.. Enter the virtual IP address that you configured for control plane API access.
.. Enter the virtual IP address that you configured for cluster ingress.
.. Enter the base domain. This base domain must be the same one that you used in the DNS records that you configured.
.. Enter a descriptive name for your cluster.
The cluster name must be the same one that you used in the DNS records that you configured.
+
[NOTE]
====
Datastore and cluster names cannot exceed 60 characters; therefore, ensure the combined string length does not exceed the 60 character limit.
====
+
[IMPORTANT]
====
All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see
Resolve reserved resource name errors in the Azure documentation.
====
If you provide a name that is longer
than 6 characters, only the first 6 characters will be used in the infrastructure
ID that is generated from the cluster name.
.. Paste the {cluster-manager-url-pull}.
.. Paste the {cluster-manager-url-pull}.
* If you do not have a {cluster-manager-url-pull}, you can paste the pull secret another private registry.
* If you do not need the cluster to pull images from a private registry, you can paste `{"auths":{"fake":{"auth":"aWQ6cGFzcwo="}}}` as the pull secret.

+
[NOTE]
====
If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.
====

. Optional: Remove or disable the `AdministratorAccess` policy from the IAM
account that you used to install the cluster.
+
[NOTE]
====
The elevated permissions provided by the `AdministratorAccess` policy are required only during installation.
====

. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.
** If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
** If you included the `Service Account Key Admin` role,
you can remove it.

.Verification

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.

* Credential information also outputs to `<installation_directory>/.openshift_install.log`.
+
[IMPORTANT]
====
Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.
====
+
.Example output
[source,terminal]
----
...
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
INFO Login to the console with user: "kubeadmin", and password: "password"
INFO Time elapsed: 36m22s
----
+
[IMPORTANT]
====
* The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

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

[role="_additional-resources"]
.Additional resources

* Accessing the web console

== Next steps

* Customize your cluster.
* If necessary, you can
Remote health reporting.
