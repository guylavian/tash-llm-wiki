---
title: "OSPFv3 Multiarea Adjacency"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-multiarea-adjacency
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 53 OSPFv3 Multiarea Adjacency The OSPFv3 Multiarea Adjacency feature allows you to configure a link that multiple Open Shortest Path First version 3 (OSPFv3) areas can share to enable optimized routing. You can add more than one area to an existing OSPFv3 primary interface. • Finding Feature Information, page 497 • Prerequisites for OSPFv3 Multiarea Adjacency, page 497 • Restrictions for"
---

# OSPFv3 Multiarea Adjacency

CHAPTER

53

OSPFv3 Multiarea Adjacency
The OSPFv3 Multiarea Adjacency feature allows you to configure a link that multiple Open Shortest Path
First version 3 (OSPFv3) areas can share to enable optimized routing. You can add more than one area to
an existing OSPFv3 primary interface.
• Finding Feature Information, page 497
• Prerequisites for OSPFv3 Multiarea Adjacency, page 497
• Restrictions for OSPFv3 Multiarea Adjacency, page 498
• Information About OSPFv3 Multiarea Adjacency, page 498
• How to Configure OSPFv3 Multiarea Adjacency, page 499
• Verifying OSPFv3 Multiarea Adjacency, page 500
• Configuration Examples for OSPFv3 Multiarea Adjacency, page 501
• Additional References for OSPFv3 Multiarea Adjacency, page 502
• Feature Information for OSPFv3 Multiarea Adjacency, page 503

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv3 Multiarea Adjacency
• Ensure that Open Shortest Path First version 3 (OSPFv3) is configured on the primary interface.
• Ensure that the primary interface type is point-to-point.

IP Routing: OSPF Configuration Guide
497


OSPFv3 Multiarea Adjacency
Restrictions for OSPFv3 Multiarea Adjacency

Restrictions for OSPFv3 Multiarea Adjacency
• A multiarea interface operates only if OSPFv3 is configured on the primary interface and the OSPFv3
network type of the primary interface is point-to-point.
• A multiarea interface exists as a logical construct over a primary interface for OSPFv3; however, the
neighbor state on the primary interface is independent of the multiarea interface.
• A multiarea interface establishes a neighbor relationship with the corresponding multiarea interface on
the neighboring device. A mixture of multiarea and primary interfaces is not supported.
• A multiarea interface advertises a point-to-point connection to another device in the device link-state
advertisement (LSA) for the corresponding area when the neighbor state is full.
• A multiarea interface inherits all the OSPFv3 parameters (such as, authentication) from the primary
interface. You cannot configure the parameters on a multiarea interface; however, you can configure
the parameters on the primary interface.

Information About OSPFv3 Multiarea Adjacency
OSPFv3 Multiarea Adjacency Overview
Open Shortest Path First version 3 (OSPFv3) allows a single physical link to be shared by multiple areas.
This creates an intra-area path in each of the corresponding areas sharing the same link. All areas have an
interface on which you can configure OSPFv3. One of these interfaces is designated as the primary interface
and others as secondary interfaces.
The OSPFv3 Multiarea Adjacency feature allows you to configure a link on the primary interface to enable
optimized routing in multiple areas. Each multiarea interface is announced as a point-to-point unnumbered
link. The multiarea interface exists as a logical construct over an existing primary interface. The neighbor
state on the primary interface is independent of the neighbor state of the multiarea interface. The multiarea
interface establishes a neighbor relationship with the corresponding multiarea interface on the neighboring
device. You can only configure multiarea adjacency on an interface that has two OSPFv3 speakers.
Use the ospfv3 multi-area command to configure multiarea adjacency on the primary OSPFv3 interface.

IP Routing: OSPF Configuration Guide
498


OSPFv3 Multiarea Adjacency
How to Configure OSPFv3 Multiarea Adjacency

How to Configure OSPFv3 Multiarea Adjacency
Configuring OSPFv3 Multiarea Adjacency
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. ipv6 enable
5. ospfv3 multi-area multi-area-id
6. ospfv3 multi-area multi-area-id cost interface-cost
7. ospfv3 process-id ipv6 area area-id
8. serial restart-delay count
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

Specifies the interface type and number.

Example:
Device(config)# interface serial 2/0

Step 4

ipv6 enable

Enables IPv6 processing on an interface that has not been configured
with an explicit IPv6 address.

Example:
Device(config-if)# ipv6 enable

Step 5

ospfv3 multi-area multi-area-id
Example:
Device(config-if)# ospfv3 multi-area 100

Configures multiarea adjacency on the interface.
• The multi-area-id argument identifies the OSPFv3 multiarea.
The range is from 0 to 4294967295, or you can use an IP
address.

IP Routing: OSPF Configuration Guide
499


OSPFv3 Multiarea Adjacency
Verifying OSPFv3 Multiarea Adjacency

Step 6

Command or Action

Purpose

ospfv3 multi-area multi-area-id cost
interface-cost

(Optional) Specifies the cost of sending a packet on an OSPFv3
multiarea interface. Use this command to specify the cost only if you
want the cost of the multiarea interface to be different than the cost
of the primary interface.

Example:
Device(config-if)# ospfv3 multi-area 100
cost 512

Step 7

ospfv3 process-id ipv6 area area-id
Example:
Device(config-if)# ospfv3 1 ipv6 area 0

Configures the OSPFv3 interface.
• The process-id argument identifies the OSPF process. The
range is from 1 to 65535.
• The area-id argument identifies the OSPF area. The range is
from 0 to 4294967295, or you can use an IP address.

Step 8

serial restart-delay count

Sets the amount of time that the router waits before trying to bring
up a serial interface when it goes down. The count argument specifies
the frequency (in seconds) at which that hardware is reset. The range
Example:
Device(config-if)# serial restart-delay is from 0 to 900.
0

Step 9

Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Verifying OSPFv3 Multiarea Adjacency
SUMMARY STEPS
1. enable
2. show ospfv3 interface brief
3. show ospfv3 multi-area
4. show ospfv3 interface

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device> enable

IP Routing: OSPF Configuration Guide
500

• Enter your password if prompted.


OSPFv3 Multiarea Adjacency
Configuration Examples for OSPFv3 Multiarea Adjacency

Step 2

Command or Action

Purpose

show ospfv3 interface brief

Displays brief information about Open Shortest Path First
version 3 (OSPFv3) interfaces.

Example:
Device# show ospfv3 interface brief

Step 3

Displays information about OSPFv3 multiarea interfaces.

show ospfv3 multi-area
Example:
Device# show ospfv3 multi-area

Step 4

Displays information about OSPFv3 interfaces.

show ospfv3 interface
Example:
Device# show ospfv3 interface

Configuration Examples for OSPFv3 Multiarea Adjacency
Example: OSPFv3 Multiarea Adjacency Configuration
Device> enable
Device# configure terminal
Device(config)# interface serial 2/0
Device(config-if)# ipv6 enable
Device(config-if)# ospfv3 multi-area 100
Device(config-if)# ospfv3 multi-area 100 cost 512
Device(config-if)# ospfv3 1 ipv6 area 0
Device(config-if)# serial restart-delay 0
Device(config-if)# end

Example: Verifying OSPFv3 Multiarea Adjacency
Sample Output for the show ospfv3 interface brief Command
To display brief information about Open Shortest Path First version 3 (OSPFv3) interfaces, use the show
ospfv3 interface brief command in privileged EXEC mode.
Device# show ospfv3 interface brief
Interface PID Area AF
Se2/0
1
0
ipv6
MA2 1
1
100 ipv6

Cost
64
512

State Nbrs F/C
P2P
1/1
P2P
1/1

IP Routing: OSPF Configuration Guide
501


OSPFv3 Multiarea Adjacency
Additional References for OSPFv3 Multiarea Adjacency

Sample Output for the show ospfv3 multi-area Command
To display information about OSPFv3 multiarea interfaces, use the show ospfv3 multi-area command in
privileged EXEC mode.
Device# show ospfv3 multi-area
OSPFV3_MA2 is up, line protocol is up
Primary Interface Serial2/0, Area 100
Interface ID 10
MTU is 1500 bytes
Neighbor Count is 1

Sample Output for the show ospfv3 interface Command
To display information about OSPFv3 interfaces, use the show ospfv3 interface command in privileged
EXEC mode.
Device# show ospfv3 interface
Serial2/0 is up, line protocol is up
Link Local Address 2001:DB8:0:ABCD::1, Interface ID 10
Area 0, Process ID 1, Instance ID 0, Router ID 10.0.0.12
Network Type POINT_TO_POINT, Cost: 64
Transmit Delay is 1 sec, State POINT_TO_POINT
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:07
Graceful restart helper support enabled
Index 1/1/1, flood queue length 0
Next 0x0(0)/0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.0.0.22
Suppress hello for 0 neighbor(s)
Multi-area interface Count is 1
OSPFV3_MA2 interface exists in area 100 Neighbor Count is 1
OSPFV3_MA2 is up, line protocol is up
Link Local Address 2001:DB8:0:ABCD::1, Interface ID 10
Area 100, Process ID 1, Instance ID 0, Router ID 10.0.0.12
Network Type POINT_TO_POINT, Cost: 512
Transmit Delay is 1 sec, State POINT_TO_POINT
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:08
Graceful restart helper support enabled
Index 1/1/2, flood queue length 0
Next 0x0(0)/0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.0.0.22

Additional References for OSPFv3 Multiarea Adjacency
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

IPv6 commands

Cisco IOS IPv6 Command Reference

IP Routing: OSPF Configuration Guide
502


OSPFv3 Multiarea Adjacency
Feature Information for OSPFv3 Multiarea Adjacency

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

Feature Information for OSPFv3 Multiarea Adjacency
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Feature Name
OSPFv3 Multiarea Adjacency

Releases

Feature Information
The OSPFv3 Multiarea Adjacency
feature allows you to configure a
link that multiple Open Shortest
Path First version 3 (OSPFv3)
areas can share to enable optimized
routing. You can add more than
one area to an existing OSPFv3
primary interface.

IP Routing: OSPF Configuration Guide
503


OSPFv3 Multiarea Adjacency
Feature Information for OSPFv3 Multiarea Adjacency

IP Routing: OSPF Configuration Guide
504
