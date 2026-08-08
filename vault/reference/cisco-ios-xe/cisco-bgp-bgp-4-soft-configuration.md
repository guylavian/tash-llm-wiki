---
title: "BGP 4 Soft Configuration"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-4-soft-configuration
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 5 BGP 4 Soft Configuration BGP4 soft configuration allows BGP4 policies to be configured and activated without clearing the BGP session, hence without invalidating the forwarding cache. • Finding Feature Information, on page 161 • Information About BGP 4 Soft Configuration, on page 161 • How to Configure BGP 4 Soft Configuration, on page 162 • Configuration Examples for BGP 4 Soft Config"
---

# BGP 4 Soft Configuration

CHAPTER

5

BGP 4 Soft Configuration
BGP4 soft configuration allows BGP4 policies to be configured and activated without clearing the BGP
session, hence without invalidating the forwarding cache.
• Finding Feature Information, on page 161
• Information About BGP 4 Soft Configuration, on page 161
• How to Configure BGP 4 Soft Configuration, on page 162
• Configuration Examples for BGP 4 Soft Configuration, on page 165
• Additional References, on page 166
• Feature Information for BGP 4 Soft Configuration, on page 166

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP 4 Soft Configuration
BGP Session Reset
Whenever the routing policy changes due to a configuration change, BGP peering sessions must be reset by
using the clear ip bgp command. Cisco software supports the following three mechanisms to reset BGP
peering sessions:
• Hard reset—A hard reset tears down the specified peering sessions including the TCP connection and
deletes routes coming from the specified peer.
• Soft reset—A soft reset uses stored prefix information to reconfigure and activate BGP routing tables
without tearing down existing peering sessions. Soft reconfiguration uses stored update information, at
the cost of additional memory for storing the updates, to allow you to apply new BGP policy without
disrupting the network. Soft reconfiguration can be configured for inbound or outbound sessions.

IP Routing: BGP Configuration Guide
161


BGP 4 Soft Configuration
How to Configure BGP 4 Soft Configuration

• Dynamic inbound soft reset—The route refresh capability, as defined in RFC 2918, allows the local
device to reset inbound routing tables dynamically by exchanging route refresh requests to supporting
peers. The route refresh capability does not store update information locally for nondisruptive policy
changes. It instead relies on dynamic exchange with supporting peers. Route refresh must first be advertised
through BGP capability negotiation between peers. All BGP devices must support the route refresh
capability. To determine if a BGP device supports this capability, use the show ip bgp neighbors
command. The following message is displayed in the output when the device supports the route refresh
capability:
Received route refresh capability from peer.

The bgp soft-reconfig-backup command was introduced to configure BGP to perform inbound soft
reconfiguration for peers that do not support the route refresh capability. The configuration of this command
allows you to configure BGP to store updates (soft reconfiguration) only as necessary. Peers that support the
route refresh capability are unaffected by the configuration of this command.

How to Configure BGP 4 Soft Configuration
Configuring Inbound Soft Reconfiguration When Route Refresh Capability Is
Missing
Perform this task to configure inbound soft reconfiguration using the bgp soft-reconfig-backup command
for BGP peers that do not support the route refresh capability. BGP peers that support the route refresh
capability are unaffected by the configuration of this command. Note that the memory requirements for storing
the inbound update information can become quite large.
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
11.
12.
13.
14.
15.

enable
configure terminal
router bgp autonomous-system-number
bgp log-neighbor-changes
bgp soft-reconfig-backup
neighbor {ip-address | peer-group-name} remote-as autonomous-system-number
neighbor {ip-address | peer-group-name} soft-reconfiguration [inbound]
neighbor {ip-address | peer-group-name} route-map map-name {in | out}
Repeat Steps 6 through 8 for every peer that is to be configured with inbound soft reconfiguration.
exit
route-map map-name [permit | deny] [sequence-number]
set ip next-hop ip-address
end
show ip bgp neighbors [neighbor-address]
show ip bgp [network] [network-mask]

IP Routing: BGP Configuration Guide
162


BGP 4 Soft Configuration
Configuring Inbound Soft Reconfiguration When Route Refresh Capability Is Missing

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

Device(config)# router bgp 45000

Step 4

bgp log-neighbor-changes

Enables logging of BGP neighbor resets.

Example:
Device(config-router)# bgp log-neighbor-changes

Step 5

bgp soft-reconfig-backup
Example:
Device(config-router)# bgp soft-reconfig-backup

Step 6

neighbor {ip-address | peer-group-name} remote-as
autonomous-system-number
Example:

Configures a BGP speaker to perform inbound soft
reconfiguration for peers that do not support the route
refresh capability.
• This command is used to configure BGP to perform
inbound soft reconfiguration for peers that do not
support the route refresh capability. The configuration
of this command allows you to configure BGP to
store updates (soft reconfiguration) only as necessary.
Peers that support the route refresh capability are
unaffected by the configuration of this command.
Adds the IP address of the neighbor in the specified
autonomous system to the IPv4 multiprotocol BGP
neighbor table of the local device.

Device(config-router)# neighbor 192.168.1.2
remote-as 40000

Step 7

neighbor {ip-address | peer-group-name}
soft-reconfiguration [inbound]
Example:
Device(config-router)# neighbor 192.168.1.2
soft-reconfiguration inbound

Configures the Cisco software to start storing updates.
• All the updates received from this neighbor will be
stored unmodified, regardless of the inbound policy.
When inbound soft reconfiguration is done later, the
stored information will be used to generate a new set
of inbound updates.

IP Routing: BGP Configuration Guide
163


BGP 4 Soft Configuration
Configuring Inbound Soft Reconfiguration When Route Refresh Capability Is Missing

Step 8

Command or Action

Purpose

neighbor {ip-address | peer-group-name} route-map
map-name {in | out}

Applies a route map to incoming or outgoing routes.
• In this example, the route map named LOCAL will
be applied to incoming routes.

Example:
Device(config-router)# neighbor 192.168.1.2
route-map LOCAL in

Step 9

Repeat Steps 6 through 8 for every peer that is to be
configured with inbound soft reconfiguration.

—

Step 10

exit

Exits router configuration mode and enters global
configuration mode.

Example:
Device(config-router)# exit

Step 11

route-map map-name [permit | deny]
[sequence-number]
Example:

Configures a route map and enters route-map configuration
mode.
• In this example, a route map named LOCAL is
created.

Device(config)# route-map LOCAL permit 10

Step 12

set ip next-hop ip-address
Example:

Specifies where output packets that pass a match clause
of a route map for policy routing.
• In this example, the ip address is set to 192.168.1.144.

Device(config-route-map)# set ip next-hop
192.168.1.144

Step 13

end
Example:

Exits route-map configuration mode and enters privileged
EXEC mode.

Device(config-route-map)# end

Step 14

show ip bgp neighbors [neighbor-address]
Example:

(Optional) Displays information about the TCP and BGP
connections to neighbors.
Note

Device# show ip bgp neighbors 192.168.1.2

Step 15

show ip bgp [network] [network-mask]

(Optional) Displays the entries in the BGP routing table.

Example:

Note

Device# show ip bgp

IP Routing: BGP Configuration Guide
164

Only the syntax applicable to this task is used
in this example. For more details, see the Cisco
IOS IP Routing: BGP Command Reference.

Only the syntax applicable to this task is used
in this example. For more details, see the Cisco
IOS IP Routing: BGP Command Reference.


BGP 4 Soft Configuration
Configuration Examples for BGP 4 Soft Configuration

Examples
The following partial output from the show ip bgp neighbors command shows information about
the TCP and BGP connections to the BGP neighbor 192.168.2.1. This peer supports route refresh.
BGP neighbor is 192.168.1.2, remote AS 40000, external link
Neighbor capabilities:
Route refresh: advertised and received(new)

The following partial output from the show ip bgp neighbors command shows information about
the TCP and BGP connections to the BGP neighbor 192.168.3.2. This peer does not support route
refresh so the soft-reconfig inbound paths for BGP peer 192.168.3.2 will be stored because there is
no other way to update any inbound policy updates.
BGP neighbor is 192.168.3.2,
Neighbor capabilities:
Route refresh: advertised

remote AS 50000, external link

The following sample output from the show ip bgp command shows the entry for the network
172.17.1.0. Both BGP peers are advertising 172.17.1.0/24, but only the received-only path is stored
for 192.168.3.2.
BGP routing table entry for 172.17.1.0/24, version 11
Paths: (3 available, best #3, table Default-IP-Routing-Table, RIB-failure(4))
Flag: 0x820
Advertised to update-groups:
1
50000
192.168.3.2 from 192.168.3.2 (172.17.1.0)
Origin incomplete, metric 0, localpref 200, valid, external
50000, (received-only)
192.168.3.2 from 192.168.3.2 (172.17.1.0)
Origin incomplete, metric 0, localpref 100, valid, external
40000
192.168.1.2 from 192.168.1.2 (172.16.1.0)
Origin incomplete, metric 0, localpref 200, valid, external, best

Configuration Examples for BGP 4 Soft Configuration
Examples: BGP Soft Reset
The following examples show two ways to reset the connection for BGP peer 192.168.1.1.
Example: Dynamic Inbound Soft Reset
The following example shows the command used to initiate a dynamic soft reconfiguration in the BGP peer
192.168.1.1. This command requires that the peer support the route refresh capability.
clear ip bgp 192.168.1.1 soft in

IP Routing: BGP Configuration Guide
165


BGP 4 Soft Configuration
Additional References

Example: Inbound Soft Reset Using Stored Information
The following example shows how to enable inbound soft reconfiguration for the neighbor 192.168.1.1. All
the updates received from this neighbor will be stored unmodified, regardless of the inbound policy. When
inbound soft reconfiguration is performed later, the stored information will be used to generate a new set of
inbound updates.
router bgp 100
neighbor 192.168.1.1 remote-as 200
neighbor 192.168.1.1 soft-reconfiguration inbound

The following example clears the session with the neighbor 192.168.1.1:
clear ip bgp 192.168.1.1 soft in

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

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

Feature Information for BGP 4 Soft Configuration
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.

IP Routing: BGP Configuration Guide
166


BGP 4 Soft Configuration
Feature Information for BGP 4 Soft Configuration

Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 14: Feature Information for BGP 4 Soft Configuration

Feature Name

Releases

Feature Information

BGP 4 Soft Configuration

Cisco IOS XE Release 2.1

BGP 4 Soft Configuration allows
BGP4 policies to be configured and
activated without clearing the BGP
session, hence without invalidating
the forwarding cache.
This feature was introduced on the
Cisco ASR 1000 Series Routers.

IP Routing: BGP Configuration Guide
167


BGP 4 Soft Configuration
Feature Information for BGP 4 Soft Configuration

IP Routing: BGP Configuration Guide
168
