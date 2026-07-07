---
title: "About disaster recovery"
type: reference
domain: openshift
slug: backup-and-restore-4-22-about-disaster-recovery
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/about-disaster-recovery
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# About disaster recovery

//NOTE TO CONTRIBUTORS:
//
//If you update any of the content in this assembly file, be sure to also make the same changes in the assemblies in the following directory: etcd/etcd-backup-restore/etcd-disaster-recovery.adoc.

[id="about-dr"]
= About disaster recovery

The disaster recovery documentation provides information for administrators on
how to recover from several disaster situations that might occur with their
OpenShift Container Platform cluster. As an administrator, you might need to follow one or
more of the following procedures to return your cluster to a working
state.

[IMPORTANT]
====
Disaster recovery requires you to have at least one healthy control plane host.
====

Quorum restoration:: This solution handles situations where you have lost the majority of your control plane hosts, leading to etcd quorum loss and the cluster going offline. This solution does not require an etcd backup.
+
[NOTE]
====
If you have a majority of your control plane nodes still available and have an etcd quorum, then replace a single unhealthy etcd member.
====

This solution handles situations where you want to restore your cluster to
an earlier state, for example, if an administrator deletes something critical.
If you have taken an etcd backup, you can restore your cluster to an earlier state.
+
If applicable, you might also need to recover from expired control plane certificates.
+
[WARNING]
====
Restoring to an earlier cluster state is a destructive and destablizing action to take on a running cluster. This procedure should only be used as a last resort.

Prior to performing a restore, see About restoring cluster state for more information on the impact to the cluster.
====

Recovering from expired control plane certificates::
This solution handles situations where your control plane certificates have
expired. For example, if you shut down your cluster before the first certificate
rotation, which occurs 24 hours after installation, your certificates will not
be rotated and will expire. You can follow this procedure to recover from
expired control plane certificates.

// Testing restore procedures
// Module included in the following assemblies:
//
// * disaster_recovery/about-disaster-recovery.adoc
// * etcd/etcd-backup-restore/etcd-disaster-recovery.adoc

[id="dr-testing-restore-procedures_{context}"]
= Testing restore procedures

Testing the restore procedure is important to ensure that your automation and workload handle the new cluster state gracefully. Due to the complex nature of etcd quorum and the etcd Operator attempting to mend automatically, it is often difficult to correctly bring your cluster into a broken enough state that it can be restored.

[WARNING]
====
You **must** have SSH access to the cluster. Your cluster might be entirely lost without SSH access.
====

.Prerequisites

* You have SSH access to control plane hosts.
* You have installed the {oc-first}.

.Procedure

. Use SSH to connect to each of your nonrecovery nodes and run the following commands to disable etcd and the `kubelet` service:

.. Disable etcd by running the following command:
+
[source,terminal]
----
$ sudo /usr/local/bin/disable-etcd.sh
----

.. Delete variable data for etcd by running the following command:
+
[source,terminal]
----
$ sudo rm -rf /var/lib/etcd
----

.. Disable the `kubelet` service by running the following command:
+
[source,terminal]
----
$ sudo systemctl disable kubelet.service
----

. Exit every SSH session.

. Run the following command to ensure that your nonrecovery nodes are in a `NOT READY` state:
+
[source,terminal]
----
$ oc get nodes
----

. Follow the steps in "Restoring to a previous cluster state" to restore your cluster.

. After you restore the cluster and the API responds, use SSH to connect to each nonrecovery node and enable the `kubelet` service:
+
[source,terminal]
----
$ sudo systemctl enable kubelet.service
----

. Exit every SSH session.

. Run the following command to observe your nodes coming back into the `READY` state:
+
[source,terminal]
----
$ oc get nodes
----

. Run the following command to verify that etcd is available:
+
[source,terminal]
----
$ oc get pods -n openshift-etcd
----

[role="_additional-resources"]
.Additional resources
* Restoring to an earlier cluster state
