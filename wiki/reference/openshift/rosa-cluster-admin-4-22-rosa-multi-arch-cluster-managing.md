---
title: "Managing a cluster with multi-architecture compute machines"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-multi-arch-cluster-managing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-multi-arch-cluster-managing
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Managing a cluster with multi-architecture compute machines

//This assembly duplicates the following file to avoid symbolic links:
[id="rosa-multi-arch-managing"]
= Managing a cluster with multi-architecture compute machines

[role="_abstract"]
Managing a cluster that has nodes with multiple architectures requires you to consider node architecture as you monitor the cluster and manage your workloads. This requires you to take additional considerations into account when you schedule workloads in a multi-architecture cluster.

[id="multi-architecture-scheduling_{context}"]
= Scheduling workloads on clusters with multi-architecture compute machines

When you deploy workloads on a cluster with compute nodes that use different architectures, you must align pod architecture with the architecture of the underlying node. Your workload may also require additional configuration to particular resources depending on the underlying node architecture.

You can use the Multiarch Tuning Operator to enable architecture-aware scheduling of workloads on clusters with multi-architecture compute machines. The Multiarch Tuning Operator implements additional scheduler predicates in the pods specifications based on the architectures that the pods can support at creation time.

For information about the Multiarch Tuning Operator, see Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator.

// Module included in the following assembly
//
//post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-compute-managing.adoc

[id="multi-architecture-scheduling-examples_{context}"]
= Sample multi-architecture node workload deployments

Scheduling a workload to an appropriate node based on architecture works in the same way as scheduling based on any other node characteristic.
Consider the following options when determining how to schedule your workloads.
