---
title: "BGP Event-Based VPN Import"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-event-based-vpn-import
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 44 BGP Event-Based VPN Import The BGP Event-Based VPN Import feature introduces a modification to the existing Border Gateway Protocol (BGP) path import process. The enhanced BGP path import is driven by events; when a BGP path changes, all of its imported copies are updated as soon as processing is available. Convergence times are significantly reduced because there is no longer any del"
---

# BGP Event-Based VPN Import

CHAPTER

44

BGP Event-Based VPN Import
The BGP Event-Based VPN Import feature introduces a modification to the existing Border Gateway Protocol
(BGP) path import process. The enhanced BGP path import is driven by events; when a BGP path changes,
all of its imported copies are updated as soon as processing is available. Convergence times are significantly
reduced because there is no longer any delay in the propagation of routes due to the software waiting for a
periodic scanner time interval before processing the updates. To implement the new processing, new
command-line interface (CLI) commands are introduced.
• Finding Feature Information, on page 709
• Prerequisites for BGP Event-Based VPN Import, on page 709
• Information About BGP Event-Based VPN Import, on page 710
• How to Configure BGP Event-Based VPN Import, on page 711
• Configuration Examples for BGP Event-Based VPN Import, on page 717
• Additional References, on page 717
• Feature Information for BGP Event-Based VPN Import, on page 718

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP Event-Based VPN Import
Cisco Express Forwarding or distributed Cisco Express Forwarding must be enabled on all participating
routers.

IP Routing: BGP Configuration Guide
709


BGP Event-Based VPN Import
Information About BGP Event-Based VPN Import

Information About BGP Event-Based VPN Import
BGP Event-Based VPN Import
The BGP Event-Based VPN Import feature introduces a modification to the existing BGP path import process.
BGP Virtual Private Network (VPN) import provides importing functionality for BGP paths where BGP paths
are imported from the BGP VPN table into a BGP virtual routing and forwarding (VRF) topology. In the
existing path import process, when path updates occur, the import updates are processed during the next scan
time which is a configurable interval of 5 to 15 seconds. The scan time adds a delay in the propagation of
routes. The enhanced BGP path import is driven by events; when a BGP path changes, all of its imported
copies are updated as soon as processing is available.
Using the BGP Event-Based VPN Import feature, convergence times are significantly reduced because provider
edge (PE) routers can propagate VPN paths to customer edge (CE) routers without the scan time delay.
Configuration changes such as adding imported route-targets to a VRF are not processed immediately, and
are still handled during the 60-second periodic scanner pass.

Import Path Selection Policy
Event-based VPN import introduces three path selection policies:
• All—Import all available paths from the exporting net that match any route target (RT) associated with
the importing VRF instance.
• Best path—Import the best available path that matches the RT of the VRF instance. If the best path in
the exporting net does not match the RT of the VRF instance, a best available path that matches the RT
of the VRF instance is imported.
• Multipath—Import the best path and all paths marked as multipaths that match the RT of the VRF
instance. If there are no best path or multipath matches, then the best available path is selected.
Multipath and best path options can be restricted using an optional keyword to ensure that the selection is
made only on the configured option. If the strict keyword is configured in the import path selection command,
the software disables the fall back safety option of choosing the best available path. If no paths appropriate
to the configured option (best path or multipath) in the exporting net match the RT of the VRF instance, then
no paths are imported. This behavior matches the behavior of the software before the BGP Event-Based VPN
Import feature was introduced.
When the restriction is not set, paths that are imported as the best available path are tagged. In show command
output these paths are identified with the wording, “imported safety path.”
The paths existing in an exporting net that are considered for import into a VRF instance may have been
received from another peer router and were not subject to the VPN importing rules. These paths may contain
the same route-distinguisher (RD) information because the RD information is local to a router, but some of
these paths do not match the RT of the importing VRF instance and are marked as “not-in-vrf” in the show
command output. Any path that is marked as “not-in-vrf” is not considered as a best path because paths not
in the VRF appear less attractive than paths in the VRF.

Import Path Limit
To control the memory utilization, a maximum limit of the number of paths imported from an exporting net
can be specified per importing net. When a selection is made of paths to be imported from one or more

IP Routing: BGP Configuration Guide
710


BGP Event-Based VPN Import
How to Configure BGP Event-Based VPN Import

exporting net, the first selection priority is a best path, the next selection priority is for multipaths, and the
lowest selection priority is for nonmultipaths.

How to Configure BGP Event-Based VPN Import
Configuring a Multiprotocol VRF
Perform this task to configure a multiprotocol VRF that allows you to share route-target policies (import and
export) between IPv4 and IPv6 or to configure separate route-target policies for IPv4 and IPv6 VPNs. In this
task, only the IPv4 address family is configured, but we recommend using the multiprotocol VRF configuration
for all new VRF configurations.

Note

This task is not specific to the BGP Event-Based VPN Import feature.

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
vrf definition vrf-name
rd route-distinguisher
route-target {import | export | both} route-target-ext-community
address-family ipv4 [unicast]
exit-address-family
exit
interface type number
vrf forwarding vrf-name
ip address ip-address mask
no shutdown
exit
Repeat Step 3 through Step 13 to bind other VRF instances with an interface.
end

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

IP Routing: BGP Configuration Guide
711


BGP Event-Based VPN Import
Configuring a Multiprotocol VRF

Command or Action

Purpose

Router# configure terminal

Step 3

vrf definition vrf-name
Example:
Router(config)# vrf definition vrf-A

Step 4

rd route-distinguisher
Example:
Router(config-vrf)# rd 45000:1

Step 5

route-target {import | export | both}
route-target-ext-community
Example:
Router(config-vrf)# route-target both 45000:100

Configures a VRF routing table and enters VRF
configuration mode.
• Use the vrf-name argument to specify a name to be
assigned to the VRF.
Creates routing and forwarding tables and specifies the
default route distinguisher for a VPN.
• Use the route-distinguisher argument to add an 8-byte
value to an IPv4 prefix to create a unique VPN IPv4
prefix.
Creates a route target extended community for a VRF.
• Use the import keyword to import routing
information from the target VPN extended
community.
• Use the export keyword to export routing information
to the target VPN extended community.
• Use the both keyword to both import routing
information from, and export routing information to,
the target VPN extended community.
• Use the route-target-ext-community argument to add
the route target extended community attributes to the
VRF’s list of import, export, or both (import and
export) route target extended communities.

Step 6

address-family ipv4 [unicast]
Example:
Router(config-vrf)# address-family ipv4 unicast

Step 7

exit-address-family
Example:

Specifies the IPv4 address family and enters VRF address
family configuration mode.
• This step is required here to specify an address family
for the VRF defined in the previous steps.
Exits VRF address family configuration mode and returns
to VRF configuration mode.

Router(config-vrf-af)# exit-address-family

Step 8

exit
Example:
Router(config-vrf)# exit

IP Routing: BGP Configuration Guide
712

Exits VRF configuration mode and enters global
configuration mode.


BGP Event-Based VPN Import
Configuring Event-Based VPN Import Processing for BGP Paths

Step 9

Command or Action

Purpose

interface type number

Enters interface configuration mode.

Example:
Router(config)# interface FastEthernet 1/1

Step 10

vrf forwarding vrf-name
Example:

Associates a VRF instance with the interface configured
in Step 9.
• When the interface is bound to a VRF, previously
configured IP addresses are removed, and the
interface is disabled.

Router(config-if)# vrf forwarding vrf-A

Step 11

ip address ip-address mask

Configures an IP address for the interface.

Example:
Router(config-if)# ip address 10.4.8.149
255.255.255.0

Step 12

no shutdown

Restarts a disabled interface.

Example:
Router(config-if)# no shutdown

Step 13

exit
Example:

Exits interface configuration mode and enters global
configuration mode.

Router(config-if)# exit

Step 14

Repeat Step 3 through Step 13 to bind other VRF instances -with an interface.

Step 15

end
Example:

Exits global configuration mode and returns to privileged
EXEC mode.

Router(config)# end

Configuring Event-Based VPN Import Processing for BGP Paths
Perform this task to reduce convergence times when BGP paths change by configuring event-based processing
for importing BGP paths into a VRF table. Two new CLI commands allow the configuration of a maximum
number of import paths per importing net and the configuration of a path selection policy.
Before you begin
This task assumes that you have previously configured the VRF to be used with the VRF address family
syntax. To configure a VRF, see the “Configuring a Multiprotocol VRF” section earlier in this module.
Complete BGP neighbor configuration is also assumed. For an example configuration, see the “Example:
Configuring Event-Based VPN Import Processing for BGP Paths” section in this module.

IP Routing: BGP Configuration Guide
713


BGP Event-Based VPN Import
Configuring Event-Based VPN Import Processing for BGP Paths

SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 vrf vrf-name
import path selection {all | bestpath [strict] | multipath [strict]}
import path limit number-of-import-paths
end

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

router bgp autonomous-system-number
Example:

Enters router configuration mode for the specified routing
process.

Router(config)# router bgp 45000

Step 4

address-family ipv4 vrf vrf-name
Example:
Router(config-router)# address-family ipv4 vrf
vrf-A

Step 5

Specifies the IPv4 address family and enters address family
configuration mode.
• Use the vrf keyword and vrf-name argument to specify
the name of the VRF instance to associate with
subsequent IPv4 address family configuration mode
commands.

import path selection {all | bestpath [strict] | multipath Specifies the BGP path selection policy for importing routes
into a VRF table.
[strict]}
Example:

• In this example, all paths that match any RT of the
VRF instance are imported.

Router(config-router-af)# import path selection
all

Step 6

import path limit number-of-import-paths
Example:
Router(config-router-af)# import path limit 3

IP Routing: BGP Configuration Guide
714

Specifies, per importing net, a maximum number of BGP
paths that can be imported from an exporting net.


BGP Event-Based VPN Import
Monitoring and Troubleshooting BGP Event-Based VPN Import Processing

Step 7

Command or Action

Purpose

end

Exits address family configuration mode and returns to
privileged EXEC mode.

Example:
Router(config-router-af)# end

Monitoring and Troubleshooting BGP Event-Based VPN Import Processing
Perform the steps in this task as required to monitor and troubleshoot the BGP event-based VPN import
processing.
Only partial command syntax for the show commands used in this task is displayed. For more details, see the
Cisco IOS IP Routing: BGP Command Reference.
SUMMARY STEPS
1.
2.
3.
4.

enable
show ip bgp vpnv4 {all | rd route-distinguisher | vrf vrf-name} [network-address [mask]]
show ip route [vrf vrf-name] [ip-address [mask]]
debug ip bgp vpnv4 unicast import {events | updates [access-list]}

DETAILED STEPS

Step 1

enable
Enables privileged EXEC mode. Enter your password if prompted.
Example:
Router> enable

Step 2

show ip bgp vpnv4 {all | rd route-distinguisher | vrf vrf-name} [network-address [mask]]
In this example output, a safe import path selection policy is in effect because the strict keyword is not configured using
the import path selection command. When a path is imported as the best available path (when the bestpath or multipaths
are not eligible for import), the path is marked with "imported safety path," as shown in the output.
Example:
Router# show ip bgp vpnv4 all 172.17.0.0
BGP routing table entry for 45000:1:172.17.0.0/16, version 10
Paths: (1 available, best #1, table vrf-A)
Flag: 0x820
Not advertised to any peer
2, imported safety path from 50000:2:172.17.0.0/16
10.0.101.1 from 10.0.101.1 (10.0.101.1)
Origin IGP, metric 200, localpref 100, valid, internal, best
Extended Community: RT:45000:100

The paths existing in an exporting net that are considered for import into a VRF instance may have been received from
another peer router and were not subject to the VPN importing rules. These paths may contain the same route-distinguisher

IP Routing: BGP Configuration Guide
715


BGP Event-Based VPN Import
Monitoring and Troubleshooting BGP Event-Based VPN Import Processing

(RD) information because the RD information is local to a router, but some of these paths do not match the RT of the
importing VRF instance and are marked as "not-in-vrf" in the show command output.
In the following example output, a path was received from another peer router and was not subject to the VPN importing
rules. This path, 10.0.101.2, was added to the VPNv4 table and associated with the vrf-A net because it contains a match
of the RD information although the RD information was from the original router. This path is not, however, an RT match
for vrf-A and is marked as "not-in-vrf." Note that on the net for vrf-A, this path is not the bestpath because any paths that
are not in the VRF appear less attractive than paths in the VRF.
Example:
Router# show ip bgp vpnv4 all 172.17.0.0
BBGP routing table entry for 45000:1:172.17.0.0/16, version 11
Paths: (2 available, best #2, table vrf-A)
Flag: 0x820
Not advertised to any peer
2
10.0.101.2 from 10.0.101.2 (10.0.101.2)
Origin IGP, metric 100, localpref 100, valid, internal, not-in-vrf
Extended Community: RT:45000:200
mpls labels in/out nolabel/16
2
10.0.101.1 from 10.0.101.1 (10.0.101.1)
Origin IGP, metric 50, localpref 100, valid, internal, best
Extended Community: RT:45000:100
mpls labels in/out nolabel/16

Step 3

show ip route [vrf vrf-name] [ip-address [mask]]
In this example output, information about the routing table for VRF vrf-A is displayed:
Example:
Router# show ip route vrf vrf-A 172.17.0.0
Routing Table: vrf-A
Routing entry for 172.17.0.0/16
Known via "bgp 1", distance 200, metric 50
Tag 2, type internal
Last update from 10.0.101.33 00:00:32 ago
Routing Descriptor Blocks:
* 10.0.101.33 (default), from 10.0.101.33, 00:00:32 ago
Route metric is 50, traffic share count is 1
AS Hops 1
Route tag 2
MPLS label: 16
MPLS Flags: MPLS Required

Step 4

debug ip bgp vpnv4 unicast import {events | updates [access-list]}
Use this command to display debugging information related to the importing of BGP paths into a VRF instance table.
The actual output depends on the commands that are subsequently entered.
If no access list to filter prefixes is specified when using the updates keyword, all updates for all prefixes are
displayed and this may slow down your network.

Note

Example:
Router# debug ip bgp vpnv4 unicast import events

IP Routing: BGP Configuration Guide
716


BGP Event-Based VPN Import
Configuration Examples for BGP Event-Based VPN Import

BGP import events debugging is on

Configuration Examples for BGP Event-Based VPN Import
Example: Configuring Event-Based VPN Import Processing for BGP Paths
In this example, a VRF (vrf-A) is configured and VRF forwarding is applied to Fast Ethernet interface 1/1.
In address family mode, the import path selection is set to all and the number of import paths is set to 3. Two
BGP neighbors are configured under the IPv4 address family and activated under the VPNv4 address family.
vrf definition vrf-A
rd 45000:1
route-target import 45000:100
address-family ipv4
exit-address-family
!
interface FastEthernet1/1
no ip address
vrf forwarding vrf-A
ip address 10.4.8.149 255.255.255.0
no shut
exit
!
router bgp 45000
network 172.17.1.0 mask 255.255.255.0
neighbor 192.168.1.2 remote-as 40000
neighbor 192.168.3.2 remote-as 50000
address-family ipv4 vrf vrf-A
import path selection all
import path limit 3
exit-address-family
address-family vpnv4
neighbor 192.168.1.2 activate
neighbor 192.168.3.2 activate
end

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Routing: BGP Configuration Guide
717


BGP Event-Based VPN Import
Feature Information for BGP Event-Based VPN Import

Standards
Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not —
been modified by this feature.
MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this To locate and download MIBs for selected platforms, Cisco
feature, and support for existing MIBs has not IOS releases, and feature sets, use Cisco MIB Locator
been modified by this feature.
found at the following URL:
http://www.cisco.com/go/mibs
RFCs
RFC

Title

No new or modified RFCs are supported by this feature, and support for existing RFCs has not been —
modified by this feature.
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

Feature Information for BGP Event-Based VPN Import
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
718


BGP Event-Based VPN Import
Feature Information for BGP Event-Based VPN Import

Table 60: Feature Information for BGP Event-Based VPN Import

Feature Name

Releases

Feature Information

BGP
Event-Based
VPN Import

Cisco IOS XE
Release 2.6

The BGP Event-Based VPN Import feature introduces a modification
to the existing Border Gateway Protocol (BGP) path import process.
The enhanced BGP path import is driven by events; when a BGP path
changes, all of its imported copies are updated as soon as processing
is available. Convergence times are significantly reduced because
there is no longer any delay in the propagation of routes due to the
software waiting for a periodic scanner time interval before processing
the updates. To implement the new processing, new command-line
interface (CLI) commands are introduced.

Cisco IOS XE
Release 3.3SG

The following commands were introduced or modified:
• bgp scan-time
• import path limit
• import path selection
• maximum-path ebgp
• maximum-path ibgp
• show ip bgp vpnv4
• show ip bgp vpnv6

IP Routing: BGP Configuration Guide
719


BGP Event-Based VPN Import
Feature Information for BGP Event-Based VPN Import

IP Routing: BGP Configuration Guide
720
