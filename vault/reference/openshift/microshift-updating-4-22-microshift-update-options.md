---
title: "Update options for Red Hat Device Edge"
type: reference
domain: openshift
slug: microshift-updating-4-22-microshift-update-options
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_updating/microshift-update-options
version: 4.22
family: microshift_updating
documentKind: "Documentation"
---

# Update options for Red Hat Device Edge

[id="microshift-update-options"]
= Update options for Red Hat Device Edge

[role="_abstract"]
To update {op-system-bundle}, you can update both OpenShift Container Platform and {op-system-base-full}, or each part by itself without updating the other. You must keep the parts in a supported configuration. Consider the following options when planning updates to your current deployments.

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-rhde-updates_{context}"]
= {op-system-bundle} updates

[role="_abstract"]
You can update {op-system-base-full} operating system independently of your OpenShift Container Platform version if the version combination is supported.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-install-get-ready.adoc
// * microshift_troubleshooting/microshift-troubleshoot-updates.adoc
// * microshift_updating/microshift-update-options.adoc

[id="microshift-rhde-compatibility-table_{context}"]
= {op-system-bundle} release compatibility matrix

[role="_abstract"]
{op-system-base-full} and {microshift-short} work together as a single solution for device-edge computing. You can update each component separately, but the product versions must be compatible.

Supported configurations of {op-system-bundle} use verified releases for each together as listed in the following table:

[NOTE]
====
Be sure to check the support status of a release on the product lifecycle page.
====

[%header,cols="3",cols="1,1,2"]
|===
^|*{op-system-base} Version(s)*
^|*{microshift-short} Version*
^|*Supported {microshift-short} Version{nbsp}&#8594;{nbsp}Version Updates*

^|10.2
^|4.22
^|4.22.0{nbsp}&#8594;{nbsp}4.22.z (Technology Preview)

^|9.8
^|4.22
^|4.22.0{nbsp}&#8594;{nbsp}4.22.z, 4.22 on {op-system-base} 9.8{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 10.2 (Technology Preview)

^|9.6
^|4.21
^|4.21.0{nbsp}&#8594;{nbsp}4.21.z, 4.21{nbsp}&#8594;{nbsp}4.22, 4.21{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 9.8, 4.21{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 10.2 (Technology Preview)

^|9.6
^|4.20
^|4.20.0{nbsp}&#8594;{nbsp}4.20.z, 4.20{nbsp}&#8594;{nbsp}4.21, 4.20{nbsp}&#8594;{nbsp}4.22 on {op-system-base} 10.2 (Technology Preview)

^|9.6
^|4.19
^|4.19.0{nbsp}&#8594;{nbsp}4.19.z, 4.19{nbsp}&#8594;{nbsp}4.20

^|9.4
^|4.18
^|4.18.0{nbsp}&#8594;{nbsp}4.18.z, 4.18{nbsp}&#8594;{nbsp}4.20 on {op-system-base} 9.6

^|9.4
^|4.17
^|4.17.1{nbsp}&#8594;{nbsp}4.17.z, 4.17{nbsp}&#8594;{nbsp}4.18

^|9.4
^|4.16
^|4.16.0{nbsp}&#8594;{nbsp}4.16.z, 4.16{nbsp}&#8594;{nbsp}4.17, 4.16{nbsp}&#8594;{nbsp}4.18
|===

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-standalone-updates_{context}"]
= Standalone {microshift-short} updates

[role="_abstract"]
You can update just your {microshift-short} version by embedding the new version in a {op-system-base} image or by installing the RPMs on a standard {op-system-base} operating system. Consider your current operating system version and deployments when planning a {microshift-short} update.

The following factors apply to a standalone {microshift-short} version update:

* {microshift-short} operates as an in-place update and does not require removal of the earlier version.
* Data backups beyond those required for the usual functioning of your applications are not required.
* You can potentially update {microshift-short} without reinstalling your applications and Operators.
* Only `rpm-ostree` updates include automatic rollbacks.

[IMPORTANT]
====
You must update {op-system-base} to update {microshift-short} if your current operating system is not compatible with the new version of {microshift-short} that you want to use.
====

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-rpm-ostree-updates_{context}"]
= Updating {microshift-short} on {op-system-ostree}

[role="_abstract"]
You can have automated backup and system rollback in case any part of the update fails by using the `rpm-ostree` update path for a new or existing {op-system-ostree} deployment.

* You can update {microshift-short} on an `rpm-ostree` system such as {op-system-ostree} by building a new system image containing the new version of {microshift-short}.
* The `rpm-ostree` image can be the same version or an updated version, but the versions of {op-system-ostree} and {microshift-short} must be compatible.

The following features are available in the {op-system-ostree} update path:

* The system automatically rolls back to an earlier healthy system state if the update fails.
* You do not need to reinstall applications.
* You do not need to reinstall Operators.
* You can update an application without updating {microshift-short} using this update type.
* The image you build can contain other updates as needed.

To begin a {microshift-short} update by embedding the new version in a {op-system-ostree} image, use the procedures in the following documentation:

* Applying updates on a RHEL for Edge system

To understand more about greenboot, see the following documentation:

* The greenboot health check framework

* Using greenboot for application and workload health checks

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-manual-rpm-updates_{context}"]
= Manual RPM updates

[role="_abstract"]
You can update {microshift-short} manually on {op-system-base-full} by updating the RPMs. This type of update is useful for development environments and testing.

* To complete this update type, use the subscription manager to enable the repository that has the new RPMs.
* Use manual processes to ensure system health and complete additional system backups.
* To begin a manual RPM update, use the procedures in the following documentation:

** About updating MicroShift RPMs manually

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-updates-rhde-config-rhel-repos_{context}"]
= Keeping {microshift-short} and {op-system-base} in a supported configuration

[role="_abstract"]
When using RPM updates, avoid creating an unsupported configuration or breaking your node by carefully managing your {op-system-base} repositories.

.Prerequisites

* You understand the support status of the version of {microshift-short} you are using.
* You have root-user access to your build host.
* You reviewed the {op-system-bundle} release compatibility matrix.

.Procedure

. Avoid unintended updates by locking your operating system version by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager release --set={op-system-version}
----

. If you are using an EUS {microshift-short} release, disable the {op-system-base} standard-support-scope repositories by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager repos \
    --disable=rhel-{op-system-version-major}-for-$(uname -m)-appstream-rpms \
    --disable=rhel-{op-system-version-major}-for-$(uname -m)-baseos-rpms
----
+
You can replace _{op-system-version-major}_ with the major version of your compatible {op-system-base} system if it is not same version given in this example.

. After you disable the standard-support repositories, enable the {op-system-base} EUS repos by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager repos \
    --enable rhel-{op-system-version-major}-for-$(uname -m)-appstream-eus-rpms \
    --enable rhel-{op-system-version-major}-for-$(uname -m)-baseos-eus-rpms
----
+
You can replace _{op-system-version-major}_ with the major version of your compatible {op-system-base} system if it is not same version given in this example.

.Verification

*  List the repositories you have enabled for {op-system-base} by running the following command:
+
[source,terminal]
----
$ sudo subscription-manager repos --list-enabled
----
+
.Example output
[source,terminal]
----
+----------------------------------------------------------+
    Available Repositories in /etc/yum.repos.d/redhat.repo
+----------------------------------------------------------+
Repo ID:   rhel-9-for-x86_64-baseos-eus-rpms
Repo Name: Red Hat Enterprise Linux 9 for x86_64 - BaseOS - Extended Update Support (RPMs)
Repo URL:  https://cdn.redhat.com/content/eus/rhel9/$releasever/x86_64/baseos/os
Enabled:   1
Repo ID:   rhel-9-for-x86_64-appstream-eus-rpms
Repo Name: Red Hat Enterprise Linux 9 for x86_64 - AppStream - Extended Update Support (RPMs)
Repo URL:  https://cdn.redhat.com/content/eus/rhel9/$releasever/x86_64/appstream/os
Enabled:   1
----

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-standalone-rhel-updates_{context}"]
= Standalone {op-system-base} updates

[role="_abstract"]
You can update to any {op-system-base} type without updating {microshift-short} if the two final versions in your {op-system-bundle} are compatible. Check compatibilities before beginning an update. Use the {op-system-base} documentation specific to your use case.

[role="_additional-resources"]
.Additional resources
* Red Hat Enterprise Linux 10
* Red Hat Enterprise Linux 9
* Composing, installing, and managing RHEL for Edge images
* Introducing image mode for RHEL

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-simultaneous-microshift-rhel-updates_{context}"]
= Simultaneous {microshift-short} and {op-system-base} updates

[role="_abstract"]
You can update your {op-system-base} operating system type and update {microshift-short} at the same time, if the final versions are a supported configuration of {op-system-bundle}. You can use following workflow to plan the general steps to take:

. Check for compatibility before beginning an update.
. Use the {op-system-base} documentation specific to your update path to plan and update the operating system.
. Enable the correct {microshift-short} repository to ensure alignment between your {op-system-base} and {microshift-short} versions.
. Use the {microshift-short} update type specific to your update path, such as using an RPM installation or embedding {microshift-short} into an operating system image.

// Module included in the following assemblies:
//
//microshift_updating/microshift-update-options.adoc

[id="microshift-migrate-rhel-edge-to-image-mode_{context}"]
= Migrating {microshift-short} from {op-system-ostree} to {op-system-image}

[role="_abstract"]
Starting with {microshift-short} 4.19, you can migrate your {microshift-short} node from {op-system-ostree} to {op-system-image} if the final versions are a supported configuration of {op-system-bundle}. Check compatibilities before beginning a migration. See the {op-system-base} documentation for instructions to migrate your image-based {op-system-base} system.

[id="additional-resources_microshift-update-options"]
[role="_additional-resources"]
== Additional resources

* How to Access EUS
* Composing a customized RHEL system image
* The greenboot system health check
* Greenboot workload health checks
