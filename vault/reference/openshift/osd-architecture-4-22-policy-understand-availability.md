---
title: "Understanding availability for {product-title}"
type: reference
domain: openshift
slug: osd-architecture-4-22-policy-understand-availability
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_architecture/policy-understand-availability
version: 4.22
family: osd_architecture
documentKind: "Documentation"
---

# Understanding availability for {product-title}

[id="policy-understand-availability"]
= Understanding availability for OpenShift Container Platform

[role="_abstract"]
Availability and disaster avoidance are extremely important aspects of any application platform. OpenShift Container Platform provides many protections against failures at several levels, but customer-deployed applications must be appropriately configured for high availability. In addition, to account for cloud provider outages that might occur, other options are available, such as deploying a cluster across multiple availability zones or maintaining multiple clusters with failover mechanisms.

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/policy-understand-availability.adoc

[id="policy-failure-points_{context}"]
= Potential points of failure

[role="_abstract"]
{OCP} provides many features and options for protecting your workloads against downtime, but applications must be architected appropriately to take advantage of these features.

OpenShift Container Platform can help further protect you against many common Kubernetes issues by adding Red Hat Site Reliability Engineer (SRE) support and the option to deploy a multi-zone cluster, but there are a number of ways in which a container or infrastructure can still fail. By understanding potential points of failure, you can understand risks and appropriately architect both your applications and your clusters to be as resilient as necessary at each specific level.

[NOTE]
====
An outage can occur at several different levels of infrastructure and cluster components.
====

[id="container-pod-failure_{context}"]
== Container or pod failure
By design, pods are meant to exist for a short time. Appropriately scaling services so that multiple instances of your application pods are running protects against issues with any individual pod or container. The node scheduler can also ensure that these workloads are distributed across different worker nodes to further improve resiliency.

When accounting for possible pod failures, it is also important to understand how storage is attached to your applications. Single persistent volumes attached to single pods cannot leverage the full benefits of pod scaling, whereas replicated databases, database services, or shared storage can.

To avoid disruption to your applications during planned maintenance, such as upgrades, it is important to define a pod disruption budget. These are part of the Kubernetes API and can be managed with the OpenShift CLI (`oc`) like other object types. They allow the specification of safety constraints on pods during operations, such as draining a node for maintenance.

[id="worker-node-failure_{context}"]
== Worker node failure
Worker nodes are the virtual machines that contain your application pods. By default, an OpenShift Container Platform cluster has a minimum of four worker nodes for a single availability-zone cluster. In the event of a worker node failure, pods are relocated to functioning worker nodes, as long as there is enough capacity, until any issue with an existing node is resolved or the node is replaced. More worker nodes means more protection against single node outages, and ensures proper cluster capacity for rescheduled pods in the event of a node failure.

[NOTE]
====
When accounting for possible node failures, it is also important to understand how storage is affected.
====

[id="cluster-failure_{context}"]
== Cluster failure
OpenShift Container Platform clusters have at least three control plane nodes and three infrastructure nodes that are preconfigured for high availability, either in a single zone or across multiple zones depending on the type of cluster you have selected. This means that control plane and infrastructure nodes have the same resiliency of worker nodes, with the added benefit of being managed completely by Red Hat.

In the event of a complete control plane node outage, the OpenShift APIs will not function, and existing worker node pods will be unaffected. However, if there is also a pod or node outage at the same time, the control plane nodes will have to recover before new pods or nodes can be added or scheduled.

All services running on infrastructure nodes are configured by Red Hat to be highly available and distributed across infrastructure nodes. In the event of a complete infrastructure outage, these services will be unavailable until these nodes have been recovered.

[id="zone-failure_{context}"]
== Zone failure
A zone failure from a public cloud provider affects all virtual components, such as worker nodes, block or shared storage, and load balancers that are specific to a single availability zone. To protect against a zone failure, OpenShift Container Platform provides the option for clusters that are distributed across three availability zones, called multi-availability zone clusters. Existing stateless workloads are redistributed to unaffected zones in the event of an outage, as long as there is enough capacity.

[id="storage-failure_{context}"]
== Storage failure
If you have deployed a stateful application, then storage is a critical component and must be accounted for when thinking about high availability. A single block storage PV is unable to withstand outages even at the pod level. The best ways to maintain availability of storage are to use replicated storage solutions, shared storage that is unaffected by outages, or a database service that is independent of the cluster.
