---
title: "Policy-Based Routing Default Next-Hop Routes"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-policy-based-routing-default-next-hop-routes
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 15 Policy-Based Routing Default Next-Hop Routes The Policy-Based Routing Default Next-Hop Route feature introduces the ability for packets that are forwarded as a result of the set ip default next-hop command to be switched at the hardware level. In prior software releases, the packets to be forwarded that are generated from the route map for policy-based routing are switched at the soft"
---

# Policy-Based Routing Default Next-Hop Routes

CHAPTER

15

Policy-Based Routing Default Next-Hop Routes
The Policy-Based Routing Default Next-Hop Route feature introduces the ability for packets that are forwarded
as a result of the set ip default next-hop command to be switched at the hardware level. In prior software
releases, the packets to be forwarded that are generated from the route map for policy-based routing are
switched at the software level.
• Finding Feature Information, on page 157
• Information About Policy-Based Routing Default Next-Hop Routes, on page 157
• How to Configure Policy-Based Routing Default Next-Hop Routes, on page 159
• Configuration Examples for Policy-Based Routing Default Next-Hop Routes, on page 161
• Additional References, on page 161
• Feature Information for Policy-Based Routing Default Next-Hop Routes, on page 162

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Information About Policy-Based Routing Default Next-Hop
Routes
Policy-Based Routing
Policy-based routing (PBR) is a process whereby the device puts packets through a route map before routing
them. The route map determines which packets are routed to which device next. You might enable policy-based
routing if you want certain packets to be routed some way other than the obvious shortest path. Possible
applications for policy-based routing are to provide equal access, protocol-sensitive routing, source-sensitive
routing, routing based on interactive versus batch traffic, and routing based on dedicated links. Policy-based
routing is a more flexible mechanism for routing packets than destination routing.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
157


Policy-Based Routing Default Next-Hop Routes
Precedence Setting in the IP Header

To enable policy-based routing, you must identify which route map to use for policy-based routing and create
the route map. The route map itself specifies the match criteria and the resulting action if all of the match
clauses are met.
To enable policy-based routing on an interface, indicate which route map the device should use by using the
ip policy route-map map-tag command in interface configuration mode. A packet arriving on the specified
interface is subject to policy-based routing. This ip policy route-map command disables fast switching of
all packets arriving on this interface.
To define the route map to be used for policy-based routing, use the route-map map-tag [permit | deny]
[sequence-number] [ordering-seq] [sequence-name global configuration command.
To define the criteria by which packets are examined to learn if they will be policy-based routed, use either
the match length minimum-length maximum-length command or the match ip address {access-list-number
| access-list-name} [access-list-number | access-list-name] command or both in route map configuration mode.
No match clause in the route map indicates all packets.
To display the cache entries in the policy route cache, use the show ip cache policy command.

Note

Mediatrace will show statistics of incorrect interfaces with policy-based routing (PBR) if the PBR does not
interact with CEF or Resource Reservation Protocol (RSVP). Hence configure PBR to interact with CEF or
RSVP directly so that mediatrace collects statistics only on tunnel interfaces and not physical interfaces.

Precedence Setting in the IP Header
The precedence setting in the IP header determines whether, during times of high traffic, the packets are
treated with more or less precedence than other packets. By default, the Cisco software leaves this value
untouched; the header remains with the precedence value that it had.
The precedence bits in the IP header can be set in the device when policy-based routing is enabled. When the
packets containing those headers arrive at another device, the packets are ordered for transmission according
to the precedence set, if the queueing feature is enabled. The device does not honor the precedence bits if
queueing is not enabled; the packets are sent in FIFO order.
You can change the precedence setting, using either a number or name (the names came from RFC 791). You
can enable other features that use the values in the set ip precedence route map configuration command to
determine precedence. The table below lists the possible numbers and their corresponding name, from lowest
to highest precedence.
Table 16: IP Precedence Values

Number Name
0

routine

1

priority

2

immediate

3

flash

4

flash-override

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
158


Policy-Based Routing Default Next-Hop Routes
How to Configure Policy-Based Routing Default Next-Hop Routes

Number Name
5

critical

6

internet

7

network

The set commands can be used with each other. They are evaluated in the order shown in the previous table.
A usable next hop implies an interface. Once the local device finds a next hop and a usable interface, it routes
the packet.

How to Configure Policy-Based Routing Default Next-Hop
Routes
Configuring Precedence for Policy-Based Routing Default Next-Hop Routes
Perform this task to configure the precedence of packets and specify where packets that pass the match criteria
are output.

Note

The set ip next-hop and set ip default next-hop commands are similar but have a different order of operation.
Configuring the set ip next-hop command causes the system to first use policy routing and then use the routing
table. Configuring the set ip default next-hop command causes the system to first use the routing table and
then the policy-route-specified next hop.

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
route-map map-tag [permit | deny] [sequence-number] [
set ip precedence {number | name}
set ip next-hop ip-address [ip-address]
set interface type number [...type number]
set ip default next-hop ip-address [ip-address]
set default interface type number [...type number]
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

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
159


Policy-Based Routing Default Next-Hop Routes
Configuring Precedence for Policy-Based Routing Default Next-Hop Routes

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed.
[
Example:
Device(config)# route-map alpha permit ordering-seq

Step 4

set ip precedence {number | name}

Sets the precedence value in the IP header.

Example:

Note

You can specify either a precedence number or
a precedence name.

Device(config-route-map)# set ip precedence 5

Step 5

set ip next-hop ip-address [ip-address]

Specifies the next hop for routing packets.

Example:

Note

The next hop must be an adjacent device.

Device(config-route-map)# set ip next-hop 192.0.2.1

Step 6

set interface type number [...type number]

Specifies the output interface for the packet.

Example:
Device(config-route-map)# set interface
gigabitethernet 0/0/0

Step 7

set ip default next-hop ip-address [ip-address]
Example:

Specifies the next hop for routing packets if there is no
explicit route for this destination.
Note

Device(config-route-map)# set ip default next-hop
172.16.6.6

Step 8

set default interface type number [...type number]
Example:

Like the set ip next-hop command, the set ip
default next-hop command must specify an
adjacent device.

Specifies the output interface for the packet if there is no
explicit route for the destination.

Device(config-route-map)# set default interface
serial 0/0/0

Step 9

end
Example:

Exits route-map configuration mode and returns to
privileged EXEC mode.

Device(config-route-map)# end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
160


Policy-Based Routing Default Next-Hop Routes
Configuration Examples for Policy-Based Routing Default Next-Hop Routes

Configuration Examples for Policy-Based Routing Default
Next-Hop Routes
Example: Policy-Based Routing
The following example provides two sources with equal access to two different service providers. Packets
that arrive on asynchronous interface 1/0/0 from the source 10.1.1.1 are sent to the device at 172.16.6.6 if the
device has no explicit route for the destination of the packet. Packets that arrive from the source 172.17.2.2
are sent to the device at 192.168.7.7 if the device has no explicit route for the destination of the packet. All
other packets for which the device has no explicit route to the destination are discarded.
Device(config)# access-list 1 permit ip 10.1.1.1
Device(config)# access-list 2 permit ip 172.17.2.2
Device(config)# interface async 1/0/0
Device(config-if)# ip policy route-map equal-access
Device(config-if)# exit
Device(config)# route-map equal-access permit 10
Device(config-route-map)# match ip address 1
Device(config-route-map)# set ip default next-hop 172.16.6.6
Device(config-route-map)# exit
Device(config)# route-map equal-access permit 20
Device(config-route-map)# match ip address 2
Device(config-route-map)# set ip default next-hop 192.168.7.7
Device(config-route-map)# exit
Device(config)# route-map equal-access permit 30
Device(config-route-map)# set default interface null 0
Device(config-route-map)# exit

Additional References
Related Documents
Related Topic

Document Title

IP routing protocol-independent commands Cisco IOS IP Routing: Protocol-Independent Command
Reference
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

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
161


Policy-Based Routing Default Next-Hop Routes
Feature Information for Policy-Based Routing Default Next-Hop Routes

Feature Information for Policy-Based Routing Default Next-Hop
Routes
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 17: Feature Information for Policy-Based Routing Default Next-Hop Routes

Feature Name

Releases

Feature Information

Policy-Based Routing Default
Next-Hop Routes

12.1(11)E

The Policy-Based Routing Default
Next-Hop Route feature introduces
the ability for packets that are
forwarded as a result of the set ip
default next-hop command to be
switched at the hardware level. In
prior releases, the packets to be
forwarded that were generated from
the route map for policy-based
routing were switched at the
software level.

Cisco IOS XE Release 2.2

The following command was
introduced or modified: set ip
default next-hop.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
162
