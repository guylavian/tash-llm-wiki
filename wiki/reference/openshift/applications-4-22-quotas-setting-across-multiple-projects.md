---
title: "Resource quotas across multiple projects"
type: reference
domain: openshift
slug: applications-4-22-quotas-setting-across-multiple-projects
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/quotas-setting-across-multiple-projects
version: 4.22
family: applications
documentKind: "Documentation"
---

# Resource quotas across multiple projects

[id="setting-quotas-across-multiple-projects"]
= Resource quotas across multiple projects

A multi-project quota, defined by a `ClusterResourceQuota` object, allows quotas to be shared across multiple projects. Resources used in each selected project are aggregated and that aggregate is used to limit resources across all the selected projects.

This guide describes how cluster administrators can set and manage resource quotas across multiple projects.

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-across-multiple-projects.adoc

[id="quotas-setting-projects_{context}"]
= Selecting multiple projects during quota creation

When creating quotas, you can select multiple projects based on annotation selection, label selection, or both.

.Procedure

. To select projects based on annotations, run the following command:
+
[source,terminal]
----
$ oc create clusterquota for-user \
     --project-annotation-selector openshift.io/requester=<user_name> \
     --hard pods=10 \
     --hard secrets=20
----
+
This creates the following `ClusterResourceQuota` object:
+
[source,yaml]
----
apiVersion: quota.openshift.io/v1
kind: ClusterResourceQuota
metadata:
  name: for-user
spec:
  quota: <1>
    hard:
      pods: "10"
      secrets: "20"
  selector:
    annotations: <2>
      openshift.io/requester: <user_name>
    labels: null <3>
status:
  namespaces: <4>
  - namespace: ns-one
    status:
      hard:
        pods: "10"
        secrets: "20"
      used:
        pods: "1"
        secrets: "9"
  total: <5>
    hard:
      pods: "10"
      secrets: "20"
    used:
      pods: "1"
      secrets: "9"
----
<1> The `ResourceQuotaSpec` object that will be enforced over the selected projects.
<2> A simple key-value selector for annotations.
<3> A label selector that can be used to select projects.
<4> A per-namespace map that describes current quota usage in each selected project.
<5> The aggregate usage across all selected projects.
+
This multi-project quota document controls all projects requested by `<user_name>` using the default project request endpoint. You are limited to 10 pods and 20 secrets.

. Similarly, to select projects based on labels, run this command:
+
[source,terminal]
----
$  oc create clusterresourcequota for-name \//<1>
    --project-label-selector=name=frontend \//<2>
    --hard=pods=10 --hard=secrets=20
----
+
<1> Both `clusterresourcequota` and `clusterquota` are aliases of the same command. `for-name` is the name of the `ClusterResourceQuota` object.
<2> To select projects by label, provide a key-value pair by using the format `--project-label-selector=key=value`.
+
This creates the following `ClusterResourceQuota` object definition:
+
[source,yaml]
----
apiVersion: quota.openshift.io/v1
kind: ClusterResourceQuota
metadata:
  creationTimestamp: null
  name: for-name
spec:
  quota:
    hard:
      pods: "10"
      secrets: "20"
  selector:
    annotations: null
    labels:
      matchLabels:
        name: frontend
----

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-across-multiple-projects.adoc

[id="quotas-viewing-clusterresourcequotas_{context}"]
= Viewing applicable cluster resource quotas

A project administrator is not allowed to create or modify the multi-project quota that limits his or her project, but the administrator is allowed to view the multi-project quota documents that are applied to his or her project. The project administrator can do this via the `AppliedClusterResourceQuota` resource.

.Procedure

. To view quotas applied to a project, run:
+
[source,terminal]
----
$ oc describe AppliedClusterResourceQuota
----
+
.Example output
[source,terminal]
----
Name:   for-user
Namespace:  <none>
Created:  19 hours ago
Labels:   <none>
Annotations:  <none>
Label Selector: <null>
AnnotationSelector: map[openshift.io/requester:<user-name>]
Resource  Used  Hard
--------  ----  ----
pods        1     10
secrets     9     20
----

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-across-multiple-projects.adoc

[id="quotas-selection-granularity_{context}"]
= Selection granularity

Because of the locking consideration when claiming quota allocations, the number of
active projects selected by a multi-project quota is an important consideration.
Selecting more than 100 projects under a single multi-project quota can have
detrimental effects on API server responsiveness in those projects.
