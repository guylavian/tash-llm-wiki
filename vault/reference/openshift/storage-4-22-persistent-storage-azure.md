---
title: "Persistent storage using Azure"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-azure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-azure
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using Azure

[id="persistent-storage-using-azure"]
= Persistent storage using Azure

OpenShift Container Platform supports Microsoft Azure Disk volumes. You can
provision your OpenShift Container Platform cluster with persistent storage using Azure.
Some familiarity with Kubernetes and Azure is assumed.
The Kubernetes persistent volume framework allows administrators to provision a
cluster with persistent storage and gives users a way to request those
resources without having any knowledge of the underlying infrastructure.
Azure Disk volumes can be provisioned dynamically.
Persistent volumes are not bound to a single project or namespace; they can be
shared across the OpenShift Container Platform cluster.
Persistent volume claims are specific to a project or namespace and can be
requested by users.

[IMPORTANT]
====
OpenShift Container Platform 4.11 and later provides automatic migration for the Azure Disk in-tree volume plugin to its equivalent CSI driver.

CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes. For more information about migration, see CSI automatic migration.
====

[IMPORTANT]
====
High availability of storage in the infrastructure is left to the underlying
storage provider.
====

[role="_additional-resources"]
.Additional resources

* Microsoft Azure Disk

// Module included in the following assemblies:
//
// * storage/persistent_storage-azure.adoc

[id="storage-create-azure-storage-class_{context}"]
= Creating the Azure storage class

Storage classes are used to differentiate and delineate storage levels and
usages. By defining a storage class, users can obtain dynamically provisioned
persistent volumes.

.Procedure

. In the OpenShift Container Platform web console, click *Storage* -> *Storage Classes*.

. In the storage class overview, click *Create Storage Class*.

. Define the desired options on the page that appears.

.. Enter a name to reference the storage class.

.. Enter an optional description.

.. Select the reclaim policy.

.. Select `kubernetes.io/azure-disk` from the drop down list.

... Enter the storage account type. This corresponds to your Azure
storage account SKU tier. Valid options are `Premium_LRS`, `PremiumV2_LRS`, `Standard_LRS`,
`StandardSSD_LRS`, and `UltraSSD_LRS`.
+
[IMPORTANT]
====
The skuname `PremiumV2_LRS` is not supported in all regions, and in some supported regions, not all of the availability zones are supported. For more information, see Azure doc.
====

... Enter the kind of account. Valid options are `shared`, `dedicated,`
and `managed`.
+
[IMPORTANT]
====
Red Hat only supports the use of `kind: Managed` in the storage class.

With `Shared` and `Dedicated`, Azure creates unmanaged disks, while OpenShift Container Platform creates a managed disk for machine OS (root) disks. But because Azure Disk does not allow the use of both managed and unmanaged disks on a node, unmanaged disks created with `Shared` or `Dedicated` cannot be attached to OpenShift Container Platform nodes.
====

.. Enter additional parameters for the storage class as desired.

. Click *Create* to create the storage class.

[role="_additional-resources"]
.Additional resources

* https://kubernetes.io/docs/concepts/storage/storage-classes/#new-azure-disk-storage-class-starting-from-v1-7-2[Azure Disk Storage Class]

// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc

[id="creating-volume-claim_{context}"]
= Creating the persistent volume claim

.Prerequisites

Storage must exist in the underlying infrastructure before it can be mounted as
a volume in OpenShift Container Platform.

.Procedure

. In the OpenShift Container Platform web console, click *Storage* -> *Persistent Volume Claims*.

. In the persistent volume claims overview, click *Create Persistent Volume Claim*.

. Define the desired options on the page that appears.

.. Select the previously-created storage class from the drop-down menu.

.. Enter a unique name for the storage claim.

.. Select the access mode. This selection determines the read and write access for the storage claim.

.. Define the size of the storage claim.

. Click *Create* to create the persistent volume claim and generate a persistent
volume.

// Module included in the following assemblies:
//
// * storage/persistent_storage-azure.adoc

[id="volume-format-azure_{context}"]
= Volume format

Before OpenShift Container Platform mounts the volume and passes it to a container, it checks
that it contains a file system as specified by the `fsType` parameter in the
persistent volume definition. If the device is not formatted with the file
system, all data from the device is erased and the device is automatically
formatted with the given file system.

This allows using unformatted Azure volumes as persistent volumes, because
OpenShift Container Platform formats them before the first use.

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
* Machine sets that deploy machines on ultra disks using CSI PVCs
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
