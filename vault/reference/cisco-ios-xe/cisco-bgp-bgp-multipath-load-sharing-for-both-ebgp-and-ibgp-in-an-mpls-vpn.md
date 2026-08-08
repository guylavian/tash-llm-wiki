---
title: "BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-multipath-load-sharing-for-both-ebgp-and-ibgp-in-an-mpls-vpn
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 33 BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN The BGP Multipath Load Sharing for both eBGP and iBGP in an MPLS-VPN feature allows you to configure multipath load balancing with both external BGP (eBGP) and internal BGP (iBGP) paths in Border Gateway Protocol (BGP) networks that are configured to use Multiprotocol Label Switching (MPLS) Virtual Private Networks (VPNs"
---

# BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN

CHAPTER

33

BGP Multipath Load Sharing for Both eBGP and
iBGP in an MPLS-VPN
The BGP Multipath Load Sharing for both eBGP and iBGP in an MPLS-VPN feature allows you to configure
multipath load balancing with both external BGP (eBGP) and internal BGP (iBGP) paths in Border Gateway
Protocol (BGP) networks that are configured to use Multiprotocol Label Switching (MPLS) Virtual Private
Networks (VPNs). This feature provides improved load balancing deployment and service offering capabilities
and is useful for multihomed autonomous systems and Provider Edge (PE) routers that import both eBGP and
iBGP paths from multihomed and stub networks.
• Finding Feature Information, on page 575
• Prerequisites for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN, on page 576
• Restrictions for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN, on page 576
• Information About BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN, on page
576
• HOw to COnfigure BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN, on page
578
• Configuration Examples for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN,
on page 580
• Where to Go Next, on page 582
• Additional References, on page 582
• Feature Information for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN, on
page 583

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
575


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
Prerequisites for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN

Prerequisites for BGP Multipath Load Sharing for Both eBGP
and iBGP in an MPLS-VPN
Load Balancing is Configured Under CEF
Cisco Express Forwarding (CEF) or distributed CEF (dCEF) must be enabled on all participating routers.

Restrictions for BGP Multipath Load Sharing for Both eBGP and
iBGP in an MPLS-VPN
Address Family Support
This feature is configured on a per VPN routing and forwarding instance (VRF) basis. This feature can be
configured under only the IPv4 VRF address family.
Memory Consumption Restriction
Each BGP multipath routing table entry will use additional memory. We recommend that you do not use this
feature on a router with a low amount of available memory and especially if router is carries full Internet
routing tables.
Route Reflector Limitation
When multiple iBGP paths installed in a routing table, a route reflector will advertise only one paths (next
hop). If a router is behind a route reflector, all routers that are connected to multihomed sites will not be
advertised unless a different route distinguisher is configured for each VRF.

Information About BGP Multipath Load Sharing for Both eBGP
and iBGP in an MPLS-VPN
Multipath Load Sharing Between eBGP and iBGP
A BGP routing process will install a single path as the best path in the routing information base (RIB) by
default. The maximum-paths command allows you to configure BGP to install multiple paths in the RIB for
multipath load sharing. BGP uses the best path algorithm to still select a single multipath as the best path and
advertise the best path to BGP peers.

Note

The number of paths of multipaths that can be configured is documented on the maximum-paths command
reference page.

IP Routing: BGP Configuration Guide
576


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
eBGP and iBGP Multipath Load Sharing in a BGP MPLS Network

Load balancing over the multipaths is performed by CEF. CEF load balancing is configured on a per-packet
round robin or on a per session (source and destination pair) basis. For information about CEF, refer to the
"Cisco Express Forwarding Overview" documentation:
The BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS VPN feature is enabled only under
the IPv4 VRF address family configuration mode. When enabled, this feature can perform load balancing on
eBGP and/or iBGP paths that are imported into the VRF. The number of multipaths is configured on a per
VRF basis. Separate VRF multipath configurations are isolated by unique route distinguisher.

Note

The BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS VPN feature operates within the
parameters of configured outbound routing policy.

eBGP and iBGP Multipath Load Sharing in a BGP MPLS Network
The figure below shows a service provider BGP MPLS network that connects two remote networks to PE
router 1 and PE router 2. PE router 1 and PE router 2 are both configured for VPNv4 unicast iBGP peering.
Network 2 is a multihomed network that is connected to PE router 1 and PE router 2. Network 2 also has
extranet VPN services configured with Network 1. Both Network 1 and Network 2 are configured for eBGP
peering with the PE routers.
Figure 57: A Service Provider BGP MPLS Network

PE router 1 can be configured with the BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS
VPN feature so that both iBGP and eBGP paths can be selected as multipaths and imported into the VRF of
Network 1. The multipaths will be used by CEF to perform load balancing. IP traffic that is sent from Network
2 to PE router 1 and PE router 2 will be sent across the eBGP paths as IP traffic. IP traffic that is sent across
the iBGP path will be sent as MPLS traffic, and MPLS traffic that is sent across an eBGP path will be sent
as IP traffic. Any prefix that is advertised from Network 2 will be received by PE router 1 through route
distinguisher (RD) 21 and RD 22.The advertisement through RD 21 will be carried in IP packets, and the
advertisement through RD 22 will be carried in MPLS packets. Both paths can be selected as multipaths for
VRF1 and installed into the VRF1 RIB.

IP Routing: BGP Configuration Guide
577


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
eBGP and iBGP Multipath Load Sharing With Route Reflectors

eBGP and iBGP Multipath Load Sharing With Route Reflectors
The figure below shows a topology that contains three PE routers and a route reflector, all configured for
iBGP peering. PE router 2 and PE router 3 each advertise an equal preference eBGP path to PE router 1. By
default, the route reflector will choose only one path and advertise PE router 1.
Figure 58: A Topology with a Route Reflector

For all equal preference paths to PE router 1 to be advertised through the route reflector, you must configure
each VRF with a different RD. The prefixes received by the route reflector will be recognized differently and
advertised to PE router 1.

Benefits of Multipath Load Sharing for Both eBGP and iBGP
The BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS VPN feature allows multihomed
autonomous systems and PE routers to be configured to distribute traffic across both eBGP and iBGP paths.

HOw to COnfigure BGP Multipath Load Sharing for Both eBGP
and iBGP in an MPLS-VPN
Configuring Multipath Load Sharing for Both eBGP and iBGP
To configure this feature, perform the steps in this section.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 vrf vrf-name
maximum-paths eibgp number

IP Routing: BGP Configuration Guide
578


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
Verifying Multipath Load Sharing for Both eBGP an iBGP

6. end
DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged EXEC
mode.

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

Enters router configuration mode to create or configure a
BGP routing process.

Device(config)# router bgp 40000

Step 4

address-family ipv4 vrf vrf-name
Example:

Places the router in address family configuration mode.
• Separate VRF multipath configurations are isolated
by unique route distinguisher.

Device(config-router)# address-family ipv4 vrf RED

Step 5

maximum-paths eibgp number
Example:

Configures the number of parallel iBGP and eBGP routes
that can be installed into a routing table.
Note

Device(config-router-af)# maximum-paths eibgp 6

Step 6

The maximum-paths eibgp command can be
configured only under the IPv4 VRF address
family configuration mode and cannot be
configured in any other address family
configuration mode.

Exits address family configuration mode, and enters
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Verifying Multipath Load Sharing for Both eBGP an iBGP
SUMMARY STEPS
1. enable
2. show ip bgp neighbors [neighbor-address [advertised-routes | dampened-routes | flap-statistics |
paths [regexp] | received prefix-filter | received-routes | routes]]
3. show ip bgp vpnv4 {all | rd route-distinguisher | vrf vrf-name}

IP Routing: BGP Configuration Guide
579


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
Configuration Examples for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN

4. show ip route vrf vrf-name
DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged EXEC
mode.

Example:

• Enter your password if prompted.
Device> enable

Step 2

show ip bgp neighbors [neighbor-address
[advertised-routes | dampened-routes | flap-statistics |
paths [regexp] | received prefix-filter | received-routes |
routes]]

Displays information about the TCP and BGP connections
to neighbors.

Example:
Device# show ip bgp neighbors

Step 3

show ip bgp vpnv4 {all | rd route-distinguisher | vrf
vrf-name}
Example:

Displays VPN address information from the BGP table.
This command is used to verify that the VRF has been
received by BGP.

Device# show ip bgp vpnv4 vrf RED

Step 4

show ip route vrf vrf-name
Example:

Displays the IP routing table associated with a VRF
instance. The show ip route vrf command is used to verify
that the VRF is in the routing table.

Device# show ip route vrf RED

Configuration Examples for BGP Multipath Load Sharing for
Both eBGP and iBGP in an MPLS-VPN
Example: Configuring eBGP and iBGP Multipath Load Sharing
This following configuration example configures a router in address-family mode to select six BGP routes
(eBGP or iBGP) as multipaths:
Device(config)# router bgp 40000
Device(config-router)# address-family ipv4 vrf RED
Device(config-router-af)# maximum-paths eibgp 6
Device(config-router-af)# end

IP Routing: BGP Configuration Guide
580


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
Example: Verifying eBGP and iBGP Multipath Load Sharing

Example: Verifying eBGP and iBGP Multipath Load Sharing
To verify that iBGP and eBGP routes have been configured for load sharing, use the show ip bgp vpnv4
EXEC command or the show ip route vrf EXEC command.
In the following example, the show ip bgp vpnv4 command is entered to display multipaths installed in the
VPNv4 RIB:
Device# show ip bgp vpnv4 all 10.22.22.0
BGP routing table entry for 10:1:22.22.22.0/24, version 19
Paths:(5 available, best #5)
Multipath:eiBGP
Advertised to non peer-group peers:
10.0.0.2 10.0.0.3 10.0.0.4 10.0.0.5
22
10.0.0.2 (metric 20) from 10.0.0.4 (10.0.0.4)
Origin IGP, metric 0, localpref 100, valid, internal, multipath
Extended Community:0x0:0:0 RT:100:1 0x0:0:0
Originator:10.0.0.2, Cluster list:10.0.0.4
22
10.0.0.2 (metric 20) from 10.0.0.5 (10.0.0.5)
Origin IGP, metric 0, localpref 100, valid, internal, multipath
Extended Community:0x0:0:0 RT:100:1 0x0:0:0
Originator:10.0.0.2, Cluster list:10.0.0.5
22
10.0.0.2 (metric 20) from 10.0.0.2 (10.0.0.2)
Origin IGP, metric 0, localpref 100, valid, internal, multipath
Extended Community:RT:100:1 0x0:0:0
22
10.0.0.2 (metric 20) from 10.0.0.3 (10.0.0.3)
Origin IGP, metric 0, localpref 100, valid, internal, multipath
Extended Community:0x0:0:0 RT:100:1 0x0:0:0
Originator:10.0.0.2, Cluster list:10.0.0.3
22
10.1.1.12 from 10.1.1.12 (10.22.22.12)
Origin IGP, metric 0, localpref 100, valid, external, multipath, best
Extended Community:RT:100:1

In the following example, the show ip route vrf command is entered to display multipath routes in the VRF
table:
Device# show ip route vrf PATH 10.22.22.0
Routing entry for 10.22.22.0/24
Known via "bgp 1", distance 20, metric 0
Tag 22, type external
Last update from 10.1.1.12 01:59:31 ago
Routing Descriptor Blocks:
* 10.0.0.2 (Default-IP-Routing-Table), from 10.0.0.4, 01:59:31 ago
Route metric is 0, traffic share count is 1
AS Hops 1
10.0.0.2 (Default-IP-Routing-Table), from 10.0.0.5, 01:59:31 ago
Route metric is 0, traffic share count is 1
AS Hops 1
10.0.0.2 (Default-IP-Routing-Table), from 10.0.0.2, 01:59:31 ago
Route metric is 0, traffic share count is 1
AS Hops 1
10.0.0.2 (Default-IP-Routing-Table), from 10.0.0.3, 01:59:31 ago
Route metric is 0, traffic share count is 1
AS Hops 1

IP Routing: BGP Configuration Guide
581


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
Where to Go Next

10.1.1.12, from 10.1.1.12, 01:59:31 ago
Route metric is 0, traffic share count is 1
AS Hops 1

Where to Go Next
For information about advertising the bandwidth of an autonomous system exit link as an extended community,
refer to the “BGP Link Bandwidth” module.

Additional References
Related Documents
Related Topic

Document Title

BGP commands: complete command syntax,
command mode, command history, defaults, usage
guidelines, and examples

Cisco IOS IP Routing: BGP Command Reference

Comprehensive BGP link bandwidth configuration
examples and tasks

“BGP Link Bandwidth” module in the IP Routing:
BGP Configuration Guide

CEF configuration tasks

“CEF Overview” module in the IP Switching Cisco
Express Forwarding Configuration Guide

Standards
Standards

Title

No new or modified standards are supported by this feature, and support for existing standards has not —
been modified by this feature.
MIBs
MIBs

MIBs Link

No new or modified MIBs are supported To obtain lists of supported MIBs by platform and Cisco IOS
by this feature, and support for existing release, and to download MIB modules, go to the Cisco MIB
MIBs has not been modified by this
website on Cisco.com at the following URL:
feature.
http://www.cisco.com/public/sw-center/netmgmt/cmtk/mibs.shtml
RFCs
RFCs

Title

RFC 1771 A Border Gateway Protocol 4 (BGP4)
RFC 2547 BGP/MPLS VPNs

IP Routing: BGP Configuration Guide
582


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
Feature Information for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN

RFCs

Title

RFC 2858 Multiprotocol Extensions for BGP-4
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

Feature Information for BGP Multipath Load Sharing for Both
eBGP and iBGP in an MPLS-VPN
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 49: Feature Information for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN

Feature Name

Releases

Feature Information

BGP Multipath Load Sharing for Both Cisco IOS XE Release
eBGP and iBGP in an MPLS-VPN
2.1

This feature was introduced on the Cisco
ASR 1000 Series Aggregation Services
Routers.

IP Routing: BGP Configuration Guide
583


BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN
Feature Information for BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN

IP Routing: BGP Configuration Guide
584
