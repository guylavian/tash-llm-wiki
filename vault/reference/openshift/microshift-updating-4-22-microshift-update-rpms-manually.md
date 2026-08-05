---
title: "Updating RPMs manually"
type: reference
domain: openshift
slug: microshift-updating-4-22-microshift-update-rpms-manually
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_updating/microshift-update-rpms-manually
version: 4.22
family: microshift_updating
documentKind: "Documentation"
---

# Updating RPMs manually

[id="microshift-update-rpms-manually"]
= Updating RPMs manually

[role="_abstract"]
You can update {microshift-short} or {op-system-bundle} manually using RPMs.

//Module included in the following assemblies:
//
//*  microshift_updating/microshift-update-rpms.adoc

[id="microshift-updates-rpms-con_{context}"]
= About updates using RPMs

[role="_abstract"]
Updating OpenShift Container Platform for non-image-based {op-system-base-full} systems requires updating the RPMs.

* For patch releases, such as .1 to .2, simply update the RPMs.
* For minor-version release updates, add the step of enabling the compatible update repository by using your subscription manager.

[NOTE]
====
You can back up application data as needed and move the data copy to a secure location when using any update type.
====

//Module included in the following assemblies:
//
//*  microshift_updating/microshift-update-rpms.adoc

[id="microshift-applying-patch-updates-rpms_{context}"]
= Applying patch updates using RPMs

[role="_abstract"]
Updating {microshift-short} on non `rpm-ostree` systems such as {op-system-base-full} requires downloading then updating the RPMs. For example, use the following procedure to upgrade from 4.22.0 to 4.22.1.

[NOTE]
====
You cannot downgrade {microshift-short} with this process. Downgrades are not supported.
====

.Prerequisites

* The system requirements for installing {microshift-short} have been met.
* You have root user access to the host.
* The version of {microshift-short} you have is compatible to upgrade to the version you are preparing to use.
* You have verified that your host operating system is compatible with the version of {microshift-short} you are preparing to install.
* You have completed a system backup.

.Procedure

. Update the {microshift-short} RPMs by running the following command:
+
[source,terminal]
----
$ sudo dnf update microshift
----

. Restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----
+
[NOTE]
====
The greenboot system health check runs on this update type, but does not perform any actions. If the update fails, an error message appears with the instruction to check the logs.
====

//Module included in the following assemblies:
//
//*  microshift_updating/microshift-update-rpms.adoc

[id="microshift-updating-rpms_{context}"]
= Applying minor-version updates with RPMs

[role="_abstract"]
Updating a {microshift-short} minor version on non `rpm-ostree` systems such as {op-system-base-full} requires downloading then updating the RPMs. For example, use the following procedure to update from 4.18 to 4.20.

[NOTE]
====
You cannot downgrade {microshift-short} with this process. Downgrades are not supported.
====

.Prerequisites
* The system requirements for installing {microshift-short} have been met.
* You have root user access to the host.
* The version of {microshift-short} you have is compatible to upgrade to the version you are preparing to use.
* You have verified that your host operating system is compatible with the version of {microshift-short} you are preparing to install.
* You have completed a system backup.

.Procedure

. For all lifecycles, enable the repository for the release you want to update to by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager repos \
    --enable rhocp-{ocp-version}-for-rhel-{op-system-version-major}-$(uname -m)-rpms \
    --enable fast-datapath-for-rhel-{op-system-version-major}-$(uname -m)-rpms
----

. For extended support (EUS) releases, also enable the EUS repositories by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager repos \
    --enable rhel-{op-system-version-major}-for-$(uname -m)-appstream-eus-rpms \
    --enable rhel-{op-system-version-major}-for-$(uname -m)-baseos-eus-rpms
----

. Avoid unintended future updates into an unsupported configuration by locking your operating system version with the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager release --set={op-system-version}
----

. Update the {microshift-short} RPMs by running the following command:
+
[source,terminal]
----
$ sudo dnf update microshift
----

. Reboot the host to apply updates by running the following command:
+
[source,terminal]
----
$ sudo systemctl reboot
----
+
[NOTE]
====
The system health check runs on this update type, but does not perform any actions. If the update fails, an error message appears with the instruction to check the logs.
====

.Verification

. Check if the health checks exited with a successful boot by running the following command:
+
[source,terminal]
----
$ sudo systemctl status greenboot-healthcheck
----

. Check the health check logs by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u greenboot-healthcheck
----

[id="additional-resources_microshift-update-rpms-manually"]
[role="_additional-resources"]
== Additional resources

* Backup and restore
