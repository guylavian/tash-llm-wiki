---
title: "Sizing guidance for {hcp}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-sizing-guidance
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-sizing-guidance
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Sizing guidance for {hcp}

[id="hcp-sizing-guidance"]
= Sizing guidance for {hcp}

[role="_abstract"]
Many factors, including hosted cluster workload and worker node count, affect how many hosted control planes can fit within a certain number of worker nodes.

Use this sizing guide to help with hosted cluster capacity planning.

This guidance assumes a highly available {hcp} topology. The load-based sizing examples were measured on a bare-metal cluster. Cloud-based instances might have different limiting factors, such as memory size.

You can override the following resource utilization sizing measurements and disable the metric service monitoring.

See the following highly available {hcp} requirements, which were tested with OpenShift Container Platform version 4.12.9 and later:

* 78 pods
* Three 8 GiB PVs for etcd
* Minimum vCPU: approximately 5.5 cores
* Minimum memory: approximately 19 GiB

[role="_additional-resources"]
.Additional resources

* Overriding resource utilization measurements
* Distributing hosted cluster workloads

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-sizing-guidance.adoc

[id="hcp-pod-limits_{context}"]
= Pod limits

[role="_abstract"]
The `maxPods` setting for each node affects how many hosted clusters can fit in a control-plane node. It is important to note the `maxPods` value on all control-plane nodes. Plan for about 75 pods for each highly available hosted control plane.

For bare-metal nodes, the default `maxPods` setting of 250 is likely to be a limiting factor because roughly three {hcp} fit for each node given the pod requirements, even if the machine has plenty of resources to spare. Setting the `maxPods` value to 500 by configuring the `KubeletConfig` value allows for greater hosted control plane density, which can help you take advantage of additional compute resources.

[role="_additional-resources"]
.Additional resources

* Configuring the maximum number of pods per node

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-sizing-guidance.adoc

[id="hcp-resource-limit_{context}"]
= Request-based resource limit

[role="_abstract"]
The maximum number of hosted control planes that the cluster can host is calculated based on the hosted control plane CPU and memory requests from the pods.

A highly available hosted control plane consists of 78 pods that request 5 vCPUs and 18 GiB memory. These baseline numbers are compared to the cluster worker node resource capacities to estimate the maximum number of hosted control planes.

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-sizing-guidance.adoc

[id="hcp-load-based-limit_{context}"]
= Load-based limit

[role="_abstract"]
As you plan your deployment, consider the maximum number of hosted control planes that the cluster can host. That number is calculated based on the hosted control plane pods CPU and memory utilizations when some workload is put on the hosted control plane Kubernetes API server.

The following method is used to measure the hosted control plane resource utilizations as the workload increases:

* A hosted cluster with 9 workers that use 8 vCPU and 32 GiB each, while using the KubeVirt platform
* The workload test profile that is configured to focus on API control-plane stress, based on the following definition:

+
** Created objects for each namespace, scaling up to 100 namespaces total
+
** Additional API stress with continuous object deletion and creation
+
** Workload queries-per-second (QPS) and Burst settings set high to remove any client-side throttling

As the load increases by 1000 QPS, the hosted control plane resource utilization increases by 9 vCPUs and 2.5 GB memory.

For general sizing purposes, consider the 1000 QPS API rate that is a _medium_ hosted cluster load, and a 2000 QPS API that is a _heavy_ hosted cluster load.

[NOTE]
====
This test provides an estimation factor to increase the compute resource utilization based on the expected API load. Exact utilization rates can vary based on the type and pace of the cluster workload.
====

The following example shows hosted control plane resource scaling for the workload and API rate definitions:

.API rate table
|===
| QPS (API rate) | vCPU usage | Memory usage (GiB)

| Low load (Less than 50 QPS)
| 2.9
| 11.1

| Medium load (1000 QPS)
| 11.9
| 13.6

| High load (2000 QPS)
| 20.9
| 16.1
|===

The hosted control plane sizing is about control-plane load and workloads that cause heavy API activity, etcd activity, or both. Hosted pod workloads that focus on data-plane loads, such as running a database, might not result in high API rates.

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-sizing-guidance.adoc

[id="hcp-sizing-calculation_{context}"]
= Sizing calculation example

[role="_abstract"]
Review an example of how to size a deployment of {hcp}.

This example provides sizing guidance for the following scenario:

* Three bare-metal workers that are labeled as `hypershift.openshift.io/control-plane` nodes
* `maxPods` value set to 500
* The expected API rate is medium or about 1000, according to the load-based limits

.Limit inputs
|===
| Limit description | Server 1 | Server 2

| Number of vCPUs on worker node
| 64
| 128

| Memory on worker node (GiB)
| 128
| 256

| Maximum pods per worker
| 500
| 500

| Number of workers used to host control planes
| 3
| 3

| Maximum QPS target rate (API requests per second)
| 1000
| 1000
|===

.Sizing calculation example
|===

| Calculated values based on worker node size and API rate | Server 1 | Server 2 | Calculation notes

| Maximum {hcp} per worker based on vCPU requests
| 12.8
| 25.6
| Number of worker vCPUs ÷ 5 total vCPU requests per hosted control plane

| Maximum {hcp} per worker based on vCPU usage
| 5.4
| 10.7
| Number of vCPUS ÷ (2.9 measured idle vCPU usage + (QPS target rate ÷ 1000) × 9.0 measured vCPU usage per 1000 QPS increase)

| Maximum {hcp} per worker based on memory requests
| 7.1
| 14.2
| Worker memory GiB ÷ 18 GiB total memory request per hosted control plane

| Maximum {hcp} per worker based on memory usage
| 9.4
| 18.8
| Worker memory GiB ÷ (11.1 measured idle memory usage + (QPS target rate ÷ 1000) × 2.5 measured memory usage per 1000 QPS increase)

| Maximum {hcp} per worker based on per node pod limit
| 6.7
| 6.7
| 500 `maxPods` ÷ 75 pods per hosted control plane

| Minimum of previously mentioned maximums
| 5.4
| 6.7
|

|
| vCPU limiting factor
| `maxPods` limiting factor
|

| Maximum number of {hcp} within a management cluster
| 16
| 20
| Minimum of previously mentioned maximums × 3 control-plane workers
|===

.{hcp-capital} capacity metrics
|===

| Name | Description

| `mce_hs_addon_request_based_hcp_capacity_gauge`
| Estimated maximum number of {hcp} the cluster can host based on a highly available {hcp} resource request.

| `mce_hs_addon_low_qps_based_hcp_capacity_gauge`
| Estimated maximum number of {hcp} the cluster can host if all {hcp} make around 50 QPS to the clusters Kube API server.

| `mce_hs_addon_medium_qps_based_hcp_capacity_gauge`
| Estimated maximum number of {hcp} the cluster can host if all {hcp} make around 1000 QPS to the clusters Kube API server.

| `mce_hs_addon_high_qps_based_hcp_capacity_gauge`
| Estimated maximum number of {hcp} the cluster can host if all {hcp} make around 2000 QPS to the clusters Kube API server.

| `mce_hs_addon_average_qps_based_hcp_capacity_gauge`
| Estimated maximum number of {hcp} the cluster can host based on the existing average QPS of {hcp}. If you do not have an active {hcp}, you can expect low QPS.
|===

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-sizing-guidance.adoc

[id="hcp-shared-infra_{context}"]
= Shared infrastructure between hosted and standalone control planes

[role="_abstract"]
As a service provider, you can more effectively use your resources by sharing infrastructure between a standalone OpenShift Container Platform control plane and {hcp}. A 3-node OpenShift Container Platform cluster can be a management cluster for a hosted cluster.

Sharing infrastructure can be beneficial in constrained environments, such as in small-scale deployments where you need resource efficiency.

Before you share infrastructure, ensure that your infrastructure has enough resources to support {hcp}. On the OpenShift Container Platform management cluster, nothing else can be deployed except {hcp}. Ensure that the management cluster has enough CPU, memory, storage, and network resources to handle the combined load of the hosted clusters. Workload must not be demanding, and it must fall within a low queries-per-second (QPS) profile. For more information about resources and workload, see "Sizing guidance for {hcp}".

[role="_additional-resources"]
.Additional resources

* Sizing guidance for {hcp}
