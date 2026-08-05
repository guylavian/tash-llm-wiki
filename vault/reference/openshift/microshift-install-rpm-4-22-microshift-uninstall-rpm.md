---
title: "Uninstalling {microshift-short}"
type: reference
domain: openshift
slug: microshift-install-rpm-4-22-microshift-uninstall-rpm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_rpm/microshift-uninstall-rpm
version: 4.22
family: microshift_install_rpm
documentKind: "Documentation"
---

# Uninstalling {microshift-short}

[id="microshift-uninstall-rpm"]
= Uninstalling {microshift-short}

[role="_abstract"]
When you want to uninstall {microshift-short} RPMs, you must take specific steps to remove the data from your host.

// Module included in the following assemblies:
//
// microshift_install_rpm/microshift-uninstall.adoc

[id="microshift-uninstall-microshift-rpms_{context}"]
= Uninstalling {microshift-short} from an RPM package

[role="_abstract"]
When you want to uninstall {microshift-short}, you must first clean up all data, pods, and configurations before removing the RPM packages.

.Prerequisites

* You are logged into {microshift-short} as an administrator with root-user access.
* You have filed a support case.
* You have root access to the {microshift-short} node.

.Procedure

. Clean all your data by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo microshift-cleanup-data --all
----
+
When you run the script with the `--all` argument, you perform the following clean up actions:

* Stop and disable all {microshift-short} services
* Delete all {microshift-short} pods
* Delete all container image storage
* Reset network configuration
* Delete the `/var/lib/microshift` data directory
* Delete OVN-K networking configuration
+
. Run the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo dnf remove -y microshift*
----
+
