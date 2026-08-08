---
title: "OSPFv3 External Path Preference Option"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-external-path-preference-option
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 6 OSPFv3 External Path Preference Option The Open Shortest Path First version 3 (OSPFv3) external path preference option feature provides a way to calculate external path preferences per RFC 5340. • Finding Feature Information, page 89 • Information About OSPFv3 External Path Preference Option, page 89 • How to Calculate OSPFv3 External Path Preference Option, page 90 • Configuration Exa"
---

# OSPFv3 External Path Preference Option

CHAPTER

6

OSPFv3 External Path Preference Option
The Open Shortest Path First version 3 (OSPFv3) external path preference option feature provides a way to
calculate external path preferences per RFC 5340.
• Finding Feature Information, page 89
• Information About OSPFv3 External Path Preference Option, page 89
• How to Calculate OSPFv3 External Path Preference Option, page 90
• Configuration Examples for OSPFv3 External Path Preference Option, page 91
• Additional References, page 91
• Feature Information for OSPFv3 External Path Preference Option, page 92

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPFv3 External Path Preference Option
OSPFv3 External Path Preference Option
Per RFC 5340, the following rules indicate which paths are preferred when multiple intra-AS paths are available
to ASBRs or forwarding addresses:
• Intra-area paths using nonbackbone areas are always the most preferred.
• The other paths, intraarea backbone paths and interarea paths, are of equal preference.

IP Routing: OSPF Configuration Guide
89


OSPFv3 External Path Preference Option
How to Calculate OSPFv3 External Path Preference Option

These rules apply when the same ASBR is reachable through multiple areas, or when trying to decide which
of several AS-external-LSAs should be preferred. In the former case the paths all terminate at the same ASBR,
and in the latter the paths terminate at separate ASBRs or forwarding addresses. In either case, each path is
represented by a separate routing table entry. This feature applies only when RFC 1583 compatibility is set
to disabled using the no compatibility rfc1583 command (RFC 5340 provides an update to RFC 1583).

Caution

To minimize the chance of routing loops, set identical RFC compatibility for all OSPF routers in an OSPF
routing domain.

How to Calculate OSPFv3 External Path Preference Option
Calculating OSPFv3 External Path Preferences per RFC 5340
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. no compatible rfc1583

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

router ospfv3 [process-id]
Example:
Device(config)# router ospfv3 1

IP Routing: OSPF Configuration Guide
90

Enables OSPFv3 router configuration mode for the IPv4
or IPv6 address family.


OSPFv3 External Path Preference Option
Configuration Examples for OSPFv3 External Path Preference Option

Step 4

Command or Action

Purpose

no compatible rfc1583

Changes the method used to calculate external path
preferences per RFC 5340.

Example:
Device(config-router)# no compatible rfc1583

Configuration Examples for OSPFv3 External Path Preference
Option
Example: Calculating OSPFv3 External Path Preferences per RFC 5340
show ospfv3
Routing Process "ospfv3 1" with ID 10.1.1.1
SPF schedule delay 5 secs, Hold time between two SPFs 10 secs
Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs
LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
Number of external LSA 0. Checksum Sum 0x000000
Number of areas in this router is 1. 1 normal 0 stub 0 nssa
Reference bandwidth unit is 100 mbps
RFC 1583 compatibility disabled
Area BACKBONE(0) (Inactive)
Number of interfaces in this area is 1
SPF algorithm executed 1 times
Number of LSA 1. Checksum Sum 0x00D03D
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0

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

IP Routing: OSPF Configuration Guide
91


OSPFv3 External Path Preference Option
Feature Information for OSPFv3 External Path Preference Option

Related Topic

Document Title

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

OSPFv3 External Path Preference Option

“Configuring OSPF ” module

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

Feature Information for OSPFv3 External Path Preference Option
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
92


OSPFv3 External Path Preference Option
Feature Information for OSPFv3 External Path Preference Option

Table 9: Feature Information for OSPFv3 External Path Preference Option

Feature Name

Releases

Feature Information

OSPFv3 External Path Preference Cisco IOS XE Release 3.4S
Option

This feature provides a way to
calculate external path preferences
per RFC 5340.
The following commands were
introduced or modified:
compatible rfc1583, show ospfv3.

IP Routing: OSPF Configuration Guide
93


OSPFv3 External Path Preference Option
Feature Information for OSPFv3 External Path Preference Option

IP Routing: OSPF Configuration Guide
94
