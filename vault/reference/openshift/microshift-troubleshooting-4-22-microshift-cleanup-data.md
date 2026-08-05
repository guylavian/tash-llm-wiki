---
title: "Cleaning up data with support"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-cleanup-data
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-cleanup-data
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Cleaning up data with support

[id="microshift-cleanup-data"]
= Cleaning up data with support

[role="_abstract"]
You can use the `microshift-cleanup-data` script for troubleshooting tasks such as deleting data, certificates, and container images.

[WARNING]
====
Do not run this script without the guidance of product Support. Contact Support by Submitting a support case.
====

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-cleanup-data.adoc

[id="microshift-data-cleaning-overview_{context}"]
= Data cleanup script overview

[role="_abstract"]
You can see the usage and list available options of the `microshift-cleanup-data` script by running the script without arguments. Running the script without arguments does not delete any data or stop the {microshift-short} service.

.Procedure

. See the usage and list the available options of the `microshift-cleanup-data` script by entering the following command:
+
[WARNING]
====
Some script operations are destructive and can cause data loss. Review the specific procedure for each argument for detailed warnings.
====
+
[source,terminal]
----
$ microshift-cleanup-data
----
+
.Example output
[source,terminal]
----
Stop all MicroShift services, also cleaning their data

Usage: microshift-cleanup-data <--all [--keep-images] | --ovn | --cert>
   --all         Clean all MicroShift and OVN data
   --keep-images Keep container images when cleaning all data
   --ovn         Clean OVN data only
   --cert        Clean certificates only
----

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-cleanup-data.adoc

[id="microshift-data-cleaning-full-cleanup_{context}"]
= Cleaning all data and configuration

[role="_abstract"]
You can clean up all the {microshift-short} data and configuration by running the `microshift-cleanup-data` script.

When you run the script with the `--all` argument, you perform the following clean up actions:

* Stop and disable all {microshift-short} services
* Delete all {microshift-short} pods
* Delete all container image storage
* Reset network configuration
* Delete the `/var/lib/microshift` data directory
* Delete OVN-K networking configuration

.Prerequisites
* You are logged into {microshift-short}.
* You have filed a support case.

.Procedure

. Clean up all the {microshift-short} data and configuration by running the `microshift-cleanup-data` script with the `--all` argument, by entering the following command:
+
[WARNING]
====
This option deletes all {microshift-short} data and user workloads. Use with caution.
====
+
[source,terminal]
----
$ sudo microshift-cleanup-data --all
----
+
[TIP]
====
The script prompts you to confirm the operation. Enter `1` or `Yes` to continue. Any other entry cancels the cleanup.
====
+
.Example output when you continue the cleanup
[source,terminal]
----
DATA LOSS WARNING: Do you wish to stop and clean ALL MicroShift data AND cri-o container workloads?
1) Yes
2) No
#? 1
Stopping MicroShift services
Disabling MicroShift services
Removing MicroShift pods
Removing crio image storage
Deleting the br-int interface
Killing conmon, pause and OVN processes
Removing MicroShift configuration
Removing OVN configuration
MicroShift service was stopped
MicroShift service was disabled
Cleanup succeeded
----
+
.Example output when you cancel the cleanup
[source,terminal]
----
DATA LOSS WARNING: Do you wish to stop and clean ALL MicroShift data AND cri-o container workloads?
1) Yes
2) No
#? no
Aborting cleanup
----
+
[IMPORTANT]
====
The `microshift-cleanup-data` script stops and disables the {microshift-short} service.
====
. Restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl enable --now microshift
----

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-cleanup-data.adoc

[id="microshift-data-cleaning-container-images_{context}"]
= Cleaning all data and keeping the container images

[role="_abstract"]
You can retain the {microshift-short} container images while cleaning all data by running the `microshift-cleanup-data` script with the `--all` and `--keep-images` arguments.

Keeping the container images helps speed up {microshift-short} restart after data clean up because the necessary container images are already present locally when you start the service.

When you run the script with the `--all` and `--keep-images` arguments, you perform the following clean up actions:

* Stop and disable all {microshift-short} services
* Delete all {microshift-short} pods
* Reset network configuration
* Delete the `/var/lib/microshift` data directory
* Delete OVN-K networking configuration

[WARNING]
====
This option deletes all {microshift-short} data and user workloads. Use with caution.
====

.Prerequisites
* You are logged into {microshift-short}.
* You have filed a support case.

.Procedure

. Clean up all data and user workloads when retaining the {microshift-short} container images by running the following command:
+
[source,terminal]
----
$ sudo microshift-cleanup-data --all --keep-images
----
+
.Example output
[source,terminal]
----
DATA LOSS WARNING: Do you wish to stop and clean ALL MicroShift data AND cri-o container workloads?
1) Yes
2) No
#? Yes
Stopping MicroShift services
Disabling MicroShift services
Removing MicroShift pods
Deleting the br-int interface
Killing conmon, pause and OVN processes
Removing MicroShift configuration
Removing OVN configuration
MicroShift service was stopped
MicroShift service was disabled
Cleanup succeeded
----
. Verify that the container images are still present by running the following command:
+
[source,terminal]
----
$ sudo crictl images | awk '{print $1}'
----
+
.Example output
[source,terminal]
----
IMAGE
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
quay.io/openshift-release-dev/ocp-v4.0-art-dev
registry.redhat.io/lvms4/topolvm-rhel9
registry.redhat.io/openshift4/ose-csi-external-provisioner
registry.redhat.io/openshift4/ose-csi-external-resizer
registry.redhat.io/openshift4/ose-csi-livenessprobe
registry.redhat.io/openshift4/ose-csi-node-driver-registrar
registry.redhat.io/ubi9
----
+
[IMPORTANT]
====
The `microshift-cleanup-data` script stops and disables the {microshift-short} service.
====
. Restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl enable --now microshift
----

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-cleanup-data.adoc

[id="microshift-data-cleaning-ovn-data_{context}"]
= Cleaning the OVN-Kubernetes data

[role="_abstract"]
Reset OVN-Kubernetes (OVN-K) network configurations by running the `microshift-cleanup-data` script.

When you run the script with the `--ovn` argument, you perform the following clean up actions:

* Stop all {microshift-short} services
* Delete all {microshift-short} pods
* Delete the OVN-K networking configuration

.Prerequisites
* You are logged into {microshift-short}.
* You have filed a support case.

.Procedure

. Clean up the OVN-K data by running the `microshift-cleanup-data` script with the `--ovn` argument, by entering the following command:
+
[source,terminal]
----
$ sudo microshift-cleanup-data --ovn
----
+
.Example output
[source,terminal]
----
Stopping MicroShift services
Removing MicroShift pods
Killing conmon, pause and OVN processes
Removing OVN configuration
MicroShift service was stopped
Cleanup succeeded
----
+
[IMPORTANT]
====
The `microshift-cleanup-data` script stops the {microshift-short} service.
====
. Restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-cleanup-data.adoc

[id="microshift-data-cleaning-certs_{context}"]
= Cleaning custom certificates data

[role="_abstract"]
To recreate {microshift-short} custom certificates upon service restart, reset them by using the `microshift-cleanup-data` script.

When you run the script with the `--cert` argument, you perform the following clean up actions:

* Stop all {microshift-short} services
* Delete all {microshift-short} pods
* Delete all {microshift-short} certificates

.Prerequisites
* You are logged into {microshift-short}.
* You have filed a support case.

.Procedure

. Clean up the {microshift-short} certificates by running the `microshift-cleanup-data` script with the `--cert` argument, by entering the following command:
+
[source,terminal]
----
$ sudo microshift-cleanup-data --cert
----
+
.Example output
[source,terminal]
----
Stopping MicroShift services
Removing MicroShift pods
Removing MicroShift certificates
MicroShift service was stopped
Cleanup succeeded
----
+
[IMPORTANT]
====
Running the script stops the {microshift-short} service.
====

. Restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----
