---
title: "Private Service Connect overview"
type: reference
domain: openshift
slug: osd-gcp-clusters-4-22-creating-a-gcp-psc-enabled-private-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_gcp_clusters/creating-a-gcp-psc-enabled-private-cluster
version: 4.22
family: osd_gcp_clusters
documentKind: "Documentation"
---

# Private Service Connect overview

[id="creating-a-gcp-psc-enabled-private-cluster"]
= Private Service Connect overview

[role="_abstract"]
You can create a private OpenShift Container Platform cluster on {GCP} using {gcp-full}'s security-enhanced networking feature Private Service Connect (PSC).

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

[id="private-service-connect-prereqs"]
= Prerequisites

[role="_abstract"]
In addition to the prerequisites that you need to complete before deploying any OpenShift Container Platform on {GCP} cluster, you must also complete the following prerequisites to deploy a private cluster using Private Service Connect (PSC):

* A pre-created Virtual Private Cloud (VPC) with the following subnets in the same {GCP} region where your cluster will be deployed:

** A control plane subnet
** A worker subnet
** A subnet used for the PSC service attachment with the purpose set to Private Service Connect
+
[IMPORTANT]
====
The subnet mask for the PSC service attachment must be /29 or larger and must be dedicated to an individual OpenShift Container Platform cluster. Additionally, the subnet must be contained within the Machine CIDR range used while provisioning the OpenShift Container Platform cluster.
====
+
For information about how to create a VPC on {GCP}, see Create and manage VPC networks in the {gcp-full} documentation.

* Provide a path from the OpenShift Dedicated cluster to the internet for the domains and ports listed in the _{gcp-short} firewall prerequisites_ in the _Additional resources_ section.

* Enabled Cloud Identity-Aware Proxy API at the {GCP} project level.

In addition to the requirements listed above, clusters configured with the **Service Account authentication type** must grant the `IAP-Secured Tunnel User` role to `osd-ccs-admin` service account.

For more information about the prerequisites that must be completed before deploying an OpenShift Container Platform on {GCP}, see _Customer Requirements_.

[NOTE]
====
PSC is supported with the Customer Cloud Subscription (CCS) infrastructure type only. To create an OpenShift Container Platform on {GCP} using PSC, see _Creating a cluster on {gcp-short} with Workload Identity Federation_.
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

[id="next-steps-psc_{context}"]
== Next steps
* To learn more about OpenShift Container Platform on {GCP} cluster prerequisites, see Customer Requirements.

* To configure your firewalls, see {gcp-short} firewall prerequisites.

* To create an OpenShift Container Platform on {GCP} using PSC with the Workload Identity Federation authentication type, see
 Creating a cluster on {gcp-short} with Workload Identity Federation authentication.
