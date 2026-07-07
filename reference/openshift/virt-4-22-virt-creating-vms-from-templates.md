---
title: "Creating virtual machines from templates"
type: reference
domain: openshift
slug: virt-4-22-virt-creating-vms-from-templates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-creating-vms-from-templates
version: 4.22
family: virt
documentKind: "Documentation"
---

# Creating virtual machines from templates

[id="virt-creating-vms-from-templates"]
= Creating virtual machines from templates

[role="_abstract"]
You can create virtual machines (VMs) from Red Hat templates by using the OpenShift Container Platform web console.

[id="virt-about-templates"]
== About VM templates

You can use VM templates to help you easily create VMs.

Expedite creation with boot sources::
You can expedite VM creation by using templates that have an available boot source. Templates with a boot source are labeled *Available boot source* if they do not have a custom label.
+
Templates without a boot source are labeled *Boot source required*. See "Managing automatic boot source updates" for details.

Customize before starting the VM::
You can customize the disk source and VM parameters before you start the VM.

+
[NOTE]
====
If you copy a VM template with all its labels and annotations, your version of the template is marked as deprecated when a new version of the Scheduling, Scale, and Performance (SSP) Operator is deployed. You can remove this designation. See "Removing a deprecated designation from a customized VM template by using the web console".
====

{sno-caps}::
Due to differences in storage behavior, some templates are incompatible with {sno}. To ensure compatibility, do not set the `evictionStrategy` field for templates or VMs that use data volumes or storage profiles.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-creating-vms-from-templates.adoc

[id="virt-creating-vm-from-template_{context}"]
= Creating a VM from a template

[role="_abstract"]
You can create a virtual machine (VM) from a template with an available boot source by using the OpenShift Container Platform web console. You can customize template or VM parameters, such as data sources, Cloud-init, or SSH keys, before you start the VM.

You can choose between two views in the web console to create the VM:

* A virtualization-focused view, which provides a concise list of virtualization-related options at the top of the view
* A general view, which provides access to the various web console options, including *Virtualization*

.Procedure

. From the OpenShift Container Platform web console, choose your view:
** For a virtualization-focused view, select *Administrator* -> *Virtualization* -> *Catalog*.
+
** For a general view, navigate to *Virtualization* -> *Catalog*.
. Click the *Template catalog* tab.
. Click the *Boot source available* checkbox to filter templates with boot sources. The catalog displays the default templates.

. Heterogeneous clusters only: To filter the search results to show templates associated with a particular architecture, click *Architecture Type* .

. Click *All templates* to view the available templates for your filters.
** To focus on particular templates, enter the keyword in the `Filter by keyword` field.
** Choose a template project from the *All projects* dropdown menu, or view all projects.
. Click a template tile to view its details.
** Optional: If you are using a Windows template, you can mount a Windows driver disk by selecting the *Mount Windows drivers disk* checkbox.
** If you do not need to customize the template or VM parameters, click *Quick create VirtualMachine* to create a VM from the template.
+
** If you need to customize the template or VM parameters, do the following:

.. Click *Customize VirtualMachine*. The *Customize and create VirtualMachine* page displays the *Overview*, *YAML*, *Scheduling*, *Environment*, *Network interfaces*, *Disks*, *Scripts*, and *Metadata* tabs.
.. Click the *Scripts* tab to edit the parameters that must be set before the VM boots, such as `Cloud-init`, `SSH key`, or `Sysprep` (Windows VM only).
.. Optional: Click the *Start this virtualmachine after creation (Always)* checkbox.
.. Click *Create VirtualMachine*.
+
The *VirtualMachine details* page displays the provisioning status.

// Module included in the following assemblies:
//
// * virt/creating_vm/virt-creating-vms-from-templates.adoc

[id="virt-customizing-vm-template-web_{context}"]
= Removing a deprecated designation from a customized VM template by using the web console

[role="_abstract"]
You can customize an existing virtual machine (VM) template by modifying the VM or template parameters, such as data sources, cloud-init, or SSH keys, before you start the VM. If you customize a template by copying it and including all of its labels and annotations, the customized template is marked as deprecated when a new version of the Scheduling, Scale, and Performance (SSP) Operator is deployed.

You can remove the deprecated designation from the customized template.

.Procedure

. Navigate to *Virtualization* -> *Templates* in the web console.

. From the list of VM templates, click the template marked as deprecated.

. Click *Edit* next to the pencil icon beside *Labels*.

. Remove the following two labels:

* `template.kubevirt.io/type: "base"`
* `template.kubevirt.io/version: "version"`

. Click *Save*.

. Click the pencil icon beside the number of existing *Annotations*.

. Remove the following annotation:

* `template.kubevirt.io/deprecated`

. Click *Save*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vm/virt-creating-vms-from-templates.adoc

[id="virt-creating-template_{context}"]
= Creating a custom VM template in the web console

[role="_abstract"]
You can create a virtual machine template by editing a YAML file example in the OpenShift Container Platform web console.

.Procedure

. In the web console, click *Virtualization* -> *Templates* in the side menu.
. Optional: Use the *Project* drop-down menu to change the project associated with the new template. All templates are saved to the `openshift` project by default.
. Click *Create Template*.
. Specify the template parameters by editing the YAML file.
. Click *Create*.
+
The template is displayed on the *Templates* page.

. Optional: Click *Download* to download and save the YAML file.

// Module included in the following assemblies:
//
// * virt/creating_vm/virt-creating-vms-from-templates.adoc

[id="virt-dedicated-resources-vm-template_{context}"]
= Enabling dedicated resources for a virtual machine template

[role="_abstract"]
You can enable dedicated resources for a virtual machine (VM) template in the OpenShift Container Platform web console.
VMs that are created from this template will be scheduled with dedicated resources.

.Procedure

. In the OpenShift Container Platform web console, click *Virtualization* -> *Templates* in the side menu.
. Select the template that you want to edit to open the *Template details* page.
. On the *Scheduling* tab, click the edit icon beside *Dedicated Resources*.
. Select *Schedule this workload with dedicated resources (guaranteed policy)*.
. Click *Save*.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Managing automatic boot source updates
