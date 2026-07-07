---
title: "Recovering an unhealthy etcd cluster for {hcp}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-recovering-etcd-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-recovering-etcd-cluster
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Recovering an unhealthy etcd cluster for {hcp}

[id="hcp-recovering-etcd-cluster"]
= Recovering an unhealthy etcd cluster for {hcp}

In a highly available control plane, three etcd pods run as a part of a stateful set in an etcd cluster. To recover an etcd cluster, identify unhealthy etcd pods by checking the etcd cluster health.

// Module included in the following assembly:
//
// * hosted_control_planes/hcp_high_availability/hcp-recovering-etcd-cluster.adoc

[id="hosted-cluster-etcd-status_{context}"]
= Checking the status of an etcd cluster

You can check the status of the etcd cluster health by logging into any etcd pod.

.Procedure

. Log in to an etcd pod by entering the following command:
+
[source,terminal]
----
$ oc rsh -n clusters-<hosted_cluster_name> -c etcd <etcd_pod_name>
----

. Print the health status of an etcd cluster by entering the following command:
+
[source,terminal]
----
sh-4.4# etcdctl endpoint status -w table
----
+
.Example output
[source,terminal]
----
+------------------------------+-----------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|          ENDPOINT            |       ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+------------------------------+-----------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
| https://192.168.1xxx.20:2379 | 8fxxxxxxxxxx    |  3.5.12 |  123 MB |     false |      false |        10 |     180156 |             180156 |        |
| https://192.168.1xxx.21:2379 | a5xxxxxxxxxx    |  3.5.12 |  122 MB |     false |      false |        10 |     180156 |             180156 |        |
| https://192.168.1xxx.22:2379 | 7cxxxxxxxxxx    |  3.5.12 |  124 MB |      true |      false |        10 |     180156 |             180156 |        |
+-----------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
----

// Module included in the following assembly:
//
// * hosted_control_planes/hcp_high_availability/hcp-recovering-etcd-cluster.adoc

[id="hcp-recover-failing-etcd-pods_{context}"]
= Recovering a failing etcd pod

Each etcd pod of a 3-node cluster has its own persistent volume claim (PVC) to store its data. An etcd pod might fail because of corrupted or missing data. You can recover a failing etcd pod and its PVC.

.Procedure

. To confirm that the etcd pod is failing, enter the following command:
+
[source,terminal]
----
$ oc get pods -l app=etcd -n clusters-<hosted_cluster_name>
----
+
`<hosted_cluster_name>`:: Specifies the hosted cluster of the etcd instance.
+
.Example output
[source,terminal]
----
NAME     READY   STATUS             RESTARTS     AGE
etcd-0   2/2     Running            0            64m
etcd-1   2/2     Running            0            45m
etcd-2   1/2     CrashLoopBackOff   1 (5s ago)   64m
----
+
The failing etcd pod might have the `CrashLoopBackOff` or `Error` status.

. Delete the failing pod and its PVC by entering the following command:
+
[source,terminal]
----
$ oc delete pods <etcd_pod_name> -n clusters-<hosted_cluster_name>
----
+
`<etcd_pod_name>`:: Specifies the failing pod.

.Verification

* Verify that a new etcd pod is up and running by entering the following command:
+
[source,terminal]
----
$ oc get pods -l app=etcd -n clusters-<hosted_cluster_name>
----
+
.Example output
[source,terminal]
----
NAME     READY   STATUS    RESTARTS   AGE
etcd-0   2/2     Running   0          67m
etcd-1   2/2     Running   0          48m
etcd-2   2/2     Running   0          2m2s
----
