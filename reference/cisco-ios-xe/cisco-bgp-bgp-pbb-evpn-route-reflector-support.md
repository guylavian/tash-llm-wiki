---
title: "BGP PBB EVPN Route Reflector Support"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-pbb-evpn-route-reflector-support
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 78 BGP PBB EVPN Route Reflector Support The BGP PBB EVPN Route Reflector Support feature provides Boarder Gateway Protocol (BGP) route reflector functionality for Ethernet VPN (EVPN) and provider backbone bridging (PBB) EVPN of Layer 2 VPN address family. EVPN enables customer MAC addresses as routable addresses and distributes them in BGP to avoid any data plane MAC address learning ove"
---

# BGP PBB EVPN Route Reflector Support

CHAPTER

78

BGP PBB EVPN Route Reflector Support
The BGP PBB EVPN Route Reflector Support feature provides Boarder Gateway Protocol (BGP) route
reflector functionality for Ethernet VPN (EVPN) and provider backbone bridging (PBB) EVPN of Layer 2
VPN address family. EVPN enables customer MAC addresses as routable addresses and distributes them in
BGP to avoid any data plane MAC address learning over the Multiprotocol Label Switching (MPLS) core
network. The route reflector is enhanced to store the received EVPN updates without configuring EVPN
explicitly on the route reflector and then advertises these updates to other provider edge (PE) devices so that
the PEs do not need to have a full mesh of BGP sessions.
• Finding Feature Information, on page 1077
• Prerequisites for BGP PBB EVPN Route Reflector Support, on page 1077
• Information About BGP PBB EVPN Route Reflector Support , on page 1078
• How to Configure BGP PBB EVPN Route Reflector Support , on page 1079
• Configuration Examples for BGP PBB EVPN Route Reflector Support , on page 1080
• Additional References for BGP PBB EVPN Route Reflector Support, on page 1081
• Feature Information for BGP PBB EVPN Route Reflector Support , on page 1081

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP PBB EVPN Route Reflector Support
• Before you configure the BGP PBB EVPN Route Reflector Support feature, you must configure the RT
filter unicast address family type to support for EVPN address family. For more information, see the
"Configuring BGP: RT Constrained Route Distribution" module in the IP Routing: BGP Configuration
Guide.
• The EVPN Subsequent Address Family Identifier (SAFI) needs to be enabled globally before you enable
it under the BGP neighbor.

IP Routing: BGP Configuration Guide
1077


BGP PBB EVPN Route Reflector Support
Information About BGP PBB EVPN Route Reflector Support

Information About BGP PBB EVPN Route Reflector Support
EVPN Overview
Ethernet VPN (EVPN) allows Multiprotocol Label Switching (MPLS) networks to provide multipoint Layer
2 VPN (L2VPN) services.
In EVPN, the customer MAC addresses are learned in the data plane over links connecting customer devices
(CE) to the provider edge (PE) devices. The MAC addresses are then distributed over the Multiprotocol Label
Switching (MPLS) core network using Boarder Gateway Protocol (BGP) with an MPLS label identifying the
service instance. A single MPLS label per EVPN instance is sufficient as long as the receiving PE device
performs a MAC lookup in the disposition path. Receiving PE devices inject these routable MAC addresses
into their Layer 2 routing information base (RIB) and forwarding information base (FIB) along with their
associated adjacencies.
EVPN defines a BGP Network Layer Reachability Information (NLRI) that advertises different route types
and route attributes. The EVPN NLRI is carried in BGP using BGP multiprotocol extensions with an Address
Family Identifier (AFI) and a Subsequent Address Family Identifier (SAFI). BGP drops unsupported route
types and does not propagate them to neighbors.

BGP EVPN Autodiscovery Support on Route Reflector
By default, routes received from an internal BGP (iBGP) peer are not sent to another iBGP peer unless a full
mesh configuration is formed between all Boarder Gateway Protocol (BGP) devices within an autonomous
system (AS). Configuring a route reflector allows a device to advertise or reflect the iBGP learned routes to
other iBGP speakers.
Ethernet VPN (EVPN) Autodiscovery supports BGP route reflectors. A BGP route reflector can be used to
reflect BGP EVPN prefixes without EVPN being explicitly configured on the route reflector. The route
reflector does not participate in autodiscovery; that is, no pseudowires are set up between the route reflector
and the provider edge (PE) devices. A route reflector reflects EVPN prefixes to other PE devices so that these
PE devices do not need to have a full mesh of BGP sessions. The network administrator configures only the
BGP EVPN address family on a route reflector.
BGP uses the Layer 2 VPN (L2VPN) routing information base (RIB) to store endpoint provisioning information,
which is updated each time any Layer 2 virtual forwarding instance (VFI) is configured. The prefix and path
information is stored in the L2VPN database, which allows BGP to make decisions about the best path. When
BGP distributes the endpoint provisioning information in an update message to all its BGP neighbors, this
endpoint information is used to configure a pseudowire mesh to support L2VPN-based services.

EVPN Address Family
BGP supports Layer 2 VPN (L2VPN) EVPN address family under router configuration mode to carry L2VPN
EVPN autodiscovery and signaling Network Layer Reachability Information (NLRI) to Boarder Gateway
Protocol (BGP) neighbors. This address family is allowed on both internal BGP (iBGP) and external BGP
(eBGP) neighbors under default virtual routing and forwarding (VRF) for both IPv4 and IPv6 neighbors. The
EVPN SAFI is not supported under VRF and VRF neighbors.

IP Routing: BGP Configuration Guide
1078


BGP PBB EVPN Route Reflector Support
How to Configure BGP PBB EVPN Route Reflector Support

How to Configure BGP PBB EVPN Route Reflector Support
Configuring BGP PBB EVPN Route Reflector
Perform this task on the Boarder Gateway Protocol (BGP) route reflector to configure the device as a BGP
route reflector and configure the specified neighbor as its client and to display the information from the BGP
routing table.
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
router bgp as-number
address-family l2vpn [vpls | evpn]
neighbor {ip-address | peer-group-name} activate
neighbor {ip-address | ipv6-address | peer-group-name} route-reflector-client
end
show bgp l2vpn evpn all
debug bgp l2vpn evpn updates
clear bgp l2vpn evpn

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

router bgp as-number
Example:

Configures a BGP routing process and enters router
configuration mode.

Device(config)# router bgp 1

Step 4

address-family l2vpn [vpls | evpn]

Step 5

neighbor {ip-address | peer-group-name} activate

Specifies the L2VPN address family and enters address
family configuration mode. The optional evpn keyword
Example:
specifies that EVPN endpoint provisioning information is
Device(config-router)# address-family l2vpn evpn to be distributed to BGP peers.
Enables PBB EVPN with the specified BGP neighbor.

Example:
Device(config-router-af)# neighbor 10.0.0.2
activate

IP Routing: BGP Configuration Guide
1079


BGP PBB EVPN Route Reflector Support
Configuration Examples for BGP PBB EVPN Route Reflector Support

Command or Action
Step 6

Purpose

neighbor {ip-address | ipv6-address | peer-group-name} Configures the local device as the BGP route reflector and
the specified neighbor as one of its clients.
route-reflector-client
Example:
Device(config-router-af)# neighbor 10.0.0.2
route-reflector-client

Step 7

end
Example:

Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

Step 8

show bgp l2vpn evpn all

(Optional) Displays the complete L2VPN EVPN database.

Example:
Device# show bgp l2vpn evpn all

Step 9

debug bgp l2vpn evpn updates

(Optional) Specifies debugging messages for BGP update.

Example:
Device# debug bgp l2vpn evpn updates events

Step 10

clear bgp l2vpn evpn
Example:

(Optional) Specifies that all current BGP sessions will be
reset.

Device# clear bgp l2vpn evpn *

Configuration Examples for BGP PBB EVPN Route Reflector
Support
Example: Configuring BGP PBB EVPN Route Reflector
In the following example, the local device is a route reflector. It passes learned iBGP routes to the neighbor
at 10.0.0.2:
Device# configure terminal
Device(config)# router bgp 1
Device(config-router)# address-family l2vpn evpn
Device(config-router-af)# neighbor 10.0.0.2 activate
Device(config-router-af)# neighbor 10.0.0.2 route-reflector-client
Device(config-router-af)# exit address-family

In the following example, the show bgp l2vpn evpn all route-type 1 command displays the Ethernet
autodiscovery route information:
show bgp l2vpn evpn all route-type 1
BGP routing table entry for
[1][100.100.100.100:11111][AAAABBBBCCCCDDDDEEEE][23456789][101234]/25, version 2
Paths: (1 available, best #1, table EVPN-BGP-Table)
Advertised to update-groups:
1
2
3

IP Routing: BGP Configuration Guide
1080


BGP PBB EVPN Route Reflector Support
Additional References for BGP PBB EVPN Route Reflector Support

Refresh Epoch 1
Local, (Received from a RR-client)
19.0.101.1 from 19.0.101.1 (19.0.101.1)
Origin IGP, localpref 100, valid, internal, best
Extended Community: RT:100:101 EVPN LABEL:0x1:Label-101234
rx pathid: 0, tx pathid: 0x0

Additional References for BGP PBB EVPN Route Reflector
Support
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

Standards and RFCs
Standard/RFC Title
RFC 4456

BGP Route Reflection: An Alternative to Full Mesh Internal BGP (IBGP)

RFC 4684

Constrained Route Distribution for Border Gateway Protocol/MultiProtocol Label Switching
(BGP/MPLS) Internet Protocol (IP) Virtual Private Networks (VPNs)

Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.

http://www.cisco.com/support

To receive security and technical information about your products, you can
subscribe to various services, such as the Product Alert Tool (accessed from
Field Notices), the Cisco Technical Services Newsletter, and Really Simple
Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com user
ID and password.

Feature Information for BGP PBB EVPN Route Reflector Support
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.

IP Routing: BGP Configuration Guide
1081


BGP PBB EVPN Route Reflector Support
Feature Information for BGP PBB EVPN Route Reflector Support

Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 98: Feature Information for BGP PBB EVPN Route Reflector Support

Feature Name

Releases

Feature Information

BGP PBB EVPN
Route Reflector
Support

Cisco IOS XE The BGP PBB EVPN Route Reflector Support feature provides Boarder
Release 3.11S Gateway Protocol (BGP) route reflector functionality for Ethernet VPN
(EVPN) and provider backbone bridging (PBB) EVPN of Layer 2 VPN
address family. EVPN enables customer MAC addresses as routable
addresses and distributes them in BGP to avoid any data plane MAC
address learning over the Multiprotocol Label Switching (MPLS) core
network. The route reflector is enhanced to store the received EVPN
updates without configuring EVPN explicitly on the route reflector and
then advertises these updates to other provider edge (PE) devices so
that the PEs do not need to have a full mesh of BGP sessions.
The following command was modified: address-family l2vpn.

IP Routing: BGP Configuration Guide
1082
