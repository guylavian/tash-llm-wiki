---
title: "Working with different Kubernetes API versions on the same cluster"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-different-kubernetes-api-versions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-different-kubernetes-api-versions
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Working with different Kubernetes API versions on the same cluster

[id="oadp-different-kubernetes-api-versions"]
= Working with different Kubernetes API versions on the same cluster

[role="_abstract"]
Manage different Kubernetes API versions on your cluster during backup and restore operations. Enabling Velero to back up all supported API group versions helps you maintain compatibility when moving resources to a new destination cluster.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-advanced-topics/oadp-different-kubernetes-api-versions.adoc

[id="oadp-checking-api-group-versions_{context}"]
= Listing the Kubernetes API group versions on a cluster

[role="_abstract"]
Identify the preferred Kubernetes API group versions on your source cluster. This helps you select the correct API version when multiple API versions are available for a single API.

A source cluster might offer multiple versions of an API, where one of these versions is the preferred API version. For example, a source cluster with an API named `Example` might be available in the `example.com/v1` and `example.com/v1beta2` API groups.

If you use Velero to back up and restore such a source cluster, Velero backs up only the version of that resource that uses the preferred version of its Kubernetes API.

To return to the above example, if `example.com/v1` is the preferred API, then Velero only backs up the version of a resource that uses `example.com/v1`. Moreover, the target cluster needs to have `example.com/v1` registered in its set of available API resources in order for Velero to restore the resource on the target cluster.

Therefore, you need to generate a list of the Kubernetes API group versions on your target cluster to be sure the preferred API version is registered in its set of available API resources.

.Procedure

* Enter the following command:
+
[source,terminal]
----
$ oc api-resources
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-advanced-topics/oadp-different-kubernetes-api-versions.adoc

[id="oadp-about-enable-api-group-versions_{context}"]
= About Enable API Group Versions

[role="_abstract"]
Enable the API Group Versions feature to back up all supported Kubernetes API versions on your cluster, rather than just the preferred one. This helps you maintain complete API compatibility when restoring data to a destination cluster.

By default, Velero only backs up resources that use the preferred version of the Kubernetes API. However, Velero also includes the Enable API Group Versions feature that overcomes this limitation. When enabled on the source cluster, this feature causes Velero to back up _all_ Kubernetes API group versions that are supported on the cluster, not only the preferred one. After the versions are stored in the backup .tar file, they are available to be restored on the destination cluster.

For example, a source cluster with an API named `Example` might be available in the `example.com/v1` and `example.com/v1beta2` API groups, with `example.com/v1` being the preferred API.

Without the Enable API Group Versions feature enabled, Velero backs up only the preferred API group version for `Example`, which is `example.com/v1`. With the feature enabled, Velero also backs up `example.com/v1beta2`.

When the Enable API Group Versions feature is enabled on the destination cluster, Velero selects the version to restore on the basis of the order of priority of API group versions.

[NOTE]
====
Enable API Group Versions is still in beta.
====

Velero uses the following algorithm to assign priorities to API versions, with `1` as the top priority:

. Preferred version of the _destination_ cluster
. Preferred version of the source_ cluster
. Common non-preferred supported version with the highest Kubernetes version priority

[role="_additional-resources"]
.Additional resources
* Enable API Group Versions Feature

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-advanced-topics/oadp-different-kubernetes-api-versions.adoc

[id="oadp-using-enable-api-group-versions_{context}"]
= Using Enable API Group Versions

[role="_abstract"]
Configure the `EnableAPIGroupVersions` feature flag to back up all Kubernetes API group versions that are supported on a cluster, not only the preferred one. This helps you maintain compatibility across different API groups in your cluster.

[NOTE]
====
Enable API Group Versions is still in beta.
====

.Procedure

* Configure the `EnableAPIGroupVersions` feature flag:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/vialpha1
kind: DataProtectionApplication
...
spec:
  configuration:
    velero:
      featureFlags:
      - EnableAPIGroupVersions
----

[role="_additional-resources"]
.Additional resources
* Enable API Group Versions Feature
