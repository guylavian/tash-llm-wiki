---
title: "BGP—Selective Route Download"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-selective-route-download
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 72 BGP—Selective Route Download The BGP—Selective Route Download feature allows a network administrator to selectively download some or none of the BGP routes into the Routing Information Base (RIB). The primary application for this feature is to suppress the unnecessary downloading of certain BGP routes to the RIB or Forwarding Information Base (FIB) on a dedicated route reflector, whic"
---

# BGP—Selective Route Download

CHAPTER

72

BGP—Selective Route Download
The BGP—Selective Route Download feature allows a network administrator to selectively download some
or none of the BGP routes into the Routing Information Base (RIB). The primary application for this feature
is to suppress the unnecessary downloading of certain BGP routes to the RIB or Forwarding Information Base
(FIB) on a dedicated route reflector, which propagates BGP updates without carrying transit traffic. The feature
thereby helps to maximize resources available and to improve routing scalability and convergence on the
dedicated route reflector.
• Finding Feature Information, on page 1039
• Information About BGP—Selective Route Download, on page 1039
• How to Selectively Download BGP Routes, on page 1040
• Configuration Examples for BGP—Selective Route Download, on page 1044
• Additional References for Selective Route Download, on page 1045
• Feature Information for Selective Route Download, on page 1046

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP—Selective Route Download
Dedicated Route Reflector Does Not Need All Routes
The role of a dedicated route reflector (RR) is to propagate BGP updates without participating in the actual
forwarding of transit traffic. That means the RR does not need to have all BGP routes downloaded into its
RIB or FIB. It is beneficial for the RR to preserve its resources by not processing and storing those routes.
By default, BGP routes are downloaded to the RIB. To save resources on a dedicated route reflector, such
downloading can be reduced or prevented by configuring a table map. A table map is so named because it
controls what is put into the BGP routing table.

IP Routing: BGP Configuration Guide
1039


BGP—Selective Route Download
Benefits of Selective Route Download

A table map references a route map, in this context to control the downloading of routes. A table map can be
used in other features, such as the BGP Policy Accounting Output Interface Accounting feature.
It is important to understand the use of the filter keyword in the table-map command.
• When the table-map command is used without the filter keyword, the route map referenced in the
table-map command is used to set certain properties (such as the traffic index) of the routes for installation
into the RIB. The route is always downloaded, regardless of whether it is permitted or denied by the
route map.
• When the table-map command is used with the filter keyword, the route map referenced is also used to
control whether a BGP route is to be downloaded to the RIB (hence the filter). A BGP route is not
downloaded to the RIB if it is denied by the route map.
Note that the Selective Route Download feature is not applicable to Multiprotocol Label Switching (MPLS)
Layer 3 VPN because the route download is already automatically suppressed on a route reflector.

Benefits of Selective Route Download
The BGP—Selective Route Download feature allows a network administrator to selectively download some
or none of the BGP routes into the Routing Information Base (RIB). The primary application for this feature
is to suppress the unnecessary downloading of certain BGP routes to the RIB or Forwarding Information Base
(FIB) on a dedicated route reflector, which propagates BGP updates without carrying transit traffic. The feature
thereby helps to maximize resources available and to improve routing scalability and convergence on the
dedicated route reflector.

How to Selectively Download BGP Routes
Suppressing the Downloading of All BGP Routes on a Dedicated RR
Perform this task on a dedicated route reflector (RR) to prevent all BGP routes from being downloaded to the
RIB, and thereby save resources.
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

enable
configure terminal
route-map route-map-name deny [sequence-number]
exit
router bgp as-number
address-family ipv4 unicast
table-map route-map-name filter
end
clear ip bgp ipv4 unicast table-map

IP Routing: BGP Configuration Guide
1040


BGP—Selective Route Download
Suppressing the Downloading of All BGP Routes on a Dedicated RR

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

route-map route-map-name deny [sequence-number]
Example:
Router(config)# route-map bgp-to-rib deny 10

Step 4

exit
Example:

Enters route map configuration mode to configure a route
map.
• In this example, the route map named bgp-to-rib denies
all routes.
Exits route-map configuration mode and enters global
configuration mode.

Router(config-route-map)# exit

Step 5

router bgp as-number
Example:

Enters router configuration mode and creates a BGP routing
process.

Router(config)# router bgp 100

Step 6

address-family ipv4 unicast
Example:

Enters address family configuration mode to configure BGP
peers to accept address-family-specific configurations.

Router(config-router)# address-family ipv4 unicast

Step 7

table-map route-map-name filter
Example:
Router(config-router-af)# table-map bgp-to-rib
filter

Step 8

end
Example:

Specifies a route map that filters what goes into the BGP
routing table (the Routing Information Base [RIB]).
• The routes that are permitted by the route map are
downloaded into the RIB.
• The routes that are denied by the route map are filtered
from (not downloaded into) the RIB.
Exits address family configuration mode and enters
privileged EXEC mode.

Router(config-router-af)# end

IP Routing: BGP Configuration Guide
1041


BGP—Selective Route Download
Selectively Downloading BGP Routes on a Dedicated RR

Step 9

Command or Action

Purpose

clear ip bgp ipv4 unicast table-map

Reloads the BGP RIB after the table map or the route map
is configured or changed in order to put the changes into
effect.

Example:
Router# clear ip bgp ipv4 unicast table-map

Selectively Downloading BGP Routes on a Dedicated RR
Perform this task on a dedicated route reflector (RR) to selectively download BGP routes to the RIB. When
the externally connected routes are carried in BGP, it is necessary to download these routes to the RIB for
next hop resolution on the RR. One scalable approach to accomplish the selective route download is to use a
BGP community to identify the externally connected routes. That is, attach a designated BGP community
during the redistribution of the externally connected routes on the ASBRs, and then on the RR, filter the route
download based on the BGP community. This task illustrates the configuration of the RR using a route map
that matches on a community list to control which routes are downloaded.
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
11.

enable
configure terminal
ip community-list standard-list-number permit AA:NN
route-map route-map-name permit [sequence-number]
match community standard-list-number
exit
router bgp as-number
address-family ipv4 unicast
table-map route-map-name filter
end
clear ip bgp ipv4 unicast table-map

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
Example:
Router# configure terminal

IP Routing: BGP Configuration Guide
1042

Enters global configuration mode.


BGP—Selective Route Download
Selectively Downloading BGP Routes on a Dedicated RR

Command or Action
Step 3

Purpose

ip community-list standard-list-number permit AA:NN Creates a standard community list and specifies an
autonomous system and network number allowed in the
Example:
community list.
Router(config)# ip community-list 100 permit
65510:100

Step 4

route-map route-map-name permit [sequence-number]
Example:
Router(config)# route-map bgp-to-rib permit 10

Step 5

match community standard-list-number
Example:

Enters route-map configuration mode to configure a route
map.
• The route map named bgp-to-rib permits routes that
match the community list identified in the next step.
Matches on routes that are permitted by community list
100.

Router(config-route-map)# match community 100

Step 6

exit
Example:

Exits route-map configuration mode and enters global
configuration mode.

Router(config-route-map)# exit

Step 7

router bgp as-number
Example:

Enters router configuration mode and creates a BGP
routing process.

Router(config)# router bgp 65510

Step 8

address-family ipv4 unicast
Example:

Enters address family configuration mode to configure
BGP peers to accept address family-specific configurations.

Router(config-router)# address-family ipv4 unicast

Step 9

table-map route-map-name filter
Example:

Specifies a route map that filters what goes into the BGP
routing table (the Routing Information Base [RIB]).

Router(config-router-af)# table-map bgp-to-rib
filter

Step 10

end
Example:

Exits address family configuration mode and enters
privileged EXEC mode.

Router(config-router-af)# end

Step 11

clear ip bgp ipv4 unicast table-map
Example:

Reloads the BGP RIB after the table map or the route map
is configured or changed in order to put the changes into
effect.

Router# clear ip bgp ipv4 unicast table-map

IP Routing: BGP Configuration Guide
1043


BGP—Selective Route Download
Configuration Examples for BGP—Selective Route Download

Configuration Examples for BGP—Selective Route Download
Examples: Selective Route Download
The role of a dedicated route reflector (RR) is to propagate BGP updates without participating in the
actual forwarding of transit traffic. In some cases, the dedicated RR may need only selected routes
downloaded; in some cases it may not need any routes downloaded.
It is likely that the dedicated RR would have the overload bit set if the IS-IS routing protocol is being
used, or an OSPF stub router would be configured if OSPF is being used.
Example: Next Hop is Loopback Address—Filter All Routes From Being Downloaded
In this example, the ASBRs are configured with the next-hop-self command for iBGP sessions. (That
configuration is not shown). The next hops of the BGP routes advertised to iBGP sessions are the loopback
addresses carried in the IGP (either OSPF or IS-IS). There is no need to download any BGP routes to the RIB.
The following configuration on the dedicated RR suppresses the downloading of all BGP routes because the
table map command includes the filter keyword, and the route map that the table map references denies all
routes.
route-map bgp-to-rib deny 10
!
router bgp 65000
address-family ipv6 unicast
table-map bgp-to-rib filter

Example: Redistribution of Connected Routes in IGP—Filter All Routes From Being Downloaded
In this example, the next hops of the BGP routes are resolved on the externally connected routes, which are
carried in an IGP, such as OSPF or IS-IS, via a prefix-list-based selective redistribution of the connected
routes. The routes are received from iBGP.
Although the scenario is different from the preceding example, the configuration is the same. The following
configuration on the dedicated RR suppresses the downloading of all BGP routes because the table map
command includes the filter keyword, and the route map that the table map references denies all routes.
route-map bgp-to-rib deny 10
!
router bgp 65000
address-family ipv6 unicast
table-map bgp-to-rib filter

Example: Redistribution of Connected Routes in BGP—Selectively Filter Routes From Being Downloaded
When the externally connected routes are carried in BGP, it is necessary to download these routes to the RIB,
where the nexthop resolution on the RR can be calculated. One scalable way to achieve the selective route
download is to use a BGP community on the ASBR to identify these externally connected routes. That is, on
the border routers, attach a designated BGP community during the redistribution of the externally connected

IP Routing: BGP Configuration Guide
1044


BGP—Selective Route Download
Additional References for Selective Route Download

routes, and then on the RR, filter the route download based on the BGP community. The following shows the
configuration on the ASBR and the configuration on the RR.
ASBR Configuration
router bgp 65510
address-family ipv4 unicast
redistribute connected route-map connected-to-bgp
!
route-map connected-to-bgp permit 10
match ip address prefix-list extend-connected
set community 65510:100
!
ip prefix-list extend-connected permit 192.168.1.1/30

RR Configuration
ip community-list 100 permit 65510:100
!
route-map bgp-to-rib permit 10
match community 100
!
router bgp 65510
address-family ipv4 unicast
table-map bgp-to-rib filter

Additional References for Selective Route Download
Related Documents
Related Topic

Document Title

Cisco IOS
Commands

Cisco IOS Master Commands List, All Releases

BGP Commands

Cisco IOS IP Routing: BGP Command Reference

Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.

http://www.cisco.com/support

To receive security and technical information about your products, you can
subscribe to various services, such as the Product Alert Tool (accessed from
Field Notices), the Cisco Technical Services Newsletter, and Really Simple
Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com user
ID and password.

IP Routing: BGP Configuration Guide
1045


BGP—Selective Route Download
Feature Information for Selective Route Download

Feature Information for Selective Route Download
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 92: Feature Information for Selective Route Download

Feature Name

Releases

Feature Information

Selective Route Download

Cisco IOS XE Release 2.3S

The BGP—Selective Route
Download feature allows a network
administrator to selectively
download some or none of the BGP
routes into the Routing Information
Base (RIB). The primary
application for this feature is to
suppress the unnecessary
downloading of certain BGP routes
to the RIB or Forwarding
Information Base (FIB) on a
dedicated route reflector, which
propagates BGP updates without
carrying transit traffic. The feature
thereby helps to maximize
resources available and to improve
routing scalability and convergence
on the dedicated route reflector.
The following command was
modified:
• table-map

IP Routing: BGP Configuration Guide
1046
