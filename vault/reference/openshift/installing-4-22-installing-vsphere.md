---
title: "Installing a cluster on vSphere with user-provisioned infrastructure"
type: reference
domain: openshift
slug: installing-4-22-installing-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-vsphere
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on vSphere with user-provisioned infrastructure

[id="installing-vsphere"]
= Installing a cluster on vSphere with user-provisioned infrastructure

In OpenShift Container Platform version , you can install a cluster on
VMware vSphere infrastructure that you provision.

[IMPORTANT]
====
The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the vSphere platform and the installation process of OpenShift Container Platform. Use the user-provisioned infrastructure installation instructions as a guide; you are free to create the required resources through other methods.
====

[id="prerequisites_installing-vsphere_{context}"]
== Prerequisites

* You have completed the tasks in Preparing to install a cluster using user-provisioned infrastructure.
* You reviewed your VMware platform licenses. Red{nbsp}Hat does not place any restrictions on your VMware licenses, but some VMware infrastructure components require licensing.
* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You provisioned persistent storage for your cluster. To deploy a private image registry, your storage must provide `ReadWriteMany` access modes.
* Completing the installation requires that you upload the {op-system-first} OVA on vSphere hosts. The machine from which you complete this process requires access to port 443 on the vCenter and ESXi hosts. You verified that port 443 is accessible.
* If you use a firewall, you confirmed with the administrator that port 443 is accessible. Control plane nodes must be able to reach vCenter and ESXi hosts on port 443 for the installation to succeed.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.
+
[NOTE]
====
Be sure to also review this site list if you are configuring a proxy.
====

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

// Module included in the following assemblies:
//
//* installing/installing-vsphere-installer-provisioned-customizations.adoc [IPI]
//* installing/installing-vsphere.adoc [UPI]
//* installing/installing-vsphere-network-customizations.adoc [UPI]
//* installing/installing-restricted-networks-installer-provisioned-vsphere.adoc [IPI]
//* installing/installing-restricted-networks-vsphere.adoc [IPI]

[id="installation-vsphere-regions-zones_{context}"]
= VMware vSphere region and zone enablement

You can deploy an OpenShift Container Platform cluster to multiple vSphere data centers. Each data center can run multiple clusters. This configuration reduces the risk of a hardware failure or network outage that can cause your cluster to fail. To enable regions and zones, you must define multiple failure domains for your OpenShift Container Platform cluster.

[IMPORTANT]
====
The VMware vSphere region and zone enablement feature requires the vSphere Container Storage Interface (CSI) driver as the default storage driver in the cluster. As a result, the feature is only available on a newly installed cluster.

For a cluster that was upgraded from a previous release, you must enable CSI automatic migration for the cluster. You can then configure multiple regions and zones for the upgraded cluster.
====

The default installation configuration deploys a cluster to a single vSphere data center. If you want to deploy a cluster to multiple vSphere data centers, you must create an installation configuration file that enables the region and zone feature.

The default `install-config.yaml` file includes `vcenters` and `failureDomains` fields, where you can specify multiple vSphere data centers and clusters for your OpenShift Container Platform cluster. You can use the default `failureDomains` from `install-config.yaml` if you want to install an OpenShift Container Platform cluster in a vSphere environment that consists of single data center.

The following list describes terms associated with defining zones and regions for your cluster:

* Failure domain: Establishes the relationships between a region and zone. You define a failure domain by using vCenter objects, such as a `datastore` object. A failure domain defines the vCenter location for OpenShift Container Platform cluster nodes.
* Region: Specifies a vCenter data center. You define a region by using a tag from the  `openshift-region` tag category.
* Zone: Specifies a vCenter cluster. You define a zone by using a tag from the `openshift-zone` tag category.

[NOTE]
====
If you plan on specifying more than one failure domain in your `install-config.yaml` file, you must create tag categories, zone tags, and region tags in advance of creating the configuration file.
====

You must create a vCenter tag for each vCenter data center, which represents a region. Additionally, you must create a vCenter tag for each cluster than runs in a data center, which represents a zone. After you create the tags, you must attach each tag to their respective data centers and clusters.

The following table outlines an example of the relationship among regions, zones, and tags for a configuration with multiple vSphere data centers running in a single VMware vCenter.

[cols="2,2a,4a",options="header"]
|===
|Data center (region)| Cluster (zone)| Tags

.4+|us-east

.2+|us-east-1
|us-east-1a
|us-east-1b
.2+|us-east-2
|us-east-2a
|us-east-2b

.4+|us-west
.2+|us-west-1
|us-west-1a
|us-west-1b
.2+|us-west-2
|us-west-2a
|us-west-2b
|===

[role="_additional-resources"]
.Additional resources

* Additional VMware vSphere configuration parameters

* Deprecated VMware vSphere configuration parameters

* vSphere automatic migration

* VMware vSphere CSI Driver Operator

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
* Installation configuration parameters

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc

[id="installation-vsphere-config-yaml_{context}"]
= Sample install-config.yaml file for a {vmw-first} cluster

[role="_abstract"]
You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster's platform or change the values of the required parameters.

[IMPORTANT]
====
Carefully review the "Installation configuration parameters for {vmw-short}" page for detailed parameter explanations.
====

[source,yaml]
----
apiVersion: v1
baseDomain: example.com
metadata:
  name: test
sshKey: ssh-ed25519 AAAA...
compute:
- name:  <worker_name>
  platform: {}
  replicas: 0
  replicas: 3
controlPlane:
  name: <control_plane_name>
  platform: {}
  replicas: 3
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  vsphere:
    apiVIPs:
    - 10.0.0.1
    ingressVIPs:
    - 10.0.0.2
    failureDomains:
    - name: <failure_domain_name>
      region: <default_region_name>
      server: <fully_qualified_domain_name>
      topology:
        computeCluster: "/<data_center>/host/<cluster>"
        datacenter: <data_center>
        datastore: "/<data_center>/datastore/<datastore>"
        networks:
        - <VM_Network_name>
      zone: <default_zone_name>
    vcenters:
    - datacenters:
      - <data_center>
      server: <fully_qualified_domain_name>
      user: administrator@vsphere.local
----
where:

`compute`:: Specifes the parameters that apply to compute nodes.
`controlPlane`:: Specifies the parameters that apply to control plane nodes.
`networking`:: Specifies the parameters that apply to cluster networking configuration.
`platform`:: Specifies the parameters that apply to the configuration of the platform hosting the cluster.

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

//include::modules/installation-three-node-cluster.adoc[leveloffset=+2]

// Module included in the following assemblies:
//
//* installing/Installing-vsphere-installer-provisioned-customizations.adoc [IPI]
//* installing/installing-vsphere.adoc [UPI]
//* installing/installing-vsphere-network-customizations.adoc [UPI]
//* installing/installing-restricted-networks-installer-provisioned-vsphere.adoc [IPI]
//* installing/installing-restricted-networks-vsphere.adoc [IPI]

[id="configuring-vsphere-regions-zones_{context}"]
= Configuring regions and zones for a VMware vCenter

You can modify the default installation configuration file, so that you can deploy an OpenShift Container Platform cluster to multiple vSphere data centers.

The default `install-config.yaml` file configuration from the previous release of OpenShift Container Platform is deprecated. You can continue to use the deprecated default configuration, but the `openshift-installer` will prompt you with a warning message that indicates the use of deprecated fields in the configuration file.

.Prerequisites
* You have an existing `install-config.yaml` installation configuration file.
+
[IMPORTANT]
====
You must specify at least one failure domain for your OpenShift Container Platform cluster, so that you can provision data center objects for your VMware vCenter server. Consider specifying multiple failure domains if you need to provision virtual machine nodes in different data centers, clusters, datastores, and other components. To enable regions and zones, you must define multiple failure domains for your OpenShift Container Platform cluster.
====
+
* You have installed the `govc` command line tool.
+
[IMPORTANT]
====
The example uses the `govc` command. The `govc` command is an open source command available from VMware; it is not available from Red{nbsp}Hat. The Red{nbsp}Hat support team does not maintain the `govc` command. Instructions for downloading and installing `govc` are found on the VMware documentation website.
====

.Procedure

. Create the `openshift-region` and `openshift-zone` vCenter tag categories by running the following commands:
+
[IMPORTANT]
====
If you specify different names for the `openshift-region` and `openshift-zone` vCenter tag categories, the installation of the OpenShift Container Platform cluster fails.
====
+
[source,terminal]
----
$ govc tags.category.create -d "OpenShift region" openshift-region
----
+
[source,terminal]
----
$ govc tags.category.create -d "OpenShift zone" openshift-zone
----

. For each region where you want to deploy your cluster, create a region tag by running the following command:
+
[source,terminal]
----
$ govc tags.create -c <region_tag_category> <region_tag>
----

. For each zone where you want to deploy your cluster, create a zone tag by running the following command:
+
[source,terminal]
----
$ govc tags.create -c <zone_tag_category> <zone_tag>
----

. Attach region tags to each vCenter data center object by running the following command:
+
[source,terminal]
----
$ govc tags.attach -c <region_tag_category> <region_tag_1> /<data_center_1>
----

. Attach the zone tags to each vCenter cluster object by running the following command:
+
[source,terminal]
----
$ govc tags.attach -c <zone_tag_category> <zone_tag_1> /<data_center_1>/host/<cluster1>
----

. Change to the directory that contains the installation program and initialize the cluster deployment according to your chosen installation requirements.
+
.Sample `install-config.yaml` file with multiple data centers defined in a vSphere center

[source,yaml]
----
# ...
compute:
---
  vsphere:
      zones:
        - "<machine_pool_zone_1>"
        - "<machine_pool_zone_2>"
# ...
controlPlane:
# ...
vsphere:
      zones:
        - "<machine_pool_zone_1>"
        - "<machine_pool_zone_2>"
# ...
platform:
  vsphere:
    vcenters:
# ...
    datacenters:
      - <data_center_1_name>
      - <data_center_2_name>
    failureDomains:
    - name: <machine_pool_zone_1>
      region: <region_tag_1>
      zone: <zone_tag_1>
      server: <fully_qualified_domain_name>
      topology:
        datacenter: <data_center_1>
        computeCluster: "/<data_center_1>/host/<cluster1>"
        networks:
        - <VM_Network1_name>
        datastore: "/<data_center_1>/datastore/<datastore1>"
        resourcePool: "/<data_center_1>/host/<cluster1>/Resources/<resourcePool1>"
        folder: "/<data_center_1>/vm/<folder1>"
    - name: <machine_pool_zone_2>
      region: <region_tag_2>
      zone: <zone_tag_2>
      server: <fully_qualified_domain_name>
      topology:
        datacenter: <data_center_2>
        computeCluster: "/<data_center_2>/host/<cluster2>"
        networks:
        - <VM_Network2_name>
        datastore: "/<data_center_2>/datastore/<datastore2>"
        resourcePool: "/<data_center_2>/host/<cluster2>/Resources/<resourcePool2>"
        folder: "/<data_center_2>/vm/<folder2>"
# ...
----

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

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc

[id="installation-extracting-infraid_{context}"]
= Extracting the infrastructure name

[role="_abstract"]
The Ignition config files contain a unique cluster identifier that you can use to uniquely identify your cluster in {cp-first}. The infrastructure name is also used to locate the appropriate {cp} resources during an OpenShift Container Platform installation.
The provided {cp-template} templates contain references to this infrastructure name, so you must extract it.

The Ignition config files contain a unique cluster identifier that you can use to uniquely identify your cluster in {cp-first}. The provided {cp-template-first} ({cp-template}) templates contain references to this infrastructure name, so you must extract it.

The Ignition config files contain a unique cluster identifier that you can use to
uniquely identify your cluster in {cp-first}. If you plan to use the cluster identifier as the name of your virtual machine folder, you must extract it.

[WARNING]
====
Do not run the `openshift-install create manifests` command again after creating any {gcp-short} resources. Running the command again generates a new cluster identifier, which will cause errors in existing resources. If you need to regenerate the manifests because you modified the `install-config.yaml` file, delete any {gcp-short} resources you created and recreate them with the new cluster identifier.
====

.Prerequisites
* You obtained the OpenShift Container Platform installation program and the pull secret for your cluster.
* You generated the Ignition config files for your cluster.
* You installed the `jq` package.

.Procedure

* To extract and view the infrastructure name from the Ignition config file
metadata, run the following command:
+
[source,terminal]
----
$ jq -r .infraID <installation_directory>/metadata.json
----
+
For `<installation_directory>`, specify the path to the directory that you stored the installation files in.
+
.Example output
[source,terminal]
----
$ openshift-vw9j6
----
+
The output of this command is your cluster name and a random string.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc

[id="installation-vsphere-machines_{context}"]
= Installing {op-system} and starting the OpenShift Container Platform bootstrap process

To install OpenShift Container Platform on user-provisioned infrastructure on VMware vSphere, you must install {op-system-first} on vSphere hosts. When you install {op-system}, you must provide the Ignition config file that was generated by the OpenShift Container Platform installation program for the type of machine you are installing. If you have configured suitable networking, DNS, and load balancing infrastructure, the OpenShift Container Platform bootstrap process begins automatically after the {op-system} machines have rebooted.

.Prerequisites

* You have obtained the Ignition config files for your cluster.
* You have access to an HTTP server that you can access from your computer and that the machines that you create can access.
* You have created a vSphere cluster.

.Procedure

. Upload the bootstrap Ignition config file, which is named `<installation_directory>/bootstrap.ign`, that the installation program created to your HTTP server. Note the URL of this file.
+
. Save the following secondary Ignition config file for your bootstrap node to your computer as `<installation_directory>/merge-bootstrap.ign`:
+
[source,text]
----
{
  "ignition": {
    "config": {
      "merge": [
        {
          "source": "<bootstrap_ignition_config_url>", <1>
          "verification": {}
        }
      ]
    },
    "timeouts": {},
    "version": "3.2.0"
  },
  "networkd": {},
  "passwd": {},
  "storage": {},
  "systemd": {}
}
----
+
<1> Specify the URL of the bootstrap Ignition config file that you hosted.
+
When you create the virtual machine (VM) for the bootstrap machine, you use this Ignition config file.
+
. Locate the following Ignition config files that the installation program created:
+
* `<installation_directory>/master.ign`
* `<installation_directory>/worker.ign`
* `<installation_directory>/merge-bootstrap.ign`
+
. Convert the Ignition config files to Base64 encoding. Later in this procedure, you must add these files to the extra configuration parameter `guestinfo.ignition.config.data` in your VM.
+
For example, if you use a Linux operating system, you can use the `base64` command to encode the files.
+
[source,terminal]
----
$ base64 -w0 <installation_directory>/master.ign > <installation_directory>/master.64
----
+
[source,terminal]
----
$ base64 -w0 <installation_directory>/worker.ign > <installation_directory>/worker.64
----
+
[source,terminal]
----
$ base64 -w0 <installation_directory>/merge-bootstrap.ign > <installation_directory>/merge-bootstrap.64
----
+
[IMPORTANT]
====
If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
====

. Obtain the {op-system} OVA image. Images are available from the {op-system} image mirror page.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform. You must download an image with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image version that matches your OpenShift Container Platform version if it is available.
====
+
The filename contains the OpenShift Container Platform version number in the format `rhcos-vmware.<architecture>.ova`.
. Obtain the {op-system} images from the {op-system} Downloads page

. In the vSphere Client, create a folder in your data center to store your VMs.
.. Click the *VMs and Templates* view.
.. Right-click the name of your data center.
.. Click *New Folder* -> *New VM and Template Folder*.
.. In the window that is displayed, enter the folder name. If you did not specify an existing folder in the `install-config.yaml` file, then create a folder with the same name as the infrastructure ID. You use this folder name so vCenter dynamically provisions storage in the appropriate location for its Workspace configuration.

. In the vSphere Client, create a template for the OVA image and then clone the template as needed.
+
[NOTE]
====
In the following steps, you create a template and then clone the template for all of your cluster machines. You then provide the location for the Ignition config file for that cloned machine type when you provision the VMs.
====
.. From the *Hosts and Clusters* tab, right-click your cluster name and select *Deploy OVF Template*.
.. On the *Select an OVF* tab, specify the name of the {op-system} OVA file that you downloaded.
.. On the *Select a name and folder* tab, set a *Virtual machine name* for your template, such as `Template-{op-system}`. Click the name of your vSphere cluster and select the folder you created in the previous step.
.. On the *Select a compute resource* tab, click the name of your vSphere cluster.
.. On the *Select storage* tab, configure the storage options for your VM.
*** Select *Thin Provision* or *Thick Provision*, based on your storage preferences.
*** Select the datastore that you specified in your `install-config.yaml` file.
*** If you want to encrypt your virtual machines, select *Encrypt this virtual machine*. See the section titled "Requirements for encrypting virtual machines" for more information.
.. On the *Select network* tab, specify the network that you configured for the cluster, if available.
.. When creating the OVF template, do not specify values on the *Customize template* tab or configure the template any further.
+
[IMPORTANT]
====
Do not start the original VM template. The VM template must remain off and must be cloned for new {op-system} machines. Starting the VM template configures the VM template as a VM on the platform, which prevents it from being used as a template that compute machine sets can apply configurations to.
//This admonition note also appears in `modules/installation-vsphere-machines.adoc` and `modules/windows-machineset-vsphere.adoc`.
====

. Optional: Update the configured virtual hardware version in the VM template, if necessary. Follow Upgrading a virtual machine to the latest hardware version in the VMware documentation for more information.
+
[IMPORTANT]
====
It is recommended that you update the hardware version of the VM template to version 15 before creating VMs from it, if necessary. Using hardware version 13 for your cluster nodes running on vSphere is now deprecated. If your imported template defaults to hardware version 13, you must ensure that your ESXi host is on 6.7U3 or later before upgrading the VM template to hardware version 15. If your vSphere version is less than 6.7U3, you can skip this upgrade step; however, a future version of OpenShift Container Platform is scheduled to remove support for hardware version 13 and vSphere versions less than 6.7U3.
====

. After the template deploys, deploy a VM for a machine in the cluster.
.. Right-click the template name and click *Clone* -> *Clone to Virtual Machine*.

.. On the *Select a name and folder* tab, specify a name for the VM. You might include the machine type in the name, such as `control-plane-0` or `compute-1`.
+
[NOTE]
====
Ensure that all virtual machine names across a vSphere installation are unique.
====
.. On the *Select a name and folder* tab, select the name of the folder that you created for the cluster.

.. On the *Select a compute resource* tab, select the name of a host in your data center.
+
.. On the *Select clone options* tab, select *Customize this virtual machine's hardware*.

.. On the *Customize hardware* tab, click *Advanced Parameters*.
+
[IMPORTANT]
====
The following configuration suggestions are for example purposes only. As a cluster administrator, you must configure resources according to the resource demands placed on your cluster. To best manage cluster resources, consider creating a resource pool from the cluster's root resource pool.
====
+
*** Optional: Override default DHCP networking in vSphere. To enable static IP networking:
+
**** Set your static IP configuration:
+
.Example command
[source,terminal]
----
$ export IPCFG="ip=<ip>::<gateway>:<netmask>:<hostname>:<iface>:none nameserver=srv1 [nameserver=srv2 [nameserver=srv3 [...]]]"
----
+
.Example command
[source,terminal]
----
$ export IPCFG="ip=192.168.100.101::192.168.100.254:255.255.255.0:::none nameserver=8.8.8.8"
----
+
**** Set the `guestinfo.afterburn.initrd.network-kargs` property before you boot a VM from an OVA in vSphere:
+
.Example command
[source,terminal]
----
$ govc vm.change -vm "<vm_name>" -e "guestinfo.afterburn.initrd.network-kargs=${IPCFG}"
----
+
*** Add the following configuration parameter names and values by specifying data in the *Attribute* and *Values* fields. Ensure that you select the *Add* button for each parameter that you create.
**** `guestinfo.ignition.config.data`: Locate the base-64 encoded files that you created previously in this procedure, and paste the contents of the base64-encoded Ignition config file for this machine type.
**** `guestinfo.ignition.config.data.encoding`: Specify `base64`.
**** `disk.EnableUUID`: Specify `TRUE`.
**** `stealclock.enable`: If this parameter was not defined, add it and specify `TRUE`.
**** Create a child resource pool from the cluster's root resource pool. Perform resource allocation in this child resource pool.

.. In the *Virtual Hardware* panel of the *Customize hardware* tab, modify the specified values as required. Ensure that the amount of RAM, CPU, and disk storage meets the minimum requirements for the
machine type.

.. Complete the remaining configuration steps. On clicking the *Finish* button, you have completed the cloning operation.
.. From the *Virtual Machines* tab, right-click on your VM and then select *Power* -> *Power On*.

.. Check the console output to verify that Ignition ran.
+
.Example command
[source,terminal]
----
Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
Ignition: user-provided config was applied
----

.Next steps

* Create the rest of the machines for your cluster by following the preceding steps for each machine.
+
[IMPORTANT]
====
You must create the bootstrap and control plane machines at this time. Because some pods are deployed on compute machines by default, also create at least two compute machines before you install the cluster.
====

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * machine_management/user_infra/adding-vsphere-compute-user-infra.adoc

[id="machine-vsphere-machines_{context}"]
= Adding more compute machines to a cluster in vSphere

You can add more compute machines to a user-provisioned OpenShift Container Platform cluster on VMware vSphere.

After your vSphere template deploys in your OpenShift Container Platform cluster, you can deploy a virtual machine (VM) for a machine in that cluster.

[NOTE]
====
If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.
====

.Prerequisites

* Obtain the base64-encoded Ignition file for your compute machines.
* You have access to the vSphere template that you created for your cluster.

.Procedure

. Right-click the template's name and click *Clone* -> *Clone to Virtual Machine*.

. On the *Select a name and folder* tab, specify a name for the VM. You might include the machine type in the name, such as `compute-1`.
+
[NOTE]
====
Ensure that all virtual machine names across a vSphere installation are unique.
====

. On the *Select a name and folder* tab, select the name of the folder that you created for the cluster.

. On the *Select a compute resource* tab, select the name of a host in your data center.

. On the *Select storage* tab, select storage for your configuration and disk files.

. On the *Select clone options* tab, select *Customize this virtual machine's hardware*.

. On the *Customize hardware* tab, click *Advanced Parameters*.
** Add the following configuration parameter names and values by specifying data in the *Attribute* and *Values* fields. Ensure that you select the *Add* button for each parameter that you create.
*** `guestinfo.ignition.config.data`: Paste the contents of the base64-encoded compute Ignition config file for this machine type.
*** `guestinfo.ignition.config.data.encoding`: Specify `base64`.
*** `disk.EnableUUID`: Specify `TRUE`.

. In the *Virtual Hardware* panel of the *Customize hardware* tab, modify the specified values as required. Ensure that the amount of RAM, CPU, and disk storage meets the minimum requirements for the machine type. If many networks exist, select *Add New Device* > *Network Adapter*, and then enter your network information in the fields provided by the *New Network* menu item.

. Complete the remaining configuration steps. On clicking the *Finish* button, you have completed the cloning operation.

. From the *Virtual Machines* tab, right-click on your VM and then select *Power* -> *Power On*.

.Next steps

* Continue to create more compute machines for your cluster.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc

// This content was sourced from the bare metal RHCOS assembly file `modules/installation-user-infra-machines-advanced.adoc` under the `== Disk partitioning` subheader. "Disk partioning" content in the bare metal assembly is not modularized, so anything in this vsphere module should be checked against that file for consistency until such time that the large bare metal assembly can be modularized.

[id="installation-disk-partitioning_{context}"]
= Disk partitioning

In most cases, data partitions are originally created by installing {op-system}, rather than by installing another operating system. In such cases, the OpenShift Container Platform installer should be allowed to configure your disk partitions.

However, there are two cases where you might want to intervene to override the default partitioning when installing an
OpenShift Container Platform node:

* Create separate partitions: For greenfield installations on an empty
disk, you might want to add separate storage to a partition. This is
officially supported for making `/var` or a subdirectory of `/var`, such as `/var/lib/etcd`, a separate partition, but not both.
+
[IMPORTANT]
====
For disk sizes larger than 100GB, and especially disk sizes larger than 1TB, create a separate `/var` partition. See "Creating a separate `/var` partition" and this Red Hat Knowledgebase article for more information.
====
+
[IMPORTANT]
====
Kubernetes supports only two file system partitions. If you add more than one partition to the original configuration, Kubernetes cannot monitor all of them.
====
* Retain existing partitions: For a brownfield installation where you are reinstalling OpenShift Container Platform on an existing node and want to retain data partitions installed from your previous operating system, there are both boot arguments and options to `coreos-installer` that allow you to retain existing data partitions.

= Creating a separate `/var` partition

In general, disk partitioning for OpenShift Container Platform should be left to the
installer. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach
storage to either the `/var` partition or a subdirectory of `/var`.
For example:

* `/var/lib/containers`: Holds container-related content that can grow
as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.
+
[IMPORTANT]
====
For disk sizes larger than 100GB, and especially larger than 1TB, create a separate `/var` partition.
====

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date and keep that data intact. With this method, you will not have to pull all your containers again, nor will you have to copy massive log files when you update systems.

Because `/var` must be in place before a fresh installation of
{op-system-first}, the following procedure sets up the separate `/var` partition
by creating a machine config manifest that is inserted during the `openshift-install`
preparation phases of an OpenShift Container Platform installation.

.Procedure

. Create a directory to hold the OpenShift Container Platform installation files:
+
[source,terminal]
----
$ mkdir $HOME/clusterconfig
----

. Run `openshift-install` to create a set of files in the `manifest` and
`openshift` subdirectories. Answer the system questions as you are prompted:
+
[source,terminal]
----
$ openshift-install create manifests --dir $HOME/clusterconfig
? SSH Public Key ...
$ ls $HOME/clusterconfig/openshift/
99_kubeadmin-password-secret.yaml
99_openshift-cluster-api_master-machines-0.yaml
99_openshift-cluster-api_master-machines-1.yaml
99_openshift-cluster-api_master-machines-2.yaml
...
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
  - device: /dev/disk/by-id/<device_name> <1>
    partitions:
    - label: var
      start_mib: <partition_start_offset> <2>
      size_mib: <partition_size> <3>
      number: 5
  filesystems:
    - device: /dev/disk/by-partlabel/var
      path: /var
      format: xfs
      mount_options: [defaults, prjquota] <4>
      with_mount_unit: true
----
+
<1> The storage device name of the disk that you want to partition.
<2> When adding a data partition to the boot disk, a minimum value of 25000 mebibytes is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of {op-system} might overwrite the beginning of the data partition.
<3> The size of the data partition in mebibytes.
<4> The `prjquota` mount option must be enabled for filesystems used for container storage.
+
[NOTE]
====
When creating a separate `/var` partition, you cannot use different instance types for worker nodes, if the different instance types do not have the same device name.
====

. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:
+
[source,terminal]
----
$ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
----

. Run `openshift-install` again to create Ignition configs from a set of files in the `manifest` and `openshift` subdirectories:
+
[source,terminal]
----
$ openshift-install create ignition-configs --dir $HOME/clusterconfig
$ ls $HOME/clusterconfig/
auth  bootstrap.ign  master.ign  metadata.json  worker.ign
----

Now you can use the Ignition config files as input to the vSphere installation procedures to install {op-system-first} systems.

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

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring-registry-operator.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="registry-removed_{context}"]
= Image registry removed during installation

[role="_abstract"]
On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types.

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage.

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
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="registry-configuring-storage-vsphere_{context}"]
= Configuring registry storage for VMware vSphere

[role="_abstract"]
As a cluster administrator, following installation you must configure your registry to use storage.

.Prerequisites

* Cluster administrator permissions.
* A cluster on VMware vSphere.
* Persistent storage provisioned for your cluster, such as {rh-storage-first}.
+
[IMPORTANT]
====
OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.
====
+
* Must have "100Gi" capacity.

[IMPORTANT]
====
Testing shows issues with using the NFS server on RHEL as storage backend for
core services. This includes the OpenShift Container Registry and Quay,
Prometheus for monitoring storage, and Elasticsearch for logging storage.
Therefore, using RHEL NFS to back PVs used by core services is not recommended.

Other NFS implementations on the marketplace might not have these issues.
Contact the individual NFS implementation vendor for more information on any
testing that was possibly completed against these OpenShift Container Platform core
components.
====

.Procedure

. Change the `spec.storage.pvc` field in the `configs.imageregistry/cluster` resource.
+
[NOTE]
====
When you use shared storage, review your security settings to prevent outside access.
====

. Verify that you do not have a registry pod by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-image-registry -l docker-registry=default
----
+
.Example output
[source,terminal]
----
No resourses found in openshift-image-registry namespace
----
+
[NOTE]
=====
If you do have a registry pod in your output, you do not need to continue with this procedure.
=====
. Check the registry configuration by running the following command:
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
Leave the `claim` field blank to allow the automatic creation of an `image-registry-storage` persistent volume claim (PVC). The PVC is generated based on the default storage class. However, be aware that the default storage class might provide ReadWriteOnce (RWO) volumes, such as a RADOS Block Device (RBD), which can cause issues when you replicate to more than one replica.

. Check the `clusteroperator` status by running the following command:
+
[source,terminal]
----
$ oc get clusteroperator image-registry
----
+
.Example output
[source,terminal]
----
NAME             VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
image-registry   4.7       True        False         False      6h50m
----

//+
//There will be warning similar to:
//+
//----
//- lastTransitionTime: 2019-03-26T12:45:46Z
//message: storage backend not configured
//reason: StorageNotConfigured
//status: "True"
//type: Degraded
//----

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
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="installation-registry-storage-block-recreate-rollout_{context}"]
= Configuring block registry storage for VMware vSphere

[role="_abstract"]
To allow the image registry to use block storage types such as vSphere Virtual Machine Disk (VMDK) during upgrades as a cluster administrator, you can use the `Recreate` rollout strategy.

[IMPORTANT]
====
Block storage volumes are supported but not recommended for use with image
registry on production clusters. An installation where the registry is
configured on block storage is not highly available because the registry cannot
have more than one replica.
====

.Procedure

. Enter the following command to set the image registry storage as a block storage type, patch the registry so that it uses the `Recreate` rollout strategy, and runs with only `1` replica:
+
[source,terminal]
----
$ oc patch config.imageregistry.operator.openshift.io/cluster --type=merge -p '{"spec":{"rolloutStrategy":"Recreate","replicas":1}}'
----
+
. Provision the persistent volume (PV) for the block storage device, and create a persistent volume claim (PVC) for that volume. The requested block volume uses the ReadWriteOnce (RWO) access mode.
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
--
`metadata.name`:: Specifies a unique name that represents the `PersistentVolumeClaim` object.
`metadata.namespace`:: Specifies the `namespace` for the `PersistentVolumeClaim` object, which is `openshift-image-registry`.
`spec.accessModes`:: Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.
`spec.resources.requests.storage`:: Specifies the size of the persistent volume claim.
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

For instructions about configuring registry storage so that it references the correct PVC, see Configuring the registry for vSphere.

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

You can add extra compute machines after the cluster installation is completed by following Adding compute machines to vSphere.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere.adoc

[id="anti-affinity-vsphere_{context}"]
= Configuring vSphere DRS anti-affinity rules for control plane nodes

vSphere Distributed Resource Scheduler (DRS) anti-affinity rules can be configured to support higher availability of OpenShift Container Platform Control Plane nodes. Anti-affinity rules ensure that the vSphere Virtual Machines for the OpenShift Container Platform Control Plane nodes are not scheduled to the same vSphere Host.

[IMPORTANT]
====
* The following information applies to compute DRS only and does not apply to storage DRS.

* The `govc` command is an open-source command available from VMware; it is not available from Red Hat. The `govc` command is not supported by the Red Hat support.

* Instructions for downloading and installing `govc` are found on the VMware documentation website.
====

// https://docs.vmware.com/en/VMware-Telco-Cloud-Operations/1.4.0/deployment-guide-140/GUID-5249E662-D792-4A1A-93E6-CF331552364C.html#:~:text=Govc%20is%20an%20open%20source,operations%20on%20the%20target%20vCenter.

Create an anti-affinity rule by running the following command:

.Example command

[source,terminal]
----
$ govc cluster.rule.create \
  -name openshift4-control-plane-group \
  -dc MyDatacenter -cluster MyCluster \
  -enable \
  -anti-affinity master-0 master-1 master-2
----

After creating the rule, your control plane nodes are automatically migrated by vSphere so they are not running on the same hosts. This might take some time while vSphere reconciles the new rule. Successful command completion is shown in the following procedure.

[NOTE]
====
The migration occurs automatically and might cause brief OpenShift API outage or latency until the migration finishes.
====

The vSphere DRS anti-affinity rules need to be updated manually in the event of a control plane VM name change or migration to a new vSphere Cluster.

.Procedure

. Remove any existing DRS anti-affinity rule by running the following command:
+
[source,terminal]
----
$ govc cluster.rule.remove \
  -name openshift4-control-plane-group \
  -dc MyDatacenter -cluster MyCluster
----
+
.Example Output
[source,terminal]
----
[13-10-22 09:33:24] Reconfigure /MyDatacenter/host/MyCluster...OK
----

. Create the rule again with updated names by running the following command:
+
[source,terminal]
----
$ govc cluster.rule.create \
  -name openshift4-control-plane-group \
  -dc MyDatacenter -cluster MyOtherCluster \
  -enable \
  -anti-affinity master-0 master-1 master-2
----

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

[id="next-steps_installing-vsphere"]
== Next steps

* Customize your cluster.
* If necessary, you can
Remote health reporting.
* Set up your registry and configure registry storage.
* Optional: View the events from the vSphere Problem Detector Operator to determine if the cluster has permission or storage configuration issues.
* Optional: if you created encrypted virtual machines, create an encrypted storage class.
