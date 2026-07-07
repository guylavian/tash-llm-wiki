---
title: "BGP Dynamic Neighbors"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-dynamic-neighbors
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 18 BGP Dynamic Neighbors BGP dynamic neighbor support allows BGP peering to a group of remote neighbors that are defined by a range of IP addresses. Each range can be configured as a subnet IP address. BGP dynamic neighbors are configured using a range of IP addresses and BGP peer groups. • Finding Feature Information, on page 403 • Information About BGP Dynamic Neighbors, on page 403 •"
---

# BGP Dynamic Neighbors

CHAPTER

18

BGP Dynamic Neighbors
BGP dynamic neighbor support allows BGP peering to a group of remote neighbors that are defined by a
range of IP addresses. Each range can be configured as a subnet IP address. BGP dynamic neighbors are
configured using a range of IP addresses and BGP peer groups.
• Finding Feature Information, on page 403
• Information About BGP Dynamic Neighbors, on page 403
• How to Configure BGP Dynamic Neighbors, on page 404
• Configuration Examples for BGP Dynamic Neighbors, on page 413
• Additional References, on page 416
• Feature Information for BGP Dynamic Neighbors, on page 416

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Dynamic Neighbors
BGP Dynamic Neighbors
Support for the BGP Dynamic Neighbors feature was introduced in Cisco IOS Release 12.2(33)SXH on the
Cisco Catalyst 6500 series switches. BGP dynamic neighbor support allows BGP peering to a group of remote
neighbors that are defined by a range of IP addresses. Each range can be configured as a subnet IP address.
BGP dynamic neighbors are configured using a range of IP addresses and BGP peer groups.
In Cisco IOS XE Denali 16.3 release, support for BGP dynamic neighbors was extended to IPv6 BGP peering
with VRF support.
After a subnet range is configured for a BGP peer group and a TCP session is initiated by another router for
an IP address in the subnet range, a new BGP neighbor is dynamically created as a member of that group.

IP Routing: BGP Configuration Guide
403


BGP Dynamic Neighbors
How to Configure BGP Dynamic Neighbors

After the initial configuration of subnet ranges and activation of the peer group (referred to as a listen range
group ), dynamic BGP neighbor creation does not require any further CLI configuration on the initial router.
Other routers can establish a BGP session with the initial router, but the initial router need not establish a BGP
session to other routers if the IP address of the remote peer used for the BGP session is not within the configured
range.
To support the BGP Dynamic Neighbors feature, the output for the show ip bgp neighbors, show ip bgp
peer-group, and show ip bgp summary commands was updated to display information about dynamic
neighbors.
A dynamic BGP neighbor will inherit any configuration for the peer group. In larger BGP networks,
implementing BGP dynamic neighbors can reduce the amount and complexity of CLI configuration and save
CPU and memory usage. Only IPv4 peering is supported.

How to Configure BGP Dynamic Neighbors
Implementing BGP Dynamic Neighbors Using Subnet Ranges
In Cisco IOS Release 12.2(33)SXH, support for BGP dynamic neighbors was introduced. Perform this task
to implement the dynamic creation of BGP neighbors using subnet ranges.
In this task, a BGP peer group is created on Router B in the figure below, a global limit is set on the number
of dynamic BGP neighbors, and a subnet range is associated with a peer group. Configuring the subnet range
enables the dynamic BGP neighbor process. The peer group is added to the BGP neighbor table of the local
router, and an alternate autonomous system number is also configured. The peer group is activated under the
IPv4 address family.
The next step is to move to another router—Router E in the figure below—where a BGP session is started
and the neighbor router, Router B, is configured as a remote BGP peer. The peering configuration opens a
TCP session and triggers Router B to create a dynamic BGP neighbor because the IP address that starts the
TCP session (192.168.3.2) is within the configured subnet range for dynamic BGP peers. The task moves
back to the first router, Router B, to run three show commands that have been modified to display dynamic
BGP peer information.

IP Routing: BGP Configuration Guide
404


BGP Dynamic Neighbors
Implementing BGP Dynamic Neighbors Using Subnet Ranges

Figure 36: BGP Dynamic Neighbor Topology

Before you begin
This task requires Cisco IOS Release 12.2(33)SXH, or a later release, to be running.

Note

This task supports only IPv4 BGP peering.

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
16.

enable
configure terminal
router bgp autonomous-system-number
bgp log-neighbor-changes
neighbor peer-group-name peer-group
bgp listen [limit max-number]
bgp listen [limit max-number | range network / length peer-group peer-group-name]
neighbor {ip-address | ipv6-address | peer-group-name} ebgp-multihop [ttl]
neighbor peer-group-name remote-as autonomous-system-number [alternate-as
autonomous-system-number...]
address-family ipv4 [mdt | multicast | unicast [vrf vrf-name]]
neighbor {ip-address | peer-group-name} activate
end
Move to another router that has an interface within the subnet range for the BGP peer group configured
in this task.
enable
configure terminal
router bgp autonomous-system-number

IP Routing: BGP Configuration Guide
405


BGP Dynamic Neighbors
Implementing BGP Dynamic Neighbors Using Subnet Ranges

17.
18.
19.
20.
21.

neighbor {ip-address| peer-group-name} remote-as autonomous-system-number [alternate-as
autonomous-system-number...]
Return to the first router.
show ip bgp summary
show ip bgp peer-group [peer-group-name] [summary]
show ip bgp neighbors [ip-address]

DETAILED STEPS

Step 1

Step 2

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

DeviceB> enable

• The configuration is entered on router B.

configure terminal

Enters global configuration mode.

Example:
DeviceB# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.

DeviceB(config)# router bgp 45000

Step 4

bgp log-neighbor-changes
Example:
DeviceB(config-router)# bgp log-neighbor-changes

Step 5

neighbor peer-group-name peer-group
Example:
DeviceB(config-router)# neighbor group192
peer-group

Step 6

bgp listen [limit max-number]
Example:
DeviceB(config-router)# bgp listen limit 200

(Optional) Enables logging of BGP neighbor status changes
(up or down) and neighbor resets.
• Use this command for troubleshooting network
connectivity problems and measuring network
stability. Unexpected neighbor resets might indicate
high error rates or high packet loss in the network and
should be investigated.
Creates a BGP peer group.
• In this example, a peer group named group192 is
created. This group will be used as a listen range
group.
Sets a global limit of BGP dynamic subnet range neighbors.
• Use the optional limit keyword and max-number
argument to define the maximum number of BGP
dynamic subnet range neighbors that can be created.
Note

IP Routing: BGP Configuration Guide
406

Only the syntax applicable to this task is used
in this example. For the complete syntax, see
Step 7.


BGP Dynamic Neighbors
Implementing BGP Dynamic Neighbors Using Subnet Ranges

Step 7

Command or Action

Purpose

bgp listen [limit max-number | range network / length
peer-group peer-group-name]

Associates a subnet range with a BGP peer group and
activates the BGP dynamic neighbors feature.

Example:
DeviceB(config-router)# bgp listen range
192.168.0.0/16 peer-group group192

• Use the optional limit keyword and max-number
argument to define the maximum number of BGP
dynamic neighbors that can be created.
• Use the optional range keyword and network / length
argument to define a prefix range to be associated
with the specified peer group.
• In this example, the prefix range 192.168.0.0/16 is
associated with the listen range group named
group192.

Step 8

neighbor {ip-address | ipv6-address | peer-group-name} Accepts and attempts BGP connections to external peers
residing on networks that are not directly connected.
ebgp-multihop [ttl]
Example:
DeviceB(config-router)# neighbor group192
ebgp-multihop 255

Step 9

neighbor peer-group-name remote-as
autonomous-system-number [alternate-as
autonomous-system-number...]
Example:
DeviceB(config-router)# neighbor group192
remote-as 40000 alternate-as 50000

Adds the IP address or peer group name of the neighbor
in the specified autonomous system to the IPv4
multiprotocol BGP neighbor table of the local router.
• Use the optional alternate-as keyword and
autonomous-system-number argument to identify up
to five alternate autonomous system numbers for
listen range neighbors.
• In this example, the peer group named group192 is
configured with two possible autonomous system
numbers.
Note

Step 10

address-family ipv4 [mdt | multicast | unicast [vrf
vrf-name]]
Example:

The alternate-as keyword is used only with the
listen range peer groups, not with individual
BGP neighbors.

Enters address family configuration mode to configure
BGP peers to accept address-family-specific
configurations.

DeviceB(config-router)# address-family ipv4
unicast

Step 11

neighbor {ip-address | peer-group-name} activate
Example:
DeviceB(config-router-af)# neighbor group192
activate

Activates the neighbor or listen range peer group for the
configured address family.
• In this example, the neighbor 172.16.1.1 is activated
for the IPv4 address family.

IP Routing: BGP Configuration Guide
407


BGP Dynamic Neighbors
Implementing BGP Dynamic Neighbors Using Subnet Ranges

Command or Action

Purpose
Note

Step 12

end
Example:

Usually BGP peer groups cannot be activated
using this command, but the listen range peer
groups are a special case.

Exits address family configuration mode and returns to
privileged EXEC mode.

DeviceB(config-router-af)# end

Step 13

Move to another router that has an interface within the
subnet range for the BGP peer group configured in this
task.

—

Step 14

enable

Enables privileged EXEC mode.

Step 15

Example:

• Enter your password if prompted.

DeviceE> enable

• The configuration is entered on Router E.

configure terminal

Enters global configuration mode.

Example:
DeviceE# configure terminal

Step 16

router bgp autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.

DeviceE(config)# router bgp 50000

Step 17

neighbor {ip-address| peer-group-name} remote-as
autonomous-system-number [alternate-as
autonomous-system-number...]

Adds the IP address or peer group name of the neighbor
in the specified autonomous system to the IPv4
multiprotocol BGP neighbor table of the local router.
• In this example, the interface (192.168.3.2 in the
figure above) at Router E is with the subnet range set
for the BGP listen range group, group192. When TCP
opens a session to peer to Router B, Router B creates
this peer dynamically.

Example:
DeviceE(config-router)# neighbor 192.168.3.1
remote-as 45000

Step 18

Return to the first router.

—

Step 19

show ip bgp summary

(Optional) Displays the BGP path, prefix, and attribute
information for all connections to BGP neighbors.

Example:
DeviceB# show ip bgp summary

Step 20

• In this step, the configuration has returned to Router
B.

show ip bgp peer-group [peer-group-name] [summary] (Optional) Displays information about BGP peer groups.
Example:

IP Routing: BGP Configuration Guide
408


BGP Dynamic Neighbors
Implementing BGP Dynamic Neighbors Using Subnet Ranges

Command or Action

Purpose

DeviceB# show ip bgp peer-group group192

Step 21

show ip bgp neighbors [ip-address]
Example:
DeviceB# show ip bgp neighbors 192.168.3.2

(Optional) Displays information about BGP and TCP
connections to neighbors.
• In this example, information is displayed about the
dynamically created neighbor at 192.168.3.2. The IP
address of this BGP neighbor can be found in the
output of either the show ip bgp summary or the
show ip bgp peer-group command.
Note

Only the syntax applicable to this task is used
in this example. For more details, see the Cisco
IOS IP Routing: BGP Command Reference.

Examples
The following output examples were taken from Router B in the figure above after the appropriate
configuration steps in this task were completed on both Router B and Router E.
The following output from the show ip bgp summary command shows that the BGP neighbor
192.168.3.2 was dynamically created and is a member of the listen range group, group192. The
output also shows that the IP prefix range of 192.168.0.0/16 is defined for the listen range named
group192.
Router# show ip bgp summary
BGP router identifier 192.168.3.1, local AS number 45000
BGP table version is 1, main routing table version 1
Neighbor
V
AS MsgRcvd MsgSent
TblVer InQ OutQ Up/Down State/PfxRcd
*192.168.3.2
4 50000
2
2
0
0
0 00:00:37
0
* Dynamically created based on a listen range command
Dynamically created neighbors: 1/(200 max), Subnet ranges: 1
BGP peergroup group192 listen range group members:
192.168.0.0/16

The following output from the show ip bgp peer-group command shows information about the
listen range group, group192 that was configured in this task:
Router# show ip bgp peer-group group192
BGP peer-group is group192, remote AS 40000
BGP peergroup group192 listen range group members:
192.168.0.0/16
BGP version 4
Default minimum time between advertisement runs is 30 seconds
For address family: IPv4 Unicast
BGP neighbor is group192, peer-group external, members:
*192.168.3.2
Index 0, Offset 0, Mask 0x0
Update messages formatted 0, replicated 0
Number of NLRIs in the update sent: max 0, min 0

IP Routing: BGP Configuration Guide
409


BGP Dynamic Neighbors
Configuring BGP IPv6 Dynamic Neighbor Support with VRF Support

The following sample output from the show ip bgp neighbors command shows that the neighbor
192.168.3.2 is a member of the peer group, group192, and belongs to the subnet range group
192.168.0.0/16, which shows that this peer was dynamically created:
Router# show ip bgp neighbors 192.168.3.2
BGP neighbor is *192.168.3.2, remote AS 50000, external link
Member of peer-group group192 for session parameters
Belongs to the subnet range group: 192.168.0.0/16
BGP version 4, remote router ID 192.168.3.2
BGP state = Established, up for 00:06:35
Last read 00:00:33, last write 00:00:25, hold time is 180, keepalive intervals
Neighbor capabilities:
Route refresh: advertised and received(new)
Address family IPv4 Unicast: advertised and received
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
0
0
Keepalives:
7
7
Route Refresh:
0
0
Total:
8
8
Default minimum time between advertisement runs is 30 seconds
For address family: IPv4 Unicast
BGP table version 1, neighbor version 1/0
Output queue size : 0
Index 1, Offset 0, Mask 0x2
1 update-group member
group192 peer-group member
.
.
.

Configuring BGP IPv6 Dynamic Neighbor Support with VRF Support
In Cisco IOS XE Denali 16.3 release, support for BGP dynamic neighbors was extended to IPv6 BGP peering.

Note

You can also configure BGP IPv6 dynamic neighbors without VRF support.

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
bgp listen [limit max-number | range network / length peer-group peer-group-name]
address-family [ipv4 | ipv6] [mdt | multicast | unicast [vrf vrf-name]]
bgp listen [limit max-number]
neighbor peer-group-name peer-group
neighbor peer-group-name remote-as autonomous-system-number [alternate-as
autonomous-system-number...]

IP Routing: BGP Configuration Guide
410


BGP Dynamic Neighbors
Configuring BGP IPv6 Dynamic Neighbor Support with VRF Support

9.
10.
11.

address-family [ipv4 | ipv6] [mdt | multicast | unicast [vrf vrf-name]]
neighbor {ip-address | peer-group-name} activate
end

DETAILED STEPS

Step 1

Step 2

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

• The configuration is entered on router B.

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

bgp listen [limit max-number | range network / length
peer-group peer-group-name]
Example:
Device(config-router)# bgp listen range 2001::0/64
peer-group group192

Associates a subnet range with a BGP peer group and
activates the BGP dynamic neighbors feature.
• Use the optional limit keyword and max-number
argument to define the maximum number of BGP
dynamic neighbors that can be created.
• Use the optional range keyword and network / length
argument to define a prefix range to be associated
with the specified peer group.
• In this example, the prefix range 2001::0/64 is
associated with the listen range group named
group192.

Step 5

address-family [ipv4 | ipv6] [mdt | multicast | unicast Enters address family configuration mode to configure
BGP peers to accept address-family-specific
[vrf vrf-name]]
configurations.
Example:
Device(config-router-af)# address-family ipv6
unicast vrf vrf1

Step 6

bgp listen [limit max-number]
Example:

Specifies the maximum number of prefixes in VRF address
family.

Device(config-router)# bgp listen limit 500

Step 7

neighbor peer-group-name peer-group

Creates a BGP peer group.

IP Routing: BGP Configuration Guide
411


BGP Dynamic Neighbors
Verifying BGP IPv6 Dynamic Neighbor Configuration

Command or Action
Example:
Device(config-router)# neighbor group192
peer-group

Step 8

neighbor peer-group-name remote-as
autonomous-system-number [alternate-as
autonomous-system-number...]
Example:
Device(config-router)# neighbor group192 remote-as
101 alternate-as 102

Purpose
• In this example, a peer group named group192 is
created. This group will be used as a listen range
group.
Adds the IP address or peer group name of the neighbor
in the specified autonomous system to the IPv6 BGP
neighbor table.
• Use the optional alternate-as keyword and
autonomous-system-number argument to identify up
to five alternate autonomous system numbers for
listen range neighbors.
• In this example, the peer group named group192 is
configured with two possible autonomous system
numbers.
Note

Step 9

The alternate-as keyword is used only with the
listen range peer groups, not with individual
BGP neighbors.

address-family [ipv4 | ipv6] [mdt | multicast | unicast Enable IPv4 address family for this peer-group.
[vrf vrf-name]]
Example:
Device(config-router-af)# address-family ipv4
unicast vrf vrf1

Step 10

neighbor {ip-address | peer-group-name} activate
Example:

Activates the neighbor or listen range peer group for the
configured address family.

Device(config-router-af)# neighbor group192
activate

Step 11

end
Example:

Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

Verifying BGP IPv6 Dynamic Neighbor Configuration
Use the show bgp ipv6 unicast summary command to verify the BGP IPv6 unicast address family
configuration in global routing table:
Device# show bgp ipv6 unicast summary
BGP router identifier 192.168.3.1, local AS number 45000
BGP table version is 1, main routing table version 1
Neighbor V AS MsgRcvd MsgSent TblVer InQ OutQ Up/Down State/PfxRcd
*2001::1 4 50000 2 2 0 0 0 00:00:37 0
* Dynamically created based on a listen range command

IP Routing: BGP Configuration Guide
412


BGP Dynamic Neighbors
Configuration Examples for BGP Dynamic Neighbors

Dynamically created neighbors: 1/(200 max), Subnet ranges: 1
BGP peergroup group192 listen range group members:
2001::0/64

Use the show bgp { ipv4 | ipv6 } unicast peer-group< name> command to verify the IPv6 dynamic neighbors
configuration in global routing table:
Device# show bgp ipv6 unicast peer-group group192
BGP peer-group is group192, remote AS 40000
BGP peergroup group192 listen range group members:
2001::0/64
BGP version 4
Default minimum time between advertisement runs is 30 seconds
For address family: IPv6 Unicast
BGP neighbor is group192, peer-group external, members:
*2001::1
Index 0, Offset 0, Mask 0x0
Update messages formatted 0, replicated 0
Number of NLRIs in the update sent: max 0, min 0

You can use the following commands to verify the BGP IPv6 dynamic neighbors configuration in the VRF
routing table:
• show bgp vpnv6 unicast vrf <name> neighbors
• show bgp vpnv6 unicast vrf <name> summary
• show bgp vpnv6 unicast vrf <name> peer-group <name>
• debug bgp [ipv6 | vpnv6 ] unicast range

Configuration Examples for BGP Dynamic Neighbors
Example: Implementing BGP Dynamic Neighbors Using Subnet Ranges
In the following example, two BGP peer groups are created on Router B in the figure below, a global limit is
set on the number of dynamic BGP neighbors, and a subnet range is associated with a peer group. Configuring
the subnet range enables the dynamic BGP neighbor process. The peer groups are added to the BGP neighbor
table of the local router, and an alternate autonomous system number is also configured for one of the peer
groups, group192. The subnet range peer groups and a standard BGP peer are then activated under the IPv4
address family.
The configuration moves to another router—Router A in the figure below—where a BGP session is started
and the neighbor router, Router B, is configured as a remote BGP peer. The peering configuration opens a
TCP session and triggers Router B to create a dynamic BGP neighbor because the IP address that starts the
TCP session (192.168.1.2) is within the configured subnet range for dynamic BGP peers.
A third router—Router E in the figure below—also starts a BGP peering session with Router B. Router E is
in the autonomous system 50000, which is the configured alternate autonomous system. Router B responds
to the resulting TCP session by creating another dynamic BGP peer.
This example concludes with the output of the show ip bgp summary command entered on Router B.

IP Routing: BGP Configuration Guide
413


BGP Dynamic Neighbors
Example: Implementing BGP Dynamic Neighbors Using Subnet Ranges

Figure 37: BGP Dynamic Neighbor Topology

Router B
enable
configure terminal
router bgp 45000
bgp log-neighbor-changes
bgp listen limit 200
bgp listen range 172.21.0.0/16 peer-group group172
bgp listen range 192.168.0.0/16 peer-group group192
neighbor group172 peer-group
neighbor group172 remote-as 45000
neighbor group192 peer-group
neighbor group192 remote-as 40000 alternate-as 50000
neighbor 172.16.1.2 remote-as 45000
address-family ipv4 unicast
neighbor group172 activate
neighbor group192 activate
neighbor 172.16.1.2 activate
end

Router A
enable
configure terminal
router bgp 40000
neighbor 192.168.1.1 remote-as 45000
exit

Router E
enable
configure terminal
router bgp 50000

IP Routing: BGP Configuration Guide
414


BGP Dynamic Neighbors
Example: Configuring BGP IPv6 Dynamic Neighbor Support with VRF Support

neighbor 192.168.3.1 remote-as 45000
exit

After both Router A and Router E are configured, the show ip bgp summary command is run on Router B.
The output displays the regular BGP neighbor, 172.16.1.2, and the two BGP neighbors that were created
dynamically when Router A and Router E initiated TCP sessions for BGP peering to Router B. The output
also shows information about the configured listen range subnet groups.
BGP router identifier 192.168.3.1, local AS number 45000
BGP table version is 1, main routing table version 1
Neighbor
V
AS MsgRcvd MsgSent
TblVer InQ OutQ Up/Down State/PfxRcd
172.16.1.2
4 45000
15
15
1
0
0 00:12:20
0
*192.168.1.2
4 40000
3
3
1
0
0 00:00:37
0
*192.168.3.2
4 50000
6
6
1
0
0 00:04:36
0
* Dynamically created based on a listen range command
Dynamically created neighbors: 2/(200 max), Subnet ranges: 2
BGP peergroup group172 listen range group members:
172.21.0.0/16
BGP peergroup group192 listen range group members:
192.168.0.0/16

Example: Configuring BGP IPv6 Dynamic Neighbor Support with VRF Support
Configuring BGP IPv6 Dynamic Neighbor Support with VRF Support
enable
configure terminal
router bgp 55000
bgp listen range 2001::0/64 peer-group group182
address-family ipv6 unicast vrf vrf2
bgp listen limit 600
neighbor group182 peer-group
neighbor group182 remote-as 103 alternate-as 104
address-family ipv4 unicast vrf vrf2
neighbor group182 activate
end

Configuring BGP IPv6 Dynamic Neighbor Support without VRF Support
enable
configure terminal
router bgp 100
bgp listen range 2001::0/64 peer-group group192
bgp listen limit 500
neighbor group192 peer-group
neighbor group192 remote-as 101 alternate-as 102
address family ipv6 unicast
neighbor group192 activate
address family ipv4 unicast
neighbor group192 activate
end

IP Routing: BGP Configuration Guide
415


BGP Dynamic Neighbors
Additional References

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

Feature Information for BGP Dynamic Neighbors
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.

IP Routing: BGP Configuration Guide
416


BGP Dynamic Neighbors
Feature Information for BGP Dynamic Neighbors

Table 34: Feature Information for BGP Dynamic Neighbors

Feature Name

Releases

Feature Information

BGP Dynamic Neighbors

Cisco IOS XE Release 3.1S

BGP dynamic neighbor support
allows BGP peering to a group of
remote neighbors that are defined
by a range of IP addresses. Each
range can be configured as a subnet
IP address. BGP dynamic neighbors
are configured using a range of IP
addresses and BGP peer groups.
After a subnet range is configured
for a BGP peer group and a TCP
session is initiated for an IP address
in the subnet range, a new BGP
neighbor is dynamically created as
a member of that group. The new
BGP neighbor will inherit any
configuration for the peer group.
The following commands were
introduced or modified by this
feature: bgp listen, debug ip bgp
range, neighbor remote-as, show
ip bgp neighbors, show ip bgp
peer-group, and show ip bgp
summary.

BGP IPv6 Dynamic Neighbor
Support and VRF Support

Cisco IOS XE Denali 16.3.1

In Cisco IOS XE Denali 16.3
release, support for BGP dynamic
neighbors was extended to IPv6
BGP peering with support for VRF.
The following commands were
introduced or modified by this
feature: bgp listen, debug ip bgp
range, neighbor remote-as, show
bgp neighbors, show bgp
summary, show bgp vpnv6
unicast vrf neighbors, show bgp
vpnv6 unicast vrf peer-group ,
show bgp vpnv6 unicast vrf
summary.

IP Routing: BGP Configuration Guide
417


BGP Dynamic Neighbors
Feature Information for BGP Dynamic Neighbors

IP Routing: BGP Configuration Guide
418
