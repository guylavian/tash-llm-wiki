---
title: "BGP Link Bandwidth"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-link-bandwidth
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 30 BGP Link Bandwidth The Border Gateway Protocol (BGP) Link Bandwidth feature is used to advertise the bandwidth of an autonomous system exit link as an extended community. This feature is configured for links between directly connected external BGP (eBGP) neighbors. The link bandwidth extended community attribute is propagated to iBGP peers when extended community exchange is enabled."
---

# BGP Link Bandwidth

CHAPTER

30

BGP Link Bandwidth
The Border Gateway Protocol (BGP) Link Bandwidth feature is used to advertise the bandwidth of an
autonomous system exit link as an extended community. This feature is configured for links between directly
connected external BGP (eBGP) neighbors. The link bandwidth extended community attribute is propagated
to iBGP peers when extended community exchange is enabled. This feature is used with BGP multipath
features to configure load balancing over links with unequal bandwidth.
• Finding Feature Information, on page 543
• Prerequisites for BGP Link Bandwidth, on page 543
• Restrictions for BGP Link Bandwidth, on page 544
• Information About BGP Link Bandwidth, on page 544
• How to Configure BGP Link Bandwidth, on page 545
• Configuration Examples for BGP Link Bandwidth, on page 547
• Additional References, on page 551
• Feature Information for BGP Link Bandwidth, on page 552

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP Link Bandwidth
• BGP load balancing or multipath load balancing must be configured before BGP Link Bandwidth feature
is enabled.
• BGP extended community exchange must be enabled between iBGP neighbors to which the link bandwidth
attribute is to be advertised.
• Cisco Express Forwarding or distributed Cisco Express Forwarding must be enabled on all participating
routers.

IP Routing: BGP Configuration Guide
543


BGP Link Bandwidth
Restrictions for BGP Link Bandwidth

Restrictions for BGP Link Bandwidth
• The BGP Link Bandwidth feature can be configured only under IPv4 and VPNv4 address family sessions.
• BGP can originate the link bandwidth community only for directly connected links to eBGP neighbors.
• Both iBGP and eBGP load balancing are supported in IPv4 and VPNv4 address families. However,
eiBGP load balancing is supported only in VPNv4 address families.

Information About BGP Link Bandwidth
BGP Link Bandwidth Overview
The BGP Link Bandwidth feature is used to enable multipath load balancing for external links with unequal
bandwidth capacity. This feature is enabled under an IPv4 or VPNv4 address family session by entering the
bgp dmzlink-bw command. This feature supports iBGP, eBGP multipath load balancing, and eiBGP multipath
load balancing in Multiprotocol Label Switching (MPLS) VPNs. When this feature is enabled, routes learned
from directly connected external neighbor are propagated through the internal BGP (iBGP) network with the
bandwidth of the source external link.
The link bandwidth extended community indicates the preference of an autonomous system exit link in terms
of bandwidth. This extended community is applied to external links between directly connected eBGP peers
by entering the neighbor dmzlink-bw command. The link bandwidth extended community attribute is
propagated to iBGP peers when extended community exchange is enabled with the neighbor send-community
command.

Link Bandwidth Extended Community Attribute
The link bandwidth extended community attribute is a 4-byte value that is configured for a link on the
demilitarized zone (DMZ) interface that connects two single hop eBGP peers. The link bandwidth extended
community attribute is used as a traffic sharing value relative to other paths while traffic is being forwarded.
Two paths are designated as equal for load balancing if the weight, local-pref, as-path length, Multi Exit
Discriminator (MED), and Interior Gateway Protocol (IGP) costs are the same.

Benefits of the BGP Link Bandwidth Feature
The BGP Link Bandwidth feature allows BGP to be configured to send traffic over multiple iBGP or eBGP
learned paths where the traffic that is sent is proportional to the bandwidth of the links that are used to exit
the autonomous system. The configuration of this feature can be used with eBGP and iBGP multipath features
to enable unequal cost load balancing over multiple links. Unequal cost load balancing over links with unequal
bandwidth was not possible in BGP before the BGP Link Bandwidth feature was introduced.

IP Routing: BGP Configuration Guide
544


BGP Link Bandwidth
How to Configure BGP Link Bandwidth

How to Configure BGP Link Bandwidth
Configuring BGP Link Bandwidth
To configure the BGP Link Bandwidth feature, perform the steps in this section.
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 [mdt | multicast | tunnel | unicast [vrf vrf-name] | vrf vrf-name] | vpnv4 [unicast]
bgp dmzlink-bw
neighbor ip-address dmzlink-bw
neighbor ip-address send-community [both | extended | standard]
end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged EXEC
mode.

Example:

• Enter your password if prompted.
Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Enters router configuration mode to create or configure a
BGP routing process.

Router(config)# router bgp 50000

Step 4

address-family ipv4 [mdt | multicast | tunnel | unicast
[vrf vrf-name] | vrf vrf-name] | vpnv4 [unicast]
Example:

Enters address family configuration mode.
• The BGP Link Bandwidth feature is supported only
under the IPv4 and VPNv4 address families.

Router(config-router)# address-family ipv4

Step 5

bgp dmzlink-bw
Example:
Router(config-router-af)# bgp dmzlink-bw

Configures BGP to distribute traffic proportionally to the
bandwidth of the link.
• This command must be entered on each router that
contains an external interface that is to be used for
multipath load balancing.

IP Routing: BGP Configuration Guide
545


BGP Link Bandwidth
Verifying BGP Link Bandwidth Configuration

Step 6

Command or Action

Purpose

neighbor ip-address dmzlink-bw

Configures BGP to include the link bandwidth attribute for
routes learned from the external interface specified IP
address.

Example:
Router(config-router-af)#
neighbor 172.16.1.1 dmzlink-bw

Step 7

• This command must be configured for each eBGP link
that is to be configured as a multipath. Enabling this
command allows the bandwidth of the external link to
be propagated through the link bandwidth extended
community.

neighbor ip-address send-community [both | extended (Optional) Enables community and/or extended community
exchange with the specified neighbor.
| standard]
Example:
Router(config-router-af)# neighbor 10.10.10.1
send-community extended

Step 8

• This command must be configured for iBGP peers to
which the link bandwidth extended community
attribute is to be propagated.
Exits address family configuration mode, and enters
Privileged EXEC mode.

end
Example:
Router(config-router-af)# end

Verifying BGP Link Bandwidth Configuration
To verify the BGP Link Bandwidth feature, perform the steps in this section.
SUMMARY STEPS
1. enable
2. show ip bgp ip-address [longer-prefixes [injected] | shorter-prefixes [mask-length]]
3. show ip route [[ip-address [mask] [longer-prefixes]] | [protocol [process-id]] | [list access-list-number
| access-list-name] | [static download]]
DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged EXEC
mode.

Example:

• Enter your password if prompted.
Router> enable

Step 2

show ip bgp ip-address [longer-prefixes [injected] |
shorter-prefixes [mask-length]]
Example:
Router# show ip bgp 10.0.0.0

IP Routing: BGP Configuration Guide
546

Displays information about the TCP and BGP connections
to neighbors.
• The output displays the status of the link bandwidth
configuration. The bandwidth of the link is shown in
kilobytes.


BGP Link Bandwidth
Configuration Examples for BGP Link Bandwidth

Step 3

Command or Action

Purpose

show ip route [[ip-address [mask] [longer-prefixes]] |
[protocol [process-id]] | [list access-list-number |
access-list-name] | [static download]]

Displays the current state of the routing table.

Example:

• The output displays traffic share values, including the
weights of the links that are used to direct traffic
proportionally to the bandwidth of each link.

Router# show ip route 10.0.0.0

Configuration Examples for BGP Link Bandwidth
BGP Link Bandwidth Configuration Example
In the following examples, the BGP Link Bandwidth feature is configured so BGP will distribute traffic
proportionally to the bandwidth of each external link. The figure below shows two external autonomous
systems connected by three links that each carry a different amount of bandwidth (unequal cost links). Multipath
load balancing is enabled and traffic is balanced proportionally.
Figure 46: BGP Link Bandwidth Configuration

Router A Configuration
In the following example, Router A is configured to support iBGP multipath load balancing and to exchange
the BGP extended community attribute with iBGP neighbors:
Router A(config)# router bgp 100

IP Routing: BGP Configuration Guide
547


BGP Link Bandwidth
BGP Link Bandwidth Configuration Example

Router A(config-router)# neighbor 10.10.10.2 remote-as 100
Router A(config-router)# neighbor 10.10.10.2 update-source Loopback 0
Router A(config-router)# neighbor 10.10.10.3 remote-as 100
Router A(config-router)# neighbor 10.10.10.3 update-source Loopback 0
Router A(config-router)# address-family ipv4
Router A(config-router)# bgp dmzlink-bw
Router A(config-router-af)# neighbor 10.10.10.2 activate
Router A(config-router-af)# neighbor 10.10.10.2 send-community both
Router A(config-router-af)# neighbor 10.10.10.3 activate
Router A(config-router-af)# neighbor 10.10.10.3 send-community both
Router A(config-router-af)# maximum-paths ibgp 6

Router B Configuration
In the following example, Router B is configured to support multipath load balancing, to distribute Router D
and Router E link traffic proportionally to the bandwidth of each link, and to advertise the bandwidth of these
links to iBGP neighbors as an extended community:
Router B(config)# router bgp 100
Router B(config-router)# neighbor 10.10.10.1 remote-as 100
Router B(config-router)# neighbor 10.10.10.1 update-source Loopback 0
Router B(config-router)# neighbor 10.10.10.3 remote-as 100
Router B(config-router)# neighbor 10.10.10.3 update-source Loopback 0
Router B(config-router)# neighbor 172.16.1.1 remote-as 200
Router B(config-router)# neighbor 172.16.1.1 ebgp-multihop 1
Router B(config-router)# neighbor 172.16.2.2 remote-as 200
Router B(config-router)# neighbor 172.16.2.2 ebgp-multihop 1
Router B(config-router)# address-family ipv4
Router B(config-router-af)# bgp dmzlink-bw
Router B(config-router-af)# neighbor 10.10.10.1 activate
Router B(config-router-af)# neighbor 10.10.10.1 next-hop-self
Router B(config-router-af)# neighbor 10.10.10.1 send-community both
Router B(config-router-af)# neighbor 10.10.10.3 activate
Router B(config-router-af)# neighbor 10.10.10.3 next-hop-self
Router B(config-router-af)# neighbor 10.10.10.3 send-community both
Router B(config-router-af)# neighbor 172.16.1.1
activate

IP Routing: BGP Configuration Guide
548


BGP Link Bandwidth
Verifying BGP Link Bandwidth

Router B(config-router-af)# neighbor 172.16.1.1 dmzlink-bw
Router B(config-router-af)# neighbor 172.16.2.2 activate
Router B(config-router-af)# neighbor 172.16.2.2 dmzlink-bw
Router B(config-router-af)# maximum-paths ibgp 6
Router B(config-router-af)# maximum-paths 6

Router C Configuration
In the following example, Router C is configured to support multipath load balancing and to advertise the
bandwidth of the link with Router E to iBGP neighbors as an extended community:
Router C(config)# router bgp 100
Router C(config-router)# neighbor 10.10.10.1 remote-as 100
Router C(config-router)# neighbor 10.10.10.1 update-source Loopback 0
Router C(config-router)# neighbor 10.10.10.2 remote-as 100
Router C(config-router)# neighbor 10.10.10.2 update-source Loopback 0
Router C(config-router)# neighbor 172.16.3.30 remote-as 200
Router C(config-router)# neighbor 172.16.3.30 ebgp-multihop 1
Router C(config-router)# address-family ipv4
Router C(config-router-af)# bgp dmzlink-bw
Router C(config-router-af)# neighbor 10.10.10.1 activate
Router C(config-router-af)# neighbor 10.10.10.1 send-community both
Router C(config-router-af)# neighbor 10.10.10.1 next-hop-self
Router C(config-router-af)# neighbor 10.10.10.2 activate
Router C(config-router-af)# neighbor 10.10.10.2 send-community both
Router C(config-router-af)# neighbor 10.10.10.2 next-hop-self
Router C(config-router-af)# neighbor 172.16.3.3 activate
Router C(config-router-af)# neighbor 172.16.3.3 dmzlink-bw
Router C(config-router-af)# maximum-paths ibgp 6
Router C(config-router-af)# maximum-paths 6

Verifying BGP Link Bandwidth
The examples in this section show the verification of this feature on Router A and Router B.
Router B
In the following example, the show ip bgp command is entered on Router B to verify that two unequal cost
best paths have been installed into the BGP routing table. The bandwidth for each link is displayed with each
route.
Router B# show ip bgp 192.168.1.0
BGP routing table entry for 192.168.1.0/24, version 48
Paths: (2 available, best #2)
Multipath: eBGP
Advertised to update-groups:
1
2
200
172.16.1.1 from 172.16.1.2 (192.168.1.1)
Origin incomplete, metric 0, localpref 100, valid, external, multipath, best
Extended Community: 0x0:0:0
DMZ-Link Bw 278 kbytes
200

IP Routing: BGP Configuration Guide
549


BGP Link Bandwidth
Verifying BGP Link Bandwidth

172.16.2.2 from 172.16.2.2 (192.168.1.1)
Origin incomplete, metric 0, localpref 100, valid, external, multipath, best
Extended Community: 0x0:0:0
DMZ-Link Bw 625 kbytes

Router A
In the following example, the show ip bgp command is entered on Router A to verify that the link bandwidth
extended community has been propagated through the iBGP network to Router A. The output shows that a
route for each exit link (on Router B and Router C) to autonomous system 200 has been installed as a best
path in the BGP routing table.
Router A# show ip bgp 192.168.1.0
BGP routing table entry for 192.168.1.0/24, version 48
Paths: (3 available, best #3)
Multipath: eBGP
Advertised to update-groups:
1
2
200
172.16.1.1 from 172.16.1.2 (192.168.1.1)
Origin incomplete, metric 0, localpref 100, valid, external, multipath
Extended Community: 0x0:0:0
DMZ-Link Bw 278 kbytes
200
172.16.2.2 from 172.16.2.2 (192.168.1.1)
Origin incomplete, metric 0, localpref 100, valid, external, multipath, best
Extended Community: 0x0:0:0
DMZ-Link Bw 625 kbytes
200
172.16.3.3 from 172.16.3.3 (192.168.1.1)
Origin incomplete, metric 0, localpref 100, valid, external, multipath, best
Extended Community: 0x0:0:0
DMZ-Link Bw 2500 kbytes

Router A
In the following example, the show ip route command is entered on Router A to verify the multipath routes
that are advertised and the associated traffic share values:
Router A# show ip route 192.168.1.0
Routing entry for 192.168.1.0/24
Known via "bgp 100", distance 200, metric 0
Tag 200, type internal
Last update from 172.168.1.1 00:01:43 ago
Routing Descriptor Blocks:
* 172.168.1.1, from 172.168.1.1, 00:01:43 ago
Route metric is 0, traffic share count is 13
AS Hops 1, BGP network version 0
Route tag 200
172.168.2.2, from 172.168.2.2, 00:01:43 ago
Route metric is 0, traffic share count is 30
AS Hops 1, BGP network version 0
Route tag 200
172.168.3.3, from 172.168.3.3, 00:01:43 ago
Route metric is 0, traffic share count is 120
AS Hops 1, BGP network version 0
Route tag 200

IP Routing: BGP Configuration Guide
550


BGP Link Bandwidth
Additional References

Additional References
The following sections provide references related to the BGP Link Bandwidth feature.
Related Documents
Related Topic

Document Title

BGP commands: complete command syntax, command Cisco IOS IP Routing: BGP Command Reference
mode, command history, defaults, usage guidelines, and
examples
BGP multipath load sharing for both eBGP and iBGP in " BGP Multipath Load Sharing for Both eBGP and
an MPLS-VPN
iBGP in an MPLS-VPN"
iBGP multipath load sharing

"iBGP Multipath Load Sharing"

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not -been modified by this feature.
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

The Cisco Support website provides extensive online resources, including http://www.cisco.com/techsupport
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.
To receive security and technical information about your products, you
can subscribe to various services, such as the Product Alert Tool (accessed
from Field Notices), the Cisco Technical Services Newsletter, and Really
Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com
user ID and password.

IP Routing: BGP Configuration Guide
551


BGP Link Bandwidth
Feature Information for BGP Link Bandwidth

Feature Information for BGP Link Bandwidth
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 46: Feature Information for BGP Link Bandwidth

Feature Name

Releases

BGP Link Bandwidth Cisco IOS XE Release
2.1

Feature Information
This feature was introduced on the Cisco ASR 1000 Series
Aggregation Services Routers.
The following commands were added or modified by this
feature: bgp dmzlink-bw, neighbor dmzlink-bw.

IP Routing: BGP Configuration Guide
552
