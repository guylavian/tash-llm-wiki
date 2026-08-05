---
title: "IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-ipv6-nsf-and-graceful-restart-for-mp-bgp-ipv6-address-family
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 29 IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family • Finding Feature Information, on page 537 • Information About IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family, on page 537 • How to Configure IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family, on page 538 • Configuration Examples for IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family, on pa"
---

# IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family

CHAPTER

29

IPv6 NSF and Graceful Restart for MP-BGP IPv6
Address Family
• Finding Feature Information, on page 537
• Information About IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family, on page 537
• How to Configure IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family, on page 538
• Configuration Examples for IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family, on page
539
• Additional References, on page 539
• Feature Information for IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family, on page 540

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About IPv6 NSF and Graceful Restart for MP-BGP
IPv6 Address Family
Nonstop Forwarding and Graceful Restart for MP-BGP IPv6 Address Family
The graceful restart capability is supported for IPv6 BGP unicast, multicast, and VPNv6 address families,
enabling Cisco nonstop forwarding (NSF) functionality for BGP IPv6. The BGP graceful restart capability
allows the BGP routing table to be recovered from peers without keeping the TCP state.
NSF continues forwarding packets while routing protocols converge, therefore avoiding a route flap on
switchover. Forwarding is maintained by synchronizing the FIB between the active and standby RP. On
switchover, forwarding is maintained using the FIB. The RIB is not kept synchronized; therefore, the RIB is
empty on switchover. The RIB is repopulated by the routing protocols and subsequently informs FIB about

IP Routing: BGP Configuration Guide
537


IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family
How to Configure IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family

RIB convergence by using the NSF_RIB_CONVERGED registry call. The FIB tables are updated from the
RIB, removing any stale entries. The RIB starts a failsafe timer during RP switchover, in case the routing
protocols fail to notify the RIB of convergence.
The Cisco BGP address family identifier (AFI) model is designed to be modular and scalable, and to support
multiple AFI and subsequent address family identifier (SAFI) configurations.

How to Configure IPv6 NSF and Graceful Restart for MP-BGP
IPv6 Address Family
Configuring the IPv6 BGP Graceful Restart Capability
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp as-number
address-family ipv6 [ vrf vrf-name ] [unicast | multicast | vpnv6]
bgp graceful-restart [restart-time seconds | stalepath-time seconds] [all]

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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 65000

Step 4

address-family ipv6 [ vrf vrf-name ] [unicast | multicast Specifies the IPv6 address family.
| vpnv6]
Example:
Device(config-router)# address-family ipv6

Step 5

bgp graceful-restart [restart-time seconds |
stalepath-time seconds] [all]

IP Routing: BGP Configuration Guide
538

Enables the BGP graceful restart capability.


IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family
Configuration Examples for IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family

Command or Action

Purpose

Example:
Device(config-router-af)# bgp graceful-restart

Configuration Examples for IPv6 NSF and Graceful Restart for
MP-BGP IPv6 Address Family
Example: Configuring the IPv6 BGP Graceful Restart Capability
In the following example, the BGP graceful restart capability is enabled:
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# address-family ipv6
Device(config-router-af)# bgp graceful-restart

In the following example, the restart timer is set to 130 seconds:
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# address-family ipv6
Device(config-router-af)# bgp graceful-restart restart-time 130

In the following example, the stalepath timer is set to 350 seconds:
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# address-family ipv6
Device(config-router-af)# bgp graceful-restart stalepath-time 350

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
539


IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family
Feature Information for IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family

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

Feature Information for IPv6 NSF and Graceful Restart for
MP-BGP IPv6 Address Family
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
540


IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family
Feature Information for IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family

Table 45: Feature Information for IPv6: NSF and Graceful Restart for MP-BGP IPv6 Address Family

Feature Name

Releases

Feature Information

IPv6: NSF and Graceful Restart for Cisco IOS XE Release 3.1
MP-BGP IPv6 Address Family

The graceful restart capability is
supported for IPv6 BGP unicast,
multicast, and VPNv6 address
families, enabling Cisco NSF
functionality for BGP IPv6. The
BGP graceful restart capability
allows the BGP routing table to be
recovered from peers without
keeping the TCP state.

IP Routing: BGP Configuration Guide
541


IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family
Feature Information for IPv6 NSF and Graceful Restart for MP-BGP IPv6 Address Family

IP Routing: BGP Configuration Guide
542
