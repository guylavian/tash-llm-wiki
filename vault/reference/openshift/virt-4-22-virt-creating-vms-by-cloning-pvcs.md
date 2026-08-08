---
title: "Creating VMs by cloning PVCs"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-by-cloning-pvcs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-by-cloning-pvcs
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating VMs by cloning PVCs

[id="virt-creating-vms-by-cloning-pvcs"]
= Creating VMs by cloning PVCs

[role="_abstract"]
You can create virtual machines (VMs) by cloning existing persistent volume claims (PVCs) with custom images.

You must install the QEMU guest agent on VMs created from operating system images that are not provided by Red{nbsp}Hat.

You clone a PVC by creating a data volume that references a source PVC.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-creating-vms-by-cloning-pvcs.adoc

[id="virt-about-cloning_{context}"]
= About cloning

[role="_abstract"]
When cloning a data volume, the Containerized Data Importer (CDI) chooses one of the Container Storage Interface (CSI) clone methods: CSI volume cloning or smart cloning. Both methods are efficient but have certain requirements. If the requirements are not met, the CDI uses host-assisted cloning.

Host-assisted cloning is the slowest and least efficient method of cloning, but it has fewer requirements than either of the other two cloning methods.

[id="csi-volume-cloning_{context}"]
== CSI volume cloning

Container Storage Interface (CSI) cloning uses CSI driver features to more efficiently clone a source data volume.

CSI volume cloning has the following requirements:

* The CSI driver that backs the storage class of the persistent volume claim (PVC) must support volume cloning.
* For provisioners not recognized by the CDI, the corresponding storage profile must have the `cloneStrategy` set to CSI Volume Cloning.
* The source and target PVCs must have the same storage class and volume mode.
* If you create the data volume, you must have permission to create the `datavolumes/source` resource in the source namespace.
* The source volume must not be in use.

[id="smart-cloning_{context}"]
== Smart cloning

When a Container Storage Interface (CSI) plugin with snapshot capabilities is available, the Containerized Data Importer (CDI) creates a persistent volume claim (PVC) from a snapshot, which then allows efficient cloning of additional PVCs.

Smart cloning has the following requirements:

* A snapshot class associated with the storage class must exist.
* The source and target PVCs must have the same storage class and volume mode.
* If you create the data volume, you must have permission to create the `datavolumes/source` resource in the source namespace.
* The source volume must not be in use.

[id="host-assisted-cloning_{context}"]
== Host-assisted cloning

When the requirements for neither Container Storage Interface (CSI) volume cloning nor smart cloning have been met, host-assisted cloning is used as a fallback method. Host-assisted cloning is less efficient than either of the two other cloning methods.

Host-assisted cloning uses a source pod and a target pod to copy data from the source volume to the target volume. The target persistent volume claim (PVC) is annotated with the fallback reason that explains why host-assisted cloning has been used, and an event is created.

Example PVC target annotation:

[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    cdi.kubevirt.io/cloneFallbackReason: The volume modes of source and target are incompatible
    cdi.kubevirt.io/clonePhase: Succeeded
    cdi.kubevirt.io/cloneType: copy
----

Example event:

[source,terminal]
----
NAMESPACE   LAST SEEN   TYPE      REASON                    OBJECT                              MESSAGE
test-ns     0s          Warning   IncompatibleVolumeModes   persistentvolumeclaim/test-target   The volume modes of source and target are incompatible
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-by-cloning-pvcs.adoc
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-container-disks.adoc
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-web-images.adoc

[id="virt-creating-vm-custom-image-web_{context}"]
= Creating a VM {title-frag} by using the web console

[role="_abstract"]
You can create a virtual machine (VM) by importing {a-object} from a {data-source} by using the OpenShift Container Platform web console.
[role="_abstract"]
You can create a virtual machine (VM) by cloning a persistent volume claim (PVC) by using the OpenShift Container Platform web console.

.Prerequisites

* You must have access to the {data-source} that contains the {object}.
* You must have access to the namespace that contains the source PVC.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.
. Click a template tile without an available boot source.
. Click *Customize VirtualMachine*.
. On the *Customize template parameters* page, expand *Storage* and select *{menu-item}* from the *Disk source* list.
. Enter the image URL. Example: `\https://access.redhat.com/downloads/content/69/ver=/rhel---7/7.9/x86_64/product-software`
. Enter the container image URL. Example: `\https://mirror.arizona.edu/fedora/linux/releases/38/Cloud/x86_64/images/Fedora-Cloud-Base-38-1.6.x86_64.qcow2`
. Select the PVC project and the PVC name.
. Set the disk size.
. Click *Next*.
. Click *Create VirtualMachine*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-creating-vms-by-cloning-pvcs.adoc

[id="virt-creating-vm-by-cloning-pvcs-cli_{context}"]
= Creating a VM from a PVC by using the CLI

[role="_abstract"]
You can create a virtual machine (VM) by cloning the persistent volume claim (PVC) of an existing VM by using the command line.

You can clone a PVC by using one of the following options:

* Cloning a PVC to a new data volume.
+
This method creates a data volume whose lifecycle is independent of the original VM. Deleting the original VM does not affect the new data volume or its associated PVC.

* Cloning a PVC by creating a `VirtualMachine` manifest with a `dataVolumeTemplates` stanza.
+
This method creates a data volume whose lifecycle is dependent on the original VM. Deleting the original VM deletes the cloned data volume and its associated PVC.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-by-cloning-pvcs.adoc

[id="virt-optimizing-clone-performance-at-scale-in-openshift-data-foundation_{context}"]
= Optimizing clone Performance at scale in {rh-storage}

[role="_abstract"]
When you use {rh-storage}, the storage profile configures the default cloning strategy as `csi-clone`. However, this method has limitations, as shown in the following link.

After a certain number of clones are created from a persistent volume claim (PVC), a background flattening process begins, which can significantly reduce clone creation performance at scale.

To improve performance when creating hundreds of clones from a single source PVC, use the `VolumeSnapshot` cloning method instead of the default `csi-clone` strategy.

.Procedure

. Create a `VolumeSnapshot` custom resource (CR) of the source image by using the following content:
+
[source,yaml]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: golden-volumesnapshot
  namespace: golden-ns
spec:
  volumeSnapshotClassName: ocs-storagecluster-rbdplugin-snapclass
  source:
    persistentVolumeClaimName: golden-snap-source
----

. Add the  `spec.source.snapshot` stanza to reference the `VolumeSnapshot` as the source for the `DataVolume clone`:
+
[source,yaml]
----
spec:
  source:
    snapshot:
      namespace: golden-ns
      name: golden-volumesnapshot
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-by-cloning-pvcs.adoc

[id="virt-cloning-pvc-to-dv-cli_{context}"]
= Cloning a PVC to a data volume

[role="_abstract"]
You can clone the persistent volume claim (PVC) of an existing virtual machine (VM) disk to a data volume by using the command line.

You create a data volume that references the original source PVC. The lifecycle of the new data volume is independent of the original VM. Deleting the original VM does not affect the new data volume or its associated PVC.

Cloning between different volume modes is supported for host-assisted cloning, such as cloning from a block persistent volume (PV) to a file system PV, as long as the source and target PVs belong to the `kubevirt` content type.

[NOTE]
====
Smart-cloning is faster and more efficient than host-assisted cloning because it uses snapshots to clone PVCs. Smart-cloning is supported by storage providers that support snapshots, such as {rh-storage-first}.

Cloning between different volume modes is not supported for smart-cloning.
====

.Prerequisites

* You have installed the {oc-first}.
* The VM with the source PVC must be powered down.
* If you clone a PVC to a different namespace, you must have permissions to create resources in the target namespace.
* Additional prerequisites for smart-cloning:
** Your storage provider must support snapshots.
** The source and target PVCs must have the same storage provider and volume mode.
** The value of the `driver` key of the `VolumeSnapshotClass` object must match the value of the `provisioner` key of the `StorageClass` object as shown in the following example:
+
Example `VolumeSnapshotClass` object:
+
[source,yaml]
----
kind: VolumeSnapshotClass
apiVersion: snapshot.storage.k8s.io/v1
driver: openshift-storage.rbd.csi.ceph.com
# ...
----
+
Example `StorageClass` object:
+
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
# ...
provisioner: openshift-storage.rbd.csi.ceph.com
----

.Procedure

. Create a `DataVolume` manifest as shown in the following example:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: <datavolume>
spec:
  source:
    pvc:
      namespace: "<source_namespace>"
      name: "<my_vm_disk>"
  storage: {}
----
+
where:
+
`<datavolume>`:: Specifies the name of the new data volume.
`<source_namespace>`:: Specifies the namespace of the source PVC.
`<my_vm_disk>`:: Specifies the name of the source PVC.

. Create the data volume by running the following command:
+
[source,terminal]
----
$ oc create -f <datavolume>.yaml
----
+
[NOTE]
====
Data volumes prevent a VM from starting before the PVC is prepared. You can create a VM that references the new data volume while the
PVC is being cloned.
====

// Module included in the following assemblies:
//
// * virt/creating_vms_advanced/creating_vms_cli/virt-creating-vms-by-cloning-pvcs.adoc

[id="virt-creating-vm-cloning-pvc-data-volume-template_{context}"]
= Creating a VM from a cloned PVC by using a data volume template

[role="_abstract"]
You can create a virtual machine (VM) that clones the persistent volume claim (PVC) of an existing VM by using a data volume template. This method creates a data volume whose lifecycle is independent on the original VM.

.Prerequisites

* The VM with the source PVC must be powered down.
* You have installed the `virtctl` CLI.
* You have installed the {oc-first}.

.Procedure

. Create a `VirtualMachine` manifest for your VM and save it as a YAML file, for example:
+
[source,terminal]
----
$ virtctl create vm --name rhel-9-clone --volume-import type:pvc,src:my-project/imported-volume-q5pr9
----

. Review the `VirtualMachine` manifest for your VM:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: rhel-9-clone
spec:
  dataVolumeTemplates:
  - metadata:
      name: imported-volume-h4qn8
    spec:
      source:
        pvc:
          name: imported-volume-q5pr9
          namespace: my-project
      storage:
        resources: {}
  instancetype:
    inferFromVolume: imported-volume-h4qn8
    inferFromVolumeFailurePolicy: Ignore
  preference:
    inferFromVolume: imported-volume-h4qn8
    inferFromVolumeFailurePolicy: Ignore
  runStrategy: Always
  template:
    spec:
      domain:
        devices: {}
        memory:
          guest: 512Mi
        resources: {}
      terminationGracePeriodSeconds: 180
      volumes:
      - dataVolume:
          name: imported-volume-h4qn8
        name: imported-volume-h4qn8
----
+
* `metadata.name` defines the VM name.
* `spec.dataVolumeTemplates.spec.source.pvc.name` defines the name of the source PVC.
* `spec.dataVolumeTemplates.spec.source.pvc.namespace` defines the namespace of the source PVC.
* `spec.instancetype.inferFromVolume` defines that if the PVC source has appropriate labels, the instance type is inferred from the selected `DataSource` object.
* `spec.preference.inferFromVolume` defines that if the PVC source has appropriate labels, the preference is inferred from the selected `DataSource` object.

. Create the virtual machine with the PVC-cloned data volume:
+
[source,terminal]
----
$ oc create -f <vm_manifest_file>.yaml
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Setting a default cloning strategy using a storage profile
* Installing the QEMU guest agent
* Volume cloning
* CSI volume snapshots
