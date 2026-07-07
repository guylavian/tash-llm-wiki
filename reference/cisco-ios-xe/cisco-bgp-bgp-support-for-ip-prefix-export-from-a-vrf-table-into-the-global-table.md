---
title: "BGP Support for IP Prefix Export from a VRF Table into the Global Table"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-ip-prefix-export-from-a-vrf-table-into-the-global-table
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 39 BGP Support for IP Prefix Export from a VRF Table into the Global Table This feature allows a network administrator to export IP prefixes from a VRF table into the global routing table. • Finding Feature Information, on page 635 • Information About IP Prefix Export from a VRF Table into the Global Table, on page 635 • How to Export IP Prefixes from a VRF Table into the Global Table, o"
---

# BGP Support for IP Prefix Export from a VRF Table into the Global Table

CHAPTER

39

BGP Support for IP Prefix Export from a VRF Table
into the Global Table
This feature allows a network administrator to export IP prefixes from a VRF table into the global routing
table.
• Finding Feature Information, on page 635
• Information About IP Prefix Export from a VRF Table into the Global Table, on page 635
• How to Export IP Prefixes from a VRF Table into the Global Table, on page 637
• Configuration Examples for IP Prefix Export from a VRF Table into the Global Table, on page 643
• Additional References, on page 644
• Feature Information for IP Prefix Export from a VRF Table into the Global Table, on page 644

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About IP Prefix Export from a VRF Table into the
Global Table
Benefits of IP Prefix Export from a VRF Table into the Global Table
• You can manage some network resources inside a VRF by using a network management node residing
in the global table.
• You own some internet public IP address space, but prefer to have a VRF to manage those IP addresses.

IP Routing: BGP Configuration Guide
635


BGP Support for IP Prefix Export from a VRF Table into the Global Table
How IP Prefix Export from a VRF Table into the Global Table Works

How IP Prefix Export from a VRF Table into the Global Table Works
MPLS-VPN using Multiprotocol BGP (MP-BGP) provides a very flexible but secured VPN provisioning
mechanism for service providers and customers. However, some customers prefer to relax the boundary so
that some specific prefixes can be reachable in a VRF as well as in the global routing table.
Prior to the BGP Support for IP Prefix Export from a VRF Table into Global Table feature, BGP already
supported the global-to-VRF import of prefixes. See the “BGP Support for IP Prefix Import from Global
Table into a VRF Table” module for complete documentation of that feature. Together, the import feature
and export feature provide L3VPN dynamic route leaking.
The BGP Support for IP Prefix Export from a VRF Table into the Global Table feature provides the reverse
mechanism of the import feature referenced above; it supports the export of prefixes from a VRF table to the
global routing table. It is achieved with an export {ipv4 | ipv6} {unicast | multicast} map command, which
specifies a route map to control the prefixes that are exported from a VRF table to the global routing table.

Caution

The IP Prefix Export from a VRF Table into Global Table feature leaks VRF routes into the global BGP
routing table; those routes will be installed into the IPv4 or IPv6 routing table. Use extreme caution to design
the network so that such leaking does not affect the normal Internet routing.
Export actions are triggered when a new routing update is received or when routes are withdrawn. During the
initial BGP update period, the export action is postponed to allow BGP to converge more quickly. Once BGP
converges, incremental BGP updates are evaluated immediately and qualified prefixes are exported as they
are received.
Each VRF can export to only one of the global topologies in IPv4 (unicast or multicast) and can export to
only one of the global topologies in IPv6 (unicast or multicast).
There is no limit to the number of VRFs per router that can be configured to export IPv4 or IPv6 prefixes to
the global routing table.
By default, the software limits the number of prefixes that can be exported per VRF to 1000 prefixes. You
can change that limit to a number in the range from 1 to 2,147,483,647 prefixes for each VRF. We recommend
that you use caution if you increase the prefix limit above 1000. Configuring the device to export too many
prefixes can interrupt normal router operation.
The following match and set commands are supported in this feature:
• match as-path
• match community [exact-match]
• match extcommunity
• match ip address [prefix-list]
• match ip next-hop
• match ip route-source
• match ipv6 address [prefix-list]
• match ipv6 route-source
• match ipv6 next-hop

IP Routing: BGP Configuration Guide
636


BGP Support for IP Prefix Export from a VRF Table into the Global Table
How to Export IP Prefixes from a VRF Table into the Global Table

• match policy-list
• match route-type
• set as-path prepend [last-as]
• set community additive
• set extcommunity [cost | rt]
• set extcomm-list delete
• set ip next-hop
• set ipv6 next-hop
• set local-preference
• set metric
• set origin
• set weight

Note

The set ip vrf next-hop and set ipv6 vrf next-hop commands are not supported in this feature.

How to Export IP Prefixes from a VRF Table into the Global Table
Creating the VRF and the Export Route Map for an Address Family
The IP prefixes that are defined for export are processed through a match clause in a route map. IP prefixes
that pass through the route map are exported into the global routing table.
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

enable
configure terminal
vrf definition vrf-name
rd route-distinguisher
address-family {ipv4 | ipv6}
export {ipv4 | ipv6} {unicast | multicast} [prefix-limit] map map-name
route-target import route-target-ext-community
route-target export route-target-ext-community
exit
exit
route-map map-tag [permit | deny] [sequence-number]
match ip address {acl-number [acl-number | acl-name] | acl-name [acl-name | acl-number] | prefix-list
prefix-list-name [prefix-list-name]}

IP Routing: BGP Configuration Guide
637


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Creating the VRF and the Export Route Map for an Address Family

13.

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

vrf definition vrf-name
Example:

Creates a VRF routing table and specifies the VRF name
(or tag).

Device(config)# vrf definition vpn1

Step 4

rd route-distinguisher
Example:
Device(config-vrf)# rd 100:100

Step 5

address-family {ipv4 | ipv6}

Creates routing and forwarding tables for the VRF instance.
• There are two formats for configuring the argument.
It can be configured in the as-number:network number
(ASN:nn) format, as shown in the example, or it can
be configured in the IP address:network number
format (IP-address:nn).
Configures the IPv4 or IPv6 address family.

Example:
Device(config-vrf)# address-family ipv4

Step 6

export {ipv4 | ipv6} {unicast | multicast} [prefix-limit] Exports IPv4 or IPv6 prefixes from the VRF table to the
global routing table, filtered by the specified route map.
map map-name
Example:
Device(config-vrf-af)# export ipv4 unicast 500
map UNICAST

• Specify ipv4 or ipv6, which you specified in Step 5.
This example exports IPv4 unicast prefixes.
• Based on this example, no more than 500 prefixes
will be exported.
• The prefixes exported are those that pass the route
map.

Step 7

route-target import route-target-ext-community
Example:
Device(config-vrf-af)# route-target import 100:100

IP Routing: BGP Configuration Guide
638

Creates a route-target extended community for a VRF
instance.
• For information about route-target import or export,
see the MPLS: Layer 3 VPNs Configuration Guide.


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Creating the VRF and the Export Route Map for a VRF (IPv4 only)

Step 8

Command or Action

Purpose

route-target export route-target-ext-community

Creates a route-target extended community for a VRF
instance.

Example:
Device(config-vrf-af)# route-target export 100:100

Step 9

exit
Example:

Exits address family configuration mode and enters global
configuration mode.

Device(config-vrf-af)# exit

Step 10

exit
Example:

Exits VRF configuration mode and enters global
configuration mode.

Device(config-vrf)# exit

Step 11

route-map map-tag [permit | deny] [sequence-number] Enables policy routing.
Example:

• The example creates a route map named UNICAST.

Device(config)# route-map UNICAST permit 10

Step 12

match ip address {acl-number [acl-number | acl-name] Distributes any routes that have a destination network
number address that is permitted by a standard or extended
| acl-name [acl-name | acl-number] | prefix-list
access list, and performs policy routing on matched
prefix-list-name [prefix-list-name]}
packets.
Example:
• Both IP access lists and IP prefix lists are supported.
Device(config-route-map)# match ip address 50

• The example configures the route map to use standard
access list 50 to define match criteria.
• Define the access list (not shown in this task); for
example, access-list 50 permit 192.168.1.0
255.255.255.0.

Step 13

end
Example:

Exits route-map configuration mode and returns to
privileged EXEC mode.

Device(config-route-map)# end

Creating the VRF and the Export Route Map for a VRF (IPv4 only)
The IP prefixes that are defined for export are processed through a match clause in a route map. IP prefixes
that pass through the route map are exported into the global routing table.

IP Routing: BGP Configuration Guide
639


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Creating the VRF and the Export Route Map for a VRF (IPv4 only)

Note

• Only IPv4 unicast and multicast prefixes can be exported from a VRF table to the global routing table
under the ip vrf command, as shown in this task. To export IPv6 prefixes, you must do so under the IPv6
address family; see the section “Creating the VRF and the Export Route Map Per Address Family.”
• IPv4 prefixes exported into the global routing table using this feature cannot be exported into a VPNv4
VRF.

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
ip vrf vrf-name
rd route-distinguisher
export ipv4 {unicast | multicast} [prefix-limit] map map-tag
route-target import route-target-ext-community
route-target export route-target-ext-community
exit
route-map map-tag [permit | deny] [sequence-number]
match ip address {acl-number [acl-number | acl-name] | acl-name [acl-name | acl-number] | prefix-list
prefix-list-name [prefix-list-name]}
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

ip vrf vrf-name
Example:
Device(config)# ip vrf GREEN

Step 4

rd route-distinguisher
Example:
Device(config-vrf)# rd 100:10

IP Routing: BGP Configuration Guide
640

Creates a VRF routing table and specifies the VRF name
(or tag).
• The ip vrf vrf-name command creates a VRF routing
table and a CEF table, and both are named using the
vrf-name argument. Associated with these tables is
the default route distinguisher value.
Creates routing and forwarding tables for the VRF instance.
• There are two formats for configuring the argument.
It can be configured in the as-number:network number
(ASN:nn) format, as shown in the example, or it can


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Creating the VRF and the Export Route Map for a VRF (IPv4 only)

Command or Action

Purpose
be configured in the IP-address:network number
format (IP-address:nn).

Step 5

export ipv4 {unicast | multicast} [prefix-limit] map
map-tag

Exports IPv4 prefixes from the VRF table to the global
routing table, filtered by the specified route map.

Example:

• Unicast or multicast prefixes are specified.

Device(config-vrf)# export ipv4 unicast 500 map
UNICAST

• By default, up to 1000 prefixes can be exported. The
prefix-limit argument is used to specify a limit from
1 to 2,147,483,647 prefixes.
• The example creates an export map that will export
up to 500 unicast prefixes that pass through the route
map named UNICAST.

Step 6

route-target import route-target-ext-community
Example:
Device(config-vrf)# route-target import 100:100

Step 7

route-target export route-target-ext-community
Example:

Creates a route-target extended community for a VRF
instance.
• For information about route-target import or export,
see the MPLS: Layer 3 VPNs Configuration Guide.
Creates a route-target extended community for a VRF
instance.

Device(config-vrf)# route-target export 100:100

Step 8

exit
Example:

Exits VRF configuration mode and enters global
configuration mode.

Device(config-vrf)# exit

Step 9

route-map map-tag [permit | deny] [sequence-number] Defines the conditions for redistributing routes from one
routing protocol into another, or enables policy routing.
Example:
• The route map name must match the route map
Device(config)# route-map UNICAST permit 10
specified in Step 5.
• The example creates a route map named UNICAST.

Step 10

match ip address {acl-number [acl-number | acl-name] Distributes any routes that have a destination network
number address that is permitted by a standard or extended
| acl-name [acl-name | acl-number] | prefix-list
access list, and performs policy routing on matched
prefix-list-name [prefix-list-name]}
packets.
Example:
• Both IP access lists and IP prefix lists are supported.
Device(config-route-map)# match ip address 50

• The example configures the route map to use standard
access list 50 to define match criteria.

IP Routing: BGP Configuration Guide
641


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Displaying Information About IP Prefix Export from a VRF into the Global Table

Step 11

Command or Action

Purpose

end

Exits route-map configuration mode and returns to
privileged EXEC mode.

Example:
Device(config-route-map)# end

Displaying Information About IP Prefix Export from a VRF into the Global Table
Perform any of the steps in this task to see information about the prefixes exported from a VRF table into the
global table.
SUMMARY STEPS
1.
2.
3.
4.

enable
show ip bgp {ipv4 | ipv6} {unicast | multicast} [prefix]
debug ip bgp import event
debug ip bgp import update

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

show ip bgp {ipv4 | ipv6} {unicast | multicast} [prefix]
Example:

Displays information about the imported path from a VRF
to the global table.

Device# show ip bgp ipv4 unicast 192.168.1.1

Step 3

debug ip bgp import event

Displays messages related to IPv4 prefix import events.

Example:
Device# debug ip bgp import event

Step 4

debug ip bgp import update
Example:
Device# debug ip bgp import update

IP Routing: BGP Configuration Guide
642

Displays messages related to IPv4 prefix import updates.


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Configuration Examples for IP Prefix Export from a VRF Table into the Global Table

Configuration Examples for IP Prefix Export from a VRF Table
into the Global Table
Example: Exporting IP Prefixes from a VRF Table into the Global Table Using
IPv6 Address Family
vrf definition X
rd 100:100
address-family ipv6
export ipv6 unicast map OnlyNet2000
route-target import 100:100
route-target export 100:100
!
ipv6 prefix-list net2000 permit 2000::/16
!
route-map OnlyNet2000 permit 10
match ipv6 address prefix-list net2000

Example: Exporting IP Prefixes from a VRF Table into the Global Table Using
IPv4 Address Family
vrf definition X
rd 100:100
address-family ipv4
export ipv4 unicast map OnlyNet200
route-target import 100:100
route-target export 100:100
!
ip prefix-list net200 permit 200.0.0.0/8
!
route-map OnlyNet200 permit 10
match ip address prefix-list net200

Example: Exporting IP Prefixes from a VRF Table into the Global Table Using
IP VRF (IPv4 Only)
ip vrf vrfname
rd 100:100
export ipv4 unicast map OnlyNet200
route-target import 100:100
route-target export 100:100
!
ip prefix-list net200 permit 200.0.0.0/8
!
route-map OnlyNet200 permit 10
match ip address prefix-list net200

IP Routing: BGP Configuration Guide
643


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

BGP commands

Cisco IOS BGP Command
Reference

Use of route-target import and export

MPLS: Layer 3 VPNs
Configuration Guide

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

Feature Information for IP Prefix Export from a VRF Table into
the Global Table
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
644


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Feature Information for IP Prefix Export from a VRF Table into the Global Table

Table 55: Feature Information for BGP Support for IP Prefix Export from a VRF Table into the Global Table

Feature Name

Releases

Feature Information

BGP Support for IP Prefix Export Cisco IOS XE Release 3.7S
from a VRF Table into the Global
Table

This feature allows a network
administrator to export IP prefixes
from a VRF routing table into the
global routing table.
The following command was
introduced: export map (VRF
table to global table).
The following commands were
modified: debug ip bgp import
and show ip bgp.

IP Routing: BGP Configuration Guide
645


BGP Support for IP Prefix Export from a VRF Table into the Global Table
Feature Information for IP Prefix Export from a VRF Table into the Global Table

IP Routing: BGP Configuration Guide
646
