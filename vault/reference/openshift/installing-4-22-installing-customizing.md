---
title: "Customizing nodes"
type: reference
domain: openshift
slug: installing-4-22-installing-customizing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-customizing
version: 4.22
family: installing
documentKind: "Documentation"
---

# Customizing nodes

[id="installing-customizing"]
= Customizing nodes

OpenShift Container Platform supports both cluster-wide and per-machine configuration via Ignition,
which allows arbitrary partitioning and file content changes to the operating system.
In general, if a configuration file is documented in {op-system-base-full}, then modifying
it via Ignition is supported.

There are two ways to deploy machine config changes:

* Creating machine configs that are included in manifest files
to start up a cluster during `openshift-install`.

* Creating machine configs that are passed to running
OpenShift Container Platform nodes via the Machine Config Operator.

Additionally, modifying the reference config, such as
the Ignition config that is passed to `coreos-installer` when installing bare-metal nodes
allows per-machine configuration. These changes are currently not visible
to the Machine Config Operator.

The following sections describe features that you might want to
configure on your nodes in this way.

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-butane_{context}"]
= Creating machine configs with Butane

Machine configs are used to configure control plane and worker machines by instructing machines how to create users and file systems, set up the network, install systemd units, and more.

Because modifying machine configs can be difficult, you can use Butane configs to create machine configs for you, thereby making node configuration much easier.

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-butane-about_{context}"]
= About Butane

Butane is a command-line utility that OpenShift Container Platform uses to provide convenient, short-hand syntax for writing machine configs, as well as for performing additional validation of machine configs. The format of the Butane config file that Butane accepts is defined in the
https://coreos.github.io/butane/specs/[OpenShift Butane config spec].

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-butane-install_{context}"]
= Installing Butane

You can install the Butane tool (`butane`) to create OpenShift Container Platform machine configs from a command-line interface. You can install `butane` on Linux, Windows, or macOS by downloading the corresponding binary file.

[TIP]
====
Butane releases are backwards-compatible with older releases and with the Fedora CoreOS Config Transpiler (FCCT).
====

.Procedure

. Navigate to the Butane image download page at https://mirror.openshift.com/pub/openshift-v4/clients/butane/.
. Get the `butane` binary:
.. For the newest version of Butane, save the latest `butane` image to your current directory:
+
[source,terminal]
----
$ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane --output butane
----
+
.. Optional: For a specific type of architecture you are installing Butane on, such as aarch64 or ppc64le, indicate the appropriate URL. For example:
+
[source,terminal]
----
$ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-aarch64 --output butane
----
+
. Make the downloaded binary file executable:
+
[source,terminal]
----
$ chmod +x butane
----
+
. Move the `butane` binary file to a directory on your `PATH`.
+
To check your `PATH`, open a terminal and execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification steps

* You can now use the Butane tool by running the `butane` command:
+
[source,terminal]
----
$ butane <butane_file>
----

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-butane-create_{context}"]
= Creating a MachineConfig object by using Butane

You can use Butane to produce a `MachineConfig` object so that you can configure worker or control plane nodes at installation time or via the Machine Config Operator.

.Prerequisites

* You have installed the `butane` utility.

.Procedure

. Create a Butane config file. The following example creates a file named `99-worker-custom.bu` that configures the system console to show kernel debug messages and specifies custom settings for the chrony time service:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 99-worker-custom
  labels:
    machineconfiguration.openshift.io/role: worker
openshift:
  kernel_arguments:
    - loglevel=7
storage:
  files:
    - path: /etc/chrony.conf
      mode: 0644
      overwrite: true
      contents:
        inline: |
          pool 0.rhel.pool.ntp.org iburst
          driftfile /var/lib/chrony/drift
          makestep 1.0 3
          rtcsync
          logdir /var/log/chrony
----
+
[NOTE]
====
The `99-worker-custom.bu` file is set to create a machine config for worker nodes. To deploy on control plane nodes, change the role from `worker` to `master`. To do both, you could repeat the whole procedure using different file names for the two types of deployments.
====

. Create a `MachineConfig` object by giving Butane the file that you created in the previous step:
+
[source,terminal]
----
$ butane 99-worker-custom.bu -o ./99-worker-custom.yaml
----
+
A `MachineConfig` object YAML file is created for you to finish configuring your machines.
. Save the Butane config in case you need to update the `MachineConfig` object in the future.
. If the cluster is not running yet, generate manifest files and add the `MachineConfig` object YAML file to the `openshift` directory. If the cluster is already running, apply the file as follows:
+
[source,terminal]
----
$ oc create -f 99-worker-custom.yaml
----

[role="_additional-resources"]
.Additional resources

* Adding kernel modules to nodes
* Encrypting and mirroring disks during installation

// Module included in the following assemblies:
//
// * installing/installing-special-config.adoc

[id="installation-special-config-kargs_{context}"]

= Adding day-1 kernel arguments

Although it is often preferable to modify kernel arguments as a day-2 activity,
you might want to add kernel arguments to all master or worker nodes during initial cluster
installation. Here are some reasons you might want
to add kernel arguments during cluster installation so they take effect before
the systems first boot up:

* You need to do some low-level network configuration before the systems start.

* You want to disable a feature, such as SELinux, so it has no impact on the systems when they first come up.
+
[WARNING]
====
Disabling SELinux on {op-system} in production is not supported.
Once SELinux has been disabled on a node, it must be re-provisioned before re-inclusion in a production cluster.
====

To add kernel arguments to master or worker nodes, you can create a `MachineConfig` object
and inject that object into the set of manifest files used by Ignition during
cluster setup.

For a listing of arguments you can pass to a RHEL 8 kernel at boot time, see
Kernel.org kernel parameters.
It is best to only add kernel arguments with this procedure if they are needed to complete the initial
OpenShift Container Platform installation.

.Procedure

. Change to the directory that contains the installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----

. Decide if you want to add kernel arguments to worker or control plane nodes.

. In the `openshift` directory, create a file (for example,
`99-openshift-machineconfig-master-kargs.yaml`) to define a `MachineConfig`
object to add the kernel settings.
This example adds a `loglevel=7` kernel argument to control plane nodes:
+
[source,terminal]
----
$ cat << EOF > 99-openshift-machineconfig-master-kargs.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 99-openshift-machineconfig-master-kargs
spec:
  kernelArguments:
    - loglevel=7
EOF
----
+
You can change `master` to `worker` to add kernel arguments to worker nodes instead.
Create a separate YAML file to add to both master and worker nodes.

You can now continue on to create the cluster.

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-rtkernel_{context}"]

= Adding a real-time kernel to nodes (during installation)

Some OpenShift Container Platform workloads require a high degree of determinism.
While Linux is not a real-time operating system, the Linux real-time
kernel includes a preemptive scheduler that provides the operating
system with real-time characteristics.

If your OpenShift Container Platform workloads require these real-time characteristics,
you can set up your compute (worker) and/or control plane machines to use the
Linux real-time kernel when you first install the cluster. To do this,
create a `MachineConfig` object and inject that object into the set of manifest
files used by Ignition during cluster setup, as described in the following
procedure.

[NOTE]
====
This procedure is fully supported with bare metal installations using
systems that are certified for Red Hat Enterprise Linux for Real Time 8.
Real time support in OpenShift Container Platform is also limited to specific subscriptions.
This procedure is also supported for use with {gcp-full}.
====

.Prerequisites
* For a bare metal installation of OpenShift Container Platform, prepare masters and workers.
* Use OpenShift Container Platform version 4.4 or later.

.Procedure

. Create the `intall-config.yaml` file using the installer or prepare it manually.
To create it using installer, run:
+
[source,terminal]
----
$ ./openshift-install create install-config --dir <installation_directory>
----

. Generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----

. Decide if you want to add the real-time kernel to worker or control plane nodes.

. In the `openshift` directory, create a file (for example,
`99-worker-realtime.yaml`) to define a `MachineConfig` object that applies a
real-time kernel to the selected nodes (worker nodes in this case):
+
[source,terminal]
----
$ cat << EOF > 99-worker-realtime.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: "worker"
  name: 99-worker-realtime
spec:
  kernelType: realtime
EOF
----
+
You can change `worker` to `master` to add kernel arguments to control plane nodes instead.
Create a separate YAML file to add to both master and worker nodes.

. Create the cluster.  You can now continue on to create the OpenShift Container Platform cluster.
+
[source,terminal]
----
$ ./openshift-install create cluster --dir <installation_directory>
----

. Check the real-time kernel: Once the cluster comes up, log in to the cluster
and run the following commands to make sure that the real-time kernel has
replaced the regular kernel for the set of worker or control plane nodes you
configured:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                        STATUS  ROLES    AGE   VERSION
ip-10-0-139-200.us-east-2.compute.internal  Ready   master   111m  v1.35.4
ip-10-0-143-147.us-east-2.compute.internal  Ready   worker   103m  v1.35.4
ip-10-0-146-92.us-east-2.compute.internal   Ready   worker   101m  v1.35.4
ip-10-0-156-255.us-east-2.compute.internal  Ready   master   111m  v1.35.4
ip-10-0-164-74.us-east-2.compute.internal   Ready   master   111m  v1.35.4
ip-10-0-169-2.us-east-2.compute.internal    Ready   worker   102m  v1.35.4
----
+
[source,terminal]
----
$ oc debug node/ip-10-0-143-147.us-east-2.compute.internal
----
+
.Example output
[source,terminal]
----
Starting pod/ip-10-0-143-147us-east-2computeinternal-debug ...
To use host binaries, run `chroot /host`
----
+
[source,terminal]
----
sh-4.4# uname -a
----
+
.Example output
[source,terminal]
----
Linux <worker_node> 4.22.0-147.3.1.rt24.96.el8_1.x86_64 #1 SMP PREEMPT RT
        Wed Feb 25 18:29:55 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
----
+
The kernel name contains `rt` and text `PREEMPT RT` indicates that this is a
real-time kernel.

// Module included in the following assemblies:
//
// * installing/installing-special-config.adoc

[id="installation-special-config-kmod_{context}"]
= Adding kernel modules to nodes

For most common hardware, the Linux kernel includes the device driver
modules needed to use that hardware when the computer starts up. For
some hardware, however, modules are not available in Linux. Therefore, you must
find a way to provide those modules to each host computer. This
procedure describes how to do that for nodes in an OpenShift Container Platform cluster.

When a kernel module is first deployed by following these instructions,
the module is made available for the current kernel. If a new kernel
is installed, the kmods-via-containers software will rebuild and deploy
the module so a compatible version of that module is available with the
new kernel.

The way that this feature is able to keep the module up to date on each
node is by:

* Adding a systemd service to each node that starts at boot time to detect
if a new kernel has been installed and
* If a new kernel is detected, the
service rebuilds the module and installs it to the kernel

For information on the software needed for this procedure, see the
kmods-via-containers github site.

A few important issues to keep in mind:

* This procedure is Technology Preview.
* Software tools and examples are not yet available in official RPM form
and can only be obtained for now from unofficial `github.com` sites noted in the procedure.
* Third-party kernel modules you might add through these procedures are not supported by Red Hat.
* In this procedure, the software needed to build your kernel modules is
deployed in a RHEL 8 container. Keep in mind that modules are rebuilt
automatically on each node when that node gets a new kernel. For that
reason, each node needs access to a `yum` repository that contains the
kernel and related packages needed to rebuild the module. That content
is best provided with a valid RHEL subscription.

[id="building-testing-kernel-module-container_{context}"]
== Building and testing the kernel module container

Before deploying kernel modules to your OpenShift Container Platform cluster,
you can test the process on a separate RHEL system.
Gather the kernel module's source code, the KVC framework, and the
kmod-via-containers software. Then build and test the module. To do
that on a RHEL 8 system, do the following:

.Procedure

. Register a RHEL 8 system:
+
[source,terminal]
----
# subscription-manager register
----

. Attach a subscription to the RHEL 8 system:
+
[source,terminal]
----
# subscription-manager attach --auto
----

. Install software that is required to build the software and container:
+
[source,terminal]
----
# yum install podman make git -y
----

. Clone the `kmod-via-containers` repository:
.. Create a folder for the repository:
+
[source,terminal]
----
$ mkdir kmods; cd kmods
----

.. Clone the repository:
+
[source,terminal]
----
$ git clone https://github.com/kmods-via-containers/kmods-via-containers
----

. Install a KVC framework instance on your RHEL 8 build host to test the module.
This adds a `kmods-via-container` systemd service and loads it:

.. Change to the `kmod-via-containers` directory:
+
[source,terminal]
----
$ cd kmods-via-containers/
----

.. Install the KVC framework instance:
+
[source,terminal]
----
$ sudo make install
----

.. Reload the systemd manager configuration:
+
[source,terminal]
----
$ sudo systemctl daemon-reload
----

. Get the kernel module source code. The source code might be used to
build a third-party module that you do not
have control over, but is supplied by others. You will need content
similar to the content shown in the `kvc-simple-kmod` example that can
be cloned to your system as follows:
+
[source,terminal]
----
$ cd .. ; git clone https://github.com/kmods-via-containers/kvc-simple-kmod
----

. Edit the configuration file, `simple-kmod.conf` file, in this example, and
change the name of the Dockerfile to `Dockerfile.rhel`:

.. Change to the `kvc-simple-kmod` directory:
+
[source,terminal]
----
$ cd kvc-simple-kmod
----

.. Rename the Dockerfile:
+
[source,terminal]
----
$ cat simple-kmod.conf
----
+
.Example Dockerfile
[source,terminal]
----
KMOD_CONTAINER_BUILD_CONTEXT="https://github.com/kmods-via-containers/kvc-simple-kmod.git"
KMOD_CONTAINER_BUILD_FILE=Dockerfile.rhel
KMOD_SOFTWARE_VERSION=dd1a7d4
KMOD_NAMES="simple-kmod simple-procfs-kmod"
----

. Create an instance of `kmods-via-containers@.service` for your kernel module,
`simple-kmod` in this example:
+
[source,terminal]
----
$ sudo make install
----

. Enable the `kmods-via-containers@.service` instance:
+
[source,terminal]
----
$ sudo kmods-via-containers build simple-kmod $(uname -r)
----

. Enable and start the systemd service:
+
[source,terminal]
----
$ sudo systemctl enable kmods-via-containers@simple-kmod.service --now
----

.. Review the service status:
+
[source,terminal]
----
$ sudo systemctl status kmods-via-containers@simple-kmod.service
----
+
.Example output
[source,terminal]
----
● kmods-via-containers@simple-kmod.service - Kmods Via Containers - simple-kmod
   Loaded: loaded (/etc/systemd/system/kmods-via-containers@.service;
          enabled; vendor preset: disabled)
   Active: active (exited) since Sun 2020-01-12 23:49:49 EST; 5s ago...
----

. To confirm that the kernel modules are loaded, use the `lsmod` command to list the modules:
+
[source,terminal]
----
$ lsmod | grep simple_
----
+
.Example output
[source,terminal]
----
simple_procfs_kmod     16384  0
simple_kmod            16384  0
----

. Optional. Use other methods to check that the `simple-kmod` example is working:
** Look for a "Hello world" message in the kernel ring buffer with `dmesg`:
+
[source,terminal]
----
$ dmesg | grep 'Hello world'
----
+
.Example output
[source,terminal]
----
[ 6420.761332] Hello world from simple_kmod.
----

** Check the value of `simple-procfs-kmod` in `/proc`:
+
[source,terminal]
----
$ sudo cat /proc/simple-procfs-kmod
----
+
.Example output
[source,terminal]
----
simple-procfs-kmod number = 0
----

** Run the `spkut` command to get more information from the module:
+
[source,terminal]
----
$ sudo spkut 44
----
+
.Example output
[source,terminal]
----
KVC: wrapper simple-kmod for 4.22.0-147.3.1.el8_1.x86_64
Running userspace wrapper using the kernel module container...
+ podman run -i --rm --privileged
   simple-kmod-dd1a7d4:4.22.0-147.3.1.el8_1.x86_64 spkut 44
simple-procfs-kmod number = 0
simple-procfs-kmod number = 44
----

Going forward, when the system boots this service will check if a new
kernel is running. If there is a new kernel, the service builds a new
version of the kernel module and then loads it. If the module is already
built, it will just load it.

[id="provisioning-kernel-module-to-ocp_{context}"]
== Provisioning a kernel module to OpenShift Container Platform

Depending on whether or not you must have the kernel module in place
when OpenShift Container Platform cluster first boots, you can set up the
kernel modules to be deployed in one of two ways:

* **Provision kernel modules at cluster install time (day-1)**:
You can create the content as a `MachineConfig` object and provide it to `openshift-install`
by including it with a set of manifest files.

* **Provision kernel modules via Machine Config Operator (day-2)**: If you can wait until the
cluster is up and running to add your kernel module, you can deploy the kernel
module software via the Machine Config Operator (MCO).

In either case, each node needs to be able to get the kernel packages and related
software packages at the time that a new kernel is detected. There are a few ways
you can set up each node to be able to obtain that content.

* Provide RHEL entitlements to each node.
* Get RHEL entitlements from an existing RHEL host, from the `/etc/pki/entitlement` directory
and copy them to the same location as the other files you provide
when you build your Ignition config.
* Inside the Dockerfile, add pointers to a `yum` repository containing the kernel and other packages.
This must include new kernel packages as they are needed to match newly installed kernels.

[id="provision-kernel-modules-via-machineconfig_{context}"]
=== Provision kernel modules via a MachineConfig object

By packaging kernel module software with a `MachineConfig` object, you can
deliver that software to worker or control plane nodes at installation time
or via the Machine Config Operator.

.Procedure

. Register a RHEL 8 system:
+
[source,terminal]
----
# subscription-manager register
----

. Attach a subscription to the RHEL 8 system:
+
[source,terminal]
----
# subscription-manager attach --auto
----

. Install software needed to build the software:
+
[source,terminal]
----
# yum install podman make git -y
----

. Create a directory to host the kernel module and tooling:
+
[source,terminal]
----
$ mkdir kmods; cd kmods
----

. Get the `kmods-via-containers` software:

.. Clone the `kmods-via-containers` repository:
+
[source,terminal]
----
$ git clone https://github.com/kmods-via-containers/kmods-via-containers
----

.. Clone the `kvc-simple-kmod` repository:
+
[source,terminal]
----
$ git clone https://github.com/kmods-via-containers/kvc-simple-kmod
----

. Get your module software. In this example, `kvc-simple-kmod` is used.

. Create a fakeroot directory and populate it with files that you want to
deliver via Ignition, using the repositories cloned earlier:

.. Create the directory:
+
[source,terminal]
----
$ FAKEROOT=$(mktemp -d)
----

.. Change to the `kmod-via-containers` directory:
+
[source,terminal]
----
$ cd kmods-via-containers
----

.. Install the KVC framework instance:
+
[source,terminal]
----
$ make install DESTDIR=${FAKEROOT}/usr/local CONFDIR=${FAKEROOT}/etc/
----

.. Change to the `kvc-simple-kmod` directory:
+
[source,terminal]
----
$ cd ../kvc-simple-kmod
----

.. Create the instance:
+
[source,terminal]
----
$ make install DESTDIR=${FAKEROOT}/usr/local CONFDIR=${FAKEROOT}/etc/
----

. Clone the fakeroot directory, replacing any symbolic links with copies of their targets, by running the following command:
+
[source,terminal]
----
$ cd .. && rm -rf kmod-tree && cp -Lpr ${FAKEROOT} kmod-tree
----

. Create a Butane config file, `99-simple-kmod.bu`, that embeds the kernel module tree and enables the systemd service.
+
[NOTE]
====
See "Creating machine configs with Butane" for information about Butane.
====
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 99-simple-kmod
  labels:
    machineconfiguration.openshift.io/role: worker <1>
storage:
  trees:
    - local: kmod-tree
systemd:
  units:
    - name: kmods-via-containers@simple-kmod.service
      enabled: true
----
+
<1> To deploy on control plane nodes, change `worker` to `master`.  To deploy on both control plane and worker nodes, perform the remainder of these instructions once for each node type.

. Use Butane to generate a machine config YAML file, `99-simple-kmod.yaml`, containing the files and configuration to be delivered:
+
[source,terminal]
----
$ butane 99-simple-kmod.bu --files-dir . -o 99-simple-kmod.yaml
----

. If the cluster is not up yet, generate manifest files and add this file to the
`openshift` directory. If the cluster is already running, apply the file as follows:
+
[source,terminal]
----
$ oc create -f 99-simple-kmod.yaml
----
+
Your nodes will start the `kmods-via-containers@simple-kmod.service`
service and the kernel modules will be loaded.

. To confirm that the kernel modules are loaded, you can log in to a node
(using `oc debug node/<openshift-node>`, then `chroot /host`).
To list the modules, use the `lsmod` command:
+
[source,terminal]
----
$ lsmod | grep simple_
----
+
.Example output
[source,terminal]
----
simple_procfs_kmod     16384  0
simple_kmod            16384  0
----

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-storage_{context}"]
= Encrypting and mirroring disks during installation

During an OpenShift Container Platform installation, you can enable boot disk encryption and mirroring on the cluster nodes.

[id="installation-special-config-encrypt-disk_{context}"]
== About disk encryption

You can enable encryption for the boot disks on the control plane and compute nodes at installation time.
OpenShift Container Platform supports the Trusted Platform Module (TPM) v2 and Tang encryption modes.

TPM v2:: This is the preferred mode.
TPM v2 stores passphrases in a secure cryptoprocessor on the server.
You can use this mode to prevent decryption of the boot disk data on a cluster node if the disk is removed from the server.
Tang:: Tang and Clevis are server and client components that enable network-bound disk encryption (NBDE).
You can bind the boot disk data on your cluster nodes to one or more Tang servers.
This prevents decryption of the data unless the nodes are on a secure network where the Tang servers are accessible.
Clevis is an automated decryption framework used to implement decryption on the client side.

[IMPORTANT]
====
The use of the Tang encryption mode to encrypt your disks is only supported for bare metal and vSphere installations on user-provisioned infrastructure.
====

In earlier versions of {op-system-first}, disk encryption was configured by specifying `/etc/clevis.json` in the Ignition config.
That file is not supported in clusters created with OpenShift Container Platform 4.7 or later.
Configure disk encryption by using the following procedure.

When the TPM v2 or Tang encryption modes are enabled, the {op-system} boot disks are encrypted using the LUKS2 format.

This feature:

* Is available for installer-provisioned infrastructure, user-provisioned infrastructure, and Assisted Installer deployments
  * For Assisted installer deployments:
    - Each cluster can only have a single encryption method, Tang or TPM
    - Encryption can be enabled on some or all nodes
    - There is no Tang threshold; all servers must be valid and operational
    - Encryption applies to the installation disks only, not to the workload disks
* Is supported on {op-system-first} systems only
* Sets up disk encryption during the manifest installation phase, encrypting all data written to disk, from first boot forward
* Requires no user intervention for providing passphrases
* Uses AES-256-XTS encryption

[id="installation-special-config-encryption-threshold_{context}"]
=== Configuring an encryption threshold

In OpenShift Container Platform, you can specify a requirement for more than one Tang server.
You can also configure the TPM v2 and Tang encryption modes simultaneously.
This enables boot disk data decryption only if the TPM secure cryptoprocessor is present and the Tang servers are accessible over a secure network.

You can use the `threshold` attribute in your Butane configuration to define the minimum number of TPM v2 and Tang encryption conditions required for decryption to occur.

The threshold is met when the stated value is reached through any combination of the declared conditions. In the case of offline provisioning, the offline server is accessed using an included advertisement, and only uses that supplied advertisement if the number of online servers do not meet the set threshold.

For example, the `threshold` value of `2` in the following configuration can be reached by accessing two Tang servers, with the offline server available as a backup, or by accessing the TPM secure cryptoprocessor and one of the Tang servers:

.Example Butane configuration for disk encryption

[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: worker-storage
  labels:
    machineconfiguration.openshift.io/role: worker
boot_device:
  layout: x86_64 <1>
  luks:
    tpm2: true <2>
    tang: <3>
      - url: http://tang1.example.com:7500
        thumbprint: jwGN5tRFK-kF6pIX89ssF3khxxX
      - url: http://tang2.example.com:7500
        thumbprint: VCJsvZFjBSIHSldw78rOrq7h2ZF
      - url: http://tang3.example.com:7500
        thumbprint: PLjNyRdGw03zlRoGjQYMahSZGu9
        advertisement: "{\"payload\": \"...\", \"protected\": \"...\", \"signature\": \"...\"}" <4>
    threshold: 2 <5>
openshift:
  fips: true
----
<1> Set this field to the instruction set architecture of the cluster nodes.
Some examples include, `x86_64`, `aarch64`, or `ppc64le`.
<2> Include this field if you want to use a Trusted Platform Module (TPM) to encrypt the root file system.
<3> Include this section if you want to use one or more Tang servers.
<4> Optional: Include this field for offline provisioning. Ignition will provision the Tang server binding rather than fetching the advertisement from the server at runtime. This lets the server be unavailable at provisioning time.
<5> Specify the minimum number of TPM v2 and Tang encryption conditions required for decryption to occur.

[IMPORTANT]
====
The default `threshold` value is `1`.
If you include multiple encryption conditions in your configuration but do not specify a threshold, decryption can occur if any of the conditions are met.
====

[NOTE]
====
If you require TPM v2 _and_ Tang for decryption, the value of the `threshold` attribute must equal the total number of stated Tang servers plus one.
If the `threshold` value is lower, it is possible to reach the threshold value by using a single encryption mode.
For example, if you set `tpm2` to `true` and specify two Tang servers, a threshold of `2` can be met by accessing the two Tang servers, even if the TPM secure cryptoprocessor is not available.
====

[id="installation-special-config-mirrored-disk_{context}"]
== About disk mirroring

During OpenShift Container Platform installation on control plane and worker nodes, you can enable mirroring of the boot and other disks to two or more redundant storage devices.
A node continues to function after storage device failure provided one device remains available.

Mirroring does not support replacement of a failed disk.
Reprovision the node to restore the mirror to a pristine, non-degraded state.

[NOTE]
====
For user-provisioned infrastructure deployments, mirroring is available only on {op-system} systems.
Support for mirroring is available on `x86_64` nodes booted with BIOS or UEFI and on `ppc64le` nodes.
====

[id="installation-special-config-storage-procedure_{context}"]
== Configuring disk encryption and mirroring

You can enable and configure encryption and mirroring during an OpenShift Container Platform installation.

.Prerequisites

* You have downloaded the OpenShift Container Platform installation program on your installation node.
* You installed Butane on your installation node.
+
[NOTE]
====
Butane is a command-line utility that OpenShift Container Platform uses to offer convenient, short-hand syntax for writing and validating machine configs.
For more information, see "Creating machine configs with Butane".
====
+
* You have access to a {op-system-base-full} 8 machine that can be used to generate a thumbprint of the Tang exchange key.

.Procedure

. If you want to use TPM v2 to encrypt your cluster, check to see if TPM v2 encryption needs to be enabled in the host firmware for each node.
This is required on most Dell systems.
Check the manual for your specific system.

. If you want to use Tang to encrypt your cluster, follow these preparatory steps:

.. Set up a Tang server or access an existing one.
See Network-bound disk encryption for instructions.

.. Install the `clevis` package on a {op-system-base} 8 machine, if it is not already installed:
+
[source,terminal]
----
$ sudo yum install clevis
----

.. On the {op-system-base} 8 machine, run the following command to generate a thumbprint of the exchange key.
Replace `\http://tang1.example.com:7500` with the URL of your Tang server:
+
[source,terminal]
----
$ clevis-encrypt-tang '{"url":"http://tang1.example.com:7500"}' < /dev/null > /dev/null <1>
----
<1> In this example, `tangd.socket` is listening on port `7500` on the Tang server.
+
[NOTE]
====
The `clevis-encrypt-tang` command generates a thumbprint of the exchange key.
No data passes to the encryption command during this step; `/dev/null` exists here as an input instead of plain text.
The encrypted output is also sent to `/dev/null`, because it is not required for this procedure.
====
+
.Example output
[source,terminal]
----
The advertisement contains the following signing keys:

PLjNyRdGw03zlRoGjQYMahSZGu9 <1>
----
<1> The thumbprint of the exchange key.
+
When the `Do you wish to trust these keys? [ynYN]` prompt displays, type `Y`.

.. Optional: For offline Tang provisioning:

... Obtain the advertisement from the server using the `curl` command. Replace `\http://tang2.example.com:7500` with the URL of your Tang server:
+
[source,terminal]
----
$ curl -f http://tang2.example.com:7500/adv > adv.jws && cat adv.jws
----
+
.Expected output
[source,text]
----
{"payload": "eyJrZXlzIjogW3siYWxnIjogIkV", "protected": "eyJhbGciOiJFUzUxMiIsImN0eSI", "signature": "ADLgk7fZdE3Yt4FyYsm0pHiau7Q"}
----

... Provide the advertisement file to Clevis for encryption:
+
[source,terminal]
----
$ clevis-encrypt-tang '{"url":"http://tang2.example.com:7500","adv":"adv.jws"}' < /dev/null > /dev/null
----

.. If the nodes are configured with static IP addressing, run `coreos-installer iso customize --dest-karg-append` or use the `coreos-installer` `--append-karg` option when installing {op-system} nodes to set the IP address of the installed system.
Append the `ip=` and other arguments needed for your network.
+
[IMPORTANT]
====
Some methods for configuring static IPs do not affect the initramfs after the first boot and will not work with Tang encryption.
These include the `coreos-installer` `--copy-network` option, the `coreos-installer iso customize` `--network-keyfile` option, and the `coreos-installer pxe customize` `--network-keyfile` option, as well as adding `ip=` arguments to the kernel command line of the live ISO or PXE image during installation.
Incorrect static IP configuration causes the second boot of the node to fail.
====

. On your installation node, change to the directory that contains the installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory> <1>
----
<1> Replace `<installation_directory>` with the path to the directory that you want to store the installation files in.

. Create a Butane config that configures disk encryption, mirroring, or both.
For example, to configure storage for compute nodes, create a `$HOME/clusterconfig/worker-storage.bu` file.
+
[source,yaml,subs="attributes+"]
.Butane config example for a boot device
----
variant: openshift
version: .0
metadata:
  name: worker-storage <1>
  labels:
    machineconfiguration.openshift.io/role: worker <1>
boot_device:
  layout: x86_64 <2>
  luks: <3>
    tpm2: true <4>
    tang: <5>
      - url: http://tang1.example.com:7500 <6>
        thumbprint: PLjNyRdGw03zlRoGjQYMahSZGu9 <7>
      - url: http://tang2.example.com:7500
        thumbprint: VCJsvZFjBSIHSldw78rOrq7h2ZF
        advertisement: "{"payload": "eyJrZXlzIjogW3siYWxnIjogIkV", "protected": "eyJhbGciOiJFUzUxMiIsImN0eSI", "signature": "ADLgk7fZdE3Yt4FyYsm0pHiau7Q"}" <8>
    threshold: 1 <9>
  mirror: <10>
    devices: <11>
      - /dev/sda
      - /dev/sdb
openshift:
  fips: true <12>
----
+
<1> For control plane configurations, replace `worker` with `master` in both of these locations.
<2> Set this field to the instruction set architecture of the cluster nodes.
Some examples include, `x86_64`, `aarch64`, or `ppc64le`.
<3> Include this section if you want to encrypt the root file system.
For more details, see "About disk encryption".
<4> Include this field if you want to use a Trusted Platform Module (TPM) to encrypt the root file system.
<5> Include this section if you want to use one or more Tang servers.
<6> Specify the URL of a Tang server.
In this example, `tangd.socket` is listening on port `7500` on the Tang server.
<7> Specify the exchange key thumbprint, which was generated in a preceding step.
<8> Optional: Specify the advertisement for your offline Tang server in valid JSON format.
<9> Specify the minimum number of TPM v2 and Tang encryption conditions that must be met for decryption to occur.
The default value is `1`.
For more information about this topic, see "Configuring an encryption threshold".
<10> Include this section if you want to mirror the boot disk.
For more details, see "About disk mirroring".
<11> List all disk devices that should be included in the boot disk mirror, including the disk that {op-system} will be installed onto.
<12> Include this directive to enable FIPS mode on your cluster.
+
[IMPORTANT]
====
To enable FIPS mode for your cluster, you must run the installation program from a {op-system-base-full} computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see Installing the system in FIPS mode. If you are configuring nodes to use both disk encryption and mirroring, both features must be configured in the same Butane configuration file.
If you are configuring disk encryption on a node with FIPS mode enabled, you must include the `fips` directive in the same Butane configuration file, even if FIPS mode is also enabled in a separate manifest.
====

. Create a control plane or compute node manifest from the corresponding Butane configuration file and save it to the `<installation_directory>/openshift` directory.
For example, to create a manifest for the compute nodes, run the following command:
+
[source,terminal]
----
$ butane $HOME/clusterconfig/worker-storage.bu -o <installation_directory>/openshift/99-worker-storage.yaml
----
+
Repeat this step for each node type that requires disk encryption or mirroring.

. If you enable encryption, edit the manifest that was produced by the previous step and replace the cipher `aes-cbc-essiv:sha256` with `aes-xts-plain64`.
The following excerpt shows a sample encryption configuration after this change:
+
[source,yaml]
----
# ...
        luks:
# ...
          options:
            - --cipher
            - aes-xts-plain64
----

. Save the Butane configuration file in case you need to update the manifests in the future.

. Continue with the remainder of the OpenShift Container Platform installation.
+
[TIP]
====
You can monitor the console log on the {op-system} nodes during installation for error messages relating to disk encryption or mirroring.
====
+
[IMPORTANT]
====
If you configure additional data partitions, they will not be encrypted unless encryption is explicitly requested.
====

.Verification

After installing OpenShift Container Platform, you can verify if boot disk encryption or mirroring is enabled on the cluster nodes.

. From the installation host, access a cluster node by using a debug pod:
.. Start a debug pod for the node, for example:
+
[source,terminal]
----
$ oc debug node/compute-1
----
+
.. Set `/host` as the root directory within the debug shell.
The debug pod mounts the root file system of the node in `/host` within the pod.
By changing the root directory to `/host`, you can run binaries contained in the executable paths on the node:
+
[source,terminal]
----
# chroot /host
----
+
[NOTE]
====
OpenShift Container Platform cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes.
Accessing cluster nodes using SSH is not recommended.
However, if the OpenShift Container Platform API is not available, or `kubelet` is not properly functioning on the target node, `oc` operations will be impacted.
In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.
====

. If you configured boot disk encryption, verify if it is enabled:
.. From the debug shell, review the status of the root mapping on the node:
+
[source,terminal]
----
# cryptsetup status root
----
+
.Example output
[source,terminal]
----
/dev/mapper/root is active and is in use.
  type:    LUKS2 <1>
  cipher:  aes-xts-plain64 <2>
  keysize: 512 bits
  key location: keyring
  device:  /dev/sda4 <3>
  sector size:  512
  offset:  32768 sectors
  size:    15683456 sectors
  mode:    read/write
----
<1> The encryption format.
When the TPM v2 or Tang encryption modes are enabled, the {op-system} boot disks are encrypted using the LUKS2 format.
<2> The encryption algorithm used to encrypt the LUKS2 volume.
<3> The device that contains the encrypted LUKS2 volume.
If mirroring is enabled, the value will represent a software mirror device, for example `/dev/md126`.
+
.. List the Clevis plugins that are bound to the encrypted device:
+
[source,terminal]
----
# clevis luks list -d /dev/sda4 <1>
----
<1> Specify the device that is listed in the `device` field in the output of the preceding step.
+
.Example output
[source,terminal]
----
1: sss '{"t":1,"pins":{"tang":[{"url":"http://tang.example.com:7500"}]}}' <1>
----
<1> In the example output, the Tang plugin is used by the Shamir's Secret Sharing (SSS) Clevis plugin for the `/dev/sda4` device.

. If you configured mirroring, verify if it is enabled:
.. From the debug shell, list the software RAID devices on the node:
+
[source,terminal]
----
# cat /proc/mdstat
----
+
.Example output
[source,terminal]
----
Personalities : [raid1]
md126 : active raid1 sdb3[1] sda3[0] <1>
	  393152 blocks super 1.0 [2/2] [UU]

md127 : active raid1 sda4[0] sdb4[1] <2>
	  51869632 blocks super 1.2 [2/2] [UU]

unused devices: <none>
----
<1> The `/dev/md126` software RAID mirror device uses the `/dev/sda3` and `/dev/sdb3` disk devices on the cluster node.
<2> The `/dev/md127` software RAID mirror device uses the `/dev/sda4` and `/dev/sdb4` disk devices on the cluster node.
+
.. Review the details of each of the software RAID devices listed in the output of the preceding command.
The following example lists the details of the `/dev/md126` device:
+
[source,terminal]
----
# mdadm --detail /dev/md126
----
+
.Example output
[source,terminal]
----
/dev/md126:
           Version : 1.0
     Creation Time : Wed Jul  7 11:07:36 2021
        Raid Level : raid1 <1>
        Array Size : 393152 (383.94 MiB 402.59 MB)
     Used Dev Size : 393152 (383.94 MiB 402.59 MB)
      Raid Devices : 2
     Total Devices : 2
       Persistence : Superblock is persistent

       Update Time : Wed Jul  7 11:18:24 2021
             State : clean <2>
    Active Devices : 2 <3>
   Working Devices : 2 <3>
    Failed Devices : 0 <4>
     Spare Devices : 0

Consistency Policy : resync

              Name : any:md-boot <5>
              UUID : ccfa3801:c520e0b5:2bee2755:69043055
            Events : 19

    Number   Major   Minor   RaidDevice State
       0     252        3        0      active sync   /dev/sda3 <6>
       1     252       19        1      active sync   /dev/sdb3 <6>
----
<1> Specifies the RAID level of the device.
`raid1` indicates RAID 1 disk mirroring.
<2> Specifies the state of the RAID device.
<3> States the number of underlying disk devices that are active and working.
<4> States the number of underlying disk devices that are in a failed state.
<5> The name of the software RAID device.
<6> Provides information about the underlying disk devices used by the software RAID device.
+
.. List the file systems mounted on the software RAID devices:
+
[source,terminal]
----
# mount | grep /dev/md
----
+
.Example output
[source,terminal]
----
/dev/md127 on / type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /etc type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /usr type xfs (ro,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /sysroot type xfs (ro,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /var type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /var/lib/containers/storage/overlay type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/1 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/2 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/3 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/4 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/5 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
/dev/md126 on /boot type ext4 (rw,relatime,seclabel)
----
+
In the example output, the `/boot` file system is mounted on the `/dev/md126` software RAID device and the root file system is mounted on `/dev/md127`.

. Repeat the verification steps for each OpenShift Container Platform node type.

[role="_additional-resources"]
.Additional resources

* For more information about the TPM v2 and Tang encryption modes, see Configuring automated unlocking of encrypted volumes using policy-based decryption.

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-raid_{context}"]
= Configuring a RAID-enabled data volume

[role="_abstract"]
You can enable software Redundant Array of Independent Disks (RAID) partitioning to provide an external data volume.

OpenShift Container Platform supports RAID 0, RAID 1, RAID 4, RAID 5, RAID 6, and RAID 10 for data protection and fault tolerance. See "About disk mirroring" for more details.

[NOTE]
====
OpenShift Container Platform  supports manually configuring a hybrid RAID on an installation drive. For a manually configured example, see "Configuring an Intel(R) Virtual RAID on CPU (VROC) data volume".
====

.Prerequisites

* You have downloaded the OpenShift Container Platform installation program on your installation node.
* You have installed Butane on your installation node.
+
[NOTE]
====
Butane is a command-line utility that OpenShift Container Platform uses to write machine configs. The utility provides convenient, short-hand syntax for writing machine configs and for performing additional validation of machine configs. For more information, see the _Creating machine configs with Butane_ section.
====

.Procedure

. Create a Butane config that configures a data volume by using software RAID.

* To configure a data volume with RAID 1 on the same disks that are used for a mirrored boot disk, create a `$HOME/clusterconfig/raid1-storage.bu` file:
+
.Example configuration for RAID 1 on a mirrored boot disk
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: raid1-storage
  labels:
    machineconfiguration.openshift.io/role: worker
boot_device:
  mirror:
    devices:
      - /dev/disk/by-id/scsi-3600508b400105e210000900000490000
      - /dev/disk/by-id/scsi-SSEAGATE_ST373453LW_3HW1RHM6
storage:
  disks:
    - device: /dev/disk/by-id/scsi-3600508b400105e210000900000490000
      partitions:
        - label: root-1
          size_mib: 25000
        - label: var-1
    - device: /dev/disk/by-id/scsi-SSEAGATE_ST373453LW_3HW1RHM6
      partitions:
        - label: root-2
          size_mib: 25000
        - label: var-2
  raid:
    - name: md-var
      level: raid1
      devices:
        - /dev/disk/by-partlabel/var-1
        - /dev/disk/by-partlabel/var-2
  filesystems:
    - device: /dev/md/md-var
      path: /var
      format: xfs
      wipe_filesystem: true
      with_mount_unit: true
# ...
----
+
The `size_mib` field adds a data partition to the boot disk. A minimum value of 25000 mebibytes is recommended. If no value is specified or the specified value is smaller than the recommended minimum, the resulting root file system will be too small. Future reinstalls of {op-system} might overwrite the beginning of the data partition.

* To configure a data volume with RAID 1 on secondary disks, create a `$HOME/clusterconfig/raid1-alt-storage.bu` file:
+
.Example configuration for RAID 1 on secondary disks
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: raid1-alt-storage
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  disks:
    - device: /dev/sdc
      wipe_table: true
      partitions:
        - label: data-1
    - device: /dev/sdd
      wipe_table: true
      partitions:
        - label: data-2
  raid:
    - name: md-var-lib-containers
      level: raid1
      devices:
        - /dev/disk/by-partlabel/data-1
        - /dev/disk/by-partlabel/data-2
  filesystems:
    - device: /dev/md/md-var-lib-containers
      path: /var/lib/containers
      format: xfs
      wipe_filesystem: true
      with_mount_unit: true
# ...
----

. Create a RAID manifest from the Butane config. Save the config to the `<installation_directory>/openshift` directory. For example, to create a manifest for the compute nodes, run the following command:
+
[source,terminal]
----
$ butane $HOME/clusterconfig/<butane_config>.bu -o <installation_directory>/openshift/<manifest_name>.yaml
----
+
Replace the `<manifest_name>` and `<butane_config>` values with the file names from a previous step. For example, `raid1-alt-storage.bu` and `raid1-alt-storage.yaml` for secondary disks.

. Save the Butane config in case you need to update the manifest in the future.

. Continue with the remainder of the OpenShift Container Platform installation.

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc

[id="installation-special-config-raid-intel-vroc_{context}"]
== Configuring an Intel(R) Virtual RAID on CPU (VROC) data volume

Intel(R) VROC is a type of hybrid RAID, where some of the maintenance is offloaded to the hardware, but appears as software RAID to the operating system.

The following procedure configures an Intel(R) VROC-enabled RAID1.

.Prerequisites

* You have a system with Intel(R) Volume Management Device (VMD) enabled.

.Procedure

. Create the Intel(R) Matrix Storage Manager (IMSM) RAID container by running the following command:
+
[source,terminal]
----
$ mdadm -CR /dev/md/imsm0 -e \
  imsm -n2 /dev/nvme0n1 /dev/nvme1n1 <1>
----
<1> The RAID device names. In this example, there are two devices listed. If you provide more than two device names, you must adjust the `-n` flag. For example, listing three devices would use the flag `-n3`.

. Create the RAID1 storage inside the container:

.. Create a dummy RAID0 volume in front of the real RAID1 volume by running the following command:
+
[source,terminal]
----
$ mdadm -CR /dev/md/dummy -l0 -n2 /dev/md/imsm0 -z10M --assume-clean
----

.. Create the real RAID1 array by running the following command:
+
[source,terminal]
----
$ mdadm -CR /dev/md/coreos -l1 -n2 /dev/md/imsm0
----

.. Stop both RAID0 and RAID1 member arrays and delete the dummy RAID0 array with the following commands:
+
[source,terminal]
----
$ mdadm -S /dev/md/dummy \
  mdadm -S /dev/md/coreos \
  mdadm --kill-subarray=0 /dev/md/imsm0
----

.. Restart the RAID1 arrays by running the following command:
+
[source,terminal]
----
$ mdadm -A /dev/md/coreos /dev/md/imsm0
----

. Install {op-system} on the RAID1 device:

.. Get the UUID of the IMSM container by running the following command:
+
[source,terminal]
----
$ mdadm --detail --export /dev/md/imsm0
----

.. Install {op-system} and include the `rd.md.uuid` kernel argument by running the following command:
+
[source,terminal]
----
$ coreos-installer install /dev/md/coreos \
  --append-karg rd.md.uuid=<md_UUID> <1>
  ...
----
<1> The UUID of the IMSM container.
+
Include any additional `coreos-installer` arguments you need to install {op-system}.

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * machine_configuration/machine-configs-configure.adoc

[id="installation-special-config-chrony_{context}"]
= Configuring chrony time service

[role="_abstract"]
You
set the time server and related settings used by the chrony time service (`chronyd`)
by modifying the contents of the `chrony.conf` file and passing those contents
to your nodes as a machine config.

.Procedure

. Create a Butane config including the contents of the `chrony.conf` file. For example, to configure chrony on worker nodes, create a `99-worker-chrony.bu` file.
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
  name: 99-worker-chrony
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  files:
  - path: /etc/chrony.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        pool 0.rhel.pool.ntp.org iburst
        driftfile /var/lib/chrony/drift
        makestep 1.0 3
        rtcsync
        logdir /var/log/chrony
----
+
--
* `name: 99-worker-chrony` - Specify a name for the machine config file. On control plane nodes, substitute `master` for `worker`.
* `machineconfiguration.openshift.io/role: worker` - On control plane nodes, substitute `master` for `worker`.
* `mode: 0644` - Specify an octal value mode for the `mode` field in the machine config file. After creating the file and applying the changes, the `mode` is converted to a decimal value. You can check the YAML file with the command `oc get mc <mc-name> -o yaml`.
* `pool 0.rhel.pool.ntp.org iburst` - Specify any valid, reachable time source, such as the one provided by your DHCP server.
--

+
[NOTE]
====
For all-machine to all-machine communication, the Network Time Protocol (NTP) on UDP is port `123`. If an external NTP time server is configured, you must open UDP port `123`.
====

. Use Butane to generate a `MachineConfig` object file, `99-worker-chrony.yaml`, containing the configuration to be delivered to the nodes:
+
[source,terminal]
----
$ butane 99-worker-chrony.bu -o 99-worker-chrony.yaml
----

. Apply the configurations in one of two ways:
+
* If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
+
* If the cluster is already running, apply the file:
+
[source,terminal]
----
$ oc apply -f ./99-worker-chrony.yaml
----

For more information on chrony best practices, see the following resources:

* https://access.redhat.com/solutions/3073261[Configuring chrony]
* https://access.redhat.com/solutions/778603[Best practices for NTP]
* https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/troubleshooting_guide/basic-chrony-NTP-troubleshooting_diag#basic-chrony-NTP-troubleshooting_diag[Basic chrony NTP troubleshooting]

[role="_additional-resources"]
== Additional resources

* For information on Butane, see Creating machine configs with Butane.

* For information on FIPS support, see Support for FIPS cryptography.
