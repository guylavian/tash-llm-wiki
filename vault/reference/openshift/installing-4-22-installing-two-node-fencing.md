---
title: "Preparing to install a two-node OpenShift cluster with fencing"
type: reference
domain: openshift
slug: installing-4-22-installing-two-node-fencing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-two-node-fencing
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing to install a two-node OpenShift cluster with fencing

[id="installing-two-node-fencing"]
= Preparing to install a two-node OpenShift cluster with fencing

[role="_abstract"]
A two-node OpenShift Container Platform cluster with fencing provides high availability (HA) with a reduced hardware footprint. This configuration is designed for distributed or edge environments where deploying a full three-node control plane cluster is not practical.

A two-node cluster does not include compute nodes. The two control plane machines run user workloads in addition to managing the cluster.

Fencing is managed by Pacemaker, which can isolate an unresponsive node by using the Baseboard Management Console (BMC) of the node. After the unresponsive node is fenced, the remaining node can safely continue operating the cluster without the risk of resource corruption.

[NOTE]
====
You can deploy a two-node OpenShift Container Platform cluster with fencing by using either the user-provisioned infrastructure method or the installer-provisioned infrastructure method.
====

The two-node OpenShift cluster with fencing requires the following hosts:

.Minimum required hosts
[options="header"]
|===

|Hosts |Description

|Two control plane machines
|The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane.

|One temporary bootstrap machine
|You need a bootstrap machine to deploy the OpenShift Container Platform cluster on the control plane machines. You can remove the bootstrap machine after you install the cluster.

|===

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. For instructions on installing RHCOS and starting the bootstrap process, see "Installing RHCOS and starting the OpenShift Container Platform bootstrap process".

[NOTE]
====
The requirement to use RHCOS applies only to user-provisioned infrastructure deployments. For installer-provisioned infrastructure deployments, the bootstrap and control plane machines are provisioned automatically by the installation program, and you do not need to manually install RHCOS.
====

[id="installation-two-node-fencing-minimum-resource-requirements_{context}"]
= Minimum resource requirements for installing the two-node OpenShift cluster with fencing

Each cluster machine must meet the following minimum requirements:

.Minimum resource requirements
[cols="2,2,2,2,2,2",options="header"]

|===

| Machine | Operating System | CPU ^[1]^ | RAM | Storage | Input/Output Per Second (IOPS) ^[1]^
| Bootstrap | RHCOS | 4 | 16 GB | 120 GB | 300
| Control plane |RHCOS | 4 | 16 GB | 120 GB | 300

|===

[.small]
--
1. One CPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = CPUs.
2. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.
--

// Two-node-dns-requirements - user-provisioned infrastructure
// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-network-customizations-user-infra.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="installation-dns-user-infra_{context}"]
= User-provisioned DNS requirements

[role="_abstract"]
In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

* The Kubernetes API
* The OpenShift Container Platform application wildcard
* The bootstrap and control plane machines
* The compute machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, and the control plane machines.

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because {op-system-first} uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

[NOTE]
====
It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the _DHCP recommendations for user-provisioned infrastructure_ section for more information.
====

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

.Required DNS records
[cols="1a,3a,5a",options="header"]
|===

|Component
|Record
|Description

.2+a|Kubernetes API
|`api.<cluster_name>.<base_domain>.`
|A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.

|`api-int.<cluster_name>.<base_domain>.`
|A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.
[IMPORTANT]
====
The API server must be able to resolve the worker nodes by the hostnames
that are recorded in Kubernetes. If the API server cannot resolve the node
names, then proxied API calls can fail, and you cannot retrieve logs from pods.
====

|Routes
|`*.apps.<cluster_name>.<base_domain>.`
|A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods.
By default, the Ingress Controller pods run on compute nodes. In cluster topologies without dedicated compute nodes, such as two-node or three-node clusters, the control plane nodes also carry the worker label, so the Ingress pods are scheduled on the control plane nodes.
The Ingress Controller pods run on the compute machines by default.
These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.

For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console.

|Bootstrap machine
|`bootstrap.<cluster_name>.<base_domain>.`
|A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap
machine. These records must be resolvable by the nodes within the cluster.

|Control plane machines
|`<control_plane><n>.<cluster_name>.<base_domain>.`
|DNS A/AAAA or CNAME records and DNS PTR records to identify each machine
for the control plane nodes. These records must be resolvable by the nodes within the cluster.

|Compute machines
|`<compute><n>.<cluster_name>.<base_domain>.`
|DNS A/AAAA or CNAME records and DNS PTR records to identify each machine
for the worker nodes. These records must be resolvable by the nodes within the cluster.

|===

[NOTE]
====
In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.
====

[TIP]
====
You can use the `dig` command to verify name and reverse name resolution. See the section on _Validating DNS resolution for user-provisioned infrastructure_ for detailed validation steps.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-user-infra.adoc
// * installing/installing_vmc/installing-vmc-network-customizations-user-infra.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="installation-dns-user-infra-example_{context}"]
= Example DNS configuration for user-provisioned clusters

[role="_abstract"]
Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

[NOTE]
====
In a two-node cluster with fencing, the control plane machines are also schedulable worker nodes. The DNS configuration must therefore include only the two control plane nodes. If you later add compute machines, provide corresponding A and PTR records for them as in a standard user-provisioned installation.
====

The following example is a BIND zone file that shows sample DNS A records for name resolution in a user-provisioned cluster.

[NOTE]
====
In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.
====

[source,text]
----
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
	IN	MX 10	smtp.example.com.
;
;
ns1.example.com.		IN	A	192.168.1.5
smtp.example.com.		IN	A	192.168.1.5
;
helper.example.com.		IN	A	192.168.1.5
helper.ocp4.example.com.	IN	A	192.168.1.5
;
api.ocp4.example.com.		IN	A	192.168.1.5
api-int.ocp4.example.com.	IN	A	192.168.1.5
;
*.apps.ocp4.example.com.	IN	A	192.168.1.5
;
bootstrap.ocp4.example.com.	IN	A	192.168.1.96
;
control-plane0.ocp4.example.com.	IN	A	192.168.1.97
control-plane1.ocp4.example.com.	IN	A	192.168.1.98
;
control-plane2.ocp4.example.com.	IN	A	192.168.1.99
;
compute0.ocp4.example.com.	IN	A	192.168.1.11
compute1.ocp4.example.com.	IN	A	192.168.1.7
;
;EOF
----

where:

`api.ocp4.example.com.`:: Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer.
`api-int.ocp4.example.com.`:: Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications.
`*.apps.ocp4.example.com.`:: Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods.
`bootstrap.ocp4.example.com`:: Provides name resolution for the bootstrap machine.
`control-plane0.ocp4.example.com`:: Provides name resolution for the control plane machines.
`compute0.ocp4.example.com.`:: Provides name resolution for the compute machines.

The following example BIND zone file shows sample PTR records for reverse name resolution in a user-provisioned cluster:

[source,text]
----
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
;
5.1.168.192.in-addr.arpa.	IN	PTR	api.ocp4.example.com.
5.1.168.192.in-addr.arpa.	IN	PTR	api-int.ocp4.example.com.
;
96.1.168.192.in-addr.arpa.	IN	PTR	bootstrap.ocp4.example.com.
;
97.1.168.192.in-addr.arpa.	IN	PTR	control-plane0.ocp4.example.com.
98.1.168.192.in-addr.arpa.	IN	PTR	control-plane1.ocp4.example.com.
;
99.1.168.192.in-addr.arpa.	IN	PTR	control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	compute1.ocp4.example.com.
;
;EOF
----

where:

`api.ocp4.example.com.`:: Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer.
`api-int.ocp4.example.com.`:: Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications.
`bootstrap.ocp4.example.com.`:: Provides reverse DNS resolution for the bootstrap machine.
`control-plane0.ocp4.example.com.`:: Provides rebootstrap.ocp4.example.com.verse DNS resolution for the control plane machines.
`compute0.ocp4.example.com.`:: Provides reverse DNS resolution for the compute machines.

[NOTE]
====
A PTR record is not required for the OpenShift Container Platform application wildcard.
====

// Two-node-dns-requirements - installer-provisioned infrastructure

[id="installation-installer-user-infra_{context}"]
= Installer-provisioned DNS requirements

//  Creating a manifest object that includes a customized br-ex bridge
[id="creating-manifest-custom-br-ex_{context}"]
= Creating a manifest object for a customized br-ex bridge

You must create a manifest object to modify the cluster’s network configuration after installation. The manifest configures the br-ex bridge, which manages external network connectivity for the cluster.

For instructions on creating this manifest, "Creating a manifest file for a customized br-ex bridge".

[role="_additional-resources"]
== Additional resources

* Installing RHCOS and starting the OpenShift Container Platform bootstrap process

* Creating a manifest file for a customized br-ex bridge

* Configuring and managing high availability clusters in RHEL.
