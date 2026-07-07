---
title: "Troubleshooting updates"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-troubleshoot-updates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-troubleshoot-updates
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Troubleshooting updates

// This assembly is included in the following assemblies:
//
// * microshift_troubleshooting/microshift-troubleshoot-updates.adoc
[id="microshift-troubleshoot-updates"]
= Troubleshooting updates

[role="_abstract"]
To troubleshoot {microshift-short} updates, you can check update paths, review journal and greenboot health check logs, and use other techniques to help you solve update problems.

//Module included in the following assemblies:
//
//* microshift_troubleshooting/microshift-updates-troubleshooting.adoc

[id="microshift-troubleshooting-updates_{context}"]
= Troubleshooting {microshift-short} updates

[role="_abstract"]
In some cases, {microshift-short} might fail to update. In these events, it is helpful to understand failure types and how to troubleshoot them.

[id="microshift-update-path-blocked-by-version-sequence_{context}"]
== Update path is blocked by {microshift-short} version sequence
Non-EUS versions of {microshift-short} require serial updates. For example, if you attempt to update from {microshift-short} `4.15.5` directly to `4.17.1`, the update fails. You must first update `4.15.5` to `4.16.z`, and then you can update from `4.16.z` to `4.17.0`.

[id="microshift-update-path-blocked-by-version-incompatibility_{context}"]
== Update path is blocked by version incompatibility
RPM dependency errors result if a {microshift-short} update is incompatible with the version of {op-system-ostree-first} or {op-system-base-full}. For more information, see "{op-system-bundle} release compatibility matrix".

[id="microshift-ostree-update-failed_{context}"]
== {op-system-ostree} update failed
If you updated on an `rpm-ostree` system, the greenboot health check automatically logs and acts on system health. A system rollback by greenboot can indicate an update failure. In cases where the update failed, but greenboot did not complete a system rollback, you can troubleshoot using the {op-system-ostree} documentation linked in the "Additional resources" section.

* Manually check the greenboot logs to verify system health by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart --no-block greenboot-healthcheck && sudo journalctl -fu greenboot-healthcheck
----

[id="microshift-rpm-update-failed_{context}"]
== Manual RPM update failed
If you updated by using RPMs on a non-OSTree system, greenboot can indicate an update failure, but the health checks are only informative. Checking the system logs is the next step in troubleshooting a manual RPM update failure. You can use greenboot and the `sos report` tool to check both the {microshift-short} update and the host system.

[role="_additional-resources"]
.Additional resources

* {op-system-bundle} release compatibility matrix

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-troubleshoot-updates.adoc

[id="microshift-check-journal-logs-updates_{context}"]
= Checking journal logs after updates

[role="_abstract"]
You can use journal logs to help diagnose {microshift-short} update failures. The default configuration of the `systemd` journal service stores data in a volatile directory, which does not persist across restarts. To retain logs across restarts, enable log persistence and set a maximum size limit for journal data.

.Procedure

* Get comprehensive {microshift-short} journal logs by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u microshift
----

* Check the greenboot journal logs by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u greenboot-healthcheck
----

* Examining the comprehensive logs of a specific boot uses three steps. First list the boots, then select the one you want from the list you obtained:

** List the boots present in the journal logs by running the following command:
+
[source,terminal]
----
$ sudo journalctl --list-boots
----
+
.Example output
[source,text]
----
IDX  BOOT ID                          	FIRST ENTRY                 LAST ENTRY
 0   681ece6f5c3047e183e9d43268c5527f 	<Day> <Date> 12:27:58 UTC 	<Day> <Date>> 13:39:41 UTC
#....
----

** Check the journal logs for the specific boot by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo journalctl --boot __<idx_or_boot_id>_
----
+
where:
+
idx_or_boot_id::
Replace `_<idx_or_boot_id>_` with the `IDX` or the `BOOT ID` number assigned to the specific boot that you want to check.

** Check the journal logs for the boot of a specific service by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo journalctl --boot __<idx_or_boot_id>__ -u __<service_name>__
----
+
where:
+
idx_or_boot_id::
Replace `_<idx_or_boot_id>_` with the `IDX` or the `BOOT ID` number assigned to the specific boot that you want to check.
service_name::
Replace `_<service_name>_` with the name of the service that you want to check.

// Module included in the following assemblies:
//
// * microshift_running applications/checking-greenboot-scripts-status.adoc

[id="microshift-greenboot-check-status_{context}"]
= Checking the status of greenboot health checks

[role="_abstract"]
You can check the status of greenboot health checks before making changes to the system or while troubleshooting. By using helpful commands to verify that greenboot scripts have finished running.

.Procedure

* Check the current greenboot health check status by running the following command:
+
[source,terminal]
----
$ systemctl show --property=SubState --value greenboot-healthcheck.service
----
+
where:
+
`start`:: Greenboot checks are still running.
`exited`:: Checks have passed and greenboot has exited. Greenboot runs the scripts in the `green.d` directory when the system is in a healthy state.
`failed`:: Checks have not passed. Greenboot runs the scripts in the `red.d` directory when the system is in this state and restarts the system.

* Check the numerical exit code of the greenboot health check service by running the following command:
+
[source,terminal]
----
$ systemctl show --property=ExecMainStatus --value greenboot-healthcheck.service
----
+
An exit code of `0` means the health check succeeded. A non-zero exit code means the health check failed.

* To see a report showing a message about boot status, such as `Boot Status is GREEN - Health Check SUCCESS`, use the following command:
+
[source,terminal]
----
$ cat /run/motd.d/boot-status
----
+
.Example output
[source,text]
----
Boot Status is GREEN - Health Check SUCCESS
----

[id="additional-resources_microshift-troubleshoot-updates"]
[role="_additional-resources"]
== Additional resources
* Enabling `systemd` journal service data persistency
* Checking the MicroShift version
* Stopping the MicroShift service
* Starting the MicroShift service
* Composing, installing, and managing RHEL for Edge images
* Rolling back RHEL for Edge images
