---
title: "PBR Recursive Next Hop"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-pbr-recursive-next-hop
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 5 PBR Recursive Next Hop The PBR Recursive Next Hop feature enhances route maps to enable configuration of a recursive next-hop IP address that is used by policy-based routing (PBR). The recursive next-hop IP address is installed in the routing table and can be a subnet that is not directly connected. If the recursive next-hop IP address is not available, packets are routed using a defau"
---

# PBR Recursive Next Hop

CHAPTER

5

PBR Recursive Next Hop
The PBR Recursive Next Hop feature enhances route maps to enable configuration of a recursive next-hop
IP address that is used by policy-based routing (PBR). The recursive next-hop IP address is installed in the
routing table and can be a subnet that is not directly connected. If the recursive next-hop IP address is not
available, packets are routed using a default route.
Because Cisco Express Forwarding (CEF) or process switching provides the infrastructure, the benefit of this
feature is the CEF loadsharing.
• Finding Feature Information, on page 61
• Restrictions for PBR Recursive Next Hop, on page 61
• Information About PBR Recursive Next-Hop, on page 62
• How to Configure PBR Recursive Next Hop, on page 62
• Configuration Examples for PBR Recursive Next Hop, on page 66
• Additional References for PBR Recursive Next Hop , on page 66
• Feature Information for PBR Recursive Next Hop, on page 67

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Restrictions for PBR Recursive Next Hop
If there are multiple equal-cost routes to the subnet that have been configured by the set next-hop recursive
command, load balancing will occur only if all the adjacencies to the routes are resolved. If any of the
adjacencies have not been resolved, load balancing will not occur and only one of the routes whose adjacency
is resolved will be used. If none of the adjacencies are resolved, then the packets will be processed, resulting
in the resolution of at least one of the adjacencies, leading to the programming of the adjacency in the hardware.
Policy based routing relies on routing protocols or other means to resolve all adjacencies and as a result, load
balancing occurs.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
61


PBR Recursive Next Hop
Information About PBR Recursive Next-Hop

PBR Recursive Next Hope for IPv6 does not support load sharing.

Information About PBR Recursive Next-Hop
PBR Recursive Next Hop Overview
The PBR Recursive Next Hop feature enhances route maps to enable configuration of a recursive next-hop
IP address that is used by policy-based routing (PBR). The recursive next-hop IP address is installed in the
routing table and can be a subnet that is not directly connected. If the recursive next-hop IP address is not
available, packets are routed using a default route.
PBR Recursive Next Hop for IPv6 also supports non-directly connected next hop. The recursive next hop
specified can be a host address or a subnet address. The routing table is looked up to get the next hop based
on the longest match of addresses. Only one such recursive next hop is supported per route map entry.

How to Configure PBR Recursive Next Hop
Setting the Recursive Next-Hop IP Address
The infrastructure provided by CEF or process switching performs the recursion to the next-hop IP address.
The configuration sequence, which affects routing, is as follows:
1. Next-hop
2. Next-hop recursive
3. Interface
4. Default next-hop
5. Default interface
If both a next-hop address and a recursive next-hop IP address are present in the same route-map entry, the
next hop is used. If the next hop is not available, the recursive next hop is used. If the recursive next hop is
not available and no other IP address is present, the packet is routed using the default routing table; it is not
dropped. If the packet is supposed to be dropped, use the set ip next-hopcommand with the recursive keyword,
followed by a set interface null0 configuration.
Perform this task to set the IP address for the recursive next-hop router.
Before you begin
If loadsharing is required, CEF loadsharing should be configured for per-packet or per-destination loadsharing.
Loadbalancing should be done over all equal-cost routes to the subnet that has been configured by the set ip
next-hop recursivecommand.
This functionality should be available in centralized and distributed systems.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
62


PBR Recursive Next Hop
Setting the Recursive Next-Hop IP Address

Note

Only one recursive next-hop IP address is supported per route-map entry.
>

SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
access-list access-list-number {deny | permit} source[source-wildcard] [log]
route-map map-tag
Do one of the following:
• set ip next-hop ip-address
• set ipv6 next-hop ip-address

6. Do one of the following:
• set ip next-hop {ip-address [...ip-address] | recursive ip-address}
• set ipv6 next-hop {ipv6-address [...ipv6-address] | recursive ipv6-address}
7. Do one of the following:
• match ip address access-list-number
• match ipv6 address {prefix-list prefix-list-name |access-list-name}
8. end
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

Enters global configuration mode.

configure terminal
Example:
Router# configure terminal

Step 3

access-list access-list-number {deny | permit}
source[source-wildcard] [log]
Example:

Configures an access list. The example configuration
permits any source IP address that falls within the 10.60.0.0.
0.0.255.255 subnet.

Router(config)# access-list 101 permit 10.60.0.0
0.0.255.255

Step 4

route-map map-tag
Example:

Enables policy routing and enters route-map configuration
mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
63


PBR Recursive Next Hop
Setting the Recursive Next-Hop IP Address

Command or Action

Purpose

Router(config)# route-map abccomp

Step 5

Do one of the following:
• set ip next-hop ip-address
• set ipv6 next-hop ip-address

Sets a next-hop router IPv4 or IPv6 address.
Note

Set this IPv4/IPv6 address separately from the
next-hop recursive router configuration.

Example:
Router(config-route-map)# set ip next-hop 10.10.1.1

Example:
Router(config-route-map)# set ipv6 next-hop
2001:DB8:2003:1::95

Step 6

Do one of the following:

Sets a recursive next-hop IPv4/IPv6 address.

• set ip next-hop {ip-address [...ip-address] | recursive Note
ip-address}
• set ipv6 next-hop {ipv6-address [...ipv6-address] |
recursive ipv6-address}

This configuration does not ensure that packets
get routed using the recursive IP address if an
intermediate IP address is a shorter route to the
destination.

Example:
Router(config-route-map)# set ip next-hop recursive
10.20.3.3

Example:
Router(config-route-map)# set ipv6 next-hop
recursive 2001:DB8:2003:2::95

Step 7

Do one of the following:

Sets an access list to be matched.

• match ip address access-list-number
• match ipv6 address {prefix-list prefix-list-name
|access-list-name}
Example:
Router(config-route-map)# match ip address 101

Example:
Router(config-route-map)# match ipv6 address kmd

Step 8

end
Example:

Exits route-map configuration mode and returns to
privileged EXEC mode.

Router(config-route-map)# end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
64


PBR Recursive Next Hop
Verifying the Recursive Next-Hop Configuration

Verifying the Recursive Next-Hop Configuration
To verify the recursive next-hop configuration, perform the following steps.
SUMMARY STEPS
1. show running-config | begin abccomp
2. show route-map map-name
DETAILED STEPS

Step 1

show running-config | begin abccomp
Use this command to verify the IPv4/IPv6 addresses for a next-hop and recursive next-hop IPv4/IPv6 address as listed
in the following examples:
Example:
Router# show running-config | begin abccomp
route-map abccomp permit 10
match ip address 101 ! Defines the match criteria for an access list.
set ip next-hop recursive 10.3.3.3 ! If the match criteria are met, the recursive IP
set.
set ip next-hop 10.1.1.1 10.2.2.2 10.4.4.4

address is

Router# show running-config | begin abccomp
route-map abccomp permit 10
match ip address kmd! Defines the match criteria for an access list.
set ipv6 next-hop recursive 2001:DB8:3000:1 ! If the match criteria are met, the recursive IPv6
address is set.
set ipv6 next-hop 2001:DB8:3000:1 2001:DB8:4000:1 2001:DB8:5000:1

Step 2

show route-map map-name
Use this command to display the route maps, for example:
Example:
Router# show route-map abccomp
route-map abccomp, permit, sequence 10
Match clauses:
ip address (access-lists): 101
Set clauses:
ip next-hop recursive 10.3.3.3
ip next-hop 10.1.1.1 10.2.2.2 10.4.4.4
Policy routing matches: 0 packets, 0 bytes
Router# show route-map abccomp
route-map abccomp, permit, sequence 10
Match clauses:
ipv6 address (access-lists): kmd
Set clauses:
ipv6 next-hop recursive 2001:DB8:3000:1
ipv6 next-hop 2001:DB8:3000:1 2001:DB8:4000:1 2001:DB8:5000:1
Policy routing matches: 0 packets, 0 bytes

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
65


PBR Recursive Next Hop
Configuration Examples for PBR Recursive Next Hop

Configuration Examples for PBR Recursive Next Hop
Example: Recursive Next-Hop IP Address
The following example shows the configuration of IP address 10.3.3.3 as the recursive next-hop router:
route-map abccomp
set ip next-hop 10.1.1.1
set ip next-hop 10.2.2.2
set ip next-hop recursive 10.3.3.3
set ip next-hop 10.4.4.4

The following example shows the configuration of IPv6 address 2001:DB8:2003:1::95 as the recursive next-hop
router:
route-map abccomp
set ipv6 next-hop 2001:DB8:2003:1::95
set ipv6 next-hop 2001:DB8:2004:3::96
set ipv6 next-hop recursive 2001:DB8:2005:2::95
set ipv6 next-hop 2001:DB8:2006:1::95

Additional References for PBR Recursive Next Hop
Related Documents
Related Topic

Document Title

IP routing protocol-independent commands:
complete command syntax, command mode,
defaults, usage guidelines, and examples

Cisco IOS IP Routing: Protocol-Independent Command
Reference

Performing basic system management

Basic System Management Configuration Guide

Changing the maximum number of paths

"BGP Multipath Load Sharing for Both eBGP and iBGP
in an MPLS-VPN" module in the BGP Configuration
Guide

BGP route map configuration tasks and
configuration examples.

"Connecting to a Service Provider Using External BGP"
module in the BGP Configuration Guide

BGP communities and route maps.

"BGP Cost Community" module in the BGP Configuration
Guide

IPv6 Policy-Based Routing

"IPv6 Policy-Based Routing " module in the IP Routing:
Protocol-Independent Configuration Guide

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
66


PBR Recursive Next Hop
Feature Information for PBR Recursive Next Hop

RFCs
RFC

Title

RFC 791

Internet Protocol

RFC 1219 Variable-Length Subnet Masks
Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including http://www.cisco.com/techsupport
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.
To receive security and technical information about your products, you
can subscribe to various services, such as the Product Alert Tool (accessed
from Field Notices), the Cisco Technical Services Newsletter, and Really
Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com
user ID and password.

Feature Information for PBR Recursive Next Hop
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 6: Feature Information for PBR Recursive Next Hop

Feature Name Releases Feature Information

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
67


PBR Recursive Next Hop
Feature Information for PBR Recursive Next Hop

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
68
