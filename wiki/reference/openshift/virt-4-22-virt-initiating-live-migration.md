---
title: "Initiating and canceling live migration"
type: reference
domain: openshift
slug: virt-4-22-virt-initiating-live-migration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-initiating-live-migration
version: 4.22
family: virt
documentKind: "Documentation"
---

# Initiating and canceling live migration

[id="virt-initiating-live-migration"]
= Initiating and canceling live migration

[role="_abstract"]
To move a running virtual machine (VM) to a different node without interrupting the workload, you can initiate a live migration. You can also cancel an ongoing migration to keep the VM on its original node.

You can initiate the live migration of a virtual machine (VM) to another node by using the OpenShift Container Platform web console or the command line.

You can cancel a live migration by using the web console or the command line. The VM remains on its original node.

[TIP]
====
You can also initiate and cancel live migration by using the `virtctl migrate <vm_name>` and `virtctl migrate-cancel <vm_name>` commands.
====

// Module included in the following assemblies:
//
// * virt/live_migration/virt-initiating-live-migration.adoc

[id="virt-initiating-vm-migration-web_{context}"]
= Initiating live migration by using the web console

[role="_abstract"]
You can live migrate a running virtual machine (VM) to a different node in the cluster by using the OpenShift Container Platform web console.

[NOTE]
====
The *Migrate* action is visible to all users but only cluster administrators can initiate a live migration.
====

.Prerequisites

* You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.
* The VM is able to be migrated.
* If the VM is configured with a host model CPU, the cluster has an available node that supports the CPU model.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Take either of the following steps:
* Click the Options menu {kebab} beside the VM you want to migrate, hover over the *Migrate* option, and select *Compute*.
+
* Open the *VM details* page of the VM you want to migrate, click the *Actions* menu, hover over the *Migrate* option, and select *Compute*.
. In the *Migrate Virtual Machine to a different Node* dialog box, select either *Automatically Selected Node* or *Specific Node*.
.. If you selected the *Specific Node* option, choose a node from the list.
. Click *Migrate Virtual Machine*.

// Module included in the following assemblies:
//
// * virt/live_migration/virt-initiating-live-migration.adoc

[id="virt-initiating-vm-migration-cli_{context}"]
= Initiating live migration by using the CLI

[role="_abstract"]
You can initiate the live migration of a running virtual machine (VM) by using the command line to create a `VirtualMachineInstanceMigration` object for the VM.

.Prerequisites

* You have installed the {oc-first}.
* You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.

.Procedure

. Create a `VirtualMachineInstanceMigration` manifest for the VM that you want to migrate:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstanceMigration
metadata:
  name: <migration_name>
spec:
  vmiName: <vm_name>
----

. Create the object by running the following command:
+
[source,terminal]
----
$ oc create -f <migration_name>.yaml
----
+
The `VirtualMachineInstanceMigration` object triggers a live migration of the VM. This object exists in the cluster only while the virtual machine instance is running, unless manually deleted.

.Verification

* Obtain the VM status by running the following command:
+
[source,terminal]
----
$ oc describe vmi <vm_name> -n <namespace>
----
+
Example output:
+
[source,yaml]
----
# ...
Status:
  Conditions:
    Last Probe Time:       <nil>
    Last Transition Time:  <nil>
    Status:                True
    Type:                  LiveMigratable
  Migration Method:  LiveMigration
  Migration State:
    Completed:                    true
    End Timestamp:                2018-12-24T06:19:42Z
    Migration UID:                d78c8962-0743-11e9-a540-fa163e0c69f1
    Source Node:                  node2.example.com
    Start Timestamp:              2018-12-24T06:19:35Z
    Target Node:                  node1.example.com
    Target Node Address:          10.9.0.18:43891
    Target Node Domain Detected:  true
----

// Module included in the following assemblies:
//
// * virt/live_migration/virt-initiating-live-migration.adoc

[id="virt-canceling-vm-migration-web_{context}"]
= Canceling live migration by using the web console

[role="_abstract"]
You can cancel the live migration of a virtual machine (VM) by using the OpenShift Container Platform web console.

.Prerequisites

* You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select *Cancel Migration* on the Options menu {kebab} beside a VM.

// Module included in the following assemblies:
//
// * virt/live_migration/virt-initiating-live-migration.adoc

[id="virt-canceling-vm-migration-cli_{context}"]
= Canceling live migration by using the CLI

[role="_abstract"]
Cancel the live migration of a virtual machine by deleting the
`VirtualMachineInstanceMigration` object associated with the migration.

.Prerequisites

* You have installed the {oc-first}.
* You have the `kubevirt.io:migrate` RBAC role or you are a cluster administrator.

.Procedure

* Delete the `VirtualMachineInstanceMigration` object that triggered the live
migration, `migration-job` in this example:
+
[source,terminal]
----
$ oc delete vmim migration-job
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* About live migration permissions
* Initiating live migration by using the web console
* Initiating live migration by using the CLI
* Canceling live migration by using the web console
* Canceling live migration by using the CLI
