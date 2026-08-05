---
title: "BGP-MVPN SAFI 129 IPv6"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-mvpn-safi-129-ipv6
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 61 BGP-MVPN SAFI 129 IPv6 Subsequent Address Family Identifier (SAFI) 129, known as VPN Multicast SAFI, provides the capability to support multicast routing in the service provider's core IPv6 network. Border Gateway Protocol (BGP) Multicast Virtual Private Network (MVPN) provides a means for service providers to use different encapsulation methods (generic routing encapsulation [GRE], M"
---

# BGP-MVPN SAFI 129 IPv6

CHAPTER

61

BGP-MVPN SAFI 129 IPv6
Subsequent Address Family Identifier (SAFI) 129, known as VPN Multicast SAFI, provides the capability
to support multicast routing in the service provider's core IPv6 network.
Border Gateway Protocol (BGP) Multicast Virtual Private Network (MVPN) provides a means for service
providers to use different encapsulation methods (generic routing encapsulation [GRE], Multicast Label
Distribution Protocol [MLDP], and ingress replication) for forwarding MVPN multicast data traffic in the
service provider network.
The BGP-MVPN SAFI 129 IPv6 feature is required to support BGP-based MVPNs.
• Finding Feature Information, on page 925
• Prerequisites for BGP-MVPN SAFI 129 IPv6, on page 925
• Information About BGP-MVPN SAFI 129 IPv6, on page 926
• How to Configure BGP-MVPN SAFI 129 IPv6, on page 926
• Configuration Examples for BGP-MVPN SAFI 129 IPv6, on page 929
• Additional References, on page 932
• Feature Information for BGP-MVPN SAFI 129 IPv6, on page 932

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP-MVPN SAFI 129 IPv6
• Before you configure a SAFI 129 IPv6-related address family, the ipv6 unicast-routing command must
be configured on the device.
• To create a multicast IPv6 VRF address family under BGP, IPv6 must first be activated on the VRF
itself.

IP Routing: BGP Configuration Guide
925


BGP-MVPN SAFI 129 IPv6
Information About BGP-MVPN SAFI 129 IPv6

Note

There is no separate multicast configuration on the VRF. Configuring the
address-family ipv6 command on the VRF will enable both unicast and multicast
topologies.

• If you want prefixes to be installed into the Routing Information Base (RIB), you must configure the
pim command on a VRF interface.

Information About BGP-MVPN SAFI 129 IPv6
Overview of BGP-MVPN SAFI 129 IPv6
MVPN utilizes the existing VPN infrastructure to allow multicast traffic to pass through the provider space.
Information derived from VPN routes is one of the components needed to set up tunnels within the core.
Currently, multicast traffic will derive this information from the unicast VPNv6 tables, which forces multicast
traffic to be dependent on unicast topologies.
For scenarios in which multicast and unicast traffic would be better suited with separate topologies, the
customer edge (CE) router may advertise a special set of routes to be used exclusively for multicast VPNs.
Multicast routes learned from the CE router can be propagated to remote provider edge (PE) routers via SAFI
129. Multicast routes learned from the CE router or multicast VPN routes learned from remote PE routers
can now be installed directly into the multicast RIB, instead of using replicated routes from the unicast RIB.
Maintaining separate routes and entries for unicast and multicast allows you to create differing topologies for
each service within the core.

How to Configure BGP-MVPN SAFI 129 IPv6
Configuring BGP-MVPN SAFI 129 IPv6
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

enable
configure terminal
vrf definition vrf1
rd route-distinguisher
route-target export route-target-ext-community
route-target import route-target-ext-community
address-family ipv6
mdt default group-address
exit
exit
router bgp autonomous-system-number
address-family vpnv6 multicast

IP Routing: BGP Configuration Guide
926


BGP-MVPN SAFI 129 IPv6
Configuring BGP-MVPN SAFI 129 IPv6

13.
14.
15.
16.

neighbor peer-group-name send-community extended
neighbor {ip-address | peer-group-name | ipv6-address %} activate
address-family ipv6 multicast vrf vrf-name
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

vrf definition vrf1
Example:

Defines a VRF instance and enters VRF configuration
mode.

Device(config)# vrf definition vrf1

Step 4

rd route-distinguisher

Specifies a route distinguisher (RD) for a VRF instance.

Example:
Device(config-vrf)# rd 1:1

Step 5

route-target export route-target-ext-community
Example:

Creates a route target export extended community for a
VRF instance.

Device(config-vrf)# route-target export 1:1

Step 6

route-target import route-target-ext-community
Example:

Creates a route target import extended community for a
VRF instance.

Device(config-vrf)# route-target import 1:1

Step 7

address-family ipv6
Example:

Configures a routing session using IPv6 address prefixes
and enters address family configuration mode.

Device(config-vrf)# address-family ipv6

Step 8

mdt default group-address
Example:

Configures a default multicast distribution tree (MDT)
group for a VRF instance.

Device(config-vrf-af)# mdt default 239.0.0.1

IP Routing: BGP Configuration Guide
927


BGP-MVPN SAFI 129 IPv6
Configuring BGP-MVPN SAFI 129 IPv6

Step 9

Command or Action

Purpose

exit

Exits address family configuration mode and enters VRF
configuration mode.

Example:
Device(config-vrf-af)# exit

Step 10

exit
Example:

Exits VRF configuration mode and enters global
configuration mode.

Device(config-vrf)# exit

Step 11

router bgp autonomous-system-number
Example:

Configures a BGP routing process and enters router
configuration mode.

Device(config)# router bgp 50000

Step 12

address-family vpnv6 multicast
Example:

Configures a routing session using VPN Version 6
multicast address prefixes and enters address family
configuration mode.

Device(config-router)# address-family vpnv6
multicast

Step 13

neighbor peer-group-name send-community extended Specifies that a communities attribute should be sent to a
BGP neighbor.
Example:
Device(config-router-af)# neighbor client1
send-community extended

Step 14

neighbor {ip-address | peer-group-name | ipv6-address
%} activate

Enables the neighbor to exchange prefixes for the specified
family type with the neighbor and the local router.

Example:
Router(config-router-af)# neighbor
2001:DB8:0:CC00::1 % activate

Step 15

address-family ipv6 multicast vrf vrf-name
Example:

Configures a routing session using IPv6 multicast address
prefixes for a VRF instance.

Device(config-router-af)# address-family ipv6
multicast vrf vrf1

Step 16

end
Example:
Device(config-router-af)# end

IP Routing: BGP Configuration Guide
928

Exits address family configuration mode and returns to
privileged EXEC mode.


BGP-MVPN SAFI 129 IPv6
Configuration Examples for BGP-MVPN SAFI 129 IPv6

Configuration Examples for BGP-MVPN SAFI 129 IPv6
Example: Configuring BGP-MVPN SAFI 129 IPv6
The example below shows the configuration for a PE router:
hostname PE1
!
!
vrf definition blue
rd 55:1111
route-target export 55:1111
route-target import 55:1111
!
address-family ipv6
mdt default 232.1.1.1
mdt data 232.1.200.0 0.0.0.0
exit-address-family
!
!ip multicast-routing
ip multicast-routing vrf blue
ip cef
!
ipv6 unicast-routing
ipv6 multicast-routing
ipv6 multicast-routing vrf blue
ipv6 cef
!
!interface Loopback0
ip address 205.1.0.1 255.255.255.255
ip pim sparse-dense-mode
ipv6 address FE80::205:1:1 link-local
ipv6 address 205::1:1:1/64
ipv6 enable
!
interface Ethernet0/0
! interface connect to the core vpn
bandwidth 1000
ip address 30.3.0.1 255.255.255.0
ip pim sparse-dense-mode
delay 100
ipv6 address FE80::70:1:1 link-local
ipv6 address 70::1:1:1/64
ipv6 enable
mpls ip
!
interface Ethernet1/1
! interface connect to CE (vrf interface)
bandwidth 1000
vrf forwarding blue
ip address 10.1.0.1 255.255.255.0
ip pim sparse-dense-mode
delay 100
ipv6 address FE80::20:1:1 link-local
ipv6 address 20::1:1:1/64
ipv6 enable
!
router ospf 200

IP Routing: BGP Configuration Guide
929


BGP-MVPN SAFI 129 IPv6
Example: Configuring BGP-MVPN SAFI 129 IPv6

redistribute connected subnets
redistribute bgp 55 metric 10
passive-interface Loopback0
network 30.3.0.0 0.0.255.255 area 1
!
router bgp 55
bgp log-neighbor-changes
no bgp default route-target filter
! neighbor to another PE in core
neighbor 205.3.0.3 remote-as 55
neighbor 205.3.0.3 update-source Loopback0
!
address-family ipv4 mdt
! neighbor to another PE in core
neighbor 205.3.0.3 activate
neighbor 205.3.0.3 send-community extended
exit-address-family
!
address-family vpnv6
! neighbor to another PE in core
neighbor 205.3.0.3 activate
neighbor 205.3.0.3 send-community extended
exit-address-family
!
address-family vpnv6 multicast
! neighbor to another PE in core
! this address-family is added to enable
! safi129 between two PEs
neighbor 205.3.0.3 activate
neighbor 205.3.0.3 send-community extended
exit-address-family
!
address-family ipv6 vrf blue
! neighbor to CE1 in vrf
redistribute connected
redistribute static
neighbor FE80::20:1:6%Ethernet1/1 remote-as 56
neighbor FE80::20:1:6%Ethernet1/1 activate
exit-address-family
!
address-family ipv6 multicast vrf blue
! neighbor to CE1 in vrf
! this address-family is added to enable
! safi2 on PE-CE
redistribute connected
redistribute static
neighbor FE80::20:1:6%Ethernet1/1 remote-as 56
neighbor FE80::20:1:6%Ethernet1/1 activate
exit-address-family
!
ipv6 pim vrf blue rp-address 201::1:1:7 blue_bidir_acl bidir
ipv6 pim vrf blue rp-address 202::1:1:6 blue_sparse_acl
!
ipv6 access-list black_bidir_acl
permit ipv6 any FF06::/64
!
ipv6 access-list black_sparse_acl
permit ipv6 any FF04::/64
!
ipv6 access-list blue_bidir_acl
permit ipv6 any FF05::/64
!
ipv6 access-list blue_sparse_acl
permit ipv6 any FF03::/64

IP Routing: BGP Configuration Guide
930


BGP-MVPN SAFI 129 IPv6
Example: Configuring BGP-MVPN SAFI 129 IPv6

!
end

The example below shows the configuration for a CE router:
hostname CE1
!
ip multicast-routing
ip cef
ipv6 unicast-routing
ipv6 multicast-routing
ipv6 multicast rpf use-bgp
ipv6 cef
!
interface Ethernet1/1
bandwidth 1000
ip address 10.1.0.6 255.255.255.0
no ip redirects
no ip proxy-arp
ip pim sparse-dense-mode
delay 100
ipv6 address FE80::20:1:6 link-local
ipv6 address 20::1:1:6/64
ipv6 enable
no keepalive
!
router bgp 56
bgp log-neighbor-changes
neighbor FE80::20:1:1%Ethernet1/1 remote-as 55
!
address-family ipv6
redistribute connected
redistribute static
neighbor FE80::20:1:1%Ethernet1/1 activate
exit-address-family
!
address-family ipv6 multicast
redistribute connected
redistribute static
neighbor FE80::20:1:1%Ethernet1/1 activate
exit-address-family
!
ipv6 pim rp-address 201::1:1:7 blue_bidir_acl bidir
ipv6 pim rp-address 202::1:1:6 blue_sparse_acl
!
ipv6 access-list blue_bidir_acl
permit ipv6 any FF05::/64
!
ipv6 access-list blue_sparse_acl
permit ipv6 any FF03::/64
!
end

IP Routing: BGP Configuration Guide
931


BGP-MVPN SAFI 129 IPv6
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

BGP commands: complete command syntax, command modes, command Cisco IOS IP Routing: BGP
history, defaults, usage guidelines, and examples
Command Reference
Standards and RFCs
Standard/RFC

Title

MDT SAFI

Subsequent Address Family
Identifiers (SAFI) Parameters

RFC 2547

BGP/MPLS VPNs

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

Feature Information for BGP-MVPN SAFI 129 IPv6
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
932


BGP-MVPN SAFI 129 IPv6
Feature Information for BGP-MVPN SAFI 129 IPv6

Table 80: Feature Information for BGP—MVPN SAFI 129 IPv6

Feature Name

Releases

Feature Information

BGP—MVPN SAFI 129 IPv6

15.2(4)S

SAFI 129 , known as VPN
Multicast SAFI, provides the
capability to support multicast
routing in the service provider's
core IPv6 network.

Cisco IOS XE Release 3.7S
15.3(1)T

The following commands were
introduced or modified:
address-family ipv6,
address-family vpnv6, and show
bgp vpnv6 multicast.

IP Routing: BGP Configuration Guide
933


BGP-MVPN SAFI 129 IPv6
Feature Information for BGP-MVPN SAFI 129 IPv6

IP Routing: BGP Configuration Guide
934
