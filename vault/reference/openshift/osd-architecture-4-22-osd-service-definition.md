---
title: "{product-title} service definition"
type: reference
domain: openshift
slug: osd-architecture-4-22-osd-service-definition
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_architecture/osd-service-definition
version: 4.22
family: osd_architecture
documentKind: "Documentation"
---

# {product-title} service definition

[id="osd-service-definition"]
= OpenShift Container Platform service definition

[role="_abstract"]
This document provides you with an overview of the OpenShift Container Platform service definition, including account management, logging, monitoring, networking, storage, platform, and security aspects.

[id="sdpolicy-account-management_{context}"]
== Account management
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="billing_{context}"]
= Billing options

[role="_abstract"]
Customers have the option to purchase annual subscriptions of OpenShift Container Platform (OSD) or consume on-demand through cloud marketplaces. Customers can decide to bring their own cloud infrastructure account, referred to as Customer Cloud Subscription (CCS), or deploy in cloud provider accounts owned by Red Hat. The table below provides additional information regarding billing, as well as the corresponding supported deployment options.
[cols="2a,3a,3a",options="header"]
|===

|OSD Subscription-type
|Cloud infrastructure account
|Billed through

.2+|Annual fixed capacity subscriptions through Red Hat |Red Hat cloud account

|Red Hat for consumption of both OSD subscriptions and cloud infrastructure

|Customer's own cloud account
|Red Hat for consumption of the OSD subscriptions

Cloud provider for consumption of cloud infrastructure

|On-demand usage-based consumption through {gcp-full} Marketplace

|Customer's own {gcp-full} account
|{gcp-full} for both cloud infrastructure and Red Hat OSD subscriptions

|===

[IMPORTANT]
====

Customers that use their own cloud infrastructure account, referred to as Customer Cloud Subscription (CSS), are responsible to pre-purchase or provide Reserved Instance (RI) compute instances to ensure lower cloud infrastructure costs.
====

Additional resources can be purchased for an OpenShift Dedicated cluster, including:

* Additional nodes (can be different types and sizes through the use of machine pools)
* Middleware (JBoss EAP, JBoss Fuse, and so on) - additional pricing based on specific middleware component
* Additional storage in increments of 500 GB (non-CCS only; 100 GB included)
* Additional 12 TiB Network I/O (non-CCS only; 12 TB included)
* Load Balancers for Services are available in bundles of 4; enables non-HTTP/SNI traffic or non-standard ports (non-CCS only)
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="cluster-self-service_{context}"]
= Cluster self-service

[role="_abstract"]
Customers can create, scale, and delete their clusters from {cluster-manager-url}, provided that they have already purchased the necessary subscriptions.

Actions available in {cluster-manager-first} must not be directly performed from within the cluster as this might cause adverse affects, including having all actions automatically reverted.
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="cloud-providers_{context}"]
= Cloud providers

[role="_abstract"]
OpenShift Container Platform offers OpenShift Container Platform clusters as a managed service on the following cloud providers:

* Amazon Web Services (AWS)
* {gcp-first}
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="instance-types_{context}"]
= Instance types

[role="_abstract"]
Single availability zone clusters require a minimum of 2 worker nodes for Customer Cloud Subscription (CCS) clusters deployed to a single availability zone. A minimum of 4 worker nodes is required for non-CCS clusters. These 4 worker nodes are included in the base subscription.

Multiple availability zone clusters require a minimum of 3 worker nodes for Customer Cloud Subscription (CCS) clusters, 1 deployed to each of 3 availability zones. A minimum of 9 worker nodes are required for non-CCS clusters. These 9 worker nodes are included in the base subscription, and additional nodes must be purchased in multiples of 3 to maintain proper node distribution.

[NOTE]
====
All worker nodes within a single OpenShift Container Platform machine pool must be of the same type and size. However, worker nodes across multiple machine pools within an OpenShift Container Platform cluster can be of different types and sizes.
====

Control plane and infrastructure nodes are deployed and managed by Red{nbsp}Hat. There are at least 3 control plane nodes that handle etcd and API-related workloads. There are at least 2 infrastructure nodes that handle metrics, routing, the web console, and other workloads. You must not run any workloads on the control plane and infrastructure nodes. Any workloads you intend to run must be deployed on worker nodes.
[IMPORTANT]
====
Shutting down the underlying infrastructure through the cloud provider console is unsupported and can lead to data loss.
====

For more information about Red{nbsp}Hat workloads that must be deployed on worker nodes, see the _Red{nbsp}Hat Operator support_ section below.

[NOTE]
====
Approximately 1 vCPU core and 1 GiB of memory are reserved on each worker node and removed from allocatable resources. This is necessary to run processes required by the underlying platform. This includes system daemons such as udev, kubelet, container runtime, and so on, and also accounts for kernel reservations. {OCP} core systems such as audit log aggregation, metrics collection, DNS, image registry, SDN, and so on might consume additional allocatable resources to maintain the stability and maintainability of the cluster. The additional resources consumed might vary based on usage.
====

.Additional resources
* Red Hat Operator Support

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="aws-instance-types-ccs_{context}"]
= AWS instance types for Customer Cloud Subscription clusters

[role="_abstract"]
OpenShift Container Platform offers the following worker node instance types and sizes on AWS:

.General purpose
[%collapsible]
====
- m5.metal (96&#8224;  vCPU, 384 GiB)
- m5.xlarge (4 vCPU, 16 GiB)
- m5.2xlarge (8 vCPU, 32 GiB)
- m5.4xlarge (16 vCPU, 64 GiB)
- m5.8xlarge (32 vCPU, 128 GiB)
- m5.12xlarge (48 vCPU, 192 GiB)
- m5.16xlarge (64 vCPU, 256 GiB)
- m5.24xlarge (96 vCPU, 384 GiB)
- m5a.xlarge (4 vCPU, 16 GiB)
- m5a.2xlarge (8 vCPU, 32 GiB)
- m5a.4xlarge (16 vCPU, 64 GiB)
- m5a.8xlarge (32 vCPU, 128 GiB)
- m5a.12xlarge (48 vCPU, 192 GiB)
- m5a.16xlarge (64 vCPU, 256 GiB)
- m5a.24xlarge (96 vCPU, 384 GiB)
- m5ad.xlarge (4 vCPU, 16 GiB)
- m5ad.2xlarge (8 vCPU, 32 GiB)
- m5ad.4xlarge (16 vCPU, 64 GiB)
- m5ad.8xlarge (32 vCPU, 128 GiB)
- m5ad.12xlarge (48 vCPU, 192 GiB)
- m5ad.16xlarge (64 vCPU, 256 GiB)
- m5ad.24xlarge (96 vCPU, 384 GiB)
- m5d.metal (96&#8224;  vCPU, 384 GiB)
- m5d.xlarge (4 vCPU, 16 GiB)
- m5d.2xlarge (8 vCPU, 32 GiB)
- m5d.4xlarge (16 vCPU, 64 GiB)
- m5d.8xlarge (32 vCPU, 128 GiB)
- m5d.12xlarge (48 vCPU, 192 GiB)
- m5d.16xlarge (64 vCPU, 256 GiB)
- m5d.24xlarge (96 vCPU, 384 GiB)
- m5n.metal (96 vCPU, 384 GiB)
- m5n.xlarge (4 vCPU, 16 GiB)
- m5n.2xlarge (8 vCPU, 32 GiB)
- m5n.4xlarge (16 vCPU, 64 GiB)
- m5n.8xlarge (32 vCPU, 128 GiB)
- m5n.12xlarge (48 vCPU, 192 GiB)
- m5n.16xlarge (64 vCPU, 256 GiB)
- m5n.24xlarge (96 vCPU, 384 GiB)
- m5dn.metal (96 vCPU, 384 GiB)
- m5dn.xlarge (4 vCPU, 16 GiB)
- m5dn.2xlarge (8 vCPU, 32 GiB)
- m5dn.4xlarge (16 vCPU, 64 GiB)
- m5dn.8xlarge (32 vCPU, 128 GiB)
- m5dn.12xlarge (48 vCPU, 192 GiB)
- m5dn.16xlarge (64 vCPU, 256 GiB)
- m5dn.24xlarge (96 vCPU, 384 GiB)
- m5zn.metal (48 vCPU, 192 GiB)
- m5zn.xlarge (4 vCPU, 16 GiB)
- m5zn.2xlarge (8 vCPU, 32 GiB)
- m5zn.3xlarge (12 vCPU, 48 GiB)
- m5zn.6xlarge (24 vCPU, 96 GiB)
- m5zn.12xlarge (48 vCPU, 192 GiB)
- m6a.xlarge (4 vCPU, 16 GiB)
- m6a.2xlarge (8 vCPU, 32 GiB)
- m6a.4xlarge (16 vCPU, 64 GiB)
- m6a.8xlarge (32 vCPU, 128 GiB)
- m6a.12xlarge (48 vCPU, 192 GiB)
- m6a.16xlarge (64 vCPU, 256 GiB)
- m6a.24xlarge (96 vCPU, 384 GiB)
- m6a.32xlarge (128 vCPU, 512 GiB)
- m6a.48xlarge (192 vCPU, 768 GiB)
- m6i.metal (128 vCPU, 512 GiB)
- m6i.xlarge (4 vCPU, 16 GiB)
- m6i.2xlarge (8 vCPU, 32 GiB)
- m6i.4xlarge (16 vCPU, 64 GiB)
- m6i.8xlarge (32 vCPU, 128 GiB)
- m6i.12xlarge (48 vCPU, 192 GiB)
- m6i.16xlarge (64 vCPU, 256 GiB)
- m6i.24xlarge (96 vCPU, 384 GiB)
- m6i.32xlarge (128 vCPU, 512 GiB)
- m6id.xlarge (4 vCPU, 16 GiB)
- m6id.2xlarge (8 vCPU, 32 GiB)
- m6id.4xlarge (16 vCPU, 64 GiB)
- m6id.8xlarge (32 vCPU, 128 GiB)
- m6id.12xlarge (48 vCPU, 192 GiB)
- m6id.16xlarge (64 vCPU, 256 GiB)
- m6id.24xlarge (96 vCPU, 384 GiB)
- m6id.32xlarge (128 vCPU, 512 GiB)
- m7i.xlarge (4 vCPU, 16 GiB)
- m7i.2xlarge (8 vCPU, 32 GiB)
- m7i.4xlarge (16 vCPU, 64 GiB)
- m7i.8xlarge (32 vCPU, 128 GiB)
- m7i.12xlarge (48 vCPU, 192 GiB)
- m7i.16xlarge (64 vCPU, 256 GiB)
- m7i.24xlarge (96 vCPU, 384 GiB)
- m7i.48xlarge (192 vCPU, 768 GiB)
- m7i.metal-24xl (96 vCPU, 384 GiB)
- m7i.metal-48xl (192 vCPU, 768 GiB)
- m7i-flex.xlarge (4 vCPU, 16 GiB)
- m7i-flex.2xlarge (8 vCPU, 32 GiB)
- m7i-flex.4xlarge (16 vCPU, 64 GiB)
- m7i-flex.8xlarge (32 vCPU, 128 GiB)
- m7a.xlarge (4 vCPU, 16 GiB)
- m7a.2xlarge (8 vCPU, 32 GiB)
- m7a.4xlarge (16 vCPU, 64 GiB)
- m7a.8xlarge (32 vCPU, 128 GiB)
- m7a.12xlarge (48 vCPU, 192 GiB)
- m7a.16xlarge (64 vCPU, 256 GiB)
- m7a.24xlarge (96 vCPU, 384 GiB)
- m7a.32xlarge (128 vCPU, 512 GiB)
- m7a.48xlarge (192 vCPU, 768 GiB)
- m7a.metal-48xl (192 vCPU, 768 GiB)
- m8i.xlarge (4 vCPU, 16 GiB)
- m8i.2xlarge (8 vCPU, 32 GiB)
- m8i.4xlarge (16 vCPU, 64 GiB)
- m8i.8xlarge (32 vCPU, 128 GiB)
- m8i.12xlarge (48 vCPU, 192 GiB)
- m8i.16xlarge (64 vCPU, 256 GiB)
- m8i.24xlarge (96 vCPU, 384 GiB)
- m8i.32xlarge (128 vCPU, 512 GiB)
- m8i.48xlarge (192 vCPU, 768 GiB)
- m8i.96xlarge (384 vCPU, 1,536 GiB)
- m8i.metal-48xl (192 vCPU, 768 GiB)
- m8i.metal-96xl (384 vCPU, 1,536 GiB)
- m8i-flex.large (2 vCPU, 8 GiB)
- m8i-flex.xlarge (4 vCPU, 16 GiB)
- m8i-flex.2xlarge (8 vCPU, 32 GiB)
- m8i-flex.4xlarge (16 vCPU, 64 GiB)
- m8i-flex.8xlarge (32 vCPU, 128 GiB)
- m8i-flex.12xlarge (48 vCPU, 192 GiB)
- m8i-flex.16xlarge (64 vCPU, 256 GiB)
- m8a.xlarge (4 vCPU, 16 GiB)
- m8a.2xlarge (8 vCPU, 32 GiB)
- m8a.4xlarge (16 vCPU, 64 GiB)
- m8a.8xlarge (32 vCPU, 128 GiB)
- m8a.12xlarge (48 vCPU, 192 GiB)
- m8a.16xlarge (64 vCPU, 256 GiB)
- m8a.24xlarge (96 vCPU, 384 GiB)
- m8a.48xlarge (192 vCPU, 768 GiB)
- m8a.metal-24xl (96 vCPU, 384 GiB)
- m8a.metal-48xl (192 vCPU, 768 GiB)

&#8224; These instance types provide 96 logical processors on 48 physical cores. They run on single servers with two physical Intel sockets.
====

.Burstable general purpose
[%collapsible]
====
- t3.xlarge (4 vCPU, 16 GiB)
- t3.2xlarge (8 vCPU, 32 GiB)
- t3a.xlarge (4 vCPU, 16 GiB)
- t3a.2xlarge (8 vCPU, 32 GiB)
====

.Memory intensive
[%collapsible]
====
- u7i-6tb.112xlarge (448 vCPU, 6,144 GiB)
- u7i-8tb.112xlarge (448 vCPU, 6,144 GiB)
- u7i-12tb.224xlarge (896 vCPU, 12,288 GiB)
- u7in-16tb.224xlarge (896 vCPU, 16,384 GiB)
- u7in-24tb.224xlarge (896 vCPU, 24,576 GiB)
- u7in-32tb.224xlarge (896 vCPU, 32,768 GiB)
- u7inh-32tb.480xlarge (1920 vCPU, 32,768 GiB)
- x1.16xlarge (64 vCPU, 976 GiB)
- x1.32xlarge (128 vCPU, 1952 GiB)
- x1e.xlarge (4 vCPU, 122 GiB)
- x1e.2xlarge (8 vCPU, 244 GiB)
- x1e.4xlarge (16 vCPU, 488 GiB)
- x1e.8xlarge (32 vCPU, 976 GiB)
- x1e.16xlarge (64 vCPU, 1,952 GiB)
- x1e.32xlarge (128 vCPU, 3,904 GiB)
- x2idn.16xlarge (64 vCPU, 1024 GiB)
- x2idn.24xlarge (96 vCPU, 1536 GiB)
- x2idn.32xlarge (128 vCPU, 2048 GiB)
- x2iedn.xlarge (4 vCPU, 128 GiB)
- x2iedn.2xlarge (8 vCPU, 256 GiB)
- x2iedn.4xlarge (16 vCPU, 512 GiB)
- x2iedn.8xlarge (32 vCPU, 1024 GiB)
- x2iedn.16xlarge (64 vCPU, 2048 GiB)
- x2iedn.24xlarge (96 vCPU, 3072 GiB)
- x2iedn.32xlarge (128 vCPU, 4096 GiB)
- x2iezn.2xlarge (8 vCPU, 256 GiB)
- x2iezn.4xlarge (16vCPU, 512 GiB)
- x2iezn.6xlarge (24vCPU, 768 GiB)
- x2iezn.8xlarge (32vCPU, 1,024 GiB)
- x2iezn.12xlarge (48vCPU, 1,536 GiB)
- x2idn.metal (128vCPU, 2,048 GiB)
- x2iedn.metal (128vCPU, 4,096 GiB)
- x2iezn.metal (48 vCPU, 1,536 GiB)
====

.Memory optimized
[%collapsible]
====
- r4.xlarge (4 vCPU, 30.5 GiB)
- r4.2xlarge (8 vCPU, 61 GiB)
- r4.4xlarge (16 vCPU, 122 GiB)
- r4.8xlarge (32 vCPU, 244 GiB)
- r4.16xlarge (64 vCPU, 488 GiB)
- r5.metal (96&#8224; vCPU, 768 GiB)
- r5.xlarge (4 vCPU, 32 GiB)
- r5.2xlarge (8 vCPU, 64 GiB)
- r5.4xlarge (16 vCPU, 128 GiB)
- r5.8xlarge (32 vCPU, 256 GiB)
- r5.12xlarge (48 vCPU, 384 GiB)
- r5.16xlarge (64 vCPU, 512 GiB)
- r5.24xlarge (96 vCPU, 768 GiB)
- r5a.xlarge (4 vCPU, 32 GiB)
- r5a.2xlarge (8 vCPU, 64 GiB)
- r5a.4xlarge (16 vCPU, 128 GiB)
- r5a.8xlarge  (32 vCPU, 256 GiB)
- r5a.12xlarge (48 vCPU, 384 GiB)
- r5a.16xlarge (64 vCPU, 512 GiB)
- r5a.24xlarge (96 vCPU, 768 GiB)
- r5ad.xlarge (4 vCPU, 32 GiB)
- r5ad.2xlarge (8 vCPU, 64 GiB)
- r5ad.4xlarge (16 vCPU, 128 GiB)
- r5ad.8xlarge (32 vCPU, 256 GiB)
- r5ad.12xlarge (48 vCPU, 384 GiB)
- r5ad.16xlarge (64 vCPU, 512 GiB)
- r5ad.24xlarge (96 vCPU, 768 GiB)
- r5d.metal (96&#8224; vCPU, 768 GiB)
- r5d.xlarge (4 vCPU, 32 GiB)
- r5d.2xlarge (8 vCPU, 64 GiB)
- r5d.4xlarge (16 vCPU, 128 GiB)
- r5d.8xlarge (32 vCPU, 256 GiB)
- r5d.12xlarge (48 vCPU, 384 GiB)
- r5d.16xlarge (64 vCPU, 512 GiB)
- r5d.24xlarge (96 vCPU, 768 GiB)
- r5n.metal (96 vCPU, 768 GiB)
- r5n.xlarge (4 vCPU, 32 GiB)
- r5n.2xlarge (8 vCPU, 64 GiB)
- r5n.4xlarge (16 vCPU, 128 GiB)
- r5n.8xlarge (32 vCPU, 256 GiB)
- r5n.12xlarge (48 vCPU, 384 GiB)
- r5n.16xlarge (64 vCPU, 512 GiB)
- r5n.24xlarge (96 vCPU, 768 GiB)
- r5dn.metal (96 vCPU, 768 GiB)
- r5dn.xlarge (4 vCPU, 32 GiB)
- r5dn.2xlarge (8 vCPU, 64 GiB)
- r5dn.4xlarge (16 vCPU, 128 GiB)
- r5dn.8xlarge (32 vCPU, 256 GiB)
- r5dn.12xlarge (48 vCPU, 384 GiB)
- r5dn.16xlarge (64 vCPU, 512 GiB)
- r5dn.24xlarge (96 vCPU, 768 GiB)
- r6a.xlarge (4 vCPU, 32 GiB)
- r6a.2xlarge (8 vCPU, 64 GiB)
- r6a.4xlarge (16 vCPU, 128 GiB)
- r6a.8xlarge (32 vCPU, 256 GiB)
- r6a.12xlarge (48 vCPU, 384 GiB)
- r6a.16xlarge (64 vCPU, 512 GiB)
- r6a.24xlarge (96 vCPU, 768 GiB)
- r6a.32xlarge (128 vCPU, 1,024 GiB)
- r6a.48xlarge (192 vCPU, 1,536 GiB)
- r6a.metal	(192 vCPU, 1,536 GiB)
- r6i.metal (128 vCPU, 1,024 GiB)
- r6i.xlarge (4 vCPU, 32 GiB)
- r6i.2xlarge (8 vCPU, 64 GiB)
- r6i.4xlarge (16 vCPU, 128 GiB)
- r6i.8xlarge (32 vCPU, 256 GiB)
- r6i.12xlarge (48 vCPU, 384 GiB)
- r6i.16xlarge (64 vCPU, 512 GiB)
- r6i.24xlarge (96 vCPU, 768 GiB)
- r6i.32xlarge (128 vCPU, 1,024 GiB)
- r6id.xlarge (4 vCPU, 32 GiB)
- r6id.2xlarge (8 vCPU, 64 GiB)
- r6id.4xlarge (16 vCPU, 128 GiB)
- r6id.8xlarge (32 vCPU, 256 GiB)
- r6id.12xlarge (48 vCPU, 384 GiB)
- r6id.16xlarge (64 vCPU, 512 GiB)
- r6id.24xlarge (96 vCPU, 768 GiB)
- r6id.32xlarge (128 vCPU, 1,024 GiB)
- z1d.metal (48&#135; vCPU, 384 GiB)
- z1d.xlarge (4 vCPU, 32 GiB)
- z1d.2xlarge (8 vCPU, 64 GiB)
- z1d.3xlarge (12 vCPU, 96 GiB)
- z1d.6xlarge (24 vCPU, 192 GiB)
- z1d.12xlarge (48 vCPU, 384 GiB)
- r7a.xlarge (4 vCPU, 32 GiB)
- r7a.2xlarge (8 vCPU, 64 GiB)
- r7a.4xlarge  (16 vCPU, 128 GiB)
- r7a.8xlarge (32 vCPU, 256 GiB)
- r7a.12xlarge (48 vCPU, 384 GiB)
- r7a.16xlarge (64 vCPU, 512 GiB)
- r7a.24xlarge (96 vCPU, 768 GiB)
- r7a.32xlarge (128 vCPU, 1024 GiB)
- r7a.48xlarge (192 vCPU, 1536 GiB)
- r7a.metal-48xl (192 vCPU, 1536 GiB)
- r7i.xlarge (4 vCPU, 32 GiB)
- r7i.2xlarge (8 vCPU, 64 GiB)
- r7i.4xlarge (16 vCPU, 128 GiB)
- r7i.8xlarge (32 vCPU, 256 GiB)
- r7i.12xlarge (48 vCPU, 384 GiB)
- r7i.16xlarge (64 vCPU, 512 GiB)
- r7i.24xlarge (96 vCPU, 768 GiB)
- r7i.metal-24xl (96 vCPU, 768 GiB)
- r7iz.xlarge (4 vCPU, 32 GiB)
- r7iz.2xlarge (8 vCPU, 64 GiB)
- r7iz.4xlarge (16 vCPU, 128 GiB)
- r7iz.8xlarge (32 vCPU, 256 GiB)
- r7iz.12xlarge (48 vCPU, 384 GiB)
- r7iz.16xlarge (64 vCPU, 512 GiB)
- r7iz.32xlarge (128 vCPU, 1024 GiB)
- r7iz.metal-16xl (64 vCPU, 512 GiB)
- r7iz.metal-32xl (128 vCPU, 1024 GiB)
- r8i.xlarge (4 vCPU, 32 GiB)
- r8i.2xlarge (8 vCPU, 64 GiB)
- r8i.4xlarge (16 vCPU, 128 GiB)
- r8i.8xlarge (32 vCPU, 256 GiB)
- r8i.12xlarge (48 vCPU, 384 GiB)
- r8i.16xlarge (64 vCPU, 512 GiB)
- r8i.24xlarge (96 vCPU, 768 GiB)
- r8i.32xlarge (128 vCPU, 1,024 GiB)
- r8i.48xlarge (192 vCPU, 1,536 GiB)
- r8i.96xlarge (384 vCPU, 3,072 GiB)
- r8i.metal-48xl (192 vCPU, 1,536 GiB)
- r8i.metal-96xl (384 vCPU, 3,072 GiB)
- r8i-flex.xlarge (4 vCPU, 32 GiB)
- r8i-flex.2xlarge (8 vCPU, 64 GiB)
- r8i-flex.4xlarge (16 vCPU, 128 GiB)
- r8i-flex.8xlarge (32 vCPU, 256 GiB)
- r8i-flex.12xlarge (48 vCPU, 384 GiB)
- r8i-flex.16xlarge (64 vCPU, 512 GiB)

&#8224; These instance types provide 96 logical processors on 48 physical cores. They run on single servers with two physical Intel sockets.

&#135; This instance type provides 48 logical processors on 24 physical cores.
====
.Accelerated computing
[%collapsible]
====
- p3.2xlarge (8 vCPU, 61 GiB)
- p3.8xlarge (32 vCPU, 244 GiB)
- p3.16xlarge (64 vCPU, 488 GiB)
- p3dn.24xlarge (96 vCPU, 768 GiB)
- p4d.24xlarge (96 vCPU, 1,152 GiB)
- p4de.24xlarge (96 vCPU, 1,152 GiB)
- p5.48xlarge (192 vCPU, 2,048 GiB)
- p5.4xlarge (16 vCPU, 256 GiB)
- p5e.48xlarge (192 vCPU, 2,048 GiB)
- p5en.48xlarge (192 vCPU, 2,048 GiB)
- g4ad.xlarge (4 vCPU, 16 GiB)
- g4ad.2xlarge (8 vCPU, 32 GiB)
- g4ad.4xlarge (16 vCPU, 64 GiB)
- g4ad.8xlarge (32 vCPU, 128 GiB)
- g4ad.16xlarge (64 vCPU, 256 GiB)
- g4dn.xlarge (4 vCPU, 16 GiB)
- g4dn.2xlarge (8 vCPU, 32 GiB)
- g4dn.4xlarge (16 vCPU, 64 GiB)
- g4dn.8xlarge (32 vCPU, 128 GiB)
- g4dn.12xlarge (48 vCPU, 192 GiB)
- g4dn.16xlarge (64 vCPU, 256 GiB)
- g4dn.metal (96 vCPU, 384 GiB)
- g5.xlarge (4 vCPU, 16 GiB)
- g5.2xlarge (8 vCPU, 32 GiB)
- g5.4xlarge (16 vCPU, 64 GiB)
- g5.8xlarge (32 vCPU, 128 GiB)
- g5.16xlarge (64 vCPU, 256 GiB)
- g5.12xlarge (48 vCPU, 192 GiB)
- g5.24xlarge (96 vCPU, 384 GiB)
- g5.48xlarge (192 vCPU, 768 GiB)
- dl1.24xlarge  (96 vCPU, 768 GiB)&#8224;
- g6.xlarge (4 vCPU, 16 GiB)
- g6.2xlarge (8 vCPU, 32 GiB)
- g6.4xlarge (16 vCPU,	64 GiB)
- g6.8xlarge (32 vCPU, 128 GiB)
- g6.12xlarge (48 vCPU, 192 GiB)
- g6.16xlarge (64 vCPU, 256 GiB)
- g6.24xlarge (96 vCPU, 384 GiB)
- g6.48xlarge (192 vCPU, 768 GiB)
- g6e.xlarge (4 vCPU, 32 GiB)
- g6e.2xlarge (8 vCPU, 64 GiB)
- g6e.4xlarge (16 vCPU, 128 GiB)
- g6e.8xlarge (32 vCPU, 256 GiB)
- g6e.12xlarge (48 vCPU, 384 GiB)
- g6e.16xlarge (64 vCPU, 512 GiB)
- g6e.24xlarge (96 vCPU, 768 GiB)
- g6e.48xlarge (192 vCPU, 1,536 GiB)
- gr6.4xlarge (16 vCPU, 128 GiB)
- gr6.8xlarge (32 vCPU, 256 GiB)

&#8224; Intel specific; not covered by Nvidia

Support for the GPU instance type software stack is provided by AWS. Ensure that your AWS service quotas can accommodate the desired GPU instance types.
====
.Compute optimized
[%collapsible]
====
- c5.metal (96 vCPU, 192 GiB)
- c5.xlarge (4 vCPU, 8 GiB)
- c5.2xlarge (8 vCPU, 16 GiB)
- c5.4xlarge (16 vCPU, 32 GiB)
- c5.9xlarge (36 vCPU, 72 GiB)
- c5.12xlarge (48 vCPU, 96 GiB)
- c5.18xlarge (72 vCPU, 144 GiB)
- c5.24xlarge (96 vCPU, 192 GiB)
- c5d.metal (96 vCPU, 192 GiB)
- c5d.xlarge (4 vCPU, 8 GiB)
- c5d.2xlarge (8 vCPU, 16 GiB)
- c5d.4xlarge (16 vCPU, 32 GiB)
- c5d.9xlarge (36 vCPU, 72 GiB)
- c5d.12xlarge (48 vCPU, 96 GiB)
- c5d.18xlarge (72 vCPU, 144 GiB)
- c5d.24xlarge (96 vCPU, 192 GiB)
- c5a.xlarge (4 vCPU, 8 GiB)
- c5a.2xlarge (8 vCPU, 16 GiB)
- c5a.4xlarge (16 vCPU, 32 GiB)
- c5a.8xlarge (32 vCPU, 64 GiB)
- c5a.12xlarge (48 vCPU, 96 GiB)
- c5a.16xlarge (64 vCPU, 128 GiB)
- c5a.24xlarge (96 vCPU, 192 GiB)
- c5ad.xlarge (4 vCPU, 8 GiB)
- c5ad.2xlarge (8 vCPU, 16 GiB)
- c5ad.4xlarge (16 vCPU, 32 GiB)
- c5ad.8xlarge (32 vCPU, 64 GiB)
- c5ad.12xlarge (48 vCPU, 96 GiB)
- c5ad.16xlarge (64 vCPU, 128 GiB)
- c5ad.24xlarge (96 vCPU, 192 GiB)
- c5n.metal (72 vCPU, 192 GiB)
- c5n.xlarge (4 vCPU, 10.5 GiB)
- c5n.2xlarge (8 vCPU, 21 GiB)
- c5n.4xlarge (16 vCPU, 42 GiB)
- c5n.9xlarge (36 vCPU, 96 GiB)
- c5n.18xlarge (72 vCPU, 192 GiB)
- c6a.xlarge (4 vCPU, 8 GiB)
- c6a.2xlarge (8 vCPU, 16 GiB)
- c6a.4xlarge (16 vCPU, 32 GiB)
- c6a.8xlarge (32 vCPU, 64 GiB)
- c6a.12xlarge (48 vCPU, 96 GiB)
- c6a.16xlarge (64 vCPU, 128 GiB)
- c6a.24xlarge (96 vCPU, 192 GiB)
- c6a.32xlarge (128 vCPU, 256 GiB)
- c6a.48xlarge (192 vCPU, 384 GiB)
- c6a.metal	(192 vCPU, 384 GiB)
- c6i.metal (128 vCPU, 256 GiB)
- c6i.xlarge (4 vCPU, 8 GiB)
- c6i.2xlarge (8 vCPU, 16 GiB)
- c6i.4xlarge (16 vCPU, 32 GiB)
- c6i.8xlarge (32 vCPU, 64 GiB)
- c6i.12xlarge (48 vCPU, 96 GiB)
- c6i.16xlarge (64 vCPU, 128 GiB)
- c6i.24xlarge (96 vCPU, 192 GiB)
- c6i.32xlarge (128 vCPU, 256 GiB)
- c6id.xlarge (4 vCPU, 8 GiB)
- c6id.2xlarge (8 vCPU, 16 GiB)
- c6id.4xlarge (16 vCPU, 32 GiB)
- c6id.8xlarge (32 vCPU, 64 GiB)
- c6id.12xlarge (48 vCPU, 96 GiB)
- c6id.16xlarge (64 vCPU, 128 GiB)
- c6id.24xlarge (96 vCPU, 192 GiB)
- c6id.32xlarge (128 vCPU, 256 GiB)
- c7a.xlarge (4 vCPU, 8 GiB)
- c7a.2xlarge (8 vCPU, 16 GiB)
- c7a.4xlarge (16 vCPU, 32 GiB)
- c7a.8xlarge (32 vCPU, 64 GiB)
- c7a.12xlarge (48 vCPU, 96 GiB)
- c7a.16xlarge (64 vCPU, 128 GiB)
- c7a.24xlarge (96 vCPU, 192 GiB)
- c7a.32xlarge (128 vCPU, 256 GiB)
- c7a.48xlarge (192 vCPU, 384 GiB)
- c7a.metal-48xl (192 vCPU, 384 GiB)
- c7i.xlarge (4 vCPU, 8 GiB)
- c7i.2xlarge (8 vCPU, 16 GiB)
- c7i.4xlarge (16 vCPU, 32 GiB)
- c7i.8xlarge (32 vCPU, 64 GiB)
- c7i.12xlarge (48 vCPU, 96 GiB)
- c7i.16xlarge (64 vCPU, 128 GiB)
- c7i.24xlarge (96 vCPU, 192 GiB)
- c7i.48xlarge (192 vCPU, 384 GiB)
- c7i-flex.xlarge (4 vCPU, 8 GiB)
- c7i-flex.2xlarge (8 vCPU, 16 GiB)
- c7i-flex.4xlarge (16 vCPU, 32 GiB)
- c7i-flex.8xlarge (32 vCPU, 64 GiB)
- c7i.metal-24xl (96 vCPU, 192 GiB)
- c7i.metal-48xl (192 vCPU, 384 GiB)
- c8i.xlarge (4 vCPU, 8 GiB)
- c8i.2xlarge (8 vCPU, 16 GiB)
- c8i.4xlarge (16 vCPU, 32 GiB)
- c8i.8xlarge (32 vCPU, 64 GiB)
- c8i.12xlarge (48 vCPU, 96 GiB)
- c8i.16xlarge (64 vCPU, 128 GiB)
- c8i.24xlarge (96 vCPU, 192 GiB)
- c8i.32xlarge (128 vCPU, 256 GiB)
- c8i.48xlarge (192 vCPU, 384 GiB)
- c8i.96xlarge (384 vCPU, 768 GiB)
- c8i.metal-48xl (192 vCPU, 384 GiB)
- c8i.metal-96xl (384 vCPU, 768 GiB)
- c8i-flex.xlarge (4 vCPU, 8 GiB)
- c8i-flex.2xlarge (8 vCPU, 16 GiB)
- c8i-flex.4xlarge (16 vCPU, 48 GiB)
- c8i-flex.8xlarge (32 vCPU, 64 GiB)
- c8i-flex.12xlarge (48 vCPU, 96 GiB)
- c8i-flex.16xlarge (64 vCPU, 128 GiB)
- hpc6a.48xlarge (96 vCPU, 384 GiB)
- hpc6id.32xlarge (64 vCPU, 1024 GiB)
- hpc7a.12xlarge (24 vCPU, 768 GiB)
- hpc7a.24xlarge (48 vCPU, 768 GiB)
- hpc7a.48xlarge (96 vCPU, 768 GiB)
- hpc7a.96xlarge (192 vCPU, 768 GiB)
====

.Storage optimized
[%collapsible]
====
- i3.metal (72&#8224; vCPU, 512 GiB)
- i3.xlarge	(4 vCPU, 30.5 GiB)
- i3.2xlarge (8 vCPU, 61 GiB)
- i3.4xlarge (16 vCPU, 122 GiB)
- i3.8xlarge (32 vCPU, 244 GiB)
- i3.16xlarge (64 vCPU, 488 GiB)
- i3en.metal (96 vCPU, 768 GiB)
- i3en.xlarge (4 vCPU, 32 GiB)
- i3en.2xlarge (8 vCPU, 64 GiB)
- i3en.3xlarge (12 vCPU, 96 GiB)
- i3en.6xlarge (24 vCPU, 192 GiB)
- i3en.12xlarge (48 vCPU, 384 GiB)
- i3en.24xlarge (96 vCPU, 768 GiB)
- i4i.xlarge (4 vCPU, 32 GiB)
- i4i.2xlarge (8 vCPU, 64 GiB)
- i4i.4xlarge (16 vCPU, 128 GiB)
- i4i.8xlarge (32 vCPU, 256 GiB)
- i4i.12xlarge (48 vCPU, 384 GiB)
- i4i.16xlarge (64 vCPU, 512 GiB)
- i4i.24xlarge (96 vCPU, 768 GiB)
- i4i.32xlarge (128 vCPU, 1024 GiB)
- i4i.metal (128 vCPU, 1024 GiB)

&#8224; This instance type provides 72 logical processors on 36 physical cores.
====

[NOTE]
====
Virtual instance types initialize faster than ".metal" instance types.
====

.High memory
[%collapsible]
====
- u-3tb1.56xlarge (224 vCPU, 3,072 GiB)
- u-6tb1.56xlarge (224 vCPU, 6,144 GiB)
- u-6tb1.112xlarge (448 vCPU, 6,144 GiB)
- u-6tb1.metal (448 vCPU, 6,144 GiB)
- u-9tb1.112xlarge (448 vCPU, 9,216 GiB)
- u-9tb1.metal (448 vCPU, 9,216 GiB)
- u-12tb1.112xlarge (448 vCPU, 12,288 GiB)
- u-12tb1.metal (448 vCPU, 12,288 GiB)
- u-18tb1.metal (448 vCPU, 18,432 GiB)
- u-24tb1.metal (448 vCPU, 24,576 GiB)
====

.High performance compute
[%collapsible]
====
- hpc6a.48xlarge (96 vCPU, 384 GiB)
====
[role="_additional-resources-instance-types"]
.Additional resources

* AWS Instance Types

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="aws-instance-types-non-ccs_{context}"]
= AWS instance types for non-CCS clusters

[role="_abstract"]
OpenShift Container Platform offers the following worker node types and sizes on AWS:

.General purpose
[%collapsible]
====
- m5.xlarge (4 vCPU, 16 GiB)
- m5.2xlarge (8 vCPU, 32 GiB)
- m5.4xlarge (16 vCPU, 64 GiB)
====

.Memory-optimized
[%collapsible]
====
- r5.xlarge (4 vCPU, 32 GiB)
- r5.2xlarge (8 vCPU, 64 GiB)
- r5.4xlarge (16 vCPU, 128 GiB)
====

.Compute-optimized
[%collapsible]
====
- c5.2xlarge (8 vCPU, 16 GiB)
- c5.4xlarge (16 vCPU, 32 GiB)
====
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="gcp-compute-types_{context}"]
= {gcp-full} instance types

[role="_abstract"]
OpenShift Container Platform offers the following worker node types and sizes on {gcp-full} that are chosen to have a common CPU and memory capacity that are the same as other cloud instance types:
[NOTE]
====

`a2`, `a3`, `e2`, `c3`, `n4`, `c2d`, `c3d`, `g2`, `g4`, `n2d`, and `t2d` instance types are available for clusters created with the Customer Cloud Subscription (CCS) infrastructure type only.

`custom`, `c2`, and `n2` instance types are available for clusters created with both CCS and Red{nbsp}Hat cloud account infrastructure types.

`g2` and `g4` instance types are available for OpenShift Container Platform version 4.21 and later.

`c3` and `n4` instance types are available for OpenShift Container Platform version 4.18 and later.
====

.General purpose
[%collapsible]
====
* custom-4-16384 (4 vCPU, 16 GiB)
* custom-8-32768 (8 vCPU, 32 GiB)
* custom-16-65536 (16 vCPU, 64 GiB)
* custom-32-131072 (32 vCPU, 128 GiB)
* custom-48-199608 (48 vCPU, 192 GiB)
* custom-64-262144 (64 vCPU, 256 GiB)
* custom-96-393216 (96 vCPU, 384 GiB)
* c2d-standard-4 (4 vCPU, 16 GiB)
* c2d-standard-8 (8 vCPU, 32 GiB)
* c2d-standard-16 (16 vCPU, 64 GiB)
* c2d-standard-32 (32 vCPU, 128 GiB)
* c2d-standard-56 (56 vCPU, 224 GiB)
* c2d-standard-112 (112 vCPU, 448 GiB)
* c3-standard-192-metal (192 vCPU, 768 GiB)
* c3d-standard-4 (4 vCPU, 16 GiB)
* c3d-standard-8 (8 vCPU, 32 GiB)
* c3d-standard-16 (16 vCPU, 64 GiB)
* c3d-standard-30 (30 vCPU, 120 GiB)
* c3d-standard-60 (60 vCPU, 240 GiB)
* c3d-standard-90 (90 vCPU, 360 GiB)
* c3d-standard-180 (180 vCPU, 720 GiB)
* c3d-standard-360 (360 vCPU, 1440 GiB)
* c3d-standard-8-lssd (8 vCPU, 32 GiB)
* c3d-standard-16-lssd (16 vCPU, 64 GiB)
* c3d-standard-30-lssd (30 vCPU, 120 GiB)
* c3d-standard-60-lssd (60 vCPU, 240 GiB)
* c3d-standard-90-lssd (90 vCPU, 360 GiB)
* c3d-standard-180-lssd (180 vCPU, 720 GiB)
* c3d-standard-360-lssd (360 vCPU, 1440 GiB)
* e2-standard-4 (4 vCPU, 16 GiB)
* e2-standard-8 (8 vCPU, 32 GiB)
* e2-standard-16 (16 vCPU, 64 GiB)
* e2-standard-32 (32 vCPU, 128 GiB)
* n2-standard-4 (4 vCPU, 16 GiB)
* n2-standard-8 (8 vCPU, 32 GiB)
* n2-standard-16 (16 vCPU, 64 GiB)
* n2-standard-32 (32 vCPU, 128 GiB)
* n2-standard-48 (48 vCPU, 192 GiB)
* n2-standard-64 (64 vCPU, 256 GiB)
* n2-standard-80 (80 vCPU, 320 GiB)
* n2-standard-96 (96 vCPU, 384 GiB)
* n2-standard-128 (128 vCPU, 512 GiB)
* n2d-standard-4 (4 vCPU, 16 GiB)
* n2d-standard-8 (8 vCPU, 32 GiB)
* n2d-standard-16 (16 vCPU, 64 GiB)
* n2d-standard-32 (32 vCPU, 128 GiB)
* n2d-standard-48 (48 vCPU, 192 GiB)
* n2d-standard-64 (64 vCPU, 256 GiB)
* n2d-standard-80 (80 vCPU, 320 GiB)
* n2d-standard-96 (96 vCPU, 384 GiB)
* n2d-standard-128 (128 vCPU, 512 GiB)
* n2d-standard-224 (224 vCPU, 896 GiB)
* n4-standard-4 (4 vCPU, 16 GiB)
* n4-standard-8 (8 vCPU, 32 GiB)
* n4-standard-16 (16 vCPU, 64 GiB)
* n4-standard-32 (32 vCPU, 128 GiB)
* n4-standard-48 (48 vCPU, 192 GiB)
* n4-standard-64 (64 vCPU, 256 GiB)
* n4-standard-80 (80 vCPU, 320 GiB)
* t2d-standard-4 (4 vCPU, 16 GiB)
* t2d-standard-8 (8 vCPU, 32 GiB)
* t2d-standard-16 (16 vCPU, 64 GiB)
* t2d-standard-32 (32 vCPU, 128 GiB)
* t2d-standard-48 (48 vCPU, 192 GiB)
* t2d-standard-60 (60 vCPU, 240 GiB)
====

.Memory-optimized
[%collapsible]
====
* custom-4-32768-ext (4 vCPU, 32 GiB)
* custom-8-65536-ext (8 vCPU, 64 GiB)
* custom-16-131072-ext (16 vCPU, 128 GiB)
* c2d-highmem-4 (4 vCPU, 32 GiB)
* c2d-highmem-8 (8 vCPU, 64 GiB)
* c2d-highmem-16 (16 vCPU, 128 GiB)
* c2d-highmem-32 (32 vCPU, 256 GiB)
* c2d-highmem-56 (56 vCPU, 448 GiB)
* c2d-highmem-112 (112 vCPU, 896 GiB)
* c3-highmem-192-metal (192 vCPU, 1536 GiB)
* c3d-highmem-4 (4 vCPU, 32 GiB)
* c3d-highmem-8 (8 vCPU, 64 GiB)
* c3d-highmem-16 (16 vCPU, 128 GiB)
* c3d-highmem-30 (30 vCPU, 240 GiB)
* c3d-highmem-60 (60 vCPU, 480 GiB)
* c3d-highmem-90 (90 vCPU, 720 GiB)
* c3d-highmem-180 (180 vCPU, 1440 GiB)
* c3d-highmem-360 (360 vCPU, 2880 GiB)
* c3d-highmem-8-lssd (8 vCPU, 64 GiB)
* c3d-highmem-16-lssd (16 vCPU, 128 GiB)
* c3d-highmem-30-lssd (30 vCPU, 240 GiB)
* c3d-highmem-60-lssd (60 vCPU, 480 GiB)
* c3d-highmem-90-lssd (90 vCPU, 720 GiB)
* c3d-highmem-180-lssd (180 vCPU, 1440 GiB)
* c3d-highmem-360-lssd (360 vCPU, 2880 GiB)
* e2-highmem-4 (4 vCPU, 32 GiB)
* e2-highmem-8 (8 vCPU, 64 GiB)
* e2-highmem-16 (16 vCPU, 128 GiB)
* n2-highmem-4 (4 vCPU, 32 GiB)
* n2-highmem-8 (8 vCPU, 64 GiB)
* n2-highmem-16 (16 vCPU, 128 GiB)
* n2-highmem-32 (32 vCPU, 256 GiB)
* n2-highmem-48 (48 vCPU, 384 GiB)
* n2-highmem-64 (64 vCPU, 512 GiB)
* n2-highmem-80 (80 vCPU, 640 GiB)
* n2-highmem-96 (96 vCPU, 768 GiB)
* n2-highmem-128 (128 vCPU, 864 GiB)
* n2d-highmem-4 (4 vCPU, 32 GiB)
* n2d-highmem-8 (8 vCPU, 64 GiB)
* n2d-highmem-16 (16 vCPU, 128 GiB)
* n2d-highmem-32 (32 vCPU, 256 GiB)
* n2d-highmem-48 (48 vCPU, 384 GiB)
* n2d-highmem-64 (64 vCPU, 512 GiB)
* n2d-highmem-80 (80 vCPU, 640 GiB)
* n2d-highmem-96 (96 vCPU, 768 GiB)
* n4-highmem-4 (4 vCPU, 32 GiB)
* n4-highmem-8 (8 vCPU, 64 GiB)
* n4-highmem-16 (16 vCPU, 128 GiB)
* n4-highmem-32 (32 vCPU, 256 GiB)
* n4-highmem-48 (48 vCPU, 384 GiB)
* n4-highmem-64 (64 vCPU, 512 GiB)
* n4-highmem-80 (80 vCPU, 640 GiB)
====

.Compute-optimized
[%collapsible]
====
* custom-8-16384 (8 vCPU, 16 GiB)
* custom-16-32768 (16 vCPU, 32 GiB)
* custom-36-73728 (36 vCPU, 72 GiB)
* custom-48-98304 (48 vCPU, 96 GiB)
* custom-72-147456 (72 vCPU, 144 GiB)
* custom-96-196608 (96 vCPU, 192 GiB)
* c2-standard-4 (4 vCPU, 16 GiB)
* c2-standard-8 (8 vCPU, 32 GiB)
* c2-standard-16 (16 vCPU, 64 GiB)
* c2-standard-30 (30 vCPU, 120 GiB)
* c2-standard-60 (60 vCPU, 240 GiB)
* c2d-highcpu-4 (4 vCPU, 8 GiB)
* c2d-highcpu-8 (8 vCPU, 16 GiB)
* c2d-highcpu-16 (16 vCPU, 32 GiB)
* c2d-highcpu-32 (32 vCPU, 64 GiB)
* c2d-highcpu-56 (56 vCPU, 112 GiB)
* c2d-highcpu-112 (112 vCPU, 224 GiB)
* c3-highcpu-192-metal (192 vCPU, 512 GiB)
* c3d-highcpu-4 (4 vCPU, 8 GiB)
* c3d-highcpu-8 (8 vCPU, 16 GiB)
* c3d-highcpu-16 (16 vCPU, 32 GiB)
* c3d-highcpu-30 (30 vCPU, 60 GiB)
* c3d-highcpu-60 (60 vCPU, 120 GiB)
* c3d-highcpu-90 (90 vCPU, 180 GiB)
* c3d-highcpu-180 (180 vCPU, 360 GiB)
* c3d-highcpu-360 (360 vCPU, 720 GiB)
* e2-highcpu-8 (8 vCPU, 8 GiB)
* e2-highcpu-16 (16 vCPU, 16 GiB)
* e2-highcpu-32 (32 vCPU, 32 GiB)
* n2-highcpu-8 (8 vCPU, 8 GiB)
* n2-highcpu-16 (16 vCPU, 16 GiB)
* n2-highcpu-32 (32 vCPU, 32 GiB)
* n2-highcpu-48 (48 vCPU, 48 GiB)
* n2-highcpu-64 (64 vCPU, 64 GiB)
* n2-highcpu-80 (80 vCPU, 80 GiB)
* n2-highcpu-96 (96 vCPU, 96 GiB)
* n2d-highcpu-4 (4 vCPU, 4 GiB)
* n2d-highcpu-8 (8 vCPU, 8 GiB)
* n2d-highcpu-16 (16 vCPU, 16 GiB)
* n2d-highcpu-32 (32 vCPU, 32 GiB)
* n2d-highcpu-48 (48 vCPU, 48 GiB)
* n2d-highcpu-64 (64 vCPU, 64 GiB)
* n2d-highcpu-80 (80 vCPU, 80 GiB)
* n2d-highcpu-96 (96 vCPU, 96 GiB)
* n2d-highcpu-128 (128 vCPU, 128 GiB)
* n2d-highcpu-224 (224 vCPU, 224 GiB)
* n4-highcpu-4 (4 vCPU, 8 GiB)
* n4-highcpu-8 (8 vCPU, 16 GiB)
* n4-highcpu-16 (16 vCPU, 32 GiB)
* n4-highcpu-32 (32 vCPU, 64 GiB)
* n4-highcpu-48 (48 vCPU, 96 GiB)
* n4-highcpu-64 (64 vCPU, 128 GiB)
* n4-highcpu-80 (80 vCPU, 160 GiB)
====

.Accelerated computing
[%collapsible]
====
* a2-highgpu-1g (12 vCPU, 85 GiB)
* a2-highgpu-2g (24 vCPU, 170 GiB)
* a2-highgpu-4g (48 vCPU, 340 GiB)
* a2-highgpu-8g (96 vCPU, 680 GiB)
* a2-megagpu-16g (96 vCPU, 1.33 TiB)
* a2-ultragpu-1g (12 vCPU, 170 GiB)
* a2-ultragpu-2g (24 vCPU, 340 GiB)
* a2-ultragpu-4g (48 vCPU, 680 GiB)
* a2-ultragpu-8g (96 vCPU, 1360 GiB)
* a3-highgpu-1g (26 vCPU, 234 GiB)
* a3-highgpu-2g (52 vCPU, 468 GiB)
* a3-highgpu-4g (104 vCPU, 936 GiB)
* a3-highgpu-8g (208 vCPU, 1872 GiB)
* a3-megagpu-8g (208 vCPU, 1872 GiB)
* a3-edgegpu-8g (208 vCPU, 1872 GiB)
* g2-standard-4 (4 vCPU, 16 GiB)
* g2-standard-8 (8 vCPU, 32 GiB)
* g2-standard-12 (12 vCPU, 48 GiB)
* g2-standard-16 (16 vCPU, 64 GiB)
* g2-standard-24 (24 vCPU, 96 GiB)
* g2-standard-32 (32 vCPU, 128 GiB)
* g2-standard-48 (48 vCPU, 192 GiB)
* g2-standard-96 (96 vCPU, 384 GiB)
* g4-standard-6 (6 vCPU, 22 GiB)
* g4-standard-12 (12 vCPU, 45 GiB)
* g4-standard-24 (24 vCPU, 90 GiB)
* g4-standard-48 (48 vCPU, 180 GiB)
* g4-standard-96 (96 vCPU, 360 GiB)
* g4-standard-192 (192 vCPU, 720 GiB)
* g4-standard-384 (384 vCPU, 1440 GiB)
====
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="regions-availability-zones_{context}"]
= Regions and availability zones

[role="_abstract"]
The following regions are supported by {OCP} 4 and are supported for OpenShift Container Platform.

[id="aws-regions-availability-zones_{context}"]
== AWS regions and availability zones
The following AWS regions are supported by {OCP} 4 and are supported for OpenShift Container Platform:

* af-south-1 (Cape Town, AWS opt-in required)
* ap-east-1 (Hong Kong, AWS opt-in required)
* ap-northeast-1 (Tokyo)
* ap-northeast-2 (Seoul)
* ap-northeast-3 (Osaka)
* ap-south-1 (Mumbai)
* ap-south-2 (Hyderabad, AWS opt-in required)
* ap-southeast-1 (Singapore)
* ap-southeast-2 (Sydney)
* ap-southeast-3 (Jakarta, AWS opt-in required)
* ap-southeast-4 (Melbourne, AWS opt-in required)
* ca-central-1 (Central Canada)
* eu-central-1 (Frankfurt)
* eu-central-2 (Zurich, AWS opt-in required)
* eu-north-1 (Stockholm)
* eu-south-1 (Milan, AWS opt-in required)
* eu-south-2 (Spain, AWS opt-in required)
* eu-west-1 (Ireland)
* eu-west-2 (London)
* eu-west-3 (Paris)
* me-central-1 (UAE, AWS opt-in required)
* me-south-1 (Bahrain, AWS opt-in required)
* sa-east-1 (São Paulo)
* us-east-1 (N. Virginia)
* us-east-2 (Ohio)
* us-west-1 (N. California)
* us-west-2 (Oregon)

[id="gcp-regions-availability-zones_{context}"]
== {gcp-full} regions and availability zones
The following {gcp-full} regions are currently supported:

* asia-east1, Changhua County, Taiwan
* asia-east2, Hong Kong
* asia-northeast1, Tokyo, Japan
* asia-northeast2, Osaka, Japan
* asia-south1, Mumbai, India
* asia-south2, Delhi, India
* asia-southeast1, Jurong West, Singapore
* australia-southeast1, Sydney, Australia
* australia-southeast2, Melbourne, Australia
* europe-north1, Hamina, Finland
* europe-west1, St. Ghislain, Belgium
* europe-west2, London, England, UK
* europe-west3, Frankfurt, Germany
* europe-west4, Eemshaven, Netherlands
* europe-west6, Zürich, Switzerland
* europe-west8, Milan, Italy
* europe-west12, Turin, Italy
* europe-southwest1, Madrid, Spain
* northamerica-northeast1, Montréal, Québec, Canada
* southamerica-east1, Osasco (São Paulo), Brazil
* southamerica-west1, Santiago, Chile
* us-central1, Council Bluffs, Iowa, USA
* us-east1, Moncks Corner, South Carolina, USA
* us-east4, Ashburn, Northern Virginia, USA
* us-west1, The Dalles, Oregon, USA
* us-west2, Los Angeles, California, USA
* me-central1, Doha, Qatar
* me-central2, Dammam, Saudi Arabia

Multi-AZ clusters can only be deployed in regions with at least 3 availability zones (see AWS and {gcp-full}).

Each new OpenShift Container Platform cluster is installed within a dedicated Virtual Private Cloud (VPC) in a single Region, with the option to deploy into a single Availability Zone (Single-AZ) or across multiple Availability Zones (Multi-AZ). This provides cluster-level network and resource isolation, and enables cloud-provider VPC settings, such as VPN connections and VPC Peering. Persistent volumes are backed by cloud block storage and are specific to the availability zone in which they are provisioned. Persistent volumes do not bind to a volume until the associated pod resource is assigned into a specific availability zone in order to prevent unschedulable pods. Availability zone-specific resources are only usable by resources in the same availability zone.

[WARNING]
====
The region and the choice of single or multi availability zone cannot be changed once a cluster has been deployed.
====
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="sla_{context}"]
= Service level agreement (SLA)

[role="_abstract"]
Any SLAs for the service itself are defined in Appendix 4 of the Red Hat Enterprise Agreement Appendix 4 (Online Subscription Services).
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="limited-support_{context}"]
= Limited support status

[role="_abstract"]
When a cluster transitions to a _Limited Support_ status, Red Hat no longer proactively monitors the cluster, the SLA is no longer applicable, and credits requested against the SLA are denied. It does not mean that you no longer have product support. In some cases, the cluster can return to a fully-supported status if you remediate the violating factors. However, in other cases, you might have to delete and recreate the cluster.

A cluster might transition to a Limited Support status for many reasons, including the following scenarios:

If you do not upgrade a cluster to a supported version before the end-of-life date:: Red Hat does not make any runtime or SLA guarantees for versions after their end-of-life date. To receive continued support, upgrade the cluster to a supported version prior to the end-of-life date. If you do not upgrade the cluster prior to the end-of-life date, the cluster transitions to a Limited Support status until it is upgraded to a supported version.
+
Red Hat provides commercially reasonable support to upgrade from an unsupported version to a supported version. However, if a supported upgrade path is no longer available, you might have to create a new cluster and migrate your workloads.

If you remove or replace any native OpenShift Container Platform components or any other component that is installed and managed by Red Hat:: If cluster administrator permissions were used, Red Hat is not responsible for any of your or your authorized users’ actions, including those that affect infrastructure services, service availability, or data loss. If Red Hat detects any such actions, the cluster might transition to a Limited Support status. Red Hat notifies you of the status change and you should either revert the action or create a support case to explore remediation steps that might require you to delete and recreate the cluster.

If you have questions about a specific action that might cause a cluster to transition to a Limited Support status or need further assistance, open a support ticket.
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc
[id="support_{context}"]
= Support

[role="_abstract"]
OpenShift Container Platform includes Red Hat Premium Support, which can be accessed by using the Red Hat Customer Portal.

See the Scope of Coverage Page for more details on what is covered with included support for OpenShift Container Platform.

See OpenShift Container Platform SLAs for support response times.
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc

[id="sdpolicy-logging_{context}"]
= Logging

[role="_abstract"]
OpenShift Container Platform provides optional integrated log forwarding to Amazon CloudWatch (on AWS) or {gcp-full} Logging (on {gcp-short}).

For more information, see About log collection and forwarding.

[id="audit-logging_{context}"]
== Cluster audit logging
Cluster audit logs are available through Amazon CloudWatch (on AWS) or {gcp-full} Logging (on {gcp-short}), if the integration is enabled. If the integration is not enabled, you can request the audit logs by opening a support case. Audit log requests must specify a date and time range not to exceed 21 days. When requesting audit logs, customers should be aware that audit logs are many GB per day in size.
[id="application-logging_{context}"]
== Application logging
Application logs sent to `STDOUT` are forwarded to Amazon CloudWatch (on AWS) or {gcp-full} Logging (on {gcp-short}) through the cluster logging stack, if it is installed.

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc

[id="sdpolicy-monitoring_{context}"]
= Monitoring

[role="_abstract"]
Review the tools you need to monitor cluster performance and stay informed about your cluster's status.

[id="cluster-metrics_{context}"]
== Cluster metrics

OpenShift Container Platform clusters come with an integrated Prometheus/Grafana stack for cluster monitoring including CPU, memory, and network-based metrics. This is accessible through the web console and can also be used to view cluster-level status and capacity/usage through a Grafana dashboard. These metrics also allow for horizontal pod autoscaling based on CPU or memory metrics provided by an OpenShift Container Platform user.

[id="cluster-status-notification_{context}"]
== Cluster notifications

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc

[id="sdpolicy-networking_{context}"]
= Networking

[role="_abstract"]
Review the networking aspects of OpenShift Container Platform.

[id="custom-domains_{context}"]
== Custom domains for applications

[WARNING]
====
Starting with OpenShift Container Platform 4.14, the Custom Domain Operator is deprecated. To manage Ingress in OpenShift Container Platform 4.14 or later, use the Ingress Operator. The functionality is unchanged for OpenShift Container Platform 4.13 and earlier versions.
====

To use a custom hostname for a route, you must update your DNS provider by creating a canonical name (CNAME) record. Your CNAME record should map the OpenShift canonical router hostname to your custom domain. The OpenShift canonical router hostname is shown on the *Route Details* page after a Route is created. Alternatively, a wildcard CNAME record can be created once to route all subdomains for a given hostname to the cluster's router.

[id="custom-domains-cluster_{context}"]
== Custom domains for cluster services
Custom domains and subdomains are not available for the platform service routes, for example, the API or web console routes, or for the default application routes.

[id="domain-validated-certificates_{context}"]
== Domain validated certificates
OpenShift Container Platform includes TLS security certificates needed for both internal and external services on the cluster. For external routes, there are two, separate TLS wildcard certificates that are provided and installed on each cluster, one for the web console and route default hostnames and the second for the API endpoint. _Let’s Encrypt_ is the certificate authority used for certificates. Routes within the cluster, for example, the internal API endpoint, use TLS certificates signed by the cluster's built-in certificate authority and require the CA bundle available in every pod for trusting the TLS certificate.

[id="custom-certificate-authorities_{context}"]
== Custom certificate authorities for builds
OpenShift Container Platform supports the use of custom certificate authorities to be trusted by builds when pulling images from an image registry.

[id="load-balancers_{context}"]
== Load balancers
OpenShift Container Platform uses up to 5 different load balancers:

* Internal control plane load balancer that is internal to the cluster and used to balance traffic for internal cluster communications.
* External control plane load balancer that is used for accessing the {OCP} and Kubernetes APIs. This load balancer can be disabled in {cluster-manager-first}. If this load balancer is disabled, Red{nbsp}Hat reconfigures the API DNS to point to the internal control load balancer.
* External control plane load balancer for Red{nbsp}Hat that is reserved for cluster management by Red{nbsp}Hat. Access is strictly controlled, and communication is only possible from allowlisted bastion hosts.
* Default router/ingress load balancer that is the default application load balancer, denoted by `apps` in the URL. The default load balancer can be configured in {cluster-manager} to be either publicly accessible over the internet, or only privately accessible over a pre-existing private connection. All application routes on the cluster are exposed on this default router load balancer, including cluster services such as the logging UI, metrics API, and registry.
* Optional: Secondary router/ingress load balancer that is a secondary application load balancer, denoted by `apps2` in the URL. The secondary load balancer can be configured in {cluster-manager} to be either publicly accessible over the internet, or only privately accessible over a pre-existing private connection. If a 'Label match' is configured for this router load balancer, then only application routes matching this label will be exposed on this router load balancer, otherwise all application routes are also exposed on this router load balancer.
* Optional: Load balancers for services that can be mapped to a service running on OpenShift Container Platform to enable advanced ingress features, such as non-HTTP/SNI traffic or the use of non-standard ports. These can be purchased in groups of 4 for non-CCS clusters, or they can be provisioned through the cloud provider console in Customer Cloud Subscription (CCS) clusters; however, each AWS account has a quota that limits the number of Classic Load Balancers that can be used within each cluster.

[id="network-usage_{context}"]
== Network usage
For non-CCS OpenShift Container Platform clusters, network usage is measured based on data transfer between inbound, VPC peering, VPN, and AZ traffic. On a non-CCS OpenShift Container Platform base cluster, 12 TB of network I/O is provided. Additional network I/O can be purchased in 12 TB increments. For CCS OpenShift Container Platform clusters, network usage is not monitored, and is billed directly by the cloud provider.

[id="cluster-ingress_{context}"]
== Cluster ingress
Project administrators can add route annotations for many different purposes, including ingress control through IP allowlisting.

Ingress policies can also be changed by using `NetworkPolicy` objects, which leverage the `ovs-networkpolicy` plugin. This allows for full control over the ingress network policy down to the pod level, including between pods on the same cluster and even in the same namespace.

All cluster ingress traffic goes through the defined load balancers. Direct access to all nodes is blocked by cloud configuration.

[id="cluster-egress_{context}"]
== Cluster egress
Pod egress traffic control through `EgressNetworkPolicy` objects can be used to prevent or limit outbound traffic in OpenShift Container Platform.

Public outbound traffic from the control plane and infrastructure nodes is required and necessary to maintain cluster image security and cluster monitoring. This requires the `0.0.0.0/0` route to belong only to the internet gateway; it is not possible to route this range over private connections.

OpenShift Container Platform clusters use NAT Gateways to present a public, static IP for any public outbound traffic leaving the cluster. Each subnet a cluster is deployed into receives a distinct NAT Gateway. For clusters deployed on AWS with multiple availability zones, up to 3 unique static IP addresses can exist for cluster egress traffic. For clusters deployed on {gcp-full}, regardless of availability zone topology, there will by 1 static IP address for worker node egress traffic. Any traffic that remains inside the cluster or does not go out to the public internet will not pass through the NAT Gateway and will have a source IP address belonging to the node that the traffic originated from. Node IP addresses are dynamic, and therefore a customer should not rely on allowlisting individual IP address when accessing private resources.

Customers can determine their public static IP addresses by running a pod on the cluster and then querying an external service. For example:

[source,terminal]
----
$ oc run ip-lookup --image=busybox -i -t --restart=Never --rm -- /bin/sh -c "/bin/nslookup -type=a myip.opendns.com resolver1.opendns.com | grep -E 'Address: [0-9.]+'"
----

[id="cloud-network-configuration_{context}"]
== Cloud network configuration
{Product-title} allows for the configuration of a private network connection through several cloud provider managed technologies:

* VPN connections
* AWS VPC peering
* AWS Transit Gateway
* AWS Direct Connect
* {gcp-full} VPC Network peering
* {gcp-full} Classic VPN
* {gcp-full} HA VPN

[IMPORTANT]
====
Red{nbsp}Hat SREs do not monitor private network connections. Monitoring these connections is the responsibility of the customer.
====

[id="dns-forwarding_{context}"]
== DNS forwarding
For OpenShift Container Platform clusters that have a private cloud network configuration, a customer can specify internal DNS servers available on that private connection that should be queried for explicitly provided domains.

[id="osd-network-verification_{context}"]
== Network verification

Network verification checks run automatically when you deploy an OpenShift Container Platform cluster into an existing Virtual Private Cloud (VPC) or create an additional machine pool with a subnet that is new to your cluster. The checks validate your network configuration and highlight errors, enabling you to resolve configuration issues prior to deployment.

You can also run the network verification checks manually to validate the configuration for an existing cluster.

[role="_additional-resources"]
.Additional resources

* Network verification

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc

[id="sdpolicy-storage_{context}"]
= Storage

[role="_abstract"]
Review the storage options available for OpenShift Container Platform clusters.

[id="encrypt-rest-node_{context}"]
== Encrypted-at-rest OS/node storage
Control plane nodes use encrypted-at-rest-EBS storage.

[id="encrypt-rest-pv_{context}"]
== Encrypted-at-rest PV
EBS volumes used for persistent volumes (PVs) are encrypted-at-rest by default.

[id="block-storage_{context}"]
== Block storage (RWO)
Persistent volumes (PVs) are backed by AWS EBS and {gcp-full} persistent disk block storage, which uses the ReadWriteOnce (RWO) access mode. On a non-CCS OpenShift Container Platform base cluster, 100 GB of block storage is provided for PVs, which is dynamically provisioned and recycled based on application requests. Additional persistent storage can be purchased in 500 GB increments.

PVs can only be attached to a single node at a time and are specific to the availability zone in which they were provisioned, but they can be attached to any node in the availability zone.

Each cloud provider has its own limits for how many PVs can be attached to a single node. See AWS instance type limits or {gcp-full} custom machine types  for details.

[id="shared-storage_{context}"]
== Shared storage (RWX)

The AWS CSI Driver can be used to provide RWX support for OpenShift Container Platform on AWS. A community Operator is provided to simplify setup. For more information, see AWS EFS Setup for OpenShift Dedicated and Red Hat OpenShift Service on AWS.

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc

[id="sdpolicy-platform_{context}"]
= Platform

[role="_abstract"]
This guide outlines the automated backup measures provided by the OpenShift Container Platform service and clarifies the steps you must take to protect your unique application data.

[id="cluster-backup-policy_{context}"]
== Cluster backup policy

[IMPORTANT]
====
It is critical that customers have a backup plan for their applications and application data.
====
Application and application data backups are not a part of the OpenShift Container Platform service.
All Kubernetes objects in each OpenShift Container Platform cluster are backed up to facilitate a prompt recovery in the unlikely event that a cluster becomes irreparably inoperable.

The backups are stored in a secure object storage (Multi-AZ) bucket in the same account as the cluster.
Node root volumes are not backed up because Red Hat Enterprise Linux CoreOS is fully managed by the {OCP} cluster and no stateful data should be stored on the root volume of a node.

The following table shows the frequency of backups:
[cols="4",options="header"]
|===

|Component
|Snapshot Frequency
|Retention
|Notes

|Full object store backup
|Daily at 0100 UTC
|7 days
|This is a full backup of all Kubernetes objects. No persistent volumes (PVs) are backed up in this backup schedule.

|Full object store backup
|Weekly on Mondays at 0200 UTC
|30 days
|This is a full backup of all Kubernetes objects. No PVs are backed up in this backup schedule.

|Full object store backup
|Hourly at 17 minutes past the hour
|24 hours
|This is a full backup of all Kubernetes objects. No PVs are backed up in this backup schedule.

|===

[id="autoscaling_{context}"]
== Autoscaling
Node autoscaling is available on OpenShift Container Platform. See About autoscaling nodes on a cluster for more information on autoscaling nodes on a cluster.

[id="daemon-sets_{context}"]
== Daemon sets
Customers may create and run DaemonSets on OpenShift Container Platform. In order to restrict DaemonSets to only running on worker nodes, use the following nodeSelector:

[source,yaml]
----
...
spec:
  nodeSelector:
    role: worker
...
----

[id="multi-availability-zones_{context}"]
== Multiple availability zone
In a multiple availability zone cluster, control nodes are distributed across availability zones and at least three worker nodes are required in each availability zone.

[id="node-labels_{context}"]
== Node labels
Custom node labels are created by Red Hat during node creation and cannot be changed on OpenShift Container Platform clusters at this time.

[id="openshift-version_{context}"]
== OpenShift version
OpenShift Container Platform is run as a service and is kept up to date with the latest {OCP} version.

[id="upgrades_{context}"]
== Upgrades
Refer to OpenShift Container Platform Life Cycle for more information on the upgrade policy and procedures.

[id="windows-containers_{context}"]
== Windows containers
Windows containers are not available on OpenShift Container Platform at this time.

[id="container-engine_{context}"]
== Container engine
OpenShift Container Platform runs on OpenShift 4 and uses CRI-O  as the only available container engine.

[id="operating-system_{context}"]
== Operating system
OpenShift Container Platform runs on OpenShift 4 and uses Red Hat Enterprise Linux CoreOS as the operating system for all control plane and worker nodes.

== Red Hat Operator support
[id="sdpolicy-red-hat-operator_{context}"]
Red Hat workloads typically refer to Red Hat-provided Operators made available through Operator Hub. Red Hat workloads are not managed by the Red Hat SRE team, and must be deployed on worker nodes. These Operators may require additional Red Hat subscriptions, and may incur additional cloud infrastructure costs. Examples of these Red Hat-provided Operators are:

* {rhq-short}
* Red Hat Advanced Cluster Management
* Red Hat Advanced Cluster Security
* {SMProductName}
* {ServerlessProductName}
* {logging-sd}
* {pipelines-title}

[id="kubernetes-operator-support_{context}"]
== Kubernetes Operator support
All Operators listed in the software catalog marketplace should be available for installation. Operators installed from the software catalog, including Red Hat Operators, are not SRE managed as part of the OpenShift Container Platform service. Refer to the Red Hat Customer Portal for more information on the supportability of a given Operator.
// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-service-definition.adoc

[id="sdpolicy-security_{context}"]
= Security

[role="_abstract"]
Review the security features and configurations of OpenShift Container Platform.

[id="auth-provider_{context}"]
== Authentication provider
Authentication for the cluster is configured as part of {cluster-manager-first} cluster creation process. OpenShift is not an identity provider, and all access to the cluster must be managed by the customer as part of their integrated solution. Provisioning multiple identity providers provisioned at the same time is supported. The following identity providers are supported:

* GitHub or GitHub Enterprise OAuth
* GitLab OAuth
* Google OAuth
* LDAP
* OpenID connect

[id="privileged-containers_{context}"]
== Privileged containers
Privileged containers are not available by default on OpenShift Container Platform. The `anyuid` and `nonroot` Security Context Constraints are available for members of the `dedicated-admins` group, and should address many use cases. Privileged containers are only available for `cluster-admin` users.

[id="cluster-admin-user_{context}"]
== Customer administrator user
In addition to normal users, OpenShift Container Platform provides access to an OpenShift Container Platform-specific group called `dedicated-admin`. Any users on the cluster that are members of the `dedicated-admin` group:

* Have administrator access to all customer-created projects on the cluster.
* Can manage resource quotas and limits on the cluster.
* Can add and manage `NetworkPolicy` objects.
* Are able to view information about specific nodes and PVs in the cluster, including scheduler information.
* Can access the reserved `dedicated-admin` project on the cluster, which allows for the creation of service accounts with elevated privileges and also gives the ability to update default limits and quotas for projects on the cluster.
* Can install Operators from the software catalog (`\*` verbs in all `*.operators.coreos.com` API groups).

[id="cluster-admin-role_{context}"]
== Cluster administration role
As an administrator of OpenShift Container Platform with Customer Cloud Subscriptions (CCS), you have access to the `cluster-admin` role. While logged in to an account with the `cluster-admin` role, users have mostly unrestricted access to control and configure the cluster. There are some configurations that are blocked with webhooks to prevent destablizing the cluster, or because they are managed in {cluster-manager} and any in-cluster changes would be overwritten.

[id="project-self-service_{context}"]
== Project self-service
All users, by default, have the ability to create, update, and delete their projects. This can be restricted if a member of the `dedicated-admin` group removes the self-provisioner role from authenticated users:

[source,terminal]
----
$ oc adm policy remove-cluster-role-from-group self-provisioner system:authenticated:oauth
----

Restrictions can be reverted by applying:

[source,terminal]
----
$ oc adm policy add-cluster-role-to-group self-provisioner system:authenticated:oauth
----

[id="regulatory-compliance_{context}"]
== Regulatory compliance
See the _Security and control certifications for OpenShift Container Platform_ table in _Understanding process and security for OpenShift Container Platform_ for the latest compliance information.

[id="network-security_{context}"]
== Network security
Each OpenShift Container Platform cluster is protected by a secure network configuration at the cloud infrastructure level using firewall rules (AWS Security Groups or {gcp-full} Compute Engine firewall rules). OpenShift Container Platform customers on AWS are also protected against DDoS attacks with AWS Shield Standard.
Similarly, all {gcp-short} load balancers and public IP addresses used by OpenShift Container Platform on {gcp-short} are protected against DDoS attacks with {gcp-full} Armor Standard.

[id="etcd-encryption_{context}"]
== etcd encryption

In OpenShift Container Platform, the control plane storage is encrypted at rest by default and this includes encryption of the etcd volumes. This storage-level encryption is provided through the storage layer of the cloud provider.

You can also enable etcd encryption, which encrypts the key values in etcd, but not the keys. If you enable etcd encryption, the following Kubernetes API server and OpenShift API server resources are encrypted:

* Secrets
* Config maps
* Routes
* OAuth access tokens
* OAuth authorize tokens

The etcd encryption feature is not enabled by default and it can be enabled only at cluster installation time. Even with etcd encryption enabled, the etcd key values are accessible to anyone with access to the control plane nodes or `cluster-admin` privileges.

[IMPORTANT]
====
By enabling etcd encryption for the key values in etcd, you will incur a performance overhead of approximately 20%. The overhead is a result of introducing this second layer of encryption, in addition to the default control plane storage encryption that encrypts the etcd volumes. Red Hat recommends that you enable etcd encryption only if you specifically require it for your use case.
====
