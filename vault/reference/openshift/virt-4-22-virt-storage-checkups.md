---
title: "Storage checkups"
type: reference
domain: openshift
slug: virt-4-22-virt-storage-checkups
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-storage-checkups
version: 4.22
family: virt
documentKind: "Documentation"
---

# Storage checkups

[id="virt-storage-checkups"]
= Storage checkups

[role="_abstract"]
You can use a storage checkup to verify that the cluster storage is optimally configured for {VirtProductName}.

// Module included in the following assemblies:
//
// * virt/monitoring/virt-running-cluster-checkups.adoc

[id="virt-retain-storage-checkup-resources_{context}"]
= Retaining resources for troubleshooting storage checkups

[role="_abstract"]
The predefined storage checkup includes `skipTeardown` configuration options, which control resource clean up after a storage checkup runs.
By default, the `skipTeardown` field value is `Never`, which means that the checkup always performs teardown steps and deletes all resources after the checkup runs.

You can retain resources for further inspection in case a failure occurs by setting the `skipTeardown` field to `onfailure`.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Run the following command to edit the `storage-checkup-config` config map:
+
[source,terminal]
----
$ oc edit configmap storage-checkup-config -n <checkup_namespace>
----

. Configure the `skipTeardown` field to use the `onfailure` value. You can do this by modifying the `storage-checkup-config` config map, stored in the `storage_checkup.yaml` file:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: storage-checkup-config
  namespace: <checkup_namespace>
data:
  spec.param.skipTeardown: onfailure
# ...
----

. Reapply the `storage-checkup-config` config map by running the following command:
+
[source,terminal]
----
$ oc apply -f storage_checkup.yaml -n <checkup_namespace>
----

// Module included in the following assemblies:
//
// * virt/monitoring/virt-running-cluster-checkups.adoc

[id="virt-storage-checkup-web-console_{context}"]
= Running a storage checkup by using the web console

[role="_abstract"]
You can run a storage checkup to validate that storage is working correctly for virtual machines.

.Procedure

. Navigate to *Virtualization* -> *Checkups* in the web console.
. Click the *Storage* tab.
. Click *Install permissions*.
. Click *Run checkup*.
. Enter a name for the checkup in the *Name* field.
. Enter a timeout value for the checkup in the *Timeout (minutes)* fields.
. Click *Run*.

.Result

You can view the status of the storage checkup in the *Checkups* list on the *Storage* tab. Click on the name of the checkup for more details.

// Module included in the following assemblies:
//
// * virt/monitoring/virt-running-cluster-checkups.adoc

[id="virt-checking-storage-configuration_{context}"]
= Running a storage checkup by using the CLI

[role="_abstract"]
Use a predefined checkup to verify that the OpenShift Container Platform cluster storage is configured optimally to run {VirtProductName} workloads.

.Prerequisites

* You have installed the {oc-first}.
* The cluster administrator has created the required `cluster-reader` permissions for the storage checkup service account and namespace, such as in the following example:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubevirt-storage-checkup-clustereader
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-reader
subjects:
- kind: ServiceAccount
  name: storage-checkup-sa
  namespace: <target_namespace>
----
+
where:

`<target_namespace>`:: Specifies the namespace where the checkup is to be run.

.Procedure

. Create a `ServiceAccount`, `Role`, and `RoleBinding` manifest file for the storage checkup.
+
Example service account, role, and rolebinding manifest:
+
[%collapsible]
[source,yaml]
----
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: storage-checkup-sa
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: storage-checkup-role
rules:
  - apiGroups: [ "" ]
    resources: [ "configmaps" ]
    verbs: ["get", "update"]
  - apiGroups: [ "kubevirt.io" ]
    resources: [ "virtualmachines" ]
    verbs: [ "create", "delete" ]
  - apiGroups: [ "kubevirt.io" ]
    resources: [ "virtualmachineinstances" ]
    verbs: [ "get" ]
  - apiGroups: [ "subresources.kubevirt.io" ]
    resources: [ "virtualmachineinstances/addvolume", "virtualmachineinstances/removevolume" ]
    verbs: [ "update" ]
  - apiGroups: [ "kubevirt.io" ]
    resources: [ "virtualmachineinstancemigrations" ]
    verbs: [ "create" ]
  - apiGroups: [ "cdi.kubevirt.io" ]
    resources: [ "datavolumes" ]
    verbs: [ "create", "delete" ]
  - apiGroups: [ "" ]
    resources: [ "persistentvolumeclaims" ]
    verbs: [ "delete" ]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: storage-checkup-role
subjects:
  - kind: ServiceAccount
    name: storage-checkup-sa
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: storage-checkup-role
----

. Apply the `ServiceAccount`, `Role`, and `RoleBinding` manifest in the target namespace:
+
[source,terminal]
----
$ oc apply -n <target_namespace> -f <storage_sa_roles_rolebinding>.yaml
----

. Create a `ConfigMap` and `Job` manifest file. The config map contains the input parameters for the checkup job.
+
Example input config map and job manifest:
+
[source,yaml,subs="attributes+"]
----
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: storage-checkup-config
  namespace: $CHECKUP_NAMESPACE
data:
  spec.timeout: 10m
  spec.param.storageClass: ocs-storagecluster-ceph-rbd-virtualization
  spec.param.vmiTimeout: 3m
---
apiVersion: batch/v1
kind: Job
metadata:
  name: storage-checkup
  namespace: $CHECKUP_NAMESPACE
spec:
  backoffLimit: 0
  template:
    spec:
      serviceAccount: storage-checkup-sa
      restartPolicy: Never
      containers:
        - name: storage-checkup
          image: quay.io/kiagnose/kubevirt-storage-checkup:main
          imagePullPolicy: Always
          env:
            - name: CONFIGMAP_NAMESPACE
              value: $CHECKUP_NAMESPACE
            - name: CONFIGMAP_NAME
              value: storage-checkup-config
----

. Apply the `ConfigMap` and `Job` manifest file in the target namespace to run the checkup:
+
[source,terminal]
----
$ oc apply -n <target_namespace> -f <storage_configmap_job>.yaml
----

. Wait for the job to complete:
+
[source,terminal]
----
$ oc wait job storage-checkup -n <target_namespace> --for condition=complete --timeout 10m
----

. Review the results of the checkup by running the following command:
+
[source,terminal]
----
$ oc get configmap storage-checkup-config -n <target_namespace> -o yaml
----
+
Example output config map (success):
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: storage-checkup-config
  labels:
    kiagnose/checkup-type: kubevirt-storage
data:
  spec.timeout: 10m
  status.succeeded: "true"
  status.failureReason: ""
  status.startTimestamp: "2023-07-31T13:14:38Z"
  status.completionTimestamp: "2023-07-31T13:19:41Z"
  status.result.cnvVersion: 4.21.2
  status.result.defaultStorageClass: trident-nfs
  status.result.goldenImagesNoDataSource: <data_import_cron_list>
  status.result.goldenImagesNotUpToDate: <data_import_cron_list>
  status.result.ocpVersion: 4.21.0
  status.result.pvcBound: "true"
  status.result.storageProfileMissingVolumeSnapshotClass: <storage_class_list>
  status.result.storageProfilesWithEmptyClaimPropertySets: <storage_profile_list>
  status.result.storageProfilesWithSmartClone: <storage_profile_list>
  status.result.storageProfilesWithSpecClaimPropertySets: <storage_profile_list>
  status.result.storageProfilesWithRWX: |-
    ocs-storagecluster-ceph-rbd
    ocs-storagecluster-ceph-rbd-virtualization
    ocs-storagecluster-cephfs
    trident-iscsi
    trident-minio
    trident-nfs
    windows-vms
  status.result.vmBootFromGoldenImage: VMI "vmi-under-test-dhkb8" successfully booted
  status.result.vmHotplugVolume: |-
    VMI "vmi-under-test-dhkb8" hotplug volume ready
    VMI "vmi-under-test-dhkb8" hotplug volume removed
  status.result.vmLiveMigration: VMI "vmi-under-test-dhkb8" migration completed
  status.result.vmVolumeClone: 'DV cloneType: "csi-clone"'
  status.result.vmsWithNonVirtRbdStorageClass: <vm_list>
  status.result.vmsWithUnsetEfsStorageClass: <vm_list>
----
+
* `data.status.succeeded` defines if the checkup is successful (`true`) or not (`false`).
* `data.status.failureReason` defines the reason for failure if the checkup fails.
* `data.status.startTimestamp` defines the time when the checkup started, in RFC 3339 time format.
* `data.status.completionTimestamp` defines the time when the checkup has completed, in RFC 3339 time format.
* `data.status.result.cnvVersion` defines the {VirtProductName} version.
* `data.status.result.defaultStorageClass` defines if there is a default storage class.
* `data.status.result.goldenImagesNoDataSource` defines the list of golden images whose data source is not ready.
* `data.status.result.goldenImagesNotUpToDate` defines the list of golden images whose data import cron is not up-to-date.
* `data.status.result.ocpVersion` defines the OpenShift Container Platform version.
* `data.status.result.pvcBound` defines if a PVC of 10Mi has been created and bound by the provisioner.
* `data.status.result.storageProfileMissingVolumeSnapshotClass` defines the list of storage profiles using snapshot-based clone but missing VolumeSnapshotClass.
* `data.status.result.storageProfilesWithEmptyClaimPropertySets` defines the list of storage profiles with unknown provisioners.
* `data.status.result.storageProfilesWithSmartClone` defines the list of storage profiles with smart clone support (CSI/snapshot).
* `data.status.result.storageProfilesWithSpecClaimPropertySets` defines the list of storage profiles spec-overriden claimPropertySets.
* `data.status.result.vmsWithNonVirtRbdStorageClass` defines the list of virtual machines that use the Ceph RBD storage class when the virtualization storage class exists.
* `data.status.result.vmsWithUnsetEfsStorageClass` defines the list of virtual machines that use an Elastic File Store (EFS) storage class where the GID and UID are not set in the storage class.

. Delete the job and config map that you previously created by running the following commands:
+
[source,terminal]
----
$ oc delete job -n <target_namespace> storage-checkup
----
+
[source,terminal]
----
$ oc delete config-map -n <target_namespace> storage-checkup-config
----

. Optional: If you do not plan to run another checkup, delete the `ServiceAccount`, `Role`, and `RoleBinding` manifest:
+
[source,terminal]
----
$ oc delete -f <storage_sa_roles_rolebinding>.yaml
----

// Module included in the following assemblies:
//
// * /virt/monitoring/virt-running-cluster-checkups.adoc

[id="virt-troubleshoot-storage-checkup_{context}"]
= Troubleshooting a failed storage checkup

[role="_abstract"]
If a storage checkup fails, there are steps that you can take to identify the reason for failure.

.Prerequisites

* You have installed the {oc-first}.
* You have downloaded the directory provided by the `must-gather` tool.

.Procedure

. Review the `status.failureReason` field in the `storage-checkup-config` config map by running the following command and observing the output:
+
[source,terminal]
----
$ oc get configmap storage-checkup-config -n <namespace> -o yaml
----
+
Example output config map:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: storage-checkup-config
  labels:
    kiagnose/checkup-type: kubevirt-storage
data:
  spec.timeout: 10m
  status.succeeded: "false"
  status.failureReason: "ErrNoDefaultStorageClass"
# ...
----
** If the checkup has failed, the `status.succeeded` value is `false`.
** If the checkup has failed, the `status.failureReason` field contains an error message. In this example output, the `ErrNoDefaultStorageClass` error message means that no default storage class is configured.

. Search the directory provided by the `must-gather` tool for logs, events, or terms related to the error in the `data.status.failureReason` field value.

[role="_additional-resources"]
.Additional resources
* Collecting data for Red{nbsp}Hat Support
* Using the `must-gather` tool for {VirtProductName}

// Module included in the following assemblies:
//
// * virt/monitoring/virt-running-cluster-checkups.adoc

[id="virt-troubleshoot-storage-checkup-error-codes_{context}"]
= Storage checkup error codes

[role="_abstract"]
The following error codes might appear in the `storage-checkup-config` config map after a storage checkup fails.

[options="header"]
|===

|Error code |Meaning

|`ErrNoDefaultStorageClass`
|No default storage class is configured.

|`ErrPvcNotBound`
|One or more persistent volume claims (PVCs) failed to bind.

|`ErrMultipleDefaultStorageClasses`
|Multiple default storage classes are configured.

|`ErrEmptyClaimPropertySets`
|There are `StorageProfile` objects containing empty `ClaimPropertySets` specs.

|`ErrVMsWithUnsetEfsStorageClass`
|There are VMs using elastic file system (EFS) storage classes, where the GID and UID are not set in the `StorageClass` object.

|`ErrGoldenImagesNotUpToDate`
|One or more golden images has a `DataImportCron` object that is either not up to date or has a `DataSource` object which is not ready.

|`ErrGoldenImageNoDataSource`
|The `DataSource` object of the golden image has either no PVC or no snapshot source configured.

|`ErrBootFailedOnSomeVMs`
|Some VMs failed to boot within the expected time.

|===
