---
title: "OSPFv2 Autoroute Exclude"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv2-autoroute-exclude
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 14 OSPFv2 Autoroute Exclude The OSPFv2 Autoroute Exclude feature allows specific destinations and prefixes to avoid Traffic Engineering (TE) tunnels for the packet transport. The rest of the prefixes can still be set to use TE tunnels. Prefixes that are excluded do not use a TE tunnel path. Only native non-TE paths are downloaded to RIB for such routes. This module describes how to confi"
---

# OSPFv2 Autoroute Exclude

CHAPTER

14

OSPFv2 Autoroute Exclude
The OSPFv2 Autoroute Exclude feature allows specific destinations and prefixes to avoid Traffic Engineering
(TE) tunnels for the packet transport. The rest of the prefixes can still be set to use TE tunnels. Prefixes that
are excluded do not use a TE tunnel path. Only native non-TE paths are downloaded to RIB for such routes.
This module describes how to configure the OSPFv2 Autoroute Exclude feature.
• Finding Feature Information, page 157
• Prerequisites for OSPFv2 Autoroute Exclude, page 157
• Information About OSPFv2 Autoroute Exclude, page 158
• How to Configure OSPFv2 Autoroute Exclude, page 158
• Configuration Examples for OSPFv2 Autoroute Exclude, page 159
• Additional References for OSPFv2 Autoroute Exclude, page 160
• Feature Information for OSPFv2 Autoroute Exclude, page 160

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv2 Autoroute Exclude
• Open Shortest Path First (OSPF) must be configured in your network.
• Cisco Express Forwarding (CEF) must be enabled.
• Multiprotocol Label Switching (MPLS) TE tunnels must be configured.

IP Routing: OSPF Configuration Guide
157


OSPFv2 Autoroute Exclude
Information About OSPFv2 Autoroute Exclude

Information About OSPFv2 Autoroute Exclude
Overview of OSPFv2 Autoroute Exclude
The Autoroute feature is an IP routing method that forces OSPF to use MPLS TE tunnels to build paths for
IP traffic routes.
The Autoroute feature enables all routes to use TE Tunnels, even if there is an alternate non-TE path available
for that route.
The OSPFv2 Autoroute Exclude feature allows specific destinations or prefixes to avoid TE tunnels, while
other prefixes can still be configured to use TE tunnels. Prefixes that are excluded do not use a TE tunnel
path. Only native non-TE paths are downloaded to RIB for such routes.
The auto route exclude option is configured under the router OSPF configuration mode by using a prefix list.
IP addresses and prefixes that are members of this prefix list are excluded from TE tunnels, even when the
auto route is enabled on them. If the IP addresses or prefixes are added to the prefix list, they are dynamically
routed without passing through the TE tunnel. If the IP addresses or prefixes are removed from the prefix list,
they are dynamically rerouted back on the TE tunnel path.

How to Configure OSPFv2 Autoroute Exclude
Configuring OSPFv2 Autoroute Exclude
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-ID
4. router-id ip-address
5. mpls traffic-eng router-id interface-name
6. mpls traffic-eng areanumber
7. mpls traffic-eng autoroute-exclude prefix-list prefix-list-name
8. exit

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device> enable

IP Routing: OSPF Configuration Guide
158

• Enter your password if prompted.


OSPFv2 Autoroute Exclude
Configuration Examples for OSPFv2 Autoroute Exclude

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router ospf process-ID

Configures OSPF routing process and enters OSPF router
configuration mode.

Example:
Device(config)# router ospf 18

Step 4

router-id ip-address

Enables to use a fixed router ID in router configuration
mode.

Example:
Device(config-router)# router-id 10.1.1.1

Step 5

mpls traffic-eng router-id interface-name

Specifies the traffic engineering router identifier for the node
and the IP address associated with a given interface.

Example:
Device(config-router)# mpls traffic-eng
router-id Loopback0

Step 6

mpls traffic-eng areanumber

Configures a router running OSPF MPLS so that it floods
traffic engineering for the indicated OSPF area.

Example:
Device(config-router)# mpls traffic-eng area
0

Step 7

mpls traffic-eng autoroute-exclude prefix-list
prefix-list-name
Example:

Allows specific destinations and prefixes to avoid routing
through TE tunnels.
• Prefixes that are excluded do not use a TE tunnel path.

Device(config-router)# mpls traffic-eng
autoroute-exclude prefix-list kmd

Step 8

Exits router configuration mode and returns to privileged
EXEC mode.

exit
Example:
Device(config-router)# exit

Configuration Examples for OSPFv2 Autoroute Exclude
Example: Configuring OSPFv2 Autoroute Exclude
!
router ospf 1

IP Routing: OSPF Configuration Guide
159


OSPFv2 Autoroute Exclude
Additional References for OSPFv2 Autoroute Exclude

router-id 3.3.3.3
mpls traffic-eng router-id Loopback0
mpls traffic-eng area 0
mpls traffic-eng autoroute-exclude prefix-list XX
!

Additional References for OSPFv2 Autoroute Exclude
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

Configuring OSPF

IP Routing: OSPF Configuration Guide

Configuring Basic Cisco Express Forwarding

IP Switching: Cisco Express Forwarding
Configuration Guide

MPLS Traffic Engineering Tunnel Source

MPLS Traffic Engineering Path Calculation and
Setup Configuration Guide

Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/support
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies.
To receive security and technical information about
your products, you can subscribe to various services,
such as the Product Alert Tool (accessed from Field
Notices), the Cisco Technical Services Newsletter,
and Really Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website
requires a Cisco.com user ID and password.

Feature Information for OSPFv2 Autoroute Exclude
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.

IP Routing: OSPF Configuration Guide
160


OSPFv2 Autoroute Exclude
Feature Information for OSPFv2 Autoroute Exclude

Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 17: Feature Information for OSPFv2 Autoroute Exclude

Feature Name

Releases

Feature Information

OSPFv2 Autoroute Exclude

Cisco IOS XE 3.13S

The OSPFv2 Autoroute Exclude
feature allows specific destinations
and prefixes to avoid TE tunnels
for the packet transport.
The following commands were
introduced or modified: mpls
traffic-eng autoroute-exclude
prefix list.

IP Routing: OSPF Configuration Guide
161


OSPFv2 Autoroute Exclude
Feature Information for OSPFv2 Autoroute Exclude

IP Routing: OSPF Configuration Guide
162
