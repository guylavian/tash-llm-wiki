---
title: "Limits and scalability"
type: reference
domain: openshift
slug: rosa-planning-4-22-rosa-limits-scalability
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_planning/rosa-limits-scalability
version: 4.22
family: rosa_planning
documentKind: "Documentation"
---

# Limits and scalability

[id="rosa-limits-scalability"]
= Limits and scalability

This document details the tested cluster maximums for OpenShift Container Platform (ROSA) clusters, along with information about the test environment and configuration used to test the maximums. Information about control plane and infrastructure node sizing and scaling is also provided.

// Module included in the following assemblies:
//
// * osd_planning/osd-limits-scalability.adoc
// * rosa_planning/rosa-limits-scalability.adoc

[id="tested-cluster-maximums-sd_{context}"]
= Cluster maximums

[role="_abstract"]
Review the tested object maximums when planning
a OpenShift Container Platform
an OpenShift Container Platform
cluster installation. Adhering to these supported limits helps you successfully architect and deploy a scalable, reliable environment.

These guidelines are based on a cluster of 249 compute (also known as worker) nodes in a multiple availability zone configuration. For smaller clusters, the maximums are lower.

.Tested cluster maximums
[options="header",cols="50,50"]
|===
|Maximum type |4.x tested maximum

|Number of pods ^[1]^
|25,000

|Number of pods per node
|250

|Number of pods per core
|There is no default value

|Number of namespaces ^[2]^
|5,000

|Number of pods per namespace ^[3]^
|25,000

|Number of services ^[4]^
|10,000

|Number of services per namespace
|5,000

|Number of back ends per service
|5,000

|Number of deployments per namespace ^[3]^
|2,000
|===
[.small]
--
1. The pod count displayed here is the number of test pods. The actual number of pods depends on the memory, CPU, and storage requirements of the application.
2. When there are a large number of active projects, etcd can suffer from poor performance if the keyspace grows excessively large and exceeds the space quota. Periodic maintenance of etcd, including defragmentation, is highly recommended to make etcd storage available.
3. There are several control loops in the system that must iterate over all objects in a given namespace as a reaction to some changes in state. Having a large number of objects of a type, in a single namespace, can make those loops expensive and slow down processing the state changes. The limit assumes that the system has enough CPU, memory, and disk to satisfy the application requirements.
4. Each service port and each service back end has a corresponding entry in `iptables`. The number of back ends of a given service impacts the size of the endpoints objects, which then impacts the size of data sent throughout the system.
--
// Module included in the following assemblies:
//
// * osd_planning/osd-limits-scalability.adoc
// * rosa_planning/rosa-limits-scalability.adoc

[id="planning-cluster-maximums-environment-sd_{context}"]
= OpenShift Container Platform testing environment and configuration

[role="_abstract"]
To successfully plan your deployment on the AWS cloud platform, review the tested OpenShift Container Platform environment and configuration settings. Adhering to these cluster maximums ensures your environment is fully supported and optimized for scale.

[options="header",cols="8*"]
|===
| Node |Type |vCPU |RAM(GiB) |Disk type|Disk size(GiB)/IOPS |Count |Region

|Control plane/etcd ^[1]^
|m5.4xlarge
|16
|64
|gp3
|350 / 1,000
|3
|us-west-2

|Infrastructure nodes ^[2]^
|r5.2xlarge
|8
|64
|gp3
|300 / 900
|3
|us-west-2

|Workload ^[3]^
|m5.2xlarge
|8
|32
|gp3
|350 / 900
|3
|us-west-2

|Compute nodes
|m5.2xlarge
|8
|32
|gp3
|350 / 900
|102
|us-west-2
|===
[.small]
--
1. io1 disks are used for control plane/etcd nodes in all versions prior to 4.10.
2. Infrastructure nodes are used to host monitoring components because Prometheus can claim a large amount of memory, depending on usage patterns.
3. Workload nodes are dedicated to run performance and scalability workload generators.
--

Larger cluster sizes and higher object counts might be reachable. However, the sizing of the infrastructure nodes limits the amount of memory that is available to Prometheus. When creating, modifying, or deleting objects, Prometheus stores the metrics in its memory for roughly 3 hours prior to persisting the metrics on disk. If the rate of creation, modification, or deletion of objects is too high, Prometheus can become overwhelmed and fail due to the lack of memory resources.
// Module included in the following assemblies:
//
// * osd_planning/osd-limits-scalability.adoc
// * rosa_planning/rosa-limits-scalability.adoc

[id="control-plane-and-infra-node-sizing-and-scaling-sd_{context}"]
= Control plane and infrastructure node sizing and scaling

[role="_abstract"]
When you install
a OpenShift Container Platform
an OpenShift Container Platform
cluster, the sizing of the control plane and infrastructure nodes are automatically determined by the compute node count. To maintain cluster stability, the Red{nbsp}Hat Site Reliability Engineering (SRE) team automatically adjusts your control plane and infrastructure nodes whenever you change your compute node count.

[id="node-sizing-during-installation_{context}"]
== Node sizing during installation

During the installation process, the sizing of the control plane and infrastructure nodes are dynamically calculated. The sizing calculation is based on the number of compute nodes in a cluster.

The following
table lists
tables list
the control plane and infrastructure node sizing that is applied during installation.

AWS control plane and infrastructure node size:
[options="header",cols="3*"]
|===
|Number of compute nodes |Control plane size |Infrastructure node size

|1 to 25
|m5.2xlarge
|r5.xlarge

|26 to 100
|m5.4xlarge
|r5.2xlarge

|101 to 249
|m5.8xlarge
|r5.4xlarge
|===

{gcp-short} control plane and infrastructure node size:
[options="header",cols="2a,2a,2a"]
|===
|Number of compute nodes
|Control plane size
|Infrastructure node size

|1 to 25
|custom-8-32768
|custom-4-32768-ext

|26 to 100
|custom-16-65536
|custom-8-65536-ext

|101 to 249
|custom-32-131072
|custom-16-131072-ext
|===

{gcp-short} control plane and infrastructure node size for clusters created on or after 21 June 2024:
[options="header",cols="2a,2a,2a"]
|===
|Number of compute nodes
|Control plane size
|Infrastructure node size

|1 to 25
|n2-standard-8
|n2-highmem-4

|26 to 100
|n2-standard-16
|n2-highmem-8

|101 to 249
|n2-standard-32
|n2-highmem-16
|===

[NOTE]
====
The maximum number of compute nodes on
OpenShift Container Platform
OpenShift Container Platform
clusters version 4.14.14 and later is 249. For earlier versions, the limit is 180.
====

[id="node-scaling-after-installation_{context}"]
== Node scaling after installation

If you change the number of compute nodes after installation, the control plane and infrastructure nodes are scaled by the Red{nbsp}Hat Site Reliability Engineering (SRE) team as required. The nodes are scaled to maintain platform stability.

Postinstallation scaling requirements for control plane and infrastructure nodes are assessed on a case-by-case basis. Node resource consumption and received alerts are taken into consideration.

.Rules for control plane node resizing alerts

The resizing alert is triggered for the control plane nodes in a cluster when the following occurs:

* Control plane nodes sustain over 66% utilization on average in a cluster.
+
[NOTE]
====
The maximum number of compute nodes on
OpenShift Container Platform
OpenShift Container Platform
is 180.
====

.Rules for infrastructure node resizing alerts

Resizing alerts are triggered for the infrastructure nodes in a cluster when it has high-sustained CPU or memory utilization. This high-sustained utilization status is:

* Infrastructure nodes sustain over 50% utilization on average in a cluster with a single availability zone using 2 infrastructure nodes.
* Infrastructure nodes sustain over 66% utilization on average in a cluster with multiple availability zones using 3 infrastructure nodes.
+
[NOTE]
====
The maximum number of compute nodes on
{rosa-title}
OpenShift Container Platform
cluster versions 4.14.14 and later is 249. For earlier versions, the limit is 180.

The resizing alerts only appear after sustained periods of high utilization. Short usage spikes, such as a node temporarily going down causing the other node to scale up, do not trigger these alerts.
====

The SRE team might scale the control plane and infrastructure nodes for additional reasons, for example to manage an increase in resource consumption on the nodes.

When scaling is applied, the customer is notified through a service log entry. For more information about the service log, see _Accessing the service logs for ROSA clusters_.

[id="sizing-considerations-for-larger-clusters_{context}"]
== Sizing considerations for larger clusters

For larger clusters, infrastructure node sizing can become a significant impacting factor to scalability. There are many factors that influence the stated thresholds, including the etcd version or storage data format.

Exceeding these limits does not necessarily mean that the cluster will fail. In most cases, exceeding these numbers results in lower overall performance.

[id="next-steps_configuring-alert-notifications"]
== Next steps

* Planning your environment

[role="_additional-resources"]
[id="additional-resources_rosa-limits-scalability"]
== Additional resources

* Viewing cluster notifications using the {hybrid-console}
