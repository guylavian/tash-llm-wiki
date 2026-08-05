---
title: "Installing a three-node cluster on {gcp-short}"
type: reference
domain: openshift
slug: installing-4-22-installing-gcp-three-node
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-gcp-three-node
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a three-node cluster on {gcp-short}

[id="installing-gcp-three-node"]
= Installing a three-node cluster on {gcp-short}

[role="_abstract"]
In OpenShift Container Platform version , you can install a three-node cluster on {gcp-first}. A three-node cluster consists of three control plane machines, which also act as compute machines. This type of cluster provides a smaller, more resource efficient cluster, for cluster administrators and developers to use for testing, development, and production.

You can install a three-node cluster using either installer-provisioned or user-provisioned infrastructure.

// Module included in the following assemblies:
// * installing/installing_aws/installing-aws-three-node.adoc
// * installing/installing_azure/installing-azure-three-node.adoc
// * installing/installing_gcp/installing-gcp-three-node.adoc
// * installing/installing_vsphere/installing-vsphere-three-node.adoc

[id="installation-three-node-cluster_{context}"]
= Configuring a three-node cluster

[role="_abstract"]
To configure a three-node cluster, set the number of worker nodes to `0` in the `install-config.yaml` file before you deploy the cluster.

Setting the number of worker nodes to `0` ensures that the control plane machines are schedulable. This allows application workloads to be scheduled to run from the control plane nodes.

[NOTE]
====
Because application workloads run from control plane nodes, additional subscriptions are required, as the control plane nodes are considered to be compute nodes.
====

.Prerequisites

* You have an existing `install-config.yaml` file.

.Procedure

. Set the number of compute replicas to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:

* Set the number of compute replicas to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:

+
.Example `install-config.yaml` file for a three-node cluster
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
compute:
- name: worker
  platform: {}
  replicas: 0
# ...
----

. If you are deploying a cluster with user-provisioned infrastructure:
** After you create the Kubernetes manifest files, make sure that the `spec.mastersSchedulable` parameter is set to `true` in `cluster-scheduler-02-config.yml` file. You can locate this file in `<installation_directory>/manifests`.
For more information, see "Creating the Kubernetes manifest and Ignition config files" in "Installing a cluster on user-provisioned infrastructure in AWS by using CloudFormation templates".
For more information, see "Creating the Kubernetes manifest and Ignition config files" in "Installing a cluster on Azure using ARM templates".
For more information, see "Creating the Kubernetes manifest and Ignition config files" in "Installing a cluster on user-provisioned infrastructure in {gcp-short} by using Infrastructure Manager templates".
** Do not create additional worker nodes.

. If you are deploying a cluster with user-provisioned infrastructure:
** Configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. In a three-node cluster, the Ingress Controller pods run on the control plane nodes. For more information, see the "Load balancing requirements for user-provisioned infrastructure".
** After you create the Kubernetes manifest files, make sure that the `spec.mastersSchedulable` parameter is set to `true` in `cluster-scheduler-02-config.yml` file. You can locate this file in `<installation_directory>/manifests`.
For more information, see "Creating the Kubernetes manifest and Ignition config files" in "Installing a cluster on vSphere with user-provisioned infrastructure".
** Do not create additional worker nodes.

+
--
.Example `cluster-scheduler-02-config.yml` file for a three-node cluster
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  creationTimestamp: null
  name: cluster
spec:
  mastersSchedulable: true
  policy:
    name: ""
status: {}
----
--

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Installing a cluster on {gcp-short} with customizations
* Installing a cluster on user-provisioned infrastructure in {gcp-short} by using Infrastructure Manager templates
