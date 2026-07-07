---
title: "Configuring a private cluster"
type: reference
domain: openshift
slug: osd-cluster-admin-4-22-private-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_cluster_admin/private-cluster
version: 4.22
family: osd_cluster_admin
documentKind: "Documentation"
---

# Configuring a private cluster

[id="private-cluster"]
= Configuring a private cluster

[role="_abstract"]
Configure OpenShift Container Platform clusters as private to host internal applications inside your corporate network and restrict API endpoint access to private connections only. This enhances security by preventing public internet access to the cluster control plane.

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/private-cluster.adoc

[id="enable-private-cluster-new_{context}"]
= Enable a private cluster during cluster creation

[role="_abstract"]
Enable private cluster settings when creating a new cluster to restrict Application Programming Interface (API) endpoint access to private connections only. This enhances security by preventing public internet access to your cluster's control plane.

.Prerequisites

* The following private connections are configured to allow private access:
** Virtual Private Cloud (VPC) Peering
** Cloud VPN
** DirectConnect (AWS only)
** TransitGateway (AWS only)
** Cloud Interconnect ({gcp-short} only)

.Procedure

. Log in to {cluster-manager-url}.
. Click *Create cluster* -> *OpenShift Container Platform* -> *Create cluster*.
. Configure your cluster details.
. When selecting your preferred network configuration, select *Advanced*.
. Select *Private*.
+
[WARNING]
====
When set to *Private*, you cannot access your cluster unless you have configured the private connections in your cloud provider as outlined in the prerequisites.
====

. Click *Create cluster*. The cluster creation process begins and takes about 30-40 minutes to complete.

.Verification

* The *Installing cluster* heading, under the *Overview* tab, indicates that the cluster is installing and you can view the installation logs from this heading. The *Status* indicator under the *Details* heading indicates when your cluster is *Ready* for use.

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/private-cluster.adoc

[id="enable-private-cluster-existing_{context}"]
= Enable an existing cluster to be private

[role="_abstract"]
Configure an existing public cluster to be private by restricting Application Programming Interface (API) endpoint access to private connections only. This enhances security by preventing public internet access to your cluster's control plane.

.Prerequisites

* The following private connections are configured to allow private access:
** Virtual Private Cloud (VPC) Peering
** Cloud VPN
** DirectConnect (AWS only)
** TransitGateway (AWS only)
** Cloud Interconnect ({gcp-short} only)

.Procedure

. Log in to {cluster-manager-url}.

. Select the public cluster you want to make private.

. On the *Networking* tab, select *Make API private* under *Control Plane API endpoint*.
+

[WARNING]
====
When set to *Private*, you cannot access your cluster unless you have configured the private connections in your cloud provider as outlined in the prerequisites.
====

. Click *Change settings*.
+
[NOTE]
====
Transitioning your cluster between private and public can take several minutes to complete.
====

// Module included in the following assemblies:
//
// * osd_cluster_admin/osd_private_connections/private-cluster.adoc

[id="enable-public-cluster_{context}"]
= Configure an existing private cluster to be public

[role="_abstract"]
Configure an existing private cluster to be public by allowing Application Programming Interface (API) endpoint access from the internet. This enables access to your cluster without requiring private connection configuration.

.Procedure

. Log in to {cluster-manager-url}.

. Select the private cluster you want to make public.

. On the *Networking* tab, deselect *Make API private* under *Control Plane API endpoint*.

. Click *Change settings*.
+
[NOTE]
====
Transitioning your cluster between private and public can take several minutes to complete.
====

[role="_additional-resources"]
== Additional resources

* Amazon Virtual Private Cloud
* AWS Site-to-Site VPN
* AWS Direct Connect
