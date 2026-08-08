---
title: "Multi-VRF Selection Using Policy-Based Routing"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-multi-vrf-selection-using-policy-based-routing
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 9 Multi-VRF Selection Using Policy-Based Routing The Multi-VRF Selection Using Policy-Based Routing (PBR) feature allows a specified interface on a provider edge (PE) device to route packets to Virtual Private Networks (VPNs) based on packet length or match criteria defined in an IP access list. You can enable VPN routing and forwarding (VRF) selection by policy routing packets through a"
---

# Multi-VRF Selection Using Policy-Based Routing

CHAPTER

9

Multi-VRF Selection Using Policy-Based Routing
The Multi-VRF Selection Using Policy-Based Routing (PBR) feature allows a specified interface on a provider
edge (PE) device to route packets to Virtual Private Networks (VPNs) based on packet length or match criteria
defined in an IP access list.
You can enable VPN routing and forwarding (VRF) selection by policy routing packets through a route map,
through the global routing table, or to a specified VRF.
You can enable policy-routing packets for VRF instances by using route map commands with set commands.
On supported hardware, you can configure both the Multi-VRF Selection Using Policy-Based Routing feature
and the MPLS VPN VRF Selection Based on a Source IP Address feature on the same interface.
• Finding Feature Information, on page 99
• Prerequisites for Multi-VRF Selection Using Policy-Based Routing, on page 100
• Restrictions for Multi-VRF Selection Using Policy-Based Routing, on page 100
• Information About Multi-VRF Selection Using Policy-Based Routing, on page 101
• How to Configure Multi-VRF Selection Using Policy-Based Routing, on page 104
• Configuration Examples for Multi-VRF Selection Using Policy-Based Routing, on page 112
• Additional References, on page 113
• Feature Information for Multi-VRF Selection Using Policy-Based Routing, on page 113
• Glossary, on page 114

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
99


Multi-VRF Selection Using Policy-Based Routing
Prerequisites for Multi-VRF Selection Using Policy-Based Routing

Prerequisites for Multi-VRF Selection Using Policy-Based
Routing
• The device must support policy-based routing (PBR) in order for you to configure this feature. For
platforms that do not support PBR, use the MPLS VPN VRF Selection Based on a Source IP Address
feature.
• A Virtual Private Network (VPN) virtual routing and forwarding (VRF) instance must be defined before
you configure this feature. An error message is displayed on the console if no VRF exists.

RestrictionsforMulti-VRFSelectionUsingPolicy-BasedRouting
• All commands that aid in routing also support hardware switching, except for the set ip next-hop verify
availability command because Cisco Discovery Protocol information is not available in the line cards.
• Protocol Independent Multicast (PIM) and multicast packets do not support policy-based routing (PBR)
and cannot be configured for a source IP address that is a match criterion for this feature.
• The set vrf and set ip global next-hop commands can be configured with the set default interface, set
interface , set ip default next-hop, and set ip next-hop commands. But the set vrf and set ip global
next-hop commands take precedence over the set default interface, set interface , set ip default
next-hop, and set ip next-hop commands. No error message is displayed if you attempt to configure the
set vrf command with any of these three set commands.
• The Multi-VRF Selection Using Policy-Based Routing feature cannot be configured with IP prefix lists.
• The set global and set vrf commands cannot be simultaneously applied to a route map.
• The Multi-VRF Selection Using Policy-Based Routing feature supports VRF-lite; that is, only IP routing
protocols run on the device. Multiprotocol Label Switching (MPLS) and Virtual Private Networks (VPNs)
cannot be configured. However, the set vrf command will work in MPLS VPN scenarios.
• If you delete one VRF using no vrf definition vrf-name command, then other VRFs in the VRF routing
table are also removed unexpectedly; when ip vrf receive command is configured with receive entries
above 400, and IPv4 and IPv6 routes above 2000. This is applicable only for Cisco ASR 1000 platform.
• In a VRF receive scenario, the memory requirements are proportional to the number of VRF receives
that are configured multiplied by the number of directly connected neighbours (Cisco Express Forwarding
adjacencies). When the ip vrf receive command is configured, Cisco Express Forwarding adjacency
prefixes are copied to the VRF. Network resources might be exhausted based on number of bytes per
each adjacency prefix, number of adjacency prefixes, number of VRF receives configured, and the
platform-specific route processor memory restrictions applicable to Cisco Express Forwarding entries.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
100


Multi-VRF Selection Using Policy-Based Routing
Information About Multi-VRF Selection Using Policy-Based Routing

Information About Multi-VRF Selection Using Policy-Based
Routing
Policy Routing of VPN Traffic Based on Match Criteria
The Multi-VRF Selection Using Policy-Based Routing feature is an extension of the MPLS VPN VRF Selection
Based on a Source IP Address feature. The Multi-VRF Selection Using Policy-Based Routing feature allows
you to policy route Virtual Private Network (VPN) traffic based on match criteria. Match criteria are defined
in an IP access list and/or are based on packet length. The following match criteria are supported in Cisco
software:
• IP access lists—Define match criteria based on IP addresses, IP address ranges, and other IP packet
access list filtering options. Named, numbered, standard, and extended access lists are supported. All IP
access list configuration options in Cisco software can be used to define match criteria.
• Packet lengths—Define match criteria based on the length of a packet, in bytes. The packet length filter
is defined in a route map with the match length route-map configuration command.
Policy routing is defined in the route map. The route map is applied to the incoming interface with the ip
policy route-map interface configuration command. An IP access list is applied to the route map with the
match ip address route-map configuration command. Packet length match criteria are applied to the route
map with the match length route-map configuration command. The set action is defined with the set vrf
route-map configuration command. The match criteria are evaluated, and the appropriate VRF is selected by
the set command. This combination allows you to define match criteria for incoming VPN traffic and policy
route VPN packets out to the appropriate virtual routing and forwarding (VRF) instance.

Policy-Based Routing set Commands
Policy-routing Packets for VRF Instances
To enable policy-routing packets for virtual routing and forwarding (VRF) instances, you can use route map
commands with the following set commands. They are listed in the order in which the device uses them during
the routing of packets.
• set tos—Sets the Type of Service (TOS) bits in the header of an IP packet.
• set df—Sets the Don’t Fragment (DF) bit in the header of an IP packet.
• set vrf—Routes packets through the specified interface. The destination interface can belong only to a
VRF instance.
• set global—Routes packets through the global routing table. This command is useful for routing ingress
packets belonging to a specific VRF through the global routing table.
• set ip vrf next-hop—Indicates where to output IPv4 packets that pass a match criteria of a route map
for policy routing when the IPv4 next hop must be under a specified VRF.
• set ipv6 vrf next-hop—Indicates where to output IPv6 packets that pass a match criteria of a route map
for policy routing when the IPv6 next hop must be under a specified VRF.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
101


Multi-VRF Selection Using Policy-Based Routing
Change of Normal Routing and Forwarding Behavior

• set ip global next-hop—Indicates where to forward IPv4 packets that pass a match criterion of a route
map for policy routing and for which the Cisco software uses the global routing table. The global keyword
explicitly defines that IPv4 next-hops are under the global routing table.
• set ipv6 global next-hop—Indicates where to forward IPv6 packets that pass a match criterion of a route
map for policy routing and for which the Cisco software uses the global routing table. The global keyword
explicitly defines that IPv6 next-hops are under the global routing table.
• set interface—When packets enter a VRF, routes the packets out of the egress interface under the same
VRF according to the set interface policy, provided that the Layer 2 rewrite information is available.
• set ip default vrf—Provides IPv4 inherit-VRF and inter-VRF routing. With inherit-VRF routing, IPv4
packets arriving at a VRF interface are routed by the same outgoing VRF interface. With inter-VRF
routing, IPv4 packets arriving at a VRF interface are routed through any other outgoing VRF interface.
• set ipv6 default vrf—Provides IPv6 inherit-VRF and inter-VRF routing. With inherit-VRF routing, IPv6
packets arriving at a VRF interface are routed by the same outgoing VRF interface. With inter-VRF
routing, IPv6 packets arriving at a VRF interface are routed through any other outgoing VRF interface.
• set ip default global—Provides IPv4 VRF to global routing.
• set ipv6 default global—Provides IPv6 VRF to global routing.
• set default interface—Indicates where to output packets that pass a match criterion of a route map for
policy routing and have no explicit route to the destination. The interface can belong to any VRF.
• set ip default next-hop—Indicates where to output IPv4 packets that pass a match criterion of a route
map for policy routing and for which the Cisco software has no explicit route to a destination.
• set ipv6 default next-hop—Indicates where to IPv6 output packets that pass a match criterion of a route
map for policy routing and for which the Cisco software has no explicit route to a destination.

Change of Normal Routing and Forwarding Behavior
When you configure policy-based routing (PBR), you can use the following six set commands to change
normal routing and forwarding behavior. Configuring any of these set commands, with the potential exception
of the set ip next-hop command, overrides the routing behavior of packets entering the interface if the packets
do not belong to a virtual routing and forwarding (VRF) instance. The packets are routed from the egress
interface across the global routing table.
• set default interface—Indicates where to output packets that pass a match criterion of a route map for
policy routing and have no explicit route to the destination.
• set interface—When packets enter a VRF interface, routes the packets out of the egress interface under
the same VRF according to the set interface policy, provided that the Layer 2 rewrite information is
available.

Note

The interface must be a peer-to-peer (P2P) interface.

• set ip default next-hop—Indicates where to output IPv4 packets that pass a match criterion of a route
map for policy routing and for which the Cisco software has no explicit route to a destination.
• set ipv6 default next-hop—Indicates where to output IPv6 packets that pass a match criterion of a route
map for policy routing and for which the Cisco software has no explicit route to a destination.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
102


Multi-VRF Selection Using Policy-Based Routing
Support of Inherit-VRF Inter-VRF and VRF-to-Global Routing

• set ip next-hop—Indicates where to output IPv4 packets that pass a match criterion of a route map for
policy routing. If an IPv4 packet is received on a VRF interface and is transmitted from another interface
within the same VPN, the VRF context of the incoming packet is inherited from the interface.
• set ipv6 next-hop—Indicates where to output IPv6 packets that pass a match criterion of a route map
for policy routing. If an IPv6 packet is received on a VRF interface and is transmitted from another
interface within the same Virtual Private Network (VPN), the VRF context of the incoming packet is
inherited from the interface.

Support of Inherit-VRF Inter-VRF and VRF-to-Global Routing
The Multi-VRF Selection Using Policy-Based Routing (PBR) feature supports inherit-VRF and inter-VRF.
With inherit-VRF routing, packets arriving at a virtual routing and forwarding (VRF) interface are routed by
the same outgoing VRF interface. With inter-VRF routing, packets arriving at a VRF interface are routed
through any other outgoing VRF interface.
VRF-to-global routing causes packets that enter any VRF interface to be routed through the global routing
table. When a packet arrives on a VRF interface, the destination lookup normally is done only in the
corresponding VRF table. If a packet arrives on a global interface, the destination lookup is done in the global
routing table.
The Multi-VRF Selection Using Policy-Based Routing feature modifies the following set commands to support
inherit-VRF, inter-VRF, and VRF-to-global routing. The commands are listed in the order in which the device
uses them during the routing of packets.
• set global—Routes packets through the global routing table. This command is useful for routing ingress
packets belonging to a specific VRF through the global routing table.
• set ip global next-hop—Indicates where to forward IPv4 packets that pass a match criterion of a route
map for policy routing and for which the Cisco software uses the global routing table.
• set ipv6 global next-hop—Indicates where to forward IPv6 packets that pass a match criterion of a route
map for policy routing and for which the Cisco software uses the global routing table.
• set ip vrf next-hop—Causes the device to look up the IPv4 next hop in the VRF table. If an IPv4 packet
arrives on an interface that belongs to a VRF and the packet needs to be routed through a different VRF,
you can use the set ip vrf next-hop command.
• set ipv6 vrf next-hop—Causes the device to look up the IPv6 next hop in the VRF table. If an IPv6
packet arrives on an interface that belongs to a VRF and the packet needs to be routed through a different
VRF, you can use the set ipv6 vrf next-hop command.
• set ip default vrf—Provides IPv4 inherit-VRF and inter-VRF routing. With IPv4 inherit-VRF routing,
IPv4 packets arriving at a VRF interface are routed by the same outgoing VRF interface. With inter-VRF
routing, IPv4 packets arriving at a VRF interface are routed through any other outgoing VRF interface.
• set ipv6 default vrf—Provides IPv6 inherit-VRF and inter-VRF routing. With IPv6 inherit-VRF routing,
IPv6 packets arriving at a VRF interface are routed by the same outgoing VRF interface. With inter-VRF
routing, IPv6 packets arriving at a VRF interface are routed through any other outgoing VRF interface.
• set interface—When packets enter a VRF, routes the packets out of the egress interface under the same
VRF, according to the set interface policy, provided that the Layer 2 rewrite information is available.
• set default interface—Indicates where to output packets that pass a match criterion of a route map for
policy routing and have no explicit route to the destination. The interface can belong to any VRF.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
103


Multi-VRF Selection Using Policy-Based Routing
How to Configure Multi-VRF Selection Using Policy-Based Routing

• set ip next-hop—Routes IPv4 packets through the global routing table in an IPv4-to-IPv4 routing and
forwarding environment.
• set ipv6 next-hop—Routes IPv6 packets through the global routing table in an IPv6-to-IPv6 routing and
forwarding environment.
• set vrf—Selects the appropriate VRF after a successful match occurs in the route map. VRS-aware PSV
allows only inter-VRF (or VRF-to-VRF) switching.

How to Configure Multi-VRF Selection Using Policy-Based
Routing
DefiningtheMatchCriteriaforMulti-VRFSelectionUsingPolicy-BasedRouting
Define the match criteria for the Multi-VRF Selection using Policy-Based Routing (PBR) feature so that you
can selectively route the packets instead of using their default routing and forwarding.
The match criteria for the Multi-VRF Selection using Policy-Based Routing are defined in an access list.
Standard, named, and extended access lists are supported.
You can define the match criteria based on the packet length by configuring the match length route-map
configuration command. This configuration option is defined entirely within a route map.
The following sections explain how to configure PBR route selection:

Configuring Multi-VRF Selection Using Policy-Based Routing with a Standard Access List
Before you begin
The tasks in the following sections assume that the virtual routing and forwarding (VRF) instance and associated
IP address are already defined.
SUMMARY STEPS
1. enable
2. configure terminal
3. access-list access-list-number {deny | permit} [source source-wildcard] [log]
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
104


Multi-VRF Selection Using Policy-Based Routing
Configuring Multi-VRF Selection Using Policy-Based Routing with a Named Extended Access List

Command or Action

Purpose

Device# configure terminal

Step 3

access-list access-list-number {deny | permit} [source
source-wildcard] [log]
Example:
Device(config)# access-list 40 permit source
10.1.1.0/24 0.0.0.255

Creates an access list and defines the match criteria for the
route map.
• Match criteria can be defined based on IP addresses,
IP address ranges, and other IP packet access list
filtering options. Named, numbered, standard, and
extended access lists are supported. You can use all
IP access list configuration options to define match
criteria.
• The example creates a standard access list numbered
40. This filter permits traffic from any host with an IP
address in the 10.1.1.0/24 subnet.

Configuring Multi-VRF Selection Using Policy-Based Routing with a Named Extended Access List
To configure Multi-VRF Selection using Policy-Based Routing (PBR) with a named extended access list,
complete the following steps.
Before you begin
The tasks in the following sections assume that the virtual routing and forwarding (VRF) instance and associated
IP address are already defined.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
ip access-list {standard | extended} [access-list-name | access-list-number]
[sequence-number] {permit | deny} protocol source source-wildcard destination destination-wildcard
[option option-value] [precedence precedence] [tostos] [ttl operator-vaue] [log] [time-range
time-range-name] [fragments]

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
Device# configure terminal

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
105


Multi-VRF Selection Using Policy-Based Routing
Configuring Multi-VRF Selection in a Route Map

Step 3

Command or Action

Purpose

ip access-list {standard | extended} [access-list-name |
access-list-number]

Specifies the IP access list type and enters the corresponding
access list configuration mode.

Example:

• You can specify a standard, extended, or named access
list.

Device(config)# ip access-list extended NAMEDACL

Step 4

[sequence-number] {permit | deny} protocol source
Defines the criteria for which the access list will permit or
source-wildcard destination destination-wildcard [option deny packets.
option-value] [precedence precedence] [tostos] [ttl
• Match criteria can be defined based on IP addresses,
operator-vaue] [log] [time-range time-range-name]
IP address ranges, and other IP packet access list
[fragments]
filtering options. Named, numbered, standard, and
extended access lists are supported. You can use all
Example:
IP access list configuration options to define match
Device(config-ext-nacl)# permit ip any any option
criteria.
any-options

• The example creates a named access list that permits
any configured IP option.

Configuring Multi-VRF Selection in a Route Map
Incoming packets are filtered through the match criteria that are defined in the route map. After a successful
match occurs, the set command configuration determines the VRF through which the outbound Virtual Private
Network (VPN) packets will be policy routed.
Before you begin
You must define the virtual routing and forwarding (VRF) instance before you configure the route map;
otherwise an error message appears on the console.
A receive entry must be added to the VRF selection table with the ip vrf receive command. If a match and
set operation occurs in the route map but there is no receive entry in the local VRF table, the packet will be
dropped if the packet destination is local.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
named-ordering-route-map enable ]
route-map map-tag [permit | deny] [sequence-number] [
Do one of the following :
• set ip vrf vrf-name next-hop global-ipv4-address [...global-ipv4-address]
• set ipv6 vrf vrf-name next-hop global-ipv6-address [...global-ipv6-address]
• set ip next-hop recursive vrf global-ipv4-address [...global-ipv4-address]
• set ip global next-hop global-ipv4-address [...global-ipv4-address]
• set ipv6 global next-hop global-ipv6-address [...global-ipv6-address]

6. Do one of the following:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
106


Multi-VRF Selection Using Policy-Based Routing
Configuring Multi-VRF Selection in a Route Map

• match ip address {acl-number [acl-name | acl-number]}
• match length minimum-lengthmaximum-length
7. end
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

named-ordering-route-map enable ]
Example:

Enables ordering of route-maps based on a string provided
by the user.

Device(config)# named-ordering-route-map enable

Step 4

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. .
[
Example:
Device(config)# route-map alpha permit ordering-seq

Step 5

Do one of the following :
• set ip vrf vrf-name next-hop global-ipv4-address
[...global-ipv4-address]
• set ipv6 vrf vrf-name next-hop global-ipv6-address
[...global-ipv6-address]
• set ip next-hop recursive vrf global-ipv4-address
[...global-ipv4-address]
• set ip global next-hop global-ipv4-address
[...global-ipv4-address]
• set ipv6 global next-hop global-ipv6-address
[...global-ipv6-address]
Example:

Indicates where to forward packets that pass a match
criterion of a route map for policy routing when the IPv4
next hop must be under a specified VRF.
Indicates where to forward packets that pass a match
criterion of a route map for policy routing when the IPv6
next hop must be under a specified VRF.
Indicates the IPv4 address to which destination or next hop
is used for packets that pass the match criterion configured
in the route map.
Indicates the IPv4 address to forward packets that pass a
match criterion of a route map for policy routing and for
which the software uses the global routing table.
Indicates the IPv6 address to forward packets that pass a

Device(config-route-map)# set ip vrf myvrf next-hop
match criterion of a route map for policy routing and for
10.0.0.0

which the software uses the global routing table.

Example:
Device(config-route-map)# set ipv6 vrf myvrf
next-hop 2001.DB8:4:1::1/64

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
107


Multi-VRF Selection Using Policy-Based Routing
Configuring Multi-VRF Selection Using Policy-Based Routing and IP VRF Receive on the Interface

Command or Action

Purpose

Example:
Device(config-route-map)# set ip next-hop recursive
vrf 10.0.0.0

Example:
Device(config-route-map)# set ip global next-hop
10.0.0.0

Example:
Device(config-route-map)# set ipv6 global next-hop
2001.DB8:4:1::1/64

Step 6

Do one of the following:
• match ip address {acl-number [acl-name |
acl-number]}
• match length minimum-lengthmaximum-length

• The example configures the route map to use standard
access list 1 to define match criteria.

Example:
Device(config-route-map)# match ip address 1
or

Example:
Device(config-route-map)# match length 3 200

Step 7

Distributes any routes that have a destination network
number address that is permitted by a standard or extended
access list, and performs policy routing on matched packets.
IP access lists are supported.

Specifies the Layer 3 packet length in the IP header as a
match criterion in a class map.
• The example configures the route map to match
packets that are 3 to 200 bytes in length.
Returns to privileged EXEC mode.

end
Example:
Device(config-route-map)# end

Configuring Multi-VRF Selection Using Policy-Based Routing and IP VRF
Receive on the Interface
The route map is attached to the incoming interface with the ip policy route-map interface configuration
command.
The source IP address must be added to the virtual routing and forwarding (VRF) selection table. VRF selection
is a one-way (unidirectional) feature. It is applied to the incoming interface. If a match and set operation
occurs in the route map but there is no receive entry in the local VRF table, the packet is dropped if the packet
destination is local.
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number [name-tag]

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
108


Multi-VRF Selection Using Policy-Based Routing
Verifying the Configuration of Multi-VRF Selection Using Policy-Based Routing

4. ip policy route-map map-tag
5. ip vrf receive vrf-name
6. end
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

interface type number [name-tag]

Configures an interface and enters interface configuration
mode.

Example:
Device(config)# interface FastEthernet 0/1/0

Step 4

Identifies a route map to use for policy routing on an
interface.

ip policy route-map map-tag
Example:
Device(config-if)# ip policy route-map map1

Step 5

Adds the IP addresses that are associated with an interface
into the VRF table.

ip vrf receive vrf-name
Example:
Device(config-if)# ip vrf receive VRF-1

Step 6

• The configuration example attaches the route map
named map1 to the interface.

• This command must be configured for each VRF that
will be used for VRF selection.
Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Verifying the Configuration of Multi-VRF Selection Using Policy-Based Routing
To verify the configuration of the Multi-VRF Selection Using Policy-Based Routing (PBR) feature, perform
the following steps. You can enter the commands in any order.
SUMMARY STEPS
1. show ip access-list [access-list-number | access-list-name]
2. show route-map [map-name]

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
109


Multi-VRF Selection Using Policy-Based Routing
Verifying the Configuration of Multi-VRF Selection Using Policy-Based Routing

3. show ip policy
DETAILED STEPS

Step 1

show ip access-list [access-list-number | access-list-name]
Verifies the configuration of match criteria for Multi-VRF Selection Using Policy-Based Routing. The command output
displays three subnet ranges defined as match criteria in three standard access lists:
Example:
Device# show ip access-list
Standard IP access list 40
10 permit 10.1.0.0, wildcard bits 0.0.255.255
Standard IP access list 50
10 permit 10.2.0.0, wildcard bits 0.0.255.255
Standard IP access list 60
10 permit 10.3.0.0, wildcard bits 0.0.255.255

Step 2

show route-map [map-name]
Verifies match and set commands within the route map:
Example:
Device# show route-map

The output displays the match criteria and set action for each route-map sequence. The output also displays the number
of packets and bytes that have been policy routed per each route-map sequence.
Example:
Device# show route-map map1
route-map map1, permit, sequence 10
Match clauses:
Set clauses:
ip next-hop vrf myvrf 10.5.5.5 10.6.6.6 10.7.7.7
ip next-hop global 10.8.8.8 10.9.9.9
Policy routing matches: 0 packets, 0 bytes
Device# show route-map map2
route-map map2, permit, sequence 10
Match clauses:
Set clauses:
vrf myvrf
Policy routing matches: 0 packets, 0 bytes
Device# show route-map map3
route-map map3, permit, sequence 10
Match clauses:
Set clauses:
global
Policy routing matches: 0 packets, 0 bytes

The following show route-map command displays output from the set ip vrf next-hop command:
Example:
Device(config)# route-map test

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
110


Multi-VRF Selection Using Policy-Based Routing
Verifying the Configuration of Multi-VRF Selection Using Policy-Based Routing

Device(config-route-map)# set ip vrf myvrf next-hop
Device(config-route-map)# set ip vrf myvrf next-hop 192.168.3.2
Device(config-route-map)# match ip address 255 101
Device(config-route-map)# end
Device# show route-map
route-map test, permit, sequence 10
Match clauses:
ip address (access-lists): 101
Set clauses:
ip vrf myvrf next-hop 192.168.3.2
Policy routing matches: 0 packets, 0 bytes

The following show route-map command displays output from the set ip global command:
Example:
Device(config)# route-map test
Device(config-route-map)# match ip address 255 101
Device(config-route-map)# set ip global next-hop 192.168.4.2
Device(config-route-map)# end
Device# show route-map
*May 25 13:45:55.551: %SYS-5-CONFIG_I: Configured from console by consoleout-map
route-map test, permit, sequence 10
Match clauses:
ip address (access-lists): 101
Set clauses:
ip global next-hop 192.168.4.2
Policy routing matches: 0 packets, 0 bytes

Step 3

show ip policy
Verifies the Multi-VRF Selection Using Policy-Based Routing policy.
Example:
Device# show ip policy

The following show ip policy command output displays the interface and associated route map that is configured for
policy routing:
Example:
Device# show ip policy
Interface
FastEthernet0/1/0

Route map
PBR-VRF-Selection

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
111


Multi-VRF Selection Using Policy-Based Routing
Configuration Examples for Multi-VRF Selection Using Policy-Based Routing

Configuration Examples for Multi-VRF Selection Using
Policy-Based Routing
Example: Defining the Match Criteria for Multi-VRF Selection Using
Policy-Based Routing
In the following example, three standard access lists are created to define match criteria for three different
subnetworks. Any packets received on FastEthernet interface 0/1/0 will be policy routed through the
PBR-VRF-Selection route map to the virtual routing and forwarding (VRF) that is matched in the same
route-map sequence. If the source IP address of the packet is part of the 10.1.0.0/24 subnet, VRF1 will be
used for routing and forwarding.
access-list 40 permit source 10.1.0.0 0.0.255.255
access-list 50 permit source 10.2.0.0 0.0.255.255
access-list 60 permit source 10.3.0.0 0.0.255.255
route-map PBR-VRF-Selection permit 10
match ip address 40
set vrf VRF1
!
route-map PBR-VRF-Selection permit 20
match ip address 50
set vrf VRF2
!
route-map PBR-VRF-Selection permit 30
match ip address 60
set vrf VRF3
!
interface FastEthernet 0/1/0
ip address 192.168.1.6 255.255.255.252
ip policy route-map PBR-VRF-Selection
ip vrf receive VRF1
ip vrf receive VRF2
ip vrf receive VRF3

Example: Configuring Multi-VRF Selection in a Route Map
The following example shows a set ip vrf next-hop command that applies policy-based routing to the virtual
routing and forwarding (VRF) interface named myvrf and specifies that the IP address of the next hop is
10.0.0.2:
Device(config)# route-map map1 permit
Device(config)# set vrf myvrf
Device(config-route-map)# set ip vrf myvrf next-hop 10.0.0.2
Device(config-route-map)# match ip address 101
Device(config-route-map)# end

The following example shows a set ip global command that specifies that the device should use the next hop
address 10.0.0.1 in the global routing table:
Device(config-route-map)# set ip global next-hop 10.0.0.1

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
112


Multi-VRF Selection Using Policy-Based Routing
Additional References

Additional References
Related Documents
Related Topic

Document Title

MPLS and MPLS applications commands Cisco IOS Multiprotocol Label Switching Command Reference
IP access list commands

Cisco IOS Security Command Reference

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

FeatureInformationforMulti-VRFSelectionUsingPolicy-Based
Routing
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
113


Multi-VRF Selection Using Policy-Based Routing
Glossary

Table 9: Feature Information for Multi-VRF Selection Using Policy-Based Routing

Feature Name

Releases

Feature Information

Multi-VRF Selection Using
Policy-Based Routing (PBR)

12.2(33)SRB1

The Multi-VRF Selection Using
Policy-Based Routing (PBR)
feature allows a specified interface
on a provider edge (PE) router to
route packets to Virtual Private
Networks (VPNs) based on packet
length or match criteria defined in
an IP access list. This feature and
the MPLS VPN VRF Selection
Based on Source IP Address feature
can be configured together on the
same interface

12.2(33)SXH1
12.4(24)T
Cisco IOS XE Release 2.2

In Cisco IOS Release
12.2(33)SRB1, this feature was
introduced.
In Cisco IOS Release
12.2(33)SXH1, support was added.
In Cisco IOS Release 12.4(24)T,
this feature was integrated.
In Cisco IOS XE Release 2.2, this
feature was implemented on the
Cisco ASR 1000 Series
Aggregation Services Routers.
The following commands were
modified: set ip global next-hop
and set ip vrf next-hop.
IPv6 VRF-Aware PBR Next-hop
Enhancement

15.2(2)S
Cisco IOS XE Release 3.6S

In Cisco IOS Release 15.2(2)S, this
feature was introduced.
In Cisco IOS XE Release 3.6S, this
feature was implemented on the
Cisco ASR 1000 Series
Aggregation Services Routers.
The following commands were
introduced: set ipv6 default
next-hop, set ipv6 next-hop (PBR)

Glossary
CE device—customer edge device. A device that is part of a customer network and that interfaces to a provider
edge (PE) device.
Inherit-VRF routing—Packets arriving at a VRF interface are routed by the same outgoing VRF interface.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
114


Multi-VRF Selection Using Policy-Based Routing
Glossary

Inter-VRF routing—Packets arriving at a VRF interface are routed via any other outgoing VRF interface.
IP—Internet Protocol. Network layer protocol in the TCP/IP stack offering a connectionless internetwork
service. IP provides features for addressing, type-of-service specification, fragmentation and reassembly, and
security. Defined in RFC 791.
PBR—policy-based routing. PBR allows a user to manually configure how received packets should be routed.
PE device—provider edge device. A device that is part of a service provider’s network and that is connected
to a CE device. It exchanges routing information with CE devices by using static routing or a routing protocol
such as BGP, RIPv1, or RIPv2.
VPN—Virtual Private Network. A collection of sites sharing a common routing table. A VPN provides a
secure way for customers to share bandwidth over an ISP backbone network.
VRF—A VPN routing and forwarding instance. A VRF consists of an IP routing table, a derived forwarding
table, a set of interfaces that use the forwarding table, and a set of rules and routing protocols that determine
what goes into the forwarding table.
VRF-lite—A feature that enables a service provider to support two or more VPNs, where IP addresses can
be overlapped among the VPNs.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
115


Multi-VRF Selection Using Policy-Based Routing
Glossary

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
116
