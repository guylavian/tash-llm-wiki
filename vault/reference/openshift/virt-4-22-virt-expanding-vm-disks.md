---
title: "Expand virtual machine disks"
type: reference
domain: openshift
slug: virt-4-22-virt-expanding-vm-disks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-expanding-vm-disks
version: 4.22
family: virt
documentKind: "Documentation"
---

# Expand virtual machine disks

[id="virt-expanding-vm-disks"]
= Expand virtual machine disks

[role="_abstract"]
Expand the  persistent volume claim (PVC) of your virtual machine disk to accomodate growing data requirements. If your storage provider does not support volume expansion, you can expand the available virtual storage of a VM by adding blank data volumes.

You cannot reduce the size of a VM disk.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-expanding-vm-disks.adoc

[id="virt-expanding-vm-disk-pvc-web-console_{context}"]
= Expand a VM disk PVC by using the web console

[role="_abstract"]
You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk. To specify the increased PVC volume, you can use the *VirtualMachines* page in the web console, with the VM running.

[NOTE]
====
If the PVC uses the file system volume mode, the disk image file expands to the available size while reserving some space for file system overhead.
====

.Procedure

. In the *Administrator* or *Virtualization* perspective, open the *VirtualMachines* page.
. Select the running VM to open its *Details* page.
. Select the *Configuration* tab and click *Storage*.
. Click the options menu {kebab} next to the disk you want to expand. Select the *Edit* option.
+
The *Edit disk* dialog opens.
. In the *PersistentVolumeClaim size* field, enter the desired size.
+
[NOTE]
====
You can enter any value greater than the current one. However, if the new value exceeds the available size, an error is displayed.
====
. Click *Save*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-expanding-vm-disks.adoc

[id="virt-expanding-vm-disk-pvc-cli_{context}"]
= Expanding a VM disk PVC by using the CLI

[role="_abstract"]
You can increase the size of a virtual machine (VM) disk by expanding the persistent volume claim (PVC) of the disk. To specify the increased PVC volume, you can edit the `PersistentVolumeClaim` manifest by using the {oc-first}.

[NOTE]
====
If the PVC uses the file system volume mode, the disk image file expands to the available size while reserving some space for file system overhead.
====

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Edit the `PersistentVolumeClaim` manifest of the VM disk that you want to expand:
+
[source,terminal]
----
$ oc edit pvc <pvc_name>
----

. Update the disk size:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
   name: vm-disk-expand
spec:
  accessModes:
     - ReadWriteOnce
     - ReadWriteMany
  resources:
    requests:
       storage: 3Gi
# ...
----
** `spec.resources.requests.storage` specifies the new disk size.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-expanding-vm-disks.adoc

[id="virt-expanding-storage-with-data-volumes_{context}"]
= Expanding available virtual storage by adding blank data volumes

[role="_abstract"]
You can expand the available storage of a virtual machine (VM) by adding blank data volumes.

.Prerequisites

* You must have at least one persistent volume.
* You have installed the {oc-first}.

.Procedure

. Create a `DataVolume` manifest as shown in the following example:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: blank-image-datavolume
spec:
  source:
    blank: {}
  storage:
    resources:
      requests:
        storage: <2Gi>
  storageClassName: "<storage_class>"
----
** `spec.storage.resources.requests.storage` specifies the amount of available space requested for the data volume.
** `spec.storageClassName` is an optional field that specifies a storage class. If you do not specify a storage class, the default storage class is used.

. Create the data volume by running the following command:
+
[source,terminal]
----
$ oc create -f <blank-image-datavolume>.yaml
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Extending a basic volume in Windows
* Extending an existing file system partition without destroying data in Red Hat Enterprise Linux
* Extending a logical volume and its file system online in Red Hat Enterprise Linux
* Configuring preallocation mode for data volumes
* Managing data volume annotations
