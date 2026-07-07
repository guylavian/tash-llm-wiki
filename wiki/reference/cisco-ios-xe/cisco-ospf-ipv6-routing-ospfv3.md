---
title: "IPv6 Routing: OSPFv3"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ipv6-routing-ospfv3
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 3 IPv6 Routing: OSPFv3 Open Shortest Path First version 3 (OSPFv3) is an IPv4 and IPv6 link-state routing protocol that supports IPv6 and IPv4 unicast address families (AFs). • Finding Feature Information, page 57 • Prerequisites for IPv6 Routing: OSPFv3, page 57 • Restrictions for IPv6 Routing: OSPFv3, page 58 • Information About IPv6 Routing: OSPFv3, page 58 • How to Configure Load Bal"
---

# IPv6 Routing: OSPFv3

CHAPTER

3

IPv6 Routing: OSPFv3
Open Shortest Path First version 3 (OSPFv3) is an IPv4 and IPv6 link-state routing protocol that supports
IPv6 and IPv4 unicast address families (AFs).
• Finding Feature Information, page 57
• Prerequisites for IPv6 Routing: OSPFv3, page 57
• Restrictions for IPv6 Routing: OSPFv3, page 58
• Information About IPv6 Routing: OSPFv3, page 58
• How to Configure Load Balancing in OSPFv3, page 61
• Configuration Examples for Load Balancing in OSPFv3, page 67
• Additional References, page 68
• Feature Information for IPv6 Routing: OSPFv3, page 69

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for IPv6 Routing: OSPFv3
• Complete the OSPFv3 network strategy and planning for your IPv6 network. For example, you must
decide whether multiple areas are required.
• Enable IPv6 unicast routing.
• Enable IPv6 on the interface.

IP Routing: OSPF Configuration Guide
57


IPv6 Routing: OSPFv3
Restrictions for IPv6 Routing: OSPFv3

Restrictions for IPv6 Routing: OSPFv3
When running a dual-stack IP network with OSPF version 2 for IPv4 and OSPFv3, be careful when changing
the defaults for commands used to enable OSPFv3. Changing these defaults may affect your OSPFv3 network,
possibly adversely.

Information About IPv6 Routing: OSPFv3
How OSPFv3 Works
OSPFv3 is a routing protocol for IPv4 and IPv6. It is a link-state protocol, as opposed to a distance-vector
protocol. Think of a link as being an interface on a networking device. A link-state protocol makes its routing
decisions based on the states of the links that connect source and destination machines. The state of a link is
a description of that interface and its relationship to its neighboring networking devices. The interface
information includes the IPv6 prefix of the interface, the network mask, the type of network it is connected
to, the devices connected to that network, and so on. This information is propagated in various type of link-state
advertisements (LSAs).
A device’s collection of LSA data is stored in a link-state database. The contents of the database, when subjected
to the Dijkstra algorithm, result in the creation of the OSPF routing table. The difference between the database
and the routing table is that the database contains a complete collection of raw data; the routing table contains
a list of shortest paths to known destinations via specific device interface ports.
OSPFv3, which is described in RFC 5340, supports IPv6 and IPv4 unicast AFs.

Comparison of OSPFv3 and OSPF Version 2
Much of OSPF version 3 is the same as in OSPF version 2. OSPFv3, which is described in RFC 5340, expands
on OSPF version 2 to provide support for IPv6 routing prefixes and the larger size of IPv6 addresses.
In OSPFv3, a routing process does not need to be explicitly created. Enabling OSPFv3 on an interface will
cause a routing process, and its associated configuration, to be created.
In OSPFv3, each interface must be enabled using commands in interface configuration mode. This feature is
different from OSPF version 2, in which interfaces are indirectly enabled using the device configuration mode.
When using a nonbroadcast multiaccess (NBMA) interface in OSPFv3, you must manually configure the
device with the list of neighbors. Neighboring devices are identified by their device ID.
In IPv6, you can configure many address prefixes on an interface. In OSPFv3, all address prefixes on an
interface are included by default. You cannot select some address prefixes to be imported into OSPFv3; either
all address prefixes on an interface are imported, or no address prefixes on an interface are imported.
Unlike OSPF version 2, multiple instances of OSPFv3 can be run on a link.
OSPF automatically prefers a loopback interface over any other kind, and it chooses the highest IP address
among all loopback interfaces. If no loopback interfaces are present, the highest IP address in the device is
chosen. You cannot tell OSPF to use any particular interface.

IP Routing: OSPF Configuration Guide
58


IPv6 Routing: OSPFv3
LSA Types for OSPFv3

LSA Types for OSPFv3
The following list describes LSA types, each of which has a different purpose:
• Device LSAs (Type 1)—Describes the link state and costs of a device’s links to the area. These LSAs
are flooded within an area only. The LSA indicates if the device is an Area Border Router (ABR) or
Autonomous System Boundary Router (ASBR), and if it is one end of a virtual link. Type 1 LSAs are
also used to advertise stub networks. In OSPFv3, these LSAs have no address information and are
network-protocol-independent. In OSPFv3, device interface information may be spread across multiple
device LSAs. Receivers must concatenate all device LSAs originated by a given device when running
the SPF calculation.
• Network LSAs (Type 2)—Describes the link-state and cost information for all devices attached to the
network. This LSA is an aggregation of all the link-state and cost information in the network. Only a
designated device tracks this information and can generate a network LSA. In OSPFv3, network LSAs
have no address information and are network-protocol-independent.
• Interarea-prefix LSAs for ABRs (Type 3)—Advertises internal networks to devices in other areas
(interarea routes). Type 3 LSAs may represent a single network or a set of networks summarized into
one advertisement. Only ABRs generate summary LSAs. In OSPFv3, addresses for these LSAs are
expressed as prefix, prefix length instead of address, mask. The default route is expressed as a prefix
with length 0.
• Interarea-device LSAs for ASBRs (Type 4)—Advertises the location of an ASBR. Devices that are
trying to reach an external network use these advertisements to determine the best path to the next hop.
Type 4 LSAs are generated by ABRs on behalf of ASBRs.
• Autonomous system external LSAs (Type 5)—Redistributes routes from another autonomous system,
usually from a different routing protocol into OSPFv3. In OSPFv3, addresses for these LSAs are expressed
as prefix, prefix length instead of address, mask. The default route is expressed as a prefix with length
0.
• Link LSAs (Type 8)—Have local-link flooding scope and are never flooded beyond the link with which
they are associated. Link LSAs provide the link-local address of the device to all other devices attached
to the link, inform other devices attached to the link of a list of prefixes to associate with the link, and
allow the device to assert a collection of Options bits to associate with the network LSA that will be
originated for the link.
• Intra-Area-Prefix LSAs (Type 9)—A device can originate multiple intra-area-prefix LSAs for each
device or transit network, each with a unique link-state ID. The link-state ID for each intra-area-prefix
LSA describes its association to either the device LSA or the network LSA and contains prefixes for
stub and transit networks.
An address prefix occurs in almost all newly defined LSAs. The prefix is represented by three fields:
PrefixLength, PrefixOptions, and Address Prefix. In OSPFv3, addresses for these LSAs are expressed as
prefix, prefix length instead of address, mask. The default route is expressed as a prefix with length 0. Type
3 and Type 9 LSAs carry all prefix (subnet) information that, in OSPFv2, is included in device LSAs and
network LSAs. The Options field in certain LSAs (device LSAs, network LSAs, interarea-device LSAs, and
link LSAs) has been expanded to 24 bits to provide support for OSPFv3.
In OSPFv3, the sole function of the link-state ID in interarea-prefix LSAs, interarea-device LSAs, and
autonomous-system external LSAs is to identify individual pieces of the link-state database. All addresses or
device IDs that are expressed by the link-state ID in OSPF version 2 are carried in the body of the LSA in
OSPFv3.

IP Routing: OSPF Configuration Guide
59


IPv6 Routing: OSPFv3
Load Balancing in OSPFv3

The link-state ID in network LSAs and link LSAs is always the interface ID of the originating device on the
link being described. For this reason, network LSAs and link LSAs are now the only LSAs whose size cannot
be limited. A network LSA must list all devices connected to the link, and a link LSA must list all of the
address prefixes of a device on the link.

Load Balancing in OSPFv3
When a device learns multiple routes to a specific network via multiple routing processes (or routing protocols),
it installs the route with the lowest administrative distance in the routing table. Sometimes the device must
select a route from among many learned via the same routing process with the same administrative distance.
In this case, the device chooses the path with the lowest cost (or metric) to the destination. Each routing process
calculates its cost differently and the costs may need to be manipulated in order to achieve load balancing.
OSPFv3 performs load balancing automatically in the following way. If OSPFv3 finds that it can reach a
destination through more than one interface and each path has the same cost, it installs each path in the routing
table. The only restriction on the number of paths to the same destination is controlled by the maximum-paths
command. The default maximum paths is 16, and the range is from 1 to 64.

Addresses Imported into OSPFv3
When importing the set of addresses specified on an interface on which OSPFv3 is running into OSPFv3, you
cannot select specific addresses to be imported. Either all addresses are imported, or no addresses are imported.

OSPFv3 Customization
You can customize OSPFv3 for your network, but you likely will not need to do so. The defaults for OSPFv3
are set to meet the requirements of most customers and features. If you must change the defaults, refer to the
IPv6 command reference to find the appropriate syntax.

Caution

Be careful when changing the defaults. Changing defaults will affect your OSPFv3 network, possibly
adversely.

Force SPF in OSPFv3
When the process keyword is used with the clear ipv6 ospf command, the OSPFv3 database is cleared and
repopulated, and then the SPF algorithm is performed. When the force-spf keyword is used with the clear
ipv6 ospf command, the OSPFv3 database is not cleared before the SPF algorithm is performed.

IP Routing: OSPF Configuration Guide
60


IPv6 Routing: OSPFv3
How to Configure Load Balancing in OSPFv3

How to Configure Load Balancing in OSPFv3
Configuring the OSPFv3 Device Process
Once you have completed step 3 and entered OSPFv3 router configuration mode, you can perform any of the
subsequent steps in this task as needed to configure OSPFv3 Device configuration.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. area area-ID [default-cost | nssa | stub]
5. auto-cost reference-bandwidth Mbps
6. default {area area-ID [range ipv6-prefix | virtual-link router-id]} [default-information originate
[always | metric | metric-type | route-map] | distance | distribute-list prefix-list prefix-list-name {in |
out} [interface] | maximum-paths paths | redistribute protocol | summary-prefix ipv6-prefix]
7. ignore lsa mospf
8. interface-id snmp-if-index
9. log-adjacency-changes [detail]
10. passive-interface [default | interface-type interface-number]
11. queue-depth {hello | update} {queue-size | unlimited}
12. router-id router-id

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

router ospfv3 [process-id]

Enters router configuration mode for the IPv4 or IPv6
address family.

Example:
Device(config)# router ospfv3 1

IP Routing: OSPF Configuration Guide
61


IPv6 Routing: OSPFv3
Configuring the OSPFv3 Device Process

Step 4

Command or Action

Purpose

area area-ID [default-cost | nssa | stub]

Configures the OSPFv3 area.

Example:
Device(config-router)# area 1

Step 5

auto-cost reference-bandwidth Mbps
Example:

Controls the reference value OSPFv3 uses when
calculating metrics for interfaces in an IPv4 OSPFv3
process.

Device(config-router)# auto-cost
reference-bandwidth 1000

Step 6

Returns an OSPFv3 parameter to its default value.
default {area area-ID [range ipv6-prefix | virtual-link
router-id]} [default-information originate [always | metric
| metric-type | route-map] | distance | distribute-list
prefix-list prefix-list-name {in | out} [interface] |
maximum-paths paths | redistribute protocol |
summary-prefix ipv6-prefix]
Example:
Device(config-router)# default area 1

Step 7

ignore lsa mospf
Example:

Suppresses the sending of syslog messages when the
device receives LSA Type 6 multicast OSPFv3 packets,
which are unsupported.

Device(config-router)# ignore lsa mospf

Step 8

interface-id snmp-if-index
Example:

Configures OSPFv3 interfaces with Simple Network
Management Protocol (SNMP) MIB-II interface Index
(ifIndex) identification numbers in IPv4 and IPv6.

Device(config-router)# interface-id snmp-if-index

Step 9

log-adjacency-changes [detail]

Configures the device to send a syslog message when
an OSPFv3 neighbor goes up or down.

Example:
Device(config-router)# log-adjacency-changes

Step 10

passive-interface [default | interface-type interface-number] Suppresses sending routing updates on an interface
when an IPv4 OSPFv3 process is used.
Example:
Device(config-router)# passive-interface default

IP Routing: OSPF Configuration Guide
62


IPv6 Routing: OSPFv3
Forcing an SPF Calculation

Step 11

Command or Action

Purpose

queue-depth {hello | update} {queue-size | unlimited}

Configures the number of incoming packets that the
IPv4 OSPFv3 process can keep in its queue.

Example:
Device(config-router)# queue-depth update 1500

Step 12

router-id router-id

Enter this command to use a fixed router ID.

Example:
Device(config-router)# router-id 10.1.1.1

Forcing an SPF Calculation
SUMMARY STEPS
1. enable
2. clear ospfv3 [process-id] force-spf
3. clear ospfv3 [process-id] process
4. clear ospfv3 [process-id] redistribution
5. clear ipv6 ospf [process-id] {process | force-spf | redistribution}

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

clear ospfv3 [process-id] force-spf
Example:
Device# clear ospfv3 1 force-spf

Step 3

clear ospfv3 [process-id] process

Runs SPF calculations for an OSPFv3 process.
• If the clear ospfv3 force-spf command is configured, it overwrites
the clear ipv6 ospf configuration.
• Once the clear ospfv3 force-spf command has been used, the clear
ipv6 ospf command cannot be used.
Resets an OSPFv3 process.

IP Routing: OSPF Configuration Guide
63


IPv6 Routing: OSPFv3
Verifying OSPFv3 Configuration and Operation

Command or Action

• If the clear ospfv3 force-spf command is configured, it overwrites
the clear ipv6 ospf configuration.

Example:
Device# clear ospfv3 2 process

Step 4

clear ospfv3 [process-id] redistribution

• Once the clear ospfv3 force-spf command has been used, the clear
ipv6 ospf command cannot be used.
Clears OSPFv3 route redistribution.
• If the clear ospfv3 force-spf command is configured, it overwrites
the clear ipv6 ospf configuration.

Example:
Device# clear ospfv3 redistribution

Step 5

Purpose

clear ipv6 ospf [process-id] {process |
force-spf | redistribution}

• Once the clear ospfv3 force-spf command has been used, the clear
ipv6 ospf command cannot be used.
Clears the OSPFv3 state based on the OSPFv3 routing process ID, and
forces the start of the SPF algorithm.
• If the clear ospfv3 force-spf command is configured, it overwrites
the clear ipv6 ospf configuration.

Example:
Device# clear ipv6 ospf force-spf

• Once the clear ospfv3 force-spf command has been used, the clear
ipv6 ospf command cannot be used.

Verifying OSPFv3 Configuration and Operation
This task is optional, and the commands can be entered in any order, as needed.

IP Routing: OSPF Configuration Guide
64


IPv6 Routing: OSPFv3
Verifying OSPFv3 Configuration and Operation

SUMMARY STEPS
1. enable
2. show ospfv3 [process-id] [address-family] border-routers
3. show ospfv3 [process-id [area-id]] [address-family] database [database-summary | internal | external
[ipv6-prefix ] [link-state-id] | grace | inter-area prefix [ipv6-prefix | link-state-id] | inter-area router
[destination-router-id | link-state-id] | link [interface interface-name | link-state-id] | network [link-state-id]
| nssa-external [ipv6-prefix] [link-state-id] | prefix [ref-lsa {router | network} | link-state-id] |
promiscuous | router [link-state-id] | unknown [{area | as | link} [link-state-id]] [adv-router router-id]
[self-originate]
4. show ospfv3 [process-id] [address-family] events [generic | interface | lsa | neighbor | reverse | rib |
spf]
5. show ospfv3 [process-id] [area-id] [address-family] flood-list interface-type interface-number
6. show ospfv3 [process-id] [address-family] graceful-restart
7. show ospfv3 [process-id] [area-id] [address-family] interface [type number] [brief]
8. show ospfv3 [process-id] [area-id] [address-family] neighbor [interface-type interface-number]
[neighbor-id] [detail]
9. show ospfv3 [process-id] [area-id] [address-family] request-list[neighbor] [interface] [interface-neighbor]
10. show ospfv3 [process-id] [area-id] [address-family] retransmission-list [neighbor] [interface]
[interface-neighbor]
11. show ospfv3 [process-id] [address-family] statistic [detail]
12. show ospfv3 [process-id] [address-family] summary-prefix
13. show ospfv3 [process-id] [address-family] timers rate-limit
14. show ospfv3 [process-id] [address-family] traffic[interface-type interface-number]
15. show ospfv3 [process-id] [address-family] virtual-links

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

show ospfv3 [process-id] [address-family] border-routers

Displays the internal OSPFv3 routing table
entries to an ABR and ASBR.

Example:
Device# show ospfv3 border-routers

Step 3

Displays lists of information related to the
show ospfv3 [process-id [area-id]] [address-family] database
[database-summary | internal | external [ipv6-prefix ] [link-state-id] OSPFv3 database for a specific device.
| grace | inter-area prefix [ipv6-prefix | link-state-id] | inter-area
router [destination-router-id | link-state-id] | link [interface

IP Routing: OSPF Configuration Guide
65


IPv6 Routing: OSPFv3
Verifying OSPFv3 Configuration and Operation

Command or Action

Purpose

interface-name | link-state-id] | network [link-state-id] | nssa-external
[ipv6-prefix] [link-state-id] | prefix [ref-lsa {router | network} |
link-state-id] | promiscuous | router [link-state-id] | unknown [{area
| as | link} [link-state-id]] [adv-router router-id] [self-originate]
Example:
Device# show ospfv3 database

Step 4

show ospfv3 [process-id] [address-family] events [generic | interface Displays detailed information about OSPFv3
events.
| lsa | neighbor | reverse | rib | spf]
Example:
Device# show ospfv3 events

Step 5

show ospfv3 [process-id] [area-id] [address-family] flood-list
interface-type interface-number

Displays a list of OSPFv3 LSAs waiting to be
flooded over an interface.

Example:
Device# show ospfv3 flood-list

Step 6

show ospfv3 [process-id] [address-family] graceful-restart

Displays OSPFv3 graceful restart information.

Example:
Device# show ospfv3 graceful-restart

Step 7

show ospfv3 [process-id] [area-id] [address-family] interface [type Displays OSPFv3-related interface
information.
number] [brief]
Example:
Device# show ospfv3 interface

Step 8

show ospfv3 [process-id] [area-id] [address-family] neighbor
[interface-type interface-number] [neighbor-id] [detail]

Displays OSPFv3 neighbor information on a
per-interface basis.

Example:
Device# show ospfv3 neighbor

Step 9

show ospfv3 [process-id] [area-id] [address-family]
request-list[neighbor] [interface] [interface-neighbor]
Example:
Device# show ospfv3 request-list

IP Routing: OSPF Configuration Guide
66

Displays a list of all LSAs requested by a
device.


IPv6 Routing: OSPFv3
Configuration Examples for Load Balancing in OSPFv3

Step 10

Command or Action

Purpose

show ospfv3 [process-id] [area-id] [address-family]
retransmission-list [neighbor] [interface] [interface-neighbor]

Displays a list of all LSAs waiting to be
re-sent.

Example:
Device# show ospfv3 retransmission-list

Step 11

show ospfv3 [process-id] [address-family] statistic [detail]

Displays OSPFv3 SPF calculation statistics.

Example:
Device# show ospfv3 statistic

Step 12

show ospfv3 [process-id] [address-family] summary-prefix
Example:

Displays a list of all summary address
redistribution information configured under
an OSPFv3 process.

Device# show ospfv3 summary-prefix

Step 13

show ospfv3 [process-id] [address-family] timers rate-limit

Displays all of the LSAs in the rate limit
queue.

Example:
Device# show ospfv3 timers rate-limit

Step 14

show ospfv3 [process-id] [address-family] traffic[interface-type
interface-number]

Displays OSPFv3 traffic statistics.

Example:
Device# show ospfv3 traffic

Step 15

show ospfv3 [process-id] [address-family] virtual-links

Displays parameters and the current state of
OSPFv3 virtual links.

Example:
Device# show ospfv3 virtual-links

Configuration Examples for Load Balancing in OSPFv3
Example: Configuring the OSPFv3 Device Process
Device# show ospfv3 database
OSPFv3 Device with ID (172.16.4.4) (Process ID 1)
Device Link States (Area 0)
ADV Device
Age
Seq#
Fragment ID
Link count
172.16.4.4
239
0x80000003 0
1

Bits
B

IP Routing: OSPF Configuration Guide
67


IPv6 Routing: OSPFv3
Example: Forcing SPF Configuration

172.16.6.6
ADV Device
172.16.4.4
172.16.4.4
172.16.6.6
172.16.6.6
172.16.6.6
ADV Device
172.16.4.4
172.16.6.6
ADV Device
172.16.4.4
172.16.6.6
ADV Device
172.16.4.4
172.16.6.6

239
0x80000003 0
1
Inter Area Prefix Link States (Area 0)
Age
Seq#
Prefix
249
0x80000001 FEC0:3344::/32
219
0x80000001 FEC0:3366::/32
247
0x80000001 FEC0:3366::/32
193
0x80000001 FEC0:3344::/32
82
0x80000001 FEC0::/32
Inter Area Device Link States (Area 0)
Age
Seq#
Link ID
Dest DevID
219
0x80000001 50529027
172.16.3.3
193
0x80000001 50529027
172.16.3.3
Link (Type-8) Link States (Area 0)
Age
Seq#
Link ID
242
0x80000002 14
252
0x80000002 14
Intra Area Prefix Link States (Area 0)
Age
Seq#
Link ID
242
0x80000002 0
252
0x80000002 0

B

Interface
PO4/0
PO4/0
Ref-lstype
0x2001
0x2001

Ref-LSID
0
0

Device# show ospfv3 neighbor
OSPFv3 Device with ID (10.1.1.1) (Process ID 42)
Neighbor ID
Pri
State
Dead Time
Interface ID
10.4.4.4
1
FULL/ 00:00:39
12
OSPFv3 Device with ID (10.2.1.1) (Process ID 100)
Neighbor ID
Pri
State
Dead Time
Interface ID
10.5.4.4
1
FULL/ 00:00:35
12

Interface
vm1
Interface
vm1

Example: Forcing SPF Configuration
The following example shows how to trigger SPF to redo the SPF and repopulate the routing tables:
clear ipv6 ospf force-spf

Additional References
Related Documents
Related Topic

Document Title

IPv6 addressing and connectivity

IPv6 Configuration Guide

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

IPv6 commands

Cisco IOS IPv6 Command
Reference

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

IPv6 Routing: OSPFv3

“Configuring OSPF” module

IP Routing: OSPF Configuration Guide
68


IPv6 Routing: OSPFv3
Feature Information for IPv6 Routing: OSPFv3

Standards and RFCs
Standard/RFC

Title

RFCs for IPv6

IPv6 RFCs

MIBs
MIB

MIBs Link
To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

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

Feature Information for IPv6 Routing: OSPFv3
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 4: Feature Information for IPv6 Routing: OSPFv3

Feature Name

Releases

Feature Information

IPv6 Routing: OSPFv3

12.2(33)SRA

OSPF version 3 for IPv6 expands
on OSPF version 2 to provide
support for IPv6 routing prefixes
and the larger size of IPv6
addresses.

Cisco IOS XE Release 2.1

IP Routing: OSPF Configuration Guide
69


IPv6 Routing: OSPFv3
Feature Information for IPv6 Routing: OSPFv3

IP Routing: OSPF Configuration Guide
70
