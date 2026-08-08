---
title: "BGP MIB Support"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-mib-support
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 54 BGP MIB Support The BGP MIB Support Enhancements feature introduces support in the CISCO-BGP4-MIB for new SNMP notifications. • Finding Feature Information, on page 859 • Information About BGP MIB Support, on page 859 • How to Enable BGP MIB Support, on page 861 • Configuration Examples for BGP MIB Support, on page 863 • Additional References, on page 863 • Feature Information for BGP"
---

# BGP MIB Support

CHAPTER

54

BGP MIB Support
The BGP MIB Support Enhancements feature introduces support in the CISCO-BGP4-MIB for new SNMP
notifications.
• Finding Feature Information, on page 859
• Information About BGP MIB Support, on page 859
• How to Enable BGP MIB Support, on page 861
• Configuration Examples for BGP MIB Support, on page 863
• Additional References, on page 863
• Feature Information for BGP MIB Support, on page 864

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP MIB Support
BGP MIB Support
The Management Information Base (MIB) that supports BGP is the CISCO-BGP4-MIB. The BGP MIB
Support Enhancements feature introduces support in the CISCO-BGP4-MIB for new SNMP notifications.
The following sections describe the objects and notifications (traps) that are supported:
BGP FSM Transition Change Support
The cbgpRouteTable supports BGP Finite State Machine (FSM) transition state changes.
The cbgpFsmStateChange object allows you to configure SNMP notifications (traps) for all FSM transition
state changes. This notification contains the following MIB objects:

IP Routing: BGP Configuration Guide
859


BGP MIB Support
BGP MIB Support

• bgpPeerLastError
• bgpPeerState
• cbgpPeerLastErrorTxt
• cbgpPeerPrevState
The cbgpBackwardTransition object supports all BGP FSM transition state changes. This object is sent each
time the FSM moves to either a higher or lower numbered state. This notification contains the following MIB
objects:
• bgpPeerLastError
• bgpPeerState
• cbgpPeerLastErrorTxt
• cbgpPeerPrevState
The snmp-server enable bgp traps command allows you to enable the traps individually or together with
the existing FSM backward transition and established state traps as defined in RFC 1657.
BGP Route Received Route Support
The cbgpRouteTable object supports the total number of routes received by a BGP neighbor. The following
MIB object is used to query the CISCO-BGP4-MIB for routes that are learned from individual BGP peers:
• cbgpPeerAddrFamilyPrefixTable
Routes are indexed by the address-family identifier (AFI) or subaddress-family identifier (SAFI). The prefix
information displayed in this table can also viewed in the output of the show ip bgp command.
BGP Prefix Threshold Notification Support
The cbgpPrefixMaxThresholdExceed and cbgpPrfefixMaxThresholdClear objects were introduced to allow
you to poll for the total number of routes received by a BGP peer.
The cbgpPrefixMaxThresholdExceed object allows you to configure SNMP notifications to be sent when the
prefix count for a BGP session has exceeded the configured value. This notification is configured on a per
address family basis. The prefix threshold is configured with the neighbor maximum-prefix command. This
notification contains the following MIB objects:
• cbgpPeerPrefixAdminLimit
• cbgpPeerPrefixThreshold
The cbgpPrfefixMaxThresholdClear object allows you to configure SNMP notifications to be sent when the
prefix count drops below the clear trap limit. This notification is configured on a per address family basis.
This notification contains the following objects:
• cbgpPeerPrefixAdminLimit
• cbgpPeerPrefixClearThreshold
Notifications are sent when the prefix count drops below the clear trap limit for an address family under a
BGP session after the cbgpPrefixMaxThresholdExceed notification is generated. The clear trap limit is

IP Routing: BGP Configuration Guide
860


BGP MIB Support
How to Enable BGP MIB Support

calculated by subtracting 5 percent from the maximum prefix limit value configured with the neighbor
maximum-prefix command. This notification will not be generated if the session goes down for any other
reason after the cbgpPrefixMaxThresholdExceed is generated.
VPNv4 Unicast Address Family Route Support
The cbgpRouteTable object allows you to configure SNMP GET operations for VPNv4 unicast address-family
routes.
The following MIB object allows you to query for multiple BGP capabilities (for example, route refresh,
multiprotocol BGP extensions, and graceful restart):
• cbgpPeerCapsTable
The following MIB object allows you to query for IPv4 and VPNv4 address family routes:
• cbgpPeerAddrFamilyTable
Each route is indexed by peer address, prefix, and prefix length. This object indexes BGP routes by the AFI
and then by the SAFI. The AFI table is the primary index, and the SAFI table is the secondary index. Each
BGP speaker maintains a local Routing Information Base (RIB) for each supported AFI and SAFI combination.
cbgpPeerTable Support
The cbgpPeerTable has been modified to support the enhancements described in this document. The following
new table objects are supported in the CISCO-BGP-MIB.my:
• cbgpPeerLastErrorTxt
• cbgpPeerPrevState
The following table objects are not supported. The status of these objects is listed as deprecated, and these
objects are not operational:
• cbgpPeerPrefixAccepted
• cbgpPeerPrefixDenied
• cbgpPeerPrefixLimit
• cbgpPeerPrefixAdvertised
• cbgpPeerPrefixSuppressed
• cbgpPeerPrefixWithdrawn

How to Enable BGP MIB Support
Enabling BGP MIB Support
SNMP notifications can be configured on the router and GET operations can be performed from an external
management station only after BGP SNMP support is enabled. Perform this task on a router to configure
SNMP notifications for the BGP MIB.

IP Routing: BGP Configuration Guide
861


BGP MIB Support
Enabling BGP MIB Support

SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
snmp-server enable traps bgp [[state-changes [all] [backward-trans] [limited]] | [threshold prefix]]
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

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

snmp-server enable traps bgp [[state-changes [all]
[backward-trans] [limited]] | [threshold prefix]]
Example:
Device(config)# snmp-server enable traps bgp

Enables BGP support for SNMP operations. Entering this
command with no keywords or arguments enables support
for all BGP events.
• The state-changes keyword is used to enable support
for FSM transition events.
• The all keyword enables support for FSM transitions
events.
• The backward-trans keyword enables support only
for backward transition state change events.
• The limited keyword enables support for backward
transition state changes and established state events.
• The threshold and prefix keywords are used to enable
notifications when the configured maximum prefix
limit is reached on the specified peer.

Step 4

exit
Example:
Device(config)# exit

IP Routing: BGP Configuration Guide
862

Exits global configuration mode, and enters privileged
EXEC mode.


BGP MIB Support
Configuration Examples for BGP MIB Support

Configuration Examples for BGP MIB Support
Example: Enabling BGP MIB Support
The following example enables SNMP support for all supported BGP events:
Device(config)# snmp-server enable traps bgp

The following verification example shows that SNMP support for BGP is enabled by displaying any lines in
the running configuration file that include “snmp-server”:
Device# show run | include snmp-server
snmp-server enable traps bgp

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

IP Routing: BGP Command Reference

MIB objects supported in CISCO-BGP-MIBv8.1

“Cisco-BGP-MIBv2” module in the IP Routing: BGP
Configuration Guide

Information about SNMP and SNMP operations

SNMP Configuration Guide in the Network
Management Configuration Guide Library

MIBs
MIB

MIBs Link

CISCO-BGP4-MIB To locate and download MIBs for selected platforms, Cisco software releases, and
feature sets, use Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: BGP Configuration Guide
863


BGP MIB Support
Feature Information for BGP MIB Support

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

Feature Information for BGP MIB Support
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 70: Feature Information for BGP MIB Support

Feature Name

Releases

BGP MIB Support Enhancements 12.0(26)S
12.2(25)S
12.3(7)T
12.2(33)SRA
12.2(22)SXH
15.0(1)SY

IP Routing: BGP Configuration Guide
864

Feature Information
The BGP MIB Support
Enhancements feature introduced
support in the CISCO-BGP4-MIB
for new SNMP notifications.
The following command was
introduced: snmp-server enable
traps bgp.
