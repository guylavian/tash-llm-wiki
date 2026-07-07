---
title: "What's new for {product-title}"
type: reference
domain: openshift
slug: rosa-release-notes-4-22-rosa-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_release_notes/rosa-release-notes
version: 4.22
family: rosa_release_notes
documentKind: "Documentation"
---

# What's new for {product-title}

[id="rosa-whats-new"]
= What's new for OpenShift Container Platform

[role="_abstract"]
Find new additions, recent changes, and relevant updates for OpenShift Container Platform listed below in quarterly increments.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q2-2026_{context}"]
= Q2 2026

[role="_abstract"]
The following items were added during the second quarter of 2026.

{autonode} based on Karpenter v1.9 is available for managing compute nodes::
+
With this update, you can use {autonode} to automatically provision compute nodes based on workload demand. {autonode} is based on the open-source Karpenter project and provides dynamic node provisioning that matches workload requirements without requiring pre-configured node pools. When pods no longer require a node, {autonode} removes the node to reduce costs.

//For more information, see Managing compute nodes using {autonode}.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform version 4.22 is available for new clusters.

Upgrade channels are available::
+
You can select the new channels option for more precise, version-specific control over your cluster updates. You can target exact minor version paths, such as `stable-4.20` or `fast-4.21`, instead of relying on broader channel groups, which are being deprecated. For more information, see
 Channels in OpenShift Container Platform clusters.
Channels in OpenShift Container Platform clusters.

The `fast` upgrade channel is available as an update option::
+
You can select `fast` as an upgrade channel when creating or updating your OpenShift Container Platform clusters. Red{nbsp}Hat updates the `fast` channel with new versions of OpenShift Container Platform as soon as Red{nbsp}Hat declares the version as a general availability (GA) release.

FIPS-encrypted OpenShift Container Platform clusters::
+
With this update, you can create OpenShift Container Platform clusters with Federal Information Processing Standards (FIPS) encryption that adhere to the highest data security levels. For more information, see Deploying OpenShift Container Platform clusters using FIPS encryption.

The Modern TLS 1.3 security profile for OpenShift Container Platform clusters::
+
With this update, you can enhance the security of your managed endpoints by enforcing the Modern Transport Layer Security (TLS) 1.3 security profile. This profile ensures that all communications with the API server and OAuth endpoints comply with the latest security standards.

Machine pools can be scaled to zero nodes::
+
With this update, you can optimize infrastructure costs for OpenShift Container Platform by configuring machine pools to autoscale to zero nodes. By setting a minimum replica count of 0, use the cluster autoscaler to decommission all idle nodes in a pool. By doing this, you eliminate subscription and infrastructure expenses for high-cost resources, like GPU nodes or specialized on-demand workloads. For more information, see Creating a machine pool.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q1-2026_{context}"]
= Q1 2026

[role="_abstract"]
The following items were added during the first quarter of 2026.

Cluster admins can create multiple users with htpasswd identity providers::
+
Cluster administrators can add multiple users to an htpasswd identity providers (IDPs) for OpenShift Container Platform clusters using the command-line interface (CLI). You can add multiple users to a single htpasswd IDP, streamlining managing user identities. Using the CLI or Terraform, administrators can add users interactively and noninteractively. For more information, see Configuring an htpasswd identity provider.

Platform monitoring using the Cluster Monitoring Operator::
+
With this update, you can configure the in-cluster monitoring stack components, metrics, and alerts to monitor both core platform components and user-defined projects. Previously, you could only monitor user-defined projects. This change applies to both new and existing OpenShift Container Platform clusters. However, it affects them differently.

* For new clusters created after this change, the default, in-cluster monitoring stack is installed during cluster installation and immediately begins collecting metrics. After installation, you can use the default configuration, or you can modify the monitoring components to suit your needs.
* For existing clusters created prior to this change, no changes will be made to the cluster's monitoring configuration. However, you can begin to use the core platform monitoring components, and modify them to suit your needs.

+
For more information, see Monitoring projects on OpenShift Container Platform.

AWS Windows License Included is available for OpenShift Container Platform::
+
You can add a Windows License Included enabled machine pool to a OpenShift Container Platform cluster. For more information, see Creating a machine pool with AWS Windows License Included enabled using the {rosa-cli}.

Updating the global pull secret is available for OpenShift Container Platform clusters::
+
You can modify the global pull secret to include additional pull secrets for accessing container images from private registries. For more information, see Updating the global cluster pull secret.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform version 4.21 is available for new clusters.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q4-2025_{context}"]
= Q4 2025

[role="_abstract"]
The following items were added during the fourth quarter of 2025.

AWS GovCloud::
+
The Amazon Web Services (AWS) GovCloud service is now available for federal and government agencies. Commercial organizations and Federal Information Security Modernization Act (FISMA) R&D Universities may also use the service if they support a current government contract or are in the process of bidding on a government contract such as a request for proposal (RFP) or request for information (RFI) pre-bid stage. For more information, see
Getting started with ROSA GovCloud.
Getting started with ROSA GovCloud.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform version 4.20 is available for new clusters.

On-Demand Capacity Reservations and Capacity Blocks for ML are supported::
+
With this update, you can use pre-purchased Capacity Reservations when creating new machine pools on OpenShift Container Platform clusters. For more information, see Managing compute nodes.

ImageDigestMirrorSets (IDMS) is supported::
+
OpenShift Container Platform adds support for ImageDigestMirrorSets (IDMS), enabling clusters to redirect image pulls to a private, mirrored registry. This critical enhancement means customers in restricted networks can host their own mirrors for third-party images while satisfying strict security and compliance requirements. For more information, see Image registry mirroring for OpenShift Container Platform.

OpenShift Container Platform regions added::
+
OpenShift Container Platform is available in the following regions:

** Mexico (`mx-central-1`)
** Thailand (`ap-southeast-7`)

+
For more information on region availabilities, see Regions and availability zones.

The EUS channel group is available::
+
You can select the Extended Update Support (EUS) channel group when creating or editing your OpenShift Container Platform cluster. The EUS channel group allows you to extend the life cycle of your even-numbered version OpenShift Container Platform cluster, giving you additional time to plan and budget for future upgrades as well as providing continued security patches and critical bug fixes. For more information, see
Life cycle dates.
Life cycle dates.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q3-2025_{context}"]
= Q3 2025

[role="_abstract"]
The following items were added during the third quarter of 2025.

New cluster deletion policy::
+
OpenShift Container Platform clusters now have a new deletion policy. This policy is based on a set time period of customer non-response to service notifications. For more information, see Deletion policy. For specific revised terms and conditions, refer to Product Appendix 4.

Shared VPC for OpenShift Container Platform clusters::
+
You can create OpenShift Container Platform clusters in shared, centrally-managed AWS virtual private clouds (VPCs). For more information, see Configuring a shared VPC for ROSA with HCP clusters.

Deprecated `--private-link` flags for OpenShift Container Platform clusters::
+
Architectural changes to the ROSA CLI 1.2.55 make networking more flexible for OpenShift Container Platform clusters. The `--private-link` flag previously used when creating a OpenShift Container Platform cluster is now deprecated in favor of the `--private` and `--default-ingress-private` flags. Now, users can choose to have a combination of a public or private API with a public or private ingress. For more information, see Creating a private cluster on OpenShift Container Platform.

Changed default ingress listening method to begin with Day 1 operations::
+
Previously, the default ingress listening method was a Day 2 operation. Now, the default ingress listening method is a Day 1 operation.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q2-2025_{context}"]
= Q2 2025

[role="_abstract"]
The following items were added during the second quarter of 2025.

Updated version requirements for migration from OpenShift SDN to OVN-Kubernetes::
+
Your cluster version must be 4.16.43 or above to initiate live migration from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin.
+
If your cluster uses the OpenShift SDN network plugin, you cannot upgrade to future major versions of OpenShift Container Platform without migrating to OVN-Kubernetes.
+
For more information about migrating to OVN-Kubernetes, see Migrating from OpenShift SDN network plugin to OVN-Kubernetes network plugin.

AWS Trainium and Inferentia instance types now supported::
+
You can now use {AWS} Trainium and Inferentia instance types for your OpenShift Container Platform clusters. For more information, see
OpenShift Container Platform instance types.
OpenShift Container Platform instance types.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform version 4.19 is now available for new clusters. For more information about upgrading to this latest version, see Upgrading ROSA (classic architecture) clusters.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform version 4.19 is now available for new clusters. For more information about upgrading to this latest version, see Upgrading {hcp-title} clusters.

OpenShift Container Platform cluster ownership transfer is now available for OpenShift Container Platform::
+
You can now transfer ownership of OpenShift Container Platform clusters. For more information, see Initiating ownership transfer of a OpenShift Container Platform cluster.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q1-2025_{context}"]
= Q1 2025

[role="_abstract"]
The following items were added during the first quarter of 2025.

Cluster autoscaling is now available for OpenShift Container Platform::
+
You can configure cluster autoscaling for OpenShift Container Platform. For more information, see Cluster autoscaling.

OpenShift Container Platform region added::
+
OpenShift Container Platform is now available in the following regions:

* Tel Aviv (`il-central-1`)
* Calgary (`ca-west-1`)

+
For more information on region availabilities, see Regions and availability zones.

OpenShift Container Platform region added::
+
OpenShift Container Platform is now available in the following regions:

* Malaysia (`ap-southeast-5`)
* Tel Aviv (`il-central-1`)
* Calgary (`ca-west-1`)

+
For more information on region availabilities, see Regions and availability zones.

Cluster autoscaling is now available for OpenShift Container Platform::
+
You can configure cluster autoscaling for OpenShift Container Platform. For more information, see Cluster autoscaling.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform version 4.18 is now available. For more information about upgrading to this latest version, see Upgrading OpenShift Container Platform clusters.

New version of OpenShift Container Platform available::
+
OpenShift Container Platform version 4.18 is now available. For more information about upgrading to this latest version, see Upgrading OpenShift Container Platform clusters.

Graphical installer enhancements::
+
You can now use the graphical installer in {hybrid-console} to configure the following options when you create your cluster:

* Configure a `cluster-admin` user and optionally define a custom password.
* Configure the root disk size for the default machine pool.

Image configuration is now available for OpenShift Container Platform::
+
You can configure registries within a cluster to exclude some registries or allow only a defined list. It also allows to expose additional trusted bundle for registries to pull from. For more information, see Image configuration resources for OpenShift Container Platform.

OpenShift Container Platform cluster node limit update::
+
OpenShift Container Platform clusters versions 4.14.14 and greater can now scale to 249 worker nodes. This is an increase from the previous limit of 180 nodes.

Red{nbsp}Hat SRE log-based alerting endpoints have been updated::
+
OpenShift Container Platform customers who are using a firewall to control egress traffic can now remove all references to `*.osdsecuritylogs.splunkcloud.com:9997` from your firewall allowlist. OpenShift Container Platform clusters still require the `http-inputs-osdsecuritylogs.splunkcloud.com:443` log-based alerting endpoint to be accessible from the cluster.

OpenShift Container Platform now creates independent security groups for the AWS PrivateLink endpoint and worker nodes::
+
OpenShift Container Platform clusters version 4.17.2 and greater can now add additional AWS security groups to the AWS PrivateLink endpoint to allow additional ingress traffic to the cluster's API. For more information, see Adding additional AWS security groups to the AWS PrivateLink endpoint.

Egress zero is now generally available on OpenShift Container Platform clusters::
+
You can create a fully operational cluster that does not require a public egress by configuring a virtual private cloud (VPC) and using the `--properties zero_egress:true` flag when creating your cluster. For more information, see Creating a {egress-zero-title}.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q4-2024_{context}"]
= Q4 2024

[role="_abstract"]
The following items were added during the fourth quarter of 2024.

Learning tutorials for OpenShift Container Platform cluster and application deployment::
+
You can now use the Getting started with OpenShift Container Platform tutorials to quickly deploy a OpenShift Container Platform cluster for demo or learning purposes. You can also use the Deploying an application tutorials to deploy an application on your demo cluster.

Create a VPC using the ROSA CLI::
+
The `rosa create network` command lets you use the ROSA CLI to create a VPC for your cluster based on an AWS CloudFormation template. You can use this command to create and configure a VPC before creating your cluster.
For more information, see create network.
For more information, see create network.

Create additional security groups in OpenShift Container Platform clusters::
+
Starting with ROSA CLI version 1.2.47, you can now create additional security groups using the ROSA CLI when creating OpenShift Container Platform clusters. Note that additional security group IDs attached to the machine pool cannot be modified. To remove or add more security group IDs, replace the entire machine pool with a new one.

ROSA CLI update::
+
The ROSA CLI (`rosa`) was updated to a new version. For information about what has changed in this release, see the ROSA CLI release notes. For more information about the ROSA CLI (`rosa`), see
About the ROSA CLI.
About the ROSA CLI.

`VolumeDetachTimeout` configuration applied to machine pools for OpenShift Container Platform::
+
OpenShift Container Platform is applying a `VolumeDetachTimeout` configuration of 5 minutes to all machine pools. This prevents issues with node deletion when volumes fail to detach.

Configure machine pool disk volume for OpenShift Container Platform clusters::
+
You can now configure the disk volume size for machine pools in OpenShift Container Platform clusters. The default disk size is 300 GiB, and you can configure it from a minimum of 75 GiB to a maximum of 16,384 GiB. For more information, see Configuring machine pool disk volume.

Edit the billing account for existing OpenShift Container Platform clusters::
+
You can now update the billing account associated with your OpenShift Container Platform clusters after cluster creation. For more information, see Updating billing accounts for OpenShift Service on AWS Hosted Control Planes clusters.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q3-2024_{context}"]
= Q3 2024

[role="_abstract"]
The following items were added during the third quarter of 2024.

OpenShift Container Platform multi-architecture cluster update::
+
OpenShift Container Platform clusters created before 25 July, 2024 will migrate to a multi-architecture image on their next upgrade allowing you to use {AWS} Arm-based Graviton instance types for your workloads. For more information, see Upgrading {hcp-title} clusters.

OpenShift Container Platform cluster node limit update::
+
OpenShift Container Platform clusters can now scale to 500 worker nodes. This is an increase from the previous limit of 250 nodes. The 250 node limit is an increase from the previous limit 90 nodes on 26 August, 2024.

IMDSv2 support in OpenShift Container Platform::
+
You can now enforce the use of the IMDSv2 endpoint for default machine pool worker nodes on new OpenShift Container Platform clusters and for new machine pools on existing clusters. For more information, see Creating a default OpenShift Container Platform cluster using Terraform.

Upgrade multiple nodes simultaneously::
+
You can now configure a machine pool to upgrade multiple nodes simultaneously. Two new machine pool parameters, `max-surge` and `max-unavailable`, give you greater control over how machine pool upgrades occur. For more information, see Upgrading OpenShift Container Platform clusters.

OpenShift Container Platform Graviton Arm-based instance types::
+
You can now use {AWS} Arm-based Graviton instance types for your workloads in OpenShift Container Platform clusters created after 24 July, 2024. For more information, see AWS Graviton Arm-based instance types.

ROSA CLI update::
+
The ROSA CLI (`rosa`) was updated to a new version. For information about what has changed in this release, see the ROSA CLI release notes. For more information about the ROSA CLI (`rosa`), see
About the ROSA CLI.
About the ROSA CLI.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q2-2024_{context}"]
= Q2 2024

[role="_abstract"]
The following items were added during the second quarter of 2024.

Approve additional principals for OpenShift Container Platform clusters::
+
You can approve additional user-roles to connect to your cluster's private API server endpoint. For more information, see Additional principals on your OpenShift Container Platform cluster.

ROSA CLI update::
+
The ROSA CLI (`rosa`) was updated to a new version. For information about what has changed in this release, see the ROSA CLI release notes. For more information about the ROSA CLI (`rosa`),
see About the ROSA CLI.
see About the ROSA CLI.

Approved Access for OpenShift Container Platform clusters::
+
Red{nbsp}Hat Site Reliability Engineering (SRE) managing and proactively supporting OpenShift Container Platform clusters will typically not require elevated access to customer clusters as part of the normal operations. In the unlikely event should Red{nbsp}Hat SRE (Site Reliability Engineer) need elevated access, the _Approved Access_ functionality provides an interface for customers to review and _approve_ or _deny_ access requests.
+
Elevated access requests to OpenShift Container Platform clusters and the corresponding cloud accounts can be created by Red{nbsp}Hat SRE either in response to a customer-initiated support ticket or in response to alerts received by a Red{nbsp}Hat SRE, as part of the standard incident response process. For more information,
see Approved Access.
see Approved Access.

`rosa` command enhancement::
+
The `rosa describe` command has a new optional argument, `--get-role-policy-bindings`. This new argument allows users to view the policies attached to STS roles assigned to the selected cluster. For more information,
see describe cluster.
see describe cluster.

Expanded customer-managed policy capabilities::
+
You can now attach customer-managed policies to the IAM roles required to run OpenShift Container Platform clusters. Furthermore, these customer-managed policies, including the permissions attached to those policies, are not modified during cluster or role upgrades. For more information,
see Customer-managed policies.
see Customer-managed policies.

Permission boundaries for the installer role policy::
+
You can apply a policy as a _permissions boundary_ on the OpenShift Container Platform installer role. The combination of policy and boundary policy limits the maximum permissions for the Amazon Web Services(AWS) Identity and Access Management (IAM) entity role. OpenShift Container Platform includes a set of three prepared permission boundary policy files, with which you can restrict permissions for the installer role since changing the installer policy itself is not supported. For more information, see Permission boundaries for the installer role.

Cluster delete protection::
+
You can now enable the cluster delete protection option, which helps to prevent you from accidentally deleting a cluster. For more information on using the cluster delete protection option with the ROSA CLI, see edit cluster. For more information on using the cluster delete protection option in the UI, see Creating a cluster with the default options using OpenShift Cluster Manager.
OpenShift Container Platform regions added::
+
OpenShift Container Platform is now available in the following regions:

** Zurich (`eu-central-2`)
** Hong Kong (`ap-east-1`)
** Osaka (`ap-northeast-3`)
** Spain (`eu-south-2`)
** UAE (`me-central-1`)

+
For more information on region availabilities, see Regions and availability zones.

Added support for external authentication providers::
+
You can now create clusters configured with external authentication providers, such as Microsoft Entra ID and KeyCloak. For more information, see Creating OpenShift Container Platform clusters with external authentication.

Longer cluster names enhancement::
+
You can now specify a cluster name that is longer than 15 characters. For cluster names that are longer than 15 characters, you can customize the domain prefix for the cluster URL by using the `domain-prefix` flag in the ROSA CLI (`rosa`) or by selecting the **Create custom domain prefix** checkbox in the {hybrid-console}. For more information,
see create cluster in Managing objects with the ROSA CLI.
see create cluster in Managing objects with the ROSA CLI.

Additional Security Groups for OpenShift Container Platform::
+
Starting with ROSA CLI version 1.2.37, you can now use the `--additional-security-group-ids <sec_group_id>` when creating machine pools on {hcp-title} clusters. For more information, see Creating a machine pool using the ROSA CLI and the create machinepool section of the ROSA CLI reference.

Node management improvements::
+
Now, you can perform specific tasks to make clusters more efficient. You can cordon, uncordon, and drain a specific node. For more information,
see Working with nodes.
see Working with nodes.

Node drain grace periods::
+
You can now configure node drain grace periods in {hcp-title} clusters with the `rosa` CLI.
+
For more information about configuring node drain grace periods, see Configuring node drain grace periods in OpenShift Container Platform.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q1-2024_{context}"]
= Q1 2024

[role="_abstract"]
The following items were added during the first quarter of 2024.

Machine pool update::
+
You can now upgrade machine pools that are configured on ROSA with HCP clusters. For more information, see upgrade machinepool.

OpenShift Container Platform regions added::
+
OpenShift Container Platform is now available in the following regions:

** Hyderabad (`ap-south-2`)
** Milan (`eu-south-1`)
** London (`eu-west-2`)
** Mumbai (`ap-south-1`)
** Cape Town (`af-south-1`)
** Seoul (`ap-northeast-2`)
** Stockholm (`eu-north-1`)

+
For more information on region availabilities, see Regions and availability zones.

ROSA CLI update::
+
The ROSA CLI (`rosa`) was updated to a new version. For information about what has changed in this release, see the ROSA CLI release notes. For more information about the ROSA CLI (`rosa`), see
About the ROSA CLI.
About the ROSA CLI.

Log linking is enabled by default::
+
Beginning with OpenShift Container Platform 4.15, log linking is enabled by default. Log linking gives you access to the container logs for your pods.

Availability zone update::
+
You can now optionally select a single availability zone (AZ) for machine pools when you have a multi-AZ cluster. For more information, see
Creating a machine pool using the ROSA CLI.
Creating a machine pool using the ROSA CLI.

Delete cluster command enhancement::
+
With the release of ROSA CLI (`rosa`) version 1.2.31, the `--best-effort` argument was added, which allows you to force-delete clusters when using the `rosa delete cluster` command. For more information, see
delete cluster.
delete cluster.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q4-2023_{context}"]
= Q4 2023

[role="_abstract"]
The following items were added during the fourth quarter of 2023.

ROSA CLI update::
+
The ROSA CLI (`rosa`) was updated to a new version. For information about what has changed in this release, see the ROSA CLI release notes. For more information about the ROSA CLI (`rosa`), see About the ROSA CLI.

Delete cluster command enhancement::
+
With the release of ROSA CLI (`rosa`) version 1.2.31, the `--best-effort` argument was added, which allows you to force-delete clusters when using the `rosa delete cluster` command. For more information, see delete cluster.

{hcp-title-first} that uses {hcp} is now generally available::
+
For more information, see Creating OpenShift Container Platform clusters using the default options.

Configurable process identifier (PID) limits::
+
With the release of ROSA CLI (`rosa`) version 1.2.31, administrators can use the `rosa create kubeletconfig` and `rosa edit kubeletconfig` commands to set the maximum PIDs for an existing cluster. For more information, see Changing the maximum number of process IDs per pod (podPidsLimit) for OpenShift Container Platform.

Configure custom security groups::
+
With the release of ROSA CLI (`rosa`) version 1.2.31, administrators can use the `rosa create` command or the OpenShift Cluster Manager to create a new cluster or a new machine pool with up to 5 additional custom security groups. Configuring custom security groups gives administrators greater control over resource access in new clusters and machine pools. For more information, see Security groups.

Command update::
+
With the release of ROSA CLI (`rosa`) version 1.2.28, a new command, `rosa describe machinepool`, was added that allows you to check detailed information regarding a specific OpenShift Container Platform cluster machine pool. For more information, see describe machinepool.

Documentation update::
+
The Operators section was added to the OpenShift Container Platform documentation. Operators are the preferred method of packaging, deploying, and managing services on the control plane. For more information, see Operators overview.

{VirtProductName} support::
+
The release of {VirtProductName} 4.14 added support for running {VirtProductName} on OpenShift Container Platform clusters. For more information, see {VirtProductName} on AWS bare metal in the {OCP} documentation.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q3-2023_{context}"]
= Q3 2023

[role="_abstract"]
The following items were added during the third quarter of 2023.

ROSA CLI update::
+
The ROSA CLI (`rosa`) was updated to a new version. For information about what has changed in this release, see the ROSA CLI release notes. For more information about the ROSA CLI (`rosa`), see About the ROSA CLI.

Cluster autoscaling::
+
You can now enable cluster autoscaling using OpenShift Container Platform clusters. Cluster autoscaling automatically adjusts the size of a cluster so that all pods have a place to run, and there are no unneeded nodes. You can enable autoscaling during and after cluster creation using either OpenShift Cluster Manager or the ROSA CLI (`rosa`). For more information, see Cluster autoscaling.

Shared virtual private clouds::
+
OpenShift Container Platform now supports installing clusters into VPCs shared among AWS accounts that are part of AWS organizations. AWS account installing {rosa-classic-title} clusters can now use shared subnets owned by a management account. For more information, see Configuring a shared virtual private cloud for OpenShift Container Platform clusters.

Machine pool disk volume size::
+
You can now configure your machine pool disk volume size for additional flexibility. You can select your own sizing for the disk volumes of their worker machine pool nodes. For more information, see Configuring machine pool disk volume.

Machine pool update::
+
You can now add taints to the machine pool that is automatically generated during cluster creation. You can also delete this machine pool. This new feature provides more flexibility and cost-effectiveness for cluster administrators, specifically in regards to scaling infrastructure based on changing resource requirements. For more information, see Creating a machine pool.

Documentation update::
+
The CLI Tools section was added to the OpenShift Container Platform documentation and includes more detailed information to help you fully use all of the supported CLI tools. The ROSA CLI section can now be found nested inside the CLI Tools heading. For more information, see CLI tools overview.

Documentation update::
+
The Monitoring section in the documentation was expanded and now includes more detailed information to help you conveniently manage your OpenShift Container Platform clusters. For more information, see About OpenShift Container Platform monitoring.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q2-2023_{context}"]
= Q2 2023

[role="_abstract"]
The following items were added during the second quarter of 2023.

ROSA CLI update::
+
The ROSA CLI (`rosa`) was updated to a new version. For information about what has changed in this release, see the ROSA CLI release notes. For more information about the ROSA CLI (`rosa`), see About the ROSA CLI.

OpenShift Container Platform region added::
+
OpenShift Container Platform is now available in the United Arab Emirates (`me-central-1`) region. For more information on region availability, see Regions and availability zones.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-q1-2023_{context}"]
= Q1 2023

[role="_abstract"]
The following items were added during the first quarter of 2023.

OIDC provider endpoint URL update::
+
Starting with ROSA CLI version 1.2.7, all new cluster OIDC provider endpoint URLs are no longer regional. Amazon CloudFront is part of this implementation to improve access speed, reduce latency, and improve resiliency. This change is only available for new clusters created with ROSA CLI 1.2.7 or later. There are no supported migration paths for existing OIDC provider configurations.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-known-issues_{context}"]
= Known issues

[role="_abstract"]
The following items are known issues with OpenShift Container Platform releases.

`ocm-role` and `user-role` can be enabled accidentally::
+
The {cluster-manager} roles (`ocm-role`) and user roles (`user-role`) that are key to the OpenShift Container Platform provisioning wizard might get enabled accidentally in your Red{nbsp}Hat organization by another user. However, this behavior does not affect the usability.

`htpasswd` does not function as expected::
+
The `htpasswd` identity provider does not function as expected in all scenarios against the `rosa create admin` function.

// Module included in the following assemblies:
// * rosa-release-notes.adoc

[id="rosa-deprecated-removed-features_{context}"]
= Deprecated and removed features

[role="_abstract"]
Some features available in previous releases have been deprecated or removed. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.

Disable workload monitoring::
+
Previously, users could disable workload monitoring on OpenShift Container Platform clusters. However, to allow users to own the full Cluster Monitoring Operator (CMO) stack on OpenShift Container Platform clusters, the ability to disable workload monitoring has been deprecated. For more information, see Preparing to configure the user workload monitoring stack.

OpenShift Container Platform non-STS deployment mode::
+
OpenShift Container Platform non-STS deployment mode is no longer the preferred method for new clusters. Instead, users must deploy OpenShift Container Platform with the STS mode. This deprecation is in line with our new OpenShift Container Platform provisioning wizard UI experience on the Red Hat Hybrid Cloud Console.

Label removal on core namespaces::
+
OpenShift Container Platform is no longer labeling OpenShift core using the `name` label. Customers should migrate to referencing the `kubernetes.io/metadata.name` label if needed for Network Policies or other use cases.
