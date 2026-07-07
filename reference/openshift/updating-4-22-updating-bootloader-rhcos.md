---
title: "Updating the boot loader on {op-system} nodes using bootupd"
type: reference
domain: openshift
slug: updating-4-22-updating-bootloader-rhcos
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/updating/updating-bootloader-rhcos
version: 4.22
family: updating
documentKind: "Documentation"
---

# Updating the boot loader on {op-system} nodes using bootupd

[id="updating-bootloader-rhcos"]
= Updating the boot loader on {op-system} nodes using bootupd

[role="_abstract"]
To update the boot loader on {op-system} nodes using `bootupd`, you must either run the `bootupctl update` command on {op-system} machines manually or provide a machine config with a `systemd` unit.

Unlike `grubby` or other boot loader tools, `bootupd` does not manage kernel space configuration such as passing kernel arguments.
To configure kernel arguments, see Adding kernel arguments to nodes.

[NOTE]
====
You can use `bootupd` to update the boot loader to protect against the BootHole vulnerability.
====

[id="updating-bootloader-manual_{context}"]
= Updating the boot loader manually

[role="_abstract"]
You can manually inspect the status of the system and update the boot loader by using the `bootupctl` command-line tool.

.Procedure

. Inspect the system status by running the following command:
+
[source,terminal]
----
# bootupctl status
----
+
.Example output for `x86_64`
[source,terminal]
----
Component EFI
  Installed: grub2-efi-x64-1:2.04-31.el8_4.1.x86_64,shim-x64-15-8.el8_1.x86_64
  Update: At latest version
----
+
.Example output for `aarch64`
[source,terminal]
----
Component EFI
  Installed: grub2-efi-aa64-1:2.02-99.el8_4.1.aarch64,shim-aa64-15.4-2.el8_1.aarch64
  Update: At latest version
----

[start=2]
. OpenShift Container Platform clusters initially installed on version 4.4 and older require an explicit adoption phase.
+
If the system status is `Adoptable`, perform the adoption by running the following command:
+
[source,terminal]
----
# bootupctl adopt-and-update
----
+
.Example output
[source,terminal]
----
Updated: grub2-efi-x64-1:2.04-31.el8_4.1.x86_64,shim-x64-15-8.el8_1.x86_64
----

. If an update is available, apply the update so that the changes take effect on the next reboot by running the following command:
+
[source,terminal]
----
# bootupctl update
----
+
.Example output
[source,terminal]
----
Updated: grub2-efi-x64-1:2.04-31.el8_4.1.x86_64,shim-x64-15-8.el8_1.x86_64
----

[id="updating-bootloader-auto_{context}"]
= Updating the boot loader automatically by using a machine config

[role="_abstract"]
You can automatically update the boot loader with `bootupd` by creating a systemd service unit that will update the boot loader as needed on every boot.
This unit will run the `bootupctl update` command during the boot process and will be installed on the nodes via a machine config.

[NOTE]
====
This configuration is not enabled by default because unexpected interruptions of the update operation might lead to unbootable nodes.
If you enable this configuration, make sure to avoid interrupting nodes during the boot process while the boot loader update is in progress.
The boot loader update operation generally completes quickly thus the risk is low.
====

.Procedure

. Create a Butane config file, `99-worker-bootupctl-update.bu`, including the contents of the `bootupctl-update.service` systemd unit.
+
[NOTE]
====

====
+
.Example output
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 99-worker-chrony
  labels:
    machineconfiguration.openshift.io/role: worker
systemd:
  units:
  - name: bootupctl-update.service
    enabled: true
    contents: |
      [Unit]
      Description=Bootupd automatic update

      [Service]
      ExecStart=/usr/bin/bootupctl update
      RemainAfterExit=yes

      [Install]
      WantedBy=multi-user.target
----
+
On control plane nodes, substitute `master` for `worker` in `metadata.name` and `metadata.labels.machineconfiguration.openshift.io/role`.

. Generate a `MachineConfig` object file, `99-worker-bootupctl-update.yaml`, containing the configuration to be delivered to the nodes by running the following command:
+
[source,terminal]
----
$ butane 99-worker-bootupctl-update.bu -o 99-worker-bootupctl-update.yaml
----

. Apply the configurations in one of two ways:
+
* If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
+
* If the cluster is already running, apply the file by running the following command:
+
[source,terminal]
----
$ oc apply -f ./99-worker-bootupctl-update.yaml
----
