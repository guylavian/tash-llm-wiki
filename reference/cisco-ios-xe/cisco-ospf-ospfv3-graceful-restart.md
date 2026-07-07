---
title: "OSPFv3 Graceful Restart"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-graceful-restart
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 7 OSPFv3 Graceful Restart The graceful restart feature in Open Shortest Path First version 3 (OSPFv3) allows nonstop data forwarding along routes that are already known while the OSPFv3 routing protocol information is being restored. • Finding Feature Information, page 95 • Information About OSPFv3 Graceful Restart, page 95 • How to Enable OSPFv3 Graceful Restart, page 96 • Configuration"
---

# OSPFv3 Graceful Restart

CHAPTER

7

OSPFv3 Graceful Restart
The graceful restart feature in Open Shortest Path First version 3 (OSPFv3) allows nonstop data forwarding
along routes that are already known while the OSPFv3 routing protocol information is being restored.
• Finding Feature Information, page 95
• Information About OSPFv3 Graceful Restart, page 95
• How to Enable OSPFv3 Graceful Restart, page 96
• Configuration Examples for OSPFv3 Graceful Restart, page 100
• Additional References, page 100
• Feature Information for OSPFv3 Graceful Restart, page 102

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPFv3 Graceful Restart
OSPFv3 Graceful Restart
The graceful restart feature in OSPFv3 allows nonstop data forwarding along routes that are already known
while the OSPFv3 routing protocol information is being restored. A device can participate in graceful restart
either in restart mode (such as in a graceful-restart-capable device) or in helper mode (such as in a
graceful-restart-aware device).

IP Routing: OSPF Configuration Guide
95


OSPFv3 Graceful Restart
How to Enable OSPFv3 Graceful Restart

To perform the graceful restart function, a device must be in high availability (HA) stateful switchover (SSO)
mode (that is, dual Route Processor (RP)). A device capable of graceful restart will perform the graceful restart
function when the following failures occur:
• A RP failure that results in switchover to standby RP
• A planned RP switchover to standby RP
The graceful restart feature requires that neighboring devices be graceful-restart aware.
For further information about SSO and nonstop forwarding (NSF), see the Stateful Switchover and Cisco
Nonstop Forwarding documents.

How to Enable OSPFv3 Graceful Restart
Enabling OSPFv3 Graceful Restart on a Graceful-Restart-Capable Router
The task can be performed in Cisco IOS XE 3.4S and later releases.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. graceful-restart [restart-interval interval]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospfv3 [process-id]
Example:
Router(config)# router ospfv3 1

IP Routing: OSPF Configuration Guide
96

Enables OSPFv3 router configuration mode for the IPv4
or IPv6 address family.


OSPFv3 Graceful Restart
Enabling OSPFv3 Graceful Restart on a Graceful-Restart-Capable Router

Step 4

Command or Action

Purpose

graceful-restart [restart-interval interval]

Enables the OSPFv3 graceful restart feature on a
graceful-restart-capable router.

Example:
Router(config-rtr)# graceful-restart

Enabling OSPFv3 Graceful Restart on a Graceful-Restart-Capable Router
The task can be performed in releases prior to Cisco IOS XE Release 3.4S.

SUMMARY STEPS
1. enable
2. configure terminal
3. ipv6 router ospf process-id
4. graceful-restart [restart-interval interval]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

ipv6 router ospf process-id

Enables OSPFv3 router configuration mode.

Example:
Router(config)# ipv6 router ospf 1

Step 4

graceful-restart [restart-interval interval]

Enables the OSPFv3 graceful restart feature on a
graceful-restart-capable router.

Example:
Router(config-rtr)# graceful-restart

IP Routing: OSPF Configuration Guide
97


OSPFv3 Graceful Restart
Enabling OSPFv3 Graceful Restart on a Graceful-Restart-Aware Router

Enabling OSPFv3 Graceful Restart on a Graceful-Restart-Aware Router
The task can be performed in Cisco IOS XE Release 3.4S and later releases.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. graceful-restart helper {disable | strict-lsa-checking

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for the IPv4
or IPv6 address family.

Example:
Router(config)# router ospfv3 1

Step 4

graceful-restart helper {disable | strict-lsa-checking Enables the OSPFv3 graceful restart feature on a
graceful-restart-aware router.
Example:
Router(config-rtr)# graceful-restart helper
strict-lsa-checking

IP Routing: OSPF Configuration Guide
98


OSPFv3 Graceful Restart
Enabling OSPFv3 Graceful Restart on a Graceful-Restart-Aware Router

Example:

What to Do Next

Enabling OSPFv3 Graceful Restart on a Graceful-Restart-Aware Router
The task can be performed in releases prior to Cisco IOS XE Release 3.4S.

SUMMARY STEPS
1. enable
2. configure terminal
3. ipv6 router ospf process-id
4. graceful-restart helper {disable | strict-lsa-checking

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

ipv6 router ospf process-id

Enables OSPFv3 router configuration mode.

Example:
Router(config)# ipv6 router ospf 1

Step 4

graceful-restart helper {disable | strict-lsa-checking

Enables the OSPFv3 graceful restart feature on a
graceful-restart-aware router.

Example:
Router(config-rtr)# graceful-restart helper
strict-lsa-checking

IP Routing: OSPF Configuration Guide
99


OSPFv3 Graceful Restart
Configuration Examples for OSPFv3 Graceful Restart

Example:

What to Do Next

Configuration Examples for OSPFv3 Graceful Restart
Example: Enabling OSPFv3 Graceful Restart
Router# show ipv6 ospf graceful-restart
Routing Process "ospf 1"
Graceful Restart enabled
restart-interval limit: 120 sec, last restart 00:00:15 ago (took 36 secs)
Graceful Restart helper support enabled
Router status : Active
Router is running in SSO mode
OSPF restart state : NO_RESTART
Router ID 10.1.1.1, checkpoint Router ID 10.0.0.0

The following example shows OSPFv3 information with graceful-restart helper support enabled on a
graceful-restart-aware router.
Router# show ospfv3
Routing Process "ospfv3 1" with ID 10.0.0.1
Supports IPv6 Address Family
Event-log enabled, Maximum number of events: 1000, Mode: cyclic
Initial SPF schedule delay 5000 msecs
Minimum hold time between two consecutive SPFs 10000 msecs
Maximum wait time between two consecutive SPFs 10000 msecs
Minimum LSA interval 5 secs
Minimum LSA arrival 1000 msecs
LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
Number of external LSA 0. Checksum Sum 0x000000
Number of areas in this router is 0. 0 normal 0 stub 0 nssa
Graceful restart helper support enabled
Reference bandwidth unit is 100 mbps
Relay willingness value is 128
Pushback timer value is 2000 msecs
Relay acknowledgement timer value is 1000 msecs
LSA cache Disabled : current count 0, maximum 1000
ACK cache Disabled : current count 0, maximum 1000
Selective Peering is not enabled
Hello requests and responses will be sent multicast

Additional References
Related Documents
Related Topic

Document Title

IPv6 addressing and connectivity

IPv6 Configuration Guide

Stateful switchover and Cisco nonstop forwarding

High Availability Configuration
Guide

IP Routing: OSPF Configuration Guide
100


OSPFv3 Graceful Restart
Additional References

Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

IPv6 commands

Cisco IOS IPv6 Command
Reference

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

OSPFv3 Graceful Restart

“OSPF RFC 3623 Graceful Restart
Helper Mode” module

OSPFv3 Graceful Restart

“Configuring OSPF ” module

OSPFv3 Graceful Restart

“NSF-OSPF RFC 3623 OSPF
Graceful Restart ” module

Standards and RFCs
Standard/RFC

Title

RFCs for IPv6

IPv6 RFCs

MIBs
MIB

MIBs Link
To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

Technical Assistance
Description

Link

The Cisco Support and Documentation website
http://www.cisco.com/cisco/web/support/index.html
provides online resources to download documentation,
software, and tools. Use these resources to install and
configure the software and to troubleshoot and resolve
technical issues with Cisco products and technologies.
Access to most tools on the Cisco Support and
Documentation website requires a Cisco.com user ID
and password.

IP Routing: OSPF Configuration Guide
101


OSPFv3 Graceful Restart
Feature Information for OSPFv3 Graceful Restart

Feature Information for OSPFv3 Graceful Restart
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 10: Feature Information for OSPFv3 Graceful Restart

Feature Name

Releases

Feature Information

OSPFv3 Graceful Restart

Cisco IOS XE Release 2.1

The graceful restart feature in
OSPFv3 allows nonstop data
forwarding along routes that are
already known while the OSPFv3
routing protocol information is
being restored.
The following commands were
introduced or modified:
graceful-restart, graceful-restart
helper, ipv6 router ospf, router
ospfv3, show ipv6 ospf
graceful-restart, show ospfv3
graceful-restart.

IP Routing: OSPF Configuration Guide
102
