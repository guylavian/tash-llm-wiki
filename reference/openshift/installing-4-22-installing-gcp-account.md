---
title: "Configuring a {gcp-short} project"
type: reference
domain: openshift
slug: installing-4-22-installing-gcp-account
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-gcp-account
version: 4.22
family: installing
documentKind: "Documentation"
---

# Configuring a {gcp-short} project

[id="installing-gcp-account"]
= Configuring a {gcp-short} project

[role="_abstract"]
Before you can install OpenShift Container Platform, you must configure a {gcp-first} project to host it. You can configure custom roles and permissions, DNS configuration, and manage your own {gcp-short} firewall rules.

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

[role="_additional-resources"]
.Additional resources
* Reducing permissions while using the {gcp-short} CSI Driver Operator

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
// * installing/installing_gcp/installing-gcp-account.adoc

[id="minimum-required-permissions-ipi-gcp_{context}"]
= Required {gcp-short} permissions for installer-provisioned infrastructure

[role="_abstract"]
When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization's security policies require a more restrictive set of permissions, you can create custom roles with the necessary permissions.

The following permissions are required for the installer-provisioned infrastructure for creating and deleting the OpenShift Container Platform cluster.

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
** This permission is not required if you install into an existing VPC and manage your own firewall rules. See the _Managing your own firewall rules_ section.
* `compute.firewalls.delete`
** This permission is not required if you install into an existing VPC and manage your own firewall rules. See the _Managing your own firewall rules_ section.
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
====

.Required permissions for creating Service Account resources
[%collapsible]
====
* `iam.serviceAccountKeys.create`
* `iam.serviceAccountKeys.delete`
* `iam.serviceAccountKeys.get`
* `iam.serviceAccountKeys.list`
* `iam.serviceAccounts.actAs`
** This permission can be limited to act as the control plane and compute service accounts. Alternatively, you may grant the service account that the installation program uses the `iam.serviceAccountUser` role on the control plane and compute service accounts.
* `iam.serviceAccounts.create`
* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.get`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`
** This permission is not required if you use `credentialsMode: Manual` and supply your own service accounts for compute and control plane nodes.
====

.Required permissions for creating compute resources
[%collapsible]
====
* `compute.disks.create`
* `compute.disks.get`
* `compute.disks.list`
* `compute.disks.setLabels`
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
* `iam.roles.create`
* `iam.roles.get`
* `iam.roles.update`
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

.Optional Images permissions for installation
[%collapsible]
====
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
* `compute.images.list`
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc

[id="minimum-required-permissions-ipi-gcp-xpn_{context}"]
= Required {gcp-short} permissions for shared VPC installations

[role="_abstract"]
When you are installing a cluster to a shared VPC, you must configure the service account for both the host project and the service project.

[IMPORTANT]
====
You can use granular permissions for a Cloud Credential Operator (CCO) that operates in either Manual or Mint credentials mode. For more information about the minimum permissions required for a standard installation that is configured with either of these credentials modes, see "Required Google Cloud permissions for installer-provisioned infrastructure".

You cannot use granular permissions in Passthrough credentials mode. For more information about the minimum roles required, see "Required Google Cloud roles".
====

If you are not installing to a shared Virtual Private Cloud (VPC), you can skip the procedure.

[IMPORTANT]
====
When installing a cluster on a shared VPC by using short-lived credentials, you must grant the `compute.subnetworks.use` permission in the host project to Day 2 Operator service accounts.

After using the `ccoctl` utility to generate the {gcp-short} credentials, manually grant this permission to the {cluster-capi-operator} and Machine API Operator service accounts.
====

Ensure that the host project applies one of the following configurations to the service account, noting that the permissions for creating and deleting firewalls are not required if you manage your own firewall rules:

.Required permissions for creating firewalls in the host project
====
* `projects/<host-project>/roles/dns.networks.bindPrivateDNSZone`
* `roles/compute.networkAdmin`
* `roles/compute.securityAdmin`
====

.Required permissions for deleting firewalls in the host project
====
* `compute.firewalls.delete`
* `compute.networks.updatePolicy`
====

.Required minimal permissions
====
* `projects/<host-project>/roles/dns.networks.bindPrivateDNSZone`
* `roles/compute.networkUser`
====

If you do not supply a service account for control plane nodes in the `install-config.yaml` file, grant the following permissions to the service account in the host project. If you do not supply a service account for compute nodes in the `install-config.yaml` file, grant the following permissions to the service account in the host project for cluster destruction. If you do supply service accounts for control plane and compute nodes, you do not need to grant the following permissions.

====
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`
====

The following permissions are required when you select a separate project for the location of the DNS zone or zones. These permissions are also required when the DNS zone or zones are located in a third project.

.Required minimal permissions for provisioning DNS resources in a separate project
====
* `dns.changes.create`
* `dns.changes.get`
* `dns.managedZones.create`
* `dns.managedZones.delete`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.managedZones.update`
* `dns.resourceRecordSets.create`
* `dns.resourceRecordSets.delete`
* `dns.resourceRecordSets.list`
====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc

[id="minimum-required-permissions-ipi-gcp-provided-sas_{context}"]
= Required {gcp-short} permissions for user-provided service accounts

When you are installing a cluster, the compute and control plane nodes require their own service accounts.
By default, the installation program creates a service account for the control plane and compute nodes.
The service account that the installation program uses requires the roles and permissions that are listed in the _Creating a service account in {gcp-short}_ section, as well as the `resourcemanager.projects.getIamPolicy` and `resourcemanager.projects.setIamPolicy` permissions.
These permissions should be applied to the service account in the host project.
If this approach does not meet the security requirements of your organization, you can provide a service account email address for the control plane or compute nodes in the `install-config.yaml` file.
For more information, see the _Installation configuration parameters for {gcp-short}_ page.
If you provide a service account for control plane nodes during an installation into a shared VPC, you must grant that service account the `roles/compute.networkUser` role in the host project.
If you want the installation program to automatically create firewall rules when you supply the control plane service account, you must grant that service account the `roles/compute.networkAdmin` and `roles/compute.securityAdmin` roles in the host project.
If you only supply the `roles/compute.networkUser` role, you must create the firewall rules manually.

[IMPORTANT]
====
The following roles are required for user-provided service accounts for control plane and compute nodes respectively.
====

.Required roles	for control plane nodes
[%collapsible]
====
* `roles/compute.instanceAdmin`
* `roles/compute.networkAdmin`
* `roles/compute.securityAdmin`
* `roles/storage.admin`
====

.Required roles for compute nodes
[%collapsible]
====
* `roles/compute.viewer`
* `roles/storage.admin`
* `roles/artifactregistry.reader`
====

// Module included in the following assembly:
//
// * installing/installing_gcp/installing-gcp-account.adoc

[id="installation-gcp-user-managed-firewall-rules_{context}"]
= Managing your own firewall rules

[role="_abstract"]
You can manage your own firewall rules when installing a cluster on {gcp-short} into an existing VPC by enabling the `firewallRulesManagement` parameter in the `install-config.yaml` file. You can limit the permissions that you grant to the installation program by managing your own firewall rules.

[IMPORTANT]
====
If you manage your own firewall rules, you must continue to manage them through the lifetime of the cluster. If you create a new service, create a new firewall rule that permits traffic on the service port, from the desired source addresses to the compute nodes. An example rule is described in the table below.
====

If you want to manage your own firewall rules, you must create the following rules before installation:

[cols="1,1,1,1"]
|====
|Rule Name |Protocol:Port |Source |Destination

|bootstrap-in-ssh
|`tcp:22`
|`<allowed_external_cidr>`
|`<control_plane_node_tags>`

|api
|`tcp:6443`
|`<allowed_external_cidr>`
|`<control_plane_node_tags>`

|health-checks
|`tcp:6080,6443,22624`
|`35.191.0.0/16`, `130.211.0.0/22`, `209.85.152.0/22`, `209.85.204.0/22`
|`<control_plane_node_tags>`

|etcd
|`tcp:2379,2380`
|`<control_plane_node_tags>`
|`<control_plane_node_tags>`

|control-plane
|`tcp:10257,10259,22623`
|`<control_plane_node_tags>`, `<compute_node_tags>`
|`<control_plane_node_tags>`

|internal-network
|icmp,`tcp:22`
|`<internal_network_cidr>`
|`<control_plane_node_tags>`, `<compute_node_tags>`

|internal-cluster
|`udp:500,4500,4789,6081`, `udp:9000-9999,30000-32767`, `esp`, `tcp:9000-9999,10250`, `tcp:30000-32767`
|`<control_plane_node_tags>`, `<compute_node_tags>`
|`<control_plane_node_tags>`, `<compute_node_tags>`

|ingress-k8s-fw
|`tcp:80,443`
|`<allowed_external_cidr>`
|`<control_plane_node_tags>`, `<compute_node_tags>`

|ingress-k8s-http-hc
|`tcp:30000-32767`
|`35.191.0.0/16`, `130.211.0.0/22`, `209.85.152.0/22`, `209.85.204.0/22`
|`<control_plane_node_tags>`, `<compute_node_tags>`

|`<sample_rule_name>`
|`<service_port>`
|`<allowed_external_cidr>`
|`<compute_node_tags>`
|====
where:

`<allowed_external_cidr>`:: Specifies a network CIDR of the machines that you want to grant access to your cluster. For a public cluster, this would typically be `0.0.0.0/0`. For a private cluster, access might be restricted to the cluster machine network.
`<control_plane_node_tags>`:: Specifies the network tags that apply to the control plane machines in your cluster. These tags must be specified in the `install-config.yaml` file you use to deploy the cluster.
`<compute_node_tags>`:: Specifies the network tags that apply to the compute machines in your cluster. These tags must be specified in the `install-config.yaml` file you use to deploy the cluster.
`<internal_network_cidr>`:: Specifies the network CIDR of the machine network that contains all the machines in your cluster.
`<sample_rule_name>`:: Specifies the name of a custom rule added after installation, for example if you create a new service in your cluster. You can add multiple custom rules as needed.
`<service_port>`:: Specifies the port or port range of the service you created, and the network protocol, such as TCP or UDP. If you create a service using `oc expose`, you can find the service port and protocol by running the command `oc get service <service_name> -o jsonpath='{.spec.ports[0].port}'`, where `<service_name>` is the name of the service you created.

After installation, you can reduce the port range of the `ingress-k8s-http-hc` and `internal-cluster` rules from `tcp:30000-32767` to the individual port that the ingress load balancer service uses, which is not known before installation. You can determine the service port by running the following command after installation:

[source,terminal]
----
$ oc get svc router-default -n openshift-ingress -o jsonpath='{.spec.ports[*].nodePort}'
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-account.adoc

[id="installation-gcp-organization-policies_{context}"]
= Configuring {gcp-short} organization policies and VPC service controls

[role="_abstract"]
OpenShift Container Platform requires that you modify or remove some organization policies and VPC service controls when installing a cluster on {gcp-first}.

If your organization uses the following policies, they must be modified or removed:

* `compute.trustedImageProjects`
* `iam.allowedPolicyMemberDomains`
* `storage.publicAccessPrevention`
* VPC Service Controls egress rules

.Prerequisites

* You created a project to host your cluster.

.Procedure

. Modify the `constraints/compute.trustedImageProjects` constraint in your {gcp-short} project and add `projects/rhcos-cloud` to the `allowedValues` list, as in the following example:
+
[source,yaml]
----
constraint: constraints/compute.trustedImageProjects
listPolicy:
 allowedValues:
    - projects/rhcos-cloud
----
+
Alternatively, you can delete the `constraints/compute.trustedImageProjects` constraint.

. Modify the `iam.managed.allowedPolicyMembers` constraint to allow the service account that the installation program uses to authenticate with {gcp-short} and create storage as in the following example:
+
[source,yaml]
----
name: organizations/<organization_id>/policies/iam.managed.allowedPolicyMembers
spec:
rules:
 - enforce: true
   parameters:
     allowedMemberSubjects:
       - <allowed_member>
----
+
where:
+
`<organization_id>`:: Specifies the numeric ID of your {gcp-short} organization.
`<allowed_member>`:: Specifies the IAM role that you created for the installation program. You can specify a service account in the format of "serviceAccount:example-service-account@example.com" or a user in the format of "user:example-user@example.com".

. Disable the `storage.publicAccessPrevention` constraint so that the installation program can access the cloud storage for your project.

. Create an egress rule that allows access to the {op-system} project, as in the following example:
+
[source,yaml]
----
- egressFrom:
    identityType: ANY_IDENTITY
    identities:
      - "serviceAccount:<installation_program_sa>@<project_id>.iam.gserviceaccount.com"
      - "user:<admin_email>"
  egressTo:
    resources:
      - <project_id>
    operations:
      - serviceName: "compute.googleapis.com"
        methodSelectors: [{method: "*"}]
      - serviceName: "storage.googleapis.com"
        methodSelectors: [{method: "*"}]
      - serviceName: "dns.googleapis.com"
        methodSelectors: [{method: "*"}]
      - serviceName: "iam.googleapis.com"
        methodSelectors: [{method: "*"}]
      - serviceName: "cloudresourcemanager.googleapis.com"
        methodSelectors: [{method: "*"}]
      - serviceName: "serviceusage.googleapis.com"
        methodSelectors: [{method: "*"}]
      - serviceName: "artifactregistry.googleapis.com"
        methodSelectors: [{method: "*"}]
      - serviceName: "deploymentmanager.googleapis.com"
        methodSelectors: [{method: "*"}]
----
+
where:
+
`<installation_program_sa>`:: Specifies the service account that you created for the installation program. This service account will be granted access to the specified resources.
`<project_id>`:: Specifies the project ID of the {gcp-first} project where you are installing the cluster.
`<admin_email>`:: Specifies the email address of an administrator account. You do not need to specify both a service account and an administrator email address. This service account will be granted access to the specified resources.
`<project_id>`:: Specifies one or more projects that the specified identities can access. You can specify a wildcard such as `projects/*` to grant access to all projects, or specific project IDs such as `projects/1234567890`.

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

== Next steps

* Install an OpenShift Container Platform cluster on {gcp-short}. You can
install a customized cluster
or quickly install a cluster
with default options.
