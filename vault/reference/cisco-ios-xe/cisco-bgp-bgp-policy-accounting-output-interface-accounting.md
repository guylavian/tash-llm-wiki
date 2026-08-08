---
title: "BGP Policy Accounting Output Interface Accounting"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-policy-accounting-output-interface-accounting
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 36 BGP Policy Accounting Output Interface Accounting Border Gateway Protocol (BGP) policy accounting (PA) measures and classifies IP traffic that is sent to, or received from, different peers. Policy accounting was previously available on an input interface only. The BGP Policy Accounting Output Interface Accounting feature introduces several extensions to enable BGP PA on an output inte"
---

# BGP Policy Accounting Output Interface Accounting

CHAPTER

36

BGP Policy Accounting Output Interface
Accounting
Border Gateway Protocol (BGP) policy accounting (PA) measures and classifies IP traffic that is sent to, or
received from, different peers. Policy accounting was previously available on an input interface only. The
BGP Policy Accounting Output Interface Accounting feature introduces several extensions to enable BGP
PA on an output interface and to include accounting based on a source address for both input and output traffic
on an interface. Counters based on parameters such as community list, autonomous system number, or
autonomous system path are assigned to identify the IP traffic.
• Finding Feature Information, on page 599
• Prerequisites for BGP PA Output Interface Accounting, on page 599
• Information About BGP PA Output Interface Accounting, on page 600
• How to Configure BGP PA Output Interface Accounting, on page 601
• Configuration Examples for BGP PA Output Interface Accounting, on page 607
• Additional References, on page 608
• Feature Information for BGP Policy Accounting Output Interface Accounting, on page 609
• Glossary, on page 610

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP PA Output Interface Accounting
Before using the BGP Policy Accounting Output Interface Accounting feature, you must enable BGP and
Cisco Express Forwarding or distributed CEF on the router.

IP Routing: BGP Configuration Guide
599


BGP Policy Accounting Output Interface Accounting
Information About BGP PA Output Interface Accounting

Information About BGP PA Output Interface Accounting
BGP PA Output Interface Accounting
Policy accounting using BGP measures and classifies IP traffic that is sent to, or received from, different
peers. Originally, BGP PA was available on an input interface only. BGP PA output interface accounting
introduces several extensions to enable BGP PA on an output interface and to include accounting based on a
source address for both input and output traffic on an interface. Counters based on parameters such as
community list, autonomous system number, or autonomous system path are assigned to identify the IP traffic.
Using the BGP table-map command, prefixes added to the routing table are classified by BGP attribute,
autonomous system number, or autonomous system path. Packet and byte counters are incremented per input
or output interface. A Cisco policy-based classifier maps the traffic into one of eight possible buckets that
represent different traffic classes.
Using BGP PA, you can account for traffic according to its origin or the route it traverses. Service providers
(SPs) can identify and account for all traffic by customer and can bill accordingly. In the figure below, BGP
PA can be implemented in Router A to measure packet and byte volumes in autonomous system buckets.
Customers are billed appropriately for traffic that is routed from a domestic, international, or satellite source.
Figure 60: Sample Topology for BGP Policy Accounting

BGP policy accounting using autonomous system numbers can be used to improve the design of network
circuit peering and transit agreements between Internet service providers (ISPs).

Benefits of BGP PA Output Interface Accounting
Accounting for IP Traffic Differentially
BGP policy accounting classifies IP traffic by autonomous system number, autonomous system path, or
community list string, and increments packet and byte counters. Policy accounting can also be based on the

IP Routing: BGP Configuration Guide
600


BGP Policy Accounting Output Interface Accounting
How to Configure BGP PA Output Interface Accounting

source address. Service providers can account for traffic and apply billing according to the origin of the traffic
or the route that specific traffic traverses.
Efficient Network Circuit Peering and Transit Agreement Design
Implementing BGP policy accounting on an edge router can highlight potential design improvements for
peering and transit agreements.

How to Configure BGP PA Output Interface Accounting
Specifying the Match Criteria for BGP PA
The first task in configuring BGP PA is to specify the criteria that must be matched. Community lists,
autonomous system paths, or autonomous system numbers are examples of BGP attributes that can be specified
and subsequently matched using a route map. Perform this task to specify the BGP attribute to use for BGP
PA and to create the match criteria in a route map.
SUMMARY STEPS
1. enable
2. configure terminal
3. ip community-list {standard-list-number | expanded-list-number [regular-expression] | {standard |
expanded} community-list-name} {permit | deny} {community-number | regular-expression}
4. route-map map-name [permit | deny] [sequence-number]
5. match community-list community-list-number [exact]
6. set traffic-index bucket-number
7. exit
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

ip community-list {standard-list-number |
expanded-list-number [regular-expression] | {standard |
expanded} community-list-name} {permit | deny}
{community-number | regular-expression}

Creates a community list for BGP and controls access to it.
• Repeat this step for each community to be specified.

Example:

IP Routing: BGP Configuration Guide
601


BGP Policy Accounting Output Interface Accounting
Classifying the IP Traffic and Enabling BGP PA

Command or Action

Purpose

Device(config)# ip community-list 30 permit 100:190

Step 4

route-map map-name [permit | deny] [sequence-number] Enters route-map configuration mode and defines the
conditions for policy routing.
Example:
• The map-name argument identifies a route map.
Device(config)# route-map set_bucket permit 10

• The optional permit and deny keywords work with
the match and set criteria to control how the packets
are accounted for.
• The optional sequence-number argument indicates the
position that a new route map is to have in the list of
route maps already configured with the same name.

Step 5

match community-list community-list-number [exact]

Matches a BGP community.

Example:
Router(config-route-map)# match community-list 30

Step 6

set traffic-index bucket-number
Example:

Indicates where to output packets that pass a match clause
of a route map for BGP policy accounting.

Device(config-route-map)# set traffic-index 2

Step 7

Exits route-map configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-route-map)# exit

Classifying the IP Traffic and Enabling BGP PA
After a route map has been defined to specify match criteria, you must configure a way to classify the IP
traffic before enabling BGP policy accounting.
Using the table-map command, BGP classifies each prefix that it adds to the routing table according to the
match criteria. When the bgp-policy accounting command is configured on an interface, BGP policy accounting
is enabled.
Perform this task to classify the IP traffic and enable BGP policy accounting.
SUMMARY STEPS
1.
2.
3.
4.
5.
6.

enable
configure terminal
router bgp as-number
table-map route-map-name
network network-number [mask network-mask]
neighbor ip-address remote-as as-number

IP Routing: BGP Configuration Guide
602


BGP Policy Accounting Output Interface Accounting
Classifying the IP Traffic and Enabling BGP PA

7.
8.
9.
10.
11.

exit
interface type number
ip address ip-address mask
bgp-policy accounting [input | output] [source]
exit

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
Device(config)# router bgp 65000

Step 4

table-map route-map-name

Configures a BGP routing process and enters router
configuration mode for the specified routing process.
• The as-number argument identifies a BGP
autonomous system number.
Classifies BGP prefixes entered in the routing table.

Example:
Device(config-router)# table-map set_bucket

Step 5

network network-number [mask network-mask]
Example:

Specifies a network to be advertised by the BGP routing
process.

Device(config-router)# network 10.15.1.0 mask
255.255.255.0

Step 6

neighbor ip-address remote-as as-number
Example:

Specifies a BGP peer by adding an entry to the BGP
routing table.

Device(config-router)# neighbor 10.14.1.1
remote-as 65100

Step 7

exit
Example:

Exits router configuration mode and returns to global
configuration mode.

Device(config-router)# exit

Step 8

interface type number
Example:

Specifies the interface type and number and enters interface
configuration mode.

IP Routing: BGP Configuration Guide
603


BGP Policy Accounting Output Interface Accounting
Verifying BGP Policy Accounting

Command or Action

Purpose
• The type argument identifies the type of interface.

Device(config)# interface POS 7/0

• The number argument identifies the slot and port
numbers of the interface. The space between the
interface type and number is optional.
Step 9

ip address ip-address mask

Configures the interface with an IP address.

Example:
Device(config-if)# ip-address 10.15.1.2
255.255.255.0

Step 10

bgp-policy accounting [input | output] [source]
Example:
Device(config-if)# bgp-policy accounting input
source

Enables BGP policy accounting for the interface.
• Use the optional input or output keyword to account
for traffic either entering or leaving the router. By
default, BGP policy accounting is based on traffic
entering the router.
• Use the optional source keyword to account for traffic
based on source address.

Step 11

Exits interface configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-if)# exit

Verifying BGP Policy Accounting
Perform this task to verify that BGP policy accounting is operating.
SUMMARY STEPS
1.
2.
3.
4.

show ip cef [network [mask]] [detail]
show ip bgp [network] [network-mask] [longer-prefixes]
show cef interface [type number] policy-statistics [input | output]
show cef interface [type number] [statistics] [detail]

DETAILED STEPS

Step 1

show ip cef [network [mask]] [detail]
Enter the show ip cef command with the detail keyword to learn which accounting bucket is assigned to a specified
prefix.
In this example, the output is displayed for the prefix 192.168.5.0. It shows that accounting bucket number 4 (traffic_index
4) is assigned to this prefix.
Example:

IP Routing: BGP Configuration Guide
604


BGP Policy Accounting Output Interface Accounting
Verifying BGP Policy Accounting

Device# show ip cef 192.168.5.0 detail
192.168.5.0/24, version 21, cached adjacency to POS7/2
0 packets, 0 bytes, traffic_index 4
via 10.14.1.1, 0 dependencies, recursive
next hop 10.14.1.1, POS7/2 via 10.14.1.0/30
valid cached adjacency

Step 2

show ip bgp [network] [network-mask] [longer-prefixes]
Enter the show ip bgp command for the same prefix used in Step 1--192.168.5.0--to learn which community is assigned
to this prefix.
In this example, the output is displayed for the prefix 192.168.5.0. It shows that the community of 100:197 is assigned
to this prefix.
Example:
Device# show ip bgp 192.168.5.0
BGP routing table entry for 192.168.5.0/24, version 2
Paths: (1 available, best #1)
Not advertised to any peer
100
10.14.1.1 from 10.14.1.1 (32.32.32.32)
Origin IGP, metric 0, localpref 100, valid, external, best
Community: 100:197

Step 3

show cef interface [type number] policy-statistics [input | output]
Displays the per-interface traffic statistics.
In this example, the output shows the number of packets and bytes that have been assigned to each accounting bucket:
Example:
Device# show cef interface policy-statistics input
FastEthernet1/0/0 is up (if_number 6)
Corresponding hwidb fast_if_number 6
Corresponding hwidb firstsw->if_number 6
BGP based Policy accounting on input is enabled
Index
Packets
Bytes
1
9999
999900
2
0
0
3
0
0
4
0
0
5
0
0
6
0
0
7
0
0
8
0
0
9
0
0
10
0
0
11
0
0
12
0
0
13
0
0
14
0
0
15
0
0
16
0
0
17
0
0
18
0
0
19
0
0

IP Routing: BGP Configuration Guide
605


BGP Policy Accounting Output Interface Accounting
Verifying BGP Policy Accounting

20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64

Step 4

0
0
0
0
0
0
0
0
0
0
0
0
0
0
1234
0
0
0
0
0
0
0
0
0
0
1000
0
0
0
0
0
0
0
0
5123
0
0
0
0
0
0
0
0
0
0

0
0
0
0
0
0
0
0
0
0
0
0
0
0
123400
0
0
0
0
0
0
0
0
0
0
100000
0
0
0
0
0
0
0
0
1198782
0
0
0
0
0
0
0
0
0
0

show cef interface [type number] [statistics] [detail]
Displays the state of BGP policy accounting on a specified interface.
In this example, the output shows that BGP policy accounting has been configured to be based on input traffic at Fast
Ethernet interface 1/0/0:
Example:
Device# show cef interface Fast Ethernet 1/0/0
FastEthernet1/0/0 is up (if_number 6)
Corresponding hwidb fast_if_number 6
Corresponding hwidb firstsw->if_number 6
Internet address is 10.1.1.1/24
ICMP redirects are always sent
Per packet load-sharing is disabled
IP unicast RPF check is disabled

IP Routing: BGP Configuration Guide
606


BGP Policy Accounting Output Interface Accounting
Configuration Examples for BGP PA Output Interface Accounting

Inbound access list is not set
Outbound access list is not set
IP policy routing is disabled
BGP based policy accounting on input is enabled
BGP based policy accounting on output is disabled
Hardware idb is FastEthernet1/0/0 (6)
Software idb is FastEthernet1/0/0 (6)
Fast switching type 1, interface type 18
IP Distributed CEF switching enabled
IP Feature Fast switching turbo vector
IP Feature CEF switching turbo vector
Input fast flags 0x100, Output fast flags 0x0, Flags 0x0
ifindex 7(7)
Slot 1 Slot unit 0 VC -1
Transmit limit accumulator 0xE8001A82 (0xE8001A82)
IP MTU 1500

ConfigurationExamplesforBGPPAOutputInterfaceAccounting
Specifying the Match Criteria for BGP Policy Accounting Example
In the following example, BGP communities are specified in community lists, and a route map named set_bucket
is configured to match each of the community lists to a specific accounting bucket using the set traffic-index
command:
ip community-list 30 permit 100:190
ip community-list 40 permit 100:198
ip community-list 50 permit 100:197
ip community-list 60 permit 100:296
!
route-map set_bucket permit 10
match community-list 30
set traffic-index 2
!
route-map set_bucket permit 20
match community-list 40
set traffic-index 3
!
route-map set_bucket permit 30
match community-list 50
set traffic-index 4
!
route-map set_bucket permit 40
match community-list 60
set traffic-index 5

Classifying the IP Traffic and Enabling BGP Policy Accounting Example
In the following example, BGP policy accounting is enabled on POS interface 2/0/0. The policy accounting
criteria is based on the source address of the input traffic, and the table-map command is used to modify the
bucket number when the IP routing table is updated with routes learned from BGP.
router bgp 65000

IP Routing: BGP Configuration Guide
607


BGP Policy Accounting Output Interface Accounting
Additional References

table-map set_bucket
network 10.15.1.0 mask 255.255.255.0
neighbor 10.14.1.1 remote-as 65100
!
ip classless
ip bgp-community new-format
!
interface POS2/0/0
ip address 10.15.1.2 255.255.255.0
bgp-policy accounting input source
no keepalive
crc 32
clock source internal

Additional References
The following sections provide references related to the BGP policy accounting output interface accounting
feature.
Related Documents
Related Topic

Document Title

BGP commands: complete command syntax, command
mode, defaults, usage guidelines, and examples

Cisco IOS IP Routing: BGP Command
Reference

Switching commands: complete command syntax, command Cisco IOS IP Switching Command Reference
mode, defaults, usage guidelines, and examples
Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standards

Title

No new or modified standards are supported by this feature, and support for existing standards has not -been modified by this feature.
MIBs
MIBs

MIBs Link

CISCO-BGP-POLICY-ACCOUNTING-MIB To locate and download MIBs for selected platforms, Cisco
IOS XE software releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: BGP Configuration Guide
608


BGP Policy Accounting Output Interface Accounting
Feature Information for BGP Policy Accounting Output Interface Accounting

RFCs
RFCs

Title

No new or modified RFCs are supported by this feature, and support for existing RFCs has not been -modified by this feature.
Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including http://www.cisco.com/techsupport
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.
To receive security and technical information about your products, you
can subscribe to various services, such as the Product Alert Tool (accessed
from Field Notices), the Cisco Technical Services Newsletter, and Really
Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com
user ID and password.

Feature Information for BGP Policy Accounting Output Interface
Accounting
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 52: Feature Information for BGP Policy Accounting Output Interface Accounting

Feature Name

Releases

BGP Policy Accounting Cisco IOS XE
Release 2.1

Feature Information
BGP policy accounting measures and classifies IP traffic
that is sent to, or received from, different peers.
This feature was introduced on the Cisco ASR 1000 Series
Aggregation Services Routers.

IP Routing: BGP Configuration Guide
609


BGP Policy Accounting Output Interface Accounting
Glossary

Feature Name

Releases

BGP Policy Accounting Cisco IOS XE
Output Interface
Release 2.1
Accounting

Feature Information
This feature introduces several extensions to enable BGP
PA on an output interface and to include accounting based
on a source address for both input and output traffic on an
interface.
This feature was introduced on the Cisco ASR 1000 Series
Routers.
The following commands were introduced or modified for
this feature: bgp-policy, set traffic-index, show cef
interface, show cef interface policy-statistics

SNMP Support for BGP Cisco IOS XE
Policy Accounting
Release 2.1

The CISCO-BGP-POLICY-ACCOUNTING-MIB was
introduced.
This feature was introduced on the Cisco ASR 1000 Series
Routers.

Glossary
AS --autonomous system. An IP term to describe a routing domain that has its own independent routing policy
and is administered by a single authority.
BGP --Border Gateway Protocol. Interdomain routing protocol that exchanges reachability information with
other BGP systems.
CEF --Cisco Express Forwarding.
dCEF --distributed Cisco Express Forwarding.

IP Routing: BGP Configuration Guide
610
