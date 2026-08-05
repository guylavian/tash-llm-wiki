---
title: "Configuring the registry for {gcp-short} user-provisioned infrastructure"
type: reference
domain: openshift
slug: registry-4-22-configuring-registry-storage-gcp-user-infrastructure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-storage-gcp-user-infrastructure
version: 4.22
family: registry
documentKind: "Documentation"
---

# Configuring the registry for {gcp-short} user-provisioned infrastructure

[id="configuring-registry-storage-gcp-user-infrastructure"]
= Configuring the registry for {gcp-short} user-provisioned infrastructure

[role="_abstract"]
Save your container images to a durable storage location by configuring the built-in image registry to use dedicated {gcp-short} storage. This setup provides persistent scalable storage for your registry, separate from ephemeral cluster storage.

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage-gcp-user-infrastructure.adoc

[id="registry-operator-config-resources-secret-gcp_{context}"]
= Configuring a secret for the Image Registry Operator

[role="_abstract"]
In addition to the `configs.imageregistry.operator.openshift.io` and ConfigMap
resources, configuration is provided to the Operator by a separate secret
resource located within the `openshift-image-registry` namespace.

The `image-registry-private-configuration-user` secret provides
credentials needed for storage access and management. It overrides the default
credentials used by the Operator, if default credentials were found.

For GCS on {gcp-short} storage, the secret is expected to contain one key whose value is the
contents of a credentials file provided by {gcp-short}:

* `REGISTRY_STORAGE_GCS_KEYFILE`

.Procedure

* Create an OpenShift Container Platform secret that contains the required keys.
+
[source,terminal]
----
$ oc create secret generic image-registry-private-configuration-user --from-file=REGISTRY_STORAGE_GCS_KEYFILE=<path_to_keyfile> --namespace openshift-image-registry
----

// Undefine the attribute to catch any errors at the end

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage-gcp-user-infrastructure.adoc

[id="registry-configuring-storage-gcp-user-infra_{context}"]
= Configuring the registry storage for {gcp-short} with user-provisioned infrastructure

[role="_abstract"]
If the Registry Operator cannot create a {gcp-first} bucket, you must set up the storage medium manually and configure the settings in the registry custom resource (CR).

.Prerequisites

* A cluster on {gcp-short} with user-provisioned infrastructure.
* To configure registry storage for {gcp-short}, you need to provide Registry Operator
cloud credentials.
* For GCS on {gcp-short} storage, the secret is expected to contain one key whose value is the
contents of a credentials file provided by {gcp-short}:
** `REGISTRY_STORAGE_GCS_KEYFILE`

[WARNING]
====
You can secure your registry images that use a {gcp-full} Storage bucket by setting public access prevention.
====

.Procedure

. Set up an Object Lifecycle Management policy to abort incomplete multipart uploads that are one day old.

. Fill in the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`:
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
    gcs:
      bucket: <bucket_name>
      projectID: <project_id>
      region: <region_name>
----

// Module included in the following assemblies:
//
// * openshift_images/configuring-registry-operator.adoc

[id="registry-operator-configuration-resource-overview-gcp-gcs_{context}"]
= Image Registry Operator configuration parameters for {gcp-short} GCS

[role="_abstract"]
The following parameters configure are available to configure your {gcp-short} GCS registry storage.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`bucket`
|Bucket is the bucket name in which you want to store the registry's data.
It is optional and is generated if not provided.

|`region`
|Region is the GCS location in which your bucket exists. It is optional and is
set based on the installed GCS Region.

|`projectID`
|ProjectID is the Project ID of the {gcp-short} project that this bucket should be
associated with. It is optional.

|`keyID`
|KeyID is the KMS key ID to use for encryption. It is optional because
buckets are encrypted by default on {gcp-short}. This allows for the use of a custom
encryption key.

|===
