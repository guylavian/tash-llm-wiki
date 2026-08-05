---
title: "BGP Support for MTR"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-mtr
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 81 BGP Support for MTR The BGP Support for MTR feature provides Border Gateway Protocol (BGP) support for multiple logical topologies over a single physical network. This module describes how to configure BGP for Multitopology Routing (MTR). • Finding Feature Information, on page 1113 • Prerequisites for BGP Support for MTR, on page 1113 • Restrictions for BGP Support for MTR, on page 11"
---

# BGP Support for MTR

CHAPTER

81

BGP Support for MTR
The BGP Support for MTR feature provides Border Gateway Protocol (BGP) support for multiple logical
topologies over a single physical network. This module describes how to configure BGP for Multitopology
Routing (MTR).
• Finding Feature Information, on page 1113
• Prerequisites for BGP Support for MTR, on page 1113
• Restrictions for BGP Support for MTR, on page 1114
• Information About BGP Support for MTR, on page 1114
• How to Configure BGP Support for MTR, on page 1116
• Configuration Examples for BGP Support for MTR, on page 1122
• Additional References, on page 1125
• Feature Information for BGP Support for MTR, on page 1125

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP Support for MTR
• Be familiar with all the concepts in the “Information About BGP Support for MTR” section.
• Configure and activate a global Multitopology Routing (MTR) topology configuration.

IP Routing: BGP Configuration Guide
1113


BGP Support for MTR
Restrictions for BGP Support for MTR

Restrictions for BGP Support for MTR
• Redistribution within a topology is permitted. Redistribution from one topology to another is not permitted.
This restriction is designed to prevent routing loops. You can use topology translation or topology import
functionality to move routes from one topology to another.
• Only a single multicast topology can be configured, and only the base topology can be specified if a
multicast topology is created.

Information About BGP Support for MTR
Routing Protocol Support for MTR
You must enable IP routing on the device for Multitopology Routing (MTR) to operate. MTR supports static
and dynamic routing in Cisco software. You can enable dynamic routing per topology to support interdomain
and intradomain routing. Route calculation and forwarding are independent for each topology. MTR support
is integrated into Cisco software for the following protocols:
• Border Gateway Protocol (BGP)
• Integrated Intermediate System-to-Intermediate System (IS-IS)
You apply the per-topology configuration in router address family configuration mode of the global routing
process (router configuration mode). The address family and subaddress family are specified when the device
enters address family configuration mode. You specify the topology name and topology ID by entering the
topology command in address family configuration mode.
You configure each topology with a unique topology ID under the routing protocol. The topology ID is used
to identify and group Network Layer Reachability Information (NLRI) for each topology in updates for a
given protocol. In OSPF, EIGRP, and IS-IS, you enter the topology ID during the first configuration of the
topology command for a class-specific topology. In BGP, you configure the topology ID by entering the bgp
tid command under the topology configuration.
You can configure class-specific topologies with different metrics than the base topology. Interface metrics
configured on the base topology can be inherited by the class-specific topology. Inheritance occurs if no
explicit inheritance metric is configured in the class-specific topology.
You configure BGP support only in router configuration mode. You configure Interior Gateway Protocol
(IGP) support in router configuration mode and in interface configuration mode.
By default, interfaces are not included in nonbase topologies. For routing protocol support for EIGRP, IS-IS,
and OSPF, you must explicitly configure a nonbase topology on an interface. You can override the default
behavior by using the all-interfaces command in address family topology configuration mode. The
all-interfaces command causes the nonbase topology to be configured on all interfaces of the device that are
part of the default address space or the virtual routing and forwarding (VRF) instance in which the topology
is configured.

IP Routing: BGP Configuration Guide
1114


BGP Support for MTR
BGP Network Scope

BGP Network Scope
To implement Border Gateway Protocol (BGP) support for Multitopology Routing (MTR), the scope hierarchy
is required, but the scope hierarchy is not limited to MTR use. The scope hierarchy introduces new configuration
modes such as router scope configuration mode. The device enters router scope configuration mode when
you configure the scope command in router configuration mode. When this command is entered, a collection
of routing tables is created.
You configure BGP commands under the scope hierarchy for a single network (globally), or on a per-virtual
routing and forwarding (VRF) basis; these configurations are referred to as scoped commands. The scope
hierarchy can contain one or more address families.

MTR CLI Hierarchy Under BGP
The Border Gateway Protocol (BGP) CLI provides backward compatibility for pre-Multitopology Routing
(MTR) BGP configuration and provides a hierarchical implementation of MTR. Router configuration mode
is backward compatible with the pre-address family and pre-MTR configuration CLI. Global commands that
affect all networks are configured in this configuration mode. For address family and topology configuration,
you configure general session commands and peer templates to be used in address family configuration mode
or in topology configuration mode.
After configuring any global commands, you define the scope either globally or for a specific virtual routing
and forwarding (VRF) instance. The device enters address family configuration mode when you configure
the address-family command in router scope configuration mode or in router configuration mode. Unicast
is the default address family if no subaddress family identifier (SAFI) is specified. MTR supports only the
IPv4 address family with a SAFI of unicast or multicast.
When the device enters address family configuration mode from router configuration mode, the software
configures BGP to use pre-MTR-based CLI. This configuration mode is backward compatible with pre-existing
address family configurations. Entering address family configuration mode from router scope configuration
mode configures the device to use the hierarchical CLI that supports MTR. Address family configuration
parameters that are not specific to a topology are entered in this address family configuration mode.
The device enters BGP topology configuration mode when you configure the topology command in address
family configuration mode. You can configure up to 32 topologies (including the base topology) on a device.
You configure the topology ID by entering the bgp tid command. All address family and subaddress family
configuration parameters for the topology are configured here.

Note

Configuring a scope for a BGP routing process removes CLI support for pre-MTR-based configuration.
The following example shows the hierarchy levels that are used when you configure BGP for MTR
implementation:
router bgp <autonomous-system-number>
! Global commands
scope {global | vrf <vrf-name>}
! Scoped commands
address-family {<afi>} [<safi>]
! Address family specific commands

IP Routing: BGP Configuration Guide
1115


BGP Support for MTR
BGP Sessions for Class-Specific Topologies

topology {<topology-name> | base}
! topology specific commands

BGP Sessions for Class-Specific Topologies
Multitopology Routing (MTR) is configured under the Border Gateway Protocol (BGP) on a per-session
basis. The base unicast and multicast topologies are carried in the global (default) session. A separate session
is created for each class-specific topology that is configured under a BGP routing process. Each session is
identified by its topology ID. BGP performs a best-path calculation individually for each class-specific
topology. A separate Routing Information Base (RIB) and Forwarding Information Base (FIB) are maintained
for each session.

Topology Translation Using BGP
Depending on the design and policy requirements for your network, you might need to install routes from a
class-specific topology on one device in a class-specific topology on a neighboring device. Topology translation
functionality using the Border Gateway Protocol (BGP) provides support for this operation. Topology translation
is BGP neighbor-session based. You configure the neighbor translate-topology command by using the IP
address and topology ID from the neighbor.
The topology ID identifies the class-specific topology of the neighbor. The routes in the class-specific topology
of the neighbor are installed in the local class-specific Routing Information Base (RIB). BGP performs a
best-path calculation on all installed routes and installs these routes into the local class-specific RIB. If a
duplicate route is translated, BGP selects and installs only one instance of the route per standard BGP best-path
calculation behavior.

Topology Import Using BGP
Importing topologies using the Border Gateway Protocol (BGP) is similar to topology translation. The difference
is that routes are moved between class-specific topologies on the same device. You configure this function
by entering the import topology command and specify the name of the class-specific topology or base
topology. Best-path calculations are run on the imported routes before they are installed into the topology
Routing Information Base (RIB). This import topology command also includes a route-map keyword to
allow you to filter routes that are moved between class-specific topologies.

How to Configure BGP Support for MTR
Activating an MTR Topology by Using BGP
Perform this task to activate a Multitopology Routing (MTR) topology inside an address family by using the
Border Gateway Protocol (BGP). This task is configured on Device B in the figure below and must also be
configured on Device D and Device E. In this task, a scope hierarchy is configured to apply globally, and a
neighbor is configured in router scope configuration mode. Under the IPv4 unicast address family, an MTR
topology that applies to video traffic is activated for the specified neighbor. There is no interface configuration
mode for BGP topologies.

IP Routing: BGP Configuration Guide
1116


BGP Support for MTR
Activating an MTR Topology by Using BGP

Figure 93: BGP Network Diagram

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

enable
configure terminal
router bgp autonomous-system-number
scope {global | vrf vrf-name}
neighbor {ip-address | peer-group-name} remote-as autonomous-system-number
neighbor {ip-address | peer-group-name} transport {connection-mode {active | passive} |
path-mtu-discovery | multi-session | single-session}
address-family ipv4 [mdt | multicast | unicast]
topology {base | topology-name}
bgp tid number
neighbor ip-address activate
neighbor {ip-address | peer-group-name} translate-topology number
end
clear ip bgp topology {* | topology-name} {as-number | dampening [network-address [network-mask]]
| flap-statistics [network-address [network-mask]] | peer-group peer-group-name | table-map |
update-group [number | ip-address]} [in [prefix-filter] | out | soft [in [prefix-filter] | out]]
show ip bgp topology {* | topology} summary

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

IP Routing: BGP Configuration Guide
1117


BGP Support for MTR
Activating an MTR Topology by Using BGP

Command or Action

Purpose

Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Enters router configuration mode to create or configure a
BGP routing process.

Device(config)# router bgp 45000

Step 4

scope {global | vrf vrf-name}
Example:
Device(config-router)# scope global

Defines the scope for the BGP routing process and enters
router scope configuration mode.
• BGP general session commands that apply to a single
network, or a specified virtual and routing forwarding
(VRF) instance, are entered in this configuration
mode.
• Use the global keyword to specify that BGP uses the
global routing table.
• Use the vrf vrf-name keyword and argument to
specify that BGP uses a specific VRF routing table.
The VRF must already exist.

Step 5

neighbor {ip-address | peer-group-name} remote-as
autonomous-system-number
Example:

Adds the IP address of the neighbor in the specified
autonomous system to the multiprotocol BGP neighbor
table of the local device.

Device(config-router-scope)# neighbor 172.16.1.2
remote-as 45000

Step 6

neighbor {ip-address | peer-group-name} transport
{connection-mode {active | passive} |
path-mtu-discovery | multi-session | single-session}
Example:
Device(config-router-scope)# neighbor 172.16.1.2
transport multi-session

Enables a TCP transport session option for a BGP session.
• Use the connection-mode keyword to specify the
type of connection, either active or passive.
• Use the path-mtu-discovery keyword to enable the
TCP transport path maximum transmission unit
(MTU) discovery.
• Use the multi-session keyword to specify a separate
TCP transport session for each address family.
• Use the single-session keyword to specify that all
address families use a single TCP transport session.

Step 7

address-family ipv4 [mdt | multicast | unicast]
Example:

IP Routing: BGP Configuration Guide
1118

Specifies the IPv4 address family and enters router scope
address family configuration mode.


BGP Support for MTR
Activating an MTR Topology by Using BGP

Command or Action
Device(config-router-scope)# address-family ipv4

Purpose
• Use the mdt keyword to specify IPv4 multicast
distribution tree (MDT) address prefixes.
• Use the multicast keyword to specify IPv4 multicast
address prefixes.
• Use the unicast keyword to specify the IPv4 unicast
address family. By default, the device is placed in
address family configuration mode for the IPv4
unicast address family if the unicast keyword is not
specified with the address-family ipv4 command.
• Nontopology-specific configuration parameters are
configured in this configuration mode.

Step 8

topology {base | topology-name}
Example:

Configures the topology instance in which BGP routes
class-specific or base topology traffic, and enters router
scope address family topology configuration mode.

Device(config-router-scope-af)# topology VIDEO

Step 9

bgp tid number
Example:
Device(config-router-scope-af-topo)# bgp tid 100

Step 10

neighbor ip-address activate
Example:

Step 11

• Each topology must be configured with a unique
topology ID.
Enables the BGP neighbor to exchange prefixes for the
network service access point (NSAP) address family with
the local device.
If you have configured a peer group as a BGP
neighbor, do not use this command because
peer groups are automatically activated when
any peer group parameter is configured.

Device(config-router-scope-af-topo)# neighbor
172.16.1.2 activate

Note

neighbor {ip-address | peer-group-name}
translate-topology number

(Optional) Configures BGP to install routes from a
topology on another device to a topology on the local
device.

Example:
Device(config-router-scope-af-topo)# neighbor
172.16.1.2 translate-topology 200

Step 12

Associates a BGP routing process with the specified
topology ID.

end
Example:

• The topology ID is entered for the number argument
to identify the topology on the device.
(Optional) Exits router scope address family topology
configuration mode and returns to privileged EXEC mode.

Device(config-router-scope-af-topo)# end

Step 13

clear ip bgp topology {* | topology-name} {as-number Resets BGP neighbor sessions under a specified topology
or all topologies.
| dampening [network-address [network-mask]] |
flap-statistics [network-address [network-mask]] |

IP Routing: BGP Configuration Guide
1119


BGP Support for MTR
What to Do Next

Command or Action

Purpose

peer-group peer-group-name | table-map | update-group
[number | ip-address]} [in [prefix-filter] | out | soft [in
[prefix-filter] | out]]
Example:
Device# clear ip bgp topology VIDEO 45000

Step 14

show ip bgp topology {* | topology} summary
Example:

(Optional) Displays BGP information about a topology.
• Most standard BGP keywords and arguments can be
entered following the topology keyword.

Device# show ip bgp topology VIDEO summary

Note

Only the syntax required for this task is shown.
For more details, see the Cisco IOS IP Routing:
BGP Command Reference.

What to Do Next
Repeat this task for every topology that you want to enable, and repeat this configuration on all neighbor
devices that are to use the topologies.
If you want to import routes from one Multitopology Routing (MTR) topology to another on the same device,
see the “Importing Routes from an MTR Topology by Using BGP” section.

Importing Routes from an MTR Topology by Using BGP
Perform this task to import routes from one Multitopology Routing (MTR) topology to another on the same
device, when multiple topologies are configured on the same device. In this task, a prefix list is defined to
permit prefixes from the 10.2.2.0 network, and this prefix list is used with a route map to filter routes moved
from the imported topology. A global scope is configured, address family IPv4 is entered, the VIDEO topology
is specified, the VOICE topology is imported, and the routes are filtered using the route map named 10NET.
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

enable
configure terminal
ip prefix-list list-name [seq number] {deny | permit} network/length [ge ge-length] [le le-length]
route-map map-name [permit | deny] [sequence-number]
match ip address {access-list-number [access-list-number ... | access-list-name...] | access-list-name
[access-list-number ... | access-list-name] | prefix-list prefix-list-name [prefix-list-name...]}
exit
router bgp autonomous-system-number
scope {global | vrf vrf-name}
address-family ipv4 [mdt | multicast | unicast]
topology {base | topology-name}
import topology {base | topology-name} [route-map map-name]
end

IP Routing: BGP Configuration Guide
1120


BGP Support for MTR
Importing Routes from an MTR Topology by Using BGP

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

ip prefix-list list-name [seq number] {deny | permit}
network/length [ge ge-length] [le le-length]
Example:

Configures an IP prefix list.
• In this example, prefix list TEN permits advertising
of the 10.2.2.0/24 prefix depending on a match set
by the match ip address command.

Device(config)# ip prefix-list TEN permit
10.2.2.0/24

Step 4

route-map map-name [permit | deny] [sequence-number] Creates a route map and enters route-map configuration
mode.
Example:
• In this example, the route map named 10NET is
Device(config)# route-map 10NET
created.

Step 5

match ip address {access-list-number [access-list-number Configures the route map to match a prefix that is permitted
by a standard access list, an extended access list, or a prefix
... | access-list-name...] | access-list-name
list.
[access-list-number ... | access-list-name] | prefix-list
prefix-list-name [prefix-list-name...]}
• In this example, the route map is configured to match
prefixes permitted by prefix list TEN.
Example:
Device(config-route-map)# match ip address
prefix-list TEN

Step 6

exit
Example:

Exits route-map configuration mode and returns to global
configuration mode.

Device(config-route-map)# exit

Step 7

router bgp autonomous-system-number
Example:

Enters router configuration mode to create or configure a
Border Gateway Protocol (BGP) routing process.

Device(config)# router bgp 50000

Step 8

scope {global | vrf vrf-name}
Example:
Device(config-router)# scope global

Defines the scope to the BGP routing process and enters
router scope configuration mode.
• BGP general session commands that apply to a single
network, or a specified virtual routing and forwarding

IP Routing: BGP Configuration Guide
1121


BGP Support for MTR
Configuration Examples for BGP Support for MTR

Command or Action

Purpose
(VRF) instance, are entered in this configuration
mode.
• Use the global keyword to specify that BGP uses the
global routing table.
• Use the vrf vrf-name keyword and argument to
specify that BGP uses a specific VRF routing table.
The VRF must already exist.

Step 9

address-family ipv4 [mdt | multicast | unicast]
Example:
Device(config-router-scope)# address-family ipv4

Step 10

topology {base | topology-name}
Example:

Enters router scope address family configuration mode to
configure an address family session under BGP.
• Nontopology-specific configuration parameters are
configured in this configuration mode.
Configures the topology instance in which BGP routes
class-specific or base topology traffic, and enters router
scope address family topology configuration mode.

Device(config-router-scope-af)# topology VIDEO

Step 11

import topology {base | topology-name} [route-map
map-name]
Example:

(Optional) Configures BGP to move routes from one
topology to another on the same device.
• The route-map keyword can be used to filter routes
that moved between topologies.

Device(config-router-scope-af-topo)# import
topology VOICE route-map 10NET

Step 12

end
Example:

(Optional) Exits router scope address family topology
configuration mode and returns to privileged EXEC mode.

Device(config-router-scope-af-topo)# end

Configuration Examples for BGP Support for MTR
Example: BGP Topology Translation Configuration
The following example shows how to configure the Border Gateway Protocol (BGP) in the VIDEO topology
and how to configure topology translation with the 192.168.2.2 neighbor:
router bgp 45000
scope global
neighbor 172.16.1.1 remote-as 50000
neighbor 192.168.2.2 remote-as 55000
neighbor 172.16.1.1 transport multi-session
neighbor 192.168.2.2 transport multi-session
address-family ipv4
topology VIDEO

IP Routing: BGP Configuration Guide
1122


BGP Support for MTR
Example: BGP Global Scope and VRF Configuration

bgp tid 100
neighbor 172.16.1.1 activate
neighbor 192.168.2.2 activate
neighbor 192.168.2.2 translate-topology 200
end
clear ip bgp topology VIDEO 50000

Example: BGP Global Scope and VRF Configuration
The following example shows how to configure a global scope for a unicast topology and also for a multicast
topology. After the device exits the router scope configuration mode, a scope is configured for the virtual
routing and forwarding (VRF) instance named DATA.
router bgp 45000
scope global
bgp default ipv4-unicast
neighbor 172.16.1.2 remote-as 45000
neighbor 192.168.3.2 remote-as 50000
address-family ipv4 unicast
topology VOICE
bgp tid 100
neighbor 172.16.1.2 activate
exit
address-family ipv4 multicast
topology base
neighbor 192.168.3.2 activate
exit
exit
exit
scope vrf DATA
neighbor 192.168.1.2 remote-as 40000
address-family ipv4
neighbor 192.168.1.2 activate
end

Examples: BGP Topology Verification
The following example shows summary output for the show ip bgp topology command. Information is
displayed about Border Gateway Protocol (BGP) neighbors configured to use the Multitopology Routing
(MTR) topology named VIDEO.
Device# show ip bgp topology VIDEO summary
BGP router identifier 192.168.3.1, local AS number 45000
BGP table version is 1, main routing table version 1
Neighbor
V
AS MsgRcvd MsgSent
TblVer InQ OutQ Up/Down State/PfxRcd
172.16.1.2
4 45000
289
289
1
0
0 04:48:44
0
192.168.3.2
4 50000
3
3
1
0
0 00:00:27
0

The following partial output displays BGP neighbor information under the VIDEO topology:
Device# show ip bgp topology VIDEO neighbors 172.16.1.2
BGP neighbor is 172.16.1.2, remote AS 45000, internal link
BGP version 4, remote router ID 192.168.2.1
BGP state = Established, up for 04:56:30
Last read 00:00:23, last write 00:00:21, hold time is 180, keepalive interval is 60
seconds

IP Routing: BGP Configuration Guide
1123


BGP Support for MTR
Example: Importing Routes from an MTR Topology by Using BGP

Neighbor sessions:
1 active, is multisession capable
Neighbor capabilities:
Route refresh: advertised and received(new)
Message statistics, state Established:
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
296
296
Route Refresh:
0
0
Total:
297
297
Default minimum time between advertisement runs is 0 seconds
For address family: IPv4 Unicast topology VIDEO
Session: 172.16.1.2 session 1
BGP table version 1, neighbor version 1/0
Output queue size : 0
Index 1, Offset 0, Mask 0x2
1 update-group member
Topology identifier: 100
.
.
.
Address tracking is enabled, the RIB does have a route to 172.16.1.2
Address tracking requires at least a /24 route to the peer
Connections established 1; dropped 0
Last reset never
Transport(tcp) path-mtu-discovery is enabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0
Minimum incoming TTL 0, Outgoing TTL 255
Local host: 172.16.1.1, Local port: 11113
Foreign host: 172.16.1.2, Foreign port: 179
.
.
.

Example: Importing Routes from an MTR Topology by Using BGP
The following example shows how to configure an access list to be used by a route map named VOICE to
filter routes imported from the Multitopology Routing (MTR) topology named VOICE. Only routes with the
prefix 192.168.1.0 are imported.
access-list 1 permit 192.168.1.0 0.0.0.255
route-map BLUE
match ip address 1
exit
router bgp 50000
scope global
neighbor 10.1.1.2 remote-as 50000
neighbor 172.16.1.1 remote-as 60000
address-family ipv4
topology VIDEO
bgp tid 100
neighbor 10.1.1.2 activate
neighbor 172.16.1.1 activate
import topology VOICE route-map VOICE
end
clear ip bgp topology VIDEO 50000

IP Routing: BGP Configuration Guide
1124


BGP Support for MTR
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

Multitopology Routing (MTR) commands

Cisco IOS Multitopology Routing
Command Reference

Border Gateway Protocol (BGP) commands

Cisco IOS IP Routing: BGP
Command Reference

BGP concepts and tasks

IP Routing: BGP Configuration
Guide

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

Feature Information for BGP Support for MTR
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
1125


BGP Support for MTR
Feature Information for BGP Support for MTR

Table 101: Feature Information for BGP Support for MTR

Feature Name

Releases

Feature Information

BGP Support for MTR

12.2(33)SRB

This feature provides Border
Gateway Protocol (BGP) support
for multiple logical topologies over
a single physical network.

15.0(1)S
Cisco IOS XE Release 2.5

In Cisco IOS XE Release 2.5,
support was added for the Cisco
ASR 1000 Series Routers.
The following commands were
introduced or modified:
address-family ipv4, bgp tid,
clear ip bgp topology, import
topology, neighbor
translate-topology, neighbor
transport, scope, show ip bgp
topology, topology.

IP Routing: BGP Configuration Guide
1126
