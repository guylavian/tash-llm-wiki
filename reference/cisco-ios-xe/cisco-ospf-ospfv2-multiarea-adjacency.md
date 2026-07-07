---
title: "OSPFv2 Multiarea Adjacency"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv2-multiarea-adjacency
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 13 OSPFv2 Multiarea Adjacency This module describes how to configure multiarea adjacency for Open Shortest Path First version 2 (OSPFv2). You can add more than one area to an existing OSPFv2 primary interface. The additional logical interfaces support multiarea adjacency. • Finding Feature Information, page 151 • Prerequisites for OSPFv2 Multiarea Adjacency, page 151 • Restrictions for O"
---

# OSPFv2 Multiarea Adjacency

CHAPTER

13

OSPFv2 Multiarea Adjacency
This module describes how to configure multiarea adjacency for Open Shortest Path First version 2 (OSPFv2).
You can add more than one area to an existing OSPFv2 primary interface. The additional logical interfaces
support multiarea adjacency.
• Finding Feature Information, page 151
• Prerequisites for OSPFv2 Multiarea Adjacency, page 151
• Restrictions for OSPFv2 Multiarea Adjacency, page 152
• Information About OSPFv2 Multiarea Adjacency, page 152
• How to Configure OSPFv2 Multiarea Adjacency, page 153
• Configuration Examples for OSPFv2 Multiarea Adjacency, page 154
• Additional References for OSPFv2 Multiarea Adjacency, page 155
• Feature Information for OSPFv2 Multiarea Adjacency, page 156

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv2 Multiarea Adjacency
• Ensure that Open Shortest Path First (OSPF) is configured on the primary interface.
• Ensure that the primary interface type is point-to-point.

IP Routing: OSPF Configuration Guide
151


OSPFv2 Multiarea Adjacency
Restrictions for OSPFv2 Multiarea Adjacency

Restrictions for OSPFv2 Multiarea Adjacency
A multiarea interface has the following restrictions.
• Operates only if OSPF is configured on the primary interface.
• Exists as a logical construct over a primary interface for OSPF; however, the neighbor state on the
primary interface is independent of the multiarea interface.
• Establishes a neighbor relationship with the corresponding multiarea interface on the neighboring device.
A mixture of multiarea and primary interfaces is not supported.
• Advertises an unnumbered point-to-point link in the device link-state advertisement (LSA) for the
corresponding area when the neighbor state is full.
• Inherits all the OSPF parameters (such as, authentication) from the primary interface. You cannot
configure the parameters on a multiarea interface; however, you can configure the parameters on the
primary interface.

Information About OSPFv2 Multiarea Adjacency
OSPFv2 Multiarea Adjacency Overview
The Open Shortest Path First (OSPF) protocol allows you to divide a network topology into separate areas.
The interface on which OSPF is configured belongs to only one area at any given point of time. This causes
suboptimal routing for certain topologies, due to intra-area route preference over the interarea routes.
Open Shortest Path First version 2 (OSPFv2) allows a single physical link to be shared by multiple areas.
This creates an intra-area path in each of the corresponding areas sharing the same link. All areas have an
interface on which OSPF is configured. One of these interfaces is designated as the primary interface and
others as secondary interfaces.
The OSPFv2 Multiarea Adjacency feature allows you to configure a link on the primary interface to enable
optimized routing in multiple areas. Each multiarea interface is announced as a point-to-point unnumbered
link. The multiarea interface exists as a logical construct over an existing primary interface. The neighbor
state on the primary interface is independent of the neighbor state of the multiarea interface. The multiarea
interface establishes a neighbor relationship with the corresponding multiarea interface on the neighboring
device. You can only configure multiarea adjacency on an interface that has two OSPF speakers. In case of
native broadcast networks, the interface must be configured as an OSPF point-to-point type to enable the
interface for multiarea adjacency.
Use the ip ospf multi-area command to configure multiarea adjacency on the primary OSPFv2 interface.

IP Routing: OSPF Configuration Guide
152


OSPFv2 Multiarea Adjacency
How to Configure OSPFv2 Multiarea Adjacency

How to Configure OSPFv2 Multiarea Adjacency
Configuring OSPFv2 Multiarea Adjacency
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. ip address ip-address mask
5. ip ospf proces-id area area-id
6. ip ospf network point-to-point
7. ip ospf multi-area multi-area-id
8. ip ospf multi-area multi-area-id cost interface-cost
9. end

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

interface type number

Specifies an interface and enters interface configuration mode.

Example:
Device(config)# interface Ethernet 0/0

Step 4

ip address ip-address mask

Assigns an IP address to this interface.

Example:
Device(config)# ip address 10.0.12.1
255.255.255.0

Step 5

ip ospf proces-id area area-id
Example:
Device (config-if)# ip ospf 10 area 8

Configures the primary OSPF interface.
• The process-id argument identifies the OSPF process.
The range is from 1 to 65535.

IP Routing: OSPF Configuration Guide
153


OSPFv2 Multiarea Adjacency
Configuration Examples for OSPFv2 Multiarea Adjacency

Command or Action

Purpose
• The area-id argument identifies the OSPF area. The range
is from 0 to 4294967295, or you can use an IP address.

Step 6

ip ospf network point-to-point

Specifies the primary interface type as point-to-point.

Example:
Device (config-if)# ip ospf network
point-to-point

Step 7

ip ospf multi-area multi-area-id

Configures multiarea adjacency on the interface.
• The multi-area-id argument identifies the OSPF multiarea.
The range is from 0 to 4294967295, or you can use an IP
address.

Example:
Device (config-if)# ip ospf multi-area 11

Step 8

ip ospf multi-area multi-area-id cost interface-cost (Optional) Specifies the cost of sending a packet on an Open
Shortest Path First (OSPF) multiarea interface,
Example:
Device (config-if)# ip ospf multi-area 11
cost 10

Step 9

Exits interface configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-if)# end

Configuration Examples for OSPFv2 Multiarea Adjacency
Example: Configuring OSPFv2 Multiarea Adjacency
Device# enable
Device# configure terminal
Device(config)# interface Ethernet 0/0
Device (config-if)# ip address 10.0.12.1 255.255.255.0
Device (config-if)# ip ospf 1 area 0
Device (config-if)# ip ospf network point-to-point
Device (config-if)# ip ospf multi-area 2
Device (config-if)# ip ospf multi-area 2 cost 10
Device (config-if)# end

The following is a sample output from the show ip ospf 2 multi-area command.
Device# show ip ospf 2 multi-area
OSPF_MA1 is up, line protocol is up
Primary Interface Ethernet0/0, Area 2
Interface ID 2
MTU is 1500 bytes
Neighbor Count is 1

IP Routing: OSPF Configuration Guide
154


OSPFv2 Multiarea Adjacency
Additional References for OSPFv2 Multiarea Adjacency

The following is a sample output from the show ip ospf interface command.
Device# show ip ospf interface
Ethernet0/0 is up, line protocol is up
Internet Address 10.0.12.1/24, Area 0, Attached via Interface Enable
Process ID 1, Router ID 10.0.0.2, Network Type POINT_TO_POINT, Cost: 10
Topology-MTID
Cost
Disabled
Shutdown
Topology Name
0
10
no
no
Base
Enabled by interface config, including secondary ip addresses
Transmit Delay is 1 sec, State POINT_TO_POINT
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
oob-resync timeout 40
Hello due in 00:00:06
Supports Link-local Signaling (LLS)
Cisco NSF helper support enabled
IETF NSF helper support enabled
Can be protected by per-prefix Loop-Free FastReroute
Can be used for per-prefix Loop-Free FastReroute repair paths
Index 2/2, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.0.0.1
Suppress hello for 0 neighbor(s)
Multi-area interface Count is 1
OSPF_MA1 interface exists in area 2 Neighbor Count is 1
OSPF_MA1 is up, line protocol is up
Interface is unnumbered. Using address of Ethernet0/0 (10.0.12.1), Area 2, Attached via
Multi-area
Process ID 1, Router ID 10.0.0.2, Network Type POINT_TO_POINT, Cost: 10
Topology-MTID
Cost
Disabled
Shutdown
Topology Name
0
10
no
no
Base
Transmit Delay is 1 sec, State POINT_TO_POINT
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
oob-resync timeout 40
Hello due in 00:00:06
Supports Link-local Signaling (LLS)
Cisco NSF helper support enabled
IETF NSF helper support enabled
Can be protected by per-prefix Loop-Free FastReroute
Can be used for per-prefix Loop-Free FastReroute repair paths
Index 1/3, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 2
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.0.0.1
Suppress hello for 0 neighbor(s)

Additional References for OSPFv2 Multiarea Adjacency
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Protocol-independent features that work with OSPF “Configuring IP Routing Protocol-Independent
Features” module

IP Routing: OSPF Configuration Guide
155


OSPFv2 Multiarea Adjacency
Feature Information for OSPFv2 Multiarea Adjacency

RFCs
RFC

Title

RFC 5185

OSPF Multi-Area Adjacency, May 2008

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

Feature Information for OSPFv2 Multiarea Adjacency
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 16: Feature Information for OSPFv2 Multiarea Adjacency

Feature Name

Releases

Feature Information

OSPFv2 Multiarea Adjacency

Cisco IOS XE Release
3.10S

OSPFv2 multiarea adjacency allows you
to configure a link on the primary interface
in multiple OSPF areas to enable optimized
routing.
The following commands were introduced
or modified: ip ospf multi-area, ip ospf
multi-area cost, and show ip ospf
multi-area.

IP Routing: OSPF Configuration Guide
156
