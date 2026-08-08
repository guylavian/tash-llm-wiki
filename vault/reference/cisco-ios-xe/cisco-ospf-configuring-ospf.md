---
title: "Configuring OSPF"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-configuring-ospf
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 2 Configuring OSPF This module describes how to configure Open Shortest Path First (OSPF). OSPF is an Interior Gateway Protocol (IGP) developed by the OSPF working group of the Internet Engineering Task Force (IETF). OSPF was designed expressly for IP networks and it supports IP subnetting and tagging of externally derived routing information. OSPF also allows packet authentication and u"
---

# Configuring OSPF

CHAPTER

2

Configuring OSPF
This module describes how to configure Open Shortest Path First (OSPF). OSPF is an Interior Gateway
Protocol (IGP) developed by the OSPF working group of the Internet Engineering Task Force (IETF). OSPF
was designed expressly for IP networks and it supports IP subnetting and tagging of externally derived
routing information. OSPF also allows packet authentication and uses IP multicast when sending and receiving
packets.
Cisco supports RFC 1253, OSPF Version 2 Management Information Base, August 1991. The OSPF MIB
defines an IP routing protocol that provides management information related to OSPF and is supported by
Cisco routers.
For protocol-independent features that work with OSPF, see the "Configuring IP Routing Protocol-Independent
Features" module.
• Finding Feature Information, page 3
• Information About OSPF, page 4
• How to Configure OSPF, page 11
• Configuration Examples for OSPF, page 37
• Additional References for OSPF Not-So-Stubby Areas (NSSA), page 54
• Feature Information for Configuring OSPF, page 55

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
3


Configuring OSPF
Information About OSPF

Information About OSPF
Cisco OSPF Implementation
The Cisco implementation conforms to the OSPF Version 2 specifications detailed in the Internet RFC 2328.
The following list outlines key features supported in the Cisco OSPF implementation:
• Stub areas—The definition of stub areas is supported.
• Route redistribution—Routes learned via any IP routing protocol can be redistributed into any other IP
routing protocol. At the intradomain level, OSPF can import routes learned via Interior Gateway Routing
Protocol (IGRP), Routing Information Protocol (RIP), and Intermediate System-to-Intermediate System
(IS-IS). OSPF routes can also be exported into IGRP, RIP, and IS-IS. At the interdomain level, OSPF
can import routes learned via Exterior Gateway Protocol (EGP) and Border Gateway Protocol (BGP).
OSPF routes can be exported into EGP and BGP.
• Authentication—Plain text and message-digest algorithm 5 (MD5) authentication among neighboring
routers within an area is supported.
• Routing interface parameters—Configurable parameters supported include interface output cost,
retransmission interval, interface transmit delay, router priority, router “dead” and hello intervals, and
authentication key.
• Virtual links—Virtual links are supported.
• Not-so-stubby area (NSSA)—RFC 3101, which replaces and is backward compatible with RFC 1587.
• OSPF over demand circuit—RFC 1793.

Router Coordination for OSPF
OSPF typically requires coordination among many internal routers: Area Border Routers (ABRs), which are
routers connected to multiple areas, and Autonomous System Boundary Routers (ASBRs). At a minimum,
OSPF-based routers or access servers can be configured with all default parameter values, no authentication,
and interfaces assigned to areas. If you intend to customize your environment, you must ensure coordinated
configurations of all routers.

Route Distribution for OSPF
You can specify route redistribution; see the task “Redistribute Routing Information” in the Network Protocols
Configuration Guide, Part 1, for information on how to configure route redistribution.
The Cisco OSPF implementation allows you to alter certain interface-specific OSPF parameters, as needed.
You are not required to alter any of these parameters, but some interface parameters must be consistent across
all routers in an attached network. Those parameters are controlled by the ip ospf hello-interval, ip ospf
dead-interval, and ip ospf authentication-key interface configuration commands. Therefore, if you do
configure any of these parameters, ensure that the configurations for all routers on your network have compatible
values.
By default, OSPF classifies different media into the following three types of networks:

IP Routing: OSPF Configuration Guide
4


Configuring OSPF
Route Distribution for OSPF

• Broadcast networks (Ethernet, Token Ring, and FDDI)
• Nonbroadcast multiaccess (NBMA) networks (Switched Multimegabit Data Service [SMDS], Frame
Relay, and X.25)
• Point-to-point networks (High-Level Data Link Control [HDLC] and PPP)
You can configure your network as either a broadcast or an NBMA network.
X.25 and Frame Relay provide an optional broadcast capability that can be configured in the map to allow
OSPF to run as a broadcast network. See the x25 map and frame-relay map command pages in the Cisco
IOS Wide-Area Networking Command Reference publication for more detail.

OSPF Network Type
You have the choice of configuring your OSPF network type as either broadcast or NBMA, regardless of the
default media type. Using this feature, you can configure broadcast networks as NBMA networks when, for
example, you have routers in your network that do not support multicast addressing. You also can configure
NBMA networks (such as X.25, Frame Relay, and SMDS) as broadcast networks. This feature saves you
from needing to configure neighbors, as described in the “Configuring OSPF for Nonbroadcast Networks”section
later in this module.
Configuring NBMA networks as either broadcast or nonbroadcast assumes that there are virtual circuits (VCs)
from every router to every router, that is, a fully meshed network. This is not true in some cases, for example,
because of cost constraints or when you have only a partially meshed network. In these cases, you can configure
the OSPF network type as a point-to-multipoint network. Routing between two routers that are not directly
connected will go through the router that has VCs to both routers. Note that you need not configure neighbors
when using this feature.
An OSPF point-to-multipoint interface is defined as a numbered point-to-point interface having one or more
neighbors. It creates multiple host routes. An OSPF point-to-multipoint network has the following benefits
compared to NBMA and point-to-point networks:
• Point-to-multipoint is easier to configure because it requires no configuration of neighbor commands,
it consumes only one IP subnet, and it requires no designated router election.
• It costs less because it does not require a fully meshed topology.
• It is more reliable because it maintains connectivity in the event of VC failure.
On point-to-multipoint broadcast networks, there is no need to specify neighbors. However, you can specify
neighbors with the neighbor router configuration command, in which case you should specify a cost to that
neighbor.
Before the point-to-multipoint keyword was added to the ip ospf network interface configuration command,
some OSPF point-to-multipoint protocol traffic was treated as multicast traffic. Therefore, the neighbor router
configuration command was not needed for point-to-multipoint interfaces because multicast took care of the
traffic. Hello, update, and acknowledgment messages were sent using multicast. In particular, multicast hello
messages discovered all neighbors dynamically.
On any point-to-multipoint interface (broadcast or not), the Cisco IOS software assumed that the cost to each
neighbor was equal. The cost was configured with the ip ospf cost interface configuration command. In reality,
the bandwidth to each neighbor is different, so the cost should differ. With this feature, you can configure a
separate cost to each neighbor. This feature applies to point-to-multipoint interfaces only.

IP Routing: OSPF Configuration Guide
5


Configuring OSPF
Route Distribution for OSPF

Because many routers might be attached to an OSPF network, a designated router is selected for the network.
Special configuration parameters are needed in the designated router selection if broadcast capability is not
configured.
These parameters need only be configured in those devices that are themselves eligible to become the designated
router or backup designated router (in other words, routers with a nonzero router priority value).
You can specify the following neighbor parameters, as required:
• Priority for a neighboring router
• Nonbroadcast poll interval
On point-to-multipoint, nonbroadcast networks, use the neighbor router configuration command to identify
neighbors. Assigning a cost to a neighbor is optional.
Prior to Cisco IOS Release 12.0, some customers were using point-to-multipoint on nonbroadcast media (such
as classic IP over ATM), so their routers could not dynamically discover their neighbors. This feature allows
the neighbor router configuration command to be used on point-to-multipoint interfaces.

Area Parameters
Use OSPF Not-So-Stubby Areas (NSSA) feature to simplify administration if you are an Internet service
provider (ISP) or a network administrator that must connect a central site that is using OSPF to a remote site
that is using a different routing protocol.
Prior to NSSA, the connection between the corporate site border router and the remote router could not be
run as an OSPF stub area because routes for the remote site could not be redistributed into the stub area, and
two routing protocols needed to be maintained. A simple protocol such as RIP was usually run and handled
the redistribution. With NSSA, you can extend OSPF to cover the remote connection by defining the area
between the corporate router and the remote router as an NSSA.
As with OSPF stub areas, NSSA areas cannot be injected with distributed routes via Type 5 LSAs. Route
redistribution into an NSSA area is possible only with a special type of LSA that is known as Type 7 that can
exist only in an NSSA area. An NSSA ASBR generates the Type 7 LSA so that the routes can be redistributed,
and an NSSA ABR translates the Type 7 LSA into a Type 5 LSA, which can be flooded throughout the whole
OSPF routing domain. Summarization and filtering are supported during the translation.
RFC 3101 allows you to configure an NSSA ABR router as a forced NSSA LSA translator. This means that
the NSSA ABR router will unconditionally assume the role of LSA translator, preempting the default behavior,
which would only include it among the candidates to be elected as translator.

Note

Even a forced translator might not translate all LSAs; translation depends on the contents of each LSA.
The figure below shows a network diagram in which OSPF Area 1 is defined as the stub area. The Enhanced
Interior Gateway Routing Protocol (EIGRP) routes cannot be propagated into the OSPF domain because

IP Routing: OSPF Configuration Guide
6


Configuring OSPF
Route Distribution for OSPF

routing redistribution is not allowed in the stub area. However, once OSPF Area 1 is defined as an NSSA, an
NSSA ASBR can inject the EIGRP routes into the OSPF NSSA by creating Type 7 LSAs.
Figure 1: OSPF NSSA

The redistributed routes from the RIP router will not be allowed into OSPF Area 1 because NSSA is an
extension to the stub area. The stub area characteristics will still exist, including the exclusion of Type 5 LSAs.
Route summarization is the consolidation of advertised addresses. This feature causes a single summary route
to be advertised to other areas by an ABR. In OSPF, an ABR will advertise networks in one area into another
area. If the network numbers in an area are assigned in a way such that they are contiguous, you can configure
the ABR to advertise a summary route that covers all the individual networks within the area that fall into the
specified range.
When routes from other protocols are redistributed into OSPF (as described in the module "Configuring IP
Routing Protocol-Independent Features"), each route is advertised individually in an external LSA. However,
you can configure the Cisco IOS software to advertise a single route for all the redistributed routes that are
covered by a specified network address and mask. Doing so helps decrease the size of the OSPF link-state
database.
In OSPF, all areas must be connected to a backbone area. If there is a break in backbone continuity, or the
backbone is purposefully partitioned, you can establish a virtual link. The two endpoints of a virtual link are
ABRs. The virtual link must be configured in both routers. The configuration information in each router
consists of the other virtual endpoint (the other ABR) and the nonbackbone area that the two routers have in
common (called the transit area). Note that virtual links cannot be configured through stub areas.
You can force an ASBR to generate a default route into an OSPF routing domain. Whenever you specifically
configure redistribution of routes into an OSPF routing domain, the router automatically becomes an ASBR.
However, an ASBR does not, by default, generate a defaultroute into the OSPF routing domain.
You can configure OSPF to look up Domain Naming System (DNS) names for use in all OSPF show EXEC
command displays. You can use this feature to more easily identify a router, because the router is displayed
by name rather than by its router ID or neighbor ID.

IP Routing: OSPF Configuration Guide
7


Configuring OSPF
Route Distribution for OSPF

OSPF uses the largest IP address configured on the interfaces as its router ID. If the interface associated with
this IP address is ever brought down, or if the address is removed, the OSPF process must recalculate a new
router ID and resend all its routing information out its interfaces.
If a loopback interface is configured with an IP address, the Cisco IOS software will use this IP address as its
router ID, even if other interfaces have larger IP addresses. Because loopback interfaces never go down,
greater stability in the routing table is achieved.
OSPF automatically prefers a loopback interface over any other kind, and it chooses the highest IP address
among all loopback interfaces. If no loopback interfaces are present, the highest IP address in the router is
chosen. You cannot tell OSPF to use any particular interface.
In Cisco IOS Release 10.3 and later releases, by default OSPF calculates the OSPF metric for an interface
according to the bandwidth of the interface. For example, a 64-kbps link gets a metric of 1562, and a T1 link
gets a metric of 64.
The OSPF metric is calculated as the ref-bw value divided by the bandwidth value, with the ref-bw value
equal to 108 by default, and the bandwidth value determined by the bandwidth interface configuration command.
The calculation gives FDDI a metric of 1. If you have multiple links with high bandwidth, you might want
to specify a larger number to differentiate the cost on those links.
An administrative distance is a rating of the trustworthiness of a routing information source, such as an
individual router or a group of routers. Numerically, an administrative distance is an integer from 0 to 255.
In general, the higher the value, the lower the trust rating. An administrative distance of 255 means the routing
information source cannot be trusted at all and should be ignored.
OSPF uses three different administrative distances: intra-area, interarea, and external. Routes within an area
are intra-area; routes to another area are interarea; and routes from another routing domain learned via
redistribution are external. The default distance for each type of route is 110.
Because simplex interfaces between two devices on an Ethernet represent only one network segment, for
OSPF you must configure the sending interface to be a passive interface. This configuration prevents OSPF
from sending hello packets for the sending interface. Both devices are able to see each other via the hello
packet generated for the receiving interface.
You can configure the delay time between when OSPF receives a topology change and when it starts a shortest
path first (SPF) calculation. You can also configure the hold time between two consecutive SPF calculations.
The OSPF on-demand circuit is an enhancement to the OSPF protocol that allows efficient operation over
on-demand circuits such as ISDN, X.25 switched virtual circuits (SVCs), and dialup lines. This feature supports
RFC 1793, Extending OSPF to Support Demand Circuits.
Prior to this feature, OSPF periodic hello and LSA updates would be exchanged between routers that connected
the on-demand link, even when no changes occurred in the hello or LSA information.
With this feature, periodic hellos are suppressed and the periodic refreshes of LSAs are not flooded over the
demand circuit. These packets bring up the link only when they are exchanged for the first time, or when a
change occurs in the information they contain. This operation allows the underlying data link layer to be
closed when the network topology is stable.
This feature is useful when you want to connect telecommuters or branch offices to an OSPF backbone at a
central site. In this case, OSPF for on-demand circuits allows the benefits of OSPF over the entire domain,
without excess connection costs. Periodic refreshes of hello updates, LSA updates, and other protocol overhead
are prevented from enabling the on-demand circuit when there is no "real" data to send.
Overhead protocols such as hellos and LSAs are transferred over the on-demand circuit only upon initial setup
and when they reflect a change in the topology. This means that critical changes to the topology that require
new SPF calculations are sent in order to maintain network topology integrity. Periodic refreshes that do not
include changes, however, are not sent across the link.

IP Routing: OSPF Configuration Guide
8


Configuring OSPF
Route Distribution for OSPF

The OSPF LSA group pacing feature allows the router to group OSPF LSAs and pace the refreshing,
checksumming, and aging functions. The group pacing results in more efficient use of the router.
The router groups OSPF LSAs and paces the refreshing, checksumming, and aging functions so that sudden
increases in CPU usage and network resources are avoided. This feature is most beneficial to large OSPF
networks.
OSPF LSA group pacing is enabled by default. For typical customers, the default group pacing interval for
refreshing, checksumming, and aging is appropriate and you need not configure this feature.

Original LSA Behavior
Each OSPF LSA has an age, which indicates whether the LSA is still valid. Once the LSA reaches the maximum
age (1 hour), it is discarded. During the aging process, the originating router sends a refresh packet every 30
minutes to refresh the LSA. Refresh packets are sent to keep the LSA from expiring, whether there has been
a change in the network topology or not. Checksumming is performed on all LSAs every 10 minutes. The
router keeps track of LSAs that it generates and LSAs that it receives from other routers. The router refreshes
LSAs that it generated; it ages the LSAs that it received from other routers.
Prior to the LSA group pacing feature, the Cisco software would perform refreshing on a single timer and
checksumming and aging on another timer. In the case of refreshing, for example, the software would scan
the whole database every 30 minutes, refreshing every LSA that the router generated, no matter how old it
was. The figure below illustrates all the LSAs being refreshed at once. This process wasted CPU resources
because only a small portion of the database needed to be refreshed. A large OSPF database (several thousand
LSAs) could have thousands of LSAs with different ages. Refreshing on a single timer resulted in the age of
all LSAs becoming synchronized, which resulted in much CPU processing at once. Furthermore, a large
number of LSAs could cause a sudden increase of network traffic, consuming a large amount of network
resources in a short time.
Figure 2: OSPF LSAs on a Single Timer Without Group Pacing

LSA Group Pacing with Multiple Timers
Configuring each LSA to have its own timer avoids excessive CPU processing and sudden network-traffic
increase. To again use the example of refreshing, each LSA gets refreshed when it is 30 minutes old,
independent of other LSAs. So the CPU is used only when necessary. However, LSAs being refreshed at
frequent, random intervals would require many packets for the few refreshed LSAs that the router must send,
which would be inefficient use of bandwidth.
Therefore, the router delays the LSA refresh function for an interval of time instead of performing it when
the individual timers are reached. The accumulated LSAs constitute a group, which is then refreshed and sent
out in one packet or more. Thus, the refresh packets are paced, as are the checksumming and aging. The pacing
interval is configurable; it defaults to 4 minutes, which is randomized to further avoid synchronization.

IP Routing: OSPF Configuration Guide
9


Configuring OSPF
Route Distribution for OSPF

The figure below illustrates the case of refresh packets. The first timeline illustrates individual LSA timers;
the second timeline illustrates individual LSA timers with group pacing.
Figure 3: OSPF LSAs on Individual Timers with Group Pacing

The group pacing interval is inversely proportional to the number of LSAs that the router is refreshing,
checksumming, and aging. For example, if you have approximately 10,000 LSAs, decreasing the pacing
interval would benefit you. If you have a very small database (40 to 100 LSAs), increasing the pacing interval
to 10 to 20 minutes might benefit you slightly.
The default value of pacing between LSA groups is 240 seconds (4 minutes). The range is from 10 seconds
to 1800 seconds (30 minutes).
By default, OSPF floods new LSAs over all interfaces in the same area, except the interface on which the
LSA arrives. Some redundancy is desirable, because it ensures robust flooding. However, too much redundancy
can waste bandwidth and might destabilize the network due to excessive link and CPU usage in certain
topologies. An example would be a fully meshed topology.
You can block OSPF flooding of LSAs in two ways, depending on the type of networks:
• On broadcast, nonbroadcast, and point-to-point networks, you can block flooding over specified OSPF
interfaces.
• On point-to-multipoint networks, you can block flooding to a specified neighbor.
The growth of the Internet has increased the importance of scalability in IGPs such as OSPF. By design, OSPF
requires LSAs to be refreshed as they expire after 3600 seconds. Some implementations have tried to improve
the flooding by reducing the frequency to refresh from 30 minutes to about 50 minutes. This solution reduces
the amount of refresh traffic but requires at least one refresh before the LSA expires. The OSPF flooding
reduction solution works by reducing unnecessary refreshing and flooding of already known and unchanged
information. To achieve this reduction, the LSAs are now flooded with the higher bit set. The LSAs are now
set as “do not age.”
Cisco routers do not support LSA Type 6 Multicast OSPF (MOSPF), and they generate syslog messages if
they receive such packets. If the router is receiving many MOSPF packets, you might want to configure the
router to ignore the packets and thus prevent a large number of syslog messages.

IP Routing: OSPF Configuration Guide
10


Configuring OSPF
How to Configure OSPF

The former OSPF implementation for sending update packets needed to be more efficient. Some update
packets were getting lost in cases where the link was slow, a neighbor could not receive the updates quickly
enough, or the router was out of buffer space. For example, packets might be dropped if either of the following
topologies existed:
• A fast router was connected to a slower router over a point-to-point link.
• During flooding, several neighbors sent updates to a single router at the same time.
OSPF update packets are now automatically paced so they are not sent less than 33 milliseconds apart. Pacing
is also added between resends to increase efficiency and minimize lost retransmissions. Also, you can display
the LSAs waiting to be sent out an interface. The benefit of pacing is that OSPF update and retransmission
packets are sent more efficiently. There are no configuration tasks for this feature; it occurs automatically.
You can display specific statistics such as the contents of IP routing tables, caches, and databases. Information
provided can be used to determine resource utilization and solve network problems. You can also display
information about node reachability and discover the routing path that your device packets are taking through
the network.

How to Configure OSPF
To configure OSPF, perform the tasks described in the following sections. The tasks in the “Enabling OSPF”
section are required; the tasks in the remaining sections are optional, but might be required for your application.
For information about the maximum number of interfaces, see the “Restrictions for OSPF” section.

Enabling OSPF
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. network ip-address wildcard-mask area area-id
5. end

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
11


Configuring OSPF
Configuring OSPF Interface Parameters

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Device(config)# router ospf 109

Step 4

network ip-address wildcard-mask area area-id

Defines an interface on which OSPF runs and defines the
area ID for that interface.

Example:
Device(config-router)# network 192.168.129.16
0.0.0.3 area 20

Step 5

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Configuring OSPF Interface Parameters
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. ip ospf cost cost
5. ip ospf retransmit-interval seconds
6. ip ospf transmit-delay seconds
7. ip ospf priority number-value
8. ip ospf hello-interval seconds
9. ip ospf dead-interval seconds
10. ip ospf authentication-key key
11. ip ospf message-digest-key key-id md5 key
12. ip ospf authentication [message-digest | null]
13. end

IP Routing: OSPF Configuration Guide
12


Configuring OSPF
Configuring OSPF Interface Parameters

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

Configures an interface type and enters interface configuration
mode.

Example:
Device(config)# interface Gigabitethernet 0/0

Step 4

ip ospf cost cost

Explicitly specifies the cost of sending a packet on an OSPF
interface.

Example:
Device(config-if)# ip ospf cost 65

Step 5

ip ospf retransmit-interval seconds
Example:

Specifies the number of seconds between link-state
advertisement (LSA) retransmissions for adjacencies
belonging to an OSPF interface.

Device(config-if)# ip ospf retransmit-interval
1

Step 6

ip ospf transmit-delay seconds

Sets the estimated number of seconds required to send a
link-state update packet on an OSPF interface.

Example:
Device(config-if)# ip ospf transmit-delay

Step 7

ip ospf priority number-value

Sets priority to help determine the OSPF designated router
for a network.

Example:
Device(config-if)# ip ospf priority 1

Step 8

ip ospf hello-interval seconds

Specifies the length of time between the hello packets that
the Cisco IOS software sends on an OSPF interface.

Example:
Device(config-if)# ip ospf hello-interval 1

IP Routing: OSPF Configuration Guide
13


Configuring OSPF
Configuring OSPF over Different Physical Networks

Step 9

Command or Action

Purpose

ip ospf dead-interval seconds

Sets the number of seconds that a device must wait before it
declares a neighbor OSPF router down because it has not
received a hello packet.

Example:
Device(config-if)# ip ospf dead-interval 1

Step 10

ip ospf authentication-key key
Example:

Assigns a password to be used by neighboring OSPF routers
on a network segment that is using the OSPF simple password
authentication.

Device(config-if)# ip ospf authentication-key
1

Step 11

ip ospf message-digest-key key-id md5 key
Example:

Enables OSPF MD5 authentication. The values for the key-id
and key arguments must match values specified for other
neighbors on a network segment.

Device(config-if)# ip ospf message-digest-key
1 md5 23456789

Step 12

ip ospf authentication [message-digest | null]

Specifies the authentication type for an interface.

Example:
Device(config-if)# ip ospf authentication
message-digest

Step 13

Exits interface configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-if)# end

Configuring OSPF over Different Physical Networks
Configuring OSPF for Point-to-Multipoint Broadcast Networks
SUMMARY STEPS
1. configure terminal
2. interface type number
3. ip ospf network point-to-multipoint
4. exit
5. router ospf process-id
6. neighbor ip-address [cost number]

IP Routing: OSPF Configuration Guide
14


Configuring OSPF
Configuring OSPF over Different Physical Networks

DETAILED STEPS

Step 1

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 2

interface type number

Specifies an interface type and number, and enters interface
configuration mode.

Example:
Device(config)# interface gigabitethernet
0/0/0

Step 3

ip ospf network point-to-multipoint

Configures an interface as point-to-multipoint for broadcast
media.

Example:
Device#(config-if) ip ospf network
point-to-multipoint

Step 4

exit

Enters global configuration mode.

Example:
Device#(config-if) exit

Step 5

router ospf process-id

Configures an OSPF routing process and enters router
configuration mode.

Example:
Device#(config) router ospf 109

Step 6

neighbor ip-address [cost number]

Specifies a neighbor and assigns a cost to the neighbor.
Note

Example:
Device#(config-router) neighbor 192.168.3.4
cost 180

Repeat this step for each neighbor if you want to
specify a cost. Otherwise, neighbors will assume the
cost of the interface, based on the ip ospf cost
interface configuration command.

IP Routing: OSPF Configuration Guide
15


Configuring OSPF
Configuring OSPF over Different Physical Networks

Configuring OSPF for Nonbroadcast Networks
SUMMARY STEPS
1. configure terminal
2. interface type number
3. ip ospf network point-to-multipoint non-broadcast
4. exit
5. router ospf process-id
6. neighbor ip-address [cost number]

DETAILED STEPS

Step 1

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 2

interface type number

Specifies an interface type and number, and enters interface
configuration mode.

Example:
Device(config)# interface gigabitethernet
0/0/0

Step 3

ip ospf network point-to-multipoint non-broadcast Configures an interface as point-to-multipoint for
nonbroadcast media.
Example:
Device#(config-if) ip ospf network
point-to-multipoint non-broadcast

Step 4

exit

Enters global configuration mode.

Example:
Device#(config-if) exit

Step 5

router ospf process-id

Configures an OSPF routing process and enters router
configuration mode.

Example:
Device#(config) router ospf 109

Step 6

neighbor ip-address [cost number]

IP Routing: OSPF Configuration Guide
16

Specifies a neighbor and assigns a cost to the neighbor.


Configuring OSPF
Configuring OSPF Area Parameters

Command or Action

Purpose
Note

Example:
Device#(config-router) neighbor 192.168.3.4
cost 180

Repeat this step for each neighbor if you want to
specify a cost. Otherwise, neighbors will assume the
cost of the interface, based on the ip ospf cost
interface configuration command.

Configuring OSPF Area Parameters
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. area area-id authentication
5. area area-id stub [no summary]
6. area area-id default-cost cost
7. end

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

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Device(config)# router ospf 10

IP Routing: OSPF Configuration Guide
17


Configuring OSPF
Configuring OSPFv2 NSSA

Step 4

Command or Action

Purpose

area area-id authentication

Enables authentication for an OSPF area.

Example:
Device(config-router)# area 10.0.0.0
authentication

Step 5

area area-id stub [no summary]

Defines an area to be a stub area.

Example:
Device(config-router)# area 10.0.0.0 stub
no-summary

Step 6

area area-id default-cost cost

Specifies a cost for the default summary route that is
sent into a stub area or not-so-stubby area (NSSA)

Example:
Device(config-router)# area 10.0.0.0 default-cost
1

Step 7

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Configuring OSPFv2 NSSA
Configuring an OSPFv2 NSSA Area and Its Parameters
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. redistribute protocol [process-id] {level-1 | level-1-2 | level-2} [autonomous-system-number] [metric
{metric-value | transparent}] [metric-type type-value] [match {internal | external 1 | external 2}]
[tag tag-value] [route-map map-tag] [subnets] [nssa-only]
5. network ip-address wildcard-mask area area-id
6. area area-id nssa [no-redistribution] [default-information-originate [metric] [metric-type]]
[no-summary] [nssa-only]
7. summary-address prefix mask [not-advertise] [tag tag] [nssa-only]
8. end

IP Routing: OSPF Configuration Guide
18


Configuring OSPF
Configuring OSPFv2 NSSA

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

router ospf process-id
Example:
Device(config)# router ospf 10

Step 4

Enables OSPF routing and enters router configuration
mode.
• The process-id argument identifies the OSPF
process. The range is from 1 to 65535.

Redistributes routes from one routing domain to another
redistribute protocol [process-id] {level-1 | level-1-2 |
level-2} [autonomous-system-number] [metric {metric-value routing domain.
| transparent}] [metric-type type-value] [match {internal
• In the example, Routing Information Protocol
| external 1 | external 2}] [tag tag-value] [route-map
(RIP) subnets are redistributed into the OSPF
map-tag] [subnets] [nssa-only]
domain.
Example:
Device(config-router)# redistribute rip subnets

Step 5

network ip-address wildcard-mask area area-id

Defines the interfaces on which OSPF runs and the area
ID for those interfaces.

Example:
Device(config-router)# network 192.168.129.11
0.0.0.255 area 1

Step 6

area area-id nssa [no-redistribution]
[default-information-originate [metric] [metric-type]]
[no-summary] [nssa-only]

Configures a Not-So-Stubby Area (NSSA) area.

Example:
Device(config-router)# area 1 nssa

Step 7

summary-address prefix mask [not-advertise] [tag tag]
[nssa-only]

Controls the route summarization and filtering during
the translation and limits the summary to NSSA areas.

Example:
Device(config-router)# summary-address 10.1.0.0

IP Routing: OSPF Configuration Guide
19


Configuring OSPF
Configuring OSPFv2 NSSA

Command or Action

Purpose

255.255.0.0 not-advertise

Step 8

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Configuring an NSSA ABR as a Forced NSSA LSA Translator
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. area area-id nssa translate type7 always
5. area area-id nssa translate type7 suppress-fa
6. end

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

router ospf process-id
Example:
Device(config)# router ospf 1

IP Routing: OSPF Configuration Guide
20

Enables OSPF routing and enters router configuration mode.
• The process-id argument identifies the OSPF process. The
range is from 1 to 65535.


Configuring OSPF
Configuring OSPFv2 NSSA

Step 4

Command or Action

Purpose

area area-id nssa translate type7 always

Configures a Not-So-Stubby Area Area Border Router (NSSA
ABR) device as a forced NSSA Link State Advertisement (LSA)
translator.

Example:
Device(config-router)# area 10 nssa
translate type7 always

Step 5

Note

You can use the always keyword in the area nssa
translate command to configure an NSSA ABR device
as a forced NSSA LSA translator. This command can be
used if RFC 3101 is disabled and RFC 1587 is used.

area area-id nssa translate type7 suppress-fa Allows ABR to suppress the forwarding address in translated Type-5
LSA.
Example:
Device(config-router)# area 10 nssa
translate type7 suppress-fa

Step 6

Exits router configuration mode and returns to privileged EXEC
mode.

end
Example:
Device(config-router)# end

Disabling RFC 3101 Compatibility and Enabling RFC 1587 Compatibility
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. compatible rfc1587
5. end

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
21


Configuring OSPF
Configuring OSPF NSSA Parameters

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router ospf process-id

• The process-id argument identifies the OSPF process.

Example:
Device(config)# router ospf 1

Step 4

Enables OSPF routing and enters router configuration mode.

compatible rfc1587

• Use router ospf process-id command to enable OSPFv2
routing.
Enables the device to be RFC 1587 compliant.

Example:
Device(config-router)# compatible rfc1587

Step 5

Exits router configuration mode and returns to privileged EXEC
mode.

end
Example:
Device(config-router)# end

Configuring OSPF NSSA Parameters
Prerequisites
Evaluate the following considerations before you implement this feature:
• You can set a Type 7 default route that can be used to reach external destinations. When configured, the
device generates a Type 7 default into the Not-So-Stubby Area (NSSA or the NSSA Area Border Router
(ABR).
• Every device within the same area must agree that the area is NSSA; otherwise, the devices cannot
communicate.

IP Routing: OSPF Configuration Guide
22


Configuring OSPF
Configuring Route Summarization Between OSPF Areas

Configuring Route Summarization Between OSPF Areas
Configuring Route Summarization When Redistributing Routes into OSPF
SUMMARY STEPS
1. summary-address {ip-address mask | prefix mask} [not-advertise][tag tag [nssa-only]

DETAILED STEPS

Step 1

Command or Action

Purpose

summary-address {ip-address mask | prefix mask}
[not-advertise][tag tag [nssa-only]

Specifies an address and mask that covers redistributed routes,
so that only one summary route is advertised.

Example:
Device#(config-router) summary-address 10.1.0.0
255.255.0.0

• You can use the optional not-advertise keyword to filter
out a set of routes.

Establishing Virtual Links
SUMMARY STEPS
1. area area-id virtual-link router-id [authentication [message-digest | null]] [hello-interval seconds]
[retransmit-interval seconds] [transmit-delay seconds] [dead-interval seconds] [authentication-key
key | message-digest-key key-id md5 key]

DETAILED STEPS
Command or Action
Step 1

Purpose

Establishes a virtual link.
area area-id virtual-link router-id [authentication [message-digest | null]]
[hello-interval seconds] [retransmit-interval seconds] [transmit-delay seconds]
[dead-interval seconds] [authentication-key key | message-digest-key key-id md5 key]
Example:
Device(config-router-af)# area 1 virtual-link 10.1.1.1 router1

IP Routing: OSPF Configuration Guide
23


Configuring OSPF
Generating a Default Route

Generating a Default Route
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. default-information originate [always] [metric metric-value] [metric-type type-value] [route-map
map-name]
5. end

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

router ospf process-id

Enables OSPF routing and enters router configuration mode.

Example:
Device(config)# router ospf 109

Step 4

default-information originate [always] [metric Forces the ASBR to generate a default route into the OSPF
metric-value] [metric-type type-value] [route-map routing domain.
map-name]
Note
The always keyword includes the following exception
Example:
Device(config-router)# default-information
originate always

Step 5

end
Example:
Device(config-router)# end

IP Routing: OSPF Configuration Guide
24

when a route map is used. When a route map is used,
the origination of the default route by OSPF is not
bound to the existence of a default route in the routing
table.
Exits router configuration mode and returns to privileged EXEC
mode.


Configuring OSPF
Configuring Lookup of DNS Names

Configuring Lookup of DNS Names
SUMMARY STEPS
1. enable
2. configure terminal
3. ip ospf name-lookup
4. end

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

ip ospf name-lookup

Enables OSPF routing and enters router configuration mode.

Example:
Device# ip ospf name-lookup

Step 4

end

Exits global configuration mode and returns to privileged
EXEC mode.

Example:
Device(config)# end

Forcing the Router ID Choice with a Loopback Interface
SUMMARY STEPS
1. configure terminal
2. interface type number
3. ip address ip-address mask

IP Routing: OSPF Configuration Guide
25


Configuring OSPF
Controlling Default Metrics

DETAILED STEPS

Step 1

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 2

interface type number

Creates a loopback interface and enters interface
configuration mode.

Example:
Device(config)# interface loopback 0

Step 3

ip address ip-address mask

Assigns an IP address to this interface.

Example:
Device#(config-if) ip address 192.108.1.27
255.255.255.0

Controlling Default Metrics
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. auto-cost reference-bandwidth ref-bw
5. end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device> enable

IP Routing: OSPF Configuration Guide
26

• Enter your password if prompted.


Configuring OSPF
Changing the OSPF Administrative Distances

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Device# router ospf 109

Step 4

auto-cost reference-bandwidth ref-bw

Differentiates high -bandwidth links.

Example:
Device(config-router)# auto-cost
reference-bandwidth 101

Step 5

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Changing the OSPF Administrative Distances
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. distance ospf {intra-area | inter-area | external} dist
5. end

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
27


Configuring OSPF
Configuring OSPF on Simplex Ethernet Interfaces

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Device(config)# router ospf 109

Step 4

distance ospf {intra-area | inter-area | external} dist

Changes the OSPF distance values.

Example:
Device(config-router)# distance ospf external
200

Step 5

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Configuring OSPF on Simplex Ethernet Interfaces
Command

Purpose

Suppresses the sending of hello packets through the
passive-interface interface-type interface-number specified interface.

Configuring Route Calculation Timers
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. timers throttle spf spf-start spf-hold spf-max-wait
5. end

IP Routing: OSPF Configuration Guide
28


Configuring OSPF
Configuring OSPF over On-Demand Circuits

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

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Device(config)# router ospf 109

Step 4

timers throttle spf spf-start spf-hold spf-max-wait

Configures route calculation timers.

Example:
Device(config-router)# timers throttle spf 5 1000
9000

Step 5

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Configuring OSPF over On-Demand Circuits
SUMMARY STEPS
1. router ospf process-id
2. interface type number
3. ip ospf demand-circuit

IP Routing: OSPF Configuration Guide
29


Configuring OSPF
Configuring OSPF over On-Demand Circuits

DETAILED STEPS
Command or Action

Purpose

Step 1

router ospf process-id

Enables OSPF operation.

Step 2

interface type number

Enters interface configuration mode.

Step 3

ip ospf demand-circuit

Configures OSPF over an on-demand circuit.

What to Do Next

Note

You can prevent an interface from accepting demand-circuit requests from other routers to by specifying
the ignore keyword in the ip ospf demand-circuit command.

Prerequisites
Evaluate the following considerations before implementing the On-Demand Circuits feature:
• Because LSAs that include topology changes are flooded over an on-demand circuit, we recommend
that you put demand circuits within OSPF stub areas or within NSSAs to isolate the demand circuits
from as many topology changes as possible.
• Every router within a stub area or NSSA must have this feature loaded in order to take advantage of the
on-demand circuit functionality. If this feature is deployed within a regular area, all other regular areas
must also support this feature before the demand circuit functionality can take effect because Type 5
external LSAs are flooded throughout all areas.
• Hub-and-spoke network topologies that have a point-to-multipoint (P2MP) OSPF interface type on a
hub might not revert to nondemand circuit mode when needed. You must simultaneously reconfigure
OSPF on all interfaces on the P2MP segment when reverting them from demand circuit mode to
nondemand circuit mode.
• Do not implement this feature on a broadcast-based network topology because the overhead protocols
(such as hello and LSA packets) cannot be successfully suppressed, which means the link will remain
up.
• Configuring the router for an OSPF on-demand circuit with an asynchronous interface is not a supported
configuration. The supported configuration is to use dialer interfaces on both ends of the circuit. For
more information, refer to Why OSPF Demand Circuit Keeps Bringing Up the Link .

IP Routing: OSPF Configuration Guide
30


Configuring OSPF
Logging Neighbors Going Up or Down

Logging Neighbors Going Up or Down
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. log-adjacency-changes [detail]
5. end

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

router ospf process-id

Enables OSPF routing and enters router configuration mode.

Example:
Device(config)# router ospf 109

Step 4

log-adjacency-changes [detail]
Example:
Device(config-router)#
log-adjacency-changes detail

Step 5

end

Changes the group pacing of LSAs.
Note
Configure the log-adjacency-changes command if you want
to know about OSPF neighbors going up or down without
turning on the debug ip ospf adjacency EXEC command
because the log-adjacency-changes command provides a
higher-level view of the peer relationship with less output.
Configure the log-adjacency-changes detail command if you
want to see messages for each state change.
Exits router configuration mode and returns to privileged EXEC mode.

Example:
Device(config-router)# end

IP Routing: OSPF Configuration Guide
31


Configuring OSPF
Logging Neighbors Going Up or Down

Changing the LSA Group Pacing Interval
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. timers pacing lsa-group seconds
5. end

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

router ospf process-id

Enables OSPF routing and enters router configuration
mode.

Example:
Device(config)# router ospf 109

Step 4

timers pacing lsa-group seconds

Changes the group pacing of LSAs.

Example:
Device(config-router)# timers pacing lsa-group
60

Step 5

end
Example:
Device(config-router)# end

IP Routing: OSPF Configuration Guide
32

Exits router configuration mode and returns to privileged
EXEC mode.


Configuring OSPF
Blocking OSPF LSA Flooding

Blocking OSPF LSA Flooding
Command

Purpose

ip ospf database-filter all out

Blocks the flooding of OSPF LSA packets to the
interface.

On point-to-multipoint networks, to block flooding of OSPF LSAs, use the following command in router
configuration mode:
Command

Purpose

neighbor ip-address database-filter all out

Blocks the flooding of OSPF LSA packets to the
specified neighbor.

Reducing LSA Flooding
Command

Purpose

ip ospf flood-reduction

Suppresses the unnecessary flooding of LSAs in stable
topologies.

Ignoring MOSPF LSA Packets
Command

Purpose

ignore lsa mospf

Prevents the router from generating syslog messages
when it receives MOSPF LSA packets.

IP Routing: OSPF Configuration Guide
33


Configuring OSPF
Monitoring and Maintaining OSPF

Monitoring and Maintaining OSPF
Command

Purpose

show ip ospf [process-id]

Displays general information about
OSPF routing processes.

show ip ospf border-routers

Displays the internal OSPF routing
table entries to the ABR and ASBR.
Displays lists of information related
to the OSPF database.

IP Routing: OSPF Configuration Guide
34


Configuring OSPF
Monitoring and Maintaining OSPF

Command

Purpose

show ip ospf [process-id
[area-id]] database
show ip ospf [process-id
[area-id]] database [database-summary]
show ip ospf [process-id
[area-id]] database [router] [self-originate]
show ip ospf [process-id
[area-id]] database [router] [adv-router [ip-address]]
show ip ospf [process-id
[area-id]] database [router] [link-state-id]
show ip ospf [process-id
[area-id]] database [network] [link-state-id]
show ip ospf [process-id
[area-id]] database [summary] [link-state-id]
show ip ospf [process-id
[area-id]] database [asbr-summary] [link-state-id]
show ip ospf [process-id
[Router# area-id]] database [external] [link-state-id]
show ip ospf [process-id
[area-id]] database [nssa-external] [link-state-id]
show ip ospf [process-id
[area-id]] database [opaque-link] [link-state-id]
show ip ospf [process-id
[area-id]] database [opaque-area] [link-state-id]
show ip ospf [process-id
[area-id]] database [opaque-as] [link-state-id]
show ip ospf flood-list interface type

Displays a list of LSAs waiting to be
flooded over an interface (to observe
OSPF packet pacing).

show ip ospf interface [type number]

Displays OSPF-related interface
information.

IP Routing: OSPF Configuration Guide
35


Configuring OSPF
Monitoring and Maintaining OSPF

Command

Purpose

show ip ospf neighbor [interface-name] [neighbor-id] detail

Displays OSPF neighbor information
on a per-interface basis.
Displays a list of all LSAs requested
by a router.

show ip ospf request-list [neighbor] [interface]
[interface-neighbor]
show ip ospf retransmission-list [neighbor] [interface]
[interface-neighbor]

Displays a list of all LSAs waiting to
be re-sent.

show ip ospf [process-id] summary-address

Displays a list of all summary address
redistribution information configured
under an OSPF process.

show ip ospf virtual-links

Displays OSPF-related virtual links
information.

To restart an OSPF process, use the following command in EXEC mode:
Command

Purpose

clear ip ospf [pid] {process | redistribution
| counters [neighbor [ neighbor - interface]

Clears redistribution based on the OSPF routing
process ID. If the pid option is not specified, all OSPF
processes are cleared.

[neighbor-id]]}

Displaying OSPF Update Packet Pacing
SUMMARY STEPS
1. show ip ospf flood-list interface-type interface-number

DETAILED STEPS

Step 1

Command or Action

Purpose

show ip ospf flood-list interface-type interface-number

Displays a list of OSPF LSAs waiting to be flooded
over an interface.

Example:
Device> show ip ospf flood-list ethernet 1

IP Routing: OSPF Configuration Guide
36


Configuring OSPF
Restrictions for OSPF

Restrictions for OSPF
On systems with a large number of interfaces, it may be possible to configure OSPF such that the number of
links advertised in the router LSA causes the link-state update packet to exceed the size of a “huge” Cisco
buffer. To resolve this problem, reduce the number of OSPF links or increase the huge buffer size by entering
the buffers huge size size command.
A link-state update packet containing a router LSA typically has a fixed overhead of 196 bytes, and an
additional 12 bytes are required for each link description. With a huge buffer size of 18024 bytes, there can
be a maximum of 1485 link descriptions.
Because the maximum size of an IP packet is 65,535 bytes, there is still an upper bound on the number of
links possible on a router.

Configuration Examples for OSPF
Example: OSPF Point-to-Multipoint
In the figure below, Router 1 uses data-link connection identifier (DLCI) 201 to communicate with Router 2,
DLCI 202 to communicate with Router 4, and DLCI 203 to communicate with Router 3. Router 2 uses DLCI
101 to communicate with Router 1 and DLCI 102 to communicate with Router 3. Router 3 communicates
with Router 2 (DLCI 401) and Router 1 (DLCI 402). Router 4 communicates with Router 1 (DLCI 301).
Configuration examples follow the figure.
Figure 4: OSPF Point-to-Multipoint Example

Router 1 Configuration
hostname Router 1
!
interface serial 1
ip address 10.0.0.2 255.0.0.0
ip ospf network point-to-multipoint
encapsulation frame-relay
frame-relay map ip 10.0.0.1 201 broadcast
frame-relay map ip 10.0.0.3 202 broadcast
frame-relay map ip 10.0.0.4 203 broadcast
!
router ospf 1
network 10.0.0.0 0.0.0.255 area 0

IP Routing: OSPF Configuration Guide
37


Configuring OSPF
Example: OSPF Point-to-Multipoint with Broadcast

Router 2 Configuration
hostname Router 2
!
interface serial 0
ip address 10.0.0.1 255.0.0.0
ip ospf network point-to-multipoint
encapsulation frame-relay
frame-relay map ip 10.0.0.2 101 broadcast
frame-relay map ip 10.0.0.4 102 broadcast
!
router ospf 1
network 10.0.0.0 0.0.0.255 area 0

Router 3 Configuration
hostname Router 3
!
interface serial 3
ip address 10.0.0.4 255.0.0.0
ip ospf network point-to-multipoint
encapsulation frame-relay
clock rate 1000000
frame-relay map ip 10.0.0.1 401 broadcast
frame-relay map ip 10.0.0.2 402 broadcast
!
router ospf 1
network 10.0.0.0 0.0.0.255 area 0

Router 4 Configuration
hostname Router 4
!
interface serial 2
ip address 10.0.0.3 255.0.0.0
ip ospf network point-to-multipoint
encapsulation frame-relay
clock rate 2000000
frame-relay map ip 10.0.0.2 301 broadcast
!
router ospf 1
network 10.0.0.0 0.0.0.255 area 0

Example: OSPF Point-to-Multipoint with Broadcast
The following example illustrates a point-to-multipoint network with broadcast:
interface Serial0
ip address 10.0.1.1 255.255.255.0
encapsulation frame-relay
ip ospf cost 100
ip ospf network point-to-multipoint
frame-relay map ip 10.0.1.3 202 broadcast
frame-relay map ip 10.0.1.4 203 broadcast
frame-relay map ip 10.0.1.5 204 broadcast
frame-relay local-dlci 200
!
router ospf 1
network 10.0.1.0 0.0.0.255 area 0
neighbor 10.0.1.5 cost 5
neighbor 10.0.1.4 cost 10

IP Routing: OSPF Configuration Guide
38


Configuring OSPF
Example: OSPF Point-to-Multipoint with Nonbroadcast

The following example shows the configuration of the neighbor at 10.0.1.3:
interface serial 0
ip address 10.0.1.3 255.255.255.0
ip ospf network point-to-multipoint
encapsulation frame-relay
frame-relay local-dlci 301
frame-relay map ip 10.0.1.1 300 broadcast
no shutdown
!
router ospf 1
network 10.0.1.0 0.0.0.255 area 0

The output shown for neighbors in the first configuration is as follows:
Device# show ip ospf neighbor
Neighbor ID
Pri
State
172.16.1.1
1
FULL/
172.16.1.4
1
FULL/
172.16.1.8
1
FULL/

-

Dead Time
Address
00:01:50
10.0.1.5
00:01:47
10.0.1.4
00:01:45
10.0.1.3

Interface
Serial0
Serial0
Serial0

The route information in the first configuration is as follows:
Device# show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, * - candidate default
U - per-user static route, o - ODR
Gateway of last resort is not set
C
1.0.0.0/8 is directly connected, Loopback0
10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O
10.0.1.3/32 [110/100] via 10.0.1.3, 00:39:08, Serial0
C
10.0.1.0/24 is directly connected, Serial0
O
10.0.1.5/32 [110/5] via 10.0.1.5, 00:39:08, Serial0
O
10.0.1.4/32 [110/10] via 10.0.1.4, 00:39:08, Serial0

Example: OSPF Point-to-Multipoint with Nonbroadcast
The following example illustrates a point-to-multipoint network with nonbroadcast:
interface Serial0
ip address 10.0.1.1 255.255.255.0
ip ospf network point-to-multipoint non-broadcast
encapsulation frame-relay
no keepalive
frame-relay local-dlci 200
frame-relay map ip 10.0.1.3 202
frame-relay map ip 10.0.1.4 203
frame-relay map ip 10.0.1.5 204
no shutdown
!
router ospf 1
network 10.0.1.0 0.0.0.255 area 0
neighbor 10.0.1.3 cost 5
neighbor 10.0.1.4 cost 10
neighbor 10.0.1.5 cost 15

The following example is the configuration for the router on the other side:
interface Serial9/2
ip address 10.0.1.3 255.255.255.0
encapsulation frame-relay
ip ospf network point-to-multipoint non-broadcast
no ip mroute-cache
no keepalive
no fair-queue

IP Routing: OSPF Configuration Guide
39


Configuring OSPF
Example: Variable-Length Subnet Masks

frame-relay local-dlci 301
frame-relay map ip 10.0.1.1 300
no shutdown
!
router ospf 1
network 10.0.1.0 0.0.0.255 area 0

The output shown for neighbors in the first configuration is as follows:
Device# show ip ospf neighbor
Neighbor ID
172.16.1.1
172.16.1.4
172.16.1.8

Pri

State
1
FULL/
1
FULL/
1
FULL/

-

Dead Time
Address
00:01:52
10.0.1.5
00:01:52
10.0.1.4
00:01:52
10.0.1.3

Interface
Serial0
Serial0
Serial0

Example: Variable-Length Subnet Masks
OSPF, static routes, and IS-IS support variable-length subnet masks (VLSMs). With VLSMs, you can use
different masks for the same network number on different interfaces, which allows you to conserve IP addresses
and more efficiently use available address space.
In the following example, a 30-bit subnet mask is used, leaving two bits of address space reserved for serial-line
host addresses. There is sufficient host address space for two host endpoints on a point-to-point serial link.
interface ethernet 0
ip address 172.16.10.1 255.255.255.0
! 8 bits of host address space reserved for ethernets
interface serial 0
ip address 172.16.20.1 255.255.255.252
! 2 bits of address space reserved for serial lines
! Router is configured for OSPF and assigned AS 107
router ospf 107
! Specifies network directly connected to the router
network 172.16.0.0 0.0.255.255 area 0.0.0.0

Example: Configuring OSPF NSSA
In the following example, an Open Shortest Path First (OSPF) stub network is configured to include OSPF
Area 0 and OSPF Area 1, using five devices. Device 3 is configured as the NSSA Autonomous System Border
Router (ASBR). Device 2 configured to be the NSSA Area Border Router (ABR). OSPF Area 1 is defined
as a Not-So-Stubby Area (NSSA).
Device 1
hostname Device1
!
interface Loopback1
ip address 10.1.0.1 255.255.255.255
!
interface Ethernet0/0
ip address 192.168.0.1 255.255.255.0
ip ospf 1 area 0
no cdp enable
!
interface Serial10/0
description Device2 interface s11/0
ip address 192.168.10.1 255.255.255.0
ip ospf 1 area 1
serial restart-delay 0
no cdp enable

IP Routing: OSPF Configuration Guide
40


Configuring OSPF
Example: Configuring OSPF NSSA

!
router ospf 1
area 1 nssa
!
end

Device 2
hostname Device2
!
!
interface Loopback1
ip address 10.1.0.2 255.255.255.255
!
interface Serial10/0
description Device1 interface s11/0
no ip address
shutdown
serial restart-delay 0
no cdp enable
!
interface Serial11/0
description Device1 interface s10/0
ip address 192.168.10.2 255.255.255.0
ip ospf 1 area 1
serial restart-delay 0
no cdp enable
!
interface Serial14/0
description Device3 interface s13/0
ip address 192.168.14.2 255.255.255.0
ip ospf 1 area 1
serial restart-delay 0
no cdp enable
!
router ospf 1
area 1 nssa
!
end

Device 3
hostname Device3
!
interface Loopback1
ip address 10.1.0.3 255.255.255.255
!
interface Ethernet3/0
ip address 192.168.3.3 255.255.255.0
no cdp enable
!
interface Serial13/0
description Device2 interface s14/0
ip address 192.168.14.3 255.255.255.0
ip ospf 1 area 1
serial restart-delay 0
no cdp enable
!
router ospf 1
log-adjacency-changes
area 1 nssa
redistribute rip subnets
!
router rip
version 2
redistribute ospf 1 metric 15
network 192.168.3.0
end

IP Routing: OSPF Configuration Guide
41


Configuring OSPF
Example: OSPF NSSA Area with RFC 3101 Disabled and RFC 1587 Active

Device 4
hostname Device4
!
interface Loopback1
ip address 10.1.0.4 255.255.255.255
!
interface Ethernet3/0
ip address 192.168.3.4 255.255.255.0
no cdp enable
!
interface Ethernet4/1
ip address 192.168.41.4 255.255.255.0
!
router rip
version 2
network 192.168.3.0
network 192.168.41.0
!
end

Device 5
hostname Device5
!
interface Loopback1
ip address 10.1.0.5 255.255.255.255
!
interface Ethernet0/0
ip address 192.168.0.10 255.255.255.0
ip ospf 1 area 0
no cdp enable
!
interface Ethernet1/1
ip address 192.168.11.10 255.255.255.0
ip ospf 1 area 0
!
router ospf 1
!
end

Example: OSPF NSSA Area with RFC 3101 Disabled and RFC 1587 Active
In the following example, the output for the show ip ospf and show ip ospf database nssa commands shows
an Open Shortest Path First Not-So-Stubby Area (OSPF NSSA) area where RFC 3101 is disabled, RFC 1587
is active, and an NSSA Area Border Router (ABR) device is configured as a forced NSSA LSA translator. If
RFC 3101 is disabled, the forced NSSA LSA translator remains inactive.
Device# show ip ospf
Routing Process "ospf 1" with ID 10.0.2.1
Start time: 00:00:25.512, Time elapsed: 00:01:02.200
Supports only single TOS(TOS0) routes
Supports opaque LSA
Supports Link-local Signaling (LLS)
Supports area transit capability
Supports NSSA (compatible with RFC 1587)
Event-log enabled, Maximum number of events: 1000, Mode: cyclic
Router is not originating router-LSAs with maximum metric
Initial SPF schedule delay 5000 msecs
Minimum hold time between two consecutive SPFs 10000 msecs
Maximum wait time between two consecutive SPFs 10000 msecs
Incremental-SPF disabled
Minimum LSA interval 5 secs
Minimum LSA arrival 1000 msecs

IP Routing: OSPF Configuration Guide
42


Configuring OSPF
Example: OSPF NSSA Area with RFC 3101 Disabled and RFC 1587 Active

LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
Number of external LSA 0. Checksum Sum 0x000000
Number of opaque AS LSA 0. Checksum Sum 0x000000
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 1. 0 normal 0 stub 1 nssa
Number of areas transit capable is 0
External flood list length 0
IETF NSF helper support enabled
Cisco NSF helper support enabled
Reference bandwidth unit is 100 mbps
Area 1
Number of interfaces in this area is 1
It is a NSSA area
Configured to translate Type-7 LSAs, inactive (RFC3101 support
disabled)
Area has no authentication
SPF algorithm last executed 00:00:07.160 ago
SPF algorithm executed 3 times
Area ranges are
Number of LSA 3. Checksum Sum 0x0245F0
Number of opaque link LSA 0. Checksum Sum 0x000000
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0

The table below describes the show ip ospf display fields and their descriptions.
Table 1: show ip ospf Field Descriptions

Field

Description

Supports NSSA (compatible with RFC 1587)

Specifies that RFC 1587 is active or that the OSPF
NSSA area is RFC 1587 compatible.

Configured to translate Type-7 LSAs, inactive
(RFC3101 support disabled)

Specifies that OSPF NSSA area has an ABR device
configured to act as a forced translator of Type 7
LSAs. However, it is inactive because RFC 3101 is
disabled

Device2# show ip ospf database nssa
Router Link States (Area 1)
LS age: 28
Options: (No TOS-capability, DC)
LS Type: Router Links
Link State ID: 10.0.2.1
Advertising Router: 10.0.2.1
LS Seq Number: 80000004
Checksum: 0x5CA2
Length: 36
Area Border Router
AS Boundary Router
Unconditional NSSA translator
Number of Links: 1
Link connected to: a Stub Network
(Link ID) Network/subnet number: 192.0.2.5
(Link Data) Network Mask: 255.255.255.0
Number of MTID metrics: 0
TOS 0 Metrics: 10

The table below describes the show ip ospf database nssa display fields and their descriptions.

IP Routing: OSPF Configuration Guide
43


Configuring OSPF
Example: OSPF Routing and Route Redistribution

Table 2: show ip ospf database nssa Field Descriptions

Field

Description

Unconditional NSSA translator

Specifies that NSSA ASBR device is a forced NSSA
LSA translator

Example: OSPF Routing and Route Redistribution
OSPF typically requires coordination among many internal routers, ABRs, and ASBRs. At a minimum,
OSPF-based routers can be configured with all default parameter values, with no authentication, and with
interfaces assigned to areas.
Three types of examples follow:
• The first is a simple configuration illustrating basic OSPF commands.
• The second example illustrates a configuration for an internal router, ABR, and ASBRs within a single,
arbitrarily assigned, OSPF autonomous system.
• The third example illustrates a more complex configuration and the application of various tools available
for controlling OSPF-based routing environments.

Example: Basic OSPF Configuration
The following example illustrates a simple OSPF configuration that enables OSPF routing process 9000,
attaches Ethernet interface 0 to area 0.0.0.0, and redistributes RIP into OSPF and OSPF into RIP:
interface ethernet 0
ip address 10.93.1.1 255.255.255.0
ip ospf cost 1
!
interface ethernet 1
ip address 10.94.1.1 255.255.255.0
!
router ospf 9000
network 10.93.0.0 0.0.255.255 area 0.0.0.0
redistribute rip metric 1 subnets
!
router rip
network 10.94.0.0
redistribute ospf 9000
default-metric 1

Example: Basic OSPF Configuration for Internal Router ABR and ASBRs
The following example illustrates the assignment of four area IDs to four IP address ranges. In the example,
OSPF routing process 109 is initialized, and four OSPF areas are defined: 10.9.50.0, 2, 3, and 0. Areas
10.9.50.0, 2, and 3 mask specific address ranges, and area 0 enables OSPF for all other networks.
router ospf 109
network 192.168.10.0 0.0.0.255 area 10.9.50.0
network 192.168.20.0 0.0.255.255 area 2
network 192.168.30.0 0.0.0.255 area 3
network 192.168.40.0 255.255.255.255 area 0

IP Routing: OSPF Configuration Guide
44


Configuring OSPF
Example: OSPF Routing and Route Redistribution

!
! Interface Ethernet0 is in area 10.9.50.0:
interface ethernet 0
ip address 192.168.10.5 255.255.255.0
!
! Interface Ethernet1 is in area 2:
interface ethernet 1
ip address 192.168.20.5 255.255.255.0
!
! Interface Ethernet2 is in area 2:
interface ethernet 2
ip address 192.168.20.7 255.255.255.0
!
! Interface Ethernet3 is in area 3:
interface ethernet 3
ip address 192.169.30.5 255.255.255.0
!
! Interface Ethernet4 is in area 0:
interface ethernet 4
ip address 192.168.40.1 255.255.255.0
!
! Interface Ethernet5 is in area 0:
interface ethernet 5
ip address 192.168.40.12 255.255.0.0

Each network area router configuration command is evaluated sequentially, so the order of these commands
in the configuration is important. The Cisco software sequentially evaluates the address/wildcard-mask pair
for each interface. See the network area command page in the Cisco IOS IP Routing: OSPF Command
Reference for more information.
Consider the first network area command. Area ID 10.9.50.0 is configured for the interface on which subnet
192.168.10.0 is located. Assume that a match is determined for Ethernet interface 0. Ethernet interface 0 is
attached to area 10.9.50.0 only.
The second network area command is evaluated next. For area 2, the same process is then applied to all
interfaces (except Ethernet interface 0). Assume that a match is determined for Ethernet interface 1. OSPF is
then enabled for that interface, and Ethernet interface 1 is attached to area 2.
This process of attaching interfaces to OSPF areas continues for all network area commands. Note that the
last network area command in this example is a special case. With this command, all available interfaces
(not explicitly attached to another area) are attached to area 0.

IP Routing: OSPF Configuration Guide
45


Configuring OSPF
Example: OSPF Routing and Route Redistribution

Example: Complex Internal Router with ABR and ASBR
The following example outlines a configuration for several routers within a single OSPF autonomous system.
The figure below provides a general network map that illustrates this sample configuration.
Figure 5: Sample OSPF Autonomous System Network Map

In this configuration, five routers are configured with OSPF:
• Router A and Router B are both internal routers within area 1.
• Router C is an OSPF ABR. Note that for Router C, Area 1 is assigned to E3 and area 0 is assigned to
S0.
• Router D is an internal router in area 0 (backbone area). In this case, both network router configuration
commands specify the same area (area 0, or the backbone area).
• Router E is an OSPF ASBR. Note that BGP routes are redistributed into OSPF and that these routes are
advertised by OSPF.

IP Routing: OSPF Configuration Guide
46


Configuring OSPF
Example: OSPF Routing and Route Redistribution

Note

You do not need to include definitions of all areas in an OSPF autonomous system in the configuration
of all routers in the autonomous system. Only the directly connected areas must be defined. In the example
that follows, routes in area 0 are learned by the routers in area 1 (Router A and Router B) when the ABR
(Router C) injects summary LSAs into area 1.
The OSPF domain in BGP autonomous system 109 is connected to the outside world via the BGP link to the
external peer at IP address 10.0.0.6. Sample configurations follow.
Following is the sample configuration for the general network map shown in the figure above.
Router A Configuration—Internal Router
interface ethernet 1
ip address 192.168.1.1 255.255.255.0
router ospf 1
network 192.168.0.0 0.0.255.255 area 1

Router B Configuration—Internal Router
interface ethernet 2
ip address 192.168.1.2 255.255.255.0
router ospf 202
network 192.168.0.0 0.0.255.255 area 1

Router C Configuration—ABR
interface ethernet 3
ip address 192.168.1.3 255.255.255.0
interface serial 0
ip address 192.168.2.3 255.255.255.0
router ospf 999
network 192.168.1.0 0.0.0.255 area 1
network 192.168.2.0 0.0.0.255 area 0

Router D Configuration—Internal Router
interface ethernet 4
ip address 10.0.0.4 255.0.0.0
interface serial 1
ip address 192.168.2.4 255.255.255.0
router ospf 50
network 192.168.2.0 0.0.0.255 area 0
network 10.0.0.0 0.255.255.255 area 0

Router E Configuration—ASBR
interface ethernet 5
ip address 10.0.0.5 255.0.0.0
interface serial 2
ip address 172.16.1.5 255.255.255.0
router ospf 65001
network 10.0.0.0 0.255.255.255 area 0
redistribute bgp 109 metric 1 metric-type 1
router bgp 109
network 192.168.0.0
network 10.0.0.0
neighbor 172.16.1.6 remote-as 110

IP Routing: OSPF Configuration Guide
47


Configuring OSPF
Example: OSPF Routing and Route Redistribution

Example: Complex OSPF Configuration for ABR
The following sample configuration accomplishes several tasks in setting up an ABR. These tasks can be split
into two general categories:
• Basic OSPF configuration
• Route redistribution
The specific tasks outlined in this configuration are detailed briefly in the following descriptions. The figure
below illustrates the network address ranges and area assignments for the interfaces.
Figure 6: Interface and Area Specifications for OSPF Sample Configuration

The basic configuration tasks in this example are as follows:
• Configure address ranges for Ethernet interface 0 through Ethernet interface 3.
• Enable OSPF on each interface.
• Set up an OSPF authentication password for each area and network.
• Assign link-state metrics and other OSPF interface configuration options.
• Create a stub area with area ID 36.0.0.0. (Note that the authentication and stub options of the area
router configuration command are specified with separate area command entries, but can be merged
into a single area command.)
• Specify the backbone area (area 0).
Configuration tasks associated with redistribution are as follows:
• Redistribute IGRP and RIP into OSPF with various options set (including including metric-type, metric,
tag, and subnet).
• Redistribute IGRP and OSPF into RIP.

IP Routing: OSPF Configuration Guide
48


Configuring OSPF
Examples: Route Map

The following is a sample OSPF configuration:
interface ethernet 0
ip address 192.0.2.201 255.255.255.0
ip ospf authentication-key abcdefgh
ip ospf cost 10
!
interface ethernet 1
ip address 172.19.251.202 255.255.255.0
ip ospf authentication-key ijklmnop
ip ospf cost 20
ip ospf retransmit-interval 10
ip ospf transmit-delay 2
ip ospf priority 4
!
interface ethernet 2
ip address 172.19.254.2 255.255.255.0
ip ospf authentication-key abcdefgh
ip ospf cost 10
!
interface ethernet 3
ip address 10.56.0.0 255.255.0.0
ip ospf authentication-key ijklmnop
ip ospf cost 20
ip ospf dead-interval 80

In the following configuration, OSPF is on network 172.16.0.0:
router ospf 201
network 10.10.0.0 0.255.255.255 area 10.10.0.0
network 192.42.110.0 0.0.0.255 area 192.42.110.0
network 172.16.0.0 0.0.255.255 area 0
area 0 authentication
area 10.10.0.0 stub
area 10.10.0.0 authentication
area 10.10.0.0 default-cost 20
area 192.42.110.0 authentication
area 10.10.0.0 range 10.10.0.0 255.0.0.0
area 192.42.110.0 range 192.42.110.0 255.255.255.0
area 0 range 172.16.251.0 255.255.255.0
area 0 range 172.16.254.0 255.255.255.0
redistribute igrp 200 metric-type 2 metric 1 tag 200 subnets
redistribute rip metric-type 2 metric 1 tag 200

In the following configuration, IGRP autonomous system 200 is on 192.0.2.1:
router igrp 200
network 172.31.0.0
!
! RIP for 192.168.110
!
router rip
network 192.168.110.0
redistribute igrp 200 metric 1
redistribute ospf 201 metric 1

Examples: Route Map
The examples in this section illustrate the use of redistribution, with and without route maps. Examples from
the IP and Connectionless Network Service (CLNS) routing protocols are given.
The following example redistributes all OSPF routes into IGRP:
router igrp 109
redistribute ospf 110

IP Routing: OSPF Configuration Guide
49


Configuring OSPF
Examples: Route Map

The following example redistributes RIP routes with a hop count equal to 1 into OSPF. These routes will be
redistributed into OSPF as external LSAs with a metric of 5, a metric type of Type 1, and a tag equal to 1.
router ospf 109
redistribute rip route-map rip-to-ospf
!
route-map rip-to-ospf permit
match metric 1
set metric 5
set metric-type type1
set tag 1

The following example redistributes OSPF learned routes with tag 7 as a RIP metric of 15:
router rip
redistribute ospf 109 route-map 5
!
route-map 5 permit
match tag 7
set metric 15

The following example redistributes OSPF intra-area and interarea routes with next-hop routers on serial
interface 0 into BGP with an INTER_AS metric of 5:
router bgp 109
redistribute ospf 109 route-map 10
!
route-map 10 permit
match route-type internal
match interface serial 0
set metric 5

The following example redistributes two types of routes into the integrated IS-IS routing table (supporting
both IP and CLNS). The first type is OSPF external IP routes with tag 5; these routes are inserted into Level
2 IS-IS link state packets (LSPs) with a metric of 5. The second type is ISO-IGRP derived CLNS prefix routes
that match CLNS access list 2000; these routes will be redistributed into IS-IS as Level 2 LSPs with a metric
of 30.
router isis
redistribute ospf 109 route-map 2
redistribute iso-igrp nsfnet route-map 3
!
route-map 2 permit
match route-type external
match tag 5
set metric 5
set level level-2
!
route-map 3 permit
match address 2000
set metric 30

With the following configuration, OSPF external routes with tags 1, 2, 3, and 5 are redistributed into RIP with
metrics of 1, 1, 5, and 5, respectively. The OSPF routes with a tag of 4 are not redistributed.
router rip
redistribute ospf 109 route-map 1
!
route-map 1 permit
match tag 1 2
set metric 1
!
route-map 1 permit
match tag 3
set metric 5
!
route-map 1 deny
match tag 4
!

IP Routing: OSPF Configuration Guide
50


Configuring OSPF
Examples: Route Map

route map 1 permit
match tag 5
set metric 5

In the following configuration, a RIP-learned route for network 192.168.0.0 and an ISO-IGRP-learned route
with prefix 49.0001.0002 are redistributed into an IS-IS Level 2 LSP with a metric of 5:
router isis
redistribute rip route-map 1
redistribute iso-igrp remote route-map 1
!
route-map 1 permit
match ip address 1
match clns address 2
set metric 5
set level level-2
!
access-list 1 permit 192.168.0.0 0.0.255.255
clns filter-set 2 permit 49.0001.0002...

The following configuration example illustrates how a route map is referenced by the default-information
router configuration command. This type of reference is called conditional default origination. OSPF will
originate the default route (network 0.0.0.0) with a Type 2 metric of 5 if 172.16.0.0 is in the routing table.

Note

Only routes external to the OSPF process can be used for tracking, such as non-OSPF routes or OSPF
routes from a separate OSPF process.
route-map ospf-default permit
match ip address 1
set metric 5
set metric-type type-2
!
access-list 1 permit 172.16.0.0 0.0.255.255
!
router ospf 109
default-information originate route-map ospf-default

IP Routing: OSPF Configuration Guide
51


Configuring OSPF
Example: Changing the OSPF Administrative Distances

Example: Changing the OSPF Administrative Distances
The following configuration changes the external distance to 200, making it less trustworthy. The figure below
illustrates the example.
Figure 7: OSPF Administrative Distance

Router A Configuration
router ospf 1
redistribute ospf 2 subnet
distance ospf external 200
!
router ospf 2
redistribute ospf 1 subnet
distance ospf external 200

Router B Configuration
router ospf 1
redistribute ospf 2 subnet
distance ospf external 200
!
router ospf 2
redistribute ospf 1 subnet
distance ospf external 200

IP Routing: OSPF Configuration Guide
52


Configuring OSPF
Example: OSPF over On-Demand Routing

Example: OSPF over On-Demand Routing
The following configuration allows OSPF over an on-demand circuit, as shown in the figure below. Note that
the on-demand circuit is defined on one side only (BRI 0 on Router A); it is not required to be configured on
both sides.
Figure 8: OSPF over On-Demand Circuit

Router A Configuration
username RouterB password 7 060C1A2F47
isdn switch-type basic-5ess
ip routing
!
interface TokenRing0
ip address 192.168.50.5 255.255.255.0
no shutdown
!
interface BRI0
no cdp enable
description connected PBX 1485
ip address 192.168.45.30 255.255.255.0
encapsulation ppp
ip ospf demand-circuit
dialer map ip 192.0.2.6 name RouterB broadcast 61484
dialer-group 1
ppp authentication chap
no shutdown
!
router ospf 100
network 192.168.45.0 0.0.0.255 area 0
network 192.168.45.50 0.0.0.255 area 0
!
dialer-list 1 protocol ip permit

Router B Configuration
username RouterA password 7 04511E0804
isdn switch-type basic-5ess
ip routing
!
interface Ethernet0
ip address 192.168.50.16 255.255.255.0
no shutdown
!
interface BRI0
no cdp enable
description connected PBX 1484
ip address 192.168.45.17 255.255.255.0
encapsulation ppp
dialer map ip 192.168.45.19 name RouterA broadcast 61485
dialer-group 1
ppp authentication chap
no shutdown
!
router ospf 100
network 192.168.45.0 0.0.0.255 area 0

IP Routing: OSPF Configuration Guide
53


Configuring OSPF
Example: LSA Group Pacing

network 192.168.45.50 0.0.0.255 area 0
!
dialer-list 1 protocol ip permit

Example: LSA Group Pacing
The following example changes the OSPF pacing between LSA groups to 60 seconds:
router ospf
timers pacing lsa-group 60

Example: Blocking OSPF LSA Flooding
The following example prevents flooding of OSPF LSAs to broadcast, nonbroadcast, or point-to-point networks
reachable through Ethernet interface 0:
interface ethernet 0
ip ospf database-filter all out

The following example prevents flooding of OSPF LSAs to point-to-multipoint networks to the neighbor at
IP address 10.10.10.45:
router ospf 109
neighbor 10.10.10.45 database-filter all out

Example: Ignoring MOSPF LSA Packets
The following example configures the router to suppress the sending of syslog messages when it receives
MOSPF packets:
router ospf 109
ignore lsa mospf

Additional References for OSPF Not-So-Stubby Areas (NSSA)
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Protocol-independent features that work with OSPF “Configuring IP Routing Protocol-Independent
Features” module in IP Routing:
Protocol-Independent Configuration Guide

IP Routing: OSPF Configuration Guide
54


Configuring OSPF
Feature Information for Configuring OSPF

RFCs
RFC

Title

RFC 1587

The OSPF NSSA Option, March 1994

RFC 3101

The OSPF NSSA Option January 2003

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

Feature Information for Configuring OSPF
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 3: Feature Information for OSPF

Feature Name
OSPF

Releases

Feature Information
OSPF is an IGP developed by the
OSPF working group of the IETF.
Designed expressly for IP
networks, OSPF supports IP
subnetting and tagging of
externally derived routing
information. OSPF also allows
packet authentication and uses IP
multicast when sending and
receiving packets.

IP Routing: OSPF Configuration Guide
55


Configuring OSPF
Feature Information for Configuring OSPF

Feature Name

Releases

Feature Information

OSPFv3 RFC 3101 Support

Cisco IOS XE Release 3.7S

The area nssa translate (OSPFv3),
compatible rfc1587 (OSPFv3),
and show ospfv3 commands were
added. The nssa-only keyword
was added to the summary-prefix
(OSPFv3) command.

IP Routing: OSPF Configuration Guide
56
