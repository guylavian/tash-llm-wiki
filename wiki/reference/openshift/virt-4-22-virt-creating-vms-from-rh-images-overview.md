---
title: "Creating virtual machines from Red Hat images"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-from-rh-images-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-from-rh-images-overview
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating virtual machines from Red Hat images

[id="virt-creating-vms-from-rh-images-overview"]
= Creating virtual machines from Red Hat images

[role="_abstract"]
{op-system-base} images are golden images. They are published as container disks in a secure registry. The Containerized Data Importer (CDI) polls and imports the container disks into your cluster and stores them in the `openshift-virtualization-os-images` project as snapshots or persistent volume claims (PVCs). You can optionally use a custom namespace for golden images.

{op-system-base} images are automatically updated. You can disable and re-enable automatic updates for these images. For more information, see "Additional resources".

Cluster administrators can enable automatic subscription for {op-system-base} virtual machines in the OpenShift Container Platform web console.

You can create virtual machines (VMs) from operating system images provided by Red{nbsp}Hat by using one of the following methods:

* Create a VM from a template by using the web console.

* Create a VM from an instance type by using the web console.

* Create a VM from a `VirtualMachine` manifest by using the command line.

[IMPORTANT]
====
Do not create VMs in the default `openshift-*` namespaces. Instead, create a new namespace or use an existing namespace without the `openshift` prefix.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_rh/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-about-golden-images_{context}"]
= About golden images

[role="_abstract"]
A golden image is a preconfigured snapshot of a virtual machine (VM) that you can use as a resource to deploy new VMs. For example, you can use golden images to provision the same system environment consistently and deploy systems more quickly and efficiently.

[id="virt-how-golden-images-work_{context}"]
== How do golden images work?

Golden images are created by installing and configuring an operating system and software applications on a reference machine or virtual machine. This includes setting up the system, installing required drivers, applying patches and updates, and configuring specific options and preferences.

After the golden image is created, it is saved as a template or image file that can be replicated and deployed across multiple clusters. The golden image can be updated by its maintainer periodically to incorporate necessary software updates and patches, ensuring that the image remains up to date and secure, and newly created VMs are based on this updated image.

[id="virt-golden-images-implementation_{context}"]
== Red Hat implementation of golden images

Red Hat publishes golden images as container disks in the registry for versions of {op-system-base-full}. Container disks are virtual machine images that are stored as a container image in a container image registry. Any published image will automatically be made available in connected clusters after the installation of OpenShift Virtualization. After the images are available in a cluster, they are ready to use to create VMs.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_rh/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-about-vms-and-boot-sources_{context}"]
= About VM boot sources

[role="_abstract"]
Virtual machines (VMs) consist of a VM definition and one or more disks that are backed by data volumes. VM templates enable you to create VMs using predefined specifications.

Every template requires a boot source, which is a fully configured disk image including configured drivers. Each template contains a VM definition with a pointer to the boot source. Each boot source has a predefined name and namespace. For some operating systems, a boot source is automatically provided. If it is not provided, then an administrator must prepare a custom boot source.

Provided boot sources are updated automatically to the latest version of the operating system. For auto-updated boot sources, persistent volume claims (PVCs) and volume snapshots are created with the cluster's default storage class. If you select a different default storage class after configuration, you must delete the existing boot sources in the cluster namespace that are configured with the previous default storage class.

// Module included in the following assemblies:
//
// * virt/creating_vms_advanced/creating_vms_advanced_web/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-golden-images-namespace-web_{context}"]
= Configuring a custom namespace for golden images by using the web console

[role="_abstract"]
You can configure a custom namespace for golden images in your cluster by using the OpenShift Container Platform web console.

.Procedure

. In the web console, select *Virtualization* -> *Settings*.

. On the *Cluster* tab, select *General settings* -> *Templates and images management*.

. Click *Bootable volumes project*.

. Select a namespace to use for golden images.
.. If you already created a namespace, select it from the *Project* list.

.. If you did not create a namespace, scroll to the bottom of the list and click *Create project*.

... Enter a name for your new namespace in the *Name* field of the *Create project* dialog.

... Click *Create*.

// Module included in the following assemblies:
//
// * virt/creating_vms_advanced/creating_vms_advanced_web/virt-creating-vms-from-rh-images-overview.adoc

[id="virt-golden-images-namespace-cli_{context}"]
= Configuring a custom namespace for golden images by using the CLI

[role="_abstract"]
You can configure a custom namespace for golden images in your cluster by setting the `spec.commonBootImageNamespace` field in the `HyperConverged` custom resource (CR).

.Prerequisites

* You installed the {oc-first}.
* You created a namespace to use for golden images.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Configure the custom namespace by updating the value of the `spec.commonBootImageNamespace` field.
+
Example configuration file:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  commonBootImageNamespace: <custom_namespace>
# ...
----
+
where:
+
`spec.commonBootImageNamespace`:: Specifies the namespace to use for golden images.

. Save your changes and exit the editor.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Managing Red{nbsp}Hat boot source updates
* Creating a VM from a template by using the web console
* Creating a VM from an instance type by using the web console
* Creating a VM from a `VirtualMachine` manifest by using the command line
