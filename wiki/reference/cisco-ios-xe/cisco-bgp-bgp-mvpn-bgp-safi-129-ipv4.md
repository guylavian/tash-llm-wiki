---
title: "BGP — mVPN BGP sAFI 129 - IPv4"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-mvpn-bgp-safi-129-ipv4
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 60 BGP — mVPN BGP sAFI 129 - IPv4 The BGP—mVPN BGP sAFI 129 IPv4 feature provides the capability to support multicast routing in the service provider’s core IPv4 network. This feature is needed to support BGP-based MVPNs. BGP MVPN provides a means for service providers to use different encapsulation methods (generic routing encapsulation [GRE], Multicast Label Distribution Protocol [MPDP"
---

# BGP — mVPN BGP sAFI 129 - IPv4

CHAPTER

60

BGP — mVPN BGP sAFI 129 - IPv4
The BGP—mVPN BGP sAFI 129 IPv4 feature provides the capability to support multicast routing in the
service provider’s core IPv4 network. This feature is needed to support BGP-based MVPNs. BGP MVPN
provides a means for service providers to use different encapsulation methods (generic routing encapsulation
[GRE], Multicast Label Distribution Protocol [MPDP], and ingress replication) for forwarding MVPN multicast
data traffic in the service provider network.
• Finding Feature Information, on page 915
• Information About BGP--mVPN BGP sAFI 129 - IPv4, on page 915
• How to Configure BGP -- mVPN BGP sAFI 129 - IPv4, on page 916
• Configuration Examples for BGP--mVPN BGPsAFI 129 - IPv4, on page 919
• Additional References, on page 922
• Feature Information for BGP - mVPN BGP sAFI 129 - IPv4, on page 923

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP--mVPN BGP sAFI 129 - IPv4
BGP — mVPN BGP sAFI 129 - IPv4 Overview
The Cisco BGP Address Family Identifier (AFI) model was introduced with multiprotocol BGP and is designed
to be modular and scalable and to support multiple AFI and Subsequent Address Family Identifier (SAFI)
configurations. SAFI provides additional information about the type of Network Layer Reachability Information
(NLRI) that is used to describe a route and how to connect to a destination.
SAFI 129 provides the capability to support multicast routing in the service provider’s core IPv4 network.
This feature is needed to support BGP-based MVPNs. The addition of SAFI 129 allows multicast to select
an upstream multicast hop that may be independent of the unicast topology. Multicast routes learned from

IP Routing: BGP Configuration Guide
915


BGP — mVPN BGP sAFI 129 - IPv4
How to Configure BGP -- mVPN BGP sAFI 129 - IPv4

the customer edge (CE) router or multicast VPN routes learned from remote provider edge (PE) routers are
installed into the multicast Routing Information Base (RIB), whereas previously unicast routes in the unicast
RIB were replicated into the multicast RIB.
The address-family ipv4 command has been updated to support IP version 4 (IPv4) multicast address prefixes
for a VPN routing and forwarding (VRF) instance, and the address-family vpnv4 command has been updated
to support VPN version 4 (VPNv4) multicast address prefixes.

How to Configure BGP -- mVPN BGP sAFI 129 - IPv4
Configure BGP — mVPN BGP sAFI 129 - IPv4
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
14.
15.
16.
17.
18.
19.
20.
21.
22.

enable
configure terminal
vrf definition vrf1
rd route-distinguisher
route-target export route-target-ext-community
route-target import route-target-ext-community
address-family ipv4
mdt default group-address
exit
router bgp autonomous-system-number
address-family vpnv4 multicast
neighbor peer-group-name send-community extended
neighbor peer-group-name route-reflector-client
exit-address-family
address-family ipv4 vrf vrf-name
no synchronization
exit-address-family
address-family ipv4 multicast vrf vrf-name
no synchronization
exit-address-family
end
show running-config | b router bgp

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device> enable

IP Routing: BGP Configuration Guide
916

• Enter your password if prompted.


BGP — mVPN BGP sAFI 129 - IPv4
Configure BGP — mVPN BGP sAFI 129 - IPv4

Step 2

Command or Action

Purpose

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

address-family ipv4
Example:

Configures a routing session using IPv4 address prefixes
and enters address family configuration mode.

Device(config-router)# address-family ipv4

Step 8

mdt default group-address
Example:

Configures a default multicast distribution tree (MDT)
group for a VRF instance.

Device(config-vrf)# mdt default 239.0.0.1

Step 9

exit
Example:

Exits VRF configuration mode and returns to global
configuration mode.

Device(config-vrf)# exit

Step 10

router bgp autonomous-system-number
Example:

Configures the BGP routing process and enters router
configuration mode.

Device(config)# router bgp 50000

IP Routing: BGP Configuration Guide
917


BGP — mVPN BGP sAFI 129 - IPv4
Configure BGP — mVPN BGP sAFI 129 - IPv4

Step 11

Command or Action

Purpose

address-family vpnv4 multicast

Configures a routing session using VPN Version 4
multicast address prefixes and enters address family
configuration mode.

Example:
Device(config-router)# address-family vpnv4
multicast

Step 12

neighbor peer-group-name send-community extended Specifies that a communities attribute should be sent to a
BGP neighbor.
Example:
Device(config-router-af)# neighbor client1
send-community extended

Step 13

neighbor peer-group-name route-reflector-client
Example:

(Optional) Configures the router as a BGP route reflector
and configures the specified neighbor as its client.

Device(config-router-af)# neighbor client1
route-reflector-client

Step 14

exit-address-family
Example:

Exits address family configuration mode and enters router
configuration mode.

Device(config-router-af)# exit-address-family

Step 15

address-family ipv4 vrf vrf-name
Example:
Device(config-router)# address-family ipv4 vrf
vrf1

Step 16

no synchronization
Example:

Places the router in address family configuration mode
and specifies the name of the VRF instance to associate
with subsequent IPv4 address family configuration mode
commands.

Enables the Cisco software to advertise a network route
without waiting for the Interior Gateway Protocol (IGP)
system.

Device(config-router-af)# no synchronization

Step 17

exit-address-family
Example:

Exits address family configuration mode and enters router
configuration mode.

Device(config-router-af)# exit-address-family

Step 18

address-family ipv4 multicast vrf vrf-name
Example:

Configures a routing session using IPv4 multicast address
prefixes for a VRF instance and enters address family
configuration mode.

Device(config-router)# address-family ipv4
multicast vrf vrf1

Step 19

no synchronization
Example:

IP Routing: BGP Configuration Guide
918

Enables the Cisco software to advertise a network route
without waiting for the IGP system.


BGP — mVPN BGP sAFI 129 - IPv4
Configuration Examples for BGP--mVPN BGPsAFI 129 - IPv4

Command or Action

Purpose

Device(config-router-af)# no synchronization

Step 20

exit-address-family
Example:

Exits address family configuration mode and enters router
configuration mode.

Device(config-router-af)# exit-address-family

Step 21

end
Example:

Exits router configuration mode and returns to privileged
EXEC mode.

Device(config)# end

Step 22

show running-config | b router bgp
Example:

(Optional) Displays the running configuration for specified
device.

Device# show running-config | b router bgp

Configuration Examples for BGP--mVPN BGPsAFI 129 - IPv4
Example: Configuring BGP - mVPN BGP sAFI 129 - IPv4
This example uses the topology illustrated in the figure below.

The following example configures BGP SAFI 129 on the route reflector (RR):
!
ip multicast-routing
!
!<<< Define BGP update-source loopback0
!<<< on RR as 192.0.2.10
interface loopback0
ip pim sparse-dense-mode
ip address 192.0.2.10 255.255.255.255
!
.
.

IP Routing: BGP Configuration Guide
919


BGP — mVPN BGP sAFI 129 - IPv4
Example: Configuring BGP - mVPN BGP sAFI 129 - IPv4

.
router bgp 65000
no synchronization
neighbor 192.0.2.1 remote-as 65000
neighbor 192.0.2.1 update-source loopback0
neighbor 192.0.2.2 remote-as 65000
neighbor 192.0.2.2 update-source loopback0
neighbor 192.0.2.3 remote-as 65000
neighbor 192.0.2.3 update-source loopback0
!
.
.
address-family vpnv4 unicast
neighbor 192.0.2.1 activate
neighbor 192.0.2.1 send-community extended
neighbor 192.0.2.1 route-reflector-client
neighbor 192.0.2.2 activate
neighbor 192.0.2.2 send-community extended
neighbor 192.0.2.2 route-reflector-client
neighbor 192.0.2.3 activate
neighbor 192.0.2.3 send-community extended
neighbor 192.0.2.3 route-reflector-client
exit-address-family
!
address-family vpnv4 multicast
!<<< want route from CE1 with nexthop
!<<< through PE3 in multicast routing table
neighbor 192.0.2.1 activate
neighbor 192.0.2.1 send-community extended
neighbor 192.0.2.1 route-reflector-client
neighbor 192.0.2.3 activate
neighbor 192.0.2.3 send-community extended
neighbor 192.0.2.3 route-reflector-client
exit-address-family
!
.
.

The following example configures BGP SAFI 129 on the PE1 router (PE2 and PE3 will have a similar
configuration):

Hostname PE1
!
vrf definition vrf1
rd 1:1
route-target export 1:1
route-target import 1:1
!
address-family ipv4
mdt default 239.0.0.1
exit-address-family
!
ip multicast-routing
ip multicast-routing vrf vrf1
!
.
.
.
!<<< Define BGP update-source on Loopback0
!<<< on PE1
inteface loopback0
ip pim sparse-dense-mode
ip address 192.0.2.1 255.255.255.255

IP Routing: BGP Configuration Guide
920


BGP — mVPN BGP sAFI 129 - IPv4
Example: Configuring BGP - mVPN BGP sAFI 129 - IPv4

!
.
.
.
!<<< Define vrf vrf1 interface on PE1 to CE1
interface ethernet0/0
vrf forwarding vrf1
ip pim sparse-dense-mode
ip address 192.0.2.1 255.255.255.0
!
.
.
,
router bgp 65000
!<<<< PE peer neighbor with RR
neighbor 192.0.2.10 remote-as 65000
neighbor 192.0.2.10 update-source loopback0
no synchronization
.
.
.
address-family vpnv4
neighbor 192.0.2.10 activate
neighbor 192.0.2.10 send-community extended
exit-address-family
!
!<<< Define vpnv4 safi129 with neighbor
!<<< to RR
address-family vpnv4 multicast
neighbor 192.0.2.10 activate
neighbor 192.0.2.10 send-community extended
exit-address-family
!
.
.
.
!<<< Define unicast address-family vrf vrf1.
!<<< PE-CE is eBGP in this case.
!<<< If PE-CE is not eBGP, please use
!<<< redistribute cli, instead of
!<<< neighbor cli below.
address-family ipv4 vrf vrf1
no synchronization
redistribute connected
neighbor 192.0.2.5 remote-as 65011
exit-address-family
!
!<<< Define multicast address-family vrf vrf1
!<<< (safi2. PE-CE is eBGP in this case.
!<<< If PE-CE is not eBGP, please use
!<<< redistribute cli, instead of
!<<< neighbor cli below.
address-family ipv4 multicast vrf vrf1
no synchronization
redistribute connected
neighbor 192.0.2.5 remote-as 65011
exit-address-family
!

The following example configures BGP SAFI 129 on the CE1 router. (In this case, PE-CE routing is eBGP.
CE2 will have a similar configuration):

interface ethernet0/0

IP Routing: BGP Configuration Guide
921


BGP — mVPN BGP sAFI 129 - IPv4
Additional References

ip address 192.0.2.5 255.255.255.0
ip pim sparse-dense-mode
!
.
.
.
router bgp 65011
bgp router-id 192.0.2.5
bgp log-neighbor-changes
!
address-family ipv4
redistribute connected
neighbor 192.0.2.1 remote-as 65000
exit-address-family
!
address-family ipv4 multicast
redistribute connected
neighbor 192.0.2.1 remote-as 65000
exit-address-family
!

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

Standards and RFCs
Standard/RFC Title
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

IP Routing: BGP Configuration Guide
922


BGP — mVPN BGP sAFI 129 - IPv4
Feature Information for BGP - mVPN BGP sAFI 129 - IPv4

Feature Information for BGP - mVPN BGP sAFI 129 - IPv4
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 79: Feature Information for BGP - mVPN BGP sAFI 129 - IPv4

Feature Name

Releases

Feature Information

BGP - mVPN BGP sAFI 129 IPv4

15.2(2)S

The BGP - mVPN BGP sAFI 129
IPv4 feature provides the capability
to support multicast routing in the
service provider’s core IPv4
network. This feature is needed to
support BGP-based MVPNs. BGP
MVPN provides a means for
service providers to use different
encapsulation methods (generic
route encapsulation (GRE),
Multicast Label Distribution
Protocol (MLDP), and ingress
replication) for forwarding MVPN
multicast data traffic in the service
provider network. In Cisco IOS
Release 15.2(4)S, support was
added for the Cisco 7200 series
router.

15.2(4)S
Cisco IOS XE Release 3.6S

The following commands were
modified: address-family ipv4,
address-family vpnv4.

IP Routing: BGP Configuration Guide
923


BGP — mVPN BGP sAFI 129 - IPv4
Feature Information for BGP - mVPN BGP sAFI 129 - IPv4

IP Routing: BGP Configuration Guide
924
