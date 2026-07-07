---
title: "Using dynamic storage with the LVMS plugin"
type: reference
domain: openshift
slug: microshift-storage-4-22-microshift-storage-plugin-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_storage/microshift-storage-plugin-overview
version: 4.22
family: microshift_storage
documentKind: "Documentation"
---

# Using dynamic storage with the LVMS plugin

[id="microshift-storage-plugin-overview"]
= Using dynamic storage with the LVMS plugin

[role="_abstract"]
By using dynamic provisioning, you can create storage volumes on-demand to eliminate the need for pre-provisioned storage.

{microshift-short} enables dynamic storage provisioning that is ready for immediate use with the logical volume manager storage (LVMS) Container Storage Interface (CSI) provider. The LVMS plugin is the Red{nbsp}Hat downstream version of TopoLVM, a CSI plugin for managing logical volume management (LVM) logical volumes (LVs) for Kubernetes.

LVMS provisions new LVM logical volumes for container workloads with appropriately configured persistent volume claims (PVCs). Each PVC references a storage class that represents an LVM Volume Group (VG) on the host node. LVs are only provisioned for scheduled pods.

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-lvms-system-requirements_{context}"]
= LVMS system requirements

[role="_abstract"]
To prepare your infrastructure for storage operations, review the system specifications for using LVMS in {microshift-short}. Verifying these requirements ensures your environment meets the necessary resource standards for a successful deployment.

[id="lvms-volume-group-name_{context}"]
== Volume group name

If you did not configure LVMS in an `lvmd.yaml` file placed in the `/etc/microshift/` directory, {microshift-short} attempts to assign a default volume group (VG) dynamically by running the `vgs` command.

* {microshift-short} assigns a default VG when only one VG is found.
* If more than one VG is present, the VG named `microshift` is assigned as the default.
* If a VG named `microshift` does not exist, LVMS is not deployed.

If there are no volume groups on the {microshift-short} host, LVMS is disabled.

If you want to use a specific VG, LVMS must be configured to select that VG. You can change the default name of the VG in the configuration file. For details, read the "Configuring the LVMS" section of this document.

You can change the default name of the VG in the configuration file. For details, read the "Configuring the LVMS" section of this document.

After {microshift-short} starts, you can update the `lvmd.yaml` to include or remove VGs. To implement changes, you must restart {microshift-short}. If the `lvmd.yaml` is deleted, {microshift-short} attempts to find a default VG again.

[id="lvms-volume-size-increments_{context}"]
== Volume size increments

The LVMS provisions storage in increments of 1 gigabyte (GB). Storage requests are rounded up to the nearest GB. When the capacity of a VG is less than 1 GB, the `PersistentVolumeClaim` registers a `ProvisioningFailed` event, for example:

.Example output
[source,terminal]
----
Warning  ProvisioningFailed    3s (x2 over 5s)  topolvm.cybozu.com_topolvm-controller-858c78d96c-xttzp_0fa83aef-2070-4ae2-bcb9-163f818dcd9f failed to provision volume with
StorageClass "topolvm-provisioner": rpc error: code = ResourceExhausted desc = no enough space left on VG: free=(BYTES_INT), requested=(BYTES_INT)
----

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-disabling-uninstalling-lvms-csi-snapshot_{context}"]
= Disabling and uninstalling LVMS CSI provider and CSI snapshot deployments

[role="_abstract"]
To reduce the use of runtime resources, such as RAM, CPU, and storage, remove or disable the LVMS CSI provider and CSI snapshot deployments. This configuration optimizes system performance by eliminating storage components that are not required for your specific workload.

[NOTE]
====
You can configure {microshift-short} to disable CSI provider and CSI snapshot only before installing and running {microshift-short}. After {microshift-short} is installed and running, you must update the configuration file and uninstall the components.
====

To reduce the use of runtime resources, you can remove or disable the following storage components:

* You can configure {microshift-short} to disable the built-in logical volume manager storage (LVMS) Container Storage Interface (CSI) provider.
* You can configure {microshift-short} to disable the Container Storage Interface (CSI) snapshot capabilities.
* You can uninstall the installed CSI implementations using `oc` commands.

[IMPORTANT]
====
Automated uninstallation is not supported as this can cause orphaning of the provisioned volumes. Without the LVMS CSI driver, the node does not detect the underlying storage interface and cannot perform provisioning and deprovisioning or mounting and unmounting operations.
====

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc
// * microshift_configuring/microshift-disable-lvms-csi-provider-csi-snapshot.adoc

[id="microshift-disabling-lvms-csi-snapshot_{context}"]
= Disabling deployments that run CSI snapshot implementations

[role="_abstract"]
To prevent the installation of CSI implementation pods, disable the deployments that run CSI snapshot implementations. This configuration conserves system resources by ensuring that snapshot components are not deployed when they are not required.

[IMPORTANT]
====
Use the procedure if you are defining the configuration file before installing and running {microshift-short}. If {microshift-short} is already started, the CSI snapshot implementation will be running. You must manually remove the implementation by following the uninstallation instructions.
====

[NOTE]
====
{microshift-short} does not delete CSI snapshot implementation pods. You must configure {microshift-short} to disable installation of the CSI snapshot implementation pods during the startup process.
====

.Procedure

. Disable installation of the CSI snapshot controller by entering the `optionalCsiComponents` value under the `storage` section of the {microshift-short} configuration file in `/etc/microshift/config.yaml`:
+
[source,yaml]
----
# ...
  storage: {}
# ...
----
+
where:
+
`storage`:: Specifies the storage details. You can choose to not define `optionalCsiComponents`. If you do specify the `optionalCsiComponents` field, valid values include: an empty value (`[]`) or a single empty string element (`[""]`), `snapshot-controller`, or `none`. A value of `none` is mutually exclusive with all other values.
+
[NOTE]
====
If the `optionalCsiComponents` value is empty or null, {microshift-short} defaults to deploying `snapshot-controller`.
====

. After the `optionalCsiComponents` field is specified with a supported value in the `config.yaml`, start {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----
+
[NOTE]
====
{microshift-short} does not redeploy the disabled components after a restart.
====

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc
// * microshift_configuring/microshift-disable-lvms-csi-provider-csi-snapshot.adoc

[id="microshift-disabling-lvms-csi-driver_{context}"]
= Disabling deployments that run the CSI driver implementations

[role="_abstract"]
You can disable installation of the CSI implementation pods. {microshift-short} does not delete CSI driver implementation pods. You must configure {microshift-short} to disable installation of the CSI driver implementation pods during the startup process.

[IMPORTANT]
====
This procedure is for defining the configuration file before installing and running {microshift-short}. If {microshift-short} is already started, then the CSI driver implementation is running. You must manually remove it by following the uninstallation instructions.
====

.Procedure

. Disable installation of the CSI driver by entering the `driver` value under the `storage` section of the {microshift-short} configuration file in `/etc/microshift/config.yaml`:
+
[source,yaml]
----
# ...
  storage
   driver:
   - "none"
# ...
----
+
where:
+
`storage.driver.none`:: Specifies the driver to disable. Valid values are `none` or `lvms`.
+
[NOTE]
====
By default, the `driver` value is empty or null and LVMS is deployed.
====

. Start {microshift-short} after the `driver` field is specified with a supported value in the `/etc/microshift/config.yaml` file by running the following command:
+
[source,terminal]
----
$ sudo systemctl enable --now microshift
----
+
[NOTE]
====
{microshift-short} does not redeploy the disabled components after a restart operation.
====

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-uninstalling-lvms-csi-snapshot_{context}"]
= Uninstalling the CSI snapshot implementation

[role="_abstract"]
To remove the Container Storage Interface (CSI) snapshot capability from your cluster, uninstall the CSI snapshot implementation.

.Prerequisites

* {microshift-short} is installed and running.
* The CSI snapshot implementation is deployed on the {microshift-short} node.

.Procedure

* Uninstall the CSI snapshot implementation by running the following command:
+
[source,terminal]
----
$ oc delete -n kube-system deployment.apps/snapshot-controller
----
+
.Example output
[source,terminal]
----
deployment.apps "snapshot-controller" deleted
----

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-uninstalling-lvms-csi-driver_{context}"]
= Uninstalling the CSI driver implementation

[role="_abstract"]
To remove the Container Storage Interface (CSI) integration from your cluster, uninstall the CSI driver implementation.

.Prerequisites

* {microshift-short} is installed and running.
* The CSI driver implementation is deployed on the {microshift-short} node.

.Procedure

. Delete the `lvmclusters` object by running the following command:
+
[source,terminal]
----
$ oc delete -n openshift-storage lvmclusters.lvm.topolvm.io/lvms
----
+
.Example output
[source,terminal]
----
lvmcluster.lvm.topolvm.io "lvms" deleted
----

. Delete the `lvms-operator` by running the following command:
+
[source,terminal]
----
$ oc delete -n openshift-storage deployment.apps/lvms-operator
----
+
.Example output
[source,terminal]
----
deployment.apps "lvms-operator" deleted
----

. Delete the `topolvm-provisioner` `StorageClass` by running the following command:
+
[source,terminal]
----
$ oc delete storageclasses.storage.k8s.io/topolvm-provisioner
----
+
.Example output
[source,terminal]
----
storageclass.storage.k8s.io "topolvm-provisioner" deleted
----

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-lvms-deployment_{context}"]
= LVMS deployment

[role="_abstract"]
To ensure local storage is ready for use, {microshift-short} automatically deploys LVMS into the `openshift-storage` namespace at startup. This automated process prepares the node for storage operations immediately, eliminating the need for manual installation.

LVMS uses `StorageCapacity` tracking to ensure that pods with an LVMS PVC are not scheduled if the requested storage is greater than the free storage of the volume group. For more information about `StorageCapacity` tracking, see "Storage Capacity".

[role="_additional-resource"]
.Additional resources

* Storage Capacity

//OCP module with edits
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

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-lvmd-yaml-creating_{context}"]
= Creating an LVMS configuration file

[role="_abstract"]
To customize storage settings, create an LVMS configuration file named lvmd.yaml. You must place this file in the `/etc/microshift/` directory to ensure {microshift-short} detects and applies your configuration at startup.

.Procedure

* To create the `lvmd.yaml` configuration file, run the following command:
+
[source,terminal]
----
$ sudo cp /etc/microshift/lvmd.yaml.default /etc/microshift/lvmd.yaml
----

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-lvms-config-example-basic_{context}"]
= Basic LVMS configuration example

[role="_abstract"]
To customize storage operations, pass through your LVM configuration to {microshift-short}. With this flexibility, you can define custom volume groups, thin volume provisioning parameters, and reserved unallocated space by editing the LVMS configuration file.

You must restart {microshift-short} to deploy configuration changes after editing the file.

[NOTE]
====
If you need to take volume snapshots, you must use thin provisioning in your `lvmd.conf` file. If you do not need to take volume snapshots, you can use thick volumes.
====

The following `lvmd.yaml` example file shows a basic LVMS configuration:

.LVMS configuration example
[source,yaml]
----
socket-name:
device-classes:
  - name: "default"
    volume-group: "VGNAMEHERE"
    spare-gb: 0 <5>
    default: <6>
----
+
where:
+
--
`socket-name`:: Specifies the UNIX domain socket endpoint of gRPC. Defaults to `/run/lvmd/lvmd.socket`. Takes a string value.
`device-classes`:: Specifies a list of maps for the settings for each `device-class`.
`device-classes.name`:: Specifies the name of the `device-class`. Takes a string value.
`device-classes.volume-group`:: Specifies the group where the `device-class` creates the logical volumes. Takes a string value.
`device-classes.spare-gb`:: Specifies the storage capacity in GB to be left unallocated in the volume group. Defaults to `0`. Takes an unsigned 64-bit integer.
`device-classes.default`:: Specifies that the `device-class` is used by default. Defaults to `false`. At least one value must be entered in the YAML file when this value is set to `true`. Takes a boolean value.
--

[IMPORTANT]
====
A race condition prevents LVMS from accurately tracking the allocated space and preserving the `spare-gb` for a device class when multiple PVCs are created simultaneously. Use separate volume groups and device classes to protect the storage of highly dynamic workloads from each other.
====

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc

[id="microshift-lvms-using_{context}"]
= Using the LVMS

[role="_abstract"]
To automatically provision and mount a logical volume to a pod, use the LVMS default `StorageClass`. By creating a `PersistentVolumeClaim` object without defining the `.spec.storageClassName` field, you trigger the dynamic provisioning of a `PersistentVolume` from this default resource.

Use the following procedure to provision and mount a logical volume to a pod.

.Procedure

* To provision and mount a logical volume to a pod, run the following command:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: my-lv-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1G
---
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: nginx
    image: nginx
    command: ["/usr/bin/sh", "-c"]
    args: ["sleep", "1h"]
    volumeMounts:
    - mountPath: /mnt
      name: my-volume
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
          - ALL
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
  volumes:
    - name: my-volume
      persistentVolumeClaim:
        claimName: my-lv-pvc
EOF
----

// Module included in the following assemblies:
//
// * microshift_storage/volume-snapshots-microshift.adoc

[id="microshift-storage-device-classes_{context}"]
= Device classes

[role="_abstract"]
To define custom storage groups, create custom device classes by adding a `device-classes` array to your logical volume manager storage (LVMS) configuration. With this configuration, you can enable {microshift-short} to categorize devices based on your specific storage requirements.

Add the array to the `/etc/microshift/lvmd.yaml` configuration file. A single device class must be set as the default. You must restart {microshift-short} for configuration changes to take effect.

[WARNING]
====
Removing a device class while there are still persistent volumes or `VolumeSnapshotContent` objects connected to that device class breaks both thick and thin provisioning.
====

You can define multiple device classes in the `device-classes` array. These classes can be a mix of thick and thin volume configurations.

.Example of a mixed `device-class` array
[source,terminal]
----
socket-name: /run/topolvm/lvmd.sock
device-classes:
  - name: ssd
    volume-group: ssd-vg
    spare-gb: 0
    default: true
  - name: hdd
    volume-group: hdd-vg
    spare-gb: 0
  - name: thin
    spare-gb: 0
    thin-pool:
      name: thin
      overprovision-ratio: 10
    type: thin
    volume-group: ssd
  - name: striped
    volume-group: multi-pv-vg
    spare-gb: 0
    stripe: 2
    stripe-size: "64"
    lvcreate-options:
----
** device-classes.spare-gb`: Specifies the spare capacity. When you set this value to anything other than `0`, more space can be allocated than expected.
** `device-classes.lvcreate-options`: Specifies extra arguments to pass to the `lvcreate` command, such as `--type=<type>`. Neither {microshift-short} nor the LVMS verifies `lvcreate-options` values. These optional values are passed as is to the `lvcreate` command. Ensure that the options specified here are correct.
