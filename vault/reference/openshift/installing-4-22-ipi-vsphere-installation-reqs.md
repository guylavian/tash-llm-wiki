---
title: "vSphere installation requirements"
type: reference
domain: openshift
slug: installing-4-22-ipi-vsphere-installation-reqs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/ipi-vsphere-installation-reqs
version: 4.22
family: installing
documentKind: "Documentation"
---

# vSphere installation requirements

[id="ipi-vsphere-installation-reqs"]
= vSphere installation requirements

Before you begin an installation using installer-provisioned infrastructure, be sure that your vSphere environment meets the following installation requirements.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/ipi/ipi-vsphere-installation-reqs.adoc
// * installing/installing_vsphere/upi/upi-vpshere-installation-reqs.adoc

[id="installation-vsphere-infrastructure_{context}"]
= VMware vSphere infrastructure requirements

You must install an OpenShift Container Platform cluster on one of the following versions of a {vmw-full} instance that meets the requirements for the components that you use:

* Version 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later
* {vmw-full} Foundation 9 or later, or VMware Cloud Foundation 9 or later

Both of these releases support Container Storage Interface (CSI) migration, which is enabled by default on OpenShift Container Platform .

You can host the VMware vSphere infrastructure on-premise or on a VMware Cloud Verified provider that meets the requirements outlined in the following tables:

.Version requirements for vSphere virtual environments
[cols=2, options="header"]
|===
|Virtual environment product |Required version
|VMware virtual hardware | 15 or later
|vSphere ESXi hosts | 8.0 Update 1 or later, or {vmw-full} Foundation 9 or later; VMware Cloud Foundation 5.0 or later, or VMware Cloud Foundation 9 or later
|vCenter host | 8.0 Update 1 or later, or {vmw-full} Foundation 9 or later; VMware Cloud Foundation 5.0 or later, or VMware Cloud Foundation 9 or later
|===

[IMPORTANT]
====
You must ensure that the time on your ESXi hosts is synchronized before you install OpenShift Container Platform. See Edit Time Configuration for a Host in the VMware documentation.
====

.Minimum supported vSphere version for VMware components
|===
|Component | Minimum supported versions |Description

|Hypervisor
|vSphere 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later with virtual hardware version 15; {vmw-full} Foundation 9 or later, or VMware Cloud Foundation 9 or later
|This hypervisor version is the minimum version that {op-system-first} supports. For more information about supported hardware on the latest version of {op-system-base-full} that is compatible with {op-system}, see Hardware on the Red Hat Customer Portal.

|Networking (NSX)
|vSphere 8.0 Update 1 or later, or VMware Cloud Foundation 5.0 or later; VMware vSphere Foundation 9 or later, or VMware Cloud Foundation 9 or later
|Red Hat uses the Partner Certification process to verify NSX compatibility.

|CPU micro-architecture
|x86-64-v2 or higher
|OpenShift Container Platform version 4.13 and later are based on the {op-system-base} 9.2 host operating system, which raised the microarchitecture requirements to x86-64-v2. See Architectures in the {op-system-base} documentation.
|===

[IMPORTANT]
====
To ensure the best performance conditions for your cluster workloads that operate on {oci-first} and on the {ocvs-first} service, ensure volume performance units (VPUs) for your block volume are sized for your workloads.

The following list provides some guidance in selecting the VPUs needed for specific performance needs:

* Test or proof of concept environment: 100 GB, and 20 to 30 VPUs.
* Base-production environment: 500 GB, and 60 VPUs.
* Heavy-use production environment: More than 500 GB, and 100 or more VPUs.

Consider allocating additional VPUs to give enough capacity for updates and scaling activities. See Block Volume Performance Levels (Oracle documentation).
====

[NOTE]
====
The following additional {vmw-full} Foundation and VMware Cloud Foundation components are outside the scope of Red Hat support:

* Management: VCF Operations, VCF Automation, VCF Fleet Management, and VCF Identity Broker.
* Networking: VMware NSX Container Plugin (NCP).
* Migration: VMware HCX.
====

// Module included in the following assemblies:
//
// * installing/installing_vsphere/ipi/ipi-vsphere-installation-reqs.adoc

[id="installation-vsphere-installer-network-requirements_{context}"]
= Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate.

Review the following details about the required network ports.

.Ports used for all-machine to all-machine communications
[cols="2a,2a,5a",options="header"]
|===

|Protocol
|Port
|Description

|VRRP
|N/A
|Required for keepalived

|ICMP
|N/A
|Network reachability tests

.3+|TCP
|`1936`
|Metrics

|`9000`-`9999`
|Host level services, including the node exporter on ports `9100`-`9101` and
the Cluster Version Operator on port `9099`.

|`10250`-`10259`
|The default ports that Kubernetes reserves

.5+|UDP

|`6081`
|Geneve

|`9000`-`9999`
|Host level services, including the node exporter on ports `9100`-`9101`.

|`500`
|IPsec IKE packets

|`4500`
|IPsec NAT-T packets

|TCP/UDP
|`30000`-`32767`
|Kubernetes node port

|ESP
|N/A
|IPsec Encapsulating Security Payload (ESP)

|===

.Ports used for all-machine to control plane communications
[cols="2a,2a,5a",options="header"]
|===

|Protocol
|Port
|Description

|TCP
|`6443`
|Kubernetes API

|===

.Ports used for control plane machine to control plane machine communications
[cols="2a,2a,5a",options="header"]
|===

|Protocol
|Port
|Description

|TCP
|`2379`-`2380`
|etcd server and peer ports

|===

// Module included in the following assemblies for vSphere:
//
// * installing/installing_vsphere/ipi/ipi-vsphere-installation-reqs.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc

[id="vsphere-csi-driver-reqs_{context}"]
= VMware vSphere CSI Driver Operator requirements

To install the vSphere Container Storage Interface (CSI) Driver Operator, the following requirements must be met:

* VMware vSphere version 8.0 Update 1 or later; or VMware vSphere Foundation (VVF) 9; or VMware Cloud Foundation (VCF) 5 or later
* vCenter version 8.0 Update 1 or later; or VVF 9; or VCF 5 or later
* Virtual machines of hardware version 15 or later
* No third-party vSphere CSI driver already installed in the cluster

If a third-party vSphere CSI driver is present in the cluster, OpenShift Container Platform does not overwrite it. The presence of a third-party vSphere CSI driver prevents OpenShift Container Platform from updating to OpenShift Container Platform 4.13 or later.

[NOTE]
====
The VMware vSphere CSI Driver Operator is supported only on clusters deployed with `platform: vsphere` in the installation manifest.
====

You can create a custom role for the Container Storage Interface (CSI) driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator. The custom role can include privilege sets that assign a minimum set of permissions to each vSphere object. This means that the CSI driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator can establish a basic interaction with these objects.

[IMPORTANT]
====
Installing an OpenShift Container Platform cluster in a vCenter is tested against a full list of privileges as described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected and unsupported behaviors that might occur when creating a custom role with a set of restricted privileges.
====

[role="_additional-resources"]
.Additional resources

* To remove a third-party vSphere CSI driver, see Removing a third-party vSphere CSI Driver.
* To update the hardware version for your vSphere nodes, see Updating hardware on nodes running in vSphere.
* Minimum permissions for the storage components

// Module included in the following assemblies for vSphere:
//
// * installing/installing_vsphere/ipi/ipi-vsphere-installation-reqs.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

// Note: The ifndef statements add content to IPI documents

[id="installation-vsphere-installer-infra-requirements_{context}"]
= vCenter requirements

Before you install an OpenShift Container Platform cluster on your vCenter that uses infrastructure that the installation program provisions, you must prepare your environment.

Before you install an OpenShift Container Platform cluster on your vCenter that uses infrastructure that you provided, you must prepare your environment.

[id="installation-vsphere-installer-infra-requirements-account_{context}"]
== Required vCenter account privileges

To install an OpenShift Container Platform cluster in a vCenter, the installation program requires access to an account with privileges to read and create the required resources. Using an account that has global administrative privileges is the simplest way to access all of the necessary permissions.

If you cannot use an account with global administrative privileges, you must create roles to grant the privileges necessary for OpenShift Container Platform cluster installation. Most of the privileges are always required. Some privileges are required only if you plan for the installation program to provision a folder to contain the OpenShift Container Platform cluster on your vCenter instance, which is the default behavior. You must create or change vSphere roles for the specified objects to grant the required privileges.

The installation program requires an additional role to create a vSphere virtual machine folder.

To install an OpenShift Container Platform cluster in a vCenter, your vSphere account must include privileges for reading and creating the required resources. Using an account that has global administrative privileges is the simplest way to access all of the necessary permissions.

[NOTE]
====
The following tables do not explicitly list the ESXi host object. In the {vmw-short} hierarchy, ESXi hosts are child objects of the cluster. If you apply your custom role to the vSphere vCenter Cluster object with the "Propagate to children" setting enabled, the required privileges automatically propagate down to the ESXi hosts. You do not need to apply permissions directly to individual ESXi host objects.
====

.Roles and privileges required for installation in vSphere API
[%collapsible]
====
[cols="3a,3a,3a",options="header"]
|===
|vSphere object for role
|When required
|Required privileges in vSphere API

|vSphere vCenter
|Always
|
[%hardbreaks]
`Cns.Searchable`
`InventoryService.Tagging.AttachTag`
`InventoryService.Tagging.CreateCategory`
`InventoryService.Tagging.CreateTag`
`InventoryService.Tagging.DeleteCategory`
`InventoryService.Tagging.DeleteTag`
`InventoryService.Tagging.EditCategory`
`InventoryService.Tagging.EditTag`
`Sessions.ValidateSession`
`StorageProfile.Update`
`StorageProfile.View`

|vSphere vCenter Cluster
|Always
|
[%hardbreaks]
`Host.Config.Storage`
`Resource.AssignVMToPool`
`VApp.AssignResourcePool`
`VApp.Import`
`VirtualMachine.Config.AddNewDisk`

|vSphere vCenter Resource Pool
|For a provided existing resource pool
|
[%hardbreaks]
`Resource.AssignVMToPool`
`VApp.AssignResourcePool`
`VApp.Import`
`VirtualMachine.Config.AddNewDisk`

|vSphere Datastore
|Always
|
[%hardbreaks]
`Datastore.AllocateSpace`
`Datastore.Browse`
`Datastore.FileManagement`
`InventoryService.Tagging.ObjectAttachable`

|vSphere Port Group
|Always
|`Network.Assign`

|Virtual Machine Folder
|Always
|
[%hardbreaks]
`InventoryService.Tagging.ObjectAttachable`
`Resource.AssignVMToPool`
`VApp.Import`
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddNewDisk`
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Config.AdvancedConfig`
`VirtualMachine.Config.Annotation`
`VirtualMachine.Config.CPUCount`
`VirtualMachine.Config.DiskExtend`
`VirtualMachine.Config.DiskLease`
`VirtualMachine.Config.EditDevice`
`VirtualMachine.Config.Memory`
`VirtualMachine.Config.RemoveDisk`
`VirtualMachine.Config.Rename`
`Host.Config.Storage`
`VirtualMachine.Config.ResetGuestInfo`
`VirtualMachine.Config.Resource`
`VirtualMachine.Config.Settings`
`VirtualMachine.Config.UpgradeVirtualHardware`
`VirtualMachine.Interact.GuestControl`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Interact.Reset`
`VirtualMachine.Inventory.Create`
`VirtualMachine.Inventory.CreateFromExisting`
`VirtualMachine.Inventory.Delete`
`VirtualMachine.Provisioning.Clone`
`VirtualMachine.Provisioning.MarkAsTemplate`
`VirtualMachine.Provisioning.DeployTemplate`

|vSphere vCenter data center
|The installation program creates the virtual machine folder.
|`VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API. See the "Minimum permissions for the Machine API" table.
|
[%hardbreaks]
`InventoryService.Tagging.ObjectAttachable`
`Resource.AssignVMToPool`
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddNewDisk`
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Config.AdvancedConfig`
`VirtualMachine.Config.Annotation`
`VirtualMachine.Config.CPUCount`
`VirtualMachine.Config.DiskExtend`
`VirtualMachine.Config.DiskLease`
`VirtualMachine.Config.EditDevice`
`VirtualMachine.Config.Memory`
`VirtualMachine.Config.RemoveDisk`
`VirtualMachine.Config.Rename`
`VirtualMachine.Config.ResetGuestInfo`
`VirtualMachine.Config.Resource`
`VirtualMachine.Config.Settings`
`VirtualMachine.Config.UpgradeVirtualHardware`
`VirtualMachine.Interact.GuestControl`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Interact.Reset`
`VirtualMachine.Inventory.Create`
`VirtualMachine.Inventory.CreateFromExisting`
`VirtualMachine.Inventory.Delete`
`VirtualMachine.Provisioning.Clone`
`VirtualMachine.Provisioning.DeployTemplate`
`VirtualMachine.Provisioning.MarkAsTemplate`
`Folder.Create`
`Folder.Delete`
|===
====

.Roles and privileges required for installation in vCenter graphical user interface (GUI)
[%collapsible]
====
[cols="2a,3a,3a",options="header"]
|===
|vSphere object for role
|When required
|Required privileges in vCenter GUI

|vSphere vCenter
|Always
|
[%hardbreaks]
`Cns.Searchable`
`"vSphere Tagging"."Assign or Unassign vSphere Tag"`
`"vSphere Tagging"."Create vSphere Tag Category"`
`"vSphere Tagging"."Create vSphere Tag"`
`vSphere Tagging"."Delete vSphere Tag Category"`
`"vSphere Tagging"."Delete vSphere Tag"`
`"vSphere Tagging"."Edit vSphere Tag Category"`
`"vSphere Tagging"."Edit vSphere Tag"`
`Sessions."Validate session"`
`"VM storage policies"."Update VM storage policies"`
`"VM storage policies"."View VM storage policies"`

|vSphere vCenter Cluster
|Always
|
[%hardbreaks]
`Host.Configuration."Storage partition configuration"`
`Resource."Assign virtual machine to resource pool"`
`VApp."Assign resource pool"`
`VApp.Import`
`"Virtual machine"."Change Configuration"."Add new disk"`

|vSphere vCenter Resource Pool
|If providing an existing resource pool
|
[%hardbreaks]
`Host.Configuration."Storage partition configuration"`
`Resource."Assign virtual machine to resource pool"`
`VApp."Assign resource pool"`
`VApp.Import`
`"Virtual machine"."Change Configuration"."Add new disk"`

|vSphere Datastore
|Always
|
[%hardbreaks]
`Datastore."Allocate space"`
`Datastore."Browse datastore"`
`Datastore."Low level file operations"`
`"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"`

|vSphere Port Group
|Always
|`Network."Assign network"`

|Virtual Machine Folder
|Always
|
[%hardbreaks]
`"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"`
`Resource."Assign virtual machine to resource pool"`
`VApp.Import`
`"Virtual machine"."Change Configuration"."Add existing disk"`
`"Virtual machine"."Change Configuration"."Add new disk"`
`"Virtual machine"."Change Configuration"."Add or remove device"`
`"Virtual machine"."Change Configuration"."Advanced configuration"`
`"Virtual machine"."Change Configuration"."Set annotation"`
`"Virtual machine"."Change Configuration"."Change CPU count"`
`"Virtual machine"."Change Configuration"."Extend virtual disk"`
`"Virtual machine"."Change Configuration"."Acquire disk lease"`
`"Virtual machine"."Change Configuration"."Modify device settings"`
`"Virtual machine"."Change Configuration"."Change Memory"`
`"Virtual machine"."Change Configuration"."Remove disk"`
`"Virtual machine"."Change Configuration".Rename`
`"Virtual machine"."Change Configuration"."Reset guest information"`
`"Virtual machine"."Change Configuration"."Change resource"`
`"Virtual machine"."Change Configuration"."Change Settings"`
`"Virtual machine"."Change Configuration"."Upgrade virtual machine compatibility"`
`"Virtual machine".Interaction."Guest operating system management by VIX API"`
`"Virtual machine".Interaction."Power off"`
`"Virtual machine".Interaction."Power on"`
`"Virtual machine".Interaction.Reset`
`"Virtual machine"."Edit Inventory"."Create new"`
`"Virtual machine"."Edit Inventory"."Create from existing"`
`"Virtual machine"."Edit Inventory"."Remove"`
`"Virtual machine".Provisioning."Clone virtual machine"`
`"Virtual machine".Provisioning."Mark as template"`
`"Virtual machine".Provisioning."Deploy template"`

|vSphere vCenter data center
|The installation program creates the virtual machine folder.
|`VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API.
|
[%hardbreaks]
`"vSphere Tagging"."Assign or Unassign vSphere Tag on Object"`
`Resource."Assign virtual machine to resource pool"`
`VApp.Import`
`"Virtual machine"."Change Configuration"."Add existing disk"`
`"Virtual machine"."Change Configuration"."Add new disk"`
`"Virtual machine"."Change Configuration"."Add or remove device"`
`"Virtual machine"."Change Configuration"."Advanced configuration"`
`"Virtual machine"."Change Configuration"."Set annotation"`
`"Virtual machine"."Change Configuration"."Change CPU count"`
`"Virtual machine"."Change Configuration"."Extend virtual disk"`
`"Virtual machine"."Change Configuration"."Acquire disk lease"`
`"Virtual machine"."Change Configuration"."Modify device settings"`
`"Virtual machine"."Change Configuration"."Change Memory"`
`"Virtual machine"."Change Configuration"."Remove disk"`
`"Virtual machine"."Change Configuration".Rename`
`"Virtual machine"."Change Configuration"."Reset guest information"`
`"Virtual machine"."Change Configuration"."Change resource"`
`"Virtual machine"."Change Configuration"."Change Settings"`
`"Virtual machine"."Change Configuration"."Upgrade virtual machine compatibility"`
`"Virtual machine".Interaction."Guest operating system management by VIX API"`
`"Virtual machine".Interaction."Power off"`
`"Virtual machine".Interaction."Power on"`
`"Virtual machine".Interaction.Reset`
`"Virtual machine"."Edit Inventory"."Create new"`
`"Virtual machine"."Edit Inventory"."Create from existing"`
`"Virtual machine"."Edit Inventory"."Remove"`
`"Virtual machine".Provisioning."Clone virtual machine"`
`"Virtual machine".Provisioning."Deploy template"`
`"Virtual machine".Provisioning."Mark as template"`
`Folder."Create folder"`
`Folder."Delete folder"`
|===
====

Additionally, the user requires some `ReadOnly` permissions, and some of the roles require permission to propagate the permissions to child objects. These settings vary depending on whether or not you install the cluster into an existing folder.

.Required permissions and propagation settings
[%collapsible]
====
[cols="3a,3a,3a,3a",options="header"]
|===
|vSphere object
|When required
|Propagate to children
|Permissions required

|vSphere vCenter
|Always
|False
|Listed required privileges

|vSphere vCenter data center
|Existing folder
|False
|`ReadOnly` permission

.2+|vSphere vCenter data center
|Existing folder
|False
|`ReadOnly` permission

|Installation program creates the folder
|True
|Listed required privileges

|vSphere vCenter Cluster
|Always
|True
|Listed required privileges

|vSphere vCenter Datastore
|Always
|False
|Listed required privileges

|vSphere Switch
|Always
|False
|`ReadOnly` permission

|vSphere Port Group
|Always
|False
|Listed required privileges

|vSphere vCenter Virtual Machine Folder
|Existing folder
|True
|Listed required privileges

|vSphere vCenter Resource Pool
|Existing resource pool
|True
|Listed required privileges
|===
====

For more information about creating an account with only the required privileges, see vSphere Permissions and User Management Tasks in the vSphere documentation.

[id="installation-vsphere-installer-infra-minimum-requirements_{context}"]
== Minimum required vCenter account privileges

After you create a custom role and assign privileges to the role, you can create permissions by selecting specific vSphere objects. You can then assign the custom role to a user or group for each object.

Before you create permissions or request for the creation of permissions for a vSphere object, decide what minimum permissions apply to the vSphere object. By doing this task, you can ensure a basic interaction exists between a vSphere object and OpenShift Container Platform architecture.

[IMPORTANT]
====
If you create a custom role and you do not assign privileges to it, the vSphere Server by default assigns a `Read Only` role to the custom role. Note that for the cloud provider API, the custom role only needs to inherit the privileges of the `Read Only` role.
====

Consider creating a custom role when an account with global administrative privileges does not meet your needs.

[IMPORTANT]
====
Red{nbsp}Hat does not support configuring an account without including the required privileges. Red{nbsp}Hat tests OpenShift Container Platform cluster installations in vCenter against the full list of privileges described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected behaviors that might occur when creating a custom role with a restricted set of privileges. You must retain the full set of privileges from the "Required vCenter account privileges" section after cluster installation. Reducing the account to only the permissions listed in the minimum permission tables in the "Minimum required vCenter account privileges" section after installation is not supported and can cause unexpected cluster behavior. The minimum permission tables are for reference only; they show which privileges apply to which OpenShift Container Platform components (such as storage or the Machine API) when you design or audit custom roles. The supported configuration is to assign the full set of privileges from the "Required vCenter account privileges" section at all times, both during and after installation.
====

The following tables specify how the required vCenter account privileges provided earlier in this document are relevant to different aspects of OpenShift Container Platform architecture.

[id="installation-vsphere-minimum-permissions-ipi_{context}"]
.Minimum permissions on installer-provisioned infrastructure
[%collapsible]
====
[cols="4a,4a,3a",options="header"]
|===
|vSphere object for role
|When required
|Required privileges

|vSphere vCenter
|Always
|
[%hardbreaks]
`Cns.Searchable`
`InventoryService.Tagging.AttachTag`
`InventoryService.Tagging.CreateCategory`
`InventoryService.Tagging.CreateTag`
`InventoryService.Tagging.DeleteCategory`
`InventoryService.Tagging.DeleteTag`
`InventoryService.Tagging.EditCategory`
`InventoryService.Tagging.EditTag`
`Sessions.ValidateSession`
`StorageProfile.Update`
`StorageProfile.View`

|vSphere vCenter Cluster
|If you intend to create VMs in the cluster root
|
[%hardbreaks]
`Host.Config.Storage`
`Resource.AssignVMToPool`
`VApp.AssignResourcePool`
`VApp.Import`
`VirtualMachine.Config.AddNewDisk`

|vSphere vCenter Resource Pool
|If you included an existing resource pool in the `install-config.yaml` file
|
[%hardbreaks]

`Host.Config.Storage`
`Resource.AssignVMToPool`
`VApp.AssignResourcePool`
`VApp.Import`minimum`

|vSphere Datastore
|If you referenced a datastore in the `install-config.yaml` file
|
[%hardbreaks]

`Datastore.Browse`
`Datastore.FileManagement`
`InventoryService.Tagging.ObjectAttachable`

|vSphere Port Group
|Always
|
[%hardbreaks]
`Network.Assign`

|Virtual Machine Folder
|Always
|
[%hardbreaks]
`InventoryService.Tagging.ObjectAttachable`
`Resource.AssignVMToPool`
`VApp.Import`
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddNewDisk`
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Config.AdvancedConfig`
`VirtualMachine.Config.Annotation`
`VirtualMachine.Config.CPUCount`
`VirtualMachine.Config.DiskExtend`
`VirtualMachine.Config.DiskLease`
`VirtualMachine.Config.EditDevice`
`VirtualMachine.Config.Memory`
`VirtualMachine.Config.RemoveDisk`
`VirtualMachine.Config.Rename`
`VirtualMachine.Config.ResetGuestInfo`
`VirtualMachine.Config.Resource`
`VirtualMachine.Config.Settings`
`VirtualMachine.Config.UpgradeVirtualHardware`
`VirtualMachine.Interact.GuestControl`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Interact.Reset`
`VirtualMachine.Inventory.Create`
`VirtualMachine.Inventory.CreateFromExisting`
`VirtualMachine.Inventory.Delete`
`VirtualMachine.Provisioning.Clone`
`VirtualMachine.Provisioning.MarkAsTemplate`
`VirtualMachine.Provisioning.DeployTemplate`

|vSphere vCenter data center
|If the virtual machine folder does not already exist, the installation program creates the virtual machine folder. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.
|
[%hardbreaks]
`Folder.Create`
`Folder.Delete`
`InventoryService.Tagging.ObjectAttachable`
`Resource.AssignVMToPool`
`VApp.Import`
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddNewDisk`
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Config.AdvancedConfig`
`VirtualMachine.Config.Annotation`
`VirtualMachine.Config.CPUCount`
`VirtualMachine.Config.DiskExtend`
`VirtualMachine.Config.DiskLease`
`VirtualMachine.Config.EditDevice`
`VirtualMachine.Config.Memory`
`VirtualMachine.Config.RemoveDisk`
`VirtualMachine.Config.Rename`
`VirtualMachine.Config.ResetGuestInfo`
`VirtualMachine.Config.Resource`
`VirtualMachine.Config.Settings`
`VirtualMachine.Config.UpgradeVirtualHardware`
`VirtualMachine.Interact.GuestControl`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Interact.Reset`
`VirtualMachine.Inventory.Create`
`VirtualMachine.Inventory.CreateFromExisting`
`VirtualMachine.Inventory.Delete`
`VirtualMachine.Provisioning.Clone`
`VirtualMachine.Provisioning.DeployTemplate`
`VirtualMachine.Provisioning.MarkAsTemplate`
|===
====

[id="post-installation-vsphere-minimum-permissions_{context}"]
.Minimum permissions for postinstallation management of components
[%collapsible]
====
[cols="4a,4a,3a",options="header"]
|===
|vSphere object for role
|When required
|Required privileges

|vSphere vCenter
|Always
|
[%hardbreaks]
`Cns.Searchable`
`InventoryService.Tagging.AttachTag`
`InventoryService.Tagging.CreateCategory`
`InventoryService.Tagging.CreateTag`
`InventoryService.Tagging.DeleteCategory`
`InventoryService.Tagging.DeleteTag`
`InventoryService.Tagging.EditCategory`
`InventoryService.Tagging.EditTag`
`Sessions.ValidateSession`
`StorageProfile.Update`
`StorageProfile.View`

|vSphere vCenter Cluster
|If you intend to create VMs in the cluster root
|
[%hardbreaks]
`Host.Config.Storage`
`Resource.AssignVMToPool`

|vSphere vCenter Resource Pool
|If you included an existing resource pool in the `install-config.yaml` file
|
[%hardbreaks]
`Host.Config.Storage`

|vSphere Datastore
|Always
|
[%hardbreaks]
`Datastore.AllocateSpace`
`Datastore.Browse`
`Datastore.FileManagement`
`InventoryService.Tagging.ObjectAttachable`

|vSphere Port Group
|Always
|
[%hardbreaks]
`Network.Assign`

|Virtual Machine Folder
|Always
|
[%hardbreaks]
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Config.AdvancedConfig`
`VirtualMachine.Config.Annotation`
`VirtualMachine.Config.CPUCount`
`VirtualMachine.Config.DiskExtend`
`VirtualMachine.Config.Memory`
`VirtualMachine.Config.Settings`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Inventory.CreateFromExisting`
`VirtualMachine.Inventory.Delete`
`VirtualMachine.Provisioning.Clone`
`VirtualMachine.Provisioning.DeployTemplate`

|vSphere vCenter data center
|If the virtual machine folder does not already exist, the installation program creates the virtual machine folder.
|`VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.
|
[%hardbreaks]
`Resource.AssignVMToPool`
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Provisioning.DeployTemplate`
|===
====

[id="installation-vsphere-minimum-permissions-storage_{context}"]
.Minimum permissions for the storage components
[%collapsible]
====
[cols="4a,4a,3a",options="header"]
|===
|vSphere object for role
|When required
|Required privileges

|vSphere vCenter
|Always
|
[%hardbreaks]
`Cns.Searchable`
`InventoryService.Tagging.CreateCategory`
`InventoryService.Tagging.CreateTag`
`InventoryService.Tagging.EditCategory`
`InventoryService.Tagging.EditTag`
`StorageProfile.Update`
`StorageProfile.View`

|vSphere vCenter Cluster
|If you intend to create VMs in the cluster root
|
[%hardbreaks]
`Host.Config.Storage`

|vSphere vCenter Resource Pool
|If you included an existing resource pool in the `install-config.yaml` file
|
[%hardbreaks]
`Host.Config.Storage`

|vSphere Datastore
|Always
|
[%hardbreaks]
`Datastore.Browse`
`Datastore.FileManagement`
`InventoryService.Tagging.ObjectAttachable`

|vSphere Port Group
|Always
|
[%hardbreaks]
`Read Only`

|Virtual Machine Folder
|Always
|
[%hardbreaks]
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddRemoveDevice`

|vSphere vCenter data center
|If the virtual machine folder does not already exist, the installation program creates the virtual machine folder.
|`VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API. If your cluster does use the Machine API and you want to set the minimum set of permissions for the API, see the "Minimum permissions for the Machine API" table.
|
[%hardbreaks]
`VirtualMachine.Config.AddExistingDisk`
`VirtualMachine.Config.AddRemoveDevice`
|===
====

[id="post-installation-vsphere-minimum-machine-api_{context}"]
.Minimum permissions for the Machine API
[%collapsible]
====
[cols="4a,4a,3a",options="header"]
|===
|vSphere object for role
|When required
|Required privileges

|vSphere vCenter
|Always
|
[%hardbreaks]
`InventoryService.Tagging.AttachTag`
`InventoryService.Tagging.CreateCategory`
`InventoryService.Tagging.CreateTag`
`InventoryService.Tagging.DeleteCategory`
`InventoryService.Tagging.DeleteTag`
`InventoryService.Tagging.EditCategory`
`InventoryService.Tagging.EditTag`
`Sessions.ValidateSession`
`StorageProfile.Update`
`StorageProfile.View`

|vSphere vCenter Cluster
|If you intend to create VMs in the cluster root
|
[%hardbreaks]
`Resource.AssignVMToPool`

|vSphere vCenter Resource Pool
|If you included an existing resource pool in the `install-config.yaml` file
|
[%hardbreaks]
`Read Only`

|vSphere Datastore
|Always
|
[%hardbreaks]
`Datastore.AllocateSpace`
`Datastore.Browse`

|vSphere Port Group
|Always
|
[%hardbreaks]
`Network.Assign`

|Virtual Machine Folder
|Always
|
[%hardbreaks]
`VirtualMachine.Config.AddRemoveDevice`
`VirtualMachine.Config.AdvancedConfig`
`VirtualMachine.Config.Annotation`
`VirtualMachine.Config.CPUCount`
`VirtualMachine.Config.DiskExtend`
`VirtualMachine.Config.Memory`
`VirtualMachine.Config.Settings`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Inventory.CreateFromExisting`
`VirtualMachine.Inventory.Delete`
`VirtualMachine.Provisioning.Clone`
`VirtualMachine.Provisioning.DeployTemplate`

|vSphere vCenter data center
|If the virtual machine folder does not already exist, the installation program creates the virtual machine folder.
|`VirtualMachine.Inventory.Create` and `VirtualMachine.Inventory.Delete` privileges are optional if your cluster does not use the Machine API.
|
[%hardbreaks]
`Resource.AssignVMToPool`
`VirtualMachine.Interact.PowerOff`
`VirtualMachine.Interact.PowerOn`
`VirtualMachine.Provisioning.DeployTemplate`
|===
====

[id="installation-vsphere-installer-infra-requirements-vmotion_{context}"]
== Using OpenShift Container Platform with vMotion

If you intend on using vMotion in your vSphere environment, consider the following before installing an OpenShift Container Platform cluster.

* Using Storage vMotion can cause issues and is not supported.
* Using VMware compute vMotion to migrate the workloads for both OpenShift Container Platform compute machines and control plane machines is generally supported, where _generally_ implies that you meet all VMware best practices for vMotion.
+
--
To help ensure the uptime of your compute and control plane nodes, ensure that you follow the VMware best practices for vMotion, and use VMware anti-affinity rules to improve the availability of OpenShift Container Platform during maintenance or hardware issues.

For more information about vMotion and anti-affinity rules, see the VMware vSphere documentation for  vMotion networking requirements and VM anti-affinity rules.
--
* If you are using {vmw-full} volumes in your pods, migrating a VM across datastores, either manually or through Storage vMotion, causes invalid references within OpenShift Container Platform persistent volume (PV) objects that can result in data loss.
* OpenShift Container Platform does not support selective migration of virtual machine disks (VMDKs) across datastores, using datastore clusters for VM provisioning or for dynamic or static provisioning of PVs, or using a datastore that is part of a datastore cluster for dynamic or static provisioning of PVs.
+
[IMPORTANT]
====
You can specify the path of any datastore that exists in a datastore cluster. By default, Storage Distributed Resource Scheduler (SDRS), which uses Storage vMotion, is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable SDRS to avoid data loss issues for your OpenShift Container Platform cluster.
If you must specify VMs across many datastores, use a `datastore` object to specify a failure domain in your cluster's `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".
====

[id="installation-vsphere-installer-infra-requirements-resources_{context}"]
== Cluster resources

When you deploy an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, the installation program must be able to create several resources in your vCenter instance.

A standard OpenShift Container Platform installation creates the following vCenter resources:

When you deploy an OpenShift Container Platform cluster that uses infrastructure that you provided, you must create the following resources in your vCenter instance:

* 1 Folder
* 1 Tag category
* 1 Tag
* Virtual machines:
** 1 template
** 1 temporary bootstrap node
** 3 control plane nodes
** 3 compute machines

Although these resources use 856 GB of storage, the bootstrap node gets deleted during the cluster installation process. At a minimum, a standard cluster requires 800 GB of storage.

If you deploy more compute machines, the OpenShift Container Platform cluster will use more storage.

[id="installation-vsphere-installer-infra-requirements-limits_{context}"]
== Cluster limits

Available resources vary between clusters. A limit exists for the number of possible clusters within vCenter, primarily by available storage space and any limitations on the number of required resources. Be sure to consider both limitations to the vCenter resources that the cluster creates and the resources that you require to deploy a cluster, such as IP addresses and networks.

[id="installation-vsphere-installer-infra-requirements-networking_{context}"]
== Networking requirements

You can use Dynamic Host Configuration Protocol (DHCP) for the network and configure the DHCP server to set persistent IP addresses to machines in your cluster. In the DHCP lease, you must configure the DHCP to use the default gateway.

[NOTE]
====
You do not need to use the DHCP for the network if you want to provision nodes with static IP addresses.
====

If you specify nodes or groups of nodes on different VLANs for a cluster that you want to install on user-provisioned infrastructure, you must ensure that machines in your cluster meet the requirements outlined in the "Network connectivity requirements" section of the _Networking requirements for user-provisioned infrastructure_ document.

If you are installing to a restricted environment, the VM in your restricted network must have access to vCenter so that it can provision and manage nodes, persistent volume claims (PVCs), and other resources.

[NOTE]
====
Ensure that each OpenShift Container Platform node in the cluster has access to a Network Time Protocol (NTP) server that is discoverable by DHCP. Installation is possible without an NTP server. However, asynchronous server clocks can cause errors, which the NTP server prevents.
====

Additionally, you must create the following networking resources before you install the OpenShift Container Platform cluster:

[id="installation-vsphere-installer-infra-requirements-_{context}"]
=== Required IP addresses
For a network that uses DHCP, an installer-provisioned vSphere installation requires two static IP addresses:

* The **API** address for accessing the cluster API.
* The **Ingress** address for cluster ingress traffic.

You must give these IP addresses to the installation program when you install the OpenShift Container Platform cluster.

[id="installation-vsphere-installer-infra-requirements-dns-records_{context}"]
=== DNS records
You must create DNS records for two static IP addresses in the appropriate DNS server for the vCenter instance that hosts your OpenShift Container Platform cluster. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

.Required DNS records
[cols="1a,5a,3a",options="header"]
|===

|Component
|Record
|Description

|API VIP
|`api.<cluster_name>.<base_domain>.`
|This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the control plane machines. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.

|Ingress VIP
|`*.apps.<cluster_name>.<base_domain>.`
|A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the worker nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster.
|===

// Module included in the following assemblies:
//
// * installing/installing_vsphere/ipi/ipi-vsphere-installation-reqs.adoc

[id="installation-vsphere-installer-infra-static-ip-nodes_{context}"]
== Static IP addresses for vSphere nodes

You can provision bootstrap, control plane, and compute nodes to be configured with static IP addresses in environments where Dynamic Host Configuration Protocol (DHCP) does not exist. To configure this environment, you must provide values to the `platform.vsphere.hosts.role` parameter in the `install-config.yaml` file.

By default, the installation program is configured to use the DHCP for the network, but this network has limited configurable capabilities.

After you define one or more machine pools in your `install-config.yaml` file, you can define network definitions for nodes on your network. Ensure that the number of network definitions matches the number of machine pools that you configured for your cluster.

.Example network configuration that specifies different roles
[source,yaml]
----
# ...
platform:
  vsphere:
    hosts:
    - role: bootstrap # <1>
      networkDevice:
        ipAddrs:
        - 192.168.204.10/24 # <2>
        gateway: 192.168.204.1 # <3>
        nameservers: # <4>
        - 192.168.204.1
    - role: control-plane
      networkDevice:
        ipAddrs:
        - 192.168.204.11/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
    - role: control-plane
      networkDevice:
        ipAddrs:
        - 192.168.204.12/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
    - role: control-plane
      networkDevice:
        ipAddrs:
        - 192.168.204.13/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
    - role: compute
      networkDevice:
        ipAddrs:
        - 192.168.204.14/24
        gateway: 192.168.204.1
        nameservers:
        - 192.168.204.1
# ...
----
<1> Valid network definition values include `bootstrap`, `control-plane`, and `compute`. You must list at least one `bootstrap` network definition in your `install-config.yaml` configuration file.
<2> Lists IPv4, IPv6, or both IP addresses that the installation program passes to the network interface. The machine API controller assigns all configured IP addresses to the default network interface.
<3> The default gateway for the network interface.
<4> Lists up to 3 DNS nameservers.

After you deployed your cluster to run nodes with static IP addresses, you can scale a machine to use one of these static IP addresses. Additionally, you can use a machine set to configure a machine to use one of the configured static IP addresses.

[role="_additional-resources"]
.Additional resources

* Scaling machines to use static IP addresses
* Using a machine set to scale machines with configured static IP addresses
