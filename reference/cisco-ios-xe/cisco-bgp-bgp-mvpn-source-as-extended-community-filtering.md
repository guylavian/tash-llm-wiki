---
title: "BGP MVPN Source-AS Extended Community Filtering"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-mvpn-source-as-extended-community-filtering
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 83 BGP MVPN Source-AS Extended Community Filtering The BGP MVPN Source-AS Extended Community Filtering feature enables the provider edge (PE) device to suppress attaching the multicast VPN (MVPN)-related extended communities to routes learned from a customer edge (CE) device or redistributed in a virtual routing and forwarding (VRF) instance for a specified neighbor. • Finding Feature In"
---

# BGP MVPN Source-AS Extended Community Filtering

CHAPTER

83

BGP MVPN Source-AS Extended Community
Filtering
The BGP MVPN Source-AS Extended Community Filtering feature enables the provider edge (PE) device
to suppress attaching the multicast VPN (MVPN)-related extended communities to routes learned from a
customer edge (CE) device or redistributed in a virtual routing and forwarding (VRF) instance for a specified
neighbor.
• Finding Feature Information, on page 1135
• Information About BGP MVPN Source-AS Extended Community Filtering, on page 1135
• How to Configure BGP MVPN Source-AS Extended Community Filtering, on page 1136
• Configuration Examples for BGP MVPN Source-AS Extended Community Filtering, on page 1137
• Additional References for BGP MVPN Source-AS Extended Community Filtering, on page 1138
• Feature Information for BGP MVPN Source-AS Extended Community Filtering, on page 1138

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP MVPN Source-AS Extended Community
Filtering
Overview of BGP MVPN Source-AS Extended Community Filtering
VPN routes carry special extended communities (source autonomous system [AS] extended community and
virtual routing and forwarding [VRF] route import extended community) to support multicast VPN (MVPN).
Legacy provider edge (PE) devices interpret the source AS extended community as old style multicast
distribution tree (MDT). You can attach the extended communities when the prefix is created. After the BGP

IP Routing: BGP Configuration Guide
1135


BGP MVPN Source-AS Extended Community Filtering
How to Configure BGP MVPN Source-AS Extended Community Filtering

MVPN Source-AS Extended Community Filtering feature is enabled, this allows the PE device to suppress
these extended communities. You can use this functionality to suppress extended communities from being
sent for Subsequent Address Family Identifier (SAFI) 128 routes and instead use SAFI 129. Devices with
SAFI 129 must be able to identify the source AS extended community correctly.

How to Configure BGP MVPN Source-AS Extended Community
Filtering
Configuring BGP MVPN Source-AS Extended Community Filtering
SUMMARY STEPS
1.
2.
3.
4.
5.
6.

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 vrf vrf-name
unicast-reachability [source-as | vrf-route-import] [disable]
end

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

Device(config)# router bgp 45000

Step 4

address-family ipv4 vrf vrf-name
Example:
Device(config-router)# address-family ipv4 vrf vpn1

IP Routing: BGP Configuration Guide
1136

Specifies the IPv4 address family and enters address family
configuration mode.
• Use the vrf keyword and vrf-name argument to specify
the name of the VRF instance to associate with
subsequent IPv4 address family configuration mode
commands.


BGP MVPN Source-AS Extended Community Filtering
Configuration Examples for BGP MVPN Source-AS Extended Community Filtering

Step 5

Command or Action

Purpose

unicast-reachability [source-as | vrf-route-import]
[disable]

Disables advertising extended communities for non-MVPN
profiles.

Example:
Device(config-router-af)# unicast-reachability
source-as disable

Step 6

Exits address family configuration mode and enters
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuration Examples for BGP MVPN Source-AS Extended
Community Filtering
Example: Configuring BGP MVPN Source-AS Extended Community Filtering
The following example configures BGP MVPN source-AS extended community filtering:
Device# configure terminal
Device(config)# router bgp 45000
Device(config)# address-family ipv4 vrf vpn1
Device(config-router-af)# unicast-reachability source-as disable
Device(config-router-af)# exit

The following example shows summary output for the show ip bgp vpnv4 vrf vpn1 command.
Device# show ip bgp vpnv4 vrf vpn1
BGP routing table entry for 10:10:1.1.1.1/32, version 25
Paths: (2 available, best #2, table red)
Multipath: eiBGP
Advertised to update-groups:
1
Refresh Epoch 1
Local, imported path from 10:11:1.1.1.1/32 (global)
1.1.1.2 (metric 11) (via default) from 1.1.1.5 (1.1.1.5)
Origin incomplete, metric 11, localpref 100, valid, internal
Extended Community: RT:1:1 OSPF DOMAIN ID:0x0005:0x000000C80200
MVPN AS:55:0.0.0.0 MVPN VRF:1.1.1.2:2 OSPF RT:0.0.0.0:2:0
OSPF ROUTER ID:10.10.20.2:0
Originator: 1.1.1.2, Cluster list: 1.1.1.5
Connector Attribute: count=1
type 1 len 12 value 10:11:1.1.1.2
mpls labels in/out 20/21
rx pathid: 0, tx pathid: 0
Refresh Epoch 1
Local
10.10.10.100 (via vrf red) from 0.0.0.0 (1.1.1.1)
Origin incomplete, metric 11, localpref 100, weight 32768, valid, sourced, best
Extended Community: RT:1:1 OSPF DOMAIN ID:0x0005:0x000000C80200
MVPN VRF:1.1.1.1:1 OSPF RT:0.0.0.0:2:0 OSPF ROUTER ID:10.10.10.1:0

IP Routing: BGP Configuration Guide
1137


BGP MVPN Source-AS Extended Community Filtering
Additional References for BGP MVPN Source-AS Extended Community Filtering

mpls labels in/out 20/nolabel
rx pathid: 0, tx pathid: 0x0

Additional References for BGP MVPN Source-AS Extended
Community Filtering
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

BGP concepts and tasks IP Routing: BGP Configuration Guide
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

Feature Information for BGP MVPN Source-AS Extended
Community Filtering
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
1138


BGP MVPN Source-AS Extended Community Filtering
Feature Information for BGP MVPN Source-AS Extended Community Filtering

Table 103: Feature Information for BGP MVPN Source-AS Extended Community Filtering

Feature Name

Releases

BGP MVPN Source-AS Cisco IOS XE
Extended Community
Release 3.13S
Filtering

Feature Information
The BGP MVPN Source-AS Extended Community Filtering
feature enables the provider edge (PE) device to suppress
attaching the multicast VPN (MVPN)-related extended
communities to routes learned from a customer edge (CE)
device or redistributed in a virtual routing and forwarding
(VRF) instance for a specified neighbor.
The following command was introduced or modified:
unicast-reachability.

IP Routing: BGP Configuration Guide
1139


BGP MVPN Source-AS Extended Community Filtering
Feature Information for BGP MVPN Source-AS Extended Community Filtering

IP Routing: BGP Configuration Guide
1140
