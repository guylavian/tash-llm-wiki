---
title: "Troubleshooting etcd"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-etcd-troubleshoot
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-etcd-troubleshoot
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Troubleshooting etcd

[id="microshift-etcd-troubleshoot"]
= Troubleshooting etcd

[role="_abstract"]
To troubleshoot etcd and improve performance, configure the memory allowance for the service.

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
