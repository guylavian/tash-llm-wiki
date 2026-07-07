---
title: "Cluster maintenance"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-troubleshooting-cluster-maintenance
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/troubleshooting-cluster-maintenance
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Cluster maintenance

[id="troubleshooting-cluster-maintenance"]
= Cluster maintenance

When deploying OpenShift Container Platform on bare-metal infrastructure, you must pay more attention to certain configurations which can have a significant impact on cluster stability.
You can troubleshoot more effectively by completing these tasks:

* Monitor for failed or failing hardware components
* Periodically check the status of the cluster Operators

[NOTE]
====
For hardware monitoring, contact your hardware vendor to find the appropriate logging tool for your specific hardware.
====

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cluster-maintenance.adoc

[id="troubleshooting-clusters-check-cluster-operators_{context}"]
= Checking cluster Operators

[role="_abstract"]
Periodically check the status of your cluster Operators to find issues early.

.Procedure

* Check the status of the cluster Operators by running the following command:
+
[source,terminal]
----
$ oc get co
----
// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cluster-maintenance.adoc

[id="troubleshooting-clusters-check-for-failed-pods_{context}"]
= Watching for failed pods

[role="_abstract"]
To reduce troubleshooting time, regularly monitor for failed pods in your cluster.

.Procedure

* To watch for failed pods, run the following command:
+
[source,terminal]
----
$ oc get po -A | grep -Eiv 'complete|running'
----
