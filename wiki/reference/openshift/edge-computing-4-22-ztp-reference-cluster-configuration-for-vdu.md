---
title: "Recommended {sno} cluster configuration for vDU application workloads"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-reference-cluster-configuration-for-vdu
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-reference-cluster-configuration-for-vdu
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Recommended {sno} cluster configuration for vDU application workloads

[id="sno-configure-for-vdu"]
= Recommended {sno} cluster configuration for vDU application workloads

Use the following reference information to understand the {sno} configurations required to deploy virtual distributed unit (vDU) applications in the cluster. Configurations include cluster optimizations for high performance workloads, enabling workload partitioning, and minimizing the number of reboots required postinstallation.

[role="_additional-resources"]
.Additional resources

* To deploy a single cluster by hand, see Manually installing a {sno} cluster with {ztp}.

* To deploy a fleet of clusters using {ztp-first}, see Deploying far edge sites with {ztp}.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-low-latency_{context}"]
= Running low latency applications on OpenShift Container Platform

OpenShift Container Platform enables low latency processing for applications running on commercial off-the-shelf (COTS) hardware by using several technologies and specialized hardware devices:

Real-time kernel for RHCOS:: Ensures workloads are handled with a high degree of process determinism.

CPU isolation:: Avoids CPU scheduling delays and ensures CPU capacity is available consistently.

NUMA-aware topology management:: Aligns memory and huge pages with CPU and PCI devices to pin guaranteed container memory and huge pages to the non-uniform memory access (NUMA) node. Pod resources for all Quality of Service (QoS) classes stay on the same NUMA node. This decreases latency and improves performance of the node.

Huge pages memory management:: Using huge page sizes improves system performance by reducing the amount of system resources required to access page tables.

Precision timing synchronization using PTP:: Allows synchronization between nodes in the network with sub-microsecond accuracy.

// Module included in the following assemblies:
//
// * edge_computing/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-install-sno-hardware-reqs_{context}"]
= Recommended cluster host requirements for vDU application workloads

[role="_abstract"]
Running vDU application workloads requires a bare-metal host with sufficient resources to run OpenShift Container Platform services and production workloads.

.Minimum resource requirements
[options="header"]
|====
|Profile|vCPU|Memory|Storage
|Minimum|4 vCPU|32 GB of RAM|120 GB
|Recommended|8 vCPU|32 GB of RAM|120 GB
|====

[IMPORTANT]
====
Running {sno} on 4 vCPUs leaves very little headroom for vDU application workloads.
With all cluster capabilities enabled, the platform alone can request over 2.5 vCPUs and consume over 2 vCPUs at idle, leaving minimal capacity for application workloads.
====

To run on 4 vCPUs, you must minimize the cluster resource footprint:

* Set `baselineCapabilitySet` to `None` in the `install-config.yaml` file and use `additionalEnabledCapabilities` to enable only the capabilities that your workload requires, such as `Storage`, `Console`, and `Ingress`. For more information, see "Cluster capabilities".

* Use a performance profile to partition CPU resources between cluster housekeeping duties and application workloads, ensuring that your vDU containers run on isolated CPUs with minimal interruption. For more information, see "Tuning nodes for low latency with the performance profile".

If your deployment does not require these optimizations, it is recommended to use at least 8 vCPUs..

[NOTE]
====
One vCPU equals one physical core. However, if you enable simultaneous multithreading (SMT), or Hyper-Threading, use the following formula to calculate the number of vCPUs that represent one physical core:

* (threads per core × cores) × sockets = vCPUs
====

[IMPORTANT]
====
The server must have a Baseboard Management Controller (BMC) when booting with virtual media.
====

[role="_additional-resources"]
.Additional resources

* Cluster capabilities
* Tuning nodes for low latency with the performance profile

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-du-configuring-host-firmware-requirements_{context}"]
= Configuring host firmware for low latency and high performance

Bare-metal hosts require the firmware to be configured before the host can be provisioned. The firmware configuration is dependent on the specific hardware and the particular requirements of your installation.

.Procedure

. Set the *UEFI/BIOS Boot Mode* to `UEFI`.
. In the host boot sequence order, set *Hard drive first*.
. Apply the specific firmware configuration for your hardware. The following table describes a representative firmware configuration for an Intel Xeon Skylake server and later hardware generations, based on the Intel FlexRAN 4G and 5G baseband PHY reference design.
+
[IMPORTANT]
====
The exact firmware configuration depends on your specific hardware and network requirements. The following sample configuration is for illustrative purposes only.
====
+
.Sample firmware configuration
[cols=2*, width="90%", options="header"]
|====
|Firmware setting
|Configuration

|CPU Power and Performance Policy
|Performance

|Uncore Frequency Scaling
|Disabled

|Performance P-limit
|Disabled

|Enhanced Intel SpeedStep (R) Tech
|Enabled

|Intel Configurable TDP
|Enabled

|Configurable TDP Level
|Level 2

|Intel(R) Turbo Boost Technology
|Enabled

|Energy Efficient Turbo
|Disabled

|Hardware P-States
|Disabled

|Package C-State
|C0/C1 state

|C1E
|Disabled

|Processor C6
|Disabled
|====

[NOTE]
====
Enable global SR-IOV and VT-d settings in the firmware for the host. These settings are relevant to bare-metal environments.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-managed-cluster-network-prereqs_{context}"]
= Connectivity prerequisites for managed cluster networks

Before you can install and provision a managed cluster with the {ztp-first} pipeline, the managed cluster host must meet the following networking prerequisites:

* There must be bi-directional connectivity between the {ztp} container in the hub cluster and the Baseboard Management Controller (BMC) of the target bare-metal host.

* The managed cluster must be able to resolve and reach the API hostname of the hub hostname and `{asterisk}.apps` hostname. Here is an example of the API hostname of the hub and `{asterisk}.apps` hostname:

** `api.hub-cluster.internal.domain.com`
** `console-openshift-console.apps.hub-cluster.internal.domain.com`

* The hub cluster must be able to resolve and reach the API and `{asterisk}.apps` hostname of the managed cluster. Here is an example of the API hostname of the managed cluster and `{asterisk}.apps` hostname:

** `api.sno-managed-cluster-1.internal.domain.com`
** `console-openshift-console.apps.sno-managed-cluster-1.internal.domain.com`

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-workload-partitioning-sno_{context}"]
= Workload partitioning in {sno} with {ztp}

Workload partitioning configures OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved number of host CPUs.

To configure workload partitioning with {ztp-first}, you configure a `cpuPartitioningMode` field in the `ClusterInstance` custom resource (CR) that you use to install the cluster and you apply a `PerformanceProfile` CR that configures the `isolated` and `reserved` CPUs on the host.

Configuring the `ClusterInstance` CR enables workload partitioning at cluster installation time and applying the `PerformanceProfile` CR configures the specific allocation of CPUs to reserved and isolated sets.
Both of these steps happen at different points during cluster provisioning.

The workload partitioning configuration pins the OpenShift Container Platform infrastructure pods to the `reserved` CPU set.
Platform services such as systemd, CRI-O, and kubelet run on the `reserved` CPU set.
The `isolated` CPU sets are exclusively allocated to your container workloads.
Isolating CPUs ensures that the workload has guaranteed access to the specified CPUs without contention from other applications running on the same node.
All CPUs that are not isolated should be reserved.

[IMPORTANT]
====
Ensure that `reserved` and `isolated` CPU sets do not overlap with each other.
====

[role="_additional-resources"]
.Additional resources

* TPM encryption

[id="ztp-sno-install-time-cluster-config"]
== Recommended cluster install manifests

The ZTP pipeline applies the following custom resources (CRs) during cluster installation. These configuration CRs ensure that the cluster meets the feature and performance requirements necessary for running a vDU application.

[NOTE]
====
When using the {ztp} plugin and `ClusterInstance` CRs for cluster deployment, the following `MachineConfig` CRs are included by default.
====

Use the `ClusterInstance` `extraManifestRefs` to alter the CRs that are included by default. For more information, see Advanced managed cluster configuration with ClusterInstance CRs.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-the-container-mountspace_{context}"]
= Reduced platform management footprint

To reduce the overall management footprint of the platform, a `MachineConfig` custom resource (CR) is required that places all Kubernetes-specific mount points in a new namespace separate from the host operating system.
The following base64-encoded example `MachineConfig` CR illustrates this configuration.

.Recommended container mount namespace configuration (`01-container-mount-ns-and-kubelet-conf-master.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-enabling-sctp_{context}"]
= SCTP

Stream Control Transmission Protocol (SCTP) is a key protocol used in RAN applications. This `MachineConfig` object adds the SCTP kernel module to the node to enable this protocol.

.Recommended control plane node SCTP configuration (`03-sctp-machine-config-master.yaml`)
[source,yaml]
----
----

.Recommended worker node SCTP configuration (`03-sctp-machine-config-worker.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-setting-rcu-normal_{context}"]
= Setting rcu_normal

The following `MachineConfig` CR configures the system to set `rcu_normal` to 1 after the system has finished startup. This improves kernel latency for vDU applications.

.Recommended configuration for disabling `rcu_expedited` after the node has finished startup (`08-set-rcu-normal-master.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-enabling-kdump_{context}"]
= Automatic kernel crash dumps with kdump

`kdump` is a Linux kernel feature that creates a kernel crash dump when the kernel crashes. `kdump` is enabled with the following `MachineConfig` CRs.

.Recommended control plane node kdump configuration (`06-kdump-master.yaml`)
[source,yaml]
----
----

.Recommended kdump worker node configuration (`06-kdump-worker.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-disabling-crio-wipe_{context}"]
= Disable automatic CRI-O cache wipe

After an uncontrolled host shutdown or cluster reboot, CRI-O automatically deletes the entire CRI-O cache, causing all images to be pulled from the registry when the node reboots.
This can result in unacceptably slow recovery times or recovery failures.
To prevent this from happening in {sno} clusters that you install with {ztp}, disable the CRI-O delete cache feature during cluster installation.

.Recommended `MachineConfig` CR to disable CRI-O cache wipe on control plane nodes (`99-crio-disable-wipe-master.yaml`)
[source,yaml]
----
----

.Recommended `MachineConfig` CR to disable CRI-O cache wipe on worker nodes (`99-crio-disable-wipe-worker.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-crun-container-runtime_{context}"]
= Configuring crun as the default container runtime

The following `ContainerRuntimeConfig` custom resources (CRs) configure crun as the default OCI container runtime for control plane and worker nodes.
The crun container runtime is fast and lightweight and has a low memory footprint.

[IMPORTANT]
====
For optimal performance, enable crun for control plane and worker nodes in {sno}, {3no}, and standard clusters.
To avoid the cluster rebooting when the CR is applied, apply the change as a {ztp} additional Day 0 install-time manifest.
====

.Recommended `ContainerRuntimeConfig` CR for control plane nodes (`enable-crun-master.yaml`)
[source,yaml]
----
----

.Recommended `ContainerRuntimeConfig` CR for worker nodes (`enable-crun-worker.yaml`)
[source,yaml]
----
----

[role="_additional-resources"]
.Additional resources

[id="ztp-sno-post-install-time-cluster-config"]
== Recommended postinstallation cluster configurations

When the cluster installation is complete, the ZTP pipeline applies the following custom resources (CRs) that are required to run DU workloads.

[NOTE]
====
In {ztp} v4.10 and earlier, you configure UEFI secure boot with a `MachineConfig` CR. This is no longer required in {ztp} v4.11 and later. In v4.11, you configure UEFI secure boot for {sno} clusters by updating the `spec.nodes[].bootMode` field in the `ClusterInstance` CR that you use to install the cluster. For more information, see Deploying a managed cluster with ClusterInstance and {ztp}.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-the-operators_{context}"]
= Operators

{sno-caps} clusters that run DU workloads require the following Operators to be installed:

* Local Storage Operator
* Logging Operator
* PTP Operator
* SR-IOV Network Operator

You also need to configure a custom `CatalogSource` CR, disable the default `OperatorHub` configuration, and configure an `ImageContentSourcePolicy` mirror registry that is accessible from the clusters that you install.

.Recommended Storage Operator namespace and Operator group configuration (`StorageNS.yaml`, `StorageOperGroup.yaml`)
[source,yaml]
----
---
---
----

.Recommended Cluster Logging Operator namespace and Operator group configuration (`ClusterLogNS.yaml`, `ClusterLogOperGroup.yaml`)
[source,yaml]
----
----

.Recommended PTP Operator namespace and Operator group configuration (`PtpSubscriptionNS.yaml`, `PtpSubscriptionOperGroup.yaml`)
[source,yaml]
----
---
----

.Recommended SR-IOV Operator namespace and Operator group configuration (`SriovSubscriptionNS.yaml`, `SriovSubscriptionOperGroup.yaml`)
[source,yaml]
----
---
---
----

.Recommended `CatalogSource` configuration (`DefaultCatsrc.yaml`)
[source,yaml]
----
----

.Recommended `ImageContentSourcePolicy` configuration (`DisconnectedICSP.yaml`)
[source,yaml]
----
----

.Recommended `OperatorHub` configuration (`OperatorHub.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-subscribing-to-the-operators-needed-for-platform-configuration_{context}"]
= Operator subscriptions

{sno-caps} clusters that run DU workloads require the following `Subscription` CRs. The subscription provides the location to download the following Operators:

* Local Storage Operator
* Logging Operator
* PTP Operator
* SR-IOV Network Operator
* SRIOV-FEC Operator

For each Operator subscription, specify the channel to get the Operator from. The recommended channel is `stable`.

You can specify `Manual` or `Automatic` updates.
In `Automatic` mode, the Operator automatically updates to the latest versions in the channel as they become available in the registry.
In `Manual` mode, new Operator versions are installed only when they are explicitly approved.

[TIP]
====
Use `Manual` mode for subscriptions. This allows you to control the timing of Operator updates to fit within scheduled maintenance windows.
====

.Recommended Local Storage Operator subscription (`StorageSubscription.yaml`)
[source,yaml]
----
----

.Recommended SR-IOV Operator subscription (`SriovSubscription.yaml`)
[source,yaml]
----
----

.Recommended PTP Operator subscription (`PtpSubscription.yaml`)
[source,yaml]
----
----

.Recommended Cluster Logging Operator subscription (`ClusterLogSubscription.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * edge_computing/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-logging-locally-and-forwarding_{context}"]
= Cluster logging and log forwarding

{sno-caps} clusters that run DU workloads require logging and log forwarding for debugging.
The following custom resources (CRs) are required.

[id="ztp-clusterlogforwarder-yaml"]
.Recommended ClusterLogForwarder.yaml
[source,yaml]
----
----

[NOTE]
====
Set the `spec.outputs.kafka.url` field to the URL of the Kafka server where the logs are forwarded to.
====

[id="ztp-clusterlogns-yaml"]
.Recommended ClusterLogNS.yaml
[source,yaml]
----
----

[id="ztp-clusterlogopergroup-yaml"]
.Recommended ClusterLogOperGroup.yaml
[source,yaml]
----
----

[id="ztp-clusterlogserviceaccount-yaml"]
.Recommended ClusterLogServiceAccount.yaml
[source,yaml]
----
----

[id="ztp-clusterlogserviceaccountauditbinding-yaml"]
.Recommended ClusterLogServiceAccountAuditBinding.yaml
[source,yaml]
----
----

[id="ztp-clusterlogserviceaccountinfrastructurebinding-yaml"]
.Recommended ClusterLogServiceAccountInfrastructureBinding.yaml
[source,yaml]
----
----

[id="ztp-clusterlogsubscription-yaml"]
.Recommended ClusterLogSubscription.yaml
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-performance-addons_{context}"]
= Performance profile

{sno-caps} clusters that run DU workloads require a Node Tuning Operator performance profile to use real-time host capabilities and services.

[NOTE]
====
In earlier versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.
====

The following example `PerformanceProfile` CR illustrates the required {sno} cluster configuration.

.Recommended performance profile configuration (`PerformanceProfile.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-time-sync_{context}"]
= Configuring cluster time synchronization

Run a one-time system time synchronization job for control plane or worker nodes.

.Recommended one time time-sync for control plane nodes (`99-sync-time-once-master.yaml`)
[source,yaml]
----
----

.Recommended one time time-sync for worker nodes (`99-sync-time-once-worker.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-ptp_{context}"]
= PTP

[role="_abstract"]
{sno-caps} clusters use Precision Time Protocol (PTP) for network time synchronization.
The following example `PtpConfig` custom resources (CRs) illustrate configurations for ordinary clocks, boundary clocks, and Telecom Grandmaster clocks on supported Intel Ethernet hardware.
You must select the profile that matches your qualified GNR-D hardware layout and complete interface renaming prerequisites before you apply Granite Rapids-D Telecom Grandmaster YAML on Intel Granite Rapids-D servers.

.Recommended PTP ordinary clock configuration (`PtpConfigSlave.yaml`)
[source,yaml]
----
----

.Recommended boundary clock configuration (`PtpConfigBoundary.yaml`)
[source,yaml]
----
----

.Recommended PTP Westport Channel e810 grandmaster clock configuration (`PtpConfigGmWpc.yaml`)
[source,yaml]
----
----

.Recommended PTP Granite Rapids-D Telecom Grandmaster clock configuration (`PtpConfigGnrdTGM.yaml`)
[source,yaml]
----
----

The following optional `PtpOperatorConfig` CR configures PTP events reporting for the node.

.Recommended PTP events configuration (`PtpOperatorConfigForEvent.yaml`)
[source,yaml]
----
----

[role="_additional-resources"]
.Additional resources

* Configuring linuxptp services as a Telecom Grandmaster clock on Intel Granite Rapids-D hardware

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-tuning-the-performance-patch_{context}"]
= Extended Tuned profile

{sno-caps} clusters that run DU workloads require additional performance tuning configurations necessary for high-performance workloads. The following example `Tuned` CR extends the `Tuned` profile:

.Recommended extended `Tuned` profile configuration (`TunedPerformancePatch.yaml`)
[source,yaml]
----
----

.`Tuned` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|Tuned CR field
|Description

|`spec.profile.data`
a|* The `include` line that you set in `spec.profile.data` must match the associated `PerformanceProfile` CR name.
For example, `include=openshift-node-performance-${PerformanceProfile.metadata.name}`.
|====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-configuring-sriov_{context}"]
= SR-IOV

Single root I/O virtualization (SR-IOV) is commonly used to enable fronthaul and midhaul networks. The following YAML example configures SR-IOV for a {sno} cluster.

[NOTE]
====
The configuration of the `SriovNetwork` CR will vary depending on your specific network and infrastructure requirements.
====

.Recommended `SriovOperatorConfig` CR configuration (`SriovOperatorConfig.yaml`)
[source,yaml]
----
----

.`SriovOperatorConfig` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|SriovOperatorConfig CR field
|Description

|`spec.enableInjector`
a|Disable `Injector` pods to reduce the number of management pods.
Start with the `Injector` pods enabled, and only disable them after verifying the user manifests.
If the injector is disabled, containers that use SR-IOV resources must explicitly assign them in the `requests` and `limits` section of the container spec.

For example:
[source,yaml]
----
containers:
- name: my-sriov-workload-container
  resources:
    limits:
      openshift.io/<resource_name>:  "1"
    requests:
      openshift.io/<resource_name>:  "1"
----

|`spec.enableOperatorWebhook`
|Disable `OperatorWebhook` pods to reduce the number of management pods. Start with the `OperatorWebhook` pods enabled, and only disable them after verifying the user manifests.

|====

.Recommended `SriovNetwork` configuration (`SriovNetwork.yaml`)
[source,yaml]
----
----

.`SriovNetwork` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|SriovNetwork CR field
|Description

|`spec.vlan`
|Configure `vlan` with the VLAN for the midhaul network.
|====

.Recommended `SriovNetworkNodePolicy` CR configuration (`SriovNetworkNodePolicy.yaml`)
[source,yaml]
----
----

.`SriovNetworkPolicy` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|SriovNetworkNodePolicy CR field
|Description

|`spec.deviceType`
|Configure `deviceType` as `vfio-pci` or `netdevice`.
For Mellanox NICs, set `deviceType: netdevice`, and `isRdma: true`.
For Intel based NICs, set `deviceType: vfio-pci` and `isRdma: false`.

|`spec.nicSelector.pfNames`
|Specifies the interface connected to the fronthaul network.

|`spec.numVfs`
|Specifies the number of VFs for the fronthaul network.

|`spec.nicSelector.pfNames`
|The exact name of physical function must match the hardware.
|====

.Recommended SR-IOV kernel configurations (`07-sriov-related-kernel-args-master.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-removing-the-console-operator_{context}"]
= Console Operator

Use the cluster capabilities feature to prevent the Console Operator from being installed.
When the node is centrally managed it is not needed.
Removing the Operator provides additional space and capacity for application workloads.

To disable the Console Operator during the installation of the managed cluster, set the following in the `spec.installConfigOverrides` field of the `ClusterInstance` custom resource (CR):

[source,yaml]
----
installConfigOverrides:  "{\"capabilities\":{\"baselineCapabilitySet\": \"None\" }}"
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-reducing-resource-usage-with-cluster-monitoring_{context}"]
= Alertmanager

{sno-caps} clusters that run DU workloads require reduced CPU resources consumed by the OpenShift Container Platform monitoring components. The following `ConfigMap` custom resource (CR) disables Alertmanager.

.Recommended cluster monitoring configuration (`ReduceMonitoringFootprint.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-reducing-resource-usage-with-olm-pprof_{context}"]
= Operator Lifecycle Manager

{sno-caps} clusters that run distributed unit workloads require consistent access to CPU resources. Operator Lifecycle Manager (OLM) collects performance data from Operators at regular intervals, resulting in an increase in CPU utilisation. The following `ConfigMap` custom resource (CR) disables the collection of Operator performance data by OLM.

.Recommended cluster OLM configuration (`ReduceOLMFootprint.yaml`)
[source,yaml]
----
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="lvms-configuring-lvms-on-sno_{context}"]
= {lvms}

You can dynamically provision local storage on {sno} clusters with {lvms-first}.

[NOTE]
====
The recommended storage solution for {sno} is the Local Storage Operator. Alternatively, you can use {lvms} but it requires additional CPU resources to be allocated.
====

The following YAML example configures the storage of the node to be available to OpenShift Container Platform applications.

.Recommended `LVMCluster` configuration (`StorageLVMCluster.yaml`)
[source,yaml]
----
----

.`LVMCluster` CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|LVMCluster CR field
|Description

|`deviceSelector.paths`
|Configure the disks used for LVM storage. If no disks are specified, the {lvms} uses all the unused disks in the specified thin pool.
|====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.adoc

[id="ztp-sno-du-disabling-network-diagnostics_{context}"]
= Network diagnostics

{sno-caps} clusters that run DU workloads require less inter-pod network connectivity checks to reduce the additional load created by these pods. The following custom resource (CR) disables these checks.

.Recommended network diagnostics configuration (`DisableSnoNetworkDiag.yaml`)
[source,yaml]
----
----

[role="_additional-resources"]
.Additional resources

* Deploying far edge sites using ZTP
