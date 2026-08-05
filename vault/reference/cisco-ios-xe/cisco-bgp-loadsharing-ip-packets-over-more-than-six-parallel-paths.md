---
title: "Loadsharing IP Packets over More Than Six Parallel Paths"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-loadsharing-ip-packets-over-more-than-six-parallel-paths
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 34 Loadsharing IP Packets over More Than Six Parallel Paths This document describes the Loadsharing IP Packets over More Than Six Parallel Paths feature, which increases the maximum number of parallel routes that can be installed to the routing table for multipath loadsharing. • Finding Feature Information, on page 585 • Overview of Loadsharing IP Packets over More Than Six Parallel Path"
---

# Loadsharing IP Packets over More Than Six Parallel Paths

CHAPTER

34

Loadsharing IP Packets over More Than Six
Parallel Paths
This document describes the Loadsharing IP Packets over More Than Six Parallel Paths feature, which increases
the maximum number of parallel routes that can be installed to the routing table for multipath loadsharing.
• Finding Feature Information, on page 585
• Overview of Loadsharing IP Packets over More Than Six Parallel Paths, on page 585
• Additional References, on page 586
• Feature Information for Loadsharing IP Packets over More Than Six Parallel Paths, on page 587

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Overview of Loadsharing IP Packets over More Than Six
Parallel Paths
The Loadsharing IP Packets over More Than Six Parallel Paths feature increases the maximum number of
parallel routes that can be installed to the routing table. The maximum number has been increased from six
to sixteen for the following commands:
• maximum-paths
• maximum-paths eibgp
• maximum-paths ibgp
The output of the show ip route summary command has been updated to display the number of parallel
routes supported by the routing table.

IP Routing: BGP Configuration Guide
585


Loadsharing IP Packets over More Than Six Parallel Paths
Additional References

The benefits of this feature include the following:
• More flexible configuration of parallel routes in the routing table.
• Ability to configure multipath loadsharing over more links to allow for the configuration of
higher-bandwidth aggregation using lower-speed links.

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

eBGP multipath load sharing “BGP Multipath Load Sharing for Both eBGP and iBGP in an MPLS-VPN”
module
iBGP multipath load sharing “iBGP Multipath Load Sharing” module
MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this To locate and download MIBs for selected platforms, Cisco
feature, and support for existing MIBs has not IOS XE software releases, and feature sets, use Cisco MIB
been modified by this feature.
Locator found at the following URL:
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

IP Routing: BGP Configuration Guide
586


Loadsharing IP Packets over More Than Six Parallel Paths
Feature Information for Loadsharing IP Packets over More Than Six Parallel Paths

Feature Information for Loadsharing IP Packets over More Than
Six Parallel Paths
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 50: Feature Information for Loadsharing IP Packets over More Than Six Parallel Paths

Feature Name

Releases

Loadsharing IP Packets over Cisco IOS XE
More Than Six Parallel Paths Release 2.1

Feature Information
This feature was introduced on the Cisco ASR 1000
Series Aggregation Services Routers.
The following commands were modified by this feature:
maximum-paths, maximum-paths eibgp,
maximum-paths ibgp, show ip route summary

IP Routing: BGP Configuration Guide
587


Loadsharing IP Packets over More Than Six Parallel Paths
Feature Information for Loadsharing IP Packets over More Than Six Parallel Paths

IP Routing: BGP Configuration Guide
588
