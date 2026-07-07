---
title: "About clusters with multi-architecture compute machines"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-multi-architecture-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/multi-architecture-configuration
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# About clusters with multi-architecture compute machines

[id="post-install-multi-architecture-configuration"]
= About clusters with multi-architecture compute machines

[role="_abstract"]
An OpenShift Container Platform cluster with multi-architecture compute machines is a cluster that supports compute machines with different architectures.

Configuring multi-architecture compute machines involves some additional considerations:

* When there are nodes with multiple architectures in your cluster, the architecture of the container image that you deploy to a node must be consistent with the architecture of that node. You need to ensure that the pod is assigned to the node with the appropriate architecture and that it matches the container image architecture. For more information on assigning pods to nodes, see "Assigning pods to nodes".

* In installer-provisioned installations, you are restricted to using the infrastructure provided by a single cloud provider. Adding external nodes, regardless of their architecture, to these clusters is not supported.

* Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.
+
[IMPORTANT]
====
See "Deploying OpenShift 4.x on non-tested platforms using the bare metal install method" before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments.
====

* The Cluster Samples Operator is not supported on clusters with multi-architecture compute machines. Your cluster can be created without this capability. For more information, see "Cluster capabilities".

* For information on migrating your single-architecture cluster to a cluster that supports multi-architecture compute machines, see "Migrating to a cluster with multi-architecture compute machines".

// Configuring your cluster with multi-architecture compute machines
// Module included in the following assemblies:

// * post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-configuration.adoc

[id="multi-architecture-configuring-your-cluster_{context}"]
= Configuring your cluster with multi-architecture compute machines

[role="_abstract"]
To create a cluster with multi-architecture compute machines with different installation options and platforms, see the documentation references.

.Cluster with multi-architecture compute machine installation options
[cols="3,1,1,1,1,1",options="header"]
|===
|Documentation section |Platform |User-provisioned installation |Installer-provisioned installation |Control Plane |Compute node

|"Creating a cluster with multi-architecture compute machines on Azure"
|Microsoft Azure
|&#10003;
|&#10003;
|`aarch64` or `x86_64`
|`aarch64`, `x86_64`

|"Creating a cluster with multi-architecture compute machines on AWS"
|Amazon Web Services (AWS)
|&#10003;
|&#10003;
|`aarch64` or `x86_64`
|`aarch64`, `x86_64`

|"Creating a cluster with multi-architecture compute machines on {gcp-short}"
|{gcp-first}
|
|&#10003;
|`aarch64` or `x86_64`
|`aarch64`, `x86_64`

.3+|"Creating a cluster with multi-architecture compute machines on bare metal, {ibm-power-title}, or {ibm-z-title}"
|Bare metal
|&#10003;
|&#10003;
|`aarch64` or `x86_64`
|`aarch64`, `x86_64`

|{ibm-power-title}
|&#10003;
|
|`x86_64` or `ppc64le`
|`x86_64`, `ppc64le`

|{ibm-z-title}
|&#10003;
|
|`x86_64` or `s390x`
|`x86_64`, `s390x`

|"Creating a cluster with multi-architecture compute machines on {ibm-z-name} and {ibm-linuxone-name} with z/VM"
|{ibm-z-name} and {ibm-linuxone-name}
|&#10003;
|
|`x86_64`, `s390x`
|`x86_64`, `s390x`

|"Creating a cluster with multi-architecture compute machines on {ibm-z-name} and {ibm-linuxone-name} with {op-system-base} KVM"
|{ibm-z-name} and {ibm-linuxone-name}
|&#10003;
|
|`x86_64`, `s390x`
|`x86_64`, `s390x`

|"Creating a cluster with multi-architecture compute machines on {ibm-power-name}"
|{ibm-power-name}
|&#10003;
|
|`x86_64`
|`x86_64`, `ppc64le`

|===

[role="_additional-resources"]
.Additional resources

* Creating a cluster with multi-architecture compute machines on Azure

* Creating a cluster with multi-architecture compute machines on AWS

* Creating a cluster with multi-architecture compute machines on {gcp-short}

* Creating a cluster with multi-architecture compute machines on bare metal, {ibm-power-title}, or {ibm-z-title}

* Creating a cluster with multi-architecture compute machines on {ibm-z-name} and {ibm-linuxone-name} with z/VM

* Creating a cluster with multi-architecture compute machines on {ibm-z-name} and {ibm-linuxone-name} with {op-system-base} KVM

* Creating a cluster with multi-architecture compute machines on {ibm-power-name}

// Verifying cluster compatibility
// Module included in the following assemblies:

// * post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-configuration.adoc

[id="multi-architecture-verifying-cluster-compatibility_{context}"]
= Verifying cluster compatibility

[role="_abstract"]
Before you can start adding compute nodes of different architectures to your cluster, you must verify that your cluster is multi-architecture compatible.

.Prerequisites

* You installed the {oc-first}.
* {ibm-power-title} only: Ensure that you meet the following prerequisites:
** When using multiple architectures, hosts for OpenShift Container Platform nodes must share the same storage layer. If they do not have the same storage layer, use a storage provider such as `nfs-provisioner`.
** You should limit the number of network hops between the compute and control plane as much as possible.

.Procedure

. Log in to the {oc-first}.

. You can check that your cluster uses the architecture payload by running the following command:
+
[source,terminal]
----
$ oc adm release info -o jsonpath="{ .metadata.metadata}"
----

.Verification

* If you see the following output, your cluster is using the multi-architecture payload:
+
[source,terminal]
----
{
 "release.openshift.io/architecture": "multi",
 "url": "https://access.redhat.com/errata/<errata_version>"
}
----
You can then begin adding multi-arch compute nodes to your cluster.

* If you see the following output, your cluster is not using the multi-architecture payload:
+
[source,terminal]
----
{
 "url": "https://access.redhat.com/errata/<errata_version>"
}
----
+
[IMPORTANT]
====
To migrate your cluster so the cluster supports multi-architecture compute machines, see "Migrating to a cluster with multi-architecture compute machines".
====

[role="_additional-resources"]
.Additional resources

* Migrating to a cluster with multi-architecture compute machines

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Assigning pods to nodes

* Deploying OpenShift 4.x on non-tested platforms using the bare metal install method (Red{nbsp}Hat Knowledgebase article)

* Cluster capabilities

* Migrating to a cluster with multi-architecture compute machines
