---
title: "Using the CLI tools"
type: reference
domain: openshift
slug: virt-4-22-virt-using-the-cli-tools
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-using-the-cli-tools
version: 4.22
family: virt
documentKind: "Documentation"
---

# Using the CLI tools

[id="virt-using-the-cli-tools"]
= Using the CLI tools

[role="_abstract"]
You can manage {VirtProductName} resources by using the `virtctl` command-line tool. Virtual machine (VM) commands can also be used to manage virtual machine instances (VMIs) unless otherwise specified.

[NOTE]
====
You can access and change VM disk images by using the `libguestfs` command-line tool. You deploy `libguestfs` by using the `virtctl libguestfs` command.
====

// Module included in the following assemblies:
//
// * virt/getting_started/virt-using-the-cli-tools.adoc

[id="virt-installing-virtctl-binary_{context}"]
= Installing the virtctl binary on {op-system-base} 9 or later, Linux, Windows, or macOS

[role="_abstract"]
You can download the `virtctl` binary by using the OpenShift Container Platform web console and then install it on {op-system-base-full} 9 or later, Linux, Windows, or macOS.

.Procedure

. Navigate to the *Virtualization* page in the web console.

. Click the *Question Mark (?)* icon in the top right corner of screen.

. Select *Command Line Tools* from the menu.

. Locate the *virtctl - KubeVirt command line interface* section of the page.

. Click the *Download virtctl* link to download the `virtctl` binary for your operating system.

. Install `virtctl`:

* For {op-system-base} and other Linux operating systems:

.. Decompress the archive file:
+
[source,terminal]
----
$ tar -xvf <virtctl-version-distribution.arch>.tar.gz
----

.. Run the following command to make the `virtctl` binary executable:
+
[source,terminal]
----
$ chmod +x <path/virtctl-file-name>
----

.. Move the `virtctl` binary to a directory in your `PATH` environment variable.
+
You can check your path by running the following command:
+
[source,terminal]
----
$ echo $PATH
----

.. Set the `KUBECONFIG` environment variable:
+
[source,terminal]
----
$ export KUBECONFIG=/home/<user>/clusters/current/auth/kubeconfig
----

* For Windows:
+
.. Decompress the archive file.

.. Navigate the extracted folder hierarchy and double-click the `virtctl` executable file to install the client.

.. Move the `virtctl` binary to a directory in your `PATH` environment variable.
+
You can check your path by running the following command:
+
[source,terminal]
----
C:\> path
----

* For macOS:
+
.. Decompress the archive file.

.. Move the `virtctl` binary to a directory in your `PATH` environment variable.
+
You can check your path by running the following command:
+
[source,terminal]
----
echo $PATH
----

[id="virtctl-information-commands_{context}"]
= virtctl information commands

[role="_abstract"]
You can use the following `virtctl` information commands to view information about the `virtctl` client.

.Information commands
[width="100%",cols="1a,2a",options="header"]
|===
|Command |Description
|`virtctl version`
|View the `virtctl` client and server versions.

|`virtctl help`
|View a list of `virtctl` commands.

|`virtctl <command> -h\|--help`
|View a list of options for a specific command.

|`virtctl options`
|View a list of global command options for any `virtctl` command.
|===

[id="vm-information-commands_{context}"]
= VM information commands

[role="_abstract"]
You can use `virtctl` to view information about virtual machines (VMs) and virtual machine instances (VMIs).

.VM information commands
[width="100%",cols="1a,2a",options="header"]
|===
|Command |Description
|`virtctl fslist <vm_name>`
|View the file systems available on a guest machine.

|`virtctl guestosinfo <vm_name>`
|View information about the operating systems on a guest machine.

|`virtctl userlist <vm_name>`
|View the logged-in users on a guest machine.
|===

[id="vm-manifest-creation-commands_{context}"]
= VM manifest creation commands

[role="_abstract"]
You can use the following `virtctl create` commands to create manifests for virtual machines, instance types, and preferences.

.VM manifest creation commands
[width="100%",cols="2a,1a",options="header"]
|===
|Command |Description

|`virtctl create vm`
|Create a `VirtualMachine` (VM) manifest.

|`virtctl create vm --name <vm_name>`
|Create a VM manifest, specifying a name for the VM.

|`virtctl create vm --user <user_name> --ssh-key\|password-file=<value>`
|Create a VM manifest with a cloud-init configuration to create the selected user and either add an SSH public key from the supplied string, or a password from a file.

|`virtctl create vm --access-cred type:password,src:<secret>`
|Create a VM manifest with a user and password combination injected from the selected secret.

|`virtctl create vm --access-cred type:ssh,src:<secret>,user:<user_name>`
|Create a VM manifest with an SSH public key injected from the selected secret.

|`virtctl create vm --volume-sysprep src:<config_map>`
|Create a VM manifest, specifying a config map to use as the sysprep volume. The config map must contain a valid answer file named `unattend.xml` or `autounattend.xml`.

|`virtctl create vm --instancetype <instancetype_name>`
|Create a VM manifest that uses an existing cluster-wide instance type.

|`virtctl create vm --instancetype=virtualmachineinstancetype/<instancetype_name>`
|Create a VM manifest that uses an existing namespaced instance type.

|`virtctl create instancetype --cpu <cpu_value> --memory <memory_value> --name <instancetype_name>`
|Create a manifest for a cluster-wide instance type.

|`virtctl create instancetype --cpu <cpu_value> --memory <memory_value> --name <instancetype_name> --namespace <namespace_value>`
|Create a manifest for a namespaced instance type.

|`virtctl create preference --name <preference_name>`
|Create a manifest for a cluster-wide VM preference, specifying a name for the preference.

|`virtctl create preference --namespace <namespace_value>`
|Create a manifest for a namespaced VM preference.
|===

[id="vm-management-commands_{context}"]
= VM management commands

[role="_abstract"]
You can use the following `virtctl` commands to manage and migrate virtual machines (VMs) and VM instances (VMIs).

.VM management commands
[width="100%",cols="1a,2a",options="header"]
|===
|Command |Description

|`virtctl start <vm_name>`
|Start a VM.

|`virtctl start --paused <vm_name>`
|Start a VM in a paused state. This option enables you to interrupt the boot process from the VNC console.

|`virtctl stop <vm_name>`
|Stop a VM.

|`virtctl stop <vm_name> --grace-period 0 --force`
|Force stop a VM. This option might cause data inconsistency or data loss.

|`virtctl pause vm <vm_name>`
|Pause a VM. The machine state is kept in memory.

|`virtctl unpause vm <vm_name>`
|Unpause a VM.

|`virtctl migrate <vm_name>`
|Migrate a VM.

|`virtctl migrate-cancel <vm_name>`
|Cancel a VM migration.

|`virtctl restart <vm_name>`
|Restart a VM.
|===

[id="vm-connection-commands_{context}"]
= VM connection commands

[role="_abstract"]
You use can use the following `virtctl` commands to expose ports and connect to virtual machines (VMs) and VM instances (VMIs).

.VM connection commands
[width="100%",cols="1a,2a",options="header"]
|===
|Command |Description
|`virtctl console <vm_name>`
|Connect to the serial console of a VM.

|`virtctl expose vm <vm_name> --name <service_name> --type <ClusterIP\|NodePort\|LoadBalancer> --port <port>`
|Create a service that forwards a designated port of a VM and expose the service on the specified port of the node.

Example: `virtctl expose vm rhel9_vm --name rhel9-ssh --type NodePort --port 22`

|`virtctl scp -i <ssh_key> <file_name> <user_name>@vm/<vm_name>`
|Copy a file from your machine to a VM. This command uses the private key of an SSH key pair. The VM must be configured with the public key.

|`virtctl scp -i <ssh_key> <user_name@vm/<vm_name>:<file_name> .`
|Copy a file from a VM to your machine. This command uses the private key of an SSH key pair. The VM must be configured with the public key.

|`virtctl ssh -i <ssh_key> <user_name>@vm/<vm_name>`
|Open an SSH connection with a VM. This command uses the private key of an SSH key pair. The VM must be configured with the public key.

|`virtctl vnc <vm_name>`
|Connect to the VNC console of a VM.

You must have `virt-viewer` installed.

|`virtctl vnc --proxy-only=true <vm_name>`
|Display the port number and connect manually to a VM by using any viewer through the VNC connection.

|`virtctl vnc --port=<port-number> <vm_name>`
|Specify a port number to run the proxy on the specified port, if that port is available.

If a port number is not specified, the proxy runs on a random port.
|===

[id="vm-export-commands_{context}"]
= VM export commands

[role="_abstract"]
Use `virtctl vmexport` commands to create, download, or delete a volume exported from a VM, VM snapshot, or persistent volume claim (PVC). Certain manifests also contain a header secret, which grants access to the endpoint to import a disk image in a format that {VirtProductName} can use.

.VM export commands
[width="100%",cols="1a,2a",options="header"]
|===
|Command |Description
|`virtctl vmexport create <vmexport_name> --vm\|snapshot\|pvc=<object_name>`
|Create a `VirtualMachineExport` custom resource (CR) to export a volume from a VM, VM snapshot, or PVC.

* `--vm`: Exports the PVCs of a VM.
* `--snapshot`: Exports the PVCs contained in a `VirtualMachineSnapshot` CR.
* `--pvc`: Exports a PVC.
* Optional: `--ttl=1h` specifies the time to live. The default duration is 2 hours.

|`virtctl vmexport delete <vmexport_name>`
|Delete a `VirtualMachineExport` CR manually.

|`virtctl vmexport download <vmexport_name> --output=<output_file> --volume=<volume_name>`
|Download the volume defined in a `VirtualMachineExport` CR.

* `--output` specifies the file format. Example: `disk.img.gz`.
* `--volume` specifies the volume to download. This flag is optional if only one volume is available.

Optional:

* `--keep-vme` retains the `VirtualMachineExport` CR after download. The default behavior is to delete the `VirtualMachineExport` CR after download.
* `--insecure` enables an insecure HTTP connection.

|`virtctl vmexport download <vmexport_name> --vm\|snapshot\|pvc=<object_name> --output=<output_file> --volume=<volume_name>`
|Create a `VirtualMachineExport` CR and then download the volume defined in the CR.

|`virtctl vmexport download export --manifest`
|Retrieve the manifest for an existing export. The manifest does not include the header secret.

|`virtctl vmexport download export --manifest --vm=example`
|Create a VM export for a VM example, and retrieve the manifest. The manifest does not include the header secret.

|`virtctl vmexport download export --manifest --snap=example`
|Create a VM export for a VM snapshot example, and retrieve the manifest. The manifest does not include the header secret.

|`virtctl vmexport download export --manifest --include-secret`
|Retrieve the manifest for an existing export. The manifest includes the header secret.

|`virtctl vmexport download export --manifest --manifest-output-format=json`
|Retrieve the manifest for an existing export in json format. The manifest does not include the header secret.

|`virtctl vmexport download export --manifest --include-secret --output=manifest.yaml`
|Retrieve the manifest for an existing export. The manifest includes the header secret and writes it to the file specified.
|===

[id="hot-plug-and-hot-unplug-commands_{context}"]
= Hot plug and hot unplug  commands

[role="_abstract"]
You can use the following `virtctl` commands to add or remove resources from running virtual machines (VMs) and VM instances (VMIs).

.Hot plug and hot unplug commands
[width="100%",cols="1a,2a",options="header"]
|===
|Command |Description
|`virtctl addvolume <vm_name> --volume-name=<datavolume_or_PVC> [--persist] [--serial=<label>]`
|Hot plug a data volume or persistent volume claim (PVC).

Optional:

* `--persist` mounts the virtual disk permanently on a VM. *This flag does not apply to VMIs.*
* `--serial=<label>` adds a label to the VM. If you do not specify a label, the default label is the data volume or PVC name.

|`virtctl removevolume <vm_name> --volume-name=<virtual_disk>`
|Hot unplug a virtual disk.
|===

[id="image-upload-commands_{context}"]
= Image upload commands

[role="_abstract"]
You can use the following `virtctl image-upload` commands to upload a VM image to a data volume.

.Image upload commands
[width="100%",cols="1a,2a",options="header"]
|===
|Command |Description
|`virtctl image-upload dv <datavolume_name> --image-path=</path/to/image> --no-create`
|Upload a VM image to a data volume that already exists.

|`virtctl image-upload dv <datavolume_name> --size=<datavolume_size> --image-path=</path/to/image>`
|Upload a VM image to a new data volume of a specified requested size.

|`virtctl image-upload dv <datavolume_name> --datasource --size=<datavolume_size> --image-path=</path/to/image>`
|Upload a VM image to a new data volume and create an associated `DataSource` object for it.
|===

// Module included in the following assemblies:
//
// * virt/getting_started/virt-using-the-cli-tools.adoc

[id="virt-deploying-libguestfs-with-virtctl_{context}"]
= Deploying libguestfs by using virtctl

[role="_abstract"]
You can use the `virtctl guestfs` command to deploy an interactive container with `libguestfs-tools` and a persistent volume claim (PVC) attached to it.

.Procedure

* To deploy a container with `libguestfs-tools`, mount the PVC, and attach a shell to it, run the following command:
+
[source,terminal]
----
$ virtctl guestfs -n <namespace> <pvc_name>
----
+
[IMPORTANT]
====
The `<pvc_name>` argument is required. If you do not include it, an error message appears.
====
// Module included in the following assemblies:
//
// * virt/getting_started/virt-using-the-cli-tools.adoc

[id="virt-about-libguestfs-tools-virtctl-guestfs_{context}"]
= Libguestfs and virtctl guestfs commands

[role="_abstract"]
`Libguestfs` tools help you access and modify virtual machine (VM) disk images. You can use `libguestfs` tools to view and edit files in a guest, clone and build virtual machines, and format and resize disks.

You can also use the `virtctl guestfs` command and its sub-commands to modify, inspect, and debug VM disks on a PVC. To see a complete list of possible sub-commands, enter `virt-` on the command line and press the Tab key. For example:

[width="100%",cols="42%,58%",options="header",]
|===
|Command |Description

|`virt-edit -a /dev/vda /etc/motd`
|Edit a file interactively in your terminal.

|`virt-customize -a /dev/vda --ssh-inject root:string:<public key example>`
|Inject an ssh key into the guest and create a login.

|`virt-df -a /dev/vda -h`
|See how much disk space is used by a VM.

|`virt-customize -a /dev/vda --run-command 'rpm -qa > /rpm-list'`
|See the full list of all RPMs installed on a guest by creating an output file containing the full list.

|`virt-cat -a /dev/vda /rpm-list`
|Display the output file list of all RPMs created using the `virt-customize -a /dev/vda --run-command 'rpm -qa > /rpm-list'` command in your terminal.

|`virt-sysprep -a /dev/vda`
|Seal a virtual machine disk image to be used as a template.
|===

By default, `virtctl guestfs` creates a session with everything needed to manage a VM disk. However, the command also supports several flag options if you want to customize the behavior:

[width="100%",cols="42%,58%",options="header",]
|===
|Flag Option |Description

|`--h` or `--help`
|Provides help for `guestfs`.

|`-n <namespace>` option with a `<pvc_name>` argument
|To use a PVC from a specific namespace.

If you do not use the `-n <namespace>` option, your current project is used. To change projects, use `oc project <namespace>`.

If you do not include a `<pvc_name>` argument, an error message appears.

|`--image string`
|Lists the `libguestfs-tools` container image.

You can configure the container to use a custom image by using the `--image` option.

|`--kvm`
|Indicates that `kvm` is used by the `libguestfs-tools` container.

By default, `virtctl guestfs` sets up `kvm` for the interactive container, which greatly speeds up the `libguest-tools` execution because it uses QEMU.

If a cluster does not have any `kvm` supporting nodes, you must disable `kvm` by setting the option `--kvm=false`.

If not set, the `libguestfs-tools` pod remains pending because it cannot be scheduled on any node.

|`--pull-policy string`
|Shows the pull policy for the `libguestfs` image.

You can also overwrite the image's pull policy by setting the `pull-policy` option.
|===

The command also checks if a PVC is in use by another pod, in which case an error message appears. However, once the `libguestfs-tools` process starts, the setup cannot avoid a new pod using the same PVC. You must verify that there are no active `virtctl guestfs` pods before starting the VM that accesses the same PVC.

[NOTE]
=====
The `virtctl guestfs` command accepts only a single PVC attached to the interactive pod.
=====

[role="_additional-resources"]
== Additional resources
* Red{nbsp}Hat Ansible Automation Hub
* `libguestfs`
