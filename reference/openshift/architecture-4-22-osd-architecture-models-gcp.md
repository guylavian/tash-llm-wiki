---
title: "{product-title} on {GCP} architecture models"
type: reference
domain: openshift
slug: architecture-4-22-osd-architecture-models-gcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/osd-architecture-models-gcp
version: 4.22
family: architecture
documentKind: "Documentation"
---

# {product-title} on {GCP} architecture models

[id="osd-architecture-models-gcp"]
= OpenShift Container Platform on {GCP} architecture models

[role="_abstract"]
Understand the different cluster architecture models available for OpenShift Container Platform on {GCP} to choose the deployment option that best fits your organization's networking and security requirements.

// Module included in the following assemblies:
//
// * osd-architecture-models-gcp.adoc

[id="osd-gcp-architecture_{context}"]
= Private OpenShift Container Platform on {GCP} architecture on public and private networks

[role="_abstract"]
You can customize the access patterns for your API server endpoint and Red Hat Site Reliability Engineering (SRE) management by configuring a private cluster with Private Service Connect (PSC), a private cluster without PSC, or a public cluster.

[IMPORTANT]
====
Red Hat recommends using PSC when deploying a private OpenShift Container Platform cluster on {GCP}. PSC ensures there is a secured, private connectivity between Red Hat infrastructure, SRE, and private OpenShift clusters.
====

// Module included in the following assemblies:
//
// * osd-architecture-models-gcp.adoc
// * osd_gcp_clusters/creating-a-gcp-psc-enabled-private-cluster.adoc

[id="osd-understanding-private-service-connect_{context}"]
= Understanding Private Service Connect

[role="_abstract"]
Private Service Connect (PSC), a capability of {gcp-full} networking, enables private communication between services across different projects or organizations within {gcp-short}. Users that implement PSC as part of their network connectivity can deploy OpenShift Container Platform clusters in a private and secured environment within {GCP} without any public facing cloud resources.

For more information about PSC, see Private Service Connect.

[IMPORTANT]
====
PSC is only available on OpenShift Container Platform version 4.17 and later, and is only supported by the Customer Cloud Subscription (CCS) infrastructure type.
====

// Module included in the following assemblies:
//
// * osd_gcp_clusters/creating-a-gcp-psc-enabled-private-cluster.adoc
// * architecture/osd-architecture-models-gcp.adoc

[id="psc-architecture_{context}"]
= Private Service Connect architecture

[role="_abstract"]
The Private Service Connect (PSC) architecture includes producer services and consumer services. Using PSC, the consumers can access producer services privately from inside their VPC network. Similarly, it allows producers to host services in their own separate VPC networks and offer a private connect to their consumers.

The following image depicts how Red HAT SREs and other internal resources access and support clusters created using PSC.

* A unique PSC service attachment is created for each OpenShift Container Platform cluster in the customer {gcp-short} project. The PSC service attachment points to the cluster API server load balancer created in the customer {gcp-short} project.

* Similar to service attachments, a unique PSC endpoint is created in the Red Hat Management {gcp-short} project for each OpenShift Container Platform cluster.

* A dedicated subnet for {gcp-short} Private Service Connect is created in the cluster’s network within the customer {gcp-short} project. This is a special subnet type where the producer services are published via PSC service attachments. This subnet is used to Source NAT (SNAT) incoming requests to the cluster API server. Additionally, the PSC subnet must be within the Machine CIDR range and cannot be used in more than one service attachment.

* Red Hat internal resources and SREs access private OpenShift Container Platform clusters using the connectivity between a PSC endpoint and service attachment. Even though the traffic transits multiple VPC networks, it remains entirely within {gcp-full}.

* Access to PSC service attachments is possible only via the Red Hat Management project.

.PSC architecture overview
image::psc_arch_2.png[Diagram showing a customer Google Cloud project with a PSC service attachment connected to a cluster API server load balancer, a dedicated PSC subnet, and a PSC endpoint in the Red Hat Management GCP project. Traffic flows from Red Hat internal resources through the PSC endpoint to the service attachment and cluster API server.]

// Module included in the following assemblies:
//
// * osd-architecture-models-gcp.adoc

[id="osd-private-psc-architecture-model-gcp_{context}"]
= Private OpenShift Container Platform on {GCP} with Private Service Connect architecture model

[role="_abstract"]
With a private {gcp-short} Private Service Connect (PSC) network configuration, your cluster API server endpoint and application routes are private. Public subnets or NAT gateways are not required in your VPC for egress.
Red Hat SRE management access the cluster over the {gcp-short} PSC-enabled private connectivity. The default ingress controller are private. Additional ingress controllers can be public or private. The following diagram shows network connectivity of a private cluster with PSC.

.OpenShift Container Platform on {GCP} deployed on a private network with PSC
image::484_a_OpenShift_osd_gcp_private_psc_arch_0525.png[Architecture diagram showing Developer and Red Hat Management connecting through Google Cloud Private Service Connect to a customer Google Cloud project private network. The network contains an Internal API load balancer and Default Ingress load balancer routing traffic to three node groups distributed across availability zones: Control plane nodes (x3) running apiserver, etcd, and controller; Worker nodes (xN) running compute and persistent storage; and Infra nodes (x2, x3) running registry, router, and monitoring.]
// Module included in the following assemblies:
//
// * osd-architecture-models-gcp.adoc

[id="osd-private-architecture-model_{context}"]
= Private OpenShift Container Platform on {GCP} without Private Service Connect architecture model

[role="_abstract"]
With a private network configuration, your cluster API server endpoint and application routes are private. Private OpenShift Container Platform on {gcp-short} clusters use some public subnets, but no control plane or worker nodes are deployed in public subnets.

[IMPORTANT]
====
Red Hat recommends using Private Service Connect (PSC) when deploying a private OpenShift Container Platform cluster on {GCP}. PSC ensures there is a secured, private connectivity between Red Hat infrastructure, Site Reliability Engineering (SRE), and private OpenShift clusters.
====

Red Hat SRE management access the cluster through a public load balancer endpoint that are restricted to Red Hat IPs. The API server endpoint is private. A separate Red Hat API server endpoint is public (but restricted to Red Hat trusted IP addresses). The default ingress controller can be public or private. The following image shows network connectivity of a private cluster without Private Service Connect (PSC).

.OpenShift Container Platform on {GCP} deployed on a private network without PSC
image::484_b_Openshift_osd_gcp_private_no_psc_arch_0525.png[Architecture diagram of a private OpenShift Dedicated cluster on Google Cloud without Private Service Connect. The diagram shows a customer Google Cloud project divided into public and private networks. In the public network: developers and Red Hat management access the cluster via the Internet, a Red Hat API LB restricted to Red Hat IPs, and a Default Ingress LB. In the private network: an Internal API LB connects to three node types deployed across availability zones - Control plane nodes (x3) running apiserver, etcd, and controller; Worker nodes (xN) running compute and persistent storage; and Infra nodes (x2 or x3) running registry, router, and monitoring.]
// Module included in the following assemblies:
//
// * osd-architecture-models-gcp.adoc

[id="osd-public-architecture-model-gcp_{context}"]
= Public OpenShift Container Platform on {GCP} architecture model

[role="_abstract"]
With a public network configuration, your cluster API server endpoint and application routes are internet-facing. The default ingress controller can be public or private. The following image shows the network connectivity of a public cluster.

.OpenShift Container Platform on {GCP} deployed on a public network
image::484_c_Openshift_osd_gcp_public_arch_0525.png[Architecture diagram showing a customer Google Cloud project with public and private network layers. The public network contains an External API load balancer and Default Ingress load balancer, both accessible from the internet. The private network contains an Internal API load balancer connecting to three node types: Control plane nodes (x3) with apiserver, etcd, and controller components; Worker nodes (xN) with compute and persistent storage; and Infra nodes (x2, x3) with registry, router, and monitoring. All node groups are distributed across availability zones.]

[role="_additional-resources"]
[id="osd-architecture-models-additional-resources"]
== Additional resources

*  Private Service Connect overview

* Creating a cluster on {gcp-short} with Workload Identity Federation authentication

* Creating a cluster on {gcp-short} with Service Account authentication
