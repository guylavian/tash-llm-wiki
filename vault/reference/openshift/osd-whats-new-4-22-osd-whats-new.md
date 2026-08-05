---
title: "What's new with {product-title}"
type: reference
domain: openshift
slug: osd-whats-new-4-22-osd-whats-new
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_whats_new/osd-whats-new
version: 4.22
family: osd_whats_new
documentKind: "Documentation"
---

# What's new with {product-title}

[id="osd-whats-new"]
= What's new with OpenShift Container Platform

[role="_abstract"]
With its foundation in Kubernetes, OpenShift Container Platform is a complete {OCP} cluster provided as a cloud service, configured for high availability, and dedicated to a single customer.

OpenShift Container Platform is professionally managed by Red{nbsp}Hat and hosted on {GCP} or {AWS}. Each OpenShift Container Platform cluster includes a fully managed control plane (Control and Infrastructure nodes), application nodes, installation and management by Red{nbsp}Hat Site Reliability Engineers (SRE), premium Red{nbsp}Hat Support, and cluster services such as logging, metrics, monitoring, notifications portal, and a cluster portal.

OpenShift Container Platform clusters are available on the Hybrid Cloud Console. With the Red{nbsp}Hat {cluster-manager} application, you can deploy OpenShift Container Platform clusters to cloud environments.

Find new additions, recent changes, and relevant updates for OpenShift Container Platform listed below in quarterly increments.

// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q2-2026_{context}"]
= Q2 2026

[role="_abstract"]
The following items were added during the second quarter of 2026.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform on {gcp} and OpenShift Container Platform on {aws} versions 4.22 are available for new clusters.

Upgrade channels are available::
+
You can choose the new channels option for more precise, version-specific control over your cluster updates. You can target exact minor version paths, such as `stable-4.20` or `fast-4.21`, instead of relying on broader channel groups, which are being deprecated. For more information, see Channels in OpenShift Container Platform clusters.

The `fast` upgrade channel is available as an update option::
+
You can choose `fast` as an upgrade channel when creating or updating your OpenShift Container Platform clusters. The `fast` channel is updated with new versions of OpenShift Container Platform as soon as Red{nbsp}Hat declares the version as a general availability (GA) release.

GCNV for {VirtProductName} on {GCP}::
+
{VirtProductName} on OpenShift Container Platform on {GCP} 4.21 and later adds support for {GCP} NetApp Volumes (GCNV) as a certified NFS storage backend when you use the NetApp Trident CSI Operator version 26.02.0 or later together with {VirtProductName} 4.21.2 or later.
+
GCNV provides NFS-based shared storage that supports ReadWriteMany (RWX) access in `Filesystem` mode. The NetApp Trident CSI driver provisions GCNV storage volumes.
+
For more information about using GCNV with {VirtProductName} on {GCP}, see the following articles in the Red{nbsp}Hat Knowledgebase:
+

* {GCP} with {GCP} NetApp Volumes - Configuration
* {GCP} with {GCP} NetApp Volumes - Known errors and limits

Support for excluding namespaces from default ingress load controller using label selectors::
+
With this update, you can use the `ocm` CLI to configure default ingress namespace exclusions for your cluster. For more information, see Configure excluded namespaces for the default ingress controller.

Support for new {gcp-short} instances::
+
With this update, you can create clusters with `g2` and `g4` instance types on OpenShift Container Platform version 4.21 and later. For more information, see {gcp-full} instance types.

OpenShift Container Platform managed DNS zones are available::
+
You can create and manage your own DNS zones for Shared VPC deployments on {GCP}, giving you greater control over your OpenShift Container Platform cluster's network configuration and security. This new capability allows you to maintain ownership of your DNS infrastructure while still leveraging the powerful features of OpenShift Container Platform.
+
By using managed DNS zones, you can ensure that your cluster's DNS records are managed according to your organization's policies and compliance requirements, without granting broad administrative access to your host projects. This improvement enhances security and provides a more flexible deployment option for customers with strict governance needs.
+
To support these managed DNS zones, additional permissions have been added to the Workload Identity Federation (WIF) template for OpenShift Container Platform versions 4.20 and 4.21. The deployer service account now includes the `dns.managedZones.update` permission so that the deployer can perform update operations on managed DNS zones.
+
For more information about managed DNS zones for OpenShift Container Platform on {GCP}, see Creating a managed DNS zone.

Support for new {gcp-short} instances::
+
OpenShift Container Platform version 4.18 and later adds support for `c2d`, `c3d`, `n2d` and `t2d` instance types on {gcp-full}. For more information, see {gcp-full} compute types.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q1-2026_{context}"]
= Q1 2026

[role="_abstract"]
The following items were added during the first quarter of 2026.

Virtualization support for OpenShift Container Platform on {GCP}::
+
OpenShift Container Platform on {GCP} version 4.21.5 supports running virtualized workloads using the {VirtProductName} Operator version 4.21.1, leveraging {GCP} C3 bare-metal instances and {GCP} Hyperdisk. This enables you to migrate and modernize virtual machines (VMs) from existing platforms directly onto OpenShift Container Platform, managing them alongside containerized workloads on a single, unified application platform.
+
For more information about using {VirtProductName} on OpenShift Container Platform on {gcp}, see:

* Virtualization
* OpenShift Virtualization release notes

OpenShift Container Platform is available in {GCP} console::
+
OpenShift Container Platform is available directly within the {GCP} console, making it easier to find and deploy alongside native {GCP} services. This integration simplifies the initial setup by allowing you to validate environment prerequisites for OpenShift Container Platform cluster deployment.
+
**Key improvements:**

* Improved discoverability: Locate OpenShift Container Platform quickly within the {GCP} console alongside Google's native compute and container offerings, allowing you to start creating clusters immediately.
* Streamlined onboarding: Validate your {GCP} configuration directly in the console before transitioning to a guided deployment flow in the {hybrid-console}.
* Unified billing and procurement: Use the {GCP} Marketplace to simplify setup and apply your existing {GCP} committed spend, negotiated discounts, or pay-as-you-go pricing.

+
For more information about deploying OpenShift Container Platform on {GCP}, see Understanding Customer Cloud Subscriptions on Google Cloud.

Cluster admins can create multiple users with htpasswd identity providers::
+
Cluster administrators can add multiple users to an htpasswd identity providers (IDPs) for OpenShift Container Platform clusters using the command-line interface (CLI). You can add multiple users to a single htpasswd IDP, streamlining managing user identities. Using the CLI, administrators can add multiple users interactively and noninteractively. For more information, see Configuring an htpasswd identity provider.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform on {gcp} and OpenShift Container Platform on {aws} versions 4.21 are available for new clusters.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q4-2025_{context}"]
= Q4 2025

[role="_abstract"]
The following items were added during the fourth quarter of 2025.

Support for managing workload identity pools and providers in a dedicated {GCP} project::
+
You can update an existing Workload Identity Federation (WIF) configuration on OpenShift Container Platform on {GCP} to use a dedicated project for managing workload identity pools and providers. For more information, see Updating a Workload Identity Federation configuration.

Required API services table updated::
+
The _Required API services_ table within the _Required customer procedure_ guide has been updated to restore APIs that were previously removed due to a bug. These APIs are required for new OpenShift Container Platform on {GCP} cluster creation.
+
The APIs that were restored are:

* Google Cloud APIs
* Network Security API

+
For more information, see the _Required API services_ table in the Required customer procedure.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform on {gcp} and OpenShift Container Platform on {aws} versions 4.20 are available for new clusters.

The EUS channel group is available::
+
You can select the Extended Update Support (EUS) channel group when creating or editing your OpenShift Container Platform cluster. The EUS channel group allows you to extend the life cycle of your even-numbered version OpenShift Container Platform cluster, giving you additional time to plan and budget for future upgrades. This channel group also provides continued security patches and critical bug fixes.
+
For additional information, see Life cycle dates.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q3-2025_{context}"]
= Q3 2025

[role="_abstract"]
The following items were added during the third quarter of 2025.

Updates to Workload Identity Federation (WIF) permissions and roles::
+
The default IAM permissions for WIF in the managed-cluster-config template have been updated. This means newly created WIF configurations will have fewer, less overly permissive permissions by default.

* The `sd-sre-platform-gcp-access@redhat.com` principal no longer needs the `compute.firewalls.create` permission. If Red{nbsp}Hat site reliability engineering (SRE) ever need this permission, they will reach out through a support case.
* The `osd-deployer` service account no longer requires the `resourcemanager.projects.setIamPolicy` permission, which has been removed.
* The `osd-deployer` service account no longer uses the `iam.serviceAccounts.signBlob` permission. This has been replaced with the `iam.serviceAccountTokenCreator` role, which is now specifically assigned to the service accounts that require it.
* The `osd-deployer` service account no longer uses the `iam.serviceAccounts.actAs` permission. This has been replaced with the `iam.serviceAccountUser` role, which is now specifically assigned to the service accounts that require it.

+
If you have existing `wif-config` instances, you can get these new, less permissive permissions by running the `ocm gcp update wif-config` command. For more information, see Updating a Workload Identify Federation configuration.

Workload Identify Federation (WIF) is now the default authentication type for OpenShift Container Platform clusters on {GCP}::
+
In alignment with the principle of least privilege as well as {gcp-full}'s preferred method of credential authentication, WIF is now the default authentication type when creating an OpenShift Container Platform cluster on {GCP}. WIF greatly improves an OpenShift Container Platform cluster's resilience against unauthorized access by using short-lived, least-privilege credentials and eliminating the need for static service account keys. For more information, see Creating a cluster on {gcp-short} with Workload Identity Federation authentication.

Support for managing workload identity pools and providers in a dedicated {GCP} project::
+
OpenShift Container Platform on {GCP} now supports the option of creating and managing workload identity pools and providers in a specified dedicated project during the creation of a WIF configuration. Red{nbsp}Hat plans on offering this option for existing WIF configurations in an upcoming release. For more information, see Creating a Workload Identify Federation configuration.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q2-2025_{context}"]
= Q2 2025

[role="_abstract"]
The following items were added during the second quarter of 2025.

// * **OpenShift Container Platform SDN network plugin blocks future major upgrades**
Updated version requirements for migration from OpenShift SDN to OVN-Kubernetes::
+
Your cluster version must be 4.16.43 or above to initiate live migration from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin.
+
If your cluster uses the OpenShift SDN network plugin, you cannot upgrade to future major versions of OpenShift Container Platform without migrating to OVN-Kubernetes.
+
For more information about migrating to OVN-Kubernetes, see Migrating from OpenShift SDN network plugin to OVN-Kubernetes network plugin.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform on {gcp} and OpenShift Container Platform on {aws} versions 4.19 are now available for new clusters.

Support for enabling and disabling Secure Boot for Shielded VMs on a per machine basis::
+
OpenShift Container Platform on {GCP} users can now enable or disable Secure Boot for Shielded VMs on a per machine basis. For more information, see Managing compute nodes.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q1-2025_{context}"]
= Q1 2025

[role="_abstract"]
The following items were added during the first quarter of 2025.

Support for new {gcp-short} instances::
+
OpenShift Container Platform version 4.18 and later now supports `n4` and `c3` instance types on {gcp-full}. For more information, see {gcp-full} compute types.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform on {gcp} and OpenShift Container Platform on {aws} versions 4.18 are now available. For more information about upgrading to this latest version, see OpenShift Dedicated cluster upgrades.

Support for assigning newly created machine pools to specific availability zones within a Multi-AZ cluster::
+
OpenShift Container Platform on {GCP} users can now assign machine pools to specific availability zones using the {cluster-manager} command line interface (CLI) (`ocm`). For more information, see Deploying a machine pool in a single availability zone within a Multi-AZ cluster.

Support for specifying OpenShift Container Platform versions when creating or updating a Workload Identity Federation (WIF) configuration::
+
OpenShift Container Platform on {GCP} users can now specify minor versions when creating or updating a WIF configuration. For more information, see Creating a Workload Identity Federation cluster using the OCM CLI.

Cluster node limit update::
+
OpenShift Container Platform clusters versions 4.14.14 and greater can now scale to 249 worker nodes. This is an increase from the previous limit of 180 nodes. For more information, see Limits and scalability.
// * **OpenShift Container Platform SDN network plugin blocks future major upgrades**
Initiate live migration from OpenShift SDN to OVN-Kubernetes::
+
As part of the OpenShift Container Platform move to OVN-Kubernetes as the only supported network plugin starting with OpenShift Container Platform version 4.17, users can now initiate live migration from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin.
+
If your cluster uses the OpenShift SDN network plugin, you cannot upgrade to future major versions of OpenShift Container Platform without migrating to OVN-Kubernetes.
+
For more information about migrating to OVN-Kubernetes, see Migrating from OpenShift SDN network plugin to OVN-Kubernetes network plugin.

Red{nbsp}Hat SRE log-based alerting endpoints have been updated::
+
OpenShift Container Platform customers who are using a firewall to control egress traffic can now remove all references to `*.osdsecuritylogs.splunkcloud.com:9997` from your firewall allowlist. OpenShift Container Platform clusters still require the `http-inputs-osdsecuritylogs.splunkcloud.com:443` log-based alerting endpoint to be accessible from the cluster.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q4-2024_{context}"]
= Q4 2024

[role="_abstract"]
The following items were added during the fourth quarter of 2024.

Workload Identity Federation (WIF) authentication type is now available::
+
OpenShift Container Platform on {gcp-first} customers can now use WIF as an authentication type when creating a cluster. WIF is a {gcp-short} Identity and Access Management (IAM) feature that provides third parties a secure method to access resources on a customer's cloud account. WIF is {gcp-full}'s preferred method for credential authentication.
+
For more information, see
Creating a cluster on {gcp-short} with Workload Identity Federation authentication.

Private Service Connect (PSC) networking feature is now available::
+
You can now create a private OpenShift Container Platform cluster on {gcp-first} using {gcp-full}'s security-enhanced networking feature Private Service Connect (PSC).
+
PSC is a capability of {gcp-full} networking that enables private communication between services across different {gcp-short} projects or organizations. Implementing PSC as part of your network connectivity allows you to deploy OpenShift Dedicated clusters in a private and secured environment within {gcp-short} without using any public-facing cloud resources.
+
For more information, see Private Service Connect overview.

Support for {gcp-short} A3 instances with NVIDIA H100 80GB GPUs::
+
OpenShift Container Platform on {GCP} now supports A3 instance types with NVIDIA H100 80GB GPUs. The {gcp-short} A3 instance type is available in all three zones of a {gcp-short} region, which is a prerequisite for multiple Availability Zone (Multiple AZ) deployment. For more information, see {gcp-full} instance types.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q3-2024_{context}"]
= Q3 2024

[role="_abstract"]
The following items were added during the third quarter of 2024.

Support for {gcp-short} A2 instance types with A100 80GB GPUs::
+
OpenShift Container Platform on {GCP} now supports A2 instance types with A100 80GB GPUs. These instance types meet the specific requirements listed by IBM Watsonx.ai. For more information, see {gcp-full} instance types.

Expanded support for {gcp-short} standard instance types::
+
OpenShift Container Platform on {GCP} now supports standard instance types for control plane and infrastructure nodes.
For more information, see Control plane and infrastructure node sizing and scaling.

OpenShift Container Platform regions added::
+
OpenShift Container Platform on {GCP} is now available in the following additional regions:

* Melbourne (`australia-southeast2`)
* Milan (`europe-west8`)
* Turin (`europe-west12`)
* Madrid (`europe-southwest1`)
* Santiago (`southamerica-west1`)
* Doha (`me-central1`)
* Dammam (`me-central2`)

+
For more information about region availabilities, see Regions and availability zones.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q2-2024_{context}"]
= Q2 2024

[role="_abstract"]
The following items were added during the second quarter of 2024.

Cluster delete protection::
+
OpenShift Container Platform on {GCP}  users can now enable the cluster delete protection option, which helps to prevent users from accidentally deleting a cluster.
//Removed link as is no longer valid. Need to decide if we need a link here and if so, what it will be.
// For more information, see Creating a cluster on GCP with CCS.

CSI Operator update::
+
OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Google Compute Platform (GCP) Filestore Storage. For more information, see Google Cloud Filestore CSI Driver Operator.

Support for new {gcp-short} instances::
+
OpenShift Container Platform now supports more worker node types and sizes on {gcp-full}. For more information, see {gcp-full} instance types.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q1-2024_{context}"]
= Q1 2024

[role="_abstract"]
The following items were added during the first quarter of 2024.

OpenShift Container Platform regions added::
+
OpenShift Container Platform on {GCP} is now available in the Delhi, India (`asia-south2`) region. For more information on region availabilities, see Regions and availability zones.

Policy constraint update::
+
OpenShift Container Platform on {GCP} users are now allowed to deploy clusters with the `constraints/iam.allowedPolicyMemberDomains` constraint in place. This feature allows users to restrict the set of identities that are allowed to be used in Identity and Access Management policies, further enhancing overall security for their resources.
// Module included in the following assemblies:
// * osd-whats-new.adoc

[id="osd-q4-2023_{context}"]
= Q4 2023

[role="_abstract"]
The following items were added during the fourth quarter of 2023.

Policy constraint update::
+
OpenShift Container Platform on {gcp-full} users can now enable UEFISecureBoot during cluster installation, as required by the {gcp-full} ShieldVM policy. This new feature adds further protection from boot or kernel-level malware or rootkits.

Cluster install update::
+
OpenShift Container Platform clusters can now be installed on {gcp-full} shared VPCs.

OpenShift Container Platform on {gcp-full} Marketplace availability::
+
When creating an OpenShift Container Platform cluster on {gcp-full} through the Hybrid Cloud Console, customers can now select {gcp-full} Marketplace as their preferred billing model. This billing model allows Red{nbsp}Hat customers to take advantage of their Google Committed Use Discounts (CUD) towards OpenShift Container Platform purchased through the {gcp-full} Marketplace.
