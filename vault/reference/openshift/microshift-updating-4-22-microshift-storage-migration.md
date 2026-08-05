---
title: "Updating existing Kubernetes storage objects"
type: reference
domain: openshift
slug: microshift-updating-4-22-microshift-storage-migration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_updating/microshift-storage-migration
version: 4.22
family: microshift_updating
documentKind: "Documentation"
---

# Updating existing Kubernetes storage objects

[id="microshift-storage-migration"]
= Updating existing Kubernetes storage objects

[role="_abstract"]
To update existing objects to their latest version without recreating them, use storage version migration in {microshift-short}. By creating a `StorageVersionMigration` custom resource (CR), you request the Kube Storage Version Migrator embedded controller to handle the transition automatically.

Either you or a controller can create a `StorageVersionMigration` custom resource (CR) that requests a migration through the Migrator Controller.

// Module included in the following assemblies:
//
// * microshift_updating/microshift-storage-migration.adoc

[id="microshift-updating-stored-data-to-latest-storage-version_{context}"]
= Updating stored data to the latest storage version

[role="_abstract"]
To update stored data to the latest Kubernetes storage version, perform a storage migration.

The procedure shows an example of converting existing objects on the `v1beta1` version to the current version, such as `v1beta2`, to ensure compatibility with the cluster APIs.

.Procedure

* Either you or any controller that has support for the `StorageVersionMigration` API must trigger a migration request. Use the following example request for reference:
+
.Example request
[source,terminal]
----
apiVersion: migration.k8s.io/v1alpha1
kind: StorageVersionMigration
metadata:
  name: v1beta1
spec:
  resource:
    group: example.storage.k8s.io
    resource: volumeclasses
    version: v1alpha1
# ...
----
+
where:
+
`resource.resource`:: Specifies the plural name of the resource.
`resource.version`:: Specifies the version to update to.

.Verification

* To monitor the progress of the update, review the status of the `StorageVersionMigration` custom resource (CR).

[NOTE]
====
A migration fails when you misname a group or resource. Incompatible versions between the previous and latest versions can also cause a migration to fail.
====
