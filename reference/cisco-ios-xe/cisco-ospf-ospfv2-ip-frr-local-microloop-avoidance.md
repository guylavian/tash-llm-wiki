---
title: "OSPFv2 IP FRR Local Microloop Avoidance"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv2-ip-frr-local-microloop-avoidance
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 19 OSPFv2 IP FRR Local Microloop Avoidance The OSPFv2 IP FRR Local Microloop Avoidance feature helps to avoid local microloop that happens between a node and its neighbor where the link-down event occurred. This document explains how to configure the OSPFv2 IP FRR Local Microloop Avoidance feature. • Finding Feature Information, page 207 • Information About OSPFv2 IP FRR Local Microloop"
---

# OSPFv2 IP FRR Local Microloop Avoidance

CHAPTER

19

OSPFv2 IP FRR Local Microloop Avoidance
The OSPFv2 IP FRR Local Microloop Avoidance feature helps to avoid local microloop that happens between
a node and its neighbor where the link-down event occurred. This document explains how to configure the
OSPFv2 IP FRR Local Microloop Avoidance feature.
• Finding Feature Information, page 207
• Information About OSPFv2 IP FRR Local Microloop Avoidance, page 207
• How to Configure OSPFv2 IP FRR Local Microloop Avoidance, page 208
• Configuration Examples for OSPFv2 IP FRR Local Microloop Avoidance, page 209
• Additional References for OSPFv2 IP FRR Local Microloop Avoidance, page 210
• Feature Information for OSPFv2 IP FRR Local Microloop Avoidance, page 210

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPFv2 IP FRR Local Microloop Avoidance
Overview of OSPFv2 IP FRR Local Microloop Avoidance
IP fast reroute (IPFRR) provides rapid convergence during the link-down events by moving the traffic to a
pre computed backup path until the regular convergence mechanisms move the traffic to the newly found best
path referred to as the post-convergence path.

IP Routing: OSPF Configuration Guide
207


OSPFv2 IP FRR Local Microloop Avoidance
How to Configure OSPFv2 IP FRR Local Microloop Avoidance

Once the traffic is moved to the post-convergence path, it is inclined to a microloop. Microloops are formed
as a result of the fact that each node on the path does its calculation at different times and independently of
other nodes. If certain nodes converge and sends traffic to a neighbor node, which has not converged yet,
traffic may be looped between these two nodes.
Microloops are formed between the router where the failure is detected and its neighbors. Local microloops
are created in cases where there is no local loop-free alternate (LFA) backup available in ring or square
topologies. In such topologies, remote LFA provides a backup, but the fast-convergence benefit of the remote
LFA cannot be completely utilized due to the high probability of the local microloop creation. Avoiding the
local micro loop provides a significant improvement in the fast convergence in the ring and square topologies.

Note

Microloop avoidance is automatically enabled as soon as remote LFA (rLFA) is enabled.
When using microloop avoidance for prefixes (for which a repair path has been installed in the forwarding
plane), the OSPFv2 IP FRR Local Microloop Avoidance feature is enabled when the forwarding plane is
triggered to switch to using a pre installed repair path. The local microloop avoidance for the link-down event
supports the following triggers:
• Interface down event.
• Adjacency down event due to the Bidirectional Forwarding Detection (BFD) session down.
If microloop avoidance is used regardless of whether a repair path has been installed in the forwarding plane,
then in addition the third trigger is used:
• Adjacency down event due to neighbor hold time expiration.
When the neighbor reports loss of adjacency to the local system in its link state neighbor advertisements, the
value of using microloop avoidance depends on whether the remote event that caused loss of adjacency on
the neighbor is detectable by the local forwarding plane (that is, whether the forwarding plane will react and
switch to using pre programmed repair paths).

How to Configure OSPFv2 IP FRR Local Microloop Avoidance
Configuring OSPFv2 IP FRR Local Microloop Avoidance
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. microloop avoidance [protected | disable]
5. microloop avoidance rib-update-delay delay-period
6. exit

IP Routing: OSPF Configuration Guide
208


OSPFv2 IP FRR Local Microloop Avoidance
Configuration Examples for OSPFv2 IP FRR Local Microloop Avoidance

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

router ospf process-id

Configures an OSPF routing process and enters router
configuration mode.

Example:
Device(config)# router ospf 109

Step 4

microloop avoidance [protected | disable]
Example:
Device(config-router)# microloop avoidance
protected

Configures the local microloop avoidance between a node and its
neighbor where the link-down event has occurred.
• When the protected keyword is used, the local microloop
avoidance is only applied to prefixes that have a valid backup
path.
• When the disable keyword is used, the local microloop
avoidance is disabled if it is enabled automatically earlier.

Step 5

microloop avoidance rib-update-delay
delay-period

Delays the local microloop avoidance as per the configured delay
period.

Example:
Device(config-router)# microloop avoidance
rib-update-delay 6500

Step 6

Exits router configuration mode and returns to privileged EXEC
mode.

exit
Example:
Device(config-router)# exit

Configuration Examples for OSPFv2 IP FRR Local Microloop
Avoidance
Example: Configuring OSPFv2 IP FRR Local Microloop Avoidance
router ospf 10
microloop avoidance protected

IP Routing: OSPF Configuration Guide
209


OSPFv2 IP FRR Local Microloop Avoidance
Additional References for OSPFv2 IP FRR Local Microloop Avoidance

microloop avoidance rib-update-delay 6500
!

Additional References for OSPFv2 IP FRR Local Microloop
Avoidance
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

Configuring OSPF features

IP Routing: OSPF Configuration Guide

Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/support
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies.
To receive security and technical information about
your products, you can subscribe to various services,
such as the Product Alert Tool (accessed from Field
Notices), the Cisco Technical Services Newsletter,
and Really Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website
requires a Cisco.com user ID and password.

Feature Information for OSPFv2 IP FRR Local Microloop
Avoidance
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
210


OSPFv2 IP FRR Local Microloop Avoidance
Feature Information for OSPFv2 IP FRR Local Microloop Avoidance

Table 22: Feature Information for OSPFv2 IP FRR Local Microloop Avoidance

Feature Name

Releases

Feature Information

OSPFv2 IP FRR Local Microloop Cisco IOS XE Release 3.11S
Avoidance
15.4(1)S

The OSPFv2 IP FRR Local
Microloop Avoidance feature helps
to avoid local microloop that
happens between a node and its
neighbor where the link-down
event occurred.
The following commands were
introduced or modified: microloop
avoidance, microloop avoidance
rib-update-delay.

IP Routing: OSPF Configuration Guide
211


OSPFv2 IP FRR Local Microloop Avoidance
Feature Information for OSPFv2 IP FRR Local Microloop Avoidance

IP Routing: OSPF Configuration Guide
212
