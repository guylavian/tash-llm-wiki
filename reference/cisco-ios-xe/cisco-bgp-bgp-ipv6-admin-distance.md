---
title: "BGP IPv6 Admin Distance"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-ipv6-admin-distance
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 11 BGP IPv6 Admin Distance The BGP IPv6 Admin Distance feature lets you prioritize the BGP IPv6 routes in your network by enabling you to configure the source specific distance of a route and associate a prefix-list with the route. The RIB uses the distance from the source to determine the priority of the BGP IPv6 route in the network. • Information About BGP IPv6 Admin Distance, on page"
---

# BGP IPv6 Admin Distance

CHAPTER

11

BGP IPv6 Admin Distance
The BGP IPv6 Admin Distance feature lets you prioritize the BGP IPv6 routes in your network by enabling
you to configure the source specific distance of a route and associate a prefix-list with the route. The RIB uses
the distance from the source to determine the priority of the BGP IPv6 route in the network.
• Information About BGP IPv6 Admin Distance, on page 255
• Configuring BGP IPv6 Admin Distance, on page 255
• Additional References for BGP IPv6 Admin Distance, on page 257
• Feature Information for BGP IPv6 Admin Distance, on page 258

Information About BGP IPv6 Admin Distance
The BGP IPv6 Admin Distance feature supports selection of route path for a set prefix by prioritizing the
BGP routes in the RIB. The BGP routes provided in the RIB are prioritized based on the distance they are
configured from a source. With BGP IPv6 Admin Distance feature you can configure the distance from a
source and can associate the route with a prefix-list. The route with the source specific distance and the
prefix-list is then utilized by the RIB to prioritize the BGP IPv6 routes.

Benefits of Using BGP IPv6 Admin Distance
The BGP IPv6 Admin Distance feature can be used to prioritize or de-prioritize the BGP IPv6 routes in your
network.

Configuring BGP IPv6 Admin Distance
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.

enable
configure terminal
ipv6 unicast-routing
router bgpautonomous-system-number
address-family ipv6 unicast
distance admin-distance ipv6-address/prefix prelengthinterface nameprefix-list
end

IP Routing: BGP Configuration Guide
255


BGP IPv6 Admin Distance
Verifying BGP Admin Distance Configuration

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

ipv6 unicast-routing

Enables the forwarding of IPv6 unicast datagrams

Example:
Device(config)# ipv6 unicast-routing

Step 4

router bgpautonomous-system-number
Example:
Device(config)# router bgp 5

Step 5

address-family ipv6 unicast
Example:

Specifies the number of an autonomous system that
identifies the router to other BGP routers and tags the
routing information that is passed along.
• The range is from 1 to 65535.
Enters the address family configuration mode for
configuring routing sessions.

Device(config-router)# address-family ipv6 unicast

Step 6

distance admin-distance ipv6-address/prefix
prelengthinterface nameprefix-list
Example:
Device(config-router-af)# distance 12
2001:DB8:0:CC00::1/128 list1

Step 7

Specifies the administrative distance, IPv6 address, prefix
length and prefix list name for configuring the source
specific distance for BGP routes.
Interface name is optional and is required only if the
neighbor address is a link local address.
Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Verifying BGP Admin Distance Configuration
Use the show run sec bgp command to verify the BGP configuration:
Device(config-device-af)# show run | sec bgp
router bgp 200
bgp log-neighbor-changes
neighbor FE80::A8BB:CCFF:FE02:BE01%Ethernet0/0 remote-as 200
neighbor FE80::A8BB:CCFF:FE02:BE01%Ethernet0/0 update-source Ethernet0/0

IP Routing: BGP Configuration Guide
256


BGP IPv6 Admin Distance
Additional References for BGP IPv6 Admin Distance

!
address-family ipv4
no neighbor FE80::A8BB:CCFF:FE02:BE01%Ethernet0/0 activate
exit-address-family
!
address-family ipv6
distance 90 FE80::A8BB:CCFF:FE02:BE01/128 interface Ethernet0/0
network 1:1:1:1::/120
neighbor FE80::A8BB:CCFF:FE02:BE01%Ethernet0/0 activate
exit-address-family

Use the do show ipv6 route command to verify the IPv6 route configuration:
Device(config-device-af)# show ipv6 route
IPv6 Routing Table - default - 4 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
B - BGP, R - RIP, H - NHRP, I1 - ISIS L1
I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
NDr - Redirect, O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF ext 1
OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
la - LISP alt, lr - LISP site-registrations, ld - LISP dyn-eid
lA - LISP away, a - Application
C
1:1:1:1::/120 [0/0]
via Ethernet0/0, directly connected
L
1:1:1:1::2/128 [0/0]
via Ethernet0/0, receive
B
3:4:5:6::1/128 [90/0]
via FE80::A8BB:CCFF:FE02:BF01, Ethernet0/0
L
FF00::/8 [0/0]
via Null0, receive

Additional References for BGP IPv6 Admin Distance
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

Cisco IOS IP Routing: BGP commands Cisco IOS IP Routing: BGP Command Reference
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
257


BGP IPv6 Admin Distance
Feature Information for BGP IPv6 Admin Distance

Feature Information for BGP IPv6 Admin Distance
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 23: Feature Information for ASR1K NPTv6

Feature Name

Releases

Feature Configuration
Information

BGP IPv6 Admin Distance

Cisco IOS XE Denali 16.3.1

The BGP IPv6 Admin
Distance feature lets you
prioritize the BGP IPv6 routes
in your network by enabling
you to configure the source
specific distance of a route
and associate a prefix-list with
the route. The RIB uses the
distance from the source to
determine the priority of the
BGP IPv6 route in the
network.
The following commands
were modified: distance

IP Routing: BGP Configuration Guide
258
