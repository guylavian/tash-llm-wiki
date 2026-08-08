---
title: "Cisco BGP Overview"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-cisco-bgp-overview
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 2 Cisco BGP Overview Border Gateway Protocol (BGP) is an interdomain routing protocol designed to provide loop-free routing between separate routing domains that contain independent routing policies (autonomous systems). The Cisco software implementation of BGP version 4 includes support for 4-byte autonomous system numbers and multiprotocol extensions to allow BGP to carry routing infor"
---

# Cisco BGP Overview

CHAPTER

2

Cisco BGP Overview
Border Gateway Protocol (BGP) is an interdomain routing protocol designed to provide loop-free routing
between separate routing domains that contain independent routing policies (autonomous systems). The Cisco
software implementation of BGP version 4 includes support for 4-byte autonomous system numbers and
multiprotocol extensions to allow BGP to carry routing information for IP multicast routes and multiple Layer
3 protocol address families including IP Version 4 (IPv4), IP Version 6 (IPv6), Virtual Private Networks
Version 4 (VPNv4), Connectionless Network Services (CLNS), and Layer 2 VPN (L2VPN). This module
contains conceptual material to help you understand how BGP is implemented in Cisco software.
• Finding Feature Information, on page 3
• Prerequisites for Cisco BGP, on page 3
• Restrictions for Cisco BGP, on page 4
• Information About Cisco BGP, on page 4
• Additional References, on page 18
• Feature Information for Cisco BGP Overview, on page 19

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for Cisco BGP
This document assumes knowledge of CLNS, IPv4, IPv6, multicast, VPNv4, and Interior Gateway Protocols
(IGPs). The amount of knowledge required for each technology is dependent on your deployment.

IP Routing: BGP Configuration Guide
3


Cisco BGP Overview
Restrictions for Cisco BGP

Restrictions for Cisco BGP
A router that runs Cisco software can be configured to run only one BGP routing process and to be a member
of only one BGP autonomous system. However, a BGP routing process and autonomous system can support
multiple concurrent BGP address family and subaddress family configurations.

Information About Cisco BGP
BGP Version 4
Border Gateway Protocol (BGP) is an interdomain routing protocol designed to provide loop-free routing
between separate routing domains that contain independent routing policies (autonomous systems). The Cisco
software implementation of BGP version 4 includes multiprotocol extensions to allow BGP to carry routing
information for IP multicast routes and multiple Layer 3 protocol address families including IP Version 4
(IPv4), IP Version 6 (IPv6), Virtual Private Networks version 4 (VPNv4), and Connectionless Network
Services (CLNS).
BGP is mainly used to connect a local network to an external network to gain access to the Internet or to
connect to other organizations. When connecting to an external organization, external BGP (eBGP) peering
sessions are created. For more details about connecting to external BGP peers, see the “Connecting to a Service
Provider Using External BGP” chapter.
Although BGP is referred to as an exterior gateway protocol (EGP), many networks within an organization
are becoming so complex that BGP can be used to simplify the internal network used within the organization.
BGP peers within the same organization exchange routing information through internal BGP (iBGP) peering
sessions. For more details about internal BGP peers, see the “Configuring Internal BGP Features” chapter of
the Cisco IOS IP Routing Configuration Guide.

Note

BGP requires more configuration than other routing protocols and the effects of any configuration changes
must be fully understood. Incorrect configuration can create routing loops and negatively impact normal
network operation.

BGP Version 4 Functional Overview
BGP is an interdomain routing protocol designed to provide loop-free routing links between organizations.
BGP is designed to run over a reliable transport protocol; it uses TCP (port 179) as the transport protocol
because TCP is a connection-oriented protocol. The destination TCP port is assigned 179, and the local port
is assigned a random port number. Cisco software supports BGP version 4 and it is this version that has been
used by Internet service providers (ISPs) to help build the Internet. RFC 1771 introduced and discussed a
number of new BGP features to allow the protocol to scale for Internet use. RFC 2858 introduced multiprotocol
extensions to allow BGP to carry routing information for IP multicast routes and multiple Layer 3 protocol
address families, including IPv4, IPv6, and CLNS.
BGP is mainly used to connect a local network to an external network to gain access to the Internet or to
connect to other organizations. When connecting to an external organization, external BGP (eBGP) peering
sessions are created. Although BGP is referred to as an exterior gateway protocol (EGP), many networks

IP Routing: BGP Configuration Guide
4


Cisco BGP Overview
BGP Autonomous Systems

within an organization are becoming so complex that BGP can be used to simplify the internal network used
within the organization. BGP peers within the same organization exchange routing information through internal
BGP (iBGP) peering sessions.
BGP uses a path-vector routing algorithm to exchange network reachability information with other
BGP-speaking networking devices. Network reachability information is exchanged between BGP peers in
routing updates. Network reachability information contains the network number, path-specific attributes, and
the list of autonomous system numbers that a route must transit to reach a destination network. This list is
contained in the AS-path attribute. BGP prevents routing loops by rejecting any routing update that contains
the local autonomous system number because this indicates that the route has already traveled through that
autonomous system and a loop would therefore be created. The BGP path-vector routing algorithm is a
combination of the distance-vector routing algorithm and the AS-path loop detection.
BGP selects a single path, by default, as the best path to a destination host or network. The best path selection
algorithm analyzes path attributes to determine which route is installed as the best path in the BGP routing
table. Each path carries well-known mandatory, well-known discretionary, and optional transitive attributes
that are used in BGP best path analysis. Cisco software provides the ability to influence BGP path selection
by altering some of these attributes using the command-line interface (CLI.) BGP path selection can also be
influenced through standard BGP policy configuration. For more details about using BGP to influence path
selection and configuring BGP policies to filter traffic, see the “BGP 4 Prefix Filter and Inbound Route Maps”
module and the “BGP Prefix-Based Outbound Route Filtering” module.
BGP uses the best-path selection algorithm to find a set of equally good routes. These routes are the potential
multipaths. In Cisco IOS Release 12.2(33)SRD and later releases, when there are more equally good multipaths
available than the maximum permitted number, the oldest paths are selected as multipaths.
BGP can be used to help manage complex internal networks by interfacing with Interior Gateway Protocols
(IGPs). Internal BGP can help with issues such as scaling the existing IGPs to match the traffic demands while
maintaining network efficiency.

Note

BGP requires more configuration than other routing protocols and the effects of any configuration changes
must be fully understood. Incorrect configuration can create routing loops and negatively impact normal
network operation.

BGP Autonomous Systems
An autonomous system is a network controlled by a single technical administration entity. BGP autonomous
systems are used to divide global external networks into individual routing domains where local routing
policies are applied. This organization simplifies routing domain administration and simplifies consistent
policy configuration. Consistent policy configuration is important to allow BGP to efficiently process routes
to destination networks.
Each routing domain can support multiple routing protocols. However, each routing protocol is administered
separately. Other routing protocols can dynamically exchange routing information with BGP through
redistribution. Separate BGP autonomous systems dynamically exchange routing information through eBGP
peering sessions. BGP peers within the same autonomous system exchange routing information through iBGP
peering sessions.
The figure below illustrates two routers in separate autonomous systems that can be connected using BGP.
Router A and Router B are ISP routers in separate routing domains that use public autonomous system numbers.

IP Routing: BGP Configuration Guide
5


Cisco BGP Overview
BGP Autonomous System Number Formats

These routers carry traffic across the Internet. Router A and Router B are connected through eBGP peering
sessions.
Figure 1: BGP Topology with Two Autonomous Systems

Each public autonomous system that directly connects to the Internet is assigned a unique number that identifies
both the BGP routing process and the autonomous system.

BGP Autonomous System Number Formats
Prior to January 2009, BGP autonomous system numbers that were allocated to companies were two-octet
numbers in the range from 1 to 65535 as described in RFC 4271, A Border Gateway Protocol 4 (BGP-4).
Due to increased demand for autonomous system numbers, the Internet Assigned Number Authority (IANA)
will start in January 2009 to allocate four-octet autonomous system numbers in the range from 65536 to
4294967295. RFC 5396, Textual Representation of Autonomous System (AS) Numbers, documents three
methods of representing autonomous system numbers. Cisco has implemented the following two methods:
• Asplain--Decimal value notation where both 2-byte and 4-byte autonomous system numbers are
represented by their decimal value. For example, 65526 is a 2-byte autonomous system number and
234567 is a 4-byte autonomous system number.
• Asdot--Autonomous system dot notation where 2-byte autonomous system numbers are represented by
their decimal value and 4-byte autonomous system numbers are represented by a dot notation. For
example, 65526 is a 2-byte autonomous system number and 1.169031 is a 4-byte autonomous system
number (this is dot notation for the 234567 decimal number).
For details about the third method of representing autonomous system numbers, see RFC 5396.
Asdot Only Autonomous System Number Formatting
In Cisco IOS Release 12.0(32)S12, 12.4(24)T, and later releases, the 4-octet (4-byte) autonomous system
numbers are entered and displayed only in asdot notation, for example, 1.10 or 45000.64000. When using
regular expressions to match 4-byte autonomous system numbers the asdot format includes a period which
is a special character in regular expressions. A backslash must be entered before the period for example, 1\.14,
to ensure the regular expression match does not fail. The table below shows the format in which 2-byte and

IP Routing: BGP Configuration Guide
6


Cisco BGP Overview
BGP Autonomous System Number Formats

4-byte autonomous system numbers are configured, matched in regular expressions, and displayed in show
command output in Cisco IOS images where only asdot formatting is available.
Table 1: Asdot Only 4-Byte Autonomous System Number Format

Format Configuration Format

Show Command Output and Regular Expression Match
Format

asdot

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535

2-byte: 1 to 65535 4-byte: 1.0 to
65535.65535

Asplain as Default Autonomous System Number Formatting
In Cisco IOS Release 12.0(32)SY8, 12.0(33)S3, 12.2(33)SRE, 12.2(33)XNE, 12.2(33)SXI1, and later releases,
the Cisco implementation of 4-byte autonomous system numbers uses asplain as the default display format
for autonomous system numbers, but you can configure 4-byte autonomous system numbers in both the asplain
and asdot format. In addition, the default format for matching 4-byte autonomous system numbers in regular
expressions is asplain, so you must ensure that any regular expressions to match 4-byte autonomous system
numbers are written in the asplain format. If you want to change the default show command output to display
4-byte autonomous system numbers in the asdot format, use the bgp asnotation dot command under router
configuration mode. When the asdot format is enabled as the default, any regular expressions to match 4-byte
autonomous system numbers must be written using the asdot format, or the regular expression match will fail.
The tables below show that although you can configure 4-byte autonomous system numbers in either asplain
or asdot format, only one format is used to display show command output and control 4-byte autonomous
system number matching for regular expressions, and the default is asplain format. To display 4-byte
autonomous system numbers in show command output and to control matching for regular expressions in the
asdot format, you must configure the bgp asnotation dot command. After enabling the bgp asnotation dot
command, a hard reset must be initiated for all BGP sessions by entering the clear ip bgp * command.

Note

If you are upgrading to an image that supports 4-byte autonomous system numbers, you can still use 2-byte
autonomous system numbers. The show command output and regular expression match are not changed and
remain in asplain (decimal value) format for 2-byte autonomous system numbers regardless of the format
configured for 4-byte autonomous system numbers.
Table 2: Default Asplain 4-Byte Autonomous System Number Format

Format Configuration Format

Show Command Output and Regular Expression
Match Format

asplain 2-byte: 1 to 65535 4-byte: 65536 to
4294967295

2-byte: 1 to 65535 4-byte: 65536 to 4294967295

asdot

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535 2-byte: 1 to 65535 4-byte: 65536 to 4294967295

IP Routing: BGP Configuration Guide
7


Cisco BGP Overview
Classless Interdomain Routing

Table 3: Asdot 4-Byte Autonomous System Number Format

Format Configuration Format

Show Command Output and Regular Expression
Match Format

asplain 2-byte: 1 to 65535 4-byte: 65536 to
4294967295

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535

asdot

2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535 2-byte: 1 to 65535 4-byte: 1.0 to 65535.65535

Reserved and Private Autonomous System Numbers
In Cisco IOS Release 12.0(32)S12, 12.0(32)SY8, 12.0(33)S3, 12.2(33)SRE, 12.2(33)XNE, 12.2(33)SXI1,
12.4(24)T, and later releases, the Cisco implementation of BGP supports RFC 4893. RFC 4893 was developed
to allow BGP to support a gradual transition from 2-byte autonomous system numbers to 4-byte autonomous
system numbers. A new reserved (private) autonomous system number, 23456, was created by RFC 4893 and
this number cannot be configured as an autonomous system number in the Cisco IOS CLI.
RFC 5398, Autonomous System (AS) Number Reservation for Documentation Use, describes new reserved
autonomous system numbers for documentation purposes. Use of the reserved numbers allow configuration
examples to be accurately documented and avoids conflict with production networks if these configurations
are literally copied. The reserved numbers are documented in the IANA autonomous system number registry.
Reserved 2-byte autonomous system numbers are in the contiguous block, 64496 to 64511 and reserved 4-byte
autonomous system numbers are from 65536 to 65551 inclusive.
Private 2-byte autonomous system numbers are still valid in the range from 64512 to 65534 with 65535 being
reserved for special use. Private autonomous system numbers can be used for internal routing domains but
must be translated for traffic that is routed out to the Internet. BGP should not be configured to advertise
private autonomous system numbers to external networks. Cisco IOS software does not remove private
autonomous system numbers from routing updates by default. We recommend that ISPs filter private
autonomous system numbers.

Note

Autonomous system number assignment for public and private networks is governed by the IANA. For
information about autonomous-system numbers, including reserved number assignment, or to apply to register
an autonomous system number, see the following URL: http://www.iana.org/.

Classless Interdomain Routing
BGP version 4 supports classless interdomain routing (CIDR). CIDR eliminates classful network boundaries,
providing more efficient usage of the IPv4 address space. CIDR provides a method to reduce the size of
routing tables by configuring aggregate routes (or supernets). CIDR processes a prefix as an IP address and
bit mask (bits are processed from left to right) to define each network. A prefix can represent a network,
subnetwork, supernet, or single host route.
For example, using classful IP addressing, the IP address 192.168.2.1 is defined as a single host in the Class
C network 192.168.2.0. Using CIDR, the IP address can be shown as 192.168.2.1/16, which defines a network
(or supernet) of 192.168.0.0.
CIDR is enabled by default for all routing protocols in Cisco software. Enabling CIDR affects how packets
are forwarded, but it does not change the operation of BGP.

IP Routing: BGP Configuration Guide
8


Cisco BGP Overview
Multiprotocol BGP

Multiprotocol BGP
Cisco software supports multiprotocol BGP extensions as defined in RFC 2858, Multiprotocol Extensions for
BGP-4. The extensions introduced in this RFC allow BGP to carry routing information for multiple
network-layer protocols, including CLNS, IPv4, IPv6, and VPNv4. These extensions are backward-compatible
to enable routers that do not support multiprotocol extensions to communicate with those routers that do
support multiprotocol extensions. Multiprotocol BGP carries routing information for multiple network-layer
protocols and IP multicast routes. BGP carries different sets of routes depending on the protocol. For example,
BGP can carry one set of routes for IPv4 unicast routing, one set of routes for IPv4 multicast routing, and one
set of routes for MPLS VPNv4 routes.

Note

A multiprotocol BGP network is backward-compatible with a BGP network, but BGP peers that do not support
multiprotocol extensions cannot forward routing information, such as address family identifier information,
that the multiprotocol extensions carry.

Benefits of Using Multiprotocol BGP Versus BGP
In complex networks with multiple network layer protocols, multiprotocol BGP must be used. In less complex
networks we recommend using multiprotocol BGP because it offers the following benefits:
• All of the BGP commands and routing policy capabilities of BGP can be applied to multiprotocol BGP.
• A network can carry routing information for multiple network layer protocol address families (for example,
IP Version 4 or VPN Version 4) as specified in RFC 1700, Assigned Numbers.
• A network can support incongruent unicast and multicast topologies.
• A multiprotocol BGP network is backward compatible because the routers that support the multiprotocol
extensions can interoperate with routers that do not support the extensions.
In summary, multiprotocol BGP support for multiple network layer protocol address families provides a
flexible and scalable infrastructure that allows you to define independent policy and peering configurations
on a per-address family basis.

Multiprotocol BGP Extensions for IP Multicast
The routes associated with multicast routing are used by the Protocol Independent Multicast (PIM) feature to
build data distribution trees. Multiprotocol BGP is useful when you want a link that is dedicated to multicast
traffic, perhaps to limit which resources are used for which traffic. For example, you want all multicast traffic
exchanged at one network access point (NAP). Multiprotocol BGP allows you to have a unicast routing
topology different from a multicast routing topology, which allows you more control over your network and
resources.
In BGP, the only way to perform interdomain multicast routing is to use the BGP infrastructure that is in place
for unicast routing. If the routers are not multicast-capable, or if there are differing policies about where
multicast traffic should flow, multicast routing cannot be supported without multiprotocol BGP.
A multicast routing protocol, such as PIM, uses both the multicast and unicast BGP database to source the
route, perform Reverse Path Forwarding (RPF) lookups for multicast-capable sources, and build a multicast
distribution tree (MDT). The multicast table is the primary source for the router, but if the route is not found

IP Routing: BGP Configuration Guide
9


Cisco BGP Overview
Multiprotocol BGP Extensions for IP Multicast

in the multicast table, the unicast table is searched. Although multicast can be performed with unicast BGP,
multicast BGP routes allow an alternative topology to be used for RPF.
It is possible to configure BGP peers that exchange both unicast and multicast Network Layer Reachability
Information (NLRI) where multiprotocol BGP routes can be redistributed into BGP. Multiprotocol extensions,
however, will be ignored by any peers that do not support multiprotocol BGP. When PIM builds a multicast
distribution tree through a unicast BGP network (because the route through the unicast network is the most
attractive), the RPF check may fail, preventing the MDT from being built. If the unicast network runs
multiprotocol BGP, peering can be configured using the appropriate multicast address family. The multicast
address family configuration enables multiprotocol BGP to carry the multicast information and the RPF lookup
will succeed.
The figure below illustrates a simple example of unicast and multicast topologies that are incongruent; these
topologies cannot exchange information without implementing multiprotocol BGP. Autonomous systems
100, 200, and 300 are each connected to two NAPs that are FDDI rings. One is used for unicast peering (and
therefore the exchanging of unicast traffic). The Multicast Friendly Interconnect (MFI) ring is used for multicast
peering (and therefore the exchanging of multicast traffic). Each router is unicast- and multicast-capable.
Figure 2: Incongruent Unicast and Multicast Routes

The figure below is a topology of unicast-only routers and multicast-only routers. The two routers on the left
are unicast-only routers (that is, they do not support or are not configured to perform multicast routing). The
two routers on the right are multicast-only routers. Routers A and B support both unicast and multicast routing.
The unicast-only and multicast-only routers are connected to a single NAP.
In the figure below, only unicast traffic can travel from Router A to the unicast routers to Router B and back.
Multicast traffic could not flow on that path, because multicast routing is not configured on the unicast routers
and therefore the BGP routing table does not contain any multicast routes. On the multicast routers, multicast
routes are enabled and BGP builds a separate routing table to hold the multicast routes. Multicast traffic uses
the path from Router A to the multicast routers to Router B and back.
The figure below illustrates a multiprotocol BGP environment with a separate unicast route and multicast
route from Router A to Router B. Multiprotocol BGP allows these routes to be noncongruent. Both of the
autonomous systems must be configured for internal multiprotocol BGP (labeled “IMBGP” in the figure).

IP Routing: BGP Configuration Guide
10


Cisco BGP Overview
NLRI Configuration CLI

Figure 3: Multicast BGP Environment

For more information about IP multicast, see the “Configuring IP Multicast” configuration library.

NLRI Configuration CLI
BGP was designed to carry only unicast IPv4 routing information. BGP configuration used the Network NLRI
format CLI in Cisco software. The NLRI format offers only limited support for multicast routing information
and does not support multiple network layer protocols. We do not recommend using NLRI format CLI for
BGP configuration.
Using the BGP hybrid CLI feature, you can configure commands in the address family VPNv4 format and
save these command configurations without modifying an existing NLRI formatted configuration. If you want
to use other address family configurations such as IPv4 unicast or multicast, then you must upgrade the
configuration using the bgp upgrade-cli command.
For more details about using BGP hybrid CLI commands, see the "Configuring a Basic BGP Network” module.
See the “Multiprotocol BGP” and “Cisco BGP Address Family Model” sections for more information about
address family configuration format and the limitations of the NLRI CLI format.

Cisco BGP Address Family Model
The Cisco BGP address family identifier (AFI) model was introduced with multiprotocol BGP and is designed
to be modular and scalable, and to support multiple AFI and subsequent address family identifier (SAFI)
configurations. Networks are increasing in complexity and many companies are now using BGP to connect

IP Routing: BGP Configuration Guide
11


Cisco BGP Overview
Cisco BGP Address Family Model

to many autonomous systems, as shown in the network topology in the figure below. Each of the separate
autonomous systems shown in the figure below may be running several routing protocols such as Multiprotocol
Label Switching (MPLS) and IPv6 and require both unicast and multicast routes to be transported via BGP.
Figure 4: BGP Network Topology for Multiple Address Families

The Cisco BGP AFI model introduced new command-line interface (CLI) commands supported by a new
internal structure. Multiprotocol BGP carries routing information for multiple network layer protocols and IP
multicast routes. This routing information is carried in the AFI model as appended BGP attributes (multiprotocol
extensions). Each address family maintains a separate BGP database, which allows you to configure BGP
policy on per-address family basis. SAFI configurations are subsets of the parent AFI. SAFIs can be used to
refine BGP policy configurations.
The AFI model was created because of scalability limitations of the NLRI format. A router that is configured
in NLRI format has IPv4 unicast but limited multicast capabilities. Networks that are configured in the NLRI
format have the following limitations:
• No support for AFI and SAFI configuration information. Many new BGP (and other protocols such as
MPLS) features are supported only in AFI and SAFI configuration modes and cannot be configured in
NLRI configuration modes.
• No support for IPv6. A router that is configured in the NLRI format cannot establish peering with an
IPv6 neighbor.
• Limited support for multicast interdomain routing and incongruent multicast and unicast topologies. In
the NLRI format, not all configuration options are available and there is no support for VPNv4. The
NLRI format configurations can be more complex than configurations that support the AFI model. If the
routers in the infrastructure do not have multicast capabilities, or if policies differ as to where multicast
traffic is configured to flow, multicast routing cannot be supported.
The AFI model in multiprotocol BGP supports multiple AFIs and SAFIs, all NLRI-based commands and
policy configurations, and is backward compatible with routers that support only the NLRI format. A router
that is configured using the AFI model has the following features:

IP Routing: BGP Configuration Guide
12


Cisco BGP Overview
Cisco BGP Address Family Model

• AFI and SAFI information and configurations are supported. A router that is configured using the AFI
model can carry routing information for multiple network layer protocol address families (for example,
IPv4 and IPv6).
• AFI configuration is similar in all address families, making the CLI syntax easier to use than the NLRI
format syntax.
• All BGP routing policy capabilities and commands are supported.
• Congruent unicast and multicast topologies that have different policies (BGP filtering configurations)
are supported, as are incongruent multicast and unicast topologies.
• CLNS is supported.
• Interoperation between routers that support only the NLRI format (AFI-based networks are backward
compatible) is supported. This includes both IPv4 unicast and multicast NLRI peers.
• Virtual Private Networks (VPNs) and VPN routing and forwarding (VRF) instances are supported.
Unicast IPv4 for VRFs can be configured from a specific address family IPv4 VRF; this configuration
update is integrated into the BGP VPNv4 database.
Within a specific address family configuration mode, the question mark (?) online help function can be used
to display supported commands. The BGP commands supported in address family configuration mode configure
the same functionality as the BGP commands supported in router configuration mode; however, the BGP
commands in router configuration mode configure functionality only for the IPv4 unicast address prefix. To
configure BGP commands and functionality for other address family prefixes (for example, the IPv4 multicast
or IPv6 unicast address prefixes), you must enter address family configuration mode for those address prefixes.
The BGP address family model consists of four address families in Cisco IOS software; IPv4, IPv6, CLNS,
and VPNv4. In Cisco IOS Release 12.2(33)SRB, and later releases, support for the L2VPN address family
was introduced, and within the L2VPN address family the VPLS SAFI is supported. Within the IPv4 and
IPv6 address families, SAFIs such as Multicast Distribution Tree (MDT), tunnel, and VRF exist. The table
below shows the list of SAFIs supported by Cisco IOS software. To ensure compatibility between networks
running all types of AFI and SAFI configuration, we recommend configuring BGP on Cisco IOS devices
using the multiprotocol BGP address family model.
Table 4: SAFIs Supported by Cisco IOS Software

SAFI Field Value Description

Reference

1

NLRI used for unicast forwarding.

RFC 2858

2

NLRI used for multicast forwarding.

RFC 2858

3

NLRI used for both unicast and multicast
forwarding.

RFC 2858

4

NLRI with MPLS labels.

RFC 3107

64

Tunnel SAFI.

draft-nalawade-kapoor-tunnel- safi
-01.txt

65

Virtual Private LAN Service (VPLS).

—

66

BGP MDT SAFI.

draft-nalawade-idr-mdt-safi-00.txt

IP Routing: BGP Configuration Guide
13


Cisco BGP Overview
IPv4 Address Family

SAFI Field Value Description

Reference

128

RFC-ietf-l3vpn-rfc2547bis-03.txt

MPLS-labeled VPN address.

IPv4 Address Family
The IPv4 address family is used to identify routing sessions for protocols such as BGP that use standard IP
version 4 address prefixes. Unicast or multicast address prefixes can be specified within the IPv4 address
family. Routing information for address family IPv4 unicast is advertised by default when a BGP peer is
configured unless the advertisement of unicast IPv4 information is explicitly turned off.
VRF instances can also be associated with IPv4 AFI configuration mode commands.
In Cisco IOS Release 12.0(28)S, the tunnel SAFI was introduced to support multipoint tunneling IPv4 routing
sessions. The tunnel SAFI is used to advertise the tunnel endpoints and the SAFI specific attributes that contain
the tunnel type and tunnel capabilities. Redistribution of tunnel endpoints into the BGP IPv4 tunnel SAFI
table occurs automatically when the tunnel address family is configured. However, peers need to be activated
under the tunnel address family before the sessions can exchange tunnel information.
In Cisco IOS Release 12.0(29)S, the multicast distribution tree (MDT) SAFI was introduced to support
multicast VPN architectures. The MDT SAFI is a transitive multicast capable connector attribute that is defined
as an IPv4 address family in BGP. The MDT address family session operates as a SAFI under the IPv4
multicast address family, and is configured on provider edge (PE) routers to establish VPN peering sessions
with customer edge (CE) routers that support inter-AS multicast VPN peering sessions.

IPv6 Address Family
The IPv6 address family is used to identify routing sessions for protocols such as BGP that use standard IPv6
address prefixes. Unicast or multicast address prefixes can be specified within the IPv6 address family.

Note

Routing information for address family IPv4 unicast is advertised by default when you configure a BGP peer
unless you explicitly turn off the advertisement of unicast IPv4 information.

CLNS Address Family
The CLNS address family is used to identify routing sessions for protocols such as BGP that use standard
network service access point (NSAP) address prefixes. Unicast address prefixes are the default when NSAP
address prefixes are configured.
CLNS routes are used in networks where CLNS addresses are configured. This is typically a telecommunications
Data Communications Network (DCN). Peering is established using IP addresses, but update messages contain
CLNS routes.
For more details about configuring BGP support for CLNS, which provides the ability to scale CLNS networks,
see the “Configuring Multiprotocol BGP (MP-BGP) support for CLNS” module.

IP Routing: BGP Configuration Guide
14


Cisco BGP Overview
VPNv4 Address Family

VPNv4 Address Family
The VPNv4 multicast address family is used to identify routing sessions for protocols such as BGP that use
standard VPN Version 4 address prefixes. Unicast address prefixes are the default when VPNv4 address
prefixes are configured. VPNv4 routes are the same as IPv4 routes, but VPNv4 routes have a route descriptor
(RD) prepended that allows replication of prefixes. It is possible to associate every different RD with a different
VPN. Each VPN needs its own set of prefixes.
Companies use an IP VPN as the foundation for deploying or administering value-added services including
applications and data hosting network commerce, and telephony services to business customers.
In private LANs, IP-based intranets have fundamentally changed the way companies conduct their business.
Companies are moving their business applications to their intranets to extend over a WAN. Companies are
also addressing the needs of their customers, suppliers, and partners by using extranets (an intranet that
encompasses multiple businesses). With extranets, companies reduce business process costs by facilitating
supply-chain automation, electronic data interchange (EDI), and other forms of network commerce. To take
advantage of this business opportunity, service providers must have an IP VPN infrastructure that delivers
private network services to businesses over a public infrastructure.
VPNs, when used with MPLS, allow several sites to transparently interconnect through a service provider's
network. One service provider network can support several different IP VPNs. Each of these appears to its
users as a private network, separate from all other networks. Within a VPN, each site can send IP packets to
any other site in the same VPN. Each VPN is associated with one or more VPN VRFs. VPNv4 routes are a
superset of routes from all VRFs, and route injection is done per VRF under the specific VRF address family.
The router maintains a separate routing and Cisco Express Forwarding (CEF) table for each VRF. This prevents
information from being sent outside the VPN and allows the same subnet to be used in several VPNs without
causing duplicate IP address problems. The router using BGP distributes the VPN routing information using
the BGP extended communities.
The VPN address space is isolated from the global address space by design. BGP distributes reachability
information for VPN-IPv4 prefixes for each VPN using the VPNv4 multiprotocol extensions to ensure that
the routes for a given VPN are learned only by other members of that VPN, enabling members of the VPN
to communicate with each other.
RFC 3107 specifies how to add label information to multiprotocol BGP address families using a SAFI. The
Cisco IOS implementation of MPLS uses RFC 3107 to provide support for sending IPv4 routes with a label.
VPNv4 routes implicitly have a label associated with each route.

L2VPN Address Family
L2VPN is defined as a secure network that operates inside an unsecured network by using an encryption
technology such as IP security (IPsec) or Generic Routing Encapsulation (GRE). The L2VPN address family
is configured under BGP routing configuration mode, and within the L2VPN address family the VPLS
subsequent address family identifier (SAFI) is supported.
BGP support for the L2VPN address family introduces a BGP-based autodiscovery mechanism to distribute
L2VPN endpoint provisioning information. BGP uses a separate L2VPN routing information base (RIB) to
store endpoint provisioning information, which is updated each time any Layer 2 VFI is configured. Prefix
and path information is stored in the L2VPN database, allowing BGP to make best-path decisions. When BGP
distributes the endpoint provisioning information in an update message to all its BGP neighbors, the endpoint
information is used to set up a pseudowire mesh to support L2VPN-based services.
The BGP autodiscovery mechanism facilitates the setting up of L2VPN services, which are an integral part
of the Cisco IOS Virtual Private LAN Service (VPLS) feature. VPLS enables flexibility in deploying services

IP Routing: BGP Configuration Guide
15


Cisco BGP Overview
BGP CLI Removal Considerations

by connecting geographically dispersed sites as a large LAN over high-speed Ethernet in a robust and scalable
IP MPLS network. For more details about VPLS, see the “VPLS Autodiscovery: BGP Based” feature.
Under L2VPN address family the following BGP command-line interface (CLI) commands are supported:
• bgp scan-time
• bgp nexthop
• neighbor activate
• neighbor advertisement-interval
• neighbor allowas-in
• neighbor capability
• neighbor inherit
• neighbor peer-group
• neighbor maximum-prefix
• neighbor next-hop-self
• neighbor next-hop-unchanged
• neighbor remove-private-as
• neighbor route-map
• neighbor route-reflector-client
• neighbor send-community
• neighbor soft-reconfiguration
• neighbor soo
• neighbor weight

Note

For route reflectors using L2VPNs, the neighbor next-hop-self and neighbor next-hop-unchanged
commands are not supported.
For route maps used within BGP, all commands related to prefix processing, tag processing, and automated
tag processing are ignored when used under L2VPN address family configuration. All other route map
commands are supported.
BGP multipaths and confederations are not supported under the L2VPN address family.
For details on configuring BGP under the L2VPN address family, see the “BGP Support for the L2VPN
Address Family” module.

BGP CLI Removal Considerations
BGP CLI configuration can become quite complex even in smaller BGP networks. If you need to remove any
CLI configuration, you must consider all the implications of removing the CLI. Analyze the current running

IP Routing: BGP Configuration Guide
16


Cisco BGP Overview
BGP CLI Removal Considerations

configuration to determine the current BGP neighbor relationships, any address family considerations, and
even other routing protocols that are configured. Many BGP CLI commands affect other parts of the CLI
configuration. For example, in the following configuration, a route map is used to match a BGP autonomous
system number and then set the matched routes with another autonomous system number for EIGRP:
route-map bgp-to-eigrp permit 10
match tag 50000
set tag 65000

BGP neighbors in three different autonomous systems are configured and activated:
router bgp 45000
bgp log-neighbor-changes
address-family ipv4
neighbor 172.16.1.2 remote-as 45000
neighbor 192.168.1.2 remote-as 40000
neighbor 192.168.3.2 remote-as 50000
neighbor 172.16.1.2 activate
neighbor 192.168.1.2 activate
neighbor 192.168.3.2 activate
network 172.17.1.0 mask 255.255.255.0
exit-address-family

An EIGRP routing process is then configured and BGP routes are redistributed into EIGRP with a route map
filtering the routes:
router eigrp 100
redistribute bgp 45000 metric 10000 100 255 1 1500 route-map bgp-to-eigrp
no auto-summary
exit

If you later decide to remove the route map, you will use the no form of the route-map command. Almost
every configuration command has a no form, and the no form generally disables a function. However, in this
configuration example, if you disable only the route map, the route redistribution will continue, but without
the filtering or matching from the route map. Redistribution without the route map may cause unexpected
behavior in your network. When you remove an access list or route map, you must also review the commands
that referenced that access list or route map to consider whether the command will give you the behavior you
intended.
The following configuration will remove both the route map and the redistribution:
configure terminal
no route-map bgp-to-eigrp
router eigrp 100
no redistribute bgp 45000
end

For details on configuring the removal of BGP CLI configuration, see the “Configuring a Basic BGP Network”
module.

IP Routing: BGP Configuration Guide
17


Cisco BGP Overview
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

Standards
Standard

Title

MDT SAFI MDT SAFI
MIBs
MIB

MIBs Link

CISCO-BGP4-MIB To locate and download MIBs for selected platforms, Cisco software releases, and
feature sets, use Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs
RFCs
RFC

Title

RFC 1700 Assigned Numbers
RFC 2858 Multiprotocol Extensions for BGP-4
RFC 3107 Carrying Label Information in BGP-4
RFC 4271 A Border Gateway Protocol 4 (BGP-4)
RFC 4893 BGP Support for Four-Octet AS Number Space
RFC 5396 Textual Representation of Autonomous System (AS) Numbers
RFC 5398 Autonomous System (AS) Number Reservation for Documentation Use

IP Routing: BGP Configuration Guide
18


Cisco BGP Overview
Feature Information for Cisco BGP Overview

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

Feature Information for Cisco BGP Overview
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 5: Feature Information for Cisco BGP Overview

Feature Name

Releases

Feature Information

Multiprotocol
BGP

Cisco IOS XE
3.1.0SG

Cisco IOS software supports multiprotocol BGP extensions as defined
in RFC 2858, Multiprotocol Extensions for BGP-4 . The extensions
introduced in this RFC allow BGP to carry routing information for
multiple network layer protocols including CLNS, IPv4, IPv6, and
VPNv4. These extensions are backward compatible to enable routers
that do not support multiprotocol extensions to communicate with those
routers that do support multiprotocol extensions. Multiprotocol BGP
carries routing information for multiple network layer protocols and IP
multicast routes.

IP Routing: BGP Configuration Guide
19


Cisco BGP Overview
Feature Information for Cisco BGP Overview

IP Routing: BGP Configuration Guide
20
