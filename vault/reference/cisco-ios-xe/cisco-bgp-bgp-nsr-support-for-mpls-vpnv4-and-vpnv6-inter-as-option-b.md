---
title: "BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-nsr-support-for-mpls-vpnv4-and-vpnv6-inter-as-option-b
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 76 BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B Border Gateway Protocol (BGP) nonstop routing (NSR) provides support for NSR and nonstop forwarding (NSF) in the event of a switchover from an active to a standby Route Processor (RP). BGP NSR supports provider-edge-to-customer-edge (PE-CE) connections for IPv4 and IPv6 address families and also for Internal BGP (IBGP) peers a"
---

# BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B

CHAPTER

76

BGP NSR Support for MPLS VPNv4 and VPNv6
Inter-AS Option B
Border Gateway Protocol (BGP) nonstop routing (NSR) provides support for NSR and nonstop forwarding
(NSF) in the event of a switchover from an active to a standby Route Processor (RP). BGP NSR supports
provider-edge-to-customer-edge (PE-CE) connections for IPv4 and IPv6 address families and also for Internal
BGP (IBGP) peers at the PE device for IPv4, IPv6, VPN version 4 (VPNv4), and VPN version 6 (VPNv6)
address families. The BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B feature provides
support for NSR at the autonomous system boundary routers (ASBRs) in Multiprotocol Label Switching
(MPLS) Inter-Autonomous System (Inter-AS) Option B deployments for both VPNv4 and VPNv6 address
families.
This module describes how to enable BGP NSR support at ASBRs in Inter-AS Option B for VPNv4 and
VPNv6 address families.
• Restrictions for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B, on page 1063
• Information About BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B, on page 1064
• How to Configure BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B, on page 1066
• Configuration Examples for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B, on
page 1067
• Additional References for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B, on page
1068
• Feature Information for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B, on page
1069

Restrictions for BGP NSR Support for MPLS VPNv4 and VPNv6
Inter-AS Option B
• If a peer is activated under an address family for which nonstop routing (NSR) is not supported (for
example, multicast distribution tree [MDT]), and if the address family topology is tied to the same session
as other address family topologies for which NSR is supported (for example, VPN version 4 [VPNv4]),
then NSR will not be supported for that peer-established session. NSR cannot be supported for a session
if the session establishment involves activating the peer in an address family for which NSR is not
supported. As a workaround, you can create a multisession and activate the nonsupported topology as
part of a new session.
• NSR can be configured only on a per-neighbor basis.

IP Routing: BGP Configuration Guide
1063


BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B
Information About BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B

• There can be some performance and memory impact as a result of enabling BGP NSR support at
autonomous system boundary routers (ASBRs) in Inter-AS Option B.

Information About BGP NSR Support for MPLS VPNv4 and VPNv6
Inter-AS Option B
Overview of BGP NSR
Border Gateway Protocol (BGP) nonstop routing (NSR) with stateful switchover (SSO) provides a high
availability (HA) solution to service providers whose provider edge (PE) routers engage in External BGP
(EBGP) peering relationships with customer edge (CE) routers that do not support BGP graceful restart (GR).
BGP NSR works with SSO to synchronize BGP state information between the active and standby Route
Processors (RPs). SSO minimizes the amount of time for which a network is unavailable to users following
a switchover.
BGP NSR with SSO is supported in BGP peer, BGP peer group, and BGP session template configurations.
To configure support for BGP NSR with SSO in BGP peer and BGP peer group configurations, use the
neighbor ha-mode sso command in address family configuration mode for IPv4 virtual routing and forwarding
(VRF) address family BGP peer sessions. To include support for Cisco BGP NSR with SSO in a BGP session
template, use the ha-mode sso command in session-template configuration mode.

Inter-Autonomous Systems
BGP autonomous systems (ASs) are used to divide global external networks into individual routing domains
where local routing policies are applied. Separate BGP ASs dynamically exchange routing information through
External BGP (EBGP) peering sessions. BGP peers within the same AS exchange routing information through
Internal BGP (IBGP) peering sessions.
When multiple sites of a VPN are connected to different ASs, Inter-Autonomous System (Inter-AS) deployments
are useful for providing VPN services between different ASs. In this scenario, provider edge (PE) routers
attached to the VPN cannot maintain IBGP connections with each other or with a common route reflector
(RR). EBGP is used to distribute VPN-IPv4/IPv6 addresses. RFC 2547bis presents the following Inter-AS
VPN solutions:
• Virtual routing and forwarding (VRF)-to-VRF connections at autonomous system boundary routers
(ASBRs)—PEs act as ASBRs of their ASs. The ASBRs are directly connected and manage VPN routes
between them through multiple subinterfaces. The ASBRs associate each such subinterface with a VRF
and use EBGP to distribute unlabeled IPv4 addresses to each other. This solution is also called "Inter-AS
Option A." Inter-AS Option A provides IP-based forwarding between the ASBRs connecting the different
ASs; however, it also requires a single BGP session for each VPN connection. Inter-AS Option A is easy
to implement, but it has limited scalability.
• EBGP redistribution of labeled VPN-IPv4 routes—Neighboring ASBRs use Multiprotocol External BGP
(MP-EBGP) to exchange labeled VPN-IPv4 routes that the ASBRs obtain from PEs in their respective
ASs. PE routers use IBGP to redistribute labeled VPN-IPv4 routes either to an ASBR or to an RR of
which an ASBR is a client. This solution is also called "Inter-AS Option B." Inter-AS Option B provides
Multiprotocol Label Switching (MPLS)-based forwarding between the ASBRs connecting different ASs.
Inter-AS Option B provides better scalability than Inter-AS Option A because Option B requires only
one BGP session to exchange all VPN prefixes between the ASBRs.

IP Routing: BGP Configuration Guide
1064


BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B
Overview of MPLS VPNv4 and VPNv6 Inter-AS Option B

• Multihop EBGP redistribution of labeled VPN-IPv4 routes—PEs exchange labeled VPN-IPv4 routes
directly with each other through MP-EBGP without the participation of ASBRs. ASBRs advertise labeled
IPv4 routes to PEs in their respective ASs through MP-IBGP. ASBRs neither maintain VPN-IPv4 routes
nor advertise VPN-IPv4 routes to each other. This solution is also called "Inter-AS Option C."

Overview of MPLS VPNv4 and VPNv6 Inter-AS Option B
In the Inter-Autonomous System (Inter-AS) Option B solution, two autonomous system border routers (ASBRs)
use Multiprotocol External BGP (MP-EBGP) to exchange labeled VPN-IPv4 routes that they obtain from the
provider edge (PEs) devices in their respective ASs. Multiprotocol Label Switching (MPLS)-based forwarding
is used between the ASBRs. If a failure is encountered at an ASBR, routing and forwarding is impacted in
the absence of nonstop routing (NSR) or graceful restart (GR). NSR provides the ability to preserve the routing
state to a redundant Route Processor (RP), which can take over the functionality of the active RP in the event
of a failover. In conjunction with nonstop forwarding (NSF), the routing and forwarding states can remain
unimpacted during a failover.
The figure below illustrates two ASs, AS1 and AS2, each containing customer edge (CE) routers that belong
to different VPNs. Each PE tracks which route distinguisher (RD) corresponds to which VPN, thus controlling
the traffic that belongs to each VPN.
• Customer edge 1 (CE1) and CE3 belong to VPN 1.
• CE2 and CE4 belong to VPN 2.
• Provider edge 1 (PE1) uses route distinguisher 1 (RD 1) for VPN 1 (VRF 1) and RD 2 for VPN 2 (VRF
2).
• PE2 uses RD 3 for VPN 1 (VRF 1) and RD 4 for VPN 2 (VRF 2).
Figure 92: Flow of Routes in Inter-AS Option B

In an Inter-AS Option B scenario like the one in the figure above, the routes are carried across an AS boundary
from ASBR1 to ASBR2 over an MP-EBGP session.
In Inter-AS Option B, the routes are advertised as follows:
1. PEs in AS1 advertise labeled VPN-IPv4 routes to either the ASBR of AS1 or the route reflector (RR) of
the ASBR through Multiprotocol Internal BGP (MP-IBGP).
2. The ASBR of AS1 advertises labeled VPN-IPv4 routes to the ASBR of AS2 through MP-EBGP.
3. The ASBR of AS2 advertises labeled VPN-IPv4 routes to either the PEs in AS2 or the RR of the PEs
through MP-IBGP.
The ASBRs must perform special processing on the labeled VPN-IPv4 routes, which is also called the ASBR
extension method.

IP Routing: BGP Configuration Guide
1065


BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B
How to Configure BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B

How to Configure BGP NSR Support for MPLS VPNv4 and VPNv6
Inter-AS Option B
Configuring an ASBR to Enable BGP NSR Support in Inter-AS Option B
Border Gateway Protocol (BGP) nonstop routing (NSR) support at autonomous system boundary router
(ASBR) in Inter-Autonomous System (Inter-AS) Option B can be configured in the same way that BGP NSR
is configured for Multiprotocol Internal BGP (MP-IBGP) peers at the provider edge (PE). The configuration
is performed in global router mode, on a per-neighbor basis. The NSR support is applied to all address families
under which the neighbor has been activated (provided the neighbor is not activated under a nonsupported
address family). If a neighbor is activated under an unsupported address family, that topology must be made
to be part of a different session using multisession.
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

enable
configure terminal
router bgp autonomous-system-number
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address ha-mode sso
address-family {vpnv4 | vpnv6} [multicast | unicast]
neighbor ip-address activate
end
show ip bgp vpnv4 all sso summary
show ip bgp vpnv4 neighbors ip-address

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

router bgp autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 400

Step 4

neighbor ip-address remote-as
autonomous-system-number
Example:

IP Routing: BGP Configuration Guide
1066

Specifies the AS of the neighbor.


BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B
Configuration Examples for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B

Command or Action

Purpose

Device(config-router)# neighbor 192.168.1.1
remote-as 4000

Step 5

neighbor ip-address ha-mode sso
Example:

Configures a BGP neighbor to support BGP NSR with
stateful switchover (SSO).

Device(config-router)# neighbor 192.168.1.1
ha-mode sso

Step 6

address-family {vpnv4 | vpnv6} [multicast | unicast]
Example:

Enters address family configuration mode for configuring
routing sessions that use standard VPNv4 or VPNv6
address prefixes.

Device(config-router)# address-family vpnv4
unicast

Step 7

neighbor ip-address activate

Activates the specified peer.

Example:
Device(config-router-af)# neighbor 192.168.1.1
activate

Step 8

end
Example:

Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

Step 9

show ip bgp vpnv4 all sso summary
Example:

Displays information about BGP peers that support BGP
NSR with SSO.

Device# show ip bgp vpnv4 all sso summary

Step 10

show ip bgp vpnv4 neighbors ip-address
Example:

Displays information about BGP and TCP connections to
neighbors.

Device# show ip bgp vpnv4 neighbors 192.168.1.1

Configuration Examples for BGP NSR Support for MPLS VPNv4
and VPNv6 Inter-AS Option B
Example: Configuring an ASBR to Enable BGP NSR Support in Inter-AS Option
B
Configuring an ASBR to Be NSR-Capable at the VPNv4 Address Family Level
router bgp 200
neighbor 192.168.1.1 remote-as 200
neighbor 192.168.1.1 ha-mode sso
address-family vpnv4 unicast
neighbor 192.168.1.1 activate

IP Routing: BGP Configuration Guide
1067


BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B
Additional References for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B

Configuring an ASBR to Be NSR-Capable at the VPNv6 Address Family Level
router bgp 300
neighbor 192.168.1.10 remote-as 300
neighbor 192.168.1.10 ha-mode sso
address-family vpnv6 multicast
neighbor 192.168.1.10 activate

To verify that an ASBR is NSR-capable, check the show ip bgp vpnv4 neighbors command output
for the Stateful switchover support enabled field.
ASBR# show ip bgp vpnv4 neighbors 192.168.1.10
BGP neighbor is 192.168.1.10, vrf A, remote AS 200, external link
BGP version 4, remote router ID 192.168.1.10
BGP state = Established, up for 00:16:01
Last read 00:00:04, last write 00:00:35, hold time is 180, keepalive interval is 60 seconds
Neighbor sessions:
1 active, is not multisession capable (disabled)
Neighbor capabilities:
Route refresh: advertised and received(new)
Four-octets ASN Capability: advertised and received
Address family IPv4 Unicast: advertised and received
Enhanced Refresh Capability: advertised and received
Multisession Capability:
Stateful switchover support enabled: YES for session 1

Additional References for BGP NSR Support for MPLS VPNv4
and VPNv6 Inter-AS Option B
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
1068


BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B
Feature Information for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B

Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.

http://www.cisco.com/support

To receive security and technical information about your products, you can
subscribe to various services, such as the Product Alert Tool (accessed from
Field Notices), the Cisco Technical Services Newsletter, and Really Simple
Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com user
ID and password.

Feature Information for BGP NSR Support for MPLS VPNv4 and
VPNv6 Inter-AS Option B
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 96: Feature Information for BGP NSR Support for Inter-AS Option B

Feature Name

Releases

Feature Information

BGP NSR Support for MPLS
VPNv4 and VPNv6 Inter-AS
Option B

Cisco IOS XE Release 3.10S

The BGP NSR Support for MPLS
VPNv4 and VPNv6 Inter-AS
Option B feature provides support
for nonstop routing (NSR) at the
autonomous system boundary
routers (ASBR) in
Inter-Autonomous System
(Inter-AS) Option B deployments
for both VPNv4 and VPNv6
address families.
No commands were introduced or
modified.

IP Routing: BGP Configuration Guide
1069


BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B
Feature Information for BGP NSR Support for MPLS VPNv4 and VPNv6 Inter-AS Option B

IP Routing: BGP Configuration Guide
1070
