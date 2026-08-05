---
title: "Disabling monitoring for user-defined projects"
type: reference
domain: openshift
slug: observability-4-22-sd-disabling-monitoring-for-user-defined-projects
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/sd-disabling-monitoring-for-user-defined-projects
version: 4.22
family: observability
documentKind: "Documentation"
---

# Disabling monitoring for user-defined projects

[id="sd-disabling-monitoring-for-user-defined-projects"]
= Disabling monitoring for user-defined projects

[role="_abstract"]
As a `dedicated-admin`, you can disable monitoring for user-defined projects. You can also exclude individual projects from user workload monitoring.

// Disabling monitoring for user-defined projects
// Module included in the following assemblies:
//
// * observability/monitoring/sd-disabling-monitoring-for-user-defined-projects.adoc

[id="sd-disabling-monitoring-for-user-defined-projects_{context}"]
= Disabling monitoring for user-defined projects

[role="_abstract"]
By default, monitoring for user-defined projects is enabled. If you do not want to use the built-in monitoring stack to monitor user-defined projects, you can disable it.

.Prerequisites

* You logged in to {cluster-manager-url}.

.Procedure

. From the {cluster-manager} {hybrid-console-second}, select a cluster.

. Click the *Settings* tab.

. Click the *Enable user workload monitoring* checkbox to deselect the option, and then click *Save*.
+
User workload monitoring is disabled. The Prometheus, Prometheus Operator, and Thanos Ruler components are stopped in the `openshift-user-workload-monitoring` project.

// Excluding a user-defined project from monitoring
// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc
// * observability/monitoring/sd-disabling-monitoring-for-user-defined-projects.adoc

[id="excluding-a-user-defined-project-from-monitoring_{context}"]
= Excluding a user-defined project from monitoring

[role="_abstract"]
Individual user-defined projects can be excluded from user workload monitoring. To do so, add the `openshift.io/user-monitoring` label to the project's namespace with a value of `false`.

.Procedure

. Add the label to the project namespace:
+
[source,terminal]
----
$ oc label namespace my-project 'openshift.io/user-monitoring=false'
----
+
. To re-enable monitoring, remove the label from the namespace:
+
[source,terminal]
----
$ oc label namespace my-project 'openshift.io/user-monitoring-'
----
+
[NOTE]
====
If there were any active monitoring targets for the project, it can take a few minutes for Prometheus to stop scraping them after adding the label.
====
