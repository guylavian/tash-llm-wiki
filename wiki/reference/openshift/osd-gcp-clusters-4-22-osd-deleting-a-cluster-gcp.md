---
title: "Deleting an {product-title} cluster on {gcp-short}"
type: reference
domain: openshift
slug: osd-gcp-clusters-4-22-osd-deleting-a-cluster-gcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_gcp_clusters/osd-deleting-a-cluster-gcp
version: 4.22
family: osd_gcp_clusters
documentKind: "Documentation"
---

# Deleting an {product-title} cluster on {gcp-short}

[id="osd-deleting-a-cluster"]
= Deleting an OpenShift Container Platform cluster on {gcp-short}

[role="_abstract"]
As cluster owner, you can delete your OpenShift Container Platform clusters.

// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-deleting-a-cluster.adoc
// * osd_aws_clusters/osd-deleting-a-cluster.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="deleting-cluster_{context}"]
= Deleting your cluster

[role="_abstract"]
You can delete your OpenShift Container Platform cluster in {cluster-manager-first}.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.

.Procedure

. From {cluster-manager-url}, select the cluster you want to delete.

. Select *Delete cluster* from the *Actions* drop-down menu.

. Type the name of the cluster highlighted in bold, then click *Delete*. Cluster deletion occurs automatically.

+
[NOTE]
====
If you delete a cluster that was installed into a {gcp-short} Shared VPC, inform the VPC owner of the host project to remove the IAM policy roles granted to the service account that was referenced during cluster creation.
====
