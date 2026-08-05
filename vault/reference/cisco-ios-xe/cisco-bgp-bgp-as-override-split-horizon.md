---
title: "BGP AS-Override Split-Horizon"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-as-override-split-horizon
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 84 BGP AS-Override Split-Horizon The BGP AS-Override Split-Horizon feature enables a Provider Edge (PE) device using split-horizon to avoid advertisement of routes propagated by a Customer Edge (CE) device to the same CE device. The BGP AS-Override Split-Horizon feature also enables a PE or CE device to send route updates to a specific PE or CE device in the same replication group. • Fin"
---

# BGP AS-Override Split-Horizon

CHAPTER

84

BGP AS-Override Split-Horizon
The BGP AS-Override Split-Horizon feature enables a Provider Edge (PE) device using split-horizon to avoid
advertisement of routes propagated by a Customer Edge (CE) device to the same CE device. The BGP
AS-Override Split-Horizon feature also enables a PE or CE device to send route updates to a specific PE or
CE device in the same replication group.
• Finding Feature Information, on page 1141
• Information About BGP AS-Override Split-Horizon, on page 1141
• How to Configure BGP AS-Override Split-Horizon, on page 1142
• Verifying BGP AS-Override Split-Horizon, on page 1143
• Configuration Examples for BGP AS-Override Split-Horizon, on page 1144
• Additional References for BGP AS-Override Split-Horizon, on page 1146
• Feature Information for BGP AS-Override Split-Horizon, on page 1147

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP AS-Override Split-Horizon
BGP AS-Override Split-Horizon Overview
When you configure split-horizon on a device, the Provider Edge (PE) device may advertise routes propagated
from a Customer Edge (CE) device to the same CE device. The BGP AS-Override Split Horizon feature
groups all the BGP neighbors into separate replication-groups, even when they are in the same update-group,
and ensures that the route updates propagated from a CE device are not sent to the same CE device.
The BGP AS-Override Split Horizon feature enables a PE or CE device to selectively send and block updates
to one or more neighboring PE or CE devices in the same update-group. The PE or CE device sends or blocks

IP Routing: BGP Configuration Guide
1141


BGP AS-Override Split-Horizon
How to Configure BGP AS-Override Split-Horizon

a message to a neighboring PE or CE device based on the type of the message and on whether the originator
of the message matches the router ID of the PE or CE device.

How to Configure BGP AS-Override Split-Horizon
Configuring BGP AS-Override Split-Horizon
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
address family ipv4 vrf vrf-name
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address activate
neighbor ip-address as-override split-horizon
Repeat Step 5 to Step 7 to enable split-horizon for different neighbors in a virtual routing and forwarding
(VRF) instance.
9. end
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

Configures the Border Gateway Protocol (BGP) routing
process and enters router configuration mode.

Device(config)# router bgp 21

Step 4

address family ipv4 vrf vrf-name
Example:
Device(config-router)# address-family ipv4 vrf vrf1

IP Routing: BGP Configuration Guide
1142

Specifies the name of the VPN routing and forwarding
(VRF) instance to associate with subsequent IPv4 address
family configuration mode commands and enters
address-family configuration mode.


BGP AS-Override Split-Horizon
Verifying BGP AS-Override Split-Horizon

Step 5

Command or Action

Purpose

neighbor ip-address remote-as
autonomous-system-number

Configures peering with a BGP neighbor in the specified
autonomous system.

Example:
Device(config-router-af)# neighbor 192.0.2.1
remote-as 1

Step 6

neighbor ip-address activate
Example:

Enables the neighbor to exchange prefixes for the IPv4
address family with the local device.

Device(config-router-af)# neighbor 192.0.2.1
activate

Step 7

neighbor ip-address as-override split-horizon

Enables split-horizon per neighbor in a VRF instance.

Example:
Device(config-router-af)# neighbor 192.0.2.1
as-override split-horizon

Step 8

Repeat Step 5 to Step 7 to enable split-horizon for different —
neighbors in a virtual routing and forwarding (VRF)
instance.

Step 9

end

Exits router address-family configuration mode and enters
privileged EXEC mode.

Example:
Device(config-router-af)# end

Verifying BGP AS-Override Split-Horizon
SUMMARY STEPS
1.
2.
3.
4.

enable
show ip bgp vpn4 all update-group
show ip bgp vpnv4 all neighbors ip-address
show ip bgp vpnv4 all neighbors ip-address policy

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

IP Routing: BGP Configuration Guide
1143


BGP AS-Override Split-Horizon
Configuration Examples for BGP AS-Override Split-Horizon

Step 2

Command or Action

Purpose

show ip bgp vpn4 all update-group

Displays information on update groups.

Example:
Device# show ip bgp vpn4 all update-group

Step 3

show ip bgp vpnv4 all neighbors ip-address

Displays details about neighbor connections.

Example:
Device# show ip bgp vpnv4 all neighbors 192.0.2.1

Step 4

show ip bgp vpnv4 all neighbors ip-address policy

Displays neighbor policies per address-family.

Example:
Device# show ip bgp vpnv4 all neighbors 192.0.2.1
policy

Configuration Examples for BGP AS-Override Split-Horizon
Example: BGP AS-Override Split-Horizon Configuration
Device> enable
Device# configure terminal
Device(config)# router bgp 21
Device(config-router)# address-family ipv4 vrf vrf1
Device(config-router-af)# neighbor 192.0.2.1 remote-as 1
Device(config-router-af)# neighbor 192.0.2.1 activate
Device(config-router-af)# neighbor 192.0.2.1 as-override split-horizon
Device(config-router-af)# neighbor 198.51.100.1 remote-as 1
Device(config-router-af)# neighbor 198.51.100.1 activate
Device(config-router-af)# neighbor 198.51.100.1 as-override split-horizon
Device(config-router-af)# end

Example: Verifying BGP AS-Override Split-Horizon
Sample output for the show ip bgp vpn4 all update-group command
To display information about update groups, use the show ip bgp vpn4 all update-group command in
privileged EXEC mode.
Device> enable
Device# show ip bgp vpn4 all update-group
BGP version 4 update-group 3, external, Address Family: VPNv4 Unicast
BGP Update version : 5/0, messages 0 active RGs: 2 <<<<<<<<<<<<<<
Overrides the neighbor AS 1 with my AS before sending updates
Topology: blue, highest version: 5, tail marker: 5
Format state: Current working (OK, last not in list)
Refresh blocked (not in list, last not in list)
Update messages formatted 1, replicated 2, current 0, refresh 0, limit 1000
Number of NLRIs in the update sent: max 4, min 0

IP Routing: BGP Configuration Guide
1144


BGP AS-Override Split-Horizon
Example: Verifying BGP AS-Override Split-Horizon

Minimum time between advertisement runs is 0 seconds
Has 2 members:
192.0.2.1
198.51.100.1

Sample output for the show ip bgp vpnv4 all neighbors ip-address command
To display details about neighbor connections, use the show ip bgp vpnv4 all neighbors ip-address
command in privileged EXEC mode.
Device> enable
Device# show ip bgp vpnv4 all neighbors 209.165.200.228
BGP neighbor is 209.165.200.228, vrf vrf1, remote AS 1, external link
BGP version 4, remote router ID 209.165.201.28
BGP state = Established, up for 00:01:26
Last read 00:00:35, last write 00:00:28, hold time is 180, keepalive interval is 60 seconds
Neighbor sessions:
1 active, is not multisession capable (disabled)
Neighbor capabilities:
Route refresh: advertised and received(new)
Four-octets ASN Capability: advertised and received
Address family IPv4 Unicast: advertised and received
Enhanced Refresh Capability: advertised and received
Multisession Capability:
Stateful switchover support enabled: NO for session 1
Message statistics:
InQ depth is 0
OutQ depth is 0
Sent
Rcvd
Opens:
1
1
Notifications:
0
0
Updates:
6
2
Keepalives:
3
3
Route Refresh:
0
0
Total:
12
6
Default minimum time between advertisement runs is 0 seconds
For address family: VPNv4 Unicast
Translates address family IPv4 Unicast for VRF vrf1
Session: 209.165.200.228
BGP table version 40, neighbor version 40/0
Output queue size : 0
Index 1, Advertise bit 1
1 update-group member
Overrides the neighbor AS with my AS before sending updates
Split horizon processing before sending updates
Slow-peer detection is disabled
Slow-peer split-update-group dynamic is disabled
Sent
Rcvd
Prefix activity:
------Prefixes Current:
10
2 (Consumes 160 bytes)
Prefixes Total:
10
2
Implicit Withdraw:
0
0
Explicit Withdraw:
0
0
Used as bestpath:
n/a
2
Used as multipath:
n/a
0
Outbound
Inbound
Local Policy Denied Prefixes:
-------------Total:
0
0
Number of NLRIs in the update sent: max 5, min 0
Last detected as dynamic slow peer: never
Dynamic slow peer recovered: never
Refresh Epoch: 1

IP Routing: BGP Configuration Guide
1145


BGP AS-Override Split-Horizon
Additional References for BGP AS-Override Split-Horizon

Last Sent Refresh Start-of-rib: 00:01:26
Last Sent Refresh End-of-rib: 00:01:26
Refresh-Out took 0 seconds
Last Received Refresh Start-of-rib: never
Last Received Refresh End-of-rib: never
Sent
Refresh activity:
---Refresh Start-of-RIB
1
Refresh End-of-RIB
1

Rcvd
---0
0

Address tracking is enabled, the RIB does have a route to 209.165.200.228
Connections established 3; dropped 2
Last reset 00:01:35, due to split-horizon config change of session 1
Transport(tcp) path-mtu-discovery is enabled
Graceful-Restart is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0
Connection is ECN Disabled
Mininum incoming TTL 0, Outgoing TTL 1
Local host: 209.165.200.225, Local port: 22789
Foreign host: 209.165.200.228, Foreign port: 179
Connection tableid (VRF): 2

Sample output for the show ip bgp vpnv4 all neighbors ip-address policy command
To display neighbor policies per address-family, use the show ip bgp vpnv4 all neighbors ip-address
policy command in privileged EXEC mode.
Device> enable
Device# show ip bgp vpnv4 all neighbors 209.165.200.228
Neighbor: 209.165.200.228, Address-Family: VPNv4 Unicast (vrf1)
Locally configured policies:
as-override split-horizon

Additional References for BGP AS-Override Split-Horizon
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
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

IP Routing: BGP Configuration Guide
1146


BGP AS-Override Split-Horizon
Feature Information for BGP AS-Override Split-Horizon

Feature Information for BGP AS-Override Split-Horizon
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 104: Feature Information for BGP AS-Override Split-Horizon

Feature Name

Releases

Feature Information

BGP AS-Override Split-Horizon

Cisco IOS XE Release 3.14S

The BGP AS-Override
Split-Horizon feature enables a
Provider Edge (PE) device using
split-horizon to avoid advertisement
of routes propagated by a Customer
Edge (CE) device to the same CE
device. The BGP AS-Override
Split-Horizon feature also enables
a PE or CE device to send route
updates to specific PE or CE device
in the same replication group.
The following command was
introduced or modified: neighbor
ip-address as-override
split-horizon.

IP Routing: BGP Configuration Guide
1147


BGP AS-Override Split-Horizon
Feature Information for BGP AS-Override Split-Horizon

IP Routing: BGP Configuration Guide
1148
