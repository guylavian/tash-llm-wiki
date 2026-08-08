---
title: "IPv6 Multicast Address Family Support for Multiprotocol BGP"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-ipv6-multicast-address-family-support-for-multiprotocol-bgp
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 9 IPv6 Multicast Address Family Support for Multiprotocol BGP • Finding Feature Information, on page 205 • Information About IPv6 Multicast Address Family Support for Multiprotocol BGP, on page 205 • How to Implement IPv6 Multicast Address Family Support for Multiprotocol BGP, on page 206 • Configuration Examples for IPv6 Multicast Address Family Support for Multiprotocol BGP, on page 21"
---

# IPv6 Multicast Address Family Support for Multiprotocol BGP

CHAPTER

9

IPv6 Multicast Address Family Support for
Multiprotocol BGP
• Finding Feature Information, on page 205
• Information About IPv6 Multicast Address Family Support for Multiprotocol BGP, on page 205
• How to Implement IPv6 Multicast Address Family Support for Multiprotocol BGP, on page 206
• Configuration Examples for IPv6 Multicast Address Family Support for Multiprotocol BGP, on page
214
• Additional References, on page 215
• Feature Information for IPv6 Multicast Address Family Support for Multiprotocol BGP, on page 216

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About IPv6 Multicast Address Family Support for
Multiprotocol BGP
Multiprotocol BGP for the IPv6 Multicast Address Family
The multiprotocol BGP for the IPv6 multicast address family feature provides multicast BGP extensions for
IPv6 and supports the same features and functionality as IPv4 BGP. IPv6 enhancements to multicast BGP
include support for an IPv6 multicast address family and network layer reachability information (NLRI) and
next hop (the next router in the path to the destination) attributes that use IPv6 addresses.
Multicast BGP is an enhanced BGP that allows the deployment of interdomain IPv6 multicast. Multiprotocol
BGP carries routing information for multiple network layer protocol address families; for example, IPv6
address family and for IPv6 multicast routes. The IPv6 multicast address family contains routes used for RPF

IP Routing: BGP Configuration Guide
205


IPv6 Multicast Address Family Support for Multiprotocol BGP
How to Implement IPv6 Multicast Address Family Support for Multiprotocol BGP

lookup by the IPv6 PIM protocol, and multicast BGP IPv6 provides for interdomain transport of the same.
Users must use multiprotocol BGP for IPv6 multicast when using IPv6 multicast with BGP because the unicast
BGP learned routes will not be used for IPv6 multicast.
Multicast BGP functionality is provided through a separate address family context. A subsequent address
family identifier (SAFI) provides information about the type of the network layer reachability information
that is carried in the attribute. Multiprotocol BGP unicast uses SAFI 1 messages, and multiprotocol BGP
multicast uses SAFI 2 messages. SAFI 1 messages indicate that the routes are usable only for IP unicast, not
IP multicast. Because of this functionality, BGP routes in the IPv6 unicast RIB must be ignored in the IPv6
multicast RPF lookup.
A separate BGP routing table is maintained to configure incongruent policies and topologies (for example,
IPv6 unicast and multicast) by using IPv6 multicast RPF lookup. Multicast RPF lookup is very similar to the
IP unicast route lookup.
No MRIB is associated with the IPv6 multicast BGP table. However, IPv6 multicast BGP operates on the
unicast IPv6 RIB when needed. Multicast BGP does not insert or update routes into the IPv6 unicast RIB.

How to Implement IPv6 Multicast Address Family Support for
Multiprotocol BGP
Configuring an IPv6 Peer Group to Perform Multicast BGP Routing
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.

enable
configure terminal
router bgp as-number
neighbor peer-group-name peer-group
neighbor {ip-address | ipv6-address | peer-group-name} remote-as as-number
address-family ipv6 [unicast | multicast]
neighbor {ip-address | peer-group-name | ipv6-address} activate
neighbor {ip-address | ipv6-address} peer-group peer-group-name

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
Example:
Device# configure terminal

IP Routing: BGP Configuration Guide
206

Enters global configuration mode.


IPv6 Multicast Address Family Support for Multiprotocol BGP
Advertising Routes into IPv6 Multiprotocol BGP

Step 3

Command or Action

Purpose

router bgp as-number

Enters router configuration mode for the specified BGP
routing process.

Example:
Device(config)# router bgp 65000

Step 4

neighbor peer-group-name peer-group

Creates a BGP peer group.

Example:
Device(config-router)# neighbor group1 peer-group

Step 5

neighbor {ip-address | ipv6-address | peer-group-name} Adds the IPv6 address of the neighbor in the specified
autonomous system to the IPv6 multicast BGP neighbor
remote-as as-number
table of the local router.
Example:
• The ipv6-address argument in the neighbor remote-as
Device(config-router)# neighbor 2001:DB8:0:CC00::1
command must be in the form documented in RFC
remote-as 64600
2373 where the address is specified in hexadecimal
using 16-bit values between colons.

Step 6

address-family ipv6 [unicast | multicast]
Example:
Device(config-router)# address-family ipv6
multicast

Step 7

neighbor {ip-address | peer-group-name | ipv6-address}
activate
Example:
Device(config-router-af)# neighbor
2001:DB8:0:CC00::1 activate

Step 8

neighbor {ip-address | ipv6-address} peer-group
peer-group-name

Specifies the IPv6 address family, and enters address family
configuration mode.
• The unicast keyword specifies the IPv6 unicast address
family. By default, the router is placed in configuration
mode for the IPv6 unicast address family if a keyword
is not specified in the address-family ipv6 command.
• The multicast keyword specifies IPv6 multicast
address prefixes.
Enables the neighbor to exchange prefixes for the specified
family type with the neighbor and the local router.
• To avoid extra configuration steps for each neighbor,
use the neighbor activate command with the
peer-group-name argument as an alternative in this
step.
Assigns the IPv6 address of a BGP neighbor to a peer group.

Example:
Device(config-router-af)# neighbor
2001:DB8:0:CC00::1 peer-group group1

Advertising Routes into IPv6 Multiprotocol BGP
By default, networks that are defined in router configuration mode using the network command are injected
into the IPv4 unicast database. To inject a network into another database, such as the IPv6 BGP database, you
must define the network using the network command in address family configuration mode for the other
database, as shown for the IPv6 BGP database.

IP Routing: BGP Configuration Guide
207


IPv6 Multicast Address Family Support for Multiprotocol BGP
Advertising Routes into IPv6 Multiprotocol BGP

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
address-family ipv6 [vrf vrf-name] [unicast | multicast | vpnv6]
network {network-number [mask network-mask] | nsap-prefix} [route-map map-tag]
exit

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

Enters router configuration mode for the specified BGP
routing process.

Device(config)# router bgp 65000

Step 4

address-family ipv6 [vrf vrf-name] [unicast | multicast Specifies the IPv6 address family, and enters address family
configuration mode.
| vpnv6]
Example:
Device(config-router)# address-family ipv6 unicast

• The unicast keyword specifies the IPv6 unicast address
family. By default, the device is placed in configuration
mode for the IPv6 unicast address family if a keyword
is not specified with the address-family ipv6
command.
• The multicast keyword specifies IPv6 multicast
address prefixes.

Step 5

network {network-number [mask network-mask] |
nsap-prefix} [route-map map-tag]
Example:
Device(config-router-af)# network 2001:DB8::/24

Advertises (injects) the specified prefix into the IPv6 BGP
database (the routes must first be found in the IPv6 unicast
routing table).
• The prefix is injected into the database for the address
family specified in the previous step.
• Routes are tagged from the specified prefix as “local
origin.”
• The ipv6-prefix argument in the network command
must be in the form documented in RFC 2373 where

IP Routing: BGP Configuration Guide
208


IPv6 Multicast Address Family Support for Multiprotocol BGP
Redistributing Prefixes into IPv6 Multiprotocol BGP

Command or Action

Purpose
the address is specified in hexadecimal using 16-bit
values between colons.
• The prefix-length argument is a decimal value that
indicates how many of the high-order contiguous bits
of the address comprise the prefix (the network portion
of the address). A slash mark must precede the decimal
value.

Step 6

Exits address family configuration mode, and returns the
device to router configuration mode.

exit
Example:
Device(config-router-af)# exit

• Repeat this step to exit router configuration mode and
return the device to global configuration mode.

Redistributing Prefixes into IPv6 Multiprotocol BGP
Redistribution is the process of redistributing, or injecting, prefixes from one routing protocol into another
routing protocol. This task explains how to inject prefixes from a routing protocol into IPv6 multiprotocol
BGP. Specifically, prefixes that are redistributed into IPv6 multiprotocol BGP using the redistribute router
configuration command are injected into the IPv6 unicast database.
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
address-family ipv6 [vrf vrf-name] [unicast | multicast | vpnv6]
redistribute bgp [process-id] [metric metric-value] [route-map map-name] [source-protocol-options]
exit

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

Enters router configuration mode for the specified BGP
routing process.

IP Routing: BGP Configuration Guide
209


IPv6 Multicast Address Family Support for Multiprotocol BGP
Assigning a BGP Administrative Distance

Command or Action

Purpose

Device(config)# router bgp 65000

Step 4

address-family ipv6 [vrf vrf-name] [unicast | multicast Specifies the IPv6 address family, and enters address family
configuration mode.
| vpnv6]
Example:
Device(config-router)# address-family ipv6

Step 5

redistribute bgp [process-id] [metric metric-value]
[route-map map-name] [source-protocol-options]

• The unicast keyword specifies the IPv6 unicast address
family. By default, the device is placed in configuration
mode for the IPv6 unicast address family if a keyword
is not specified with the address-family ipv6
command.
• The multicast keyword specifies IPv6 multicast
address prefixes.
Redistributes IPv6 routes from one routing domain into
another routing domain.

Example:
Device(config-router-af)# redistribute bgp 64500
metric 5

Step 6

Exits address family configuration mode, and returns the
device to router configuration mode.

exit
Example:
Device(config-router-af)# exit

• Repeat this step to exit router configuration mode and
return the device to global configuration mode.

Assigning a BGP Administrative Distance
Caution

Changing the administrative distance of BGP internal routes is not recommended. One problem that can occur
is the accumulation of routing table inconsistencies, which can break routing.

SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp as-number
address-family ipv6 [unicast | multicast}
distance bgp external-distance internal-distance local-distance

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

IP Routing: BGP Configuration Guide
210

• Enter your password if prompted.


IPv6 Multicast Address Family Support for Multiprotocol BGP
Generating Translate Updates for IPv6 Multicast BGP

Command or Action

Purpose

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

Device(config)# router bgp 100

Step 4

address-family ipv6 [unicast | multicast}
Example:

Enters address family configuration mode for configuring
routing sessions such as BGP that use standard IPv6 address
prefixes.

Device(config-router)# address-family ipv6
multicast

Step 5

distance bgp external-distance internal-distance
local-distance

Assigns a BGP administrative distance.

Example:
Device(config-router)# distance bgp 20 20 200

Generating Translate Updates for IPv6 Multicast BGP
The multicast BGP translate-update feature generally is used in a multicast BGP-capable router that peers
with a customer site that has only a BGP-capable router; the customer site has not or cannot upgrade its router
to a multicast BGP-capable image. Because the customer site cannot originate multicast BGP advertisements,
the router with which it peers will translate the BGP prefixes into multicast BGP prefixes, which are used for
multicast-source RPF lookup.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp as-number
address-family ipv6 [unicast | multicast}
neighbor ipv6-address translate-update ipv6 multicast [unicast]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

IP Routing: BGP Configuration Guide
211


IPv6 Multicast Address Family Support for Multiprotocol BGP
Resetting IPv6 BGP Sessions

Command or Action

Purpose

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

Device(config)# router bgp 100

Step 4

address-family ipv6 [unicast | multicast}
Example:

Enters address family configuration mode for configuring
routing sessions such as BGP that use standard IPv6 address
prefixes.

Device(config-router)# address-family ipv6
multicast

Step 5

neighbor ipv6-address translate-update ipv6 multicast Generates multiprotocol IPv6 BGP updates that correspond
to unicast IPv6 updates received from a peer.
[unicast]
Example:
Device(config-router)# neighbor 2001:DB8:7000::2
translate-update ipv6 multicast

Resetting IPv6 BGP Sessions
SUMMARY STEPS
1. enable
2. clear bgp ipv6 {unicast | multicast} {* | autonomous-system-number | ip-address | ipv6-address |
peer-group peer-group-name} [soft] [in | out]
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

clear bgp ipv6 {unicast | multicast} {* |
autonomous-system-number | ip-address | ipv6-address |
peer-group peer-group-name} [soft] [in | out]
Example:

IP Routing: BGP Configuration Guide
212

Resets IPv6 BGP sessions.


IPv6 Multicast Address Family Support for Multiprotocol BGP
Clearing External BGP Peers

Command or Action

Purpose

Device# clear bgp ipv6 unicast peer-group marketing
soft out

Clearing External BGP Peers
SUMMARY STEPS
1. enable
2. clear bgp ipv6 {unicast | multicast} external [soft] [in | out]
3. clear bgp ipv6 {unicast | multicast} peer-group name
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

clear bgp ipv6 {unicast | multicast} external [soft] [in | Clears external IPv6 BGP peers.
out]
Example:
Device# clear bgp ipv6 unicast external soft in

Step 3

clear bgp ipv6 {unicast | multicast} peer-group name

Clears all members of an IPv6 BGP peer group.

Example:
Device# clear bgp ipv6 unicast peer-group marketing

Clearing IPv6 BGP Route Dampening Information
SUMMARY STEPS
1. enable
2. clear bgp ipv6 {unicast | multicast} dampening [ipv6-prefix/prefix-length]
DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

IP Routing: BGP Configuration Guide
213


IPv6 Multicast Address Family Support for Multiprotocol BGP
Clearing IPv6 BGP Flap Statistics

Command or Action

Purpose

Device> enable

Step 2

clear bgp ipv6 {unicast | multicast} dampening
[ipv6-prefix/prefix-length]

Clears IPv6 BGP route dampening information and
unsuppresses the suppressed routes.

Example:
Device# clear bgp ipv6 unicast dampening
2001:DB8::/64

Clearing IPv6 BGP Flap Statistics
SUMMARY STEPS
1. enable
2. clear bgp ipv6 {unicast | multicast} flap-statistics [ipv6-prefix/prefix-length | regexp regexp | filter-list
list]
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

clear bgp ipv6 {unicast | multicast} flap-statistics
[ipv6-prefix/prefix-length | regexp regexp | filter-list list]

Clears IPv6 BGP flap statistics.

Example:
Device# clear bgp ipv6 unicast flap-statistics
filter-list 3

Configuration Examples for IPv6 Multicast Address Family
Support for Multiprotocol BGP
Example: Configuring an IPv6 Multiprotocol BGP Peer Group
The following example configures the IPv6 multiprotocol BGP peer group named group1:
router bgp 65000
no bgp default ipv4-unicast
neighbor group1 peer-group
neighbor 2001:DB8:0:CC00::1 remote-as 64600

IP Routing: BGP Configuration Guide
214


IPv6 Multicast Address Family Support for Multiprotocol BGP
Example: Advertising Routes into IPv6 Multiprotocol BGP

address-family ipv6 unicast
neighbor group1 activate
neighbor 2001:DB8:0:CC00::1 peer-group group1

Example: Advertising Routes into IPv6 Multiprotocol BGP
The following example injects the IPv6 network 2001:DB8::/24 into the IPv6 unicast database of the local
device. (BGP checks that a route for the network exists in the IPv6 unicast database of the local device before
advertising the network.)
router bgp 65000
no bgp default ipv4-unicast
address-family ipv6 unicast
network 2001:DB8::/24

Example: Redistributing Prefixes into IPv6 Multiprotocol BGP
The following example redistributes RIP routes into the IPv6 unicast database of the local device:
router bgp 64900
no bgp default ipv4-unicast
address-family ipv6 unicast
redistribute rip

Example: Generating Translate Updates for IPv6 Multicast BGP
The following example shows how to generate IPv6 multicast BGP updates that correspond to unicast IPv6
updates:
router bgp 64900
no bgp default ipv4-unicast
address-family ipv6 multicast
neighbor 2001:DB8:7000::2 translate-update ipv6 multicast

Additional References
Related Documents
Related Topic

Document Title

IPv6 addressing and connectivity

IPv6 Configuration Guide

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

IPv6 commands

Cisco IOS IPv6 Command
Reference

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

IP Routing: BGP Configuration Guide
215


IPv6 Multicast Address Family Support for Multiprotocol BGP
Feature Information for IPv6 Multicast Address Family Support for Multiprotocol BGP

Standards and RFCs
Standard/RFC Title
RFCs for
IPv6

IPv6
RFCs

MIBs
MIB MIBs Link
—

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

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

Feature Information for IPv6 Multicast Address Family Support
for Multiprotocol BGP
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 21: Feature Information for IPv6 Multicast: Address Family Support for Multiprotocol BGP

Feature Name

Releases

Feature Information

IPv6 Multicast: Address Family
Support for Multiprotocol BGP

Cisco IOS XE Release 2.1

This feature provides multicast
BGP extensions for IPv6 and
supports the same features and
functionality as IPv4 BGP.

IP Routing: BGP Configuration Guide
216
