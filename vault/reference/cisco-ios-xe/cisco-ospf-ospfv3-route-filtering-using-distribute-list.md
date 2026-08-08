---
title: "OSPFv3 Route Filtering Using Distribute-List"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-route-filtering-using-distribute-list
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 23 OSPFv3 Route Filtering Using Distribute-List The OSPFv3 route filtering using distribute-list feature allows users to filter the incoming routes that are programmed in routing table, and the outgoing routes that are advertised. • Finding Feature Information, page 235 • Prerequisites for OSPFv3 Route Filtering Using Distribute-List, page 235 • Information About OSPFv3 Route Filtering U"
---

# OSPFv3 Route Filtering Using Distribute-List

CHAPTER

23

OSPFv3 Route Filtering Using Distribute-List
The OSPFv3 route filtering using distribute-list feature allows users to filter the incoming routes that are
programmed in routing table, and the outgoing routes that are advertised.
• Finding Feature Information, page 235
• Prerequisites for OSPFv3 Route Filtering Using Distribute-List, page 235
• Information About OSPFv3 Route Filtering Using Distribute-List, page 235
• How to Configure OSPFv3 Route Filtering Using Distribute-List, page 236
• Additional References, page 241
• Feature Information for OSPFv3 Route Filtering Using Distribute-List, page 242

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv3 Route Filtering Using Distribute-List
It is presumed that you have OSPF configured in your network.

Information About OSPFv3 Route Filtering Using Distribute-List
Users can define a route map to prevent OSPF routes from being added to the routing table. This filtering
happens at the moment when OSPF is installing the route in the routing table. This feature has no effect on
link-state advertisement (LSA) flooding.

IP Routing: OSPF Configuration Guide
235


OSPFv3 Route Filtering Using Distribute-List
How to Configure OSPFv3 Route Filtering Using Distribute-List

This feature can be useful during redistribution if the user tags prefixes when they get redistributed on
Autonomous System Boundary Routers (ASBRs) and later uses the tag to filter the prefixes from being
installed in the routing table on other routers. The below mentioned options are available only for distribute-list
filtering using route-map.
Filtering Based on Route Tag
Users can assign tags to external routes when they are redistributed to OSPF. Then the user can deny or permit
those routes in the OSPF domain by identifying that tag in the route-map and distribute-list in or
distribute-list out commands.
Filtering Based on Route Type
In OSPF, the external routes could be Type 1 or Type 2. Users can create route maps to match either Type 1
or Type 2 and then use the distribute-list in command to filter certain prefixes. Also, route maps can identify
internal routes (interarea and intra-area) and then those routes can be filtered.
Filtering Based on Route Source
When a match is done on the route source, the route source represents the OSPF Router ID of the LSA
originator of the LSA in which the prefix is advertised.
Filtering Based on Interface
When a match is done on the interface, the interface represents the outgoing interface for the route that OSPF
is trying to install in the routing table.
Filtering Based on Next Hop
When a match is done on the next hop, the next hop represents the next hop for the route that OSPF is trying
to install in the routing table.

Note

The distribute-list in command can be configured to prevent routes from being installed in the global
Routing Information Base (RIB). Prior to the implementation of OSPF local RIB (for feature information
on OSPF local RIB, see OSPFv2 Local RIB), OSPF would attempt to install a less preferred route (e.g.
an inter-area route when the intra-area path is filtered). With OSPF local RIB, only the best route is
considered (because this is the only route the local RIB maintains). There is no concept of a "second-best"
OSPF route. For more information on the routing algorithm used by Cisco OSPF routers, please refer to
RFC 2328.

How to Configure OSPFv3 Route Filtering Using Distribute-List
Configuring OSPFv3 (IPv4 address-family)
Command Mode: Address family mode (address-family ipv4 unicast). Following is the syntax:
[no] distribute-list [<access-list #> | <access-list name>] |
{prefix <name1> gateway <name2>} |
{prefix <name1>} | {gateway <name2>} |

IP Routing: OSPF Configuration Guide
236


OSPFv3 Route Filtering Using Distribute-List
Configuring OSPFv3 (IPv4 address-family)

{route-map name} in [<interface>]
[no] distribute-list [<access-list #> | <access-list name>] | [prefix <name>] out
[{ <routing-process> | <interface> }]

Interface: Incoming (used with Inbound filtering) or outgoing (used with outbound filtering) interface.
Routing-process: Source protocol for the route to be filtered.

Configuring Inbound Filtering: Route Map
SUMMARY STEPS
1. Configure OSPFv3.
2. Configure address-family ipv4 unicast.
3. Configure distribute list with the appropriate route-map.

DETAILED STEPS
Step 1

Configure OSPFv3.
Device(config)#router ospfv3 1

Step 2

Configure address-family ipv4 unicast.
Device(config-router)#address-family ipv4 unicast

Step 3

Configure distribute list with the appropriate route-map.
Device(config-router-af)#distribute-list route-map rmap-name in

The following match options in a route-map are supported:
• match interface
• match ip address
• match ip next-hop
• match ip route-source
• match metric
• match route-type
• match tag

IP Routing: OSPF Configuration Guide
237


OSPFv3 Route Filtering Using Distribute-List
Configuring OSPFv3 (IPv4 address-family)

Configuring Inbound Filtering: Prefix-List/Access-List
SUMMARY STEPS
1. Configure OSPFv3.
2. Configure address-family ipv4 unicast.
3. Defines prefix list to be used and the direction for the filter.

DETAILED STEPS
Step 1

Configure OSPFv3.
Device(config)#router ospfv3 1

Step 2

Configure address-family ipv4 unicast.
Device(config-router)#address-family ipv4 unicast

Step 3

Defines prefix list to be used and the direction for the filter.
Device(config-router-af)#distribute-list prefix pfxname in

Note

The following are the available optional arguments. You can use these arguments to filter based on incoming
interface. Choose any interface that is available on your device.

Ethernet
Loopback
Null
Port-channel
Serial
Tunnel
Vlan

IEEE 802.3
Loopback interface
Null interface
Ethernet Channel of interfaces
Serial
Tunnel interface
Catalyst Vlans

Configuring Outbound Filtering
SUMMARY STEPS
1. Configure OSPFv3.
2. Configure address-family ipv4 unicast.
3. Configure distribute list with the appropriate route-map.

DETAILED STEPS
Step 1

Configure OSPFv3.
Device(config)#router ospfv3 1

Step 2

Configure address-family ipv4 unicast.
Device(config-router)#address-family ipv4 unicast

IP Routing: OSPF Configuration Guide
238


OSPFv3 Route Filtering Using Distribute-List
Configuring Route Filtering Using Distribute-List for OSPFv3 (IPv6 address-family)

Step 3

Configure distribute list with the appropriate route-map.
Device(config-router-af)#distribute-list prefix pfxlist-name out

Note

The following are the available optional arguments. You can use these options to filter based on the source
protocol of the route.

bgp
Border Gateway Protocol (BGP)
connected Connected
eigrp
Enhanced Interior Gateway Routing Protocol (EIGRP)
isis
ISO IS-IS
lisp
Locator ID Separation Protocol (LISP)
ospf
Open Shortest Path First (OSPF)
ospfv3
OSPFv3
rip
Routing Information Protocol (RIP)
static
Static routes

Configuring Route Filtering Using Distribute-List for OSPFv3 (IPv6
address-family)
Mode: Address-family mode (address-family ipv6 unicast). Prefix-list and route-map are supported as filtering
options. Following is the syntax:
[no] distribute-list prefix-list <name> in [<interface>]
[no] distribute-list route-map <name> in
[no] distribute-list prefix-list <name> out <routing-process>

Interface: Incoming (used with Inbound filtering) or outgoing (used with outbound filtering) interface.
Routing-process: Source protocol for the route to be filtered.

Configuring Inbound Filtering: Route Map
SUMMARY STEPS
1. Configure OSPFv3.
2. Configure address-family ipv6unicast.
3. Define route map.

DETAILED STEPS
Step 1

Configure OSPFv3.
Device(config)#router ospfv3 1

Step 2

Configure address-family ipv6unicast.
Device(config-router)#address-family ipv6 unicast

Step 3

Define route map.
Device(config-router-af)#distribute-list route-map rmap-name in

The following match options in a route-map are supported:

IP Routing: OSPF Configuration Guide
239


OSPFv3 Route Filtering Using Distribute-List
Configuring Route Filtering Using Distribute-List for OSPFv3 (IPv6 address-family)

• match interface
• match ip address
• match ip next-hop
• match metric
• match route-type
• match tag

Configuring Inbound Filtering: Prefix-List
SUMMARY STEPS
1.
2.
3.
4.

Configure OSPFv3.
Configure address-family ipv6 unicast.
Define prefix list name.
Define filter incoming routing updates.

DETAILED STEPS
Step 1

Configure OSPFv3.
Device(config)#router ospfv3 1

Step 2

Configure address-family ipv6 unicast.
Device(config-router)#address-family ipv6 unicast

Step 3

Define prefix list name.
Device(config-router-af)#distribute-list prefix pfxlist-name

Step 4

Define filter incoming routing updates.
Device(config-router-af)#distribute-list prefix pfxname in

Note

The following are the available optional arguments. You can use these arguments to filter based on incoming
interface. Choose any interface that is available on your device.

Ethernet
Loopback
Null
Port-channel
Serial
Tunnel
Vlan

IEEE 802.3
Loopback interface
Null interface
Ethernet Channel of interfaces
Serial
Tunnel interface
Catalyst Vlans

IP Routing: OSPF Configuration Guide
240


OSPFv3 Route Filtering Using Distribute-List
Additional References

Configuring Outbound Filtering
SUMMARY STEPS
1. Configure OSPFv3.
2. Configure address-family ipv6 unicast.
3. Define prefix list name.

DETAILED STEPS
Step 1

Configure OSPFv3.
Device(config)#router ospfv3 1

Step 2

Configure address-family ipv6 unicast.
Device(config-router)#address-family ipv6 unicast

Step 3

Define prefix list name.
Device(config-router-af)#distribute-list prefix-list pfxlist-name out

Note

These are the available options for the routing process. The <routing-process> argument is mandatory for IPv6
outbound route filtering.

bgp
Border Gateway Protocol (BGP)
connected Connected Routes
eigrp
Enhanced Interior Gateway Routing Protocol (EIGRP)
isis
ISO IS-IS
lisp
Locator ID Separation Protocol (LISP)
ospf
Open Shortest Path First (OSPFv3)
rip
IPv6 Routing Information Protocol (RIPv6)
static
Static Routes

Additional References
Related Documents
Related Topic

Document Title

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

IP Routing: OSPF Configuration Guide
241


OSPFv3 Route Filtering Using Distribute-List
Feature Information for OSPFv3 Route Filtering Using Distribute-List

MIBs
MIBs

MIBs Link

None

To locate and download MIBs for selected platforms,
Cisco software releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFCs

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

Feature Information for OSPFv3 Route Filtering Using
Distribute-List
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
242


OSPFv3 Route Filtering Using Distribute-List
Feature Information for OSPFv3 Route Filtering Using Distribute-List

Table 26: Feature Information for OSPFv3 Route Filtering Using Distribute-List

Feature Name

Releases

Feature Information

OSPFv3 Route Filtering Using
Distribute-List

Cisco IOS XE Denali 16.3.1

The route-map support for OSPFv3
route-filtering using distribute-list
is supported.

IP Routing: OSPF Configuration Guide
243


OSPFv3 Route Filtering Using Distribute-List
Feature Information for OSPFv3 Route Filtering Using Distribute-List

IP Routing: OSPF Configuration Guide
244
