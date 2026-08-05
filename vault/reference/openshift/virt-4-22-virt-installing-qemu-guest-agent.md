---
title: "Install the QEMU guest agent"
type: reference
domain: openshift
slug: virt-4-22-virt-installing-qemu-guest-agent
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-installing-qemu-guest-agent
version: 4.22
family: virt
documentKind: "Documentation"
---

# Install the QEMU guest agent

[id="virt-installing-qemu-guest-agent"]
= Install the QEMU guest agent

[role="_abstract"]
Enable advanced features like quiesced snapshots and improved monitoring by installing the QEMU guest agent on your virtual machines (VMs). The QEMU guest agent is a daemon that runs on the VM and passes information to the host about the VM, users, file systems, and secondary networks. You must install the QEMU guest agent on VMs created from operating system images that are not provided by Red{nbsp}Hat.

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

[id="virt-installing-qemu-guest-agent-on-linux-vm_{context}"]
= Installing the QEMU guest agent on a Linux VM

[role="_abstract"]
The `qemu-guest-agent` is available by default in {op-system-base-full} virtual machines (VMs). To create snapshots of a VM in the `Running` state with the highest integrity, install the QEMU guest agent.

The QEMU guest agent takes a consistent snapshot by attempting to quiesce the VM file system. This ensures that in-flight I/O is written to the disk before the snapshot is taken. If the guest agent is not present, quiescing is not possible and a best-effort snapshot is taken.

The conditions under which a snapshot is taken are reflected in the snapshot indications that are displayed in the web console or CLI. If these conditions do not meet your requirements, try creating the snapshot again, or use an offline snapshot

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Log in to the VM by using a console or SSH.

. Install the QEMU guest agent by running the following command:
+
[source,terminal]
----
$ yum install -y qemu-guest-agent
----

. Ensure the service is persistent and start it:
+
[source,terminal]
----
$ systemctl enable --now qemu-guest-agent
----

.Verification
* Run the following command to verify that `AgentConnected` is listed in the VM spec:

+
[source,terminal]
----
$ oc get vm <vm_name>
----

// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

[id="installing-qemu-guest-agent-on-windows-vm_{context}"]
= Installing the QEMU guest agent on a Windows VM

[role="_abstract"]
For Windows virtual machines (VMs), the QEMU guest agent is included in the VirtIO drivers. You can install the drivers during a Windows installation or on an existing Windows VM.

To create snapshots of a VM in the `Running` state with the highest integrity, install the QEMU guest agent.

The QEMU guest agent takes a consistent snapshot by attempting to quiesce the VM file system. This ensures that in-flight I/O is written to the disk before the snapshot is taken. If the guest agent is not present, quiescing is not possible and a best-effort snapshot is taken.

Note that in a Windows guest operating system, quiescing also requires the Volume Shadow Copy Service (VSS). Therefore, before you create a snapshot, ensure that VSS is enabled on the VM as well.

The conditions under which a snapshot is taken are reflected in the snapshot indications that are displayed in the web console or CLI. If these conditions do not meet your requirements, try creating the snapshot again or use an offline snapshot.

.Procedure

. In the Windows guest operating system, use the *File Explorer* to navigate to the `guest-agent` directory in the `virtio-win` CD drive.
. Run the `qemu-ga-x86_64.msi` installer.

.Verification
. Obtain a list of network services by running the following command:
+
[source,terminal]
----
$ net start
----

. Verify that the output contains the `QEMU Guest Agent`.
