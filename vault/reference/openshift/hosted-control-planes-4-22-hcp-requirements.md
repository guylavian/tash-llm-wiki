---
title: "Requirements for {hcp}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-requirements
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-requirements
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Requirements for {hcp}

[id="hcp-requirements"]
= Requirements for {hcp}

[role=_abstract]
Ensure you are familiar with the general requirements to deploy {hcp}.

The following requirements apply to {hcp}:

* In order to run the HyperShift Operator, your management cluster needs at least three worker nodes. In the context of {hcp}, a _management cluster_ is an OpenShift Container Platform cluster where the HyperShift Operator is deployed and where the control planes for hosted clusters are hosted.
+
The control plane is associated with a hosted cluster and runs as pods in a single namespace. When the cluster service consumer creates a hosted cluster, it creates a worker node that is independent of the control plane.

* You must open the firewall port `53` on Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) to allow the Domain Name Service (DNS) protocol to work as expected.

* You can run both the management cluster and the worker nodes on-premise, such as on a bare-metal platform or on {VirtProductName}. In addition, you can run both the management cluster and the worker nodes on cloud infrastructure, such as {aws-first}.

* If you use a mixed infrastructure, such as running the management cluster on {aws-short} and your worker nodes on-premise, or running your worker nodes on {aws-short} and your management cluster on-premise, you must use the `PublicAndPrivate` publishing strategy and follow the latency requirements in the support matrix.

* In Bare Metal Host (BMH) deployments, where the Bare Metal Operator starts machines, the hosted control plane must be able to reach baseboard management controllers (BMCs). If your security profile does not permit the Cluster Baremetal Operator to access the network where the BMHs have their BMCs in order to enable Redfish automation, you can use BYO ISO support. However, in BYO mode, OpenShift Container Platform cannot automate the powering on of BMHs.

//Support matrix for HCP
// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-prepare/hcp-requirements.adoc

[id="hcp-support-matrix_{context}"]
= Support matrix for {hcp}

[role="_abstract"]
Because {mce} includes the HyperShift Operator, releases of {hcp} align with releases of {mce-short}. The support matrix includes details about supported clusters, platforms, and architectures, as well as information about updates and technology preview features.

For more information, see "OpenShift Operator Life Cycles".

[id="hcp-matrix-mgmt_{context}"]
== Management cluster support

Any supported OpenShift Container Platform cluster can be a management cluster.

[NOTE]
====
A single-node OpenShift Container Platform cluster is not supported as a management cluster. If you have resource constraints, you can share infrastructure between a standalone OpenShift Container Platform control plane and {hcp}. For more information, see "Shared infrastructure between hosted and standalone control planes".
====

The following table maps {mce-short} versions to the management cluster versions that support them:

.Supported {mce-short} versions for OpenShift Container Platform management clusters
[cols="2",options="header"]
|===
|Management cluster version |Supported {mce-short} version

|4.14, 4.16
|2.6

|4.16
|2.7

|4.16, 4.18
|2.8

|4.18 - 4.19
|2.9

|4.18 - 4.20
|2.10

|4.19 - 4.21
|2.11

|4.20 - 4.22
|2.17
|===

[id="hcp-matrix-hc_{context}"]
== Hosted cluster support

For hosted clusters, no direct relationship exists between the management cluster version and the hosted cluster version. The hosted cluster version depends on the HyperShift Operator that is included with your {mce-short} version.

[NOTE]
====
Ensure a maximum latency of 200 ms between the management cluster and hosted clusters. This requirement is especially important for mixed infrastructure deployments, such as when your management cluster is on {aws-short} and your compute nodes are on-premise.
====

The following table shows the hosted cluster versions that you can create by using the HyperShift Operator that is associated with a version of {mce-short}:

[NOTE]
====
Although the HyperShift Operator supports the hosted cluster versions in the following table, {mce-short} supports only as far back as 2 versions earlier than the current version. For example, if the current hosted cluster version is 4.21, {mce-short} supports as far back as version 4.19. If you want to use a hosted cluster version that is earlier than one of the versions that {mce-short} supports, you can detach your hosted clusters from {mce-short} to be unmanaged, or you can use an earlier version of {mce-short}. For instructions to detach your hosted clusters from {mce-short}, see "Removing a cluster from management" ({rh-rhacm} documentation). For more information about {mce-short} support, see "The multicluster engine for Kubernetes operator 2.17 Support Matrix" (Red{nbsp}Hat Knowledgebase).
====

.Hosted cluster version mapped to HyperShift Operator associated with {mce-short} version
[cols="8",options="header"]
|===
|Hosted cluster version |HyperShift Operator in {mce-short} 2.6 |HyperShift Operator in {mce-short} 2.7 |HyperShift Operator in {mce-short} 2.8 |HyperShift Operator in {mce-short} 2.9 |HyperShift Operator in {mce-short} 2.10 |HyperShift Operator in {mce-short} 2.11 |HyperShift Operator in {mce-short} 2.17

|4.14
|Yes
|Yes
|Yes
|No
|No
|No
|No

|4.16
|Yes
|Yes
|Yes
|Yes
|No
|No
|No

|4.18
|No
|No
|Yes
|Yes
|Yes
|No
|No

|4.19
|No
|No
|No
|Yes
|Yes
|Yes
|No

|4.20
|No
|No
|No
|No
|Yes
|Yes
|Yes

|4.21
|No
|No
|No
|No
|No
|Yes
|Yes

|4.22
|No
|No
|No
|No
|No
|No
|Yes

|===

[id="hcp-matrix-platform_{context}"]
== Hosted cluster platform support

A hosted cluster supports only one infrastructure platform. For example, you cannot create multiple node pools on different infrastructure platforms.

The following table indicates which OpenShift Container Platform versions are supported for each platform of {hcp}.

[IMPORTANT]
====
For {ibm-power-title} and {ibm-z-title}:

* You must run the control plane on machine types that are based on 64-bit x86 architecture or s390x architecture
* You must run node pools on {ibm-power-title} or {ibm-z-title}
====

In the following table, the management cluster version is the OpenShift Container Platform version where the {mce-short} is enabled:

.Required OpenShift Container Platform versions for platforms
[cols="3",options="header"]
|===
|Hosted cluster platform |Management cluster version |Hosted cluster version

|{aws-full}
|4.16, 4.18 - 4.22
|4.16, 4.18 - 4.22

|{ibm-power-title}
|4.18 - 4.22
|4.18 - 4.22

|{ibm-z-title}
|4.18 - 4.22
|4.18 - 4.22

|{VirtProductName}
|4.14, 4.16, 4.18 - 4.22
|4.14, 4.16, 4.18 - 4.22

|Bare metal
|4.14, 4.16, 4.18 - 4.22
|4.14, 4.16, 4.18 - 4.22

|Non-bare-metal agent machines (Technology Preview)
|4.16, 4.18 - 4.22
|4.16, 4.18 - 4.22

|{rh-openstack-first} (Technology Preview)
|4.19 - 4.22
|4.19 - 4.22

|{azure-first} (Technology Preview)
|4.22
|4.22
|===

[id="hcp-matrix-multiarch_{context}"]
== Multi-architecture support

The following tables indicate the supported architectures for {hcp}, organized by platform. If an architecture is not listed, it is not yet fully supported.

.Multi-architecture support for {hcp}
[cols="4",options="header"]
|===
|Platform |Control planes |Compute nodes |OpenShift Container Platform version support

|{aws-short}
|64-bit x86
|64-bit x86
|4.16, 4.18 - 4.22

|{aws-short}
|64-bit x86
|ARM64
|4.18 - 4.22

|{aws-short}
|ARM64
|ARM64
|4.18 - 4.22

|{aws-short}
|ARM64
|64-bit x86
|4.18 - 4.22

|Bare metal (Agent platform)
|64-bit x86
|64-bit x86
|4.14, 4.16, 4.18 - 4.22

|Bare metal (Agent platform)
|64-bit x86
|ARM64
|4.21 - 4.22

|{ibm-power-title}
|64-bit x86
|64-bit x86
|4.19 - 4.22

|{ibm-power-title}
|64-bit x86
|ppc64le
|4.18 - 4.22

|{ibm-z-title}
|64-bit x86
|64-bit x86
|4.18 - 4.22

|{ibm-z-title}
|64-bit x86
|s390x
|4.18 - 4.22

|{ibm-z-title}
|s390x
|s390x
|4.20 - 4.22

|Non-bare-metal Agent machines (Technology Preview)
|64-bit x86
|64-bit x86
|4.16, 4.18 - 4.22

|{VirtProductName}
|64-bit x86
|64-bit x86
|4.14, 4.16, 4.18 - 4.22

|{VirtProductName}
|s390x
|s390x
|4.22

|{rh-openstack-first} (Technology Preview)
|64-bit x86
|64-bit x86
|4.19 - 4.22

|===

[id="hcp-matrix-updates_{context}"]
== Updates of {mce-short}

When you update to another version of the {mce-short}, your hosted cluster can continue to run if the HyperShift Operator that is included in the version of {mce-short} supports the hosted cluster version. The following table shows which hosted cluster versions are supported on which updated {mce-short} versions.

[NOTE]
====
Although the HyperShift Operator supports the hosted cluster versions in the following table, {mce-short} supports only as far back as 2 versions earlier than the current version. For example, if the current hosted cluster version is 4.21, {mce-short} supports as far back as version 4.19. If you want to use a hosted cluster version that is earlier than one of the versions that {mce-short} supports, you can detach your hosted clusters from {mce-short} to be unmanaged, or you can use an earlier version of {mce-short}. For instructions to detach your hosted clusters from {mce-short}, see "Removing a cluster from management" ({rh-rhacm} documentation). For more information about {mce-short} support, see "The multicluster engine for Kubernetes operator 2.17 Support Matrix" (Red{nbsp}Hat Knowledgebase).
====

.Hosted cluster version supported while updating {mce-short}
[cols="2",options="header"]
|===
|{mce-short} version |Supported hosted cluster version while updating

|Updating from 2.5 to 2.6
|OpenShift Container Platform 4.14, 4.16

|Updating from 2.6 to 2.7
|OpenShift Container Platform 4.14, 4.16

|Updating from 2.7 to 2.8
|OpenShift Container Platform 4.14, 4.16

|Updating from 2.8 to 2.9
|OpenShift Container Platform 4.16, 4.18

|Updating from 2.9 to 2.10
|OpenShift Container Platform 4.18, 4.19

|Updating from 2.10 to 2.11
|OpenShift Container Platform 4.19, 4.20

|Updating from 2.11 to 2.17
|OpenShift Container Platform 4.20, 4.21
|===

For example, if you have an OpenShift Container Platform 4.18 hosted cluster on the management cluster and you update from {mce-short} 2.8 to 2.9, the hosted cluster can continue to run.

[id="hcp-matrix-tp_{context}"]
== Technology Preview features

For a list of features in this release that have a Technology Preview status, see the "Technology Preview features status" section of the _{hcp-capital} release notes_.

[role="_additional-resources"]
.Additional resources

* OpenShift Operator Life Cycles
* Shared infrastructure between hosted and standalone control planes
* Technology Preview features status
* Removing a cluster from management
* The multicluster engine for Kubernetes operator 2.17 Support Matrix

//FIPS-enabled hosted clusters
// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-prepare/hcp-requirements.adoc

[id="hcp-fips_{context}"]
= FIPS-enabled hosted clusters

[role="_abstract"]
The binaries for {hcp} are FIPs-compliant, with the exception of the {hcp} command-line interface, `hcp`.

If you want to deploy a FIPS-enabled hosted cluster, you must use a FIPS-enabled management cluster. To enable FIPS mode for your management cluster, you must run the installation program from a {op-system-base-full} computer configured to operate in FIPS mode. For more information about configuring FIPS mode on {op-system-base}, see Switching {op-system-base} to FIPS mode.

When running {op-system-base} or {op-system-first} booted in FIPS mode, OpenShift Container Platform core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

After you set up your management cluster in FIPS mode, the hosted cluster creation process runs on that management cluster.

[role="_additional-resources"]
.Additional resources
* The multicluster engine for Kubernetes operator 2.17 Support Matrix
* Red{nbsp}Hat OpenShift Container Platform Operator Update Information Checker
* Shared infrastructure between hosted and standalone control planes

//CIDR ranges for hosted control planes
// Module included in the following assemblies:
//
// * /networking/networking_overview/cidr-range-definitions.adoc

[id="hcp-cidr-ranges_{context}"]
= CIDR ranges for {hcp}

[role="_abstract"]
To successfully deploy {hcp} on OpenShift Container Platform, define the network environment by using specific Classless Inter-Domain Routing (CIDR) subnet ranges.

The following Classless Inter-Domain Routing (CIDR) subnet ranges are the default settings for {hcp}:

* `v4InternalSubnet`: 100.65.0.0/16 (OVN-Kubernetes)
* `clusterNetwork`: 10.132.0.0/14 (pod network)
* `serviceNetwork`: 172.31.0.0/16

By using one of the default subnet ranges, you can avoid CIDR overlap with the management cluster and avoid connectivity issues. However, you can use other CIDR subnet ranges if they do not overlap with the management cluster.

[role="_additional-resources"]
.Additional resources
* CIDR range definitions
