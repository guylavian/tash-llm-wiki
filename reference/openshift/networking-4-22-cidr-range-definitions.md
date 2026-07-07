---
title: "CIDR range definitions"
type: reference
domain: openshift
slug: networking-4-22-cidr-range-definitions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/cidr-range-definitions
version: 4.22
family: networking
documentKind: "Documentation"
---

# CIDR range definitions

[id="cidr-range-definitions"]
= CIDR range definitions

[role="_abstract"]
If your cluster uses OVN-Kubernetes, you must specify non-overlapping ranges for Classless Inter-Domain Routing (CIDR) subnet ranges.

[IMPORTANT]
====
For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` for IPv4 and `fd69::/112` for IPv6 as the default masquerade subnet. You must avoid these ranges. For upgraded clusters, there is no change to the default masquerade subnet.
====

[TIP]
====
You can use the Red Hat OpenShift Network Calculator to decide your networking needs before setting CIDR range during cluster creation.

You must have a Red Hat account to use the calculator.
====

The following subnet types are mandatory for a cluster that uses OVN-Kubernetes:

* Join: Uses a join switch to connect gateway routers to distributed routers. A join switch reduces the number of IP addresses for a distributed router. For a cluster that uses the OVN-Kubernetes plugin, an IP address from a dedicated subnet is assigned to any logical port that attaches to the join switch.
* Masquerade: Prevents collisions for identical source and destination IP addresses that are sent from a node as hairpin traffic to the same node after a load balancer makes a routing decision.
* Transit: A transit switch is a type of distributed switch that spans across all nodes in the cluster. A transit switch routes traffic between different zones. For a cluster that uses the OVN-Kubernetes plugin, an IP address from a dedicated subnet is assigned to any logical port that attaches to the transit switch.

[NOTE]
====
You can change the join, masquerade, and transit CIDR ranges for your cluster as a postinstallation task.
====

When specifying subnet CIDR ranges, ensure that the subnet CIDR range is within the defined Machine CIDR. You must verify that the subnet CIDR ranges allow for enough IP addresses for all intended workloads depending on which platform the cluster is hosted.

OVN-Kubernetes, the default network provider in OpenShift Container Platform 4.14 and later versions, internally uses the following IP address subnet ranges:

* `V4JoinSubnet`: `100.64.0.0/16`
* `V6JoinSubnet`: `fd98::/64`
* `V4TransitSwitchSubnet`: `100.88.0.0/16`
* `V6TransitSwitchSubnet`: `fd97::/64`
* `defaultV4MasqueradeSubnet`: `169.254.0.0/17`
* `defaultV6MasqueradeSubnet`: `fd69::/112`

[IMPORTANT]
====
The earlier list includes join, transit, and masquerade IPv4 and IPv6 address subnets. If your cluster uses OVN-Kubernetes, do not include any of these IP address subnet ranges in any other CIDR definitions in your cluster or infrastructure.
====

[role="_additional-resources"]
.Additional resources

* Configuring OVN-Kubernetes internal IP address subnets

// Module included in the following assemblies:
//
// * /networking/networking_overview/cidr-range-definitions.adoc

[id="machine-cidr-description_{context}"]
= Machine CIDR

[role="_abstract"]
In the Machine classless inter-domain routing (CIDR) field, you must specify the IP address range for machines or cluster nodes.

[NOTE]
====
You cannot change Machine CIDR ranges after you create your cluster.
====

This range must encompass all CIDR address ranges for your virtual private cloud (VPC) subnets. Subnets must be contiguous. A minimum range of 128 IP addresses, using the subnet prefix `/25`, is supported for single availability zone deployments. A minimum address range of 256 addresses, using the subnet prefix `/24`, is supported for deployments that use multiple availability zones.

The default is `10.0.0.0/16`. This range must not conflict with any connected networks.

[NOTE]
====
When using OpenShift Container Platform, the static IP address `172.20.0.1` is reserved for the internal Kubernetes API address. The machine, pod, and service CIDR ranges must not conflict with this IP address.
====

[role="_additional-resources"]
.Additional resources

* Cluster Network Operator configuration

// Module included in the following assemblies:
//
// * /networking/networking_overview/cidr-range-definitions.adoc

[id="service-cidr-description_{context}"]
= Service classless inter-domain routing (CIDR)

[role="_abstract"]
In the Service CIDR field, you must specify the IP address range for services.

Red{nbsp}Hat recommends, but this task is not mandatory, that the address block is the same between clusters. This does not create IP address conflicts.

The range must be large enough to accommodate your workload. The address block must not overlap with any external service accessed from within the cluster. The default is `172.30.0.0/16`.

// Module included in the following assemblies:
//
// * /networking/networking_overview/cidr-range-definitions.adoc

[id="pod-cidr-description_{context}"]
= Pod classless inter-domain routing (CIDR)

[role="_abstract"]
In the pod CIDR field, you must specify the IP address range for pods.

The pod CIDR is the same as the `clusterNetwork` CIDR and the cluster CIDR.
Red{nbsp}Hat recommends, but this task is not mandatory, that the address block is the same between clusters. This does not create IP address conflicts.
The range must be large enough to accommodate your workload. The address block must not overlap with any external service accessed from within the cluster. The default is `10.128.0.0/14`.
You can expand the range after cluster installation.

[role="_additional-resources"]
.Additional resources
* Cluster Network Operator configuration
* Configuring the cluster network range

// Module included in the following assemblies:
//
// * /networking/networking_overview/cidr-range-definitions.adoc

[id="host-prefix-description_{context}"]
= Host prefix

[role="_abstract"]
In the `hostPrefix` parameter, you must specify the subnet prefix length assigned to pods scheduled to individual machines. The host prefix determines the pod IP address pool for each machine.

For example, if you set the `hostPrefix` parameter to `/23`, each machine is assigned a `/23` subnet from the pod CIDR address range. The default is `/23`, allowing 512 cluster nodes and 512 pods per node. Note that where 512 cluster nodes and 512 pods are beyond the maximum supported.

For example, if the host prefix is set to `/23`, each machine is assigned a `/23` subnet from the pod CIDR address range. The default is `/23`, allowing 510 cluster nodes and 510 pod IP addresses per node.

Consider another example where you set the `clusterNetwork.cidr` parameter to `10.128.0.0/16`, you define the complete address space for the cluster. This assigns a pool of 65,536 IP addresses to your cluster. If you then set the `hostPrefix` parameter to `/23`, you define a subnet slice to each node in the cluster, where the `/23` slice becomes a subnet of the `/16` subnet network. This assigns 512 IP addresses to each node, where 2 IP addresses get reserved for networking and broadcasting purposes. The following example calculation uses these IP address figures to determine the maximum number of nodes that you can create for your cluster:

[source,text]
----
65536 / 512 = 128
----

You can use the Red Hat OpenShift Network Calculator to calculate the maximum number of nodes for your cluster.

// CIDR ranges for HCP
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
