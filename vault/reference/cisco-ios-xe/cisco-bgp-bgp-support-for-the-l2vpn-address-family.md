---
title: "BGP Support for the L2VPN Address Family"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-the-l2vpn-address-family
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 43 BGP Support for the L2VPN Address Family BGP support for the Layer 2 Virtual Private Network (L2VPN) address family introduces a BGP-based autodiscovery mechanism to distribute L2VPN endpoint provisioning information. BGP uses a separate L2VPN Routing Information Base (RIB) to store endpoint provisioning information, which is updated each time any Layer 2 virtual forwarding instance ("
---

# BGP Support for the L2VPN Address Family

CHAPTER

43

BGP Support for the L2VPN Address Family
BGP support for the Layer 2 Virtual Private Network (L2VPN) address family introduces a BGP-based
autodiscovery mechanism to distribute L2VPN endpoint provisioning information. BGP uses a separate
L2VPN Routing Information Base (RIB) to store endpoint provisioning information, which is updated each
time any Layer 2 virtual forwarding instance (VFI) is configured. When BGP distributes the endpoint
provisioning information in an update message to all its BGP neighbors, the endpoint information is used to
set up a pseudowire mesh to support L2VPN-based services.
• Finding Feature Information, on page 695
• Prerequisites for BGP Support for the L2VPN Address Family, on page 695
• Restrictions for BGP Support for the L2VPN Address Family, on page 696
• Information About BGP Support for the L2VPN Address Family, on page 696
• How to Configure BGP Support for the L2VPN Address Family, on page 697
• Configuration Examples for BGP Support for the L2VPN Address Family, on page 703
• Where to Go Next, on page 706
• Additional References, on page 706
• Feature Information for BGP Support for the L2VPN Address Family, on page 707

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP Support for the L2VPN Address Family
The BGP Support for L2VPN Address Family feature assumes prior knowledge of Virtual Private Network
(VPN), Virtual Private LAN Service (VPLS), and Multiprotocol Layer Switching (MPLS) technologies.

IP Routing: BGP Configuration Guide
695


BGP Support for the L2VPN Address Family
Restrictions for BGP Support for the L2VPN Address Family

Restrictions for BGP Support for the L2VPN Address Family
• For route maps used within BGP, all commands related to prefix processing, tag processing, and automated
tag processing are ignored when used under L2VPN address family configuration. All other route map
commands are supported.
• BGP multipaths and confederations are not supported under the L2VPN address family.

Information About BGP Support for the L2VPN Address Family
L2VPN Address Family
In Cisco IOS XE Release 2.6 and later releases, support for the L2VPN address family is introduced. L2VPN
is defined as a secure network that operates inside an unsecured network by using an encryption technology
such as IP security (IPsec) or Generic Routing Encapsulation (GRE). The L2VPN address family is configured
under BGP routing configuration mode, and within the L2VPN address family the VPLS subsequent address
family identifier (SAFI) is supported.
BGP support for the L2VPN address family introduces a BGP-based autodiscovery mechanism to distribute
L2VPN endpoint provisioning information. BGP uses a separate L2VPN Routing Information Base (RIB) to
store endpoint provisioning information, which is updated each time any Layer 2 VFI is configured. Prefix
and path information is stored in the L2VPN database, allowing BGP to make best-path decisions. When BGP
distributes the endpoint provisioning information in an update message to all its BGP neighbors, the endpoint
information is used to set up a pseudowire mesh to support L2VPN-based services.
The BGP autodiscovery mechanism facilitates the setting up of L2VPN services, which are an integral part
of the Cisco IOS Virtual Private LAN Service (VPLS) feature. VPLS enables flexibility in deploying services
by connecting geographically dispersed sites as a large LAN over high-speed Ethernet in a robust and scalable
IP MPLS network. For more details about VPLS, see the VPLS Autodiscovery: BGP Based feature.
In L2VPN address family, the following BGP commands are supported:
• bgp nexthop
• bgp scan-time
• neighbor activate
• neighbor advertisement-interval
• neighbor allowas-in
• neighbor capability
• neighbor inherit
• neighbor maximum-prefix
• neighbor next-hop-self
• neighbor next-hop-unchanged
• neighbor peer-group

IP Routing: BGP Configuration Guide
696


BGP Support for the L2VPN Address Family
VPLS ID

• neighbor remove-private-as
• neighbor route-map
• neighbor route-reflector-client
• neighbor send-community
• neighbor soft-reconfiguration
• neighbor soo
• neighbor weight

Note

For route reflectors using L2VPNs, the neighbor next-hop-self and neighbor next-hop-unchangedcommands
are not supported.
For route maps used within BGP, all commands related to prefix processing, tag processing, and automated
tag processing are ignored when used under L2VPN address family configuration. All other route map
commands are supported.
BGP multipaths and confederations are not supported under the L2VPN address family.

VPLS ID
A VPLS ID is a BGP extended community value that identifies the VPLS domain. Manual configuration of
this ID is optional because a default VPLS ID is generated using the BGP autonomous system number and
the configured VPN ID. A VPLS ID can be composed in one of two ways: with an autonomous system number
and an arbitrary number or with an IP address and an arbitrary number.
You can enter a VPLS ID in either of these formats:
• Enter a 16-bit autonomous system number, a colon, and a 32-bit number. For example:
45000:3
• Enter a 32-bit IP address, a colon, and a 16-bit number. For example:
192.168.10.15:1

How to Configure BGP Support for the L2VPN Address Family
Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family
Perform this task to implement VPLS autodiscovery of each provider edge (PE) router that is a member of a
specific VPLS. In Cisco IOS XE Release 2.6, the BGP L2VPN address family was introduced with a separate
L2VPN RIB that contains endpoint provisioning information. BGP learns the endpoint provisioning information
from the L2VPN database, which is updated each time any Layer 2 (L2) virtual forwarding instance (VFI) is
configured. When BGP distributes the endpoint provisioning information in an update message to all its BGP
neighbors, the endpoint information is used to set up a pseudowire mesh to support L2VPN-based services.

IP Routing: BGP Configuration Guide
697


BGP Support for the L2VPN Address Family
Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family

BGP-based VPLS autodiscovery eliminates the need to manually provision a VPLS neighbor. After a PE
router configures itself to be a member of a particular VPLS, information needed to set up connections to
remote routers in the same VPLS is distributed by a discovery process. When the discovery process is complete,
each member of the VPLS will have the information needed to set up VPLS pseudowires to form the full
mesh of pseudowires needed for the VPLS.
This task is configured at router N-PE3 in the figure below and must be repeated at routers N-PE1 and N-PE2
with the appropriate changes such as different IP addresses. For a full configuration of these routers, see the
figure below.
Figure 63: Network Diagram for BGP Autodiscovery Using the L2VPN Address Family

In this task, the PE router N-PE3 in the figure above is configured with a Layer 2 router ID, a VPN ID, a
VPLS ID, and is enabled to automatically discover other PE routers that are part of the same VPLS domain.
A BGP session is created to activate BGP neighbors under the L2VPN address family. Finally, two optional
show commands are entered to verify the steps in the task.
Before you begin
This task assumes that MPLS is configured with VPLS options. For more details, see the "VPLS Autodiscovery:
BGP Based" feature.
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
l2 router-id ip-address
l2 vfi vfi-name autodiscovery
vpn id vpn-id
vpls-id vpls-id
exit
Repeat Step 4 through Step 6 to configure other L2 VFIs and associated VPN and VPLS IDs.
router bgp autonomous-system-number
no bgp default ipv4-unicast
bgp log-neighbor-changes
bgp update-delay seconds

IP Routing: BGP Configuration Guide
698


BGP Support for the L2VPN Address Family
Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family

13.
14.
15.
16.
17.
18.
19.
20.
21.
22.

neighbor {ip-address| peer-group-name} remote-as autonomous-system-number
neighbor {ip-address| peer-group-name} update-source interface-type interface-number
Repeat Step 13 and Step 14 to configure other BGP neighbors.
address-family l2vpn [vpls]
neighbor ip-address activate
neighbor {ip-address| peer-group-name} send-community[both| standard| extended]
Repeat Step 17 and Step 18 to activate other BGP neighbors under L2VPN address family.
end
show vfi
show ip bgp l2vpn vpls {all | rd vpn-rd}

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

l2 router-id ip-address
Example:
Router(config)# l2 router-id 10.1.1.3

Step 4

l2 vfi vfi-name autodiscovery
Example:
Router(config)# l2 vfi customerA autodiscovery

Specifies a router ID (in IP address format) for the PE
router to use with VPLS autodiscovery pseudowires.
• In this example, the L2 router ID is defined as
10.1.1.3.
Creates an L2 VFI, enables the VPLS PE router to
automatically discover other PE routers that are part of the
same VPLS domain, and enters L2 VFI autodiscovery
configuration mode.
• In this example, the L2 VFI named customerA is
created.

Step 5

vpn id vpn-id
Example:
Router(config-vfi)# vpn id 100

Specifies a VPN ID.
• Use the same VPN ID for the PE routers that belong
to the same VPN. Make sure that the VPN ID is
unique for each VPN in the service provider network.
• Use the vpn-id argument to specify a number in the
range from 1 to 4294967295.
• In this example, a VPN ID of 100 is specified.

Step 6

vpls-id vpls-id

(Optional) Specifies a VPLS ID.

IP Routing: BGP Configuration Guide
699


BGP Support for the L2VPN Address Family
Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family

Command or Action

Purpose

Example:

• The VPLS ID is an identifier that is used to identify
the VPLS domain. This command is optional because
a default VPLS ID is automatically generated using
the BGP autonomous system number and the VPN
ID configured for the VFI. Only one VPLS ID can
be configured per VFI, and the same VPLS ID cannot
be configured in multiple VFIs on the same router.

Router(config-vfi)# vpls-id 65000:100

• In this example, a VPLS ID of 65000:100 is specified.
Step 7

exit
Example:

Exits L2 VFI autodiscovery configuration mode and returns
to global configuration mode.

Router(config-vfi)# exit

Step 8

Repeat Step 4 through Step 6 to configure other L2 VFIs -and associated VPN and VPLS IDs.

Step 9

router bgp autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.

Router(config)# router bgp 65000

Step 10

no bgp default ipv4-unicast
Example:

Disables the IPv4 unicast address family for the BGP
routing process.
Note

Router(config-router)# no bgp default ipv4-unicast

Step 11

bgp log-neighbor-changes

Routing information for the IPv4 unicast
address family is advertised by default for each
BGP routing session configured with the
neighbor remote-as router configuration
command unless you configure the no bgp
default ipv4-unicastrouter configuration
command before configuring the neighbor
remote-as command. Existing neighbor
configurations are not affected.

Enables logging of BGP neighbor resets.

Example:
Router(config-router)# bgp log-neighbor-changes

Step 12

bgp update-delay seconds
Example:

Sets the maximum initial delay period before a
BGP-speaking networking device sends its first updates.
• Use the seconds argument to set the delay period.

Router(config-router)# bgp update-delay 1

Step 13

neighbor {ip-address| peer-group-name} remote-as
autonomous-system-number
Example:

IP Routing: BGP Configuration Guide
700

Adds the IP address or peer group name of the neighbor
in the specified autonomous system to the IPv4
multiprotocol BGP neighbor table of the local router.


BGP Support for the L2VPN Address Family
Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family

Command or Action

Purpose
• If the autonomous-system-number argument matches
the autonomous system number specified in the
router bgp command, the neighbor is an internal
neighbor.

Router(config-router)# neighbor 10.10.10.1
remote-as 65000

• If the autonomous-system-number argument does not
match the autonomous system number specified in
the router bgp command, the neighbor is an external
neighbor.
• In this example, the neighbor at 10.10.10.1 is an
internal BGP neighbor.
Step 14

neighbor {ip-address| peer-group-name} update-source (Optional) Configures a router to select a specific source
or interface to receive routing table updates.
interface-type interface-number
Example:

• This example uses a loopback interface. The
advantage to this configuration is that the loopback
interface is not as susceptible to the effects of a
flapping interface.

Router(config-router)# neighbor 10.10.10.1
update-source loopback 1

Step 15

Repeat Step 13 and Step 14 to configure other BGP
neighbors.

--

Step 16

address-family l2vpn [vpls]

Specifies the L2VPN address family and enters address
family configuration mode.

Example:
Router(config-router)# address-family l2vpn vpls

• The optional vpls keyword specifies that VPLS
endpoint provisioning information is to be distributed
to BGP peers.
• In this example, an L2VPN VPLS address family
session is created.

Step 17

neighbor ip-address activate
Example:

Enables the neighbor to exchange information for the
L2VPN VPLS address family with the local router.
Note

Router(config-router-af)# neighbor 10.10.10.1
activate

Step 18

neighbor {ip-address| peer-group-name}
send-community[both| standard| extended]
Example:

If you have configured a BGP peer group as a
neighbor, you do not use this step. BGP peer
groups are activated when a BGP parameter is
configured. For example, the neighbor
send-community command in the next step
will automatically activate a peer group.

Specifies that a communities attribute should be sent to a
BGP neighbor.
• In this example, an extended communities attribute
is sent to the neighbor at 10.10.10.1.

Router(config-router-af)# neighbor 10.10.10.1
send-community extended

IP Routing: BGP Configuration Guide
701


BGP Support for the L2VPN Address Family
Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family

Command or Action

Purpose

Step 19

Repeat Step 17 and Step 18 to activate other BGP
neighbors under L2VPN address family.

--

Step 20

end

Exits address family configuration mode and returns to
privileged EXEC mode.

Example:
Router(config-router-af)# end

Step 21

show vfi
Example:

(Optional) Displays information about the configured VFI
instances.

Router# show vfi

Step 22

show ip bgp l2vpn vpls {all | rd vpn-rd}
Example:

(Optional) Displays information about the L2 VPN VPLS
address family.

Router# show ip bgp l2vpn vpls all

Examples
The following is sample output from the show vfi command that shows two VFIs, CustomerA and
CustomerB, with their associated VPN and VPLS IDs:
Router# show vfi
Legend: RT=Route-target, S=Split-horizon, Y=Yes, N=No
VFI name: customerA, state: down, type: multipoint
VPN ID: 100, VPLS-ID: 65000:100
RD: 65000:100, RT: 65000:100
Local attachment circuits:
Neighbors connected via pseudowires:
Peer Address
VC ID
Discovered Router ID
10.10.10.1
100
10.10.10.99
VFI name: customerB, state: down, type: multipoint
VPN ID: 200, VPLS-ID: 65000:200
RD: 65000:200, RT: 65000:200
Local attachment circuits:
Neighbors connected via pseudowires:
Peer Address
VC ID
Discovered Router ID
10.10.10.3
200
10.10.10.98

S
Y

S
Y

The following is sample output from the show ip bgp l2vpn vpls all command that shows two VFIs
identified by their VPN route distinguisher:
Router# show ip bgp l2vpn vpls all
BGP table version is 5, local router ID is 10.10.10.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete
Network
Next Hop
Metric LocPrf Weight Path
Route Distinguisher: 65000:100
*> 65000:100:10.10.10.1/96
0.0.0.0
32768 ?
*>i65000:100:192.168.1.1/96

IP Routing: BGP Configuration Guide
702


BGP Support for the L2VPN Address Family
What to Do Next

10.10.10.2
Route Distinguisher: 65000:200
*> 65000:200:10.10.10.3/96
0.0.0.0
*>i65000:200:192.168.2.2/96
10.10.10.2

0

100

0 ?

32768 ?
0

100

0 ?

What to Do Next
To configure more VPLS features, see the main VPLS documentation in the “VPLS Autodiscovery: BGP
Based” module in the MPLS Layer 2 VPNs Configuration Guide.

Configuration Examples for BGP Support for the L2VPN Address
Family
Example: Configuring VPLS Autodiscovery Using BGP and the L2VPN Address
Family
In this configuration example, all the routers in autonomous system 65000 in the figure below are configured
to provide BGP support for the L2VPN address family. VPLS autodiscovery is enabled and L2 VFI and VPN
IDs are configured. BGP neighbors are configured and activated under L2VPN address family to ensure that
the VPLS endpoint provisioning information is saved to a separate L2VPN RIB and then distributed to the
other BGP peers in BGP update messages. When the endpoint information is received by the BGP peers, a
pseudowire mesh is set up to support L2VPN-based services.
Figure 64: Network Diagram for VPLS Autodiscovery Using BGP and the L2VPN Address Family

Router N-PE1
ip subnet-zero
ip cef
no ip dhcp use vrf connected

IP Routing: BGP Configuration Guide
703


BGP Support for the L2VPN Address Family
Example: Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family

!
no mpls traffic-eng auto-bw timers frequency 0
mpls label range 1000 2000
mpls label protocol ldp
l2 router-id 10.1.1.1
l2 vfi auto autodiscovery
vpn id 100
!
pseudowire-class mpls
encapsulation mpls
!
interface Loopback1
ip address 10.1.1.1 255.255.255.255
!
interface GigabitEthernet0/0/1
description Backbone interface
ip address 10.0.0.1 255.255.255.0
mpls ip
!
router ospf 1
log-adjacency-changes
network 10.10.1.0 0.0.0.255 area 0
network 192.168.0.0 0.0.0.255 area 0
!
router bgp 65000
no bgp default ipv4-unicast
bgp log-neighbor-changes
bgp update-delay 1
neighbor 10.10.10.2 remote-as 65000
neighbor 10.10.10.2 update-source Loopback 1
neighbor 10.10.10.3 remote-as 65000
neighbor 10.10.10.3 update-source Loopback 1
!
address-family l2vpn vpls
neighbor 10.10.10.2 activate
neighbor 10.10.10.2 send-community extended
neighbor 10.10.10.3 activate
neighbor 10.10.10.3 send-community extended
exit-address-family
!
ip classless

Router N-PE2
ip subnet-zero
ip cef
no ip dhcp use vrf connected
!
no mpls traffic-eng auto-bw timers frequency 0
mpls label range 2000 3000
mpls label protocol ldp
l2 router-id 10.1.1.2
l2 vfi auto autodiscovery
vpn id 100
!
pseudowire-class mpls
encapsulation mpls
!
interface Loopback1
ip address 10.1.1.2 255.255.255.255
!
interface GigabitEthernet0/0/1
description Backbone interface

IP Routing: BGP Configuration Guide
704


BGP Support for the L2VPN Address Family
Example: Configuring VPLS Autodiscovery Using BGP and the L2VPN Address Family

ip address 10.0.0.2 255.255.255.0
mpls ip
!
router ospf 1
log-adjacency-changes
network 10.10.1.0 0.0.0.255 area 0
network 192.168.0.0 0.0.0.255 area 0
!
router bgp 65000
no bgp default ipv4-unicast
bgp log-neighbor-changes
bgp update-delay 1
neighbor 10.10.10.1 remote-as 65000
neighbor 10.10.10.1 update-source Loopback1
neighbor 10.10.10.3 remote-as 65000
neighbor 10.10.10.3 update-source Loopback1
!
address-family l2vpn vpls
neighbor 10.10.10.1 activate
neighbor 10.10.10.1 send-community extended
neighbor 10.10.10.3 activate
neighbor 10.10.10.3 send-community extended
exit-address-family
!
ip classless

Router N-PE3
ip subnet-zero
ip cef
no ip dhcp use vrf connected
!
no mpls traffic-eng auto-bw timers frequency 0
mpls label range 2000 3000
mpls label protocol ldp
l2 router-id 10.1.1.3
l2 vfi auto autodiscovery
vpn id 100
!
pseudowire-class mpls
encapsulation mpls
!
interface Loopback1
ip address 10.1.1.3 255.255.255.255
!
interface GigabitEthernet0/0/1
description Backbone interface
ip address 10.0.0.3 255.255.255.0
mpls ip
!
router ospf 1
log-adjacency-changes
network 10.10.1.0 0.0.0.255 area 0
network 192.168.0.0 0.0.0.255 area 0
!
router bgp 65000
no bgp default ipv4-unicast
bgp log-neighbor-changes
bgp update-delay 1
neighbor 10.10.10.1 remote-as 65000
neighbor 10.10.10.1 update-source Loopback1
neighbor 10.10.10.2 remote-as 65000
neighbor 10.10.10.2 update-source Loopback1

IP Routing: BGP Configuration Guide
705


BGP Support for the L2VPN Address Family
Where to Go Next

!
address-family l2vpn vpls
neighbor 10.10.10.1 activate
neighbor 10.10.10.1 send-community extended
neighbor 10.10.10.2 activate
neighbor 10.10.10.2 send-community extended
exit-address-family
!
ip classless

Where to Go Next
For more details about configuring VPLS autodiscovery, see the “VPLS Autodiscovery: BGP Based” module
in the MPLS Layer 2 VPNs Configuration Guide.

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

MIBs
MIB MIBs Link
—

To locate and download MIBs for selected platforms, Cisco software releases, and feature sets, use
Cisco MIB Locator found at the following URL:
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
706


BGP Support for the L2VPN Address Family
Feature Information for BGP Support for the L2VPN Address Family

Feature Information for BGP Support for the L2VPN Address
Family
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 59: Feature Information for BGP Support for the L2VPN Address Family

Feature Name

Releases

Feature Information

BGP Support for
the L2VPN
Address Family

Cisco IOS XE
Release 2.6

BGP support for the L2VPN address family introduces a
BGP-based autodiscovery mechanism to distribute L2VPN
endpoint provisioning information. BGP uses a separate L2VPN
Routing Information Base (RIB) to store endpoint provisioning
information, which is updated each time any Layer 2 VFI is
configured. When BGP distributes the endpoint provisioning
information in an update message to all its BGP neighbors, the
endpoint information is used to set up a pseudowire mesh to
support L2VPN-based services.

Cisco IOS XE
Release 3.3SG

The following commands were introduced or modified by this
feature: address-family l2vpn, clear ip bgp l2vpn, and show ip
bgp l2vpn.

IP Routing: BGP Configuration Guide
707


BGP Support for the L2VPN Address Family
Feature Information for BGP Support for the L2VPN Address Family

IP Routing: BGP Configuration Guide
708
