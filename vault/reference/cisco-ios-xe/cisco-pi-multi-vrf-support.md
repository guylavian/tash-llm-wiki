---
title: "Multi-VRF Support"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-multi-vrf-support
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 10 Multi-VRF Support The Multi-VRF Support feature allows you to configure and maintain more than one instance of a routing and forwarding table within the same customer edge (CE) device. • Finding Feature Information, on page 117 • Prerequisites for Multi-VRF Support, on page 117 • Restrictions for Multi-VRF Support, on page 117 • Information About Multi-VRF Support, on page 118 • How t"
---

# Multi-VRF Support

CHAPTER

10

Multi-VRF Support
The Multi-VRF Support feature allows you to configure and maintain more than one instance of a routing
and forwarding table within the same customer edge (CE) device.
• Finding Feature Information, on page 117
• Prerequisites for Multi-VRF Support, on page 117
• Restrictions for Multi-VRF Support, on page 117
• Information About Multi-VRF Support, on page 118
• How to Configure Multi-VRF Support, on page 120
• Configuration Examples for Multi-VRF Support, on page 128
• Additional References, on page 130
• Feature Information for Multi-VRF Support, on page 130

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Prerequisites for Multi-VRF Support
The network’s core and provider edge (PE) devices must be configured for Virtual Private Network (VPN)
operation.

Restrictions for Multi-VRF Support
• You can configure the Multi-VRF Support feature only on Layer 3 interfaces.
• The Multi-VRF Support feature is not supported by Interior Gateway Routing Protocol (IGRP) nor
Intermediate System to Intermediate System (IS-IS).

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
117


Multi-VRF Support
Information About Multi-VRF Support

• Label distribution for a given VPN routing and forwarding (VRF) instance on a given device can be
handled by either Border Gateway Protocol (BGP) or Label Distribution Protocol (LDP), but not by both
protocols at the same time.
• Multicast cannot operate on a Layer 3 interface that is configured with the Multi-VRF Support feature.

Information About Multi-VRF Support
How the Multi-VRF Support Feature Works
The Multi-VRF Support feature enables a service provider to support two or more Virtual Private Networks
(VPNs), where the IP addresses can overlap several VPNs. The Multi-VRF Support feature uses input interfaces
to distinguish routes for different VPNs and forms virtual packet-forwarding tables by associating one or more
Layer 3 interfaces with each virtual routing and forwarding (VRF) instance. Interfaces in a VRF can be either
physical, such as FastEthernet ports, or logical, such as VLAN , but a Layer 3 interface cannot belong to more
than one VRF at any one time. The Multi-VRF Support feature allows an operator to support two or more
routing domains on a customer edge (CE) device, with each routing domain having its own set of interfaces
and its own set of routing and forwarding tables. The Multi-VRF Support feature makes it possible to extend
the label switched paths (LSPs) to the CE and into each routing domain that the CE supports.
The Multi-VRF Support feature works as follows:
• Each CE device advertises its site’s local routes to a provider edge (PE) device and learns the remote
VPN routes from that provider edge (PE) device.
• PE devices exchange routing information with CE devices by using static routing or a routing protocol
such as the Border Gateway Protocol (BGP), Routing Information Protocol version 1 (RIPv1), or RIPv2.
• PE devices exchange MPLS label information with CE devices through Label Distribution Protocol
(LDP) or BGP.
• The PE device needs to maintain VPN routes only for those VPNs to which it is directly attached,
eliminating the requirement that the PE maintain all of the service provider’s VPN routes. Each PE device
maintains a VRF for each of its directly connected sites. Two or more interfaces on a PE device can be
associated with a single VRF if all the sites participate in the same VPN. Each VPN is mapped to a
specified VRF. After learning local VPN routes from CE devices, the PE device exchanges VPN routing
information with other PE devices through internal BGP (iBGP).
With the Multi-VRF Support feature, two or more customers can share one CE device, and only one physical
link is used between the CE and the PE devices. The shared CE device maintains separate VRF tables for
each customer and routes packets for each customer based on that customer’s own routing table. The Multi-VRF
Support feature extends limited PE device functionality to a CE device, giving it the ability, through the
maintenance of separate VRF tables, to extend the privacy and security of a VPN to the branch office.
The figure below shows a configuration where each CE device acts as if it were two CE devices. Because the
Multi-VRF Support feature is a Layer 3 feature, each interface associated with a VRF must be a Layer 3
interface.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
118


Multi-VRF Support
How Packets Are Forwarded in a Network Using the Multi-VRF Support Feature

Figure 7: Each CE Device Acting as Several Virtual CE Devices

How Packets Are Forwarded in a Network Using the Multi-VRF Support Feature
Following is the packet-forwarding process in an Multi-VRF customer edge (CE)-enabled network, as illustrated
in the figure above:
• When the CE receives a packet from a Virtual Private Network (VPN), it looks up the routing table based
on the input interface. When a route is found, the CE imposes the Multiprotocol Label Switching (MPLS)
label that it received from the provider edge (PE) for that route and forwards the packet to the PE.
• When the ingress PE receives a packet from the CE, it swaps the incoming label with the corresponding
label stack and sends the packet to the MPLS network.
• When an egress PE receives a packet from the network, it swaps the VPN label with the label that it had
earlier received for the route from the CE, and it forwards the packet to the CE.
• When a CE receives a packet from an egress PE, it uses the incoming label on the packet to forward the
packet to the correct VPN.
To configure Multi-VRF, you create a VRF table and then specify the Layer 3 interface associated with that
VRF. Next, you configure the routing protocols within the VPN, and between the CE and the PE. The Border
Gateway Protocol (BGP) is the preferred routing protocol for distributing VPN routing information across
the provider’s backbone.
The Multi-VRF network has three major components:
• VPN route target communities: These are lists of all other members of a VPN community. You must
configure VPN route targets for each VPN community member.
• Multiprotocol BGP peering of VPN community PE devices: This propagates VRF reachability information
to all members of a VPN community. You must configure BGP peering in all PE devices within a VPN
community.
• VPN forwarding: This transports all traffic between VPN community members across a VPN
service-provider network.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
119


Multi-VRF Support
Considerations When Configuring the Multi-VRF Support Feature

Considerations When Configuring the Multi-VRF Support Feature
• A device with the Multi-VRF Support feature is shared by several customers, and each customer has its
own routing table.
• Because each customer uses a different virtual routing and forwarding (VRF) table, the same IP addresses
can be reused. Overlapping IP addresses are allowed in different Virtual Private Networks (VPNs).
• The Multi-VRF Support feature lets several customers share the same physical link between the provider
edge (PE) and the customer edge (CE) devices. Trunk ports with several VLANs separate packets among
the customers. Each customer has its own VLAN.
• For the PE device, there is no difference between using the Multi-VRF Support feature or using several
CE devices.
• The Multi-VRF Support feature does not affect the packet-switching rate.

How to Configure Multi-VRF Support
Configuring VRFs
To configure virtual routing and forwarding (VRF) instances, complete the following procedure. Be sure to
configure VRFs on both the provider edge (PE) and customer edge (CE) devices.
If a VRF has not been configured, the device has the following default configuration:
• No VRFs have been defined.
• No import maps, export maps, or route maps have been defined.
• No VRF maximum routes exist.
• Only the global routing table exists on the interface.
The following are the supported flavors of multicast over VRF on Cisco ASR 920 RSP2 module:
• Multicast with multi-VRF (MPLS VPN/MLDP)
• Multicast with GRE tunnel (MVPN GRE)
• Multicast with VRF-lite

Note

Multi-VRF/MVPN GRE configured layer-3 interface cannot participate in more than one VRF at the same
time.

SUMMARY STEPS
1.
2.
3.

enable
configure terminal
ip routing

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
120


Multi-VRF Support
Configuring VRFs

4.
5.
6.
7.
8.
9.
10.
11.
12.

ip vrf vrf-name
rd route-distinguisher
route-target {export | import | both} route-target-ext-community
import map route-map
exit
interface type slot/subslot/port[.subinterface]
ip vrf forwarding vrf-name
end
show ip vrf

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

Enables IP routing.

ip routing
Example:
Device(config)# ip routing

Step 4

Names the VRF, and enters VRF configuration mode.

ip vrf vrf-name
Example:
Device(config)# ip vrf v1

Step 5

Step 6

rd route-distinguisher

Creates a VRF table by specifying a route distinguisher.

Example:
Device(config-vrf)# rd 100:1

Enter either an autonomous system number and an arbitrary
number (xxx:y), or an IP address and an arbitrary number
(A.B.C.D:y).

route-target {export | import | both}
route-target-ext-community

Creates a list of import, export, or import and export route
target communities for the specified VRF.

Example:

Enter either an autonomous system number and an arbitrary
number (xxx:y), or an IP address and an arbitrary number
(A.B.C.D:y).

Device(config-vrf)# route-target export 100:1

Note

This command works only if BGP is running.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
121


Multi-VRF Support
Configuring BGP as the Routing Protocol

Step 7

Command or Action

Purpose

import map route-map

(Optional) Associates a route map with the VRF.

Example:
Device(config-vrf)# import map importmap1

Step 8

Returns to global configuration mode.

exit
Example:
Device(config-vrf)# exit

Step 9

interface type slot/subslot/port[.subinterface]
Example:

Specifies the Layer 3 interface to be associated with the
VRF and enters interface configuration mode.
The interface can be a routed port or an .

Device(config)# interface

Step 10

ip vrf forwarding vrf-name

Associates the VRF with the Layer 3 interface.

Example:
Device(config-if)# ip vrf forwarding v1

Step 11

Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Step 12

Displays the settings of the VRFs.

show ip vrf
Example:
Device# show ip vrf

Configuring BGP as the Routing Protocol
Most routing protocols can be used between the customer edge (CE) and the provider edge (PE) devices.
However, external BGP (eBGP) is recommended, because:
• BGP does not require more than one algorithm to communicate with many CE devices.
• BGP is designed to pass routing information between systems run by different administrations.
• BGP makes it easy to pass route attributes to the CE device.
When BGP is used as the routing protocol, it can also be used to handle the Multiprotocol Label Switching
(MPLS) label exchange between the PE and CE devices. By contrast, if Open Shortest Path First (OSPF),
Enhanced Interior Gateway Routing Protocol (EIGRP), Routing Information Protocol (RIP), or static routing
is used, the Label Distribution Protocol (LDP) must be used to signal labels.
To configure a BGP PE-to-CE routing session, perform the following steps on the CE and on the PE devices.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
122


Multi-VRF Support
Configuring BGP as the Routing Protocol

SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.
9.

enable
configure terminal
router bgp autonomous-system-number
network ip-address mask network-mask
redistribute ospf process-id match internal
network ip-address wildcard-mask area area-id
address-family ipv4 vrf vrf-name
neighbor {ip-address | peer-group-name} remote-as as-number
neighbor address activate

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Configures the BGP routing process with the autonomous
system number passed to other BGP devices, and enters
router configuration mode.

Device(config)# router bgp 100

Step 4

network ip-address mask network-mask

Specifies a network and mask to announce using BGP.

Example:
Device(config-router)# network 10.0.0.0 mask
255.255.255.0

Step 5

redistribute ospf process-id match internal

Sets the device to redistribute OSPF internal routes.

Example:
Device(config-router)# redistribute ospf 2 match
internal

Step 6

network ip-address wildcard-mask area area-id
Example:

Identifies the network address and mask on which OSPF is
running, and the area ID of that network address.

Device(config-router)# network 10.0.0.0
255.255.255.0 area 0

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
123


Multi-VRF Support
Configuring PE-to-CE MPLS Forwarding and Signaling with BGP

Step 7

Command or Action

Purpose

address-family ipv4 vrf vrf-name

Identifies the name of the virtual routing and forwarding
(VRF) instance that will be associated with the next two
commands, and enters VRF address-family mode.

Example:
Device(config-router)# address-family ipv4 vrf v12

Step 8

neighbor {ip-address | peer-group-name} remote-as
as-number
Example:

Informs this device’s BGP neighbor table of the neighbor’s
address (or peer group name) and the neighbor’s
autonomous system number.

Device(config-router-af)# neighbor 10.0.0.3
remote-as 100

Step 9

neighbor address activate
Example:

Activates the advertisement of the IPv4 address-family
neighbors.

Device(config-router-af)# neighbor 10.0.0.3
activate

Configuring PE-to-CE MPLS Forwarding and Signaling with BGP
If the Border Gateway Protocol (BGP) is used for routing between the provider edge (PE) and the customer
edge (CE) devices, configure BGP to signal the labels on the virtual routing and forwarding (VRF) interfaces
of both the CE and the PE devices. You must enable signalling globally at the router-configuration level and
for each interface:
• At the router-configuration level, to enable Multiprotocol Label Switching (MPLS) label signalling via
BGP, use the neighbor send-label command).
• At the interface level, to enable MPLS forwarding on the interface used for the PE-to-CE external BGP
(eBGP) session, use the mpls bgp forwarding command.
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 vrf vrf-name
neighbor address send-label
neighbor address activate
end
configure terminal
interface type slot/subslot/port[.subinterface]
mpls bgp forwarding

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
124


Multi-VRF Support
Configuring PE-to-CE MPLS Forwarding and Signaling with BGP

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Configures the BGP routing process with the autonomous
system number passed to other BGP devices and enters
router configuration mode.

Device(config)# router bgp 100

Step 4

Identifies the name of the VRF instance that will be
associated with the next two commands and enters address
family configuration mode.

address-family ipv4 vrf vrf-name
Example:
Device(config-router)# address-family ipv4 vrf
v12

Step 5

Enables the device to use BGP to distribute MPLS labels
along with the IPv4 routes to the peer devices.

neighbor address send-label
Example:
Device(config-router-af)# neighbor 10.0.0.3
send-label

Step 6

If a BGP session is running when you issue this command,
the command does not take effect until the BGP session
is restarted.
Activates the advertisement of the IPv4 address-family
neighbors.

neighbor address activate
Example:
Device(config-router-af)# neighbor 10.0.0.3
activate

Step 7

Returns to privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Step 8

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 9

interface type slot/subslot/port[.subinterface]
Example:

Enters interface configuration mode for the interface to be
used for the BGP session.
The interface can be a routed port or an .

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
125


Multi-VRF Support
Configuring a Routing Protocol Other than BGP

Command or Action

Purpose

Device(config)# interface

Step 10

mpls bgp forwarding

Enables MPLS forwarding on the interface.

Example:
Device(config-if)# mpls bgp forwarding

Configuring a Routing Protocol Other than BGP
You can use the Routing Information Protocol (RIP), Enhanced Interior Gateway Routing Protocol (EIGRP),
Open Shortest Path First (OSPF), or static routing. This configuration uses OSPF, but the process is the same
for other protocols.
If you use OSPF as the routing protocol between the provider edge (PE) and the customer edge (CE) devices,
issue the capability vrf-lite command in router configuration mode.

Note

If RIP EIGRP, OSPF or static routing is used, the Label Distribution Protocol (LDP) must be used to signal
labels.
The Multi-VRF Support feature is not supported by Interior Gateway Routing Protocol (IGRP) or Intermediate
System-to-Intermediate System (IS-IS).
Multicast cannot be configured on the same Layer 3 interface as the Multi-VRF Support feature is configured.

SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.

enable
configure terminal
router ospf process-id [vrf vpn-name]
log-adjacency-changes
redistribute bgp autonomous-system-number subnets
network ip-address subnet-mask area area-id
end
show ip ospf

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
126


Multi-VRF Support
Configuring PE-to-CE MPLS Forwarding and Signaling with LDP

Command or Action

Purpose

Device# configure terminal

Step 3

router ospf process-id [vrf vpn-name]
Example:

Enables OSPF routing, specifies a virtual routing and
forwarding (VRF) table, and enters router configuration
mode.

Device(config)# router ospf 100 vrf v1

Step 4

log-adjacency-changes

(Optional) Logs changes in the adjacency state.

Example:

This is the default state.

Device(config-router)# log-adjacency-changes

Step 5

redistribute bgp autonomous-system-number subnets
Example:

Sets the device to redistribute information from the Border
Gateway Protocol (BGP) network to the OSPF network.

Device(config-router)# redistribute bgp 800 subnets

Step 6

network ip-address subnet-mask area area-id
Example:

Indicates the network address and mask on which OSPF
runs, and the area ID of that network address.

Device(config-router)# network 10.0.0.0
255.255.255.0 area 0

Step 7

Returns to privileged EXEC mode.

end
Example:
Device(config-router)# end

Step 8

Displays information about the OSPF routing processes.

show ip ospf
Example:
Device# show ip ospf

Configuring PE-to-CE MPLS Forwarding and Signaling with LDP
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
interface type slot /subslot/port[.subinterface]
mpls ip

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
127


Multi-VRF Support
Configuration Examples for Multi-VRF Support

Command or Action
Example:

Purpose
• Enter your password if prompted.

Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

interface type slot /subslot/port[.subinterface]
Example:

Enters interface configuration mode for the interface
associated with the VRF. The interface can be a routed port
or an .

Device(config)# interface

Step 4

Enables MPLS forwarding of IPv4 packets along normally
routed paths for this interface.

mpls ip
Example:
Device(config-if)# mpls ip

Configuration Examples for Multi-VRF Support
The figure below is an example of a Multi-VRF topology.

Example: Configuring Multi-VRF Support on the PE Device
The following example shows how to configure a VRF:
configure terminal
ip vrf v1
rd 100:1
route-target export 100:1
route-target import 100:1
exit
ip vrf v2
rd 100:2
route-target export 100:2
route-target import 100:2
exit

The following example shows how to configure on PE device, PE-to-CE connections using BGP for both
routing and label exchange:
The following example shows how to configure on PE device, PE-to-CE connections using OSPF for routing
and LDP for label exchange:

Example: Configuring Multi-VRF Support on the CE Device
The following example shows how to configure VRFs:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
128


Multi-VRF Support
Example: Configuring Multi-VRF Support on the CE Device

configure terminal
ip routing
ip vrf v11
rd 800:1
route-target export 800:1
route-target import 800:1
exit
ip vrf v12
rd 800:2
route-target export 800:2
route-target import 800:2
exit

The following example shows how to configure CE device VPN connections:
interface
ip vrf forwarding v11
ip address 10.0.0.8 255.255.255.0
exit
interface
ip vrf forwarding v12
ip address 10.0.0.8 255.255.255.0
exit
router ospf 1 vrf v11
network 10.0.0.0 255.255.255.0 area 0
network 10.0.0.0 255.255.255.0 area 0
exit
router ospf 2 vrf v12
network 10.0.0.0 255.255.255.0 area 0
network 10.0.0.0 255.255.255.0 area 0
exit

Note

If BGP is used for routing between the PE and CE devices, the BGP-learned routes from the PE device can
be redistributed into OSPF using the commands in the following example.

router ospf 1 vrf v11
redistribute bgp 800 subnets
exit
router ospf 2 vrf v12
redistribute bgp 800 subnets
exit

The following example shows how to configure on CE devices, PE-to-CE connections using BGP for both
routing and label exchange:
The following example shows how to configure on CE devices, PE-to-CE connections using OSPF for both
routing and LDP for label exchange:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
129


Multi-VRF Support
Additional References

Additional References
Related Documents
Related Topic

Document Title

MPLS and MPLS applications commands Cisco IOS Multiprotocol Label Switching Command Reference
OSPF with Multi-VRF

“OSPF Support for Multi-VRF in CE Routers” module in the
OSPF Configuration Guide .

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

Feature Information for Multi-VRF Support
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 10: Feature Information for Multi-VRF Support

Feature Name
Multi-VRF Support

Releases Feature Information
The Multi-VRF Support feature allows you to configure and maintain more
than one instance of a routing and forwarding table within the same CE
device.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
130
