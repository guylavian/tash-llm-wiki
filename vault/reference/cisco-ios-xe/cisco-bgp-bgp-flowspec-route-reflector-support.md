---
title: "BGP FlowSpec Route-reflector Support"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-flowspec-route-reflector-support
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 24 BGP FlowSpec Route-reflector Support The BGP (Border Gateway Protocol) Flowspec (Flow Specification) Route Reflector feature enables service providers to control traffic flows in their network. This helps in filtering traffic and helps in taking action against distributed denial of service (DDoS) mitigation by dropping the DDoS traffic or diverting it to an analyzer. BGP flow specific"
---

# BGP FlowSpec Route-reflector Support

CHAPTER

24

BGP FlowSpec Route-reflector Support
The BGP (Border Gateway Protocol) Flowspec (Flow Specification) Route Reflector feature enables service
providers to control traffic flows in their network. This helps in filtering traffic and helps in taking action
against distributed denial of service (DDoS) mitigation by dropping the DDoS traffic or diverting it to an
analyzer.
BGP flow specification provides a mechanism to encode flow specification rules for traffic flows that can be
distributed as BGP Network Layer Reachability Information (NLRI).
• Finding Feature Information, on page 479
• Restrictions for BGP FlowSpec Route-reflector Support, on page 479
• Information About BGP FlowSpec Route-reflector Support, on page 480
• How to Configure BGP FlowSpec Route-reflector Support, on page 481
• Configuration Examples for BGP FlowSpec Route-reflector Support, on page 487
• Additional References for BGP FlowSpec Route-reflector Support, on page 489
• Feature Information for BGP FlowSpec Route-reflector Support, on page 489

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions for BGP FlowSpec Route-reflector Support
• In Cisco IOS 15.5(S) release, BGP flow specification is supported only on a route reflector.
• Mixing of address family matches and actions is not supported in flow spec rules. For example, IPv4
matches cannot be combined with IPv6 actions and vice versa.

IP Routing: BGP Configuration Guide
479


BGP FlowSpec Route-reflector Support
Information About BGP FlowSpec Route-reflector Support

Information About BGP FlowSpec Route-reflector Support
Overview of Flowspec
Flowspec specifies procedures for the distribution of flow specification rules as Border Gateway Protocol
Network Layer Reachability Information (BGP NLRI) that can be used in any application. It also defines
application for the purpose of packet filtering in order to mitigate distributed denial of service attacks.
A flow specification rule consists of a matching part encoded in the BGP NLRI field and an action part encoded
as BGP extended community as defined in the RFC 5575. A flow specification rule is a set of data (represented
in an n-tuple) consisting of several matching criteria that can be applied to IP packet data. BGP flow
specification rules are internally converted to equivalent Cisco Common Classification Policy Language
(C3PL) representing corresponding match and action parameters.
In Cisco IOS 15.5(S) release, Flowspec supports following functions for the BGP route reflector:
• Flowspec rules defined in RFC 5575
• IPv6 extensions
• Redirect IP extensions
• BGP flowspec validation

Matching Criteria
The following table lists the various Flowspec tuples that are supported for BGP.
BGP Flowspec NLRI Type QoS Matching Field (IPv6) QoS Matching Field (IPv4) Input Value
Type 1

IPv6 destination address

IPv4 destination address

Prefix length

Type 2

IPv6 source address

IPv4 source address

Prefix length

Type 3

IPv6 next header

IPv4 protocol

Multi-value range

Type 4

IPv6 source or destination IPv4 source or destination Multi-value range
port
port

Type 5

IPv6 destination port

IPv4 destination port

Multi-value range

Type 6

IPv6 source port

IPv4 source port

Multi-value range

Type 7

IPv6 ICMP type

IPv4 ICMP type

Multi-value range

Type 8

IPv6 ICMP code

IPv4 ICMP code

Multi-value range

Type 9

IPv6 TCP flags

IPv4 TCP flags (2 bytes
include reserved bits)

Bit mask

Type 10

IPv6 packet length

IPv4 packet length

Multi-value range

Type 11

IPv6 traffic class

IPv4 DSCP

Multi-value range

IP Routing: BGP Configuration Guide
480


BGP FlowSpec Route-reflector Support
How to Configure BGP FlowSpec Route-reflector Support

BGP Flowspec NLRI Type QoS Matching Field (IPv6) QoS Matching Field (IPv4) Input Value
Type 12

Reserved

IPv4 fragment bits

Bit mask

Type 13

IPv6 flow label

—

Multi-value range

How to Configure BGP FlowSpec Route-reflector Support
Configuring BGP FlowSpec Route-reflector Support
Perform this task to configure BGP FlowSpec on a route reflector. This task specifies only the IPv4 address
family but, other address families are also supported for BGP flow specifications.
Before you begin
Configure a BGP route reflector.
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
neighbor ip-address remote-as autonomous-system-number
address-family {ipv4 | ipv6 | vpnv4 | vpnv6} flowspec
neighbor ip-address activate
neighbor ip-address route-reflector-client
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

Enters router configuration mode for the BGP routing
process.

Device(config)# router bgp 1

IP Routing: BGP Configuration Guide
481


BGP FlowSpec Route-reflector Support
Disabling BGP FlowSpec Validation

Step 4

Command or Action

Purpose

neighbor ip-address remote-as
autonomous-system-number

Adds an entry to the BGP or multiprotocol BGP neighbor
table.

Example:
Device(config-router)# neighbor 10.1.1.1 remote-as
1

Step 5

address-family {ipv4 | ipv6 | vpnv4 | vpnv6} flowspec
Example:
Device(config-router)# address-family ipv4 flowspec

Step 6

neighbor ip-address activate

Specifies the address family and enters address family
configuration mode.
• Flowspec is supported on IPv4, IPv6, VPNv4 and
VPNv6 address families.
Enables the exchange of information with a BGP neighbor.

Example:
Device(config-router-af)# neighbor 10.1.1.1
activate

Step 7

neighbor ip-address route-reflector-client
Example:

Configures the router as a BGP route reflector and
configures the specified neighbor as its client.

Device(config-router-af)# neighbor 10.1.1.1
route-reflector-client

Step 8

(Optional) Exits address family configuration mode and
returns to privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Disabling BGP FlowSpec Validation
Perform this task if you want to disable the BGP flow specification validations for eBGP peers. The validations
are enabled by default.
To know more about BGP flow specification validations, see RFC 5575
(draft-ietf-idr-bgp-flowspec-oid-01-Revised Validation Procedure for BGP Flow Specifications).
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp autonomous-system-number
address-family {ipv4 | ipv6 | vpnv4 | vpnv6} flowspec
neighbor ip-address validation off

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: BGP Configuration Guide
482


BGP FlowSpec Route-reflector Support
Verifying BGP FlowSpec Route-reflector Support

Command or Action

Purpose

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

Enters router configuration mode for the BGP routing
process.

Device(config)# router bgp 1

Step 4

address-family {ipv4 | ipv6 | vpnv4 | vpnv6} flowspec
Example:

Specifies the address family and enters address family
configuration mode.
• Flowspec is supported on IPv4, IPv6, VPNv4 and
VPNv6 address families.

Device(config-router)# address-family ipv4 flowspec

Step 5

neighbor ip-address validation off

Disables validation of flow specification for eBGP peers.

Example:
Device(config-router-af)# neighbor 10.1.1.1
validation off

Verifying BGP FlowSpec Route-reflector Support
The show commands can be entered in any order.
Before you begin
Configure BGP FlowSec on a route reflector.
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

show bgp ipv4 flowspec
show bgp ipv4 flowspec detail
show bgp ipv4 flowspec summary
show bgp ipv6 flowspec
show bgp ipv6 flowspec detail
show bgp ipv6 flowspec summary
show bgp vpnv4 flowspec
show bgp vpnv4 flowspec all detail
show bgp vpnv6 flowspec
show bgp vpnv6 flowspec all detail

IP Routing: BGP Configuration Guide
483


BGP FlowSpec Route-reflector Support
Verifying BGP FlowSpec Route-reflector Support

DETAILED STEPS

Step 1

show bgp ipv4 flowspec
This command displays the IPv4 flowspec routes.
Example:
Device# show bgp ipv4 flowspec
BGP table version is 3, local router ID is 10.10.10.2 Status codes: s suppressed, d damped, h
history,
* valid, > best, i - internal, r RIB-failure, S Stale,
m multipath, b backup-path, f RT-Filter, best-external, a additional-path,
c RIB-compressed, Origin codes: i - IGP, e - EGP, ? - incomplete RPKI validation codes: V valid,
I invalid, N Not found
Network
*>i Dest:2.2.2.0/24
*>i Dest:3.3.3.0/24

Step 2

Next Hop
10.0.101.1
10.0.101.1

Metric LocPrf Weight Path
100
0 i
100
0 i

show bgp ipv4 flowspec detail
This command displays the detailed information about IPv4 flowspec routes.
Example:
Device# show bgp ipv4 flowspec detail
BGP routing table entry for Dest:2.2.2.0/24, version 2
Paths: (1 available, best #1, table IPv4-Flowspec-BGP-Table)
Advertised to update-groups:
1
Refresh Epoch 1
Local, (Received from a RR-client)
10.0.101.1 from 10.0.101.1 (10.0.101.1)
Origin IGP, localpref 100, valid, internal, best
Extended Community: FLOWSPEC Redirect-IP:0x000000000001
rx pathid: 0, tx pathid: 0x0
BGP routing table entry for Dest:3.3.3.0/24, version 3
Paths: (1 available, best #1, table IPv4-Flowspec-BGP-Table)
Advertised to update-groups:
1
Refresh Epoch 1
Local, (Received from a RR-client)
10.0.101.1 from 10.0.101.1 (10.0.101.1)
Origin IGP, localpref 100, valid, internal, best
rx pathid: 0, tx pathid: 0x0

Step 3

show bgp ipv4 flowspec summary
This command displays the IPv4 flowspec neighbors.
Example:
Device# show bgp ipv4 flowspec summary
BGP router identifier 10.10.10.2, local AS number 239 BGP table version is 3, main routing table
version 3
2 network entries using 16608 bytes of memory

IP Routing: BGP Configuration Guide
484


BGP FlowSpec Route-reflector Support
Verifying BGP FlowSpec Route-reflector Support

2 path entries using 152 bytes of memory
2/2 BGP path/bestpath attribute entries using 304 bytes of memory
1 BGP AS-PATH entries using 24 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory BGP using 17136 total bytes of memory BGP
activity 18/0
prefixes, 18/0 paths, scan interval 15 secs
Neighbor
State/PfxRcd
10.0.101.1
2
10.0.101.2
Idle
10.0.101.3
Idle
10.10.10.1

Step 4

V

AS MsgRcvd MsgSent

TblVer

InQ OutQ Up/Down

4

239

70

24

3

0

0 00:10:58

4

239

0

0

1

0

0 never

4

240

0

0

1

0

0 never

4

239

19

23

3

0

0 00:10:53

show bgp ipv6 flowspec
This command displays the IPv6 flowspec routes.
Example:
Device# show bgp ipv6 flowspec
BGP table version is 2, local router ID is 10.10.10.2 Status codes: s suppressed, d damped, h
history,
* valid, > best, i - internal, r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
x best-external, a additional-path, c RIB-compressed, Origin codes: i - IGP, e - EGP,
? - incomplete RPKI validation codes: V valid, I invalid, N Not found
Network
Next Hop
*>i Dest:3::/0-24,Source:4::/0-24
FEC0::1001

Step 5

Metric LocPrf Weight Path
100

0 i

show bgp ipv6 flowspec detail
This command displays the detailed information about IPv6 flowspec routes.
Example:
Device# show bgp ipv6 flowspec detail
BGP routing table entry for Dest:3::/0-24,Source:4::/0-24, version 2
Paths: (1 available, best #1, table Global-Flowspecv6-Table)
Advertised to update-groups:
2
Refresh Epoch 1
Local
FEC0::1001 from FEC0::1001 (10.0.101.2)
Origin IGP, localpref 100, valid, internal, best
rx pathid: 0, tx pathid: 0x0

Step 6

show bgp ipv6 flowspec summary
This command displays the IPv6 flowspec neighbors.
Example:

IP Routing: BGP Configuration Guide
485


BGP FlowSpec Route-reflector Support
Verifying BGP FlowSpec Route-reflector Support

Device# show bgp ipv6 flowspec summary
BGP router identifier 10.10.10.2, local AS number 239 BGP table version is 3, main routing table
version 3
2 network entries using 16608 bytes of memory
2 path entries using 152 bytes of memory
2/2 BGP path/bestpath attribute entries using 304 bytes of memory
1 BGP AS-PATH entries using 24 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory BGP using 17136 total bytes of memory BGP
activity 18/0
prefixes, 18/0 paths, scan interval 15 secs
Neighbor
State/PfxRcd
10.0.101.1
2
10.0.101.2
Idle
10.0.101.3
Idle
10.10.10.1

Step 7

V

AS MsgRcvd MsgSent

TblVer

InQ OutQ Up/Down

4

239

70

24

3

0

0 00:10:58

4

239

0

0

1

0

0 never

4

240

0

0

1

0

0 never

4

239

19

23

3

0

0 00:10:53

show bgp vpnv4 flowspec
This command displays the VPNv4 flowspec neighbors.
Example:
Device# show bgp vpnv4 flowspec
BGP table version is 2, local router ID is 10.10.10.2 Status codes: s suppressed, d damped, h
history,
* valid, > best, i - internal,r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
x best-external, a additional-path, c RIB-compressed, Origin codes: i - IGP, e - EGP,
? - incomplete RPKI validation codes: V valid, I invalid, N Not found
Network
Next Hop
Route Distinguisher: 200:200
*>i Dest:10.0.1.0/24 10.0.101.1

Step 8

Metric LocPrf Weight Path
100

0 i

show bgp vpnv4 flowspec all detail
This command displays the VPNv4 flowspec details.
Example:
Device# show bgp vpnv4 flowspec all detail
Route Distinguisher: 200:200
BGP routing table entry for 200:200:Dest:10.0.1.0/24, version 2
Paths: (1 available, best #1, table VPNv4-Flowspec-BGP-Table)
Advertised to update-groups:
3
Refresh Epoch 1
Local
10.0.101.1 (via default) from 10.0.101.1 (10.0.101.1)
Origin IGP, localpref 100, valid, internal, best
Extended Community: RT:100:100
rx pathid: 0, tx pathid: 0x0

IP Routing: BGP Configuration Guide
486


BGP FlowSpec Route-reflector Support
Configuration Examples for BGP FlowSpec Route-reflector Support

Step 9

show bgp vpnv6 flowspec
This command displays the VPNv6 flowspec neighbors.
Example:
Device# show bgp vpnv6 flowspec
BGP table version is 2, local router ID is 10.10.10.2 Status codes: s suppressed, d damped, h
history, * valid, > best, i - internal,
r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
x best-external, a additional-path, c RIB-compressed, Origin codes: i - IGP, e - EGP,
? - incomplete RPKI validation codes: V valid, I invalid, N Not found
Network
Next Hop
Route Distinguisher: 200:200
*>i SPort:=20640
FEC0::1001

Step 10

Metric LocPrf Weight Path
100

0 i

show bgp vpnv6 flowspec all detail
This command displays the VPNv6 flowspec details.
Example:
Device# show bgp vpnv6 flowspec all detail
Route Distinguisher: 200:200
BGP routing table entry for 200:200:SPort:=20640, version 2
Paths: (1 available, best #1, table VPNv6-Flowspec-BGP-Table)
Advertised to update-groups:
3
Refresh Epoch 1
Local
FEC0::1001 (via default) from FEC0::1001 (10.0.101.2)
Origin IGP, localpref 100, valid, internal, best
Extended Community: RT:100:100
rx pathid: 0, tx pathid: 0x0

Configuration Examples for BGP FlowSpec Route-reflector
Support
Example: BGP FlowSpec Route-reflector Support
Example: Configuring BGP FlowSpec on Route Reflector
Configure BGP route reflector and inject flowspec in the route reflector.

IP Routing: BGP Configuration Guide
487


BGP FlowSpec Route-reflector Support
Example: BGP FlowSpec Route-reflector Support

Figure 42: BGP Route Reflector Topology

! Configure the topology
!Configure the interfaces on RR
RR> enable
RR# configure terminal
RR(config)# interface E0/0
RR(config-if)# ip address 10.0.0.1 255.224.0.0
RR(config-if)# no shutdown
RR(config-if)# exit
RR(config)# interface S2/0
RR(config-if)# ip address 10.32.0.1 255.224.0.0
RR(config-if)# no shutdown
RR(config-if)# exit
RR(config)# interface S3/0
RR(config-if)# ip address 10.64.0.1 255.224.0.0
RR(config-if)# no shutdown
!Configure RR as the route reflector with S2/0(R1) and S2/0 (R2) as the neighbors
RR(config)# router bgp 333
RR(config-router)# no synchronization
RR(config-router)# network 10.0.0.0 mask 255.224.0.0
RR(config-router)# network 10.64.0.0 mask 255.224.0.0
RR(config-router)# network 10.32.0.0 mask 255.224.0.0
RR(config-router)# neighbor 10.64.0.2 remote-as 333
RR(config-router)# neighbor 10.32.0.2 remote-as 333

!Configure flowspec on route reflector
RR(config-router)# address-family ipv4 flowspec
RR(configure-router-af)# neighbor 10.64.0.2 activate
RR(config-router)# neighbor 10.64.0.2 route-reflector-client
RR(configure-router-af)# neighbor 10.32.0.2 activate
RR(config-router)# neighbor 10.32.0.2 route-reflector-client
!Verify the configuration
RR> show bgp ipv4 flowspec

IP Routing: BGP Configuration Guide
488


BGP FlowSpec Route-reflector Support
Additional References for BGP FlowSpec Route-reflector Support

Additional References for BGP FlowSpec Route-reflector
Support
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

Standards and RFCs
Standard/RFC Title
RFC 5575

Dissemination of Flow Specification Rules

Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/cisco/web/support/index.html
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies.
To receive security and technical information about
your products, you can subscribe to various services,
such as the Product Alert Tool (accessed from Field
Notices), the Cisco Technical Services Newsletter, and
Really Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website
requires a Cisco.com user ID and password.

Feature Information for BGP FlowSpec Route-reflector Support
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.

IP Routing: BGP Configuration Guide
489


BGP FlowSpec Route-reflector Support
Feature Information for BGP FlowSpec Route-reflector Support

Table 40: Feature Information for BGP FlowSpec Route-reflector Support

Feature Name

Releases

BGP FlowSpec
15.5(1)S
Route-reflector Support

Feature Information
The BGP FlowSpec Route-reflector Support feature enables
services providers to control traffic flows in their network and
mitigate DDoS attack.
The following command was introduced by this feature:
address-family {ipv4 | ipv6 | vpnv4 | vpnv6} flowspec.

BGP FlowSpec
Cisco IOS XE
Route-reflector Support Release 3.14

The BGP FlowSpec Route-reflector Support feature enables
services providers to control traffic flows in their network and
mitigate DDoS attack.
This feature was introduced on the Cisco ASR 1000 Series
Routers.
The following command was introduced by this feature:
address-family {ipv4 | ipv6 | vpnv4 | vpnv6} flowspec.

IP Routing: BGP Configuration Guide
490
