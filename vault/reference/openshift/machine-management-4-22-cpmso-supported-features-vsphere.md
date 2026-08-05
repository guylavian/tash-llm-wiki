---
title: "Configuring {vmw-first} features for control plane machines"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-supported-features-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-supported-features-vsphere
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Configuring {vmw-first} features for control plane machines

[id="cpmso-supported-features-vsphere"]
= Configuring {vmw-first} features for control plane machines

[role="_abstract"]
You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".

//Adding tags to machines by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-vsphere.adoc

[id="machine-api-vmw-add-tags_{context}"]
= Adding tags to machines by using machine sets

[role="_abstract"]
To ensure that your cluster remains scalable and resilient, you can use a `MachineSet` object and machine health checks to automate the provisioning and repair of nodes. OpenShift Container Platform adds a cluster-specific tag to each virtual machine (VM) that it creates. The installation program uses these tags to select the VMs to delete when uninstalling a cluster.

In addition to the cluster-specific tags assigned to VMs, you can configure a machine set to add up to 10 additional {vmw-short} tags to the VMs it provisions.

.Prerequisites

* You have access to an OpenShift Container Platform cluster installed on {vmw-short} using an account with `cluster-admin` permissions.
* You have access to the VMware vCenter console associated with your cluster.
* You have created a tag in the vCenter console.
* You have installed the {oc-first}.

.Procedure

. Use the vCenter console to find the tag ID for any tag that you want to add to your machines:

.. Log in to the vCenter console.

.. From the *Home* menu, click *Tags & Custom Attributes*.

.. Select a tag that you want to add to your machines.

.. Use the browser URL for the tag that you select to identify the tag ID.
+
.Example tag URL
[source,text]
----
https://vcenter.example.com/ui/app/tags/tag/urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL/permissions
----
+
.Example tag ID
[source,text]
----
urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL
----

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following lines under the `providerSpec` field:
+
[source,yaml]
----
tag::compute[]
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
end::compute[]
tag::controlplane[]
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
end::controlplane[]
# ...
spec:
  template:
    spec:
      providerSpec:
        value:
          tagIDs:
          - <tag_id_value>
# ...
----
+
where
+
--
`spec.template.spec.providerSpec.value.tagIDs`:: Specifies a list of up to 10 tags to add to the machines that this machine set provisions. Replace `<tag_id_value>` with the tag that you want to add to your machines. For example, `urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL`.
--

//Configuring multiple NICs by using machine sets
//pulled from 4.18 GA
//include::modules/machineset-vsphere-multiple-nics.adoc[leveloffset=+1,tag=!compute]

//Configuring data disks by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-vsphere.adoc

[id="machineset-vsphere-data-disks_{context}"]
= Configuring data disks by using machine sets

[role="_abstract"]
To provide persistent storage beyond the root volume for specialized application workloads, define a `dataDisks` array in the `MachineSet` YAML file to specify disk size and storage policy. OpenShift Container Platform clusters on {vmw-first} support adding up to 29 disks to the virtual machine (VM) controller.

By configuring data disks, you can attach disks to VMs and use them to store data for etcd, container images, and other uses.
Separating data can help avoid filling the primary disk so that important activities such as upgrades have the resources that they require.

[NOTE]
====
Adding data disks attaches them to the VM and mounts them to the location that {op-system} designates.
// To mount the data disks to a specific location, you must configure each machine to use the data disks according to your needs.
====

.Prerequisites

* You have administrator access to {oc-first} for an OpenShift Container Platform cluster on {vmw-short}.

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following lines under the `providerSpec` field:
+
--
[source,yaml]
----
tag::compute[]
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
end::compute[]
tag::controlplane[]
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
end::controlplane[]
# ...
spec:
  template:
tag::compute[]
    spec:
      providerSpec:
        value:
          dataDisks:
          - name: "<disk_name>"
            provisioningMode: "<mode>"
            sizeGiB: 20
          - name: "<disk_name>"
            provisioningMode: "<mode>"
            sizeGiB: 20
end::compute[]
tag::controlplane[]
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            dataDisks:
            - name: "<disk_name>"
              provisioningMode: "<mode>"
              sizeGiB: 20
            - name: "<disk_name>"
              provisioningMode: "<mode>"
              sizeGiB: 20
end::controlplane[]
# ...
----
--
+
where
+
--
tag::compute[]

`spec.template.spec.providerSpec.value.dataDisks`:: Specifies a collection of 1-29 data disk definitions. This sample configuration shows the formatting to include two data disk definitions.
`spec.template.spec.providerSpec.value.dataDisks.name`:: Specifies the name of the data disk. The name must meet the following requirements:
* Start and end with an alphanumeric character
* Consist only of alphanumeric characters, hyphens (`-`), and underscores (`_`)
* Have a maximum length of 80 characters
`spec.template.spec.providerSpec.value.dataDisks.provisioningMode`:: Specifies the data disk provisioning method. This value defaults to the vSphere default storage policy if not set. Valid values are `Thin`, `Thick`, and `EagerlyZeroed`.
`spec.template.spec.providerSpec.value.dataDisks.sizeGiB`:: Specifies the size of the data disk in GiB. The maximum size is 16,384 GiB.
end::compute[]

tag::controlplane[]

`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks`:: Specifies a collection of 1-29 data disk definitions. This sample configuration shows the formatting to include two data disk definitions.
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.name`:: Specifies the name of the data disk. The name must meet the following requirements:
* Start and end with an alphanumeric character
* Consist only of alphanumeric characters, hyphens (`-`), and underscores (`_`)
* Have a maximum length of 80 characters
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.provisioningMode`:: Specifies the data disk provisioning method. This value defaults to the vSphere default storage policy if not set. Valid values are `Thin`, `Thick`, and `EagerlyZeroed`.
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.sizeGiB`:: Specifies the size of the data disk in GiB. The maximum size is 16,384 GiB.
end::controlplane[]
--

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Updating the control plane configuration
* Control plane configuration options for {vmw-full}
