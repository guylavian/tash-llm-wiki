---
title: "The etcd service"
type: reference
domain: openshift
slug: microshift-support-4-22-microshift-etcd
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_support/microshift-etcd
version: 4.22
family: microshift_support
documentKind: "Documentation"
---

# The etcd service

[id="microshift-etcd"]
= The etcd service

[role="_abstract"]
The OpenShift Container Platform RPM includes the etcd service. The etcd service runs as a separate process. {microshift-short} automatically manages the etcd lifecycle.

// Module included in the following assemblies:
//
//* microshift_support/microshift-etcd.adoc

[id="microshift-observe-debug-etcd-server_{context}"]
= Observe and debug the {microshift-short} etcd server

[role="_abstract"]
Monitoring the etcd server is critical for maintaining system stability and diagnosing errors. You can gather `journalctl` logs to observe and debug the etcd server logs.

.Prerequisites

* The {microshift-short} service is running.

.Procedure

* To get the logs for etcd, run the following command:
+
[source,terminal]
----
$ sudo journalctl -u microshift-etcd.scope
----
+
[NOTE]
====
{microshift-short} logs can be accessed separately from etcd logs using the `journalctl -u microshift` command.
====

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-version.adoc
// * microshift_support/microshift-etcd.adoc

[id="microshift-version-etcd_{context}"]
= Checking the etcd version

[role="_abstract"]
You can get the version information for the etcd database included with your {microshift-short} by using one or both of the following methods, depending on the level of information that you need.

.Procedure

* To display the base database version information, run the following command:
+
[source,terminal]
----
$ microshift-etcd version
----
+
.Example output
[source,terminal,subs="attributes+"]
----
microshift-etcd Version: 4.20.0
Base etcd Version: 3.5.13
----

* To display the full database version information, run the following command:
+
[source,terminal]
----
$ microshift-etcd version -o json
----
+
.Example output
[source,terminal]
----
{
  "major": "4",
  "minor": "20",
  "gitVersion": "4.20.0",
  "gitCommit": "140777711962eb4e0b765c39dfd325fb0abb3622",
  "gitTreeState": "clean",
  "buildDate": "2025-11-03T16:37:53Z",
  "goVersion": "go1.21.9"
  "compiler": "gc",
  "platform": "linux/amd64",
  "patch": "",
  "etcdVersion": "3.5.13"
}
----

// Module included in the following assemblies:
//
//* microshift_support/microshift-etcd.adoc

[id="microshift-troubleshooting-etcd_{context}"]
= Troubleshooting etcd

[role="_abstract"]
{microshift-short} runs etcd as a managed, separate process to store system state. To ensure optimal performance and resolve issues, as an administrator, you can observe system activity and enforce memory usage limits by using the {microshift-short} configuration file.

// Module included in the following assemblies:
//
//* microshift_support/microshift-etcd.adoc

[id="microshift-config-etcd_{context}"]
= Configuring the memoryLimitMB value to set parameters for the etcd server

[role="_abstract"]
By default, etcd uses as much memory as necessary to handle the system load. On memory-constrained systems, limiting the amount of memory etcd uses might be necessary. Configure the `memoryLimitMB` parameter to restrict the memory consumption of the etcd server.

.Procedure

* Edit the `/etc/microshift/config.yaml` configuration file to set the `memoryLimitMB` value.
+
[source,yaml]
----
etcd:
  memoryLimitMB: 128
----
+
[NOTE]
====
The minimum required value for `memoryLimitMB` on {microshift-short} is 128 MB. Values close to the minimum value are more likely to impact `etcd` performance. Lower limits increase the time etcd takes to respond to queries. If the limit is too low or etcd usage is high, queries might time out.
====

.Verification

. Restart {microshift-short} to apply the changes by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

. Verify that the new `memoryLimitMB` value is in use by running the following command:
+
[source,terminal]
----
$ systemctl show --property=MemoryHigh microshift-etcd.scope
----
