---
title: "Summarizing cluster specifications"
type: reference
domain: openshift
slug: support-4-22-summarizing-cluster-specifications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/summarizing-cluster-specifications
version: 4.22
family: support
documentKind: "Documentation"
---

# Summarizing cluster specifications

[id="summarizing-cluster-specifications"]
= Summarizing cluster specifications

[role="_abstract"]
You can summarize your cluster specifications by querying the `clusterversion` resource to view cluster version information and component status.

// Summarizing cluster specifications through `clusterversion`
// Module included in the following assemblies:
//
// * support/summarizing-cluster-specifications.adoc

[id="summarizing-cluster-specifications-through-clusterversion_{context}"]
= Summarizing cluster specifications by using a cluster version object

[role="_abstract"]
You can obtain a summary of OpenShift Container Platform cluster specifications by querying the `clusterversion` resource.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Query cluster version, availability, uptime, and general status:
+
[source,terminal]
----
$ oc get clusterversion
----
+
.Example output
[source,text]
----
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.13.8    True        False         8h      Cluster version is 4.13.8
----
. Obtain a detailed summary of cluster specifications, update availability, and update history:
+
[source,terminal]
----
$ oc describe clusterversion
----
+
.Example output
[source,text]
----
Name:         version
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  config.openshift.io/v1
Kind:         ClusterVersion
# ...
    Image:    quay.io/openshift-release-dev/ocp-release@sha256:a956488d295fe5a59c8663a4d9992b9b5d0950f510a7387dbbfb8d20fc5970ce
    URL:      https://access.redhat.com/errata/RHSA-2023:4456
    Version:  4.13.8
  History:
    Completion Time:    2023-08-17T13:20:21Z
    Image:              quay.io/openshift-release-dev/ocp-release@sha256:a956488d295fe5a59c8663a4d9992b9b5d0950f510a7387dbbfb8d20fc5970ce
    Started Time:       2023-08-17T12:59:45Z
    State:              Completed
    Verified:           false
    Version:            4.13.8
# ...
----
