---
title: "BGP—IPv6 NSR"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-ipv6-nsr
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 70 BGP—IPv6 NSR Border Gateway Protocol (BGP) support for Nonstop Routing (NSR) enables provider edge (PE) routers to maintain BGP state with customer edge (CE) routers and ensure continuous packet forwarding during a Route Processor (RP) switchover or during a planned In-Service Software Upgrade (ISSU) for a PE router. The BGP—IPv6 NSR feature extends BGP support for NSR to Cisco IPv6 V"
---

# BGP—IPv6 NSR

CHAPTER

70

BGP—IPv6 NSR
Border Gateway Protocol (BGP) support for Nonstop Routing (NSR) enables provider edge (PE) routers to
maintain BGP state with customer edge (CE) routers and ensure continuous packet forwarding during a Route
Processor (RP) switchover or during a planned In-Service Software Upgrade (ISSU) for a PE router. The
BGP—IPv6 NSR feature extends BGP support for NSR to Cisco IPv6 VPN Provider Edge Routers (6VPE).
• Finding Feature Information, on page 1023
• Prerequisites for BGP—IPv6 NSR, on page 1023
• Information About BGP—IPv6 NSR, on page 1024
• How to Configure BGP—IPv6 NSR, on page 1024
• Configuration Examples for BGP—IPv6 NSR, on page 1026
• Additional References for BGP—IPv6 NSR, on page 1026
• Feature Information for BGP—IPv6 NSR, on page 1027

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest feature
information and caveats, see the release notes for your platform and software release. To find information
about the features documented in this module, and to see a list of the releases in which each feature is supported,
see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not
required.

Prerequisites for BGP—IPv6 NSR
• Your network is configured to run BGP.
• Multiprotocol Layer Switching (MPLS) Layer 3 Virtual Private Networks (VPNs) are configured.
• All platforms are HA capable.
• You are familiar with the concepts in the “BGP Support for Nonstop Routing (NSR) with Stateful
Switchover (SSO)” and “BGP NSR Support for iBGP Peers” modules of the IP Routing: BGP
Configuration Guide.

IP Routing: BGP Configuration Guide
1023


BGP—IPv6 NSR
Information About BGP—IPv6 NSR

Information About BGP—IPv6 NSR
Overview of BGP—IPv6 NSR
Nonstop routing (NSR) is beneficial for BGP peers because it reduces the likelihood of dropped packets during
switchover from the active Route Processor (RP) to the standby RP. Switchover occurs when the active RP
fails for some reason and the standby RP takes control of active RP operations. The BGP—IPv6 NSR feature
extends BGP support for NSR to include the following IPv6-based address families:
• IPv6 unicast
• IPv6 unicast + label
• IPv6 PE-CE
• VPNv6 unicast
Figure 89: Basic 6VPE Network Configuration

The figure above depicts a basic deployment scenario. Provider edge (PE) router 1, P, and PE2 form a 6VPE
cloud. The customer edge (CE) router 1 to PE1 connection is IPv6 (VRF). The PEs are HA/SSO and NSF
capable. The P routers are capable of Multiprotocol Label Switching (MPLS) label preservation (NSF
equivalent).
As the CE1 is customer equipment, the provider cannot determine that it must be upgraded to be NSF aware.
If PE1 can perform NSR on its connection to CE1, then CE1 will not be aware or impacted when PE1 performs
a switchover in SSO mode. For all other connections within the autonomous system, the operations may be
NSF or graceful restart. This means the control plane will be reset, and all the immediate peers will be aware
of it and will resend data to help re-establish the session, but forwarding will be uninterrupted.
Neighbors not operating under NSR are still expected to be NSF capable/aware. If the CE is already NSF
aware (that is, it can handle a BGP graceful restart by its peers), then the PE-CE connection will not be NSR,
and will instead follow the regular NSF processing model. This parallels NSR for VPNv4 and assists in
conserving network resources.

How to Configure BGP—IPv6 NSR
Configuring BGP—IPv6 NSR
Perform this task on a PE router if you want to configure a BGP peer to support BGP—IPv6 NSR.

IP Routing: BGP Configuration Guide
1024


BGP—IPv6 NSR
Configuring BGP—IPv6 NSR

SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
router bgp autonomous-system-number
Enter one of the following:
• address-family ipv6 [unicast | multicast | vpnv6] [vrf vrf-name]
• address-family vpnv6 [unicast | multicast]

5.
6.
7.
8.

neighbor ipv6-address% remote-as as-number
neighbor ipv6-address% activate
neighbor ipv6-address% ha-mode sso
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

router bgp autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 4000

Step 4

Enter one of the following:
• address-family ipv6 [unicast | multicast | vpnv6]
[vrf vrf-name]
• address-family vpnv6 [unicast | multicast]
Example:
Device(config-router)# address-family ipv6 unicast

Step 5

neighbor ipv6-address% remote-as as-number

Specifies the IPv6 address family and enters address family
configuration mode.
• The unicast keyword specifies the IPv6 unicast address
family.
• The vrf keyword and vrf-name argument specify the
name of the virtual routing and forwarding (VRF)
instance to associate with subsequent IPv6 address
family configuration mode commands.
Specifies the autonomous system of the neighbor.

Example:
Device(config-router-af)# neighbor
2001:DB8:0:CC00::1 remote-as 4000

IP Routing: BGP Configuration Guide
1025


BGP—IPv6 NSR
Configuration Examples for BGP—IPv6 NSR

Step 6

Command or Action

Purpose

neighbor ipv6-address% activate

Activates the specified peer.

Example:
Device(config-router-af)# neighbor
2001:DB8:0:CC00::1 activate

Step 7

neighbor ipv6-address% ha-mode sso

Configures a BGP neighbor to support BGP NSR.

Example:
Device(config-router-af)# neighbor
2001:DB8:0:CC00::1 ha-mode sso

Step 8

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuration Examples for BGP—IPv6 NSR
Example: Configuring BGP—IPv6 NSR
router bgp 4000
address-family ipv6 unicast
neighbor 2001:DB8:0:CC00::1 remote-as 4000
neighbor 2001:DB8:0:CC00::1 activate
neighbor 2001:DB8:0:CC00::1 ha-mode sso

Additional References for BGP—IPv6 NSR
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Routing: BGP Configuration Guide
1026


BGP—IPv6 NSR
Feature Information for BGP—IPv6 NSR

Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.

http://www.cisco.com/support

To receive security and technical information about your products, you can
subscribe to various services, such as the Product Alert Tool (accessed from
Field Notices), the Cisco Technical Services Newsletter, and Really Simple
Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com user
ID and password.

Feature Information for BGP—IPv6 NSR
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 90: Feature Information for BGP—IPv6 NSR

Feature Name

Releases

Feature Information

BGP—IPv6 NSR

Cisco IOS XE Release 3.9S

BGP support for NSR enables
provider edge (PE) routers to
maintain BGP state with customer
edge (CE) routers and ensure
continuous packet forwarding
during a Route Processor (RP)
switchover or during a planned
ISSU for a PE router. The
BGP—IPv6 NSR feature extends
BGP support for NSR to Cisco
IPv6 VPN Provider Edge Routers
(6VPE).

IP Routing: BGP Configuration Guide
1027


BGP—IPv6 NSR
Feature Information for BGP—IPv6 NSR

IP Routing: BGP Configuration Guide
1028
