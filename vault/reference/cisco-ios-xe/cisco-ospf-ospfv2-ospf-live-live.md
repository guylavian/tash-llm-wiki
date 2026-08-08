---
title: "OSPFv2-OSPF Live-Live"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv2-ospf-live-live
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 20 OSPFv2-OSPF Live-Live The OSPFv2-OSPF Live-Live feature delivers multicast streams over non overlapping paths to various applications. The multicast traffic is split into multiple streams at the beginning of a protected network. All streams flow over non overlapping paths so that when a link failure occurs on one path, multicast traffic is still delivered through other paths. All stre"
---

# OSPFv2-OSPF Live-Live

CHAPTER

20

OSPFv2-OSPF Live-Live
The OSPFv2-OSPF Live-Live feature delivers multicast streams over non overlapping paths to various
applications. The multicast traffic is split into multiple streams at the beginning of a protected network. All
streams flow over non overlapping paths so that when a link failure occurs on one path, multicast traffic is
still delivered through other paths. All streams are merged back at the end of the protected network. This
module describes how to configure the OSPFv2-OSPF Live-Live feature.
• Finding Feature Information, page 213
• Information About OSPFv2-OSPF Live-Live, page 213
• How to Configure OSPFv2-OSPF Live-Live, page 215
• Configuration Examples for OSPFv2-OSPF Live-Live, page 218
• Additional References for OSPFv2-OSPF Live-Live, page 219
• Feature Information for OSPFv2-OSPF Live-Live, page 220

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPFv2-OSPF Live-Live
Overview of OSPFv2-OSPF Live-Live
Many new applications driving the growth of networking market are multicast based. Applications such as
Internet Protocol television (IPTV) are typically associated with simultaneously delivering massive amount

IP Routing: OSPF Configuration Guide
213


OSPFv2-OSPF Live-Live
Overview of OSPFv2-OSPF Live-Live

of sensitive data streams to large audiences. Packet drop is a critical issue in multimedia traffic. There is a
demand to reduce multicast traffic loss to the range of milliseconds or to zero packet loss. The zero packet
loss solution for multicast in case of single link failure is also known as live-live.
In a live-live network, multicast streams (typically two flows) form their own reverse path forwarding
(RPF)/shortest path trees (SPT) over diversified physical links, so that failure on one link does not affect
multicast traffic on other link. The existing multi topology technology in Cisco IOS software supports the
multiple multicast topologies.
The OSPFv2-OSPF Live-Live feature enables the protocol independent multicast (PIM) to handle multiple
multicast topologies. When a multicast topology is created and enabled on OSPF, IP prefixes on each topology
are injected into topology-based Routing Information Base (RIB). PIM then decides which RIB to use for
RPF lookup.
PIM RPF topology is a collection of routes used by PIM to perform the RPF operation when building shared
or source trees. In a multi topology environment, multiple RPF topologies can be created in the same network.
A particular source may be reachable in only one of the topologies or in several of them through different
paths.
To select the RPF topology for a particular multicast distribution tree, consider the following:
1 Configure a policy that maps a group range to a topology. When RPF information needs to be resolved
for the RP or the sources for a group within the range, the RPF lookup takes place in the specified topology.
This can be used for PIM Sparse Mode (PIM-SM)/source-specific multicast (SSM)/Bidirectional(Bidir)
PIM.
2 Configure a policy that maps a source prefix range to a topology. This can be used for PIM-SM and
PIM-SSM.
3 Use the topology identified by the Join Attribute encoding in the received PIM packets.
The PIM Join Attribute extends PIM signaling to identify a topology that should be used when constructing
a particular multicast distribution tree. For more details on the PIM Join Attribute, see PIM Multi-Topology
ID (MT-ID) Join-Attribute IEEE draft.

IP Routing: OSPF Configuration Guide
214


OSPFv2-OSPF Live-Live
How to Configure OSPFv2-OSPF Live-Live

How to Configure OSPFv2-OSPF Live-Live
Configuring OSPFv2-OSPF Live-Live
SUMMARY STEPS
1. enable
2. configure terminal
3. ip multicast-routing
4. ip multicast rpf multitopology
5. global-address-family ipv4 multicast
6. topology {topology-A | topology-B}
7. exit
8. interface type number
9. ip address address mask
10. ip pim sparse-dense-mode
11. ip ospf process-id area area-id
12. topology ipv4 multicast topology-name
13. exit
14. router ospf process-id
15. network ip-adddress mask area area-id
16. address-family ipv4 multicast
17. topology topology-name tid topology-id
18. end
19. configure terminal
20. ip multicast topology multicast topology-name tid topology-id
21. ip multicast rpf select topology multicast topology-name access-list number
22. ip access-list extended access-list-number
23. permit ip any ip-adddress
24. end
25. show ip multicast topology multicast topology-name
26. debug ip multicast topology

IP Routing: OSPF Configuration Guide
215


OSPFv2-OSPF Live-Live
Configuring OSPFv2-OSPF Live-Live

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

ip multicast-routing

Enables IP multicast routing.

Example:
Device(config)# ip multicast-routing

Step 4

ip multicast rpf multitopology

Enables Multi Topology Routing (MTR) support for IP
multicast routing.

Example:
Device(config)# ip multicast rpf multitopology

Step 5

global-address-family ipv4 multicast

Enters global address family configuration mode and
configures multi topology routing.

Example:
Device(config)# global-address-family ipv4
multicast

Step 6

topology {topology-A | topology-B}

Configures an OSPF process to route IP traffic under the
specified topology instance.

Example:
Device(config-af)# topology live-A

Step 7

exit

Exits address family configuration mode and returns to global
configuration mode.

Example:
Device(config-af)# exit

Step 8

interface type number

Configures an interface type and enters interface configuration
mode.

Example:
Device(config)# interface Gigabitethernet 1/0

Step 9

ip address address mask

Sets a primary or secondary IP address for an interface.

Example:
Device(config-if)# ip address 192.108.1.27
255.255.255.0

Step 10

ip pim sparse-dense-mode
Example:
Device(config-if)# ip pim sparse-dense-mode

IP Routing: OSPF Configuration Guide
216

Enables PIM on an interface and treats the interface in either
sparse mode or dense mode of operation, depending on which
mode the multicast group operates in.


OSPFv2-OSPF Live-Live
Configuring OSPFv2-OSPF Live-Live

Step 11

Command or Action

Purpose

ip ospf process-id area area-id

Enables OSPFv2 on an interface.

Example:
Device(config-if)# ip ospf 10 area 0

Step 12

topology ipv4 multicast topology-name

Configures a multi topology instance on an interface.

Example:
Device(config-if)# topology ipv4 multicast
live-A

Step 13

exit
Example:
Device(config-if)# exit

Step 14

router ospf process-id

Exits interface configuration mode and enters global
configuration mode.
• Repeat Steps 9 to 12 to configure the next topology
(topology ipv4 multicast live-B).
Enables OSPF routing and enters router configuration mode.

Example:
Device(config)# router ospf 102

Step 15

network ip-adddress mask area area-id

Defines an interface on which OSPF runs and defines the area
ID for that interface.

Example:
Device(config-router)# network 192.168.129.16
0.0.0.3 area 20

Step 16

address-family ipv4 multicast

Enters router address family configuration mode and
configures OSPF to exchange IPv4 multicast prefixes.

Example:
Device(config-router)# address-family ipv4
multicast

Step 17

topology topology-name tid topology-id
Example:
Device(config-router-af)# topology live-A tid
100

Step 18

end

Configures an OSPF process to route IP traffic under the
specified topology instance.
• Repeat this step to configure the OSPF process to route
IP traffic under another topology instance (topology
live-B tid 200).
Exits router address family configuration mode and returns
to privileged EXEC mode.

Example:
Device(config-router-af)# end

Step 19

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 20

ip multicast topology multicast topology-name tid Configures topology selection for the multicast streams.
topology-id

IP Routing: OSPF Configuration Guide
217


OSPFv2-OSPF Live-Live
Configuration Examples for OSPFv2-OSPF Live-Live

Command or Action
Example:

Purpose
• Repeat this step to configure another topology (ip
multicast topology multicast live-B tid 200).

Device(config)# ip multicast topology
multicast live-A tid 100

Step 21

ip multicast rpf select topology multicast
topology-name access-list number
Example:
Device(config)# ip multicast rpf select
topology multicast topology live-A 111

Step 22

ip access-list extended access-list-number
Example:

Associates a multicast topology with a multicast group with
a specific route entry.
• Repeat this step to associate the topology with another
multicast group (ip multicast rpf select topology
multicast live-B 122).
Defines an IP access list to enable filtering for packets with
IP helper-address destinations and enters extended named
access list configuration mode.

Device(config)# ip access-list extended 111

Step 23

permit ip any ip-adddress
Example:
Device(config-ext-nacl)# permit ip any
203.0.113.1

Step 24

Sets condition to allow a packet to pass a named IP access
list.
• Repeat Steps 22 and 23 to define another IP access list
and to set conditions to allow a packet to pass another
named IP access list.
Exits extended named access list configuration mode and
enters privileged EXEC mode.

end
Example:
Device(config-ext-nacl)# end

Step 25

show ip multicast topology multicast topology-name Displays topology information for multicast streams.
Example:
Device# show ip multicast topology multicast
live-A

Step 26

debug ip multicast topology

Enables debugging output for multicast stream topology.

Example:
Device# debug ip multicast topology

Configuration Examples for OSPFv2-OSPF Live-Live
Example: Configuring OSPFv2-OSPF Live-Live
ip multicast-routing
!
ip multicast rpf multitopology

IP Routing: OSPF Configuration Guide
218


OSPFv2-OSPF Live-Live
Additional References for OSPFv2-OSPF Live-Live

!
global-address-family ipv4 multicast
topology live-A
topology live-B
int gigabitethernet 1/0
ip address 192.0.2.1 255.255.255.0
ip pim sparse-dense-mode
ip ospf 10 area 20
topology ipv4 multicast live-A
!
int gigabitethernet 2/0
ip address 192.0.2.2 255.255.255.0
ip pim sparse-dense-mode
ip ospf 11 area 21
topology ipv4 multicast live-B
!
router ospf 1
network 192.168.129.16 0.0.0.3 area 20
address-family ipv4 multicast
!!
topology live-A tid 10
topology live-B tid 20
!
!!
ip multicast topology multicast live-A tid 100
ip multicast topology multicast live-B tid 200
!
!!
ip multicast rpf select topology multicast live-A 111
ip multicast rpf select topology multicast live-B 122
!
ip access-list extended 111
permit ip any 203.0.113.254
ip access-list extended 122
permit ip any 203.0.113.251

Additional References for OSPFv2-OSPF Live-Live
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

Configuring OSPF features

IP Routing: OSPF Configuration Guide

IP Routing: OSPF Configuration Guide
219


OSPFv2-OSPF Live-Live
Feature Information for OSPFv2-OSPF Live-Live

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

Feature Information for OSPFv2-OSPF Live-Live
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 23: Feature Information for OSPFv2-OSPF Live-Live

Feature Name

Releases

Feature Information

OSPFv2-OSPF Live-Live

Cisco IOS XE Release 3.11S

The OSPFv2-OSPF Live-Live
feature delivers multicast streams
over non overlapping paths to
various applications. The multicast
traffic is split into multiple streams
at the beginning of a protected
network. All streams flow over non
overlapping paths so that when a
link failure occurs on one path,
multicast traffic is still delivered
through other paths. All streams
are merged back at the end of the
protected network.
No commands were introduced or
modified.

IP Routing: OSPF Configuration Guide
220
