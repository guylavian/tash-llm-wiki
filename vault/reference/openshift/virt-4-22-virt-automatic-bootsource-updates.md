---
title: "Managing automatic boot source updates"
type: reference
domain: openshift
slug: virt-4-22-virt-automatic-bootsource-updates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-automatic-bootsource-updates
version: 4.22
family: virt
documentKind: "Documentation"
---

# Managing automatic boot source updates

[id="virt-automatic-bootsource-updates"]
= Managing automatic boot source updates

[role="_abstract"]
You can manage automatic updates for boot sources used to create virtual machines. This includes configuring update behavior for Red Hat and custom boot sources.

// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

[id="virt-managing-auto-update-all-system-boot-sources_{context}"]
= Managing automatic updates for all system-defined boot sources

[role="_abstract"]
Disabling automatic boot source imports and updates can lower resource usage. In disconnected environments, disabling automatic boot source updates prevents `CDIDataImportCronOutdated` alerts from filling up logs.

To disable automatic updates for all system-defined boot sources, set the `enableCommonBootImageImport` field value to `false`. Disabling automatic updates deletes the associated `DataImportCron` objects. Setting this value to `true` turns automatic updates back on.

[NOTE]
====
Custom boot sources are not affected by this setting.
====

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Enable or disable automatic boot source updates by editing the `HyperConverged` custom resource (CR).

** To disable automatic boot source updates, set the `spec.enableCommonBootImageImport` field value in the `HyperConverged` CR to `false`. For example:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op": "replace", "path": \
  "/spec/enableCommonBootImageImport", \
  "value": false}]'
----

** To re-enable automatic boot source updates, set the `spec.enableCommonBootImageImport` field value in the `HyperConverged` CR to `true`. For example:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op": "replace", "path": \
  "/spec/enableCommonBootImageImport", \
  "value": true}]'
----

// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

[id="virt-configuring-default-and-virt-default-storage-class_{context}"]
= Configuring the default and virt-default storage classes

[role="_abstract"]
A storage class determines how persistent storage is provisioned for workloads. In {VirtProductName}, the virt-default storage class takes precedence over the cluster default storage class and is used specifically for virtualization workloads.

Only one storage class should be set as virt-default or cluster default at a time. If multiple storage classes are marked as default, the virt-default storage class overrides the cluster default. To ensure consistent behavior, configure only one storage class as the default for virtualization workloads.

[IMPORTANT]
====
Boot sources are created using the default storage class. When the default storage class changes, old boot sources are automatically updated using the new default storage class. If your cluster does not have a default storage class, you must define one.

If boot source images were stored as volume snapshots and both the cluster default and virt-default storage class have been unset, the volume snapshots are cleaned up and new data volumes will be created. However the newly created data volumes will not start importing until a default storage class is set.
====

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Patch the current virt-default or a cluster default storage class to false:
.. Identify all storage classes currently marked as virt-default by running the following command:
+
[source,terminal]
----
$ oc get sc -o json| jq '.items[].metadata|select(.annotations."storageclass.kubevirt.io/is-default-virt-class"=="true")|.name'
----
+
.. For each storage class returned, remove the virt-default annotation by running the following command:
+
[source,terminal]
----
$ oc patch storageclass <storage_class_name> -p '{"metadata": {"annotations": {"storageclass.kubevirt.io/is-default-virt-class": "false"}}}'
----
+
.. Identify all storage classes currently marked as cluster default by running the following command:
+
[source,terminal]
----
$ oc get sc -o json| jq '.items[].metadata|select(.annotations."storageclass.kubernetes.io/is-default-class"=="true")|.name'
----
+
.. For each storage class returned, remove the cluster default annotation by running the following command:
+
[source,terminal]
----
$ oc patch storageclass <storage_class_name> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "false"}}}'
----

. Set a new default storage class:
.. Assign the virt-default role to a storage class by running the following command:
+
[source,terminal]
----
$ oc patch storageclass <storage_class_name> -p '{"metadata": {"annotations": {"storageclass.kubevirt.io/is-default-virt-class": "true"}}}'
----
+
.. Alternatively, assign the cluster default role to a storage class by running the following command:
+
[source,terminal]
----
$ oc patch storageclass <storage_class_name> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
----

// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

[id="virt-configuring-storage-class-bootsource-update_{context}"]
= Configuring a storage class for boot source images

[role="_abstract"]
You can configure a specific storage class in the `HyperConverged` resource.

[IMPORTANT]
====
To ensure stable behavior and avoid unnecessary re-importing, you can specify the `storageClassName` in the `dataImportCronTemplates` section of the `HyperConverged` resource.
====

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the `dataImportCronTemplate` to the spec section of the `HyperConverged` resource and set the `storageClassName`:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  dataImportCronTemplates:
  - metadata:
      name: rhel9-image-cron
    spec:
      template:
        spec:
          storage:
            storageClassName: <storage_class>
      schedule: "0 */12 * * *"
      managedDataSource: <data_source>
# ...
----
** `spec.dataImportCronTemplates.spec.template.spec.storage.storageClassName` specifies the storage class.
** `spec.dataImportCronTemplates.spec.schedule` is a required field that specifies the schedule for the job in cron format.
** `spec.dataImportCronTemplates.spec.managedDataSource` is a required field that specifies the data source to use.
+
[NOTE]
====
For the custom image to be detected as an available boot source, the value of the `spec.dataVolumeTemplates.spec.sourceRef.name` parameter in the VM template must match this value.
====

. Wait for the HyperConverged Operator (HCO) and Scheduling, Scale, and Performance (SSP) resources to complete reconciliation.

. Delete any outdated `DataVolume` and `VolumeSnapshot` objects from the `openshift-virtualization-os-images` namespace by running the following command.
+
[source,terminal]
----
$ oc delete DataVolume,VolumeSnapshot -n openshift-virtualization-os-images --selector=cdi.kubevirt.io/dataImportCron
----

. Wait for all `DataSource` objects to reach a "Ready - True" status. Data sources can reference either a PersistentVolumeClaim (PVC) or a VolumeSnapshot. To check the expected source format, run the following command:
+
[source,terminal]
----
$ oc get storageprofile <storage_class_name> -o json | jq .status.dataImportCronSourceFormat
----

// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

[id="virt-autoupdate-custom-bootsource_{context}"]
= Enabling automatic updates for custom boot sources

[role="_abstract"]
{VirtProductName} automatically updates system-defined boot sources by default, but does not automatically update custom boot sources. You must manually enable automatic updates by editing the `HyperConverged` custom resource (CR).

.Prerequisites

* The cluster has a default storage class.
* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `HyperConverged` CR, adding the appropriate template and boot source in the `dataImportCronTemplates` section. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  dataImportCronTemplates:
  - metadata:
      name: centos-stream9-image-cron
      annotations:
        cdi.kubevirt.io/storage.bind.immediate.requested: "true"
    spec:
      schedule: "0 */12 * * *"
      template:
        spec:
          source:
            registry:
              url: docker://quay.io/containerdisks/centos-stream:9
          storage:
            resources:
              requests:
                storage: 30Gi
      garbageCollect: Outdated
      managedDataSource: centos-stream9
----
** `spec.dataImportCronTemplates.metadata.annotations` specifies a required annotation for storage classes with `volumeBindingMode` set to `WaitForFirstConsumer`.
** `spec.dataImportCronTemplates.spec.schedule` specifies the schedule for the job, specified in cron format.
** `spec.dataImportCronTemplates.spec.template.spec.source.registry` specifies the registry source to use to create a data volume. Use the default `pod` `pullMethod` and not `node` `pullMethod`, which is based on the `node` docker cache. The `node` docker cache is useful when a registry image is available via `Container.Image`, but the CDI importer is not authorized to access it.
** `spec.dataImportCronTemplates.spec.managedDataSource` specifies the name of the managed data source. For the custom image to be detected as an available boot source, the name of the image's `managedDataSource` must match the name of the template's `DataSource`, which is found under `spec.dataVolumeTemplates.spec.sourceRef.name` in the VM template YAML file.

. Save the file.

// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

[id="virt-enabling-volume-snapshot-boot-source_{context}"]
= Enabling volume snapshot boot sources

[role="_abstract"]
You can enable volume snapshot boot sources by setting the parameter in the `StorageProfile` associated with the storage class that stores operating system base images.

Although `DataImportCron` was originally designed to maintain only PVC sources, `VolumeSnapshot` sources scale better than PVC sources for certain storage types.

[NOTE]
====
Use volume snapshots on a storage profile that is proven to scale better when cloning from a single snapshot.
====

.Prerequisites

* You must have access to a volume snapshot with the operating system image.
* The storage must support snapshotting.
* You have installed the {oc-first}.

.Procedure

. Open the storage profile object that corresponds to the storage class used to provision boot sources by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit storageprofile <storage_class>
----

. Review the `dataImportCronSourceFormat` specification of the `StorageProfile` to confirm whether or not the VM is using PVC or volume snapshot by default.

. Edit the storage profile, if needed, by updating the `dataImportCronSourceFormat` specification to `snapshot`.
+
Example storage profile:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: StorageProfile
metadata:
# ...
spec:
  dataImportCronSourceFormat: snapshot
----

.Verification

. Open the storage profile object that corresponds to the storage class used to provision boot sources.
+
[source,terminal,subs="attributes+"]
----
$ oc get storageprofile <storage_class>  -oyaml
----

. Confirm that the `dataImportCronSourceFormat` specification of the `StorageProfile` is set to 'snapshot', and that any `DataSource` objects that the `DataImportCron` points to now reference volume snapshots.

You can now use these boot sources to create virtual machines.

// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

[id="virt-disable-auto-updates-single-boot-source_{context}"]
= Disabling automatic updates for a single boot source

[role="_abstract"]
You can disable automatic updates for an individual boot source, whether it is custom or system-defined, by editing the `HyperConverged` custom resource (CR).

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Disable automatic updates for an individual boot source by editing the `spec.dataImportCronTemplates` field.
+
Custom boot source::
* Remove the boot source from the `spec.dataImportCronTemplates` field. Automatic updates are disabled for custom boot sources by default.

+
System-defined boot source::
.. Add the boot source to `spec.dataImportCronTemplates`.
+
[NOTE]
====
Automatic updates are enabled by default for system-defined boot sources, but these boot sources are not listed in the CR unless you add them.
====
.. Set the value of the `dataimportcrontemplate.kubevirt.io/enable` annotation to `'false'`.
+
--
For example:
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  dataImportCronTemplates:
  - metadata:
      annotations:
        dataimportcrontemplate.kubevirt.io/enable: 'false'
      name: rhel8-image-cron
# ...
----
--

. Save the file.

// Module included in the following assemblies:
//
// * virt-increasing-bootsource-disk-image-retention.adoc

[id="virt-increasing-bootsource-disk-image-retention_{context}"]
= Increasing boot source disk image retention

[role="_abstract"]
You can configure image retention settings to increase the number of older operating system image versions preserved on the cluster.

When automatic boot source updates are enabled, the Containerized Data Importer (CDI) tracks and downloads the latest versions of operating system images. By default, the system aggressively minimizes the retention of older versions to conserve disk space. However, if you require a safety mechanism that allows you to roll back if a newly imported version introduces issues, you can increase the retention count.

[NOTE]
====
Manually deleting older `PersistentVolumeClaim` or `DataVolume` objects associated with historic boot source imports does not impact cluster stability or future updates.
====

.Procedure

. Open the `HyperConverged` custom resource (CR) in your default editor:
+
[source,terminal]
----
$ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
----

. Edit the `spec.dataImportCronTemplates` field to adjust the `importsToKeep` parameter to your preferred retention threshold:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  dataImportCronTemplates:
    - metadata:
        name: rhel9-image-cron
      spec:
        garbageCollect: Outdated <1>
        importsToKeep: 3
        schedule: "0 */12 * * *"
        managedDataSource: rhel9
----

// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

[id="virt-verify-status-bootsource-update_{context}"]
= Verifying the status of a boot source

[role="_abstract"]
You can determine if a boot source is system-defined or custom by viewing the `HyperConverged` custom resource (CR).

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. View the contents of the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} -o yaml
----
+
Example output:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
# ...
status:
# ...
  dataImportCronTemplates:
  - metadata:
      annotations:
        cdi.kubevirt.io/storage.bind.immediate.requested: "true"
      name: centos-9-image-cron
    spec:
      garbageCollect: Outdated
      managedDataSource: centos-stream9
      schedule: 55 8/12 * * *
      template:
        metadata: {}
        spec:
          source:
            registry:
              url: docker://quay.io/containerdisks/centos-stream:9
          storage:
            resources:
              requests:
                storage: 30Gi
        status: {}
    status:
      commonTemplate: true
# ...
  - metadata:
      annotations:
        cdi.kubevirt.io/storage.bind.immediate.requested: "true"
      name: user-defined-dic
    spec:
      garbageCollect: Outdated
      managedDataSource: user-defined-centos-stream9
      schedule: 55 8/12 * * *
      template:
        metadata: {}
        spec:
          source:
            registry:
              pullMethod: node
              url: docker://quay.io/containerdisks/centos-stream:9
          storage:
            resources:
              requests:
                storage: 30Gi
        status: {}
    status: {}
# ...
----
** `status.dataImportCronTemplates.status.commonTemplate` specifies a system-defined boot source.
** `status.dataImportCronTemplates.status` specifies a custom boot source.

. Verify the status of the boot source by reviewing the `status.dataImportCronTemplates.status` field.
* If the field contains `commonTemplate: true`, it is a system-defined boot source.
* If the `status.dataImportCronTemplates.status` field has the value `{}`, it is a custom boot source.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* All Red Hat boot sources

* All custom boot sources

* Individual Red Hat or custom boot sources
