---
title: "OSPF Incremental SPF"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-incremental-spf
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 26 OSPF Incremental SPF The Open Shortest Path First (OSPF) protocol can be configured to use an incremental SPF algorithm for calculating the shortest path first routes. Incremental SPF is more efficient than the full SPF algorithm, thereby allowing OSPF to converge faster on a new routing topology in reaction to a network event. • Finding Feature Information, page 257 • Prerequisites f"
---

# OSPF Incremental SPF

CHAPTER

26

OSPF Incremental SPF
The Open Shortest Path First (OSPF) protocol can be configured to use an incremental SPF algorithm for
calculating the shortest path first routes. Incremental SPF is more efficient than the full SPF algorithm,
thereby allowing OSPF to converge faster on a new routing topology in reaction to a network event.
• Finding Feature Information, page 257
• Prerequisites for OSPF Incremental SPF, page 257
• Information About OSPF Incremental SPF, page 258
• How to Enable OSPF Incremental SPF, page 258
• Configuration Examples for OSPF Incremental SPF, page 259
• Additional References, page 259
• Feature Information for OSPF Incremental SPF, page 260

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPF Incremental SPF
It is presumed that you have OSPF configured in your network.

IP Routing: OSPF Configuration Guide
257


OSPF Incremental SPF
Information About OSPF Incremental SPF

Information About OSPF Incremental SPF
OSPF uses Dijkstra’s SPF algorithm to compute the shortest path tree (SPT). During the computation of the
SPT, the shortest path to each node is discovered. The topology tree is used to populate the routing table with
routes to IP networks. When changes to a Type-1 or Type-2 link-state advertisement (LSA) occur in an area,
the entire SPT is recomputed. In many cases, the entire SPT need not be recomputed because most of the tree
remains unchanged. Incremental SPF allows the system to recompute only the affected part of the tree.
Recomputing only a portion of the tree rather than the entire tree results in faster OSPF convergence and saves
CPU resources. Note that if the change to a Type-1 or Type-2 LSA occurs in the calculating router itself, then
the full SPT is performed.
Incremental SPF is scheduled in the same way as the full SPF. Routers enabled with incremental SPF and
routers not enabled with incremental SPF can function in the same internetwork.

How to Enable OSPF Incremental SPF
Enabling Incremental SPF
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. ispf
5. end

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
Example:
Router# configure terminal

IP Routing: OSPF Configuration Guide
258

Enters global configuration mode.


OSPF Incremental SPF
Configuration Examples for OSPF Incremental SPF

Step 3

Command or Action

Purpose

router ospf process-id

Configures an OSPF routing process.

Example:
Router(config)# router ospf 1

Step 4

ispf

Enables incremental SPF.

Example:
Router(config-router)# ispf

Step 5

end

Exits router configuration mode.

Example:
Router(config-router)# end

Configuration Examples for OSPF Incremental SPF
Example Incremental SPF
This example enables incremental SPF:
router ospf 1
ispf

Additional References
The following sections provide references related to OSPF Incremental SPF.
Related Documents
Related Topic

Document Title

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Configuring OSPF

"Configuring OSPF"

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

IP Routing: OSPF Configuration Guide
259


OSPF Incremental SPF
Feature Information for OSPF Incremental SPF

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

No new or modified RFCs are supported by this
feature, and support for existing RFCs has not been
modified by this feature.

--

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

Feature Information for OSPF Incremental SPF
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.

IP Routing: OSPF Configuration Guide
260


OSPF Incremental SPF
Feature Information for OSPF Incremental SPF

Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 29: Feature Information for OSPF Incremental SPF

Feature Name

Releases

Feature Information

OSPF Incremental SPF

Cisco IOS XE Release 2.1

OSPF can be configured to use an
incremental SPF algorithm for
calculating the shortest path first
routes. Incremental SPF is more
efficient than the full SPF
algorithm, thereby allowing OSPF
to converge faster on a new routing
topology in reaction to a network
event
The following commands are
introduced or modified in the
feature documented in this module:
• ispf

IP Routing: OSPF Configuration Guide
261


OSPF Incremental SPF
Feature Information for OSPF Incremental SPF

IP Routing: OSPF Configuration Guide
262
