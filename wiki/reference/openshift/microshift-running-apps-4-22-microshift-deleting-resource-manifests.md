---
title: "Deleting or updating Kustomize manifest resources"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-deleting-resource-manifests
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-deleting-resource-manifests
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Deleting or updating Kustomize manifest resources

[id="microshift-deleting-resource-manifests"]
= Deleting or updating Kustomize manifest resources

[role="_abstract"]
When creating new manifests in {microshift-short}, you can use manifest resource deletion to remove or update old objects, ensuring there are no conflicts or issues.

{microshift-short} supports the deletion of manifest resources in the following situations:

* Manifest removal: Manifests can be removed when you need to completely remove a resource from the node.
* Manifest upgrade: During an application upgrade, some resources might need to be removed while others are retained to preserve data.

[IMPORTANT]
====
Manifest files placed in the `delete` subdirectories are not automatically removed and require manual deletion. Only the resources listed in the manifest files placed in the delete subdirectories are deleted.
====

// Module included in the following assemblies:
//
// * microshift//running_applications/microshift-deleting-resource-manifests.adoc

[id="microshift-manifests-deletion-overview_{context}"]
= How manifest deletion works

[role="_abstract"]
By default, {microshift-short} searches for deletion manifests in the `delete` subdirectories within the manifests path. When a user places a manifest in these subdirectories, {microshift-short} removes the manifests when the system is started.

Read through the following to understand how manifests deletion works in {microshift-short}.

. Each time the system starts, before applying the manifests, {microshift-short} scans the following `delete` subdirectories within the configured manifests directory to identify the manifests that need to be deleted:

* `/usr/lib/microshift/manifests/delete`
* `/usr/lib/microshift/manifests.d/delete/*`
* `/etc/microshift/manifests/delete`
* `/etc/microshift/manifests.d/delete/*`

. {microshift-short} deletes the resources defined in the manifests found in the `delete` directories by running the equivalent of the `kubectl delete --ignore-not-found -k` command.

[id="microshift-examples-of-usecase_{context}"]
== Use cases for manifest resource deletion

The following sections explain the use case in which the manifest resource deletion is used.

// Module included in the following assemblies:
//
// * microshift//running_applications/microshift-deleting-resource-manifests.adoc

[id="microshift-manifests-removal-scenario-rpm_{context}"]
= Removing manifests for RPM systems

[role="_abstract"]
To remove a resource on RPM-based {microshift-short} systems, move the manifest into a `delete` subdirectory and restart {microshift-short} so the resource is deleted.

.Procedure

. Identify the manifest that needs to be placed in the `delete` subdirectories.
. Create the `delete` subdirectory in which the manifest will be placed by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo mkdir -p _<path_of_delete_directory>_
----
+
Replace `_<path_of_delete_directory>_` with one of the following valid directory paths: `/etc/microshift/manifests.d/delete`, `/etc/microshift/manifests/delete/`, `/usr/lib/microshift/manifests.d/delete`, or `/usr/lib/microshift/manifests/delete`.
. Move the manifest file into one of the `delete` subdirectories under the configured manifests directory by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ [sudo] mv _<path_of_manifests>_ _<path_of_delete_directory>_
----
+
where:

`_<path_of_manifests>_`:: Specifies the path of the manifest to be deleted, for example `/etc/microshift/manifests.d/010-SOME-MANIFEST`.
`_<path_of_delete_directory>_`:: Specifies one of the following valid directory paths: `/etc/microshift/manifests.d/delete`, `/etc/microshift/manifests/delete`, `/usr/lib/microshift/manifests.d/delete` or `/usr/lib/microshift/manifests/delete`.
. Restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----
. {microshift-short} detects and removes the resource after the manifest file is placed in the `delete` subdirectories.

// Module included in the following assemblies:
//
// * microshift/running_applications/microshift-deleting-resource-manifests.adoc

[id="microshift-manifests-removal-scenario-ostree_{context}"]
= Removing manifests for OSTree systems

[role="_abstract"]
On OSTree-based {microshift-short} systems, you can remove a resource by packaging the manifest in an RPM, adding it to a blueprint, and letting {microshift-short} process the `delete` directory.

[IMPORTANT]
====
For OSTree installation, the `delete` subdirectories are read-only.
====

.Procedure

. Identify the manifest that needs to be placed in the `delete` subdirectories.
. Package the manifest into an RPM. See Building the RPM package for the application for the procedure to package the manifest into an RPM.
. Add the packaged RPM to the blueprint file to install it into correct location. See Adding application RPMs to a blueprint for the procedure to add an RPM to a blueprint.

// Module included in the following assemblies:
//
// * microshift/running_applications/microshift-deleting-resource-manifests.adoc

[id="microshift-manifests-upgrade-scenario-rpm_{context}"]
= Upgrading manifests for RPM systems

[role="_abstract"]
To update resources while preserving data on RPM-based {microshift-short} systems, you can create new manifests for changes and deletions, and then move the deletion manifests into a `delete` subdirectory.

Use the following procedure to remove some resources while retaining others to preserve data.

.Procedure

. Identify the manifest that requires updating.
. Create new manifests to be applied in the manifest directories.
. Create new manifests for resource deletion. It is not necessary to include the `spec` in these manifests. See Using manifests example to create new manifests using the example.
. Use the procedure in "Removing manifests for RPM systems" to create `delete` subdirectories and place the manifests created for resource deletion in this path.

// Module included in the following assemblies:
//
// * microshift/running_applications/microshift-deleting-resource-manifests.adoc

[id="microshift-manifests-upgrade-scenario-ostree_{context}"]
= Upgrading manifests for OSTree systems

[role="_abstract"]
To update resources while preserving data on OSTree-based {microshift-short} systems, you can create new manifests for changes and deletions and use the OSTree removal procedure for the `delete` directory.

Use the following procedure to remove some resources while retaining others to preserve data.

[IMPORTANT]
====
For OSTree systems, the `delete` subdirectories are read-only.
====

.Procedure

. Identify the manifest that needs updating.
. Create a new manifest to apply in the manifest directories. See Using manifests example to create new manifests using the example.
. Create a new manifest for resource deletion to be placed in the `delete` subdirectories.
. Use the procedure in "Removing manifests for OSTree systems" to remove the manifests.

[id="additional-resources_microshift-deleting-resource-manifests_{context}"]
[role="_additional-resources"]
== Additional resources
* Using Kustomize manifests to deploy applications
