---
title: "Manual mode with short-term credentials for components"
type: reference
domain: openshift
slug: authentication-4-22-cco-short-term-creds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/cco-short-term-creds
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Manual mode with short-term credentials for components

[id="cco-short-term-creds"]
= Manual mode with short-term credentials for components

During installation, you can configure the Cloud Credential Operator (CCO) to operate in manual mode and use the CCO utility (`ccoctl`) to implement short-term security credentials for individual components that are created and managed outside the OpenShift Container Platform cluster.

[NOTE]
====
This credentials strategy is supported for {aws-first}, {gcp-first}, and global {azure-full} only.

For {aws-short} and {gcp-short} clusters, you must configure your cluster to use this strategy during installation of a new OpenShift Container Platform cluster.
You cannot configure an existing {aws-short} or {gcp-short} cluster that uses a different credentials strategy to use this feature.

If you did not configure your {azure-short} cluster to use {entra-first} during installation, you can enable this authentication method on an existing cluster.
====

//todo: Should provide some more info about the benefits of this here as well. Note: Azure is not yet limited-priv, but still gets the benefit of not storing root creds on the cluster and some sort of time-based rotation

Cloud providers use different terms for their implementation of this authentication method.

.Short-term credentials provider terminology
|====
|Cloud provider |Provider nomenclature

|{aws-first}
|{aws-short} {sts-first}

|{gcp-first}
|{gcp-wid-short}

|Global Microsoft Azure
|{entra-first}

|====

[id="cco-short-term-creds-aws_{context}"]
== {aws-short} {sts-full}

In manual mode with {sts-first}, the individual OpenShift Container Platform cluster components use the {aws-short} {sts-short} to assign components IAM roles that provide short-term, limited-privilege security credentials. These credentials are associated with IAM roles that are specific to each component that makes {aws-short} API calls.

[role="_additional-resources"]
.Additional resources
* Configuring an {aws-short} cluster to use short-term credentials

//AWS Security Token Service authentication process
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-auth-flow-aws_{context}"]
= AWS Security Token Service authentication process

The AWS Security Token Service (STS) and the `AssumeRole` API action allow pods to retrieve access keys that are defined by an IAM role policy.

The OpenShift Container Platform cluster includes a Kubernetes service account signing service. This service uses a private key to sign service account JSON web tokens (JWT). A pod that requires a service account token requests one through the pod specification. When the pod is created and assigned to a node, the node retrieves a signed service account from the service account signing service and mounts it onto the pod.

Clusters that use STS contain an IAM role ID in their Kubernetes configuration secrets. Workloads assume the identity of this IAM role ID. The signed service account token issued to the workload aligns with the configuration in AWS, which allows AWS STS to grant access keys for the specified IAM role to the workload.

AWS STS grants access keys only for requests that include service account tokens that meet the following conditions:

* The token name and namespace match the service account name and namespace.

* The token is signed by a key that matches the public key.

The public key pair for the service account signing key used by the cluster is stored in an AWS S3 bucket. AWS STS federation validates that the service account token signature aligns with the public key stored in the S3 bucket.

[id="cco-short-term-creds-auth-flow-aws-diagram_{context}"]
== Authentication flow for AWS STS

The following diagram illustrates the authentication flow between AWS and the OpenShift Container Platform cluster when using AWS STS.

* _Token signing_ is the Kubernetes service account signing service on the OpenShift Container Platform cluster.
* The _Kubernetes service account_ in the pod is the signed service account token.

.AWS Security Token Service authentication flow
image::347_OpenShift_credentials_with_STS_updates_0623_AWS.png[Detailed authentication flow between AWS and the cluster when using AWS STS]

Requests for new and refreshed credentials are automated by using an appropriately configured AWS IAM OpenID Connect (OIDC) identity provider combined with AWS IAM roles. Service account tokens that are trusted by AWS IAM are signed by OpenShift Container Platform and can be projected into a pod and used for authentication.

[id="cco-short-term-creds-auth-flow-aws-refresh-policy_{context}"]
== Token refreshing for AWS STS

The signed service account token that a pod uses expires after a period of time. For clusters that use AWS STS, this time period is 3600 seconds, or one hour.

The kubelet on the node that the pod is assigned to ensures that the token is refreshed. The kubelet attempts to rotate a token when it is older than 80 percent of its time to live.

[id="cco-short-term-creds-auth-flow-aws-oidc_{context}"]
== OpenID Connect requirements for AWS STS

You can store the public portion of the encryption keys for your OIDC configuration in a public or private S3 bucket.

The OIDC spec requires the use of HTTPS. AWS services require a public endpoint to expose the OIDC documents in the form of JSON web key set (JWKS) public keys. This allows AWS services to validate the bound tokens signed by Kubernetes and determine whether to trust certificates. As a result, both S3 bucket options require a public HTTPS endpoint and private endpoints are not supported.

To use AWS STS, the public AWS backbone for the AWS STS service must be able to communicate with a public S3 bucket or a private S3 bucket with a public CloudFront endpoint. You can choose which type of bucket to use when you process `CredentialsRequest` objects during installation:

* By default, the CCO utility (`ccoctl`) stores the OIDC configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint.

* As an alternative, you can have the `ccoctl` utility store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL.

//AWS component secret formats
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-format-aws_{context}"]
= AWS component secret formats

Using manual mode with the AWS Security Token Service (STS) changes the content of the AWS credentials that are provided to individual OpenShift Container Platform components. Compare the following secret formats:

.AWS secret format using long-term credentials

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace> <1>
  name: <target_secret_name> <2>
data:
  aws_access_key_id: <base64_encoded_access_key_id>
  aws_secret_access_key: <base64_encoded_secret_access_key>
----
<1> The namespace for the component.
<2> The name of the component secret.

.AWS secret format using AWS STS

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace> <1>
  name: <target_secret_name> <2>
stringData:
  credentials: |-
    [default]
    sts_regional_endpoints = regional
    role_name: <operator_role_name> <3>
    web_identity_token_file: <path_to_token> <4>
----
<1> The namespace for the component.
<2> The name of the component secret.
<3> The IAM role for the component.
<4> The path to the service account token inside the pod. By convention, this is `/var/run/secrets/openshift/serviceaccount/token` for OpenShift Container Platform components.

//AWS component secret permissions requirements
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-component-permissions-aws_{context}"]
= AWS component secret permissions requirements

OpenShift Container Platform components require the following permissions. These values are in the `CredentialsRequest` custom resource (CR) for each component.

[NOTE]
====
These permissions apply to all resources. Unless specified, there are no request conditions on these permissions.
====

[cols="a,a,a"]
|====
|Component |Custom resource |Required permissions for services

|{cluster-capi-operator}
|`openshift-cluster-api-aws`
|**EC2**

* `ec2:CreateTags`
* `ec2:DescribeAvailabilityZones`
* `ec2:DescribeDhcpOptions`
* `ec2:DescribeImages`
* `ec2:DescribeInstances`
* `ec2:DescribeInternetGateways`
* `ec2:DescribeSecurityGroups`
* `ec2:DescribeSubnets`
* `ec2:DescribeVpcs`
* `ec2:DescribeNetworkInterfaces`
* `ec2:DescribeNetworkInterfaceAttribute`
* `ec2:ModifyNetworkInterfaceAttribute`
* `ec2:RunInstances`
* `ec2:TerminateInstances`

**Elastic load balancing**

* `elasticloadbalancing:DescribeLoadBalancers`
* `elasticloadbalancing:DescribeTargetGroups`
* `elasticloadbalancing:DescribeTargetHealth`
* `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
* `elasticloadbalancing:RegisterTargets`
* `elasticloadbalancing:DeregisterTargets`

**Identity and Access Management (IAM)**

* `iam:PassRole`
* `iam:CreateServiceLinkedRole`

**Key Management Service (KMS)**

* `kms:Decrypt`
* `kms:Encrypt`
* `kms:GenerateDataKey`
* `kms:GenerateDataKeyWithoutPlainText`
* `kms:DescribeKey`
* `kms:RevokeGrant`^[1]^
* `kms:CreateGrant` ^[1]^
* `kms:ListGrants` ^[1]^

|Machine API Operator
|`openshift-machine-api-aws`
|**EC2**

* `ec2:CreateTags`
* `ec2:DescribeAvailabilityZones`
* `ec2:DescribeDhcpOptions`
* `ec2:DescribeImages`
* `ec2:DescribeInstances`
* `ec2:DescribeInstanceTypes`
* `ec2:DescribeInternetGateways`
* `ec2:DescribeSecurityGroups`
* `ec2:DescribeRegions`
* `ec2:DescribeSubnets`
* `ec2:DescribeVpcs`
* `ec2:RunInstances`
* `ec2:TerminateInstances`

**Elastic load balancing**

* `elasticloadbalancing:DescribeLoadBalancers`
* `elasticloadbalancing:DescribeTargetGroups`
* `elasticloadbalancing:DescribeTargetHealth`
* `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
* `elasticloadbalancing:RegisterTargets`
* `elasticloadbalancing:DeregisterTargets`

**Identity and Access Management (IAM)**

* `iam:PassRole`
* `iam:CreateServiceLinkedRole`

**Key Management Service (KMS)**

* `kms:Decrypt`
* `kms:Encrypt`
* `kms:GenerateDataKey`
* `kms:GenerateDataKeyWithoutPlainText`
* `kms:DescribeKey`
* `kms:RevokeGrant`^[1]^
* `kms:CreateGrant` ^[1]^
* `kms:ListGrants` ^[1]^

|Cloud Credential Operator
|`cloud-credential-operator-iam-ro`
|**Identity and Access Management (IAM)**

* `iam:GetUser`
* `iam:GetUserPolicy`
* `iam:ListAccessKeys`

|Cluster Image Registry Operator
|`openshift-image-registry`
|**S3**

* `s3:CreateBucket`
* `s3:DeleteBucket`
* `s3:PutBucketTagging`
* `s3:GetBucketTagging`
* `s3:PutBucketPublicAccessBlock`
* `s3:GetBucketPublicAccessBlock`
* `s3:PutEncryptionConfiguration`
* `s3:GetEncryptionConfiguration`
* `s3:PutLifecycleConfiguration`
* `s3:GetLifecycleConfiguration`
* `s3:GetBucketLocation`
* `s3:ListBucket`
* `s3:GetObject`
* `s3:PutObject`
* `s3:DeleteObject`
* `s3:ListBucketMultipartUploads`
* `s3:AbortMultipartUpload`
* `s3:ListMultipartUploadParts`

|Ingress Operator
|`openshift-ingress`
|**Elastic load balancing**

* `elasticloadbalancing:DescribeLoadBalancers`

**Route 53**

* `route53:ListHostedZones`
* `route53:ListTagsForResources`
* `route53:ChangeResourceRecordSets`

**Tag**

* `tag:GetResources`

**Security Token Service (STS)**

* `sts:AssumeRole`

|Cluster Network Operator
|`openshift-cloud-network-config-controller-aws`
|**EC2**

* `ec2:DescribeInstances`
* `ec2:DescribeInstanceStatus`
* `ec2:DescribeInstanceTypes`
* `ec2:UnassignPrivateIpAddresses`
* `ec2:AssignPrivateIpAddresses`
* `ec2:UnassignIpv6Addresses`
* `ec2:AssignIpv6Addresses`
* `ec2:DescribeSubnets`
* `ec2:DescribeNetworkInterfaces`

|AWS Elastic Block Store CSI Driver Operator
|`aws-ebs-csi-driver-operator`
|**EC2**

* `ec2:AttachVolume`
* `ec2:CreateSnapshot`
* `ec2:CreateTags`
* `ec2:CreateVolume`
* `ec2:DeleteSnapshot`
* `ec2:DeleteTags`
* `ec2:DeleteVolume`
* `ec2:DescribeInstances`
* `ec2:DescribeSnapshots`
* `ec2:DescribeTags`
* `ec2:DescribeVolumes`
* `ec2:DescribeVolumesModifications`
* `ec2:DetachVolume`
* `ec2:ModifyVolume`
* `ec2:DescribeAvailabilityZones`
* `ec2:EnableFastSnapshotRestores`

**Key Management Service (KMS)**

* `kms:ReEncrypt*`
* `kms:Decrypt`
* `kms:Encrypt`
* `kms:GenerateDataKey`
* `kms:GenerateDataKeyWithoutPlainText`
* `kms:DescribeKey`
* `kms:RevokeGrant`^[1]^
* `kms:CreateGrant` ^[1]^
* `kms:ListGrants` ^[1]^

|====
[.small]
--
1. Request condition: `kms:GrantIsForAWSResource: true`
--

//OLM-managed Operator support for authentication with AWS STS
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-aws-olm_{context}"]
= OLM-managed Operator support for authentication with {aws-short} {sts-short}

Certain Operators managed by the Operator Lifecycle Manager (OLM) on {aws-short} clusters can use manual mode with {sts-short}.
These Operators authenticate with limited-privilege, short-term credentials that are managed outside the cluster.
To determine if an Operator supports authentication with {aws-short} {sts-short}, see the Operator description in the software catalog.

[role="_additional-resources"]
.Additional resources
* CCO-based workflow for OLM-managed Operators with {aws-short} {sts-short}

// Content stub for later addition:
// Application support for AWS STS service account tokens
// Extra context so module can be reused within assembly (unset in module)
// Attributes used in module with cloud-specific values (unset in module)
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-workloads_{context}"]
= Application support for {cloud-auth-short} service account tokens

Applications in customer workloads on OpenShift Container Platform clusters that use {cloud-auth-first} can authenticate by using {cloud-auth-short}.
To use this authentication method with your applications, you must complete configuration steps on the cloud provider console and your OpenShift Container Platform cluster.

// Unsetting attributes defined in authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc above include:: line

[role="_additional-resources"]
.Additional resources
* xr3f:../../nodes/pods/nodes-pods-short-term-auth.adoc#nodes-pods-short-term-auth-configuring-aws_nodes-pods-short-term-auth[Configuring {aws-short} {sts-short} authentication for pods on {aws-short}]

[id="cco-short-term-creds-gcp_{context}"]
== {gcp-wid-short}

In manual mode with {gcp-wid-short}, the individual OpenShift Container Platform cluster components use the {gcp-short} workload identity provider to allow components to impersonate {gcp-short} service accounts using short-term, limited-privilege credentials.

[role="_additional-resources"]
.Additional resources
* Configuring a {gcp-short} cluster to use short-term credentials

//GCP Workload Identity authentication process
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-auth-flow-gcp_{context}"]
= {gcp-short} Workload Identity authentication process

Requests for new and refreshed credentials are automated by using an appropriately configured OpenID Connect (OIDC) identity provider combined with IAM service accounts. Service account tokens that are trusted by {gcp-short} are signed by OpenShift Container Platform and can be projected into a pod and used for authentication. Tokens are refreshed after one hour.

The following diagram details the authentication flow between {gcp-short} and the OpenShift Container Platform cluster when using {gcp-short} Workload Identity.

.{gcp-short} Workload Identity authentication flow
image::347_OpenShift_credentials_with_STS_updates_0623_GCP.png[Detailed authentication flow between {gcp-short} and the cluster when using {gcp-short} Workload Identity]

//GCP component secret formats
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-format-gcp_{context}"]
= {gcp-short} component secret formats

Using manual mode with {gcp-short} Workload Identity changes the content of the {gcp-short} credentials that are provided to individual OpenShift Container Platform components. Compare the following secret content:

.{gcp-short} secret format

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace> <1>
  name: <target_secret_name> <2>
data:
  service_account.json: <service_account> <3>
----
<1> The namespace for the component.
<2> The name of the component secret.
<3> The Base64 encoded service account.

.Content of the Base64 encoded `service_account.json` file using long-term credentials

[source,json]
----
{
   "type": "service_account", <1>
   "project_id": "<project_id>",
   "private_key_id": "<private_key_id>",
   "private_key": "<private_key>", <2>
   "client_email": "<client_email_address>",
   "client_id": "<client_id>",
   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
   "token_uri": "https://oauth2.googleapis.com/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/<client_email_address>"
}
----
<1> The credential type is `service_account`.
<2> The private RSA key that is used to authenticate to {gcp-short}. This key must be kept secure and is not rotated.

.Content of the Base64 encoded `service_account.json` file using {gcp-short} Workload Identity

[source,json]
----
{
   "type": "external_account", <1>
   "audience": "//iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/test-pool/providers/test-provider", <2>
   "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
   "token_url": "https://sts.googleapis.com/v1/token",
   "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/<client_email_address>:generateAccessToken", <3>
   "credential_source": {
      "file": "<path_to_token>", <4>
      "format": {
         "type": "text"
      }
   }
}
----
<1> The credential type is `external_account`.
<2> The target audience is the {gcp-short} Workload Identity provider.
<3> The resource URL of the service account that can be impersonated with these credentials.
<4> The path to the service account token inside the pod. By convention, this is `/var/run/secrets/openshift/serviceaccount/token` for OpenShift Container Platform components.

//GCP component secret permissions requirements
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-component-permissions-gcp_{context}"]
= {gcp-short} component secret permissions requirements

[role="_abstract"]
OpenShift Container Platform components require the following permissions. These values are in the `CredentialsRequest` custom resource (CR) for each component.

[NOTE]
====
These permissions apply to all resources. Unless specified, there are no request conditions on these permissions.
====

[cols="a,a,a"]
|====
|Component |Custom resource |Required permissions for services

|Cloud Controller Manager Operator
|`openshift-gcp-ccm`
|Compute Engine

* `compute.addresses.create`
* `compute.addresses.delete`
* `compute.addresses.get`
* `compute.addresses.list`
* `compute.firewalls.create`
* `compute.firewalls.delete`
* `compute.firewalls.get`
* `compute.firewalls.update`
* `compute.forwardingRules.create`
* `compute.forwardingRules.delete`
* `compute.forwardingRules.get`
* `compute.healthChecks.create`
* `compute.healthChecks.delete`
* `compute.healthChecks.get`
* `compute.healthChecks.update`
* `compute.httpHealthChecks.create`
* `compute.httpHealthChecks.delete`
* `compute.httpHealthChecks.get`
* `compute.httpHealthChecks.update`
* `compute.instanceGroups.create`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.get`
* `compute.instanceGroups.update`
* `compute.instances.get`
* `compute.instances.use`
* `compute.regionBackendServices.create`
* `compute.regionBackendServices.delete`
* `compute.regionBackendServices.get`
* `compute.regionBackendServices.update`
* `compute.targetPools.addInstance`
* `compute.targetPools.create`
* `compute.targetPools.delete`
* `compute.targetPools.get`
* `compute.targetPools.removeInstance`
* `compute.zones.list`

|Cloud Credential Operator
|`cloud-credential-operator-gcp-ro-creds`
|Identity and Access Management (IAM)

* `iam.roles.get`
* `iam.serviceAccountKeys.list`
* `iam.serviceAccounts.get`

Resource Manager

* `resourcemanager.projects.get`
* `resourcemanager.projects.getIamPolicy`

Service Usage

* `serviceusage.services.list`

|Cluster Image Registry Operator
|`openshift-image-registry-gcs`
|Cloud Storage

* `storage.buckets.create`
* `storage.buckets.createTagBinding`
* `storage.buckets.delete`
* `storage.buckets.get`
* `storage.buckets.list`
* `storage.buckets.listEffectiveTags`
* `storage.objects.create`
* `storage.objects.delete`
* `storage.objects.get`
* `storage.objects.list`

Resource Manager

* `resourcemanager.tagValueBindings.create`
* `resourcemanager.tagValues.get`
* `resourcemanager.tagValues.list`

|Cluster Ingress Operator
|`openshift-ingress-gcp`
|Cloud DNS

* `dns.changes.create`
* `dns.resourceRecordSets.create`
* `dns.resourceRecordSets.delete`
* `dns.resourceRecordSets.list`
* `dns.resourceRecordSets.update`

|Cluster Network Operator
|`openshift-cloud-network-config-controller-gcp`
|Compute Engine

* `compute.instances.get`
* `compute.instances.updateNetworkInterface`
* `compute.subnetworks.get`
* `compute.subnetworks.use`
* `compute.zoneOperations.get`

|Cluster Storage Operator
|`openshift-gcp-pd-csi-driver-operator`
|Compute Engine

* `compute.instances.attachDisk`
* `compute.instances.detachDisk`
* `compute.instances.get`

This component also requires the following {gcp-short} predefined roles:

* `roles/compute.storageAdmin`
* `roles/iam.serviceAccountUser`
* `roles/resourcemanager.tagUser`

|Machine API Operator
|`openshift-machine-api-gcp`
|Compute Engine

* `compute.acceleratorTypes.get`
* `compute.acceleratorTypes.list`
* `compute.disks.create`
* `compute.disks.createTagBinding`
* `compute.disks.setLabels`
* `compute.globalOperations.get`
* `compute.globalOperations.list`
* `compute.healthChecks.useReadOnly`
* `compute.images.get`
* `compute.images.getFromFamily`
* `compute.images.useReadOnly`
* `compute.instanceGroups.create`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.get`
* `compute.instanceGroups.list`
* `compute.instanceGroups.update`
* `compute.instances.create`
* `compute.instances.createTagBinding`
* `compute.instances.delete`
* `compute.instances.get`
* `compute.instances.list`
* `compute.instances.setLabels`
* `compute.instances.setMetadata`
* `compute.instances.setServiceAccount`
* `compute.instances.setTags`
* `compute.instances.update`
* `compute.instances.use`
* `compute.machineTypes.get`
* `compute.machineTypes.list`
* `compute.projects.get`
* `compute.regionBackendServices.create`
* `compute.regionBackendServices.get`
* `compute.regionBackendServices.update`
* `compute.regions.get`
* `compute.regions.list`
* `compute.subnetworks.use`
* `compute.subnetworks.useExternalIp`
* `compute.targetPools.addInstance`
* `compute.targetPools.delete`
* `compute.targetPools.get`
* `compute.targetPools.removeInstance`
* `compute.zoneOperations.get`
* `compute.zoneOperations.list`
* `compute.zones.get`
* `compute.zones.list`

Identity and Access Management (IAM)

* `iam.serviceAccounts.actAs`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`

Resource Manager

* `resourcemanager.tagValues.get`
* `resourcemanager.tagValues.list`

Service Usage

* `serviceusage.quotas.get`
* `serviceusage.services.get`
* `serviceusage.services.list`

|====

//OLM-managed Operator support for authentication with GCP Workload Identity
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-gcp-olm_{context}"]
= OLM-managed Operator support for authentication with {gcp-wid-short}

Certain Operators managed by the Operator Lifecycle Manager (OLM) on {gcp-short} clusters can use manual mode with {gcp-wid-short}.
These Operators authenticate with limited-privilege, short-term credentials that are managed outside the cluster.
To determine if an Operator supports authentication with {gcp-wid-short}, see the Operator description in the software catalog.

[role="_additional-resources"]
.Additional resources
* CCO-based workflow for OLM-managed Operators with {gcp-wid-first}

// Application support for GCP Workload Identity service account tokens
// Extra context so module can be reused within assembly (unset in module)
// Attributes used in module with cloud-specific values (unset in module)

[role="_additional-resources"]
.Additional resources
* Configuring {gcp-wid-short} authentication for applications on {gcp-short}

[id="cco-short-term-creds-azure_{context}"]
== {entra-first}

In manual mode with {entra-first}, the individual OpenShift Container Platform cluster components use the {entra-short} provider to assign components short-term security credentials.

[role="_additional-resources"]
.Additional resources
* Configuring a global {azure-first} cluster to use short-term credentials

//Microsoft Entra Workload ID authentication process
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-auth-flow-azure_{context}"]
= {entra-first} authentication process

The following diagram details the authentication flow between Azure and the OpenShift Container Platform cluster when using {entra-first}.

.{entra-short} authentication flow
image::347_OpenShift_credentials_with_STS_updates_1023_Azure.png[Detailed authentication flow between Azure and the cluster when using {entra-short}]

//Azure component secret formats
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-format-azure_{context}"]
= Azure component secret formats

Using manual mode with {entra-first} changes the content of the Azure credentials that are provided to individual OpenShift Container Platform components. Compare the following secret formats:

.Azure secret format using long-term credentials

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace> <1>
  name: <target_secret_name> <2>
data:
  azure_client_id: <client_id> <3>
  azure_client_secret: <client_secret> <4>
  azure_region: <region>
  azure_resource_prefix: <resource_group_prefix> <5>
  azure_resourcegroup: <resource_group_prefix>-rg <6>
  azure_subscription_id: <subscription_id>
  azure_tenant_id: <tenant_id>
type: Opaque
----
<1> The namespace for the component.
<2> The name of the component secret.
<3> The client ID of the Microsoft Entra ID identity that the component uses to authenticate.
<4> The component secret that is used to authenticate with Microsoft Entra ID for the `<client_id>` identity.
<5> The resource group prefix.
<6> The resource group. This value is formed by the `<resource_group_prefix>` and the suffix `-rg`.

.Azure secret format using {entra-first}

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace> <1>
  name: <target_secret_name> <2>
data:
  azure_client_id: <client_id> <3>
  azure_federated_token_file: <path_to_token_file> <4>
  azure_region: <region>
  azure_subscription_id: <subscription_id>
  azure_tenant_id: <tenant_id>
type: Opaque
----
<1> The namespace for the component.
<2> The name of the component secret.
<3> The client ID of the user-assigned managed identity that the component uses to authenticate.
<4> The path to the mounted service account token file.

//Azure component secret permissions requirements
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-component-permissions-azure_{context}"]
= Azure component secret permissions requirements

OpenShift Container Platform components require the following permissions. These values are in the `CredentialsRequest` custom resource (CR) for each component.

[cols="a,a,a"]
|====
|Component |Custom resource |Required permissions for services

|Cloud Controller Manager Operator
|`openshift-azure-cloud-controller-manager`
|* `Microsoft.Compute/virtualMachines/read`
* `Microsoft.Network/loadBalancers/read`
* `Microsoft.Network/loadBalancers/write`
* `Microsoft.Network/networkInterfaces/read`
* `Microsoft.Network/networkSecurityGroups/read`
* `Microsoft.Network/networkSecurityGroups/write`
* `Microsoft.Network/publicIPAddresses/join/action`
* `Microsoft.Network/publicIPAddresses/read`
* `Microsoft.Network/publicIPAddresses/write`

|{cluster-capi-operator}
|`openshift-cluster-api-azure`
|role: `Contributor` ^[1]^

|Machine API Operator
|`openshift-machine-api-azure`
|* `Microsoft.Compute/availabilitySets/delete`
* `Microsoft.Compute/availabilitySets/read`
* `Microsoft.Compute/availabilitySets/write`
* `Microsoft.Compute/diskEncryptionSets/read`
* `Microsoft.Compute/disks/delete`
* `Microsoft.Compute/galleries/images/versions/read`
* `Microsoft.Compute/skus/read`
* `Microsoft.Compute/virtualMachines/delete`
* `Microsoft.Compute/virtualMachines/extensions/delete`
* `Microsoft.Compute/virtualMachines/extensions/read`
* `Microsoft.Compute/virtualMachines/extensions/write`
* `Microsoft.Compute/virtualMachines/read`
* `Microsoft.Compute/virtualMachines/write`
* `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`
* `Microsoft.Network/applicationSecurityGroups/read`
* `Microsoft.Network/loadBalancers/backendAddressPools/join/action`
* `Microsoft.Network/loadBalancers/read`
* `Microsoft.Network/loadBalancers/write`
* `Microsoft.Network/networkInterfaces/delete`
* `Microsoft.Network/networkInterfaces/join/action`
* `Microsoft.Network/networkInterfaces/loadBalancers/read`
* `Microsoft.Network/networkInterfaces/read`
* `Microsoft.Network/networkInterfaces/write`
* `Microsoft.Network/networkSecurityGroups/read`
* `Microsoft.Network/networkSecurityGroups/write`
* `Microsoft.Network/publicIPAddresses/delete`
* `Microsoft.Network/publicIPAddresses/join/action`
* `Microsoft.Network/publicIPAddresses/read`
* `Microsoft.Network/publicIPAddresses/write`
* `Microsoft.Network/routeTables/read`
* `Microsoft.Network/virtualNetworks/delete`
* `Microsoft.Network/virtualNetworks/read`
* `Microsoft.Network/virtualNetworks/subnets/join/action`
* `Microsoft.Network/virtualNetworks/subnets/read`
* `Microsoft.Resources/subscriptions/resourceGroups/read`

|Cluster Image Registry Operator
|`openshift-image-registry-azure`
|**Data permissions**

* `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/delete`
* `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write`
* `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`
* `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action`
* `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/move/action`

**General permissions**

* `Microsoft.Storage/storageAccounts/blobServices/read`
* `Microsoft.Storage/storageAccounts/blobServices/containers/read`
* `Microsoft.Storage/storageAccounts/blobServices/containers/write`
* `Microsoft.Storage/storageAccounts/blobServices/generateUserDelegationKey/action`
* `Microsoft.Storage/storageAccounts/read`
* `Microsoft.Storage/storageAccounts/write`
* `Microsoft.Storage/storageAccounts/delete`
* `Microsoft.Storage/storageAccounts/listKeys/action`
* `Microsoft.Resources/tags/write`

|Ingress Operator
|`openshift-ingress-azure`
|* `Microsoft.Network/dnsZones/A/delete`
* `Microsoft.Network/dnsZones/A/write`
* `Microsoft.Network/privateDnsZones/A/delete`
* `Microsoft.Network/privateDnsZones/A/write`

|Cluster Network Operator
|`openshift-cloud-network-config-controller-azure`
|* `Microsoft.Network/networkInterfaces/read`
* `Microsoft.Network/networkInterfaces/write`
* `Microsoft.Compute/virtualMachines/read`
* `Microsoft.Network/virtualNetworks/read`
* `Microsoft.Network/virtualNetworks/subnets/join/action`
* `Microsoft.Network/loadBalancers/backendAddressPools/join/action`

|Azure File CSI Driver Operator
|`azure-file-csi-driver-operator`
|* `Microsoft.Network/networkSecurityGroups/join/action`
* `Microsoft.Network/virtualNetworks/subnets/read`
* `Microsoft.Network/virtualNetworks/subnets/write`
* `Microsoft.Storage/storageAccounts/delete`
* `Microsoft.Storage/storageAccounts/fileServices/read`
* `Microsoft.Storage/storageAccounts/fileServices/shares/delete`
* `Microsoft.Storage/storageAccounts/fileServices/shares/read`
* `Microsoft.Storage/storageAccounts/fileServices/shares/write`
* `Microsoft.Storage/storageAccounts/listKeys/action`
* `Microsoft.Storage/storageAccounts/read`
* `Microsoft.Storage/storageAccounts/write`

|Azure Disk CSI Driver Operator
|`azure-disk-csi-driver-operator`
|* `Microsoft.Compute/disks/*`
* `Microsoft.Compute/snapshots/*`
* `Microsoft.Compute/virtualMachineScaleSets/*/read`
* `Microsoft.Compute/virtualMachineScaleSets/read`
* `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/write`
* `Microsoft.Compute/virtualMachines/*/read`
* `Microsoft.Compute/virtualMachines/write`
* `Microsoft.Resources/subscriptions/resourceGroups/read`

|====
[.small]
--
1. This component requires a role rather than a set of permissions.
--

//OLM-managed Operator support for authentication with Microsoft Entra Workload ID
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

[id="cco-short-term-creds-azure-olm_{context}"]
= OLM-managed Operator support for authentication with {entra-first}

Certain Operators managed by the Operator Lifecycle Manager (OLM) on {azure-short} clusters can use manual mode with {entra-first}.
These Operators authenticate with short-term credentials that are managed outside the cluster.
To determine if an Operator supports authentication with {entra-short}, see the Operator description in the software catalog.

[role="_additional-resources"]
.Additional resources
* CCO-based workflow for OLM-managed Operators with {entra-first}

// Content stub for later addition:
// Application support for Microsoft Entra Workload ID service account tokens
// Extra context so module can be reused within assembly (unset in module)
// Attributes used in module with cloud-specific values (unset in module)

[role="_additional-resources"]
.Additional resources
* xr3f:../../nodes/pods/nodes-pods-short-term-auth.adoc#nodes-pods-short-term-auth-configuring-azure_nodes-pods-short-term-auth[Configuring {entra-first} authentication for pods on {azure-short}]

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Configuring an {aws-short} cluster to use short-term credentials
* Configuring a {gcp-short} cluster to use short-term credentials
* Configuring a global {azure-first} cluster to use short-term credentials
* Preparing to update a cluster with manually maintained credentials
