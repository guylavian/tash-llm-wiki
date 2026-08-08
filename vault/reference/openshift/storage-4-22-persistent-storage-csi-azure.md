---
title: "Azure Disk CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-azure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-azure
version: 4.22
family: storage
documentKind: "Documentation"
---

# Azure Disk CSI Driver Operator

[id="persistent-storage-csi-azure-disk"]
= Azure Disk CSI Driver Operator

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Microsoft Azure Disk Storage.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to Azure Disk storage assets, OpenShift Container Platform installs the Azure Disk CSI Driver Operator and the Azure Disk CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* The _Azure Disk CSI Driver Operator_ provides a storage class named `managed-csi` that you can use to create persistent volume claims (PVCs). The Azure Disk CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage. You can disable this default storage class if desired (see Managing the default storage class).

* The _Azure Disk CSI driver_ enables you to create and mount Azure Disk PVs.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

[NOTE]
====
OpenShift Container Platform provides automatic migration for the Azure Disk in-tree volume plugin to its equivalent CSI driver. For more information, see CSI automatic migration.
====

//
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-azure.adoc
//

[id="persistent-storage-csi-azure-disk-sc-zrs_{context}"]
= Creating a storage class with storage account type

Storage classes are used to differentiate and delineate storage levels and usages. By defining a storage class, you can obtain dynamically provisioned persistent volumes.

When creating a storage class, you can designate the storage account type. This corresponds to your Azure storage account SKU tier. Valid options are `Standard_LRS`, `Premium_LRS`, `StandardSSD_LRS`, `UltraSSD_LRS`, `Premium_ZRS`, `StandardSSD_ZRS`, and `PremiumV2_LRS`. For information about finding your Azure SKU tier, see SKU Types.

Both ZRS and PremiumV2_LRS have some region limitations. For information about these limitations, see ZRS limitations and Premium_LRS limitations.

.Prerequisites

* Access to an OpenShift Container Platform cluster with administrator rights

.Procedure

Use the following steps to create a storage class with a storage account type.

. Create a storage class designating the storage account type using a YAML file similar to the following:
+
[source,terminal]
--
$ oc create -f - << EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class> <1>
provisioner: disk.csi.azure.com
parameters:
  skuName: <storage-class-account-type> <2>
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
EOF
--
<1> Storage class name.
<2> Storage account type. This corresponds to your Azure storage account SKU tier:`Standard_LRS`, `Premium_LRS`, `StandardSSD_LRS`, `UltraSSD_LRS`, `Premium_ZRS`, `StandardSSD_ZRS`, `PremiumV2_LRS`.
+
[NOTE]
====
For PremiumV2_LRS, specify `cachingMode: None` in `storageclass.parameters`.
====

. Ensure that the storage class was created by listing the storage classes:
+
[source,terminal]
--
$ oc get storageclass
--
+
[source,terminal]
.Example output
--
$ oc get storageclass
NAME                    PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
azurefile-csi           file.csi.azure.com   Delete          Immediate              true                   68m
managed-csi (default)   disk.csi.azure.com   Delete          WaitForFirstConsumer   true                   68m
sc-prem-zrs             disk.csi.azure.com   Delete          WaitForFirstConsumer   true                   4m25s <1>
--
<1> New storage class with storage account type.

== Performance plus for Azure Disk

//
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-azure.adoc
//

[id="persistent-storage-csi-azure-disk-perf-plus-overview_{context}"]
= Overview

By enabling performance plus, the Input/Output Operations Per Second (IOPS) and throughput limits can be increased for the following types of disks that are 513 GiB, and larger:

* Azure Premium solid-state drives (SSD)

* Standard SSDs

* Standard hard disk drives (HDD)

To see what the increased limits are for IOPS and throughput, consult the columns that begin with *Expanded* in the tables in Scalability and performance targets for VM disks.

//
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-azure.adoc
//

[id="persistent-storage-csi-azure-disk-perf-plus-limits_{context}"]
= Limitations

Performance plus for Azure Disk has the following limitations:

* Can be enabled only on Standard HDD, Standard SSD, and Premium SSD managed disks that are 513 GiB or larger.
+
[IMPORTANT]
====
If you request a smaller value, the disk size is rounded up to 513GiB.
====

* Can be enabled only on new disks. For a workaround, see Section _Enabling performance plus by snapshot or cloning_.

//
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-azure.adoc
//

[id="persistent-storage-csi-azure-disk-perf-plus-sc_{context}"]
= Creating a storage class to use performance plus enhanced disks

The following procedure explains how to create a storage class to use performance plus enhanced Azure disks.

.Prerequisites

* Access to a Microsoft Azure cluster with cluster-admin privileges.

* Access to an Azure disk with performance plus enabled.
+
For information about enabling performance plus on disks, see the Microsoft Azure storage documentation.

.Procedure

To create a storage class to use performance plus enhanced disks:

. Create a storage class using the following example YAML file:
+
.Example storage class YAML file
[resource,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <azure-disk-performance-plus-sc> <1>
provisioner: disk.csi.azure.com <2>
parameters:
  skuName: Premium_LRS <3>
  cachingMode: ReadOnly
  enablePerformancePlus: "true" <4>
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
----
<1> Name of the storage class.
<2> Specifies the Azure Disk Container Storage Interface (CSI) driver provisioner.
<3> Specifies the Azure disk type SKU. In this example, `Premium_LRS` for Premium SSD Locally Redundant Storage.
<4> Enables Azure Disk performance plus.

. Create a persistent volume claim (PVC) that uses this storage class by using the following example YAML file:
+
.Example PVC YAML file
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: <my-azure-pvc> <1>
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: <azure-disk-performance-plus-sc> <2>
  resources:
    requests:
      storage: 513Gi <3>
----
<1> PVC name.
<2> Reference the performance plus storage class.
<3> Any disk size smaller than 513GiB is automatically rounded up.

//
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-azure.adoc
//

[id="persistent-storage-csi-azure-disk-perf-plus-create-new-disk-by-snapshot-clone_{context}"]
= Enabling performance plus by snapshot or cloning

Normally, performance plus can be enabled only on new disks. For a workaround, you can use this procedure.

.Prerequisites

* Access to a Microsoft Azure cluster with cluster-admin privileges.

* Access to an Azure disk with performance plus enabled.

* Have created a storage class to use performance plus enhanced Azure disks.
+
For more information about creating the storage class, see Section _Creating a storage class to use performance plus enhanced disks_.

.Procedure
To enable performance plus by snapshot or clone:

. Create a snapshot of the existing volume that does not have performance plus enabled on it.

. Provision a new disk from that snapshot using a storage class with `enablePerformancePlus` set to "true".

Or

* Clone the persistent volume claim (PVC) using a storage class with `enablePerformancePlus` set to "true" to create a new disk clone.

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-azure.adoc
// storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="byok_{context}"]
= User-managed encryption

The user-managed encryption feature allows you to provide keys during installation that encrypt OpenShift Container Platform node root volumes, and enables all managed storage classes to use these keys to encrypt provisioned storage volumes. You must specify the custom key in the `platform.<cloud_type>.defaultMachinePlatform` field in the install-config YAML file.

This features supports the following storage types:

* Amazon Web Services (AWS) Elastic Block storage (EBS)

* Microsoft Azure Disk storage

* Google Cloud Platform (GCP) persistent disk (PD) storage

* IBM Virtual Private Cloud (VPC) Block storage

[NOTE]
====
If the OS (root) disk is encrypted, and there is no encrypted key defined in the storage class, Azure Disk CSI driver uses the OS disk encryption key by default to encrypt provisioned storage volumes.
====

For information about installing with user-managed encryption for Azure, see Enabling user-managed encryption for Azure.

//Machine sets that deploy machines on ultra disks using PVCs
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * storage/persistent_storage/persistent-storage-azure.adoc
// * storage/persistent_storage/persistent-storage-csi-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-azure-ultra-disk_{context}"]
= Machine sets that deploy machines with ultra disks as data disks
= Machine sets that deploy machines with ultra disks using PVCs

[role="_abstract"]
You can create a machine set running on {azure-first} that deploys machines with ultra disks. Ultra disks are high-performance storage that are intended for use with the most demanding data workloads.

You can also create a persistent volume claim (PVC) that dynamically binds to a storage class backed by {azure-short} ultra disks and mounts them to pods.

[NOTE]
====
Data disks do not support the ability to specify disk throughput or disk IOPS. You can configure these properties by using PVCs.
====

Both the in-tree plugin and CSI driver support using PVCs to enable ultra disks. You can also deploy machines with ultra disks as data disks without creating a PVC.

[role="_additional-resources"]
.Additional resources
* Microsoft Azure ultra disks documentation
* Machine sets that deploy machines on ultra disks using in-tree PVCs
* Machine sets that deploy machines on ultra disks as data disks

//Creating machines on ultra disks by using compute machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * storage/persistent_storage/persistent-storage-azure.adoc
// * storage/persistent_storage/persistent-storage-csi-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-creating-azure-ultra-disk_{context}"]
= Creating machines with ultra disks by using machine sets

[role="_abstract"]
You can deploy machines with ultra disks on {azure-first} by editing your machine set YAML file.

.Prerequisites

* Have an existing {azure-full} cluster.

.Procedure

. Create a custom secret in the `openshift-machine-api` namespace using the `{machine-role}` data secret by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api \
get secret <role>-user-data \
--template='{{index .data.userData | base64decode}}' | jq > userData.txt
----
+
where:
+
--
`<role>`:: Replace with `{machine-role}`.
`userData.txt`:: Specifies `userData.txt` as the name of the new custom secret.
--
. In a text editor, open the `userData.txt` file and locate the final `}` character in the file.

.. On the immediately preceding line, add a `,`.

.. Create a new line after the `,` and add the following configuration details:
+
[source,json]
----
"storage": {
  "disks": [
    {
      "device": "/dev/disk/azure/scsi1/lun0",
      "partitions": [
        {
          "label": "lun0p1",
          "sizeMiB": 1024,
          "startMiB": 0
        }
      ]
    }
  ],
  "filesystems": [
    {
      "device": "/dev/disk/by-partlabel/lun0p1",
      "format": "xfs",
      "path": "/var/lib/lun0p1"
    }
  ]
},
"systemd": {
  "units": [
    {
      "contents": "[Unit]\nBefore=local-fs.target\n[Mount]\nWhere=/var/lib/lun0p1\nWhat=/dev/disk/by-partlabel/lun0p1\nOptions=defaults,pquota\n[Install]\nWantedBy=local-fs.target\n",
      "enabled": true,
      "name": "var-lib-lun0p1.mount"
    }
  ]
}
----
+
where:
+
--
`"disks"`:: Specifies the configuration details for the disk that you want to attach to a node as an ultra disk.
`"device"`:: Specifies the `lun` value that is defined in the `dataDisks` stanza of the machine set you are using. For example, if the machine set contains `lun: 0`, specify `lun0`. You can initialize multiple data disks by specifying multiple `"disks"` entries in this configuration file. If you specify multiple `"disks"` entries, ensure that the `lun` value for each matches the value in the machine set.
`"partitions"`:: Specifies the configuration details for a new partition on the disk.
`"label"`:: Specifies a label for the partition. You might find it helpful to use hierarchical names, such as `lun0p1` for the first partition of `lun0`.
`"sizeMiB"`:: Specifies the total size in MiB of the partition.
`"filesystems"`:: Specifies the filesystem to use when formatting a partition. Use the partition label to specify the partition.
`"units"`:: Specifies a `systemd` unit to mount the partition at boot. Use the partition label to specify the partition. You can create multiple partitions by specifying multiple `"partitions"` entries in this configuration file. If you specify multiple `"partitions"` entries, you must specify a `systemd` unit for each.
`"contents"`:: Specifies the value of `storage.filesystems.path` for `Where`. Specifies the value of `storage.filesystems.device` for `What`.
--
. Extract the disabling template value to a file called `disableTemplating.txt` by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api get secret <role>-user-data \
--template='{{index .data.disableTemplating | base64decode}}' | jq > disableTemplating.txt
----
+
Replace `<role>` with `{machine-role}`.

. Combine the `userData.txt` file and `disableTemplating.txt` file to create a data secret file by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api create secret generic <role>-user-data-x5 \
--from-file=userData=userData.txt \
--from-file=disableTemplating=disableTemplating.txt
----
+
For `<role>-user-data-x5`, specify the name of the secret. Replace `<role>` with `{machine-role}`.

. Copy an existing {azure-short} `MachineSet` custom resource (CR) and edit it by running the following command:
+
[source,terminal]
----
$ oc edit machineset <machine_set_name>
----
+
where:

`<machine_set_name>`:: Indicates the machine set that you want to provision machines with ultra disks.

. Add the following lines in the positions indicated:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
spec:
  template:
    spec:
      metadata:
        labels:
          disk: ultrassd
      providerSpec:
        value:
          ultraSSDCapability: Enabled
          dataDisks:
          - nameSuffix: ultrassd
            lun: 0
            diskSizeGB: 4
            deletionPolicy: Delete
            cachingType: None
            managedDisk:
              storageAccountType: UltraSSD_LRS
          userDataSecret:
            name: <role>-user-data-x5
----
+
where:
+
--
`spec.template.spec.metadata.labels.disk`:: Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value.
`spec.template.spec.providerSpec.value.ultraSSDCapability`:: Enables the use of ultra disks.
For `dataDisks`, include the entire stanza.
`spec.template.spec.providerSpec.value.dataDisks`:: Ensure you include the entire stanza for `dataDisks`.
`spec.template.spec.providerSpec.value.userDataSecret.name`:: Specifies the user data secret created earlier. Replace `<role>` with `{machine-role}`.
--
. Create a machine set using the updated configuration by running the following command:
+
[source,terminal]
----
$ oc create -f <machine_set_name>.yaml
----

. Edit your control plane machine set CR by running the following command:
+
[source,terminal]
----
$ oc --namespace openshift-machine-api edit controlplanemachineset.machine.openshift.io cluster
----

. Add the following lines in the positions indicated:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: ControlPlaneMachineSet
spec:
  template:
    spec:
      metadata:
        labels:
          disk: ultrassd
      providerSpec:
        value:
          ultraSSDCapability: Enabled
          dataDisks:
          - nameSuffix: ultrassd
            lun: 0
            diskSizeGB: 4
            deletionPolicy: Delete
            cachingType: None
            managedDisk:
              storageAccountType: UltraSSD_LRS
          userDataSecret:
            name: <role>-user-data-x5
----
+
where:
+
--
`spec.template.spec.metadata.labels.disk`:: Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value.
`spec.template.spec.providerSpec.value.ultraSSDCapability`:: Enables the use of ultra disks. For `dataDisks`, include the entire stanza.
`spec.template.spec.providerSpec.value.userDataSecret.name`:: Specifies the user data secret created earlier. Replace `<role>` with `{machine-role}`.
--
. Save your changes.

** For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

** For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

. Create a storage class that contains the following YAML definition:
+
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ultra-disk-sc
parameters:
  cachingMode: None
  diskIopsReadWrite: "2000"
  diskMbpsReadWrite: "320"
  kind: managed
  skuname: UltraSSD_LRS
provisioner: disk.csi.azure.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
----
+
where:
+
--
`metadata.name`:: Specifies the name of the storage class. The example uses `ultra-disk-sc` for this value.
`parameters.diskIopsReadWrite`:: Specifies the number of Input/Output Operations Per Second (IOPS) for the storage class.
`parameters.diskMbpsReadWrite`:: Specifies the throughput in MBps for the storage class.
`provisioner`:: For {azure-full} Kubernetes Service (AKS) version 1.21 or later, use `disk.csi.azure.com`. For earlier versions of AKS, use `kubernetes.io/azure-disk`.
`volumeBindingMode`:: Optional parameter. Specifies this parameter to wait for the creation of the pod that will use the disk.
--
. Create a persistent volume claim (PVC) to reference the `ultra-disk-sc` storage class that contains the following YAML definition:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ultra-disk
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: ultra-disk-sc
  resources:
    requests:
      storage: 4Gi
----
+
where:
+
--
`metadata.name`:: Specifies the name of the PVC. The example uses `ultra-disk` for this value.
`spec.storageClassName`:: Specifies the name of the storage class to use. The example  uses `ultra-disk-sc` storage class.
`spec.resources.requests.storage`:: Specifies the size for the storage class. The minimum value is `4Gi`.
--
. Create a pod that contains the following YAML definition:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: nginx-ultra
spec:
  nodeSelector:
    disk: ultrassd
  containers:
  - name: nginx-ultra
    image: alpine:latest
    command:
      - "sleep"
      - "infinity"
    volumeMounts:
    - mountPath: "/mnt/azure"
      name: volume
  volumes:
    - name: volume
      persistentVolumeClaim:
        claimName: ultra-disk
----
+
where:
+
--
`spec.nodeSelector.disk`:: Specifies the label of the machine set that enables the use of ultra disks. The example uses `disk.ultrassd` for this value.
`spec.volumes.persistentVolumeClaim.claimName`:: Specifies the name of the PVC to attach. This pod references the `ultra-disk` PVC.
--

.Verification

. Validate that the machines are created by running the following command:
+
[source,terminal]
----
$ oc get machines
----
+
The machines should be in the `Running` state.

. For a machine that is running and has a node attached, validate the partition by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host lsblk
----
+
In this command, `oc debug node/<node_name>` starts a debugging shell on the node `<node_name>` and passes a command with `--`. The passed command `chroot /host` provides access to the underlying host OS binaries, and `lsblk` shows the block devices that are attached to the host OS machine.

.Next steps

* To use an ultra disk from within a pod, create a workload that uses the mount point. Create a YAML file similar to the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: ssd-benchmark1
spec:
  containers:
  - name: ssd-benchmark1
    image: nginx
    ports:
      - containerPort: 80
        name: "http-server"
    volumeMounts:
    - name: lun0p1
      mountPath: "/tmp"
  volumes:
    - name: lun0p1
      hostPath:
        path: /var/lib/lun0p1
        type: DirectoryOrCreate
  nodeSelector:
    disktype: ultrassd
----

* To use an ultra disk on the control plane, reconfigure your workload to use the control plane's ultra disk mount point.

//Troubleshooting resources for compute machine sets that enable ultra disks
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * storage/persistent_storage/persistent-storage-azure.adoc
// * storage/persistent_storage/persistent-storage-csi-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-troubleshooting-azure-ultra-disk_{context}"]
= Troubleshooting resources for machine sets that enable ultra disks

[role="_abstract"]
You can recover from issues that you might encounter when you enable ultra disks for machine sets. Review fields, such as disk settings, and ensure that the parameters are correctly configured.

[id="ts-pvc-mounting-ultra_{context}"]
== Unable to mount a persistent volume claim backed by an ultra disk

If there is an issue mounting a persistent volume claim backed by an ultra disk, the pod becomes stuck in the `ContainerCreating` state and an alert is triggered.

For example, if the `additionalCapabilities.ultraSSDEnabled` parameter is not set on the machine that backs the node that hosts the pod, the following error message appears:

[source,terminal]
----
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
----

* To resolve this issue, describe the pod by running the following command:
+
[source,terminal]
----
$ oc -n <stuck_pod_namespace> describe pod <stuck_pod_name>
----

[id="ts-mapi-attach-misconfigure_{context}"]
== Incorrect ultra disk configuration

If an incorrect configuration of the `ultraSSDCapability` parameter is specified in the machine set, the machine provisioning fails.

For example, if the `ultraSSDCapability` parameter is set to `Disabled`, but an ultra disk is specified in the `dataDisks` parameter, the following error message appears:

[source,terminal]
----
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
----

* To resolve this issue, verify that your machine set configuration is correct.

[id="ts-mapi-attach-unsupported_{context}"]
== Unsupported disk parameters

If a region, availability zone, or instance size that is not compatible with ultra disks is specified in the machine set, the machine provisioning fails. Check the logs for the following error message:

[source,terminal]
----
failed to create vm <machine_name>: failure sending request for machine <machine_name>: cannot create vm: compute.VirtualMachinesClient#CreateOrUpdate: Failure sending request: StatusCode=400 -- Original Error: Code="BadRequest" Message="Storage Account type 'UltraSSD_LRS' is not supported <more_information_about_why>."
----

* To resolve this issue, verify that you are using this feature in a supported environment and that your machine set configuration is correct.

[id="ts-mapi-delete_{context}"]
== Unable to delete disks

If the deletion of ultra disks as data disks is not working as expected, the machines are deleted and the data disks are orphaned. You must delete the orphaned disks manually if desired.

[id="additional-resources_persistent-storage-csi-azure"]
[role="_additional-resources"]
== Additional resources
* Persistent storage using Azure Disk
* Configuring CSI volumes
* Microsoft Azure storage documentation
