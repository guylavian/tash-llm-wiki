---
title: "BGP Next Hop Unchanged"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-next-hop-unchanged
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 42 BGP Next Hop Unchanged In an external BGP (eBGP) session, by default, the router changes the next hop attribute of a BGP route (to its own address) when the router sends out a route. The BGP Next Hop Unchanged feature allows BGP to send an update to an eBGP multihop peer with the next hop attribute unchanged. • Finding Feature Information, on page 689 • Information About Next Hop Unch"
---

# BGP Next Hop Unchanged

CHAPTER

42

BGP Next Hop Unchanged
In an external BGP (eBGP) session, by default, the router changes the next hop attribute of a BGP route (to
its own address) when the router sends out a route. The BGP Next Hop Unchanged feature allows BGP to
send an update to an eBGP multihop peer with the next hop attribute unchanged.
• Finding Feature Information, on page 689
• Information About Next Hop Unchanged, on page 689
• How to Configure BGP Next Hop Unchanged, on page 690
• Configuration Example for BGP Next Hop Unchanged, on page 693
• Additional References, on page 693
• Feature Information for BGP Next Hop Unchanged, on page 694

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About Next Hop Unchanged
BGP Next Hop Unchanged
In an external BGP (eBGP) session, by default, the router changes the next hop attribute of a BGP route (to
its own address) when the router sends out a route. If the BGP Next Hop Unchanged feature is configured,
BGP will send routes to an eBGP multihop peer without modifying the next hop attribute. The next hop
attribute is unchanged.

IP Routing: BGP Configuration Guide
689


BGP Next Hop Unchanged
How to Configure BGP Next Hop Unchanged

Note

There is an exception to the default behavior of the router changing the next hop attribute of a BGP route
when the router sends out a route. When the next hop is in the same subnet as the peering address of the eBGP
peer, the next hop is not modified. This is referred to as third party next-hop.
The BGP Next Hop Unchanged feature provides flexibility when designing and migrating networks. It can
be used only between eBGP peers configured as multihop. It can be used in a variety of scenarios between
two autonomous systems. One scenario is when multiple autonomous systems are connected that share the
same IGP, or at least the routers have another way to reach each other’s next hops (which is why the next hop
can remain unchanged).
A common use of this feature is to configure Multiprotocol Label Switching (MPLS) inter-AS with multihop
MP-eBGP for VPNv4 between RRs.
Another common use of this feature is a VPNv4 inter-AS Option C configuration, as defined in RFC4364,
Section 10. In this configuration, VPNv4 routes are passed among autonomous systems between RR of
different autonomous systems. The RRs are several hops apart, and have neighbor next-hop unchanged
configured. PEs of different autonomous systems establish an LSP between them (via a common IGP or by
advertising the next-hops--that lead to the PEs--via labeled routes among the ASBRs--routes from different
autonomous systems separated by one hop). PEs are able to reach the next hops of the PEs in another AS via
the LSPs, and can therefore install the VPNv4 routes in the VRF RIB.
Restriction
The BGP Next Hop Unchanged feature can be configured only between multihop eBGP peers. The following
error message will be displayed if you try to configure this feature for a directly connected neighbor:
%BGP: Can propagate the nexthop only to multi-hop EBGP neighbor

How to Configure BGP Next Hop Unchanged
Configuring the BGP Next Hop Unchanged for an eBGP Peer
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
address-family {ipv4 | ipv6 | l2vpn | nsap | rtfilter | vpnv4 | vpnv6}
neighbor ip-address remote-as as-number
neighbor ip-address activate
neighbor ip-address ebgp-multihop ttl
neighbor ip-address next-hop-unchanged
end
show ip bgp

IP Routing: BGP Configuration Guide
690


BGP Next Hop Unchanged
Configuring the BGP Next Hop Unchanged for an eBGP Peer

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router bgp as-number
Example:

Enters router configuration mode, and creates a BGP
routing process.

Router(config)# router bgp 65535

Step 4

address-family {ipv4 | ipv6 | l2vpn | nsap | rtfilter |
vpnv4 | vpnv6}

Enters address family configuration mode to configure
BGP peers to accept address family specific configurations.

Example:
Router(config-router-af)# address-family vpnv4

Step 5

neighbor ip-address remote-as as-number

Adds an entry to the BGP neighbor table.

Example:
Router(config-router-af)# neighbor 10.0.0.100
remote-as 65600

Step 6

neighbor ip-address activate

Enables the exchange of information with the peer.

Example:
Router(config-router-af)# neighbor 10.0.0.100
activate

Step 7

neighbor ip-address ebgp-multihop ttl
Example:

Configures the local router to accept and initiate
connections to external peers that reside on networks that
are not directly connected.

Router(config-router-af)# neighbor 10.0.0.100
ebgp-multihop 255

Step 8

neighbor ip-address next-hop-unchanged
Example:

Configures the router to send BGP updates to the specified
eBGP peer without modifying the next hop attribute.

Router(config-router-af)# neighbor 10.0.0.100
next-hop-unchanged

IP Routing: BGP Configuration Guide
691


BGP Next Hop Unchanged
Configuring BGP Next Hop Unchanged using Route-Maps

Step 9

Command or Action

Purpose

end

Exits address family configuration mode, and enters
privileged EXEC mode.

Example:
Router(config-router-af)# end

Step 10

show ip bgp

(Optional) Displays entries in the BGP routing table.

Example:
Router# show ip bgp

• The output will indicate if the neighbor
next-hop-unchanged command has been configured
for the selected address.

Configuring BGP Next Hop Unchanged using Route-Maps
Configuring outbound route-map for eBGP neighbor
To define the route-map and apply outbound policy for neighbor, use set ip next-hop unchanged command.
In the following configuration the next-hop for prefix 1.1.1.1 is not changed while sending to the eBGP
neighbor 15.1.1.2:
enable
config terminal
router bgp 2
bgp log-neighbor-changes
neighbor 15.1.1.2 remote-as 3
neighbor 15.1.1.2 ebgp-multihop 10
!
address-family ipv4
neighbor 15.1.1.2 activate
neighbor 15.1.1.2 route-map A out
exit address-family
!
route-map A permit 10
match ip address 1
set ip next-hop unchanged
!
access-list 1 permit 1.1.1.1
end

Configuring next-hop unchanged for both iBGP and eBGP path prefixes while sending to eBGP neighbor
To configure next-hop unchanged for both iBGP and eBGP path prefixes while sending to eBGP neighbor,
use next-hop-unchanged allpaths command.

Note

From Cisco IOS XE Denali 16.3 release, thenext-hop-unchanged allpaths command supports IPv4 and IPv6
address families along with VPNv4 and VPNv6 address families.
In the following configuration the next-hop is not changed for both iBGP and eBGP path prefixes while
sending to eBGP neighbor 15.1.1.2:

IP Routing: BGP Configuration Guide
692


BGP Next Hop Unchanged
Configuration Example for BGP Next Hop Unchanged

enable
config terminal
router bgp 2
bgp log-neighbor-changes
neighbor 15.1.1.2 remote-as 3
neighbor 15.1.1.2 ebgp-multihop 10
!
address-family ipv4
neighbor 15.1.1.2 activate
neighbor 15.1.1.2 next-hop-unchanged allpaths
exit address-family
!
end

Configuration Example for BGP Next Hop Unchanged
Example: BGP Next Hop Unchanged for an eBGP Peer
The following example configures a multihop eBGP peer at 10.0.0.100 in a remote AS. When the local router
sends updates to that peer, it will send them without modifying the next hop attribute.
router bgp 65535
address-family ipv4
neighbor 10.0.0.100 remote-as 65600
neighbor 10.0.0.100 activate
neighbor 10.0.0.100 ebgp-multihop 255
neighbor 10.0.0.100 next-hop-unchanged
end

Note

All address families, such as IPv4, IPv6, VPNv4, VPNv6, L2VPN, and so on support the next-hop unchanged
command. However, for the address family L2VPN BGP VPLS signaling, you must use the next-hop self
command for its proper functioning.

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

BGP Outbound Route Map on Route Reflector “Configuring Internal BGP Features” in the IP Routing:
to Set IP Next Hop for iBGP Peer
BGP Configuration Guide

IP Routing: BGP Configuration Guide
693


BGP Next Hop Unchanged
Feature Information for BGP Next Hop Unchanged

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

Feature Information for BGP Next Hop Unchanged
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 58: Feature Information for BGP Next Hop Unchanged

Feature Name

Releases

Feature Information

BGP Next Hop Unchanged

Cisco IOS XE
Release 2.1

The BGP Next Hop Unchanged feature allows BGP to
send an update to an eBGP multihop peer with the next
hop attribute unchanged.
The following command was added by this feature:
neighbor next-hop-unchanged.

set ip next-hop
Cisco IOS XE
unchanged/next-hop-unchanged Denali 16.3.1
allpaths IPv4/IPv6

In Cisco IOS XE Denali 16.3 release, the set ip next-hop
unchanged/next-hop-unchanged allpaths IPv4/IPv6 feature
extends the support for BGP Next Hop Unchanged to IPv4
and IPv6 allpaths.
The set ip next-hop unchanged/next-hop-unchanged
allpaths IPv4/IPv6 feature adds two new knobs to support
BGP Next Hop Unchanged. The 'set ip next-hop
unchanged' knob was added under the route-map and
'next-hop-unchanged allpaths' was added under the
neighbor.
The following command was modified by this feature:
set ip next-hop unchanged.

IP Routing: BGP Configuration Guide
694
