---
title: "Policy-Based Routing"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-policy-based-routing
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 12 Policy-Based Routing The Policy-Based Routing feature is a process whereby a device puts packets through a route map before routing the packets. The route map determines which packets are routed next to which device. Policy-based routing is a more flexible mechanism for routing packets than destination routing. • Finding Feature Information, on page 137 • Prerequisites for Policy-Base"
---

# Policy-Based Routing

CHAPTER

12

Policy-Based Routing
The Policy-Based Routing feature is a process whereby a device puts packets through a route map before
routing the packets. The route map determines which packets are routed next to which device. Policy-based
routing is a more flexible mechanism for routing packets than destination routing.
• Finding Feature Information, on page 137
• Prerequisites for Policy-Based Routing, on page 137
• Information About Policy-Based Routing, on page 137
• How to Configure Policy-Based Routing, on page 139
• Configuration Examples for Policy-Based Routing, on page 141
• Additional References, on page 141
• Feature Information for Policy-Based Routing, on page 142

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Prerequisites for Policy-Based Routing
For Policy-Based Routing, IPBase is a minimum licensing requirement.

Information About Policy-Based Routing
Policy-Based Routing
Policy-based routing (PBR) is a process whereby the device puts packets through a route map before routing
them. The route map determines which packets are routed to which device next. You might enable policy-based

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
137


Policy-Based Routing
Precedence Setting in the IP Header

routing if you want certain packets to be routed some way other than the obvious shortest path. Possible
applications for policy-based routing are to provide equal access, protocol-sensitive routing, source-sensitive
routing, routing based on interactive versus batch traffic, and routing based on dedicated links. Policy-based
routing is a more flexible mechanism for routing packets than destination routing.
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
Table 12: IP Precedence Values

Number Name
0

routine

1

priority

2

immediate

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
138


Policy-Based Routing
Local Policy Routing

Number Name
3

flash

4

flash-override

5

critical

6

internet

7

network

The set commands can be used with each other. They are evaluated in the order shown in the previous table.
A usable next hop implies an interface. Once the local device finds a next hop and a usable interface, it routes
the packet.

Local Policy Routing
Packets that are generated by the device are not normally policy-routed. To enable local policy routing for
such packets, indicate which route map the device should use by using the ip local policy route-map map-tag
global configuration command. All packets originating on the device will then be subject to local policy
routing.

Note

Unlike UDP or other IP traffic, TCP traffic between a Cisco IOS or Cisco IOS-XE device and a remote host
cannot be controlled using a local IP policy, if the Cisco device does not have an entry for the remote host IP
in the Routing Information Base (RIB) (routing table) and Forwarding Information Base (FIB) (for Cisco
Express Forwarding) . It is not necessary that the RIB or FIB entry should be the same path as the one being
set by PBR. In the absence of this entry, TCP does not to detect a valid path to the destination and TCP traffic
fails. However, UDP or ICMP traffic continues to be routed as per the local policy,
Use the show ip local policy command to display the route map used for local policy routing, if one exists.

How to Configure Policy-Based Routing
Configuring Policy-Based Routing
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.

enable
configure terminal
interface type number
ip policy route-map map-tag
exit
route-map map-tag [permit | deny] [sequence-number] [
Enter one or both of the following commands:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
139


Policy-Based Routing
Configuring Policy-Based Routing

• match length
• match ip address
8. end
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

interface type number
Example:

Configures an interface type and enters interface
configuration mode.

Device(config)# interface gigabitethernet 1/0/0

Step 4

ip policy route-map map-tag
Example:

Identifies a route map to use for policy routing on an
interface.

Device(config-if)# ip policy route-map equal-access

Step 5

Returns to global configuration mode.

exit
Example:
Device(config-if)# exit

Step 6

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. .
[
Example:
Device(config)# route-map alpha permit ordering-seq

• map-tag—A meaningful name for the route map.
• permit—(Optional) If the match criteria are met for
this route map, and the permit keyword is specified,
the route is redistributed as controlled by the set
actions. In the case of policy routing, the packet is
policy routed. If the match criteria are not met, and the
permit keyword is specified, the next route map with
the same map tag is tested. If a route passes none of
the match criteria for the set of route maps sharing the
same name, it is not redistributed by that set.
• deny—(Optional) If the match criteria are met for the
route map and the deny keyword is specified, the route
is not redistributed. In the case of policy routing, the

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
140


Policy-Based Routing
Configuration Examples for Policy-Based Routing

Command or Action

Purpose
packet is not policy routed, and no further route maps
sharing the same map tag name will be examined. If
the packet is not policy routed, the normal forwarding
algorithm is used.
• sequence-number—(Optional) Number that indicates
the position a new route map will have in the list of
route maps already configured with the same name. If
used with the no form of this command, the position
of the route map configure terminal should be deleted.

Step 7

Enter one or both of the following commands:
• match length
• match ip address

Define the criteria by which packets are examined to learn
if they will be policy-based routed.

Example:
Device(config-route-map)# match ip address 1

Step 8

Exits route-map configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-route-map)# end

Configuration Examples for Policy-Based Routing
Additional References
Related Documents
Related Topic

Document Title

IP routing protocol-independent commands Cisco IOS IP Routing: Protocol-Independent Command
Reference

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
141


Policy-Based Routing
Feature Information for Policy-Based Routing

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

Feature Information for Policy-Based Routing
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 13: Feature Information for Policy-Based Routing

Feature Name

Releases

Policy-Based Routing

Feature Information
The Policy-Based Routing feature
is a process whereby a device puts
packets through a route map before
routing the packets. The route map
determines which packets are
routed next to which device.
Policy-Based Routing introduces a
more flexible mechanism for
routing packets than destination
routing.
The following command was
introduced or modified: ip policy
route-map.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
142
