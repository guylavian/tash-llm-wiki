---
title: "Configuring the registry for AWS user-provisioned infrastructure"
type: reference
domain: openshift
slug: registry-4-22-configuring-registry-storage-aws-user-infrastructure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-storage-aws-user-infrastructure
version: 4.22
family: registry
documentKind: "Documentation"
---

# Configuring the registry for AWS user-provisioned infrastructure

[id="configuring-registry-storage-aws-user-infrastructure"]
= Configuring the registry for AWS user-provisioned infrastructure

[role="_abstract"]
Save your container images to a durable storage location by configuring the built-in image registry to use dedicated {aws-short} storage. This setup provides persistent scalable storage for your registry, separate from ephemeral cluster storage.

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage-aws-user-infrastructure.adoc

[id="registry-operator-config-resources-secret-aws_{context}"]
= Configuring a secret for the Image Registry Operator

[role="_abstract"]
In addition to the `configs.imageregistry.operator.openshift.io` and ConfigMap
resources, configuration is provided to the Operator by a separate secret
resource located within the `openshift-image-registry` namespace.

The `image-registry-private-configuration-user` secret provides
credentials needed for storage access and management. It overrides the default
credentials used by the Operator, if default credentials were found.

For S3 on AWS storage, the secret is expected to contain two keys:

* `REGISTRY_STORAGE_S3_ACCESSKEY`
* `REGISTRY_STORAGE_S3_SECRETKEY`

.Procedure

* Create an OpenShift Container Platform secret that contains the required keys.
+
[source,terminal]
----
$ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_S3_ACCESSKEY=myaccesskey --from-literal=REGISTRY_STORAGE_S3_SECRETKEY=mysecretkey --namespace openshift-image-registry
----

// Undefine the attribute to catch any errors at the end

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * registry/configuring_registry_storage-aws-user-infrastructure.adoc

[id="registry-configuring-storage-aws-user-infra_{context}"]
= Configuring registry storage for AWS with user-provisioned infrastructure

[role="_abstract"]
During installation, your cloud credentials are sufficient to create an Amazon S3 bucket and the Registry Operator will automatically configure storage.

If the Registry Operator cannot create an S3 bucket and automatically configure storage, you can create an S3 bucket and configure storage with the following procedure.

[WARNING]
====
To secure your registry images in AWS, block public access
to the S3 bucket.
====

.Prerequisites

* You have a cluster on AWS with user-provisioned infrastructure.
* For Amazon S3 storage, the secret is expected to contain two keys:
** `REGISTRY_STORAGE_S3_ACCESSKEY`
** `REGISTRY_STORAGE_S3_SECRETKEY`

.Procedure

. Set up a Bucket Lifecycle Policy
to abort incomplete multipart uploads that are one day old.

. Fill in the storage configuration in
`configs.imageregistry.operator.openshift.io/cluster`:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io/cluster
----
+
.Example configuration
[source,yaml]
----
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  storage:
    s3:
      bucket: <bucket_name>
      region: <region_name>
----

// Module included in the following assemblies:
//
// * registry/configuring-registry-storage-aws-user-infrastructure.adoc

[id="registry-operator-configuration-resource-overview-aws-s3_{context}"]
= Image Registry Operator configuration parameters for AWS S3

[role="_abstract"]
The following configuration parameters are available for AWS S3 registry storage.

The image registry `spec.storage.s3` configuration parameter holds the information to configure the registry to use the AWS S3 service for back-end storage. See the S3 storage driver documentation for more information.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`bucket`
|Bucket is the bucket name in which you want to store the registry's data.
It is optional and is generated if not provided.

|`chunkSizeMiB`
|ChunkSizeMiB is the size of the multipart upload chunks of the S3 API.
The default is `10` MiB with a minimum of `5` MiB.

|`region`
|Region is the AWS region in which your bucket exists. It is optional and is
set based on the installed AWS Region.

|`regionEndpoint`
|RegionEndpoint is the endpoint for S3 compatible storage services.
It is optional and defaults based on the Region that is provided.

|`virtualHostedStyle`
|VirtualHostedStyle enables using S3 virtual hosted style bucket paths with a custom RegionEndpoint. It is optional and defaults to false.

Set this parameter to deploy OpenShift Container Platform to hidden regions.

|`encrypt`
|Encrypt specifies whether or not the registry stores the image in encrypted format.
It is optional and defaults to false.

|`keyID`
|KeyID is the KMS key ID to use for encryption. It is optional. Encrypt must be
true, or this parameter is ignored.

|`cloudFront`
|CloudFront configures Amazon Cloudfront as the storage middleware in a registry.
It is optional.

|`trustedCA`
|The namespace for the config map referenced by `trustedCA` is `openshift-config`. The key for the bundle in the config map is `ca-bundle.crt`. It is optional.
|===

[NOTE]
====
When the value of the `regionEndpoint` parameter is configured to a URL of a Rados Gateway, an explicit port must not be specified. For example:
[source,yaml]
----
regionEndpoint: http://rook-ceph-rgw-ocs-storagecluster-cephobjectstore.openshift-storage.svc.cluster.local
----
====
