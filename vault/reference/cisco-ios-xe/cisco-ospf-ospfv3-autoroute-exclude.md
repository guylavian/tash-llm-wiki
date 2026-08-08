---
title: "OSPFv3 Autoroute Exclude"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-autoroute-exclude
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 18 OSPFv3 Autoroute Exclude OSPFv3 Autoroute Exclude feature allows you to use specific destinations and prefix-list to specify a list of prefixes that are routed using native paths instead of TE tunnels for packet transport. The rest of the prefixes can still be set to use TE tunnels. Prefixes that are excluded do not use a TE tunnel path. IPv6 routes over TE tunnels are supported by OS"
---

# OSPFv3 Autoroute Exclude

CHAPTER

18

OSPFv3 Autoroute Exclude
OSPFv3 Autoroute Exclude feature allows you to use specific destinations and prefix-list to specify a list
of prefixes that are routed using native paths instead of TE tunnels for packet transport. The rest of the
prefixes can still be set to use TE tunnels. Prefixes that are excluded do not use a TE tunnel path. IPv6 routes
over TE tunnels are supported by OSPFv3 using Autoroute Announce (AA) or Forwarding Adjacencies
(FA).
This module describes how to configure the OSPFv3 Autoroute Exclude feature.
• Finding Feature Information, page 201
• Prerequisites for OSPFv3 Autoroute Exclude, page 201
• Information About OSPFv3 Autoroute Exclude, page 202
• How to Configure OSPFv3 Autoroute Exclude, page 202
• Configuration Examples for OSPFv3 Autoroute Exclude, page 203
• Additional References for OSPFv3 Autoroute Exclude, page 204
• Feature Information for OSPFv3 Autoroute Exclude, page 205

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv3 Autoroute Exclude
• Open Shortest Path First (OSPF) must be configured in your network.
• Cisco Express Forwarding (CEF) must be enabled.

IP Routing: OSPF Configuration Guide
201


OSPFv3 Autoroute Exclude
Information About OSPFv3 Autoroute Exclude

• Multiprotocol Label Switching (MPLS) TE tunnels must be configured.
• Auto route announce and forwarding adjacencies must be configured. You can configure either auto
route announce or forwarding adjacencies on an interface. You cannot configure them both on the same
interface.

Information About OSPFv3 Autoroute Exclude
Overview of OSPFv3 Autoroute Exclude
The auto route feature is an IP routing method that forces OSPF to use MPLS TE tunnels to build paths for
IP traffic routes. The auto route feature enables all routes to use TE Tunnels, even if there is an alternate
non-TE path available for that route.
The OSPFv3 Autoroute Exclude feature allows specific IPv6 destinations or prefixes to avoid TE tunnels,
while other prefixes can still be configured to use TE tunnels. Prefixes that are excluded do not use a TE
tunnel path. Only native non-TE paths are downloaded to RIB for such routes. IPv6 routes over TE tunnels
are supported by OSPFv3 using auto route announce (AA) or forwarding adjacencies (FA).
The auto route exclude option is configured under the router OSPF configuration mode by using a prefix list.
IP addresses and prefixes that are members of this prefix list are excluded from TE tunnels, even when the
auto route is enabled on them. If the IP addresses or prefixes are added to the prefix list, they are dynamically
routed without passing through the TE tunnel. If the IP addresses or prefixes are removed from the prefix list,
they are dynamically rerouted back on the TE tunnel path.
See the Autoroute Announce and Forwarding Adjacencies For OSPFv3 module in IP Routing: OSPF
Configuration Guide for details on configuring auto route announce and forwarding adjacencies For OSPFv3.

How to Configure OSPFv3 Autoroute Exclude
Configuring OSPFv3 Autoroute Exclude
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 process-ID
4. address-family ipv6 unicast
5. mpls traffic-engineering autoroute-exclude prefix-list prefix-list-name
6. end

IP Routing: OSPF Configuration Guide
202


OSPFv3 Autoroute Exclude
Configuration Examples for OSPFv3 Autoroute Exclude

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

router ospfv3 process-ID

Configures OSPFv3 routing process and enters OSPF router
configuration mode.

Example:
Device(config)# router ospfv3 18

Step 4

address-family ipv6 unicast

Enters IPv6 address family configuration mode for
OSPFv3.

Example:
Device(config-router)# address-family ipv6
unicast

Step 5

mpls traffic-engineering autoroute-exclude prefix-list Allows specific destinations and prefixes to avoid routing
through TE tunnels.
prefix-list-name
Example:
Device(config-router-af)# mpls
traffic-engineering autoroute-exclude
prefix-list kmd

Step 6

• Prefixes that are excluded do not use a TE tunnel
path.

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuration Examples for OSPFv3 Autoroute Exclude
Example: Configuring OSPFv3 Autoroute Exclude
!
router ospfv3 18
address-family ipv6 unicast
mpls traffic-engineering autoroute-exclude prefix-list kmd
!

IP Routing: OSPF Configuration Guide
203


OSPFv3 Autoroute Exclude
Additional References for OSPFv3 Autoroute Exclude

Additional References for OSPFv3 Autoroute Exclude
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

Configuring OSPF

IP Routing: OSPF Configuration
Guide

Autoroute Announce and Forwarding Adjacencies For OSPFv3

IP Routing: OSPF Configuration
Guide

Configuring Basic Cisco Express Forwarding

IP Switching: Cisco Express
Forwarding Configuration Guide

MPLS Traffic Engineering Tunnel Source

MPLS Traffic Engineering Path
Calculation and Setup
Configuration Guide

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

IP Routing: OSPF Configuration Guide
204


OSPFv3 Autoroute Exclude
Feature Information for OSPFv3 Autoroute Exclude

Feature Information for OSPFv3 Autoroute Exclude
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 21: Feature Information for OSPFv3 Autoroute Exclude

Feature Name

Releases

Feature Information

OSPFv3 Autoroute Exclude

Cisco IOS XE 3.14S

OSPFv3 Autoroute Exclude feature
allows you to use specific
destinations and prefix-list to
specify a list of prefixes that are
routed using native paths instead
of TE tunnels for packet transport.
IPv6 routes over TE tunnels are
supported by OSPFv3 using
autoroute announce or forwarding
adjacencies.
The following commands were
introduced or modified: mpls
traffic-engineering
autoroute-exclude prefix list.

IP Routing: OSPF Configuration Guide
205


OSPFv3 Autoroute Exclude
Feature Information for OSPFv3 Autoroute Exclude

IP Routing: OSPF Configuration Guide
206
