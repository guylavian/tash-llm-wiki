---
title: "Troubleshooting node network configuration"
type: reference
domain: openshift
slug: networking-4-22-k8s-nmstate-troubleshooting-node-network
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/k8s-nmstate-troubleshooting-node-network
version: 4.22
family: networking
documentKind: "Documentation"
---

# Troubleshooting node network configuration

[id="k8s-nmstate-troubleshooting-node-network"]
= Troubleshooting node network configuration

[role="_abstract"]
If the node network configuration encounters an issue, the policy is automatically rolled back and the enactments report failure. This includes issues such as:

* The configuration fails to be applied on the host.
* The host loses connection to the default gateway.
* The host loses connection to the API server.

// Troubleshooting an incorrect node network configuration policy configuration
// Module included in the following assemblies:
//
// * networking/k8s_nmstate/k8s-nmstate-troubleshooting-node-network.adoc

[id="virt-troubleshooting-incorrect-policy-config_{context}"]
= Troubleshooting an incorrect node network configuration policy configuration

[role="_abstract"]
You can apply changes to the node network configuration across your entire cluster by applying a node network configuration policy. If you applied an incorrect configuration, you can use the following example to troubleshoot and correct the failed node network policy.

The example attempts to apply a Linux bridge policy to a cluster that has three control plane nodes and three compute nodes. The policy is not applied because the policy references the wrong interface.

To find an error, you need to investigate the available NMState resources. You can then update the policy with the correct configuration.

.Prerequisites

* You installed the {oc-first}.
* You ensured that an `ens01` interface does not exist on your Linux system.

.Procedure

. Create a policy on your cluster. The following example creates a simple bridge, `br1` that has `ens01` as its member:
+
[source,yaml]
----
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: ens01-bridge-testfail
spec:
  desiredState:
    interfaces:
      - name: br1
        description: Linux bridge with the wrong port
        type: linux-bridge
        state: up
        ipv4:
          dhcp: true
          enabled: true
        bridge:
          options:
            stp:
              enabled: false
          port:
            - name: ens01
# ...
----

. Apply the policy to your network interface:
+
[source,terminal]
----
$ oc apply -f ens01-bridge-testfail.yaml
----
+
Example output:
+
[source,terminal]
----
nodenetworkconfigurationpolicy.nmstate.io/ens01-bridge-testfail created
----

. Verify the status of the policy by running the following command:
+
[source,terminal]
----
$ oc get nncp
----
+
The output shows that the policy failed:
+
[source,terminal]
----
NAME                    STATUS
ens01-bridge-testfail   FailedToConfigure
----
+
The policy status alone does not indicate if it failed on all nodes or a subset of nodes.

. List the node network configuration enactments to see if the policy was successful on any of the nodes. If the policy failed for only a subset of nodes, the output suggests that the problem is with a specific node configuration. If the policy failed on all nodes, the output suggests that the problem is with the policy.
+
[source,terminal]
----
$ oc get nnce
----
+
The output shows that the policy failed on all nodes:
+
[source,terminal]
----
NAME                                         STATUS
control-plane-1.ens01-bridge-testfail        FailedToConfigure
control-plane-2.ens01-bridge-testfail        FailedToConfigure
control-plane-3.ens01-bridge-testfail        FailedToConfigure
compute-1.ens01-bridge-testfail              FailedToConfigure
compute-2.ens01-bridge-testfail              FailedToConfigure
compute-3.ens01-bridge-testfail              FailedToConfigure
----

. View one of the failed enactments. The following command uses the output tool `jsonpath` to filter the output:
+
[source,terminal]
----
$ oc get nnce compute-1.ens01-bridge-testfail -o jsonpath='{.status.conditions[?(@.type=="Failing")].message}'
----
+
Example output:
+
[source,terminal]
----
[2024-10-10T08:40:46Z INFO  nmstatectl] Nmstate version: 2.2.37
NmstateError: InvalidArgument: Controller interface br1 is holding unknown port ens01
----
+
The previous example shows the output from an `InvalidArgument` error that indicates that the `ens01` is an unknown port. For this example, you might need to change the port configuration in the policy configuration file.

. To ensure that the policy is configured properly, view the network configuration for one or all of the nodes by requesting the `NodeNetworkState` object. The following command returns the network configuration for the `control-plane-1` node:
+
----
$ oc get nns control-plane-1 -o yaml
----
+
The output shows that the interface name on the nodes is `ens1` but the failed policy incorrectly uses `ens01`:
+
[source,yaml]
----
   - ipv4:
# ...
      name: ens1
      state: up
      type: ethernet
----

. Correct the error by editing the existing policy:
+
[source,terminal]
----
$ oc edit nncp ens01-bridge-testfail
----
+
[source,yaml]
----
# ...
          port:
            - name: ens1
----
+
Save the policy to apply the correction.

. Check the status of the policy to ensure it updated successfully:
+
[source,terminal]
----
$ oc get nncp
----
+
Example output:
+
[source,terminal]
----
NAME                    STATUS
ens01-bridge-testfail   SuccessfullyConfigured
----
+
The updated policy is successfully configured on all nodes in the cluster.

// Troubleshooting DNS connectivity issues in a disconnected environment
// Module included in the following assemblies:
//
// * networking/k8s_nmstate/k8s-nmstate-troubleshooting-node-network.adoc

[id="troubleshooting-dns-disconnected-env_{context}"]
= Troubleshooting DNS connectivity issues in a disconnected environment

[role="_abstract"]
If you experience health check probe issues when configuring `nmstate` in a disconnected environment, you can configure the DNS server to resolve the custom domain name instead of the default `root-servers.net` domain.

[IMPORTANT]
====
Ensure that the DNS server includes a name server (NS) entry for the `root-servers.net` zone. The DNS server does not need to forward a query to an upstream resolver, but the server must return a correct answer for the NS query.
====

// Creating a custom DNS host name to resolve DNS connectivity issues
// Module included in the following assemblies:
//
// * networking/k8s_nmstate/k8s-nmstate-troubleshooting-node-network.adoc

[id="k8s-nmstate-troubleshooting-dns-disconnected-bind9-dns_{context}"]
= Configuring the bind9 DNS named server

[role="_abstract"]
For a cluster configured to query a `bind9` DNS server, you can add the `root-servers.net` zone to a configuration file that contains at least one DNS record. For example you can use the `/var/named/named.localhost` as a zone file that already matches this criteria.

.Procedure

. Add the `root-servers.net` zone at the end of the `/etc/named.conf` configuration file by running the following command:
+
[source,terminal]
----
$ cat >> /etc/named.conf <<EOF
zone "root-servers.net" IN {
    	type master;
    	file "named.localhost";
};
EOF
----

. Restart the `named` service by running the following command:
+
[source,terminal]
----
$ systemctl restart named
----

. Confirm that the `root-servers.net` zone is present by running the following command:
+
[source,terminal]
----
$ journalctl -u named|grep root-servers.net
----
+
.Example output
[source,terminal]
----
Jul 03 15:16:26 rhel-8-10 bash[xxxx]: zone root-servers.net/IN: loaded serial 0
Jul 03 15:16:26 rhel-8-10 named[xxxx]: zone root-servers.net/IN: loaded serial 0
----

. Verify that the DNS server can resolve the NS record for the `root-servers.net` domain by running the following command:
+
[source,terminal]
----
$ host -t NS root-servers.net. 127.0.0.1
----
+
.Example output
[source,terminal]
----
Using domain server:
Name: 127.0.0.1
Address: 127.0.0.53
Aliases:
root-servers.net name server root-servers.net.
----

// Configuring the dnsmasq DNS server
// Module included in the following assemblies:
//
// * networking/k8s_nmstate/k8s-nmstate-troubleshooting-node-network.adoc

[id="troubleshooting-dns-disconnected-env-dnsmasq_{context}"]
= Configuring the dnsmasq DNS server

[role="_abstract"]
If you are using `dnsmasq` as the DNS server, you can delegate resolution of the `root-servers.net` domain to another DNS server, for example, by creating a new configuration file that resolves `root-servers.net` using a DNS server that you specify.

.Procedure

. Create a configuration file that delegates the domain `root-servers.net` to another DNS server by running the following command:
+
[source,terminal]
----
$ echo 'server=/root-servers.net/<DNS_server_IP>'> /etc/dnsmasq.d/delegate-root-servers.net.conf
----

. Restart the `dnsmasq` service by running the following command:
+
[source,terminal]
----
$ systemctl restart dnsmasq
----

. Confirm that the `root-servers.net` domain is delegated to another DNS server by running the following command:
+
[source,terminal]
----
$ journalctl -u dnsmasq|grep root-servers.net
----
+
.Example output
[source,terminal]
----
Jul 03 15:31:25 rhel-8-10 dnsmasq[1342]: using nameserver 192.168.1.1#53 for domain root-servers.net
----

. Verify that the DNS server can resolve the NS record for the `root-servers.net` domain by running the following command:
+
[source,terminal]
----
$ host -t NS root-servers.net. 127.0.0.1
----
+
.Example output
[source,terminal]
----
Using domain server:
Name: 127.0.0.1
Address: 127.0.0.1#53
Aliases:
root-servers.net name server root-servers.net.
----

// Creating a custom DNS host name to resolve DNS connectivity issues
// Module included in the following assemblies:
//
// * networking/k8s_nmstate/k8s-nmstate-troubleshooting-node-network.adoc

[id="k8s-nmstate-troubleshooting-dns-disconnected-env-resolv_{context}"]
= Creating a custom DNS host name to resolve DNS connectivity issues

[role="_abstract"]
In a disconnected environment where the external DNS server cannot be reached, you can resolve Kubernetes NMState Operator health probe issues by specifying a custom DNS host name in the `NMState` custom resource definition (CRD).

.Procedure

. Add the DNS host name configuration to the `NMState` CRD of your cluster:
+
[source,yaml]
----
apiVersion: nmstate.io/v1
kind: NMState
metadata:
  name: nmstate
spec:
  probeConfiguration:
    dns:
      host: redhat.com
# ...
----

. Apply the DNS host name configuration to your cluster network by running the following command. Ensure that you replace `<filename>` with the name of your CRD file.
+
[source,yaml]
----
$ oc apply -f <filename>.yaml
----
