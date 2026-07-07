---
title: "Troubleshooting a node"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-troubleshoot-node
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-troubleshoot-node
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Troubleshooting a node

[id="microshift-troubleshoot-node"]
= Troubleshooting a node

[role="_abstract"]
To troubleshoot a {microshift-short} node, first check the node status.

//Module included in the following assemblies:
//
//*  microshift_troubleshooting/microshift-troubleshoot-node

[id="microshift-check-node-status_{context}"]
= Checking the status of a node

[role="_abstract"]
You can check the status of a {microshift-short} node or see active pods. You can choose to run any or all of the following commands to help you get the information you need to troubleshoot the node.

.Procedure

* Check the system status, which returns the node status, by running the following command:
+
[source,terminal]
----
$ sudo systemctl status microshift
----
+
If {microshift-short} fails to start, this command returns the logs from the earlier run.
+
.Example healthy output
[source,text]
----
● microshift.service - MicroShift
     Loaded: loaded (/usr/lib/systemd/system/microshift.service; enabled; preset: disabled)
     Active: active (running) since <day> <date> 12:39:06 UTC; 47min ago
   Main PID: 20926 (microshift)
      Tasks: 14 (limit: 48063)
     Memory: 542.9M
        CPU: 2min 41.185s
     CGroup: /system.slice/microshift.service
             └─20926 microshift run

<Month-Day> 13:23:06 i-06166fbb376f14a8b.<hostname> microshift[20926]: kube-apiserver I0528 13:23:06.876001   20926 controll>
<Month-Day> 13:23:06 i-06166fbb376f14a8b.<hostname> microshift[20926]: kube-apiserver I0528 13:23:06.876574   20926 controll>
# ...
----

* Optional: Get comprehensive logs by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u microshift
----
+
[NOTE]
====
The default configuration of the `systemd` journal service stores data in a volatile directory, which does not persist across restarts. To retain logs across system restarts, enable log persistence and set a maximum size limit for journal data.
====

* If {microshift-short} is running, check the status of active pods by entering the following command:
+
--
--
