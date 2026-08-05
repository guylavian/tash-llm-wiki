---
title: "Multicast VPN BGP Dampening"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-multicast-vpn-bgp-dampening
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 69 Multicast VPN BGP Dampening A single receiver in a specific multicast group or a group of receivers that are going up and down frequently and interested in a specific multicast group activates the Multicast VPN BGP Dampening feature to dampen type 7 routes (C-multicast route Join/Prune) within the core using BGP signaling. The feature reduces the churn caused by customer-side join/pru"
---

# Multicast VPN BGP Dampening

CHAPTER

69

Multicast VPN BGP Dampening
A single receiver in a specific multicast group or a group of receivers that are going up and down frequently
and interested in a specific multicast group activates the Multicast VPN BGP Dampening feature to dampen
type 7 routes (C-multicast route Join/Prune) within the core using BGP signaling. The feature reduces the
churn caused by customer-side join/prune requests to avoid unnecessary BGP MVPN type 6/7 C-route control
information.
• Finding Feature Information, on page 1015
• Prerequisites for Multicast VPN BGP Dampening, on page 1015
• Information About Multicast VPN BGP Dampening, on page 1016
• How to Configure Multicast VPN BGP Dampening, on page 1017
• Configuration Examples for Multicast VPN BGP Dampening, on page 1019
• Additional References for Multicast VPN BGP Dampening, on page 1020
• Feature Information for Multicast VPN BGP Dampening, on page 1020

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for Multicast VPN BGP Dampening
• You understand the concepts in the “BGP Route Dampening” module of the IP Routing: BGP
Configuration Guide.

IP Routing: BGP Configuration Guide
1015


Multicast VPN BGP Dampening
Information About Multicast VPN BGP Dampening

Information About Multicast VPN BGP Dampening
Overview of Multicast VPN BGP Dampening
BGP Route Dampening
Route dampening is a BGP feature designed to minimize the propagation of flapping routes across an
internetwork. A route is considered to be flapping when its availability alternates repeatedly. Cisco devices
that are running BGP contain a mechanism designed to “dampen” the destabilizing effect of flapping routes.
When a Cisco device running BGP detects a flapping route, it automatically dampens that route.
The figure below shows illustrates the Multicast VPN BGP dampening mechanism.
Multicast VPN BGP Dampening
Figure 88: Multicast VPN BGP Dampening

A single receiver in a multicast group or a group of receivers that are flapping frequently and interested in a
specific multicast group actrivates multicast VPN (MVPN) BGP dampening. MVPN BGP dampening dampens
the type 7 multicast routes (customer-multicast, or “C-multicast,” route join/prune) within the core using BGP
signaling.
When MVPN BGP dampening is not enabled, the source sends data even though the receiver may be down.
When the receiver is down, there is no periodic 60-second C-PIM join towards the provider edge (PE) device
causing the PIM to timeout on the PE side after the default period (three minutes). The MVPN manager sends
a prune message to BGP, which is a type 7 route (C-multicast route withdraw).
When the receiver is up, it sends a new (S,G) join request to the customer edge (CE) device. The C-PIM join
is received by the PE device and a new type 7 C-multicast update is sent by BGP to the auto-discovered MVPN
peers. The upstream multicast peer converts the BGP type 7 update to a PIM join to the source, and the source
sends the data traffic that the receiver should receive via the downstream PE using the MDT tunnel. If the
receiver goes up and down frequently, the source side PIM receives join/prune messages frequently and can
cause the source to respond accordingly.

IP Routing: BGP Configuration Guide
1016


Multicast VPN BGP Dampening
How to Configure Multicast VPN BGP Dampening

When MVPN BGP dampening is enabled, the general dampening mechanism in BGP will be applied to
MVPN VRF instances. Join/Prune messages from the CE side are sent from an MVPN manager as
updates/withdraw to the MVPN PE device. The MVPN manager on PE devices send join/prune messages to
the customer side for Reverse Path Forwarding (RPF) and upstream multihop (UMH) nexthop changes.

How to Configure Multicast VPN BGP Dampening
Configuring Multicast VPN BGP Dampening
Perform this task to enable and configure multicast VPN BGP dampening.
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
address-family [ipv4 | ipv6] mvpn vrf vrf-name
bgp dampening [half-life reuse suppress max-suppress-time]
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

Enters router configuration mode and creates a BGP routing
process.

Device(config)# router bgp 45000

Step 4

address-family [ipv4 | ipv6] mvpn vrf vrf-name
Example:
Device(config-router)# address-family ipv4 mvpn
vrf blue

Specifies the address family and enters address family
configuration mode.
• Use the ipv4 keyword to enable IPv4 multicast C-route
exchange.
• Use the ipv6 keyword to enable IPv6 multicast C-route
exchange.

IP Routing: BGP Configuration Guide
1017


Multicast VPN BGP Dampening
Monitoring and Maintaining Multicast VPN BGP Dampening

Command or Action

Purpose
Note

Step 5

bgp dampening [half-life reuse suppress
max-suppress-time]
Example:
Device(config-router-af)# bgp dampening 30 1500
10000 120

Step 6

The vrf keyword and vrf-name argument must
be specified at this point to enable multicast VPN
BGP dampening in the next step.

Enables BGP route dampening and changes the default
values of route dampening factors. The half-life, reuse,
suppress, and max-suppress-time arguments are all position
dependent; if one argument is entered, then all the arguments
must be entered.
Note

Repeat steps 4 and 5 to enable multicast VPN
BGP dampening on alternative VRFs.

Exits address family configuration mode and enters
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Monitoring and Maintaining Multicast VPN BGP Dampening
Perform the steps in this task as required to monitor and maintain multicast VPN BGP dampening.
SUMMARY STEPS
1. enable
2. show bgp {ipv4 | ipv6} mvpn {all | rd route-distinguisher | vpn vrf-name} [dampening {dampened-paths
| flap-statistics [filter-list access-list-number | quote-regexp regexp | regexp regexp]}]
3. clear ip bgp {ipv4 | ipv6} mvpn vrf vrf-name {dampening | flap-statistics}
DETAILED STEPS

Step 1

enable
Enables privileged EXEC mode. Enter your password if prompted.
Example:
Device> enable

Step 2

show bgp {ipv4 | ipv6} mvpn {all | rd route-distinguisher | vpn vrf-name} [dampening {dampened-paths | flap-statistics
[filter-list access-list-number | quote-regexp regexp | regexp regexp]}]
Use this command to monitor multicast VPN BGP dampening.
• The dampened-path keyword displays information about BGP dampened routes.
• The parameters keyword displays detailed BGP dampening information.
• The flap-statistics keyword displays information on BGP flap statistics.

IP Routing: BGP Configuration Guide
1018


Multicast VPN BGP Dampening
Configuration Examples for Multicast VPN BGP Dampening

Example:
Device# show bgp ipv4 mvpn vrf blue route-type 7 111.111.111.111:11111 55 202.100.0.6 232.1.1.1
BGP routing table entry for [7][111.111.111.111:11111][55][202.100.0.6/32][232.1.1.1/32]/22, version
17
Paths: (1 available, no best path)
Flag: 0x820
Not advertised to any peer
Refresh Epoch 1
Local, (suppressed due to dampening)
0.0.0.0 from 0.0.0.0 (205.3.0.3)
Origin incomplete, localpref 100, weight 32768, valid, sourced, local
Extended Community: RT:205.1.0.1:1
Dampinfo: penalty 3472, flapped 4 times in 00:04:42, reuse in 00:00:23
rx pathid: 0, tx pathid: 0

Step 3

clear ip bgp {ipv4 | ipv6} mvpn vrf vrf-name {dampening | flap-statistics}
Use this command to clear the accumulated penalty for routes that are received on a router that has multicast VPN BGP
dampening enabled.
• The dampening keyword clears multicast VPN BGP dampening information.
• The flap-statistic keyword clears multicast VPN BGP dampening flap statistics.
Example:
Device# clear ip bgp ipv4 mvpn vrf blue dampening

Configuration Examples for Multicast VPN BGP Dampening
Example: Configuring Multicast VPN BGP Dampening
The following example shows multicast VPN BGP dampening is applied to the VRFs named blue
and red, but not to the VRF named green:
address-family ipv4 mvpn vrf blue
bgp dampening
address-family ipv4 mvpn vrf red
bgp dampening
address-family ipv4 mvpn vrf green
no bgp dampening

IP Routing: BGP Configuration Guide
1019


Multicast VPN BGP Dampening
Additional References for Multicast VPN BGP Dampening

Additional References for Multicast VPN BGP Dampening
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

BGP commands

Cisco IOS IP Routing: BGP
Command Reference

BGP route dampening

“BGP Route Dampening” section
of the “Configuring Internal BGP
Features” module in the IP
Routing: BGP Configuration Guide

Standards and RFCs
Standard/RFC Title
RFC 2439

BGP Route Flap Damping

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

Feature Information for Multicast VPN BGP Dampening
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
1020


Multicast VPN BGP Dampening
Feature Information for Multicast VPN BGP Dampening

Table 89: Feature Information for Multicast VPN BGP Dampening

Feature Name

Releases

Feature Information

Multicast VPN BGP Dampening

Cisco IOS XE Release 3.8S

A single receiver in a specific
multicast group or a group of
receivers that are going up and
down frequently and interested in
a specific multicast group will
cause the Multicast VPN BGP
Dampening feature to dampen type
7 routes (C-multicast route
join/prune) within the core using
BGP signaling.
The following commands were
introduced or modified:
address-family mvpn, clear ip
bgp mvpn, show bgp mvpn, and
show ip bgp ipv4.

IP Routing: BGP Configuration Guide
1021


Multicast VPN BGP Dampening
Feature Information for Multicast VPN BGP Dampening

IP Routing: BGP Configuration Guide
1022
