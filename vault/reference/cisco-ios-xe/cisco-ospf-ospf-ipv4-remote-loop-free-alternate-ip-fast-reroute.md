---
title: "OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-ipv4-remote-loop-free-alternate-ip-fast-reroute
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 52 OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute OSPF IPv4 remote loop-free alternate (LFA) IP fast reroute (IPFRR) uses a backup route, precomputed using the dynamic routing protocol, whenever a network fails. The backup routes (repair paths) are pre-computed and installed in the router as the backup for the primary paths. Once the router detects a link or adjacent node failure,"
---

# OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

CHAPTER

52

OSPF IPv4 Remote Loop-Free Alternate IP Fast
Reroute
OSPF IPv4 remote loop-free alternate (LFA) IP fast reroute (IPFRR) uses a backup route, precomputed
using the dynamic routing protocol, whenever a network fails. The backup routes (repair paths) are
pre-computed and installed in the router as the backup for the primary paths. Once the router detects a link
or adjacent node failure, it switches to the backup path to avoid traffic loss.
OSPF IPv4 remote LFA IPFRR allows the backup path to be more than one hop away. This feature is
particularly useful in some topologies (such as the commonly used ring topology) where an LFA does not
have to be directly connected to the protecting router.
• Finding Feature Information, page 487
• Prerequisites for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute, page 488
• Restrictions for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute, page 488
• Information About OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute, page 489
• How to Configure OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute, page 490
• Configuration Examples for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute, page 493
• Additional References, page 493
• Feature Information for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute, page 494

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
487


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Prerequisites for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

Prerequisites for OSPF IPv4 Remote Loop-Free Alternate IP Fast
Reroute
• Before performing the tasks in this module, you should be familiar with the concepts described in the
“OSPFv2 Loop-Free Alternate Fast Reroute” module.
• LFA must be enabled.
• Your network must be configured for Multiprotocol Label Switching (MPLS).

Restrictions for OSPF IPv4 Remote Loop-Free Alternate IP Fast
Reroute
• The OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute feature is not supported on devices that
are virtual links headends.
• The feature is supported only in global VPN routing and forwarding (VRF) OSPF instances.
• The only supported tunneling method is MPLS.
• You cannot configure a traffic engineering (TE) tunnel interface as a protected interface. Use the MPLS
Traffic Engineering—Fast Reroute Link and Node Protection feature to protect these tunnels. For more
information, see the “MPLS Traffic Engineering—Fast Reroute Link and Node Protection” section in
the Multiprotocol Label Switching Configuration Guide.
• You can configure a TE tunnel interface in a repair path, but OSPF will not verify the tunnel’s placement;
you must ensure that it is not crossing the physical interface that it is intended to protect.
• Not all routes can have repair paths. Multipath primary routes might have repair paths for all, some, or
no primary paths, depending on the network topology, the connectivity of the computing router, and the
attributes required of repair paths.
• Devices that can be selected as tunnel termination points must have a /32 address advertised in the area
in which remote LFA is enabled. This address will be used as a tunnel termination IP. If the device does
not advertise a /32 address, it may not be used for remote LFA tunnel termination.
• All devices in the network that can be selected as tunnel termination points must be configured to accept
targeted LDP sessions using the mpls ldp discovery targeted-hello accept command.

IP Routing: OSPF Configuration Guide
488


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Information About OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

Information About OSPF IPv4 Remote Loop-Free Alternate IP
Fast Reroute
IP Fast Reroute
The IP fast reroute (IPFRR) LFA computation provides protection against link failure. Locally computed
repair paths are used to prevent packet loss caused by loops that occur during network reconvergence after a
failure. For more information about IPFRR, see RFC 5286, Basic Specification for IP Fast Reroute: Loop-Free
Alternates.

OSPF IPv4 Remote LFA IPFRR with Ring Topology
Some topologies (for example the commonly used ring-based topology) require protection that is not afforded
by LFA FRR alone. Consider the topology shown in the figure below:
Figure 12: Remote LFA IPFRR with Ring Topology

The red looping arrow represents traffic that is looping immediately after a failure between node A and C
(before network reconvergence). Device A tries to send traffic destined to F to next-hop B. Device B cannot
be used as an LFA for prefixes advertised by nodes C and F. The actual LFA is node D. However, node D is
not directly connected to the protecting node A. To protect prefixes advertised by C, node A must tunnel the
packet around the failed link A-C to node D, provided that the tunnel does not traverse the failing link.
The OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute feature enables you to tunnel a packet around
a failed link to a remote loop-free alternate that is more than one hop away. In the figure above, the green
arrow between A and D shows the tunnel that is automatically created by the OSPF IPv4 Remote Loop-Free
Alternate IP Fast Reroute feature to bypass looping.

IP Routing: OSPF Configuration Guide
489


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
How to Configure OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

In the figure above, device A must be configured with fast-reroute per-prefix remote-lfa tunnel mpls-ldp
to enable remote LFA, and device D must be configured with mpls ldp discovery targeted-hello accept
to accept targeted LDP sessions.

Note

How to Configure OSPF IPv4 Remote Loop-Free Alternate IP
Fast Reroute
Configuring a Remote LFA Tunnel
Perform this task to configure a per-prefix LFA FRR path that redirects traffic to a remote LFA tunnel.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. fast-reroute per-prefix remote-lfa [area area-id] tunnel mpls-ldp

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

Enables OSPF routing and enters router configuration mode.

Example:
Device(config)# router ospf 10

Step 4

fast-reroute per-prefix remote-lfa [area area-id]
tunnel mpls-ldp

IP Routing: OSPF Configuration Guide
490

Configures a per-prefix LFA FRR path that redirects traffic
to a remote LFA tunnel via MPLS-LDP.


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Configuring the Maximum Distance to a Tunnel Endpoint

Command or Action
Example:

Purpose
• Use the area area-id keyword and argument to specify
an area in which to enable LFA FRR.

Device(config-router)# fast-reroute per-prefix
remote-lfa area 2 tunnel mpls-ldp

Configuring the Maximum Distance to a Tunnel Endpoint
Perform this task to configure the maximum distance to the tunnel endpoint in a per-prefix LFA FRR path
that redirects traffic to a remote LFA tunnel.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. fast-reroute per-prefix remote-lfa [area area-id] maximum-cost distance

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

Enables OSPF routing and enters router configuration mode.

Example:
Device(config)# router ospf 10

IP Routing: OSPF Configuration Guide
491


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Verifying Tunnel Interfaces Created by OSPF IPv4 Remote LFA IPFRR

Step 4

Command or Action

Purpose

fast-reroute per-prefix remote-lfa [area area-id]
maximum-cost distance

Configures the maximum distance to the tunnel endpoint in
a per-prefix LFA FRR path that redirects traffic to a remote
LFA tunnel.

Example:
Device(config-router)# fast-reroute per-prefix
remote-lfa area 2 maximum-cost 30

• Use the area area-id keyword and variable to specify
an area in which to enable LFA FRR.

Verifying Tunnel Interfaces Created by OSPF IPv4 Remote LFA IPFRR
SUMMARY STEPS
1. enable
2. show ip ospf fast-reroute remote-lfa tunnels

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

show ip ospf fast-reroute remote-lfa tunnels
Example:
Device# show ip ospf fast-reroute remote-lfa
tunnels

IP Routing: OSPF Configuration Guide
492

Displays information about the OSPF per-prefix LFA FRR
configuration.


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Configuration Examples for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

Configuration Examples for OSPF IPv4 Remote Loop-Free
Alternate IP Fast Reroute
Example: Configuring a Remote LFA Tunnel
The following example shows how to configure a remote per-prefix LFA FRR in area 2. The remote tunnel
type is specified as MPLS-LDP:
Router(config-router)# fast-reroute per-prefix remote-lfa area 2 tunnel mpls-ldp

Example: Configuring the Maximum Distance to a Tunnel Endpoint
The following example shows how to set a maximum cost of 30 in area 2:
Router(config-router)# fast-reroute per-prefix remote-lfa area 2 maximum-cost 30

Example: Verifying Tunnel Interfaces Created by OSPF IPv4 Remote LFA IPFRR
The following example displays information about about tunnel interfaces created by OSPF IPv4 LFA IPFRR:
Router# show ip ospf fast-reroute remote-lfa tunnels
OSPF Router with ID (192.168.1.1) (Process ID 1)
Area with ID (0)
Base Topology (MTID 0)
Interface MPLS-Remote-Lfa3
Tunnel type: MPLS-LDP
Tailend router ID: 192.168.3.3
Termination IP address: 192.168.3.3
Outgoing interface: Ethernet0/0
First hop gateway: 192.168.14.4
Tunnel metric: 20
Protects:
192.168.12.2 Ethernet0/1, total metric 30

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

OSPF commands: complete command syntax, command mode, defaults, Cisco IOS IP Routing: OSPF
command history, usage guidelines, and examples
Command Reference

IP Routing: OSPF Configuration Guide
493


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Feature Information for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

Related Topic

Document Title

Configuring OSPF

“Configuring OSPF” in the IP
Routing: OSPF Configuration
Guide.

OSPFv2 loop-free alternate fast reroute

“OSPFv2 Loop-Free Alternate Fast
Reroute” in the IP Routing: OSPF
Configuration Guide

Standards and RFCs
Standard/RFC

Title

RFC 5286

Basic Specification for IP Fast Reroute: Loop-Free
Alternates

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

Feature Information for OSPF IPv4 Remote Loop-Free Alternate
IP Fast Reroute
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
494


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Feature Information for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

Table 58: Feature Information for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

Feature Name

Releases

Feature Information

OSPF IPv4 Remote Loop-Free
Alternate IP Fast Reroute

15.2(2)S

The OSPF IPv4 Remote Loop-Free
Alternate IP Fast Reroute feature
enables a backup repair path in the
event of node failure, even if the
path is multiple hops away.

Cisco IOS XE Release 3.11S

The following commands were
introduced or modified:
fast-reroute per-prefix remote-lfa
maximum-cost, fast-reroute
per-prefix remote-lfa tunnel, and
show ip ospf fast-reroute.

IP Routing: OSPF Configuration Guide
495


OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute
Feature Information for OSPF IPv4 Remote Loop-Free Alternate IP Fast Reroute

IP Routing: OSPF Configuration Guide
496
