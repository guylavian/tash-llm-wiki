---
title: "Installing a cluster on {aws-short} with customizations"
type: reference
domain: openshift
slug: installing-4-22-installing-aws-customizations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-aws-customizations
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on {aws-short} with customizations

[id="installing-aws-customizations"]
= Installing a cluster on {aws-short} with customizations

[role="_abstract"]
In OpenShift Container Platform version , you can install a cluster on {aws-first} by using installer-provisioned infrastructure with customizations, including network configuration options. In each, you modify parameters in the `install-config.yaml` file before you install the cluster. By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. You must set most of the network configuration parameters during installation, and you can modify only `kubeProxy` configuration parameters in a running cluster.

[NOTE]
====
The scope of the OpenShift Container Platform installation configurations is intentionally narrow. It is designed for simplicity and ensured success. You can complete many more OpenShift Container Platform configuration tasks after an installation completes.
====

== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You configured an AWS account to host the cluster.
+
[IMPORTANT]
====
If you have an {aws-short} profile stored on your computer, it must not use a temporary session token that you generated while using a multi-factor authentication device. The cluster continues to use your current {aws-short} credentials to create {aws-short} resources for the entire life of the cluster, so you must use long-term credentials. To generate appropriate keys, see Managing Access Keys for IAM Users in the {aws-short} documentation. You can supply the keys when you run the installation program.
====
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc

[id="installation-aws-marketplace-subscribe_{context}"]
= Obtaining an AWS Marketplace image

If you are deploying an OpenShift Container Platform cluster using an AWS Marketplace image, you must first subscribe through AWS. Subscribing to the offer provides you with the AMI ID that the installation program uses to deploy compute nodes.

[NOTE]
====
====

.Prerequisites

* You have an AWS account to purchase the offer. This account does not have to be the same account that is used to install the cluster.

.Procedure

. Complete the OpenShift Container Platform subscription from the AWS Marketplace.
. Record the AMI ID for your specific AWS Region. As part of the installation process, you must update the `install-config.yaml` file with this value before deploying the cluster.
. Record the AMI ID for your specific AWS Region. If you use the CloudFormation template to deploy your compute nodes, you must update the `worker0.type.properties.ImageID` parameter with the AMI ID value.
+
.Sample `install-config.yaml` file with AWS Marketplace compute nodes

[source,yaml]
----
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    aws:
      amiID: ami-06c4d345f7c207239 <1>
      type: m5.4xlarge
  replicas: 3
metadata:
  name: test-cluster
platform:
  aws:
    region: us-east-2 <2>
sshKey: ssh-ed25519 AAAA...
pullSecret: '{"auths": ...}'
----
<1> The AMI ID from your AWS Marketplace subscription.
<2> Your AMI ID is associated with a specific AWS Region. When creating the installation configuration file, ensure that you select the same AWS Region that you specified when configuring your subscription.

// TODO -  possibly delete this file
// Or does it add actual value?

// Module included in the following assemblies:
//
// * networking/cluster-network-operator.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc

[id="nw-network-config_{context}"]
= Network configuration phases

[role="_abstract"]
There are two phases prior to OpenShift Container Platform installation where you can customize the network configuration. Customize settings in the `install-config.yaml` file and in the Cluster Network Operator manifest across two configuration phases.

Phase 1:: You can customize the following network-related fields in the `install-config.yaml` file before you create the manifest files:
+
* `networking.networkType`
* `networking.clusterNetwork`
* `networking.serviceNetwork`
* `networking.machineNetwork`
* `nodeNetworking`
+
For more information, see "Installation configuration parameters".
+
[NOTE]
====
Set the `networking.machineNetwork` to match the Classless Inter-Domain Routing (CIDR) where the preferred subnet is located.
====
+
[IMPORTANT]
====
The CIDR range `172.17.0.0/16` is reserved by `libVirt`. You cannot use any other CIDR range that overlaps with the `172.17.0.0/16` CIDR range for networks in your cluster.
====

Phase 2:: After creating the manifest files by running `openshift-install create manifests`, you can define a customized Cluster Network Operator manifest with only the fields you want to modify. You can use the manifest to specify an advanced network configuration.

During phase 2, you cannot override the values that you specified in phase 1 in the `install-config.yaml` file. However, you can customize the network plugin during phase 2.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_vmc/installing-vmc-customizations.adoc
// * installing/installing_vmc/installing-vmc-network-customizations.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_nutanix/configuring-iam-nutanix.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_gcp/installing-openstack-installer-restricted.adoc
// Consider also adding the installation-configuration-parameters.adoc module.
//YOU MUST SET AN IFEVAL FOR EACH NEW MODULE

[id="installation-initializing_{context}"]
= Creating the installation configuration file

[role="_abstract"]
You can customize the OpenShift Container Platform cluster you install on
Amazon Web Services (AWS).
{gcp-first}.
{ibm-cloud-name}.
{rh-openstack-first}.
VMware vSphere.
Nutanix.
{ibm-power-vc-name}.
Microsoft Azure.

[IMPORTANT]
====
Do not specify `windows`, `microsoft`, or other variants of these words in the `metadata.name` parameter of the `install-config.yaml` file. Specifying one of these words for the cluster name causes the installation program to generate an error message like the following example message:

[source,terminal]
----
The resource name 'windows-xxxx-identity' or a part of the name is a trademarked or reserved word.
----

Additionally, specifying `login` at the beginning of the name in the `metadata.name` parameter of the `install-config.yaml` file results in the generation of an error message. You can specify `login` in the middle or end of the name.
====

.Prerequisites

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
For a restricted network installation, these files are on your mirror host.
* You have the `imageContentSources` values that were generated during mirror registry creation.
* You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry.
* You have the location of the {op-system-first} image you download.
* You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry.
* You have obtained the contents of the certificate for your mirror registry.
* You have retrieved a {op-system-first} image and uploaded it to an accessible location.
* You have an Azure subscription ID and tenant ID.
* If you are installing the cluster using a service principal, you have its application ID and password.
* If you are installing the cluster using a system-assigned managed identity, you have enabled it on the virtual machine that you will run the installation program from.
* If you are installing the cluster using a user-assigned managed identity, you have met these prerequisites:
** You have its client ID.
** You have assigned it to the virtual machine that you will run the installation program from.
* You have verified that you have met the Nutanix networking requirements. For more information, see "Preparing to install on Nutanix".
* Configure a {gcp-short} account.

.Procedure

. Optional: If you have run the installation program on this computer before, and want to use an alternative service principal or managed identity, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.
+
Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.

. Create the `install-config.yaml` file.
+
.. Change to the directory that contains the installation program and run the following command:
+
[source,terminal]
----
$ ./openshift-install create install-config --dir <installation_directory>
----
* `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the
files that the installation program creates.
+
When specifying the directory:
* Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
* Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
+
[NOTE]
=====
Always delete the `~/.powervs` directory to avoid reusing a stale configuration. Run the following command:
[source,terminal]
----
$ rm -rf ~/.powervs
----
=====
+
.. At the prompts, provide the configuration details for your cloud:
+
... Optional: Select an SSH key to use to access your cluster machines.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
+
... Select *AWS* as the platform to target.
+
... If you do not have an Amazon Web Services (AWS) profile stored on your computer, enter the AWS
access key ID and secret access key for the user that you configured to run the
installation program.
+
... Select the AWS region to deploy the cluster to.
+
... Select the base domain for the Route 53 service that you configured for your cluster.
+
... Select *azure* as the platform to target.
+
If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.
+
... Enter the following Azure parameter values for your subscription:
**** *azure subscription id*: Enter the subscription ID to use for the cluster.
**** *azure tenant id*: Enter the tenant ID.
+
... Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client id*:
**** If you are using a service principal, enter its application ID.
**** If you are using a system-assigned managed identity, leave this value blank.
**** If you are using a user-assigned managed identity, specify its client ID.
+
... Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client secret*:
**** If you are using a service principal, enter its password.
**** If you are using a system-assigned managed identity, leave this value blank.
**** If you are using a user-assigned managed identity, leave this value blank.
+
... Select the region to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the Azure DNS Zone that you created for your cluster.
+
... Select *gcp* as the platform to target.
+
... If you have not configured the service account key for your {gcp-short} account on
your computer, you must obtain it from {gcp-short} and paste the contents of the file
or enter the absolute path to the file.
+
... Select the project ID to provision the cluster in. The default value is
specified by the service account that you configured.
+
... Select the region to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
+
... Select *ibmcloud* as the platform to target.
+
... Select the region to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
+
... Select *powervs* as the platform to target.
+
... Select the region to deploy the cluster to.
+
... Select the zone to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
+
... Select *openstack* as the platform to target.
+
... Specify the {rh-openstack-first} external network name to use for installing the cluster.
+
... Specify the floating IP address to use for external access to the OpenShift API.
+
... Specify a {rh-openstack} flavor with at least 16 GB RAM to use for control plane nodes
and 8 GB RAM for compute nodes.
+
... Select the base domain to deploy the cluster to. All DNS records will be
sub-domains of this base and will also include the cluster name.
+
... Select *vsphere* as the platform to target.
+
... Specify the name of your vCenter instance.
+
... Specify the user name and password for the vCenter account that has the required permissions to create the cluster.
+
The installation program connects to your vCenter instance.
+
... Select the data center in your vCenter instance to connect to.
+
[NOTE]
====
After you create the installation configuration file, you can modify the file to create a multiple vSphere data center environment. This means that you can deploy an OpenShift Container Platform cluster to multiple vSphere data centers. For more information about creating this environment, see the section named _VMware vSphere region and zone enablement_.
====
+
... Select the default vCenter datastore to use.
+
[WARNING]
====
You can specify the path of any datastore that exists in a datastore cluster. By default, Storage Distributed Resource Scheduler (SDRS), which uses Storage vMotion, is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable Storage DRS to avoid data loss issues for your OpenShift Container Platform cluster.

You cannot specify more than one datastore path. If you must specify VMs across multiple datastores, use a `datastore` object to specify a failure domain in your cluster's `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".
====
+
... Select the vCenter cluster to install the OpenShift Container Platform cluster in. The installation program uses the root resource pool of the vSphere cluster as the default resource pool.
+
... Select the network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.
+
... Enter the virtual IP address that you configured for control plane API access.
+
... Enter the virtual IP address that you configured for cluster ingress.
+
... Enter the base domain. This base domain must be the same one that you used in the DNS records that you configured.
+
... Select *nutanix* as the platform to target.
+
... Enter the Prism Central domain name or IP address.
+
... Enter the port that is used to log into Prism Central.
+
... Enter the credentials that are used to log into Prism Central.
+
The installation program connects to Prism Central.
+
... Select the Prism Element that will manage the OpenShift Container Platform cluster.
+
... Select the network subnet to use.
+
... Enter the virtual IP address that you configured for control plane API access.
+
... Enter the virtual IP address that you configured for cluster ingress.
+
... Enter the base domain. This base domain must be the same one that you configured in the DNS records.
+
... Enter a descriptive name for your cluster.
+
[IMPORTANT]
====
All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see Resolve reserved resource name errors in the Azure documentation.
====
+
+
... Paste the {cluster-manager-url-pull}.
The cluster name you enter must match the cluster name you specified when configuring the DNS records.
+
... Enter a name for your cluster. The name must be 14 or fewer characters long.

. Modify the `install-config.yaml` file. The AWS Outposts installation has the following limitations which require manual modification of the `install-config.yaml` file:
+
* Unlike AWS Regions, which offer near-infinite scale, AWS Outposts are limited by their provisioned capacity, EC2 family and generations, configured instance sizes, and availability of compute capacity that is not already consumed by other workloads. Therefore, when creating new OpenShift Container Platform cluster, you need to provide the supported instance type in the `compute.platform.aws.type` section in the configuration file.
* When deploying OpenShift Container Platform cluster with remote workers running in AWS Outposts, only one Availability Zone can be used for the compute instances - the Availability Zone in which the Outpost instance was created in. Therefore, when creating new OpenShift Container Platform cluster, it recommended to provide the relevant Availability Zone in the `compute.platform.aws.zones` section in the configuration file, in order to limit the compute instances to this Availability Zone.
* Amazon Elastic Block Store (EBS) gp3 volumes are not supported by the AWS Outposts service. This volume type is the default type used by the OpenShift Container Platform cluster. Therefore, when creating new OpenShift Container Platform cluster, you must change the volume type in the `compute.platform.aws.rootVolume.type` section to gp2.
You will find more information about how to change these values below.

. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.
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
.. Define the network and subnets for the VNet to install the cluster under the `platform.azure` field:
+
[source,yaml]
----
networkResourceGroupName: <vnet_resource_group>
virtualNetwork: <vnet>
controlPlaneSubnet: <control_plane_subnet>
computeSubnet: <compute_subnet>
----
+
where:
+
`<vnet_resource_group>`:: Specifies the resource group name that contains the existing virtual network (VNet).
`<vnet>`:: Specifies the existing virtual network name.
`<control_plane_subnet>`:: Specifies the existing subnet name to deploy the control plane machines.
`<compute_subnet>`:: Specifies the existing subnet name to deploy compute machines.
+
[NOTE]
====
If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster's control planes are schedulable. For more information, see "Installing a three-node cluster on {platform}".
====

. In the `install-config.yaml` file, set the value of `platform.openstack.clusterOSImage` to the image location or name. For example:
+
[source,yaml]
----
platform:
  openstack:
      clusterOSImage: http://mirror.example.com/images/rhcos-43.81.201912131630.0-openstack.x86_64.qcow2.gz?sha256=ffebbd68e8a1f2a245ca19522c16c86f67f9ac8e4e0c1f0a812b068b16f7265d
----

. Choose one of the following methods to speficy an {op-system} image for your cluster than runs in a {vmw-full} vCenter environment.
+
.. The `clusterOSImage` parameter method: In the `install-config.yaml` file, set the value of `platform.vsphere.clusterOSImage` to the image location or name. For example:
+
[source,yaml]
----
platform:
  vsphere:
      clusterOSImage: http://mirror.example.com/images/rhcos-43.81.201912131630.0-vmware.x86_64.ova?sha256=ffebbd68e8a1f2a245ca19522c16c86f67f9ac8e4e0c1f0a812b068b16f7265d
----
+
.. The `topology.template` parameter method:
+
... Download the *{op-system-first} - vSphere* image in Open Virtual Appliance (OVA) format to your local system. For more information, see "Creating the RHCOS image for restricted network installations".
+
... From the *Hosts and Clusters* tab on the {vmw-short} Client, right-click your cluster name and select *Deploy OVF Template*.
+
... On the *Select an OVF* tab, specify the name of the {op-system} OVA file that you downloaded.
+
... On the *Select a name and folder* tab, set a *Virtual machine name* for your template, such as `Template-{op-system}`.
+
... Click the name of your vSphere cluster and select the folder you created in the previous step.
+
... On the *Select a compute resource* tab, click the name of your vSphere cluster.
+
... On the *Select storage* tab, configure the storage options for your VM.
+
... When creating the OVF template, do not specify values on the *Customize template* tab or configure the template any further.
+
... In the `install-config.yaml` file, set the value of `topology.template` to the path where you imported the image to your {vmw-short} vCenter instance.
. In the `install-config.yaml` file, set the value of `platform.nutanix.clusterOSImage` to the image location or name. For example:
+
[source,yaml]
----
platform:
  nutanix:
      clusterOSImage: http://mirror.example.com/images/rhcos-47.83.202103221318-0-nutanix.x86_64.qcow2
----
. Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network.
+
.. Update the `pullSecret` value to contain the authentication information for
your registry:
+
[source,yaml]
----
pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
----
+
For `<mirror_host_name>`, specify the registry domain name
that you specified in the certificate for your mirror registry, and for
`<credentials>`, specify the base64-encoded user name and password for
your mirror registry.
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
.. Define the subnets for the VPC to install the cluster in, as in the following example:
+
[source,yaml]
----
platform:
  aws:
    vpc:
      subnets:
        - id: subnet-<id_1>
        - id: subnet-<id_2>
        - id: subnet-<id_3>
----
+
.. Define the network and subnets for the VNet to install the cluster under the `platform.azure` field:
+
[source,yaml]
----
networkResourceGroupName: <vnet_resource_group>
virtualNetwork: <vnet>
controlPlaneSubnet: <control_plane_subnet>
computeSubnet: <compute_subnet>
----
+
where:
+
`<vnet_resource_group>`:: Specifies the resource group name that contains the existing virtual network (VNet).
`<vnet>`:: Specifies the existing virtual network name.
`<control_plane_subnet>`:: Specifies the existing subnet name to deploy the control plane machines.
`<compute_subnet>`:: Specifies the existing subnet name to deploy compute machines.
+
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
For `platform.gcp.network`, specify the name for the existing Google VPC. For `platform.gcp.controlPlaneSubnet` and `platform.gcp.computeSubnet`, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
+
.. Define the network for the VPC to install the cluster in under the parent `platform.powervs` field:
+
[source,yaml]
----
vpcName: <existing_vpc>
----
+
For `platform.powervs.vpcName`, specify the name for the existing {ibm-cloud-name} VPC.
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
For these values, use the `imageContentSources` that you recorded during mirror registry creation.
For these values, use the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.
+
.. If your Virtual Private Cloud (VPC) network is unable to access the public endpoints for the required {ibm-cloud-name} service endpoints, add the following stanza to `platform.ibmcloud` to override them using {ibm-cloud-name} Virtual Private Endpoints (VPE).
+
[source,yaml]
----
# ...
serviceEndpoints:
  - name: IAM
    url: <iam_private_endpoint_url>
  - name: VPC
    url: <vpc_private_endpoint_url>
  - name: ResourceController
    url: <resource_controller_private_endpoint_url>
  - name: ResourceManager
    url: <resource_manager_private_endpoint_url>
  - name: DNSServices
    url: <dns_services_private_endpoint_url>
  - name: COS
    url: <cos_private_endpoint_url>
  - name: GlobalSearch
    url: <global_search_private_endpoint_url>
  - name: GlobalTagging
    url: <global_tagging_private_endpoint_url>
# ...
----
+
[NOTE]
====
Only one VPE can be specified per service.
====
+
.. Optionally, set the publishing strategy to `Internal`:
+
[source,yaml]
----
publish: Internal
----
+
By setting this option, you create an internal Ingress Controller and a private load balancer.
+
[IMPORTANT]
====
Azure Firewall does not work seamlessly with Azure Public Load balancers. Thus, when using Azure Firewall for restricting internet access, the `publish` field in `install-config.yaml` should be set to `Internal`.
====
+
[NOTE]
====
If you use the default value of `External`, your network must be able to access the public endpoint for {ibm-cloud-name} Internet Services (CIS). CIS is not enabled for Virtual Private Endpoints.
====

. Make any other modifications to the `install-config.yaml` file that you require.
+
For more information about the parameters, see "Installation configuration parameters".

. Optional: Update one or more of the default configuration parameters in the `install.config.yaml` file to customize the installation.
+
For more information about the parameters, see "Installation configuration parameters".
+
[NOTE]
====
If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that cluster's control planes are schedulable. For more information, see "Installing a three-node cluster on {platform}".
====

. Back up the `install-config.yaml` file so that you can use
it to install multiple clusters.
+
[IMPORTANT]
====
The `install-config.yaml` file is consumed during the installation process. If
you want to reuse the file, you must back it up now.
====
+
If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.

[role="_additional-resources"]
.Additional resources

* Installation configuration parameters for {aws-short}

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
// installing/installing_aws/installing-aws-china.adoc
// installing/installing_aws/installing-aws-customizations.adoc
// installing/installing_aws/installing-aws-government-region.adoc
// installing/installing_aws/installing-aws-private.adoc
// installing/installing_aws/installing-aws-secret-region.adoc
// installing/installing_aws/installing-aws-user-infra.adoc
// installing/installing_aws/installing-aws-vpc.adoc
// installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc

[id="installation-aws-tested-machine-types_{context}"]
= Tested instance types for AWS

The following Amazon Web Services (AWS) instance types have been tested with
OpenShift Container Platform.
OpenShift Container Platform for use with AWS Local Zones.
OpenShift Container Platform for use with AWS Wavelength Zones.

[NOTE]
====
Use the machine types included in the following charts for your AWS instances. If you use an instance type that is not listed in the chart, ensure that the instance size you use matches the minimum resource requirements that are listed in the section named "Minimum resource requirements for cluster installation".
====

.Machine types based on 64-bit x86 architecture
[%collapsible]
====

====
.Machine types based on 64-bit x86 architecture for AWS Local Zones
[%collapsible]
====
* `c5.*`
* `c5d.*`
* `m6i.*`
* `m5.*`
* `r5.*`
* `t3.*`
====
.Machine types based on 64-bit x86 architecture for AWS Wavelength Zones
[%collapsible]
====
* `r5.*`
* `t3.*`
====
.Machine types based on 64-bit x86 architecture for secret regions
[%collapsible]
====
* `c4.*`
* `c5.*`
* `i3.*`
* `m4.*`
* `m5.*`
* `r4.*`
* `r5.*`
* `t3.*`
====

// Module included in the following assemblies:
//
// installing/installing_aws/installing-aws-china.adoc
// installing/installing_aws/installing-aws-customizations.adoc
// installing/installing_aws/installing-aws-government-region.adoc
// installing/installing_aws/installing-aws-private.adoc
// installing/installing_aws/installing-aws-user-infra.adoc
// installing/installing_aws/installing-aws-vpc.adoc
// installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-arm-tested-machine-types_{context}"]
= Tested instance types for AWS on 64-bit ARM infrastructures

The following Amazon Web Services (AWS) 64-bit ARM instance types have been tested with OpenShift Container Platform.

[NOTE]
====
Use the machine types included in the following charts for your AWS ARM instances. If you use an instance type that is not listed in the chart, ensure that the instance size you use matches the minimum resource requirements that are listed in "Minimum resource requirements for cluster installation".
====

.Machine types based on 64-bit ARM architecture
[%collapsible]
====

====

[id="installation-aws-enabling-user-managed-DNS_{context}"]
= Enabling a user-managed DNS

[role="_abstract"]
You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution that uses the Route 53 service for {aws-first}.

For example, your organization's security policies might not allow the use of public DNS services such as {aws-full} DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

.Procedure
* Before you deploy your cluster, use a text editor to open the `install-config.yaml` file  and add the following stanza:
** To enable user-managed DNS:
+
[source,yaml]
----
featureSet: CustomNoUpgrade
featureGates: ["AWSClusterHostedDNSInstall=true"]

# ...

platform:
  aws:
    userProvisionedDNS: Enabled
----
+
where:
+
--
`userProvisionedDNS`:: Enables user-provisioned DNS management.
--

.Next steps
For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-customizations.adoc

[id="installation-aws-config-yaml-customizations_{context}"]
= Sample customized install-config.yaml file for AWS

You can customize the installation configuration file (`install-config.yaml`) to specify more details about your OpenShift Container Platform cluster's platform or modify the values of the required parameters.

[IMPORTANT]
====
This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.
For a full list and description of all installation configuration parameters, see _Installation configuration parameters for AWS_.
====

.Sample `install-config.yaml` file for {aws-short}
[source,yaml]
----
apiVersion: v1 <1>
baseDomain: example.com
sshKey: ssh-ed25519 AAAA...
pullSecret: '{"auths": ...}'
metadata:
  name: example-cluster
controlPlane: <2>
  name: master
  platform:
    aws:
      type: m6i.xlarge
  replicas: 3
compute: <3>
-  name: worker
  platform:
    aws:
      type: c5.4xlarge
  replicas: 3
networking: <4>
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform: <5>
  aws:
    region: us-west-2
----
<1> Parameters at the first level of indentation apply to the cluster globally.
<2> The `controlPlane` stanza applies to control plane machines.
<3> The `compute` stanza applies to compute machines.
<4> The `networking` stanza applies to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.
<5> The `platform` stanza applies to the infrastructure platform that hosts the cluster.

[role="_additional-resources"]
.Additional resources

* Installation configuration parameters for {aws-short}

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

[id="installing-aws-manual-modes_{context}"]
== Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

* To manage long-term cloud credentials manually, follow the procedure in Manually creating long-term credentials.

* To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in Configuring an {aws-short} cluster to use short-term credentials.

//Manually creating long-term credentials
// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-network-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//Platforms that must manually create IAM

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="manually-create-iam_{context}"]

//For providers that support multiple modes of operation
= Manually creating long-term credentials

//For providers who only support manual mode
= Manually manage cloud credentials

//For providers that support multiple modes of operation
[role="_abstract"]
The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

//For providers who only support manual mode
The Cloud Credential Operator (CCO) only supports your cloud provider in manual mode. As a result, you must specify the identity and access management (IAM) secrets for your cloud provider.

.Procedure

. Add the following granular permissions to the {gcp-short} account that the installation program uses:
+
* compute.machineTypes.list
* compute.regions.list
* compute.zones.list
* dns.changes.create
* dns.changes.get
* dns.managedZones.create
* dns.managedZones.delete
* dns.managedZones.get
* dns.managedZones.list
* dns.networks.bindPrivateDNSZone
* dns.resourceRecordSets.create
* dns.resourceRecordSets.delete
* dns.resourceRecordSets.list

. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:
+
.Sample configuration file snippet
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
----

. If you have not previously created installation manifest files, do so by running the following command:
+
[source,terminal]
----
$ openshift-install create manifests --dir <installation_directory>
----
+
where `<installation_directory>` is the directory in which the installation program creates files.

. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----

. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
----
+
where:
+
`--included`:: Specifies only the manifests that your specific cluster configuration requires.
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
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - effect: Allow
      action:
      - iam:GetUser
      - iam:GetUserPolicy
      - iam:ListAccessKeys
      resource: "*"
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
    kind: GCPProviderSpec
    predefinedRoles:
    - roles/storage.admin
    - roles/iam.serviceAccountUser
    skipServiceCheck: true
  ...
----

. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.
+
.Sample `CredentialsRequest` object with secrets
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - effect: Allow
      action:
      - s3:CreateBucket
      - s3:DeleteBucket
      resource: "*"
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
    kind: GCPProviderSpec
      predefinedRoles:
      - roles/iam.securityReviewer
      - roles/iam.roleViewer
      skipServiceCheck: true
      ...
  secretRef:
    name: <component_secret>
    namespace: <component_namespace>
  ...
----
+
.Sample `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <component_secret>
  namespace: <component_namespace>
data:
  aws_access_key_id: <base64_encoded_aws_access_key_id>
  aws_secret_access_key: <base64_encoded_aws_secret_access_key>
data:
  azure_subscription_id: <base64_encoded_azure_subscription_id>
  azure_client_id: <base64_encoded_azure_client_id>
  azure_client_secret: <base64_encoded_azure_client_secret>
  azure_tenant_id: <base64_encoded_azure_tenant_id>
  azure_resource_prefix: <base64_encoded_azure_resource_prefix>
  azure_resourcegroup: <base64_encoded_azure_resourcegroup>
  azure_region: <base64_encoded_azure_region>
data:
  service_account.json: <base64_encoded_gcp_service_account_file>
----
+
[IMPORTANT]
====
Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.
====

//Platforms that must manually create IAM

//AWS install assemblies

//GCP install assemblies

//Azure will also be moved as part of work on `ccoctl` support for Azure

//global Azure install assemblies

//Supertask: Configuring an AWS cluster to use short-term credentials
[id="installing-aws-with-short-term-creds_{context}"]
=== Configuring an {aws-short} cluster to use short-term credentials

To install a cluster that is configured to use the AWS Security Token Service (STS), you must configure the CCO utility and create the required AWS resources for your cluster.

//Task part 1: Configuring the Cloud Credential Operator utility
// Module included in the following assemblies:
//
//Postinstall and update content
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc
//
//Platforms that must use `ccoctl` and update content
// * installing/installing_ibm_cloud/configuring-iam-ibm-cloud.adoc
// * installing/installing_ibm_powervs/preparing-to-install-on-ibm-power-vs.doc
// * installing/installing_nutanix/preparing-to-install-on-nutanix.adoc
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//Postinstall  and update content

//Platforms that must use `ccoctl`

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="cco-ccoctl-configuring_{context}"]

[role="_abstract"]
//Nutanix-only intro because it needs context in its install procedure.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on Nutanix, you must set the CCO to `manual` mode as part of the installation process.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on {ibm-power-server-name}, you must set the CCO to `manual` mode as part of the installation process.

//The upgrade and postinstall procs also have a different intro, so they are excluded here.
To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

//Intro for the postinstall procs.
To configure an existing cluster to create and manage cloud credentials from outside of the cluster, extract and prepare the Cloud Credential Operator utility (`ccoctl`) binary.

//Intro for the upgrade procs.
To upgrade a cluster that uses the Cloud Credential Operator (CCO) in manual mode to create and manage cloud credentials from outside of the cluster, extract and prepare the CCO utility (`ccoctl`) binary.

[NOTE]
====
The `ccoctl` utility is a Linux binary that must run in a Linux environment.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the {oc-first}.

//Upgrade prereqs
* Your cluster was configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

//Permissions requirements (per platform, for install and key rotation)

.Procedure

. Set a variable for the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
----
$ RELEASE_IMAGE=$(oc get clusterversion -o jsonpath={..desired.image})
----

. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
----
+
[NOTE]
====
Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
====

. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
----
+
For `<rhel_version>`, specify the value that corresponds to the version of {op-system-base-full} that the host uses.
If no value is specified, `ccoctl.rhel8` is used by default.
The following values are valid:
+
* `rhel8`: Specify this value for hosts that use {op-system-base} 8.
* `rhel9`: Specify this value for hosts that use {op-system-base} 9.

+
[NOTE]
====
The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
====

. Change the permissions to make `ccoctl` executable by running the following command:
+
[source,terminal]
----
$ chmod 775 ccoctl
----

.Verification

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:
+
[source,terminal]
----
$ ./ccoctl
----
+
.Example output
[source,terminal]
----
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
----

//Postinstall and update content

//Platforms that must use `ccoctl` and update content

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

//Task part 2: Creating the required AWS resources
[id="sts-mode-create-aws-resources-ccoctl_{context}"]
==== Creating {aws-short} resources with the Cloud Credential Operator utility

You have the following options when creating {aws-short} resources:

* You can use the `ccoctl aws create-all` command to create the {aws-short} resources automatically. This is the quickest way to create the resources. See Creating {aws-short} resources with a single command.

* If you need to review the JSON files that the `ccoctl` tool creates before modifying AWS resources, or if the process the `ccoctl` tool uses to create AWS resources automatically does not meet the requirements of your organization, you can create the {aws-short} resources individually. See Creating {aws-short} resources individually.

//Task part 2a: Creating the required AWS resources all at once
// Module included in the following assemblies:
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="cco-ccoctl-creating-at-once_{context}"]
= Creating AWS resources with a single command

[role="_abstract"]
If the process the `ccoctl` tool uses to create AWS resources automatically meets the requirements of your organization, you can use the `ccoctl aws create-all` command to automate the creation of AWS resources.

Otherwise, you can create the AWS resources individually. For more information, see "Creating AWS resources individually".

= Creating {gcp-short} resources with the Cloud Credential Operator utility

[role="_abstract"]
You can use the `ccoctl gcp create-all` command to automate the creation of {gcp-short} resources.
= Creating Azure resources with the Cloud Credential Operator utility

[role="_abstract"]
You can use the `ccoctl azure create-all` command to automate the creation of Azure resources.

[NOTE]
====
By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.
====

.Prerequisites

You must have:

* Extracted and prepared the `ccoctl` binary.

* Access to your Microsoft Azure account by using the Azure CLI.

.Procedure

. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----

. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
----
+
where:
+
`--included`:: Specifies to include only the manifests that your specific cluster configuration requires.
`<path_to_directory_with_installation_configuration>`:: Specifies the location of the `install-config.yaml` file.
`<path_to_directory_for_credentials_requests>`:: Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
+
[NOTE]
====
This command might take a few moments to run.
====

. To enable the `ccoctl` utility to detect your Azure credentials automatically, log in to the Azure CLI by running the following command:
+
[source,terminal]
----
$ az login
----

. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-all \
  --name=<name> \
  --region=<aws_region> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --output-dir=<path_to_ccoctl_output_dir> \
  --create-private-s3-bucket \
  --permissions-boundary-arn=<policy_arn>
----
+
where:
+
`<name>`:: Specifies the name used to tag any cloud resources that are created for tracking.
`<aws_region>`:: Specifies the AWS region in which cloud resources will be created.
`<path_to_credentials_requests_directory>`:: Specifies the directory containing the files for the component `CredentialsRequest` objects.
`<path_to_ccoctl_output_dir>`:: Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run. This parameter is optional.
`--create-private-s3-bucket`:: Specifies that the OpenID Connect (OIDC) configuration files should be stored in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL. Note that by default, the `ccoctl` utility stores the OIDC configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint. This parameter is optional.
`<policy_arn>`:: Specifies the Amazon Resource Name (ARN) of the {aws-short} IAM policy to use as the permissions boundary for the IAM roles created by the `ccoctl` utility. This parameter is optional.
+
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
====
[source,terminal]
----
$ ccoctl gcp create-all \
  --name=<name> \
  --region=<gcp_region> \
  --project=<gcp_project_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --key-storage-method=<key_storage_method>
----
+
where:
+
`<name>`:: Specifies the user-defined name for all created {gcp-short} resources used for tracking. If you plan to install the {gcp-short} Filestore Container Storage Interface (CSI) Driver Operator, retain this value.
`<gcp_region>`:: Specifies the {gcp-short} region in which cloud resources will be created.
`<gcp_project_id>`:: Specifies the {gcp-short} project ID in which cloud resources will be created.
`<path_to_credentials_requests_directory>`:: Specifies the directory containing the files of `CredentialsRequest` manifests to create {gcp-short} service accounts.
`<key_storage_method>`:: Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional.
+
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
====
[source,terminal]
----
$ ccoctl azure create-all \
  --name=<azure_infra_name> \
  --output-dir=<ccoctl_output_dir> \
  --region=<azure_region> \
  --subscription-id=<azure_subscription_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --dnszone-resource-group-name=<azure_dns_zone_resource_group_name> \
  --tenant-id=<azure_tenant_id> \
  --network-resource-group-name <azure_resource_group> \
  --preserve-existing-roles
----
+
where:
+
`<azure_infra_name>`:: Specifies the user-defined name for all created Azure resources used for tracking.
`<ccoctl_output_dir>`:: Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run. This parameter is optional.
`<azure_region>`:: Specifies the Azure region in which cloud resources will be created.
`<azure_subscription_id>`:: Specifies the Azure subscription ID to use.
`<path_to_credentials_requests_directory>`:: Specifies the directory containing the files for the component `CredentialsRequest` objects.
`<azure_dns_zone_resource_group_name>`:: Specifies the name of the resource group containing the cluster's base domain Azure DNS zone.
`<azure_tenant_id>`:: Specifies the Azure tenant ID to use.
`<azure_resource_group>`:: Specifies the virtual network resource group if it is different from the cluster resource group. This parameter is optional.
`--preserve-existing-roles`:: Specifies that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates. This parameter is optional.
+
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

To see additional optional parameters and explanations of how to use them, run the `azure create-all --help` command.
====

.Verification

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:
+
[source,terminal]
----
$ ls <path_to_ccoctl_output_dir>/manifests
----
+
.Example output
[source,text]
----
cluster-authentication-02-config.yaml
openshift-cloud-credential-operator-cloud-credential-operator-iam-ro-creds-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capa-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-ebs-cloud-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-aws-cloud-credentials-credentials.yaml
----
+
You can verify that the IAM roles are created by querying AWS. For more information, refer to AWS documentation on listing IAM roles.
+
.Example output
[source,text]
----
cluster-authentication-02-config.yaml
openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-gcp-cloud-credentials-credentials.yaml
----
+
You can verify that the IAM service accounts are created by querying {gcp-short}. For more information, refer to {gcp-short} documentation on listing IAM service accounts.
+
.Example output
[source,text]
----
azure-ad-pod-identity-webhook-config.yaml
cluster-authentication-02-config.yaml
openshift-cloud-controller-manager-azure-cloud-credentials-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capz-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-azure-disk-credentials-credentials.yaml
openshift-cluster-csi-drivers-azure-file-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-azure-cloud-credentials-credentials.yaml
----
+
You can verify that the Microsoft Entra ID service accounts are created by querying Azure. For more information, refer to Azure documentation on listing Entra ID service accounts.

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

//Task part 2b: Creating the required AWS resources individually
// Module included in the following assemblies:
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc

[id="cco-ccoctl-creating-individually_{context}"]
= Creating AWS resources individually

You can use the `ccoctl` tool to create AWS resources individually. This option might be useful for an organization that shares the responsibility for creating these resources among different users or departments.

Otherwise, you can use the `ccoctl aws create-all` command to create the AWS resources automatically. For more information, see "Creating AWS resources with a single command".

[NOTE]
====
By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

Some `ccoctl` commands make AWS API calls to create or modify AWS resources. You can use the `--dry-run` flag to avoid making API calls. Using this flag creates JSON files on the local file system instead. You can review and modify the JSON files and then apply them with the AWS CLI tool using the `--cli-input-json` parameters.
====

.Prerequisites

* Extract and prepare the `ccoctl` binary.

.Procedure

. Generate the public and private RSA key files that are used to set up the OpenID Connect provider for the cluster by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-key-pair
----
+
.Example output
[source,text]
----
2021/04/13 11:01:02 Generating RSA keypair
2021/04/13 11:01:03 Writing private key to /<path_to_ccoctl_output_dir>/serviceaccount-signer.private
2021/04/13 11:01:03 Writing public key to /<path_to_ccoctl_output_dir>/serviceaccount-signer.public
2021/04/13 11:01:03 Copying signing key for use by installer
----
+
where `serviceaccount-signer.private` and `serviceaccount-signer.public` are the generated key files.
+
This command also creates a private key that the cluster requires during installation in `/<path_to_ccoctl_output_dir>/tls/bound-service-account-signing-key.key`.

. Create an OpenID Connect identity provider and S3 bucket on AWS by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-identity-provider \
  --name=<name> \// <1>
  --region=<aws_region> \// <2>
  --public-key-file=<path_to_ccoctl_output_dir>/serviceaccount-signer.public <3>
----
<1> `<name>` is the name used to tag any cloud resources that are created for tracking.
<2> `<aws-region>` is the AWS region in which cloud resources will be created.
<3> `<path_to_ccoctl_output_dir>` is the path to the public key file that the `ccoctl aws create-key-pair` command generated.
+
.Example output
[source,text]
----
2021/04/13 11:16:09 Bucket <name>-oidc created
2021/04/13 11:16:10 OpenID Connect discovery document in the S3 bucket <name>-oidc at .well-known/openid-configuration updated
2021/04/13 11:16:10 Reading public key
2021/04/13 11:16:10 JSON web key set (JWKS) in the S3 bucket <name>-oidc at keys.json updated
2021/04/13 11:16:18 Identity Provider created with ARN: arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com
----
+
where `openid-configuration` is a discovery document and `keys.json` is a JSON web key set file.
+
This command also creates a YAML configuration file in `/<path_to_ccoctl_output_dir>/manifests/cluster-authentication-02-config.yaml`. This file sets the issuer URL field for the service account tokens that the cluster generates, so that the AWS IAM identity provider trusts the tokens.

. Create IAM roles for each component in the cluster:

.. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----

.. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \// <1>
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \// <2>
  --to=<path_to_directory_for_credentials_requests> <3>
----
<1> The `--included` parameter includes only the manifests that your specific cluster configuration requires.
<2> Specify the location of the `install-config.yaml` file.
<3> Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

.. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-iam-roles \
  --name=<name> \
  --region=<aws_region> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --identity-provider-arn=arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com
----
+
[NOTE]
====
For AWS environments that use alternative IAM API endpoints, such as GovCloud, you must also specify your region with the `--region` parameter.

If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
====
+
For each `CredentialsRequest` object, `ccoctl` creates an IAM role with a trust policy that is tied to the specified OIDC identity provider, and a permissions policy as defined in each `CredentialsRequest` object from the OpenShift Container Platform release image.

.Verification

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:
+
[source,terminal]
----
$ ls <path_to_ccoctl_output_dir>/manifests
----
+
.Example output
[source,text]
----
cluster-authentication-02-config.yaml
openshift-cloud-credential-operator-cloud-credential-operator-iam-ro-creds-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capa-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-ebs-cloud-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-aws-cloud-credentials-credentials.yaml
----
+
You can verify that the IAM roles are created by querying AWS. For more information, refer to AWS documentation on listing IAM roles.

//Task part 3: Incorporating the Cloud Credential Operator utility manifests
// Module included in the following assemblies:
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//global Azure install assemblies

//GCP install assemblies

[id="cco-ccoctl-install-creating-manifests_{context}"]
= Incorporating the Cloud Credential Operator utility manifests

[role="_abstract"]
To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

.Prerequisites

* You have configured an account with the cloud platform that hosts your cluster.
* You have configured the Cloud Credential Operator utility (`ccoctl`).
* You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

.Procedure

. Add the following granular permissions to the {gcp-short} account that the installation program uses:
+
* compute.machineTypes.list
* compute.regions.list
* compute.zones.list
* dns.changes.create
* dns.changes.get
* dns.managedZones.create
* dns.managedZones.delete
* dns.managedZones.get
* dns.managedZones.list
* dns.networks.bindPrivateDNSZone
* dns.resourceRecordSets.create
* dns.resourceRecordSets.delete
* dns.resourceRecordSets.list

. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:
+
.Sample configuration file snippet
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
----

. If you used the `ccoctl` utility to create a new Azure resource group instead of using an existing resource group, modify the `resourceGroupName` parameter in the `install-config.yaml` as shown:
+
.Sample configuration file snippet
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
# ...
platform:
  azure:
    resourceGroupName: <azure_infra_name>
# ...
----
+
The `<azure_infra_name>` value must match the user-defined name for Azure resources that was specified with the `--name` argument of the `ccoctl azure create-all` command.

. If you have not previously created installation manifest files, do so by running the following command:
+
[source,terminal]
----
$ openshift-install create manifests --dir <installation_directory>
----
+
where `<installation_directory>` is the directory in which the installation program creates files.

. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
----

. Copy the `tls` directory that contains the private key to the installation directory:
+
[source,terminal,subs="+quotes"]
----
$ cp -a /<path_to_ccoctl_output_dir>/tls .
----

//global Azure install assemblies

//GCP install assemblies

// Network Operator specific configuration
// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * networking/cluster-network-operator.adoc
// * networking/network_security/logging-network-security.adoc
// * post_installation_configuration/network-configuration.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc

// Installation assemblies need different details than the CNO operator does

[id="nw-operator-cr_{context}"]
= Cluster Network Operator configuration

[role="_abstract"]
To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`:: IP address pools from which pod IP addresses are allocated.
`serviceNetwork`:: IP address pool for services.
//Installation no longer supports SDN, so excluding it from install docs here. Deleted in 4.17.

`defaultNetwork.type`:: Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

// For the post installation assembly, no further content is provided.
[NOTE]
====
After cluster installation, you can only modify the `clusterNetwork` IP address range. The `serviceNetwork` range cannot be modified post-installation, either directly or by using the `ServiceCIDR` API.
====

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

[id="nw-operator-cr-cno-object_{context}"]
== Cluster Network Operator configuration object

The fields for the Cluster Network Operator (CNO) are described in the following table:

.Cluster Network Operator configuration object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name of the CNO object. This name is always `cluster`.

|`spec.clusterNetwork`
|`array`
|A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:

[source,yaml]
----
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/19
    hostPrefix: 23
  - cidr: fd01::/48
    hostPrefix: 64
----

If you install a cluster on {aws-short} with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.

|`spec.serviceNetwork`
|`array`
|A block of IP addresses for services. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:

[source,yaml]
----
spec:
  serviceNetwork:
  - 172.30.0.0/14
  - fd02::/112
----

If you install a cluster on {aws-short} with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.

This value is ready-only and inherited from the `Network.config.openshift.io` object named `cluster` during cluster installation.
You can customize this field only in the `install-config.yaml` file before you create the manifests. The value is read-only in the manifest file.

|`spec.defaultNetwork`
|`object`
|Configures the network plugin for the cluster network.

|`spec.additionalRoutingCapabilities.providers`
|`array`
|This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is `FRR`.

--
- `FRR`: The FRR routing provider
--

[source,yaml]
----
spec:
  additionalRoutingCapabilities:
    providers:
    - FRR
----

|====

[IMPORTANT]
====
For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes.
====

[id="nw-operator-cr-defaultnetwork_{context}"]
== defaultNetwork object configuration

The values for the `defaultNetwork` object are defined in the following table:

.`defaultNetwork` object
[cols=".^3,.^2,.^5a",options="header"]
|====
|Field|Type|Description

|`type`
|`string`
|`OVNKubernetes`. The {openshift-networking} network plugin is selected during installation. This value cannot be changed after cluster installation.
[NOTE]
====
OpenShift Container Platform uses the OVN-Kubernetes network plugin by default.
====

|`ovnKubernetesConfig`
|`object`
|This object is only valid for the OVN-Kubernetes network plugin.

|====

[id="nw-operator-configuration-parameters-for-ovn-sdn_{context}"]
== Configuration for the OVN-Kubernetes network plugin

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

.`ovnKubernetesConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`mtu`
|`integer`
|
The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.

If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.

If your cluster requires different MTU values for different nodes, you must set this value to `100` less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of `9001`, and some have an MTU of `1500`, you must set this value to `1400`.
The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This value is normally configured automatically.

|`genevePort`
|`integer`
|
The port to use for all Geneve packets. The default value is `6081`. This value cannot be changed after cluster installation.
The UDP port for the Geneve overlay network.

|`ipsecConfig`
|`object`
|
Specify a configuration object for customizing the IPsec configuration.
An object describing the IPsec mode for the cluster.

|`ipv4`
|`object`
|Specifies a configuration object for IPv4 settings.

|`ipv6`
|`object`
|Specifies a configuration object for IPv6 settings.

|`policyAuditConfig`
|`object`
|Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used.

|`routeAdvertisements`
|`string`
a|Specifies whether to advertise cluster network routes. The default value is `Disabled`.
--
- `Enabled`: Import routes to the cluster network and advertise cluster network routes as configured in `RouteAdvertisements` objects.
- `Disabled`: Do not import routes to the cluster network or advertise cluster network routes.
--

|`gatewayConfig`
|`object`
|Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are `Shared` and `Local`. The default value is `Shared`. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. If you are using hardware offloading, Red Hat recommends to use the default `Shared` gateway mode to bypass the host routing plane. In the `Local` setting, it traverses the host network; consequently, it gets applied to the routing table of the host.

[NOTE]
====
While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes.
====

|====

.`ovnKubernetesConfig.ipv4` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalTransitSwitchSubnet`
|string
|
If your existing network infrastructure overlaps with the `100.88.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.

The default value is `100.88.0.0/16`.

|`internalJoinSubnet`
|string
|
If your existing network infrastructure overlaps with the `100.64.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the `clusterNetwork.cidr` value is `10.128.0.0/14` and the `clusterNetwork.hostPrefix` value is `/23`, then the maximum number of nodes is `2^(23-14)=512`.

The default value is `100.64.0.0/16`.

|====

.`ovnKubernetesConfig.ipv6` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalTransitSwitchSubnet`
|string
|
If your existing network infrastructure overlaps with the `fd97::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.

The default value is `fd97::/64`.

|`internalJoinSubnet`
|string
|
If your existing network infrastructure overlaps with the `fd98::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.

The default value is `fd98::/64`.

|====

// tag::policy-audit[]
.`policyAuditConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`rateLimit`
|integer
|The maximum number of messages to generate every second per node. The default value is `20` messages per second.

|`maxFileSize`
|integer
|The maximum size for the audit log in bytes. The default value is `50000000` or 50 MB.

|`maxLogFiles`
|integer
|The maximum number of log files that are retained.

|`destination`
|string
|
One of the following additional audit log targets:

`libc`:: The libc `syslog()` function of the journald process on the host.
`udp:<host>:<port>`:: A syslog server. Replace `<host>:<port>` with the host and port of the syslog server.
`unix:<file>`:: A Unix Domain Socket file specified by `<file>`.
`null`:: Do not send the audit logs to any additional target.

|`syslogFacility`
|string
|The syslog facility, such as `kern`, as defined by RFC5424. The default value is `local0`.

|====
// end::policy-audit[]

[id="gatewayConfig-object_{context}"]
.`gatewayConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`routingViaHost`
|`boolean`
|Set this field to `true` to send egress traffic from pods to the host networking stack.
For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack.
By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table.
The default value is `false`.

This field has an interaction with the Open vSwitch hardware offloading feature.
If you set this field to `true`, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack.

|`ipForwarding`
|`object`
|You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the `ipForwarding` specification in the `Network` resource. Specify `Restricted` to only allow IP forwarding for Kubernetes related traffic. Specify `Global` to allow forwarding of all IP traffic. For new installations, the default is `Restricted`. For updates to OpenShift Container Platform 4.14 or later, the default is `Global`.
[NOTE]
====
The default value of `Restricted` sets the IP forwarding to drop.
====

|`ipv4`
|`object`
|Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses.

|`ipv6`
|`object`
|Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses.

|====

[id="gatewayconfig-ipv4-object_{context}"]
.`gatewayConfig.ipv4` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalMasqueradeSubnet`
|`string`
|
The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `169.254.169.0/29`.
[IMPORTANT]
====
For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.
====

|====

[id="gatewayconfig-ipv6-object_{context}"]
.`gatewayConfig.ipv6` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalMasqueradeSubnet`
|`string`
|
The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `fd69::/125`.
[IMPORTANT]
====
For OpenShift Container Platform 4.17 and later versions, clusters use `fd69::/112` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.
====

|====

[id="nw-operator-cr-ipsec_{context}"]
.`ipsecConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`mode`
|`string`
a|Specifies the behavior of the IPsec implementation. Must be one of the following values:

--
- `Disabled`: IPsec is not enabled on cluster nodes.
- `External`: IPsec is enabled for network traffic with external hosts.
- `Full`: IPsec is enabled for pod traffic and network traffic with external hosts.
--

|====

[NOTE]
====
You can only change the configuration for your cluster network plugin during cluster installation, except for the `gatewayConfig` field that can be changed at runtime as a postinstallation activity.
====

.Example OVN-Kubernetes configuration with IPSec enabled
[source,yaml]
----
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
----

[id="nw-operator-example-cr_{context}"]
== Cluster Network Operator example configuration

A complete CNO configuration is specified in the following example:

.Example Cluster Network Operator object
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc

[id="modifying-nwoperator-config-startup_{context}"]
= Specifying advanced network configuration

[role="_abstract"]
To integrate your OpenShift Container Platform cluster with your existing network environment, you can specify advanced network configuration in a manifest before you install the cluster. Advanced network configuration can be configured only during cluster installation.

[IMPORTANT]
====
Customizing your network configuration by modifying the OpenShift Container Platform manifest files created by the installation program is not supported. Applying a manifest file that you create, as in the following procedure, is supported.
====

.Prerequisites

* You have created the `install-config.yaml` file and completed any modifications to it.

.Procedure

. Change to the directory that contains the installation program and create the manifests:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
+
The `<installation_directory>` specifies the name of the directory that contains the `install-config.yaml` file for your cluster.

. Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
----

. Specify the advanced network configuration for your cluster in the `cluster-network-03-config.yml` file, such as in the following example:
+
.Enable IPsec for the OVN-Kubernetes network provider
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      ipsecConfig:
        mode: Full
----

. Optional: Back up the `manifests/cluster-network-03-config.yml` file. The
installation program consumes the `manifests/` directory when you create the
Ignition config files.

. Remove the Kubernetes manifest files that define the control plane machines and compute `MachineSets`:
+
[source,terminal]
----
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml
----
+
Because you create and manage these resources yourself, you do not have
to initialize them.
+
* You can preserve the `MachineSet` files to create compute machines by using the machine API, but you must update references to them to match your environment.

[NOTE]
====
For more information on using a Network Load Balancer (NLB) on {aws-short}, see Configuring Ingress cluster traffic on {aws-short} using a Network Load Balancer.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-traffic-aws.adoc

[id="nw-aws-nlb-new-cluster_{context}"]
= Configuring an Ingress Controller Network Load Balancer on a new AWS cluster

[role="_abstract"]
You can create an Ingress Controller backed by an {aws-full} Network Load Balancer (NLB) on a new cluster in situations where you need more transparent networking capabilities.

.Prerequisites

* Create and edit the `install-config.yaml` file. For instructions, see "Creating the installation configuration file" in the _Additonal resources_ section.

.Procedure

. Change to the directory that contains the installation program and create the manifests:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
* For `<installation_directory>`, specify the name of the directory that contains the `install-config.yaml` file for your cluster.

. Create a file that is named `cluster-ingress-default-ingresscontroller.yaml` in the `<installation_directory>/manifests/` directory:
+
[source,terminal]
----
$ touch <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
----
`<installation_directory>`:: Specifies the directory name that contains the `manifests/` directory for your cluster.

. Check the several network configuration files that exist in the `manifests/` directory by entering the following command:
+
[source,terminal]
----
$ ls <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
----
+
.Example output
[source,terminal]
----
cluster-ingress-default-ingresscontroller.yaml
----

. Open the `cluster-ingress-default-ingresscontroller.yaml` file in an editor and enter a custom resource (CR) that describes the Operator configuration you want:
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
      providerParameters:
        type: AWS
        aws:
          type: NLB
    type: LoadBalancerService
----

. Save the `cluster-ingress-default-ingresscontroller.yaml` file and quit the text editor.

. Optional: Back up the `manifests/cluster-ingress-default-ingresscontroller.yaml` file because the installation program deletes the `manifests/` directory during cluster creation.

// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
// * networking/ovn_kubernetes_network_provider/configuring-hybrid-networking.adoc

[id="configuring-hybrid-ovnkubernetes_{context}"]
= Configuring hybrid networking with OVN-Kubernetes

[role="_abstract"]
To configure hybrid networking with OVN-Kubernetes, you can set `hybridOverlayConfig` during installation or patch the Cluster Network Operator (CNO) after installation.

[NOTE]
====
This configuration is necessary to run both Linux and Windows nodes in the same cluster.
====

.Prerequisites

* You defined `OVNKubernetes` for the `networking.networkType` parameter in the `install-config.yaml` file. See the installation documentation for configuring OpenShift Container Platform network customizations on your chosen cloud provider for more information.

* Install the OpenShift CLI (`oc`).
* Log in to the cluster as a user with `cluster-admin` privileges.
* Ensure that the cluster uses the OVN-Kubernetes network plugin.

.Procedure

. Change to the directory that contains the installation program and create the manifests:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
+
For the `<installation_directory>`, specify the name of the directory that contains the `install-config.yaml` file for your cluster.

. Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory:
+
[source,terminal]
----
$ cat <<EOF > <installation_directory>/manifests/cluster-network-03-config.yml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
EOF
----
+
For `<installation_directory>`, specify the directory name that contains the `manifests/` directory for your cluster.

. Open the `cluster-network-03-config.yml` file in an editor and specify a hybrid networking configuration similar to the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      hybridOverlayConfig:
        hybridClusterNetwork:
        - cidr: 10.132.0.0/14
          hostPrefix: 23
        hybridOverlayVXLANPort: 9898
----
+
where:

`spec.defaultNetwork.ovnKubernetesConfig.hybridOverlayConfig.hybridClusterNetwork`:: Specifies the CIDR configuration used for nodes on the additional overlay network. The `hybridClusterNetwork` CIDR must not overlap with the `clusterNetwork` CIDR.
`spec.defaultNetwork.ovnKubernetesConfig.hybridOverlayConfig.hybridOverlayVXLANPort`:: Specifies a custom VXLAN port for the additional overlay network. This is required for running Windows nodes in a cluster installed on vSphere, and must not be configured for any other cloud provider. The custom port can be any open port excluding the default `6081` port. For more information on this requirement, see Pod-to-pod connectivity between hosts is broken in the Microsoft documentation.
+
[NOTE]
====
Windows Server Long-Term Servicing Channel (LTSC): Windows Server 2019 is not supported on clusters with a custom `hybridOverlayVXLANPort` value because this Windows server version does not support selecting a custom VXLAN port.
====

. Save the `cluster-network-03-config.yml` file and quit the text editor.
. Optional: Back up the `manifests/cluster-network-03-config.yml` file. The installation program deletes the `manifests/` directory when creating the cluster.

. To configure the OVN-Kubernetes hybrid network overlay, enter the following command:
+
[source,terminal]
----
$ oc patch networks.operator.openshift.io cluster --type=merge \
  -p '{
    "spec":{
      "defaultNetwork":{
        "ovnKubernetesConfig":{
          "hybridOverlayConfig":{
            "hybridClusterNetwork":[
              {
                "cidr": "<cidr>",
                "hostPrefix": <prefix>
              }
            ],
            "hybridOverlayVXLANPort": <overlay_port>
          }
        }
      }
    }
  }'
----
+
where:

`<cidr>`:: Specifies the CIDR configuration used for nodes on the additional overlay network. This CIDR must not overlap with the cluster network CIDR.
`<prefix>`:: Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.
`<overlay_port>`:: Specifies a custom VXLAN port for the additional overlay network. This is required for running Windows nodes in a cluster installed on vSphere, and must not be configured for any other cloud provider. The custom port can be any open port excluding the default `6081` port. For more information on this requirement, see Pod-to-pod connectivity between hosts is broken in the Microsoft documentation.
+
[NOTE]
====
Windows Server Long-Term Servicing Channel (LTSC): Windows Server 2019 is not supported on clusters with a custom `hybridOverlayVXLANPort` value because this Windows server version does not support selecting a custom VXLAN port.
====
+
.Example output
[source,text]
----
network.operator.openshift.io/cluster patched
----

. To confirm that the configuration is active, enter the following command. It can take several minutes for the update to apply.
+
[source,terminal]
----
$ oc get network.operator.openshift.io -o jsonpath="{.items[0].spec.defaultNetwork.ovnKubernetesConfig}"
----

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

[id="installation-aws-provisioning-own-dns-records_{context}"]
= Provisioning your own DNS records

[role="_abstract"]
Use your cluster name and base cluster domain to configure a CNAME record for the API service `api.<cluster_name>.<base_domain>.` with the API load balancer DNS name. Similarly, use the load balancer DNS name of the Ingress service to provision a CNAME record for the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

.Prerequisites
* You have installed the {aws-short} CLI.

.Procedure

. Add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

. Install your cluster.

. If you are installing a private cluster, set the `api_lb_name` variable by running the following command:
+
[source,terminal]
----
$ api_lb_name="${INFRA_ID}-int"
----

. If you are installing a public cluster, set the `api_lb_name` variable by running the following command:
+
[source,terminal]
----
$ api_lb_name="${INFRA_ID}-ext"
----

. To retrieve the DNS name of the API service, run the following command:
+
[source,terminal]
----
$ aws --region ${REGION} elbv2 describe-load-balancers --names ${api_lb_name} --query 'LoadBalancers[*].DNSName' --output text
----

. Use the DNS name and your cluster name and base cluster domain to configure your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname.

. To retrieve the DNS name of the Ingress service, run the following command:
+
[source,terminal]
----
$ ingress_lb_name=$(aws --region ${REGION} resourcegroupstaggingapi get-resources --resource-type-filters elasticloadbalancing:loadbalancer --tag-filters Key=kubernetes.io/cluster/${INFRA_ID},Values=owned Key=kubernetes.io/service-name,Values=openshift-ingress/router-default --query 'ResourceTagMappingList[*].ResourceARN | [0]' --output text | awk -F'/' '{print $2}')
----

. Run the following command, which uses the variable `ingress_lb_name` generated from the previous command:
+
[source,terminal]
----
$ aws --region ${REGION} elb describe-load-balancers --load-balancer-names ${ingress_lb_name} --query 'LoadBalancerDescriptions[].DNSName' --output text
----

. Use the DNS name and your cluster name and base cluster domain to configure your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname.

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
// * installing/installing_aws/installing-aws-china.adoc.
// * installing/installing_aws/installing-aws-secret-region.adoc
// *installing/validation_and_troubleshooting/validating-an-installation.adoc
// *installing/installing_aws/installing-aws-user-infra.adoc
// *installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// *installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing_aws/installing-aws-wavelength-zone.adoc

[id="logging-in-by-using-the-web-console_{context}"]
= Logging in to the cluster by using the web console

The `kubeadmin` user exists by default after an OpenShift Container Platform installation. You can log in to your cluster as the `kubeadmin` user by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to the installation host.
* You completed a cluster installation and all cluster Operators are available.

.Procedure

. Obtain the password for the `kubeadmin` user from the `kubeadmin-password` file on the installation host:
+
[source,terminal]
----
$ cat <installation_directory>/auth/kubeadmin-password
----
+
[NOTE]
====
Alternatively, you can obtain the `kubeadmin` password from the `<installation_directory>/.openshift_install.log` log file on the installation host.
====

. List the OpenShift Container Platform web console route:
+
[source,terminal]
----
$ oc get routes -n openshift-console | grep 'console-openshift'
----
+
[NOTE]
====
Alternatively, you can obtain the OpenShift Container Platform route from the `<installation_directory>/.openshift_install.log` log file on the installation host.
====
+
.Example output
[source,terminal]
----
console     console-openshift-console.apps.<cluster_name>.<base_domain>            console     https   reencrypt/Redirect   None
----

. Navigate to the route detailed in the output of the preceding command in a web browser and log in as the `kubeadmin` user.

[role="_additional-resources"]
.Additional resources

* Accessing the web console

== Next steps

* Validating an installation.
* Customize your cluster.
* If necessary, you can Remote health reporting.
* If necessary, you can remove cloud provider credentials.
