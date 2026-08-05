---
title: "Autoroute Announce and Forwarding Adjacencies For OSPFv3"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-autoroute-announce-and-forwarding-adjacencies-for-ospfv3
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 17 Autoroute Announce and Forwarding Adjacencies For OSPFv3 The Autoroute Announce and Forwarding Adjacencies for OSPFv3 feature advertises IPv6 routes over MPLS/TE IPv4 tunnels. This module describes how to configure the Autoroute Announce and Forwarding Adjacencies for OSPFv3 feature. • Finding Feature Information, page 193 • Prerequisites for Autoroute Announce and Forwarding Adjacenc"
---

# Autoroute Announce and Forwarding Adjacencies For OSPFv3

CHAPTER

17

Autoroute Announce and Forwarding
Adjacencies For OSPFv3
The Autoroute Announce and Forwarding Adjacencies for OSPFv3 feature advertises IPv6 routes over
MPLS/TE IPv4 tunnels. This module describes how to configure the Autoroute Announce and Forwarding
Adjacencies for OSPFv3 feature.
• Finding Feature Information, page 193
• Prerequisites for Autoroute Announce and Forwarding Adjacencies For OSPFv3, page 194
• Restrictions for Autoroute Announce and Forwarding Adjacencies For OSPFv3, page 194
• Information About Autoroute Announce and Forwarding Adjacencies For OSPFv3, page 194
• How to Configure Autoroute Announce and Forwarding Adjacencies For OSPFv3, page 195
• Configuration Examples for Autoroute Announce and Forwarding Adjacencies For OSPFv3 , page 198
• Additional References for Autoroute Announce and Forwarding Adjacencies For OSPFv3, page 199
• Feature Information for Autoroute Announce and Forwarding Adjacencies For OSPFv3, page 200

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
193


Autoroute Announce and Forwarding Adjacencies For OSPFv3
Prerequisites for Autoroute Announce and Forwarding Adjacencies For OSPFv3

Prerequisites for Autoroute Announce and Forwarding
Adjacencies For OSPFv3
• OSPFv3 must be configured in your network.
• Cisco Express Forwarding (CEF) must be enabled.
• MPLS/TE tunnels must be configured.

Restrictions for Autoroute Announce and Forwarding
Adjacencies For OSPFv3
• Autoroute announce and forwarding adjacency cannot be configured together in a same interface.
• When an autoroute announce is used, OSPFv3 does not advertise the tunnel.
• When forwarding adjacencies are used, OSPFv3 advertises the tunnel link in an LSA.

Information About Autoroute Announce and Forwarding
Adjacencies For OSPFv3
Overview of Autoroute Announce and Forwarding Adjacencies For OSPFv3
The OSPFv3 support for Forwarding Adjacencies over MPLS Traffic Engineered Tunnels feature adds OSPFv3
support to the Multiprotocol Label Switching (MPLS) Traffic Engineering (TE) tunnels feature, which allows
a network administrator to handle a traffic engineering, MPLS tunnel as a link in an Interior Gateway Protocol
(IGP) network based on the shortest path first (SPF) algorithm. An OSPFv3 forwarding adjacency can be
created between routers in the same area.
OSPFv3 includes MPLS TE tunnels in the OSPFv3 router link-state advertisement (LSA) in the same way
that other links appear for purposes of routing and forwarding traffic. The user can assign an OSPFv3 cost to
the tunnel to give it precedence over other links. Other networking devices will see the tunnel as a link in
addition to the physical link.
OSPFv3 uses Autoroute Announce (AA) or Forwarding Adjacencies (FA) feature to install IPv6 routes over
MPLS/TE IPv4 tunnels into the IPv6 routing table . The TE tunnels are created using IPv4, and requires the
use of a routing protocol other than OSPFv3. OSPFv2 is used as the IPv4 IGP and provides data which TE
uses to create the tunnels.
OSPFv3 is configured on the TE tunnel interfaces for either autoroute-annouce or forwarding-adjacency. It
is also must be configured in router mode to advertise the address of the loopback interface which TE is using
for the tunnels that terminate on the router. That address is advertised in the TE LSA .

IP Routing: OSPF Configuration Guide
194


Autoroute Announce and Forwarding Adjacencies For OSPFv3
How to Configure Autoroute Announce and Forwarding Adjacencies For OSPFv3

How to Configure Autoroute Announce and Forwarding
Adjacencies For OSPFv3
Configuring Autoroute Announce and Forwarding Adjacencies For OSPFv3
SUMMARY STEPS
1. enable
2. configure terminal
3. ip cef distributed
4. interface type number
5. ip address ip-address-mask
6. no shutdown
7. exit
8. interface type number
9. ospfv3 pid af mpls traffic-eng autoroute announce area aid
10. ospfv3 pid af mpls traffic-eng autoroute metric {metric | absolute metric | relative delta}
11. ip ospf cost cost
12. exit
13. interface type number
14. ospfv3 pid af mpls traffic-eng forwarding-adj areaaid
15. ospfv3[ pid [af ]] mpls traffic-eng forwarding-adj interface ID [ local ID ] [nbr ID]
16. ip ospf cost cost
17. exit
18. router ospfv3 router-ID
19. address-family ipv4 unicast [vrf vrf-name ]
20. area aid mpls traffic-engineering tunnel-tail af interface type
21. exit
22. show ospfv3 database
23. show ospfv3 mpls traffic-eng

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

IP Routing: OSPF Configuration Guide
195


Autoroute Announce and Forwarding Adjacencies For OSPFv3
Configuring Autoroute Announce and Forwarding Adjacencies For OSPFv3

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

ip cef distributed

Enables distributed Cisco Express Forwarding operation.

Example:
Device(config)# ip cef distributed

Step 4

interface type number

Configures an interface type and enters interface
configuration mode.

Example:
Device(config)# interface tunnel 0

Step 5

ip address ip-address-mask

Sets a primary or secondary IP address for the specified
interface.

Example:
Device (config-if)# ip address 192.108.1.27
255.255.255.0

Step 6

no shutdown

Disables all functions on the specified interface.

Example:
Device (config-if)# no shutdown

Step 7

exit

Exits interface configuration mode and returns to
privileged EXEC mode.

Example:
Device (config-if)# exit

Step 8

interface type number

Enables loopback interface and enters interface
configuration mode.

Example:
Device (config)# interface loopback 0

Step 9

ospfv3 pid af mpls traffic-eng autoroute announce area Enable Open Shortest Path First version 3 (OSPFv3) on
an interface with the IP address family (AF).
aid
Example:
Device(config-if)# ospfv3 1 af mpls traffic-eng
autoroute announce
area 1

Step 10

ospfv3 pid af mpls traffic-eng autoroute metric {metric Specifies the MPLS traffic engineering auto route metric
value for the SPF calculation.
| absolute metric | relative delta}
Example:
Device(config-if)# ospfv3 1 af mpls traffic-eng
autoroute metric
1

IP Routing: OSPF Configuration Guide
196


Autoroute Announce and Forwarding Adjacencies For OSPFv3
Configuring Autoroute Announce and Forwarding Adjacencies For OSPFv3

Step 11

Command or Action

Purpose

ip ospf cost cost

Explicitly specifies the cost of sending a packet on an
OSPF interface.

Example:
Device(config-if)# ip ospf cost 60

Step 12

exit

Exits interface configuration mode and returns to
privileged EXEC mode.

Example:
Device(config-if)# exit

Step 13

interface type number

Enables tunnel interface and enters interface
configuration mode.

Example:
Device (config)# interface tunnel 1

Step 14

ospfv3 pid af mpls traffic-eng forwarding-adj areaaid Configure an MPLS traffic engineering forwarding
adjacency.
Example:
Device(config-if)# ospfv3 1 af mpls traffic-eng
forwarding-adj area
1

Step 15

ospfv3[ pid [af ]] mpls traffic-eng forwarding-adj
interface ID [ local ID ] [nbr ID]

Specifies the MPLS traffic engineering forwarding
adjacency for the SPF calculation.

Example:
Device(config-if)# ospfv3 1 af mpls traffic-eng
forwarding-adj
1

Step 16

ip ospf cost cost

Explicitly specifies the cost of sending a packet on an
OSPF interface.

Example:
Device(config-if)# ip ospf cost 55

Step 17

exit

Exits interface configuration mode and returns to
privileged EXEC mode.

Example:
Device(config-if)# exit

Step 18

router ospfv3 router-ID

Enters OSPFv3 router configuration mode.

Example:
Device(config)# router ospfv3 18

Step 19

address-family ipv4 unicast [vrf vrf-name ]
Example:

Configures the IPv4 address family in the OSPFv3
process and enters IPv4 address family configuration
mode.

Device(config-router)# address-family ipv4
unicast

IP Routing: OSPF Configuration Guide
197


Autoroute Announce and Forwarding Adjacencies For OSPFv3
Configuration Examples for Autoroute Announce and Forwarding Adjacencies For OSPFv3

Step 20

Command or Action

Purpose

area aid mpls traffic-engineering tunnel-tail af
interface type

Configures OSPFv3 on the tail end of the traffic
engineering tunnels.

Example:
Device(config-router-af)# area 1 mpls
traffic-engineering tunnel-tail
af loopback

Step 21

Exits address family configuration mode and returns to
global configuration mode.

exit
Example:
Device(config-router-af)# exit

Step 22

show ospfv3 database

(Optional) Displays list of information related to the
OSPFv3 database for a specific router.

Example:
Device(config)# show ospfv3 database

Step 23

show ospfv3 mpls traffic-eng

(Optional) Displays autoroute announce, forwarding
adjacency, and tunnel-tail information related to OSPFv3.

Example:
Device(config)# show ospfv3 mpls traffic-eng

ConfigurationExamplesforAutorouteAnnounceandForwarding
Adjacencies For OSPFv3
Example: Configuring Autoroute Announce and Forwarding Adjacencies For
OSPFv3
!
ip cef distributed
interface tunnel 0
ip address 192.108.1.27 255.255.255.0
no shutdown
interface loopback 0
ospfv3 1 af mpls traffic-eng autoroute announce area 1
ospfv3 1 af mpls traffic-eng autoroute metric 1
ip ospf cost 60
interface tunnel 1
ospfv3 1 af mpls traffic-eng forwarding-adj area 1
ospfv3 1 af mpls traffic-eng forwarding-adj nbr 1
ip ospf cost 55
router ospfv3 18
address-family ipv4 unicast

IP Routing: OSPF Configuration Guide
198


Autoroute Announce and Forwarding Adjacencies For OSPFv3
Additional References for Autoroute Announce and Forwarding Adjacencies For OSPFv3

area 1 mpls traffic-engineering tunnel-tail af loopback
!
!
!

Additional References for Autoroute Announce and Forwarding
Adjacencies For OSPFv3
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

Configuring OSPF features

IP Routing: OSPF Configuration Guide

Standards and RFCs
Related Topic

Document Title

Advertising a Router's Local Addresses in OSPF
Traffic Engineering (TE) Extensions

RFC5786

Traffic Engineering Extensions to OSPF Version 3

RFC5329

Traffic Engineering (TE) Extensions to OSPF Version RFC3630
2

Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/support
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies.
To receive security and technical information about
your products, you can subscribe to various services,
such as the Product Alert Tool (accessed from Field
Notices), the Cisco Technical Services Newsletter,
and Really Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website
requires a Cisco.com user ID and password.

IP Routing: OSPF Configuration Guide
199


Autoroute Announce and Forwarding Adjacencies For OSPFv3
Feature Information for Autoroute Announce and Forwarding Adjacencies For OSPFv3

Feature Information for Autoroute Announce and Forwarding
Adjacencies For OSPFv3
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 20: Feature Information for Autoroute Announce and Forwarding Adjacencies For OSPFv3

Feature Name

Releases

Feature Information

Autoroute Announce and
Forwarding Adjacencies For
OSPFv3

Cisco IOS XE Release 3.12S

The Autoroute Announce and
Forwarding Adjacencies For
OSPFv3 feature advertises IPv6
routes over MPLS/TE IPv4 tunnels.
The following commands were
introduced or modified: ospfv3 af
mpls traffic-eng autoroute
announce area , ospfv3 mpls
traffic-eng autoroute metric,
ospfv3 mpls traffic-eng
forwarding-adj area .

IP Routing: OSPF Configuration Guide
200
