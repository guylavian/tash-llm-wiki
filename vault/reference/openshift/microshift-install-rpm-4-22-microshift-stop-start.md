---
title: "Stopping and starting {microshift-short}"
type: reference
domain: openshift
slug: microshift-install-rpm-4-22-microshift-stop-start
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_rpm/microshift-stop-start
version: 4.22
family: microshift_install_rpm
documentKind: "Documentation"
---

# Stopping and starting {microshift-short}

[id="microshift-stop-start"]
= Stopping and starting {microshift-short}

[role="_abstract"]
You can stop or start {microshift-short} for a variety of reasons, including a fresh installation, adding optional RPM packages, and troubleshooting.

// Module included in the following assemblies:
//
// microshift/microshift-install-rpm.adoc

[id="starting-microshift_service_{context}"]
= Starting the {microshift-short} service

[role="_abstract"]
Use the following procedure to start the {microshift-short} service.

.Prerequisites

* You have installed {microshift-short} from an RPM package.

.Procedure

. As a root user, start the {microshift-short} service by entering the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----

. Optional: To configure your {op-system-base} machine to start {microshift-short} when your machine starts, enter the following command:
+
[source,terminal]
----
$ sudo systemctl enable microshift
----

. Optional: To disable {microshift-short} from automatically starting when your machine starts, enter the following command:
+
[source,terminal]
----
$ sudo systemctl disable microshift
----
+
[NOTE]
====
The first time that the {microshift-short} service starts, it downloads and initializes the container images for {microshift-short}. As a result, it can take several minutes for {microshift-short} to start the first time that the service is deployed. Boot time is reduced for subsequent starts of the {microshift-short} service.
====

// Module included in the following assemblies:
//
// * microshift/microshift-install-rpm.adoc
// * microshift/microshift-update-rpms-ostree.adoc
// * microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="stopping-microshift-service_{context}"]
= Stopping the {microshift-short} service

[role="_abstract"]
When you want to stop the {microshift-short} service, you must stop both the service and any deployed workloads.

.Prerequisites

* The {microshift-short} service is running.

.Procedure

. Enter the following command to stop the {microshift-short} service:
+
[source,terminal]
----
$ sudo systemctl stop microshift
----

. Workloads deployed on {microshift-short} might continue running even after the {microshift-short} service has been stopped. Enter the following command to display running workloads:
+
[source,terminal]
----
$ sudo crictl ps -a
----

. Enter the following commands to stop the deployed workloads:
+
[source,terminal]
----
$ sudo systemctl stop kubepods.slice
----
