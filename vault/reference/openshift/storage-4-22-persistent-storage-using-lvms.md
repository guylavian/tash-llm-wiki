---
title: "Persistent storage using logical volume manager storage"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-using-lvms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-using-lvms
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using logical volume manager storage

[id="persistent-storage-using-lvms"]
= Persistent storage using logical volume manager storage

[role="_abstract"]
{lvms-first} uses LVM2 through the `TopoLVM CSI` driver to dynamically provision local storage on a cluster with limited resources.

You can create volume groups, persistent volume claims (PVCs), volume snapshots, and volume clones by using {lvms}.

//deploying/requirements with RHACM
// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-about-lvm-storage-installation_{context}"]
= Logical Volume Manager Storage installation

You can install Logical Volume Manager (LVM) Storage on an OpenShift Container Platform cluster and configure it to dynamically provision storage for your workloads.

You can install {lvms} by using the OpenShift Container Platform CLI (`oc`), OpenShift Container Platform web console, or {rh-rhacm-first}.

[WARNING]
====
When using {lvms} on multi-node clusters, {lvms} only supports provisioning local storage. {lvms} does not support storage data replication mechanisms across nodes. You must ensure storage data replication through active or passive replication mechanisms to avoid a single point of failure.
====

[id="lvms-deployment-requirements-for-sno-ran_{context}"]
== Prerequisites to install LVM Storage

The prerequisites to install {lvms} are as follows:

* Ensure that you have a minimum of 10 milliCPU and 100 MiB of RAM.

* Ensure that every managed cluster has dedicated disks that are used to provision storage. {lvms} uses only those disks that are empty and do not contain file system signatures. To ensure that the disks are empty and do not contain file system signatures, wipe the disks before using them.

* Before installing {lvms} in a private CI environment where you can reuse the storage devices that you configured in the previous {lvms} installation, ensure that you have wiped the disks that are not in use. If you do not wipe the disks before installing {lvms}, you cannot reuse the disks without manual intervention.
+
[NOTE]
====
You cannot wipe the disks that are in use.
====

* If you want to install {lvms} by using {rh-rhacm-first}, ensure that you have installed {rh-rhacm} on an OpenShift Container Platform cluster. See the "Installing LVM Storage using RHACM" section.

[role="_additional-resources"]
.Additional resources

* Red Hat Advanced Cluster Management for Kubernetes: Installing while connected online

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="install-lvms-operator-cli_{context}"]
= Installing {lvms} by using the CLI

As a cluster administrator, you can install {lvms} by using the OpenShift CLI.

[NOTE]
====
The default namespace for the {lvms} Operator is `openshift-lvm-storage`.
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have logged in to OpenShift Container Platform as a user with `cluster-admin` and Operator installation permissions.

.Procedure

. Create a YAML file with the configuration for creating a namespace:
+
.Example YAML configuration for creating a namespace
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/warn: privileged
  name: openshift-lvm-storage
----

. Create the namespace by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>
----

. Create an `OperatorGroup` CR YAML file:
+
.Example `OperatorGroup` CR
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-storage-operatorgroup
  namespace: openshift-lvm-storage
spec:
  targetNamespaces:
  - openshift-storage
----

. Create the `OperatorGroup` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>
----

. Create a `Subscription` CR YAML file:
+
.Example `Subscription` CR
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: lvms
  namespace: openshift-lvm-storage
spec:
  installPlanApproval: Automatic
  name: lvms-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

. Create the `Subscription` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>
----

.Verification

. To verify that {lvms} is installed, run the following command:
+
[source,terminal]
----
$ oc get csv -n openshift-lvm-storage -o custom-columns=Name:.metadata.name,Phase:.status.phase
----
+
.Example output
[source,terminal]
----
Name                         Phase
4.13.0-202301261535          Succeeded
----

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-installing-lvms-with-web-console_{context}"]
= Installing {lvms} by using the web console

You can install {lvms} by using the OpenShift Container Platform web console.

[NOTE]
====
The default namespace for the {lvms} Operator is `openshift-lvm-storage`.
====

.Prerequisites

* You have access to the cluster.
* You have access to OpenShift Container Platform with `cluster-admin` and Operator installation permissions.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Click *Ecosystem* -> *Software Catalog*.
. Click *LVM Storage* on the software catalog page.
. Set the following options on the *Operator Installation* page:
.. *Update Channel* as *stable-*.
.. *Installation Mode* as *A specific namespace on the cluster*.
.. *Installed Namespace* as *Operator recommended namespace openshift-storage*.
   If the `openshift-lvm-storage` namespace does not exist, it is created during the operator installation.
.. *Update approval* as *Automatic* or *Manual*.
+
[NOTE]
====
If you select *Automatic* updates, the Operator Lifecycle Manager (OLM) automatically updates the running instance of {lvms} without any intervention.

If you select *Manual* updates, the OLM creates an update request.
As a cluster administrator, you must manually approve the update request to update {lvms} to a newer version.
====
. Optional: Select the *Enable Operator recommended cluster monitoring on this Namespace* checkbox.
. Click *Install*.

.Verification steps

* Verify that {lvms} shows a green tick, indicating successful installation.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-installing-lvms-disconnected-env_{context}"]
= Installing {lvms} in a disconnected environment

You can install {lvms} on OpenShift Container Platform in a disconnected environment. All sections referenced in this procedure are linked in the "Additional resources" section.

.Prerequisites

* You read the "About disconnected installation mirroring" section.
* You have access to the OpenShift Container Platform image repository.
* You created a mirror registry.

.Procedure

. Follow the steps in the "Creating the image set configuration" procedure. To create an `ImageSetConfiguration` custom resource (CR) for {lvms}, you can use the following example `ImageSetConfiguration` CR configuration:
+

. Follow the procedure in the "Mirroring an image set to a mirror registry" section.

. Follow the procedure in the "Configuring image registry repository mirroring" section.

[role="_additional-resources"]
.Additional resources

* About disconnected installation mirroring

* Creating a mirror registry with mirror registry for Red Hat OpenShift

* Mirroring the OpenShift Container Platform image repository

* Creating the image set configuration

* Mirroring an image set to a mirror registry

* Configuring image registry repository mirroring

* Why use imagestreams

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-installing-odf-logical-volume-manager-operator-using-rhacm_{context}"]
= Installing {lvms} by using {rh-rhacm}

To install {lvms} on the clusters by using {rh-rhacm-first}, you must create a `Policy` custom resource (CR). You can also configure the criteria to select the clusters on which you want to install {lvms}.

[NOTE]
====
The `Policy` CR that is created to install {lvms} is also applied to the clusters that are imported or created after creating the `Policy` CR.
====

.Prerequisites
* You have access to the {rh-rhacm} cluster using an account with `cluster-admin` and Operator installation permissions.
* You have dedicated disks that {lvms} can use on each cluster.
* The cluster must be managed by {rh-rhacm}.

.Procedure

. Log in to the {rh-rhacm} CLI using your OpenShift Container Platform credentials.

. Create a namespace.
+
[source,terminal]
----
$ oc create ns <namespace>
----

. Create a `Policy` CR YAML file:
+
.Example `Policy` CR to install and configure {lvms}
[source,yaml]
----
apiVersion: apps.open-cluster-management.io/v1
kind: PlacementRule
metadata:
  name: placement-install-lvms
spec:
  clusterConditions:
  - status: "True"
    type: ManagedClusterConditionAvailable
  clusterSelector: <1>
    matchExpressions:
    - key: mykey
      operator: In
      values:
      - myvalue
---
apiVersion: policy.open-cluster-management.io/v1
kind: PlacementBinding
metadata:
  name: binding-install-lvms
placementRef:
  apiGroup: apps.open-cluster-management.io
  kind: PlacementRule
  name: placement-install-lvms
subjects:
- apiGroup: policy.open-cluster-management.io
  kind: Policy
  name: install-lvms
---
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  annotations:
    policy.open-cluster-management.io/categories: CM Configuration Management
    policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
    policy.open-cluster-management.io/standards: NIST SP 800-53
  name: install-lvms
spec:
  disabled: false
  remediationAction: enforce
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: install-lvms
      spec:
        object-templates:
        - complianceType: musthave
          objectDefinition: <2>
            apiVersion: v1
            kind: Namespace
            metadata:
              labels:
                openshift.io/cluster-monitoring: "true"
                pod-security.kubernetes.io/enforce: privileged
                pod-security.kubernetes.io/audit: privileged
                pod-security.kubernetes.io/warn: privileged
              name: openshift-lvm-storage
        - complianceType: musthave
          objectDefinition: <3>
            apiVersion: operators.coreos.com/v1
            kind: OperatorGroup
            metadata:
              name: openshift-storage-operatorgroup
              namespace: openshift-lvm-storage
            spec:
              targetNamespaces:
              - openshift-lvm-storage
        - complianceType: musthave
          objectDefinition: <4>
            apiVersion: operators.coreos.com/v1alpha1
            kind: Subscription
            metadata:
              name: lvms
              namespace: openshift-lvm-storage
            spec:
              installPlanApproval: Automatic
              name: lvms-operator
              source: redhat-operators
              sourceNamespace: openshift-marketplace
        remediationAction: enforce
        severity: low
----
<1> Set the `key` field and `values` field in `PlacementRule.spec.clusterSelector` to match the labels that are configured in the clusters on which you want to install {lvms}.
<2> Namespace configuration.
<3> The `OperatorGroup` CR configuration.
<4> The `Subscription` CR configuration.

. Create the `Policy` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name> -n <namespace>
----
+
Upon creating the `Policy` CR, the following custom resources are created on the clusters that match the selection criteria configured in the `PlacementRule` CR:

* `Namespace`
* `OperatorGroup`
* `Subscription`

[NOTE]
====
The default namespace for the {lvms} Operator is `openshift-lvm-storage`.
====

[role="_additional-resources"]
.Additional resources

* Red Hat Advanced Cluster Management for Kubernetes: Installing while connected online

* About the `LVMCluster` custom resource

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="static-and-dynamic-device-discovery-in-lvms_{context}"]
= Static and dynamic device discovery in {lvms}

[role="_abstract"]
You can use static or dynamic discovery policies to manage how block devices join your volume groups. Selecting the appropriate policy helps you automate storage expansion safely or preserve a locked, predictable storage footprint over time.

Static::
The Operator creates the volume group by using devices it finds at installation time. The Operator ignores devices discovered after the volume group exists.
+
Static discovery is the default policy for new volume groups. It eliminates operational risk by locking the device set after the Operator creates the volume group.
+
Combined with explicit device paths, it provides a fully deterministic storage configuration.
+
Without explicit paths, the Operator discovers devices only at creation time and then stops the set.

Dynamic::
The Operator continuously discovers and adds devices to the volume group on each reconciliation cycle.
+
Dynamic discovery remains the default for existing volume groups where the policy field is nil to maintain backward compatibility.
+
However, this policy can lead to unexpected behavior in production environments. Devices that appear after the initial setup because of hardware changes, driver reloads, or kernel device renaming are automatically added to the volume group.
+
This creates operational risk because the volume group composition becomes non-deterministic and depends on the runtime state of the node rather than explicit administrator intent.

[NOTE]
====
The Operator adds the `DeviceDiscoveryPolicy` field to the `DeviceClass` specification. If you explicitly set device paths in `deviceSelector.paths` or `deviceSelector.optionalPaths`, the cluster always uses those exact paths, and ignores your discovery policy setting.
====

The cluster status reports the effective policy by using `DeviceDiscoveryPolicyStatus`, which distinguishes three runtime states:

.Effective policy status values
[cols="1,2",options="header"]
|===
|Status value |Description

|`Preconfigured`
|Explicit device paths configuration by using `deviceSelector`. Discovery policy is not applicable.

|`RuntimeDynamic`
|No explicit paths. Discovery policy is Dynamic. The Operator continuously discovers devices.
|`RuntimeStatic`
|No explicit paths. Discovery policy is Static. The Operator discovers devices once at creation time.
|===

The following table shows the behavior matrix:

.Device discovery behavior by configuration
[cols="1,1,2",options="header"]
|===
|Explicit paths |Discovery policy |Effective behavior

|Yes
|Any / nil
|`Preconfigured`: The Operator honors the specified paths and ignores the discovery policy.

|No
|`Static`
|`RuntimeStatic`: The Operator locks the device set immediately after creating the volume group
|No
|`Dynamic`
|`RuntimeDynamic`: continuous discovery every 30 seconds

|No
|nil (new volume group)
|`RuntimeStatic`: defaults to Static

|No
|nil (existing volume group)
|`RuntimeDynamic`: defaults to Dynamic for backward compatibility
|===

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="static-mode-enforcement_{context}"]
= Static mode enforcement

[role="_abstract"]
To guarantee that your storage footprint remains predictable, the system enforces `static` mode rules after discovering initial devices. If a volume group already exists and lacks explicit paths, any newly attached devices are automatically isolated on an exclusion list to prevent unintended volume expansions.

This strict filtering behavior does not apply during the very first reconciliation cycle. During this initial pass, the Operator discovers all available devices to successfully create the volume group. Once created, the Operator locks the device set during all subsequent reconciliations.

The discovery policy also controls whether the controller re-queues for periodic device scanning:

.Requeue behavior by configuration
[cols="1,1",options="header"]
|===
|Configuration |Periodic requeue

|Explicit paths
|No: paths define the exact device set; changes trigger reconciliation by using the `LVMVolumeGroup` watch

|Dynamic without explicit paths
|Yes: every 30 seconds

|Static without explicit paths
|No: device set is locked after creation
|===

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="validation-rules-for-device-discovery-policy_{context}"]
= Validation rules for device discovery policy

[role="_abstract"]
To ensure your storage cluster deploys successfully and avoids misconfiguration errors, the validating webhook enforces strict rules when you create or update an `LVMCluster` custom resource.

Creation::
* If you define one device class without paths, a webhook warning appears. Avoid the default `Static` policy in production. Set `deviceDiscoveryPolicy` explicitly.
* If multiple device classes are defined, every device class must specify device paths. Auto-discovery without paths is not allowed with many device classes. The cluster cannot determine which devices belong to which class.
* If the `deviceDiscoveryPolicy` is empty and paths are missing, a webhook warning appears. Administrators must define the policy explicitly.

Updates::
No specific update restrictions apply to the `deviceDiscoveryPolicy` field. You can change it at any time.

The following table shows how the device discovery policy feature interacts with other features:

.Device discovery policy feature interactions
[cols="1,2",options="header"]
|===
|Feature |Interaction

|`forceWipeDevicesAndDestroyAllData`
|Works independently of the discovery policy. Devices are wiped before being added to the volume group, regardless of how they were discovered.

|Node selector
|Works independently. The discovery policy applies only to the set of devices found on nodes matching the selector.
|===

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvm-cluster-custom-resource-examples_{context}"]
= LVMCluster custom resource examples

[role="_abstract"]
You can configure the `deviceDiscoveryPolicy` field in your `LVMCluster` custom resource (CR) by using these examples to meet your specific storage requirements.

Explicit device paths (recommended for production)::
+
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
  storage:
    deviceClasses:
    - name: vg1
      deviceSelector:
        paths:
        - /dev/disk/by-id/scsi-SATA_VBOX_HARDDISK_VB12345678-90abcdef
        - /dev/disk/by-id/scsi-SATA_VBOX_HARDDISK_VBabcdef01-23456789
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
----
+
The discovery policy is not relevant here. Explicit paths always define the device set.

Static discovery without explicit paths::
+
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
  storage:
    deviceClasses:
    - name: vg1
      deviceDiscoveryPolicy: Static
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
----
+
The Operator discovers and adds all available devices to the volume group during the initial reconciliation. After the Operator creates the volume group, it adds no new devices.

Dynamic discovery without explicit paths (not recommended for production)::
+
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
  storage:
    deviceClasses:
    - name: vg1
      deviceDiscoveryPolicy: Dynamic
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
----
+
The Operator continuously discovers and adds devices to the volume group every 30 seconds. This setting is useful for development and testing. However, it might introduce operational risks in production environments.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvm-cluster-custom-resource-status-reporting_{context}"]
= LVM cluster custom resource status reporting

[role="_abstract"]
To view a list of excluded devices and the reason for their exclusion, use the `LVMVolumeGroupNodeStatus` custom resource (CR).

If static device discovery excludes a device, the status report displays the error in the following format:

[source,text]
----
<device> was not part of <vg_name> at creation (static device discovery enabled)
----

The `VGStatus.DeviceDiscoveryPolicy` parameter reports the effective discovery policy as one of the following values:

* `Preconfigured`
* `RuntimeDynamic`
* `RuntimeStatic`.

// About the LVMCluster custom resource

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="about-lvmcluster_{context}"]
= About the LVMCluster custom resource

You can configure the `LVMCluster` CR to perform the following actions:

* Create LVM volume groups that you can use to provision persistent volume claims (PVCs).
* Configure a list of devices that you want to add to the LVM volume groups.
* Configure the requirements to select the nodes on which you want to create an LVM volume group, and the thin pool configuration for the volume group.
* Force wipe the selected devices.

After you have installed {lvms}, you must create an `LVMCluster` custom resource (CR).

== Explanation of fields in the LVMCluster CR

The `LVMCluster` CR fields are described in the following table:

.`LVMCluster` CR fields
[cols=".^2,.^2,.^6a",options="header"]
|====

|Field|Type|Description

|`spec.storage.deviceClasses`
|`array`
|Contains the configuration to assign the local storage devices to the LVM volume groups.

LVM Storage creates a storage class and volume snapshot class for each device class that you create.

|`deviceClasses.name`
|`string`
|Specify a name for the LVM volume group (VG).

You can also configure this field to reuse a volume group that you created in the previous installation. For more information, see "Reusing a volume group from the previous LVM Storage installation".

|`deviceClasses.fstype`
|`string`
|Set this field to `ext4` or `xfs`. By default, this field is set to `xfs`.

|`deviceClasses.default`
|`boolean`
|Set this field to `true` to indicate that a device class is the default. Otherwise, you can set it to `false`. You can only configure a single default device class.

|`deviceClasses.nodeSelector`
|`object`
|Contains the configuration to choose the nodes on which you want to create the LVM volume group. If this field is empty, all nodes without no-schedule taints are considered.

On the control-plane node, {lvms} detects and uses the additional worker nodes when the new nodes become active in the cluster.

|`nodeSelector.nodeSelectorTerms`
|`array`
|Configure the requirements that are used to select the node.

|`deviceClasses.deviceSelector`
|`object`
|Contains the configuration to perform the following actions:

* Specify the paths to the devices that you want to add to the LVM volume group.
* Force wipe the devices that are added to the LVM volume group.

For more information, see "About adding devices to a volume group".

|`deviceSelector.paths`
|`array`
|Specify the device paths.

If the device path specified in this field does not exist, or the device is not supported by {lvms}, the `LVMCluster` CR moves to the `Failed` state.

|`deviceSelector.optionalPaths`
|`array`
| Specify the optional device paths.

If the device path specified in this field does not exist, or the device is not supported by {lvms}, {lvms} ignores the device without causing an error.

|`deviceSelector.
forceWipeDevicesAndDestroyAllData`
|`boolean`
|{lvms} uses only those disks that are empty and do not contain file system signatures. To ensure that the disks are empty and do not contain file system signatures, wipe the disks before using them.

To force wipe the selected devices, set this field to `true`. By default, this field is set to `false`.

[WARNING]
====
If this field is set to `true`, {lvms} wipes all previous data on the devices. Use this feature with caution.
====

Wiping the device can lead to inconsistencies in data integrity if any of the following conditions are met:

* The device is being used as swap space.
* The device is part of a RAID array.
* The device is mounted.

If any of these conditions are true, do not force wipe the disk. Instead, you must manually wipe the disk.
| deviceClasses.storageClassOptions | object | Optional. Allows customization of the StorageClass created for this device class, including reclaim policy, volume binding mode, additional parameters, and labels. For more information, see "StorageClass customization for LVMS device classes".

|`deviceClasses.thinPoolConfig`
|`object`
|Contains the configuration to create a thin pool in the LVM volume group.

If you exclude this field, logical volumes are thick provisioned.

Using thick-provisioned storage includes the following limitations:

* No copy-on-write support for volume cloning.
* No support for snapshot class.
* No support for over-provisioning. As a result, the provisioned capacity of `PersistentVolumeClaims` (PVCs) is immediately reduced from the volume group.
* No support for thin metrics. Thick-provisioned devices only support volume group metrics.

|`thinPoolConfig.name`
|`string`
|Specify a name for the thin pool.

|`thinPoolConfig.sizePercent`
|`integer`
|Specify the percentage of space in the LVM volume group for creating the thin pool.

By default, this field is set to 90. The minimum value that you can set is 10, and the maximum value is 90.

|`thinPoolConfig.overprovisionRatio`
|`integer`
|Specify a factor by which you can provision additional storage based on the available storage in the thin pool.

For example, if this field is set to 10, you can provision up to 10 times the amount of available storage in the thin pool.
You can modify this field after the LVM cluster has been created.

To update the parameter, do any of the following tasks:

* To edit the LVM Cluster, run the following command:
[source,terminal]
----
$ oc edit lvmcluster <lvmcluster_name>
----
* To apply a patch, run the following command:
[source,terminal]
----
$ oc patch lvmcluster <lvmcluster_name> -p <patch_file.yaml>
----
To disable over-provisioning, set this field to 1.

|`thinPoolConfig.chunkSize`
|`integer`
|Specifies the statically calculated chunk size for the thin pool. This field is only used when the `ChunkSizeCalculationPolicy` field is set to `Static`. The value for this field must be configured in the range of 64 KiB to 1 GiB because of the underlying limitations of `lvm2`.

If you do not configure this field and the `ChunkSizeCalculationPolicy` field is set to `Static`, the default chunk size is set to 128 KiB.

For more information, see "Overview of chunk size".

|`thinPoolConfig.chunkSizeCalculationPolicy`
|`string`
|Specifies the policy to calculate the chunk size for the underlying volume group. You can set this field to either `Static` or `Host`. By default, this field is set to `Static`.

If this field is set to `Static`, the chunk size is set to the value of the `chunkSize` field. If the `chunkSize` field is not configured, chunk size is set to 128 KiB.

If this field is set to `Host`, the chunk size is calculated based on the configuration in the `lvm.conf` file.

For more information, see "Limitations to configure the size of the devices used in LVM Storage".

|`thinPoolConfig.metadataSize`
|`integer`
|Specifies the metadata size for the thin pool. You can configure this field only when the `MetadataSizeCalculationPolicy` field is set to `Static`.

If this field is not configured, and the `MetadataSizeCalculationPolicy` field is set to `Static`, the default metadata size is set to 1 GiB.

The value for this field must be configured in the range of 2 MiB to 16 GiB due to the underlying limitations of `lvm2`. You can only increase the value of this field during updates.

|`thinPoolConfig.metadataSizeCalculationPolicy`
|`string`
|Specifies the policy to calculate the metadata size for the underlying volume group. You can set this field to either `Static` or `Host`. By default, this field is set to `Host`.

If this field is set to `Static`, the metadata size is calculated based on the value of the `thinPoolConfig.metadataSize` field.

If this field is set to `Host`, the metadata size is calculated based on the `lvm2` settings.
|====

[role="_additional-resources"]
.Additional resources

* Overview of chunk size

* Limitations to configure the size of the devices used in {lvms}

* Reusing a volume group from the previous {lvms} installation

* About adding devices to a volume group

* Adding worker nodes to {sno} clusters

// Limitations to configure the size of the devices to be used in LVM Storage
// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="limitations-to-configure-size-of-devices_{context}"]
= Limitations to configure the size of the devices used in {lvms}

[role="_abstract"]
To ensure your devices are compatible with storage operations, review the size configuration limitations in {lvms}. Adhering to these constraints prevents provisioning failures by ensuring selected devices meet the required capacity specifications.

When provisioning storage by using {lvms}, the following factors limit device size:

* The total storage size that you can provision is limited by the size of the underlying Logical Volume Manager (LVM) thin pool and the over-provisioning factor.
* The size of the logical volume depends on the size of the Physical Extent (PE) and the Logical Extent (LE).
** You can define the size of PE and LE during the physical and logical device creation.
** The default PE and LE size is 4 MiB.
** If the size of the PE is increased, the maximum size of the LVM is determined by the kernel limits and your disk space.
** The size limit for {op-system-base-full} 9 by using the default PE and LE size is 8 EB.
** The following are the minimum storage sizes that you can request for each file system type:
*** `block`: 8 MiB
*** `xfs`: 300 MiB
*** `ext4`: 32 MiB

The following tables describe the chunk size and volume size limits for static and host configurations:

.Tested configuration
[cols="1,1", width="100%", options="header"]
|====

|Parameter
|Value

|Chunk size
|128 KiB

|Maximum volume size
|32 TiB

|====

.Theoretical size limits for static configuration
[cols="1,1,1", width="100%", options="header"]
|====

|Parameter
|Minimum value
|Maximum value

|Chunk size
|64 KiB
|1 GiB

|Volume size
|Minimum size of the underlying {op-system-first} system.
|Maximum size of the underlying {op-system} system.

|====

.Theoretical size limits for a host configuration
[cols="1,1", width="100%", options="header"]
|====

|Parameter
|Value

|Chunk size
|This value is based on the configuration in the `lvm.conf` file. By default, the configuration sets the value to `128` KiB.

|Maximum volume size
|Equal to the maximum volume size of the underlying {op-system} system.

|Minimum volume size
|Equal to the minimum volume size of the underlying {op-system} system.

|====

// About adding devices to a volume group
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="about-adding-devices-to-a-vg_{context}"]
= About adding devices to a volume group

The `deviceSelector` field in the `LVMCluster` CR contains the configuration to specify the paths to the devices that you want to add to the Logical Volume Manager (LVM) volume group.

You can specify the device paths in the `deviceSelector.paths` field, the `deviceSelector.optionalPaths` field, or both. If you do not specify the device paths in both the `deviceSelector.paths` field and the `deviceSelector.optionalPaths` field, {lvms} adds the supported unused devices to the volume group (VG).

[IMPORTANT]
====
It is recommended to avoid referencing disks using symbolic naming, such as `/dev/sdX`, as these names may change across reboots within RHCOS. Instead, you must use stable naming schemes, such as `/dev/disk/by-path/` or `/dev/disk/by-id/`, to ensure consistent disk identification.

With this change, you might need to adjust existing automation workflows in the cases where monitoring collects information about the install device for each node.

For more information, see the {op-system-base} documentation.
====

You can add the path to the Redundant Array of Independent Disks (RAID) arrays in the `deviceSelector` field to integrate the RAID arrays with {lvms}. You can create the RAID array by using the `mdadm` utility. {lvms} does not support creating a software RAID.

[NOTE]
====
You can create a RAID array only during an OpenShift Container Platform installation. For information on creating a RAID array, see the following sections:

* "Configuring a RAID-enabled data volume" in "Additional resources".
* Creating a software RAID on an installed system
* Replacing a failed disk in RAID
* Repairing RAID disks
====

You can also add encrypted devices to the volume group. You can enable disk encryption on the cluster nodes during an OpenShift Container Platform installation. After encrypting a device, you can specify the path to the LUKS encrypted device in the `deviceSelector` field. For information on disk encryption, see "About disk encryption" and "Configuring disk encryption and mirroring".

The devices that you want to add to the VG must be supported by {lvms}. For information about unsupported devices, see "Devices not supported by {lvms}".

{lvms} adds the devices to the VG only if the following conditions are met:

* The device path exists.
* The device is supported by {lvms}.

[IMPORTANT]
====
After a device is added to the VG, you cannot remove the device.
====

{lvms} supports dynamic device discovery. If you do not add the `deviceSelector` field in the `LVMCluster` CR, {lvms} automatically adds the new devices to the VG when the devices are available.

[WARNING]
====
It is not recommended to add the devices to the VG through dynamic device discovery due to the following reasons:

* When you add a new device that you do not intend to add to the VG, {lvms} automatically adds this device to the VG through dynamic device discovery.
* If {lvms} adds a device to the VG through dynamic device discovery, {lvms} does not restrict you from removing the device from the node. Removing or updating the devices that are already added to the VG can disrupt the VG. This can also lead to data loss and necessitate manual node remediation.
====

[role="_additional-resources"]
.Additional resources

* Configuring a RAID-enabled data volume

* About disk encryption

* Configuring disk encryption and mirroring

* Devices not supported by {lvms}

// About removing devices and device classes from a volume group
// Module included in the following assemblies:
//
// storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="about-removing-devices-deviceclasses-from-a-vg_{context}"]
= About removing devices and device classes from a volume group

[role="_abstract"]
The `deviceSelector` field in the `LVMCluster` CR contains the configuration to specify the paths to the devices that you can remove from the Logical Volume Manager (LVM) volume group.

[id="removing-device-paths-in-deviceselectorpaths-field_{context}"]
== Removing the device paths in the deviceSelector.paths field

You can remove the device paths in the `deviceSelector.paths` field.

[IMPORTANT]
====
Ensure that the following criteria are met before removing device paths:

* The device that you want to remove is empty. You can use the `pvdisplay` command to see attributes of physical volumes (PVs) used in LVM.

* At least one additional device is specified in the `deviceSelector.paths` field.
====

[id="removing-device-classes-from-lvmcluster_{context}"]
== Removing the deviceClass from the LVMCluster

You can also remove the `deviceClass` object from the `LVMCluster` resource. For device class deletion, there is no need to delete `deviceSelector.paths` object.

[IMPORTANT]
====
Ensure that the following criteria are met before removing a device class:

* The `deviceClasses.default` field is set to `false`.

* The disks specified in the `deviceSelector.paths` field are empty.

* At least one additional device class is specified in the `storage` field.
====

// Devices not supported by LVMS
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-unsupported-devices_{context}"]
= Devices not supported by {lvms}

When you are adding the device paths in the `deviceSelector` field of the `LVMCluster` custom resource (CR), ensure that the devices are supported by {lvms}. If you add paths to the unsupported devices, {lvms} excludes the devices to avoid complexity in managing logical volumes.

If you do not specify any device path in the `deviceSelector` field, {lvms} adds only the unused devices that it supports.

[NOTE]
====
To get information about the devices, run the following command:
[source,terminal]
----
$ lsblk --paths --json -o \
NAME,ROTA,TYPE,SIZE,MODEL,VENDOR,RO,STATE,KNAME,SERIAL,PARTLABEL,FSTYPE
----
====

{lvms} does not support the following devices:

Read-only devices:: Devices with the `ro` parameter set to `true`.

Suspended devices:: Devices with the `state` parameter set to `suspended`.

ROM devices:: Devices with the `type` parameter set to `rom`.

LVM partition devices:: Devices with the `type` parameter set to `lvm`.

Devices with invalid partition labels:: Devices with the `partlabel` parameter set to `bios`, `boot`, or `reserved`.

Devices with an invalid filesystem:: Devices with the `fstype` parameter set to any value other than `null` or `LVM2_member`.
+
[IMPORTANT]
====
{lvms} supports devices with `fstype` parameter set to `LVM2_member` only if the devices do not contain children devices.
====

Devices that are part of another volume group:: To get the information about the volume groups of the device, run the following command:
+
[source, terminal]
----
$ pvs <device-name> <1>
----
<1> Replace `<device-name>` with the device name.

Devices with bind mounts:: To get the mount points of a device, run the following command:
+
[source, terminal]
----
$ cat /proc/1/mountinfo | grep <device-name> <1>
----
<1> Replace `<device-name>` with the device name.

Devices that contain children devices::

[NOTE]
====
It is recommended to wipe the device before using it in {lvms} to prevent unexpected behavior.
====

// About creating an LVMCluster custom resource

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="about-creating-lvmcluster-cr_{context}"]
= Ways to create an LVMCluster custom resource

You can create an `LVMCluster` custom resource (CR) by using the OpenShift CLI (`oc`) or the OpenShift Container Platform web console. If you have installed {lvms} by using {rh-rhacm-first}, you can also create an `LVMCluster` CR by using {rh-rhacm}.

[IMPORTANT]
====
You must create the `LVMCluster` CR in the same namespace where you installed the {lvms} Operator, which is `openshift-storage` by default.
====

Upon creating the `LVMCluster` CR, {lvms} creates the following system-managed CRs:

* A `storageClass` and `volumeSnapshotClass` for each device class.
+
[NOTE]
====
{lvms} configures the name of the storage class and volume snapshot class in the format `lvms-<device_class_name>`, where, `<device_class_name>` is the value of the `deviceClasses.name` field in the `LVMCluster` CR. For example, if the `deviceClasses.name` field is set to vg1, the name of the storage class and volume snapshot class is `lvms-vg1`.
====

* `LVMVolumeGroup`: This CR is a specific type of persistent volume (PV) that is backed by an LVM volume group. It tracks the individual volume groups across multiple nodes.
* `LVMVolumeGroupNodeStatus`: This CR tracks the status of the volume groups on a node.

// Reusing a volume group from the previous LVM Storage installation
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-reusing-vg-from-prev-installation_{context}"]
= Reusing a volume group from the previous LVM Storage installation

You can reuse an existing volume group (VG) from the previous {lvms} installation instead of creating a new VG.

You can only reuse a VG but not the logical volume associated with the VG.

[IMPORTANT]
====
You can perform this procedure only while creating an `LVMCluster` custom resource (CR).
====

.Prerequisites

* The VG that you want to reuse must not be corrupted.
* The VG that you want to reuse must have the `lvms` tag. For more information on adding tags to LVM objects, see Grouping LVM objects with tags.

.Procedure

. Open the `LVMCluster` CR YAML file.

. Configure the `LVMCluster` CR parameters as described in the following example:
+
.Example `LVMCluster` CR YAML file
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
# ...
  storage:
    deviceClasses:
    - name: vg1  <1>
      fstype: ext4 <2>
      default: true
      deviceSelector: <3>
# ...
        forceWipeDevicesAndDestroyAllData: false <4>
      thinPoolConfig: <5>
# ...
      nodeSelector: <6>
# ...
----
<1> Set this field to the name of a VG from the previous {lvms} installation.
<2> Set this field to `ext4` or `xfs`. By default, this field is set to `xfs`.
<3> You can add new devices to the VG that you want to reuse by specifying the new device paths in the `deviceSelector` field. If you do not want to add new devices to the VG, ensure that the `deviceSelector` configuration in the current {lvms} installation is same as that of the previous {lvms} installation.
<4> If this field is set to `true`, {lvms} wipes all the data on the devices that are added to the VG.
<5> To retain the `thinPoolConfig` configuration of the VG that you want to reuse, ensure that the `thinPoolConfig` configuration in the current {lvms} installation is same as that of the previous {lvms} installation. Otherwise, you can configure the `thinPoolConfig` field as required.
<6> Configure the requirements to choose the nodes on which you want to create the LVM volume group. If this field is empty, all nodes without no-schedule taints are considered.

. Save the `LVMCluster` CR YAML file.

[NOTE]
====
To view the devices that are part a volume group, run the following command:
[source,terminal]
----
$ pvs -S vgname=<vg_name> <1>
----
<1> Replace `<vg_name>` with the name of the volume group.
====

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-creating-lvms-cluster-using-cli_{context}"]
= Creating an LVMCluster CR by using the CLI

You can create an `LVMCluster` custom resource (CR) on a worker node using the OpenShift CLI (`oc`).

[IMPORTANT]
====
You can only create a single instance of the `LVMCluster` custom resource (CR) on an OpenShift Container Platform cluster.
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to OpenShift Container Platform as a user with `cluster-admin` privileges.

* You have installed {lvms}.

* You have installed a worker node in the cluster.

* You read the "About the LVMCluster custom resource" section.

.Procedure

. Create an `LVMCluster` custom resource (CR) YAML file:
+
.Example `LVMCluster` CR YAML file
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
# ...
  storage:
    deviceClasses: <1>
# ...
      nodeSelector: <2>
# ...
      deviceSelector: <3>
# ...
      thinPoolConfig: <4>
# ...
----
<1> Contains the configuration to assign the local storage devices to the LVM volume groups.
<2> Contains the configuration to choose the nodes on which you want to create the LVM volume group. If this field is empty, all nodes without no-schedule taints are considered.
<3> Contains the configuration to specify the paths to the devices that you want to add to the LVM volume group, and force wipe the devices that are added to the LVM volume group.
<4> Contains the configuration to create a thin pool in the LVM volume group. If you exclude this field, logical volumes are thick provisioned.

. Create the `LVMCluster` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>
----
+
.Example output
[source,terminal]
----
lvmcluster/lvmcluster created
----

.Verification

. Check that the `LVMCluster` CR is in the `Ready` state:
+
[source, terminal]
----
$ oc get lvmclusters.lvm.topolvm.io -o jsonpath='{.items[*].status}' -n <namespace>
----
+
.Example output
[source,json]
----
{"deviceClassStatuses": <1>
[
  {
    "name": "vg1",
    "nodeStatus": [ <2>
        {
            "devices": [ <3>
                "/dev/nvme0n1",
                "/dev/nvme1n1",
                "/dev/nvme2n1"
            ],
            "node": "kube-node", <4>
            "status": "Ready" <5>
        }
    ]
  }
]
"state":"Ready"} <6>
----
<1> The status of the device class.
<2> The status of the LVM volume group on each node.
<3> The list of devices used to create the LVM volume group.
<4> The node on which the device class is created.
<5> The status of the LVM volume group on the node.
<6> The status of the `LVMCluster` CR.
+
[NOTE]
====
If the `LVMCluster` CR is in the `Failed` state, you can view the reason for failure in the `status` field.

Example of `status` field with the reason for failue:
[source, yaml]
----
status:
  deviceClassStatuses:
    - name: vg1
      nodeStatus:
        - node: my-node-1.example.com
          reason: no available devices found for volume group
          status: Failed
  state: Failed
----
====

. Optional: To view the storage classes created by {lvms} for each device class, run the following command:
+
[source,terminal]
----
$ oc get storageclass
----
+
.Example output
[source, terminal]
----
NAME          PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
lvms-vg1      topolvm.io           Delete          WaitForFirstConsumer   true                   31m
----

. Optional: To view the volume snapshot classes created by {lvms} for each device class, run the following command:
+
[source,terminal]
----
$ oc get volumesnapshotclass
----
+
.Example output
[source, terminal]
----
NAME          DRIVER               DELETIONPOLICY   AGE
lvms-vg1      topolvm.io           Delete           24h
----

[role="_additional-resources"]
.Additional resources

* About the `LVMCluster` custom resource

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-creating-lvms-cluster-using-web-console_{context}"]
= Creating an LVMCluster CR by using the web console

You can create an `LVMCluster` CR on a worker node using the OpenShift Container Platform web console.

[IMPORTANT]
====
You can only create a single instance of the `LVMCluster` custom resource (CR) on an OpenShift Container Platform cluster.
====

.Prerequisites

* You have access to the OpenShift Container Platform cluster with `cluster-admin` privileges.

* You have installed {lvms}.

* You have installed a worker node in the cluster.

* You read the "About the LVMCluster custom resource" section.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Click *Ecosystem* -> *Installed Operators*.
. In the `openshift-lvm-storage` namespace, click *{lvms}*.
. Click *Create LVMCluster* and select either *Form view* or *YAML view*.
. Configure the required `LVMCluster` CR parameters.
. Click *Create*.
. Optional: If you want to edit the `LVMCLuster` CR, perform the following actions:
.. Click the *LVMCluster* tab.
.. From the *Actions* menu, select *Edit LVMCluster*.
.. Click *YAML* and edit the required `LVMCLuster` CR parameters.
.. Click *Save*.

.Verification

. On the *LVMCLuster* page, check that the `LVMCluster` CR is in the `Ready` state.
. Optional: To view the available storage classes created by {lvms} for each device class, click *Storage* -> *StorageClasses*.
. Optional: To view the available volume snapshot classes created by {lvms} for each device class, click *Storage* -> *VolumeSnapshotClasses*.

[role="_additional-resources"]
.Additional resources

* About the `LVMCluster` custom resource

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-creating-lvmcluster-using-rhacm_{context}"]
= Creating an LVMCluster CR by using {rh-rhacm}

After you have installed {lvms} by using {rh-rhacm}, you must create an `LVMCluster` custom resource (CR).

.Prerequisites

* You have installed {lvms} by using {rh-rhacm}.
* You have access to the {rh-rhacm} cluster using an account with `cluster-admin` permissions.
* You read the "About the LVMCluster custom resource" section.

.Procedure

. Log in to the {rh-rhacm} CLI using your OpenShift Container Platform credentials.

. Create a `ConfigurationPolicy` CR YAML file with the configuration to create an `LVMCluster` CR:
+
.Example `ConfigurationPolicy` CR YAML file to create an `LVMCluster` CR
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: ConfigurationPolicy
metadata:
  name: lvms
  namespace: openshift-lvm-storage
spec:
  object-templates:
  - complianceType: musthave
    objectDefinition:
      apiVersion: lvm.topolvm.io/v1alpha1
      kind: LVMCluster
      metadata:
        name: my-lvmcluster
        namespace: openshift-lvm-storage
      spec:
        storage:
          deviceClasses: <1>
# ...
            deviceSelector: <2>
# ...
            thinPoolConfig: <3>
# ...
            nodeSelector: <4>
# ...
  remediationAction: enforce
  severity: low
----
<1> Contains the configuration to assign the local storage devices to the LVM volume groups.
<2> Contains the configuration to specify the paths to the devices that you want to add to the LVM volume group, and force wipe the devices that are added to the LVM volume group.
<3> Contains the configuration to create a thin pool in the LVM volume group. If you exclude this field, logical volumes are thick provisioned.
<4> Contains the configuration to choose the nodes on which you want to create the LVM volume groups. If this field is empty, then all nodes without no-schedule taints are considered.

. Create the `ConfigurationPolicy` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name> -n <cluster_namespace> <1>
----
<1> Namespace of the OpenShift Container Platform cluster on which {lvms} is installed.

[role="_additional-resources"]
.Additional resources

* Red Hat Advanced Cluster Management for Kubernetes: Installing while connected online

* About the `LVMCluster` custom resource

// Deleting the LVMCluster custom resource

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="about-deleting-lvmcluster-cr_{context}"]
= Ways to delete an LVMCluster custom resource

You can delete an `LVMCluster` custom resource (CR) by using the OpenShift CLI (`oc`) or the OpenShift Container Platform web console. If you have installed {lvms} by using {rh-rhacm-first}, you can also delete an `LVMCluster` CR by using {rh-rhacm}.

Upon deleting the `LVMCluster` CR, {lvms} deletes the following CRs:

* `storageClass`
* `volumeSnapshotClass`
* `LVMVolumeGroup`
* `LVMVolumeGroupNodeStatus`

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-deleting-lvmcluster-using-cli_{context}"]
= Deleting an LVMCluster CR by using the CLI

You can delete the `LVMCluster` custom resource (CR) using the OpenShift CLI (`oc`).

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.
* You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by {lvms}. You have also deleted the applications that are using these resources.

.Procedure

. Log in to the OpenShift CLI (`oc`).
. Delete the `LVMCluster` CR by running the following command:
+
[source,terminal]
----
$ oc delete lvmcluster <lvm_cluster_name> -n <namespace>
----

.Verification

* To verify that the `LVMCluster` CR has been deleted, run the following command:
+
[source,terminal]
----
$ oc get lvmcluster -n <namespace>
----
+
.Example output
[source,terminal]
----
No resources found in openshift-lvm-storage namespace.
----

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-deleting-lvmcluster-using-web-console_{context}"]
= Deleting an LVMCluster CR by using the web console

You can delete the `LVMCluster` custom resource (CR) using the OpenShift Container Platform web console.

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.
* You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by {lvms}. You have also deleted the applications that are using these resources.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Click *Ecosystem* -> *Installed Operators* to view all the installed Operators.
. Click *{lvms}* in the `openshift-lvm-storage` namespace.
. Click the *LVMCluster* tab.
. From the *Actions*, select *Delete LVMCluster*.
. Click *Delete*.

.Verification

* On the `LVMCLuster` page, check that the `LVMCluster` CR has been deleted.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-deleting-lvmcluster-using-rhacm_{context}"]
= Deleting an LVMCluster CR by using {rh-rhacm}

If you have installed {lvms} by using {rh-rhacm-first}, you can delete an `LVMCluster` CR by using {rh-rhacm}.

.Prerequisites

* You have access to the {rh-rhacm} cluster as a user with `cluster-admin` permissions.
* You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by {lvms}. You have also deleted the applications that are using these resources.

.Procedure

. Log in to the {rh-rhacm} CLI using your OpenShift Container Platform credentials.
. Delete the `ConfigurationPolicy` CR YAML file that was created for the `LVMCluster` CR:
+
[source,terminal]
----
$ oc delete -f <file_name> -n <cluster_namespace> <1>
----
<1> Namespace of the OpenShift Container Platform cluster on which {lvms} is installed.

. Create a `Policy` CR YAML file to delete the `LVMCluster` CR:
+
.Example `Policy` CR to delete the `LVMCluster` CR
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: policy-lvmcluster-delete
  annotations:
    policy.open-cluster-management.io/standards: NIST SP 800-53
    policy.open-cluster-management.io/categories: CM Configuration Management
    policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
spec:
  remediationAction: enforce
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        kind: ConfigurationPolicy
        metadata:
          name: policy-lvmcluster-removal
        spec:
          remediationAction: enforce <1>
          severity: low
          object-templates:
            - complianceType: mustnothave
              objectDefinition:
                kind: LVMCluster
                apiVersion: lvm.topolvm.io/v1alpha1
                metadata:
                  name: my-lvmcluster
                  namespace: openshift-lvm-storage <2>
---
apiVersion: policy.open-cluster-management.io/v1
kind: PlacementBinding
metadata:
  name: binding-policy-lvmcluster-delete
placementRef:
  apiGroup: apps.open-cluster-management.io
  kind: PlacementRule
  name: placement-policy-lvmcluster-delete
subjects:
  - apiGroup: policy.open-cluster-management.io
    kind: Policy
    name: policy-lvmcluster-delete
---
apiVersion: apps.open-cluster-management.io/v1
kind: PlacementRule
metadata:
  name: placement-policy-lvmcluster-delete
spec:
  clusterConditions:
    - status: "True"
      type: ManagedClusterConditionAvailable
  clusterSelector: <3>
    matchExpressions:
      - key: mykey
        operator: In
        values:
          - myvalue
----
<1> The `spec.remediationAction` in `policy-template` is overridden by the preceding parameter value for `spec.remediationAction`.
<2> This `namespace` field must have the `openshift-lvm-storage` value.
<3> Configure the requirements to select the clusters. {lvms} is uninstalled on the clusters that match the selection criteria.

. Create the `Policy` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name> -n <namespace>
----

. Create a `Policy` CR YAML file to check if the `LVMCluster` CR has been deleted:
+
.Example `Policy` CR to check if the `LVMCluster` CR has been deleted
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: policy-lvmcluster-inform
  annotations:
    policy.open-cluster-management.io/standards: NIST SP 800-53
    policy.open-cluster-management.io/categories: CM Configuration Management
    policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
spec:
  remediationAction: inform
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        kind: ConfigurationPolicy
        metadata:
          name: policy-lvmcluster-removal-inform
        spec:
          remediationAction: inform <1>
          severity: low
          object-templates:
            - complianceType: mustnothave
              objectDefinition:
                kind: LVMCluster
                apiVersion: lvm.topolvm.io/v1alpha1
                metadata:
                  name: my-lvmcluster
                  namespace: openshift-lvm-storage <2>
---
apiVersion: policy.open-cluster-management.io/v1
kind: PlacementBinding
metadata:
  name: binding-policy-lvmcluster-check
placementRef:
  apiGroup: apps.open-cluster-management.io
  kind: PlacementRule
  name: placement-policy-lvmcluster-check
subjects:
  - apiGroup: policy.open-cluster-management.io
    kind: Policy
    name: policy-lvmcluster-inform
---
apiVersion: apps.open-cluster-management.io/v1
kind: PlacementRule
metadata:
  name: placement-policy-lvmcluster-check
spec:
  clusterConditions:
    - status: "True"
      type: ManagedClusterConditionAvailable
  clusterSelector:
    matchExpressions:
      - key: mykey
        operator: In
        values:
          - myvalue
----
<1> The `policy-template` `spec.remediationAction` is overridden by the preceding parameter value for `spec.remediationAction`.
<2> The `namespace` field must have the `openshift-lvm-storage` value.

. Create the `Policy` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name> -n <namespace>
----

.Verification

* Check the status of the `Policy` CRs by running the following command:
+
[source,terminal]
----
$ oc get policy -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME                       REMEDIATION ACTION   COMPLIANCE STATE   AGE
policy-lvmcluster-delete   enforce              Compliant          15m
policy-lvmcluster-inform   inform               Compliant          15m
----
+
[IMPORTANT]
====
The `Policy` CRs must be in `Compliant` state.
====

// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc
// * microshift_storage/dynamic-provisioning-microshift.adoc

[id="deleting-an-lvm-cluster_{context}"]
= Deleting an LVMCluster

[role="_abstract"]
When you delete an `LVMCluster` custom resource (CR), the Operator enforces deletion gates to prevent data loss. The gates that apply depend on the reclaim policy that is configured for the storage class.

.Prerequisites

* You have administrative access to the cluster.
* You have identified the reclaim policy in use: `Delete` or `Retain`.

.Procedure

. Delete all Persistent Volume Claims (PVCs) that reference LVM `StorageClass` resources.
+
If PVCs that reference LVM StorageClasses still exist, the Operator blocks `LVMCluster` deletion and generates a `DeletionPending` event:
+
[source,terminal]
----
found PVCs provisioned by LVMS, waiting 10s for their deletion
----

. Back up any data before deleting PVCs.

.. List the PVCs that use the LVM StorageClass by running the following command:
+
[source,terminal]
----
$ oc get pvc -A -o custom-columns='NAMESPACE:.metadata.namespace,NAME:.metadata.name,SC:.spec.storageClassName' | grep lvms-vg1
----

.. Delete the PVCs by running the following command:
+
[source,terminal]
----
$ oc delete pvc <pvc_name> -n <namespace>
----
+
With the `Delete` reclaim policy, deleting the PVCs automatically removes the persistent volumes (PVs) and on-disk logical volumes. After all PVCs are removed, `LVMCluster` deletion completes automatically. No further action is required.

. If you use the `Retain` reclaim policy, delete the retained PVs.
+
After you delete PVCs, if the reclaim policy is `Retain`, the Operator blocks `LVMCluster` deletion and generates a `DeletionPending` event:
+
[source,terminal]
----
found PVs with Retain policy from LVMS, waiting 10s for manual cleanup
----

.. List the retained PVs by running the following command:
+
[source,terminal]
----
$ oc get pv -o custom-columns='NAME:.metadata.name,SC:.spec.storageClassName' | grep lvms-vg1
----

.. Delete the PVs by running the following command:
+
[source,terminal]
----
$ oc delete pv <pv_name>
----

. If you are using the `Retain` reclaim policy, delete the TopoLVM `LogicalVolume` custom resources.
+
After you delete PV objects from Kubernetes, the underlying logical volumes remain on disk because the `Retain` policy preserved them. The VG Manager detects this and generates a `ManualCleanupRequired` event:
+
[source,terminal]
----
Warning  ManualCleanupRequired  volume group vg1 has retained logical volumes [pvc-abc123]; manual cleanup required before deletion can proceed
----

. Deleting the `LogicalVolume` custom resources triggers on-disk logical volume cleanup.

.. List the `LogicalVolume` custom resources by running the following command:
+
[source,terminal]
----
$ oc get logicalvolumes
----

.. Delete the `LogicalVolume` custom resources for your device class by running the following command:
+
[source,terminal]
----
$ oc delete logicalvolume <lv_name>
----

.Verification

* Verify that the `LVMCluster` deletion completed by confirming the resource no longer exists by running the following command:
+
[source,terminal]
----
$ oc get lvmcluster -A
----

//Provisioning
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-provisioning-storage-using-lvms_{context}"]
= Provisioning storage

After you have created the LVM volume groups using the `LVMCluster` custom resource (CR), you can provision the storage by creating persistent volume claims (PVCs).

The following are the minimum storage sizes that you can request for each file system type:

* `block`: 8 MiB
* `xfs`: 300 MiB
* `ext4`: 32 MiB

To create a PVC, you must create a `PersistentVolumeClaim` object.

.Prerequisites

* You have created an `LVMCluster` CR.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Create a `PersistentVolumeClaim` object:
+
.Example `PersistentVolumeClaim` object
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: lvm-block-1 <1>
  namespace: default
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem <2>
  resources:
    requests:
      storage: 10Gi <3>
    limits:
      storage: 20Gi <4>
  storageClassName: lvms-vg1 <5>
----
<1> Specify a name for the PVC.
<2> To create a file PVC, set this field to `Filesystem`. To create a block PVC, set this field to `Block`.
<3> Specify the storage size. If the value is less than the minimum storage size, the requested storage size is rounded to the minimum storage size. The total storage size you can provision is limited by the size of the Logical Volume Manager (LVM) thin pool and the over-provisioning factor.
<4> Optional: Specify the storage limit. Set this field to a value that is greater than or equal to the minimum storage size. Otherwise, PVC creation fails with an error.
<5> The value of the `storageClassName` field must be in the format `lvms-<device_class_name>` where `<device_class_name>` is the value of the `deviceClasses.name` field in the `LVMCluster` CR.
For example, if the `deviceClasses.name` field is set to `vg1`, you must set the `storageClassName` field to `lvms-vg1`.
+
[NOTE]
====
The `volumeBindingMode` field of the storage class is set to `WaitForFirstConsumer`.
====

. Create the PVC by running the following command:
+
[source,terminal]
----
# oc create -f <file_name> -n <application_namespace>
----
+
[NOTE]
====
The created PVCs remain in `Pending` state until you deploy the pods that use them.
====

.Verification

* To verify that the PVC is created, run the following command:
+
[source, terminal]
----
$ oc get pvc -n <namespace>
----
+
.Example output
+
[source, terminal]
----
NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
lvm-block-1   Bound    pvc-e90169a8-fd71-4eea-93b8-817155f60e47   1Gi        RWO            lvms-vg1       5s
----

// Module included in the following assemblies:
//
// * storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="storageclass-customization-for-lvms-device-classes_{context}"]
= StorageClass customization for LVMS device classes

[role="_abstract"]
You can customize the StorageClass for each device class by using the optional storageClassOptions field in the `LVMCluster` custom resource (CR).

Before, Logical Volume Manager Storage (LVMS) automatically created a StorageClass for each device class without allowing modification. If you attempted to manually edit a generated StorageClass, the Operator overwrote your changes during the next reconciliation loop.

The `storageClassOptions` field lets you control four properties of the generated StorageClass:

* `reclaimPolicy`
* `volumeBindingMode`
* `additionalParameters`
* `additionalLabels`

If you omit `storageClassOptions`, LVMS creates the StorageClass with the same defaults as in previous versions. Existing `LVMCluster` configurations are fully compatible with earlier versions.

[NOTE]
====
No user action is required after upgrading. The `storageClassOptions` field is optional, and default values match the behavior before this feature was introduced.
====

// Module included in the following assemblies:
//
// * storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="storageclass-options_{context}"]
= StorageClass options

[role="_abstract"]
You can configure custom StorageClass behaviors by defining the `storageClassOptions` field in your device class specification.

If you set an empty configuration (storageClassOptions: {}) or omit the field entirely, the Operator uses the following default settings:

.StorageClass Options Reference
[cols="1,1,1,3,2", options="header"]
|===
| Field | Type | Immutable | Description | Example

| `reclaimPolicy`
| `string`
| Yes
a|
Controls what happens to the PersistentVolume (PV) and its underlying logical volume when the PersistentVolumeClaim (PVC) is deleted.

Allowed values: `Delete` (default), `Retain`

When set to `Retain`, deleting a PVC does not delete the PV or the underlying logical volume on disk. Data is preserved, useful for data protection scenarios where accidental PVC deletion must not cause data loss. Manual cleanup is required before you can delete the `LVMCluster`.

When set to `Delete`, both the PV and the on-disk logical volume are removed when the PVC is deleted.
a|
[source,yaml]
----
storageClassOptions:
  reclaimPolicy: Retain
----

| `volumeBindingMode`
| `string`
| Yes
a|
Controls when volume binding and dynamic provisioning occur.

Allowed values: `WaitForFirstConsumer` (default), `Immediate`

`WaitForFirstConsumer` delays PV provisioning until a pod that uses the PVC is scheduled, enabling topology-aware scheduling where LVMS creates the PV on the node where the pod will run.

`Immediate` provisions and binds the PV as soon as the PVC is created, without waiting for a consumer pod. On multi-node clusters, PVs might be provisioned on nodes where the consuming pod cannot run. Use `Immediate` only on single-node clusters or when node affinity is managed externally.
a|
[source,yaml]
----
storageClassOptions:
  volumeBindingMode: Immediate
----

| `additionalParameters`
| `map[string]string`
| Yes
a|
Adds custom key-value pairs to the `StorageClass .parameters` map.

Default: `{}` (empty). Maximum entries: 16.

StorageClass parameters are passed to the CSI driver (TopoLVM) during volume provisioning. TopoLVM recognizes only `topolvm.io/device-class` and `csi.storage.k8s.io/fstype`. Use `additionalParameters` for forward-compatibility or for parameters consumed by other Kubernetes components.

The following keys are managed by LVMS and are rejected at admission:

* `topolvm.io/device-class` — automatically set to the device class name
* `csi.storage.k8s.io/fstype` — automatically set from the `fstype` field on the device class

[IMPORTANT]
====
To change the filesystem type, use the `fstype` field on the device class directly. Do not use `additionalParameters`.
====
a|
[source,yaml]
----
storageClassOptions:
  additionalParameters:
    custom-param-key: custom-param-value
----

| `additionalLabels`
| `map[string]string`
| No
a|
Adds custom labels to the StorageClass metadata.

Default: none. Maximum entries: 16.

Use for organizational tagging, cluster policy integration, or monitoring. When you remove a label from `additionalLabels`, the operator removes it from the StorageClass during the next reconciliation. Labels added directly by other tools are not affected.

The following label keys are reserved and cannot be set through `additionalLabels`:

* `app.kubernetes.io/managed-by`
* `app.kubernetes.io/part-of`
* `app.kubernetes.io/name`
* `app.kubernetes.io/component`
* Any key with the prefix `owned-by.topolvm.io/`
a|
[source,yaml]
----
storageClassOptions:
  additionalLabels:
    environment: production
    team: storage
----

|===

// Module included in the following assemblies:
//
// * storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="updating-lvm-cluster-labels_{context}"]
= Updating LVM cluster labels

[role="_abstract"]
To organize and categorize your storage resources, you can update, remove, or clear custom storage class labels by patching the `LVMCluster` custom resource. Labels are the only configuration field that you can modify after cluster creation.

.Procedure

. Patch the `LVMCluster` resource to update `additionalLabels` by running the following command:
+
[source,terminal]
----
$ oc -n openshift-lvm-storage patch lvmcluster <name> --type=json \
  -p '[{"op":"replace","path":"/spec/storage/deviceClasses/0/storageClassOptions/additionalLabels","value":{"environment":"staging"}}]'
----

. To remove a specific label, update `additionalLabels` without the label you want to remove. The Operator removes the label from the `StorageClass` during the next reconciliation.

. To remove all custom labels, set `additionalLabels` to an empty map `{}`.
+
[NOTE]
====
The Operator preserves labels that you add directly to the `StorageClass`, for example with `oc label storageclass lvms-vg1 my-label=value`. The Operator prunes only the labels that you manage through the `additionalLabels` field in the `LVMCluster` custom resource (CR) when you remove them from the CR.
====

// Module included in the following assemblies:
//
// * storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="sample-lvm-cluster-configuration-with-storage-class-option_{context}"]
= Sample LVM cluster configuration with storage class option

[role="_abstract"]
Use these examples to configure `storageClassOptions` in your `LVMCluster` custom resource (CR) to meet your specific storage requirements.

.Default StorageClass behavior (no options)
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
----

This produces a `StorageClass` with `reclaimPolicy: Delete` and `volumeBindingMode: WaitForFirstConsumer`, which is the same as the behavior before this feature.

.Retain policy for data protection
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      storageClassOptions:
        reclaimPolicy: Retain
----

.Immediate binding for pre-provisioning
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      storageClassOptions:
        volumeBindingMode: Immediate
----

.All options configured together
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      storageClassOptions:
        reclaimPolicy: Retain
        volumeBindingMode: WaitForFirstConsumer
        additionalParameters:
          custom-key: custom-value
        additionalLabels:
          environment: production
          team: storage
----

.Multiple device classes with different options
[source,yaml]
----
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg-fast
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      deviceSelector:
        paths:
        - /dev/nvme0n1
      storageClassOptions:
        reclaimPolicy: Delete
        volumeBindingMode: WaitForFirstConsumer
        additionalLabels:
          tier: fast
    - name: vg-archive
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      deviceSelector:
        paths:
        - /dev/sda
      storageClassOptions:
        reclaimPolicy: Retain
        volumeBindingMode: WaitForFirstConsumer
        additionalLabels:
          tier: archive
----

For a device class named `vg1` with the full configuration, LVMS generates a `StorageClass` named `lvms-vg1` with the following structure:

[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: lvms-vg1
  annotations:
    description: "Provides RWO and RWOP Filesystem & Block volumes"
    storageclass.kubernetes.io/is-default-class: "true"
  labels:
    environment: production
    team: storage
provisioner: topolvm.io
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  custom-key: custom-value
  topolvm.io/device-class: vg1
  csi.storage.k8s.io/fstype: xfs
----

The `StorageClass` name always follows the convention `lvms-<device_class_name>`.

// Module included in the following assemblies:
//
// * storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="immutable-fields-of-the-storage-class-options_{context}"]
= Immutable fields of the storage class options

[role="_abstract"]
After you create the `LVMCluster`, you cannot change the value of the some of the `storageClassOptions` fields such as `reclaimPolicy`, `volumeBindingMode`, and `additionalParameters`. This mirrors the behavior of Kubernetes StorageClasses, which do not allow changes to these fields after creation.

If you attempt to modify an immutable field, the API server rejects the request:

[source,terminal]
----
Invalid value: "object": reclaimPolicy is immutable once set
----

There is no way to patch or update immutable fields in place. To change an immutable field, you must delete the `LVMCluster` and recreate it with the new values.

For example, you cannot change the filesystem type through `additionalParameters`.  The `csi.storage.k8s.io/fstype` parameter is managed by LVMS and is rejected at admission if set through `additionalParameters`. To use `ext4` instead of the default `xfs`, use the `fstype` field on the device class:

[source,yaml]
----
deviceClasses:
- name: vg1
  fstype: ext4
----
However, the `fstype` field is also immutable after creation.

[NOTE]
====
The deletion gates require all PVCs and, for the `Retain` policy, all PVs to be removed before the `LVMCluster` can be deleted. After you recreate the `LVMCluster` with the new values, new PVCs use the updated StorageClass configuration.
====

// Module included in the following assemblies:
//
// * storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="behaviors-not-controlled-by-storage-class-options_{context}"]
= Behaviors not controlled by StorageClass options

[role="_abstract"]
Review these behaviors before you delete an LVMCluster. Although these behaviors relate to `storageClassOptions`, the `storageClassOptions` field does not control them.

Volume expansion behavior:: Logical Volume Manager Storage (LVMS) always enables volume expansion by setting `allowVolumeExpansion: true` on generated StorageClasses. You cannot control this setting by using the `storageClassOptions` field. All LVMS volumes support online expansion.

VolumeSnapshotClass management:: The `storageClassOptions` field only affects StorageClasses. When you configure thin provisioning, LVMS generates a `VolumeSnapshotClass` for each device class. This generated class always uses a fixed value `deletionPolicy: Delete`, regardless of the reclaimPolicy that you set in `storageClassOptions`.
+
Additionally, LVMS does not apply the `additionalParameters` and `additionalLabels` fields to `VolumeSnapshotClasses`. If you need to retain snapshot data, you must manage it separately from the StorageClass reclaim policy.

Default StorageClass annotation behavior:: The default field on a device class controls the `storageclass.kubernetes.io/is-default-class` annotation on the generated StorageClass.
+
Setting `default: true` does not guarantee that the LVMS StorageClass becomes the cluster default. If another default StorageClass already exists on the cluster, for example, gp3-csi on AWS-based OpenShift Container Platform clusters, LVMS sets the annotation to `false` to prevent many cluster-wide defaults. Because the Operator actively manages this annotation, it reverts any manual, out-of-band changes during the next reconciliation loop.

//Scaling
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-about-scaling-storage-of-cluster_{context}"]
= Ways to scale up the storage of clusters

OpenShift Container Platform supports additional worker nodes for clusters on bare metal user-provisioned infrastructure. You can scale up the storage of clusters either by adding new worker nodes with available storage or by adding new devices to the existing worker nodes.

{lvms-first} detects and uses additional worker nodes when the nodes become active.

To add a new device to the existing worker nodes on a cluster, you must add the path to the new device in the `deviceSelector` field of the `LVMCluster` custom resource (CR).

[IMPORTANT]
====
You can add the `deviceSelector` field in the `LVMCluster` CR only while creating the `LVMCluster` CR. If you have not added the `deviceSelector` field while creating the `LVMCluster` CR, you must delete the `LVMCluster` CR and create a new `LVMCluster` CR containing the `deviceSelector` field.
====

If you do not add the `deviceSelector` field in the `LVMCluster` CR, {lvms} automatically adds the new devices when the devices are available.
[NOTE]
====
{lvms} adds only the supported devices. For information about unsupported devices, see "Devices not supported by LVM Storage".
====

[role="_additional-resources"]
.Additional resources

* Adding worker nodes to {sno} clusters

* Devices not supported by {lvms}

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-scaling-storage-of-clusters-using-cli_{context}"]
= Scaling up the storage of clusters by using the CLI

You can scale up the storage capacity of the worker nodes on a cluster by using the OpenShift CLI (`oc`).

.Prerequisites

* You have additional unused devices on each cluster to be used by {lvms-first}.
* You have installed the OpenShift CLI (`oc`).
* You have created an `LVMCluster` custom resource (CR).

.Procedure

. Edit the `LVMCluster` CR by running the following command:
+
[source, terminal]
----
$ oc edit <lvmcluster_file_name> -n <namespace>
----

. Add the path to the new device in the `deviceSelector` field.
+

. Save the `LVMCluster` CR.

[role="_additional-resources"]
.Additional resources

* About the `LVMCluster` custom resource

* Devices not supported by {lvms}

* About adding devices to a volume group

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-scaling-storage-of-clusters-using-web-console_{context}"]
= Scaling up the storage of clusters by using the web console

You can scale up the storage capacity of the worker nodes on a cluster by using the OpenShift Container Platform web console.

.Prerequisites

* You have additional unused devices on each cluster to be used by {lvms-first}.
* You have created an `LVMCluster` custom resource (CR).

.Procedure

. Log in to the OpenShift Container Platform web console.
. Click *Ecosystem* -> *Installed Operators*.
. Click *{lvms}* in the `openshift-lvm-storage` namespace.
. Click the *LVMCluster* tab to view the `LVMCluster` CR created on the cluster.
. From the *Actions* menu, select *Edit LVMCluster*.
. Click the *YAML* tab.
. Edit the `LVMCluster` CR to add the new device path in the `deviceSelector` field:
+
. Click *Save*.

[role="_additional-resources"]
.Additional resources

* About the `LVMCluster` custom resource

* Devices not supported by {lvms}

* About adding devices to a volume group

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-scaling-storage-of-clusters-using-rhacm_{context}"]
= Scaling up the storage of clusters by using {rh-rhacm}

You can scale up the storage capacity of worker nodes on the clusters by using {rh-rhacm}.

.Prerequisites

* You have access to the {rh-rhacm} cluster using an account with `cluster-admin` privileges.
* You have created an `LVMCluster` custom resource (CR) by using {rh-rhacm}.
* You have additional unused devices on each cluster to be used by {lvms-first}.

.Procedure

. Log in to the {rh-rhacm} CLI using your OpenShift Container Platform credentials.
. Edit the `LVMCluster` CR that you created using {rh-rhacm} by running the following command:
+
[source,terminal]
----
$ oc edit -f <file_name> -n <namespace> <1>
----
<1> Replace `<file_name>` with the name of the `LVMCluster` CR.

. In the `LVMCluster` CR, add the path to the new device in the `deviceSelector` field.
+
.Example `LVMCluster` CR
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: ConfigurationPolicy
metadata:
  name: lvms
spec:
  object-templates:
     - complianceType: musthave
       objectDefinition:
         apiVersion: lvm.topolvm.io/v1alpha1
         kind: LVMCluster
         metadata:
           name: my-lvmcluster
           namespace: openshift-lvm-storage
         spec:
           storage:
             deviceClasses:
# ...
               deviceSelector: <1>
                 paths: <2>
                 - /dev/disk/by-path/pci-0000:87:00.0-nvme-1
                 optionalPaths: <3>
                 - /dev/disk/by-path/pci-0000:89:00.0-nvme-1
# ...
----
<1> Contains the configuration to specify the paths to the devices that you want to add to the LVM volume group.
You can specify the device paths in the `paths` field, the `optionalPaths` field, or both. If you do not specify the device paths in both `paths` and `optionalPaths`, {lvms-first} adds the supported unused devices to the LVM volume group. {lvms} adds the devices to the LVM volume group only if the following conditions are met:
* The device path exists.
* The device is supported by {lvms}. For information about unsupported devices, see "Devices not supported by {lvms}".
<2> Specify the device paths. If the device path specified in this field does not exist, or the device is not supported by {lvms}, the `LVMCluster` CR moves to the `Failed` state.
<3> Specify the optional device paths. If the device path specified in this field does not exist, or the device is not supported by {lvms}, {lvms} ignores the device without causing an error.
+
[IMPORTANT]
====
After a device is added to the LVM volume group, it cannot be removed.
====

. Save the `LVMCluster` CR.

[role="_additional-resources"]
.Additional resources

* Red Hat Advanced Cluster Management for Kubernetes: Installing while connected online

* About the `LVMCluster` custom resource

* Devices not supported by {lvms}

* About adding devices to a volume group

// Expanding PVCs
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-scaling-expand-pvc_{context}"]
= Expanding a persistent volume claim

After scaling up the storage of a cluster, you can expand the existing persistent volume claims (PVCs).

To expand a PVC, you must update the `storage` field in the PVC.

.Prerequisites

* Dynamic provisioning is used.
* The `StorageClass` object associated with the PVC has the `allowVolumeExpansion` field set to `true`.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Update the value of the `spec.resources.requests.storage` field to a value that is greater than the current value by running the following command:
+
[source,terminal]
----
$ oc patch pvc <pvc_name> -n <application_namespace> \ <1>
  --type=merge -p \ '{ "spec": { "resources": { "requests": { "storage": "<desired_size>" }}}}' <2>
----
<1> Replace `<pvc_name>` with the name of the PVC that you want to expand.
<2> Replace `<desired_size>` with the new size to expand the PVC.

.Verification

* To verify that resizing is completed, run the following command:
+
[source, terminal]
----
$ oc get pvc <pvc_name> -n <application_namespace> -o=jsonpath={.status.capacity.storage}
----
+
{lvms} adds the `Resizing` condition to the PVC during expansion. It deletes the `Resizing` condition after the PVC expansion.

[role="_additional-resources"]
.Additional resources

* Ways to scale up the storage of clusters

* Enabling volume expansion support

// Deleting PVC
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-deleting-pvc_{context}"]
= Deleting a persistent volume claim

You can delete a persistent volume claim (PVC) by using the OpenShift CLI (`oc`).

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Delete the PVC by running the following command:
+
[source,terminal]
----
$ oc delete pvc <pvc_name> -n <namespace>
----

.Verification

* To verify that the PVC is deleted, run the following command:
+
[source,terminal]
----
$ oc get pvc -n <namespace>
----
+
The deleted PVC must not be present in the output of this command.

//Volume snapshots
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-about-volume-snapshots_{context}"]
= About volume snapshots

You can create snapshots of persistent volume claims (PVCs) that are provisioned by {lvms}.

You can perform the following actions using the volume snapshots:

* Back up your application data.
+
[IMPORTANT]
====
Volume snapshots are located on the same devices as the original data. To use the volume snapshots as backups, you must move the snapshots to a secure location. You can use OpenShift API for Data Protection (OADP) backup and restore solutions. For information about OADP, see "OADP features".
====

* Revert to a state at which the volume snapshot was taken.

[NOTE]
====
You can also create volume snapshots of the volume clones.
====

== Limitations for creating volume snapshots in multi-node topology

{lvms} has the following limitations for creating volume snapshots in multi-node topology:

* Creating volume snapshots is based on the LVM thin pool capabilities.
* After creating a volume snapshot, the node must have additional storage space for further updating the original data source.
* You can create volume snapshots only on the node where you have deployed the original data source.
* Pods relying on the PVC that uses the snapshot data can be scheduled only on the node where you have deployed the original data source.

[role="_additional-resources"]
.Additional resources

* OADP features

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-creating-volume-snapshots_{context}"]
= Creating volume snapshots

You can create volume snapshots based on the available capacity of the thin pool and the over-provisioning limits.
To create a volume snapshot, you must create a `VolumeSnapshotClass` object.

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.
* You ensured that the persistent volume claim (PVC) is in `Bound` state. This is required for a consistent snapshot.
* You stopped all the I/O to the PVC.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Create a `VolumeSnapshot` object:
+
.Example `VolumeSnapshot` object
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: lvm-block-1-snap <1>
spec:
  source:
    persistentVolumeClaimName: lvm-block-1 <2>
  volumeSnapshotClassName: lvms-vg1 <3>
----
<1> Specify a name for the volume snapshot.
<2> Specify the name of the source PVC. {lvms} creates a snapshot of this PVC.
<3> Set this field to the name of a volume snapshot class.
+
[NOTE]
====
To get the list of available volume snapshot classes, run the following command:
[source, terminal]
----
$ oc get volumesnapshotclass
----
====

. Create the volume snapshot in the namespace where you created the source PVC by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name> -n <namespace>
----
+
{lvms} creates a read-only copy of the PVC as a volume snapshot.

.Verification

* To verify that the volume snapshot is created, run the following command:
+
[source,terminal]
----
$ oc get volumesnapshot -n <namespace>
----
+
.Example output
+
[source, terminal]
----
NAME               READYTOUSE   SOURCEPVC     SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS   SNAPSHOTCONTENT                                    CREATIONTIME   AGE
lvm-block-1-snap   true         lvms-test-1                           1Gi           lvms-vg1        snapcontent-af409f97-55fc-40cf-975f-71e44fa2ca91   19s            19s
----
+
The value of the `READYTOUSE` field for the volume snapshot that you created must be `true`.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-restoring-volume-snapshots_{context}"]
= Restoring volume snapshots

To restore a volume snapshot, you must create a persistent volume claim (PVC) with the `dataSource.name` field set to the name of the volume snapshot.

The restored PVC is independent of the volume snapshot and the source PVC.

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.
* You have created a volume snapshot.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Create a `PersistentVolumeClaim` object with the configuration to restore the volume snapshot:
+
.Example `PersistentVolumeClaim` object to restore a volume snapshot
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: lvm-block-1-restore
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Block
  Resources:
    Requests:
      storage: 2Gi <1>
  storageClassName: lvms-vg1 <2>
  dataSource:
    name: lvm-block-1-snap <3>
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
----
<1> Specify the storage size of the restored PVC. The storage size of the requested PVC must be greater than or equal to the stoage size of the volume snapshot that you want to restore. If a larger PVC is required, you can also resize the PVC after restoring the volume snapshot.
<2> Set this field to the value of the `storageClassName` field in the source PVC of the volume snapshot that you want to restore.
<3> Set this field to the name of the volume snapshot that you want to restore.

. Create the PVC in the namespace where you created the volume snapshot by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name> -n <namespace>
----

.Verification

* To verify that the volume snapshot is restored, run the following command:
+
[source, terminal]
----
$ oc get pvc -n <namespace>
----
+
.Example output
+
[source, terminal]
----
NAME                  STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
lvm-block-1-restore   Bound    pvc-e90169a8-fd71-4eea-93b8-817155f60e47   1Gi        RWO            lvms-vg1       5s
----

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-deleting-volume-snapshots_{context}"]
= Deleting volume snapshots

You can delete the volume snapshots of the persistent volume claims (PVCs).
[IMPORTANT]
====
When you delete a persistent volume claim (PVC), {lvms} deletes only the PVC, but not the snapshots of the PVC.
====

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.
* You have ensured that the volume snpashot that you want to delete is not in use.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Delete the volume snapshot by running the following command:
+
[source,terminal]
----
$ oc delete volumesnapshot <volume_snapshot_name> -n <namespace>
----

.Verification

* To verify that the volume snapshot is deleted, run the following command:
+
[source, terminal]
----
$ oc get volumesnapshot -n <namespace>
----
+
The deleted volume snapshot must not be present in the output of this command.

//Volume cloning
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-about-volume-clones_{context}"]
= About volume clones

A volume clone is a duplicate of an existing persistent volume claim (PVC). You can create a volume clone to make a point-in-time copy of the data.

== Limitations for creating volume clones in multi-node topology

{lvms} has the following limitations for creating volume clones in multi-node topology:

* Creating volume clones is based on the LVM thin pool capabilities.
* The node must have additional storage after creating a volume clone for further updating the original data source.
* You can create volume clones only on the node where you have deployed the original data source.
* Pods relying on the PVC that uses the clone data can be scheduled only on the node where you have deployed the original data source.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-creating-volume-clones_{context}"]
= Creating volume clones

To create a clone of a persistent volume claim (PVC), you must create a `PersistentVolumeClaim` object in the namespace where you created the source PVC.

[IMPORTANT]
====
The cloned PVC has write access.
====

.Prerequisites

* You ensured that the source PVC is in `Bound` state. This is required for a consistent clone.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Create a `PersistentVolumeClaim` object:
+
.Example `PersistentVolumeClaim` object to create a volume clone
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: lvm-pvc-clone
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: lvms-vg1 <1>
  volumeMode: Filesystem <2>
  dataSource:
    kind: PersistentVolumeClaim
    name: lvm-pvc <3>
  resources:
    requests:
      storage: 1Gi <4>
----
<1> Set this field to the value of the `storageClassName` field in the source PVC.
<2> Set this field to the `volumeMode` field in the source PVC.
<3> Specify the name of the source PVC.
<4> Specify the storage size for the cloned PVC. The storage size of the cloned PVC must be greater than or equal to the storage size of the source PVC.

. Create the PVC in the namespace where you created the source PVC by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name> -n <namespace>
----

.Verification

* To verify that the volume clone is created, run the following command:
+
[source,terminal]
----
$ oc get pvc -n <namespace>
----
+
.Example output
+
[source, terminal]
----
NAME                STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
lvm-block-1-clone   Bound    pvc-e90169a8-fd71-4eea-93b8-817155f60e47   1Gi        RWO            lvms-vg1       5s
----

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-deleting-cloned-volumes_{context}"]
= Deleting volume clones

You can delete volume clones.
[IMPORTANT]
====
When you delete a persistent volume claim (PVC), {lvms} deletes only the source persistent volume claim (PVC) but not the clones of the PVC.
====

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Delete the cloned PVC by running the following command:
+
[source,terminal]
----
# oc delete pvc <clone_pvc_name> -n <namespace>
----

.Verification

* To verify that the volume clone is deleted, run the following command:
+
[source,terminal]
----
$ oc get pvc -n <namespace>
----
+
The deleted volume clone must not be present in the output of this command.

//Updating
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-updating-lvms_{context}"]
= Updating {lvms}

You can update {lvms} to ensure compatibility with the OpenShift Container Platform version.

[NOTE]
====
The default namespace for the {lvms} Operator is `openshift-lvm-storage`.
====

.Prerequisites

* You have updated your OpenShift Container Platform cluster.

* You have installed a previous version of {lvms}.

* You have installed the OpenShift CLI (`oc`).

* You have access to the cluster using an account with `cluster-admin` permissions.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Update the `Subscription` custom resource (CR) that you created while installing {lvms} by running the following command:
+
[source,terminal]
----
$ oc patch subscription lvms-operator -n openshift-lvm-storage --type merge --patch '{"spec":{"channel":"<update_channel>"}}' <1>
----
<1> Replace `<update_channel>` with the version of {lvms} that you want to install. For example, `stable-`.

. View the update events to check that the installation is complete by running the following command:
+
[source,terminal]
----
$ oc get events -n openshift-lvm-storage
----
+
.Example output
[source,terminal, subs="attributes"]
----
...
8m13s       Normal    RequirementsUnknown   clusterserviceversion/lvms-operator.v   requirements not yet checked
8m11s       Normal    RequirementsNotMet    clusterserviceversion/lvms-operator.v   one or more requirements couldn't be found
7m50s       Normal    AllRequirementsMet    clusterserviceversion/lvms-operator.v   all requirements found, attempting install
7m50s       Normal    InstallSucceeded      clusterserviceversion/lvms-operator.v   waiting for install components to report healthy
7m49s       Normal    InstallWaiting        clusterserviceversion/lvms-operator.v   installing: waiting for deployment lvms-operator to become ready: deployment "lvms-operator" waiting for 1 outdated replica(s) to be terminated
7m39s       Normal    InstallSucceeded      clusterserviceversion/lvms-operator.v   install strategy completed with no errors
...
----

.Verification

* Verify the {lvms} version by running the following command:
+
[source,terminal]
----
$ oc get subscription lvms-operator -n openshift-lvm-storage -o jsonpath='{.status.installedCSV}'
----
+
.Example output
[source,terminal, subs="attributes"]
----
lvms-operator.v
----

//Monitoring
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-monitoring_{context}"]
= Monitoring {lvms}

To enable cluster monitoring, you must add the following label in the namespace where you have installed {lvms}:
[source,text]
----
openshift.io/cluster-monitoring=true
----

[IMPORTANT]
====
For information about enabling cluster monitoring in {rh-rhacm}, see Observability and Adding custom metrics.
====

[id="lvms-monitoring-using-lvms-metrics_{context}"]
== Metrics

You can monitor {lvms} by viewing the metrics.

The following table describes the `topolvm` metrics:

.`topolvm` metrics
[%autowidth,options="header"]
|===
|Alert | Description
|`topolvm_thinpool_data_percent` | Indicates the percentage of data space used in the LVM thinpool.
|`topolvm_thinpool_metadata_percent` | Indicates the percentage of metadata space used in the LVM thinpool.
|`topolvm_thinpool_size_bytes` | Indicates the size of the LVM thin pool in bytes.
|`topolvm_volumegroup_available_bytes` | Indicates the available space in the LVM volume group in bytes.
|`topolvm_volumegroup_size_bytes` | Indicates the size of the LVM volume group in bytes.
|`topolvm_thinpool_overprovisioned_available` | Indicates the available over-provisioned size of the LVM thin pool in bytes.
|===

[NOTE]
====
Metrics are updated every 10 minutes or when there is a change, such as a new logical volume creation, in the thin pool.
====

[id="lvms-monitoring-using-lvms-alerts_{context}"]
== Alerts

When the thin pool and volume group reach maximum storage capacity, further operations fail. This can lead to data loss.

{lvms} sends the following alerts when the usage of the thin pool and volume group exceeds a certain value:

.LVM Storage alerts
[%autowidth, options="header"]
|===
|Alert| Description
|`VolumeGroupUsageAtThresholdNearFull`|This alert is triggered when both the volume group and thin pool usage exceeds 75% on nodes. Data deletion or volume group expansion is required.
|`VolumeGroupUsageAtThresholdCritical`|This alert is triggered when both the volume group and thin pool usage exceeds 85% on nodes. In this case, the volume group is critically full. Data deletion or volume group expansion is required.
|`ThinPoolDataUsageAtThresholdNearFull`|This alert is triggered when the thin pool data uusage in the volume group exceeds 75% on nodes. Data deletion or thin pool expansion is required.
|`ThinPoolDataUsageAtThresholdCritical`|This alert is triggered when the thin pool data usage in the volume group exceeds 85% on nodes. Data deletion or thin pool expansion is required.
|`ThinPoolMetaDataUsageAtThresholdNearFull`|This alert is triggered when the thin pool metadata usage in the volume group exceeds 75% on nodes. Data deletion or thin pool expansion is required.
|`ThinPoolMetaDataUsageAtThresholdCritical`|This alert is triggered when the thin pool metadata usage in the volume group exceeds 85% on nodes. Data deletion or thin pool expansion is required.
|===

// Uninstalling LVM Storage

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-unstalling-lvms-using-cli_{context}"]
= Uninstalling {lvms} by using the CLI

You can uninstall {lvms} by using the {oc-first}.

.Prerequisites

* You have logged in to `oc` as a user with `cluster-admin` permissions.
* You deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by {lvms}. You have also deleted the applications that are using these resources.
* You deleted the `LVMCluster` custom resource (CR).

.Procedure

. Get the `currentCSV` value for the {lvms} Operator by running the following command:
+
[source,terminal]
----
$ oc get subscription.operators.coreos.com lvms-operator -n <namespace> -o yaml | grep currentCSV
----
+
.Example output
[source,terminal]
----
currentCSV: lvms-operator.v4.15.3
----

. Delete the subscription by running the following command:
+
[source,terminal]
----
$ oc delete subscription.operators.coreos.com lvms-operator -n <namespace>
----
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com "lvms-operator" deleted
----

. Delete the CSV for the {lvms} Operator in the target namespace by running the following command:
+
[source,terminal]
----
$ oc delete clusterserviceversion <currentCSV> -n <namespace> <1>
----
<1> Replace `<currentCSV>` with the `currentCSV` value for the {lvms} Operator.
+
.Example output
[source,terminal]
----
clusterserviceversion.operators.coreos.com "lvms-operator.v4.15.3" deleted
----

.Verification

* To verify that the {lvms} Operator is uninstalled, run the following command:
+
[source,terminal]
----
$ oc get csv -n <namespace>
----
+
If the {lvms} Operator was successfully uninstalled, it does not appear in the output of this command.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-unstalling-lvms-with-web-console_{context}"]
= Uninstalling {lvms} by using the web console

You can uninstall {lvms} using the OpenShift Container Platform web console.

.Prerequisites

* You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.
* You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by {lvms}. You have also deleted the applications that are using these resources.
* You have deleted the `LVMCluster` custom resource (CR).

.Procedure

. Log in to the OpenShift Container Platform web console.
. Click *Ecosystem* -> *Installed Operators*.
. Click *{lvms}* in the `openshift-lvm-storage` namespace.
. Click the *Details* tab.
. From the *Actions* menu, select *Uninstall Operator*.
. Optional: When prompted, select the *Delete all operand instances for this operator* checkbox to delete the operand instances for {lvms}.
. Click *Uninstall*.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-uninstalling-lvms-rhacm_{context}"]
= Uninstalling {lvms} installed using {rh-rhacm}

To uninstall {lvms} that you installed using {rh-rhacm}, you must delete the {rh-rhacm} `Policy` custom resource (CR) that you created for installing and configuring {lvms}.

.Prerequisites

* You have access to the {rh-rhacm} cluster as a user with `cluster-admin` permissions.
* You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by {lvms}. You have also deleted the applications that are using these resources.
* You have deleted the `LVMCluster` CR that you created using {rh-rhacm}.

.Procedure

. Log in to the OpenShift CLI (`oc`).

. Delete the {rh-rhacm} `Policy` CR that you created for installing and configuring {lvms} by using the following command:
+
[source,terminal]
----
$ oc delete -f <policy> -n <namespace> <1>
----
<1> Replace `<policy>` with the name of the `Policy` CR YAML file.

. Create a `Policy` CR YAML file with the configuration to uninstall {lvms}:
+
.Example `Policy` CR to uninstall {lvms}
[source,yaml]
----
apiVersion: apps.open-cluster-management.io/v1
kind: PlacementRule
metadata:
  name: placement-uninstall-lvms
spec:
  clusterConditions:
  - status: "True"
    type: ManagedClusterConditionAvailable
  clusterSelector:
    matchExpressions:
    - key: mykey
      operator: In
      values:
      - myvalue
---
apiVersion: policy.open-cluster-management.io/v1
kind: PlacementBinding
metadata:
  name: binding-uninstall-lvms
placementRef:
  apiGroup: apps.open-cluster-management.io
  kind: PlacementRule
  name: placement-uninstall-lvms
subjects:
- apiGroup: policy.open-cluster-management.io
  kind: Policy
  name: uninstall-lvms
---
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  annotations:
    policy.open-cluster-management.io/categories: CM Configuration Management
    policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
    policy.open-cluster-management.io/standards: NIST SP 800-53
  name: uninstall-lvms
spec:
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: uninstall-lvms
      spec:
        object-templates:
        - complianceType: mustnothave
          objectDefinition:
            apiVersion: v1
            kind: Namespace
            metadata:
              name: openshift-lvm-storage
        - complianceType: mustnothave
          objectDefinition:
            apiVersion: operators.coreos.com/v1
            kind: OperatorGroup
            metadata:
              name: openshift-storage-operatorgroup
              namespace: openshift-lvm-storage
            spec:
              targetNamespaces:
              - openshift-lvm-storage
        - complianceType: mustnothave
          objectDefinition:
            apiVersion: operators.coreos.com/v1alpha1
            kind: Subscription
            metadata:
              name: lvms-operator
              namespace: openshift-lvm-storage
        remediationAction: enforce
        severity: low
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: policy-remove-lvms-crds
      spec:
        object-templates:
        - complianceType: mustnothave
          objectDefinition:
            apiVersion: apiextensions.k8s.io/v1
            kind: CustomResourceDefinition
            metadata:
              name: logicalvolumes.topolvm.io
        - complianceType: mustnothave
          objectDefinition:
            apiVersion: apiextensions.k8s.io/v1
            kind: CustomResourceDefinition
            metadata:
              name: lvmclusters.lvm.topolvm.io
        - complianceType: mustnothave
          objectDefinition:
            apiVersion: apiextensions.k8s.io/v1
            kind: CustomResourceDefinition
            metadata:
              name: lvmvolumegroupnodestatuses.lvm.topolvm.io
        - complianceType: mustnothave
          objectDefinition:
            apiVersion: apiextensions.k8s.io/v1
            kind: CustomResourceDefinition
            metadata:
              name: lvmvolumegroups.lvm.topolvm.io
        remediationAction: enforce
        severity: high
----

. Create the `Policy` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <policy> -ns <namespace>
----

//Must-gather
// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-dowloading-log-files-and-diagnostics_{context}"]
= Downloading log files and diagnostic information using must-gather

When {lvms} is unable to automatically resolve a problem, use the must-gather tool to collect the log files and diagnostic information so that you or the Red Hat Support can review the problem and determine a solution.

.Procedure
* Run the `must-gather` command from the client connected to the {lvms} cluster:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --image=registry.redhat.io/lvms4/lvms-must-gather-rhel9:v --dest-dir=<directory_name>
----

[role="_additional-resources"]
.Additional resources

* About the must-gather tool

//Troubleshooting local persistent storage using LVM Storage

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="lvms-troubleshooting-persistent-storage_{context}"]
= Troubleshooting persistent storage

While configuring persistent storage using {lvms-first}, you can encounter several issues that require troubleshooting.

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="investigating-a-pvc-stuck-in-the-pending-state_{context}"]
= Investigating a PVC stuck in the Pending state

A persistent volume claim (PVC) can get stuck in the `Pending` state for the following reasons:

- Insufficient computing resources.
- Network problems.
- Mismatched storage class or node selector.
- No available persistent volumes (PVs).
- The node with the PV is in the `Not Ready` state.

.Prerequisites

* You have installed the {oc-first}.
* You have logged in to the {oc-first} as a user with `cluster-admin` permissions.

.Procedure

. Retrieve the list of PVCs by running the following command:
+
[source,terminal]
----
$ oc get pvc
----
+
.Example output
[source,terminal]
----
NAME        STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
lvms-test   Pending                                      lvms-vg1       11s
----

. Inspect the events associated with a PVC stuck in the `Pending` state by running the following command:
+
[source,terminal]
----
$ oc describe pvc <pvc_name> <1>
----
<1> Replace `<pvc_name>` with the name of the PVC. For example, `lvms-vg1`.
+
.Example output
[source,terminal]
----
Type     Reason              Age               From                         Message
----     ------              ----              ----                         -------
Warning  ProvisioningFailed  4s (x2 over 17s)  persistentvolume-controller  storageclass.storage.k8s.io "lvms-vg1" not found
----

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="recovering-from-missing-lvms-or-operator-components_{context}"]
= Recovering from a missing storage class

If you encounter the `storage class not found` error, check the `LVMCluster` custom resource (CR) and ensure that all the {lvms-first} pods are in the `Running` state.

.Prerequisites

* You have installed the {oc-first}.
* You have logged in to the {oc-first} as a user with `cluster-admin` permissions.

.Procedure

. Verify that the `LVMCluster` CR is present by running the following command:
+
[source,terminal]
----
$ oc get lvmcluster -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME            AGE
my-lvmcluster   65m
----

. If the `LVMCluster` CR is not present, create an `LVMCluster` CR. For more information, see "Ways to create an LVMCluster custom resource".

. In the namespace where the operator is installed, check that all the {lvms} pods are in the `Running` state by running the following command:
+
[source,terminal]
----
$ oc get pods -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS      AGE
lvms-operator-7b9fb858cb-6nsml        3/3     Running   0             70m
topolvm-controller-5dd9cf78b5-7wwr2   5/5     Running   0             66m
topolvm-node-dr26h                    4/4     Running   0             66m
vg-manager-r6zdv                      1/1     Running   0             66m
----
+
The output of this command must contain a running instance of the following pods:

* `lvms-operator`
* `vg-manager`
+
If the `vg-manager` pod is stuck while loading a configuration file, it is due to a failure to locate an available disk for {lvms} to use. To retrieve the necessary information to troubleshoot this issue, review the logs of the `vg-manager` pod by running the following command:
+
[source,terminal]
----
$ oc logs -l app.kubernetes.io/component=vg-manager -n <namespace>
----

[role="_additional-resources"]
.Additional resources

* About the `LVMCluster` custom resource

* Ways to create an `LVMCluster` custom resource

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="recovering-from-node-failure_{context}"]
= Recovering from node failure

A persistent volume claim (PVC) can be stuck in the `Pending` state due to a node failure in the cluster.

To identify the failed node, you can examine the restart count of the `topolvm-node` pod. An increased restart count indicates potential problems with the underlying node, which might require further investigation and troubleshooting.

.Prerequisites

* You have installed the {oc-first}.
* You have logged in to the {oc-first} as a user with `cluster-admin` permissions.

.Procedure

* Examine the restart count of the `topolvm-node` pod instances by running the following command:
+
[source,terminal]
----
$ oc get pods -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS      AGE
lvms-operator-7b9fb858cb-6nsml        3/3     Running   0             70m
topolvm-controller-5dd9cf78b5-7wwr2   5/5     Running   0             66m
topolvm-node-dr26h                    4/4     Running   0             66m
topolvm-node-54as8                    4/4     Running   0             66m
topolvm-node-78fft                    4/4     Running   17 (8s ago)   66m
vg-manager-r6zdv                      1/1     Running   0             66m
vg-manager-990ut                      1/1     Running   0             66m
vg-manager-an118                      1/1     Running   0             66m
----

.Next steps

* If the PVC is stuck in the `Pending` state even after you have resolved any issues with the node, you must perform a forced clean-up. For more information, see "Performing a forced clean-up".

[role="_additional-resources"]
.Additional resources

* Performing a forced clean-up

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="recovering-from-disk-failure_{context}"]
= Recovering from disk failure

If you see a failure message while inspecting the events associated with the persistent volume claim (PVC), there can be a problem with the underlying volume or disk.

Disk and volume provisioning issues result with a generic error message such as `Failed to provision volume with storage class <storage_class_name>`. The generic error message is followed by a specific volume failure error message.

The following table describes the volume failure error messages:

.Volume failure error messages
[%autowidth, options="header"]
|===

|Error message |Description

|`Failed to check volume existence`
|Indicates a problem in verifying whether the volume already exists. Volume verification failure can be caused by network connectivity problems or other failures.

|`Failed to bind volume`
|Failure to bind a volume can happen if the persistent volume (PV) that is available does not match the requirements of the PVC.

|`FailedMount` or `FailedAttachVolume`
|This error indicates problems when trying to mount the volume to a node. If the disk has failed, this error can appear when a pod tries to use the PVC.

|`FailedUnMount`
|This error indicates problems when trying to unmount a volume from a node. If the disk has failed, this error can appear when a pod tries to use the PVC.

|`Volume is already exclusively attached to one node and cannot be attached to another`
|This error can appear with storage solutions that do not support `ReadWriteMany` access modes.

|===

.Prerequisites

* You have installed the {oc-first}.
* You have logged in to the {oc-first} as a user with `cluster-admin` permissions.

.Procedure

. Inspect the events associated with a PVC by running the following command:
+
[source,terminal]
----
$ oc describe pvc <pvc_name> <1>
----
<1> Replace `<pvc_name>` with the name of the PVC.

. Establish a direct connection to the host where the problem is occurring.

. Resolve the disk issue.

.Next steps

* If the volume failure messages persist or recur even after you have resolved the issue with the disk, you must perform a forced clean-up. For more information, see "Performing a forced clean-up".

[role="_additional-resources"]
.Additional resources

* Performing a forced clean-up

// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

[id="performing-a-forced-cleanup_{context}"]
= Performing a forced clean-up

If the disk or node-related problems persist even after you have completed the troubleshooting procedures, you must perform a forced clean-up. A forced clean-up is used to address persistent issues and ensure the proper functioning of {lvms-first}.

.Prerequisites

* You have installed the {oc-first}.

* You have logged in to the {oc-first} as a user with `cluster-admin` permissions.

* You have deleted all the persistent volume claims (PVCs) that were created by using {lvms}.

* You have stopped the pods that are using the PVCs that were created by using {lvms}.

.Procedure

. Switch to the namespace where you have installed the {lvms} Operator by running the following command:
+
[source,terminal]
----
$ oc project <namespace>
----

. Check if the `LogicalVolume` custom resources (CRs) are present by running the following command:
+
[source,terminal]
----
$ oc get logicalvolume
----

.. If the `LogicalVolume` CRs are present, delete them by running the following command:
+
[source,terminal]
----
$ oc delete logicalvolume <name> <1>
----
<1> Replace `<name>` with the name of the `LogicalVolume` CR.

.. After deleting the `LogicalVolume` CRs, remove their finalizers by running the following command:
+
[source,terminal]
----
$ oc patch logicalvolume <name> -p '{"metadata":{"finalizers":[]}}' --type=merge <1>
----
<1> Replace `<name>` with the name of the `LogicalVolume` CR.

. Check if the `LVMVolumeGroup` CRs are present by running the following command:
+
[source,terminal]
----
$ oc get lvmvolumegroup
----

.. If the `LVMVolumeGroup` CRs are present, delete them by running the following command:
+
[source,terminal]
----
$ oc delete lvmvolumegroup <name> <1>
----
<1> Replace `<name>` with the name of the `LVMVolumeGroup` CR.

.. After deleting the `LVMVolumeGroup` CRs, remove their finalizers by running the following command:
+
[source,terminal]
----
$ oc patch lvmvolumegroup <name> -p '{"metadata":{"finalizers":[]}}' --type=merge <1>
----
<1> Replace `<name>` with the name of the `LVMVolumeGroup` CR.

. Delete any `LVMVolumeGroupNodeStatus` CRs by running the following command:
+
[source,terminal]
----
$ oc delete lvmvolumegroupnodestatus --all
----

. Delete the `LVMCluster` CR by running the following command:
+
[source,terminal]
----
$ oc delete lvmcluster --all
----

.. After deleting the `LVMCluster` CR, remove its finalizer by running the following command:
+
[source,terminal]
----
$ oc patch lvmcluster <name> -p '{"metadata":{"finalizers":[]}}' --type=merge <1>
----
<1> Replace `<name>` with the name of the `LVMCluster` CR.
