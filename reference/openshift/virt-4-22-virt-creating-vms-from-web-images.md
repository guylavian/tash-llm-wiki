---
title: "Creating VMs by importing images from web pages"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-from-web-images
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-from-web-images
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating VMs by importing images from web pages

[id="virt-creating-vms-from-web-images"]
= Creating VMs by importing images from web pages

[role="_abstract"]
You can create virtual machines (VMs) by importing operating system images from web pages.

[IMPORTANT]
====
You must install the QEMU guest agent on VMs created from operating system images that are not provided by Red{nbsp}Hat.
====

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
// * virt/creating_vms_advanced/creating_vms_advanced_web/virt-creating-vms-from-web-images.adoc

[id="virt-creating-vm-import-cli_{context}"]
= Creating a VM from an image on a web page by using the CLI

[role="_abstract"]
You can create a virtual machine (VM) from an image on a web page by using the command line.

When the VM is created, the data volume with the image is imported into persistent storage.

.Prerequisites

* You must have access credentials for the web page that contains the image.
* You have installed the `virtctl` CLI.
* You have installed the {oc-first}.

.Procedure

. Create a `VirtualMachine` manifest for your VM and save it as a YAML file. For example, to create a minimal {op-system-base-full} VM from an image on a web page, run the following command:
+
[source,terminal]
----
$ virtctl create vm --name vm-rhel-9 --instancetype u1.small --preference rhel.9 --volume-import type:http,url:https://example.com/rhel9.qcow2,size:10Gi
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
  dataVolumeTemplates:
  - metadata:
      name: imported-volume-6dcpf
    spec:
      source:
        http:
          url: https://example.com/rhel9.qcow2
      storage:
        resources:
          requests:
            storage: 10Gi
  instancetype:
    name: u1.small
  preference:
    name: rhel.9
  runStrategy: Always
  template:
    spec:
      domain:
        devices: {}
        resources: {}
      terminationGracePeriodSeconds: 180
      volumes:
      - dataVolume:
          name: imported-volume-6dcpf
        name: imported-volume-6dcpf
----
+
* `metadata.name` defines the VM name.
* `spec.dataVolumeTemplates.metadata.name` defines the data volume name.
* `spec.dataVolumeTemplates.spec.source.http.url` defines the URL of the image.
* `spec.dataVolumeTemplates.spec.storage.resources.requests.storage` defines the size of the storage requested for the data volume.
* `spec.instancetype.name` defines the instance type to use to control resource sizing of the VM.
* `spec.preference.name` defines the preference to use.

. Create the VM by running the following command:
+
[source,terminal]
----
$ oc create -f <vm_manifest_file>.yaml
----
+
The `oc create` command creates the data volume and the VM. The CDI controller creates an underlying PVC with the correct annotation and the import process begins. When the import is complete, the data volume status changes to `Succeeded`. You can start the VM.
+
Data volume provisioning happens in the background, so there is no need to monitor the process.

.Verification

. The importer pod downloads the image from the specified URL and stores it on the provisioned persistent volume. View the status of the importer pod:
+
[source,terminal]
----
$ oc get pods
----

. Monitor the status of the data volume:
+
[source,terminal]
----
$ oc get dv <data_volume_name>
----
+
If the provisioning is successful, the data volume phase is `Succeeded`.
+
Example output:
+
[source,terminal]
----
NAME                    PHASE       PROGRESS   RESTARTS   AGE
imported-volume-6dcpf   Succeeded   100.0%                18s
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
* Installing the QEMU guest agent
