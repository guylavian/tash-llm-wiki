---
title: "Installing a cluster on Azure Stack Hub using ARM templates"
type: reference
domain: openshift
slug: installing-4-22-installing-azure-stack-hub-user-infra
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-azure-stack-hub-user-infra
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on Azure Stack Hub using ARM templates

[id="installing-azure-stack-hub-user-infra"]
= Installing a cluster on Azure Stack Hub using ARM templates

In OpenShift Container Platform version , you can install a cluster on Microsoft Azure Stack Hub by using infrastructure that you provide.

Several Azure Resource Manager (ARM) templates are provided to assist in completing these steps or to help model your own.

[IMPORTANT]
====
The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several ARM templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.
====

[id="prerequisites_installing-azure-stack-hub-user-infra"]
== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You have installed Azure Stack Hub version 2008 or later.
* You configured an Azure Stack Hub account to host the cluster.
* You downloaded the Azure CLI and installed it on your computer. See Install the Azure CLI in the Azure documentation. The documentation below was tested using version `2.28.0` of the Azure CLI. Azure CLI commands might perform differently based on the version you use.
* If you use a firewall and plan to use the Telemetry service, you configured the firewall to allow the sites that your cluster requires access to.
+
[NOTE]
====
Be sure to also review this site list if you are configuring a proxy.
====

[id="installation-azure-stack-hub-user-infra-config-project"]
== Configuring your Azure Stack Hub project

Before you can install OpenShift Container Platform, you must configure an Azure project to host it.

[IMPORTANT]
====
All Azure Stack Hub resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure Stack Hub restricts, see Resolve reserved resource name errors in the Azure documentation.
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-account.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-limits_{context}"]
= {cp} account limits

The OpenShift Container Platform cluster uses a number of Microsoft {cp} components, and the default Azure subscription and service limits, quotas, and constraints affect your ability to install OpenShift Container Platform clusters.

[IMPORTANT]
====
Default limits vary by offer category types, such as Free Trial and Pay-As-You-Go, and by series, such as Dv2, F, and G. For example, the default for Enterprise Agreement subscriptions is 350 cores.

Check the limits for your subscription type and if necessary, increase quota limits for your account before you install a default
cluster on Azure.
====
The OpenShift Container Platform cluster uses a number of Microsoft Azure Stack Hub components, and the default Quota types in Azure Stack Hub affect your ability to install OpenShift Container Platform clusters.

The following table summarizes the {cp} components whose limits can impact your
ability to install and run OpenShift Container Platform clusters.

[cols="2a,3a,3a,8a",options="header"]
|===
|Component |Number of components required by default| Default {cp} limit |Description
[cols="2a,3a,8a",options="header"]
|===
|Component |Number of components required by default |Description

|vCPU
|44
|40
|20 per region
|A default cluster requires 44 vCPUs, so you must increase the account limit.
|A default cluster requires 40 vCPUs, so you must increase the account limit.

By default, each cluster creates the following instances:

* One bootstrap machine, which is removed after installation
* Three control plane machines
* Three compute machines

Because the bootstrap and control plane machines use `Standard_D8s_v3` virtual
machines, which use 8 vCPUs, and the compute machines use `Standard_D4s_v3`
virtual machines, which use 4 vCPUs, a default cluster requires 44 vCPUs.
The bootstrap node VM, which uses 8 vCPUs, is used only during installation.
Because the bootstrap machine uses `Standard_D4s_v3` machines, which use 4 vCPUs,
the control plane machines use `Standard_D8s_v3` virtual
machines, which use 8 vCPUs, and the worker machines use `Standard_D4s_v3`
virtual machines, which use 4 vCPUs, a default cluster requires 40 vCPUs.
The bootstrap node VM, which uses 4 vCPUs, is used only during installation.
|56
|A default cluster requires 56 vCPUs, so you must increase the account limit.

By default, each cluster creates the following instances:

* One bootstrap machine, which is removed after installation
* Three control plane machines
* Three compute machines

Because the bootstrap, control plane, and worker machines use `Standard_DS4_v2` virtual machines, which use 8 vCPUs, a default cluster requires 56 vCPUs. The bootstrap node VM is used only during installation.

To deploy more worker nodes, enable autoscaling, deploy large workloads, or use
a different instance type, you must further increase the vCPU limit for your
account to ensure that your cluster can deploy the machines that you require.

|OS Disk
|7
|
|Each cluster machine must have a minimum of 100 GB of storage and 300 IOPS.
[NOTE]
====
Faster storage is recommended for production clusters and clusters with intensive workloads. For more information about optimizing storage for performance, see the page titled "Optimizing storage" in the "Scalability and performance" section.
====

|VNet
| 1
| 1000 per region
| Each default cluster requires one Virtual Network (VNet), which contains two
subnets.

|Network interfaces
|7
|65,536 per region
|Each default cluster requires seven network interfaces. If you create more
machines or your deployed workloads create load balancers, your cluster uses
more network interfaces.

|Network security groups
|2
|5000
| Each cluster creates network security groups for each subnet in the VNet.
The default cluster creates network
security groups for the control plane and for the compute node subnets:

[horizontal]
 `controlplane`:: Allows the control plane machines to be reached on port 6443
 from anywhere
`node`:: Allows worker nodes to be reached from the internet on ports 80 and 443

|Network load balancers
| 3
| 1000 per region
|Each cluster creates the following
load balancers:

[horizontal]
`default`:: Public IP address that load balances requests to ports 80 and 443 across worker machines
`internal`:: Private IP address that load balances requests to ports 6443 and 22623 across control plane machines
`external`:: Public IP address that load balances requests to port 6443 across control plane machines

If your applications create more Kubernetes `LoadBalancer` service objects,
your cluster uses more load balancers.

|Public IP addresses
|3
|
|Each of the two public load balancers uses a public IP address. The bootstrap
machine also uses a public IP address so that you can SSH into the
machine to troubleshoot issues during installation. The IP address for the
bootstrap node is used only during installation.
|2
|The public load balancer uses a public IP address. The bootstrap
machine also uses a public IP address so that you can SSH into the
machine to troubleshoot issues during installation. The IP address for the
bootstrap node is used only during installation.

|Private IP addresses
|7
|
|The internal load balancer, each of the three control plane machines, and each
of the three worker machines each use a private IP address.

|Spot VM vCPUs (optional)
|0

If you configure spot VMs, your cluster must have two spot VM vCPUs for every compute node.
|20 per region
|This is an optional component. To use spot VMs, you must increase the Azure default limit to at least twice the number of compute nodes in your cluster.
[NOTE]
====
Using spot VMs for control plane nodes is not recommended.
====
|===

To increase an account limit, file a support request on the Azure portal. For more information, see Request a quota limit increase for Azure Deployment Environments resources.

[role="_additional-resources"]
.Additional resources

* Optimizing storage

// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc

[id="installation-azure-stack-hub-network-config_{context}"]
= Configuring a DNS zone in Azure Stack Hub

To successfully install OpenShift Container Platform on Azure Stack Hub, you must create DNS records in an Azure Stack Hub DNS zone. The DNS zone must be authoritative for the domain. To delegate a registrar's DNS zone to Azure Stack Hub, see Microsoft's documentation for Azure Stack Hub datacenter DNS integration.

You can view Azure's DNS solution by visiting this example for creating DNS zones.

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

// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc

[id="installation-azure-stack-hub-permissions_{context}"]
= Required Azure Stack Hub roles

Your Microsoft Azure Stack Hub account must have the following roles for the subscription that you use:

* `Owner`

To set roles on the Azure portal, see the Manage access to resources in Azure Stack Hub with role-based access control in the Microsoft documentation.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-account.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-service-principal_{context}"]
= Creating a service principal

Because OpenShift Container Platform and its installation program create Microsoft Azure resources by using the Azure Resource Manager, you must create a service principal to represent it.

.Prerequisites

* Install or update the Azure CLI.
* Your Azure account has the required roles for the subscription that you use.
* If you want to use a custom role, you have created a custom role with the required permissions listed in the _Required Azure permissions for installer-provisioned infrastructure_ section.
* If you want to use a custom role, you have created a custom role with the required permissions listed in the _Required Azure permissions for user-provisioned infrastructure_ section.

.Procedure

. Register your environment:
+
[source,terminal]
----
$ az cloud register -n AzureStackCloud --endpoint-resource-manager <endpoint> <1>
----
<1> Specify the Azure Resource Manager endpoint, \`https://management.<region>.<fqdn>/`.
+
See the Microsoft documentation for details.

. Set the active environment:
+
[source,terminal]
----
$ az cloud set -n AzureStackCloud
----

. Update your environment configuration to use the specific API version for Azure Stack Hub:
+
[source,terminal]
----
$ az cloud update --profile 2019-03-01-hybrid
----

. Log in to the Azure CLI:
+
[source,terminal]
----
$ az login
----
+
If you are in a multitenant environment, you must also supply the tenant ID.

. If your Azure account uses subscriptions, ensure that you are using the right
subscription:

.. View the list of available accounts and record the `tenantId` value for the
subscription you want to use for your cluster:
+
[source,terminal]
----
$ az account list --refresh
----
+
.Example output
[source,terminal]
----
[
  {
    "cloudName": "AzureCloud",
    "cloudName": AzureStackCloud",
    "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
    "isDefault": true,
    "name": "Subscription Name",
    "state": "Enabled",
    "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee",
    "user": {
      "name": "you@example.com",
      "type": "user"
    }
  }
]
----

.. View your active account details and confirm that the `tenantId` value matches
the subscription you want to use:
+
[source,terminal]
----
$ az account show
----
+
.Example output
[source,terminal]
----
{
  "environmentName": "AzureCloud",
  "environmentName": AzureStackCloud",
  "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee", <1>
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
----
<1> Ensure that the value of the `tenantId` parameter is the correct subscription ID.

.. If you are not using the right subscription, change the active subscription:
+
[source,terminal]
----
$ az account set -s <subscription_id> <1>
----
<1> Specify the subscription ID.

.. Verify the subscription ID update:
+
[source,terminal]
----
$ az account show
----
+
.Example output
[source,terminal]
----
{
  "environmentName": "AzureCloud",
  "environmentName": AzureStackCloud",
  "id": "33212d16-bdf6-45cb-b038-f6565b61edda",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee",
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
----

. Record the `tenantId` and `id` parameter values from the output. You need these values during the OpenShift Container Platform installation.

. Create the service principal for your account:
+
[source,terminal]
----
$ az ad sp create-for-rbac --role Contributor --name <service_principal> \ <1>
  --scopes /subscriptions/<subscription_id> <2>
  --years <years> <3>
----
<1> Specify the service principal name.
<2> Specify the subscription ID.
<3> Specify the number of years. By default, a service principal expires in one year. By using the `--years` option you can extend the validity of your service principal.
+
.Example output
[source,terminal]
----
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
}
----

. Create the service principal for your account:
+
[source,terminal]
----
$ az ad sp create-for-rbac --role <role_name> \// <1>
     --name <service_principal> \// <2>
     --scopes /subscriptions/<subscription_id> <3>
----
<1> Defines the role name. You can use the `Contributor` role, or you can specify a custom role which contains the necessary permissions.
<2> Defines the service principal name.
<3> Specifies the subscription ID.
+
.Example output
[source,terminal]
----
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
}
----

. Record the values of the `appId` and `password` parameters from the previous
output. You need these values during OpenShift Container Platform installation.

. If you applied the `Contributor` role to your service principal, assign the `User Administrator Access` role by running the following command:
+
[source,terminal]
----
$ az role assignment create --role "User Access Administrator" \
  --assignee-object-id $(az ad sp show --id <appId> --query id -o tsv) <1>
----
<1> Specify the `appId` parameter value for your service principal.

[role="_additional-resources"]
.Additional resources

* About the Cloud Credential Operator

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installaing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-user-infra-generate_{context}"]
= Creating the installation files for {cp}

To install OpenShift Container Platform on {cp-first} using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.
To install OpenShift Container Platform on {cp-first} using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You manually create the `install-config.yaml` file, and then generate and customize the Kubernetes manifests and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.
To install OpenShift Container Platform on {cp-first} using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.
To install OpenShift Container Platform on {cp-first} into a shared VPC, you must generate the `install-config.yaml` file and modify it so that the cluster uses the correct VPC networks, DNS zones, and project names.

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
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-user-infra-exporting-common-variables-arm-templates_{context}"]
= Exporting common variables for ARM templates

You must export a common set of variables that are used with the provided Azure Resource Manager (ARM) templates used to assist in completing a user-provided infrastructure install on Microsoft {cp}.

[NOTE]
====
Specific ARM templates can also require additional exported variables, which are detailed in their related procedures.
====

.Prerequisites

* Obtain the OpenShift Container Platform installation program and the pull secret for your cluster.

.Procedure

. Export common variables found in the `install-config.yaml` to be used by the provided ARM templates:
+
[source,terminal]
----
$ export CLUSTER_NAME=<cluster_name>
----
+
where:
+
`<cluster_name>`:: The value of the `.metadata.name` attribute from the `install-config.yaml` file.
+
[source,terminal]
----
$ export AZURE_REGION=<azure_region>
----
+
where:
+
`<azure_region>`:: The region to deploy the cluster into, for example `centralus`. This is the value of the `.platform.azure.region` attribute from the `install-config.yaml` file.
`<azure_region>`:: The region to deploy the cluster into. This is the value of the `.platform.azure.region` attribute from the `install-config.yaml` file.
+
[source,terminal]
----
$ export SSH_KEY=<ssh_key>
----
+
where:
+
`<ssh_key>`:: The SSH RSA public key file as a string. You must enclose the SSH key in quotes since it contains spaces. This is the value of the `.sshKey` attribute from the `install-config.yaml` file.
+
[source,terminal]
----
$ export BASE_DOMAIN=<base_domain>
----
+
where:
+
`<base_domain>`:: The base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster. This is the value of the `.baseDomain` attribute from the `install-config.yaml` file.
`<base_domain>`:: The base domain to deploy the cluster to. The base domain corresponds to the DNS zone that you created for your cluster. This is the value of the `.baseDomain` attribute from the `install-config.yaml` file.
+
[source,terminal]
----
$ export BASE_DOMAIN_RESOURCE_GROUP=<base_domain_resource_group>
----
+
where:
+
`<base_domain_resource_group>`:: The resource group where the public DNS zone exists. This is the value of the `.platform.azure.baseDomainResourceGroupName` attribute from the `install-config.yaml` file.
`<base_domain_resource_group>`:: The resource group where the DNS zone exists. This is the value of the `.platform.azure.baseDomainResourceGroupName` attribute from the `install-config.yaml` file.
+
For example:
+
[source,terminal]
----
$ export CLUSTER_NAME=test-cluster
----
+
[source,terminal]
----
$ export AZURE_REGION=centralus
----
+
[source,terminal]
----
$ export SSH_KEY="ssh-rsa xxx/xxx/xxx= user@email.com"
----
+
[source,terminal]
----
$ export BASE_DOMAIN=example.com
----
+
[source,terminal]
----
$ export BASE_DOMAIN_RESOURCE_GROUP=ocp-cluster
----

. Export the kubeadmin credentials:
+
[source,terminal]
----
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
----
+
where:
+
`<installation_directory>`:: Specify the path to the directory that you stored the installation files in.

// Creating the Kubernetes manifest and Ignition config files
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
* Manually manage cloud credentials

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

// Similar content to what is in this module is also present in modules/installation-disk-partitioning.adoc. <-- This module is in use with the following vSphere assemblies:
//    * installing-vsphere.adoc
//    * installing-vsphere-network-customizations.adoc
//    * installing-restricted-networks-vsphere.adoc

// Similar content to what is in this module is also present in modules/installation-user-infra-machines-advanced.adoc. <-- This module is in use with the following bare metal assemblies:
//    * installing-bare-metal-network-customizations.adoc
//    * installing-bare-metal.adoc
//    * installing-restricted-networks-bare-metal.adoc

[id="installation-disk-partitioning-upi-templates_{context}"]
= Optional: Creating a separate `/var` partition

It is recommended that disk partitioning for OpenShift Container Platform be left to the installer. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` partition or a subdirectory of `/var`. For example:

* `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date and keep that data intact. With this method, you will not have to pull all your containers again, nor will you have to copy massive log files when you update systems.

Because `/var` must be in place before a fresh installation of {op-system-first}, the following procedure sets up the separate `/var` partition by creating a machine config manifest that is inserted during the `openshift-install` preparation phases of an OpenShift Container Platform installation.

[IMPORTANT]
====
If you follow the steps to create a separate `/var` partition in this procedure, it is not necessary to create the Kubernetes manifest and Ignition config files again as described later in this section.
====

.Procedure

. Create a directory to hold the OpenShift Container Platform installation files:
+
[source,terminal]
----
$ mkdir $HOME/clusterconfig
----

. Run `openshift-install` to create a set of files in the `manifest` and `openshift` subdirectories. Answer the system questions as you are prompted:
+
[source,terminal]
----
$ openshift-install create manifests --dir $HOME/clusterconfig
----
+
.Example output
+
[source,terminal]
----
? SSH Public Key ...
INFO Credentials loaded from the "myprofile" profile in file "/home/myuser/.aws/credentials"
INFO Consuming Install Config from target directory
INFO Manifests created in: $HOME/clusterconfig/manifests and $HOME/clusterconfig/openshift
----

. Optional: Confirm that the installation program created manifests in the `clusterconfig/openshift` directory:
+
[source,terminal]
----
$ ls $HOME/clusterconfig/openshift/
----
+
.Example output
+
[source,terminal]
----
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
<2> When adding a data partition to the boot disk, a minimum value of 25000 MiB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of {op-system} might overwrite the beginning of the data partition.
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
----
+
[source,terminal]
----
$ ls $HOME/clusterconfig/
auth  bootstrap.ign  master.ign  metadata.json  worker.ign
----
+
You can now use the Ignition config files as input to the installation procedures to install {op-system-first} systems.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-create-resource-group-and-identity_{context}"]
= Creating the Azure resource group

You must create a Microsoft Azure resource group and an identity for that resource group. These are both used during the installation of your OpenShift Container Platform cluster on Azure.
You must create a Microsoft Azure resource group. This is used during the installation of your OpenShift Container Platform cluster on Azure Stack Hub.

.Procedure

. Create the resource group in a supported Azure region:
* Create the resource group in a supported Azure region:
+
[source,terminal]
----
$ az group create --name ${RESOURCE_GROUP} --location ${AZURE_REGION}
----

. Create an Azure identity for the resource group:
+
[source,terminal]
----
$ az identity create -g ${RESOURCE_GROUP} -n ${INFRA_ID}-identity
----
+
This is used to grant the required access to Operators in your cluster. For
example, this allows the Ingress Operator to create a public IP and its load
balancer. You must assign the Azure identity to a role.

. Grant the Contributor role to the Azure identity:

.. Export the following variables required by the Azure role assignment:
+
[source,terminal]
----
$ export PRINCIPAL_ID=`az identity show -g ${RESOURCE_GROUP} -n ${INFRA_ID}-identity --query principalId --out tsv`
----
+
[source,terminal]
----
$ export RESOURCE_GROUP_ID=`az group show -g ${RESOURCE_GROUP} --query id --out tsv`
----

.. Assign the Contributor role to the identity:
+
[source,terminal]
----
$ az role assignment create --assignee "${PRINCIPAL_ID}" --role 'Contributor' --scope "${RESOURCE_GROUP_ID}"
----
+
[NOTE]
====
If you want to assign a custom role with all the required permissions to the identity, run the following command:
[source,terminal]
----
$ az role assignment create --assignee "${PRINCIPAL_ID}" --role <custom_role> \ <1>
--scope "${RESOURCE_GROUP_ID}"
----
<1> Specifies the custom role name.
====

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
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-create-dns-zones_{context}"]
= Example for creating DNS zones

DNS records are required for clusters that use user-provisioned infrastructure.
You should choose the DNS strategy that fits your scenario.

For this example, Azure's DNS solution
is used, so you will create a new public DNS zone for external (internet)
visibility and a private DNS zone for internal cluster resolution.
For this example, Azure Stack Hub's datacenter DNS integration is used, so you will create a DNS zone.

[NOTE]
====
The public DNS zone is not required to exist in the same resource group as the
cluster deployment and might already exist in your organization for the desired base domain. If that is the case, you can skip creating the public DNS zone; be sure the installation config you generated earlier reflects that scenario.
====

[NOTE]
====
The DNS zone is not required to exist in the same resource group as the
cluster deployment and might already exist in your organization for the desired base domain. If that is the case, you can skip creating the DNS zone; be sure the installation config you generated earlier reflects that scenario.
====

.Procedure

. Create the new public DNS zone in the resource group exported in the
`BASE_DOMAIN_RESOURCE_GROUP` environment variable:
* Create the new DNS zone in the resource group exported in the
`BASE_DOMAIN_RESOURCE_GROUP` environment variable:
+
[source,terminal]
----
$ az network dns zone create -g ${BASE_DOMAIN_RESOURCE_GROUP} -n ${CLUSTER_NAME}.${BASE_DOMAIN}
----
+

. Create the private DNS zone in the same resource group as the rest of this
deployment:
+
[source,terminal]
----
$ az network private-dns zone create -g ${RESOURCE_GROUP} -n ${CLUSTER_NAME}.${BASE_DOMAIN}
----

You can learn more about configuring a DNS zone in Azure Stack Hub by visiting that section.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-creating-azure-vnet_{context}"]
= Creating a VNet in {cp}

You must create a virtual network (VNet) in Microsoft {cp} for your
OpenShift Container Platform cluster to use. You can customize the VNet to meet your
requirements. One way to create the VNet is to modify the provided Azure
Resource Manager (ARM) template.

[NOTE]
====
If you do not use the provided ARM template to create your {cp} infrastructure,
you must review the provided information and manually create the infrastructure.
If your cluster does not initialize correctly, you might have to contact Red Hat
support with your installation logs.
====

.Procedure

. Copy the template from the *ARM template for the VNet* section of this topic
and save it as `01_vnet.json` in your cluster's installation directory. This template describes the
VNet that your cluster requires.

. Create the deployment by using the `az` CLI:
+
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/01_vnet.json" \
  --parameters baseName="${INFRA_ID}"<1>
----
<1> The base name to be used in resource names; this is usually the cluster's infrastructure ID.

. Link the VNet template to the private DNS zone:
+
[source,terminal]
----
$ az network private-dns link vnet create -g ${RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n ${INFRA_ID}-network-link -v "${INFRA_ID}-vnet" -e false
----

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-arm-vnet_{context}"]
= ARM template for the VNet

You can use the following Azure Resource Manager (ARM) template to deploy the
VNet that you need for your OpenShift Container Platform cluster:

.`01_vnet.json` ARM template
[%collapsible]
====
[source,json]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-user-infra-deploying-rhcos_{context}"]
= Deploying the {op-system} cluster image for the {cp} infrastructure

You must use a valid {op-system-first} image for Microsoft {cp} for your
OpenShift Container Platform nodes.

.Prerequisites

* Store the {op-system} virtual hard disk (VHD) cluster image in an Azure storage container.

* Store the bootstrap Ignition config file in an Azure storage container.

.Procedure

. Copy the template from the *ARM template for image storage* section of
this topic and save it as `02_storage.json` in your cluster's installation directory. This template
describes the image storage that your cluster requires.

. Export the {op-system} VHD blob URL as a variable:
+
[source,terminal]
----
$ export VHD_BLOB_URL=`az storage blob url --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -c vhd -n "rhcos.vhd" -o tsv`
----

. Deploy the cluster image:
+
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/02_storage.json" \
  --parameters vhdBlobURL="${VHD_BLOB_URL}" \ <1>
  --parameters baseName="${INFRA_ID}" \ <2>
  --parameters storageAccount="${CLUSTER_NAME}sa" \ <3>
  --parameters architecture="<architecture>" <4>
----
<1> The blob URL of the {op-system} VHD to be used to create master and worker machines.
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.
<3> The name of your Azure storage account.
<4> Specify the system architecture. Valid values are `x64` (default) or `Arm64`.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-arm-image-storage_{context}"]
= ARM template for image storage

You can use the following Azure Resource Manager (ARM) template to deploy the
stored {op-system-first} image that you need for your OpenShift Container Platform cluster:

.`02_storage.json` ARM template
[%collapsible]
====
[source,json]
----

----
====

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

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-creating-azure-dns_{context}"]
= Creating networking and load balancing components in {cp}

You must configure networking and load balancing in Microsoft {cp} for your
OpenShift Container Platform cluster to use. One way to create these components is
to modify the provided Azure Resource Manager (ARM) template.

Load balancing requires the following DNS records:

* An `api` DNS record for the API public load balancer in the DNS zone.
* An `api-int` DNS record for the API internal load balancer in the DNS zone.

[NOTE]
====
If you do not use the provided ARM template to create your {cp} infrastructure,
you must review the provided information and manually create the infrastructure.
If your cluster does not initialize correctly, you might have to contact Red Hat
support with your installation logs.
====

.Prerequisites

* Create and configure a VNet and associated subnets in {cp}.

.Procedure

. Copy the template from the *ARM template for the network and load balancers*
section of this topic and save it as `03_infra.json` in your cluster's installation directory. This
template describes the networking and load balancing objects that your cluster
requires.

. Create the deployment by using the `az` CLI:
+
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/03_infra.json" \
  --parameters privateDNSZoneName="${CLUSTER_NAME}.${BASE_DOMAIN}" \ <1>
  --parameters baseName="${INFRA_ID}"<2>
----
<1> The name of the private DNS zone.
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.

[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/03_infra.json" \
  --parameters baseName="${INFRA_ID}"<1>
----
<1> The base name to be used in resource names; this is usually the cluster's infrastructure ID.

. Create an `api` DNS record in the public zone for the API public load
balancer. The `${BASE_DOMAIN_RESOURCE_GROUP}` variable must point to the
resource group where the public DNS zone exists.

. Create an `api` DNS record and an `api-int` DNS record. When creating the API DNS records, the `${BASE_DOMAIN_RESOURCE_GROUP}` variable must point to the resource group where the DNS zone exists.

.. Export the following variable:
+
[source,terminal]
----
$ export PUBLIC_IP=`az network public-ip list -g ${RESOURCE_GROUP} --query "[?name=='${INFRA_ID}-master-pip'] | [0].ipAddress" -o tsv`
----
.. Export the following variable:
+
[source,terminal]
----
$ export PRIVATE_IP=`az network lb frontend-ip show -g "$RESOURCE_GROUP" --lb-name "${INFRA_ID}-internal" -n internal-lb-ip --query "privateIpAddress" -o tsv`
----

.. Create the `api` DNS record in a new public zone:
.. Create the `api` DNS record in a new DNS zone:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n api -a ${PUBLIC_IP} --ttl 60
----
+
If you are adding the cluster to an existing public zone, you can create the `api` DNS record in it instead:
If you are adding the cluster to an existing DNS zone, you can create the `api` DNS record in it instead:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n api.${CLUSTER_NAME} -a ${PUBLIC_IP} --ttl 60
----

.. Create the `api-int` DNS record in a new DNS zone:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z "${CLUSTER_NAME}.${BASE_DOMAIN}" -n api-int -a ${PRIVATE_IP} --ttl 60
----
+
If you are adding the cluster to an existing DNS zone, you can create the `api-int` DNS
record in it instead:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n api-int.${CLUSTER_NAME} -a ${PRIVATE_IP} --ttl 60
----

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-arm-dns_{context}"]
= ARM template for the network and load balancers

You can use the following Azure Resource Manager (ARM) template to deploy the
networking objects and load balancers that you need for your OpenShift Container Platform
cluster:

.`03_infra.json` ARM template
[%collapsible]
====
[source,json]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-creating-azure-bootstrap_{context}"]
= Creating the bootstrap machine in {cp}

You must create the bootstrap machine in Microsoft {cp} to use during
OpenShift Container Platform cluster initialization. One way to create this machine is to
modify the provided Azure Resource Manager (ARM) template.

[NOTE]
====
If you do not use the provided ARM template to create your bootstrap machine,
you must review the provided information and manually create the infrastructure.
If your cluster does not initialize correctly, you might have to contact Red Hat
support with your installation logs.
====

.Prerequisites

* Create and configure networking and load balancers in {cp}.
* Create the {cp} identity and grant the appropriate roles.

.Procedure

. Copy the template from the *ARM template for the bootstrap machine* section of
this topic and save it as `04_bootstrap.json` in your cluster's installation directory. This template
describes the bootstrap machine that your cluster requires.

. Export the bootstrap URL variable:
+
[source,terminal]
----
$ bootstrap_url_expiry=`date -u -d "10 hours" '+%Y-%m-%dT%H:%MZ'`
----
+
[source,terminal]
----
$ export BOOTSTRAP_URL=`az storage blob generate-sas -c 'files' -n 'bootstrap.ign' --https-only --full-uri --permissions r --expiry $bootstrap_url_expiry --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -o tsv`
----

. Export the bootstrap ignition variable:
+
[source,terminal]
----
$ export BOOTSTRAP_IGNITION=`jq -rcnM --arg v "3.2.0" --arg url ${BOOTSTRAP_URL} '{ignition:{version:$v,config:{replace:{source:$url}}}}' | base64 | tr -d '\n'`
----
.. If your environment uses a public certificate authority (CA), run this command:
+
[source,terminal]
----
$ export BOOTSTRAP_IGNITION=`jq -rcnM --arg v "3.2.0" --arg url ${BOOTSTRAP_URL} '{ignition:{version:$v,config:{replace:{source:$url}}}}' | base64 | tr -d '\n'`
----

.. If your environment uses an internal CA, you must add your PEM encoded bundle to the bootstrap ignition stub so that your bootstrap virtual machine can pull the bootstrap ignition from the storage account. Run the following commands, which assume your CA is in a file called `CA.pem`:
+
[source,terminal]
----
$ export CA="data:text/plain;charset=utf-8;base64,$(cat CA.pem |base64 |tr -d '\n')"
----
+
[source,terminal]
----
$ export BOOTSTRAP_IGNITION=`jq -rcnM --arg v "3.2.0" --arg url "$BOOTSTRAP_URL" --arg cert "$CA" '{ignition:{version:$v,security:{tls:{certificateAuthorities:[{source:$cert}]}},config:{replace:{source:$url}}}}' | base64 | tr -d '\n'`
----

. Create the deployment by using the `az` CLI:
+
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/04_bootstrap.json" \
  --parameters bootstrapIgnition="${BOOTSTRAP_IGNITION}" \ <1>
  --parameters baseName="${INFRA_ID}" \ <2>
  --parameter bootstrapVMSize="Standard_D4s_v3" <3>
----
<1> The bootstrap Ignition content for the bootstrap cluster.
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.
<3> Optional: Specify the size of the bootstrap VM. Use a VM size compatible with your specified architecture. If this value is not defined, the default value from the template is set.
[source,terminal]
----
$ az deployment group create --verbose -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/04_bootstrap.json" \
  --parameters bootstrapIgnition="${BOOTSTRAP_IGNITION}" \ <1>
  --parameters baseName="${INFRA_ID}" \ <2>
  --parameters diagnosticsStorageAccountName="${CLUSTER_NAME}sa" <3>
----
<1> The bootstrap Ignition content for the bootstrap cluster.
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.
<3> The name of the storage account for your cluster.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-arm-bootstrap_{context}"]
= ARM template for the bootstrap machine

You can use the following Azure Resource Manager (ARM) template to deploy the
bootstrap machine that you need for your OpenShift Container Platform cluster:

.`04_bootstrap.json` ARM template
[%collapsible]
====
[source,json]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-creating-azure-control-plane_{context}"]
= Creating the control plane machines in {cp}

You must create the control plane machines in Microsoft {cp} for your cluster
to use. One way to create these machines is to modify the provided Azure
Resource Manager (ARM) template.

[NOTE]
====
By default, Microsoft {cp} places control plane machines and compute machines in a pre-set availability zone. You can manually set an availability zone for a compute node or control plane node. To do this, modify a vendor's Azure Resource Manager (ARM) template by specifying each of your availability zones in the `zones` parameter of the virtual machine resource.
====

If you do not use the provided ARM template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, consider contacting Red Hat support with your installation logs.

.Prerequisites

* Create the bootstrap machine.

.Procedure

. Copy the template from the *ARM template for control plane machines*
section of this topic and save it as `05_masters.json` in your cluster's installation directory.
This template describes the control plane machines that your cluster requires.

. Export the following variable needed by the control plane machine deployment:
+
[source,terminal]
----
$ export MASTER_IGNITION=`cat <installation_directory>/master.ign | base64 | tr -d '\n'`
----

. Create the deployment by using the `az` CLI:
+
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/05_masters.json" \
  --parameters masterIgnition="${MASTER_IGNITION}" \ <1>
  --parameters baseName="${INFRA_ID}" \ <2>
  --parameters masterVMSize="Standard_D8s_v3" <3>
----
<1> The Ignition content for the control plane nodes.
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.
<3> Optional: Specify the size of the Control Plane VM. Use a VM size compatible with your specified architecture. If this value is not defined, the default value from the template is set.
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/05_masters.json" \
  --parameters masterIgnition="${MASTER_IGNITION}" \ <1>
  --parameters baseName="${INFRA_ID}" \ <2>
  --parameters diagnosticsStorageAccountName="${CLUSTER_NAME}sa" <3>
----
<1> The Ignition content for the control plane nodes (also known as the master nodes).
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.
<3> The name of the storage account for your cluster.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-arm-control-plane_{context}"]
= ARM template for control plane machines

You can use the following Azure Resource Manager (ARM) template to deploy the
control plane machines that you need for your OpenShift Container Platform cluster:

.`05_masters.json` ARM template
[%collapsible]
====
[source,json]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-user-infra-wait-for-bootstrap_{context}"]
= Wait for bootstrap completion and remove bootstrap resources in {cp}

After you create all of the required infrastructure in Microsoft {cp}, wait for
the bootstrap process to complete on the machines that you provisioned by using
the Ignition config files that you generated with the installation program.

.Prerequisites

* Create the control plane machines.

.Procedure

. Change to the directory that contains the installation program and run the
following command:
+
[source,terminal]
----
$ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \ <1>
    --log-level info <2>
----
<1> For `<installation_directory>`, specify the path to the directory that you
stored the installation files in.
<2> To view different installation details, specify `warn`, `debug`, or
`error` instead of `info`.
+
If the command exits without a `FATAL` warning, your production control plane
has initialized.

. Delete the bootstrap resources:
+
[source,terminal]
----
$ az network nsg rule delete -g ${RESOURCE_GROUP} --nsg-name ${INFRA_ID}-nsg --name bootstrap_ssh_in
----
+
[source,terminal]
----
$ az vm stop -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap
----
+
[source,terminal]
----
$ az vm deallocate -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap
----
+
[source,terminal]
----
$ az vm delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap --yes
----
+
[source,terminal]
----
$ az disk delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap_OSDisk --no-wait --yes
----
+
[source,terminal]
----
$ az network nic delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap-nic --no-wait
----
+
[source,terminal]
----
$ az storage blob delete --account-key ${ACCOUNT_KEY} --account-name ${CLUSTER_NAME}sa --container-name files --name bootstrap.ign
----
+
[source,terminal]
----
$ az network public-ip delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap-ssh-pip
----
+
[NOTE]
====
If you do not delete the bootstrap server, installation may not succeed due to API traffic being routed to the bootstrap server.
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-creating-azure-worker_{context}"]
= Creating additional worker machines in {cp}

You can create worker machines in Microsoft {cp} for your cluster
to use by launching individual instances discretely or by automated processes
outside the cluster, such as auto scaling groups. You can also take advantage of
the built-in cluster scaling mechanisms and the machine API in OpenShift Container Platform.

[NOTE]
====
If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.
====

In this example, you manually launch one instance by using the Azure Resource
Manager (ARM) template. Additional instances can be launched by including
additional resources of type `06_workers.json` in the file.

[NOTE]
====
By default, Microsoft {cp} places control plane machines and compute machines in a pre-set availability zone. You can manually set an availability zone for a compute node or control plane node. To do this, modify a vendor's ARM template by specifying each of your availability zones in the `zones` parameter of the virtual machine resource.
====

If you do not use the provided ARM template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, consider contacting Red Hat support with your installation logs.

.Procedure

. Copy the template from the *ARM template for worker machines*
section of this topic and save it as `06_workers.json` in your cluster's installation directory. This
template describes the worker machines that your cluster requires.

. Export the following variable needed by the worker machine deployment:
+
[source,terminal]
----
$ export WORKER_IGNITION=`cat <installation_directory>/worker.ign | base64 | tr -d '\n'`
----

. Create the deployment by using the `az` CLI:
+
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/06_workers.json" \
  --parameters workerIgnition="${WORKER_IGNITION}" \ <1>
  --parameters baseName="${INFRA_ID}" \ <2>
  --parameters nodeVMSize="Standard_D4s_v3" <3>
----
<1> The Ignition content for the worker nodes.
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.
<3> Optional: Specify the size of the compute node VM. Use a VM size compatible with your specified architecture. If this value is not defined, the default value from the template is set.
[source,terminal]
----
$ az deployment group create -g ${RESOURCE_GROUP} \
  --template-file "<installation_directory>/06_workers.json" \
  --parameters workerIgnition="${WORKER_IGNITION}" \ <1>
  --parameters baseName="${INFRA_ID}" <2>
  --parameters diagnosticsStorageAccountName="${CLUSTER_NAME}sa" <3>
----
<1> The Ignition content for the worker nodes.
<2> The base name to be used in resource names; this is usually the cluster's infrastructure ID.
<3> The name of the storage account for your cluster.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-arm-worker_{context}"]
= ARM template for worker machines

You can use the following Azure Resource Manager (ARM) template to deploy the
worker machines that you need for your OpenShift Container Platform cluster:

.`06_workers.json` ARM template
[%collapsible]
====
[source,json]
----

----
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
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-create-ingress-dns-records_{context}"]
= Adding the Ingress DNS records

If you removed the DNS Zone configuration when creating Kubernetes manifests and
generating Ignition configs, you must manually create DNS records that point at
the Ingress load balancer. You can create either a wildcard
`*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other
records per your requirements.

.Prerequisites

* You deployed an OpenShift Container Platform cluster on Microsoft {cp} by using infrastructure that you provisioned.
* Install the OpenShift CLI (`oc`).
* Install or update the Azure CLI.

.Procedure

. Confirm the Ingress router has created a load balancer and populated the
`EXTERNAL-IP` field:
+
[source,terminal]
----
$ oc -n openshift-ingress get service router-default
----
+
.Example output
[source,terminal]
----
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
router-default   LoadBalancer   172.30.20.10   35.130.120.110   80:32288/TCP,443:31215/TCP   20
----

. Export the Ingress router IP as a variable:
+
[source,terminal]
----
$ export PUBLIC_IP_ROUTER=`oc -n openshift-ingress get service router-default --no-headers | awk '{print $4}'`
----
. Add a `*.apps` record to the public DNS zone.

.. If you are adding this cluster to a new public zone, run:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps -a ${PUBLIC_IP_ROUTER} --ttl 300
----

.. If you are adding this cluster to an already existing public zone, run:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n *.apps.${CLUSTER_NAME} -a ${PUBLIC_IP_ROUTER} --ttl 300
----
. Add a `*.apps` record to the DNS zone.

.. If you are adding this cluster to a new DNS zone, run:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps -a ${PUBLIC_IP_ROUTER} --ttl 300
----
.. If you are adding this cluster to an already existing DNS zone, run:
+
[source,terminal]
----
$ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n *.apps.${CLUSTER_NAME} -a ${PUBLIC_IP_ROUTER} --ttl 300
----

. Add a `*.apps` record to the private DNS zone:
.. Create a `*.apps` record by using the following command:
+
[source,terminal]
----
$ az network private-dns record-set a create -g ${RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps --ttl 300
----
.. Add the `*.apps` record to the private DNS zone by using the following command:
+
[source,terminal]
----
$ az network private-dns record-set a add-record -g ${RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps -a ${PUBLIC_IP_ROUTER}
----

If you prefer to add explicit domains instead of using a wildcard, you can
create entries for each of the cluster's current routes:

[source,terminal]
----
$ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
----

.Example output
[source,terminal]
----
oauth-openshift.apps.cluster.basedomain.com
console-openshift-console.apps.cluster.basedomain.com
downloads-openshift-console.apps.cluster.basedomain.com
alertmanager-main-openshift-monitoring.apps.cluster.basedomain.com
prometheus-k8s-openshift-monitoring.apps.cluster.basedomain.com
----

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-user-infra-completing_{context}"]
= Completing an {cp} installation on user-provisioned infrastructure

After you start the OpenShift Container Platform installation on Microsoft {cp}
user-provisioned infrastructure, you can monitor the cluster events until the
cluster is ready.

.Prerequisites

* Deploy the bootstrap machine for an OpenShift Container Platform cluster on user-provisioned {cp} infrastructure.
* Install the `oc` CLI and log in.

.Procedure

* Complete the cluster installation:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> wait-for install-complete <1>
----
+
.Example output
[source,terminal]
----
INFO Waiting up to 30m0s for the cluster to initialize...
----
<1> For `<installation_directory>`, specify the path to the directory that you
stored the installation files in.
+
[IMPORTANT]
====
* The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

[role="_additional-resources"]
.Additional resources

* About remote health monitoring
