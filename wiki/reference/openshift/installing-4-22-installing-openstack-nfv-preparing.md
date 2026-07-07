---
title: "Preparing to install a cluster that uses SR-IOV or OVS-DPDK on OpenStack"
type: reference
domain: openshift
slug: installing-4-22-installing-openstack-nfv-preparing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-openstack-nfv-preparing
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing to install a cluster that uses SR-IOV or OVS-DPDK on OpenStack

[id="installing-openstack-nfv-preparing"]
= Preparing to install a cluster that uses SR-IOV or OVS-DPDK on OpenStack

Before you install a OpenShift Container Platform cluster that uses single-root I/O virtualization (SR-IOV) or Open vSwitch with the Data Plane Development Kit (OVS-DPDK) on {rh-openstack-first} or {rhoso-first}, you must understand the requirements for each technology and then perform preparatory tasks.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-nfv-preparing.adoc

[id="installation-openstack-nfv-requirements_{context}"]
= Requirements for clusters on {rh-openstack} or {rhoso} that use either SR-IOV or OVS-DPDK

[role="_abstract"]
If you use SR-IOV or OVS-DPDK with your deployment, you must meet the following requirements:

* OpenStack compute nodes must use a flavor that supports huge pages.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-nfv-preparing.adoc

[id="installation-openstack-sr-iov-requirements_{context}"]
= Requirements for clusters on {rh-openstack} or {rhoso} that use SR-IOV

[role="_abstract"]
To use single-root I/O virtualization (SR-IOV) with your deployment, you must meet the following requirements:

// TODO: Verify RHOSP 17.1 is still a supported platform for this OCP version.
* If you use {rh-openstack-first}, plan your {rh-openstack} SR-IOV deployment.

* If you use {rhoso-first}, plan your {rhoso} SR-IOV deployment by referring to _Deploying a network functions virtualization environment_.

* OpenShift Container Platform must support the NICs that you use. For a list of supported NICs, see "About Single Root I/O Virtualization (SR-IOV) hardware networks" in the "Hardware networks" subsection of the "Networking" documentation.

* For each node that will have an attached SR-IOV NIC, your OpenStack cluster must have:

   ** One instance from the quota
   ** One port attached to the machines subnet
   ** One port for each SR-IOV Virtual Function
   ** A flavor with at least 16 GB memory, 4 vCPUs, and 25 GB storage space

* SR-IOV deployments often employ performance optimizations, such as dedicated or isolated CPUs. For maximum performance, configure your underlying OpenStack deployment to use these optimizations, and then run OpenShift Container Platform compute machines on the optimized infrastructure.
// TODO: Verify RHOSP 17.1 is still a supported platform for this OCP version.
** If you use {rh-openstack}, see Configuring CPUs on Compute nodes.
** If you use {rhoso}, see NFV performance considerations in _Deploying a network functions virtualization environment_.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-nfv-preparing.adoc

[id="installation-openstack-ovs-dpdk-requirements_{context}"]
= Requirements for clusters on {rh-openstack} or {rhoso} that use OVS-DPDK

[role="_abstract"]
To use Open vSwitch with the Data Plane Development Kit (OVS-DPDK) with your deployment, you must meet the following requirements:

// TODO: Verify RHOSP 17.1 is still a supported platform for this OCP version.
* If you use {rh-openstack-first}:
** Plan your OVS-DPDK deployment by referring to Planning your OVS-DPDK deployment in _Configuring network functions virtualization_.
** Configure your OVS-DPDK deployment according to Configuring an OVS-DPDK deployment in _Configuring network functions virtualization_.

* If you use {rhoso-first}:
** Plan your OVS-DPDK deployment by referring to Planning an OVS-DPDK deployment in _Deploying a network functions virtualization environment_.
** Configure your OVS-DPDK deployment according to Creating the data plane for SR-IOV and DPDK environments in _Deploying a network functions virtualization environment_.

[id="installing-openstack-nfv-preparing-tasks-sr-iov"]
== Preparing to install a cluster that uses SR-IOV

You must configure your OpenStack platform before you install a cluster that uses SR-IOV on it.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-ovs-dpdk.adoc
// * installing/installing_openstack/installing-openstack-nfv-preparing.adoc
// * installing/installing_openstack/installing-openstack-user-sr-iov.adoc

[id="installation-osp-configuring-sr-iov_{context}"]
= Creating SR-IOV networks for compute machines

If your {rh-openstack-first} deployment supports single root I/O virtualization (SR-IOV), you can provision SR-IOV networks that compute machines run on.

[NOTE]
====
The following instructions entail creating an external flat network and an external, VLAN-based network that can be attached to a compute machine. Depending on your {rh-openstack} deployment, other network types might be required.
====

.Prerequisites

* Your cluster supports SR-IOV.
+
[NOTE]
====
If you are unsure about what your cluster supports, review the OpenShift Container Platform SR-IOV hardware networks documentation.
====

* You created radio and uplink provider networks as part of your {rh-openstack} deployment. The names `radio` and `uplink` are used in all example commands to represent these networks.

.Procedure

. On a command line, create a radio {rh-openstack} network:
+
[source,terminal]
----
$ openstack network create radio --provider-physical-network radio --provider-network-type flat --external
----

. Create an uplink {rh-openstack} network:
+
[source,terminal]
----
$ openstack network create uplink --provider-physical-network uplink --provider-network-type vlan --external
----

. Create a subnet for the radio network:
+
[source,terminal]
----
$ openstack subnet create --network radio --subnet-range <radio_network_subnet_range> radio
----

. Create a subnet for the uplink network:
+
[source,terminal]
----
$ openstack subnet create --network uplink --subnet-range <uplink_network_subnet_range> uplink
----

// . Create a port that allows machines to connect to your cluster and each other:
// +
// [source,terminal]
// ----
// $ openstack port os_port_worker_0 --network <infrastructure_id>-network --security-group <infrastructure_id>-worker --fixed-ip subnet=<infrastructure_id>-nodes,ip-address=<fixed_IP_address> --allowed-address ip-address=<infrastructure_ID>-ingress-port
// ----

// . Create a port for SR-IOV traffic:
// +
// [source,terminal]
// ----
// $ openstack port create radio_port --vnic-type direct --network radio --fixed-ip subnet=radio,ip-address=<fixed_IP_address> --tag=radio --disable-port-security
// ----

// . Create an {rh-openstack} server instance that uses the two ports you created as NICs:
// +
// [source,terminal]
// ----
// $ openstack server create --image <infrastructure_id>-rhcos --flavor ocp --user-data <ocp project>/build-artifacts/worker.ign --nic port-id=<os_port_worker_0 ID> --nic port-id=<radio_port_ID> --config-drive true worker-<worker_ID>.<cluster_name>.<cluster_domain>
// ----

[id="installing-openstack-nfv-preparing-tasks-ovs-dpdk"]
== Preparing to install a cluster that uses OVS-DPDK

You must configure your OpenStack platform before you install a cluster that uses OVS-DPDK on it.

// TODO: Verify RHOSP 17.1 is still a supported platform for this OCP version.
* If you use {rh-openstack-first}, create a flavor and deploy an instance for OVS-DPDK before you install a cluster on {rh-openstack}.

* If you use {rhoso-first}, create a custom OVS-DPDK compute service before you install a cluster on {rhoso}.

After you perform preinstallation tasks, install your cluster by following the most relevant OpenShift Container Platform on OpenStack installation instructions. Then, perform the tasks under "Next steps" on this page.

[role="_additional-resources"]
.Additional resources

* Creating a flavor and deploying an instance for OVS-DPDK
* Creating a custom OVS-DPDK Compute service

[id="next-steps_installing-openstack-nfv-preparing"]
== Next steps

* For either type of deployment:
** Configure the Node Tuning Operator with huge pages support.
* To complete SR-IOV configuration after you deploy your cluster:
** Install the SR-IOV Operator.
** Configure your SR-IOV network device.
** Create SR-IOV compute machines.
* Consult the following references after you deploy your cluster to improve its performance:
** A test pod template for clusters that use OVS-DPDK on OpenStack.
** A test pod template for clusters that use SR-IOV on OpenStack.
** A performance profile template for clusters that use OVS-DPDK on OpenStack
