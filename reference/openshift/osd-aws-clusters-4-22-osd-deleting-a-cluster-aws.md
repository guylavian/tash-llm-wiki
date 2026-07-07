---
title: "Deleting an {product-title} cluster on AWS"
type: reference
domain: openshift
slug: osd-aws-clusters-4-22-osd-deleting-a-cluster-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_aws_clusters/osd-deleting-a-cluster-aws
version: 4.22
family: osd_aws_clusters
documentKind: "Documentation"
---

# Deleting an {product-title} cluster on AWS

[id="osd-deleting-a-cluster"]
= Deleting an OpenShift Container Platform cluster on AWS

[role="_abstract"]
As cluster owner, you can delete your OpenShift Container Platform clusters.

// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/osd-deleting-a-cluster.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="deleting-cluster_aws_{context}"]
= Deleting your cluster

[role="_abstract"]
Delete your OpenShift Container Platform cluster from your {AWS} infrastructure to stop incurring costs and consuming cloud resources.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.

.Procedure

. From {cluster-manager-url}, click the cluster you want to delete.

. Select *Delete cluster* from the *Actions* list.

. Type the name of the cluster highlighted in bold, then click *Delete*. Cluster deletion occurs automatically.
