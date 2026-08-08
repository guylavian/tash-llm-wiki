---
title: "Configuring low latency"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-low-latency
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-low-latency
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Configuring low latency

[id="microshift-low-latency"]
= Configuring low latency

[role="_abstract"]
You can configure and tune low latency capabilities to improve application performance on edge devices.

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-concept_{context}"]
= Lowering latency in {microshift-short} applications

[role="_abstract"]
Latency is the time from an event to its response. You can optimize low latency performance on a {microshift-short} node by combining configurations, operating system tuning, and workload partitioning to ensure edge devices respond quickly.

[IMPORTANT]
====
The CPU set for management applications, such as the {microshift-short} service, OVS, CRI-O, {microshift-short} pods, and isolated cores, must contain all-online CPUs.
====

[id="microshift-low-latency-workflow_{context}"]
== Workflow for configuring low latency for {microshift-short} applications
To configure low latency for applications running in a {microshift-short} node, you must complete the following tasks:

Required::
* Install the `microshift-low-latency` RPM.
* Configure workload partitioning.
* Configure the `kubelet` section of the `config.yaml` file in the `/etc/microshift/` directory.
* Configure and activate a TuneD profile. TuneD is a {op-system-base-full} service that monitors the host system and optimizes performance under certain workloads.
* Restart the host.

Optional::
* If you are using the x86_64 architecture, you can install Red Hat Enterprise Linux for Real Time 9.

//additional resources for the low latency concept
[role="_additional-resources"]
.Additional resources
* About low latency ({OCP} documentation)

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-installing-low-latency-rpm-package_{context}"]
= Installing the {microshift-short} low latency RPM package

[role="_abstract"]
When you install {microshift-short}, the low latency RPM package is not installed by default. You can install the low latency RPM as an optional package.

.Prerequisites

* You installed the {microshift-short} RPM.
* You configured workload partitioning for {microshift-short}.

.Procedure

* Install the low latency RPM package by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y microshift-low-latency
----
+
[TIP]
====
Wait to restart the host until after activating your TuneD profile. Restarting the host restarts {microshift-short} and CRI-O, which applies the low latency manifests and activates the TuneD profile.
====

.Next steps
. Configure the kubelet parameter for low latency in the {microshift-short} `config.yaml`.
. Tune your operating system, for example, configure and activate a TuneD profile.
. Optional: Configure automatic activation of your TuneD profile.
. Optional: If you are using the x86_64 architecture, install {op-system-rt-kernel}.
. Prepare your workloads for low latency.

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-config-yaml_{context}"]
= Configuring kubelet parameters and values in {microshift-short}

[role="_abstract"]
To enable low latency on a {microshift-short} node, add the required settings to the {microshift-short} `config.yaml` file.

.Prerequisites

* You installed the {oc-first}.
* You have root access to the node.
* You made a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory, and renamed it `config.yaml`.

.Procedure

* Add the kubelet configuration to the {microshift-short} `config.yaml` file:
+
.Example passthrough `kubelet` configuration
[source,yaml]
----
apiServer:
# ...
kubelet:
  cpuManagerPolicy: static
  cpuManagerPolicyOptions:
    full-pcpus-only: "true"
  cpuManagerReconcilePeriod: 5s
  memoryManagerPolicy: Static
  topologyManagerPolicy: single-numa-node
  reservedSystemCPUs: 0-1
  reservedMemory:
  - limits:
      memory: 1100Mi
    numaNode: 0
  kubeReserved:
    memory: 500Mi
  systemReserved:
    memory: 500Mi
  evictionHard:
    imagefs.available: "15%"
    memory.available: "100Mi"
    nodefs.available: "10%"
    nodefs.inodesFree: "5%"
  evictionPressureTransitionPeriod: 5m
# ...
----
+
`kubelet`:: If you change the CPU or memory managers in the kubelet configuration, you must remove files that cache the previous configuration. Restart the host to remove them automatically, or manually remove the `/var/lib/kubelet/cpu_manager_state` and `/var/lib/kubelet/memory_manager_state` files.
`kubelet.cpuManagerPolicy`:: The name of the policy to use. Valid values are `none` and `static`. Requires the `CPUManager` feature gate to be enabled. Default value is `none`.
`kubelet.cpuManagerPolicyOptions.full-pcpus-only`:: A set of `key=value` pairs for setting extra options that fine tune the behavior of the `CPUManager` policies. The default value is `null`. Requires both the `CPUManager` and `CPUManagerPolicyOptions` feature gates to be enabled.
`kubelet.memoryManagerPolicy`:: The name of the policy used by Memory Manager. Case-sensitive. The default value is `none`. Requires the `MemoryManager` feature gate to be enabled.
`kubelet.reservedSystemCPUs`:: Required. The `reservedSystemCPUs` value must be the inverse of the offlined CPUs because both values combined must account for all of the CPUs on the system. This parameter is essential to dividing the management and application workloads. Use this parameter to define a static CPU set for the host-level system and Kubernetes daemons, plus interrupts and timers. Then the rest of the CPUs on the system can be used exclusively for workloads.
`kubelet.reservedMemory[0].limits.memory`:: The value in `reservedMemory[0].limits.memory`, `1100` Mi in this example, is equal to `kubeReserved.memory` + `systemReserved.memory` + `evictionHard.memory.available`.
`kubelet.evictionHard`:: The `evictionHard` parameters define under which conditions the kubelet evicts pods. When you change the default value of only one parameter for the `evictionHard` stanza, the default values of other parameters are not inherited and are set to zero. Provide all the threshold values even when you want to change just one.
`kubelet.evictionHard.imagefs.available`:: The `imagefs` is a filesystem that container runtimes use to store container images and container writable layers. In this example, the `evictionHard.imagefs.available` parameter means that the pod is evicted when the available space of the image filesystem is less than 15%.
`kubelet.evictionHard.memory.available`:: In this example, the `evictionHard.memory.available` parameter means that the pods are evicted when the available memory of the node drops below 100MiB.
`kubelet.evictionHard.nodefs.available`:: In this example, the `evictionHard.nodefs.available` parameter means that the pods are evicted when the main filesystem of the node has less than 10% available space.
`kubelet.evictionHard.nodefs.inodesFree`:: In this example, the `evictionHard.nodefs.inodesFree` parameter means that the pods are evicted when more than 15% of the node's main filesystem's inodes are in use.
`kubelet.evictionPressureTransitionPeriod`:: For container garbage collection: The duration to wait before transitioning out of an eviction pressure condition. Setting the `evictionPressureTransitionPeriod` parameter to `0` configures the default value of 5 minutes.

.Verification

* After you complete the next steps and restart the host, you can use a root-access account to check that your settings are in the `config.yaml` file in the `/var/lib/microshift/resources/kubelet/config/` directory.

.Next steps
. Enable workload partitioning.
. Tune your operating system. For example, configure and activate a TuneD profile.
. Optional: Configure automatic enablement of your TuneD profile.
. Optional: If you are using the x86_64 architecture, you can install {op-system-rt-kernel}.
. Prepare your {microshift-short} workloads for low latency.

//additional resources for the config.yaml
[role="_additional-resources"]
.Additional resources
* Customizing {microshift-short} by using the configuration file
* KubeletConfiguration reference (Kubernetes upstream documentation)

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-llc-enable_{context}"]
= Enabling last-level cache locality in {microshift-short}

[role="_abstract"]
You can align workloads with CPU cores that share the same last-level cache (LLC) to improve performance for latency-sensitive applications. To apply this alignment, enable the Kubernetes CPU Manager option `prefer-align-cpus-by-uncorecache`.

[WARNING]
====
This feature is part of a feature gate. After you enable feature gates, you cannot disable them or update {product-title-first}, and your cluster can become unstable or lose data. Enable feature gates only in non-production environments.
====

.Procedure

. Add the following content to `/etc/microshift/config.yaml`. If you already have a `kubelet` section from the earlier section, merge the `cpuManagerPolicyOptions` entry and ensure the feature gate is present.
+
[source,yaml]
----
apiServer:
  featureGates:
    featureSet: "CustomNoUpgrade"
    customNoUpgrade:
      enabled:
      - "CPUManagerPolicyBetaOptions"
kubelet:
  reservedSystemCPUs: "0"
  cpuManagerPolicy: static
  cpuManagerPolicyOptions:
    prefer-align-cpus-by-uncorecache: "true"
----

. To apply the configuration, restart {microshift-short} by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo systemctl restart microshift
----

//additional resources for LLC locality
[role="_additional-resources"]
.Additional resources
* Control CPU Management Policies on the Node - Static policy options (Kubernetes documentation)
* Configuration kubelet parameters and values in {microshift-short}
* Using feature gates for {microshift-short}

//RHEL TuneD
// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-tuned-conc_{context}"]
= Tuning Red Hat Enterprise Linux 9

[role="_abstract"]
As a {op-system-base-full} system administrator, you can use the TuneD service to optimize the performance profile of {op-system-base} for a variety of use cases. TuneD monitors and optimizes system performance under certain workloads, including latency performance.

* Use TuneD profiles to tune your system for different use cases, such as deploying a low-latency {microshift-short} node.
* You can modify the rules defined for each profile and customize tuning for a specific device.
* When you switch to another profile or deactivate TuneD, all changes made to the system settings by the previous profile revert back to their original state.
* You can also configure TuneD to react to changes in device usage and adjusts settings to improve performance of active devices and reduce power consumption of inactive devices.

//microshift-baseline is the name of the profile and used for automatic activation settings
//microshift-baseline-variables.conf is the file for user tweaks
// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-tuned-profile_{context}"]
= Configuring the {microshift-short} TuneD profile

[role="_abstract"]
To use low latency with {microshift-short} workloads, configure a TuneD profile for your host by using the `microshift-baseline-variables.conf` file provided in the `/etc/tuned/` directory.

.Prerequisites

* You have root access to the node.
* You installed the `microshift-low-latency` RPM package.
* Your {op-system-base} host has TuneD installed. See Getting started with TuneD (RHEL documentation).

.Procedure

. You can use the default `microshift-baseline-variables.conf` TuneD profile in the `/etc/tuned/` directory profile, or create your own to add more tunings.
+
.Example `microshift-baseline-variables.conf` TuneD profile
[source,text]
----
# Isolate cores 2-7 for running application workloads
isolated_cores=2-7

# Size of the hugepages
hugepages_size=2M

# Number of hugepages
hugepages=0

# Additional kernel arguments
additional_args=

# CPU set to be offlined
offline_cpu_set=
----
+
--
`isolated_cores`:: Controls which cores should be isolated. By default, 1 core per socket is reserved in {microshift-short} for housekeeping. The other cores are isolated. Valid values are a core list or range. You can isolate any range, for example: `isolated_cores=2,4-7` or `isolated_cores=2-23`.
+
[IMPORTANT]
====
You must keep only one `isolated_cores=` variable.
====
+
[NOTE]
====
The Kubernetes CPU manager can use any CPU to run the workload except the reserved CPUs defined in the kubelet configuration. For this reason it is best that:

* The sum of the kubelet's reserved CPUs and isolated cores include all online CPUs.
* Isolated cores are complementary to the reserved CPUs defined in the kubelet configuration.
====

`hugepages_size`:: Size of the hugepages. Valid values are 2M or 1G.

`additional_args`:: Additional kernel arguments, for example, `additional_args=console=tty0 console=ttyS0,115200`.

`offline_cpu_set`:: The CPU set to be offlined.
+
[IMPORTANT]
====
Must not overlap with `isolated_cores`.
====
--

. Enable the profile or make changes active, by running the following command:
+
[source,terminal]
----
$ sudo tuned-adm profile microshift-baseline
----

. Reboot the host to make kernel arguments active.

.Verification

* Optional: You can read the `/proc/cmdline` file that contains the arguments given to the currently running kernel on start.
+
[source,terminal]
----
$ cat /proc/cmdline
----
+
.Example output
[source,text]
----
BOOT_IMAGE=(hd0,msdos2)/ostree/rhel-7f82ccd9595c3c70af16525470e32c6a81c9138c4eae6c79ab86d5a2d108d7fc/vmlinuz-5.14.0-427.31.1.el9_4.x86_64+rt crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M rd.lvm.lv=rhel/root fips=0 console=ttyS0,115200n8 root=/dev/mapper/rhel-root rw ostree=/ostree/boot.1/rhel/7f82ccd9595c3c70af16525470e32c6a81c9138c4eae6c79ab86d5a2d108d7fc/0 skew_tick=1 tsc=reliable rcupdate.rcu_normal_after_boot=1 nohz=on nohz_full=2,4-5 rcu_nocbs=2,4-5 tuned.non_isolcpus=0000000b intel_pstate=disable nosoftlockup hugepagesz=2M hugepages=10
----

.Next steps
. Prepare your {microshift-short} workloads for low latency.
. Optional: Configure automatic enablement of your TuneD profile.
. Optional: If you are using the x86_64 architecture, you can install {op-system-rt-kernel}.

//additional resources for tuned profiles
[role="_additional-resources"]
[id="additional-resources-tuned-profile_{context}"]
.Additional resources
* Getting started with TuneD (RHEL documentation)
* How to manage tuning profiles in Linux (Red Hat blog)

//microshift-baseline is the name of the profile and used for automatic activation settings
// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-tuned-auto-activate_{context}"]
= Automatically enable the {microshift-short} TuneD profile

[role="_abstract"]
Included in the `microshift-low-latency` RPM package is a systemd service that you can configure to automatically enable a TuneD profile when the system starts. This ability is particularly useful if you are installing {microshift-short} in a large fleet of devices.

.Prerequisites

* You installed the microshift-low-latency RPM package on the host.
* You enabled low latency in the {microshift-short} `config.yaml`.
* You created a TuneD profile.
* You configured the `microshift-baseline-variables.conf` file.

.Procedure

. Configure the `tuned.yaml` in the `/etc/microshift/` directory, for example:
+
Example `tuned.yaml`:
+
[source,yaml]
----
profile: microshift-baseline
reboot_after_apply: True
----
+
`profile`:: Controls which TuneD profile is activated. In this example, the name of the profile is `microshift-baseline`.
`reboot_after_apply`:: Controls whether the host must be rebooted after applying the profile. Valid values are `True` and `False`. For example, use the `True` setting to automatically restart the host after a new `ostree` commit is deployed.
+
[IMPORTANT]
====
The host is restarted when the `microshift-tuned.service` runs, but it does not restart the system when a new commit is deployed. You must restart the host to enable a new commit, then the system starts again when the `microshift-tuned.service` runs on that boot and detects changes to profiles and variables.

This double-boot can affect rollbacks. Ensure that you adjust the number of reboots in greenboot that are allowed before rollback when using automatic profile activation. For example, if 3 reboots are allowed before a rollback in greenboot, increase that number to 4. See the "Additional resources" list for more information.
====

. Enable the `microshift-tuned.service` to run on each system start by entering the following command:
+
[source,terminal]
----
$ sudo systemctl enable microshift-tuned.service
----
+
[IMPORTANT]
====
If you set `reboot_after_apply` to `True`, ensure that a TuneD profile is active and that no other profiles have been activated outside of the {microshift-short} service. Otherwise, starting the `microshift-tuned.service` results in a host reboot.
====

. Start the `microshift-tuned.service` by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift-tuned.service
----
+
[NOTE]
====
The `microshift-tuned.service` uses collected checksums to detect changes to selected TuneD profiles and variables. If there are no checksums on the disk, the service activates the TuneD profile and restarts the host. Expect a host restart when first starting the `microshift-tuned.service`.
====

.Next steps
* Optional: If you are using the x86_64 architecture, you can install {op-system-rt-kernel}.

//additional resources for tuned profiles automatic activation
[role="_additional-resources"]
[id="additional-resources-tuned-auto_{context}"]
.Additional resources
* Greenboot directories details

//RHEL real-time kernel
// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-kernelrt-conc_{context}"]
= Using Red Hat Enterprise Linux for Real Time

[role="_abstract"]
Use the {op-system-rt-kernel} for workloads with stringent low-latency determinism requirements for core kernel features. The {op-system-rtk} provides consistent, low-latency determinism and predictable response times.

When considering system tuning, consider the following factors:

* System tuning is just as important when using the {op-system-rtk} as it is for the standard kernel.
* Installing the {op-system-rtk} on an untuned system running the standard kernel supplied as part of the RHEL 9 release is not likely to result in any noticeable benefit.
* Tuning the standard kernel yields 90% of possible latency gains.
* The {op-system-rtk} provides the last 10% of latency reduction required by the most demanding workloads.

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-install-kernelrt_{context}"]
= Installing the {op-system-rt-kernel}

[role="_abstract"]
Although the real-time kernel is not necessary for low latency workloads, using the {op-system-rtk} can optimize low latency performance. You can install it on a host by using RPM packages, and include it in a {op-system-ostree-first} image deployment.

.Prerequisites

* You have a Red Hat subscription that includes {op-system-rt-kernel}. For example, your host machine is registered and Red Hat Enterprise Linux (RHEL) is attached to a RHEL for Real Time subscription.
* You are using x86_64 architecture.

.Procedure

. Enable the {op-system-rtk} repository by running the following command:
+
[source,terminal]
----
$ sudo subscription-manager repos --enable rhel-9-for-x86_64-rt-rpms
----

. Install the real-time kernel by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y kernel-rt
----

. Query the real-time kernel version by running the following command:
+
[source,terminal]
----
$ RTVER=$(rpm -q --queryformat '%{version}-%{release}.%{arch}' kernel-rt | sort | tail -1)
----
+
. Make a persistent change in GRUB that designates the real-time kernel as the default kernel by running the following command:
+
[source,terminal]
----
$ sudo grubby --set-default="/boot/vmlinuz-${RTVER}+rt"
----

. Restart the host to activate the real-time kernel.

.Next steps
. Prepare your {microshift-short} workloads for low latency.
. Optional: Use a blueprint to install the real-time kernel in a {op-system-ostree} image.

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-install-kernelrt-rhel-edge_{context}"]
= Installing the {op-system-rt-kernel} in a {op-system-ostree-first} image

[role="_abstract"]
To configure low latency for a {microshift-short} node, you can include the real-time kernel in a {op-system-ostree} image deployment using image builder.

.Prerequisites
* You have a Red Hat subscription enabled on the host that includes {op-system-rt-kernel}.
* You are using the x86_64 architecture.
* You configured `osbuild` to use the `kernel-rt` repository.

[IMPORTANT]
====
A subscription that includes the {op-system-rtk} must be enabled on the host used to build the commit.
====

.Procedure

* Add the following example blueprint sections to your complete installation blueprint for installing the real-time kernel in a {op-system-ostree} image:
+
.Example blueprint snippet for the real-time kernel
[source,text]
----
[[packages]]
name = "microshift-low-latency"
version = "*"

# Kernel RT is supported only on the x86_64 architecture
[customizations.kernel]
name = "kernel-rt"

[customizations.services]
enabled = ["microshift", "microshift-tuned"]

[[customizations.files]]
path = "/etc/microshift/config.yaml"
data = """
kubelet:
  cpuManagerPolicy: static
  cpuManagerPolicyOptions:
    full-pcpus-only: "true"
  cpuManagerReconcilePeriod: 5s
  memoryManagerPolicy: Static
  topologyManagerPolicy: single-numa-node
  reservedSystemCPUs: 0-1
  reservedMemory:
  - limits:
      memory: 1100Mi
    numaNode: 0
  kubeReserved:
    memory: 500Mi
  systemReserved:
    memory: 500Mi
  evictionHard:
    imagefs.available: 15%
    memory.available: 100Mi
    nodefs.available: 10%
    nodefs.inodesFree: 5%
  evictionPressureTransitionPeriod: 5m
"""

[[customizations.files]]
path = "/etc/tuned/microshift-baseline-variables.conf"
data = """
# Isolated cores should be complementary to the kubelet configuration reserved CPUs.
# Isolated and reserved CPUs must contain all online CPUs.
# Core #3 is for testing offlining, therefore it is skipped.
isolated_cores=2,4-5
hugepages_size=2M
hugepages=10
additional_args=test1=on test2=true dummy
offline_cpu_set=3
"""

[[customizations.files]]
path = "/etc/microshift/tuned.yaml"
data = """
profile: microshift-baseline
reboot_after_apply: True
"""
----

.Next steps
. Complete the image building process.
. If you have not completed the previous steps for enabling low latency for your {microshift-short} cluster, do so now. Update the blueprint with the information gathered in those steps.
. If you have not configured workload partitioning, do so now.
. Prepare your {microshift-short} workloads for low latency.

[id="microshift-low-latency-install-kernelrt-rhel-edge-buildimage_{context}"]
== Building the {op-system-ostree-first} image with the real-time kernel

Complete the build process by starting with the following procedure to embed {microshift-short}in a {op-system-ostree} image. Then complete the remaining steps in the installation documentation for installing {microshift-short} in a {op-system-ostree} image:

* Embedding in a {op-system-ostree} image

//additional resources for real-time kernel
[role="_additional-resources"]
[id="additional-resources-rtk_{context}"]
.Additional resources
* Red Hat Enterprise Linux for Real Time 9 ({op-system-base} documentation)
* Using repositories that require subscription (osbuild documentation)
* Building {op-system-base} images by using the {op-system-rtk}
* Post installation instructions (RHEL for Real Time documentation)
* Embedding in a {op-system-ostree} image

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-prepare-workload_{context}"]
= Preparing a {microshift-short} workload for low latency

[role="_abstract"]
To use low latency, configure pod annotations to set the `microshift-low-latency` container runtime configuration for your workloads by using the `RuntimeClass` feature.

.Prerequisites
* You installed the `microshift-low-latency` RPM package.
* You configured workload partitioning.

.Procedure

* Use the following example to set the following annotations in the pod spec:
+
[source,text]
----
cpu-load-balancing.crio.io: "disable"
irq-load-balancing.crio.io: "disable"
cpu-quota.crio.io: "disable"
cpu-load-balancing.crio.io: "disable"
cpu-freq-governor.crio.io: "<governor>"
----
+
Example pod that runs `oslat` test:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: oslat
  annotations:
    cpu-load-balancing.crio.io: "disable"
    irq-load-balancing.crio.io: "disable"
    cpu-quota.crio.io: "disable"
    cpu-c-states.crio.io: "disable"
    cpu-freq-governor.crio.io: "<governor>"
spec:
  runtimeClassName: microshift-low-latency
  containers:
  - name: oslat
    image: quay.io/container-perf-tools/oslat
    imagePullPolicy: Always
    resources:
      requests:
        memory: "400Mi"
        cpu: "2"
      limits:
        memory: "400Mi"
        cpu: "2"
    env:
    - name: tool
      value: "oslat"
    - name: manual
      value: "n"
    - name: PRIO
      value: "1"
    - name: delay
      value: "0"
    - name: RUNTIME_SECONDS
      value: "60"
    - name: TRACE_THRESHOLD
      value: ""
    - name: EXTRA_ARGS
      value: ""
    securityContext:
      privileged: true
      capabilities:
        add:
          - SYS_NICE
          - IPC_LOCK

----
+
`metadata.annotations.cpu-load-balancing.crio.io`:: Disables the CPU load balancing for the pod.
`metadata.annotations.irq-load-balancing.crio.io`:: Opts the pod out of interrupt handling (IRQ).
`metadata.annotations.cpu-quota.crio.io`:: Disables the CPU completely fair scheduler (CFS) quota at the pod run time.
`metadata.annotations.cpu-c-states.crio.io`:: Enables or disables C-states for each CPU. Set the value to `disable` to provide the best performance for a high-priority pod.
`metadata.annotations.cpu-freq-governor.crio.io`:: Sets the `cpufreq` governor for each CPU. The `performance` governor is recommended for high-priority workloads.
`spec.runtimeClassName`:: The `runtimeClassName` must match the name of the performance profile configured in the node. For example, `microshift-low-latency`.
+
[NOTE]
====
Disable CPU load balancing only when the CPU manager static policy is enabled and for pods with guaranteed QoS that use whole CPUs. Otherwise, disabling CPU load balancing can affect the performance of other containers in the node.
====
+
[IMPORTANT]
====
For the pod to have the `Guaranteed` QoS class, it must have the same values of CPU and memory in requests and limits. See Guaranteed (Kubernetes upstream documentation)
====

//additional resources for preparing the workload
[role="_additional-resources"]
[id="additional-resources-prep-workload_{context}"]
.Additional resources

* Disabling power saving mode for high priority pods ({OCP} documentation)

* Disabling CPU CFS quota ({OCP} documentation)

* Disabling interrupt processing for CPUs where pinned containers are running ({OCP} documentation)

// Module included in the following assemblies:
//
// microshift_configuring/microshift_low_latency/microshift-low-latency.adoc

[id="microshift-low-latency-blueprint-rhel-edge-rtk_{context}"]
= Reference blueprint for installing {op-system-rt-kernel} in a {op-system-ostree} image

[role="_abstract"]
An image blueprint is a persistent definition of required image customizations that you can use to create multiple builds. You can edit, rebuild, delete, and save the blueprint to easily rebuild images.

.Example blueprint used to install the real-time kernel in a {op-system-ostree} image
[source,text]
----
name = "microshift-low-latency"
description = "RHEL 9.4 and MicroShift configured for low latency"
version = "0.0.1"
modules = []
groups = []
distro = "rhel-94"

[[packages]]
name = "microshift"
version = "*"

[[packages]]
name = "microshift-greenboot"
version = "*"

[[packages]]
name = "microshift-networking"
version = "*"

[[packages]]
name = "microshift-selinux"
version = "*"

[[packages]]
name = "microshift-low-latency"
version = "*"

# Kernel RT is only available for x86_64
[customizations.kernel]
name = "kernel-rt"

[customizations.services]
enabled = ["microshift", "microshift-tuned"]

[customizations.firewall]
ports = ["22:tcp", "80:tcp", "443:tcp", "5353:udp", "6443:tcp", "30000-32767:tcp", "30000-32767:udp"]

[customizations.firewall.services]
enabled = ["mdns", "ssh", "http", "https"]

[[customizations.firewall.zones]]
name = "trusted"
sources = ["10.42.0.0/16", "169.254.169.1"]

[[customizations.files]]
path = "/etc/microshift/config.yaml"
data = """
kubelet:
  cpuManagerPolicy: static
  cpuManagerPolicyOptions:
    full-pcpus-only: "true"
  cpuManagerReconcilePeriod: 5s
  memoryManagerPolicy: Static
  topologyManagerPolicy: single-numa-node
  reservedSystemCPUs: 0-1
  reservedMemory:
  - limits:
      memory: 1100Mi
    numaNode: 0
  kubeReserved:
    memory: 500Mi
  systemReserved:
    memory: 500Mi
  evictionHard:
    imagefs.available: 15%
    memory.available: 100Mi
    nodefs.available: 10%
    nodefs.inodesFree: 5%
  evictionPressureTransitionPeriod: 5m
"""

[[customizations.files]]
path = "/etc/tuned/microshift-baseline-variables.conf"
data = """
# Isolated cores should be complementary to the kubelet configuration reserved CPUs.
# Isolated and reserved CPUs must contain all online CPUs.
# Core #3 is for testing offlining, therefore it is skipped.
isolated_cores=2,4-5
hugepages_size=2M
hugepages=10
additional_args=test1=on test2=true dummy
offline_cpu_set=3
"""

[[customizations.files]]
path = "/etc/microshift/tuned.yaml"
data = """
profile: microshift-baseline
reboot_after_apply: True
"""
----

//additional resources for workload partitioning
[role="_additional-resources"]
[id="additional-resources-wp_{context}"]
.Additional resources
* Workload partitioning
