---
title: "Updating RPMs on a RHEL for Edge system"
type: reference
domain: openshift
slug: microshift-updating-4-22-microshift-update-rpms-ostree
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_updating/microshift-update-rpms-ostree
version: 4.22
family: microshift_updating
documentKind: "Documentation"
---

# Updating RPMs on a RHEL for Edge system

[id="microshift-update-rpms-ostree"]
= Updating RPMs on a RHEL for Edge system

[role="_abstract"]
You can update {microshift-short} on {op-system-ostree-first} {rhel-major} by embedding the new version of {microshift-short} on a new operating system image.

//Module included in the following assemblies:
//
//*  microshift_updating/microshift-update-rpms-ostree.adoc

[id="microshift-updates-rpms-ostree-con_{context}"]
= {microshift-short} updates on an {op-system-ostree} system

[role="_abstract"]
Updating {microshift-short} on a {op-system-ostree-first} system requires building a new {op-system-ostree} image containing the new version of {microshift-short} and any associated optional RPMs.

After you create the `rpm-ostree` image with {microshift-short} embedded, you can boot into that operating system image.

The procedures are the same for minor-version and patch updates. For example, use the same steps to upgrade from 4.20 to 4.21 or from 4.21.2 to 4.21.3. The following details apply:

* Back up and system rollback are automatic with this update type.
* You can use the following workflow to update applications running in the {microshift-short} node. Ensure compatibilities between the application and the adjacent versions of {microshift-short} and {op-system-ostree} before starting an update.
* Downgrades other than automatic rollbacks are not supported. The following procedure is for updates only.
+
[IMPORTANT]
====
The steps you use depends on how your existing deployment is set up. The following procedure outlines the general steps you can take, with links to the {op-system-ostree} documentation. The {op-system-ostree} documentation is your resource for specific details on building an updated operating system image.
====

//Module included in the following assemblies:
//
//*  microshift_updating/microshift-update-rpms.adoc

[id="microshift-updates-rpms-ostree_{context}"]
= Applying updates on an {op-system-ostree} system

[role="_abstract"]
To update {microshift-short} on {op-system-ostree-first}, embed the new version of {microshift-short} on a new operating system image.

[IMPORTANT]
====
You cannot downgrade {microshift-short} with this process. Downgrades other than automatic rollbacks are not supported.
====

.Prerequisites

* The system requirements for installing {microshift-short} have been met.
* You have root user access to the host.
* The version of {microshift-short} you have is compatible with the {op-system-ostree} image you are preparing to use.

.Procedure

. Create an image builder configuration file for adding the `{rpm-repo-version}` RPM repository source required to pull {microshift-short} RPMs by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ cat > {rpm-repo-version}.toml <<EOF
id = "{rpm-repo-version}"
name = "Red Hat OpenShift Container Platform {ocp-version} for RHEL {op-system-version-major}"
type = "yum-baseurl"
url = "https://cdn.redhat.com/content/dist/layered/rhel9/$(uname -m)/rhocp/{ocp-version}/os"
check_gpg = true
check_ssl = true
system = false
rhsm = true
EOF
----

. Add the update RPM source to the image builder by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo composer-cli sources add {rpm-repo-version}.toml
----

. Build a new image of {op-system-ostree} that contains the new version of {microshift-short}. To determine the steps required, use the following documentation:

* Building a commit update

. Update the host to use the new image of {op-system-ostree}. To determine the steps required, use the following documentation:

* How RHEL for Edge image updates are deployed

. Reboot the host to apply updates by running the following command:
+
[source,terminal]
----
$ sudo systemctl reboot
----
