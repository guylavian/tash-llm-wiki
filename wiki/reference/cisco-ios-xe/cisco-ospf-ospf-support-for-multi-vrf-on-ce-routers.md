---
title: "OSPF Support for Multi-VRF on CE Routers"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-support-for-multi-vrf-on-ce-routers
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 12 OSPF Support for Multi-VRF on CE Routers The OSPF Support for Multi-VRF on CE Routers feature provides the capability to suppress provider edge (PE) checks that are needed to prevent loops when the PE is performing a mutual redistribution of packets between the OSPF and BGP protocols. When VPN routing and forwarding (VRF) is used on a router that is not a PE (that is, one that is not"
---

# OSPF Support for Multi-VRF on CE Routers

CHAPTER

12

OSPF Support for Multi-VRF on CE Routers
The OSPF Support for Multi-VRF on CE Routers feature provides the capability to suppress provider edge
(PE) checks that are needed to prevent loops when the PE is performing a mutual redistribution of packets
between the OSPF and BGP protocols. When VPN routing and forwarding (VRF) is used on a router that
is not a PE (that is, one that is not running BGP), the checks can be turned off to allow for correct population
of the VRF routing table with routes to IP prefixes.
OSPF multi-VRF allows you to split the router into multiple virtual routers, where each router contains its
own set of interfaces, routing table, and forwarding table.
• Finding Feature Information, page 143
• Information About OSPF Support for Multi-VRF on CE Routers, page 143
• How to Configure OSPF Support for Multi-VRF on CE Routers, page 144
• Configuration Example for OSPF Support for Multi-VRF on CE Routers, page 146
• Additional References, page 147
• Feature Information for OSPF Support for Multi-VRF on CE Routers, page 149
• Glossary, page 149

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPF Support for Multi-VRF on CE Routers
The OSPF Support for Multi-VRF on CE Routers feature provides the capability to suppress provider edge
(PE) checks that are needed to prevent loops when the PE is performing a mutual redistribution of packets

IP Routing: OSPF Configuration Guide
143


OSPF Support for Multi-VRF on CE Routers
How to Configure OSPF Support for Multi-VRF on CE Routers

between the OSPF and BGP protocols. When VPN routing and forwarding (VRF) is used on a router that is
not a PE (that is, one that is not running BGP), the checks can be turned off to allow for correct population
of the VRF routing table with routes to IP prefixes.
OSPF multi-VRF allows you to split the router into multiple virtual routers, where each router contains its
own set of interfaces, routing table, and forwarding table. OSPF multi-VRF gives you the ability to segment
parts of your network and configure those segments to perform specific functions, yet still maintain correct
routing information.

How to Configure OSPF Support for Multi-VRF on CE Routers
Configuring the Multi-VRF Capability for OSPF Routing
Before You Begin
CEF must be running on the network.

SUMMARY STEPS
1. enable
2. show ip ospf [process-id
3. configure terminal
4. vpdn- group name
5. exit
6. resource-pool profile vpdn name
7. vpdn group name
8. vpn vrf vrf-name | id vpn-id
9. exit
10. router ospf process-id [vrf vpn-name]
11. capability vrf-lite

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

show ip ospf [process-id
Example:
Router# show ip ospf 1

IP Routing: OSPF Configuration Guide
144

Displays the status of the router. If the display indicates that the
router is connected to the VPN backbone, you can use the
capability vrf-lite command to decouple the PE router from the
VPN backbone.


OSPF Support for Multi-VRF on CE Routers
Configuring the Multi-VRF Capability for OSPF Routing

Step 3

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 4

vpdn- group

name

Creates a VPDN group.

Example:
Router(config)# vpdn-group mygroup

Step 5

Leaves the configuration mode and returns to global configuration
mode.

exit
Example:
Router(config-vpdn)# exit

Step 6

resource-pool profile vpdn name

Creates a virtual private dialup network (VPDN) profile and enters
VPDN profile configuration mode.

Example:
Router(config)# resource-pool profile vpdn
company1

Step 7

vpdn group

name

Associates a virtual private dialup network (VPDN) group with
a customer or VPDN profile.

Example:
Router(config-vpdn-profile)# vpdn group
mygroup

Step 8

vpn vrf vrf-name | id vpn-id
Example:

Specifies that the source and destination IPv4 addresses of a given
virtual private dialup network (VPDN) group belong to a specified
Virtual Private Network (VPN) routing and forwarding (VRF)
instance.

Router(config-vpdn)# vpn vrf grc

Step 9

exit

Leaves the configuration mode and returns to global configuration
mode.

Example:
Router(config-vpdn)# exit

Step 10

router ospf process-id [vrf vpn-name]
Example:
Router(config)# router ospf 1 vrf grc

Enables OSPF routing and enters router configuration mode.
• The process-id argument identifies the OSPF process.
• Use the vrf keyword and vpn-name argument to identify a
VPN.

IP Routing: OSPF Configuration Guide
145


OSPF Support for Multi-VRF on CE Routers
Verifying the OSPF Multi-VRF Configuration

Step 11

Command or Action

Purpose

capability vrf-lite

Applies the multi-VRF capability to the OSPF process.

Example:
Router(config-router)# capability vrf-lite

Verifying the OSPF Multi-VRF Configuration
No specific debug or show commands are associated with this feature. You can verify the success of the
OSPF multi-VRF configuration by using the show ip ospf process-id] command to verify that the router is
not connected to the VPN backbone.
This output from the show ip ospf processcommand indicates that the PE router is currently connected to the
backbone.
Router# show ip ospf 12
Routing Process "ospf 12" with ID 172.16.1.1 and Domain ID 0.0.0.12
Supports only single TOS(TOS0) routes
Supports opaque LSA
Connected to MPLS VPN Superbackbone
SPF schedule delay 5 secs, Hold time between two SPFs 10 secs
Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs
Number of external LSA 0. Checksum Sum 0x0
Number of opaque AS LSA 0. Checksum Sum 0x0
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 0. 0 normal 0 stub 0 nssa
External flood list length 0

When the OSPF VRF process is configured with the capability vrf-lite command under the router ospf
command, the "Connected to MPLS VPN Superbackbone" line will not be present in the display.

Configuration Example for OSPF Support for Multi-VRF on CE
Routers
Example Configuring the Multi-VRF Capability
This example shows a basic OSPF network with a VRF named grc configured. The capability vrf-lite command
is entered to suppress the PE checks.
!
ip cef
ip vrf grc
rd 1:1
interface Serial2/0/0
ip vrf forwarding grc
ip address 192.168.1.1 255.255.255.252
!
interface Serial3/0/0

IP Routing: OSPF Configuration Guide
146


OSPF Support for Multi-VRF on CE Routers
Additional References

ip vrf forwarding grc
ip address 192.168.2.1 255.255.255.252
...
!
router ospf 9000 vrf grc
log-adjacency-changes
capability vrf-lite
redistribute rip metric 1 subnets
network 192.168.1.0 0.0.0.255 area 0
!
router rip
address-family ipv4 vrf grc
redistribute ospf 9000 vrf grc
network 192.168.2.0
no auto-summary
end
Device# show ip route vrf grc
Routing Table: grc
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
ia - IS-IS inter area, * - candidate default, U - per-user static route
o - ODR, P - periodic downloaded static route
Gateway of last resort is not set
O IA 192.168.192.0/24 [110/138] via 192.168.1.13, 00:06:08, Serial2/0/0
[110/138] via 192.168.1.9, 00:06:08, Serial3/0/0
O IA 192.168.242.0/24 [110/74] via 192.168.1.13, 00:06:08, Serial2/0/0
O IA 192.168.193.0/24 [110/148] via 192.168.1.13, 00:06:08, Serial2/0/0
[110/148] via 192.168.1.9, 00:06:08, Serial3/0/0
O IA 192.168.128.0/24 [110/74] via 192.168.1.9, 00:06:08, Serial3/0/0
O IA 192.168.129.0/24 [110/84] via 192.168.1.9, 00:06:08, Serial3/0/0
O IA 192.168.130.0/24 [110/84] via 192.168.1.9, 00:06:08, Serial3/0/0
172.16.0.0/24 is subnetted, 2 subnets
O E2
172.16.9.0 [110/5] via 192.168.1.13, 00:06:08, Serial2/0/0
O E2
172.16.10.0 [110/5] via 192.168.1.13, 00:06:08, Serial2/0/0
O IA 192.168.131.0/24 [110/94] via 192.168.1.9, 00:06:20, Serial3/0/0
192.168.1.0/30 is subnetted, 4 subnets
C
192.168.1.8 is directly connected, Serial3/0/0
C
192.168.1.12 is directly connected, Serial2/0/0
O
192.168.1.0 [110/128] via 192.168.1.9, 00:06:20, Serial3/0/0
O
192.168.1.4 [110/128] via 192.168.1.13, 00:06:20, Serial2/0/0

Additional References
For additional information related to OSPF support for multi-VRF on CE routers, see the following references.
Related Documents
Related Topic

Document Title

Configuring OSPF

"Configuring OSPF"

Multiprotocol Label Switching (MPLS)

Cisco IOS XE Multiprotocol Label Switching
Configuration Guide, Release 2

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

IP Routing: OSPF Configuration Guide
147


OSPF Support for Multi-VRF on CE Routers
Additional References

Standards
Standard

Title

No new or modified standards are supported by this -feature, and support for existing standards has not
been modified by this feature.

MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS XE software releases , and feature sets,
use Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

No new or modified RFCs are supported by this
feature, and support for existing RFCs has not been
modified by this feature.

--

Technical Assistance
Description

Link

The Cisco Support and Documentation website
http://www.cisco.com/cisco/web/support/index.html
provides online resources to download documentation,
software, and tools. Use these resources to install and
configure the software and to troubleshoot and resolve
technical issues with Cisco products and technologies.
Access to most tools on the Cisco Support and
Documentation website requires a Cisco.com user ID
and password.

IP Routing: OSPF Configuration Guide
148


OSPF Support for Multi-VRF on CE Routers
Feature Information for OSPF Support for Multi-VRF on CE Routers

Feature Information for OSPF Support for Multi-VRF on CE
Routers
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 15: Feature Information for OSPF Support for Multi-VRF on CE Routers

Feature Name

Releases

Feature Information

OSPF Support for Multi-VRF on
CE Routers

Cisco IOS XE Release 2.1

The OSPF Support for Multi-VRF
on CE Routers feature provides the
capability to suppress provider
edge (PE) checks that are needed
to prevent loops when the PE is
performing a mutual redistribution
of packets between the OSPF and
BGP protocols. When VPN routing
and forwarding (VRF) is used on
a router that is not a PE (that is, one
that is not running BGP), the
checks can be turned off to allow
for correct population of the VRF
routing table with routes to IP
prefixes.

Cisco IOS XE Release 3.1.0 SG

The following commands are
introduced or modified in the
feature documented in this module:
• capability vrf-lite

Glossary
CE Router --Customer Edge router, an edge router in the C network, defined as a C router which attaches
directly to a P router.
C Network --Customer (enterprise or service provider) network.
C Router --Customer router, a router in the C network.
LSA --link-state advertisement . Broadcast packet used by link-state protocols that contains information about
neighbors and path costs. LSAs are used by the receiving routers to maintain their routing tables.

IP Routing: OSPF Configuration Guide
149


OSPF Support for Multi-VRF on CE Routers
Glossary

PE Router --Provider Edge router, an edge router in the P network, defined as a P router which attaches
directly to a C router.
P Network --MPLS-capable service provider core network. P routers perform MPLS.
P Router --Provider router, a router in the P network.
SPF --shortest path first. A routing algorithm that iterates on length of path to determine a shortest-path
spanning tree.
VPN --Virtual Private Network. Enables IP traffic to travel securely over a public TCP/IP network by encrypting
all traffic from one network to another.
VRF --VPN Routing and Forwarding.

IP Routing: OSPF Configuration Guide
150
