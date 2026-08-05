---
title: "BGP-RTC for Legacy PE"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-rtc-for-legacy-pe
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 77 BGP-RTC for Legacy PE The BGP-Route Target Constrain (RTC) for Legacy PE feature helps to prevent the propagation of VPN Network Layer Reachability Information (NLRI) to a provider edge (PE) device that is not interested in the VPN. This feature builds an outbound filter used by a Boarder Gateway Protocol (BGP) speaker to decide which routes to pass to its peer and propagates route ta"
---

# BGP-RTC for Legacy PE

CHAPTER

77

BGP-RTC for Legacy PE
The BGP-Route Target Constrain (RTC) for Legacy PE feature helps to prevent the propagation of VPN
Network Layer Reachability Information (NLRI) to a provider edge (PE) device that is not interested in the
VPN. This feature builds an outbound filter used by a Boarder Gateway Protocol (BGP) speaker to decide
which routes to pass to its peer and propagates route target (RT) reachability information between internal
BGP (iBGP) meshes.
• Finding Feature Information, on page 1071
• Prerequisites for BGP-RTC for Legacy PE, on page 1071
• Information About BGP-RTC for Legacy PE, on page 1072
• How to Configure BGP-RTC for Legacy PE, on page 1072
• Configuration Examples for BGP-RTC for Legacy PE, on page 1074
• Additional References for BGP-RTC for Legacy PE, on page 1075
• Feature Information for BGP-RTC for Legacy PE, on page 1076

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP-RTC for Legacy PE
Before you configure the BGP-RTC for Legacy PE feature, you must configure the RT filter unicast address
family type. For more information, see "Configuring BGP: RT Constrained Route Distribution" module in
the IP Routing: BGP Configuration Guide.

IP Routing: BGP Configuration Guide
1071


BGP-RTC for Legacy PE
Information About BGP-RTC for Legacy PE

Information About BGP-RTC for Legacy PE
Overview of BGP-RTC for Legacy PE
The BGP—RTC for Legacy PE feature makes use of VPN unicast route exchange from the legacy provider
edge (PE) devices to a new Boarder Gateway Protocol (BGP) speaker (route reflector [RR]) to signal route
target (RT) membership. The legacy PEs announce a set of special routes with mapped RTs to the RR along
with a standard community. The presence of the community triggers the RR to extract the RTs and build RT
membership information.
In scenarios where VPN membership is normal, this functionality helps reduce the scaling requirements on
the PE devices and the RRs. The PE devices need not to spend resources for filtering out unwanted routes.
The BGP peers that have common outbound policies are grouped under a single format group. Separate
replication groups are used within a format group to separate BGP peers with its own peer-based policies.
The Route Target Constrain (RTC)-capable peers are placed in separate format groups. Each RTC peers have
a separate replication group. When legacy RT is configured for a peer, then it must be treated the same way
as the RTC peer except that there is no capability negotiation.

Legacy PE Support-PE Behavior
Each legacy Route Target Constrain (RTC) speaking neighbor is assigned a separate replication group. BGP
checks the VPN table for any route with a reserved community value and uses it to create RTC network from
the VPN prefix received from a legacy RTC peer with community values. The PE device uses the existing
VPN advertisement mechanism to convey route target (RT) membership from the legacy provider edge (PE)
devices. The route reflector (RR) processes advertisement mechanisms of RT membership information from
legacy PE devices. RRs translate the legacy PE RT membership information to equivalent RTC Network
Layer Reachability Information (NLRIs) to propagate to other RRs.

Legacy PE Support-RR Behavior
Route reflectors (RR) identify routes from legacy provider edge (PE) devices for retrieving route target (RT)
membership information by the community value and filter VPN routes to legacy PE devices. RRs use the
existing VPN advertisement mechanism to convey and process RT membership from the legacy PEs. The
legacy PE RT membership information is translated into equivalent RT membership Network Layer Reachability
Information (NLRI) from the client to propagate to other RRs. The RR then creates the route target filter list
for each legacy client by collecting the entire set of route targets.

How to Configure BGP-RTC for Legacy PE
Configuring BGP-RTC for Legacy PE
SUMMARY STEPS
1.
2.

enable
configure terminal

IP Routing: BGP Configuration Guide
1072


BGP-RTC for Legacy PE
Configuring BGP-RTC for Legacy PE

3.
4.
5.
6.
7.
8.
9.
10.
11.

router bgp as-number
address-family {vpnv4 | vpnv6 } unicast
neighbor {ip-address | peer-group-name | ipv6-address} accept-route-legacy-rt
address-family rtfilter
end
show ip bgp vpnv4 all update-group update-group
show ip bgp vpnv4 all neighbors {ip-address | ipv6-address}
show ip bgp vpnv4 all peer-group
debug ip bgp all updates in

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

Configures a Boarder Gateway Protocol (BGP) routing
process and enters router configuration mode.

Device(config)# router bgp 1

Step 4

address-family {vpnv4 | vpnv6 } unicast
Example:

Specifies the VPNv4 or VPNv6 address family and enters
address family configuration mode.

Device(config-router)# address-family vpnv4
unicast

Step 5

neighbor {ip-address | peer-group-name | ipv6-address} Configures the neighbor on the route reflector (RR) to treat
the provider edge (PE) device as a legacy PE for the route
accept-route-legacy-rt
target (RT) and accepts VPN routes tagged with the special
Example:
community.
Device(config-router-af)# neighbor 10.0.0.1
accept-route-legacy-rt

Step 6

address-family rtfilter

Specifies the RT filter address family type.

Example:
Device(config-router-af)# address-family rtfilter

Step 7

end
Example:

Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

Step 8

show ip bgp vpnv4 all update-group update-group
Example:

(Optional) Displays the information about neighbors in
the update group.

IP Routing: BGP Configuration Guide
1073


BGP-RTC for Legacy PE
Configuration Examples for BGP-RTC for Legacy PE

Command or Action

Purpose

Device# show ip bgp vpnv4 all update-group 2

Step 9

show ip bgp vpnv4 all neighbors {ip-address |
ipv6-address}

(Optional) Displays information about the BGP VPNv4
neighbor.

Example:
Device# show ip bgp vpnv4 all neighbors
192.168.3.3

Step 10

show ip bgp vpnv4 all peer-group

(Optional) Displays information about the peer groups.

Example:
Device# show ip bgp vpnv4

Step 11

all peer-group

debug ip bgp all updates in

(Optional) Displays BGP update messages.

Example:
Device# debug ip bgp all updates in

Configuration Examples for BGP-RTC for Legacy PE
Example: BGP-RTC for Legacy PE
Configuration on the Route Reflector
The following example shows how to configure the neighbor on the route reflector (RR) to treat the provider
edge (PE) device as a legacy PE for the route target (RT) and accept VPN routes tagged with the special
community:
Device# configure terminal
Device(config)# router bgp 1
Device(config-router)# address-family vpnv4 unicast
Device(config-router-af)# neighbor 10.1.1.1 accept-route-legacy-rt
Device(config-router-af)# address-family rtfilter
Device(config-router-af)# exit address-family

Configuration on the Legacy PE
The following example shows how to create a route filter VRF and attach an export map that collects and
carries all RTs locally configured on Layer 3 VPN virtual routing and forwarding (VRF):
ip vrf route-filter
rd 55:1111
export map SET_RT
route-map SET_RT permit 10
match ip address prefix-list RT_NET1
set community 4294901762 (0xFFFF0002)
set extcommunity rt 255.220.0.0:12241 255.220.0.0:12242 additive
set extcommunity rt 255.220.0.0:12243 255.220.0.0:12244 additive
set extcommunity rt 255.220.0.0:12245 255.220.0.0:12246 additive
set extcommunity rt 255.220.0.0:12247 255.220.0.0:12248 additive
set extcommunity rt 255.220.0.0:12249 255.220.0.0:12250 additive

IP Routing: BGP Configuration Guide
1074


BGP-RTC for Legacy PE
Additional References for BGP-RTC for Legacy PE

!
route-map SET_RT permit 20
match ip address prefix-list RT_NET2
set community 4294901762 (0xFFFF0002)
set extcommunity rt 255.220.0.0:12251 255.220.0.0:12252 additive
set extcommunity rt 255.220.0.0:12253 255.220.0.0:12254 additive
set extcommunity rt 255.220.0.0:12255 additive
!
ip route vrf route-filter 5.5.5.5 255.255.255.255 Null0 – (matching prefix-set RT_NET1)
ip route vrf route-filter 6.6.6.6 255.255.255.255 Null0 –(matching prefix-set RT_NET2)
route-map LEG_PE permit 10
match ip address prefix-list RT_NET1 RT_NET2
set community no-advertise additive

The following example shows how to apply the route map to a VPNv4 neighbor:
router bgp 55
address-family vpnv4 unicast
neighbor x.x.x.x route-map LEG_PE out

The following example shows how to source a static route into a Boarder Gateway Protocol (BGP) network
using a network statement:
router bgp 55
address-family ipv4 vrf route-filter
network 5.5.5.5 mask 255.255.255.255
network 6.6.6.6 mask 255.255.255.255

Additional References for BGP-RTC for Legacy PE
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

Configuring BGP: RT Constrained Route
Distribution

"Configuring BGP: RT Constrained Route Distribution" module
in the IP Routing: BGP Configuration Guide

Standards and RFCs
Standard/RFC Title
RFC 4684

Constrained Route Distribution for Border Gateway Protocol/MultiProtocol Label Switching
(BGP/MPLS) Internet Protocol (IP) Virtual Private Networks (VPNs)

IP Routing: BGP Configuration Guide
1075


BGP-RTC for Legacy PE
Feature Information for BGP-RTC for Legacy PE

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

Feature Information for BGP-RTC for Legacy PE
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 97: Feature Information for BGP-RTC for Legacy PE

Feature Name

Releases

Feature Information

BGP-RTC for
Legacy PE

Cisco IOS XE
Release 3.11S

The BGP-RTC for Legacy PE feature helps to prevent the
propagation of VPN Network Layer Reachability Information (NLRI)
to a provider edge (PE) device that is not interested in the VPN. This
feature builds an outbound filter used by a Boarder Gateway Protocol
(BGP) speaker to decide which routes to pass to its peer and
propagates route target (RT) reachability information between
internal BGP (iBGP) meshes.
The neighbor accept-route-legacy-rt command was introduced.

IP Routing: BGP Configuration Guide
1076
