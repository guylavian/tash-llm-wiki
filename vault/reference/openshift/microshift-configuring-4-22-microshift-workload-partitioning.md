---
title: "Workload partitioning"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-workload-partitioning
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-workload-partitioning
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Workload partitioning

[id="microshift-workload-partitioning"]
= Workload partitioning

Workload partitioning divides the node CPU resources into distinct CPU sets. The primary objective is to limit the amount of CPU usage for all control plane components which reserves rest of the device CPU resources for workloads of the user.

Workload partitioning allocates reserved set of CPUs to {microshift-short} services, cluster management workloads, and infrastructure pods, ensuring that the remaining CPUs in the cluster deployment are untouched and available exclusively for non-platform workloads.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-workload-partitioning.adoc

[id="microshift-enabling-workload-partitioning_{context}"]
= Enabling workload partitioning

To enable workload partitioning on {microshift-short}, make the following configuration changes:

* Update the {microshift-short} `config.yaml` file to include the kubelet configuration file.
* Create the CRI-O systemd and configuration files.
* Create and update the systemd configuration file for the {microshift-short} and CRI-O services respectively.

.Procedure

. Update the {microshift-short} `config.yaml` file to include the kubelet configuration file to enable and configure CPU Manager for the workloads:
* Create the kubelet configuration file in the path `/etc/kubernetes/openshift-workload-pinning`. The kubelet configuration directs the kubelet to modify the node resources based on the capacity and allocatable CPUs.
+
.kubelet configuration example
[source,yaml]
----
# ...
{
  "management": {
    "cpuset": "0,6,7" <1>
  }
}
# ...
----
<1> The `cpuset` applies to a machine with 8 VCPUs (4 cores) and is valid throughout the document.
* Update the {microshift-short} config.yaml file in the path `/etc/microshift/config.yaml`. Embed the kubelet configuration in the {microshift-short} `config.yaml` file to enable and configure CPU Manager for the workloads.
+
.{microshift-short} `config.yaml` example
[source,yaml]
----
# ...
kubelet:
  reservedSystemCPUs: 0,6,7 <1>
  cpuManagerPolicy: static
  cpuManagerPolicyOptions:
    full-pcpus-only: "true" <2>
  cpuManagerReconcilePeriod: 5s
# ...
----
<1> Exclusive cpuset for the system daemons and the interrupts/timers.
<2> kubelet configuration sets the `CPUManagerPolicyOptions` option to `full-pcpus-only` to ensure allocation of whole cores to the containers workload.

. Create the CRI-O systemd and configuration files:
* Create the CRI-O configuration file in the path `/etc/crio/crio.conf.d/20-microshift-workload-partition.conf` which overrides the default configuration that already exists in the `11-microshift-ovn.conf` file.
+
.CRI-O configuration example
[source,yaml]
----
# ...
[crio.runtime]
infra_ctr_cpuset = "0,6,7"

[crio.runtime.workloads.management]
activation_annotation = "target.workload.openshift.io/management"
annotation_prefix = "resources.workload.openshift.io"
resources = { "cpushares" = 0, "cpuset" = "0,6,7" }
# ...
----
* Create the systemd file for CRI-O in the path `/etc/systemd/system/crio.service.d/microshift-cpuaffinity.conf`.
+
.CRI-O systemd configuration example
[source,yaml]
----
# ...
[Service]
CPUAffinity=0,6,7
# ...
----

. Create and update the systemd configuration file with `CPUAffinity` value for the {microshift-short} and CRI-O services:
* Create the {microshift-short} services systemd file in the path `/etc/systemd/system/microshift.service.d/microshift-cpuaffinity.conf`. {microshift-short} will be pinned using the systemd `CPUAffinity` value.
+
.{microshift-short} services systemd configuration example
[source,yaml]
----
# ...
[Service]
CPUAffinity=0,6,7
# ...
----
* Update the `CPUAffinity` value in the {microshift-short} ovs-vswitchd systemd file in the path `/etc/systemd/system/ovs-vswitchd.service.d/microshift-cpuaffinity.conf`.
+
.{microshift-short} ovs-vswitchd systemd configuration example
[source,yaml]
----
# ...
[Service]
CPUAffinity=0,6,7
# ...
----
* Update the `CPUAffinity` value in the {microshift-short} ovsdb-server systemd file in the path `/etc/systemd/system/ovsdb-server.service.d/microshift-cpuaffinity.conf`
+
.{microshift-short} ovsdb-server systemd configuration example
[source,yaml]
----
# ...
[Service]
CPUAffinity=0,6,7
# ...
----
