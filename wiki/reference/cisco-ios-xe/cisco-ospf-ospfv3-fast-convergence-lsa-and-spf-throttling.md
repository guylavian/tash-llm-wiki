---
title: "OSPFv3 Fast Convergence: LSA and SPF Throttling"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-fast-convergence-lsa-and-spf-throttling
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 28 OSPFv3 Fast Convergence: LSA and SPF Throttling The Open Shortest Path First version 3 (OSPFv3) link-state advertisement (LSAs) and shortest-path first (SPF) throttling feature provides a dynamic mechanism to slow down link-state advertisement updates in OSPFv3 during times of network instability. It also allows faster OSPFv3 convergence by providing LSA rate limiting in milliseconds."
---

# OSPFv3 Fast Convergence: LSA and SPF Throttling

CHAPTER

28

OSPFv3 Fast Convergence: LSA and SPF
Throttling
The Open Shortest Path First version 3 (OSPFv3) link-state advertisement (LSAs) and shortest-path first
(SPF) throttling feature provides a dynamic mechanism to slow down link-state advertisement updates in
OSPFv3 during times of network instability. It also allows faster OSPFv3 convergence by providing LSA
rate limiting in milliseconds.
• Finding Feature Information, page 271
• Information About OSPFv3 Fast Convergence: LSA and SPF Throttling, page 272
• How to Configure OSPFv3 Fast Convergence: LSA and SPF Throttling, page 272
• Configuration Examples for OSPFv3 Fast Convergence: LSA and SPF Throttling, page 275
• Additional References, page 275
• Feature Information for OSPFv3 Fast Convergence: LSA and SPF Throttling, page 276

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
271


OSPFv3 Fast Convergence: LSA and SPF Throttling
Information About OSPFv3 Fast Convergence: LSA and SPF Throttling

Information About OSPFv3 Fast Convergence: LSA and SPF
Throttling
Fast Convergence: LSA and SPF Throttling
The OSPFv3 LSA and SPF throttling feature provides a dynamic mechanism to slow down link-state
advertisement updates in OSPFv3 during times of network instability. It also allows faster OSPFv3 convergence
by providing LSA rate limiting in milliseconds.
OSPFv3 can use static timers for rate-limiting SPF calculation and LSA generation. Although these timers
are configurable, the values used are specified in seconds, which poses a limitation on OSPFv3 convergence.
LSA and SPF throttling achieves subsecond convergence by providing a more sophisticated SPF and LSA
rate-limiting mechanism that is able to react quickly to changes and also provide stability and protection during
prolonged periods of instability.

How to Configure OSPFv3 Fast Convergence: LSA and SPF
Throttling
Tuning LSA and SPF Timers for OSPFv3 Fast Convergence
This task can be performed in Cisco IOS Release 15.1(3)S and 15.2(1)T and later releases.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. timers lsa arrival milliseconds
5. timers pacing flood milliseconds
6. timers pacing lsa-group seconds
7. timers pacing retransmission milliseconds

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device> enable

IP Routing: OSPF Configuration Guide
272

• Enter your password if prompted.


OSPFv3 Fast Convergence: LSA and SPF Throttling
Configuring LSA and SPF Throttling for OSPFv3 Fast Convergence

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for the IPv4
or IPv6 address family.

Example:
Device(config)# router ospfv3 1

Step 4

timers lsa arrival milliseconds

Sets the minimum interval at which the software accepts
the same LSA from OSPFv3 neighbors.

Example:
Device(config-rtr)# timers lsa arrival 300

Step 5

timers pacing flood milliseconds

Configures LSA flood packet pacing.

Example:
Device(config-rtr)# timers pacing flood 30

Step 6

timers pacing lsa-group seconds

Changes the interval at which OSPFv3 LSAs are collected
into a group and refreshed, checksummed, or aged.

Example:
Device(config-router)# timers pacing lsa-group
300

Step 7

timers pacing retransmission milliseconds

Configures LSA retransmission packet pacing in IPv4
OSPFv3.

Example:
Device(config-router)# timers pacing
retransmission 100

Configuring LSA and SPF Throttling for OSPFv3 Fast Convergence
This task can be performed in releases prior to Cisco IOS Release 15.1(3)S and 15.2(1)T.

IP Routing: OSPF Configuration Guide
273


OSPFv3 Fast Convergence: LSA and SPF Throttling
Configuring LSA and SPF Throttling for OSPFv3 Fast Convergence

SUMMARY STEPS
1. enable
2. configure terminal
3. ipv6 router ospf process-id
4. timers throttle spf spf-start spf-hold spf-max-wait
5. timers throttle lsa start-interval hold-interval max-interval
6. timers lsa arrival milliseconds
7. timers pacing flood milliseconds

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

ipv6 router ospf process-id

Enables OSPFv3 router configuration mode.

Example:
Device(config)# ipv6 router ospf 1

Step 4

timers throttle spf spf-start spf-hold spf-max-wait

Turns on SPF throttling.

Example:
Device(config-rtr)# timers throttle spf 200 200 200

Step 5

timers throttle lsa start-interval hold-interval max-interval Sets rate-limiting values for OSPFv3 LSA
generation.
Example:
Device(config-rtr)# timers throttle lsa 300 300 300

Step 6

timers lsa arrival milliseconds
Example:
Device(config-rtr)# timers lsa arrival 300

IP Routing: OSPF Configuration Guide
274

Sets the minimum interval at which the software
accepts the same LSA from OSPFv3 neighbors.


OSPFv3 Fast Convergence: LSA and SPF Throttling
Configuration Examples for OSPFv3 Fast Convergence: LSA and SPF Throttling

Step 7

Command or Action

Purpose

timers pacing flood milliseconds

Configures LSA flood packet pacing.

Example:
Device(config-rtr)# timers pacing flood 30

Configuration Examples for OSPFv3 Fast Convergence: LSA and
SPF Throttling
Example: Configuring LSA and SPF Throttling for OSPFv3 Fast Convergence
The following example show how to display the configuration values for SPF and LSA throttling timers:
Device# show ipv6 ospf
Routing Process "ospfv3 1" with ID 10.9.4.1
Event-log enabled, Maximum number of events: 1000, Mode: cyclic
It is an autonomous system boundary router
Redistributing External Routes from,
ospf 2
Initial SPF schedule delay 5000 msecs
Minimum hold time between two consecutive SPFs 10000 msecs
Maximum wait time between two consecutive SPFs 10000 msecs
Minimum LSA interval 5 secs
Minimum LSA arrival 1000 msecs

Additional References
Related Documents
Related Topic

Document Title

IPv6 addressing and connectivity

IPv6 Configuration Guide

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

IPv6 commands

Cisco IOS IPv6 Command
Reference

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

IP Routing: OSPF Configuration Guide
275


OSPFv3 Fast Convergence: LSA and SPF Throttling
Feature Information for OSPFv3 Fast Convergence: LSA and SPF Throttling

Related Topic

Document Title

OSPFv3 Fast Convergence: LSA and SPF Throttling

“OSPF Link-State Advertisement
Throttling ” module

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

Feature Information for OSPFv3 Fast Convergence: LSA and SPF
Throttling
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
276


OSPFv3 Fast Convergence: LSA and SPF Throttling
Feature Information for OSPFv3 Fast Convergence: LSA and SPF Throttling

Table 31: Feature Information for OSPFv3 Fast Convergence: LSA and SPF Throttling

Feature Name

Releases

Feature Information

OSPFv3 Fast Convergence: LSA
and SPF Throttling

Cisco IOS XE Release 2.1

The OSPFv3 LSA and SPF
throttling feature provides a
dynamic mechanism to slow down
link-state advertisement updates in
OSPFv3 during times of network
instability.

IP Routing: OSPF Configuration Guide
277


OSPFv3 Fast Convergence: LSA and SPF Throttling
Feature Information for OSPFv3 Fast Convergence: LSA and SPF Throttling

IP Routing: OSPF Configuration Guide
278
