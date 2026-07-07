---
title: "BGP Flow Specification Client"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-flow-specification-client
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 25 BGP Flow Specification Client The Border Gateway Protocol (BGP) flow specification client feature enables a device to perform the role of a BGP flow specification client and receive flow specification rules from a BGP flow specification controller. Flow specification rules contain a set of match criteria and actions (also called flows). The flows are configured on a controller (device"
---

# BGP Flow Specification Client

CHAPTER

25

BGP Flow Specification Client
The Border Gateway Protocol (BGP) flow specification client feature enables a device to perform the role of
a BGP flow specification client and receive flow specification rules from a BGP flow specification controller.
Flow specification rules contain a set of match criteria and actions (also called flows). The flows are configured
on a controller (device), which advertises the flows to the client device, or specific interfaces on the client.

Attention

IOS XE software supports BGP flow specification client function and does not support BGP flow specification
controller function.
• Finding Feature Information, on page 491
• Prerequisites for BGP Flow Specification Client, on page 491
• Restrictions for BGP Flow Specification Client, on page 492
• Information About BGP Flow Specification Client, on page 492
• How to Configure BGP Flow Specification Client, on page 494
• Configuration Examples for BGP Flow Specification Client, on page 499
• Additional References for BGP Flow Specification Client, on page 500
• Feature Information for BGP Flow Specification Client, on page 501

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP Flow Specification Client
• Identify and configure flow specification rules on the controller.

IP Routing: BGP Configuration Guide
491


BGP Flow Specification Client
Restrictions for BGP Flow Specification Client

Note

When the flow specification client is enabled, the matching criteria and
corresponding actions in the controller’s flows are remotely injected into the
client device, and the flows are programmed into the platform hardware of the
client device.

Restrictions for BGP Flow Specification Client
• In Cisco IOS 15.5(S) release, BGP flow specification is supported only on a BGP flow specification
client and route reflector.
• Mixing of address family matches and actions is not supported in flow specification rules. For example,
IPv4 matches cannot be combined with IPv6 actions and vice versa.

Information About BGP Flow Specification Client
BGP Flow Specification Model
The BGP protocol is used for flow specifications due to unique advantages it offers. The three elements that
are used to route flow specifications through BGP enabled devices are: controller, client, and route-reflector
(which is optional). This document is specific to the client element function.
Though devices with the IOS XE software (such as ASR 1000, and so on) can perform BGP flow specification
client role and not the controller role, a brief outline of the BGP flow specification process is given below for
better understanding.
The BGP flow specification functionality allows you to rapidly deploy and propagate filtering and policing
functionality among a large number of BGP peer devices to mitigate the effects of a distributed denial-of-service
(DDoS) attack over your network.
The BGP flow specification model comprises of a client and a controller (route-reflector usage is optional).
The controller is responsible for sending or injecting the flow specification NRLI entry. The client (acting as
a BGP speaker) receives the NRLI and programs the hardware forwarding to act on the instruction from the
controller. An illustration of this model is provided below.

IP Routing: BGP Configuration Guide
492


BGP Flow Specification Client
Sample Flow Specification Client Configuration

Figure 43: BGP Flow Specification Model

In the above topology, the controller on the left-hand side injects the flow specification NRLI into the client
on the right-hand side. The client receives the information, sends it to the flow specification manager component,
configures the ePBR (Enhanced Policy Based Routing) infrastructure, which in turn programs the platform
hardware of the device. This way, you can create rules to handle DDoS attacks on your network.

Sample Flow Specification Client Configuration
First, associate the device to a BGP autonomous system and enable flow specification policy mapping capability
for various address families. Then, identify a neighbor (through its IP address) as a BGP peer and enable the
capability to exchange information between the devices through theneighbor activate command. This way,
flow specification information can be exchanged between the client, controller, and any other flow specification
client device.
!
router bgp 100
address-family ipv4 flowspec
neighbor 10.1.1.1 activate
!

Matching Criteria and Actions
The flow specification NLRI type consists of several optional sub-components. A specific packet is considered
to match the flow specification when it matches the intersection (AND) of all the components present in the
specification. The following are the supported component types or tuples that you can define:
BGP Flowspec NLRI Type QoS Matching Field (IPv6) QoS Matching Field (IPv4) Input Value
Type 1

IPv6 destination address

IPv4 destination address

Prefix length

Type 2

IPv6 source address

IPv4 source address

Prefix length

Type 3

IPv6 next header

IPv4 protocol

Multi-value range

IP Routing: BGP Configuration Guide
493


BGP Flow Specification Client
How to Configure BGP Flow Specification Client

BGP Flowspec NLRI Type QoS Matching Field (IPv6) QoS Matching Field (IPv4) Input Value
Type 4

IPv6 source or destination IPv4 source or destination Multi-value range
port
port

Type 5

IPv6 destination port

IPv4 destination port

Multi-value range

Type 6

IPv6 source port

IPv4 source port

Multi-value range

Type 7

IPv6 ICMP type

IPv4 ICMP type

Multi-value range

Type 8

IPv6 ICMP code

IPv4 ICMP code

Multi-value range

Type 9

IPv6 TCP flags

IPv4 TCP flags (2 bytes
include reserved bits)

Bit mask

Type 10

IPv6 packet length

IPv4 packet length

Multi-value range

Type 11

IPv6 traffic class

IPv4 DSCP

Multi-value range

Type 12

Reserved

IPv4 fragment bits

Bit mask

How to Configure BGP Flow Specification Client
Configuring a Device As a Flow Specification Client and Establishing a BGP
Peer Relationship With Neighbor
The following task explains configuration of a device as a BGP flow specification client. A device interface
within a VRF instance can also perform the role of a BGP flow specification client.
Before you begin
Before configuring a device as a flow specification client, it is a good practice to identify and configure the
flow specification controller device (and a route reflector, if required). When flow specification rules are
configured on the controller, the rules are remotely injected into the client and the matching criteria and
corresponding actions are programmed into the platform hardware of the client.
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
router bgp as-number
address-family {ipv4 | ipv6} flowspec
neighbor ip-address activate
exit
address-family {ipv4 | ipv6} flowspec vrf vrf-name
neighbor ip-address remote-as as-number
neighbor ip-address activate

IP Routing: BGP Configuration Guide
494


BGP Flow Specification Client
Configuring a Device As a Flow Specification Client and Establishing a BGP Peer Relationship With Neighbor

10.

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

Enters global configuration mode

Example:
Device# configure terminal

Step 3

router bgp as-number
Example:

Specifies the autonomous system number and enters the
BGP configuration mode, allowing you to configure the
BGP routing process.

Device(config)# router bgp 100

Step 4

address-family {ipv4 | ipv6} flowspec

Step 5

neighbor ip-address activate

Step 6

exit

Specifies either the IPv4 or IPv6 address family and enters
BGP address family configuration mode, and initializes
Example:
the global address family for flow specification policy
Device(config-bgp)# address-family ipv4 flowspec mapping.
Places the device in neighbor configuration mode for BGP
routing and configures the neighbor IP address as a BGP
Example:
peer. Enables the device to advertise (and receive
Device(config-bgp-af)# neighbor 10.1.1.1 activate information), including its IP address, to its BGP neighbor.

Example:

Exits BGP address family configuration mode and enters
BGP configuration mode.

Device(config-bgp-af)# exit

Step 7

address-family {ipv4 | ipv6} flowspec vrf vrf-name

Specifies either the IPv4 or IPv6 address family for the
VRF, enters BGP address family configuration mode, and
Example:
initializes the global address family for flow specification
Device(config-bgp)# address-family ipv4 flowspec policy mapping.
vrf vrf1

Step 8

neighbor ip-address remote-as as-number
Example:
Device(config-bgp-af)# neighbor 2001:DB8:1::1
remote-as 100

Step 9

neighbor ip-address activate
Example:

Places the device in neighbor configuration mode for BGP
routing and configures the neighbor (IP address) as a BGP
peer. The remote-as keyword assigns the specified remote
autonomous system number to the neighbor.
Enables the device to advertise (and receive information),
including its IP address, to its BGP neighbor.

Device(config-bgp-af)# neighbor 2001:DB8:1::1
activate

Step 10

exit
Example:

Exits BGP address family configuration mode and enters
BGP configuration mode.

IP Routing: BGP Configuration Guide
495


BGP Flow Specification Client
Configuring a Flow Specification Policy On All Interfaces Of a Device

Command or Action

Purpose

Device(config-bgp-af)# exit

Configuring a Flow Specification Policy On All Interfaces Of a Device
The following configuration task explains flow specification policy configuration on all interfaces of a device
for the IPv4 and IPv6 address families, and on interfaces within a VRF instance.
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

enable
configure terminal
flowspec
address-family ipv4
local-install interface-all
exit
address-family ipv6
local-install interface-all
exit
vrf vrf-name
address-family ipv4
local-install interface-all
exit
address-family ipv6
local-install interface-all
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

Enters global configuration mode

Example:
Device# configure terminal

Step 3

flowspec

Enters flowspec configuration mode.

Example:
Device(config)# flowspec

Step 4

address-family ipv4
Example:
Device(config-flowspec)# address-family ipv4

IP Routing: BGP Configuration Guide
496

Specifies the IPv4 address family and enters flow
specification address family configuration mode.


BGP Flow Specification Client
Configuring a Flow Specification Policy On All Interfaces Of a Device

Step 5

Command or Action

Purpose

local-install interface-all

Installs the flowspec policy on all interfaces.

Example:
Device(config-flowspec-af)# local-install
interface-all

Step 6

exit
Example:

Exits flow specification address family configuration mode
and enters flowspec configuration mode.

Device(config-flowspec-af)# exit

Step 7

address-family ipv6
Example:

Specifies the IPv6 address family and enters flow
specification address family configuration mode.

Device(config-flowspec)# address-family ipv6

Step 8

local-install interface-all

Installs the flowspec policy on all interfaces.

Example:
Device(config-flowspec-af)# local-install
interface-all

Step 9

exit
Example:

Exits flow specification address family configuration mode
and enters flowspec configuration mode.

Device(config-flowspec-af)# exit

Step 10

vrf vrf-name
Example:

Configures a VRF instance and enters flow specification
VRF configuration mode.

Device(config-flowspec)# vrf vrf10

Step 11

address-family ipv4
Example:

Specifies the IPv4 address family and enters VRF flow
specification address family configuration mode.

Device(config-flowspec-vrf)# address-family ipv4

Step 12

local-install interface-all

Installs the flowspec policy on all interfaces.

Example:
Device(config-flowspec-vrf-af)# local-install
interface-all

Step 13

exit
Example:

Exits VRF flow specification address family configuration
mode and enters VRF flow specification configuration
mode.

Device(config-flowspec-vrf-af)# exit

Step 14

address-family ipv6
Example:

Specifies the IPv6 address family and enters VRF flow
specification address family configuration mode.

Device(config-flowspec-vrf)# address-family ipv6

IP Routing: BGP Configuration Guide
497


BGP Flow Specification Client
Verifying BGP Flow Specification Client

Step 15

Command or Action

Purpose

local-install interface-all

Installs the flowspec policy on all interfaces.

Example:
Device(config-flowspec-vrf-af)# local-install
interface-all

Step 16

exit
Example:

Exits VRF flow specification address family configuration
mode and enters VRF flow specification configuration
mode.

Device(config-flowspec-vrf-af)# exit

Verifying BGP Flow Specification Client
These commands display flow specification configuration details:
SUMMARY STEPS
1. show flowspec summary
2. show bgp ipv4 flowspec
3. show flowspec vrf vrf-name afi-all
DETAILED STEPS

Step 1

show flowspec summary
Example:
Device # show flowspec summary
FlowSpec Manager Summary:
Tables: 2
Flows: 1

Provides a summary of the flow specification rules present on the node.
In this example, the Tables field indicates that the flow specification policy mapping capability is enabled for IPv4 and
IPv6 address families.
The Flows field indicates that a single flow has been defined across the entire table.
Step 2

show bgp ipv4 flowspec
Example:
Device # show bgp ipv4 flowspec
Dest:192.0.2.0/24, Source:10.1.1.0/24, DPort:>=120&<=130,SPort:>=25&<=30,DSCP:=30/208
BGP routing table entry for Dest:192.0.2.0/24,
Source:10.1.1.0/24,Proto:=47,DPort:>=120&<=130,SPort:>=25&<=30,DSCP:=30/208 <snip>
Paths: (1 available, best #1)
Advertised to update-groups (with more than one peer):
0.3
Path #1: Received by speaker 0

IP Routing: BGP Configuration Guide
498


BGP Flow Specification Client
Configuration Examples for BGP Flow Specification Client

Advertised to update-groups (with more than one peer):
0.3 Local
0.0.0.0 from 0.0.0.0 (3.3.3.3)
Origin IGP, localpref 100, valid, redistributed, best, group-best
Received Path ID 0, Local Path ID 1, version 42
Extended community: FLOWSPEC Traffic-rate:100,0

Use this command to verify if a flow specification rule configured on the flow specification controller (device) is available
on the BGP side. In this example, redistributed indicates that the flow specification rule is not internally originated, but
one that has been redistributed from the flow specification process to BGP. The extended community (the BGP attribute
used to send the match and action criteria to peer devices) that is configured is also displayed.
In this example, the action defined is to rate limit the traffic.
Step 3

show flowspec vrf vrf-name afi-all
Example:
Device # show flowspec vrf vrf100 afi-all
VRF: vrf100
Flow
Actions
Flow
Actions

AFI: IPv4
:DPort:=101,SPort:=101,TCPFlags:~0xFF,Length:>=100&<=1500,DSCP:=63
:Redirect: VRF vrf200 Route-target: ASN2-200:2 (bgp.1)
:DPort:=102,SPort:=102,TCPFlags:~0xFF,Length:>=100&<=1500,DSCP:=63
:Redirect: VRF vrf200 Route-target: ASN2-200:2 (bgp.1)

Use this command to verify if a flow specification rule is in a specific VRF associated with the flow specification client
(device).

Configuration Examples for BGP Flow Specification Client
Example: Configuring a Device As a Flow Specification Client and Establishing
a BGP Peer Relationship With Neighbor
Device> enable
Device# configure terminal
Device (config)# router bgp 100
Device (config-bgp)# address-family ipv4 flowspec
Device (config-bgp-af)# neighbor 10.1.1.1 activate
Device (config-bgp-af)# exit
Device (config-bgp)# address-family ipv4 flowspec vrf vrf1
Device (config-bgp-af)# neighbor 2001:DB8:1::1 remote as 100
Device (config-bgp-af)# neighbor 2001:DB8:1::1 activate
Device (config-bgp-af)# exit

IP Routing: BGP Configuration Guide
499


BGP Flow Specification Client
Example: Configuring a Flow Specification Policy On All Interfaces Of a Device

Example: Configuring a Flow Specification Policy On All Interfaces Of a Device
Device> enable
Device# configure terminal
Device(config)# flowspec
Device(config-flowspec)# address-family ipv4
Device(config-flowspec-af)# local-install interface-all
Device(config-flowspec-af)# exit
Device(config-flowspec)# address-family ipv6
Device(config-flowspec-af)# local-install interface-all
Device(config-flowspec-af)# exit
Device(config-flowspec)# vrf vrf10
Device(config-flowspec-vrf)# address-family ipv4
Device(config-flowspec-vrf-af)# local-install interface-all
Device(config-flowspec-vrf-af)# exit
Device(config-flowspec-vrf)# address-family ipv6
Device(config-flowspec-vrf-af)# local-install interface-all
Device(config-flowspec-vrf-af)# exit

Additional References for BGP Flow Specification Client
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

BGP Flow Specification Route-reflector Support IP Routing: BGP Configuration Guide
Standards and RFCs
Standard/RFC Title
RFC 5575

Dissemination of Flow Specification Rules

MIBs
MIB

MIBs Link

• CISCO-MIB To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets,
use Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: BGP Configuration Guide
500


BGP Flow Specification Client
Feature Information for BGP Flow Specification Client

Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/cisco/web/support/index.html
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies.
To receive security and technical information about
your products, you can subscribe to various services,
such as the Product Alert Tool (accessed from Field
Notices), the Cisco Technical Services Newsletter, and
Really Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website
requires a Cisco.com user ID and password.

Feature Information for BGP Flow Specification Client
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 41: Feature Information for BGP Flow Specification Client

Feature Name

Releases

BGP Flow Specification Cisco IOS XE
Client
3.15S

Feature Information
The BGP flow specification client feature enables a device to
perform the role of a BGP flow specification client and receive
flow specification rules from a BGP flow specification
controller.
The following command was introduced or modified:
flowspec, local-install interface-all.

IP Routing: BGP Configuration Guide
501


BGP Flow Specification Client
Feature Information for BGP Flow Specification Client

IP Routing: BGP Configuration Guide
502
