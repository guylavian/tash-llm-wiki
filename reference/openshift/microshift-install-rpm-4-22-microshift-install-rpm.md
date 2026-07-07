---
title: "Installing from an RPM package"
type: reference
domain: openshift
slug: microshift-install-rpm-4-22-microshift-install-rpm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_rpm/microshift-install-rpm
version: 4.22
family: microshift_install_rpm
documentKind: "Documentation"
---

# Installing from an RPM package

[id="microshift-install-rpm"]
= Installing from an RPM package

[role="_abstract"]
You can install {microshift-short} from an RPM package on a machine with a supported version of {op-system-base-full}.

// Module included in the following assemblies:
//
// microshift/microshift-install-rpm.adoc

[id="microshift-install-rpm-before_{context}"]
= Before installing {microshift-short} from an RPM package

[role="_abstract"]
Before installing {microshift-short} for memory configuration and FIPS mode, you must prepare the host.

[id="microshift-configuring-volume-groups_{context}"]
== Configuring volume groups

{microshift-short} uses the logical volume manager storage (LVMS) Container Storage Interface (CSI) plugin for providing storage to persistent volumes (PVs). LVMS relies on the Linux logical volume manager (LVM) to dynamically manage the backing logical volumes (LVs) for PVs. For this reason, your machine must have an LVM volume group (VG) with unused space in which LVMS can create the LVs for your workload's PVs.

To configure a volume group (VG) that allows LVMS to create the LVs for your workload's PVs, lower the *Desired Size* of your root volume during the installation of {op-system-base}. Lowering the size of your root volume allows unallocated space on the disk for additional LVs created by LVMS at runtime.

[id="microshift-prepare-for-fips-mode_{context}"]
== Prepare for FIPS mode

If your use case requires running {microshift-short} containers in FIPS mode, you must install {op-system-base} with FIPS enabled. After the worker machine is configured to run in FIPS mode, your {microshift-short} containers are automatically configured to also run in FIPS mode.

[IMPORTANT]
====
Because FIPS must be enabled before the operating system that your node uses starts for the first time, you cannot enable FIPS after you deploy a node.
====

// Module included in the following assemblies:
//
// microshift/microshift-install-rpm.adoc

[id="microshift-install-rpm-preparing_{context}"]
= Preparing to install {microshift-short} from an RPM package

[role="_abstract"]
When you are getting ready to install {microshift-short} RPMs, make sure you have enough storage capacity for the workload you want to run.

.Prerequisites

* The system requirements for installing {microshift-short} have been met.
* You have root user access to your machine.
* You have configured your LVM VG with the capacity needed for the PVs of your workload.

.Procedure

. In the graphical installer under *Installation Destination* in the *Storage Configuration* subsection, select *Custom* -> *Done* to open the dialog for configuring partitions and volumes. The Manual Partitioning window is displayed.

. Under *New Red Hat Enterprise Linux {op-system-version-major}.x Installation*, select *Click here to create them automatically*.

. Select the root partition, */*, reduce *Desired Capacity* so that the VG has sufficient capacity for your PVs, and then click *Update Settings*.

. Complete your installation.
+
[NOTE]
====
For more options on partition configuration, read the guide linked in the Additional information section for Configuring Manual Partitioning.
====

. As a root user, verify the VG capacity available on your system by running the following command:
+
[source,terminal]
----
$ sudo vgs
----
+
Example output:
+
[source,terminal]
----
VG   #PV #LV #SN Attr   VSize    VFree
rhel   1   2   0 wz--n- 127.00g 54.94g
----

// Module included in the following assemblies:
//
// microshift/microshift-install-rpm.adoc

[id="installing-microshift-from-rpm-package_{context}"]
= Installing {microshift-short} from an RPM package

[role="_abstract"]
Use the following procedure to install {microshift-short} from an RPM package.

.Prerequisites

* The system requirements for installing {microshift-short} have been met.
* You completed the steps of preparing to install {microshift-short} from an RPM package.

.Procedure

. For all lifecycles, enable the repository for your release by running the following command:
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

. Install {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y microshift
----

. Download your installation pull secret from the https://console.redhat.com/openshift/install/pull-secret[Red Hat Hybrid Cloud Console] to a temporary folder, for example, `$HOME/openshift-pull-secret`. This pull secret allows you to authenticate with the container registries that serve the container images used by OpenShift Container Platform.

. To copy the pull secret to the `/etc/crio` folder of your {op-system-base} machine, run the following command:
+
[source,terminal]
----
$ sudo cp $HOME/openshift-pull-secret /etc/crio/openshift-pull-secret
----

. Make the root user the owner of the `/etc/crio/openshift-pull-secret` file by running the following command:
+
[source,terminal]
----
$ sudo chown root:root /etc/crio/openshift-pull-secret
----

. Make the `/etc/crio/openshift-pull-secret` file readable and writeable by the root user only by running the following command:
+
[source,terminal]
----
$ sudo chmod 600 /etc/crio/openshift-pull-secret
----

. If your {op-system-base} machine has a firewall enabled, you must configure a few mandatory firewall rules. For `firewalld`, run the following commands:
+
[source,terminal]
----
$ sudo firewall-cmd --permanent --zone=trusted --add-source=10.42.0.0/16
----
+
[source,terminal]
----
$ sudo firewall-cmd --permanent --zone=trusted --add-source=169.254.169.1
----
+
[source,terminal]
----
$ sudo firewall-cmd --reload
----

. If the Volume Group (VG) that you have prepared for {microshift-short} used the default name `rhel`, no further configuration is necessary. If you have used a different name, or if you want to change more configuration settings, see the "Using the {microshift-short} configuration file" section.

[id="additional-resources_microshift-install-rpm"]
[role="_additional-resources"]
== Additional resources
* Using FIPS mode with {microshift-short}
* Pull secret from {cluster-manager-first}
* Customizing {microshift-short} by using the configuration file
* Configuring manual partitioning
* Overview of logical volume management
* Managing LVM Volume Groups
