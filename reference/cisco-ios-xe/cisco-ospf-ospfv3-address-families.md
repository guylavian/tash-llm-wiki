---
title: "OSPFv3 Address Families"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-address-families
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 15 OSPFv3 Address Families The Open Shortest Path First version 3 (OSPFv3) address families feature enables both IPv4 and IPv6 unicast traffic to be supported. With this feature, users may have two processes per interface, but only one process per address family (AF). • Finding Feature Information, page 163 • Prerequisites for OSPFv3 Address Families, page 163 • Information About OSPFv3"
---

# OSPFv3 Address Families

CHAPTER

15

OSPFv3 Address Families
The Open Shortest Path First version 3 (OSPFv3) address families feature enables both IPv4 and IPv6 unicast
traffic to be supported. With this feature, users may have two processes per interface, but only one process
per address family (AF).
• Finding Feature Information, page 163
• Prerequisites for OSPFv3 Address Families, page 163
• Information About OSPFv3 Address Families, page 164
• How to Configure OSPFv3 Address Families, page 165
• Configuration Examples for OSPFv3 Address Families, page 179
• Additional References, page 179
• Feature Information for OSPFv3 Address Families, page 180

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv3 Address Families
• To use the IPv4 unicast address families (AF) in OSPFv3, you must enable IPv6 on a link, although the
link may not be participating in IPv6 unicast AF.
• With the OSPFv3 Address Families feature, users may have two processes per interface, but only one
process per AF. If the AF is IPv4, an IPv4 address must first be configured on the interface, but IPv6
must be enabled on the interface.

IP Routing: OSPF Configuration Guide
163


OSPFv3 Address Families
Information About OSPFv3 Address Families

Information About OSPFv3 Address Families
OSPFv3 Address Families
The OSPFv3 address families feature enables both IPv4 and IPv6 unicast traffic to be supported. With this
feature, users may have two processes per interface, but only one process per AF. If the IPv4 AF is used, an
IPv4 address must first be configured on the interface, but IPv6 must be enabled on the interface. A single
IPv4 or IPv6 OSPFv3 process running multiple instances on the same interface is not supported.
Users with an IPv6 network that uses OSPFv3 as its IGP may want to use the same IGP to help carry and
install IPv4 routes. All devices on this network have an IPv6 forwarding stack. Some (or all) of the links on
this network may be allowed to do IPv4 forwarding and be configured with IPv4 addresses. Pockets of
IPv4-only devices exist around the edges running an IPv4 static or dynamic routing protocol. In this scenario,
users need the ability to forward IPv4 traffic between these pockets without tunneling overhead, which means
that any IPv4 transit device has both IPv4 and IPv6 forwarding stacks (e.g., is dual stack).
This feature allows a separate (possibly incongruent) topology to be constructed for the IPv4 AF. It installs
IPv4 routes in IPv4 RIB, and then the forwarding occurs natively. The OSPFv3 process fully supports an IPv4
AF topology and can redistribute routes from and into any other IPv4 routing protocol.
An OSPFv3 process can be configured to be either IPv4 or IPv6. The address-family command is used to
determine which AF will run in the OSPFv3 process, and only one address family can be configured per
instance. Once the AF is selected, users can enable multiple instances on a link and enable
address-family-specific commands.
Different instance ID ranges are used for each AF. Each AF establishes different adjacencies, has a different
link state database, and computes a different shortest path tree. The AF then installs the routes in AF-specific
RIB. LSAs that carry IPv6 unicast prefixes are used without any modification in different instances to carry
each AFs’ prefixes.
The IPv4 subnets configured on OSPFv3-enabled interfaces are advertised through intra-area prefix LSAs,
just as any IPv6 prefixes. External LSAs are used to advertise IPv4 routes redistributed from any IPv4 routing
protocol, including connected and static. The IPv4 OSPFv3 process runs the SPF calculations and finds the
shortest path to those IPv4 destinations. These computed routes are then inserted in the IPv4 RIB (computed
routes are inserted into an IPv6 RIB for an IPv6 AF).
Because the IPv4 OSPFv3 process allocates a unique pdbindex in the IPv4 RIB, all other IPv4 routing protocols
can redistribute routes from it. The parse chain for all protocols is same, so the ospfv3 keyword added to the
list of IPv4 routing protocols causes OSPFv3 to appear in the redistribute command from any IPv4 routing
protocol. With the ospfv3 keyword, IPv4 OSPFv3 routes can be redistributed into any other IPv4 routing
protocol as defined in the redistribute ospfv3 command.
Third-party devices will not neighbor with devices running the AF feature for the IPv4 AF because they do
not set the AF bit. Therefore, those devices will not participate in the IPv4 AF SPF calculations and will not
install the IPv4 OSPFv3 routes in the IPv6 RIB.

IP Routing: OSPF Configuration Guide
164


OSPFv3 Address Families
How to Configure OSPFv3 Address Families

How to Configure OSPFv3 Address Families
Configuring the OSPFv3 Router Process
Once you have completed step 3 and entered OSPFv3 router configuration mode, you can perform any of the
subsequent steps in this task as needed to perform OSPFv3 device configuration.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. area area-ID [default-cost | nssa | stub]
5. auto-cost reference-bandwidth Mbps
6. bfd all-interfaces
7. default {area area-ID[range ipv6-prefix | virtual-link router-id]} [default-information originate
[always | metric | metric-type | route-map] | distance | distribute-list prefix-list prefix-list-name {in |
out} [interface] | maximum-paths paths | redistribute protocol | summary-prefix ipv6-prefix]
8. ignore lsa mospf
9. interface-id snmp-if-index
10. log-adjacency-changes [detail]
11. passive-interface [default | interface-type interface-number]
12. queue-depth {hello | update} {queue-size | unlimited}
13. router-id {router-id}

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

IP Routing: OSPF Configuration Guide
165


OSPFv3 Address Families
Configuring the OSPFv3 Router Process

Step 3

Command or Action

Purpose

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for the
IPv4 or IPv6 address family.

Example:
Device(config)# router ospfv3 1

Step 4

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

bfd all-interfaces

Enables BFD for an OSPFv3 routing process

Example:
Device(config-router)# bfd all-interfaces

Step 7

Returns an OSPFv3 parameter to its default value.
default {area area-ID[range ipv6-prefix | virtual-link
router-id]} [default-information originate [always | metric
| metric-type | route-map] | distance | distribute-list
prefix-list prefix-list-name {in | out} [interface] |
maximum-paths paths | redistribute protocol |
summary-prefix ipv6-prefix]
Example:
Device(config-router)# default area 1

Step 8

ignore lsa mospf
Example:

Suppresses the sending of syslog messages when the
device receives LSA Type 6 multicast OSPFv3 packets,
which are unsupported.

Device(config-router)# ignore lsa mospf

Step 9

interface-id snmp-if-index
Example:
Device(config-router)# interface-id snmp-if-index

IP Routing: OSPF Configuration Guide
166

Configures OSPFv3 interfaces with Simple Network
Management Protocol (SNMP) MIB-II interface Index
(ifIndex) identification numbers in IPv4 and IPv6.


OSPFv3 Address Families
Configuring the IPv6 Address Family in OSPFv3

Step 10

Command or Action

Purpose

log-adjacency-changes [detail]

Configures the router to send a syslog message when
an OSPFv3 neighbor goes up or down.

Example:
Device(config-router)# log-adjacency-changes

Step 11

passive-interface [default | interface-type interface-number] Suppresses sending routing updates on an interface
when using an IPv4 OSPFv3 process.
Example:
Device(config-router)# passive-interface default

Step 12

queue-depth {hello | update} {queue-size | unlimited}

Configures the number of incoming packets that the
IPv4 OSPFv3 process can keep in its queue.

Example:
Device(config-router)# queue-depth update 1500

Step 13

router-id {router-id}

Use a fixed device ID.

Example:
Device(config-router)# router-id 10.1.1.1

Configuring the IPv6 Address Family in OSPFv3
Perform this task to configure the IPv6 address family in OSPFv3. Once you have completed step 4 and
entered IPv6 address-family configuration mode, you can perform any of the subsequent steps in this task as
needed to configure the IPv6 AF.

IP Routing: OSPF Configuration Guide
167


OSPFv3 Address Families
Configuring the IPv6 Address Family in OSPFv3

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. address-family ipv6 unicast
5. area area-ID range ipv6-prefix / prefix-length
6. default {area area-ID[range ipv6-prefix | virtual-link router-id]} [default-information originate
[always | metric | metric-type | route-map] | distance | distribute-list prefix-list prefix-list-name {in |
out} [interface] | maximum-paths paths | redistribute protocol | summary-prefix ipv6-prefix]
7. default-information originate [always | metric metric-value | metric-type type-value| route-map
map-name]
8. default-metric metric-value
9. distance distance
10. distribute-list prefix-list list-name {in[interface-type interface-number] | out routing-process
[as-number]}
11. maximum-paths number-paths
12. summary-prefix prefix [not-advertise | tag tag-value]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for
the IPv4 or IPv6 address family.

Example:
Router(config)# router ospfv3 1

Step 4

address-family ipv6 unicast

Enters IPv6 address family configuration mode
for OSPFv3.

Example:

or

Example:
or

IP Routing: OSPF Configuration Guide
168

Enters IPv4 address family configuration mode
for OSPFv3.


OSPFv3 Address Families
Configuring the IPv6 Address Family in OSPFv3

Command or Action

Purpose

Example:

address-family ipv4
unicast

Example:
Router(config-router)# address-family ipv6 unicast

Example:

Example:
or

Example:
Router(config-router)# address-family ipv4 unicast

Step 5

area area-ID range ipv6-prefix / prefix-length

Configures OSPFv3 area parameters.

Example:
Router(config-router-af)# area 1 range
2001:DB8:0:0::0/128

Step 6

default {area area-ID[range ipv6-prefix | virtual-link router-id]} Returns an OSPFv3 parameter to its default value.
[default-information originate [always | metric | metric-type |
route-map] | distance | distribute-list prefix-list prefix-list-name
{in | out} [interface] | maximum-paths paths | redistribute
protocol | summary-prefix ipv6-prefix]
Example:
Router(config-router-af)# default area 1

Step 7

default-information originate [always | metric metric-value |
metric-type type-value| route-map map-name]

Generates a default external route into an OSPFv3
for a routing domain.

Example:
Router(config-router-af)# default-information originate
always metric 100 metric-type 2

IP Routing: OSPF Configuration Guide
169


OSPFv3 Address Families
Configuring the IPv4 Address Family in OSPFv3

Step 8

Command or Action

Purpose

default-metric metric-value

Sets default metric values for IPv4 and IPv6 routes
redistributed into the OSPFv3 routing protocol.

Example:
Router(config-router-af)# default-metric 10

Step 9

distance distance

Configures an administrative distance for OSPFv3
routes inserted into the routing table.

Example:
Router(config-router-af)# distance 200

Step 10

distribute-list prefix-list list-name {in[interface-type
interface-number] | out routing-process [as-number]}

Applies a prefix list to OSPFv3 routing updates
that are received or sent on an interface.

Example:
Router(config-router-af)# distribute-list prefix-list
PL1 in Ethernet0/0

Step 11

maximum-paths

number-paths

Controls the maximum number of equal-cost routes
that a process for OSPFv3 routing can support.

Example:
Router(config-router-af)# maximum-paths 4

Step 12

summary-prefix prefix [not-advertise | tag tag-value]

Configures an IPv6 summary prefix in OSPFv3.

Example:
Router(config-router-af)# summary-prefix FEC0::/24

Configuring the IPv4 Address Family in OSPFv3
Perform this task to configure the IPv4 address family in OSPFv3. Once you have completed step 4 and
entered IPv4 address-family configuration mode, you can perform any of the subsequent steps in this task as
needed to configure the IPv4 AF.

IP Routing: OSPF Configuration Guide
170


OSPFv3 Address Families
Configuring the IPv4 Address Family in OSPFv3

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. address-family ipv4 unicast
5. area area-id range ip-address ip-address-mask [advertise | not-advertise] [cost cost]
6. default {area area-ID[range ipv6-prefix | virtual-link router-id]} [default-information originate
[always | metric | metric-type | route-map] | distance | distribute-list prefix-list prefix-list-name {in |
out} [interface] | maximum-paths paths | redistribute protocol | summary-prefix ipv6-prefix]
7. default-information originate [always | metric metric-value | metric-type type-value| route-map
map-name]
8. default-metric metric-value
9. distance distance
10. distribute-list prefix-list list-name {in[interface-type interface-number] | out routing-process
[as-number]}
11. maximum-paths number-paths
12. summary-prefix prefix [not-advertise | tag tag-value]

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

Enables OSPFv3 router configuration mode for the
IPv4 or IPv6 address family.

Example:
Device(config)# router ospfv3 1

Step 4

address-family ipv4 unicast

Enters IPv4 address family configuration mode for
OSPFv3.

Example:
Device(config-router)# address-family ipv4 unicast

IP Routing: OSPF Configuration Guide
171


OSPFv3 Address Families
Configuring the IPv4 Address Family in OSPFv3

Command or Action
Step 5

Purpose

area area-id range ip-address ip-address-mask [advertise | Consolidates and summarizes routes at an area
boundary.
not-advertise] [cost cost]
Example:
Device(config-router-af)# area 0 range 192.168.110.0
255.255.0.0

Step 6

Returns an OSPFv3 parameter to its default value.
default {area area-ID[range ipv6-prefix | virtual-link
router-id]} [default-information originate [always | metric |
metric-type | route-map] | distance | distribute-list prefix-list
prefix-list-name {in | out} [interface] | maximum-paths paths |
redistribute protocol | summary-prefix ipv6-prefix]
Example:
Device(config-router-af)# default area 1

Step 7

default-information originate [always | metric metric-value | Generates a default external route into an OSPFv3
for a routing domain.
metric-type type-value| route-map map-name]
Example:
Device(config-router-af)# default-information originate
always metric 100 metric-type 2

Step 8

default-metric metric-value

Sets default metric values for IPv4 and IPv6 routes
redistributed into the OSPFv3 routing protocol.

Example:
Device(config-router-af)# default-metric 10

Step 9

distance distance

Configures an administrative distance for OSPFv3
routes inserted into the routing table.

Example:
Device(config-router-af)# distance 200

Step 10

distribute-list prefix-list list-name {in[interface-type
interface-number] | out routing-process [as-number]}

Applies a prefix list to OSPFv3 routing updates
that are received or sent on an interface.

Example:
Device(config-router-af)# distribute-list prefix-list
PL1 in Ethernet0/0

Step 11

maximum-paths

number-paths

Example:
Device(config-router-af)# maximum-paths 4

IP Routing: OSPF Configuration Guide
172

Controls the maximum number of equal-cost routes
that a process for OSPFv3 routing can support.


OSPFv3 Address Families
Configuring Route Redistribution in OSPFv3

Step 12

Command or Action

Purpose

summary-prefix prefix [not-advertise | tag tag-value]

Configures an IPv6 summary prefix in OSPFv3.

Example:
Device(config-router-af)# summary-prefix FEC0::/24

Configuring Route Redistribution in OSPFv3
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. address-family ipv6 unicast
5. redistribute source-protocol [process-id] [options]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for the IPv4
or IPv6 address family.

Example:
Router(config)# router ospfv3 1

Step 4

address-family ipv6 unicast

Enters IPv6 address family configuration mode for
OSPFv3.

Example:

or
Enters IPv4 address family configuration mode for
OSPFv3.

IP Routing: OSPF Configuration Guide
173


OSPFv3 Address Families
Configuring Route Redistribution in OSPFv3

Command or Action

Purpose

Example:
or

Example:

address-family ipv4
unicast

Example:
Router(config-router)# address-family ipv6 unicast

Example:

Example:
or

Example:
Router(config-router)# address-family ipv4 unicast

Step 5

redistribute source-protocol [process-id] [options]
Example:

IP Routing: OSPF Configuration Guide
174

Redistributes IPv6 and IPv4 routes from one routing
domain into another routing domain.


OSPFv3 Address Families
Enabling OSPFv3 on an Interface

Enabling OSPFv3 on an Interface
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. Do one of the following:
• ospfv3 process-id area area-ID {ipv4 | ipv6} [instance instance-id]
• ipv6 ospf process-id

area area-id [instance instance-id]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

interface type number

Specifies an interface type and number, and places
the device in interface configuration mode.

Example:
Device(config)# interface ethernet 0/0

Step 4

Do one of the following:
• ospfv3 process-id area area-ID {ipv4 | ipv6}
[instance instance-id]
• ipv6 ospf process-id
instance-id]

area area-id [instance

Enables OSPFv3 on an interface with the IPv4 or IPv6
AF.
or
Enables OSPFv3 on an interface.

Example:
Device(config-if)# ospfv3 1 area 1 ipv4

IP Routing: OSPF Configuration Guide
175


OSPFv3 Address Families
Defining an OSPFv3 Area Range for the IPv6 or IPv4 Address Family

Command or Action

Purpose

Example:
Device(config-if)# ipv6 ospf 1 area 0

Defining an OSPFv3 Area Range for the IPv6 or IPv4 Address Family
The cost of the summarized routes will be the highest cost of the routes being summarized. For example, if
the following routes are summarized:
OI
OI
OI

2001:DB8:0:7::/64 [110/20]
via FE80::A8BB:CCFF:FE00:6F00, GigabitEthernet0/0/0
2001:DB8:0:8::/64 [110/100]
via FE80::A8BB:CCFF:FE00:6F00, GigabitEthernet0/0/0
2001:DB8:0:9::/64 [110/20]
via FE80::A8BB:CCFF:FE00:6F00, GigabitEthernet0/0/0

They become one summarized route, as follows:
OI

2001:DB8::/48 [110/100]
via FE80::A8BB:CCFF:FE00:6F00, GigabitEthernet0/0/0

Before You Begin
OSPFv3 routing must be enabled.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. address-family ipv6 unicast
5. area area-ID range ipv6-prefix

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Router> enable

IP Routing: OSPF Configuration Guide
176

• Enter your password if prompted.


OSPFv3 Address Families
Defining an OSPFv3 Area Range for the IPv6 or IPv4 Address Family

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for the
IPv4 or IPv6 address family.

Example:
Router(config)# router ospfv3 1

Step 4

address-family ipv6 unicast

Enters IPv6 address family configuration mode for
OSPFv3.

Example:

or
Enters IPv4 address family configuration mode for
OSPFv3.

Example:
or

Example:

address-family ipv4
unicast

Example:
Router(config-router)# address-family ipv6 unicast

Example:

Example:
or

Example:
Router(config-router)# address-family ipv4 unicast

Step 5

area area-ID range ipv6-prefix

Configures OSPFv3 area parameters.

Example:
Router(config-router-af)# area 1 range
2001:DB8:0:0::0/128

IP Routing: OSPF Configuration Guide
177


OSPFv3 Address Families
Defining an OSPFv3 Area Range for the IPv6 or IPv4 Address Family

Defining an OSPFv3 Area Range
This task can be performed in releases prior to Cisco IOS XE Release 3.4S.

SUMMARY STEPS
1. enable
2. configure terminal
3. ipv6 router ospf process-id
4. area area-id range ipv6-prefix / prefix-length advertise | not-advertise] [cost cost]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

ipv6 router ospf process-id

Enables OSPFv3 router configuration mode.

Example:
Router(config)# ipv6 router ospf 1

Step 4

area area-id range ipv6-prefix / prefix-length
advertise | not-advertise] [cost cost]
Example:
Router(config-rtr)# area 1 range 2001:DB8::/48

IP Routing: OSPF Configuration Guide
178

Consolidates and summarizes routes at an area
boundary.


OSPFv3 Address Families
Configuration Examples for OSPFv3 Address Families

Configuration Examples for OSPFv3 Address Families
Example: Configuring OSPFv3 Address Families
Device# show ospfv3
Routing Process "ospfv3 1" with ID 10.0.0.1
Supports IPv6 Address Family
Event-log enabled, Maximum number of events: 1000, Mode: cyclic
Initial SPF schedule delay 5000 msecs
Minimum hold time between two consecutive SPFs 10000 msecs
Maximum wait time between two consecutive SPFs 10000 msecs
Minimum LSA interval 5 secs
Minimum LSA arrival 1000 msecs
LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
Number of external LSA 0. Checksum Sum 0x000000
Number of areas in this router is 0. 0 normal 0 stub 0 nssa
Graceful restart helper support enabled
Reference bandwidth unit is 100 mbps
Relay willingness value is 128
Pushback timer value is 2000 msecs
Relay acknowledgement timer value is 1000 msecs
LSA cache Disabled : current count 0, maximum 1000
ACK cache Disabled : current count 0, maximum 1000
Selective Peering is not enabled
Hello requests and responses will be sent multicast

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

OSPFv3 Address Families

“ OSPF Forwarding Address
Suppression in Translated Type-5
LSAs ” module

IP Routing: OSPF Configuration Guide
179


OSPFv3 Address Families
Feature Information for OSPFv3 Address Families

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

Feature Information for OSPFv3 Address Families
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
180


OSPFv3 Address Families
Feature Information for OSPFv3 Address Families

Table 18: Feature Information for OSPFv3 Address Families

Feature Name

Releases

Feature Information

OSPFv3 Address Families

Cisco IOS XE Release 3.4S

IP Routing: OSPF Configuration Guide
181


OSPFv3 Address Families
Feature Information for OSPFv3 Address Families

Feature Name

Releases

Feature Information
The OSPFv3 address families
feature enables IPv4 and IPv6
unicast traffic to be supported with
a single network topology.
The following commands were
introduced or modified:
address-family ipv4 (OSPFv3),
address-family ipv6 (OSPFv3),
area (OSPFv3), auto-cost
(OSPFv3), bfd all-interfaces
(OSPFv3), clear ospfv3 counters,
clear ospfv3 force-spf, clear
ospfv3 process, clear ospfv3
redistribution, clear ospfv3
traffic, debug ospfv3, debug
ospfv3 database-timer rate-limit,
debug ospfv3 events, debug
ospfv3 lsdb, debug ospfv3 packet,
debug ospfv3 spf statistic, default
(OSPFv3), default-information
originate (OSPFv3),
default-metric (OSPFv3),
distance (OSPFv3), distribute-list
prefix-list (OSPFv3), event-log
(OSPFv3), log-adjacency-changes
(OSPFv3), maximum-paths
(OSPFv3), ospfv3 area, ospfv3
authentication, ospfv3 bfd,
ospfv3 cost, ospfv3
database-filter, ospfv3
dead-interval, ospfv3
demand-circuit, ospfv3
encryption, ospfv3
flood-reduction, ospfv3
hello-interval, ospfv3 mtu-ignore,
ospfv3 network, ospfv3 priority,
ospfv3 retransmit-interval,
ospfv3 transmit-delay,
passive-interface (OSPFv3),
queue-depth (OSPFv3),
redistribute (OSPFv3), router
ospfv3, router-id (OSPFv3), show
ospfv3 border-routers, show
ospfv3 database, show ospfv3
events, show ospfv3 flood-list,
show ospfv3 graceful-restart,
show ospfv3 interface, show
ospfv3 max-metric, show ospfv3

IP Routing: OSPF Configuration Guide
182


OSPFv3 Address Families
Feature Information for OSPFv3 Address Families

Feature Name

Releases

Feature Information
neighbor, show ospfv3
request-list, show ospfv3
retransmission-list, show ospfv3
statistics, show ospfv3
summary-prefix, show ospfv3
timers rate-limit, show ospfv3
traffic, show ospfv3 virtual-links,
summary-prefix (OSPFv3),
timers pacing flood (OSPFv3),
timers pacing lsa-group
(OSPFv3), timers pacing
retransmission (OSPFv3).

IP Routing: OSPF Configuration Guide
183


OSPFv3 Address Families
Feature Information for OSPFv3 Address Families

IP Routing: OSPF Configuration Guide
184
