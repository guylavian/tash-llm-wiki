---
title: "Installing a cluster on user-provisioned infrastructure in {gcp-short} by using Infrastructure Manager templates"
type: reference
domain: openshift
slug: installing-4-22-installing-gcp-user-infra
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-gcp-user-infra
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on user-provisioned infrastructure in {gcp-short} by using Infrastructure Manager templates

[id="installing-gcp-user-infra"]
= Installing a cluster on user-provisioned infrastructure in {gcp-short} by using Infrastructure Manager templates

[role="_abstract"]
In OpenShift Container Platform version , you can install a cluster on {gcp-first} that uses infrastructure that you provide.

The steps for performing a user-provided infrastructure install are outlined here. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods.

[IMPORTANT]
====
The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.
====

== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* If you use a firewall and plan to use the Telemetry service, you configured the firewall to allow the sites that your cluster requires access to.
* If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can manually create and maintain long-term credentials.
+
[NOTE]
====
Be sure to also review this site list if you are configuring a proxy.
====

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

[id="installation-gcp-user-infra-config-project"]
== Configuring your {gcp-short} project

Before you can install OpenShift Container Platform, you must configure a {gcp-first} project to host it.

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-project_{context}"]
= Creating a {gcp-short} project

To install OpenShift Container Platform, you must create a project in your {gcp-first} account to host the cluster.

.Procedure

* Create a project to host your OpenShift Container Platform cluster. See
Creating and Managing Projects in the {gcp-short} documentation.
+
[IMPORTANT]
====
Your {gcp-short} project must use the Premium Network Service Tier if you are using installer-provisioned infrastructure. The Standard Network Service Tier is not supported for clusters installed using the installation program. The installation program configures internal load balancing for the `api-int.<cluster_name>.<base_domain>` URL; the Premium Tier is required for internal load balancing.
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-enabling-api-services_{context}"]
= Enabling API services in {gcp-short}

Your {gcp-first} project requires access to several API services
to complete OpenShift Container Platform installation.

.Prerequisites

* You created a project to host your cluster.

.Procedure

* Enable the following required API services in the project that hosts your
cluster. You may also enable optional API services which are not required for installation. See
Enabling services
in the {gcp-short} documentation.
+
.Required API services
[cols="2a,3a",options="header"]
|===
|API service |Console service name

|Compute Engine API
|`compute.googleapis.com`

|Cloud Resource Manager API
|`cloudresourcemanager.googleapis.com`

|Cloud DNS API
|`dns.googleapis.com`

|IAM Service Account Credentials API
|`iamcredentials.googleapis.com`

|Identity and Access Management (IAM) API
|`iam.googleapis.com`

|Service Usage API
|`serviceusage.googleapis.com`

|===
+
.Optional API services
[cols="2a,3a",options="header"]
|===
|API service |Console service name

|Cloud Deployment Manager V2 API
|`deploymentmanager.googleapis.com`

|{gcp-full} APIs
|`cloudapis.googleapis.com`

|Service Management API
|`servicemanagement.googleapis.com`

|{gcp-full} Storage JSON API
|`storage-api.googleapis.com`

|Cloud Storage
|`storage-component.googleapis.com`

|===

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-dns_{context}"]
= Configuring DNS for {gcp-short}

To install OpenShift Container Platform, the {gcp-first} account you use must
have a dedicated public hosted zone
in the same project that you host the OpenShift Container Platform cluster.
in the project that hosts the shared VPC that you install the cluster into.
This zone must be authoritative for the domain. The
DNS service provides cluster DNS resolution and name lookup for external
connections to the cluster.

.Procedure

. Identify your domain, or subdomain, and registrar. You can transfer an existing domain and
registrar or obtain a new one through {gcp-short} or another source.
+
[NOTE]
====
If you purchase a new domain, it can take time for the relevant DNS
changes to propagate. For more information about purchasing domains
through Google, see Google Domains.
====

. Create a public hosted zone for your domain or subdomain in your {gcp-short} project. See
Creating public zones
in the {gcp-short} documentation.
+
Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain,
such as `clusters.openshiftcorp.com`.

. Extract the new authoritative name servers from the hosted zone records. See
Look up your Cloud DNS name servers
in the {gcp-short} documentation.
+
You typically have four name servers.

. Update the registrar records for the name servers that your domain
uses. For example, if you registered your domain to Google Domains, see the
following topic in the Google Domains Help:
How to switch to custom name servers.

. If you migrated your root domain to {gcp-full} DNS, migrate your DNS records. See Migrating to Cloud DNS in the {gcp-short} documentation.

. If you use a subdomain, follow your company's procedures to add its delegation records to the parent domain. This process might include a request to your company's IT department or the division that controls the root domain and DNS services for your company.

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-limits_{context}"]
= {gcp-short} account limits

The OpenShift Container Platform cluster uses a number of {gcp-first}
components, but the default
Quotas
do not affect your ability to install a default OpenShift Container Platform cluster.

A default cluster, which contains three compute and three control plane machines,
uses the following resources. Note that some resources are required only during
the bootstrap process and are removed after the cluster deploys.

.{gcp-short} resources used in a default cluster

[cols="2a,2a,2a,2a,2a",options="header"]
|===
|Service
|Component
|Location
|Total resources required
|Resources removed after bootstrap

|Service account |IAM	|Global	|6 |1
|Firewall rules	|Compute	|Global	|11 |1
|Forwarding rules	|Compute	|Global	|2	|0
|In-use global IP addresses	|Compute	|Global	|4	|1
|Health checks	|Compute	|Global	|3	|0
|Images	|Compute	|Global	|1	|0
|Networks	|Compute	|Global	|2	|0
|Static IP addresses	|Compute	|Region	|4	|1
|Routers	|Compute	|Global	|1	|0
|Routes	|Compute	|Global	|2	|0
|Subnetworks	|Compute	|Global	|2	|0
|Target pools	|Compute	|Global	|3	|0
|CPUs	|Compute	|Region	|28	|4
|Persistent disk SSD (GB)	|Compute	|Region	|896	|128

|Service account |IAM	|Global	|6 |1
|Firewall rules	|Networking	|Global	|11 |1
|Forwarding rules	|Compute	|Global	|2	|0
// |In-use IP addresses global	|Networking	|Global	|4	|1
|Health checks	|Compute	|Global	|2	|0
|Images	|Compute	|Global	|1	|0
|Networks	|Networking	|Global	|1	|0
// |Static IP addresses	|Compute	|Region	|4	|1
|Routers	|Networking	|Global	|1	|0
|Routes	|Networking	|Global	|2	|0
|Subnetworks	|Compute	|Global	|2	|0
|Target pools	|Networking	|Global	|2	|0
// |CPUs	|Compute	|Region	|28	|4
// |Persistent Disk SSD (GB)	|Compute	|Region	|896	|128
|===

[NOTE]
====
If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region.
====

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, static IP addresses, and persistent disk SSD (storage) quotas are the ones that are most likely to be insufficient.

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit:

* `asia-east2`
* `asia-northeast2`
* `asia-south1`
* `australia-southeast1`
* `europe-north1`
* `europe-west2`
* `europe-west3`
* `europe-west6`
* `northamerica-northeast1`
* `southamerica-east1`
* `us-west2`

You can increase resource quotas from the {gcp-short} console, but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-service-account_{context}"]
= Creating a service account in {gcp-short}

[role="_abstract"]
OpenShift Container Platform requires a {gcp-first} service account that provides authentication and authorization to access data in the Google APIs. If you do not have an existing IAM service account that contains the required roles in your project, you must create one.

[NOTE]
====
To reduce the scope of permissions granted to the main service account in your Google Cloud project while still being able to use the {gcp-short} Container Storage Interface (CSI) Driver Operator, you can transfer the control of permissions from the project-wide service account to the control plane and compute node service accounts instead, thus reducing the scope of the permission. For more information, see Section _Reducing permissions while using the {gcp-short} CSI Driver Operator_.
====

.Prerequisites

* You created a project to host your cluster.

.Procedure

. Create a service account in the project that you use to host your
OpenShift Container Platform cluster. See
Creating a service account
in the {gcp-short} documentation.

. Grant the service account the appropriate permissions. You can either
grant the individual permissions that follow or assign the `Owner` role to it.
See Granting roles to a service account for specific resources.
+
[NOTE]
====
While making the service account an owner of the project is the easiest way to gain the required permissions, it means that service account has complete control over the project. You must determine if the risk that comes from offering that power is acceptable.
====

. You can create the service account key in JSON format, or attach the service account to a {gcp-short} virtual machine.
See Creating service account keys and Creating and enabling service accounts for instances in the {gcp-short} documentation.
+
[NOTE]
====
If you use a virtual machine with an attached service account to create your cluster, you must set `credentialsMode: Manual` in the `install-config.yaml` file before installation.
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-permissions_{context}"]
= Required {gcp-short} roles

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization's security policies require a more restrictive set of permissions, you can create a service account with the following permissions. If you deploy your cluster into an existing virtual private cloud (VPC), the service account does not require certain networking permissions, which are noted in the following lists:

.Required roles for the installation program
* Compute Admin
* Role Administrator
* Security Admin
* Service Account Admin
* Service Account Key Admin
* Service Account User
* Storage Admin

.Required roles for creating network resources during installation
* DNS Administrator

.Required roles for using the Cloud Credential Operator in passthrough mode
* Compute Load Balancer Admin
* Tag User

.Required roles for user-provisioned {gcp-short} infrastructure
* Cloud Infrastructure Manager Admin

The following roles are applied to the service accounts that the control plane and compute machines use:

.{gcp-short} service account roles
[cols="2a,2a",options="header"]
|===
|Account
|Roles
.5+|Control Plane
|`roles/compute.instanceAdmin`
|`roles/compute.networkAdmin`
|`roles/compute.securityAdmin`
|`roles/storage.admin`
|`roles/iam.serviceAccountUser`
.3+|Compute
|`roles/compute.viewer`
|`roles/storage.admin`
|`roles/artifactregistry.reader`
|===

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="minimum-required-permissions-upi-gcp_{context}"]
= Required {gcp-short} permissions for user-provisioned infrastructure

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform.

If your organization's security policies require a more restrictive set of permissions, you can create custom roles with the necessary permissions. The following permissions are required for the user-provisioned infrastructure for creating and deleting the OpenShift Container Platform cluster.

.Required permissions for creating network resources
[%collapsible]
====
* `compute.addresses.create`
* `compute.addresses.createInternal`
* `compute.addresses.delete`
* `compute.addresses.get`
* `compute.addresses.list`
* `compute.addresses.use`
* `compute.addresses.useInternal`
* `compute.firewalls.create`
* `compute.firewalls.delete`
* `compute.firewalls.get`
* `compute.firewalls.list`
* `compute.forwardingRules.create`
* `compute.forwardingRules.get`
* `compute.forwardingRules.list`
* `compute.forwardingRules.setLabels`
* `compute.globalAddresses.create`
* `compute.globalAddresses.get`
* `compute.globalAddresses.use`
* `compute.globalForwardingRules.create`
* `compute.globalForwardingRules.get`
* `compute.globalForwardingRules.setLabels`
* `compute.networks.create`
* `compute.networks.get`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.networks.use`
* `compute.routers.create`
* `compute.routers.get`
* `compute.routers.list`
* `compute.routers.update`
* `compute.routes.list`
* `compute.subnetworks.create`
* `compute.subnetworks.get`
* `compute.subnetworks.list`
* `compute.subnetworks.use`
* `compute.subnetworks.useExternalIp`
====

.Required permissions for creating load balancer resources
[%collapsible]
====
* `compute.backendServices.create`
* `compute.backendServices.get`
* `compute.backendServices.list`
* `compute.backendServices.update`
* `compute.backendServices.use`
* `compute.regionBackendServices.create`
* `compute.regionBackendServices.get`
* `compute.regionBackendServices.list`
* `compute.regionBackendServices.update`
* `compute.regionBackendServices.use`
* `compute.targetPools.addInstance`
* `compute.targetPools.create`
* `compute.targetPools.get`
* `compute.targetPools.list`
* `compute.targetPools.removeInstance`
* `compute.targetPools.use`
* `compute.targetTcpProxies.create`
* `compute.targetTcpProxies.get`
* `compute.targetTcpProxies.use`
====

.Required permissions for creating DNS resources
[%collapsible]
====
* `dns.changes.create`
* `dns.changes.get`
* `dns.managedZones.create`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.networks.bindPrivateDNSZone`
* `dns.resourceRecordSets.create`
* `dns.resourceRecordSets.list`
* `dns.resourceRecordSets.update`
====

.Required permissions for creating Service Account resources
[%collapsible]
====
* `iam.serviceAccountKeys.create`
* `iam.serviceAccountKeys.delete`
* `iam.serviceAccountKeys.get`
* `iam.serviceAccountKeys.list`
* `iam.serviceAccounts.actAs`
* `iam.serviceAccounts.create`
* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.get`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`
====

.Required permissions for creating compute resources
[%collapsible]
====
* `compute.disks.create`
* `compute.disks.get`
* `compute.disks.list`
* `compute.instanceGroups.create`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.get`
* `compute.instanceGroups.list`
* `compute.instanceGroups.update`
* `compute.instanceGroups.use`
* `compute.instances.create`
* `compute.instances.delete`
* `compute.instances.get`
* `compute.instances.list`
* `compute.instances.setLabels`
* `compute.instances.setMetadata`
* `compute.instances.setServiceAccount`
* `compute.instances.setTags`
* `compute.instances.use`
* `compute.machineTypes.get`
* `compute.machineTypes.list`
====

.Required for creating storage resources
[%collapsible]
====
* `storage.buckets.create`
* `storage.buckets.delete`
* `storage.buckets.get`
* `storage.buckets.list`
* `storage.objects.create`
* `storage.objects.delete`
* `storage.objects.get`
* `storage.objects.list`
====

.Required permissions for creating health check resources
[%collapsible]
====
* `compute.healthChecks.create`
* `compute.healthChecks.get`
* `compute.healthChecks.list`
* `compute.healthChecks.useReadOnly`
* `compute.httpHealthChecks.create`
* `compute.httpHealthChecks.get`
* `compute.httpHealthChecks.list`
* `compute.httpHealthChecks.useReadOnly`
* `compute.regionHealthChecks.create`
* `compute.regionHealthChecks.get`
* `compute.regionHealthChecks.useReadOnly`
====

.Required permissions to get {gcp-short} zone and region related information
[%collapsible]
====
* `compute.globalOperations.get`
* `compute.regionOperations.get`
* `compute.regions.get`
* `compute.regions.list`
* `compute.zoneOperations.get`
* `compute.zones.get`
* `compute.zones.list`
====

.Required permissions for checking services and quotas
[%collapsible]
====
* `monitoring.timeSeries.list`
* `serviceusage.quotas.get`
* `serviceusage.services.list`
====

.Required IAM permissions for installation
[%collapsible]
====
* `iam.roles.get`
====

.Required permissions when authenticating without a service account key
[%collapsible]
====
* `iam.serviceAccounts.signBlob`
====

.Required permissions when providing Key Management Service (KMS) key rings
[%collapsible]
====
* `cloudkms.keyRings.list`
====

.Required Images permissions for installation
[%collapsible]
====
* `compute.images.create`
* `compute.images.delete`
* `compute.images.get`
* `compute.images.list`
====

.Optional permission for running gather bootstrap
[%collapsible]
====
* `compute.instances.getSerialPortOutput`
====

.Required permissions for deleting network resources
[%collapsible]
====
* `compute.addresses.delete`
* `compute.addresses.deleteInternal`
* `compute.addresses.list`
* `compute.addresses.setLabels`
* `compute.firewalls.delete`
* `compute.firewalls.list`
* `compute.forwardingRules.delete`
* `compute.forwardingRules.list`
* `compute.globalAddresses.delete`
* `compute.globalAddresses.list`
* `compute.globalForwardingRules.delete`
* `compute.globalForwardingRules.list`
* `compute.networks.delete`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.routers.delete`
* `compute.routers.list`
* `compute.routes.list`
* `compute.subnetworks.delete`
* `compute.subnetworks.list`
====

.Required permissions for deleting load balancer resources
[%collapsible]
====
* `compute.backendServices.delete`
* `compute.backendServices.list`
* `compute.regionBackendServices.delete`
* `compute.regionBackendServices.list`
* `compute.targetPools.delete`
* `compute.targetPools.list`
* `compute.targetTcpProxies.delete`
* `compute.targetTcpProxies.list`
====

.Required permissions for deleting DNS resources
[%collapsible]
====
* `dns.changes.create`
* `dns.managedZones.delete`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.resourceRecordSets.delete`
* `dns.resourceRecordSets.list`
====

.Required permissions for deleting Service Account resources
[%collapsible]
====
* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`
====

.Required permissions for deleting compute resources
[%collapsible]
====
* `compute.disks.delete`
* `compute.disks.list`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.list`
* `compute.instances.delete`
* `compute.instances.list`
* `compute.instances.stop`
* `compute.machineTypes.list`
====

.Required for deleting storage resources
[%collapsible]
====
* `storage.buckets.delete`
* `storage.buckets.getIamPolicy`
* `storage.buckets.list`
* `storage.objects.delete`
* `storage.objects.list`
====

.Required permissions for deleting health check resources
[%collapsible]
====
* `compute.healthChecks.delete`
* `compute.healthChecks.list`
* `compute.httpHealthChecks.delete`
* `compute.httpHealthChecks.list`
* `compute.regionHealthChecks.delete`
* `compute.regionHealthChecks.list`
====

.Required Images permissions for deletion
[%collapsible]
====
* `compute.images.delete`
* `compute.images.list`
====

.Required permissions to get Region related information
[%collapsible]
====
* `compute.regions.get`
====

.Required Deployment Manager permissions
[%collapsible]
====
* config.deployments.create
* config.deployments.delete
* config.deployments.get
* config.deployments.list
* config.operations.get
* config.resources.list
* cloudbuild.builds.create
* cloudbuild.builds.get
====

[role="_additional-resources"]
.Additional resources

* Optimizing storage

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-regions_{context}"]
= Supported {gcp-short} regions

You can deploy an OpenShift Container Platform cluster to the following {gcp-first}
regions:

* `africa-south1` (Johannesburg, South Africa)
* `asia-east1` (Changhua County, Taiwan)
* `asia-east2` (Hong Kong)
* `asia-northeast1` (Tokyo, Japan)
* `asia-northeast2` (Osaka, Japan)
* `asia-northeast3` (Seoul, South Korea)
* `asia-south1` (Mumbai, India)
* `asia-south2` (Delhi, India)
* `asia-southeast1` (Jurong West, Singapore)
* `asia-southeast2` (Jakarta, Indonesia)
* `australia-southeast1` (Sydney, Australia)
* `australia-southeast2` (Melbourne, Australia)
* `europe-central2` (Warsaw, Poland)
* `europe-north1` (Hamina, Finland)
* `europe-southwest1` (Madrid, Spain)
* `europe-west1` (St. Ghislain, Belgium)
* `europe-west2` (London, England, UK)
* `europe-west3` (Frankfurt, Germany)
* `europe-west4` (Eemshaven, Netherlands)
* `europe-west6` (Zürich, Switzerland)
* `europe-west8` (Milan, Italy)
* `europe-west9` (Paris, France)
* `europe-west12` (Turin, Italy)
* `me-central1` (Doha, Qatar, Middle East)
* `me-central2` (Dammam, Saudi Arabia, Middle East)
* `me-west1` (Tel Aviv, Israel)
* `northamerica-northeast1` (Montréal, Québec, Canada)
* `northamerica-northeast2` (Toronto, Ontario, Canada)
* `southamerica-east1` (São Paulo, Brazil)
* `southamerica-west1` (Santiago, Chile)
* `us-central1` (Council Bluffs, Iowa, USA)
* `us-east1` (Moncks Corner, South Carolina, USA)
* `us-east4` (Ashburn, Northern Virginia, USA)
* `us-east5` (Columbus, Ohio)
* `us-south1` (Dallas, Texas)
* `us-west1` (The Dalles, Oregon, USA)
* `us-west2` (Los Angeles, California, USA)
* `us-west3` (Salt Lake City, Utah, USA)
* `us-west4` (Las Vegas, Nevada, USA)

[NOTE]
====
To determine which machine type instances are available by region and zone, see the Google documentation.
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-install-cli_{context}"]
= Installing and configuring CLI tools for {gcp-short}

To install OpenShift Container Platform on {gcp-first} using user-provisioned
infrastructure, you must install and configure the CLI tools for {gcp-short}.

.Prerequisites

* You created a project to host your cluster.
* You created a service account and granted it the required permissions.

.Procedure

. Install the following binaries in `$PATH`:
+
--
* `gcloud`
* `gsutil`
--
+
See Install the latest Cloud SDK version
in the {gcp-short} documentation.

. Authenticate using the `gcloud` tool with your configured service account.
+
See Authorizing with a service account in the {gcp-short} documentation.

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
// installing/installing_gcp/installing-gcp-customizations.adoc
// installing/installing_gcp/installing-gcp-network-customizations.adoc
// installing/installing_gcp/installing-gcp-private.adoc
// installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// installing/installing_gcp/installing-gcp-user-infra.adoc
// installing/installing_gcp/installing-gcp-vpc.adoc
// installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-tested-machine-types_{context}"]
= Tested instance types for {gcp-short}

The following {gcp-full} instance types have been tested with OpenShift Container Platform.

[NOTE]
====
Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see regions and zones (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see machine series support for Hyperdisk (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in _Storage_.
====

.Machine series
[%collapsible]
====

====

// module included in the following assemblies
//
// installing/installing_gcp/installing-gcp-customizations.adoc
// installing/installing_gcp/installing-gcp-network-customizations.adoc
// installing/installing_gcp/installing-gcp-private.adoc
// installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// installing/installing_gcp/installing-gcp-user-infra.adoc
// installing/installing_gcp/installing-gcp-vpc.adoc
// installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-tested-machine-types-arm_{context}"]
= Tested instance types for {gcp-short} on 64-bit ARM infrastructures

The following {gcp-first} 64-bit ARM instance types have been tested with OpenShift Container Platform.

.Machine series for 64-bit ARM machines
[%collapsible]
====

====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-custom-machine-types_{context}"]
= Using custom machine types

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:
+
--
`custom-<number_of_cpus>-<amount_of_memory_in_mb>`

For example, `custom-6-20480`.
--

As part of the installation process, you specify the custom machine type in the `install-config.yaml` file.

.Sample `install-config.yaml` file with a custom machine type

[source,yaml]
----
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
----

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
* Installation configuration parameters for {gcp-short}

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-enabling-shielded-vms_{context}"]
= Enabling Shielded VMs

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google's documentation on Shielded VMs.

[NOTE]
====
Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.
====

.Procedure

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:
.. To use shielded VMs for only control plane machines:
+
[source,yaml]
----
controlPlane:
  platform:
    gcp:
       secureBoot: Enabled
----
+
.. To use shielded VMs for only compute machines:
+
[source,yaml]
----
compute:
- platform:
    gcp:
       secureBoot: Enabled
----
+
.. To use shielded VMs for all machines:
+
[source,yaml]
----
platform:
  gcp:
    defaultMachinePlatform:
       secureBoot: Enabled
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-enabling-confidential-vms_{context}"]
= Enabling Confidential VMs

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google's documentation on Confidential Computing. You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

[NOTE]
====
Confidential VMs are currently not supported on 64-bit ARM architectures.
====

.Procedure

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:
.. To use confidential VMs for only control plane machines:
+
[source,yaml]
----
controlPlane:
  platform:
    gcp:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging <1>
       type: n2d-standard-8 <2>
       onHostMaintenance: Terminate <3>
----
+
--
<1> Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional {gcp-first} configuration parameters".
<2> Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see Supported operating systems and machine types.
<3> Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
--
+
.. To use confidential VMs for only compute machines:
+
[source,yaml]
----
compute:
- platform:
    gcp:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging
       type: n2d-standard-8
       onHostMaintenance: Terminate
----
+
.. To use confidential VMs for all machines:
+
[source,yaml]
----
platform:
  gcp:
    defaultMachinePlatform:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging
       type: n2d-standard-8
       onHostMaintenance: Terminate
----

[role="_additional-resources"]
.Additional resources
* Additional {gcp-first} configuration parameters

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

* Optional: Adding the ingress DNS records

[id="installation-gcp-user-infra-exporting-common-variables"]
== Exporting common variables

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
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-user-infra-exporting-common-variables_{context}"]
= Exporting common variables for Infrastructure Manager templates

You must export a common set of variables that are used with the provided Infrastructure Manager templates used to assist in installing a cluster with user-provisioned infrastructure on {gcp-first}.

[NOTE]
====
Specific Infrastructure Manager templates can also require additional exported variables, which are detailed in their related procedures.
====

.Procedure

* Export the following common variables to be used by the provided Infrastructure Manager templates. For any command with `<installation_directory>`, specify the path to the directory that you stored the installation files in.

** Export the `BASE_DOMAIN` variable by running the following command:
+
[source,terminal]
----
$ export BASE_DOMAIN='<base_domain>'
----
+
`<base_domain>`:: If you are installing a cluster into a shared VPC, specify the value for the host project.

** Export the `BASE_DOMAIN_ZONE_NAME` variable by running the following command:
+
[source,terminal]
----
$ export BASE_DOMAIN_ZONE_NAME='<base_domain_zone_name>'
----
+
`<base_domain_zone_name>`:: Specifies the base domain zone name.

** Export the `NETWORK_CIDR` variable by running the following command:
+
[source,terminal]
----
$ export NETWORK_CIDR='<network_cidr>'
----
+
`<network_cidr>`:: Specifies the network CIDR your cluster uses. For example, `10.0.0.0/16`.

** Export the `MASTER_SUBNET_CIDR` variable by running the following command:
+
[source,terminal]
----
$ export MASTER_SUBNET_CIDR='<master_subnet_cidr>'
----
+
`<master_subnet_cidr>`:: Specifies the network CIDR that your cluster's control plane uses. For example, `10.0.0.0/17`.

** Export the `WORKER_SUBNET_CIDR` variable by running the following command:
+
[source,terminal]
----
$ export WORKER_SUBNET_CIDR='<worker_subnet_cidr>'
----
+
`<worker_subnet_cidr>`:: Specifies the network CIDR that your cluster's compute machines use. For example, `10.0.128.0/17`.

** Export the `KUBECONFIG` variable by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
----

** Export the `CLUSTER_NAME` variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_NAME=`jq -r .clusterName <installation_directory>/metadata.json`
----

** Export the `INFRA_ID` variable by running the following command:
+
[source,terminal]
----
$ export INFRA_ID=`jq -r .infraID <installation_directory>/metadata.json`
----

** Export the `PROJECT_NAME` variable by running the following command:
+
[source,terminal]
----
$ export PROJECT_NAME=`jq -r .gcp.projectID <installation_directory>/metadata.json`
----

** If you are installing a cluster into a shared VPC, export the `HOST_PROJECT` variable by running the following command:
+
[source,terminal]
----
$ export HOST_PROJECT=<host_project_name>
----
`<host_project_name>` specifies the name of the host project that contains the shared VPC.

** If you are installing a cluster into a shared VPC, export the `HOST_PROJECT_ACCOUNT` variable by running the following command:
+
[source,terminal]
----
$ export HOST_PROJECT_ACCOUNT=<host_project_account>
----
`<host_project_account>` specifies the name of an account that can access the host project that contains the shared VPC.

** Export the `REGION` variable by running the following command:
+
[source,terminal]
----
$ export REGION=`jq -r .gcp.region <installation_directory>/metadata.json`
----

** Export the `ZONE_0` variable by running the following command:
+
[source,terminal]
----
$ export ZONE_0=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[0]' | cut -d "/" -f9)
----

** Export the `ZONE_1` variable by running the following command:
+
[source,terminal]
----
$ export ZONE_1=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[1]' | cut -d "/" -f9)
----

** Export the `ZONE_2` variable by running the following command:
+
[source,terminal]
----
$ export ZONE_2=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[2]' | cut -d "/" -f9)
----

** Export the `SERVICE_ACCOUNT_EMAIL` variable by running the following command:
+
[source,terminal]
----
$ export SERVICE_ACCOUNT_EMAIL="<service_account_email>"
----
+
`<service_account_email>`:: Specifies the email address of the service account you used for the installation.

** Export the `INSTALL_SERVICE_ACCOUNT` variable by running the following command:
+
[source,terminal]
----
$ export INSTALL_SERVICE_ACCOUNT="projects/${PROJECT_NAME}/serviceAccounts/${SERVICE_ACCOUNT_EMAIL}"
----

** Export the `CLUSTER_DOMAIN` variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_DOMAIN="${CLUSTER_NAME}.${BASE_DOMAIN}"
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-creating-gcp-vpc_{context}"]
= Creating a VPC in {gcp-short}

[role="_abstract"]
You must create a VPC in {gcp-first} for your OpenShift Container Platform cluster to use. You can customize the VPC to meet your requirements. One way to create the VPC is to modify the provided Infrastructure Manager template.

[NOTE]
====
If you do not use the provided Infrastructure Manager template to create your {gcp-short} infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You have defined the variables in the _Exporting common variables_ section.

.Procedure

. Copy the template from the *Infrastructure Manager template for the VPC* section of this topic and save it as `01_vpc.tf` in a directory called `01_vpc` on your computer. This template describes the VPC that your cluster requires.

. Create a VPC by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <vpc_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},master_subnet_cidr=${MASTER_SUBNET_CIDR},worker_subnet_cidr=${WORKER_SUBNET_CIDR} \
  --project=${PROJECT_NAME} \
  --local-source=./01_vpc \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
+
`<vpc_deployment_name>` specifies the name of the VPC deployment you create.

. Configure environment variables that will be used to create other cluster infrastructure.

.. Configure the `CLUSTER_NETWORK` environment variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_NETWORK=$(gcloud compute networks describe ${INFRA_ID}-network --format json | jq -r .selfLink)
----

.. Configure the `CONTROL_SUBNET` environment variable by running the following command:
+
[source,terminal]
----
$ export CONTROL_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-master-subnet --region=${REGION} --format json | jq -r .selfLink)
----

.. Configure the `COMPUTE_SUBNET` environment variable by running the following command:
+
[source,terminal]
----
$ export COMPUTE_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-worker-subnet --region=${REGION} --format json | jq -r .selfLink)
----

.Verification

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-infrastructure-manager-vpc_{context}"]
= Infrastructure Manager template for the VPC

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the VPC that you need for your OpenShift Container Platform cluster:

.`01_vpc.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
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
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-creating-gcp-lb_{context}"]
= Creating load balancers in {gcp-short}

[role="_abstract"]
You must configure load balancers in {gcp-first} for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template.

[NOTE]
====
If you do not use the provided template to create your {gcp-short} infrastructure, you must review the provided information and manually create the infrastructure.
If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You have defined the variables in the _Exporting common variables_ section.
* If you are not installing a cluster into a shared VPC, you have defined the variables in the _Creating a VPC in {gcp-short}_ section.

.Procedure

. If you are installing a cluster into a shared VPC, set environment variables for the cluster network and control plane subnet.

.. Determine the shared VPC network name by running the following command:
+
[source,terminal]
----
$ gcloud compute networks list
----

.. Set the `CLUSTER_NETWORK` variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_NETWORK=$(gcloud compute networks describe <network_name> --format json | jq -r .selfLink)
----
+
`<network_name>` specifies the name of the network you determined.

.. List the available network subnets by running the following command:
+
[source,terminal]
----
$ gcloud compute networks subnets list --network=<network_name>
----
`<network_name>` specifies the name of the network you determined.

.. Select a subnet from the list, and set the `CONTROL_SUBNET` variable by running the following command:
+
[source,terminal]
----
$ export CONTROL_SUBNET=<control_subnet>
----
+
`<control_subnet>` specifies the name of the subnet you selected from the list of subnets.

. Copy the template from the *Infrastructure Manager template for the internal load balancer* section of this topic and save it as `02_lb_int.tf` in a directory called `02_lb_int` on your computer. This template describes the internal load balancing objects that your cluster requires.

.. Create an internal load balancer by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <internal_lb_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},control_subnet=${CONTROL_SUBNET},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2} \
  --project=${PROJECT_NAME} \
  --local-source=./02_lb_int \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
+
`<internal_lb_deployment_name>` specifies the name of the internal load balancer deployment you create.

.. Export the `CLUSTER_IP` variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-ip --region=${REGION} --format json | jq -r .address)
----

. Optional: For a public or externally available cluster, copy the template from the *Infrastructure Manager template for the external load balancer* section of this topic and save it as `02_lb_ext.tf` in a directory called `02_lb_ext` on your computer. This template describes the external load balancing objects that your cluster requires.

.. Create an external load balancer by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <external_lb_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./02_lb_ext \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
+
`<external_lb_deployment_name>` specifies the name of the external load balancer deployment you create.

.. Export the `CLUSTER_PUBLIC_IP` variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_PUBLIC_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-public-ip --region=${REGION} --format json | jq -r .address)
----

.Verification

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-infrastructure-manager-ext-lb_{context}"]
= Infrastructure Manager template for the external load balancer

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the external load balancer that you need for your OpenShift Container Platform cluster:

.`02_lb_ext.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-infrastructure-manager-int-lb_{context}"]
= Infrastructure Manager template for the internal load balancer

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the internal load balancer that you need for your OpenShift Container Platform cluster:

.`02_lb_int.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-creating-gcp-private-dns_{context}"]
= Creating a private DNS zone in {gcp-short}

[role="_abstract"]
You must configure a private DNS zone in {gcp-first} for your OpenShift Container Platform cluster to use. One way to create this component is to modify the provided Infrastructure Manager template.

[NOTE]
====
If you do not use the provided template to create your {gcp-short} infrastructure, you must review the provided information and manually create the infrastructure.
If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in {gcp-short}_ sections.

.Procedure

. Copy the template from the *Infrastructure Manager template for the private DNS* section of this topic and save it as `02_dns.tf` in a folder called `02_dns` on your computer. This template describes the private DNS objects that your cluster requires.

. If you are installing a cluster into a shared VPC, and the host project already has a private DNS zone, skip this step. Create the DNS zone by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <dns_zone_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_domain=${CLUSTER_DOMAIN},cluster_network=${CLUSTER_NETWORK} \
  --project=${PROJECT_NAME} \
  --local-source=./02_dns \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
`<dns_zone_deployment_name>` specifies the name of the DNS zone deployment you create.

. The templates do not create DNS entries due to limitations of Infrastructure Manager, so you must create them manually:
+
.. Add the internal DNS entries by running the following commands:
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api-int.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api-int.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
----
+
.. For an external cluster, also add the external DNS entries by running the following commands:
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
----
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} dns record-sets transaction add ${CLUSTER_PUBLIC_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
----
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
----
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${CLUSTER_PUBLIC_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
----

.Verification

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-infrastructure-manager-private-dns_{context}"]
= Infrastructure Manager template for the private DNS

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the private DNS that you need for your OpenShift Container Platform cluster:

.`02_dns.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-creating-gcp-firewall-rules-vpc_{context}"]
= Creating firewall rules and IAM roles in {gcp-short}

[role="_abstract"]
You must create firewall rules and IAM roles in {gcp-first} for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template.
If you are installing a cluster into a shared VPC and the host project already has the necessary firewall rules and IAM roles, you can skip creating these resources.

[NOTE]
====
If you do not use the provided Infrastructure Manager template to create your {gcp-short} infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in {gcp-short}_ sections.

.Procedure

. Copy the template from the *Infrastructure Manager template for firewall rules and IAM roles* section of this topic and save it as `03_security.tf` in a folder called `03_security` on your computer. This template describes the security groups that your cluster requires.

. Create the firewall rules and IAM roles by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <security_deployment_name> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./03_security \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},network_cidr=${NETWORK_CIDR} \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
`<security_deployment_name>` specifies the name of the deployment of firewall rules and IAM roles.

. Configure service account variables based on the roles you created by running the following commands:
+
[source,terminal]
----
$ export MASTER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-m@${PROJECT_NAME}." --format json | jq -r '.[0].email')
----
+
[source,terminal]
----
$ export WORKER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-w@${PROJECT_NAME}." --format json | jq -r '.[0].email')
----

.Verification

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-infrastructure-manager-firewall-rules_{context}"]
= Infrastructure Manager template for firewall rules and IAM roles

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the firewall rules and IAM roles that you need for your OpenShift Container Platform cluster:

.`03_security.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-creating-gcp-iam-shared-vpc_{context}"]
= Creating IAM policy bindings in {gcp-short}

[role="_abstract"]
You must create IAM policy bindings in {gcp-first} for your OpenShift Container Platform cluster to use.

.Prerequisites

* You have defined the variables in the _Exporting common variables_ section.

.Procedure

. Export the variable for the subnet that hosts the compute machines by running the following command:
+
[source,terminal]
----
$ export COMPUTE_SUBNET=(`gcloud compute networks subnets describe ${INFRA_ID}-worker-subnet --region=${REGION} --format json | jq -r .selfLink`)
----

. Assign the permissions that the installation program requires to the service accounts for the subnets that host the control plane and compute subnets:
+
.. Grant the `networkViewer` role of the project that hosts your shared VPC to the master service account by running the following command:
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} projects add-iam-policy-binding ${HOST_PROJECT} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkViewer"
----
+
.. Grant the `networkUser` role to the master service account for the control plane subnet by running the following command:
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_CONTROL_SUBNET}" --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
----
+
.. Grant the `networkUser` role to the worker service account for the control plane subnet by running the following command:
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_CONTROL_SUBNET}" --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
----
+
.. Grant the `networkUser` role to the master service account for the compute subnet by running the following command:
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_COMPUTE_SUBNET}" --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
----
+
.. Grant the `networkUser` role to the worker service account for the compute subnet by running the following command:
+
[source,terminal]
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_COMPUTE_SUBNET}" --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
----

. The templates do not create the policy bindings due to limitations of Infrastructure Manager, so you must create them manually by running the following commands:
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.instanceAdmin"
----
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkAdmin"
----
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.securityAdmin"
----
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/iam.serviceAccountUser"
----
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
----
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.viewer"
----
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
----

. Create a service account key and store it locally for later use by running the following command:
+
[source,terminal]
----
$ gcloud iam service-accounts keys create service-account-key.json --iam-account=${MASTER_SERVICE_ACCOUNT}
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc

[id="installation-gcp-user-infra-rhcos_{context}"]
= Creating the {op-system} cluster image for the {gcp-short} infrastructure

[role="_abstract"]
You must use a valid {op-system-first} image for {gcp-first} for your OpenShift Container Platform nodes.

.Prerequisites

* You have downloaded the `openshift-install` binary.

.Procedure

. Obtain the image name by running the following command:
+
[source,terminal]
----
$ source_image=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.name')
----

. Obtain the project name by running the following command:
+
[source,terminal]
----
$ source_project=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.project')
----

. Create the image by running the following command:
+
[source,terminal]
----
$ gcloud compute images create "${INFRA_ID}-rhcos-image" \
    --source-image="${source_image}" --source-image-project="${source_project}"
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-creating-gcp-bootstrap_{context}"]
= Creating the bootstrap machine in {gcp-short}

[role="_abstract"]
You must create the bootstrap machine in {gcp-first} to use during OpenShift Container Platform cluster initialization. One way to create this machine is to modify the provided Infrastructure Manager template.

[NOTE]
====
If you do not use the provided Infrastructure Manager template to create your bootstrap machine, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you need to redeploy the bootstrap machine for any reason, delete the existing bootstrap VM first. If you redeploy the bootstrap machine without deleting the existing VM, Infrastructure Manager will update the metadata and appear to succeed, but the Ignition file will not be executed again. This will result in the VM still being based on the old Ignition data.
====

.Prerequisites

* Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in {gcp-short}_ sections.

.Procedure

. Copy the template from the *Infrastructure Manager template for the bootstrap machine* section of this topic and save it as `04_bootstrap.tf` in a folder called `04_bootstrap` on your computer. This template describes the bootstrap machine that your cluster requires.

** You can edit the `04_bootstrap.tf` file to add additional tags to the bootstrap machine, by modifying the existing `tags` stanza as follows:
+
[source,bash]
----
resource "google_compute_instance" "bootstrap" {
# ...
  tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-bootstrap",
    "custom-tag-example"
  ]
# ...
}
----

. Export the location of the {op-system-first} image that the installation program requires by running the following command:
+
[source,terminal]
----
$ export CLUSTER_IMAGE=(`gcloud compute images describe ${INFRA_ID}-rhcos-image --format json | jq -r .selfLink`)
----

. Create a bucket by running the following command:
+
[source,terminal]
----
$ gcloud storage buckets create "gs://${INFRA_ID}-bootstrap-ignition"
----

. Upload the `bootstrap.ign` file by running the following command:
+
[source,terminal]
----
$ gcloud storage cp bootstrap.ign "gs://${INFRA_ID}-bootstrap-ignition/"
----

. Create a signed URL for the bootstrap instance and export the URL from the output as a variable by running the following command:
+
[source,terminal]
----
$ export BOOTSTRAP_IGN="$(gcloud storage sign-url --duration=2h --private-key-file=service-account-key.json "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign" | grep "^signed_url:" | awk '{print $2}')"
----

. Create the bootstrap deployment by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <bootstrap_deployment_name> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./04_bootstrap \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone=${ZONE_0},cluster_network=${CLUSTER_NETWORK},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},bootstrap_ign="${BOOTSTRAP_IGN}",is_public_cluster=<public_cluster_status> \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
+
where:

`<bootstrap_deployment_name>`:: Specifies the name of the bootstrap deployment.
`<public_cluster_status>`:: Specifies whether the cluster is public or private. If it is a public cluster, specify `true`. If it is a private cluster, specify `false`.

. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the bootstrap machine manually.

.. Add the bootstrap instance to the internal load balancer instance group by running the following command:
+
[source,terminal]
----
$ gcloud compute instance-groups unmanaged add-instances \
    ${INFRA_ID}-bootstrap-ig --zone=${ZONE_0} --instances=${INFRA_ID}-bootstrap
----

.. Add the bootstrap instance group to the internal load balancer backend service by running the following command:
+
[source,terminal]
----
$ gcloud compute backend-services add-backend \
    ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
----

.Verification

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-infrastructure-manager-bootstrap_{context}"]
= Infrastructure Manager template for the bootstrap machine

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster:

.`04_bootstrap.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-creating-gcp-control-plane_{context}"]
= Creating the control plane machines in {gcp-short}

[role="_abstract"]
You must create the control plane machines in {gcp-first} for your cluster to use. One way to create these machines is to modify the provided Infrastructure Manager template.

[NOTE]
====
If you do not use the provided template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You defined the variables in the _Exporting common variables_, _Creating load balancers in {gcp-short}_, _Creating IAM roles in {gcp-short}_, and _Creating the bootstrap machine in {gcp-short}_ sections.
* You created the bootstrap machine.
* You created the Ignition configuration files.

.Procedure

. Copy the template from the *Infrastructure Manager template for control plane machines* section of this topic and save it as `05_control_plane.tf` in a folder called `05_control_plane` on your computer. This template describes the control plane machines that your cluster requires.

** You can edit the `05_control_plane.tf` file to add additional tags to the control plane machines, by modifying the existing `tags` stanza. The following example adds a custom tag to the first control plane machine, which is named `master_0`:
+
[source,bash]
----
resource "google_compute_instance" "master_0" {
# ...
  tags = [
    "${var.infra_id}-master",
    "custom_tag_example"
  ]
# ...
}
----

. Copy the `master.ign` file from your installation directory into the `05_control_plane` folder by running the following command:
+
[source,terminal]
----
$ cp <installation_directory>/master.ign 05_control_plane/master.ign
----
`<installation_directory>` specifies the directory where you created the Ignition configuration files.

. Create the control plane deployment by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <control_plane_deployment> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./05_control_plane \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${MASTER_SERVICE_ACCOUNT} \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
`<control_plane_deployment>` specifies the name of the control plane deployment.

. Delete the temporary ignition file from the `05_control_plane` folder by running the following command:
+
[source,terminal]
----
$ rm 05_control_plane/master.ign
----

. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the control plane machines manually.

.. Add the first control plane machine to an internal load balancer instance group by running the following command:
+
[source,terminal]
----
$ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_0}-ig --zone=${ZONE_0} --instances=${INFRA_ID}-master-0
----

.. Add the second control plane machine to an internal load balancer instance group by running the following command:
+
[source,terminal]
----
$ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_1}-ig --zone=${ZONE_1} --instances=${INFRA_ID}-master-1
----

.. Add the third control plane machine to an internal load balancer instance group by running the following command:
+
[source,terminal]
----
$ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_2}-ig --zone=${ZONE_2} --instances=${INFRA_ID}-master-2
----

. For an external cluster, you must also add the control plane machines to external load balancer target pools.

.. Add the first control plane machine to an external load balancer pool by running the following command:
+
[source,terminal]
----
$ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_0}" --instances=${INFRA_ID}-master-0
----

.. Add the second control plane machine to an external load balancer pool by running the following command:
+
[source,terminal]
----
$ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_1}" --instances=${INFRA_ID}-master-1
----

.. Add the third control plane machine to an external load balancer pool by running the following command:
+
[source,terminal]
----
$ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_2}" --instances=${INFRA_ID}-master-2
----

.Verification

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-infrastructure-manager-control-plane_{context}"]
= Infrastructure Manager template for control plane machines

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the control plane machines that you need for your OpenShift Container Platform cluster:

.`05_control_plane.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-creating-gcp-worker_{context}"]
= Creating additional worker machines in {gcp-short}

[role="_abstract"]
You can create worker machines in {gcp-first} for your cluster by using the Infrastructure Manager template. You can adjust the number of machines by modifying the number of `google_compute_instance` resources in the provided template.

[NOTE]
====
If you do not use the provided Infrastructure Manager template to create your compute machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.
====

.Prerequisites

* Ensure you defined the variables in the _Exporting common variables_, _Creating load balancers in {gcp-short}_, and _Creating the bootstrap machine in {gcp-short}_ sections.
* Create the bootstrap machine.
* Create the control plane machines.

.Procedure

. Copy the template from the *Infrastructure Manager template for worker machines* section of this topic and save it as `06_worker.tf` in a folder called `06_worker` on your computer. This template describes the worker machines that your cluster requires.

** You can edit the `06_worker.tf` file to add additional tags to the compute machines, by modifying the existing `tags` stanza as follows:
+
[source,bash]
----
resource "google_compute_instance" "worker_0" {
# ...
  tags = [
    "${var.infra_id}-worker-0",
    "custom-tag-example"
  ]
# ...
}
----

. Copy the `worker.ign` file from your installation directory into the `06_worker` folder by running the following command:
+
[source,terminal]
----
$ cp <installation_directory>/worker.ign 06_worker/worker.ign
----
`<installation_directory>` specifies the directory where you created the Ignition configuration files.

. Create the deployment by running the following command:
+
[source,terminal]
----
$ gcloud infra-manager deployments apply <worker_deployment_name> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./06_worker \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},subnet=${COMPUTE_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${WORKER_SERVICE_ACCOUNT} \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
----
`<worker_deployment_name>` specifies the name of the deployment.

. Remove the `worker.ign` file by running the following command:
+
[source,terminal]
----
$ rm 06_worker/worker.ign
----

.Verification

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-infrastructure-manager-worker_{context}"]
= Infrastructure Manager template for worker machines

[role="_abstract"]
You can use the following Infrastructure Manager template to deploy the worker machines that you need for your OpenShift Container Platform cluster:

.`06_worker.tf` Infrastructure Manager template
[%collapsible]
====
[source,terraform]
----

----
====

// Removing bootstrap resources in GCP
// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-gcp-user-infra-wait-for-bootstrap_{context}"]
= Removing bootstrap resources in {gcp-short}

After you create all of the required infrastructure in {gcp-first}, wait for the bootstrap process to complete on the machines that you provisioned by using the Ignition config files. The installation program created the Ignition config files.

.Prerequisites

* Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in {gcp-short}_ sections.
* Create the bootstrap machine.
* Create the control plane machines.

.Procedure

. Change to the directory that includes the installation program and run the following command:
+
[source,terminal]
----
$ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \ <1>
    --log-level info <2>
----
<1> For `<installation_directory>`, specify the path to the directory where you stored the installation files.
<2> To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.
+
If the command exits without a `FATAL` warning, your production control plane has initialized.

. To remove the bootstrap instance group from the backend services' backends, run the following commands:
+
[source,terminal]
----
$ gcloud compute backend-services remove-backend ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
----
+
[source,terminal]
----
$ ingress_backendservice=$(gcloud compute backend-services list --filter="backends.group~${INFRA_ID}" --format='value(name)' | grep -v "${INFRA_ID}")
----
+
.. If `ingress_backendservice` is not empty, run the following `describe` command for the bootstrap group:
+
[source,terminal]
----
$ gcloud compute backend-services describe ${ingress_backendservice} --region=${REGION}
----
+
.. If the `describe` command displays that the bootstrap group is one of its backends, run the following `remove-backend` command to remove the bootstrap group from the backends:
+
[source,terminal]
----
$ gcloud compute backend-services remove-backend ${ingress_backendservice} --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
----

.. To remove the bucket and the deployment, run the following commands:
+
[source,terminal]
----
$ gcloud storage rm "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign"
----
+
[source,terminal]
----
$ gcloud storage rm --recursive "gs://${INFRA_ID}-bootstrap-ignition/"
----
+
[source,terminal]
----
$ gcloud infra-manager deployments delete <bootstrap_deployment_name> \
    --project=${PROJECT_NAME} --location=${REGION} --quiet
----
Specify the name of the bootstrap deployment you created for `<bootstrap_deployment_name>`.

// Installing the OpenShift CLI on Linux
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-linux_{context}"]
= Installing the OpenShift CLI on Linux

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install the {oc-first} binary on Linux.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.

. Download `oc.tar.gz`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Linux Clients* entry and save the file.
. Navigate to the Download {OCP} page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Linux Clients* entry and save the file.
. Unpack the archive:
+
[source,terminal]
----
$ tar xvf <file>
----

. Place the `oc` binary in a directory that is on your `PATH`.
+
To check your `PATH`, execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* After you install the OpenShift CLI, it is available using the `oc` command:
+
[source,terminal]
----
$ oc <command>
----

// Installing the OpenShift CLI on Windows
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-windows_{context}"]
= Installing the OpenShift CLI on Windows

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install {oc-first} binary on Windows.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.
. Download `oc.zip`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Windows Client* entry and save the file.
. Navigate to the Download {OCP} page on the Red Hat Customer Portal.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Windows Client* entry and save the file.
. Extract the archive with a ZIP program.

. Move the `oc` binary to a directory that is on your `PATH` variable.
+
To check your `PATH` variable, open the command prompt and execute the following command:
+
[source,terminal]
----
C:\> path
----

.Verification

* After you install the OpenShift CLI, it is available using the `oc` command:
+
[source,terminal]
----
C:\> oc <command>
----

// Installing the OpenShift CLI on macOS
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-macos_{context}"]
= Installing the OpenShift CLI on macOS

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install the {oc-first} binary on macOS.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.
. Download `oc.tar.gz`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v macOS Clients* entry and save the file.
+
[NOTE]
====
For macOS arm64, choose the *OpenShift v macOS arm64 Client* entry.
====
. Navigate to the Download {OCP} on the Red{nbsp}Hat Customer Portal.
. Select the appropriate version from the *Version* drop-down list.

. Click *Download Now* next to the *OpenShift v macOS Clients* entry and save the file.

. Unpack and unzip the archive.

. Move the `oc` binary to a directory on your `PATH` variable.
+
To check your `PATH` variable, open a terminal and execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* Verify your installation by using an `oc` command:
+
[source,terminal]
----
$ oc <command>
----

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
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-gcp-user-infra-adding-ingress_{context}"]
= Optional: Adding the ingress DNS records

= Adding the ingress DNS records

If you removed the DNS zone configuration when creating Kubernetes manifests and generating Ignition configs, you must manually create DNS records that point at the ingress load balancer. You can create either a wildcard `*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other records per your requirements.
DNS zone configuration is removed when creating Kubernetes manifests and generating Ignition configs. You must manually create DNS records that point at the ingress load balancer. You can create either a wildcard
`*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other records per your requirements.

.Prerequisites

* Ensure you defined the variables in the _Exporting common variables_ section.
* Remove the DNS Zone configuration when creating Kubernetes manifests and
generating Ignition configs.
* Ensure the bootstrap process completed successfully.

.Procedure

. Wait for the Ingress router to create a load balancer and populate the `EXTERNAL-IP` field:
+
[source,terminal]
----
$ oc -n openshift-ingress get service router-default
----
+
.Example output
[source,terminal]
----
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
router-default   LoadBalancer   172.30.18.154   35.233.157.184   80:32288/TCP,443:31215/TCP   98
----

. Add the A record to your zones:
+
** To use A records:
+
... Export the variable for the router IP address:
+
[source,terminal]
----
$ export ROUTER_IP=`oc -n openshift-ingress get service router-default --no-headers | awk '{print $4}'`
----
+
... Add the A record to the private zones:
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${INFRA_ID}-private-zone
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
----
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
... For an external cluster, also add the A record to the public zones:
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
----
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME} --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${BASE_DOMAIN_ZONE_NAME} --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME} --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
----

** To add explicit domains instead of using a wildcard,
create entries for each of the cluster's current routes:
+
[source,terminal]
----
$ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
----
+
.Example output
[source,terminal]
----
oauth-openshift.apps.your.cluster.domain.example.com
console-openshift-console.apps.your.cluster.domain.example.com
downloads-openshift-console.apps.your.cluster.domain.example.com
alertmanager-main-openshift-monitoring.apps.your.cluster.domain.example.com
prometheus-k8s-openshift-monitoring.apps.your.cluster.domain.example.com
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-user-infra-installation_{context}"]
= Completing a {gcp-short} installation on user-provisioned infrastructure

After you start the OpenShift Container Platform installation on {gcp-first}
user-provisioned infrastructure, you can monitor the cluster events until the
cluster is ready.

.Prerequisites

* Ensure the bootstrap process completed successfully.

.Procedure

. Complete the cluster installation:
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

. Observe the running state of your cluster.
+
.. Run the following command to view the current cluster version and status:
+
[source,terminal]
----
$ oc get clusterversion
----
+
.Example output
[source,terminal]
----
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version             False       True          24m     Working towards 4.5.4: 99% complete
----
+
.. Run the following command to view the Operators managed on the control plane by
the Cluster Version Operator (CVO):
+
[source,terminal]
----
$ oc get clusteroperators
----
+
.Example output
[source,terminal]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             4.5.4     True        False         False      7m56s
cloud-credential                           4.5.4     True        False         False      31m
cluster-autoscaler                         4.5.4     True        False         False      16m
console                                    4.5.4     True        False         False      10m
csi-snapshot-controller                    4.5.4     True        False         False      16m
dns                                        4.5.4     True        False         False      22m
etcd                                       4.5.4     False       False         False      25s
image-registry                             4.5.4     True        False         False      16m
ingress                                    4.5.4     True        False         False      16m
insights                                   4.5.4     True        False         False      17m
kube-apiserver                             4.5.4     True        False         False      19m
kube-controller-manager                    4.5.4     True        False         False      20m
kube-scheduler                             4.5.4     True        False         False      20m
kube-storage-version-migrator              4.5.4     True        False         False      16m
machine-api                                4.5.4     True        False         False      22m
machine-config                             4.5.4     True        False         False      22m
marketplace                                4.5.4     True        False         False      16m
monitoring                                 4.5.4     True        False         False      10m
network                                    4.5.4     True        False         False      23m
node-tuning                                4.5.4     True        False         False      23m
openshift-apiserver                        4.5.4     True        False         False      17m
openshift-controller-manager               4.5.4     True        False         False      15m
openshift-samples                          4.5.4     True        False         False      16m
operator-lifecycle-manager                 4.5.4     True        False         False      22m
operator-lifecycle-manager-catalog         4.5.4     True        False         False      22m
operator-lifecycle-manager-packageserver   4.5.4     True        False         False      18m
service-ca                                 4.5.4     True        False         False      23m
service-catalog-apiserver                  4.5.4     True        False         False      23m
service-catalog-controller-manager         4.5.4     True        False         False      23m
storage                                    4.5.4     True        False         False      17m
----
+
.. Run the following command to view your cluster pods:
+
[source,terminal]
----
$ oc get pods --all-namespaces
----
+
.Example output
[source,terminal]
----
NAMESPACE                                               NAME                                                                READY     STATUS      RESTARTS   AGE
kube-system                                             etcd-member-ip-10-0-3-111.us-east-2.compute.internal                1/1       Running     0          35m
kube-system                                             etcd-member-ip-10-0-3-239.us-east-2.compute.internal                1/1       Running     0          37m
kube-system                                             etcd-member-ip-10-0-3-24.us-east-2.compute.internal                 1/1       Running     0          35m
openshift-apiserver-operator                            openshift-apiserver-operator-6d6674f4f4-h7t2t                       1/1       Running     1          37m
openshift-apiserver                                     apiserver-fm48r                                                     1/1       Running     0          30m
openshift-apiserver                                     apiserver-fxkvv                                                     1/1       Running     0          29m
openshift-apiserver                                     apiserver-q85nm                                                     1/1       Running     0          29m
...
openshift-service-ca-operator                           openshift-service-ca-operator-66ff6dc6cd-9r257                      1/1       Running     0          37m
openshift-service-ca                                    apiservice-cabundle-injector-695b6bcbc-cl5hm                        1/1       Running     0          35m
openshift-service-ca                                    configmap-cabundle-injector-8498544d7-25qn6                         1/1       Running     0          35m
openshift-service-ca                                    service-serving-cert-signer-6445fc9c6-wqdqn                         1/1       Running     0          35m
openshift-service-catalog-apiserver-operator            openshift-service-catalog-apiserver-operator-549f44668b-b5q2w       1/1       Running     0          32m
openshift-service-catalog-controller-manager-operator   openshift-service-catalog-controller-manager-operator-b78cr2lnm     1/1       Running     0          31m
----
+
When the current cluster version is `AVAILABLE`, the installation is complete.

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

* Customize your cluster
* If necessary, you can Remote health reporting
* Configuring Global Access for an Ingress Controller on {gcp-short}
