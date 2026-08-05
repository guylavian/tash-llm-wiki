---
title: "IPv6 Policy-Based Routing"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-ipv6-policy-based-routing
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 8 IPv6 Policy-Based Routing Policy-based routing (PBR) in both IPv6 and IPv4 allows a user to manually configure how received packets should be routed. PBR allows the user to identify packets by using several attributes and to specify the next hop or the output interface to which the packet should be sent. PBR also provides a basic packet-marking capability. • Finding Feature Information"
---

# IPv6 Policy-Based Routing

CHAPTER

8

IPv6 Policy-Based Routing
Policy-based routing (PBR) in both IPv6 and IPv4 allows a user to manually configure how received packets
should be routed. PBR allows the user to identify packets by using several attributes and to specify the next
hop or the output interface to which the packet should be sent. PBR also provides a basic packet-marking
capability.
• Finding Feature Information, on page 87
• Information About IPv6 Policy-Based Routing, on page 87
• How to Enable IPv6 Policy-Based Routing, on page 90
• Configuration Examples for IPv6 Policy-Based Routing, on page 94
• Additional References for IPv6 Policy-Based Routing, on page 95
• Feature Information for IPv6 Policy-Based Routing, on page 96

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Information About IPv6 Policy-Based Routing
Policy-Based Routing Overview
Policy-based routing (PBR) gives you a flexible means of routing packets by allowing you to configure a
defined policy for traffic flows, which lessens reliance on routes derived from routing protocols. Therefore,
PBR gives you more control over routing by extending and complementing the existing mechanisms provided
by routing protocols. PBR allows you to set the IPv6 precedence. For a simple policy, you can use any one
of these tasks; for a complex policy, you can use all of them. It also allows you to specify a path for certain
traffic, such as priority traffic over a high-cost link. IPv6 PBR is supported on Cisco ASR 1000 Series platform.
PBR for IPv6 may be applied to both forwarded and originated IPv6 packets. For forwarded packets, PBR
for IPv6 will be implemented as an IPv6 input interface feature, supported in the following forwarding paths:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
87


IPv6 Policy-Based Routing
How Policy-Based Routing Works

• Process
• Cisco Express Forwarding (formerly known as CEF)
• Distributed Cisco Express Forwarding
Policies can be based on the IPv6 address, port numbers, protocols, or packet size.
PBR allows you to perform the following tasks:
• Classify traffic based on extended access list criteria. Access lists, then, establish the match criteria.
• Set IPv6 precedence bits, giving the network the ability to enable differentiated classes of service.
• Route packets to specific traffic-engineered paths; you might need to route them to allow a specific
quality of service (QoS) through the network.
PBR allows you to classify and mark packets at the edge of the network. PBR marks a packet by setting
precedence value. The precedence value can be used directly by devices in the network core to apply the
appropriate QoS to a packet, which keeps packet classification at your network edge.

How Policy-Based Routing Works
All packets received on an interface with policy-based routing (PBR) enabled are passed through enhanced
packet filters called route maps. The route maps used by PBR dictate the policy, determining where to forward
packets.
Route maps are composed of statements. The route map statements can be marked as permit or deny, and they
are interpreted in the following ways:
• If a packet matches all match statements for a route map that is marked as permit, the device attempts
to policy route the packet using the set statements. Otherwise, the packet is forwarded normally.
• If the packet matches any match statements for a route map that is marked as deny, the packet is not
subject to PBR and is forwarded normally.
• If the statement is marked as permit and the packets do not match any route map statements, the packets
are sent back through normal forwarding channels and destination-based routing is performed.
You must configure policy-based routing (PBR) on the interface that receives the packet, and not on the
interface from which the packet is sent.

Packet Matching
Policy-based routing (PBR) for IPv6 will match packets using the match ipv6 address command in the
associated PBR route map. Packet match criteria are those criteria supported by IPv6 access lists, as follows:
• Input interface
• Source IPv6 address (standard or extended access control list [ACL])
• Destination IPv6 address (standard or extended ACL)
• Protocol (extended ACL)
• Source port and destination port (extended ACL)

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
88


IPv6 Policy-Based Routing
Packet Forwarding Using Set Statements

• DSCP (extended ACL)
• Flow-label (extended ACL)
• Fragment (extended ACL)
Packets may also be matched by length using the match length command in the PBR route map.
Match statements are evaluated first by the criteria specified in the match ipv6 address command and then
by the criteria specified in the match length command. Therefore, if both an ACL and a length statement are
used, a packet will first be subject to an ACL match. Only packets that pass the ACL match will be subject
to the length match. Finally, only packets that pass both the ACL and the length statement will be policy
routed.

Packet Forwarding Using Set Statements
Policy-based routing (PBR) for IPv6 packet forwarding is controlled by using a number of set statements in
the PBR route map. These set statements are evaluated individually in the order shown, and PBR will attempt
to forward the packet using each of the set statements in turn. PBR evaluates each set statement individually,
without reference to any prior or subsequent set statement.
You may set multiple forwarding statements in the PBR for IPv6 route map. The following set statements
may be specified:
• IPv6 next hop. The next hop to which the packet should be sent. The next hop must be present in the
Routing Information Base (RIB), it must be directly connected, and it must be a global IPv6 address. If
the next hop is invalid, the set statement is ignored.
• Output interface. A packet is forwarded out of a specified interface. An entry for the packet destination
address must exist in the IPv6 RIB, and the specified output interface must be in the set path. If the
interface is invalid, the statement is ignored.
• Default IPv6 next hop. The next hop to which the packet should be sent. It must be a global IPv6 address.
This set statement is used only when there is no explicit entry for the packet destination in the IPv6 RIB.
• Default output interface. The packet is forwarded out of a specified interface. This set statement is used
only when there is no explicit entry for the packet destination in the IPv6 RIB.

Note

The order in which PBR evaluates the set statements is the order in which they are listed above. This order
may differ from the order in which route-map set statements are listed by show commands.

When to Use Policy-Based Routing
Policy-based routing (PBR) can be used if you want certain packets to be routed some way other than the
obvious shortest path. For example, PBR can be used to provide the following functionality:
• Equal access
• Protocol-sensitive routing
• Source-sensitive routing
• Routing based on interactive traffic versus batch traffic

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
89


IPv6 Policy-Based Routing
How to Enable IPv6 Policy-Based Routing

• Routing based on dedicated links
Some applications or traffic can benefit from Quality of Service (QoS)-specific routing; for example, you
could transfer stock records to a corporate office on a higher-bandwidth, higher-cost link for a short time
while sending routine application data such as e-mail over a lower-bandwidth, lower-cost link.

How to Enable IPv6 Policy-Based Routing
Enabling IPv6 PBR on an Interface
To enable Policy-Based Routing (PBR) for IPv6, you must create a route map that specifies the packet match
criteria and desired policy-route action. Then you associate the route map on the required interface. All packets
arriving on the specified interface that match the match clauses will be subject to PBR.
In PBR, the set vrf command decouples the virtual routing and forwarding (VRF) instance and interface
association and allows the selection of a VRF based on access control list (ACL)-based classification using
existing PBR or route-map configurations. It provides a single router with multiple routing tables and the
ability to select routes based on ACL classification. The router classifies packets based on ACL, selects a
routing table, looks up the destination address, and then routes the packet.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
route-map map-tag [permit | deny] [sequence-number] [
Do one of the following:
• match length minimum-length maximum-length
• match ipv6 address {prefix-list prefix-list-name | access-list-name}

5. Do one of the following:
• set ipv6 precedence precedence-value
• set ipv6 next-hop global-ipv6-address [global-ipv6-address...]
• set interface type number [...type number]
• set ipv6 default next-hop global-ipv6-address [global-ipv6-address...]
• set default interface type number [...type number]
• set vrf vrf-name
6.
7.
8.
9.

exit
interface type number
ipv6 policy route-map route-map-name
end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
90


IPv6 Policy-Based Routing
Enabling IPv6 PBR on an Interface

Command or Action

Purpose

Example:

• Enter your password if prompted.

Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. .
[
Example:
Device(config)# route-map alpha permit ordering-seq

Step 4

Do one of the following:

Specifies the match criteria.

• match length minimum-length maximum-length
• match ipv6 address {prefix-list prefix-list-name |
access-list-name}
Example:

• You can specify any or all of the following:
• Matches the Level 3 length of the packet.
• Matches a specified IPv6 access list.
• If you do not specify a match command, the route
map applies to all packets.

Device(config-route-map)# match length 3 200

Example:
Device(config-route-map)# match ipv6 address
marketing

Step 5

Do one of the following:
• set ipv6 precedence precedence-value
• set ipv6 next-hop global-ipv6-address
[global-ipv6-address...]
• set interface type number [...type number]
• set ipv6 default next-hop global-ipv6-address
[global-ipv6-address...]
• set default interface type number [...type number]
• set vrf vrf-name
Example:
Device(config-route-map)# set ipv6 precedence 1

Example:

Specifies the action or actions to take on the packets that
match the criteria.
• You can specify any or all of the following:
• Sets precedence value in the IPv6 header.
• Sets next hop to which to route the packet (the
next hop must be adjacent).
• Sets output interface for the packet.
• Sets next hop to which to route the packet, if there
is no explicit route for this destination.
• Sets output interface for the packet, if there is no
explicit route for this destination.
• Sets VRF instance selection within a route map
for a policy-based routing VRF selection.

Device(config-route-map)# set ipv6 next-hop
2001:DB8:2003:1::95

Example:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
91


IPv6 Policy-Based Routing
Enabling Local PBR for IPv6

Command or Action

Purpose

Device(config-route-map)# set interface
GigabitEthernet 0/0/1

Example:
Device(config-route-map)# set ipv6 default next-hop
2001:DB8:2003:1::95

Example:
Device(config-route-map)# set default interface
GigabitEthernet 0/0/0

Example:
Device(config-route-map)# set vrf vrfname

Step 6

Exits route-map configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-route-map)# exit

Step 7

interface type number
Example:

Specifies an interface type and number, and places the router
in interface configuration mode.

Device(config)# interface FastEthernet 1/0

Step 8

ipv6 policy route-map route-map-name

Identifies a route map to use for IPv6 PBR on an interface.

Example:
Device(config-if)# ipv6 policy-route-map
interactive

Step 9

Exits interface configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-if)# end

Enabling Local PBR for IPv6
Packets that are generated by the device are not normally policy routed. Perform this task to enable local IPv6
policy-based routing (PBR) for such packets, indicating which route map the device should use.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
ipv6 local policy route-map route-map-name
end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
92


IPv6 Policy-Based Routing
Verifying the Configuration and Operation of PBR for IPv6

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

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

ipv6 local policy route-map route-map-name

Configures IPv6 PBR for packets generated by the device.

Example:
Device(config)# ipv6 local policy route-map
pbr-src-90

Step 4

Returns to privileged EXEC mode.

end
Example:
Device(config)# end

Verifying the Configuration and Operation of PBR for IPv6
SUMMARY STEPS
1. enable
2. show ipv6 policy
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

show ipv6 policy

Displays IPv6 policy routing packet activity.

Example:
Device# show ipv6 policy

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
93


IPv6 Policy-Based Routing
Troubleshooting PBR for IPv6

Troubleshooting PBR for IPv6
Policy routing analyzes various parts of the packet and then routes the packet based on certain user-defined
attributes in the packet.
SUMMARY STEPS
1. enable
2. show route-map [map-name | dynamic [dynamic-map-name | application [application-name]] | all]
[detailed]
3. debug ipv6 policy [access-list-name]
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

show route-map [map-name | dynamic
[dynamic-map-name | application [application-name]] |
all] [detailed]

Displays all route maps configured or only the one specified.

Example:
Device# show route-map

Step 3

debug ipv6 policy [access-list-name]
Example:

Enables debugging of the IPv6 policy routing packet
activity.

Device# debug ipv6 policy

Configuration Examples for IPv6 Policy-Based Routing
Example: Enabling PBR on an Interface
In the following example, a route map named pbr-dest-1 is created and configured, specifying packet match
criteria and desired policy-route action. PBR is then enabled on GigabitEthernet interface 0/0/1.
ipv6 access-list match-dest-1
permit ipv6 any 2001:DB8:2001:1760::/32
route-map pbr-dest-1 permit 10
match ipv6 address match-dest-1
set interface GigabitEthernet 0/0/0
interface GigabitEthernet0/0/1
ipv6 policy-route-map interactive

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
94


IPv6 Policy-Based Routing
Example: Enabling Local PBR for IPv6

Example: Enabling Local PBR for IPv6
In the following example, packets with a destination IPv6 address that match the IPv6 address range allowed
by access list pbr-src-90 are sent to the device at IPv6 address 2001:DB8:2003:1::95:
ipv6 access-list src-90
permit ipv6 host 2001:DB8:2003::90 2001:DB8:2001:1000::/64
route-map pbr-src-90 permit 10
match ipv6 address src-90
set ipv6 next-hop 2001:DB8:2003:1::95
ipv6 local policy route-map pbr-src-90

Example: show ipv6 policy Command Output
The show ipv6 policy command displays PBR configuration, as shown in the following example:
Device# show ipv6 policy
Interface
GigabitEthernet0/0/0

Routemap
src-1

Example: Verifying Route-Map Information
The following sample output from the show route-map command displays specific route-map
information, such as a count of policy matches:
Device# show

route-map

route-map bill, permit, sequence 10
Match clauses:
Set clauses:
Policy routing matches:0 packets, 0 bytes

Additional References for IPv6 Policy-Based Routing
Related Documents
Related Topic

Document Title

IP Routing Protocol-Independent commands: complete
Cisco IOS IP Routing: Protocol-Independent
command syntax, command mode, command history, defaults, Command Reference
usage guidelines, and examples

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
95


IPv6 Policy-Based Routing
Feature Information for IPv6 Policy-Based Routing

MIBs
MIBs

MIBs Link

No new or modified MIBs are supported by this To locate and download MIBs for selected platforms, Cisco
feature, and support for existing MIBs has not software releases, and feature sets, use Cisco MIB Locator
been modified by this feature.
found at the following URL:
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

Feature Information for IPv6 Policy-Based Routing
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
96


IPv6 Policy-Based Routing
Feature Information for IPv6 Policy-Based Routing

Table 8: Feature Information for IPv6 Policy-Based Routing

Feature Name

Releases

IPv6 Policy-Based Routing

Feature Information
Policy-based routing for IPv6
allows a user to manually configure
how received packets should be
routed.
The following commands were
introduced or modified: debug fm
ipv6 pbr, debug ipv6 policy, ipv6
local policy route-map, ipv6
policy route-map, match ipv6
address, match length,
route-map, set default interface,
set interface, set ipv6 default
next-hop, set ipv6 next-hop
(PBR), set ipv6 precedence, set
vrf, show fm ipv6 pbr all, show
fm ipv6 pbr interface, show ipv6
policy, and show route-map.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
97


IPv6 Policy-Based Routing
Feature Information for IPv6 Policy-Based Routing

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
98
