---
title: "Installing a cluster on Azure Stack Hub with customizations"
type: reference
domain: openshift
slug: installing-4-22-installing-azure-stack-hub-default
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-azure-stack-hub-default
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on Azure Stack Hub with customizations

[id="installing-azure-stack-hub-default"]
= Installing a cluster on Azure Stack Hub with customizations

In OpenShift Container Platform version , you can install a cluster on Microsoft Azure Stack Hub with an installer-provisioned infrastructure. However, you must manually configure the `install-config.yaml` file to specify values that are specific to Azure Stack Hub.

[NOTE]
====
While you can select `azure` when using the installation program to deploy a cluster using installer-provisioned infrastructure, this option is only supported for the Azure Public Cloud.
====

[id="prerequisites_installing-azure-stack-hub-default-ipi"]
== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You have installed Azure Stack Hub version 2008 or later.
* You configured an Azure Stack Hub account to host the cluster.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.
* You verified that you have approximately 16 GB of local disk space. Installing the cluster requires that you download the {op-system} virtual hard drive (VHD) cluster image and upload it to your Azure Stack Hub environment so that it is accessible during deployment. Decompressing the VHD files requires this amount of local disk space.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-user-infra-uploading-rhcos_{context}"]
= Uploading the {op-system} cluster image and bootstrap Ignition config file

= Uploading the {op-system} cluster image

The Azure client does not support deployments based on files existing locally. You
must copy and store the {op-system} virtual hard disk (VHD) cluster image and bootstrap Ignition config file in a storage container so they are accessible during deployment.

You must download the {op-system} virtual hard disk (VHD) cluster image and upload it to your Azure Stack Hub environment so that it is accessible during deployment.

.Prerequisites

* Generate the Ignition config files for your cluster.

.Procedure

. Create an Azure storage account to store the VHD cluster image:
+
[source,terminal]
----
$ az storage account create -g ${RESOURCE_GROUP} --location ${AZURE_REGION} --name ${CLUSTER_NAME}sa --kind Storage --sku Standard_LRS
----
+
[WARNING]
====
The Azure storage account name must be between 3 and 24 characters in length and
use numbers and lower-case letters only. If your `CLUSTER_NAME` variable does
not follow these restrictions, you must manually define the Azure storage
account name. For more information on Azure storage account name restrictions,
see Resolve errors for storage account names
in the Azure documentation.
====

. Export the storage account key as an environment variable:
+
[source,terminal]
----
$ export ACCOUNT_KEY=`az storage account keys list -g ${RESOURCE_GROUP} --account-name ${CLUSTER_NAME}sa --query "[0].value" -o tsv`
----

. Export the URL of the {op-system} VHD to an environment variable:
+
[source,terminal]
----
$ export VHD_URL=`openshift-install coreos print-stream-json | jq -r '.architectures.<architecture>."rhel-coreos-extensions"."azure-disk".url'`
----
+
where:

`<architecture>`:: Specifies the architecture, valid values include `x86_64` or `aarch64`.
[source,terminal]
----
$ export COMPRESSED_VHD_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.azurestack.formats."vhd.gz".disk.location')
----
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform.
You must specify an image with the highest version that is
less than or equal to the OpenShift Container Platform version that you install. Use the image version
that matches your OpenShift Container Platform version if it is available.
====

. Create the storage container for the VHD:
+
[source,terminal]
----
$ az storage container create --name vhd --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY}
----
. Download the compressed {op-system} VHD file locally:
+
[source,terminal]
----
$ curl -O -L ${COMPRESSED_VHD_URL}
----

. Decompress the VHD file.
+
[NOTE]
====
The decompressed VHD file is approximately 16 GB, so be sure that your host system has 16 GB of free space available. You can delete the VHD file after you upload it.
====

. Copy the local VHD to a blob:
+
[source,terminal]
----
$ az storage blob copy start --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} --destination-blob "rhcos.vhd" --destination-container vhd --source-uri "${VHD_URL}"
----
[source,terminal]
----
$ az storage blob upload --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -c vhd -n "rhcos.vhd" -f rhcos-<rhcos_version>-azurestack.x86_64.vhd
----

. Create a blob storage container and upload the generated `bootstrap.ign` file:
+
[source,terminal]
----
$ az storage container create --name files --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY}
----
+
[source,terminal]
----
$ az storage blob upload --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -c "files" -f "<installation_directory>/bootstrap.ign" -n "bootstrap.ign"
----

. Obtain the {op-system} VHD cluster image:
.. Export the URL of the {op-system} VHD to an environment variable.
+
[source,terminal]
----
$ export COMPRESSED_VHD_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.azurestack.formats."vhd.gz".disk.location')
----
.. Download the compressed {op-system} VHD file locally.
+
[source,terminal]
----
$ curl -O -L ${COMPRESSED_VHD_URL}
----
. Decompress the VHD file.
+
[NOTE]
====
The decompressed VHD file is approximately 16 GB, so be sure that your host system has 16 GB of free space available. The VHD file can be deleted once you have uploaded it.
====
. Upload the local VHD to the Azure Stack Hub environment, making sure that the blob is publicly available. For example, you can upload the VHD to a blob using the `az` cli or the web portal.

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
* Installation configuration parameters for Azure Stack Hub

// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc

[id="installation-azure-stack-hub-config-yaml_{context}"]
= Sample customized install-config.yaml file for Azure Stack Hub

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster's platform or modify the values of the required parameters.

[IMPORTANT]
====
This sample YAML file is provided for reference only. Use it as a resource to enter parameter values into the installation configuration file that you created manually.
====

[source,yaml]
----
apiVersion: v1
baseDomain: example.com
controlPlane: <1>
  name: master
  platform:
    azure:
      osDisk:
        diskSizeGB: 1024 <2>
        diskType: premium_LRS
  replicas: 3
compute: <1>
- name: worker
  platform:
    azure:
      osDisk:
        diskSizeGB: 512 <2>
        diskType: premium_LRS
  replicas: 0
metadata:
  name: test-cluster <3>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes <4>
  serviceNetwork:
  - 172.30.0.0/16
platform:
  azure:
    armEndpoint: azurestack_arm_endpoint <5>
    baseDomainResourceGroupName: resource_group <6>
    region: azure_stack_local_region <7>
    resourceGroupName: existing_resource_group <8>
    outboundType: Loadbalancer
    cloudName: AzureStackCloud <9>
pullSecret: '{"auths": ...}' <10>
fips: false <11>
additionalTrustBundle: | <12>
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
sshKey: ssh-ed25519 AAAA... <13>
additionalTrustBundle: | <11>
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
sshKey: ssh-ed25519 AAAA... <12>
----
<1> The `controlPlane` section is a single mapping, but the `compute` section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Only one control plane pool is used.
<2> You can specify the size of the disk to use in GB. Minimum recommendation for control plane nodes is 1024 GB.
<3> Specify the name of the cluster.
<4> The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.
<5> Specify the Azure Resource Manager endpoint that your Azure Stack Hub operator provides.
<6> Specify the name of the resource group that contains the DNS zone for your base domain.
<7> Specify the name of your Azure Stack Hub local region.
<8> Specify the name of an already existing resource group to install your cluster to. If undefined, a new resource group is created for the cluster.
<9> Specify the Azure Stack Hub environment as your target platform.
<10> Specify the pull secret required to authenticate your cluster.
<11> Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
+
--
[IMPORTANT]
====
To enable FIPS mode for your cluster, you must run the installation program from a {op-system-base-full} computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see Installing the system in FIPS mode.

When running {op-system-base-full} or {op-system-first} booted in FIPS mode, OpenShift Container Platform core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.
====
--
<12> If your Azure Stack Hub environment uses an internal certificate authority (CA), add the necessary certificate bundle in `.pem` format.
<13> You can optionally provide the `sshKey` value that you use to access the machines in your cluster.
<11> If your Azure Stack Hub environment uses an internal certificate authority (CA), add the necessary certificate bundle in `.pem` format.
<12> You can optionally provide the `sshKey` value that you use to access the machines in your cluster.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====

[source,yaml]
----
apiVersion: v1
baseDomain: example.com <1>
credentialsMode: Manual
controlPlane: <2> <3>
  name: master
  platform:
    azure:
      osDisk:
        diskSizeGB: 1024 <4>
        diskType: premium_LRS
  replicas: 3
compute: <2>
- name: worker
  platform:
    azure:
      osDisk:
        diskSizeGB: 512 <4>
        diskType: premium_LRS
  replicas: 3
metadata:
  name: test-cluster <1> <5>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes <6>
  serviceNetwork:
  - 172.30.0.0/16
platform:
  azure:
    armEndpoint: azurestack_arm_endpoint <1> <7>
    baseDomainResourceGroupName: resource_group <1> <8>
    region: azure_stack_local_region <1> <9>
    resourceGroupName: existing_resource_group <10>
    outboundType: Loadbalancer
    cloudName: AzureStackCloud <1>
    clusterOSimage: https://vhdsa.blob.example.example.com/vhd/rhcos-410.84.202112040202-0-azurestack.x86_64.vhd <1> <11>
pullSecret: '{"auths": ...}' <1> <12>
fips: false <13>
sshKey: ssh-ed25519 AAAA... <14>
sshKey: ssh-ed25519 AAAA...<13>
additionalTrustBundle: | <15>
additionalTrustBundle: | <14>
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
----
<1> Required.
<2> If you do not provide these parameters and values, the installation program provides the default value.
<3> The `controlPlane` section is a single mapping, but the `compute` section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Although both sections currently define a single machine pool, it is possible that future versions of OpenShift Container Platform will support defining multiple compute pools during installation. Only one control plane pool is used.
<4> You can specify the size of the disk to use in GB. Minimum recommendation for control plane nodes is 1024 GB.
<5> The name of the cluster.
<6> The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.
<7> The Azure Resource Manager endpoint that your Azure Stack Hub operator provides.
<8> The name of the resource group that contains the DNS zone for your base domain.
<9> The name of your Azure Stack Hub local region.
<10> The name of an existing resource group to install your cluster to. If undefined, a new resource group is created for the cluster.
<11> The URL of a storage blob in the Azure Stack environment that contains an {op-system} VHD.
<12> The pull secret required to authenticate your cluster.
<13> Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
+
[IMPORTANT]
====
When running {op-system-base-full} or {op-system-first} booted in FIPS mode, OpenShift Container Platform core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.
====
<14> You can optionally provide the `sshKey` value that you use to access the machines in your cluster.
<13> You can optionally provide the `sshKey` value that you use to access the machines in your cluster.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
<15> If the Azure Stack Hub environment is using an internal Certificate Authority (CA), adding the CA certificate is required.
<14> If the Azure Stack Hub environment is using an internal Certificate Authority (CA), adding the CA certificate is required.

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

[role="_additional-resources"]
[id="additional-resources_installing-azure-stack-hub-default-cco"]
.Additional resources
* Updating cloud provider resources with manually maintained credentials

// Module included in the following assemblies:
//
// *installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc

[id="internal-certificate-authority_{context}"]
= Configuring the cluster to use an internal CA

If the Azure Stack Hub environment is using an internal Certificate Authority (CA), update the `cluster-proxy-01-config.yaml file` to configure the cluster to use the internal CA.

.Prerequisites

* Create the `install-config.yaml` file and specify the certificate trust bundle in `.pem` format.
* Create the cluster manifests.

.Procedure

. From the directory in which the installation program creates files, go to the `manifests` directory.
. Add `user-ca-bundle` to  the `spec.trustedCA.name` field.
+
.Example `cluster-proxy-01-config.yaml` file
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  creationTimestamp: null
  name: cluster
spec:
  trustedCA:
    name: user-ca-bundle
status: {}
----
. Optional: Back up the `manifests/ cluster-proxy-01-config.yaml` file. The installation program consumes the `manifests/` directory when you deploy the cluster.

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
[id="additional-resources_installing-azure-stack-hub-default-console"]
.Additional resources
* Accessing the web console

[id="next-steps_installing-azure-stack-hub-default-ipi"]
== Next steps

* Validating an installation
* Customize your cluster
* Optional: Remote health reporting
* Optional: Remove cloud provider credentials
