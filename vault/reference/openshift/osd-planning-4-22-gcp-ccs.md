---
title: "Customer Cloud Subscriptions on {gcp-short}"
type: reference
domain: openshift
slug: osd-planning-4-22-gcp-ccs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_planning/gcp-ccs
version: 4.22
family: osd_planning
documentKind: "Documentation"
---

# Customer Cloud Subscriptions on {gcp-short}

[id="gcp-ccs"]
= Customer Cloud Subscriptions on {gcp-short}

[role="_abstract"]
OpenShift Container Platform provides a Customer Cloud Subscription (CCS) model that allows Red Hat to deploy and manage clusters in a customer’s existing {gcp-first} account.

// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc

[id="ccs-gcp-understand_{context}"]
= Understanding Customer Cloud Subscriptions on {gcp-short}

[role="_abstract"]
Red{nbsp}Hat OpenShift Container Platform provides a Customer Cloud Subscription (CCS) model that allows Red{nbsp}Hat to deploy and manage OpenShift Container Platform into a customer's existing {GCP} account. Red{nbsp}Hat requires several prerequisites be met in order to provide this service.

OpenShift Container Platform cluster prerequisite integration is available within the {GCP} console. This integration allows {GCP} users to discover and validate cluster prerequisites directly from the {GCP} interface. The prerequisites validation ensures your environment is ready before you transition to the {hybrid-console} for cluster creation.

Red{nbsp}Hat recommends the usage of a {gcp-short} project, managed by the customer, to organize all of your {gcp-short} resources. A project consists of a set of users and APIs, as well as billing, authentication, and monitoring settings for those APIs.

It is recommended for the OpenShift Container Platform cluster using a CCS model to be hosted in a {gcp-short} project within a {gcp-short} organization. The organization resource is the root node of the {gcp-short} resource hierarchy and all resources that belong to an organization are grouped under the organization node. Customers have the choice of using service account keys or Workload Identity Federation (WIF) when creating the roles and credentials necessary to access {gcp-full} resources within a {gcp-short} project.

Red{nbsp}Hat and {gcp-short} recommend using WIF as the authentication type as it provides enhanced security through the use of short-lived credentials, whereas service account authentication uses long-lived credentials which are less secure.

For more information about creating and managing organization resources within {gcp-short}, see Creating and managing organization resources.
// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc

[id="ccs-gcp-customer-requirements_{context}"]
= Customer requirements

[role="_abstract"]
OpenShift Container Platform clusters using a Customer Cloud Subscription (CCS) model on {gcp-first} must meet several prerequisites before they can be deployed.

As a {gcp-short} user, you can validate many of these requirements directly within the {gcp-short} console before deployment.

[id="ccs-gcp-requirements-account_{context}"]
== Account

* The customer ensures that {gcp-full} limits and allocation quotas that apply to Compute Engine are sufficient to support OpenShift Container Platform provisioned within the customer-provided {gcp-short} account.

* The customer-provided {gcp-short} account should be in the customer's {gcp-full} Organization.

* The customer-provided {gcp-short} account must not be transferable to Red{nbsp}Hat.

* The customer may not impose {gcp-short} usage restrictions on Red{nbsp}Hat activities. Imposing restrictions severely hinders Red{nbsp}Hat's ability to respond to incidents.

* Red{nbsp}Hat deploys monitoring into {gcp-short} to alert Red{nbsp}Hat when a highly privileged account, such as a root account, logs into the customer-provided {gcp-short} account.

* The customer can deploy native {gcp-short} services within the same customer-provided {gcp-short} account.
+
[NOTE]
====
Customers are encouraged, but not mandated, to deploy resources in a Virtual Private Cloud (VPC) separate from the VPC hosting OpenShift Container Platform and other Red{nbsp}Hat supported services.
====

[id="ccs-gcp-requirements-access_{context}"]
== Access requirements

* To appropriately manage the OpenShift Container Platform service, Red{nbsp}Hat must have the `AdministratorAccess` policy applied to the administrator role at all times.
+
[NOTE]
====
This policy only provides Red{nbsp}Hat with permissions and capabilities to change resources in the customer-provided {gcp-short} account.
====

* Red{nbsp}Hat must have {gcp-short} console access to the customer-provided {gcp-short} account. This access is protected and managed by Red{nbsp}Hat.

* The customer must not utilize the {gcp-short} account to elevate their permissions within the OpenShift Container Platform cluster.

* Actions available in the {cluster-manager-url} must not be directly performed in the customer-provided {gcp-short} account.

[id="ccs-gcp-requirements-support_{context}"]
== Support requirements

* Red{nbsp}Hat recommends that the customer have at least Enhanced Support from {gcp-short}.

* Red{nbsp}Hat has authority from the customer to request {gcp-short} support on their behalf.

* Red{nbsp}Hat has authority from the customer to request {gcp-short} resource limit increases on the customer-provided account.

* Red{nbsp}Hat manages the restrictions, limitations, expectations, and defaults for all OpenShift Container Platform clusters in the same manner, unless otherwise specified in this requirements section.

[id="ccs-gcp-requirements-security_{context}"]
== Security requirements

* The customer-provided IAM credentials must be unique to the customer-provided {gcp-short} account and must not be stored anywhere in the customer-provided {gcp-short} account.

* Volume snapshots will remain within the customer-provided {gcp-short} account and customer-specified region.

* To manage, monitor, and troubleshoot OpenShift Container Platform clusters, Red{nbsp}Hat must have direct access to the cluster's API server. You must not restrict or otherwise prevent Red{nbsp}Hat's access to the OpenShift Container Platform cluster's API server.
+
[NOTE]
====
SRE uses various methods to access clusters, depending on network configuration. Access to private clusters is restricted to Red{nbsp}Hat trusted IP addresses only. These access restrictions are managed automatically by Red{nbsp}Hat.
====
+
* OpenShift Container Platform requires egress access to certain endpoints over the internet. Only clusters deployed with Private Service Connect can use a firewall to control egress traffic. For additional information, see the _{gcp-short} firewall prerequisites_ section.
// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc
[id="ccs-gcp-customer-procedure_{context}"]

= Required customer procedure

[role="_abstract"]
The Customer Cloud Subscription (CCS) model allows Red{nbsp}Hat to deploy and manage OpenShift Container Platform into a customer's {gcp-first} project. Red{nbsp}Hat requires several prerequisites to be completed before providing these services.
[NOTE]
====
The following requirements in this topic apply to OpenShift Container Platform on {GCP} clusters created using both the Workload Identity Federation (WIF) and service account authentication types.
Red{nbsp}Hat recommends using WIF as the authentication type for installing and interacting with an OpenShift Container Platform cluster deployed on {gcp-short} because WIF provides enhanced security.

For information about creating a cluster using the WIF authentication type, see _Additional resources_.

For additional requirements that apply to the WIF authentication type only, see _Workload Identity Federation authentication type procedure_.
For additional requirements that apply to the service account authentication type only, see _Service account authentication type procedure_.
====

.Prerequisites

Before using OpenShift Container Platform in your {gcp-short} project, confirm that the following organizational policy constraints are configured correctly where applicable:

* `constraints/iam.allowedPolicyMemberDomains`
** This policy constraint is supported only if Red{nbsp}Hat's Directory Customer ID's `C02k0l5e8` and `C04j7mbwl` are included in the allowlist.
* `constraints/compute.restrictLoadBalancerCreationForTypes`
** This organization policy constraint restricts the types of {GCP} load balancer types that can be created within a project. Certain load balancer types are required depending on the type of OpenShift Container Platform cluster you are creating.
*** For private Workload Identity Federation (WIF)-enabled OpenShift Container Platform clusters with {gcp-short} Private Service Connect (PSC), you must ensure the `INTERNAL_TCP_UDP` load balancer type is included in your organization's allowlist or excluded from the denylist.
*** For public WIF-enabled OpenShift Container Platform clusters, you must ensure the `INTERNAL_TCP_UDP`, `EXTERNAL_TCP_PROXY`, and `EXTERNAL_NETWORK_TCP_UDP` load balancer types are permitted in your organization's allowlist or excluded from the denylist.
+
[IMPORTANT]
====
Although the `EXTERNAL_NETWORK_TCP_UDP` load balancer type is not required when creating a private cluster with PSC, disallowing it with this constraint will prevent the cluster from being able to create externally accessible load balancers.
====

* `constraints/compute.requireShieldedVm`
** This policy constraint is supported only if the cluster is created with *Enable Secure Boot support for Shielded VMs* selected during the initial cluster creation.
* `constraints/compute.vmExternalIpAccess`
** This policy constraint is supported only when creating a private cluster with {gcp-short} Private Service Connect (PSC). For all other cluster types, this policy constraint is supported only after cluster creation.
* `constraints/compute.trustedImageProjects`
** This policy constraint is supported only when the projects `redhat-marketplace-public`, `rhel-cloud`, and `rhcos-cloud` are included in the allowlist. If this policy constraint is enabled and these projects are not included in the allowlist, cluster creation will fail.

For more information about configuring {gcp-short} organization policy constraints, see Organization policy constraints.

.Procedure

. Create a {gcp-full} project to host the OpenShift Container Platform cluster.

. Enable the following required APIs in the project that hosts your OpenShift Container Platform cluster:
+
.Required API services
[cols="2a,3a,3a",options="header"]

|===

|API service |Console service name |Purpose

|Cloud Deployment Manager V2 API
|`deploymentmanager.googleapis.com`
|Used for automated deployment and management of infrastructure resources.

|Compute Engine API
|`compute.googleapis.com`
|Used for creating and managing virtual machines, firewalls, networks, persistent disk volumes, and load balancers.

|Google Cloud APIs
|`cloudapis.googleapis.com`
|Used for managing Google Cloud services and resources.

|Cloud Resource Manager API
|`cloudresourcemanager.googleapis.com`
|Used for getting projects, getting or setting an IAM policy for projects, validating required permissions, and tagging.

|Cloud DNS API
|`dns.googleapis.com`
|Used for creating DNS zones and managing DNS records for the cluster domains.

|Network Security API
|`networksecurity.googleapis.com`
|Used for creating, managing, and enforcing network security policies for your applications and resources within Google Cloud.

|IAM Service Account Credentials API
|`iamcredentials.googleapis.com`
|Used for creating short-lived credentials for impersonating IAM service accounts.

|Identity and Access Management (IAM) API
|`iam.googleapis.com`
|Used for managing the IAM configuration for the cluster.

|Service Management API
|`servicemanagement.googleapis.com`
|Used indirectly to fetch quota information for {gcp-short} resources.

|Service Usage API
|`serviceusage.googleapis.com`
|Used for determining what services are available in the customer’s {gcp-full} account.

|Cloud Storage JSON API
|`storage-api.googleapis.com`
|Used for accessing Cloud Storage for the image registry, ignition, and cluster backups (if applicable).

|Cloud Storage
|`storage-component.googleapis.com`
|Used for managing Cloud Storage for the image registry, ignition, and cluster backups (if applicable).

|Organization Policy API
|`orgpolicy.googleapis.com`
|Used to identify governance rules applied to customer’s {gcp-full} that might impact cluster creation or management.

|Cloud Commerce Consumer Procurement API
|`cloudcommerceconsumerprocurement.googleapis.com`
|Enables users to procure products from the {gcp-short}  Marketplace. Specifically, it is required to validate that customers have accepted the Marketplace terms and conditions for OpenShift Container Platform.

This API is required when transacting through the {gcp-short} Marketplace.

|Cloud Identity-Aware Proxy API
|`iap.googleapis.com`
|Used in emergency situations to troubleshoot cluster nodes that are otherwise inaccessible.

This API is required for clusters deployed with Private Service Connect.

|===
// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc
[id="ccs-gcp-permissions-marketplace-billing_{context}"]

= Roles required for {GCP} Marketplace billing

[role="_abstract"]
To deploy an OpenShift Container Platform cluster using {GCP} Marketplace-based billing, your {GCP} account must first be prepared. This involves accepting the {GCP} Marketplace terms and agreements for the OpenShift Dedicated product listing. Contact your {GCP} administrator who has the `Consumer Procurement Entitlement Manager` role to enable OpenShift Container Platform cluster deployments in your {GCP} project.

To automate the checking and acceptance of these terms and agreements during OpenShift Dedicated cluster creation, you must grant the `Consumer Procurement Entitlement Viewer` role to the {GCP} identity (user or service account) that is creating the cluster. The `Consumer Procurement Entitlement Viewer` role includes the necessary permissions to check for existing consent to the {GCP} terms and agreements.

The following table lists the permissions that are included in the `Consumer Procurement Entitlement Viewer` role.

.Required permissions in the Consumer Procurement Entitlement Viewer role
[cols="2a,3a,3a",options="header"]
|===

|Role and description|Console role name|Permissions

|Consumer Procurement Entitlement Viewer

Allows for the inspecting of entitlements and service states for a consumer project.
|`consumerprocurement.entitlementViewer`
|commerceoffercatalog.offers.get
consumerprocurement.consents.check
consumerprocurement.consents.list
consumerprocurement.entitlements.get
consumerprocurement.entitlements.list
consumerprocurement.freeTrials.get
consumerprocurement.freeTrials.list
orgpolicy.policy.get
resourcemanager.projects.get
resourcemanager.projects.list
serviceusage.consumerpolicy.analyze
serviceusage.consumerpolicy.get
serviceusage.effectivepolicy.get
serviceusage.groups.list
serviceusage.groups.listExpandedMembers
serviceusage.groups.listMembers
serviceusage.services.get
serviceusage.services.list
serviceusage.values.test

|===

For more information about {GCP} Marketplace roles and permissions, see Access control with IAM in the {GCP} documentation.

// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc
[id="ccs-gcp-customer-procedure-wif_{context}"]

= Workload Identity Federation authentication type procedure
// TODO: Same as other module - Better procedure heading that tells you what this is doing

[role="_abstract"]
Besides the required customer procedures listed in _Required customer procedure_, there are other specific actions that you must take when creating an OpenShift Container Platform cluster on {GCP} using Workload Identity Federation (WIF) as the authentication type.

.Procedure

. Assign the following roles to the service account of the user implementing the WIF authentication type:
+
[IMPORTANT]
====
The following roles are only required when creating, updating, or deleting WIF configurations.
====
+
.Required roles
[cols="5a,3a,5a",options="header"]
|===

|Role and description|Console role name|Permissions

|Role Admin

Required by the {gcp-short} client in the OCM CLI for creating custom role.

|`roles/iam.roleAdmin`

|iam.roles.create

iam.roles.delete

iam.roles.get

iam.roles.list

iam.roles.undelete

iam.roles.update

resourcemanager.projects.get
resourcemanager.projects.getIamPolicy

|Service Account Admin

Required for the pre-creation of the service accounts used by the deployer, support, and Operators.
|`roles/iam.serviceAccountAdmin`

a| iam.serviceAccountApiKeyBindings.create
iam.serviceAccountApiKeyBindings.delete
iam.serviceAccountApiKeyBindings.undelete
iam.serviceAccounts.create
iam.serviceAccounts.create
iam.serviceAccounts.create
iam.serviceAccounts.createTagBinding
iam.serviceAccounts.delete
iam.serviceAccounts.deleteTagBinding
iam.serviceAccounts.disable
iam.serviceAccounts.enable
iam.serviceAccounts.get
iam.serviceAccounts.getIamPolicy
iam.serviceAccounts.list
iam.serviceAccounts.listEffectiveTags
iam.serviceAccounts.listTagBindings
iam.serviceAccounts.setIamPolicy
iam.serviceAccounts.undelete
iam.serviceAccounts.update
resourcemanager.projects.get
resourcemanager.projects.list

|Workload Identity Pool Admin

Required to create and configure the workload identity pool.
|`roles/iam.workloadIdentityPoolAdmin`

a| iam.googleapis.com/workloadIdentityPoolProviderKeys.create
iam.googleapis.com/workloadIdentityPoolProviderKeys.delete
iam.googleapis.com/workloadIdentityPoolProviderKeys.get
iam.googleapis.com/workloadIdentityPoolProviderKeys.list
iam.googleapis.com/workloadIdentityPoolProviderKeys.undelete
iam.googleapis.com/workloadIdentityPoolProviders.create
iam.googleapis.com/workloadIdentityPoolProviders.delete
iam.googleapis.com/workloadIdentityPoolProviders.get
iam.googleapis.com/workloadIdentityPoolProviders.list
iam.googleapis.com/workloadIdentityPoolProviders.undelete
iam.googleapis.com/workloadIdentityPoolProviders.up
iam.googleapis.com/workloadIdentityPools.delete
iam.googleapis.com/workloadIdentityPools.get
iam.googleapis.com/workloadIdentityPools.list
iam.googleapis.com/workloadIdentityPools.undelete
iam.googleapis.com/workloadIdentityPools.update
iam.workloadIdentityPools.createPolicyBinding
iam.workloadIdentityPools.deletePolicyBinding
iam.workloadIdentityPools.searchPolicyBindings
iam.workloadIdentityPools.updatePolicyBinding
resourcemanager.projects.get
resourcemanager.projects.list

|Project IAM Admin

Required for assigning roles to the service account and giving permissions to those roles that are necessary to perform operations on cloud resources.
|`roles/resourcemanager.projectIamAdmin`

a|iam.policybindings.get
iam.policybindings.list
resourcemanager.projects.createPolicyBinding
resourcemanager.projects.deletePolicyBinding
resourcemanager.projects.get
resourcemanager.projects.getIamPolicy
resourcemanager.projects.searchPolicyBindings
resourcemanager.projects.setIamPolicy
resourcemanager.projects.updatePolicyBinding

|===

. Install the OpenShift Cluster Manager API command-line interface (`ocm`).
+

[IMPORTANT]
====
The {cluster-manager} API command-line interface (`ocm`) is a Developer Preview feature only.
For more information about the support scope of Red Hat Developer Preview features, see Developer Preview Support Scope.
====
+
// To use the OCM CLI, you must authenticate against your Red Hat {cluster-manager} account. This is accomplished with the {cluster-manager} API token.
// +
// You can obtain your token here.

. To authenticate against your Red Hat {cluster-manager} account, run one of the following commands.

.. If your system supports a web-based browser, run the Red{nbsp}Hat single sign-on (SSO) authorization code command for secure authentication:
+
[source,terminal]
----
$ ocm login --use-auth-code
----
+
Running this command will redirect you to the Red Hat SSO login. Log in with your Red{nbsp}Hat login or email.
+
.. If you are working with containers, remote hosts, and other environments without a web browser, run the Red{nbsp}Hat single sign-on (SSO) device code command for secure authentication:

+
.Syntax
[source,terminal]
----
$ ocm login --use-device-code
----
Running this command will redirect you to the Red{nbsp}Hat SSO login and provide a log in code.

+

To switch accounts, logout from https://sso.redhat.com and run the `ocm logout` command in your terminal before attempting to login again.

+

. Install the gcloud CLI.
+
.  Authenticate the gcloud CLI with the Application Default Credentials (ADC).
// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc
[id="ccs-gcp-customer-procedure-sa_{context}"]

= Service account authentication type procedure
// TODO: Same as other module - Better procedure heading that tells you what this is doing

[role="_abstract"]
Besides the required customer procedures listed in _Required customer procedure_, there are other specific actions that you must take when creating an OpenShift Container Platform cluster on {GCP} using a service account as the authentication type.

.Procedure

. To ensure that Red Hat can perform necessary actions, you must create an `osd-ccs-admin` IAM service account user within the {gcp-short} project.

+

The following roles must be granted to the service account:
+
.Required roles
[cols="2a,3a",options="header"]

|===

|Role|Console role name

|Compute Admin
|`roles/compute.admin`

|DNS Administrator
|`roles/dns.admin`

|Organization Policy Viewer
|`roles/orgpolicy.policyViewer`

|Service Management Administrator
|`roles/servicemanagement.admin`

|Service Usage Admin
|`roles/serviceusage.serviceUsageAdmin`

|Storage Admin
|`roles/storage.admin`

|Compute Load Balancer Admin
|`roles/compute.loadBalancerAdmin`

|Role Viewer
|`roles/viewer`

|Role Administrator
|`roles/iam.roleAdmin`

|Security Admin
|`roles/iam.securityAdmin`

|Service Account Key Admin
|`roles/iam.serviceAccountKeyAdmin`

|Service Account Admin
|`roles/iam.serviceAccountAdmin`

|Service Account User
|`roles/iam.serviceAccountUser`

|===

+

. Create the service account key for the `osd-ccs-admin` IAM service account. Export the key to a file named `osServiceAccount.json`; this JSON file will be uploaded in {cluster-manager-first} when you create your cluster.

// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc

[id="ocm-cli-create-managed-dns-zone_{context}"]
= Creating a managed DNS zone

[role="_abstract"]
Instead of granting OpenShift Container Platform broad administrative control over your host projects, you can create your own managed DNS zones and provide OpenShift Container Platform with strictly limited, scoped permissions before cluster creation. This allows you to maintain rigorous security compliance and adhere to the principle of least privilege, ensuring that OpenShift Container Platform has exactly what it needs to run without risk to your other critical cloud workloads.

Use the {cluster-manager} CLI (`ocm`) to create a managed DNS zone associated with your account.

.Prerequisites

* You have downloaded version `v1.0.12` or later of the {cluster-manager} CLI (`ocm`) for your operating system from the Downloads page on {cluster-manager}.
* You have the required permissions to create a DNS zone in your {GCP} account.
* You have identified the {GCP} project and network where your OpenShift Container Platform cluster will be deployed, as you will need to associate the DNS zone with this information during creation.
* You have created a Workload Identity Federation (WIF) configuration to use WIF for cluster authentication. For more information, see _Creating a Workload Identity Federation configuration_.

.Procedure

* To create a managed DNS zone, run the following command:
+
[source,terminal]
----
$ ocm gcp create dns-zone --domain-prefix=<prefix> --project-id=<project_id> --network-id=<network_id> --network-project-id=<network_project_id>
----
+
where:

`--domain-prefix`:: Optional. Specifies a domain prefix for the DNS zone. If the OpenShift Container Platform cluster name is longer than 15 characters, the domain prefix is used to ensure the generated domain name does not exceed DNS length limits.

`--project-id`:: Specifies the ID of the {GCP} project where the DNS zone will be created.

`--network-id`:: Specifies the network associated with the DNS zone. This is typically the network where your OpenShift Container Platform cluster is deployed.
Note the DNS zone ID returned in the output. You will need this ID when creating your cluster.

`--network-project-id`:: Optional. Specifies the ID of the {GCP} project where the VPC network is located if it is different from the project where the DNS zone is being created. If not specified, it is assumed to be the same as the project where the DNS zone is being created.

.Verification

* To verify that the DNS zone was created successfully, run the following command:
+
[source,terminal]
----
$ ocm gcp list dns-zones
----

// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="ocm-cli-manage-dns-zones_{context}"]
= Managing DNS zones

[role="_abstract"]
Managing your domain infrastructure is a key part of maintaining a healthy cluster environment. With the {cluster-manager} CLI (`ocm`), you can easily view and manage your existing managed DNS zones associated with your account. This allows you to keep track of your DNS configurations, make necessary updates, and ensure that your cluster's network settings are always up to date and secure.

.Procedure

* Use the following commands to view and manage existing managed DNS zones associated with your account.
** To list all the managed DNS zones, run the following command:
+
[source,terminal]
----
$ ocm gcp list dns-zones
----
** To view details about a specific managed DNS zone, run the following command, replacing `<dns_zone_id>` with the ID of the DNS zone you want to view:
+
[source,terminal]
----
$ ocm gcp describe dns-zone <dns_zone_id>
----
+
** To delete a managed DNS zone, run the following command, replacing `<dns_zone_id>` with the ID of the DNS zone you want to delete:
+
[source,terminal]
----
$ ocm gcp delete dns-zone <dns_zone_id>
----
+
[NOTE]
====
You cannot delete a managed DNS zone that is currently attached to an active OpenShift Container Platform cluster.
====

// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc
[id="ccs-gcp-iam_{context}"]

= Red Hat managed {gcp-full} resources

[role="_abstract"]
Red Hat is responsible for creating and managing the following IAM {gcp-first} resources.

[IMPORTANT]
=====
The _IAM service account and roles_ and _IAM group and roles_ topics are only applicable to clusters created using the service account authentication type.
=====

[id="ccs-gcp-iam-service-account-roles_{context}"]
== IAM service account and roles

The `osd-managed-admin` IAM service account is created immediately after taking control of the customer-provided {gcp-short} account. This is the user that will perform the OpenShift Container Platform cluster installation.

The following roles are attached to the service account:

.IAM roles for osd-managed-admin
[cols="2a,3a,2a",options="header"]

|===

|Role |Console role name |Description

|Compute Admin
|`roles/compute.admin`
|Provides full control of all Compute Engine resources.

|DNS Administrator
|`roles/dns.admin`
|Provides read-write access to all Cloud DNS resources.

|Security Admin
|`roles/iam.securityAdmin`
|Security admin role, with permissions to get and set any IAM policy.

|Storage Admin
|`roles/storage.admin`
|Grants full control of objects and buckets.

When applied to an individual *bucket*, control applies only to the specified bucket and objects within the bucket.

|Service Account Admin
|`roles/iam.serviceAccountAdmin`
|Create and manage service accounts.

|Service Account Key Admin
|`roles/iam.serviceAccountKeyAdmin`
|Create and manage (and rotate) service account keys.

|Service Account User
|`roles/iam.serviceAccountUser`
|Run operations as the service account.

|Role Administrator
|`roles/iam.roleAdmin`
|Provides access to all custom roles in the project.

|===

[id="ccs-gcp-iam-group-roles_{context}"]
== IAM group and roles

The `sd-sre-platform-gcp-access` Google group is granted access to the {gcp-short} project to allow Red Hat Site Reliability Engineering (SRE) access to the console for emergency troubleshooting purposes.

[NOTE]
====
* For information regarding the roles within the `sd-sre-platform-gcp-access`  group that are specific to clusters created when using the Workload Identity Federation (WIF) authentication type, see managed-cluster-config.
* For information about creating a cluster using the Workload Identity Federation authentication type, see _Additional resources_.
====
The following roles are attached to the group:

.IAM roles for sd-sre-platform-gcp-access
[cols="2a,3a,2a",options="header"]

|===

|Role |Console role name |Description

|Compute Admin
|`roles/compute.admin`
|Provides full control of all Compute Engine resources.

|Editor
|`roles/editor`
|Provides all viewer permissions, plus permissions for actions that modify state.

|Organization Policy Viewer
|`roles/orgpolicy.policyViewer`
|Provides access to view Organization Policies on resources.

|Project IAM Admin
|`roles/resourcemanager.projectIamAdmin`
|Provides permissions to administer IAM policies on projects.

|Quota Administrator
|`roles/servicemanagement.quotaAdmin`
|Provides access to administer service quotas.

|Role Administrator
|`roles/iam.roleAdmin`
|Provides access to all custom roles in the project.

|Service Account Admin
|`roles/iam.serviceAccountAdmin`
|Create and manage service accounts.

|Service Usage Admin
|`roles/serviceusage.serviceUsageAdmin`
|Ability to enable, disable, and inspect service states, inspect operations, and consume quota and billing for a consumer project.

|Tech Support Editor
|`roles/cloudsupport.techSupportEditor`
|Provides full read-write access to technical support cases.

|===
// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc

[id="ccs-gcp-provisioned_{context}"]
= Provisioned {gcp-short} Infrastructure

[role="_abstract"]
This is an overview of the provisioned {gcp-first} components on a deployed OpenShift Container Platform cluster. For a more detailed listing of all provisioned {gcp-short} components, see the {OCP} documentation.

[id="gcp-policy-instances_{context}"]
== Compute instances

{gcp-short} compute instances are required to deploy the control plane and data plane functions of OpenShift Container Platform in {gcp-short}. Instance types might vary for control plane and infrastructure nodes depending on worker node count.

* Single availability zone
** 2 infra nodes  (n2-highmem-4 machine type: 4 vCPU and 32 GB RAM)
** 3 control plane nodes  (n2-standard-8 machine type: 8 vCPU and 32 GB RAM)
** 2 worker nodes (default n2-standard-4 machine type: 4 vCPU and 16 GB RAM)
* Multiple availability zones
** 3 infra nodes  (n2-highmem-4 machine type: 4 vCPU and 32 GB RAM)
** 3 control plane nodes (n2-standard-8 machine type: 8 vCPU and 32 GB RAM)
** 3 worker nodes (default n2-standard-4 machine type: 4 vCPU and 16 GB RAM)

[id="gcp-policy-storage_{context}"]
== Storage

* Infrastructure volumes:
** 300 GB SSD persistent disk (deleted on instance deletion)
** 110 GB  Standard persistent disk (kept on instance deletion)
* Worker volumes:
** 300 GB SSD persistent disk  (deleted on instance deletion)
* Control plane volumes:
** 350 GB SSD persistent disk  (deleted on instance deletion)

[id="gcp-policy-vpc_{context}"]
== Installing a new cluster into an existing VPC

You must have at least one VPC network within the {GCP} project where the OpenShift Container Platform cluster is being installed. The VPC network must include the following subnets within the same region as the cluster:

* A control plane subnet for the OpenShift control plane.
* A compute subnet for user workloads.
* A Private Service Connect (PSC) subnet when a private cluster is deployed using PSC.

[NOTE]
====
Installing a new OpenShift Container Platform cluster into a VPC that was automatically created by the installer for a different cluster is not supported.

IPv6 and dual-stack (IPv4 and IPv6) address ranges are not supported within the OpenShift Container Platform cluster.
====

[id="gcp-policy-services_{context}"]
== Services

For a list of services that must be enabled on a {gcp-short} CCS cluster, see the _Required API services_ table.
// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc

[id="gcp-limits_{context}"]
= {gcp-short} account limits

The OpenShift Container Platform cluster uses a number of {gcp-first} components, but the default quotas do not affect your ability to install an OpenShift Container Platform cluster.

A standard OpenShift Container Platform cluster uses the following resources. Note that some resources are required only during the bootstrap process and are removed after the cluster deploys.

[NOTE]
====
3 subnets are required to deploy a private cluster with Private Service Connect (PSC). These subnets are a control plane subnet, a worker subnet, and a subnet used for the PSC service attachment with the purpose set to Private Service Connect.

48 vCPUs for a default multi-AZ OpenShift Container Platform cluster consists of 3 compute nodes (4 vCPUs each, one per availability zone), 3 infra nodes (4 vCPU each), and 3 control plane nodes (8 vCPU each).

40 vCPUs for a default single-AZ OpenShift Container Platform cluster consists of 2 compute nodes (4 vCPUs each), 2 infra nodes (4 vCPU each) and 3 control plane nodes (8 vCPU each).
====

.{gcp-short} resources used in a default cluster

[cols="2a,2a,2a,2a,2a",options="header"]
|===
|Service
|Component
|Location
|Total resources required
|Resources removed after bootstrap

|Service account |IAM	|Global	|10 |0
|Firewall Rules	|Compute	|Global	|11 |1
|Forwarding Rules	|Compute	|Global	|2	|0
|In-use global IP addresses	|Compute	|Global	|4	|1
|Health checks	|Compute	|Global	|3	|0
|Images	|Compute	|Global	|1	|0
|Networks	|Compute	|Global	|2	|0
|Static IP addresses	|Compute	|Region	|4	|1
|Routers	|Compute	|Global	|1	|0
|Routes	|Compute	|Global	|2	|0
|Subnetworks	|Compute	|Global	|3	|0
|Target Pools	|Compute	|Global	|3	|0
|CPUs	|Compute	|Region	|48	|4
|Persistent Disk SSD (GB)	|Compute	|Region	|1060	|128

|===

[NOTE]
====
If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region.
====

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, Static IP addresses, and Persistent Disk SSD (Storage) quotas are the ones that are most likely to be insufficient.

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit:

* asia-east2
* asia-northeast2
* asia-south1
* australia-southeast1
* europe-north1
* europe-west2
* europe-west3
* europe-west6
* northamerica-northeast1
* southamerica-east1
* us-west2

You can increase resource quotas from the {gcp-short} console, but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster.
// Module included in the following assemblies:
//
// * osd_planning/gcp-ccs.adoc

[id="osd-gcp-psc-firewall-prerequisites_{context}"]
= {gcp-short} firewall prerequisites

If you are using a firewall to control egress traffic from OpenShift Container Platform on {GCP}, you must configure your firewall to grant access to certain domains and port combinations listed in the tables below. OpenShift Container Platform requires this access to provide a fully managed OpenShift service.

// .Prerequisites
// Per SMEs, no prereqs. Will confirm with QE when ticket is reviewed.

.Procedure

. Add the following URLs that are used to install and download packages and tools to an allowlist:
+
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function
|`registry.redhat.io`
|443
|Provides core container images.

|`quay.io`
|443
|Provides core container images.

|`cdn01.quay.io`

 `cdn02.quay.io`

 `cdn03.quay.io`

 `cdn04.quay.io`

 `cdn05.quay.io`

 `cdn06.quay.io`

|443
|Provides core container images.

|`sso.redhat.com`
|443
|Required. The https://console.redhat.com/openshift site uses authentication from sso.redhat.com to download the pull secret and use Red Hat SaaS solutions to facilitate monitoring of your subscriptions, cluster inventory, chargeback reporting, and so on.

|`quayio-production-s3.s3.amazonaws.com`
|443
|Provides core container images.

|`pull.q1w2.quay.rhcloud.com`
|443
|Provides core container images.

|`registry.access.redhat.com`
|443
|Hosts all the container images that are stored on the Red{nbsp}Hat Ecosytem Catalog. Additionally, the registry provides access to the `odo` CLI tool that helps developers build on OpenShift and Kubernetes.

|`registry.connect.redhat.com`
|443
|Required for all third-party images and certified Operators.

|`console.redhat.com`
|443
|Required. Allows interactions between the cluster and {cluster-manager-first} to enable functionality, such as scheduling upgrades.

|`catalog.redhat.com`
|443
|The `registry.access.redhat.com` and `https://registry.redhat.io` sites redirect through `catalog.redhat.com`.
|===
+
. Add the following telemetry URLs to an allowlist:
+
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`cert-api.access.redhat.com`
|443
|Required for telemetry.

|`api.access.redhat.com`
|443
|Required for telemetry.

|`infogw.api.openshift.com`
|443
|Required for telemetry.

|`console.redhat.com`
|443
|Required for telemetry and {red-hat-lightspeed}.

|`observatorium-mst.api.openshift.com`
|443
|Required for managed OpenShift-specific telemetry.

|`observatorium.api.openshift.com`
|443
|Required for managed OpenShift-specific telemetry.
|===
+

[NOTE]
====
Managed clusters require the enabling of telemetry to allow Red Hat to react more quickly to problems, better support the customers, and better understand how product upgrades impact clusters. For more information about how remote health monitoring data is used by Red Hat, see _About remote health monitoring_ in the _Additional resources_ section.
====

. Add the following OpenShift Container Platform URLs to an allowlist:
+
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`mirror.openshift.com`
|443
|Used to access mirrored installation content and images. This site is also a source of release image signatures.

|`api.openshift.com`
|443
|Used to check if updates are available for the cluster.
|===

. Add the following site reliability engineering (SRE) and management URLs to an allowlist:
+
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

|`api.pagerduty.com`
|443
|This alerting service is used by the in-cluster alertmanager to send alerts notifying Red{nbsp}Hat SRE of an event to take action on.

|`events.pagerduty.com`
|443
|This alerting service is used by the in-cluster alertmanager to send alerts notifying Red{nbsp}Hat SRE of an event to take action on.

|`api.deadmanssnitch.com`
|443
|Alerting service used by OpenShift Container Platform to send periodic pings that indicate whether the cluster is available and running.

|`nosnch.in`
|443
|Alerting service used by OpenShift Container Platform to send periodic pings that indicate whether the cluster is available and running.

|`http-inputs-osdsecuritylogs.splunkcloud.com`
|443
|Used by the `splunk-forwarder-operator` as a logging forwarding endpoint to be used by Red{nbsp}Hat SRE for log-based alerting.

|`sftp.access.redhat.com` (Recommended)
|22
|The SFTP server used by `must-gather-operator` to upload diagnostic logs to help troubleshoot issues with the cluster.
|===

. Add the following URLs for the {GCP} API endpoints to an allowlist:
+
[cols="6,1,6",options="header"]
|===
|Domain | Port | Function

| `accounts.google.com`
| 443
| Used to access your {gcp-short} account.

|`*.googleapis.com`

OR

 `storage.googleapis.com`

 `iam.googleapis.com`

 `serviceusage.googleapis.com`

 `cloudresourcemanager.googleapis.com`

 `compute.googleapis.com`

 `oauth2.googleapis.com`

 `dns.googleapis.com`

 `iamcredentials.googleapis.com`
| 443
| Used to access {gcp-short} services and resources. Review Cloud Endpoints in the {gcp-short} documentation to determine the endpoints to allow for your APIs.
|===
+
[NOTE]
====
Required Google APIs can be exposed using the Private Google Access restricted virtual IP (VIP), with the exception of the Service Usage API (serviceusage.googleapis.com). To circumvent this, you must expose the Service Usage API using the Private Google Access private VIP.
====

[id="additional-resources_{context}"]
== Additional resources

* About remote health monitoring

* Creating a cluster on {gcp-short} with Workload Identity Federation authentication

* Example Workload Identity Federation configuration for OpenShift Container Platform on {GCP}
