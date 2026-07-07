---
title: "Troubleshooting operating system issues"
type: reference
domain: openshift
slug: support-4-22-troubleshooting-operating-system-issues
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/troubleshooting-operating-system-issues
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting operating system issues

[id="troubleshooting-operating-system-issues"]
= Troubleshooting operating system issues

[role="_abstract"]
OpenShift Container Platform runs on {op-system}. You can follow these procedures to troubleshoot problems related to the operating system.

// Investigating kernel crashes
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operating-system-issues.adoc

[id="investigating-kernel-crashes"]
= Investigating kernel crashes

[role="_abstract"]
The `kdump` service, included in the `kexec-tools` package, provides a crash-dumping mechanism. You can use this service to save the contents of a system's memory for later analysis.

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operating-system-issues.adoc

[id="enabling-kdump"]
= Enabling kdump

[role="_abstract"]
{op-system} ships with the `kexec-tools` package, but manual configuration is required to enable the `kdump` service.

.Procedure

. To reserve memory for the crash kernel during the first kernel booting, provide kernel arguments by entering the following command:
+
[source,terminal]
----
# rpm-ostree kargs --append='crashkernel=256M'
----
+
[NOTE]
====
For the `ppc64le` platform, the recommended value for `crashkernel` is `crashkernel=2G-4G:384M,4G-16G:512M,16G-64G:1G,64G-128G:2G,128G-:4G`.
====

. Optional: To write the crash dump over the network or to some other location, rather than to the default local `/var/crash` location, edit the `/etc/kdump.conf` configuration file.
+
[NOTE]
====
If your node uses LUKS-encrypted devices, you must use network dumps as kdump does not support saving crash dumps to LUKS-encrypted devices.
====
+
For details on configuring the `kdump` service, see the comments in `/etc/sysconfig/kdump`, `/etc/kdump.conf`, and the `kdump.conf` manual page.
Also refer to the RHEL kdump documentation for further information on configuring the dump target.
+
[IMPORTANT]
====
If you have multipathing enabled on your primary disk, the dump target must be either an NFS or SSH server and you must exclude the multipath module from your `/etc/kdump.conf` configuration file.
====

. Enable the `kdump` systemd service.
+
[source,terminal]
----
# systemctl enable kdump.service
----

. Reboot your system.
+
[source,terminal]
----
# systemctl reboot
----

. Ensure that kdump has loaded a crash kernel by checking that the `kdump.service` systemd service has started and exited successfully and that the command, `cat /sys/kernel/kexec_crash_loaded`, prints the value `1`.

// Module included in the following assemblies:
//
// * support/troubleshooting-operating-system-issues.adoc

[id="enabling-kdump-day-one"]
= Enabling kdump on day-1

[role="_abstract"]
The `kdump` service is intended to be enabled per node to debug kernel problems. Because there are costs to having kdump enabled, and these costs accumulate with each additional kdump-enabled node, it is recommended that the `kdump` service only be enabled on each node as needed. Potential costs of enabling the `kdump` service on each node include:

* Less available RAM due to memory being reserved for the crash kernel.
* Node unavailability while the kernel is dumping the core.
* Additional storage space being used to store the crash dumps.

If you are aware of the downsides and trade-offs of having the `kdump` service enabled, it is possible to enable kdump in a cluster-wide fashion. Although machine-specific machine configs are not yet supported, you can use a `systemd` unit in a `MachineConfig` object as a day-1 customization and have kdump enabled on all nodes in the cluster. You can create a `MachineConfig` object and inject that object into the set of manifest files used by Ignition during cluster setup.

[NOTE]
====
See "Customizing nodes" in the _Installing -> Installation configuration_ section for more information and examples on how to use Ignition configs.
====

.Procedure

. Create a Butane config file, `99-worker-kdump.bu`, that configures and enables kdump. This creates a `MachineConfig` object for cluster-wide configuration:
+
[NOTE]
====
====
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 99-worker-kdump
  labels:
    machineconfiguration.openshift.io/role: worker
openshift:
  kernel_arguments:
    - crashkernel=256M
storage:
  files:
    - path: /etc/kdump.conf
      mode: 0644
      overwrite: true
      contents:
        inline: |
          path /var/crash
          core_collector makedumpfile -l --message-level 7 -d 31

    - path: /etc/sysconfig/kdump
      mode: 0644
      overwrite: true
      contents:
        inline: |
          KDUMP_COMMANDLINE_REMOVE="hugepages hugepagesz slub_debug quiet log_buf_len swiotlb"
          KDUMP_COMMANDLINE_APPEND="irqpoll nr_cpus=1 reset_devices cgroup_disable=memory mce=off numa=off udev.children-max=2 panic=10 rootflags=nofail acpi_no_memhotplug transparent_hugepage=never nokaslr novmcoredd hest_disable"
          KEXEC_ARGS="-s"
          KDUMP_IMG="vmlinuz"

systemd:
  units:
    - name: kdump.service
      enabled: true
----
+
where::
* Replace `worker` with `master` in both locations when creating a `MachineConfig` object for control plane nodes.
* Provide kernel arguments to reserve memory for the crash kernel. You can add other kernel arguments if necessary. For the `ppc64le` platform, the recommended value for `crashkernel` is `crashkernel=2G-4G:384M,4G-16G:512M,16G-64G:1G,64G-128G:2G,128G-:4G`.
* If you want to change the contents of `/etc/kdump.conf` from the default, include this section and modify the `inline` subsection accordingly.
* If you want to change the contents of `/etc/sysconfig/kdump` from the default, include this section and modify the `inline` subsection accordingly.
* For the `ppc64le` platform, replace `nr_cpus=1` with `maxcpus=1`, which is not supported on this platform.

[NOTE]
====
To export the dumps to NFS targets, some kernel modules must be explicitly added to the configuration file:

.Example `/etc/kdump.conf` file
[source,text]
----
nfs server.example.com:/export/cores
core_collector makedumpfile -l --message-level 7 -d 31
extra_bins /sbin/mount.nfs
extra_modules nfs nfsv3 nfs_layout_nfsv41_files blocklayoutdriver nfs_layout_flexfiles nfs_layout_nfsv41_files
----
====

. Use Butane to generate a machine config YAML file, `99-worker-kdump.yaml`, containing the configuration to be delivered to the nodes:
+
[source,terminal]
----
$ butane 99-worker-kdump.bu -o 99-worker-kdump.yaml
----

. Put the YAML file into the `<installation_directory>/manifests/` directory during cluster setup. You can also create this `MachineConfig` object after cluster setup with the YAML file:
+
[source,terminal]
----
$ oc create -f 99-worker-kdump.yaml
----

**Testing the kdump configuration**

See the Testing the kdump configuration section in the {op-system-base} documentation for kdump.

See the Capturing the Dump section in the {op-system-base} documentation for kdump.

**Analyzing a core dump**

See the Analyzing a core dump section in the {op-system-base} documentation for kdump.

See the Dump Analysis section in the {op-system-base} documentation for kdump.

[NOTE]
====
It is recommended to perform vmcore analysis on a separate {op-system-base} system.
====

[role="_additional-resources"]
.Additional resources

* Fedora CoreOS Docs on debugging kernel crashes
* Setting up kdump in Fedora
* Setting up kdump in RHEL
* Linux kernel documentation for kdump
* kdump.conf(5) manual page
* kexec(8) manual page
* Red Hat Knowledgebase article regarding kexec and kdump

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operating-system-issues.adoc

[id="debugging-ignition_{context}"]
= Debugging Ignition failures

[role="_abstract"]
If a machine cannot be provisioned, Ignition fails and {op-system} will boot into the emergency shell. Use the following procedure to get debugging information.

.Procedure

. Run the following command to show which service units failed:
+
[source,terminal]
----
$ systemctl --failed
----

. Optional: Run the following command on an individual service unit to find out more information:
+
[source,terminal]
----
$ journalctl -u <unit>.service
----
