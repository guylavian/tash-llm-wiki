---
title: "BGP Accumulated IGP"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-accumulated-igp
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 82 BGP Accumulated IGP The BGP Accumulated IGP feature is an optional nontransitive Border Gateway Protocol (BGP) path attribute. The attribute type code for the accumulated interior gateway protocol (AIGP) attribute is assigned by the Internet Assigned Numbers Authority (IANA). The value field of the AIGP attribute is defined as a set of type, length, value (TLV) elements. The AIGP TLV"
---

# BGP Accumulated IGP

CHAPTER

82

BGP Accumulated IGP
The BGP Accumulated IGP feature is an optional nontransitive Border Gateway Protocol (BGP) path attribute.
The attribute type code for the accumulated interior gateway protocol (AIGP) attribute is assigned by the
Internet Assigned Numbers Authority (IANA). The value field of the AIGP attribute is defined as a set of
type, length, value (TLV) elements. The AIGP TLV contains the AIGP metric.
• Finding Feature Information, on page 1127
• Information About BGP Accumulated IGP, on page 1127
• How to Configure BGP Accumulated IGP, on page 1129
• Configuration Examples for BGP Accumulated IGP, on page 1132
• Additional References for BGP Accumulated IGP, on page 1133
• Feature Information for BGP Accumulated IGP, on page 1134

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Accumulated IGP
Overview of BGP Accumulated IGP
The BGP Accumulated IGP feature is required to simulate the current Open Shortest Path First (OSPF)
behavior of computing the distance associated with a path. OSPF or Label Distribution Protocol (LDP) carries
the prefix or label information only in the local area. Then, Border Gateway Protocol (BGP) carries the prefix
or label to all the remote areas by redistributing the routes into BGP at area boundaries. The routes or labels
are then advertised using label-switched paths (LSP). The next-hop for the route is changed at each Area
Border Router (ABR) to a local device, which removes the need to leak OSPF routes across area boundaries.
The bandwidth available on each of the core links is mapped to the OSPF cost; therefore, it is imperative that

IP Routing: BGP Configuration Guide
1127


BGP Accumulated IGP
Sending and Receiving BGP Accumulated IGP

BGP carries this cost correctly between each of the provider edge (PE) devices. This functionality is achieved
by using the BGP Accumulated IGP feature.
You need to enable accumulated interior gateway protocol (AIGP) processing for internal Border Gateway
Protocol (iBGP) and external Border Gateway Protocol (eBGP) neighbors to carry the AIGP attribute. Neighbors
configured with the AIGP attribute are put in a separate update group from other iBGP neighbors. A separate
update group is required for neighbors that are enabled to send the AIGP value to cost community. BGP needs
to translate the AIGP attribute to the cost community or multi-exit discriminator (MED) and attach it to the
route before advertising to legacy.
When BGP installs AIGP attribute routes into the routing information base (RIB), it adds the AIGP cost with
the next-hop cost. If the next-hop is a nonrecursive IGP route, BGP sets the AIGP metric to the received AIGP
value and the first hop IGP metric to the next-hop. If the next-hop is a recursive route with the AIGP metric,
BGP adds the received AIGP metric to the next-hop AIGP metric.

Sending and Receiving BGP Accumulated IGP
When a session receives a prefix with the accumulated interior gateway protocol (AIGP) attribute and is not
configured to receive AIGP information, the session discards the AIGP attribute and processes the remainder
of the update message, and then it passes the AIGP attribute to other BGP peers. The route is then installed
into the routing information base (RIB) and the prefix is sent with the AIGP attribute to all the AIGP-enabled
neighbors. The AIGP attribute value is not updated if the next-hop of the route is not changed by the device
before advertising it to the neighbor. If the device changes the next-hop of the route, it recalculates the AIGP
attribute value by adding the next-hop metric to the received AIGP attribute value.

Originating Prefixes with Accumulated IGP
Origination of routes with the accumulated interior gateway protocol (AIGP) metric is controlled by
configuration. AIGP attributes are attached to redistributed routes that satisfy the following conditions:
• The protocol redistributing the route is enabled for AIGP.
• The route is an interior gateway protocol (IGP) route redistributed into Border Gateway Protocol (BGP).
The value assigned to the AIGP attribute is the value of the IGP next-hop to the route or as set by a route
policy.
• The route is a static route redistributed into BGP. The value assigned is the value of the next-hop to the
route or as set by a route policy.
• The route is imported into BGP through a network statement. The value assigned is the value of the
next-hop to the route or as set by a route policy.
• The inbound or outbound route map also creates an AIGP attribute route map using the set aigp-metric
command.

IP Routing: BGP Configuration Guide
1128


BGP Accumulated IGP
How to Configure BGP Accumulated IGP

How to Configure BGP Accumulated IGP
Configuring AIGP Metric Value
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
router bgp as-number
address-family ipv4 [unicast | multicast | vrf vrf-name]
redistribute protocol autonomous-system-number route-map map-tag
network network-id route-map map-tag
exit
route-map rtmap
set aigp-metric [igp-metric | value]
end

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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 40000

Step 4

address-family ipv4 [unicast | multicast | vrf vrf-name] Specifies the IPv4 address family and enters address family
configuration mode.
Example:
Device(config-router)# address-family ipv4 unicast

Step 5

redistribute protocol autonomous-system-number
route-map map-tag

Redistributes routes from one routing domain to another
routing domain.

Example:

IP Routing: BGP Configuration Guide
1129


BGP Accumulated IGP
Enabling Send and Receive for an AIGP Attribute

Command or Action

Purpose

Device(config-router-af)# redistribute bgp 100
route-map rtmap

Step 6

network network-id route-map map-tag
Example:

Specifies the networks to be advertised by the Border
Gateway Protocol (BGP) routing process.

Device(config-router-af)# network 10.1.1.1
route-map rtmap

Step 7

Exits address family configuration mode and returns to
global configuration mode.

exit
Example:
Device(config-router-af)# exit

Step 8

route-map rtmap

Enters route map configuration mode.

Example:
Device(config)# route-map rtmap

Step 9

set aigp-metric [igp-metric | value]
Example:

Specifies a metric value for the accumulated interior
gateway protocol (AIGP) attribute. The manual metric
value range is from 0 to 4294967295.

Device(config-route-map)# set aigp-metric
igp-metric

Step 10

Exits route map configuration mode and enters privileged
EXEC mode.

end
Example:
Device(config-route-map)# end

Enabling Send and Receive for an AIGP Attribute
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
address-family {ipv4 | ipv6} [unicast]
neighbor ip-address aigp
end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: BGP Configuration Guide
1130


BGP Accumulated IGP
Configuring BGP Accumulated IGP

Command or Action
Example:

Purpose
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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 40000

Step 4

address-family {ipv4 | ipv6} [unicast]
Example:

Specifies the IPv4 or IPv6 address family and enters address
family configuration mode.

Device(config-router)# address-family ipv4 unicast

Step 5

neighbor ip-address aigp

Enables send and receive of the AIGP attribute per neighbor.

Example:
Device(config-router-af)# neighbor 192.168.1.1 aigp

Step 6

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuring BGP Accumulated IGP
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp as-number
address-family {ipv4 | ipv6} [unicast]
neighbor ip-address aigp [send {cost-community community-id poi {igp-cost | pre-bestpath}
[transitive]} | med]
6. end
DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: BGP Configuration Guide
1131


BGP Accumulated IGP
Configuration Examples for BGP Accumulated IGP

Command or Action
Example:

Purpose
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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 40000

Step 4

address-family {ipv4 | ipv6} [unicast]
Example:

Specifies the IPv4 or IPv6 address family and enters address
family configuration mode.

Device(config-router)# address-family ipv4 unicast

Step 5

Translates the AIGP attribute to MED and attaches it to the
neighbor ip-address aigp [send {cost-community
community-id poi {igp-cost | pre-bestpath} [transitive]} route before advertising to legacy provider edge (PE)
devices.
| med]
Example:
Device(config-router-af)# neighbor 192.168.1.1 aigp
send med

Step 6

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuration Examples for BGP Accumulated IGP
Example: Configuring AIGP Metric Value
The following is a sample configuration for originating prefixes with the accumulated internal gateway
protocol (AIGP) metric attribute:
Device# configure terminal
Device(config)# router bgp 40000
Device(config-router)# address-family ipv4 unicast
Device(config-router-af)# redistribute bgp 100 route-map rtmap
Device(config-router-af)# network 10.1.1.1 route-map rtmap
Device(config-router-af)# exit
Device(config)# route-map rtmap

IP Routing: BGP Configuration Guide
1132


BGP Accumulated IGP
Example: Enabling Send and Receive for an AIGP Attribute

Device(config-route-map)# set aigp-metric igp-metric
Device(config-route-map)# end

Example: Enabling Send and Receive for an AIGP Attribute
The following example shows how to enable AIGP send and receive capability in address family
configuration mode:
Device# configure terminal
Device(config)# router bgp 40000
Device(config-router)# address-family ipv4 unicast
Device(config-router-af)# neighbor 192.168.1.1 aigp
Device(config-router-af)# exit

Example: Configuring BGP Accumulated IGP
In the following example, the device belongs to autonomous system 65000 and is configured to send
the cost-community attribute to its neighbor at IP address 172.16.70.23:
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# address-family ipv4 multicast
Device(config-router-af)# neighbor 172.16.70.23 aigp send cost-community 100 poi igp-cost
transitive
Device(config-router-af)# exit

In the following example, the device belongs to autonomous system 65000 and is configured to send
the MED attribute to its neighbor at IP address 172.16.70.23:
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# address-family ipv4 multicast
Device(config-router-af)# neighbor 172.16.70.23 aigp send med
Device(config-router-af)# exit

Additional References for BGP Accumulated IGP
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Routing: BGP Configuration Guide
1133


BGP Accumulated IGP
Feature Information for BGP Accumulated IGP

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

Feature Information for BGP Accumulated IGP
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 102: Feature Information for BGP Accumulated IGP

Feature Name

Releases

BGP Accumulated Cisco IOS XE
IGP
Release 3.12S

Feature Information
The BGP Accumulated IGP feature is an optional nontransitive
Border Gateway Protocol (BGP) path attribute. The attribute type
code for the accumulated interior gateway protocol (AIGP) attribute
is assigned by the IANA. The value field of the AIGP attribute is
defined as a set of type, length, value (TLV) elements. The AIGP
TLV contains the AIGP metric.
The following commands were introduced:
aigp, aigp send cost-community, aigp send med, bgp bestpath
aigp ignore, set aigp-metric

IP Routing: BGP Configuration Guide
1134
