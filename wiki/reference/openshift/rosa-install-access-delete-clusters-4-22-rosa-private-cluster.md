---
title: "Configuring a private cluster"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-private-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-private-cluster
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Configuring a private cluster

[id="rosa-private-cluster"]
= Configuring a private cluster

[role="_abstract"]
A OpenShift Container Platform cluster can be made private so that internal applications can be hosted inside a corporate network. In addition, private clusters can be configured to have only internal API endpoints for increased security.

// OpenShift Container Platform administrators can choose between public and private cluster configuration from within *{cluster-manager}*.

Privacy settings can be configured during cluster creation or after a cluster is established.
[NOTE]
====
Red{nbsp}Hat Service Reliability Engineers (SREs) can access a public or private cluster through the `cloud-ingress-operator` and existing ElasticSearch Load Balancer or Amazon S3 framework. SREs can access clusters through a secure endpoint to perform maintenance and service tasks.
====
// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-private-cluster.adoc

[id="rosa-enabling-private-cluster-new_{context}"]
= Enabling private cluster on a new cluster

[role="_abstract"]
You can enable the private cluster setting when creating a new OpenShift Container Platform cluster.

[IMPORTANT]
====
Private clusters cannot be used with AWS security token service (STS). However, STS supports AWS PrivateLink clusters.
====

.Prerequisites

* You have configured one of the following to allow private access:
** AWS VPC Peering
** VPN
** DirectConnect
** TransitGateway

.Procedure

* Enter the following command to create a new private cluster.
+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name> --private
----
+
[NOTE]
====
Alternatively, use `--interactive` to be prompted for each cluster option.
====

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-private-cluster.adoc

[id="rosa-enabling-private-cluster-existing_{context}"]
= Enabling private cluster on an existing cluster

[role="_abstract"]
After a cluster has been created, you can enable the cluster to be private.

[IMPORTANT]
====
Private clusters cannot be used with AWS security token service (STS). However, STS supports AWS PrivateLink clusters.
====

.Prerequisites

* You have configured one of the following to allow private access:
** AWS VPC Peering
** VPN
** DirectConnect
** TransitGateway

.Procedure

* Enter the following command to enable the `--private` option on an existing cluster.
+
[source,terminal]
----
$ rosa edit cluster --cluster=<cluster_name> --private
----
+
[NOTE]
====
Transitioning your cluster between private and public can take several minutes to complete.
====

[role="_additional-resources"]
== Additional resources

* Creating an AWS PrivateLink cluster on ROSA
