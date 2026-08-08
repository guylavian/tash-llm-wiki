---
title: "Preparing to install on a single node"
type: reference
domain: openshift
slug: installing-4-22-install-sno-preparing-to-install-sno
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/install-sno-preparing-to-install-sno
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing to install on a single node

[id="preparing-to-install-sno"]
= Preparing to install on a single node

[id="preparing-to-install-sno_{context}"]
== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You have read the documentation on selecting a cluster installation method and preparing it for users.

// This is included in the following assemblies:
//
// installing_sno/install-sno-preparing-to-install-sno.adoc

[id="install-sno-about-installing-on-a-single-node_{context}"]
= About OpenShift on a single node

You can create a single-node cluster with standard installation methods. OpenShift Container Platform on a single node is a specialized installation that requires the creation of a special Ignition configuration file. The primary use case is for edge computing workloads, including intermittent connectivity, portable clouds, and 5G radio access networks (RAN) close to a base station. The major tradeoff with an installation on a single node is the lack of high availability.

[IMPORTANT]
====
The use of OpenShiftSDN with {sno} is not supported. OVN-Kubernetes is the default network plugin for {sno} deployments.
====
[IMPORTANT]
====
The use of OpenShiftSDN with {sno-okd} is not supported. OVN-Kubernetes is the default network plugin for {sno-okd} deployments.
====

// This is included in the following assemblies:
//
// installing_sno/install-sno-preparing-to-install-sno.adoc

[id="install-sno-requirements-for-installing-on-a-single-node_{context}"]
= Requirements for installing OpenShift on a single node

Installing OpenShift Container Platform on a single node alleviates some of the requirements for high availability and large scale clusters. However, you must address the following requirements:

* *Administration host:* You must have a computer to prepare the ISO, to create the USB boot drive, and to monitor the installation.
+
[NOTE]
====
For the `ppc64le` platform, the host should prepare the ISO, but does not need to create the USB boot drive. The ISO can be mounted to PowerVM directly.
====
+
[NOTE]
====
ISO is not required for {ibm-z-name} installations.
====

* *CPU Architecture:* Installing OpenShift Container Platform on a single node supports `x86_64`, `arm64`,`ppc64le`, and `s390x` CPU architectures.

* *Supported platforms:*
Installing OpenShift Container Platform on a single node is supported on bare metal and Certified third-party hypervisors. In most cases, you must specify the `platform.none: {}` parameter in the `install-config.yaml` configuration file. The following list shows the only exceptions and the corresponding parameter to specify in the `install-config.yaml` configuration file:
** {aws-first}, where you use `platform=aws`
** {gcp-first}, where you use `platform=gcp`
** {azure-first}, where you use `platform=azure`
* *Production-grade server:* Installing OpenShift Container Platform on a single node requires a server with sufficient resources to run OpenShift Container Platform services and a production workload.
+
.Minimum resource requirements
[options="header"]
|====
|Profile|Compute|Memory|Storage
|Minimum|4 vCPUs|16 GB of RAM| 120 GB
|====
+
[IMPORTANT]
====
Running {sno} on 4 vCPUs leaves very little "headroom" for user applications, and creates a high risk of resource contention and performance degradation.

To ensure cluster stability at this threshold, you must take steps to minimize the total resource footprint of the cluster, such as limiting the amount of workloads running on the cluster or limiting cluster capabilities.
For more information, see "Cluster capabilities".

Otherwise, it is recommended to provide more compute resources to the cluster.
====
+
[NOTE]
====
One vCPU generally equals one physical core. However, if you enable simultaneous multithreading (SMT), or Hyper-Threading, each CPU thread counts as a vCPU.

Adding Operators during the installation process might increase the minimum resource requirements.
====
+
The server must have a Baseboard Management Controller (BMC) when booting with virtual media.
+
[NOTE]
====
BMC is not supported on {ibm-z-name} and {ibm-power-name}.
====

* *Networking:* The server must have access to the internet or access to a local registry if it is not connected to a routable network. The server must have a DHCP reservation or a static IP address for the Kubernetes API, ingress route, and cluster node domain names. You must configure the DNS to resolve the IP address to each of the following fully qualified domain names (FQDN):
+
.Required DNS records
[options="header"]
|====
|Usage|FQDN|Description
|Kubernetes API|`api.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record. This record must be resolvable by both clients external to the cluster and within the cluster.
|Internal API|`api-int.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record when creating the ISO manually. This record must be resolvable by nodes within the cluster.
|Ingress route|`*.apps.<cluster_name>.<base_domain>`| Add a wildcard DNS A/AAAA or CNAME record that targets the node. This record must be resolvable by both clients external to the cluster and within the cluster.
|====
+
[IMPORTANT]
====
Without persistent IP addresses, communications between the `apiserver` and `etcd` might fail.
====

[role="_additional-resources"]
.Additional resources

* Cluster capabilities
