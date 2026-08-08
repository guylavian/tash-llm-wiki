---
title: "BGP Cost Community"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-cost-community
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 37 BGP Cost Community The BGP Cost Community feature introduces the cost extended community attribute. The cost community is a non-transitive extended community attribute that is passed to internal BGP (iBGP) and confederation peers but not to external BGP (eBGP) peers. The cost community feature allows you to customize the local route preference and influence the best path selection pro"
---

# BGP Cost Community

CHAPTER

37

BGP Cost Community
The BGP Cost Community feature introduces the cost extended community attribute. The cost community is
a non-transitive extended community attribute that is passed to internal BGP (iBGP) and confederation peers
but not to external BGP (eBGP) peers. The cost community feature allows you to customize the local route
preference and influence the best path selection process by assigning cost values to specific routes.
In Cisco IOS Release 12.0(27)S, 12.3(8)T, 12.2(25)S, and later releases, support was introduced for mixed
EIGRP MPLS VPN network topologies that contain VPN and backdoor links.
• Finding Feature Information, on page 611
• Prerequisites for the BGP Cost Community Feature, on page 611
• Restrictions for the BGP Cost Community Feature, on page 612
• Information About the BGP Cost Community Feature, on page 612
• How to Configure the BGP Cost Community Feature, on page 615
• Configuration Examples for the BGP Cost Community Feature, on page 617
• Additional References, on page 619
• Feature Information for BGP Cost Community, on page 620

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for the BGP Cost Community Feature
This document assumes that BGP is configured in your network and that peering has been established.

IP Routing: BGP Configuration Guide
611


BGP Cost Community
Restrictions for the BGP Cost Community Feature

Restrictions for the BGP Cost Community Feature
• The BGP Cost Community feature can be configured only within an autonomous system or confederation.
The cost community is a non-transitive extended community that is passed to iBGP and confederation
peers only and is not passed to eBGP peers.
• The BGP Cost Community feature must be supported on all routers in the autonomous system or
confederation before cost community filtering is configured. The cost community should be applied
consistently throughout the local autonomous system or confederation to avoid potential routing loops.
• Multiple cost community set clauses may be configured with the set extcommunity cost command in a
single route map block or sequence. However, each set clause must be configured with a different ID
value (0-255) for each point of insertion (POI). The ID value determines preference when all other
attributes are equal. The lowest ID value is preferred.

Information About the BGP Cost Community Feature
BGP Cost Community Overview
The cost community is a nontransitive, extended community attribute that is passed to iBGP and confederation
peers, but not to eBGP peers. The configuration of the BGP Cost Community feature allows you to customize
the BGP best path selection process for a local autonomous system or confederation.
The cost community attribute is applied to internal routes by configuring the set extcommunity cost command
in a route map. The cost community set clause is configured with a cost community ID number (0-255) and
cost number (0-4294967295). The cost community ID number determines the preference for the path selection
process. The path with the lowest cost community ID number is preferred.
Paths that are not specifically configured with the cost community attribute are assigned a default cost number
value of 2147483647 (The midpoint between 0 and 4294967295) and evaluated by the best path selection
process accordingly. In the case where two paths have been configured with the same cost community ID
number, the path selection process will then prefer the path with the lowest cost number. The cost extended
community attribute is propagated to iBGP peers when extended community exchange is enabled with the
neighbor send-community command.
The following commands can be used to apply a route map that is configured with the cost community set
clause:
• aggregate-address
• neighbor default-originate route-map {in | out}
• neighbor route-map
• network route-map
• redistribute route-map

IP Routing: BGP Configuration Guide
612


BGP Cost Community
How the BGP Cost Community Influences the Best Path Selection Process

How the BGP Cost Community Influences the Best Path Selection Process
The cost community attribute influences the BGP best path selection process at the point of insertion (POI).
By default, the POI follows the IGP metric comparison. When BGP receives multiple paths to the same
destination, it uses the best path selection process to determine which path is the best path. BGP automatically
makes the decision and installs the best path into the routing table. The POI allows you to assign a preference
to o a specific path when multiple equal cost paths are available. If the POI is not valid for local best path
selection, the cost community attribute is silently ignored.
Multiple paths can be configured with the cost community attribute for the same POI. The path with the lowest
cost community ID is considered first. In other words, all of the cost community paths for a specific POI are
considered, starting with the one with the lowest cost community. Paths that do not contain the cost community
(for the POI and community ID being evaluated) are assigned the default community cost value (2147483647).
If the cost community values are equal, then cost community comparison proceeds to the next lowest community
ID for this POI.

Note

Paths that are not configured with the cost community attribute are considered by the best path selection
process to have the default cost-value (half of the maximum value [4294967295] or 2147483647).
Applying the cost community attribute at the POI allows you to assign a value to a path originated or learned
by a peer in any part of the local autonomous system or confederation. The cost community can be used as a
“tie breaker” during the best path selection process. Multiple instances of the cost community can be configured
for separate equal cost paths within the same autonomous system or confederation. For example, a lower cost
community value can be applied to a specific exit path in a network with multiple equal cost exits points, and
the specific exit path will be preferred by the BGP best path selection process. See the scenario described in
the “Influencing Route Preference in a Multi-Exit IGP Network” section.

Cost Community Support for Aggregate Routes and Multipaths
Aggregate routes and multipaths are supported by the BGP Cost Community feature. The cost community
attribute can be applied to either type of route. The cost community attribute is passed to the aggregate or
multipath route from component routes that carry the cost community attribute. Only unique IDs are passed,
and only the highest cost of any individual component route will be applied to the aggregate on a per-ID basis.
If multiple component routes contain the same ID, the highest configured cost is applied to the route. For
example, the following two component routes are configured with the cost community attribute via an inbound
route map:
• 10.0.0.1 (POI=IGP, ID=1, Cost=100)
• 192.168.0.1 (POI=IGP, ID=1, Cost=200)
If these component routes are aggregated or configured as a multipath, the cost value 200 (POI=IGP, ID=1,
Cost=200) will be advertised because it is the highest cost.
If one or more component routes does not carry the cost community attribute or if the component routes are
configured with different IDs, then the default value (2147483647) will be advertised for the aggregate or
multipath route. For example, the following three component routes are configured with the cost community
attribute via an inbound route map. However, the component routes are configured with two different IDs.
• 10.0.0.1 (POI=IGP, ID=1, Cost=100)

IP Routing: BGP Configuration Guide
613


BGP Cost Community
Influencing Route Preference in a Multi-Exit IGP Network

• 172.16.0.1 (POI=IGP, ID=2, Cost=100)
• 192.168.0.1 (POI=IGP, ID=1, Cost=200)
The single advertised path will include the aggregated cost communities as follows:
• {POI=IGP, ID=1, Cost=2147483647} {POI=IGP, ID=2, Cost=2147483647}

Influencing Route Preference in a Multi-Exit IGP Network
The figure below shows an Interior Gateway Protocol (IGP) network with two autonomous system boundary
routers (ASBRs) on the edge. Each ASBR has an equal cost path to network 10.8/16.
Figure 61: Multi-Exit Point IGP Network

Both paths are considered to be equal by BGP. If multipath loadsharing is configured, both paths will be
installed to the routing table and will be used to load balance traffic. If multipath load balancing is not
configured, then BGP will select the path that was learned first as the best path and install this path to the
routing table. This behavior may not be desirable under some conditions. For example, the path is learned
from ISP1 PE2 first, but the link between ISP1 PE2 and ASBR1 is a low-speed link.
The configuration of the cost community attribute can be used to influence the BGP best path selection process
by applying a lower cost community value to the path learned by ASBR2. For example, the following
configuration is applied to ASBR2.
route-map ISP2_PE1 permit 10
set extcommunity cost 1 1
match ip address 13
!
ip access-list 13 permit 10.8.0.0 0.0.255.255

The above route map applies a cost community number value of 1 to the 10.8.0.0 route. By default, the path
learned from ASBR1 will be assigned a cost community value of 2147483647. Because the path learned from
ASBR2 has lower cost community value, this path will be preferred.

BGP Cost Community Support for EIGRP MPLS VPN PE-CE with Backdoor Links
Before EIGRP Site of Origin (SoO) BGP Cost Community support was introduced, BGP preferred locally
sourced routes over routes learned from BGP peers. Back door links in an EIGRP MPLS VPN topology will

IP Routing: BGP Configuration Guide
614


BGP Cost Community
How to Configure the BGP Cost Community Feature

be preferred by BGP if the back door link is learned first. (A back door link, or a route, is a connection that
is configured outside of the VPN between a remote and main site. For example, a WAN leased line that
connects a remote site to the corporate network).
The "pre-bestpath" point of insertion (POI) was introduced in the BGP Cost Community feature to support
mixed EIGRP VPN network topologies that contain VPN and backdoor links. This POI is applied automatically
to EIGRP routes that are redistributed into BGP. The "pre-best path" POI carries the EIGRP route type and
metric. This POI influences the best path calculation process by influencing BGP to consider this POI before
any other comparison step. No configuration is required. This feature is enabled automatically for EIGRP
VPN sites when Cisco IOS Release 12.0(27)S is installed to a PE, CE, or back door router.
For information about configuring EIGRP MPLS VPNs, refer to the MPLS VPN Support for EIGRP Between
Provider Edge and Customer Edge document in Cisco IOS Release 12.0(27)S.
For more information about the EIGRP MPLS VPN PE-CE Site of Origin (SoO) feature, refer to the EIGRP
MPLS VPN PE-CE Site of Origin (SoO) feature documentation in Cisco IOS Release 12.0(27)S.

How to Configure the BGP Cost Community Feature
Configuring the BGP Cost Community
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

enable
configure terminal
router bgp autonomous-system-number
neighbor ip-address remote-as autonomous-system-number
address-family ipv4 [mdt | multicast | tunnel | unicast [vrf vrf-name] | vrf vrf-name] | ipv6 [multicast
| unicast] | vpnv4 [unicast]
neighbor ip-address route-map map-name {in | out}
exit
route-map map-name {permit | deny} [sequence-number]
set extcommunity cost [igp] community-id cost-value
end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged EXEC
mode.

Example:

• Enter your password if prompted.
Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

IP Routing: BGP Configuration Guide
615


BGP Cost Community
Configuring the BGP Cost Community

Step 3

Command or Action

Purpose

router bgp autonomous-system-number

Enters router configuration mode to create or configure a
BGP routing process.

Example:
Device(config)# router bgp 50000

Step 4

neighbor ip-address remote-as
autonomous-system-number

Establishes peering with the specified neighbor or
peer-group.

Example:
Device(config-router)# neighbor 10.0.0.1 remote-as
101

Step 5

address-family ipv4 [mdt | multicast | tunnel | unicast Places the router in address family configuration mode.
[vrf vrf-name] | vrf vrf-name] | ipv6 [multicast | unicast]
| vpnv4 [unicast]
Example:
Device(config-router)# address-family ipv4

Step 6

neighbor ip-address route-map map-name {in | out} Applies an incoming or outgoing route map for the
specified neighbor or peer-group.
Example:
Device(config-router)# neighbor 10.0.0.1 route-map
MAP-NAME in

Step 7

exit
Example:

Exits router configuration mode and enters global
configuration mode.

Device(config-router)# exit

Step 8

route-map map-name {permit | deny}
[sequence-number]

Enters route map configuration mode to create or configure
a route map.

Example:
Device(config)# route-map MAP-NAME permit 10

Step 9

set extcommunity cost [igp] community-id cost-value
Example:
Device(config-route-map)# set extcommunity cost
1 100

Creates a set clause to apply the cost community attribute.
• Multiple cost community set clauses can be
configured in each route map block or sequence. Each
cost community set clause must have a different ID
(0-255). The cost community set clause with the
lowest cost-value is preferred by the best path
selection process when all other attributes are equal.
• Paths that are not configured with the cost community
attribute will be assigned the default cost-value, which
is half of the maximum value (4294967295) or
2147483647.

IP Routing: BGP Configuration Guide
616


BGP Cost Community
Verifying the Configuration of the BGP Cost Community

Step 10

Command or Action

Purpose

end

Exits route map configuration mode and enters privileged
EXEC mode.

Example:
Device(config-route-map)# end

Verifying the Configuration of the BGP Cost Community
BGP cost community configuration can be verified locally or for a specific neighbor. To verify the local
configuration cost community, use the show route-map or show running-config command.
To verify that a specific neighbor carries the cost community, use the show ip bgp ip-address command. The
output from these commands displays the POI (IGP is the default POI), the configured ID, and configured
cost. For large cost community values, the output from these commands will also show, with + and - values,
the difference between the configured cost and the default cost. See “Example: BGP Cost Community
Verification” section for sample output.

Troubleshooting Tips
The bgp bestpath cost-community ignore command can be used to disable the evaluation of the cost
community attribute to help isolate problems and troubleshoot issues that relate to BGP best path selection.
The debug ip bgp updates command can be used to print BGP update messages. The cost community extended
community attribute will be displayed in the output of this command when received from a neighbor. A
message will also be displayed if a non-transitive extended community if received from an external peer.

Configuration Examples for the BGP Cost Community Feature
Example: BGP Cost Community Configuration
The following example applies the cost community ID of 1 and cost community value of 100 to routes that
are permitted by the route map. This configuration will cause the best path selection process to prefer this
route over other equal-cost paths that were not permitted by this route map sequence.
Device(config)# router bgp 50000
Device(config-router)# neighbor 10.0.0.1 remote-as 50000
Device(config-router)# neighbor 10.0.0.1 update-source Loopback 0
Device(config-router)# address-family ipv4
Device(config-router-af)# neighbor 10.0.0.1 activate
Device(config-router-af)# neighbor 10.0.0.1 route-map COST1 in
Device(config-router-af)# neighbor 10.0.0.1 send-community both
Router(config-router-af)# exit
Device(config)# route-map COST1 permit 10
Device(config-route-map)# match ip-address 1
Device(config-route-map)# set extcommunity cost 1 100

IP Routing: BGP Configuration Guide
617


BGP Cost Community
Example: BGP Cost Community Verification

Example: BGP Cost Community Verification
BGP cost community configuration can be verified locally or for a specific neighbor. To verify the local
configuration cost community, use the show route-map or show running-config command. To verify that
a specific neighbor carries the cost community, use the show ip bgp ip-address command.
The output of the show route-map command will display locally configured route-maps, match, set, continue
clauses, and the status and configuration of the cost community attribute. The following sample output is
similar to the output that will be displayed:
Device# show route-map
route-map COST1, permit, sequence 10
Match clauses:
as-path (as-path filter): 1
Set clauses:
extended community Cost:igp:1:100
Policy routing matches: 0 packets, 0 bytes
route-map COST1, permit, sequence 20
Match clauses:
ip next-hop (access-lists): 2
Set clauses:
extended community Cost:igp:2:200
Policy routing matches: 0 packets, 0 bytes
route-map COST1, permit, sequence 30
Match clauses:
interface FastEthernet0/0
extcommunity (extcommunity-list filter):300
Set clauses:
extended community Cost:igp:3:300
Policy routing matches: 0 packets, 0 bytes

The following sample output shows locally configured routes with large cost community values:
Device# show route-map
route-map set-cost, permit, sequence 10
Match clauses:
Set clauses:
extended community RT:1:1 RT:2:2 RT:3:3 RT:4:4 RT:5:5 RT:6:6 RT:7:7
RT:100:100 RT:200:200 RT:300:300 RT:400:400 RT:500:500 RT:600:600
RT:700:700 additive
extended community Cost:igp:1:4294967295 (default+2147483648)
Cost:igp:2:200 Cost:igp:3:300 Cost:igp:4:400
Cost:igp:5:2147483648 (default+1) Cost:igp:6:2147484648 (default+1001)
Cost:igp:7:2147284648 (default-198999)
Policy routing matches: 0 packets, 0 bytes

The output of the show running config command will display match, set, and continue clauses that are
configured within a route-map. The following sample output is filtered to show only the relevant part of the
running configuration:
Device# show running-config | begin route-map
route-map COST1 permit 20
match ip next-hop 2
set extcommunity cost igp 2 200
!
route-map COST1 permit 30
match interface FastEthernet0/0

IP Routing: BGP Configuration Guide
618


BGP Cost Community
Additional References

match extcommunity 300
set extcommunity cost igp 3 300
.
.
.

The output of the show ip bgp ip-address command can be used to verify if a specific neighbor carries a path
that is configured with the cost community attribute. The cost community attribute information is displayed
in the “Extended Community” field. The POI, the cost community ID, and the cost community number value
are displayed. The following sample output shows that neighbor 172.16.1.2 carries a cost community with an
ID of 1 and a cost of 100:
Device# show ip bgp 10.0.0.0
BGP routing table entry for 10.0.0.0/8, version 2
Paths: (1 available, best #1)
Not advertised to any peer
2 2 2
172.16.1.2 from 172.16.1.2 (172.16.1.2)
Origin IGP, metric 0, localpref 100, valid, external, best
Extended Community: Cost:igp:1:100

If the specified neighbor is configured with the default cost community number value or if the default value
is assigned automatically for cost community evaluation, “default” with + and - values will be displayed after
the cost community number value in the output.

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

EIGRP MPLS VPN PE-CE Site of Origin
(SoO) feature

“EIGRP MPLS VPN PE-CE Site of Origin (SoO)” module in
the IP Routing: EIGRP Configuration Guide

Standards
Standards

Title

No new or modified standards are supported by this feature, and support for existing standards has not —
been modified by this feature.

IP Routing: BGP Configuration Guide
619


BGP Cost Community
Feature Information for BGP Cost Community

MIBs
MIB MIBs Link
— To locate and download MIBs for selected platforms, Cisco software releases, and feature sets, use
Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs
RFCs
RFCs

Title

draft-retana-bgp-custom-decision-00.txt BGP Custom Decision Process
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

Feature Information for BGP Cost Community
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 53: Feature Information for BGP Cost Community

Feature Name

Releases

Feature Information

BGP Cost
Community

12.0(24)S
12.3(2)T
12.2(18)S
12.2(27)SBC
15.0(1)S

The BGP Cost Community feature introduces the cost extended
community attribute. The cost community is a non-transitive extended
community attribute that is passed to internal BGP (iBGP) and
confederation peers but not to external BGP (eBGP) peers. The cost
community feature allows you to customize the local route preference
and influence the best path selection process by assigning cost values
to specific routes.
The following commands were introduced or modified: bgp bestpath
cost-community ignore, debug ip bgp updates, and set
extcommunity cost.

IP Routing: BGP Configuration Guide
620


BGP Cost Community
Feature Information for BGP Cost Community

Feature Name

Releases

BGP Cost
12.0(27)S
Community
12.3(8)T
Support for EIGRP 12.2(25)S
MPLS VPN PE-CE
with Backdoor
Links

Feature Information
Back door links in an EIGRP MPLS VPN topology will be preferred
by BGP if the back door link is learned first. The "pre-bestpath"
point of insertion (POI) was introduced in the BGP Cost Community
feature to support mixed EIGRP VPN network topologies that contain
VPN and backdoor links. This POI is applied automatically to EIGRP
routes that are redistributed into BGP and the POI influences the
best path calculation process by influencing BGP to consider this
POI before any other comparison step. No configuration is required.
This feature is enabled automatically for EIGRP VPN sites when
Cisco IOS Release 12.0(27)S, 12.3(8)T, 12,2(25)S or later releases,
is installed to a PE, CE, or back door router.
No commands were introduced or modified.

IP Routing: BGP Configuration Guide
621


BGP Cost Community
Feature Information for BGP Cost Community

IP Routing: BGP Configuration Guide
622
