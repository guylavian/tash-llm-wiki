---
title: "IPv6 Routing: Multiprotocol BGP Link-Local Address Peering"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-ipv6-routing-multiprotocol-bgp-link-local-address-peering
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 8 IPv6 Routing: Multiprotocol BGP Link-Local Address Peering • Finding Feature Information, on page 197 • Information About IPv6 Routing: Multiprotocol BGP Link-Local Address Peering, on page 197 • How to Configure IPv6 Routing: Multiprotocol BGP Link-Local Address Peering, on page 198 • Configuration Examples for IPv6 Routing: Multiprotocol BGP Link-Local Address Peering, on page 201 •"
---

# IPv6 Routing: Multiprotocol BGP Link-Local Address Peering

CHAPTER

8

IPv6 Routing: Multiprotocol BGP Link-Local
Address Peering
• Finding Feature Information, on page 197
• Information About IPv6 Routing: Multiprotocol BGP Link-Local Address Peering, on page 197
• How to Configure IPv6 Routing: Multiprotocol BGP Link-Local Address Peering, on page 198
• Configuration Examples for IPv6 Routing: Multiprotocol BGP Link-Local Address Peering, on page 201
• Additional References, on page 202
• Feature Information for IPv6 Routing Multiprotocol BGP Link-Local Address Peering, on page 203

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About IPv6 Routing: Multiprotocol BGP Link-Local
Address Peering
IPv6 Multiprotocol BGP Peering Using a Link-Local Address
The IPv6 multiprotocol BGP can be configured between two IPv6 devices (peers) using link-local addresses.
For this function to work, you must identify the interface for the neighbor by using the neighbor update-source
command, and you must configure a route map to set an IPv6 global next hop.
Boarder Gateway Protocol (BGP) uses third-party next hops for peering with multiple peers over IPv6 link-local
addresses on the same interface. Peering over link-local addresses on different interfaces cannot use third
party next hops. The neighbors peering using link-local addresses are split into one update group per interface.
BGP splits update group membership for neighbors with link-local addresses based on the interface used to
communicate with that neighbor.

IP Routing: BGP Configuration Guide
197


IPv6 Routing: Multiprotocol BGP Link-Local Address Peering
How to Configure IPv6 Routing: Multiprotocol BGP Link-Local Address Peering

How to Configure IPv6 Routing: Multiprotocol BGP Link-Local
Address Peering
Configuring an IPv6 Multiprotocol BGP Peer Using a Link-Local Address
Configuring IPv6 multiprotocol BGP between two IPv6 routers (peers) using link-local addresses requires
that the interface for the neighbor be identified by using the update-source command and that a route map
be configured to set an IPv6 global next hop.

Note

• By default, neighbors that are defined using the neighbor remote-as command in router configuration
mode exchange only IPv4 unicast address prefixes. To exchange other address prefix types, such as IPv6
prefixes, neighbors must also be activated using the neighbor activate command in address family
configuration mode for the other prefix types, as shown for IPv6 prefixes.
• By default, route maps that are applied in router configuration mode using the neighbor route-map
command are applied to only IPv4 unicast address prefixes. Route maps for other address families must
be applied in address family configuration mode using the neighbor route-map command, as shown
for the IPv6 address family. The route maps are applied either as the inbound or outbound routing policy
for neighbors under the specified address family. Configuring separate route maps under each address
family type simplifies managing complicated or different policies for each address family.
• The route-map used to modify the next hop needs to be applied outbound only. Inbound route-map to
modify next-hop ipv6 address is not supported. Inbound route-map is supported only for IPV4 address
family.

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
11.
12.
13.

enable
configure terminal
router bgp autonomous-system-number
neighbor {ip-address | ipv6-address[%] | peer-group-name} remote-as autonomous-system-number
[alternate-as autonomous-system-number ...]
neighbor {ip-address | ipv6-address[%] | peer-group-name} update-source interface-type
interface-number
address-family ipv6 [vrf vrf-name] [unicast | multicast | vpnv6
neighbor {ip-address | peer-group-name | ipv6-address %} activate
neighbor {ip-address | peer-group-name | ipv6-address[%]} route-map map-name {in | out
exit
Repeat Step 9.
route-map map-tag [permit | deny] [sequence-number]
match ipv6 address {prefix-list prefix-list-name | access-list-name
set ipv6 next-hop ipv6-address [link-local-address] [peer-address

IP Routing: BGP Configuration Guide
198


IPv6 Routing: Multiprotocol BGP Link-Local Address Peering
Configuring an IPv6 Multiprotocol BGP Peer Using a Link-Local Address

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

Step 3

router bgp autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 65000

Step 4

Adds the link-local IPv6 address of the neighbor in the
neighbor {ip-address | ipv6-address[%] |
peer-group-name} remote-as autonomous-system-number specified remote autonomous system to the IPv6
multiprotocol BGP neighbor table of the local router.
[alternate-as autonomous-system-number ...]
Example:
Device(config-router)# neighbor
FE80::1234:BFF:FE0E:A471% remote-as 64600

Step 5

neighbor {ip-address | ipv6-address[%] |
peer-group-name} update-source interface-type
interface-number
Example:
Device(config-router)# neighbor
FE80::1234:BFF:FE0E:A471% update-source
gigabitethernet0/0/0

Step 6

• The optional % keyword is the IPv6 link-local
address identifier. This keyword needs to be added
whenever a link-local IPv6 address is used outside
the context of its interface.
Specifies the link-local address over which the peering is
to occur.
• The optional % keyword is the IPv6 link-local
address identifier. This keyword needs to be added
whenever a link-local IPv6 address is used outside
the context of its interface.
• If there are multiple connections to the neighbor and
you do not specify the neighbor interface by using
the interface-type and interface-numberarguments in
the neighbor update-source command, a TCP
connection cannot be established with the neighbor
using link-local addresses.

address-family ipv6 [vrf vrf-name] [unicast | multicast Specifies the IPv6 address family, and enters address
family configuration mode.
| vpnv6
Example:
Device(config-router)# address-family ipv6

• The unicast keyword specifies the IPv6 unicast
address family. By default, the router is placed in
configuration mode for the IPv6 unicast address
family if the unicast keyword is not specified with
the address-family ipv6 command.

IP Routing: BGP Configuration Guide
199


IPv6 Routing: Multiprotocol BGP Link-Local Address Peering
Configuring an IPv6 Multiprotocol BGP Peer Using a Link-Local Address

Command or Action

Purpose
• The multicast keyword specifies IPv6 multicast
address prefixes.

Step 7

neighbor {ip-address | peer-group-name | ipv6-address
%} activate
Example:
Device(config-router-af)# neighbor
FE80::1234:BFF:FE0E:A471% activate

Step 8

neighbor {ip-address | peer-group-name |
ipv6-address[%]} route-map map-name {in | out
Example:
Device(config-router-af)# neighbor
FE80::1234:BFF:FE0E:A471% route-map nh6 out

Step 9

exit
Example:

Enables the neighbor to exchange prefixes for the IPv6
address family with the local router using the specified
link-local addresses.
• The optional % keyword is the IPv6 link-local
address identifier. This keyword needs to be added
whenever a link-local IPv6 address is used outside
the context of its interface.
Applies a route map to incoming or outgoing routes.
• The optional % keyword is the IPv6 link-local
address identifier. This keyword needs to be added
whenever a link-local IPv6 address is used outside
the context of its interface.
Exits address family configuration mode, and returns the
device to router configuration mode.

Device(config-router-af)# exit

Step 10

Repeat Step 9.
Example:

Exits router configuration mode, and returns the device to
global configuration mode.

Device(config-router)# exit

Step 11

route-map map-tag [permit | deny] [sequence-number] Defines a route map and enters route-map configuration
mode.
Example:
Device(config)# route-map nh6 permit 10

Step 12

match ipv6 address {prefix-list prefix-list-name |
access-list-name
Example:

Distributes any routes that have a destination IPv6 network
number address permitted by a prefix list, or performs
policy routing on packets.

Device(config-route-map)# match ipv6 address
prefix-list cisco

Step 13

set ipv6 next-hop ipv6-address [link-local-address]
[peer-address
Example:
Device(config-route-map)# set ipv6 next-hop
2001:DB8::1

IP Routing: BGP Configuration Guide
200

Overrides the next hop advertised to the peer for IPv6
packets that pass a match clause of a route map for policy
routing.
• The ipv6-address argument specifies the IPv6 global
address of the next hop. It need not be an adjacent
router.


IPv6 Routing: Multiprotocol BGP Link-Local Address Peering
Configuration Examples for IPv6 Routing: Multiprotocol BGP Link-Local Address Peering

Command or Action

Purpose
• The link-local-addressargument specifies the IPv6
link-local address of the next hop. It must be an
adjacent router.
Note

The route map sets the IPv6 next-hop addresses
(global and link-local) in BGP updates. If the
route map is not configured, the next-hop
address in the BGP updates defaults to the
unspecified IPv6 address (::), which is rejected
by the peer. If you specify only the global IPv6
next-hop address (the ipv6-address argument)
with the set ipv6 next-hopcommand after
specifying the neighbor interface (the
interface-type argument) with the neighbor
update-source command in Step 5, the
link-local address of the interface specified with
the interface-type argument is included as the
next-hop in the BGP updates. Therefore, only
one route map that sets the global IPv6 next-hop
address in BGP updates is required for multiple
BGP peers that use link-local addresses.

Configuration Examples for IPv6 Routing: Multiprotocol BGP
Link-Local Address Peering
Example: Configuring an IPv6 Multiprotocol BGP Peer Using a Link-Local
Address
The following example configures the IPv6 multiprotocol BGP peer FE80::1234:BFF:FE0E:A471 over
Gigabitethernet interface 0/0 and sets the route map named nh6 to include the IPv6 next-hop global address
of Gigabitethernet interface 0/0 in BGP updates. The IPv6 next-hop link-local address can be set by the nh6
route map (not shown in the following example) or from the interface specified by the neighbor update-source
command (as shown in this example).
Device> enable
Device# configure terminal
Device(config)# router bgp 5
Device(config-router)# neighbor internal peer-group
Device(config-router)# neighbor FE80::1234:BFF:FE0E:A471% peer-group
Device(config-router)# neighbor internal remote-as 100
Device(config-router)# neighbor FE80::1234:BFF:FE0E:A471% remote-as 64600
Device(config-router)# neighbor FE80::1234:BFF:FE0E:A471% update-source Gigabitethernet 0/0
Device(config-router)# address-family ipv6
Device(config-router-af)# neighbor FE80::1234:BFF:FE0E:A471% activate
Device(config-router-af)# neighbor FE80::1234:BFF:FE0E:A471% route-map nh6 out
Device(config-router-af)# exit

IP Routing: BGP Configuration Guide
201


IPv6 Routing: Multiprotocol BGP Link-Local Address Peering
Additional References

Device(config-router)# exit
Device(config)# route-map nh6permit 10
Device(config-router-map)# match ipv6 address prefix-list cisco
Device(config-router-map)# set ipv6 next-hop 2001:DB8:526::1
Device(config-router-map)# exit
Device(config)# ipv6 prefix-list cisco permit 2001:DB8:2F22::/48 le 128
Device(config)# ipv6 prefix-list cisco deny ::/0
Device(config)# end

Note

If you specify only the global IPv6 next-hop address (the ipv6-address argument) with the set ipv6 next-hop
command after specifying the neighbor interface (the interface-type argument) with the neighbor update-source
command, the link-local address of the interface specified with the interface-type argument is included as the
next hop in the BGP updates. Therefore, only one route map that sets the global IPv6 next-hop address in
BGP updates is required for multiple BGP peers that use link-local addresses.

Additional References
Related Documents
Related Topic

Document Title

IPv6 addressing and connectivity

IPv6 Configuration Guide

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

IPv6 commands

Cisco IOS IPv6 Command
Reference

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

Standards and RFCs
Standard/RFC Title
RFCs for
IPv6

IPv6
RFCs

MIBs
MIB MIBs Link
—

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: BGP Configuration Guide
202


IPv6 Routing: Multiprotocol BGP Link-Local Address Peering
Feature Information for IPv6 Routing Multiprotocol BGP Link-Local Address Peering

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

Feature Information for IPv6 Routing Multiprotocol BGP
Link-Local Address Peering
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 20: Feature Information for IPv6 Routing: Multiprotocol BGP Link-Local Address Peering

Feature Name

Releases

Feature Information

IPv6 Routing: Multiprotocol BGP Cisco IOS XE Release 2.1
Link-Local Address Peering

This feature is supported.

IP Routing: BGP Configuration Guide
203


IPv6 Routing: Multiprotocol BGP Link-Local Address Peering
Feature Information for IPv6 Routing Multiprotocol BGP Link-Local Address Peering

IP Routing: BGP Configuration Guide
204
