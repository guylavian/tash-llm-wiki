---
title: "OADP features and plugins"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-features-plugins
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-features-plugins
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# OADP features and plugins

[id="oadp-features-plugins"]
= OADP features and plugins

[role="_abstract"]
Review {oadp-first} features and default plugins that integrate Velero with cloud providers to back up and restore OpenShift Container Platform resources. This helps you to select the right plugins and features for your backup and restore environment.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-features_{context}"]
= OADP features

[role="_abstract"]
Review the backup, restore, and scheduling features of {oadp-first} for protecting applications on OpenShift Container Platform. This helps you to understand the available capabilities for your data protection strategy.

Backup::
You can use OADP to back up all applications on the OpenShift Platform, or you can filter the resources by type, namespace, or label.
+
OADP backs up Kubernetes objects and internal images by saving them as an archive file on object storage. OADP backs up persistent volumes (PVs) by creating snapshots with the native cloud snapshot API or with the Container Storage Interface (CSI). For cloud providers that do not support snapshots, OADP backs up resources and PV data with Restic.

+
[NOTE]
====
You must exclude Operators from the backup of an application for backup and restore to succeed.
====

Restore::
You can restore resources and PVs from a backup. You can restore all objects in a backup or filter the objects by namespace, PV, or label.

+
[NOTE]
====
You must exclude Operators from the backup of an application for backup and restore to succeed.
====

Schedule::
You can schedule backups at specified intervals.

Hooks::
You can use hooks to run commands in a container on a pod, for example, `fsfreeze` to freeze a file system. You can configure a hook to run before or after a backup or restore. Restore hooks can run in an init container or in the application container.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-plugins_{context}"]
= OADP plugins

[role="_abstract"]
Review the default Velero plugins provided by {oadp-first} that integrate with storage providers to support backup and snapshot operations. This helps you to select and configure the right plugins for your cloud environment.

{oadp-short} also provides plugins for OpenShift Container Platform resource backups, OpenShift Virtualization resource backups, and Container Storage Interface (CSI) snapshots.

[cols="3", options="header"]
.OADP plugins
|===
|OADP plugin |Function |Storage location

.2+|`aws` |Backs up and restores Kubernetes objects. |AWS S3
|Backs up and restores volumes with snapshots. |AWS EBS

.2+|`azure` |Backs up and restores Kubernetes objects. |Microsoft Azure Blob storage
|Backs up and restores volumes with snapshots. |Microsoft Azure Managed Disks

.2+|`gcp` |Backs up and restores Kubernetes objects. |{gcp-full} Storage
|Backs up and restores volumes with snapshots. |Google Compute Engine Disks

|`openshift` |Backs up and restores OpenShift Container Platform resources. ^[1]^ |Object store

|`kubevirt` |Backs up and restores OpenShift Virtualization resources. ^[2]^ |Object store

|`csi` |Backs up and restores volumes with CSI snapshots. ^[3]^ |Cloud storage that supports CSI snapshots

|`hypershift` |Backs up and restores HyperShift hosted cluster resources. ^[4]^ |Object store
|===
[.small]
--
1. Mandatory.
2. Virtual machine disks are backed up with CSI snapshots or Restic.
3. The `csi` plugin uses the Kubernetes CSI snapshot API.
* OADP 1.1 or later uses `snapshot.storage.k8s.io/v1`
* OADP 1.0 uses `snapshot.storage.k8s.io/v1beta1`
4. Do not add the `hypershift` plugin in the `DataProtectionApplication` custom resource if the cluster is not a HyperShift hosted cluster.
--

[role="_additional-resources"]
.Additional resources

* Custom plugins

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-configuring-velero-plugins_{context}"]
= About OADP Velero plugins

[role="_abstract"]
Review how to configure default cloud provider plugins or install custom plugins during the {oadp-short} deployment to connect your specific storage solutions. This helps you to successfully back up and restore resources across your environments.

== Default Velero cloud provider plugins

You can install any of the following default Velero cloud provider plugins when you configure the `oadp_v1alpha1_dpa.yaml` file during deployment:

* `aws` (Amazon Web Services)
* `gcp` ({gcp-full})
* `azure` (Microsoft Azure)
* `openshift` (OpenShift Velero plugin)
* `csi` (Container Storage Interface)
* `kubevirt` (KubeVirt)

You specify the desired default plugins in the `oadp_v1alpha1_dpa.yaml` file during deployment.

The following `.yaml` file installs the `openshift`, `aws`, `azure`, and `gcp` plugins:

[source,yaml]
----
 apiVersion: oadp.openshift.io/v1alpha1
 kind: DataProtectionApplication
 metadata:
   name: dpa-sample
 spec:
   configuration:
     velero:
       defaultPlugins:
       - openshift
       - aws
       - azure
       - gcp
----

== Custom Velero plugins

You can install a custom Velero plugin by specifying the plugin `image` and `name` when you configure the `oadp_v1alpha1_dpa.yaml` file during deployment.

You specify the desired custom plugins in the `oadp_v1alpha1_dpa.yaml` file during deployment.

The following `.yaml` file installs the default `openshift`, `azure`, and `gcp` plugins and a custom plugin that has the name `custom-plugin-example` and the image `quay.io/example-repo/custom-velero-plugin`:

[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
 name: dpa-sample
spec:
 configuration:
   velero:
     defaultPlugins:
     - openshift
     - azure
     - gcp
     customPlugins:
     - name: custom-plugin-example
       image: quay.io/example-repo/custom-velero-plugin
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-supported-architecture_{context}"]
= Supported architectures for OADP

[role="_abstract"]
Review the architectures supported by {oadp-first}. This helps you to verify compatibility with your cluster infrastructure.

* AMD64
* ARM64
* PPC64le
* s390x

[NOTE]
====
OADP 1.2.0 and later versions support the ARM64 architecture.
====

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-support-ibm_{context}"]
= OADP support for {ibm-power-title} and {ibm-z-title}

[role="_abstract"]
Review {oadp-first} support and tested backup locations for {ibm-power-name} and {ibm-z-name}. This helps you to verify compatibility and supported configurations for your {ibm-power-name} or {ibm-z-name} environment.

* {oadp-short} {oadp-version-1-3} was tested successfully against OpenShift Container Platform 4.12, 4.13, 4.14, and 4.15 for both {ibm-power-name} and {ibm-z-name}. The sections that follow give testing and support information for {oadp-short} {oadp-version-1-3} in terms of backup locations for these systems.
* {oadp-short} {oadp-version-1-4} was tested successfully against OpenShift Container Platform 4.14, 4.15, 4.16, and 4.17 for both {ibm-power-name} and {ibm-z-name}. The sections that follow give testing and support information for {oadp-short} {oadp-version-1-4} in terms of backup locations for these systems.
* {oadp-short} {oadp-version-1-5} was tested successfully against OpenShift Container Platform 4.19 for both {ibm-power-name} and {ibm-z-name}. The sections that follow give testing and support information for {oadp-short} {oadp-version-1-5} in terms of backup locations for these systems.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-ibm-power-test-matrix_{context}"]
= OADP support for target backup locations using {ibm-power-title}

[role="_abstract"]
Review the tested and supported configurations for running {oadp-short} on {ibm-power-name} with various OpenShift Container Platform versions and S3-compatible backup locations. This helps you to verify that your {ibm-power-name} environment is supported before configuring backups.

* {ibm-power-name} running with OpenShift Container Platform 4.12, 4.13, 4.14, and 4.15, and {oadp-short} {oadp-version-1-3} was tested successfully against an AWS S3 backup location target. Although the test involved only an AWS S3 target, Red Hat supports running {ibm-power-name} with OpenShift Container Platform 4.13, 4.14, and 4.15, and {oadp-short} {oadp-version-1-3} against all S3 backup location targets, which are not AWS, as well.
* {ibm-power-name} running with OpenShift Container Platform 4.14, 4.15, 4.16, and 4.17, and {oadp-short} {oadp-version-1-4} was tested successfully against an AWS S3 backup location target. Although the test involved only an AWS S3 target, Red Hat supports running {ibm-power-name} with OpenShift Container Platform 4.14, 4.15, 4.16, and 4.17, and {oadp-short} {oadp-version-1-4} against all S3 backup location targets, which are not AWS, as well.
* {ibm-power-name} running with OpenShift Container Platform 4.19 and {oadp-short} {oadp-version-1-5} was tested successfully against an AWS S3 backup location target. Although the test involved only an AWS S3 target, Red Hat supports running {ibm-power-name} with OpenShift Container Platform 4.19 and {oadp-short} {oadp-version-1-5} against all S3 backup location targets, which are not AWS, as well.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-ibm-z-test-support_{context}"]
= OADP testing and support for target backup locations using {ibm-z-title}

[role="_abstract"]
Review the tested and supported {oadp-short} and OpenShift Container Platform version combinations for {ibm-z-name} against S3 backup location targets. This helps you verify that your {ibm-z-name} environment and {oadp-short} version are supported for backup operations.

* {ibm-z-name} running with OpenShift Container Platform 4.12, 4.13, 4.14, and 4.15, and {oadp-version-1-3} was tested successfully against an AWS S3 backup location target. Although the test involved only an AWS S3 target, Red Hat supports running {ibm-z-name} with OpenShift Container Platform 4.13 4.14, and 4.15, and {oadp-version-1-3} against all S3 backup location targets, which are not AWS, as well.
* {ibm-z-name} running with OpenShift Container Platform 4.14, 4.15, 4.16, and 4.17, and {oadp-version-1-4} was tested successfully against an AWS S3 backup location target. Although the test involved only an AWS S3 target, Red Hat supports running {ibm-z-name} with OpenShift Container Platform 4.14, 4.15, 4.16, and 4.17, and {oadp-version-1-4} against all S3 backup location targets, which are not AWS, as well.
* {ibm-z-name} running with OpenShift Container Platform 4.19 and {oadp-short} {oadp-version-1-5} was tested successfully against an AWS S3 backup location target. Although the test involved only an AWS S3 target, Red Hat supports running {ibm-z-name} with OpenShift Container Platform 4.19 and {oadp-short} {oadp-version-1-5} against all S3 backup location targets, which are not AWS, as well.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc

[id="oadp-ibm-power-and-z-known-issues_{context}"]
= Known issue of OADP using {ibm-power-name} and {ibm-z-name} platforms

[role="_abstract"]
Use only NFS storage with File System Backup (FSB) methods such as Kopia or Restic for {sno-caps} clusters on {ibm-power-name} and {ibm-z-name} platforms. This helps you to avoid unsupported backup configurations on these platforms.

There is currently no workaround for this restriction.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/backing_up_and_restoring/backing-up-applications.adoc

[id="oadp-fips_{context}"]
= OADP and FIPS

[role="_abstract"]
Federal Information Processing Standards (FIPS) are a set of computer security standards developed by the United States federal government inline with the Federal Information Security Management Act (FISMA).

{oadp-first} has been tested and works on FIPS-enabled OpenShift Container Platform clusters.

// Module included in the following assemblies:
// oadp-features-plugins-known-issues
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc
// * backup_and_restore/application_backup_and_restore/troubleshooting/restoring-workarounds-for-velero-backups-that-use-admission-webhooks.adoc
//

[id="avoiding-the-velero-plugin-panic-error_{context}"]
= Avoiding the Velero plugin panic error

[role="_abstract"]
Label a custom Backup Storage Location (BSL) to resolve Velero plugin panic errors during `imagestream` backups. This helps you to ensure the {oadp-short} controller creates the required registry secret when you manage the BSL outside the `DataProtectionApplication` (DPA) CR.

A missing secret can cause a panic error for the Velero plugin during image stream backups. When the backup and the BSL are managed outside the scope of the DPA, the OADP controller does not create the relevant `oadp-<bsl_name>-<bsl_provider>-registry-secret` parameter.

During the backup operation, the OpenShift Velero plugin panics on the `imagestream` backup, with the following panic error:

[source,text]
----
024-02-27T10:46:50.028951744Z time="2024-02-27T10:46:50Z" level=error msg="Error backing up item"
backup=openshift-adp/<backup name> error="error executing custom action (groupResource=imagestreams.image.openshift.io,
namespace=<BSL Name>, name=postgres): rpc error: code = Aborted desc = plugin panicked:
runtime error: index out of range with length 1, stack trace: goroutine 94…
----

.Procedure

. Label the custom BSL with the relevant label by using the following command:
+
[source,terminal]
----
$ oc label backupstoragelocations.velero.io <bsl_name> app.kubernetes.io/component=bsl
----

. After the BSL is labeled, wait until the DPA reconciles.
+
[NOTE]
====
You can force the reconciliation by making any minor change to the DPA itself.
====

.Verification

* After the DPA is reconciled, confirm that the parameter has been created and that the correct registry data has been populated into it by entering the following command:
+
[source,terminal]
----
$ oc -n openshift-adp get secret/oadp-<bsl_name>-<bsl_provider>-registry-secret -o json | jq -r '.data'
----

// Module included in the following assemblies:
// oadp-features-plugins-known-issues
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc
// * backup_and_restore/application_backup_and_restore/troubleshooting/restoring-workarounds-for-velero-backups-that-use-admission-webhooks.adoc
//

[id="workaround-for-openshift-adp-controller-segmentation-fault_{context}"]
= Workaround for OpenShift ADP Controller segmentation fault

[role="_abstract"]
Define either `velero` or `cloudstorage` in your Data Protection Application (DPA) configuration to prevent indefinite pod crashes. This configuration resolves a segmentation fault in the `openshift-adp-controller-manager` pod that occurs when both components are enabled.

The `openshift-adp-controller-manager` pod fails with a crash loop segmentation fault due to the following settings:

* If you define both `velero` and `cloudstorage`, the `openshift-adp-controller-manager` fails.
* If you do not define both `velero` and `cloudstorage`, the `openshift-adp-controller-manager` fails.

See _OADP-1054_ for more information.

[role="_additional-resources"]
.Additional resources

* OADP-1054
