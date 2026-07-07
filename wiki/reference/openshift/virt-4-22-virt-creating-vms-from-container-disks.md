---
title: "Creating VMs by using container disks"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-from-container-disks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-from-container-disks
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating VMs by using container disks

[id="virt-creating-vms-from-container-disks"]
= Creating VMs by using container disks

[role="_abstract"]
You can create virtual machines (VMs) by using container disks built from operating system images.

You can enable auto updates for your container disks. For more information, see "Additional resources".

// Hiding links in ROSA/OSD
[IMPORTANT]
====
If the container disks are large, the I/O traffic might increase and cause worker nodes to be unavailable. You can perform the following tasks to reclaim resources:

* Prune `DeploymentConfig` objects.
* Configure garbage collection.
====

[IMPORTANT]
====
If the container disks are large, the I/O traffic might increase and cause worker nodes to be unavailable. You can prune `DeploymentConfig` objects to resolve this issue:
====

You create a VM from a container disk by performing the following steps:

. Build an operating system image into a container disk and upload it to your container registry.
. If your container registry does not have TLS, configure your environment to disable TLS for your registry.
. Create a VM with the container disk as the disk source by using the OpenShift Container Platform web console or the command line.

[IMPORTANT]
====
You must install the QEMU guest agent on VMs created from operating system images that are not provided by Red{nbsp}Hat.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-container-disks.adoc

[id="virt-preparing-container-disk-for-vms_{context}"]
= Building and uploading a container disk

[role="_abstract"]
You can build a virtual machine (VM) image into a container disk and upload it to a registry.

The size of a container disk is limited by the maximum layer size of the registry where the container disk is hosted.

[NOTE]
====
For {quay}, you can change the maximum layer size by editing the YAML configuration file that is created when {quay} is first deployed.
====

.Prerequisites

* You must have `podman` installed.
* You must have a QCOW2 or RAW image file.

.Procedure

. Create a Dockerfile to build the VM image into a container image. The VM image must be owned by QEMU, which has a UID of `107`, and placed in the `/disk/` directory inside the container. Permissions for the `/disk/` directory must then be set to `0440`.
+
The following example uses the Red Hat Universal Base Image (UBI) to handle these configuration changes in the first stage, and uses the minimal `scratch` image in the second stage to store the result:
+
[source,terminal]
----
$ cat > Dockerfile << EOF
FROM registry.access.redhat.com/ubi8/ubi:latest AS builder
ADD --chown=107:107 <vm_image>.qcow2 /disk/ //
RUN chmod 0440 /disk/*

FROM scratch
COPY --from=builder /disk/* /disk/
EOF
----
+
where:
+
`<vm_image>`:: Specifies the image in either QCOW2 or RAW format. If you use a remote image, replace `<vm_image>.qcow2` with the complete URL.

. Build and tag the container:
+
[source,terminal]
----
$ podman build -t <registry>/<container_disk_name>:latest .
----

. Push the container image to the registry:
+
[source,terminal]
----
$ podman push <registry>/<container_disk_name>:latest
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-container-disks.adoc

[id="virt-disabling-tls-for-registry_{context}"]
= Disabling TLS for a container registry

[role="_abstract"]
You can disable TLS (transport layer security) for one or more container registries by editing the `insecureRegistries` field of the `HyperConverged` custom resource.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add a list of insecure registries to the `spec.storageImport.insecureRegistries` field.
+
Example `HyperConverged` custom resource:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  storageImport:
    insecureRegistries:
      - "private-registry-example-1:5000"
      - "private-registry-example-2:5000"
----
+
Replace the examples in the `insecureRegistries` list with valid registry hostnames.

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
// * virt/creating_vms_advanced/creating_vms_cli/virt-creating-vms-from-container-disks.adoc

[id="virt-creating-vm-import-cli_{context}"]
= Creating a VM from a container disk by using the CLI

[role="_abstract"]
You can create a virtual machine (VM) from a container disk by using the command line.

.Prerequisites

* You must have access credentials for the container registry that contains the container disk.
* You have installed the `virtctl` CLI.
* You have installed the {oc-first}.

.Procedure

. Create a `VirtualMachine` manifest for your VM and save it as a YAML file. For example, to create a minimal {op-system-base-full} VM from a container disk, run the following command:
+
[source,terminal]
----
$ virtctl create vm --name vm-rhel-9 --instancetype u1.small --preference rhel.9 --volume-containerdisk src:registry.redhat.io/rhel9/rhel-guest-image:9.5
----

. Review the `VirtualMachine` manifest for your VM:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-rhel-9
spec:
  instancetype:
    name: u1.small
  preference:
    name: rhel.9
  runStrategy: Always
  template:
    metadata:
      creationTimestamp: null
    spec:
      domain:
        devices: {}
        resources: {}
      terminationGracePeriodSeconds: 180
      volumes:
      - containerDisk:
          image: registry.redhat.io/rhel9/rhel-guest-image:9.5
        name: vm-rhel-9-containerdisk-0
----
+
* `metadata.name` defines the VM name.
* `spec.instancetype.name` defines the instance type to use to control resource sizing of the VM.
* `spec.preference.name` defines the preference to use.
* `spec.template.spec.volumes.containerDisk.image` defines the URL of the container disk.

. Create the VM by running the following command:
+
[source,terminal]
----
$ oc create -f <vm_manifest_file>.yaml
----

.Verification

. Monitor the status of the VM:
+
[source,terminal]
----
$ oc get vm <vm_name>
----
+
If the provisioning is successful, the VM status is `Running`. Example output:
+
[source,terminal]
----
NAME        AGE   STATUS    READY
vm-rhel-9   18s   Running   True
----

. Verify that provisioning is complete and that the VM has started by accessing its serial console:
+
[source,terminal]
----
$ virtctl console <vm_name>
----
+
If the VM is running and the serial console is accessible, the output looks as follows:
+
[source,terminal]
----
Successfully connected to vm-rhel-9 console. The escape sequence is ^]
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Managing automatic boot source updates
* Installing the QEMU guest agent
* Pruning objects to reclaim resources
* Configuring garbage collection for containers and images
