---
title: "Scheduling pods using a scheduler profile"
type: reference
domain: openshift
slug: nodes-4-22-nodes-scheduler-profiles
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-scheduler-profiles
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Scheduling pods using a scheduler profile

[id="nodes-scheduler-profiles"]
= Scheduling pods using a scheduler profile

[role="_abstract"]
You can use a scheduling profile to configure how the scheduler spreads pods across nodes to enforce low or high node utilization.

// About scheduler profiles
// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-profiles.adoc

[id="nodes-scheduler-profiles-about_{context}"]
= About scheduler profiles

[role="_abstract"]
You can use scheduler profiles to determine how the cluster distributes pods across nodes based on node resource utilization.

The following scheduler profiles are available:

`LowNodeUtilization`:: This profile attempts to spread pods evenly across nodes to get low resource usage per node. This profile provides the default scheduler behavior.

`HighNodeUtilization`:: This profile attempts to place as many pods as possible on to as few nodes as possible. This minimizes node count and has high resource usage per node.

[NOTE]
====
Switching to the `HighNodeUtilization` scheduler profile will result in all pods of a `ReplicaSet` object being scheduled on the same node. This will add an increased risk for pod failure if the node fails.
====

`NoScoring`:: This is a low-latency profile that strives for the quickest scheduling cycle by disabling all score plugins. This might sacrifice better scheduling decisions for faster ones.

// Configuring a scheduler profile
// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-profiles.adoc

[id="nodes-scheduler-profiles-configuring_{context}"]
= Configuring a scheduler profile

[role="_abstract"]
To customize how the cluster distributes pods across your nodes based on resource use, you can configure a specific scheduler profile.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `Scheduler` object:
+
[source,terminal]
----
$ oc edit scheduler cluster
----

. Specify the profile to use in the `spec.profile` field:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
#...
spec:
  mastersSchedulable: false
  profile: HighNodeUtilization
#...
----
+
Set `spec.profile` to `LowNodeUtilization`, `HighNodeUtilization`, or `NoScoring`.

. Save the file to apply the changes.
