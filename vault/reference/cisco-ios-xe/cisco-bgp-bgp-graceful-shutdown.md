---
title: "BGP Graceful Shutdown"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-graceful-shutdown
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 59 BGP Graceful Shutdown The BGP Graceful Shutdown feature reduces or eliminates the loss of traffic along a link being shut down for maintenance. Routers always have a valid route available during the convergence process. This feature is used primarily for maintenance on a link between a Provider Edge (PE), PE-PE, PE- Route Reflector (RR), PE-Customer Edge (CE) and CE. • Finding Feature"
---

# BGP Graceful Shutdown

CHAPTER

59

BGP Graceful Shutdown
The BGP Graceful Shutdown feature reduces or eliminates the loss of traffic along a link being shut down
for maintenance. Routers always have a valid route available during the convergence process. This feature is
used primarily for maintenance on a link between a Provider Edge (PE), PE-PE, PE- Route Reflector (RR),
PE-Customer Edge (CE) and CE.
• Finding Feature Information, on page 903
• Information About BGP Graceful Shutdown, on page 903
• How to Configure BGP Graceful Shutdown, on page 904
• Configuration Examples for BGP Graceful Shutdown, on page 910
• Additional References, on page 912
• Feature Information for BGP Graceful Shutdown, on page 913

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Graceful Shutdown
Purpose and Benefits of BGP Graceful Shutdown
There are times when planned maintenance operations cause routing changes in BGP. After the shutdown of
eBGP and iBGP peering sessions between autonomous system border routers (ASBRs), BGP devices are
temporarily unreachable during BGP convergence. The goal of gracefully shutting down one or more BGP
sessions is to minimize traffic loss during the planned shutdown and subsequent reestablishment of the sessions.
The BGP Graceful Shutdown feature reduces or eliminates the loss of inbound or outbound traffic flows that
were initially forwarded along the peering link that is being shut down for maintenance. This feature is primarily
for PE-CE, PE-RR and PE-PE links. Lowering the local preference for paths received over the session being
shutdown renders the affected paths less preferred by the BGP decision process, but still allows the paths to

IP Routing: BGP Configuration Guide
903


BGP Graceful Shutdown
GSHUT Community

be used during the convergence while alternative paths are propagated to the affected devices. Therefore,
devices always have a valid route available during the convergence process.
The feature also allows vendors to provide a graceful shutdown mechanism that does not require any router
reconfiguration at maintenance time. The benefits of the BGP Graceful Shutdown feature are fewer lost packets
and less time spent reconfiguring devices.

GSHUT Community
The GSHUT community is a well-known community used in conjunction with the BGP Graceful Shutdown
feature. The GSHUT community attribute is applied to a neighbor specified by the neighbor shutdown
graceful command, thereby gracefully shutting down the link in an expected number of seconds. The GSHUT
community is always sent by the GSHUT initiator.
The GSHUT community is specified in a community list, which is referenced by a route map and then used
to make policy routing decisions.
The GSHUT community can also be used in the show ip bgp community command to limit output to GSHUT
routes.

BGP GSHUT Enhancement
The BGP Graceful Shutdown (GSHUT) Enhancement feature enables graceful shutdown of either all neighbors
or only virtual routing and forwarding (VRF) neighbors across BGP sessions. To enable the BGP GSHUT
enhancement feature on the device, you must configure either the community keyword or the local-preference
keyword in the bgp graceful-shutdown all command. Use the activate keyword to activate graceful
shutdown either across all neighbors or only across all VRF neighbors, across all BGP sessions.

How to Configure BGP Graceful Shutdown
Shutting Down a BGP Link Gracefully
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp autonomous-system-number
neighbor {ipv4-address | ipv6-address} remote-as number
neighbor {ipv4-address | ipv6-address | peer-group-name} shutdown graceful seconds {community
value [local-preference value] | local-preference value}
6. end
7. show ip bgp community gshut
DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: BGP Configuration Guide
904


BGP Graceful Shutdown
Shutting Down a BGP Link Gracefully

Command or Action
Example:

Purpose
• Enter your password if prompted.

Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router bgp autonomous-system-number

Configures a BGP routing process.

Example:
Device(config)# router bgp 5000

Step 4

neighbor {ipv4-address | ipv6-address} remote-as number Configures the autonomous system (AS) to which the
neighbor belongs.
Example:
Device(config-router)# neighbor 2001:db8:3::1
remote-as 5500

Step 5

neighbor {ipv4-address | ipv6-address | peer-group-name} Configures the device to gracefully shut down the link to
the specified peer in the specified number of seconds;
shutdown graceful seconds {community value
advertises the route with the GSHUT (Graceful Shutdown)
[local-preference value] | local-preference value}
community; and advertises the route with another
Example:
community or specifies a local preference value for the
route, or both.
Device(config-router)# neighbor 2001:db8:3::1
shutdown graceful 600 community 1200
local-preference 300

• Make sure to specify an adequate amount of time for
iBGP peers to converge and to choose an alternate path
as the best path.
• If the graceful keyword is used in the neighbor
shutdown command, at least one of the two attributes
(a community or local preference) must be configured.
You may configure both attributes.
• If the graceful keyword is used in the neighbor
shutdown command, the route is advertised with the
GSHUT community by default. You may also set one
other community for policy routing purposes.
• In this particular example, the route to the neighbor is
configured to shut down in 600 seconds, is advertised
with the GSHUT community and community 1200,
and is configured with a local preference of 300.
• The device receiving the advertisement looks at the
community value(s) of the route and optionally uses
the community value to apply routing policy. Filtering
routes based on a community is done with the ip
community-list command and a route map.

IP Routing: BGP Configuration Guide
905


BGP Graceful Shutdown
Filtering BGP Routes Based on the GSHUT Community

Command or Action

Purpose
• During the graceful shutdown, the neighbor shutdown
command is not nvgened. After the timer expires,
SHUTDOWN is nvgened.

Step 6

Returns to EXEC mode.

end
Example:
Device(config-router)# end

Step 7

show ip bgp community gshut
Example:

(Optional) Displays information about the routes that are
advertised with the well-known GSHUT community.

Device# show ip bgp community gshut

Filtering BGP Routes Based on the GSHUT Community
Perform this task on a BGP peer to the device where you enabled the BGP Graceful Shutdown feature.
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

enable
configure terminal
router bgp autonomous-system-number
neighbor {ipv4-address | ipv6-address} remote-as number
neighbor {ipv4-address | ipv6-address} activate
neighbor {ipv4-address | ipv6-address} send-community
exit
route-map map-tag [permit | deny] [sequence-number]
match community {standard-list-number | expanded-list-number | community-list-name [exact]}
exit
ip community-list {standard | standard list-name} {deny | permit} gshut
router bgp autonomous-system-number
neighbor address route-map map-name in

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
Example:

IP Routing: BGP Configuration Guide
906

Enters global configuration mode.


BGP Graceful Shutdown
Filtering BGP Routes Based on the GSHUT Community

Command or Action

Purpose

Device# configure terminal

Step 3

router bgp autonomous-system-number

Configures a BGP routing process.

Example:
Device(config)# router bgp 2000

Step 4

neighbor {ipv4-address | ipv6-address} remote-as
number

Configures the autonomous system (AS) to which the
neighbor belongs.

Example:
Device(config-router)# neighbor 2001:db8:4::1
remote-as 1000

Step 5

neighbor {ipv4-address | ipv6-address} activate

Activates the neighbor.

Example:
Device(config-router)# neighbor 2001:db8:4::1
activate

Step 6

neighbor {ipv4-address | ipv6-address} send-community Enables BGP community exchange with the neighbor.
Example:
Device(config-router)# neighbor 2001:db8:4::1
send-community

Step 7

exit

Exits router configuration mode.

Example:
Device(config-router)# exit

Step 8

route-map map-tag [permit | deny] [sequence-number] Configures a route map to permit or deny routes for policy
routing.
Example:
Device(config)# route-map RM_GSHUT deny 10

Step 9

match community {standard-list-number |
expanded-list-number | community-list-name [exact]}

Configures that the routes that match ip community-list
GSHUT will be policy routed.

Example:
Device(config-route-map)# match community GSHUT

Step 10

exit

Exits route-map configuration mode.

Example:
Device(config-route-map)# exit

IP Routing: BGP Configuration Guide
907


BGP Graceful Shutdown
Configuring BGP GSHUT Enhancement

Command or Action
Step 11

Purpose

ip community-list {standard | standard list-name} {deny Configures a community list and permits or denies routes
that have the GSHUT community to the community list.
| permit} gshut
Example:
Device(config)# ip community-list standard GSHUT
permit gshut

Step 12

router bgp autonomous-system-number

• If you specify other communities in the same
statement, there is a logical AND operation and all
communities in the statement must match the
communities for the route in order for the statement
to be processed.
Configures a BGP routing process.

Example:
Device(config)# router bgp 2000

Step 13

neighbor address route-map map-name in
Example:
Device(config)# neighbor 2001:db8:4::1 route-map
RM_GSHUT in

Applies the route map to incoming routes from the
specified neighbor.
• In this example, the route map named RM_GSHUT
denies routes from the specified neighbor that have
the GSHUT community.

Configuring BGP GSHUT Enhancement
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
bgp graceful-shutdown all {neighbors | vrfs} shutdown-time {community community-value
[local-preference local-pref-value] | local-preference local-pref-value [community community-value]}
bgp graceful-shutdown all {neighbors | vrfs} activate
end
show ip bgp
show running-config

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
Example:

IP Routing: BGP Configuration Guide
908

Enters global configuration mode.


BGP Graceful Shutdown
Configuring BGP GSHUT Enhancement

Command or Action

Purpose

Device# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Enters router configuration mode to create or configure a
BGP routing process.

Device(config)# router bgp 65000

Step 4

bgp graceful-shutdown all {neighbors | vrfs}
shutdown-time {community community-value
[local-preference local-pref-value] | local-preference
local-pref-value [community community-value]}

Enables the BGP GSHUT enhancement feature on the
device.

Example:
Device(config-router)# bgp graceful-shutdown all
neighbors 180 local-preference 20 community 10

Step 5

bgp graceful-shutdown all {neighbors | vrfs} activate Activates graceful shutdown across all neighbors or only
across VRF neighbors for BGP sessions.
Example:
Device(config-router)# bgp graceful-shutdown all
neighbors activate

Step 6

end

Returns to privileged EXEC mode.

Example:
Device(config-router)# end

Step 7

show ip bgp

Displays entries in the BGP routing table.

Example:
Device# show ip bgp neighbors 10.2.2.2 | include
shutdown

Step 8

show running-config

Displays running configuration on the device.

Example:
Device# show running-config | session router bgp

IP Routing: BGP Configuration Guide
909


BGP Graceful Shutdown
Configuration Examples for BGP Graceful Shutdown

Configuration Examples for BGP Graceful Shutdown
Example: Shutting Down a BGP Link Gracefully
Graceful Shutdown While Setting a Local-Preference
This example gracefully shuts down the link to the specified neighbor in 600 seconds, adds the
GSHUT community to the route, and sets a local preference of 500 for the route.
router bgp 1000
neighbor 2001:db8:5::1 remote-as 2000
neighbor 2001:db8:5::1 shutdown graceful 600 local-preference 500
neighbor 2001:db8:5::1 send-community
exit

Graceful Shutdown While Setting an Additional Community
This example gracefully shuts down the link to the specified neighbor in 600 seconds, and adds the
GSHUT community and numbered community to the route.
router bgp 1000
neighbor 2001:db8:5::1 remote-as 2000
neighbor 2001:db8:5::1 shutdown graceful 600 community 1400
neighbor 2001:db8:5::1 send-community
exit

Graceful Shutdown while Setting an Additional Community and Local-Preference
This example gracefully shuts down the link to the specified neighbor in 600 seconds, adds the
GSHUT community and the numbered community to the route, and sets a local preference of 500
to the route.
router bgp 1000
neighbor 2001:db8:5::1 remote-as 2000
neighbor 2001:db8:5::1 shutdown graceful 600 community 1400 local-preference 500
neighbor 2001:db8:5::1 send-community
exit

Example: Filtering BGP Routes Based on the GSHUT Community
In additional to being able to gracefully shut down a BGP route, another use of the GSHUT community
is to configure a community list to filter routes with this community from getting into the BGP routing
table.

IP Routing: BGP Configuration Guide
910


BGP Graceful Shutdown
Example: BGP GSHUT Enhancement

This example illustrates how to use a community list to filter incoming BGP routes based on the
GSHUT community. In this example, a route map named RM_GSHUT denies routes based on a
standard community list named GSHUT. The community list contains routes with the GSHUT
community. The route map is then applied to incoming routes from the neighbor at 2001:db8:4::1.
router bgp 2000
neighbor 2001:db8:4::1 remote-as 1000
neighbor 2001:db8:4::1 activate
neighbor 2001:db8:4::1 send-community
exit
route-map RM_GSHUT deny 10
match community GSHUT
exit
ip community-list standard GSHUT permit gshut
router bgp 2000
neighbor 2001:db8:4::1 route-map RM_GSHUT in

Example: BGP GSHUT Enhancement
The following example shows how to enable and activate the BGP GSHUT enhancement feature
across all neighbors. In this example, the neighbors are configured to gracefully shutdown within
the specified duration of 180 seconds.
Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# bgp graceful-shutdown all neighbors 180 local-preference 20 community
10
Device(config-router)# bgp graceful-shutdown all neighbors activate
Device(config-router)# end

Following is sample output from the show ip bgp command, which displays the graceful shutdown
time for each neighbor. In this example, there are two IPv4 neighbors configured with IP address
10.2.2.2 and 172.16.2.1 and one VRF neighbor, tagged v1, is configured with IP address 192.168.1.1.
Device# show ip bgp neighbors 10.2.2.2 | include shutdown
Graceful Shutdown Timer running, schedule to reset the peer in 00:02:47 seconds
Graceful Shutdown Localpref set to 20
Graceful Shutdown Community set to 10
Device# show ip bgp neighbors 172.16.2.1 | include shutdown
Graceful Shutdown Timer running, schedule to reset the peer in 00:02:38 seconds
Graceful Shutdown Localpref set to 20
Graceful Shutdown Community set to 10
Device# show ip bgp vpnv4 vrf v1 neighbors 192.168.1.1 | include shutdown
Graceful Shutdown Timer running, schedule to reset the peer in 00:01:45 seconds
Graceful Shutdown Localpref set to 20
Graceful Shutdown Community set to 10

Following is sample output from the show running-config command, which displays information
associated with the BGP session in router configuration mode:

IP Routing: BGP Configuration Guide
911


BGP Graceful Shutdown
Additional References

Device# show running-config | session router bgp
router bgp 65000
bgp log-neighbor-changes
bgp graceful-shutdown all neighbors 180 local-preference 20 community 10
network 10.1.1.0 mask 255.255.255.0
neighbor 10.2.2.2 remote-as 40
neighbor 10.2.2.2 shutdown
neighbor 172.16.2.1 remote-as 10
neighbor 172.16.2.1 shutdown
!
address-family vpnv4
neighbor 172.16.2.1 activate
neighbor 172.16.2.1 send-community both
exit-address-family
!
address-family ipv4 vrf v1
neighbor 192.168.1.1 remote-as 30
neighbor 192.168.1.1 shutdown
neighbor 192.168.1.1 activate
neighbor 192.168.1.1 send-community both
exit-address-family

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

Standards and RFCs
Standard/RFC Title
RFC 6198

Requirements for the Graceful Shutdown of BGP Sessions

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
912


BGP Graceful Shutdown
Feature Information for BGP Graceful Shutdown

Feature Information for BGP Graceful Shutdown
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 78: Feature Information for BGP Graceful Shutdown

Feature Name

Releases

Feature Information

BGP Graceful Shutdown

Cisco IOS XE Release 3.6S

The BGP Graceful Shutdown
feature reduces or eliminates the
loss of traffic along a link being
shut down for maintenance. Routers
always have a valid route available
during the convergence process.

Cisco IOS XE Release 3.7S

The following commands were
modified: ip community-list,
neighbor shutdown, show ip bgp
community, and show ip bgp
vpnv4.
BGP GSHUT Enhancement

Cisco IOS XE Release 3.11S

The BGP Graceful Shutdown
(GSHUT) Enhancement feature
enables graceful shutdown of either
all neighbors or only virtual routing
and forwarding (VRF) neighbors
across BGP sessions.
The following command was
introduced: bgp
graceful-shutdown all.

IP Routing: BGP Configuration Guide
913


BGP Graceful Shutdown
Feature Information for BGP Graceful Shutdown

IP Routing: BGP Configuration Guide
914
