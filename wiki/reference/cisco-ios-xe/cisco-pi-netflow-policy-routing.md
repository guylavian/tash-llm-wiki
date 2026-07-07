---
title: "NetFlow Policy Routing"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-netflow-policy-routing
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 18 NetFlow Policy Routing NetFlow policy routing (NPR) integrates policy routing, which enables traffic engineering and traffic classification, with NetFlow services, which provide billing, capacity planning, and information monitoring on real-time traffic flows. IP policy routing works with Cisco Express Forwarding (formerly known as CEF), distributed Cisco Express Forwarding (formerly"
---

# NetFlow Policy Routing

CHAPTER

18

NetFlow Policy Routing
NetFlow policy routing (NPR) integrates policy routing, which enables traffic engineering and traffic
classification, with NetFlow services, which provide billing, capacity planning, and information monitoring
on real-time traffic flows. IP policy routing works with Cisco Express Forwarding (formerly known as CEF),
distributed Cisco Express Forwarding (formerly known as dCEF), and NetFlow.
• Finding Feature Information, on page 191
• Prerequisites for NetFlow Policy Routing, on page 191
• Restrictions for NetFlow Policy Routing, on page 191
• Information About NetFlow Policy Routing, on page 192
• Additional References, on page 193
• Feature Information for NetFlow Policy Routing, on page 194

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Prerequisites for NetFlow Policy Routing
For NetFlow policy routing to work, the following features must already be configured:
• Cisco Express Forwarding, distributed Cisco Express Forwarding, or NetFlow
• Policy routing

Restrictions for NetFlow Policy Routing
• NetFlow Policy Routing (NPR) is available only on Cisco platforms that support Cisco Express
Forwarding.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
191


NetFlow Policy Routing
Information About NetFlow Policy Routing

• Distributed Forwarding Information Base (FIB)-based policy routing is available only on platforms that
support distributed Cisco Express Forwarding.
• The set ip next-hop verify-availability command is not supported in distributed Cisco Express Forwarding
because distributed Cisco Express Forwarding does not support the Cisco Discovery Protocol (formerly
known as CDP) database.

Information About NetFlow Policy Routing
NetFlow Policy Routing
NetFlow policy routing (NPR) integrates policy routing, which enables traffic engineering and traffic
classification, with NetFlow services, which provide billing, capacity planning, and information monitoring
on real-time traffic flows. IP policy routing works with Cisco Express Forwarding (formerly known as CEF),
distributed Cisco Express Forwarding (formerly known as dCEF), and NetFlow.
NetFlow policy routing leverages the following technologies:
• Cisco Express Forwarding, which looks at a Forwarding Information Base (FIB) instead of a routing
table when switching packets, to address maintenance problems of a demand caching scheme.
• Distributed Cisco Express Forwarding, which addresses the scalability and maintenance problems of a
demand caching scheme.
• NetFlow, which provides accounting, capacity planning, and traffic monitoring capabilities.
The following are the benefits of NPR:
• NPR takes advantage of new switching services. Cisco Express Forwarding, distributed Cisco Express
Forwarding, and NetFlow can now use policy routing.
• Policy routing can be deployed on a wide scale and on high-speed interfaces.
NPR is the default policy routing mode. No additional configuration tasks are required to enable policy routing
with Cisco Express Forwarding, distributed Cisco Express Forwarding, or NetFlow. As soon as one of these
features is turned on, packets are automatically subjected to policy routing in the appropriate switching path.
The following example shows how to configure policy routing with Cisco Express Forwarding. The route is
configured to verify that the next hop 10.0.0.8 of the route map named test is a Cisco Discovery Protocol
neighbor before the device tries to policy-route to it.
Device(config)# ip cef
Device(config)# interface GigabitEthernet 0/0/1
Device(config-if)# ip route-cache flow
Device(config-if)# ip policy route-map test
Device(config-if)# exit
Device(config)# route-map test permit 10
Device(config-route-map)# match ip address 1
Device(config-route-map)# set ip precedence priority
Device(config-route-map)# set ip next-hop 10.0.0.8
Device(config-route-map)# set ip next-hop verify-availability
Device(config-route-map)# exit
Device(config)# route-map test permit 20
Device(config-route-map)# match ip address 101

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
192


NetFlow Policy Routing
Next-Hop Reachability

Device(config-route-map)# set interface Ethernet 0/0/3
Device(config-route-map)# set ip tos max-throughput
Device(config-route-map)# exit

Next-Hop Reachability
You can use the set ip next-hop verify-availability command to configure policy routing to verify the
reachability of the next hop of a route map before the device performs policy routing to that next hop. This
command has the following restrictions:
• It can cause performance degradation.
• Cisco Discovery Protocol must be enabled on the interface.
• The directly connected next hop must be a Cisco Discovery Protocol-enabled Cisco device.
• It does not work with distributed Cisco Express Forwarding configurations.
If a device is policy routing packets to the next hop and the next hop happens to be down, the device tries
unsuccessfully to use the Address Resolution Protocol (ARP). This behavior can continue indefinitely. You
can prevent this behavior by configuring the set ip next-hop verify availability command on the device. This
command first verifies (using a route map) whether the next hop is a Cisco Discovery Protocol neighbor of
the device before routing packets to that next hop. However, if you configure this command on a device whose
next hop is not a Cisco Discovery Protocol neighbor, the device looks at the subsequent next hop, if there is
one. If there is no available next hop, packets are not policy-routed. This configuration is optional because
some media or encapsulations do not support Cisco Discovery Protocol.
If the set ip next-hop verify availability command is not configured, packets are either policy-routed or
remain forever unrouted.
If you want to verify the availability of only some next hops, you can configure different route-map entries
(under the same route-map name) with different criteria (using access-list matching or packet-size matching),
and use the set ip next-hop verify availability configuration command selectively.

Additional References
Related Documents
Related Topic

Document Title

IP routing protocol-independent commands Cisco IOS IP Routing: Protocol-Independent Command
Reference

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
193


NetFlow Policy Routing
Feature Information for NetFlow Policy Routing

Technical Assistance
Description

Link

The Cisco Support and Documentation website provides http://www.cisco.com/cisco/web/support/index.html
online resources to download documentation, software,
and tools. Use these resources to install and configure
the software and to troubleshoot and resolve technical
issues with Cisco products and technologies. Access to
most tools on the Cisco Support and Documentation
website requires a Cisco.com user ID and password.

Feature Information for NetFlow Policy Routing
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 19: Feature Information for NetFlow Policy Routing

Feature Name

Releases

NetFlow Policy Routing

NetFlow policy routing (NPR)
integrates policy routing, which
enables traffic engineering and
traffic classification, with NetFlow
services, which provide billing,
capacity planning, and monitoring
information on real-time traffic
flows. IP policy routing works with
Cisco Express Forwarding,
distributed Cisco Express
Forwarding, and NetFlow.

Policy Routing Infrastructure

The Policy Routing Infrastructure
feature provides full support of IP
policy-based routing with Cisco
Express Forwarding and NetFlow.
When both policy routing and
NetFlow are enabled, redundant
processing is avoided.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
194

Feature Information
