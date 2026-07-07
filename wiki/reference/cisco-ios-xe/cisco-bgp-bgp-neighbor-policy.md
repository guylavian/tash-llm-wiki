---
title: "BGP Neighbor Policy"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-neighbor-policy
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 17 BGP Neighbor Policy The BGP Neighbor Policy feature introduces new keywords to two existing commands to display information about local and inherited policies. When BGP neighbors use multiple levels of peer templates, it can be difficult to determine which policies are applied to the neighbor. Inherited policies are policies that the neighbor inherits from a peer group or a peer polic"
---

# BGP Neighbor Policy

CHAPTER

17

BGP Neighbor Policy
The BGP Neighbor Policy feature introduces new keywords to two existing commands to display information
about local and inherited policies. When BGP neighbors use multiple levels of peer templates, it can be difficult
to determine which policies are applied to the neighbor. Inherited policies are policies that the neighbor inherits
from a peer group or a peer policy template.
• Finding Feature Information, on page 399
• Information About BGP Neighbor Policy, on page 399
• How to Display BGP Neighbor Policy Information, on page 400
• Additional References, on page 400
• Feature Information for BGP Neighbor Policy, on page 401

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Neighbor Policy
Benefit of BGP Neighbor Policy Feature
The BGP Neighbor Policy feature introduces new keywords to the show ip bgp neighbors policy command
and the show ip bgp template peer-policy command to display information about local and inherited policies.
When BGP neighbors use multiple levels of peer templates, it can be difficult to determine which policies are
applied to the neighbor. Inherited policies are policies that the neighbor inherits from a peer group or a peer
policy template.

IP Routing: BGP Configuration Guide
399


BGP Neighbor Policy
How to Display BGP Neighbor Policy Information

How to Display BGP Neighbor Policy Information
Displaying BGP Neighbor Policy Information
SUMMARY STEPS
1. enable
2. show ip bgp neighbors { ip-address | ipv6-address } policy [ detail]
3. show ip bgp template peer-policy [ policy-template-name [ detail] ]
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

show ip bgp neighbors { ip-address | ipv6-address }
policy [ detail]

Displays the policies applied to the specified neighbor.

Example:
Device# show ip bgp neighbors 192.168.2.3 policy
detail

Step 3

show ip bgp template peer-policy [
policy-template-name [ detail] ]

Displays the locally configured peer policy templates.

Example:
Device# show ip bgp template peer-policy

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

BGP commands

Cisco IOS IP Routing: BGP
Command Reference

IP Routing: BGP Configuration Guide
400


BGP Neighbor Policy
Feature Information for BGP Neighbor Policy

Standards and RFCs
Standard/RFC Title
RFC 2918

Route Refresh Capability for BGP-4

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

Feature Information for BGP Neighbor Policy
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 33: Feature Information for BGP Neighbor Policy

Feature Name

Releases

Feature Information

BGP Neighbor Policy

12.2(33)SB

The BGP Neighbor Policy feature
introduces new keywords to two
existing commands to display
information about local and
inherited policies. When BGP
neighbors use multiple levels of
peer templates, it can be difficult to
determine which policies are
applied to the neighbor. Inherited
policies are policies that the
neighbor inherits from a peer-group
or a peer-policy template.

12.2(33)SRB

The following commands were
modified: show ip bgp neighbors,
and show ip bgp template
peer-policy.

IP Routing: BGP Configuration Guide
401


BGP Neighbor Policy
Feature Information for BGP Neighbor Policy

IP Routing: BGP Configuration Guide
402
