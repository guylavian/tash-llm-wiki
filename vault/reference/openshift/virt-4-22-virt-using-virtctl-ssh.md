---
title: "Configure SSH by using the virtctl CLI tool"
type: reference
domain: openshift
slug: virt-4-22-virt-using-virtctl-ssh
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-using-virtctl-ssh
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configure SSH by using the virtctl CLI tool

[id="virt-using-virtctl-ssh"]
= Configure SSH by using the virtctl CLI tool

[role="_abstract"]
You can add a public SSH key to a virtual machine (VM) and connect to the VM by running the `virtctl ssh` command, or add the `virtctl port-foward` command to your `.ssh/config` file and connect to the VM by using OpenSSH.

[IMPORTANT]
====
The `virtctl ssh` command method is not recommended for high traffic loads because it places a burden on the API server.
====

You can add public SSH keys to {op-system-base-full} 9 VMs at runtime or at first boot to VMs with guest operating systems that can be configured by using a cloud-init data source.

[TIP]
====
You can copy the `virtctl ssh` command in the web console by selecting *Copy SSH command* from the options {kebab} menu beside a VM on the *VirtualMachines* page.

Alternatively, right-click the VM in the tree view and select *Copy SSH command* from the menu to copy the `virtctl ssh` command.
====

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-about-static-and-dynamic-ssh-keys_{context}"]
= About static and dynamic SSH key management

[role="_abstract"]
You can add public SSH keys to virtual machines (VMs) statically at first boot or dynamically at runtime.

[NOTE]
====
Only {op-system-base-full} 9 supports dynamic key injection.
====

[id="static-key-management_{context}"]
== Static SSH key management

You can add a statically managed SSH key to a VM with a guest operating system that supports configuration by using a cloud-init data source. The key is added to the virtual machine (VM) at first boot.

You can add the key by using one of the following methods:

* Add a key to a single VM when you create it by using the web console or the command line.
* Add a key to a project by using the web console. Afterwards, the key is automatically added to the VMs that you create in this project.

Use cases:

* As a VM owner, you can provision all your newly created VMs with a single key.

[id="dynamic-key-management_{context}"]
== Dynamic SSH key management

You can enable dynamic SSH key management for a VM with {op-system-base-full} 9 installed. Afterwards, you can update the key during runtime. The key is added by the QEMU guest agent, which is installed with Red Hat boot sources.

When dynamic key management is disabled, the default key management setting of a VM is determined by the image used for the VM.

Use cases:

* Granting or revoking access to VMs: As a cluster administrator, you can grant or revoke remote VM access by adding or removing the keys of individual users from a `Secret` object that is applied to all VMs in a namespace.
* User access: You can add your access credentials to all VMs that you create and manage.

* Ansible provisioning:

** As an operations team member, you can create a single secret that contains all the keys used for Ansible provisioning.
** As a VM owner, you can create a VM and attach the keys used for Ansible provisioning.

* Key rotation:

** As a cluster administrator, you can rotate the Ansible provisioner keys used by VMs in a namespace.
** As a workload owner, you can rotate the key for the VMs that you manage.

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-static-key-management-vm_{context}"]
= Manage static keys

[role="_abstract"]
You can add a statically managed public SSH key when you create a virtual machine (VM) by using the OpenShift Container Platform web console or the command line. The key is added as a cloud-init data source when the VM boots for the first time.

You can also add a public SSH key to a project when you create a VM by using the web console. The key is saved as a secret and is added automatically to all VMs that you create.

[NOTE]
====
If you add a secret to a project and then delete the VM, the secret is retained because it is a namespace resource. You must delete the secret manually.
====

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-adding-key-creating-vm-template_{context}"]
= {title} when creating a VM from a template

[role="_abstract"]
You can add a statically managed public SSH key when you create a virtual machine (VM) by using the OpenShift Container Platform web console. The key is added to the VM as a cloud-init data source at first boot. This method does not affect cloud-init user data.

Optional: You can add a key to a project. Afterwards, this key is added automatically to VMs that you create in the project.
[role="_abstract"]
You can enable dynamic public SSH key injection when you create a virtual machine (VM) from a template by using the OpenShift Container Platform web console. Then, you can update the key at runtime.

[NOTE]
====
Only {op-system-base-full} 9 supports dynamic key injection.
====

The key is added to the VM by the QEMU guest agent, which is installed with {op-system-base} 9.

.Prerequisites

* You generated an SSH key pair by running the `ssh-keygen` command.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.
. Click the *Red Hat Enterprise Linux 9 VM* tile.
. Click a template tile.
+
The guest operating system must support configuration from a cloud-init data source.
. Click *Customize VirtualMachine*.
. Click *Next*.
. Click the *Scripts* tab.
. If you have not already added a public SSH key to your project, click the edit icon beside *Authorized SSH key* and select one of the following options:

* *Use existing*: Select a secret from the secrets list.
* *Add new*:
.. Browse to the SSH key file or paste the file in the key field.
.. Enter the secret name.
.. Optional: Select *Automatically apply this key to any new VirtualMachine you create in this project*.
. Set *Dynamic SSH key injection* to on.
. Click *Save*.
. Click *Create VirtualMachine*.
+
The *VirtualMachine details* page displays the progress of the VM creation.

.Verification
* Click the *Scripts* tab on the *Configuration* tab.
+
The secret name is displayed in the *Authorized SSH key* section.

// Module included in the following assemblies:
//
// * virt/creating_vms_advanced/creating_vms_cli/virt-creat-vm-manifest-virtctl.adoc
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-creating-vm-instancetype_{context}"]
= Creating a VM from an instance type by using the web console

[role="_abstract"]
You can create a virtual machine (VM) from an instance type by using the OpenShift Container Platform web console. You can also use the web console to create a VM by copying an existing snapshot or to clone a VM.

You can create a VM from a list of available bootable volumes. You can add Linux- or Windows-based volumes to the list.

[role="_abstract"]
You can add a statically managed SSH key when you create a virtual machine (VM) from an instance type by using the OpenShift Container Platform web console. The key is added to the VM as a cloud-init data source at first boot. This method does not affect cloud-init user data.
[role="_abstract"]
You can enable dynamic SSH key injection when you create a virtual machine (VM) from an instance type by using the OpenShift Container Platform web console. Then, you can add or revoke the key at runtime.

[NOTE]
====
Only {op-system-base-full} 9 supports dynamic key injection.
====

The key is added to the VM by the QEMU guest agent, which is installed with {op-system-base} 9.

.Procedure

. In the web console, navigate to *Virtualization* -> *Catalog*.
+
The *InstanceTypes* tab opens by default.
+
[NOTE]
====
When configuring a downward-metrics device on an {ibm-z-name} system that uses a VM preference, set the `spec.preference.name` value to `rhel.9.s390x` or another available preference with the format `*.s390x`.
====
. Heterogeneous clusters only: To filter the bootable volumes using the options provided, click *Architecture*.

. Select either of the following options:
* Select a suitable bootable volume from the list. If the list is truncated, click the *Show all* button to display the entire list.
+
[NOTE]
====
The bootable volume table lists only those volumes in the `openshift-virtualization-os-images` namespace that have the `instancetype.kubevirt.io/default-preference` label.
====
+
** Optional: Click the star icon to designate a bootable volume as a favorite. Starred bootable volumes appear first in the volume list.

* Click *Add volume* to upload a new volume or to use an existing persistent volume claim (PVC), a volume snapshot, or a `containerDisk` volume. Click *Save*.
+
Logos of operating systems that are not available in the cluster are shown at the bottom of the list. You can add a volume for the required operating system by clicking the *Add volume* link.
+
In addition, there is a link to the *Create a Windows bootable volume* quick start. The same link appears in a popover if you hover the pointer over the question mark icon next to the _Select volume to boot from_ line.
+
Immediately after you install the environment or when the environment is disconnected, the list of volumes to boot from is empty. In that case, three operating system logos are displayed: Windows, {op-system-base}, and Linux. You can add a new volume that meets your requirements by clicking the *Add volume* button.

. Click an instance type tile and select the resource size appropriate for your workload. You can select huge pages for Red{nbsp}Hat-provided instance types of the *M* and *CX* series. Huge page options are identified by names that end with *1gi*.
. Click the *Red Hat Enterprise Linux 9 VM* tile.
. Optional: Choose the virtual machine details, including the VM's name, that apply to the volume you are booting from:
** For a Linux-based volume, follow these steps to configure SSH:

.. If you have not already added a public SSH key to your project, click the edit icon beside *Authorized SSH key* in the *VirtualMachine details* section.
.. Select one of the following options:
+
--
* *Use existing*: Select a secret from the secrets list.
* *Add new*: Follow these steps:
... Browse to the public SSH key file or paste the file in the key field.
... Enter the secret name.
... Optional: Select *Automatically apply this key to any new VirtualMachine you create in this project*.
--
.. Click *Save*.

** For a Windows volume, follow either of these set of steps to configure sysprep options:
*** If you have not already added sysprep options for the Windows volume, follow these steps:
... Click the edit icon beside *Sysprep* in the *VirtualMachine details* section.
... Add the *Autoattend.xml* answer file.
... Add the *Unattend.xml* answer file.
... Click *Save*.
*** If you want to use existing sysprep options for the Windows volume, follow these steps:
... Click *Attach existing sysprep*.
... Enter the name of the existing sysprep *Unattend.xml* answer file.
... Click *Save*.
. Set *Dynamic SSH key injection* in the *VirtualMachine details* section to on.
. Optional: If you are creating a Windows VM, you can mount a Windows driver disk:
.. Click the *Customize VirtualMachine* button.
.. On the *VirtualMachine details* page, click *Storage*.
.. Select the *Mount Windows drivers disk* checkbox.
. Optional: Click *View YAML & CLI* to view the YAML file. Click *CLI* to view the CLI commands. You can also download or copy either the YAML file contents or the CLI commands.
. Click *Create VirtualMachine*.

.Result

After the VM is created, you can monitor the status on the *VirtualMachine details* page.

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-adding-public-key-vm-cli_{context}"]
= Adding a key when creating a VM by using the CLI

[role="_abstract"]
You can add a statically managed public SSH key when you create a virtual machine (VM) by using the command line. The key is added to the VM at first boot.

The key is added to the VM as a cloud-init data source. This method separates the access credentials from the application data in the cloud-init user data. This method does not affect cloud-init user data.

.Prerequisites

* You generated an SSH key pair by running the `ssh-keygen` command.
* You have installed the {oc-first}.

.Procedure

. Create a manifest file for a `VirtualMachine` object and a `Secret` object.
+
Example manifest:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  dataVolumeTemplates:
    - metadata:
        name: example-vm-volume
      spec:
        sourceRef:
          kind: DataSource
          name: rhel9
          namespace: openshift-virtualization-os-images
        storage:
          resources: {}
  instancetype:
    name: u1.medium
  preference:
    name: rhel.9
  runStrategy: Always
  template:
    spec:
      domain:
        devices: {}
      volumes:
        - dataVolume:
            name: example-vm-volume
          name: rootdisk
        - cloudInitNoCloud:
            userData: |-
              #cloud-config
              user: cloud-user
          name: cloudinitdisk
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              noCloud: {}
            source:
              secret:
                secretName: authorized-keys
---
apiVersion: v1
kind: Secret
metadata:
  name: authorized-keys
data:
  key: c3NoLXJzYSB...
----
+
* `spec.template.spec.volumes.cloudInitNoCloud` specifies the `cloudInitNoCloud` data source.
* `spec.template.spec.accessCredentials.sshPublicKey.source.secret.secretName` specifies the `Secret` object name.
* `data.key` specifies the public SSH key.

. Create the `VirtualMachine` and `Secret` objects by running the following command:
+
[source,terminal]
----
$ oc create -f <manifest_file>.yaml
----

. Start the VM by running the following command:
+
[source,terminal]
----
$ virtctl start vm example-vm -n example-namespace
----

.Verification

* Get the VM configuration:
+
[source,terminal]
----
$ oc describe vm example-vm -n example-namespace
----
+
Example output:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  template:
    spec:
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              noCloud: {}
            source:
              secret:
                secretName: authorized-keys
# ...
----

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-adding-dynamic-key-vm_{context}"]
= Manage dynamic keys

[role="_abstract"]
You can enable dynamic key injection for a virtual machine (VM) by using the OpenShift Container Platform web console or the command line. Then, you can update the key at runtime.

[NOTE]
====
Only {op-system-base-full} 9 supports dynamic key injection.
====

If you disable dynamic key injection, the VM inherits the key management method of the image from which it was created.

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-editing-vm-dynamic-key-injection_{context}"]
= Enabling dynamic SSH key injection by using the web console

[role="_abstract"]
You can enable dynamic key injection for a virtual machine (VM) by using the OpenShift Container Platform web console. Then, you can update the public SSH key at runtime.

The key is added to the VM by the QEMU guest agent, which is installed with {op-system-base-full} 9.

.Prerequisites

* The guest operating system is {op-system-base} 9.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.
. On the *Configuration* tab, click *Scripts*.
. If you have not already added a public SSH key to your project, click the edit icon beside *Authorized SSH key* and select one of the following options:

* *Use existing*: Select a secret from the secrets list.
* *Add new*:
.. Browse to the SSH key file or paste the file in the key field.
.. Enter the secret name.
.. Optional: Select *Automatically apply this key to any new VirtualMachine you create in this project*.
. Set *Dynamic SSH key injection* to on.
. Click *Save*.

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-enabling-dynamic-key-injection-cli_{context}"]
= Enabling dynamic key injection by using the CLI

[role="_abstract"]
You can enable dynamic key injection for a virtual machine (VM) by using the command line. Then, you can update the public SSH key at runtime.

[NOTE]
====
Only {op-system-base-full} 9 supports dynamic key injection.
====

The key is added to the VM by the QEMU guest agent, which is installed automatically with {op-system-base} 9.

.Prerequisites

* You generated an SSH key pair by running the `ssh-keygen` command.
* You have installed the {oc-first}.

.Procedure

. Create a manifest file for a `VirtualMachine` object and a `Secret` object.
+
Example manifest:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  dataVolumeTemplates:
    - metadata:
        name: example-vm-volume
      spec:
        sourceRef:
          kind: DataSource
          name: rhel9
          namespace: openshift-virtualization-os-images
        storage:
          resources: {}
  instancetype:
    name: u1.medium
  preference:
    name: rhel.9
  runStrategy: Always
  template:
    spec:
      domain:
        devices: {}
      volumes:
        - dataVolume:
            name: example-vm-volume
          name: rootdisk
        - cloudInitNoCloud:
            userData: |-
              #cloud-config
              runcmd:
              - [ setsebool, -P, virt_qemu_ga_manage_ssh, on ]
          name: cloudinitdisk
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              qemuGuestAgent:
                users: ["cloud-user"]
            source:
              secret:
                secretName: authorized-keys
---
apiVersion: v1
kind: Secret
metadata:
  name: authorized-keys
data:
  key: c3NoLXJzYSB...
----
* `spec.template.spec.volumes.cloudInitNoCloud` defines the data source, for example `userData`.
* `spec.template.spec.accessCredentials.sshPublicKey.source.secret.secretName` defines the `secret` object name.
* `data.key` within the `secret` object defines the full public SSH key.

. Create the `VirtualMachine` and `Secret` objects by running the following command:
+
[source,terminal]
----
$ oc create -f <manifest_file>.yaml
----

. Start the VM by running the following command:
+
[source,terminal]
----
$ virtctl start vm example-vm -n example-namespace
----

.Verification

* Get the VM configuration by running the following command:
+
[source,terminal]
----
$ oc describe vm example-vm -n example-namespace
----
+
Example output:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  template:
    spec:
      accessCredentials:
        - sshPublicKey:
            propagationMethod:
              qemuGuestAgent:
                users: ["cloud-user"]
            source:
              secret:
                secretName: authorized-keys
# ...
----

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-using-virtctl-ssh-command_{context}"]
= Using the virtctl ssh command

[role="_abstract"]
You can use the `virtctl ssh` command to access a running virtual machine instance (VMI). The command accepts VM or VMI targets.

.Prerequisites

* You installed the `virtctl` command-line tool.
* You added a public SSH key to the VM.
* You have an SSH client installed.
* The environment where you installed the `virtctl` tool has the cluster permissions required to access the VM. For example, you ran `oc login` or you set the `KUBECONFIG` environment variable.

.Procedure

. Run the `virtctl ssh` command:
+
[source,terminal]
----
$ virtctl -n <namespace> ssh <username>@vm/<vm_name> -i <ssh_key>
----
+
You must specify the resource type (`vmi/` or `vm/`) before the VM name.
+
For example:
+
[source,terminal]
----
$ virtctl -n my-namespace ssh cloud-user@vm/example-vm -i my-key
----

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-virtctl-ssh.adoc

[id="virt-using-virtctl-port-forward-command_{context}"]
= Using the virtctl port-forward command

[role="_abstract"]
You can use your local OpenSSH client and the `virtctl port-forward` command to connect to a running virtual machine (VM). You can use this method with Ansible to automate the configuration of VMs.

This method is recommended for low-traffic applications because port-forwarding traffic is sent over the control plane. This method is not recommended for high-traffic applications such as Rsync or Remote Desktop Protocol because it places a heavy burden on the API server.

.Prerequisites
* You have installed the `virtctl` client.
* The virtual machine you want to access is running.
* The environment where you installed the `virtctl` tool has the cluster permissions required to access the VM. For example, you ran `oc login` or you set the `KUBECONFIG` environment variable.

.Procedure

. Add the following text to the `~/.ssh/config` file on your client machine:
+
[source,terminal]
----
Host vm/*
  ProxyCommand virtctl port-forward --stdio=true %h %p
----

. Connect to the VM by running the following command:
+
[source,terminal]
----
$ ssh <user>@vm/<vm_name>.<namespace>
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
