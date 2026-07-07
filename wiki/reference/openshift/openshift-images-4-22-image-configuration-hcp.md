---
title: "Image configuration resources"
type: reference
domain: openshift
slug: openshift-images-4-22-image-configuration-hcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/image-configuration-hcp
version: 4.22
family: openshift_images
documentKind: "Documentation"
---

# Image configuration resources

[id="image-configuration-hcp"]
= Image configuration resources

[role="_abstract"]
You can configure image registries to manage how OpenShift Container Platform pulls and uses container images in your cluster.

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc

[id="images-configuration-parameters-hcp_{context}"]
= Image controller configuration parameters for OpenShift Container Platform

[role="_abstract"]
The `image.config.openshift.io/cluster` resource holds cluster-wide information about how to handle images. The resource exists, but it is read only and can only be changed through supported tools such as the ROSA CLI (`rosa`). The canonical and only valid name is `cluster`. It can be configured in OpenShift Container Platform through `rosa` commands.

[NOTE]
====
Parameters such as `DisableScheduledImport`, `MaxImagesBulkImportedPerRepository`, `MaxScheduledImportsPerMinute`, `ScheduledImageImportMinimumIntervalSeconds`, `InternalRegistryHostname` are not configurable.
====

[cols="3a,8a",options="header"]
|===
|Parameters for ROSA CLI |Description

|`registry-config-allowed-registries`
|Registries for which image pull and push actions are allowed. To specify all subdomains, add the asterisk (`\*`) wildcard character as a prefix to the domain name. For example, `*.example.com`. You can specify an individual repository within a registry. For example, `reg1.io/myrepo/myapp:latest`. All other registries are blocked. The format should be a comma-separated list of allowed registries. For example, `allowed.io, allowed.io2`.

|`registry-config-insecure-registries`
|Registries which do not have a valid TLS certificate or only support HTTP connections. To specify all subdomains, add the asterisk (`\*`) wildcard character as a prefix to the domain name. For example, `*.example.com`. You can specify an individual repository within a registry. For example, `reg1.io/myrepo/myapp:latest`. The format should be a comma-separated list of insecure registries. For example, `insecure.io, insecure.io2`.

|`registry-config-blocked-registries`
|Registries for which image pull and push actions are denied. To specify all subdomains, add the asterisk (`\*`) wildcard character as a prefix to the domain name. For example, `*.example.com`. You can specify an individual repository within a registry. For example, `reg1.io/myrepo/myapp:latest`. All other registries are allowed. The format should be a comma-separated list of blocked registries. For example, `blocked.io, blocked.io2`.

|`registry-config-allowed-registries-for-import`
|Specifies configuration that determines how the container runtime should treat individual registries when accessing images for builds and pods. For example, whether or not to allow insecure access. It does not contain configuration for the internal cluster registry. Limits the container image registries from which normal users can import images. The format should be a comma-separated list of `domainName:insecure`. `domainName` specifies a domain name for the registry. `insecure` indicates whether the registry is secure or insecure.

|`registry-config-additional-trusted-ca`
|A JSON file containing the registry hostname as the key, and the Privacy Enhanced Mail (PEM)-encoded certificate as the value, for each additional registry CA to trust.

|===

[WARNING]
====
When the `allowedRegistries` parameter is defined, all registries are blocked unless explicitly listed. To prevent pod failure, a list of Red{nbsp}Hat registries is automatically allowlisted, as they are required by payload images within your environment. The current list consists of `image-registry.openshift-image-registry.svc:5000,quay.io,registry.redhat.io` and it is also visible when running the `rosa describe cluster` command.
====

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc

[id="images-configuring-image-registry-settings-hcp_{context}"]
= Configuring image registry settings for OpenShift Container Platform

[role="_abstract"]
You can configure image registry settings at cluster creation. The cluster's nodes will use the required configuration after creation.

.Procedure

* Create OpenShift Container Platform clusters with image registry by running the following command:

+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name> --sts --mode=auto \
   --hosted-cp --operator-roles-prefix <operator_role_prefix> \
   --oidc-config-id <id_of_oidc_configuration> \
   --subnet-ids=<public_subnet_id>,<private_subnet_id> \
   --registry-config-insecure-registries <insecure_registries> \
   --registry-config-allowed-registries <allowed_registries> \
   --registry-config-allowed-registries-for-import <registry_name:insecure> \
   --registry-config-additional-trusted-ca <additional_trusted_ca_file>
----
+
[NOTE]
====
When using the `allowedRegistries`, `blockedRegistries`, or `insecureRegistries` parameter, you can specify an individual repository within a registry. For example: `reg1.io/myrepo/myapp:latest`.

Avoid insecure external registries to reduce possible security risks.
Parameters `allowedRegistries`, `blockedRegistries` are mutually exclusive.
====

.Verification

. Run the `rosa describe` command to verify that your image registry is enabled by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
Name:                       rosa-hcp-test
Domain Prefix:              rosa-hcp-test
Display Name:               rosa-hcp-test
ID:                         <cluster_hcp_id>
External ID:                <cluster_hcp_id>
Control Plane:              ROSA Service Hosted
OpenShift Version:          4.Y.Z
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_id>
AWS Billing Account:        <aws_id>
API URL:                    <ocm_api>
Console URL:
Region:                     us-east-1
Availability:
 - Control Plane:           MultiAZ
 - Data Plane:              SingleAZ
Nodes:
 - Compute (desired):       2
 - Compute (current):       2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             /23
 - Subnets:                 <subnet_ids>
EC2 Metadata Http Tokens:   optional
Role (STS) ARN:             arn:aws:iam::<aws_id>:role/<account_roles_prefix>-HCP-ROSA-Installer-Role
Support Role ARN:           arn:aws:iam::<aws_id>:role/<account_roles_prefix>-HCP-ROSA-Support-Role
Instance IAM Roles:
 - Worker:                  arn:aws:iam::<aws_id>:role/<account_roles_prefix>-HCP-ROSA-Worker-Role
Operator IAM Roles:
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-kube-system-capa-controller-manager
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-kube-system-control-plane-operator
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-kube-system-kms-provider
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-image-registry-installer-cloud-cred
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-ingress-operator-cloud-credentials
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-cluster-csi-drivers-ebs-cloud-credent
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-cloud-network-config-controller-cloud
Managed Policies:           Yes
State:                      ready
Private:                    No
Delete Protection:          Disabled
Created:                    Oct 01 2030 09:48:52 UTC
User Workload Monitoring:   Enabled
OIDC Endpoint URL:          https://<endpoint> (Managed)
Audit Log Forwarding:       Disabled
External Authentication:    Disabled
Etcd Encryption:            Disabled
Registry Configuration:
 - Allowed Registries: <allowed_registry>
 - Insecure Registries: <insecure_registry>
 - Allowed Registries for Import:
    - Domain Name: <domain_name>
    - Insecure: true
 - Platform Allowlist: <platform_allowlist_id>
    - Registries:      <list_of_registries>
 - Additional Trusted CA:
    - <registry_name> : REDACTED
----
where:

`Allowed Registries`:: A comma-separated list of registries for which image pull and push actions are allowed.
`Blocked Registries`:: A comma-separated list of registries for which image pull and push actions are blocked. Parameters `allowedRegistries`, `blockedRegistries` are mutually exclusive.
`Insecure Registries`:: A comma-separated list of registries which do not have a valid TLS certificate or only support HTTP connections.
`Allowed Registries for Import`:: Limits the container image registries from which normal users can import images. The format should be a comma-separated list of `domainName:insecure`.
`domainName`:: Specifies a domain name for the registry.
`insecure`:: Indicates whether the registry is secure or insecure.
`Platform Allowlist`:: A reference to the id of the list of registries that needs to be allowlisted for the platform to work.
`Registries`:: The list of registries that needs to be allowlisted for the platform to work.
`Additional Trusted CA`:: A JSON file containing the registry hostname as the key, and the Privacy Enhanced Mail (PEM)-encoded certificate as the value, for each additional registry CA to trust.

. List your nodes to check the applied changes by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                         STATUS                     ROLES                  AGE   VERSION
worker-1.compute.local                       Ready,SchedulingDisabled   worker                 65m   v1.35.4
worker-2.compute.local                       Ready                      worker                 65m   v1.35.4
worker-3.compute.local                       Ready                      worker                 63m   v1.35.4
----

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="images-editing-image-registry-settings-hcp_{context}"]
= Editing image registry settings for OpenShift Container Platform

[role="_abstract"]
You can change the image registry config with the `rosa edit` command.

[WARNING]
====
When the `allowedRegistries` parameter is defined, all registries are blocked unless explicitly listed. To prevent pod failure, a list of Red{nbsp}Hat registries is automatically allowlisted, as they are required by payload images within your environment. The current list consists of `image-registry.openshift-image-registry.svc:5000,quay.io,registry.redhat.io` and it is also visible when running the `rosa describe cluster` command.
====

[NOTE]
====
You can change any registry-related parameter, which will trigger a rollout across all machine pools; all machine pool nodes will be recreated, following pod draining from each node.
====

.Procedure

* Update or edit the image registry for the cluster by running the following command:

+
[source,terminal]
----
$ rosa edit cluster --cluster=<cluster_name> --registry-config-insecure-registries <insecure_registries> \
   --registry-config-allowed-registries <allowed_registries> \
   --registry-config-allowed-registries-for-import <registry_name:insecure> \
   --registry-config-additional-trusted-ca <additional_trusted_ca_file>
----
+
.Example output
[source,terminal]
----
? Changing any registry related parameter will trigger a rollout across all machinepools
(all machinepool nodes will be recreated, following pod draining from each node).
Do you want to proceed? Yes
I: Updated cluster '<cluster_name>'
----

.Verification
* Run the `rosa describe` command again, to see if the changes you made to your image registry updated by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
Name:                       rosa-hcp-test
Domain Prefix:              rosa-hcp-test
Display Name:               rosa-hcp-test
ID:                         <cluster_hcp_id>
External ID:                <cluster_hcp_id>
Control Plane:              ROSA Service Hosted
OpenShift Version:          4.Y.Z
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_id>
AWS Billing Account:        <aws_id>
API URL:                    <ocm_api>
Console URL:
Region:                     us-east-1
Availability:
 - Control Plane:           MultiAZ
 - Data Plane:              SingleAZ

Nodes:
 - Compute (desired):       2
 - Compute (current):       2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             /23
 - Subnets:                 <subnet_ids>
EC2 Metadata Http Tokens:   optional
Role (STS) ARN:             arn:aws:iam::<aws_id>:role/<account_roles_prefix>-HCP-ROSA-Installer-Role
Support Role ARN:           arn:aws:iam::<aws_id>:role/<account_roles_prefix>-HCP-ROSA-Support-Role
Instance IAM Roles:
 - Worker:                  arn:aws:iam::<aws_id>:role/<account_roles_prefix>-HCP-ROSA-Worker-Role
Operator IAM Roles:
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-kube-system-capa-controller-manager
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-kube-system-control-plane-operator
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-kube-system-kms-provider
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-image-registry-installer-cloud-cred
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-ingress-operator-cloud-credentials
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-cluster-csi-drivers-ebs-cloud-credent
 - arn:aws:iam::<aws_id>:role/<operator_roles_prefix>-openshift-cloud-network-config-controller-cloud
Managed Policies:           Yes
State:                      ready
Private:                    No
Delete Protection:          Disabled
Created:                    Oct 01 2030 09:48:52 UTC
User Workload Monitoring:   Enabled
OIDC Endpoint URL:          https://<endpoint> (Managed)
Audit Log Forwarding:       Disabled
External Authentication:    Disabled
Etcd Encryption:            Disabled
Registry Configuration:
 - Allowed Registries: <allowed_registry>
 - Insecure Registries: <insecure_registry>
 - Allowed Registries for Import:
    - Domain Name: <domain_name>
    - Insecure: true
 - Platform Allowlist: <platform_allowlist_id>
    - Registries:      <list_of_registries>
 - Additional Trusted CA:
    - <registry_name> : REDACTED
----
+
where:

`Allowed Registries`:: A comma-separated list of registries for which image pull and push actions are allowed.
`Blocked Registries`:: A comma-separated list of registries for which image pull and push actions are blocked. Parameters `allowedRegistries`, `blockedRegistries` are mutually exclusive.
`Insecure Registries`:: A comma-separated list of registries which do not have a valid TLS certificate or only support HTTP connections.
`Allowed Registries for Import`:: Limits the container image registries from which normal users can import images. The format should be a comma-separated list of `domainName:insecure`.
`domainName`:: Specifies a domain name for the registry.
`insecure`:: Indicates whether the registry is secure or insecure.
`Platform Allowlist`:: A reference to the id of the list of registries that needs to be allowlisted for the platform to work.
`Registries`:: The list of registries that needs to be allowlisted for the platform to work.
`Additional Trusted CA`:: A JSON file containing the registry hostname as the key, and the Privacy Enhanced Mail (PEM)-encoded certificate as the value, for each additional registry CA to trust.

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="images-updating-platform-allowlist-hcp_{context}"]
= Updating platform allowlist for OpenShift Container Platform

[role="_abstract"]
A list of Red{nbsp}Hat registries is automatically allowed and it is visible when running rosa describe cluster. This list can be periodically updated to ensure platform can be operated correctly. Impacted clusters will receive a notification with the new allowlist ID. In such cases, the user must use this parameter to update from the previous expected ID to the newly expected ID.

.Procedure

* Update or edit the image registry for the cluster by running the following command:
+
[source,terminal]
----
$ rosa edit cluster --cluster=<cluster_name> --registry-config-platform-allowlist <newID>
----

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc

[id="images-registry-mirroring_{context}"]
=  Image registry mirroring for OpenShift Container Platform

[role="_abstract"]
You can configure an existing OpenShift Container Platform cluster to pull images from a mirrored registry by using the `ImageDigestMirrorSet (IDMS)` object.

[IMPORTANT]
====
The image mirror configuration feature operates exclusively with image references by digest, meaning that image mirroring will only activate when an image is pulled using its unique and immutable ID. Any image references using a mutable tag are currently not supported by this functionality.
====

IDMS defines a set of cluster-wide policies for registry mirroring that makes image downloads faster, more reliable and more secure. It works by intercepting any image pull request that identifies an image by its unique, content-addressable digest. Based on these policies, the IDMS transparently redirects the pull operation from its specified source registry to one or more designated mirror registries. For the developer, this means their request (still pointing to the original source) is automatically fulfilled by a faster, closer mirror, significantly improving deployment speed without requiring any changes to their workflow.

.Prerequisites
To configure an existing OpenShift Container Platform cluster to pull images from a mirrored registry by using the `ImageDigestMirrorSet (IDMS)` object, you must meet the following prerequisites:

** You have installed and configured the latest {rosa-cli-first} on your installation host.
** You have installed a OpenShift Container Platform cluster.
** The OpenShift Container Platform cluster must be in a **Ready** state to create, edit, list, or delete image mirrors.
** You have access to the mirror registries you want to configure.
** You have the required IAM permissions to manage cluster configurations. For more information, see "About IAM resources" in the _Additional resources_ section.

The benefits of configuring your OpenShift Container Platform cluster to pull images from a mirrored registry using IDMS include:

** *Enhanced Security*: By forcing image pulls from a private, mirrored registry, you can scan and approve all images for vulnerabilities before they ever enter your cluster.

** *Improved Cluster Reliability*: A local mirror guarantees stable and predictable cluster performance by eliminating reliance on public internet pathways.

** *Guaranteed Image Consistency*: IDMS uses image digests to reference images, which ensures that every node in the cluster pulls the same version of an image, preventing inconsistencies which could lead to deployment failures.

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc

[id="images-registry-mirroring-create_{context}"]
= Creating an image mirror configuration

[role="_abstract"]
You can create an image mirror configuration for a OpenShift Container Platform cluster with the {rosa-cli-first} tool.

[IMPORTANT]
====
The source registry cannot be modified after creation. You must delete and re-create the image mirror to change the source.
====

.Procedure

* Run the following command to create an image mirror configuration:
+
[source,terminal]
----
$ rosa create image-mirror [arguments]
----
+
.Arguments
[cols="30,70"]
|===
|Option |Definition

a|--cluster
|Required: The name or ID of the cluster the mirror configuration will be applied to.

|--source
|Required: The source registry that will be mirrored.

|--mirrors
|Required: List of mirror registries. Mirror registries must be comma-separated.

|--type=digest
|Optional: Type of image mirror. The `digest` type is set by default and the only available `type` option.

|--profile
|Optional: Specifies an AWS profile (string) from your credentials file.

|--region
|Optional:Specifies an AWS region, overriding the AWS_REGION environment variable.
|===
+
.Examples
Creates an image mirror configuration for a cluster named `mycluster`.
+
[source,terminal]
----
$ rosa create image-mirror --cluster=mycluster \
  --source=registry.example.com/team \
  --mirrors=mirror.corp.com/team,backup.corp.com/team
----
+
.Example Output
[source,terminal]
----
I: Image mirror with ID 'abc123def456' has been created on cluster 'mycluster'
I: Source: registry.example.com/team
I: Mirrors: [mirror.corp.com/team backup.corp.com/team]
----
+
[NOTE]
====
An ID is automatically generated and assigned to an image mirror during image mirror configuration creation.
====

* Run the following command to create an image mirror configuration with a specific type:
+
[source,terminal]
----
$ rosa create image-mirror --cluster=mycluster \
  --type=digest --source=docker.io/library \
  --mirrors=internal-registry.company.com/dockerhub
----
+
[NOTE]
====
The `digest` type is set by default and the only available `type` option.
====

* Run the following command to create a single image mirror configuration with multiple mirrors for a cluster:
+
[source,terminal]
----
$ rosa create image-mirror --cluster=mycluster \
  --source=quay.io/openshift \
  --mirrors=mirror1.company.com/openshift,mirror2.company.com/openshift,mirror3.company.com/openshift
----

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc

[id="images-registry-mirroring-edit_{context}"]
= Editing an image mirroring configuration

[role="_abstract"]
You can edit an image mirror configuration for a OpenShift Container Platform cluster with the {rosa-cli-first} tool.

[NOTE]
====
When editing an image mirror configuration, the new mirrors list completely replaces the existing mirrors list.
====

.Procedure

. Run the following command to edit an image mirror configuration:
+
[source,terminal]
----
$ rosa edit image-mirror [arguments]
----
+
.Arguments
[cols="30,70"]
|===
|Option |Definition

|--cluster
|Required: The name or ID (string) of the cluster to which the image mirror configuration applies.

|--mirrors
|Required: New list of mirror registries that replaces current mirror registries. Mirror registries must be comma-separated.

|--id
|Required: ID of the image mirror configuration to edit.

|--profile
|Optional: Use a specific AWS profile from your credential file.

|--region
|Optional: Use a specific AWS region, overriding the AWS_REGION environment variable.
|===

. Run the following command to replace a single mirror on an image mirror configuration:
+
[source,terminal]
----
$ rosa edit image-mirror --cluster=mycluster --id=abc123def456 \
  --mirrors=single-mirror.company.com/team
----
+
.Example Output
[source,terminal]
----
I: Image mirror 'abc123def456' has been updated on cluster 'mycluster'
I: Source: registry.example.com/team
I: Updated mirrors: [single-mirror.company.com/team]
----

. Run the following command to replace all mirrors on an image mirror configuration:
+
[source,terminal]
----
$ rosa edit image-mirror --cluster=mycluster --id=abc123def456 \
  --mirrors=new-primary.company.com/team,new-secondary.company.com/team
----

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc

[id="images-registry-mirroring-list_{context}"]
= Listing all image mirror configurations

[role="_abstract"]
You can list all image mirror configurations from a OpenShift Container Platform cluster with the {rosa-cli-first}.

.Procedure

. Run the following command to list all image mirror configurations for a OpenShift Container Platform cluster:
+
[source,terminal]
----
$ rosa list image-mirrors [arguments]
----
+
.Arguments
[cols="30,70"]
|===
|Option |Definition
|--cluster
|Required: Name or ID of the cluster.
|--output
|Optional: Output format. Allowed formats are `json`, `yaml`
|--profile
|Optional: Use a specific AWS profile from your credential file.
|--region
|Optional: Use a specific AWS region, overriding the AWS_REGION environment variable.
|===

. Run the following command to list all image mirror configurations for a cluster:
+
[source,terminal]
----
$ rosa list image-mirrors --cluster=mycluster
----
+
.Example Outputs
[source,terminal]
----
ID              TYPE    SOURCE                    MIRRORS
abc123def456    digest  registry.example.com/team mirror.corp.com/team, backup.corp.com/
----

// Module included in the following assemblies:
//
// * openshift_images/image-configuration-hcp.adoc

[id="images-registry-mirroring-delete_{context}"]
= Deleting an image mirror configuration

[role="_abstract"]
You can delete an image mirror configuration from a OpenShift Container Platform cluster with the {rosa-cli-first}.

[NOTE]
====
Delete operations require confirmation unless the `--yes` or `--y` argument is used.
====

.Procedure

. Run the following command to delete an image mirror configuration from a OpenShift Container Platform cluster:
+
[source,terminal]
----
$ rosa delete image-mirror [arguments]
----
+
.Arguments
[cols="30,70"]
|===
|Option |Definition

|--cluster
|Required: The name or ID (string) of the cluster that the image mirror configuration will be deleted from.
|--id
|Required: ID of the image mirror configuration to delete.
|`--yes`, `-y`
|Optional: Automatically answers "yes" to confirm deletion.
|--profile
|Optional: Use a specific AWS profile from your credential file.
|--region
|Optional: Use a specific AWS region, overriding the AWS_REGION environment variable.

|===
+
.Examples
Deletes an image mirror configuration without a confirmation prompt.
+
[source,terminal]
----
$ rosa delete image-mirror --cluster=mycluster abc123def456 --yes
----
+
.Example Output
[source,terminal]
----
I: Image mirror 'abc123def456' has been deleted from cluster 'mycluster'
----

. Run the following command to deletes an image mirror configuration with a confirmation prompt:
+
[source,terminal]
----
$ rosa delete image-mirror --cluster=mycluster --id=abc123def456
----

[role="_additional-resources"]
== Additional resources
* About IAM resources
