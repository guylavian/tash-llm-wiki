---
title: "About the OVN-Kubernetes network plugin"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-cni
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-cni
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# About the OVN-Kubernetes network plugin

[id="microshift-cni"]
= About the OVN-Kubernetes network plugin

[role="_abstract"]
You can use the OVN-Kubernetes Network Interface to create and manage network connections for internet-connected nodes.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-default-networking-plugin_{context}"]
= {microshift-short} default networking plugin

[role="_abstract"]
The OVN-Kubernetes Container Network Interface (CNI) plugin is the default networking solution for a {microshift-short} node. OVN-Kubernetes is a virtualized network for pods and services that is based on Open Virtual Network (OVN).

* Changing the CNI is not supported on {microshift-short}.
* Default network configuration and connections are applied automatically in {microshift-short} with the `microshift-networking` RPM during installation.
* A node that uses the OVN-Kubernetes network plugin also runs Open vSwitch (OVS) on the node.
* OVN-K configures OVS on the node to implement the declared network configuration.
* Host physical interfaces are not bound by default to the OVN-K gateway bridge, `br-ex`. You can use standard tools on the host for managing the default gateway, such as the Network Manager CLI (`nmcli`).

Using configuration files or custom scripts, you can configure the following networking settings:

* You can use subnet CIDR ranges to allocate IP addresses to pods.
* You can change the maximum transmission unit (MTU) value.
* You can configure firewall ingress and egress.
* You can define network policies in the {microshift-short}, including ingress and egress rules.
* You can use the {microshift-short} Multus plugin to chain other CNI plugins.
* You can configure or remove the ingress router.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-nw-customization-matrix_{context}"]
= {microshift-short} networking configuration matrix

[role="_abstract"]
The following table summarizes the status of networking features and capabilities that are either present as defaults, supported for configuration, or not available with the {microshift-short} service:

.{microshift-short} networking features and capabilities overview
[cols="50%,20%,30%",options="header"]
|===
|Network capability|Availability|Configuration supported

|Advertise address|Yes|Yes

|Kubernetes network policy|Yes|Yes

|Kubernetes network policy logs|Not available|N/A

|Load balancing|Yes|Yes

|Multicast DNS|Yes|Yes

|Network proxies|Yes|CRI-O

|Network performance|Yes|MTU configuration

|Egress IPs|Not available|N/A

|Egress firewall|Not available|N/A

|Egress router|Not available|N/A

|Firewall|No|Yes

|Hardware offloading|Not available|N/A

|Hybrid networking|Not available|N/A

|IPsec encryption for intra-cluster communication|Not available|N/A

|IPv6|Supported|N/A

|Ingress router|Yes|Yes

|Multiple networks plugin|Yes|Yes
|===

Additional details about networking capabilities::

* `Advertise address`: If unset, the default value is set to the next immediate subnet after the service network. For example, when the service network is `10.43.0.0/16`, the `advertiseAddress` is set to `10.44.0.0/32`.

* `Multicast DNS`: You can use the multicast DNS protocol (mDNS) to allow name resolution and service discovery within a Local Area Network (LAN) using multicast exposed on the `5353/UDP` port.

* `Network proxies`: There is no built-in transparent proxying of egress traffic in {microshift-short}. Egress must be manually configured.

* `Firewall`: Setting up the firewalld service is supported by {op-system-ostree}.

* `IPv6`: Is supported in both single-stack and dual-stack networks with the OVN-Kubernetes network plugin. You can also use IPv6 by connecting to other networks with the {microshift-short} Multus CNI plugin.

* `Ingress router`: Configure by using the {microshift-short} `config.yaml` file.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-default-config-yaml.adoc
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-yaml-default_{context}"]
= Default settings

[role="_abstract"]
When no `config.yaml` or configuration snippet exists, {microshift-short} uses built-in default values. To view these defaults, run `microshift show-config`.

The following example shows the default configuration settings.

.Procedure

*  To see the default values, run the following command:
+
[source,terminal]
----
$ microshift show-config
----
+
.Default values example output in YAML form
[source,yaml]
----
apiServer:
  advertiseAddress: 10.44.0.0/32
  auditLog:
    maxFileAge: 0
    maxFileSize: 200
    maxFiles: 10
    profile: Default
  namedCertificates:
    - certPath: ""
      keyPath: ""
      names:
        - ""
  subjectAltNames: []
  tls:
    cipherSuites:
    minVersion: VersionTLS12
debugging:
  logLevel: "Normal"
dns:
  baseDomain: microshift.example.com
etcd:
  memoryLimitMB: 0
genericDevicePlugin:
    devices:
        - groups:
            - count: 1
              paths:
                - limit: 1
                  mountPath: /dev/ttyACM0
                  path: /dev/ttyACM0
                  permissions: mrw
                  readOnly: false
                  type: Device
              usbs:
                - product: ""
                  serial: ""
                  vendor: ""
          name: serial
    domain: device.microshift.io
    status: Disabled
ingress:
  accessLogging:
    destination:
      type:
      container:
        maxLength: 1024
      syslog:
        address: ""
        facility: ""
        maxLength: 1024
        port: 0
        type: ""
    httpCaptureCookies:
      - matchType: ""
        maxLength: 0
        name: ""
        namePrefix: ""
    httpCaptureHeaders:
      request:
        - maxLength: 0
          name: ""
      response:
        - maxLength: 0
          name: ""
    httpLogFormat: ""
    status: Disabled
  certificateSecret: router-certs-default
  clientTLS:
    allowedSubjectPatterns:
    clientCA:
      name: ""
    clientCertificatePolicy: ""
  defaultHTTPVersion: 1
  forwardedHeaderPolicy: ""
  httpCompression:
    mimeTypes:
      - ""
  httpEmptyRequestsPolicy: Respond
  httpErrorCodePages:
      name: ""
  listenAddress: []
  logEmptyRequests: Log
  ports:
    http: 80
    https: 443
  routeAdmissionPolicy:
    namespaceOwnership: InterNamespaceAllowed
    wildcardPolicy: WildcardPolicyAllowed
  status: Managed
  tlsSecurityProfile:
    type: Intermediate
  tuningOptions:
      clientFinTimeout: "1s"
      clientTimeout: "30s"
      headerBufferBytes: 0
      headerBufferMaxRewriteBytes: 0
      healthCheckInterval: "5s"
      maxConnections: 0
      serverFinTimeout: "1s"
      serverTimeout: "30s"
      threadCount: 0
      tlsInspectDelay: "5s"
      tunnelTimeout: "1h"
kubelet:
manifests:
  kustomizePaths:
    - /usr/lib/microshift/manifests
    - /usr/lib/microshift/manifests.d/*
    - /etc/microshift/manifests
    - /etc/microshift/manifests.d/*
network:
  clusterNetwork:
    - 10.42.0.0/16
  cniPlugin: ""
  multus:
    status: Disabled
  serviceNetwork:
    - 10.43.0.0/16
  serviceNodePortRange: 30000-32767
node:
  hostnameOverride: ""
  nodeIP: ""
  nodeIPv6: ""
storage:
  driver: ""
  optionalCsiComponents:
    - ""
telemetry:
  endpoint: https://infogw.api.openshift.com
  proxy: ""
  status: Enabled
----
+
where:
+
--
`apiserver.advertiseAddress`:: Specifies the address of the service network.
`network.multus.status`:: Specifies the status of the Multus Container Network Interface (CNI).
`node.nodeIP`:: Specifies the IP address of the default route.
`storage.driver`:: Specifies the storage driver to use. Default null value deploys Logical Volume Managed Storage (LVMS).
`storage.optionalCsiComponents`:: Specifies the CSI components to deploy. Default null value deploys `snapshot-controller`.
--

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-network-features_{context}"]
= Network features

[role="_abstract"]
Understand which networking feature are available and which are not for your {microshift-short} deployments.

Networking features available with {microshift-short}  include:

* Kubernetes network policy
* Dynamic node IP
* Custom gateway interface
* Second gateway interface
* Node network on specified host interface
* Blocking external access to NodePort service on specific host interfaces

Networking features not available with {microshift-short} :

* Egress IP/firewall/QoS: disabled
* Hybrid networking: not supported
* IPsec: not supported
* Hardware offload: not supported

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-ip-forward_{context}"]
= IP forward

[role="_abstract"]
You must use `ip_forward` to access network connectivity.

The host network `sysctl net.ipv4.ip_forward` kernel parameter is automatically enabled by the `ovnkube-master` container when started. This is required to forward incoming traffic to the CNI. For example, accessing the NodePort service from outside of a node fails if `ip_forward` is disabled.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-network-performance_{context}"]
= Network performance optimizations

[role="_abstract"]
By default, three performance optimizations are applied to OVS services to minimize resource consumption:

* CPU affinity to `ovs-vswitchd.service` and `ovsdb-server.service`
* `no-mlockall` to `openvswitch.service`
* Limit handler and `revalidator` threads to `ovs-vswitchd.service`

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc

[id="microshift-nw-components-svcs_{context}"]
= {microshift-short} networking components and services

[role="_abstract"]
Understand networking components and services and their operation in {microshift-short}.

[NOTE]
====
The `microshift-networking` RPM is a package that automatically pulls in any networking-related dependencies and systemd services to initialize networking, for example, the `microshift-ovs-init` systemd service.
====

NetworkManager::
NetworkManager is required to set up the initial gateway bridge on the {microshift-short} node. The NetworkManager and `NetworkManager-ovs` RPM packages are installed as dependencies to the `microshift-networking` RPM package, which contains the necessary configuration files. NetworkManager in {microshift-short} uses the `keyfile` plugin and is restarted after installation of the `microshift-networking` RPM package.

microshift-ovs-init::
The `microshift-ovs-init.service` is installed by the `microshift-networking` RPM package as a dependent systemd service to `microshift.service`. It is responsible for setting up the OVS gateway bridge.

OVN containers::
Two OVN-Kubernetes daemon sets are rendered and applied by {microshift-short}.

* *ovnkube-master*
Includes the `northd`, `nbdb`, `sbdb` and `ovnkube-master` containers.

* *ovnkube-node*
The ovnkube-node includes the OVN-Controller container.
+
After {microshift-short} starts, the OVN-Kubernetes daemon sets are deployed in the `openshift-ovn-kubernetes` namespace.

Packaging::
OVN-Kubernetes manifests and startup logic are built into {microshift-short}. The systemd services and configurations included in the `microshift-networking` RPM are:

* `/etc/NetworkManager/conf.d/microshift-nm.conf` for `NetworkManager.service`
* `/etc/systemd/system/ovs-vswitchd.service.d/microshift-cpuaffinity.conf` for `ovs-vswitchd.service`
* `/etc/systemd/system/ovsdb-server.service.d/microshift-cpuaffinity.conf` for `ovs-server.service`
* `/usr/bin/configure-ovs-microshift.sh` for `microshift-ovs-init.service`
* `/usr/bin/configure-ovs.sh` for `microshift-ovs-init.service`
* `/etc/crio/crio.conf.d/microshift-ovn.conf` for the CRI-O service

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc.adoc

[id="microshift-bridge-mappings_{context}"]
= Bridge mappings

[role="_abstract"]
Understand how provider network traffic reaches the physical network through bridge mappings. The following concepts apply:

* Traffic leaves the provider network and arrives at the `br-int` bridge.
* A patch port between `br-int` and `br-ex` then allows the traffic to traverse to and from the provider network and the edge network.
* Kubernetes pods are connected to the `br-int` bridge through a virtual ethernet pair. One end of the virtual ethernet pair is attached to the pod namespace, and the other end is attached to the `br-int` bridge.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-cni.adoc

[id="microshift-network-topology_{context}"]
= Network topology

[role="_abstract"]
OVN-Kubernetes provides an overlay-based networking implementation. This overlay includes an OVS-based implementation of `Service` and `NetworkPolicy` resources.

The overlay network uses the Geneve (Generic Network Virtualization Encapsulation) tunnel protocol. The pod maximum transmission unit (MTU) for the Geneve tunnel is set to the default route MTU if it is not configured.

To configure the MTU, you must set an equal-to or less-than value than the MTU of the physical interface on the host. A less-than value for the MTU makes room for the required information that is added to the tunnel header before it is transmitted.

[IMPORTANT]
====
The MTU value of the OVN overlay networking in {microshift-short} must be 100 bytes smaller than the MTU value of the base network. If no MTU value is configured, {microshift-short} autoconfigures the value using the MTU value of the default gateway (Internet Protocol version 4 (IPv4) or Internet Protocol version 6 (IPv6)) of the host. If the auto-configuration does not work correctly, the MTU value can be configured manually. For example, if the MTU value of the network is `9000`, the OVN MTU size must be set to `8900`.
====

OVS runs as a systemd service on the {microshift-short} node. The OVS RPM package is installed as a dependency to the `microshift-networking` RPM package. OVS starts immediately when the `microshift-networking` RPM is installed.

image:317_RHbM_OVN_topology_0923.png[title="{microshift-short} uses an overlay-based networking implementation, details follow."]

[id="microshift-description-ovn-logical-components_{context}"]
== Description of the OVN logical components of the virtualized network

OVN node switch::
A virtual switch named `<node-name>`. The OVN node switch is named according to the hostname of the node.
** In this example, the `node-name` is `microshift-dev`.

OVN cluster router::
A virtual router named `ovn_cluster_router`, also known as the distributed router.
** In this example, the node network is `10.42.0.0/16`.

OVN join switch::
A virtual switch named `join`.

OVN gateway router::
A virtual router named `GR_<node-name>`, also known as the external gateway router.

OVN external switch::
A virtual switch named `ext_<node-name>.`

[id="microshift-description-connections-network-topology_{context}"]
== Description of the connections in the network topology figure

* The north-south traffic between the network service and the OVN external switch `ext_microshift-dev` is provided through the host kernel by the gateway bridge `br-ex`.
* The OVN gateway router `GR_microshift-dev` is connected to the external network switch `ext_microshift-dev` through the logical router port 4. Port 4 is attached with the node IP address 192.168.122.14.
* The join switch `join` connects the OVN gateway router `GR_microshift-dev` to the OVN cluster router `ovn_cluster_router`. The IP address range is 100.62.0.0/16.
** The OVN gateway router `GR_microshift-dev` connects to the OVN join switch `join` through the logical router port 3. Port 3 attaches with the internal IP address 100.64.0.2.
** The OVN cluster router `ovn_cluster_router` connects to the join switch `join` through the logical router port 2. Port 2 attaches with the internal IP address 100.64.0.1.
* The OVN cluster router `ovn_cluster_router` connects to the node switch `microshift-dev` through the logical router port 1. Port 1 is attached with the OVN cluster network IP address 10.42.0.1.
* The east-west traffic between the pods and the network service is provided by the OVN cluster router `ovn_cluster_router` and the node switch `microshift-dev`. The IP address range is 10.42.0.0/24.
* The east-west traffic between pods is provided by the node switch `microshift-dev` without network address translation (NAT).
* The north-south traffic between the pods and the external network is provided by the OVN cluster router `ovn_cluster_router` and the host network. This router is connected through the `ovn-kubernetes` management port `ovn-k8s-mp0`, with the IP address 10.42.0.2.
* All the pods are connected to the OVN node switch through their interfaces.
** In this example, Pod 1 and Pod 2 are connected to the node switch through `Interface 1` and `Interface 2`.

[id="_additional-resources_microshift-cni_{context}"]
[role="_additional-resources"]
== Additional resources

* Customizing {microshift-short} by using the configuration file
* Understanding networking settings
* About using multiple networks
* About network policies
