---
title: "Preparing CDI scratch space"
type: reference
domain: openshift
slug: virt-4-22-virt-preparing-cdi-scratch-space
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-preparing-cdi-scratch-space
version: 4.22
family: virt
documentKind: "Documentation"
---

# Preparing CDI scratch space

[id="virt-preparing-cdi-scratch-space"]
= Preparing CDI scratch space

[role="_abstract"]
To support image import and processing, configure the Containerized Data Importer (CDI) scratch space and the required storage class so that CDI can temporarily store and convert virtual machine (VM) images.

// Module included in the following assemblies:
//
// * virt/storage/virt-preparing-cdi-scratch-space.adoc

[id="virt-about-scratch-space_{context}"]
= About scratch space

[role="_abstract"]
The Containerized Data Importer (CDI) requires scratch space (temporary storage) to complete some operations, such as importing and uploading virtual machine images.
During this process, CDI provisions a scratch space PVC equal to the size of the PVC backing the destination data volume (DV).

The scratch space PVC is deleted after the operation completes or aborts.

You can define the storage class that is used to bind the scratch space PVC in the `spec.scratchSpaceStorageClass` field of the `HyperConverged` custom resource.

If the defined storage class does not match a storage class in the cluster, then the default storage class defined for the cluster is used.
If there is no default storage class defined in the cluster, the storage class used to provision the original DV or PVC is used.

[NOTE]
====
CDI requires requesting scratch space with a `file` volume mode, regardless of the PVC backing the origin data volume.
If the origin PVC is backed by `block` volume mode, you must define a storage class capable of provisioning `file` volume mode PVCs.
====

== Manual provisioning

If there are no storage classes, CDI uses any PVCs in the project that match the size requirements for the image.
If there are no PVCs that match these requirements, the CDI import pod remains in a *Pending* state until an appropriate PVC is made available or until a timeout function kills the pod.

// Module included in the following assemblies:
//
// * virt/storage/virt-preparing-cdi-scratch-space.adoc

[id="virt-operations-requiring-scratch-space_{context}"]
= CDI operations that require scratch space

[role="_abstract"]
To import and process virtual machine (VM) images, the Containerized Data Importer (CDI) uses scratch space as temporary storage during specific operations such as registry imports and image uploads.

[options="header"]
|===
| Type | Reason

| Registry imports
| CDI must download the image to a scratch space and extract the layers to find the image file. The image file is then passed to QEMU-IMG for conversion to a raw disk.

| Upload image
| QEMU-IMG does not accept input from STDIN. Instead, the image to upload is saved in scratch space before it can be passed to QEMU-IMG for conversion.

| HTTP imports of archived images
| QEMU-IMG does not know how to handle the archive formats CDI supports. Instead, the image is unarchived and saved into scratch space before it is passed to QEMU-IMG.

| HTTP imports of authenticated images
| QEMU-IMG inadequately handles authentication. Instead, the image is saved to scratch space and authenticated before it is passed to QEMU-IMG.

| HTTP imports of custom certificates
| QEMU-IMG inadequately handles custom certificates of HTTPS endpoints. Instead, CDI downloads the image to scratch space before passing the file to QEMU-IMG.
|===

// Module included in the following assemblies:
//
// * virt/storage/virt-preparing-cdi-scratch-space.adoc

[id="virt-defining-storageclass_{context}"]
= Defining a storage class

[role="_abstract"]
You can define the storage class that the Containerized Data Importer (CDI) uses when allocating scratch space by adding the `spec.scratchSpaceStorageClass` field to the `HyperConverged` custom resource (CR).

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

. Edit the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the `spec.scratchSpaceStorageClass` field to the CR and set the value to the name of a storage class that exists in the cluster. If you do not specify a storage class, CDI uses the storage class of the persistent volume claim that is being populated.
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  scratchSpaceStorageClass: "<storage_class>"
----

. Save and exit your default editor to update the `HyperConverged` CR.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-uploading-local-disk-images-virtctl.adoc
// * virt/virtual_machines/virtual_disks/virt-uploading-local-disk-images-block.adoc
// * virt/storage/virt-preparing-cdi-scratch-space.adoc
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-disk-into-new-datavolume.adoc
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-using-datavolumetemplate.adoc
// * virt/virtual_machines/cloning_vms/virt-cloning-vm-disk-to-new-block-storage-pvc.adoc
// * virt/virtual_machines/importing_vms/virt-importing-virtual-machine-images-datavolumes.adoc
// * virt/virtual_machines/importing_vms/virt-importing-virtual-machine-images-datavolumes-block.adoc
// * virt/virtual_machines/virtual_disks/virt-uploading-local-disk-images-web.adoc

[id="virt-cdi-supported-operations-matrix_{context}"]
= CDI supported operations matrix

[role="_abstract"]
This matrix shows the supported CDI operations for content types against endpoints, and which of these operations requires scratch space.

|===
|Content types | HTTP | HTTPS | Basic HTTP authentication | Registry | Upload

| KubeVirt (QCOW2)
a|&#10003; QCOW2

&#10003; GZ*

&#10003; XZ*

a|&#10003; QCOW2**

&#10003; GZ*

&#10003; XZ*

a|&#10003; QCOW2

&#10003; GZ*

&#10003; XZ*

a| &#10003; QCOW2*

&#9633; GZ

&#9633; XZ

a| &#10003; QCOW2*

&#10003; GZ*

&#10003; XZ*

| KubeVirt (raw)
a|&#10003; raw

&#10003; GZ

&#10003; XZ

a|&#10003; raw

&#10003; GZ

&#10003; XZ

a| &#10003; raw

&#10003; GZ

&#10003; XZ

a| &#10003; raw*

&#9633; GZ

&#9633; XZ

a| &#10003; raw*

&#10003; GZ*

&#10003; XZ*
|===

[horizontal]
&#10003;:: Supported operation
&#9633;:: Unsupported operation
$$*$$:: Requires scratch space
$$**$$:: Requires scratch space if a custom certificate authority is required

[id="{context}-additional-resources"]
[role="_additional-resources"]
== Additional resources

* Dynamic provisioning
