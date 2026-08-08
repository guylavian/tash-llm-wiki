---
title: "Workload partitioning"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-enabling-workload-partitioning
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/enabling-workload-partitioning
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Workload partitioning

[id="enabling-workload-partitioning"]
= Workload partitioning

[role="_abstract"]
Workload partitioning separates compute node CPU resources into distinct CPU sets. Ensure that you keep platform pods on the specified cores to avoid interrupting the CPUs the customer workloads are running on.

The minimum number of reserved CPUs required for the cluster management is four CPU Hyper-Threads (HTs).

In the context of enabling workload partitioning and managing CPU resources effectively, the cluster might not permit incorrectly configured nodes to join the cluster through a node admission webhook. When the workload partitioning feature is enabled, the machine config pools for control plane nodes and compute nodes get supplied with configurations for nodes to use. Adding new nodes to these pools ensures the pools correctly get configured before joining the cluster.

Currently, nodes must have uniform configurations per machine config pool to ensure that correct CPU affinity is set across all nodes within that pool. After admission, nodes within the cluster identify themselves as supporting a new resource type called `management.workload.openshift.io/cores` and accurately report their CPU capacity. Workload partitioning can be enabled during cluster installation only by adding the additional field `cpuPartitioningMode` to the `install-config.yaml` file.

When workload partitioning is enabled, the `management.workload.openshift.io/cores` resource allows the scheduler to correctly assign pods based on the `cpushares` capacity of the host, not just the default `cpuset`. This ensures more precise allocation of resources for workload partitioning scenarios.

Workload partitioning ensures that CPU requests and limits specified in the pod's configuration are respected. In OpenShift Container Platform 4.16 or later, accurate CPU usage limits are set for platform pods through CPU partitioning. As workload partitioning uses the custom resource type of `management.workload.openshift.io/cores`, the values for requests and limits are the same due to a requirement by Kubernetes for extended resources. However, the annotations modified by workload partitioning correctly reflect the desired limits.

[NOTE]
====
Extended resources cannot be overcommitted, so request and limit must be equal if both are present in a container spec.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/enabling-workload-partitioning.adoc

[id="enabling-workload-partitioning_{context}"]
= Enabling workload partitioning

[role="_abstract"]
To partition cluster management pods into a specified CPU affinity, enable workload partitioning. This configuration ensures that management pods operate within the reserved CPU limits defined in your Performance Profile.

Consider additional post-installation Operators that use workload partitioning when calculating how many reserved CPU cores to set aside for the platform.

Workload partitioning isolates user workloads from platform workloads using standard Kubernetes scheduling capabilities.

[NOTE]
====
You can enable workload partitioning only during cluster installation. You cannot disable workload partitioning post-installation. However, you can change the CPU configuration for `reserved` and `isolated` CPUs post-installation.
====

The procedure demonstrates enabling workload partitioning cluster-wide.

.Procedure

* In the `install-config.yaml` file, add the additional field `cpuPartitioningMode` and set it to `AllNodes`.
+
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
cpuPartitioningMode: AllNodes
compute:
  - architecture: amd64
    hyperthreading: Enabled
    name: worker
    platform: {}
    replicas: 3
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform: {}
  replicas: 3
----
** `cpuPartitioningMode`: Specifies the cluster to set up for CPU partitioning at install time. The default value is `None`, which ensures that no CPU partitioning is enabled at install time.

// Module included in the following assemblies:
//
// * scalability_and_performance/enabling-workload-partitioning.adoc

[id="performance-profile-workload-partitioning_{context}"]
= Performance profiles and workload partitioning

[role="_abstract"]
To enable workload partitioning, apply a performance profile.

An appropriately configured performance profile specifies the `isolated` and `reserved` CPUs. Create a performance profile by using the Performance Profile Creator (PPC) tool.

.Sample performance profile configuration
[source,yaml]
----
----

[role="_additional-resources"]
.Additional resources

* About the Performance Profile Creator
