---
title: "Using a firewall"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-firewall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-firewall
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Using a firewall

[id="microshift-using-a-firewall"]
= Using a firewall

[role="_abstract"]
Firewalls are not required in {microshift-short}, but using a firewall can prevent undesired access to the {microshift-short} API.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-about_{context}"]
= About network traffic through the firewall

[role="_abstract"]
Firewalld is a networking service that runs in the background and responds to connection requests, creating a dynamic customizable host-based firewall. If you are using {op-system-ostree-first} with {microshift-short}, firewalld should be installed and you only need to configure it.

Details are provided in procedures that follow. Overall, you must explicitly allow the following OVN-Kubernetes traffic when the `firewalld` service is running.

CNI pod to CNI pod::
CNI pod to Host-Network pod
Host-Network pod to Host-Network pod

CNI pod::
The Kubernetes pod that uses the CNI network

Host-Network pod::
The Kubernetes pod that uses host network
You can configure the `firewalld` service by using the following procedures. In most cases, firewalld is part of {op-system-ostree} installations. If you do not have firewalld, you can install it with the simple procedure in this section.

[IMPORTANT]
====
{microshift-short} pods must have access to the internal CoreDNS component and API servers.
====

[role="_additional-resources"]
.Additional resources

* Required firewall settings
* Allowing network traffic through the firewall

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-install_{context}"]
= Installing the firewalld service

[role="_abstract"]
To install and enable firewalld on your {op-system-ostree} host when the package is missing, you can use `dnf` to install the package and `systemctl` to enable and start the service. Optionally check for the package with `rpm -q firewalld` before you install.

.Procedure

. Optional: Check for firewalld on your system by running the following command:
+
[source,terminal]
----
$ rpm -q firewalld
----

. If the `firewalld` service is not installed, run the following command:
+
[source,terminal]
----
$ sudo dnf install -y firewalld
----

. To start the firewall, run the following command:
+
[source,terminal]
----
$ sudo systemctl enable firewalld --now
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-req-settings_{context}"]
= Required firewall settings

[role="_abstract"]
An IP address range for the node network must be enabled during firewall configuration. You can use the default values or customize the IP address range. If you choose to customize the node network IP address range from the default `10.42.0.0/16` setting, you must also use the same custom range in the firewall configuration.

.Firewall IP address settings
[cols="3",options="header"]
|===
|IP Range
|Firewall rule required
|Description

|10.42.0.0/16
|No
|Host network pod access to other pods

|169.254.169.1
|Yes
|Host network pod access to OpenShift Container Platform API server
|===

[id="microshift-firewall-req-settings-example-commands_{context}"]
== Example commands

The following are examples of commands for settings that are mandatory for firewall configuration:

* Configure host network pod access to other pods:
+
[source,terminal]
----
$ sudo firewall-cmd --permanent --zone=trusted --add-source=10.42.0.0/16
----

* Configure host network pod access to services backed by Host endpoints, such as the OpenShift Container Platform API:
+
[source,terminal]
----
$ sudo firewall-cmd --permanent --zone=trusted --add-source=169.254.169.1
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-optional-settings_{context}"]
= Using optional port settings

[role="_abstract"]
To allow external access to services and APIs in {microshift-short}, you can add custom ports to your firewall configuration. Use the listed ports and protocols as a guide for HTTP, HTTPS, NodePort, mDNS, and API access.

For a complete list of ports and protocols, see "Optional ports".

The following examples show commands to open firewall access for services running on {microshift-short}.

.Procedure

* To add customized ports to your firewall configuration, use the following command syntax:
+
[source,terminal]
----
$ sudo firewall-cmd --permanent --zone=public --add-port=<port number>/<port protocol>
----
+
For example, to configure a port for the {microshift-short} API server, enter the following command:
+
[source,terminal]
----
$ sudo firewall-cmd --permanent --zone=public --add-port=6443/tcp
----
+
To close unnecessary ports in your {microshift-short} instance, follow the procedure in "Closing unused or unnecessary ports to enhance network security".

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-optional-ports_{context}"]
= Optional ports

[role="_abstract"]
The following table lists the optional ports that are available for use with the {microshift-short} firewall service.

.Optional ports
[option="header"]
|===
|Port(s)|Protocol(s)|Description

|80
|TCP
|HTTP port used to serve applications through the {ocp} router.

|443
|TCP
|HTTPS port used to serve applications through the {ocp} router.

|5353
|UDP
|mDNS service to respond for {ocp} route mDNS hosts.

|30000-32767
|TCP
|Port range reserved for NodePort services; can be used to expose applications on the LAN.

|30000-32767
|UDP
|Port range reserved for NodePort services; can be used to expose applications on the LAN.

|6443
|TCP
|HTTPS API port for the OpenShift Container Platform API.
|===

[role="_additional-resources"]
.Additional resources
* Closing unused or unnecessary ports to enhance network security

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-add-services_{context}"]
= Adding services to open ports

[role="_abstract"]
To open default ports for predefined services through firewalld on your {microshift-short} instance, you can use the `firewall-cmd` command. Add each service with the `--add-service` option.

.Procedure

. Optional: You can view all predefined services in firewalld by running the following command
+
[source,terminal]
----
$ sudo firewall-cmd --get-services
----

. To open a service that you want on a default port, run the following example command:
+
[source,terminal]
----
$ sudo firewall-cmd --add-service=mdns
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-allow-traffic_{context}"]
= Allowing network traffic through the firewall

[role="_abstract"]
You can allow network traffic through the firewall by configuring the IP address range and inserting the DNS server to allow internal traffic from pods through the network gateway.

.Procedure

. Use one of the following commands to set the IP address range:

.. Configure the IP address range with default values by running the following command:
+
[source,terminal]
----
$ sudo firewall-offline-cmd --permanent --zone=trusted --add-source=10.42.0.0/16
----

.. Configure the IP address range with custom values by running the following command:
+
[source,terminal]
----
$ sudo firewall-offline-cmd --permanent --zone=trusted --add-source=<custom IP range>
----

. To allow internal traffic from pods through the network gateway, run the following command:
+
[source,terminal]
----
$ sudo firewall-offline-cmd --permanent --zone=trusted --add-source=169.254.169.1
----

. If you are using a load balancer, allow the IPv6 traffic through the firewall by running the following command:
+
[source,terminal]
----
$ sudo firewall-cmd --permanent --zone=trusted --add-source=fd01::/48
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-applying-settings_{context}"]
= Applying firewall settings

[role="_abstract"]
To apply firewall settings after you have finished configuring network access through the firewall, you can reload the firewall service.

.Procedure

* Restart the firewall and apply the settings by running the following command:
+
[source,terminal]
----
$ sudo firewall-cmd --reload
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-verifying-settings_{context}"]
= Verifying firewall settings

[role="_abstract"]
After you have restarted the firewall, you can verify your settings by listing them with the `firewall-cmd` command.

.Procedure

* To verify rules added in the default public zone, such as ports-related rules, run the following command:
+
[source,terminal]
----
$ sudo firewall-cmd --list-all
----

* To verify rules added in the trusted zone, such as IP-range related rules, run the following command:
+
[source,terminal]
----
$ sudo firewall-cmd --zone=trusted --list-all
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

[id="microshift-firewall-update-for-service_{context}"]
= Overview of firewall ports when a service is exposed

[role="_abstract"]
Firewalld is often active when you run services on {microshift-short}. This can disrupt certain services on {microshift-short} because traffic to the ports might be blocked by the firewall. You must ensure that the necessary firewall ports are open if you want certain services to be accessible from outside the host.

There are several options for opening your ports:

* Services of the `NodePort` and `LoadBalancer` type are automatically available with OVN-Kubernetes.
+
In these cases, OVN-Kubernetes adds iptables rules so the traffic to the node IP address is delivered to the relevant ports. This is done using the PREROUTING rule chain and is then forwarded to the OVN-K to bypass the firewalld rules for local host ports and services. Iptables and firewalld are backed by nftables in {op-system-base-full} {op-system-version-major}. The nftables rules, which the iptables generates, always have priority over the rules that the firewalld generates.

* Pods with the `HostPort` parameter settings are automatically available. This also includes the `router-default` pod, which uses ports 80 and 443.
+
For `HostPort` pods, the CRI-O config sets up iptables DNAT (Destination Network Address Translation) to the pod's IP address and port.

These methods function for clients whether they are on the same host or on a remote host. The iptables rules, which are added by OVN-Kubernetes and CRI-O, attach to the PREROUTING and OUTPUT chains. The local traffic goes through the OUTPUT chain with the interface set to the `lo` type. The DNAT runs before it hits filler rules in the INPUT chain.

Because the {microshift-short} API server does not run in CRI-O, it is subject to the firewall configurations. You can open port 6443 in the firewall to access the API server in your {microshift-short} node.

[id="additional-resources_microshift-using-a-firewall_{context}"]
[role="_additional-resources"]
== Additional resources

* RHEL: Using and configuring firewalld

* RHEL: Viewing the current status of firewalld

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-firewall-known-issue_{context}"]
= Known firewall issue

[role="_abstract"]
To avoid traffic failures after a firewalld reload or restart on {microshift-short}, run firewall commands before you start {op-system-base-full}. If you must run firewall commands later, restart the `ovnkube-master` pod in `openshift-ovn-kubernetes` to restore iptable rules that OVN-Kubernetes manages.

The CNI driver in {microshift-short} makes use of iptable rules for some traffic flows, such as those using the NodePort service. The iptable rules are generated and inserted by the CNI driver, but are deleted when the firewall reloads or restarts. The absence of the iptable rules breaks traffic flows.
