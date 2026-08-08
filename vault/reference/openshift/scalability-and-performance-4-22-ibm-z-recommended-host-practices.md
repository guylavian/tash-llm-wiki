---
title: "Host practices for IBM Z and IBM LinuxONE environments"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-ibm-z-recommended-host-practices
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/ibm-z-recommended-host-practices
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Host practices for IBM Z and IBM LinuxONE environments

[id="ibm-z-recommended-host-practices"]
= Host practices for IBM Z and IBM LinuxONE environments

[role="_abstract"]
You can apply host practices for {ibm-z-title} and {ibm-linuxone-name} environments to ensure your s390x architecture meets specific operational requirements.

The s390x architecture is unique in many aspects. Some host practice recommendations might not apply to other platforms.

[NOTE]
====
Unless stated otherwise, the host practices apply to both z/VM and {op-system-base-full} KVM installations on {ibm-z-name} and {ibm-linuxone-name}.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="ibm-z-managing-cpu-overcommitment_{context}"]
= Managing CPU overcommitment

[role="_abstract"]
To optimize infrastructure sizing in a highly virtualized {ibm-z-title} environment, manage CPU overcommitment. By adopting this strategy, you can allocate more resources to virtual machines than are physically available at the hypervisor level. This capability requires that you plan carefully for specific workload dependencies.

Depending on your setup, consider the following best practices regarding CPU overcommitment:

* Avoid over-allocating physical cores, Integrated Facilities for Linux (IFLs), at the Logical Partition (LPAR) level (PR/SM hypervisor). If your system has 4 physical IFLs, do not configure multiple LPARs with 4 logical IFLs each.
* Check and understand LPAR shares and weights.
* An excessive number of virtual CPUs can adversely affect performance. Do not define more virtual processors to a guest than logical processors are defined to the LPAR.
* Configure the number of virtual processors per guest for peak workload.
* Start small and monitor the workload. If required, increase the vCPU number incrementally.
* Not all workloads are suitable for high overcommitment ratios. If the workload is CPU intensive, you might experience performance problems with high overcommitment ratios. Workloads that are more I/O intensive can keep consistent performance even with high overcommitment ratios.

[role="_additional-resources"]
.Additional resources

* z/VM Common Performance Problems and Solutions

* z/VM overcommitment considerations

* LPAR CPU management

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="ibm-z-disable-thp_{context}"]
= Disable Transparent Huge Pages

[role="_abstract"]
To prevent the operating system from automatically managing memory segments, disable Transparent Huge Pages (THP).

Transparent Huge Pages (THP) tries to automate most aspects of creating, managing, and using huge pages. Since THP automatically manages the huge pages, THP does not always handle optimally for all types of workloads. THP can lead to performance regressions, since many applications handle huge pages on their own.

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="ibm-z-boost-networking-performance-with-rfs_{context}"]
= Boosting networking performance with RFS

[role="_abstract"]
To boost networking performance, activate Receive Flow Steering (RFS) by using the Machine Config Operator (MCO). This configuration improves packet processing efficiency.

RFS extends Receive Packet Steering (RPS) by further reducing network latency. RFS is technically based on RPS, and improves the efficiency of packet processing by increasing the CPU cache hit rate. RFS achieves this, while considering queue length, by determining the most convenient CPU for computation so that cache hits are more likely to occur within the CPU. This means that the CPU cache is invalidated less and requires fewer cycles to rebuild the cache, which reduces packet processing run time.

.Procedure

. Copy the following MCO sample profile into a YAML file. For example, `enable-rfs.yaml`:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 50-enable-rfs
spec:
  config:
    ignition:
      version: 2.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=US-ASCII,%23%20turn%20on%20Receive%20Flow%20Steering%20%28RFS%29%20for%20all%20network%20interfaces%0ASUBSYSTEM%3D%3D%22net%22%2C%20ACTION%3D%3D%22add%22%2C%20RUN%7Bprogram%7D%2B%3D%22/bin/bash%20-c%20%27for%20x%20in%20/sys/%24DEVPATH/queues/rx-%2A%3B%20do%20echo%208192%20%3E%20%24x/rps_flow_cnt%3B%20%20done%27%22%0A
        filesystem: root
        mode: 0644
        path: /etc/udev/rules.d/70-persistent-net.rules
      - contents:
          source: data:text/plain;charset=US-ASCII,%23%20define%20sock%20flow%20enbtried%20for%20%20Receive%20Flow%20Steering%20%28RFS%29%0Anet.core.rps_sock_flow_entries%3D8192%0A
        filesystem: root
        mode: 0644
        path: /etc/sysctl.d/95-enable-rps.conf
----

. Create the MCO profile by entering the following command:
+
[source,terminal]
----
$ oc create -f enable-rfs.yaml
----

. Verify that an entry named `50-enable-rfs` is listed by entering the following command:
+
[source,terminal]
----
$ oc get mc
----

. To deactivate the MCO profile, enter the following command:
+
[source,terminal]
----
$ oc delete mc 50-enable-rfs
----

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform on {ibm-z-name}: Tune your network performance with RFS

* Configuring Receive Flow Steering (RFS)

* Scaling in the Linux Networking Stack

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="ibm-z-choose-networking-setup_{context}"]
= Choose your networking setup

[role="_abstract"]
For {ibm-z-name} setups, the networking setup depends on the hypervisor of your choice. Depending on the workload and the application, the best fit usually changes with the use case and the traffic pattern.

The networking stack is one of the most important components for a Kubernetes-based product like OpenShift Container Platform.

Depending on your setup, consider these best practices:

* Consider all options regarding networking devices to optimize your traffic pattern. Explore the advantages of OSA-Express, RoCE Express, HiperSockets, z/VM VSwitch, Linux Bridge (KVM), and others to decide which option leads to the greatest benefit for your setup.
* Always use the latest available NIC version. For example, OSA Express 7S 10 GbE shows great improvement compared to OSA Express 6S 10 GbE with transactional workload types, although both are 10 GbE adapters.
* Each virtual switch adds an additional layer of latency.
* The load balancer plays an important role for network communication outside the cluster. Consider using a production-grade hardware load balancer if this is critical for your application.
* OpenShift Container Platform OVN-Kubernetes network plugin introduces flows and rules, which impact the networking performance. Make sure to consider pod affinities and placements, to benefit from the locality of services where communication is critical.
* Balance the trade-off between performance and functionality.

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform on {ibm-z-name} - Performance Experiences, Hints and Tips

* OpenShift Container Platform on {ibm-z-name} Networking Performance

* Controlling pod placement on nodes using node affinity rules

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="ibm-z-ensure-high-disk-performance-hyperpav_{context}"]
= Ensure high disk performance with HyperPAV on z/VM

[role="_abstract"]
To improve I/O performance for Direct Access Storage Devices (DASD) disks in z/VM environments, configure HyperPAV alias devices. To increase throughput for both control plane nodes and compute nodes, add YAML configurations with full-pack minidisks to the Machine Config Operator (MCO) profiles for {ibm-z-title} clusters.

DASD and Extended Count Key Data (ECKD) devices are commonly used disk types in {ibm-z-name} environments. In a typical OpenShift Container Platform setup in z/VM environments, DASD disks are commonly used to support the local storage for the nodes. You can set up HyperPAV alias devices to provide more throughput and overall better I/O performance for the DASD disks that support the z/VM guests.

Using HyperPAV for the local storage devices leads to a significant performance benefit. However, be aware of the trade-off between throughput and CPU costs.

.Procedure

. Copy the following MCO sample profile into a YAML file for the control plane node. For example, `05-master-kernelarg-hpav.yaml`:
+
[source,terminal]
----
$ cat 05-master-kernelarg-hpav.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 05-master-kernelarg-hpav
spec:
  config:
    ignition:
      version: 3.1.0
  kernelArguments:
    - rd.dasd=800-805
# ...
----

. Copy the following MCO sample profile into a YAML file for the compute node. For example, `05-worker-kernelarg-hpav.yaml`:
+
[source,terminal]
----
$ cat 05-worker-kernelarg-hpav.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 05-worker-kernelarg-hpav
spec:
  config:
    ignition:
      version: 3.1.0
  kernelArguments:
    - rd.dasd=800-805
# ...
----
+
[NOTE]
====
You must modify the `rd.dasd` arguments to fit the device IDs.
====

. Create the MCO profiles by entering the following commands:
+
[source,terminal]
----
$ oc create -f 05-master-kernelarg-hpav.yaml
----
+
[source,terminal]
----
$ oc create -f 05-worker-kernelarg-hpav.yaml
----

. To deactivate the MCO profiles, enter the following commands:
+
[source,terminal]
----
$ oc delete -f 05-master-kernelarg-hpav.yaml
----
+
[source,terminal]
----
$ oc delete -f 05-worker-kernelarg-hpav.yaml
----

[role="_additional-resources"]
.Additional resources

* Using HyperPAV for ECKD DASD

* Scaling HyperPAV alias devices on Linux guests on z/VM

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="ibm-z-rhel-kvm-host-recommendations_{context}"]
= {op-system-base} KVM on {ibm-z-title} host recommendations

[role="_abstract"]
To optimize Kernel-based Virtual Machine (KVM) performance on {ibm-z-title}, apply host recommendations.

Optimizing a KVM virtual server environment strongly depends on the workloads of the virtual servers and on the available resources. The same action that enhances performance in one environment can have adverse effects in another. Finding the best balance for a particular setting can be a challenge and often involves experimentation.

The following sections introduces some best practices when using OpenShift Container Platform with {op-system-base} KVM on {ibm-z-name} and {ibm-linuxone-name} environments.

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="use-io-threads-for-your-virtual-block-devices_{context}"]
= Use I/O threads for your virtual block devices

[role="_abstract"]
To make virtual block devices use I/O threads, you must configure one or more I/O threads for the virtual server and each virtual block device to use one of these I/O threads.

The following example specifies `<iothreads>3</iothreads>` to configure three I/O threads, with consecutive decimal thread IDs 1, 2, and 3. The `iothread="2"` parameter specifies the driver element of the disk device to use the I/O thread with ID 2.

.Sample I/O thread specification
[source,xml]
----
...
<domain>
 	<iothreads>3</iothreads>
  	 ...
    	<devices>
       ...
          <disk type="block" device="disk">
<driver ... iothread="2"/>
    </disk>
       ...
    	</devices>
   ...
</domain>
----

where:

`iothreads`:: Specifies the number of I/O threads.

`disk`:: Specifies the driver element of the disk device.

Threads can increase the performance of I/O operations for disk devices, but they also use memory and CPU resources. You can configure multiple devices to use the same thread. The best mapping of threads to devices depends on the available resources and the workload.

Start with a small number of I/O threads. Often, a single I/O thread for all disk devices is sufficient. Do not configure more threads than the number of virtual CPUs, and do not configure idle threads.

You can use the `virsh iothreadadd` command to add I/O threads with specific thread IDs to a running virtual server.

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="avoid-virtual-scsi-devices_{context}"]
= Avoid virtual SCSI devices

[role="_abstract"]
Configure virtual SCSI devices only if you need to address the device through SCSI-specific interfaces. Configure disk space as virtual block devices rather than virtual SCSI devices, regardless of the backing on the host.

However, you might need SCSI-specific interfaces for:

* A logical unit number (LUN) for a SCSI-attached tape drive on the host.

* A DVD ISO file on the host file system that is mounted on a virtual DVD drive.

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="configure-guest-caching-for-disk_{context}"]
= Configure guest caching for disk

[role="_abstract"]
To ensure that the guest manages caching instead of the host, configure your disk devices.

Ensure that the driver element of the disk device includes the `cache="none"` and `io="native"` parameters.

.Example configuration
[source,xml]
----
<disk type="block" device="disk">
    <driver name="qemu" type="raw" cache="none" io="native" iothread="1"/>
...
</disk>
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="exclude-the-memory-balloon-device_{context}"]
= Excluding the memory balloon device

[role="_abstract"]
Unless you need a dynamic memory size, do not define a memory balloon device and ensure that libvirt does not create one for you. Include the `memballoon` parameter as a child of the devices element in your domain configuration file.

.Procedure

* To disable the memory balloon driver, add the following configuration setting to your domain configuration file:
+
[source,xml]
----
<memballoon model="none"/>
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="tune-the-cpu-migration-algorithm-of-the-host-scheduler_{context}"]
= Tuning the CPU migration algorithm of the host scheduler

[role="_abstract"]
You can tune the CPU migration algorithm of the host scheduler to meet the demands of your production system.

[IMPORTANT]
====
Do not change the scheduler settings unless you are an expert who understands the implications. Do not apply changes to production systems without testing them and confirming that they have the intended effect.
====

The `kernel.sched_migration_cost_ns` parameter specifies a time interval in nanoseconds. After the last execution of a task, the CPU cache is considered to have useful content until this interval expires. Increasing this interval results in fewer task migrations. The default value is `500000` ns.

If the CPU idle time is higher than expected when there are runnable processes, try reducing this interval. If tasks bounce between CPUs or nodes too often, try increasing it.

.Procedure

* To dynamically set the interval to `60000` ns, enter the following command:
+
[source,terminal]
----
# sysctl kernel.sched_migration_cost_ns=60000
----

* To persistently change the value to `60000` ns, add the following entry to `/etc/sysctl.conf`:
+
[source,config]
----
kernel.sched_migration_cost_ns=60000
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="disabling-the-cpuset-cgroup-controller_{context}"]
= Disabling the cpuset cgroup controller

[role="_abstract"]
You can disable the cpuset cgroup controller. Disabling the controller requires a restart of the libvirtd daemon.

[NOTE]
====
This setting applies only to KVM hosts with cgroups version 1. To enable CPU hotplug on the host, disable the cgroup controller.
====

.Procedure

. Open `/etc/libvirt/qemu.conf` with an editor of your choice.

. Go to the `cgroup_controllers` line.

. Duplicate the entire line and remove the leading number sign (#) from the copy.

. Remove the `cpuset` entry, as follows:
+
[source,config]
----
cgroup_controllers = [ "cpu", "devices", "memory", "blkio", "cpuacct" ]
----

. For the new setting to take effect, you must restart the libvirtd daemon:
+
.. Stop all virtual machines.
+
.. Run the following command:
+
[source,terminal]
----
# systemctl restart libvirtd
----
+
.. Restart the virtual machines.
+
This setting persists across host reboots.

// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

[id="tune-the-polling-period-for-idle-virtual-cpus_{context}"]
= Tuning the polling period for idle virtual CPUs

[role="_abstract"]
When a virtual CPU becomes idle, KVM polls for wakeup conditions for the virtual CPU before allocating the host resource. You can specify the time interval, during which polling takes place in sysfs at `/sys/module/kvm/parameters/halt_poll_ns`.

During the specified time, polling reduces the wakeup latency for the virtual CPU at the expense of resource usage. Depending on the workload, a longer or shorter time for polling can be beneficial. The time interval is specified in nanoseconds. The default is `50000` ns.

.Procedure

* To optimize for low CPU consumption, enter a small value or write `0` to disable polling:
+
[source,terminal]
----
# echo 0 > /sys/module/kvm/parameters/halt_poll_ns
----

* To optimize for low latency, for example for transactional workloads, enter a large value:
+
[source,terminal]
----
# echo 80000 > /sys/module/kvm/parameters/halt_poll_ns
----

[role="_additional-resources"]
.Additional resources

* Linux on {ibm-z-name} Performance Tuning for KVM

* Getting started with virtualization on {ibm-z-name}
