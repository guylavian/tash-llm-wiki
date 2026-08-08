---
title: "Migrating {microshift-short} from {op-system-ostree} to {op-system-image}"
type: reference
domain: openshift
slug: microshift-updating-4-22-microshift-update-rhel-edge-to-image-mode
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_updating/microshift-update-rhel-edge-to-image-mode
version: 4.22
family: microshift_updating
documentKind: "Documentation"
---

# Migrating {microshift-short} from {op-system-ostree} to {op-system-image}

[id="microshift-update-rhel-edge-to-image-mode"]
= Migrating {microshift-short} from {op-system-ostree} to {op-system-image}

[role="_abstract"]
To migrate {microshift-short} from {op-system-ostree-first}, embed {microshift-short} on a new {op-system-image} image.

//Module included in the following assemblies:
//
//*  microshift_updating/microshift-update-rhel-edge-to-image-mode.adoc

[id="microshift-update-options-edge-to-image-mode_{context}"]
= Migrating {microshift-short} to {op-system-image}

[role="_abstract"]
Migrating {microshift-short} from a {op-system-ostree-first} system to a {op-system-image} system requires building a new {op-system-image} image containing the required version of {microshift-short} and any associated optional RPMs.

See the {op-system-base-full} documentation for general instructions on migrating {op-system-ostree} systems to {op-system-image} using the `bootc switch` command. Plan the upgrade process carefully. The following tips apply:

* Follow the instructions in the {op-system-base} documentation for converting `rpm-ostree` blueprint files to image mode container files.
* You can use the `rpm-ostree compose container-encapsulate` image-compose command to create a base container image that can be used for bootc container builds. Then you can derive and familiarize yourself with an {op-system-image} image that is based on existing `ostree` commits.
* To fully adopt {op-system-image}, define a container build pipeline.
* Plan for UID and GID drift because {op-system-ostree} and {op-system-image} are not derived from the same parent image. See the {op-system-base} documentation for more information.

//Module included in the following assemblies:
//
//*  microshift_updating/microshift-update-rhel-edge-to-image-mode.adoc

[id="microshift-updates-edge-to-image-uid-drift_{context}"]
= Working around UID and GID drift when migrating to {op-system-image}

[role="_abstract"]
If you do not re-install operating systems that are running {microshift-short}, you must use a workaround for a possible UID and GID drift during the migration process. One way to solve this problem is to add `systemd` units that apply the necessary fixes before the affected system services are started.

.Prerequisites

* You have an existing {op-system-ostree} deployment running {microshift-short}.
* You have root access to the build host.
* You have an image that you want to deploy.

.Procedure

* Solve the potential UID or GID drift for the Open vSwitch (OVS) `systemd` service, `ovsdb-server.service`, by adding the following command to the {microshift-short} image-build procedure:
+
[source,terminal]
----
# Install systemd configuration drop-ins to fix potential permission problems when upgrading from rpm-ostree commits to image mode container layers
RUN mkdir -p /usr/lib/systemd/system/ovsdb-server.service.d && \
    cat > /usr/lib/systemd/system/ovsdb-server.service.d/microshift-ovsdb-ownership.conf <<'EOF'
# The openvswitch database files must be owned by the appropriate user and its primary group. That the user and its group can be overwritten, recreate them.
[Service]
ExecStartPre=/bin/sh -c '/bin/getent passwd openvswitch >/dev/null || useradd -r openvswitch'
ExecStartPre=/bin/sh -c '/bin/getent group hugetlbfs >/dev/null || groupadd -r hugetlbfs'
ExecStartPre=/sbin/usermod -a -G hugetlbfs openvswitch
ExecStartPre=/bin/chown -Rhv openvswitch. /etc/openvswitch
EOF
----
+
[IMPORTANT]
====
After the {microshift-short} migration to {op-system-image} is complete, this workaround is not needed and can be removed.
====
