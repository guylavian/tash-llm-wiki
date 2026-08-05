---
title: "Configuring the cluster network range"
type: reference
domain: openshift
slug: networking-4-22-configuring-cluster-network-range
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-cluster-network-range
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring the cluster network range

[id="configuring-cluster-network-range"]
= Configuring the cluster network range

[role="_abstract"]
To expand the cluster network range in OpenShift Container Platform to support more nodes and IP addresses, you can modify the cluster network CIDR mask after cluster installation. This procedure requires the OVN-Kubernetes network plugin and provides more IP space for additional nodes.

For example, if you deployed a cluster and specified `10.128.0.0/19` as the cluster network range and a host prefix of `23`, you are limited to 16 nodes. You can expand that to 510 nodes by changing the CIDR mask on a cluster to `/14`.

The following limitations apply when modifying the cluster network IP address range:

- The CIDR mask size specified must always be smaller than the currently configured CIDR mask size, because you can only increase IP space by adding more nodes to an installed cluster
- The host prefix cannot be modified
- Pods that are configured with an overridden default gateway must be recreated after the cluster network expands

[IMPORTANT]
====
You cannot expand the service network CIDR range after installing the cluster, either directly or through the ServiceCIDR API. You must configure the service network CIDR during installation using the `install-config.yaml` file. To avoid service IP address exhaustion, ensure that your initial service network range is large enough to accommodate future growth.
====

// Module included in the following assemblies:
//
// * networking/configuring-cluster-network-range.adoc

[id="nw-cluster-network-range-edit_{context}"]
= Expanding the cluster network IP address range

[role="_abstract"]
To expand the cluster network IP address range in OpenShift Container Platform to support more nodes, you can modify the cluster network CIDR mask using the `oc patch` command.

[NOTE]
====
This change requires rolling out a new Operator configuration across the cluster, and can take up to 30 minutes to take effect.

For clusters configured with cluster proxy, expanding the cluster network range also triggers a MachineConfigPool update that reboots all nodes. Plan this operation during a maintenance window to avoid service disruption.
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the cluster with a user with `cluster-admin` privileges.
* You have ensured that the cluster uses the OVN-Kubernetes network plugin.

.Procedure

. To obtain the cluster network range and host prefix for your cluster, enter the following command:
+
[source,terminal]
----
$ oc get network.operator.openshift.io \
  -o jsonpath="{.items[0].spec.clusterNetwork}"
----
+
.Example output
[source,text]
----
[{"cidr":"10.217.0.0/22","hostPrefix":23}]
----

. To expand the cluster network IP address range, enter the following command. Use the CIDR IP address range and host prefix returned from the output of the previous command.
+
[source,terminal]
----
$ oc patch Network.config.openshift.io cluster --type='merge' --patch \
  '{
    "spec":{
      "clusterNetwork": [ {"cidr":"<network>/<cidr>","hostPrefix":<prefix>} ],
      "networkType": "OVNKubernetes"
    }
  }'
----
+
--
where:

`<network>`:: Specifies the network part of the `cidr` field that you obtained from the previous step. You cannot change this value.
`<cidr>`:: Specifies the network prefix length. For example, `14`. Change this value to a smaller number than the value from the output in the previous step to expand the cluster network range.
`<prefix>`:: Specifies the current host prefix for your cluster. This value must be the same value for the `hostPrefix` field that you obtained from the previous step.
--
+
.Example command
[source,terminal]
----
$ oc patch Network.config.openshift.io cluster --type='merge' --patch \
  '{
    "spec":{
      "clusterNetwork": [ {"cidr":"10.217.0.0/14","hostPrefix": 23} ],
      "networkType": "OVNKubernetes"
    }
  }'
----
+
.Example output
[source,text]
----
network.config.openshift.io/cluster patched
----

. To confirm that the configuration is active, enter the following command. It can take up to 30 minutes for this change to take effect.
+
[source,terminal]
----
$ oc get network.operator.openshift.io \
  -o jsonpath="{.items[0].spec.clusterNetwork}"
----
+
.Example output
[source,text]
----
[{"cidr":"10.217.0.0/14","hostPrefix":23}]
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* OVN-Kubernetes network plugin
* Red Hat OpenShift Network Calculator
* About the OVN-Kubernetes network plugin
