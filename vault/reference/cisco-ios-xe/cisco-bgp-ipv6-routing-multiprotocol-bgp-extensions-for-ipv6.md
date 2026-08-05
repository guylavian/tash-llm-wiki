---
title: "IPv6 Routing: Multiprotocol BGP Extensions for IPv6"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-ipv6-routing-multiprotocol-bgp-extensions-for-ipv6
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 7 IPv6 Routing: Multiprotocol BGP Extensions for IPv6 • Finding Feature Information, on page 187 • Information About IPv6 Routing: Multiprotocol BGP Extensions for IPv6, on page 187 • How to Implement Multiprotocol BGP for IPv6, on page 188 • Configuration Examples for Multiprotocol BGP for IPv6, on page 193 • Additional References, on page 195 • Feature Information for IPv6 Routing Mult"
---

# IPv6 Routing: Multiprotocol BGP Extensions for IPv6

CHAPTER

7

IPv6 Routing: Multiprotocol BGP Extensions for
IPv6
• Finding Feature Information, on page 187
• Information About IPv6 Routing: Multiprotocol BGP Extensions for IPv6, on page 187
• How to Implement Multiprotocol BGP for IPv6, on page 188
• Configuration Examples for Multiprotocol BGP for IPv6, on page 193
• Additional References, on page 195
• Feature Information for IPv6 Routing Multiprotocol BGP Extensions for IPv6, on page 196

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About IPv6 Routing: Multiprotocol BGP Extensions
for IPv6
Multiprotocol BGP Extensions for IPv6
Multiprotocol BGP is the supported Exterior Gateway Protocol (EGP) for IPv6. Multiprotocol BGP extensions
for IPv6 supports many of the same features and functionality as IPv4 BGP. IPv6 enhancements to multiprotocol
BGP include support for an IPv6 address family and Network Layer Reachability Information (NLRI) and
next hop (the next device in the path to the destination) attributes that use IPv6 addresses.

IP Routing: BGP Configuration Guide
187


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
How to Implement Multiprotocol BGP for IPv6

How to Implement Multiprotocol BGP for IPv6
Configuring an IPv6 BGP Routing Process and BGP Router ID
Perform this task to configure an IPv6 BGP routing process and an optional BGP router ID for a BGP-speaking
device.
BGP uses a router ID to identify BGP-speaking peers. The BGP router ID is 32-bit value that is often represented
by an IPv4 address. By default, the router ID is set to the IPv4 address of a loopback interface on the device.
If no loopback interface is configured on the device, then the software chooses the highest IPv4 address
configured to a physical interface on the device to represent the BGP router ID.
When configuring BGP on a device that is enabled only for IPv6 (that is, the device does not have an IPv4
address), you must manually configure the BGP router ID for the device. The BGP router ID, which is
represented as a 32-bit value using an IPv4 address syntax, must be unique to the BGP peers of the device.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp as-number
no bgp default ipv4-unicast
bgp router-id ip-address

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

router bgp as-number
Example:

Configures a BGP routing process, and enters router
configuration mode for the specified routing process.

Device(config)# router bgp 65000

Step 4

no bgp default ipv4-unicast
Example:

IP Routing: BGP Configuration Guide
188

Disables the IPv4 unicast address family for the BGP
routing process specified in the previous step.


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Configuring IPv6 Multiprotocol BGP Between Two Peers

Command or Action

Purpose
Note

Device(config-router)# no bgp default ipv4-unicast

Step 5

bgp router-id ip-address
Example:

Routing information for the IPv4 unicast address
family is advertised by default for each BGP
routing session configured with the neighbor
remote-as command unless you configure the
no bgp default ipv4-unicast command before
configuring the neighbor remote-as command.

(Optional) Configures a fixed 32-bit router ID as the
identifier of the local device running BGP.
Note

Device(config-router)# bgp router-id 192.168.99.70

Configuring a router ID using the bgp router-id
command resets all active BGP peering sessions.

Configuring IPv6 Multiprotocol BGP Between Two Peers
By default, neighbors that are defined using the neighbor remote-as command in router configuration mode
exchange only IPv4 unicast address prefixes. To exchange other address prefix types, such as IPv6 prefixes,
neighbors must also be activated using the neighbor activate command in address family configuration mode
for the other prefix types, as shown for IPv6 prefixes.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
router bgp as-number
neighbor {ip-address | ipv6-address [%] | peer-group-name} remote-as autonomous-system-number
[alternate-as autonomous-system-number ...]
5. address-family ipv6 [unicast | multicast]
6. neighbor {ip-address | peer-group-name | ipv6-address %} activate
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

router bgp as-number
Example:

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 65000

IP Routing: BGP Configuration Guide
189


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Advertising IPv4 Routes Between IPv6 BGP Peers

Command or Action
Step 4

Purpose

Adds the IPv6 address of the neighbor in the specified
neighbor {ip-address | ipv6-address [%] |
peer-group-name} remote-as autonomous-system-number autonomous system to the IPv6 multiprotocol BGP neighbor
table of the local device.
[alternate-as autonomous-system-number ...]
Example:
Device(config-router)# neighbor 2001:DB8:0:CC00::1
remote-as 64600

Step 5

address-family ipv6 [unicast | multicast]
Example:
Device(config-router)# address-family ipv6

Step 6

neighbor {ip-address | peer-group-name | ipv6-address
%} activate

Specifies the IPv6 address family and enters address family
configuration mode.
• The unicast keyword specifies the IPv6 unicast address
family. By default, the device is placed in configuration
mode for the IPv6 unicast address family if a keyword
is not specified with the address-family ipv6
command.
• The multicast keyword specifies IPv6 multicast
address prefixes.
Enables the neighbor to exchange prefixes for the IPv6
address family with the local device.

Example:
Device(config-router-af)# neighbor
2001:DB8:0:CC00::1 activate

Advertising IPv4 Routes Between IPv6 BGP Peers
If an IPv6 network is connecting two separate IPv4 networks, IPv6 can be used to advertise the IPv4 routes.
Configure the peering using the IPv6 addresses within the IPv4 address family. Set the next hop with a static
route or with an inbound route map because the advertised next hop will usually be unreachable. Advertising
IPv6 routes between two IPv4 peers is also possible using the same model.
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

enable
configure terminal
router bgp as-number
neighbor peer-group-name peer-group
neighbor {ip-address | ipv6-address[%] | peer-group-name} remote-as autonomous-system-number
[alternate-as autonomous-system-number ...]
address-family ipv4 [mdt | multicast | tunnel | unicast [vrf vrf-name] | vrf vrf-name]
neighbor ipv6-address peer-group peer-group-name
neighbor {ip-address | peer-group-name | ipv6-address [%]} route-map map-name {in | out}
exit
exit
route-map map-tag [permit | deny] [sequence-number]

IP Routing: BGP Configuration Guide
190


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Advertising IPv4 Routes Between IPv6 BGP Peers

12.

set ip next-hop ip-address [... ip-address] [peer-address]

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

router bgp as-number
Example:

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 65000

Step 4

neighbor peer-group-name peer-group

Creates a multiprotocol BGP peer group.

Example:
Device(config-router)# neighbor 6peers peer-group

Step 5

Adds the IPv6 address of the neighbor in the specified
neighbor {ip-address | ipv6-address[%] |
peer-group-name} remote-as autonomous-system-number autonomous system to the IPv6 multiprotocol BGP
neighbor table of the local device.
[alternate-as autonomous-system-number ...]
Example:
Device(config-router)# neighbor 6peers remote-as
65002

Step 6

address-family ipv4 [mdt | multicast | tunnel | unicast Enters address family configuration mode to configure a
routing session using standard IPv4 address prefixes.
[vrf vrf-name] | vrf vrf-name]
Example:
Device(config-router)# address-family ipv4

Step 7

neighbor ipv6-address peer-group peer-group-name Assigns the IPv6 address of a BGP neighbor to a peer
group.
Example:
Device(config-router-af)# neighbor
2001:DB8:1234::2 peer-group 6peers

Step 8

neighbor {ip-address | peer-group-name | ipv6-address
[%]} route-map map-name {in | out}
Example:

Applies a route map to incoming or outgoing routes.
• Changes to the route map will not take effect for
existing peers until the peering is reset or a soft reset
is performed. Using the clear bgp ipv6 command

IP Routing: BGP Configuration Guide
191


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Clearing External BGP Peers

Command or Action
Device(config-router-af)# neighbor 6peers
route-map rmap out

Step 9

exit
Example:

Purpose
with the soft and in keywords will perform a soft
reset.
Exits address family configuration mode, and returns the
device to router configuration mode.

Device(config-router-af)# exit

Step 10

exit
Example:

Exits router configuration mode, and returns the device to
global configuration mode.

Device(config-router)# exit

Step 11

route-map map-tag [permit | deny] [sequence-number] Defines a route map and enters route-map configuration
mode.
Example:
Device(config)# route-map rmap permit 10

Step 12

set ip next-hop ip-address [... ip-address] [peer-address] Overrides the next hop advertised to the peer for IPv4
packets.
Example:
Device(config-route-map)# set ip next-hop
10.21.8.10

Clearing External BGP Peers
SUMMARY STEPS
1. enable
2. clear bgp ipv6 {unicast | multicast} external [soft] [in | out]
3. clear bgp ipv6 {unicast | multicast} peer-group name
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

clear bgp ipv6 {unicast | multicast} external [soft] [in | Clears external IPv6 BGP peers.
out]
Example:
Device# clear bgp ipv6 unicast external soft in

IP Routing: BGP Configuration Guide
192


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Configuring BGP IPv6 Admin Distance

Step 3

Command or Action

Purpose

clear bgp ipv6 {unicast | multicast} peer-group name

Clears all members of an IPv6 BGP peer group.

Example:
Device# clear bgp ipv6 unicast peer-group marketing

Configuring BGP IPv6 Admin Distance
•
Before you begin
•
SUMMARY STEPS
1.
DETAILED STEPS
Command or Action
Step 1

Purpose

Example:

Example
What to do next
•

Configuration Examples for Multiprotocol BGP for IPv6
Example: Configuring a BGP Process, BGP Router ID, and IPv6 Multiprotocol
BGP Peer
The following example enables IPv6 globally, configures a BGP process, and establishes a BGP router ID.
Also, the IPv6 multiprotocol BGP peer 2001:DB8:0:CC00::1 is configured and activated.
ipv6 unicast-routing
!
router bgp 65000
no bgp default ipv4-unicast
bgp router-id 192.168.99.70
neighbor 2001:DB8:0:CC00::1 remote-as 64600
address-family ipv6 unicast
neighbor 2001:DB8:0:CC00::1 activate

IP Routing: BGP Configuration Guide
193


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Example: Configuring an IPv6 Multiprotocol BGP Peer Group

Example: Configuring an IPv6 Multiprotocol BGP Peer Group
The following example configures the IPv6 multiprotocol BGP peer group named group1:
router bgp 65000
no bgp default ipv4-unicast
neighbor group1 peer-group
neighbor 2001:DB8:0:CC00::1 remote-as 64600
address-family ipv6 unicast
neighbor group1 activate
neighbor 2001:DB8:0:CC00::1 peer-group group1

Example: Advertising Routes into IPv6 Multiprotocol BGP
The following example injects the IPv6 network 2001:DB8::/24 into the IPv6 unicast database of the local
device. (BGP checks that a route for the network exists in the IPv6 unicast database of the local device before
advertising the network.)
router bgp 65000
no bgp default ipv4-unicast
address-family ipv6 unicast
network 2001:DB8::/24

Example: Configuring a Route Map for IPv6 Multiprotocol BGP Prefixes
The following example configures the route map named rtp to permit IPv6 unicast routes from network
2001:DB8::/24 if they match the prefix list named cisco:
router bgp 64900
no bgp default ipv4-unicast
neighbor 2001:DB8:0:CC00::1 remote-as 64700
address-family ipv6 unicast
neighbor 2001:DB8:0:CC00::1 activate
neighbor 2001:DB8:0:CC00::1 route-map rtp in
ipv6 prefix-list cisco seq 10 permit 2001:DB8::/24
route-map rtp permit 10
match ipv6 address prefix-list cisco

Example: Redistributing Prefixes into IPv6 Multiprotocol BGP
The following example redistributes RIP routes into the IPv6 unicast database of the local device:
router bgp 64900
no bgp default ipv4-unicast
address-family ipv6 unicast
redistribute rip

Example: Advertising IPv4 Routes Between IPv6 Peers
The following example advertises IPv4 routes between IPv6 peers when the IPv6 network is connecting two
separate IPv4 networks. Peering is configured using IPv6 addresses in the IPv4 address family configuration

IP Routing: BGP Configuration Guide
194


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Additional References

mode. The inbound route map named rmap sets the next hop because the advertised next hop is likely to be
unreachable.
router bgp 65000
!
neighbor 6peers peer-group
neighbor 2001:DB8:1234::2 remote-as 65002
address-family ipv4
neighbor 6peers activate
neighbor 6peers soft-reconfiguration inbound
neighbor 2001:DB8:1234::2 peer-group 6peers
neighbor 2001:DB8:1234::2 route-map rmap in
!
route-map rmap permit 10
set ip next-hop 10.21.8.10

Additional References
Related Documents
Related Topic

Document Title

IPv6 addressing and connectivity

IPv6 Configuration Guide

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

IPv6 commands

Cisco IOS IPv6 Command
Reference

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

Standards and RFCs
Standard/RFC Title
RFCs for
IPv6

IPv6
RFCs

MIBs
MIB MIBs Link
—

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: BGP Configuration Guide
195


IPv6 Routing: Multiprotocol BGP Extensions for IPv6
Feature Information for IPv6 Routing Multiprotocol BGP Extensions for IPv6

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

Feature Information for IPv6 Routing Multiprotocol BGP
Extensions for IPv6
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 19: Feature Information for IPv6 Routing Multiprotocol BGP Extensions for IPv6

Feature Name

Releases

IPv6 Routing: Multiprotocol BGP Cisco IOS XE Release 2.1
Extensions for IPv6

IP Routing: BGP Configuration Guide
196

Feature Information
Multiprotocol BGP extensions for
IPv6 supports the same features and
functionality as IPv4 BGP.
