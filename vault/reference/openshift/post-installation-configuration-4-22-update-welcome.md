---
title: "Upgrading an {product-title} cluster"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-update-welcome
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/update-welcome
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Upgrading an {product-title} cluster

[id="update-welcome"]
= Upgrading an OpenShift Container Platform cluster

[role="_abstract"]
OpenShift Container Platform has long term support or extended update support (EUS) on all even releases and update paths between EUS releases.
You can update from one EUS version to the next EUS version.
It is also possible to update between y-stream and z-stream versions.

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/updating/update-welcome.adoc

[id="update-introduction_{context}"]
= Cluster updates for OpenShift clusters

[role="_abstract"]
Updating your cluster is a critical task that ensures that bugs and potential security vulnerabilities are patched.
Often, updates to cloud-native applications require additional functionality from the platform that comes when you update the cluster version.
You also must update the cluster periodically to ensure that the cluster platform version is supported.

You can minimize the effort required to stay current with updates by keeping up-to-date with EUS releases and upgrading to select important z-stream releases only.

[NOTE]
====
The update path for the cluster can vary depending on the size and topology of the cluster.
====

The following update scenarios are described:

* Control Plane Only updates
* Y-stream updates
* Z-stream updates

[IMPORTANT]
====
Control Plane Only updates were previously known as EUS-to-EUS updates.
Control Plane Only updates are only viable between even-numbered minor versions of OpenShift Container Platform.
====
