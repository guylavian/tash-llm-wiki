---
title: "BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-rt-and-vpn-distinguisher-attribute-rewrite-wildcard
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 67 BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard The BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard feature introduces the ability to set a range of route target (RT) community attributes or VPN distinguisher community attributes when mapping them. A network administrator might want to map one or more RTs at an egress ASBR to different RTs at an ingress ASBR. The VPN D"
---

# BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard

CHAPTER

67

BGP-RT and VPN Distinguisher Attribute Rewrite
Wildcard
The BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard feature introduces the ability to set a range
of route target (RT) community attributes or VPN distinguisher community attributes when mapping them.
A network administrator might want to map one or more RTs at an egress ASBR to different RTs at an ingress
ASBR. The VPN Distinguisher Attribute feature allows an administrator to map RTs to a VPN distinguisher
that is carried through an eBGP and then mapped to RTs at an ingress ASBR. The mapping is achieved by
configuring a route map that sets an RT range or VPN distinguisher range of extended community attributes.
Specifying a range rather than individual RTs saves time and simplifies the configuration. Furthermore, a
VPN distinguisher range allows more than one VPN distinguisher attribute per route-map clause, thereby
removing the restriction that applied prior to this feature.
• Finding Feature Information, on page 995
• Restrictions for BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard, on page 996
• Information About BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard, on page 996
• How to Map RTs to RTs Using a Range, on page 996
• Configuration Examples for BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard, on page 1002
• Additional References for BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard, on page 1004
• Feature Information for BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard, on page 1005

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
995


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Restrictions for BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard

RestrictionsforBGP-RTandVPNDistinguisherAttributeRewrite
Wildcard
• A range (specified in the set extcommunity rt command or the set extcommunity vpn-distinguisher
command) can include a maximum of 450 extended communities.
• The VPN distinguisher range is not relayed to an iBGP peer.

Information About BGP—RT and VPN Distinguisher Attribute
Rewrite Wildcard
Benefits of RT and VPN Distinguisher Attribute Mapping Range
A network administrator might want to rewrite (or map) one or more route targets (RTs) at an egress ASBR
to different RTs at an ingress ASBR. One use case would be to keep the RTs at the egress ASBR private from
the ingress ASBR.
The rewrite is achieved by using inbound route maps, matching prefixes to route-map clauses that match
inbound RTs, and mapping those RTs to different RTs recognized by the neighbor AS. Such a rewrite
configuration could be complex on inbound route maps, with potentially hundreds of RTs that would need to
be specified individually (configuring set extcommunity rt value1 value2 value3 ...). If the RTs being attached
to the prefixes are consecutive, the configuration can be simplified by specifying a range of RTs. Thus, the
benefits of the RT mapping range are saving time and simplifying the configuration.
Likewise, the mapping of RTs to a VPN distinguisher attribute (and vice versa) can also be simplified by
specifying a range of RTs or VPN distinguishers. The BGP—VPN Distinguisher Attribute feature allows a
network administrator to keep source RTs private from an ASBR in a destination AS. An RT at an egress
ASBR is mapped to a VPN distinguisher, the VPN distinguisher is carried through the eBGP, and then it is
mapped to an RT at the ingress ASBR.
The RT and VPN Distinguisher Attribute Mapping Range feature introduces the ability to specify a range of
either route targets (RTs) or VPN distinguishers when mapping them.
Another benefit applies to setting a VPN distinguisher. Prior to this feature, only one set extcommunity
vpn-distinguisher value was allowed per route-map clause. With the introduction of the mapping range, a
range of VPN distinguishers can be set on a route.

How to Map RTs to RTs Using a Range
Replacing an RT with a Range of RTs
Perform this task on an egress ASBR to replace a route target (RT) with an RT range. Remember to replace
the range of RTs with an RT on the ingress ASBR; that task is described in the “Replacing a Range of RTs
with an RT” section.

IP Routing: BGP Configuration Guide
996


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Replacing an RT with a Range of RTs

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
12.
13.
14.
15.
16.
17.

enable
configure terminal
ip extcommunity-list expanded-list {permit | deny} rt value
exit
route-map map-tag {permit | deny} [sequence-number]
match extcommunity extended-community-list-name
set extcomm-list extcommunity-name delete
set extcommunity rt range start-value end-value
exit
route-map map-tag {permit | deny} [sequence-number]
exit
router bgp as-number
neighbor ip-address remote-as autonomous-system-number
address-family vpnv4
neighbor ip-address activate
neighbor ip-address route-map map-tag out
exit-address-family

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

ip extcommunity-list expanded-list {permit | deny} rt
value
Example:
Device(config)# ip extcommunity-list 22 permit rt
101:100

Step 4

exit
Example:

Configures an IP extended community list to configure
Virtual Private Network (VPN) route filtering, such that
routes with the specified RT are in the extended community
list.
• This example permits routes having RT 101:100 into
the extended community list 22.
Exits the configuration mode and enters the next higher
configuration mode.

Device(config-extcomm-list)# exit

Step 5

route-map map-tag {permit | deny} [sequence-number] Configures a route map that permits or denies the routes
allowed by the subsequent match command.
Example:

IP Routing: BGP Configuration Guide
997


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Replacing an RT with a Range of RTs

Command or Action
Device(config)# route-map rt-mapping permit 10

Step 6

match extcommunity extended-community-list-name
Example:
Device(config-route-map)# match extcommunity 22

Step 7

set extcomm-list extcommunity-name delete
Example:
Device(config-route-map)# set extcomm-list 22
delete

Step 8

set extcommunity rt range start-value end-value
Example:
Device(config-route-map)# set extcommunity rt
range 500:1 500:9

Step 9

exit
Example:

Purpose
• This example permits the routes allowed by the
subsequent match command.
Matches on the specified community list.
• For this example, routes that match the extended
community list 22 (which was configured in Step 3)
are subject to the subsequent set commands.
Deletes the RT from routes that are in the specified
extended community list.
• For this example, RTs are deleted from routes that
are in extended community list 22.
For the routes that are permitted by the route map, sets the
specified RT range of extended community attributes,
inclusive.
• For this example, routes that match extended
community 22 have their RT extended community
attribute values set to 500:1, 500:2, 500:3, 500:4,
500:5, 500:6, 500:7, 500:8, and 500:9.
Exits route-map configuration mode and enters global
configuration mode.

Device(config-route-map)# exit

Step 10

route-map map-tag {permit | deny} [sequence-number] (Optional) Configures a route map entry that permits
routes.
Example:
• This example configures a route map entry that
Device(config)# route-map rt-mapping permit 20
permits other routes not subject to the RT-to-RT range
mapping. If you do not perform this step, all other
routes are subject to an implicit deny.

Step 11

exit
Example:

Exits route-map configuration mode and enters global
configuration mode.

Device(config-route-map)# exit

Step 12

router bgp as-number
Example:
Device(config)# router bgp 3000

IP Routing: BGP Configuration Guide
998

Enters router configuration mode and creates a BGP
routing process.


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Replacing a Range of RTs with an RT

Step 13

Command or Action

Purpose

neighbor ip-address remote-as
autonomous-system-number

Specifies that the neighbor belongs to the autonomous
system.

Example:
Device(config-router)# neighbor 192.168.103.1
remote-as 3000

Step 14

address-family vpnv4
Example:

Enters address family configuration mode to configure
BGP peers to accept address family-specific configurations.

Device(config-router)# address-family vpnv4

Step 15

neighbor ip-address activate

Activates the specified neighbor.

Example:
Device(config-router-af)# neighbor 192.168.103.1
activate

Step 16

neighbor ip-address route-map map-tag out
Example:

Applies the specified outgoing route map to the specified
neighbor.

Device(config-router-af)# neighbor 192.168.103.1
route-map rt-mapping out

Step 17

exit-address-family
Example:

Exits address family configuration mode and enters
privileged EXEC mode.

Device(config-router-af)# exit-address-family

Replacing a Range of RTs with an RT
Perform this task on an ingress ASBR to replace an RT range of attributes with an RT attribute. This task
assumes you already configured the egress ASBR to replace the RT with an RT range; that task is described
in the “Replacing an RT with a Range of RTs” section.
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
ip extcommunity-list expanded-list {permit | deny} rt reg-exp
exit
route-map map-tag {permit | deny} [sequence-number]
match extcommunity extended-community-list-name
set extcomm-list extcommunity-name delete
set extcommunity rt value additive
exit

IP Routing: BGP Configuration Guide
999


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Replacing a Range of RTs with an RT

10.
11.
12.
13.
14.
15.
16.
17.

route-map map-tag {permit | deny} [sequence-number]
exit
router bgp as-number
neighbor ip-address remote-as autonomous-system-number
address-family vpnv4
neighbor ip-address activate
neighbor ip-address route-map map-tag in
exit-address-family

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

ip extcommunity-list expanded-list {permit | deny} rt
reg-exp
Example:
Device(config)# ip extcommunity-list 128 permit
rt 500:[1-9]

Step 4

exit
Example:

Configures an IP extended community list to configure
Virtual Private Network (VPN) route filtering, such that
routes with the specified RT range are in the extended
community list.
• This example permits routes having RTs in the range
500:1 to 500:9 into the extended community list 128.
Exits the configuration mode and enters the next higher
configuration mode.

Device(config-extcomm-list)# exit

Step 5

route-map map-tag {permit | deny} [sequence-number] Configures a route map that permits or denies the routes
allowed by the subsequent match command.
Example:
• This example permits the routes allowed by the
Device(config)# route-map rtmap2 permit 10
subsequent match command.

Step 6

match extcommunity extended-community-list-name
Example:
Device(config-route-map)# match extcommunity 128

Step 7

set extcomm-list extcommunity-name delete
Example:

IP Routing: BGP Configuration Guide
1000

Matches on the specified community list.
• In this example, routes that match the extended
community list 128 (which was configured in Step
3) are subject to the subsequent set commands.
Deletes the RTs in the range from routes that are in the
specified extended community list.


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Replacing a Range of RTs with an RT

Command or Action
Device(config-route-map)# set extcomm-list 128
delete

Step 8

set extcommunity rt value additive
Example:
Device(config-route-map)# set extcommunity rt
400:1 additive

Step 9

exit
Example:

Purpose
• In this example, RTs in the range are deleted from
routes that are in extended community list 128.
Sets the routes that are permitted by the route map with
the specified RT.
• In this example, routes that match extended
community 128 have their RT set to 400:1. The
additive keyword causes the RT to be added to the
RT list without replacing any RTs.
Exits route-map configuration mode and enters global
configuration mode.

Device(config-route-map)# exit

Step 10

route-map map-tag {permit | deny} [sequence-number] (Optional) Configures a route map entry that permits
routes.
Example:
• This example configures a route map entry that
Device(config)# route-map rtmap2 permit 20
permits other routes not subject to the RT-range-to-RT
mapping. If you do not perform this step, all other
routes are subject to an implicit deny.

Step 11

exit
Example:

Exits route-map configuration mode and enters global
configuration mode.

Device(config-route-map)# exit

Step 12

router bgp as-number
Example:

Enters router configuration mode and creates a BGP
routing process.

Device(config)# router bgp 4000

Step 13

neighbor ip-address remote-as
autonomous-system-number

Specifies that the neighbor belongs to the autonomous
system.

Example:
Device(config-router)# neighbor 192.168.0.50
remote-as 4000

Step 14

address-family vpnv4
Example:

Enters address family configuration mode to configure
BGP peers to accept address-family-specific
configurations.

Device(config-router-af)# address-family vpnv4

Step 15

neighbor ip-address activate

Activates the specified neighbor.

Example:

IP Routing: BGP Configuration Guide
1001


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Configuration Examples for BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard

Command or Action

Purpose

Device(config-router-af)# neighbor 192.168.0.50
activate

Step 16

neighbor ip-address route-map map-tag in
Example:

Applies the specified incoming route map to the specified
neighbor.

Device(config-router-af)# neighbor 192.168.0.50
route-map rtmap2 in

Step 17

exit-address-family
Example:

Exits address family configuration mode and enters
privileged EXEC mode.

Device(config-router-af)# exit-address-family

Configuration Examples for BGP—RT and VPN Distinguisher
Attribute Rewrite Wildcard
Example: Replacing an RT with a Range of RTs
In the following example, on the egress ASBR, routes having RT 101:100 are in the extended
community list 22. A route-map named rt-mapping matches on extended community list 22 and
deletes the RT from routes in the community list. Routes that match the community list have their
RT set to an RT in the range from 500:1 to 500:9. The route map is applied to the neighbor
192.168.103.1.
Egress ASBR
ip extcommunity-list 22 permit rt 101:100
!
route-map rt-mapping permit 10
match extcommunity 22
set extcomm-list 22 delete
set extcommunity rt range 500:1 500:9
!
route-map rt-mapping permit 20
!
router bgp 3000
neighbor 192.168.103.1 remote-as 3000
address-family vpnv4
neighbor 192.168.103.1 activate
neighbor 192.168.103.1 route-map rt-mapping out
exit-address-family
!

On the ingress ASBR, RTs in the range 500:1 to 500:9 belong to extended community list 128. A
route map named rtmap2 maps those RTs to RT 400:1. The route map is applied to the neighbor
192.168.0.50.

IP Routing: BGP Configuration Guide
1002


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Example: Replacing an RT with a Range of VPN Distinguishers

Ingress ASBR
ip extcommunity-list 128 permit RT:500:[1-9]
!
route-map rtmap2 permit 10
match extcommunity 128
set extcomm-list 128 delete
set extcommunity rt 400:1 additive
!
route-map rtmap2 permit 20
!
router bgp 4000
neighbor 192.168.0.50 remote-as 4000
address-family vpnv4
neighbor 192.168.0.50 activate
neighbor 192.168.0.50 route-map rtmap2 in
exit-address-family
!

Example: Replacing an RT with a Range of VPN Distinguishers
In the following example, on the egress ASBR, routes having RT 201:100 are in the extended
community list 22. A route-map named rt-mapping matches on extended community list 22 and
deletes the RT from routes in the community list. Routes that match the community list have their
VPN distinguishers set to VPN distinguishers in the range from 600:1 to 600:8. The route map is
applied to the neighbor 192.168.103.1.
Egress ASBR
ip extcommunity-list 22 permit rt 201:100
!
route-map rt-mapping permit 10
match extcommunity 22
set extcomm-list 22 delete
set extcommunity vpn-distinguisher range 600:1 600:8
!
route-map rt-mapping permit 20
!
router bgp 3000
neighbor 192.168.103.1 remote-as 3000
address-family vpnv4
neighbor 192.168.103.1 activate
neighbor 192.168.103.1 route-map rt-mapping out
exit-address-family
!

On the ingress ASBR, VPN distinguishers in the range 600:1 to 600:8 belong to extended community
list 101. A route map named rtmap2 maps those VPN distinguishers to RT range 700:1 700:10. The
route map is applied to the neighbor 192.168.0.50. The additive option adds the new range to the
existing value without replacing it.
Ingress ASBR
ip extcommunity-list 101 permit VD:600:[1-8]
!
route-map rtmap2 permit 10
match extcommunity 101

IP Routing: BGP Configuration Guide
1003


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Additional References for BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard

set extcomm-list 101 delete
set extcommunity rt 700:1 700:10 additive
!
route-map rtmap2 permit 20
!
router bgp 4000
neighbor 192.168.0.50 remote-as 4000
address-family vpnv4
neighbor 192.168.0.50 activate
neighbor 192.168.0.50 route-map rtmap2 in
exit-address-family
!

Additional References for BGP-RT and VPN Distinguisher
Attribute Rewrite Wildcard
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

BGP commands

Cisco IOS IP Routing: BGP
Command Reference

BGP—VPN Distinguisher Attribute

“BGP—VPN Distinguisher
Attribute” module in the IP
Routing: BGP Configuration
Guide, Cisco IOS XE Release 3S

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
1004


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Feature Information for BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard

Feature Information for BGP—RT and VPN Distinguisher
Attribute Rewrite Wildcard
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 87: Feature Information for BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard

Feature Name

Releases

BGP—RT and VPN Distinguisher Cisco IOS XE 3.9S
Attribute Rewrite Wildcard

Feature Information
The BGP—RT and VPN
Distinguisher Attribute Rewrite
Wildcard feature introduces the
ability to set a range of route target
(RT) community attributes or VPN
distinguisher community attributes
when mapping them. A network
administrator might want to map
one or more RTs at an egress
ASBR to different RTs at an ingress
ASBR. The VPN Distinguisher
Attribute feature allows an
administrator to map RTs to a VPN
distinguisher that is carried through
an eBGP and then mapped to RTs
at an ingress ASBR. The mapping
is achieved by configuring a route
map that sets an RT range or VPN
distinguisher range of extended
community attributes. Specifying
a range rather than individual RTs
saves time and simplifies the
configuration. Furthermore, a VPN
distinguisher range allows more
than one VPN distinguisher
attribute per route-map clause,
thereby removing the restriction
that applied prior to this feature.
The following commands were
modified:
• set extcommunity rt
• set extcommunity
vpn-distinguisher

IP Routing: BGP Configuration Guide
1005


BGP-RT and VPN Distinguisher Attribute Rewrite Wildcard
Feature Information for BGP—RT and VPN Distinguisher Attribute Rewrite Wildcard

IP Routing: BGP Configuration Guide
1006
