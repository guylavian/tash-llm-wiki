---
title: "Audit logging for network security"
type: reference
domain: openshift
slug: networking-4-22-logging-network-security
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/logging-network-security
version: 4.22
family: networking
documentKind: "Documentation"
---

# Audit logging for network security

[id="logging-network-security"]
= Audit logging for network security

[role="_abstract"]
The OVN-Kubernetes network plugin uses Open Virtual Network (OVN) access control lists (ACLs) to manage `AdminNetworkPolicy`, `BaselineAdminNetworkPolicy`, `NetworkPolicy`, and `EgressFirewall` objects. Audit logging exposes `Allow` and `Deny` ACL events for `NetworkPolicy`, `EgressFirewall` and `BaselineAdminNetworkPolicy` custom resources (CR). Logging also exposes `Allow`, `Deny`, and `Pass` ACL events for `AdminNetworkPolicy` (ANP) CR.

[NOTE]
====
Audit logging is available for only the OVN-Kubernetes network plugin.
====

// Module included in the following assemblies:
//
// * networking/openshift_network_security/logging-network-security.adoc

[id="network-policy-audit-configuration_{context}"]
= Audit configuration

[role="_abstract"]
Audit logging configuration in OpenShift Container Platform is defined in the `policyAuditConfig` section of the cluster `Network` custom resource for OVN-Kubernetes. You can review these default settings to plan log destinations, file size limits, and rate limits before you enable logging.

The following YAML illustrates the default values for the audit logging:

.Audit logging configuration
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      policyAuditConfig:
        destination: "null"
        maxFileSize: 50
        rateLimit: 20
        syslogFacility: local0
----

The following table describes the configuration fields for audit logging.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * networking/cluster-network-operator.adoc
// * networking/network_security/logging-network-security.adoc
// * post_installation_configuration/network-configuration.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc

// Installation assemblies need different details than the CNO operator does

[id="nw-operator-cr_{context}"]
= Cluster Network Operator configuration

[role="_abstract"]
To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`:: IP address pools from which pod IP addresses are allocated.
`serviceNetwork`:: IP address pool for services.
//Installation no longer supports SDN, so excluding it from install docs here. Deleted in 4.17.

`defaultNetwork.type`:: Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

// For the post installation assembly, no further content is provided.
[NOTE]
====
After cluster installation, you can only modify the `clusterNetwork` IP address range. The `serviceNetwork` range cannot be modified post-installation, either directly or by using the `ServiceCIDR` API.
====

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

[id="nw-operator-cr-cno-object_{context}"]
== Cluster Network Operator configuration object

The fields for the Cluster Network Operator (CNO) are described in the following table:

.Cluster Network Operator configuration object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name of the CNO object. This name is always `cluster`.

|`spec.clusterNetwork`
|`array`
|A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:

[source,yaml]
----
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/19
    hostPrefix: 23
  - cidr: fd01::/48
    hostPrefix: 64
----

If you install a cluster on {aws-short} with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.

|`spec.serviceNetwork`
|`array`
|A block of IP addresses for services. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:

[source,yaml]
----
spec:
  serviceNetwork:
  - 172.30.0.0/14
  - fd02::/112
----

If you install a cluster on {aws-short} with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.

This value is ready-only and inherited from the `Network.config.openshift.io` object named `cluster` during cluster installation.
You can customize this field only in the `install-config.yaml` file before you create the manifests. The value is read-only in the manifest file.

|`spec.defaultNetwork`
|`object`
|Configures the network plugin for the cluster network.

|`spec.additionalRoutingCapabilities.providers`
|`array`
|This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is `FRR`.

--
- `FRR`: The FRR routing provider
--

[source,yaml]
----
spec:
  additionalRoutingCapabilities:
    providers:
    - FRR
----

|====

[IMPORTANT]
====
For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes.
====

[id="nw-operator-cr-defaultnetwork_{context}"]
== defaultNetwork object configuration

The values for the `defaultNetwork` object are defined in the following table:

.`defaultNetwork` object
[cols=".^3,.^2,.^5a",options="header"]
|====
|Field|Type|Description

|`type`
|`string`
|`OVNKubernetes`. The {openshift-networking} network plugin is selected during installation. This value cannot be changed after cluster installation.
[NOTE]
====
OpenShift Container Platform uses the OVN-Kubernetes network plugin by default.
====

|`ovnKubernetesConfig`
|`object`
|This object is only valid for the OVN-Kubernetes network plugin.

|====

[id="nw-operator-configuration-parameters-for-ovn-sdn_{context}"]
== Configuration for the OVN-Kubernetes network plugin

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

.`ovnKubernetesConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`mtu`
|`integer`
|
The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.

If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.

If your cluster requires different MTU values for different nodes, you must set this value to `100` less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of `9001`, and some have an MTU of `1500`, you must set this value to `1400`.
The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This value is normally configured automatically.

|`genevePort`
|`integer`
|
The port to use for all Geneve packets. The default value is `6081`. This value cannot be changed after cluster installation.
The UDP port for the Geneve overlay network.

|`ipsecConfig`
|`object`
|
Specify a configuration object for customizing the IPsec configuration.
An object describing the IPsec mode for the cluster.

|`ipv4`
|`object`
|Specifies a configuration object for IPv4 settings.

|`ipv6`
|`object`
|Specifies a configuration object for IPv6 settings.

|`policyAuditConfig`
|`object`
|Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used.

|`routeAdvertisements`
|`string`
a|Specifies whether to advertise cluster network routes. The default value is `Disabled`.
--
- `Enabled`: Import routes to the cluster network and advertise cluster network routes as configured in `RouteAdvertisements` objects.
- `Disabled`: Do not import routes to the cluster network or advertise cluster network routes.
--

|`gatewayConfig`
|`object`
|Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are `Shared` and `Local`. The default value is `Shared`. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. If you are using hardware offloading, Red Hat recommends to use the default `Shared` gateway mode to bypass the host routing plane. In the `Local` setting, it traverses the host network; consequently, it gets applied to the routing table of the host.

[NOTE]
====
While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes.
====

|====

.`ovnKubernetesConfig.ipv4` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalTransitSwitchSubnet`
|string
|
If your existing network infrastructure overlaps with the `100.88.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.

The default value is `100.88.0.0/16`.

|`internalJoinSubnet`
|string
|
If your existing network infrastructure overlaps with the `100.64.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the `clusterNetwork.cidr` value is `10.128.0.0/14` and the `clusterNetwork.hostPrefix` value is `/23`, then the maximum number of nodes is `2^(23-14)=512`.

The default value is `100.64.0.0/16`.

|====

.`ovnKubernetesConfig.ipv6` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalTransitSwitchSubnet`
|string
|
If your existing network infrastructure overlaps with the `fd97::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.

The default value is `fd97::/64`.

|`internalJoinSubnet`
|string
|
If your existing network infrastructure overlaps with the `fd98::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.

The default value is `fd98::/64`.

|====

// tag::policy-audit[]
.`policyAuditConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`rateLimit`
|integer
|The maximum number of messages to generate every second per node. The default value is `20` messages per second.

|`maxFileSize`
|integer
|The maximum size for the audit log in bytes. The default value is `50000000` or 50 MB.

|`maxLogFiles`
|integer
|The maximum number of log files that are retained.

|`destination`
|string
|
One of the following additional audit log targets:

`libc`:: The libc `syslog()` function of the journald process on the host.
`udp:<host>:<port>`:: A syslog server. Replace `<host>:<port>` with the host and port of the syslog server.
`unix:<file>`:: A Unix Domain Socket file specified by `<file>`.
`null`:: Do not send the audit logs to any additional target.

|`syslogFacility`
|string
|The syslog facility, such as `kern`, as defined by RFC5424. The default value is `local0`.

|====
// end::policy-audit[]

[id="gatewayConfig-object_{context}"]
.`gatewayConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`routingViaHost`
|`boolean`
|Set this field to `true` to send egress traffic from pods to the host networking stack.
For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack.
By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table.
The default value is `false`.

This field has an interaction with the Open vSwitch hardware offloading feature.
If you set this field to `true`, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack.

|`ipForwarding`
|`object`
|You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the `ipForwarding` specification in the `Network` resource. Specify `Restricted` to only allow IP forwarding for Kubernetes related traffic. Specify `Global` to allow forwarding of all IP traffic. For new installations, the default is `Restricted`. For updates to OpenShift Container Platform 4.14 or later, the default is `Global`.
[NOTE]
====
The default value of `Restricted` sets the IP forwarding to drop.
====

|`ipv4`
|`object`
|Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses.

|`ipv6`
|`object`
|Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses.

|====

[id="gatewayconfig-ipv4-object_{context}"]
.`gatewayConfig.ipv4` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalMasqueradeSubnet`
|`string`
|
The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `169.254.169.0/29`.
[IMPORTANT]
====
For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.
====

|====

[id="gatewayconfig-ipv6-object_{context}"]
.`gatewayConfig.ipv6` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalMasqueradeSubnet`
|`string`
|
The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `fd69::/125`.
[IMPORTANT]
====
For OpenShift Container Platform 4.17 and later versions, clusters use `fd69::/112` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.
====

|====

[id="nw-operator-cr-ipsec_{context}"]
.`ipsecConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`mode`
|`string`
a|Specifies the behavior of the IPsec implementation. Must be one of the following values:

--
- `Disabled`: IPsec is not enabled on cluster nodes.
- `External`: IPsec is enabled for network traffic with external hosts.
- `Full`: IPsec is enabled for pod traffic and network traffic with external hosts.
--

|====

[NOTE]
====
You can only change the configuration for your cluster network plugin during cluster installation, except for the `gatewayConfig` field that can be changed at runtime as a postinstallation activity.
====

.Example OVN-Kubernetes configuration with IPSec enabled
[source,yaml]
----
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
----

[id="nw-operator-example-cr_{context}"]
== Cluster Network Operator example configuration

A complete CNO configuration is specified in the following example:

.Example Cluster Network Operator object
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
----

// Audit logging
// Module included in the following assemblies:
//
// * networking/network_security/logging-network-security.adoc

[id="nw-networkpolicy-audit-concept_{context}"]
= Audit logging

[role="_abstract"]
You can enable network policy audit logging in OpenShift Container Platform by annotating namespaces with the `k8s.ovn.org/acl-logging` key and configuring log destinations for the OVN-Kubernetes plugin.

You can also configure the destination for audit logs, such as a syslog server or a UNIX domain socket. Regardless of any additional configuration, an audit log is always saved to `/var/log/ovn/acl-audit-log.log` on each OVN-Kubernetes pod in the cluster.

[NOTE]
====
A network policy does not support setting the `Pass` action set as a rule.
====

The ACL-logging implementation logs access control list (ACL) events for a network. You can view these logs to analyze any potential security issues.

.Example namespace annotation
[source,yaml]
----
kind: Namespace
apiVersion: v1
metadata:
  name: example1
  annotations:
    k8s.ovn.org/acl-logging: |-
      {
        "deny": "info",
        "allow": "info"
      }
----

To view the default ACL logging configuration values, see the `policyAuditConfig` object in the `cluster-network-03-config.yml` file. If required, you can change the ACL logging configuration values for log file parameters in this file.

The logging message format is compatible with syslog as defined by RFC5424. The syslog facility is configurable and defaults to `local0`. The following example shows key parameters and their values outputted in a log message:

.Example logging message that outputs parameters and their values
[source,terminal]
----
<timestamp>|<message_serial>|acl_log(ovn_pinctrl0)|<severity>|name="<acl_name>", verdict="<verdict>", severity="<severity>", direction="<direction>": <flow>
----

Where:

* `<timestamp>` states the time and date for the creation of a log message.
* `<message_serial>` lists the serial number for a log message.
* `acl_log(ovn_pinctrl0)` is a literal string that prints the location of the log message in the OVN-Kubernetes plugin.
* `<severity>` sets the severity level for a log message. If you enable audit logging that supports `allow` and `deny` tasks then two severity levels show in the log message output.
* `<name>` states the name of the ACL-logging implementation in the OVN Network Bridging Database (`nbdb`) that was created by the network policy.
* `<verdict>` can be either `allow` or `drop`.
* `<direction>` can be either `to-lport` or `from-lport` to indicate that the policy was applied to traffic going to or away from a pod.
* `<flow>` shows packet information in a format equivalent to the `OpenFlow` protocol. This parameter comprises Open vSwitch (OVS) fields.

The following example shows OVS fields that the `flow` parameter uses to extract packet information from system memory:

.Example of OVS fields used by the `flow` parameter to extract packet information
[source,terminal]
----
<proto>,vlan_tci=0x0000,dl_src=<src_mac>,dl_dst=<source_mac>,nw_src=<source_ip>,nw_dst=<target_ip>,nw_tos=<tos_dscp>,nw_ecn=<tos_ecn>,nw_ttl=<ip_ttl>,nw_frag=<fragment>,tp_src=<tcp_src_port>,tp_dst=<tcp_dst_port>,tcp_flags=<tcp_flags>
----

Where:

* `<proto>` states the protocol. Valid values are `tcp` and `udp`.
* `vlan_tci=0x0000` states the VLAN header as `0` because a VLAN ID is not set for internal pod network traffic.
* `<src_mac>` specifies the source for the Media Access Control (MAC) address.
* `<source_mac>` specifies the destination for the MAC address.
* `<source_ip>` lists the source IP address
* `<target_ip>` lists the target IP address.
* `<tos_dscp>` states Differentiated Services Code Point (DSCP) values to classify and prioritize certain network traffic over other traffic.
* `<tos_ecn>` states Explicit Congestion Notification (ECN) values that indicate any congested traffic in your network.
* `<ip_ttl>` states the Time To Live (TTP) information for an packet.
* `<fragment>` specifies what type of IP fragments or IP non-fragments to match.
* `<tcp_src_port>` shows the source for the port for TCP and UDP protocols.
* `<tcp_dst_port>` lists the destination port for TCP and UDP protocols.
* `<tcp_flags>` supports numerous flags such as `SYN`, `ACK`, `PSH` and so on. If you need to set multiple values then each value is separated by a vertical bar (`|`). The UDP protocol does not support this parameter.

[NOTE]
====
For more information about the previous field descriptions, go to the OVS manual page for `ovs-fields`.
====

.Example ACL deny log entry for a network policy
[source,text]
----
2023-11-02T16:28:54.139Z|00004|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
2023-11-02T16:28:55.187Z|00005|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
2023-11-02T16:28:57.235Z|00006|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
----

The following table describes namespace annotation values:

.Audit logging namespace annotation for `k8s.ovn.org/acl-logging`
[cols=".^4,.^6a",options="header"]
|====
|Field|Description

|`deny`
|Blocks namespace access to any traffic that matches an ACL rule with the `deny` action. The field supports `alert`, `warning`, `notice`, `info`, or `debug` values.

|`allow`
|Permits namespace access to any traffic that matches an ACL rule with the `allow` action. The field supports `alert`, `warning`, `notice`, `info`, or `debug` values.

|`pass`
|A `pass` action applies to an admin network policy's ACL rule. A `pass` action allows either the network policy in the namespace or the baseline admin network policy rule to evaluate all incoming and outgoing traffic. A network policy does not support a `pass` action.
|====

[role="_additional-resources"]
.Additional resources

* Understanding network policy APIs

// Module included in the following assemblies:
//
// * networking/openshift_network_security/AdminNetworkPolicy/logging-anp-policy.adoc

[id="nw-anp-audit-logging_{context}"]
= AdminNetworkPolicy audit logging

[role="_abstract"]
You can enable audit logging for individual `AdminNetworkPolicy` custom resources in OpenShift Container Platform by annotating each policy with the `k8s.ovn.org/acl-logging` key. Use the resulting logs to verify how `Allow`, `Deny`, and `Pass` rules affect traffic between namespaces.

.Example of annotation for `AdminNetworkPolicy` CR
====
[source,yaml]
----
apiVersion: policy.networking.k8s.io/v1alpha1
kind: AdminNetworkPolicy
metadata:
  annotations:
    k8s.ovn.org/acl-logging: '{ "deny": "alert", "allow": "alert", "pass" : "warning" }'
  name: anp-tenant-log
spec:
  priority: 5
  subject:
    namespaces:
      matchLabels:
        tenant: backend-storage # Selects all pods owned by storage tenant.
  ingress:
    - name: "allow-all-ingress-product-development-and-customer" # Product development and customer tenant ingress to backend storage.
      action: "Allow"
      from:
      - pods:
          namespaceSelector:
            matchExpressions:
            - key: tenant
              operator: In
              values:
              - product-development
              - customer
          podSelector: {}
    - name: "pass-all-ingress-product-security"
      action: "Pass"
      from:
      - namespaces:
          matchLabels:
              tenant: product-security
    - name: "deny-all-ingress" # Ingress to backend from all other pods in the cluster.
      action: "Deny"
      from:
      - namespaces: {}
  egress:
    - name: "allow-all-egress-product-development"
      action: "Allow"
      to:
      - pods:
          namespaceSelector:
            matchLabels:
              tenant: product-development
          podSelector: {}
    - name: "pass-egress-product-security"
      action: "Pass"
      to:
      - namespaces:
           matchLabels:
             tenant: product-security
    - name: "deny-all-egress" # Egress from backend denied to all other pods.
      action: "Deny"
      to:
      - namespaces: {}
----
====

Logs are generated whenever a specific OVN ACL is hit and meets the action criteria set in your logging annotation. For example, an event in which any of the namespaces with the label `tenant: product-development` accesses the namespaces with the label `tenant: backend-storage`, a log is generated.

[NOTE]
====
ACL logging is limited to 60 characters. If your ANP `name` field is long, the rest of the log will be truncated.
====

The following is a direction index for the examples log entries that follow:

[cols=".^4,.^6a",options="header"]
|====
|Direction|Rule

|Ingress
|
Rule0:: Allow from tenant `product-development` and `customer` to tenant `backend-storage`; Ingress0: `Allow`
Rule1:: Pass from `product-security`to tenant `backend-storage`; Ingress1: `Pass`
Rule2::	Deny ingress from all pods; Ingress2: `Deny`

|Egress
|
Rule0:: Allow to `product-development`; Egress0: `Allow`
Rule1:: Pass to `product-security`; Egress1: `Pass`
Rule2:: Deny egress to all other pods; Egress2: `Deny`

|====

.Example ACL log entry for `Allow` action of the `AdminNetworkPolicy` named `anp-tenant-log` with `Ingress:0` and `Egress:0`

[%collapsible]
====
[source,text]
----
2024-06-10T16:27:45.194Z|00052|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:1a,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.26,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=57814,tp_dst=8080,tcp_flags=syn
2024-06-10T16:28:23.130Z|00059|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:18,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.24,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=38620,tp_dst=8080,tcp_flags=ack
2024-06-10T16:28:38.293Z|00069|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Egress:0", verdict=allow, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:19,dl_dst=0a:58:0a:80:02:1a,nw_src=10.128.2.25,nw_dst=10.128.2.26,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=47566,tp_dst=8080,tcp_flags=fin|ack=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=55704,tp_dst=8080,tcp_flags=ack
----
====

.Example ACL log entry for `Pass` action of the `AdminNetworkPolicy` named `anp-tenant-log` with `Ingress:1` and `Egress:1`

[%collapsible]
====
[source,text]
----
2024-06-10T16:33:12.019Z|00075|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:1", verdict=pass, severity=warning, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:1b,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.27,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=37394,tp_dst=8080,tcp_flags=ack
2024-06-10T16:35:04.209Z|00081|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Egress:1", verdict=pass, severity=warning, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:19,dl_dst=0a:58:0a:80:02:1b,nw_src=10.128.2.25,nw_dst=10.128.2.27,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=34018,tp_dst=8080,tcp_flags=ack
----
====

.Example ACL log entry for `Deny` action of the `AdminNetworkPolicy` named `anp-tenant-log` with `Egress:2` and `Ingress2`

[%collapsible]
====
[source,text]
----
2024-06-10T16:43:05.287Z|00087|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Egress:2", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:19,dl_dst=0a:58:0a:80:02:18,nw_src=10.128.2.25,nw_dst=10.128.2.24,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=51598,tp_dst=8080,tcp_flags=syn
2024-06-10T16:44:43.591Z|00090|acl_log(ovn_pinctrl0)|INFO|name="ANP:anp-tenant-log:Ingress:2", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:80:02:1c,dl_dst=0a:58:0a:80:02:19,nw_src=10.128.2.28,nw_dst=10.128.2.25,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=33774,tp_dst=8080,tcp_flags=syn
----
====

The following table describes ANP annotation:

.Audit logging AdminNetworkPolicy annotation
[cols=".^4,.^6a",options="header"]
|====
|Annotation|Value

|`k8s.ovn.org/acl-logging`
|
You must specify at least one of `Allow`, `Deny`, or `Pass` to enable audit logging for a namespace.

`Deny`:: Optional: Specify `alert`, `warning`, `notice`, `info`, or `debug`.
`Allow`:: Optional: Specify `alert`, `warning`, `notice`, `info`, or `debug`.
`Pass`:: Optional: Specify `alert`, `warning`, `notice`, `info`, or `debug`.
|====

// Module included in the following assemblies:
//
// * networking/openshift_network_security/AdminNetworkPolicy/logging-anp-policy.adoc

[id="nw-banp-audit-logging-concept_{context}"]
= BaselineAdminNetworkPolicy audit logging

[role="_abstract"]
You can enable audit logging for `BaselineAdminNetworkPolicy` custom resources in OpenShift Container Platform by annotating each policy with the `k8s.ovn.org/acl-logging` key.

.Example of annotation for `BaselineAdminNetworkPolicy` CR
[%collapsible]
====
[source,yaml]
----
apiVersion: policy.networking.k8s.io/v1alpha1
kind: BaselineAdminNetworkPolicy
metadata:
  annotations:
    k8s.ovn.org/acl-logging: '{ "deny": "alert", "allow": "alert"}'
  name: default
spec:
  subject:
    namespaces:
      matchLabels:
          tenant: workloads # Selects all workload pods in the cluster.
  ingress:
  - name: "default-allow-dns" # This rule allows ingress from dns tenant to all workloads.
    action: "Allow"
    from:
    - namespaces:
          matchLabels:
            tenant: dns
  - name: "default-deny-dns" # This rule denies all ingress from all pods to workloads.
    action: "Deny"
    from:
    - namespaces: {} # Use the empty selector with caution because it also selects OpenShift namespaces as well.
  egress:
  - name: "default-deny-dns" # This rule denies all egress from workloads. It will be applied when no ANP or network policy matches.
    action: "Deny"
    to:
    - namespaces: {} # Use the empty selector with caution because it also selects OpenShift namespaces as well.
----
====

In the example, an event in which any of the namespaces with the label `tenant: dns` accesses the namespaces with the label `tenant: workloads`, a log is generated.

The following is a direction index for the examples log entries that follow:

[cols=".^4,.^6a",options="header"]
|====
|Direction|Rule

|Ingress
|Rule0:: Allow from tenant `dns` to tenant `workloads`; Ingress0: `Allow`
Rule1:: Deny to tenant `workloads` from all pods; Ingress1: `Deny`

|Egress
|Rule0:: Deny to all pods; Egress0: `Deny`

|====

.Example ACL allow log entry for `Allow` action of `default` BANP with `Ingress:0`

[%collapsible]
====
[source,text]
----
2024-06-10T18:11:58.263Z|00022|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=syn
2024-06-10T18:11:58.264Z|00023|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=psh|ack
2024-06-10T18:11:58.264Z|00024|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=ack
2024-06-10T18:11:58.264Z|00025|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=ack
2024-06-10T18:11:58.264Z|00026|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=fin|ack
2024-06-10T18:11:58.264Z|00027|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:0", verdict=allow, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:57,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.87,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=60510,tp_dst=8080,tcp_flags=ack
----
====

.Example ACL allow log entry for `Allow` action of `default` BANP with `Egress:0` and `Ingress:1`

[%collapsible]
====
[source,text]
----
2024-06-10T18:09:57.774Z|00016|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Egress:0", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:56,dl_dst=0a:58:0a:82:02:57,nw_src=10.130.2.86,nw_dst=10.130.2.87,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=45614,tp_dst=8080,tcp_flags=syn
2024-06-10T18:09:58.809Z|00017|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Egress:0", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:56,dl_dst=0a:58:0a:82:02:57,nw_src=10.130.2.86,nw_dst=10.130.2.87,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=45614,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:00.857Z|00018|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Egress:0", verdict=drop, severity=alert, direction=from-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:56,dl_dst=0a:58:0a:82:02:57,nw_src=10.130.2.86,nw_dst=10.130.2.87,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=45614,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:25.414Z|00019|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:1", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:58,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.88,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=40630,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:26.457Z|00020|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:1", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:58,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.88,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=40630,tp_dst=8080,tcp_flags=syn
2024-06-10T18:10:28.505Z|00021|acl_log(ovn_pinctrl0)|INFO|name="BANP:default:Ingress:1", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:82:02:58,dl_dst=0a:58:0a:82:02:56,nw_src=10.130.2.88,nw_dst=10.130.2.86,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,tp_src=40630,tp_dst=8080,tcp_flags=syn
----
====

The following table describes BANP annotation:

.Audit logging BaselineAdminNetworkPolicy annotation
[cols=".^4,.^6a",options="header"]
|====
|Annotation|Value

|`k8s.ovn.org/acl-logging`
|
You must specify at least one of `Allow` or `Deny` to enable audit logging for a namespace.

`Deny`:: Optional: Specify `alert`, `warning`, `notice`, `info`, or `debug`.
`Allow`:: Optional: Specify `alert`, `warning`, `notice`, `info`, or `debug`.
|====

// Module included in the following assemblies:
//
// * networking/network_security/logging-network-security.adoc

[id="nw-networkpolicy-audit-configure_{context}"]
= Configuring egress firewall and network policy auditing for a cluster

[role="_abstract"]
To customize egress firewall and network policy audit logging in OpenShift Container Platform, you can configure the `policyAuditConfig` section in the cluster `Network` custom resource. Adjust log destination, file size, and rate limits to control how ACL events are recorded.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in to the cluster with a user with `cluster-admin` privileges.

.Procedure

* To customize the audit logging configuration, enter the following command:
+
[source,terminal]
----
$ oc edit network.operator.openshift.io/cluster
----
+
[TIP]
====
You can also customize and apply the following YAML to configure audit logging:

[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      policyAuditConfig:
        destination: "null"
        maxFileSize: 50
        rateLimit: 20
        syslogFacility: local0
----
====

.Verification

. To create a namespace with network policies complete the following steps:
.. Create a namespace for verification:
+
[source,terminal]
----
$ cat <<EOF| oc create -f -
kind: Namespace
apiVersion: v1
metadata:
  name: verify-audit-logging
  annotations:
    k8s.ovn.org/acl-logging: '{ "deny": "alert", "allow": "alert" }'
EOF
----
+
Successful output lists the namespace with the network policy and the `created` status.

.. Create network policies for the namespace:
+
[source,terminal]
----
$ cat <<EOF| oc create -n verify-audit-logging -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector:
    matchLabels:
  policyTypes:
  - Ingress
  - Egress
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-same-namespace
  namespace: verify-audit-logging
spec:
  podSelector: {}
  policyTypes:
   - Ingress
   - Egress
  ingress:
    - from:
        - podSelector: {}
  egress:
    - to:
       - namespaceSelector:
          matchLabels:
            kubernetes.io/metadata.name: verify-audit-logging
EOF
----
+
.Example output
[source,text]
----
networkpolicy.networking.k8s.io/deny-all created
networkpolicy.networking.k8s.io/allow-from-same-namespace created
----

. Create a pod for source traffic in the `default` namespace:
+
[source,terminal]
----
$ cat <<EOF| oc create -n default -f -
apiVersion: v1
kind: Pod
metadata:
  name: client
spec:
  containers:
    - name: client
      image: registry.access.redhat.com/rhel7/rhel-tools
      command: ["/bin/sh", "-c"]
      args:
        ["sleep inf"]
EOF
----

. Create two pods in the `verify-audit-logging` namespace:
+
[source,terminal]
----
$ for name in client server; do
cat <<EOF| oc create -n verify-audit-logging -f -
apiVersion: v1
kind: Pod
metadata:
  name: ${name}
spec:
  containers:
    - name: ${name}
      image: registry.access.redhat.com/rhel7/rhel-tools
      command: ["/bin/sh", "-c"]
      args:
        ["sleep inf"]
EOF
done
----
+
Successful output lists the two pods, such as `pod/client` and `pod/server`, and the `created` status.

. To generate traffic and produce network policy audit log entries, complete the following steps:

.. Obtain the IP address for pod named `server` in the `verify-audit-logging` namespace:
+
[source,terminal]
----
$ POD_IP=$(oc get pods server -n verify-audit-logging -o jsonpath='{.status.podIP}')
----

.. Ping the IP address from an earlier command from the pod named `client` in the `default` namespace and confirm the all packets are dropped:
+
[source,terminal]
----
$ oc exec -it client -n default -- /bin/ping -c 2 $POD_IP
----
+
.Example output
[source,text]
----
PING 10.128.2.55 (10.128.2.55) 56(84) bytes of data.

--- 10.128.2.55 ping statistics ---
2 packets transmitted, 0 received, 100% packet loss, time 2041ms
----

.. From the client pod in the `verify-audit-logging` namespace, ping the IP address stored in the `POD_IP shell` environment variable and confirm the system allows all packets.
+
[source,terminal]
----
$ oc exec -it client -n verify-audit-logging -- /bin/ping -c 2 $POD_IP
----
+
.Example output
[source,text]
----
PING 10.128.0.86 (10.128.0.86) 56(84) bytes of data.
64 bytes from 10.128.0.86: icmp_seq=1 ttl=64 time=2.21 ms
64 bytes from 10.128.0.86: icmp_seq=2 ttl=64 time=0.440 ms

--- 10.128.0.86 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 0.440/1.329/2.219/0.890 ms
----

. Display the latest entries in the network policy audit log:
+
[source,terminal]
----
$ for pod in $(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node --no-headers=true | awk '{ print $1 }') ; do
    oc exec -it $pod -n openshift-ovn-kubernetes -- tail -4 /var/log/ovn/acl-audit-log.log
  done
----
+
.Example output
[source,text]
----
2023-11-02T16:28:54.139Z|00004|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
2023-11-02T16:28:55.187Z|00005|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
2023-11-02T16:28:57.235Z|00006|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:Ingress", verdict=drop, severity=alert, direction=to-lport: tcp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:01,dl_dst=0a:58:0a:81:02:23,nw_src=10.131.0.39,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=62,nw_frag=no,tp_src=58496,tp_dst=8080,tcp_flags=syn
2023-11-02T16:49:57.909Z|00028|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
2023-11-02T16:49:57.909Z|00029|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
2023-11-02T16:49:58.932Z|00030|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
2023-11-02T16:49:58.932Z|00031|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0

----

// Module included in the following assemblies:
//
// * networking/network_security/logging-network-security.adoc

[id="nw-networkpolicy-audit-enable_{context}"]
= Enabling egress firewall and network policy audit logging for a namespace

[role="_abstract"]
To enable egress firewall and network policy audit logging for a namespace in OpenShift Container Platform, you can add the `k8s.ovn.org/acl-logging` annotation with the `oc annotate` command. You can also apply a namespace YAML file that sets `Allow` and `Deny` log severity levels.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in to the cluster with a user with `cluster-admin` privileges.

.Procedure

* To enable audit logging for a namespace, enter the following command:
+
[source,terminal]
----
$ oc annotate namespace <namespace> \
  k8s.ovn.org/acl-logging='{ "deny": "alert", "allow": "notice" }'
----
+
--
where:

`<namespace>`:: Specifies the name of the namespace.
--
+
[TIP]
====
You can also apply the following YAML to enable audit logging:

[source,yaml]
----
kind: Namespace
apiVersion: v1
metadata:
  name: <namespace>
  annotations:
    k8s.ovn.org/acl-logging: |-
      {
        "deny": "alert",
        "allow": "notice"
      }
----
====
+
Successful output lists the audit logging name and the `annotated` status.

.Verification

* Display the latest entries in the audit log:
+
[source,terminal]
----
$ for pod in $(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node --no-headers=true | awk '{ print $1 }') ; do
    oc exec -it $pod -n openshift-ovn-kubernetes -- tail -4 /var/log/ovn/acl-audit-log.log
  done
----
+
.Example output
[source,text]
----
2023-11-02T16:49:57.909Z|00028|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
2023-11-02T16:49:57.909Z|00029|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
2023-11-02T16:49:58.932Z|00030|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Egress:0", verdict=allow, severity=alert, direction=from-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0
2023-11-02T16:49:58.932Z|00031|acl_log(ovn_pinctrl0)|INFO|name="NP:verify-audit-logging:allow-from-same-namespace:Ingress:0", verdict=allow, severity=alert, direction=to-lport: icmp,vlan_tci=0x0000,dl_src=0a:58:0a:81:02:22,dl_dst=0a:58:0a:81:02:23,nw_src=10.129.2.34,nw_dst=10.129.2.35,nw_tos=0,nw_ecn=0,nw_ttl=64,nw_frag=no,icmp_type=8,icmp_code=0

----

// Module included in the following assemblies:
//
// * networking/network_security/logging-network-security.adoc

[id="nw-networkpolicy-audit-disable_{context}"]
= Disabling egress firewall and network policy audit logging for a namespace

[role="_abstract"]
To disable egress firewall and network policy audit logging for a namespace in OpenShift Container Platform, you can remove the `k8s.ovn.org/acl-logging` annotation with the `oc annotate` command. You can also apply a namespace YAML file that sets the annotation to `null`.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in to the cluster with a user with `cluster-admin` privileges.

.Procedure

* To disable audit logging for a namespace, enter the following command:
+
[source,terminal]
----
$ oc annotate --overwrite namespace <namespace> k8s.ovn.org/acl-logging-
----
+
--
where:

`<namespace>`:: Specifies the name of the namespace.
--
+
[TIP]
====
You can also apply the following YAML to disable audit logging:

[source,yaml]
----
kind: Namespace
apiVersion: v1
metadata:
  name: <namespace>
  annotations:
    k8s.ovn.org/acl-logging: null
----
====
+
Successful output lists the audit logging name and the `annotated` status.

[id="{context}-additional-resources"]
[role="_additional-resources"]
== Additional resources

* About network policy
* Configuring an egress firewall for a project
