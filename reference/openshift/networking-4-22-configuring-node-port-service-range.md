---
title: "Configuring the node port service range"
type: reference
domain: openshift
slug: networking-4-22-configuring-node-port-service-range
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-node-port-service-range
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring the node port service range

[id="configuring-node-port-service-range"]
= Configuring the node port service range

[role="_abstract"]
To meet your cluster node port requirements in OpenShift Container Platform, you can configure the node port service range during installation or expand it after installation. You can expand the default range of `30000-32768` on either side while preserving this default range within your new configuration.

[IMPORTANT]
====
Red{nbsp}Hat has not performed testing outside the default port range of `30000-32768`. For ranges outside the default port range, ensure that you test to verify the expanding node port range does not impact your cluster. In particular, ensure that there is:

- No overlap with any ports already in use by host processes
- No overlap with any ports already in use by pods that are configured with host networking

If you expanded the range and a port allocation issue occurs, create a new cluster and set the required range for it.

If you expand the node port range and {oc-first} stops working because of a port conflict with the OpenShift Container Platform API server, you must create a new cluster.
====

// Expanding the node port range
// Module included in the following assemblies:
//
// * networking/configuring-node-port-service-range.adoc

[id="nw-nodeport-service-range-edit_{context}"]
= Expanding the node port range

[role="_abstract"]
To expand the node port range for your OpenShift Container Platform cluster after installation, you can use the `oc patch` command to update the `serviceNodePortRange` parameter. You can expand the range on either side, but you cannot shrink it after installation.

[IMPORTANT]
====
Red{nbsp}Hat has not performed testing outside the default port range of `30000-32768`. For ranges outside the default port range, ensure that you test to verify that expanding your node port range does not impact your cluster. If you expanded the range and a port allocation issue occurs, create a new cluster and set the required range for it.
====

[IMPORTANT]
====
When expanding the `serviceNodePortRange` parameter, ensure the value you set for the parameter does not overlap with the ephemeral port range, `net.ipv4.ip_local_port_range`, of the kernel.

OVN-Kubernetes uses this ephemeral range for source network address translation (SNAT) source port selection on outbound pod traffic. When a SNAT source port coincides with a node port number, return traffic can be misrouted, causing intermittent outbound TCP connection timeouts.

For more information, see "Safe and unsafe sysctls" in the _Additional resources_ section.
====

.Prerequisites

* Installed the {oc-first}.
* Logged in to the cluster as a user with `cluster-admin` privileges.
* You ensured that your cluster infrastructure allows access to the ports that exist in the extended range. For example, if you expand the node port range to `30000-32900`, your firewall or packet filtering configuration must allow the inclusive port range of `30000-32900`.

.Procedure

* To expand the range for the `serviceNodePortRange` parameter in the `network.config.openshift.io` object that your cluster uses to manage traffic for pods, enter the following command:
+
[source,terminal]
----
$ oc patch network.config.openshift.io cluster --type=merge -p \
  '{
    "spec":
      { "serviceNodePortRange": "<port_range>" }
  }'
----
+
--
where:

`<port_range>`:: Specifies the expanded range, such as `30000-32900`.
--
+
[TIP]
====
You can also apply the following YAML to update the node port range:

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  serviceNodePortRange: "<port_range>"
# ...
----
====
+
.Example output
[source,terminal]
----
network.config.openshift.io/cluster patched
----

.Verification

* To confirm that the updated configuration is active, enter the following command. The update can take several minutes to apply.
+
[source,terminal]
----
$ oc get configmaps -n openshift-kube-apiserver config \
  -o jsonpath="{.data['config\.yaml']}" | \
  grep -Eo '"service-node-port-range":["[[:digit:]]+-[[:digit:]]+"]'
----
+
.Example output
[source,terminal]
----
"service-node-port-range":["30000-32900"]
----

[role="_additional-resources"]
[id="configuring-node-port-service-range-additional-resources"]
== Additional resources

* Configuring ingress cluster traffic using a NodePort

* Network: config.openshift.io v1

* Service: core v1

* Safe and unsafe sysctls
