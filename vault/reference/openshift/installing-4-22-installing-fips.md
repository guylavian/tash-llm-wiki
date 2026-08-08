---
title: "Support for FIPS cryptography"
type: reference
domain: openshift
slug: installing-4-22-installing-fips
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-fips
version: 4.22
family: installing
documentKind: "Documentation"
---

# Support for FIPS cryptography

[id="installing-fips"]
= Support for FIPS cryptography

[role="_abstract"]
You can install an OpenShift Container Platform cluster in FIPS mode.

OpenShift Container Platform is designed for FIPS. When running {op-system-base-full} or {op-system-first} booted in FIPS mode, OpenShift Container Platform core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

For more information about the NIST validation program, see "Cryptographic Module Validation Program" in the _Additional resources_ section. For the latest NIST status for the individual versions of {op-system-base} cryptographic libraries that have been submitted for validation, see "Compliance Activities and Government Standards" in the _Additional resources_ section.

[IMPORTANT]
====
To enable FIPS mode for your cluster, you must run the installation program from a {op-system-base} 9 computer that is configured to operate in FIPS mode, and you must use a FIPS-capable version of the installation program. See the section titled _Obtaining a FIPS-capable installation program using `oc adm extract`_.

For more information about configuring FIPS mode on {op-system-base}, see "Installing the system in FIPS mode" in the _Additional resources_ section.
====

For the {op-system-first} machines in your cluster, this change is applied when the machines are deployed based on the status of an option in the `install-config.yaml` file, which governs the cluster options that a user can change during cluster deployment. With {op-system-base-full} machines, you must enable FIPS mode when you install the operating system on the machines that you plan to use as worker machines.

Because FIPS must be enabled before the operating system that your cluster uses boots for the first time, you cannot enable FIPS after you deploy a cluster.

// Module included in the following assembly:
// installing/installing-fips.adoc

[id="installation-obtaining-fips-installer-oc_{context}"]
= Obtaining a FIPS-capable installation program using `oc adm extract`

OpenShift Container Platform requires the use of a FIPS-capable installation binary to install a cluster in FIPS mode. You can obtain this binary by extracting it from the release image by using the {oc-first}. After you have obtained the binary, you proceed with the cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.

.Prerequisites

* You have installed the {oc-first} with version 4.16 or newer.

.Procedure

. Extract the FIPS-capable binary from the installation program by running the following command:
+
[source,terminal]
----
$ oc adm release extract --registry-config "${pullsecret_file}" --command=openshift-install-fips --to "${extract_dir}" ${RELEASE_IMAGE}
----
+
where:
+
--
`<pullsecret_file>`:: Specifies the name of a file that contains your pull secret.
`<extract_dir>`:: Specifies the directory where you want to extract the binary.
`<RELEASE_IMAGE>`:: Specifies the Quay.io URL of the OpenShift Container Platform release you are using. For more information on finding the release image, see _Extracting the OpenShift Container Platform installation program_.
--
. Proceed with cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Cryptographic Module Validation Program

* Compliance Activities and Government Standards

* Installing the system in FIPS mode

* Extracting the OpenShift Container Platform installation program

// Module included in the following assembly:
// installing/installing-fips.adoc

[id="installation-obtaining-fips-installer-mirror_{context}"]
= Obtaining a FIPS-capable installation program using the public OpenShift mirror

[role="_abstract"]
OpenShift Container Platform requires the use of a FIPS-capable installation binary to install a cluster in FIPS mode. You can obtain this binary by downloading it from the public OpenShift mirror. After you have obtained the binary, proceed with the cluster installation, replacing all instances of the `openshift-install` binary with `openshift-install-fips`.

.Prerequisites

* You have access to the internet.

.Procedure

. Download the installation program from https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.18/openshift-install-rhel9-amd64.tar.gz.

. Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar -xvf openshift-install-rhel9-amd64.tar.gz
----

. Proceed with cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.

// Module included in the following assembly:
// installing/installing-fips.adoc

[id="installation-about-fips-validation_{context}"]
= FIPS validation in OpenShift Container Platform

[role="_abstract"]
OpenShift Container Platform uses certain FIPS validated or Modules In Process modules within {op-system-base} and {op-system} for the operating system components that it uses.

For more information, see "RHEL core crypto components" in the _Additional resources_ section. For example, when users use SSH to connect to OpenShift Container Platform clusters and containers, those connections are properly encrypted.

OpenShift Container Platform components are written in Go and built with Red Hat's golang compiler. When you enable FIPS mode for your cluster, all OpenShift Container Platform components that require cryptographic signing call {op-system-base} and {op-system} cryptographic libraries.

.FIPS mode attributes and limitations in OpenShift Container Platform 
[cols="8a,8a",options="header"]
|===

|Attributes
|Limitations

|FIPS support in {op-system-base} 9 and {op-system} operating systems.
.4+|The FIPS implementation does not use a function that performs hash computation and signature generation or validation in a single step. This limitation will continue to be evaluated and improved in future OpenShift Container Platform releases.

|FIPS support in CRI-O runtimes.
|FIPS support in OpenShift Container Platform services.
|FIPS validated or Modules In Process cryptographic module and algorithms that are obtained from {op-system-base} 9 and {op-system} binaries and images.

|Use of FIPS compatible golang compiler.
|TLS FIPS support is not complete but is planned for future OpenShift Container Platform releases.

|FIPS support across multiple architectures.
|FIPS is currently only supported on OpenShift Container Platform deployments using `x86_64`, `ppc64le`, and `s390x` architectures.

|===

[role="_additional-resources"]
.Additional resources

* RHEL core crypto components

// Module included in the following assembly:
// installing/installing-fips.adoc

[id="installation-about-fips-components_{context}"]
= FIPS support in components that the cluster uses

[role="_abstract"]
Although the OpenShift Container Platform cluster itself uses FIPS validated or Modules In Process modules, ensure that the systems that support your OpenShift Container Platform cluster use FIPS validated or Modules In Process modules for cryptography.

etcd::

To ensure that the secrets that are stored in etcd use FIPS validated or Modules In Process encryption, boot the node in FIPS mode. After you install the cluster in FIPS mode, you can encrypt the etcd data by using the FIPS-approved `aes cbc` cryptographic algorithm.

Storage::

For local storage, use {op-system-base}-provided disk encryption or Container Native Storage that uses {op-system-base}-provided disk encryption. By storing all data in volumes that use {op-system-base}-provided disk encryption and enabling FIPS mode for your cluster, both data at rest and data in motion, or network data, are protected by FIPS validated or Modules In Process encryption. You can configure your cluster to encrypt the root filesystem of each node. For more information, see "Customizing nodes" in the _Additional resources_ section.

Runtimes::

To ensure that containers know that they are running on a host that is using FIPS validated or Modules In Process cryptography modules, use CRI-O to manage your runtimes.

[role="_additional-resources"]
.Additional resources

* Encrypt the etcd data
* Customizing nodes

// Module included in the following assembly:
// installing/installing-fips.adoc

[id="installing-fips-mode_{context}"]
= Installation of a cluster in FIPS mode

[role="_abstract"]
To install a cluster in FIPS mode, follow the instructions to install a customized cluster on your preferred infrastructure. Ensure that you set `fips: true` in the `install-config.yaml` file before you deploy your cluster.

[IMPORTANT]
====
To enable FIPS mode for your cluster, you must run the installation program from a {op-system-base} computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see Installing the system in FIPS mode.
====

* Amazon Web Services
* Microsoft Azure
* Bare metal
* {gcp-full}
* {ibm-cloud-name}
* {ibm-power-name}
* {ibm-z-name} and {ibm-linuxone-name}
* {ibm-z-name} and {ibm-linuxone-name} with {op-system-base} KVM
* {ibm-z-name} and {ibm-linuxone-name} in an LPAR
* {rh-openstack-first}
* VMware vSphere

[NOTE]
====
If you are using Azure File storage, you cannot enable FIPS mode.
====

To apply `AES CBC` encryption to your etcd data store, follow the "Encrypting etcd data" process after you install your cluster.

[role="_additional-resources"]
.Additional resources

* Encrypting etcd data
