---
title: "OSPF Area Transit Capability"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-area-transit-capability
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 32 OSPF Area Transit Capability The OSPF Area Transit Capability feature provides an OSPF Area Border Router (ABR) with the ability to discover shorter paths through the transit area for forwarding traffic that would normally need to travel through the virtual-link path. This functionality allows Cisco IOS XE software to be compliant with RFC 2328, OSPF Version 2. • Finding Feature Infor"
---

# OSPF Area Transit Capability

CHAPTER

32

OSPF Area Transit Capability
The OSPF Area Transit Capability feature provides an OSPF Area Border Router (ABR) with the ability to
discover shorter paths through the transit area for forwarding traffic that would normally need to travel
through the virtual-link path. This functionality allows Cisco IOS XE software to be compliant with RFC
2328, OSPF Version 2.
• Finding Feature Information, page 303
• Information About OSPF Area Transit Capability, page 303
• How to Disable OSPF Area Transit Capability, page 304
• Additional References, page 304
• Feature Information for OSPF Area Transit Capability, page 306

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPF Area Transit Capability
How the OSPF Area Transit Capability Feature Works
The OSPF Area Transit Capability feature is enabled by default. RFC 2328 defines OSPF area transit capability
as the ability of the area to carry data traffic that neither originates nor terminates in the area itself. This
capability enables the OSPF ABR to discover shorter paths through the transit area and to forward traffic
along those paths rather than using the virtual link or path, which is not optimal.
For a detailed description of OSPF area transit capability, see RFC 2328, OSPF Version 2 .

IP Routing: OSPF Configuration Guide
303


OSPF Area Transit Capability
How to Disable OSPF Area Transit Capability

How to Disable OSPF Area Transit Capability
Disabling OSPF Area Transit Capability on an Area Border Router
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id [vrf vpn-name]
4. no capability transit

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

router ospf process-id [vrf vpn-name]
Example:

Enables OSPF routing and enters router configuration mode.
• The process-id argument identifies the OSPF process.

Router(config)# router ospf 100

Step 4

no capability transit

Disables OSPF area transit capability on all areas for a router
process.

Example:
Router(config-router)# no capability transit

Additional References
The following sections provide references related to the OSPF Area Transit Capability feature.

IP Routing: OSPF Configuration Guide
304


OSPF Area Transit Capability
Additional References

Related Documents
Related Topic

Document Title

Configuring OSPF

"Configuring OSPF"

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standard

Title

No new or modified standards are supported by this -feature, and support for existing standards has not
been modified by this feature.

MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS XE releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

RFC 2328

OSPF Version 2

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
305


OSPF Area Transit Capability
Feature Information for OSPF Area Transit Capability

Feature Information for OSPF Area Transit Capability
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 35: Feature Information for OSPF Area Transit Capability

Feature Name

Releases

Feature Information

OSPF Area Transit Capability

Cisco IOS XE Release 2.1

The OSPF Area Transit Capability
feature provides an OSPF Area
Border Router (ABR) the ability to
discover shorter paths through the
transit area for forwarding traffic
that would normally need to travel
through the virtual-link path. This
functionality allows Cisco IOS XE
software to be compliant with RFC
2328.
The command related to this
feature is
• capability transit

IP Routing: OSPF Configuration Guide
306
