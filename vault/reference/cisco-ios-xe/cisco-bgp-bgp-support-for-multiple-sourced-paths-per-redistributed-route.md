---
title: "BGP Support for Multiple Sourced Paths Per Redistributed Route"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-multiple-sourced-paths-per-redistributed-route
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 85 BGP Support for Multiple Sourced Paths Per Redistributed Route The BGP Support for Multiple Sourced Paths per Redistributed Route feature allows multiple paths with route redistribution or other sourcing mechanisms like the network command into BGP. This feature also allows multiple paths from the same source to be imported and exported across virtual routing and forwarding (VRF) inst"
---

# BGP Support for Multiple Sourced Paths Per Redistributed Route

CHAPTER

85

BGP Support for Multiple Sourced Paths Per
Redistributed Route
The BGP Support for Multiple Sourced Paths per Redistributed Route feature allows multiple paths with route
redistribution or other sourcing mechanisms like the network command into BGP. This feature also allows
multiple paths from the same source to be imported and exported across virtual routing and forwarding (VRF)
instances.
This module provides an overview of the feature and describes how to configure it.
• Finding Feature Information, on page 1149
• Restrictions for BGP Support for Multiple Sourced Paths Per Redistributed Route, on page 1149
• Information About BGP Support for Multiple Sourced Paths Per Redistributed Route, on page 1150
• How to Configure BGP Support for Multiple Sourced Paths Per Redistributed Routes, on page 1150
• Configuration Examples for BGP Multiple Sourced Paths Per Redistributed Route, on page 1152
• Additional References for BGP Support for Multiple Sourced Paths Per Redistributed Route, on page
1154
• Feature Information for BGP Support for Multiple Sourced Paths Per Redistributed Route, on page 1154

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions for BGP Support for Multiple Sourced Paths Per
Redistributed Route
The following restriction apply to this feature:
• Paths that are sourced with 0.0.0.0 as the gateway address will not have multiple paths redistributed into
the Border Gateway Protocol (BGP). As a result, every sourced path must have a unique gateway.

IP Routing: BGP Configuration Guide
1149


BGP Support for Multiple Sourced Paths Per Redistributed Route
Information About BGP Support for Multiple Sourced Paths Per Redistributed Route

Information About BGP Support for Multiple Sourced Paths Per
Redistributed Route
BGP Support for Multiple Sourced Paths Per Redistributed Route Overview
The BGP Support for Multiple Sourced Paths per Redistributed Route feature allows multiple paths with route
redistribution or other sourcing mechanisms like the network command into the Border Gateway Protocol
(BGP). Prior to this feature, BGP accepted only one path from the Routing Information Base (RIB) to create
a single BGP-sourced path for a redistributed network; even if the RIB had more than one path for the same
network.
This feature also allows multiple paths from the same source to be imported and exported across virtual routing
and forwarding (VRF) instances. Import of more than the default path into a VRF instance was already
supported in BGP. However, these multiple paths had to be from different neighbors or sources and not from
the same source.
By enabling this feature, customers can export Equal Cost Multipath (ECMP) sourced paths or next-hops
from one VRF into hundreds of VRFs on the same device using BGP. Each of these paths are installed as
multipaths into the RIB, and provides ECMP paths in other VRFs also.
For BGP to accept all the paths or next-hops per route from the redistributing protocol in the RIB, configure
the bgp sourced-paths command. If you either disable or do not enable this command, BGP allows the import
of only one sourced path per network from the RIB.

How to Configure BGP Support for Multiple Sourced Paths Per
Redistributed Routes
Configuring Multiple Sourced Paths
When you configure the bgp sourced-paths command, the Border Gateway Protocol (BGP) accepts all paths
from the Routing Information Base (RIB). When the bgp sourced-paths command is removed, the configuration
returns to the default behavior of allowing only one sourced path per network from the RIB into BGP.
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

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 vrf vrf-name
bgp sourced-paths per-net static all
redistribute static
neighbor ip-address remote-as neighbor-as
neighbor ip-address activate
neighbor ip-address send-community both

IP Routing: BGP Configuration Guide
1150


BGP Support for Multiple Sourced Paths Per Redistributed Route
Configuring Multiple Sourced Paths

10.

end

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

Configures the BGP routing process and enters the routing
configuration mode.

Device(config)# router bgp 65000

Step 4

address-family ipv4 vrf vrf-name
Example:

Step 5

Enters address family configuration mode to configure a
routing session using standard IPv4 address prefixes.
You can also configure the address-family ipv6
command based on your network configuration.

Device(config-router)# address-family ipv4 vrf
blue

Note

bgp sourced-paths per-net static all

Allows per network sourcing of all static paths in the RIB.

Example:
Device(config-router-af)# bgp sourced-paths
per-net static all

Step 6

redistribute static

Redistributes static routes from another routing protocol.

Example:
Device(config-router-af)# redistribute static

Step 7

neighbor ip-address remote-as neighbor-as
Example:

Adds an entry into the BGP or multiprotocol BGP neighbor
table.

Device(config-router-af)# neighbor 204.0.0.3
remote-as 65000

Step 8

neighbor ip-address activate

Enables the exchange of information with a BGP neighbor.

Example:
Device(config-router-af)# neighbor 204.0.0.3
activate

Step 9

neighbor ip-address send-community both
Example:

Specifies that a communities attribute should be sent to a
BGP neighbor.

Device(config-router-af)# neighbor 204.0.0.3
send-community both

IP Routing: BGP Configuration Guide
1151


BGP Support for Multiple Sourced Paths Per Redistributed Route
Configuration Examples for BGP Multiple Sourced Paths Per Redistributed Route

Step 10

Command or Action

Purpose

end

Exits address family configuration mode and returns to
privileged EXEC mode.

Example:
Device(config-router-af)# end

Configuration Examples for BGP Multiple Sourced Paths Per
Redistributed Route
Example: Configuring Multiple Sourced Paths
Figure 94: Deployment Scenario for BGP Multiple Paths Replication

The above figure displays a deployment scenario in which BGP replicates multiple paths from VRF
BLUE to VRF RED. VRF RED can import more paths, in addition to the best-path, by using the
same route target export in VRF BLUE and VRF RED. This helps multiple paths to get into VRF
RED.
Device# configure terminal
Device(config)# ip vrf blue
Device(config-vrf)# rd 100:200
Device(config-vrf)# route-target export 200:200
Device(config-vrf)# route-target import 200:200
Device(config-vrf)# exit
Device(config)# ip vrf red
Device(config-vrf)# rd 200:200
Device(config-vrf)# route-target export 300:200
Device(config-vrf)# route-target import 300:200
Device(config-vrf)# route-target import 200:200
Device(config-vrf)# exit
Device(config)# interface Loopback 0
Device(config-if)# ip address 198.51.100.1 255.255.255.255

IP Routing: BGP Configuration Guide
1152


BGP Support for Multiple Sourced Paths Per Redistributed Route
Example: Configuring Multiple Sourced Paths

Device(config-if)# exit
Device(config)# interface Ethernet 1/0
Device(config-if)# ip address 203.0.113.1 19.0.0.32 255.255.255.255
Device(config-if)# no shutdown
Device(config-if)# exit
Device(config)# interface Ethernet 1/2
Device(config-if)# ip address 209.165.200.225 255.255.255.240
Device(config-if)# no shutdown
Device(config-if)# exit
Device(config)# interface Ethernet 1/2.2
Device(config-subif)# encapsulation dot1Q 2
Device(config-subif)# ip vrf forwarding blue
Device(config-subif)# ip address 192.168.0.1 255.255.255.240
Device(config-subif)# no shutdown
Device(config-subif)# exit
Device(config)# interface Ethernet 1/2.3
Device(config-subif)# encapsulation dot1Q 3
Device(config-subif)# ip vrf forwarding blue
Device(config-subif)# ip address 1922.168.0.17 255.255.255.240
Device(config-subif)# no shutdown
Device(config-subif)# exit
Device(config)# router ospf 2 vrf blue
Device(config-router)# network 192.68.0.0 0.0.0.255 area 0
Device(config-router)# network 192.68.1.16 0.0.0.255 area 0
Device(config-router)# exit
!
Device(config)# router ospf 1
Device(config-router)# network 209.165.200.224 0.0.255.255 area 0
Device(config-router)# exit
Device(config)# router bgp 65000
Device(config-router)# no bgp default ipv4-unicast
Device(config-router)# neighbor 10.0.0.2 remote-as 65000
Device(config-router)# neighbor 10.0.0.2 update-source Loopback0
Device(config-router)# address-family ipv4
Device(config-router-af)# exit-address-family
Device(config-router)# address-family vpnv4
Device(config-router-af)# neighbor 10.0.0.2 activate
Device(config-router-af)# neighbor 10.0.0.2 send-community extended
Device(config-router-af)# exit-address-family
Device(config-router)# address-family ipv4 vrf blue
Device(config-router-af)# bgp sourced-paths per-net static all
Device(config-router-af)# bgp sourced-paths per-net ospf all
Device(config-router-af)# redistribute static
Device(config-router-af)# redistribute ospf 2
Device(config-router-af)# exit-address-family
Device(config-router)# address-family ipv4 vrf red
Device(config-router-af)# import path selection all
Device(config-router-af)# import path limit 2
Device(config-router-af)# maximum-paths 2
Device(config-router-af)# exit-address-family
Device(config-router)# exit
Device(config)# ip route vrf blue 192.0.2.2 255.255.255.255 10.0.0.2 global

IP Routing: BGP Configuration Guide
1153


BGP Support for Multiple Sourced Paths Per Redistributed Route
Additional References for BGP Support for Multiple Sourced Paths Per Redistributed Route

Device(config)# ip route vrf blue 192.0.2.2 255.255.255.255 172.16.0.2 global
Device(config)# end

Additional References for BGP Support for Multiple Sourced
Paths Per Redistributed Route
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

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

Feature Information for BGP Support for Multiple Sourced Paths
Per Redistributed Route
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
1154


BGP Support for Multiple Sourced Paths Per Redistributed Route
Feature Information for BGP Support for Multiple Sourced Paths Per Redistributed Route

Table 105: Feature Information for BGP Support for Multiple Sourced Paths Per Redistributed Route

Feature Name

Releases

Feature Information

BGP Support for Multiple
Cisco IOS XE Release 3.15S The BGP Support for Multiple Sourced
Sourced Paths Per Redistributed
Paths per Redistributed Route feature allows
Route
multiple paths with route redistribution or
other sourcing mechanisms like the
network command into BGP. This feature
also allows multiple paths from the same
source to be imported and exported across
virtual routing and forwarding (VRF)
instances.
In Cisco IOS XE Release 3.15S, this feature
was introduced on Cisco ASR 1000 Series
Aggregation Services Routers.
The following command was introduced:
bgp sourced-paths.

IP Routing: BGP Configuration Guide
1155


BGP Support for Multiple Sourced Paths Per Redistributed Route
Feature Information for BGP Support for Multiple Sourced Paths Per Redistributed Route

IP Routing: BGP Configuration Guide
1156
