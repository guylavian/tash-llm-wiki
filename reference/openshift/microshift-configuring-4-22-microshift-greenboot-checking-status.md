---
title: "Checking greenboot scripts status"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-greenboot-checking-status
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-greenboot-checking-status
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Checking greenboot scripts status

[id="microshift-greenboot-checking-status"]
= Checking greenboot scripts status

[role="_abstract"]
To deploy applications or make other changes through the {microshift-short} API with tools other than `kustomize` manifests, you must wait until the greenboot health checks have finished. This ensures that your changes are not lost if greenboot rolls your `rpm-ostree` system back to an earlier state.

The `greenboot-healthcheck` service runs one time and then exits. After greenboot has exited and the system is in a healthy state, you can proceed with configuration changes and deployments.

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
