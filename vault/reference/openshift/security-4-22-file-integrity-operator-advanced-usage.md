---
title: "Performing advanced Custom File Integrity Operator tasks"
type: reference
domain: openshift
slug: security-4-22-file-integrity-operator-advanced-usage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/file-integrity-operator-advanced-usage
version: 4.22
family: security
documentKind: "Documentation"
---

# Performing advanced Custom File Integrity Operator tasks

[id="file-integrity-operator-advanced-usage"]
= Performing advanced Custom File Integrity Operator tasks

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-advanced-usage.adoc

[id="file-integrity-operator-reinitializing-database_{context}"]
= Reinitializing the database

If the File Integrity Operator detects a change that was planned, it might be required to reinitialize the database.

.Procedure

* Annotate the `FileIntegrity` custom resource (CR) with `file-integrity.openshift.io/re-init`:
+
[source,terminal]
----
$ oc annotate fileintegrities/worker-fileintegrity file-integrity.openshift.io/re-init=
----
+
The old database and log files are backed up and a new database is initialized. The old database and logs are retained on the nodes under `/etc/kubernetes`, as
seen in the following output from a pod spawned using `oc debug`:
+
.Example output
[source,terminal]
----
 ls -lR /host/etc/kubernetes/aide.*
-rw-------. 1 root root 1839782 Sep 17 15:08 /host/etc/kubernetes/aide.db.gz
-rw-------. 1 root root 1839783 Sep 17 14:30 /host/etc/kubernetes/aide.db.gz.backup-20200917T15_07_38
-rw-------. 1 root root   73728 Sep 17 15:07 /host/etc/kubernetes/aide.db.gz.backup-20200917T15_07_55
-rw-r--r--. 1 root root       0 Sep 17 15:08 /host/etc/kubernetes/aide.log
-rw-------. 1 root root     613 Sep 17 15:07 /host/etc/kubernetes/aide.log.backup-20200917T15_07_38
-rw-r--r--. 1 root root       0 Sep 17 15:07 /host/etc/kubernetes/aide.log.backup-20200917T15_07_55
----
+
To provide some permanence of record, the resulting config maps are not owned by the `FileIntegrity` object, so manual cleanup is necessary. As a
result, any previous integrity failures would still be visible in the `FileIntegrityNodeStatus` object.

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-advanced-usage.adoc

[id="file-integrity-operator-machine-config-integration_{context}"]
= Machine config integration

In OpenShift Container Platform 4, the cluster node configuration is delivered through
`MachineConfig` objects. You can assume that the changes to files that are
caused by a `MachineConfig` object are expected and should not cause the file
integrity scan to fail. To suppress changes to files caused by `MachineConfig`
object updates, the File Integrity Operator watches the node objects; when a
node is being updated, the AIDE scans are suspended for the duration of the
update. When the update finishes, the database is reinitialized and the scans
resume.

This pause and resume logic only applies to updates through the `MachineConfig`
API, as they are reflected in the node object annotations.

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-advanced-usage.adoc

[id="file-integrity-operator-exploring-daemon-sets_{context}"]
= Exploring the daemon sets

Each `FileIntegrity` object represents a scan on a number of nodes. The scan
itself is performed by pods managed by a daemon set.

To find the daemon set that represents a `FileIntegrity` object, run:

[source,terminal]
----
$ oc -n openshift-file-integrity get ds/aide-worker-fileintegrity
----

To list the pods in that daemon set, run:

[source,terminal]
----
$ oc -n openshift-file-integrity get pods -lapp=aide-worker-fileintegrity
----

To view logs of a single AIDE pod, call `oc logs` on one of the pods.

[source,terminal]
----
$ oc -n openshift-file-integrity logs pod/aide-worker-fileintegrity-mr8x6
----

.Example output
[source,terminal]
----
Starting the AIDE runner daemon
initializing AIDE db
initialization finished
running aide check
...
----

The config maps created by the AIDE daemon are not retained and are deleted
after the File Integrity Operator processes them. However, on failure and error,
the contents of these config maps are copied to the config map that the
`FileIntegrityNodeStatus` object points to.
