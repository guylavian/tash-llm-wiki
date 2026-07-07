---
title: "QoS Policy Propagation via BGP"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-qos-policy-propagation-via-bgp
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 17 QoS Policy Propagation via BGP The QoS Policy Propagation via BGP feature allows you to classify packets by IP precedence based on the Border Gateway Protocol (BGP) community lists, BGP autonomous system paths, and access lists. After packets have been classified, you can use other quality of service (QoS) features such as committed access rate (CAR) and Weighted Random Early Detectio"
---

# QoS Policy Propagation via BGP

CHAPTER

17

QoS Policy Propagation via BGP
The QoS Policy Propagation via BGP feature allows you to classify packets by IP precedence based on the
Border Gateway Protocol (BGP) community lists, BGP autonomous system paths, and access lists. After
packets have been classified, you can use other quality of service (QoS) features such as committed access
rate (CAR) and Weighted Random Early Detection (WRED) to specify and enforce policies to fit your business
model.
• Finding Feature Information, on page 177
• Prerequisites for QoS Policy Propagation via BGP, on page 177
• Information About QoS Policy Propagation via BGP, on page 178
• How to Configure QoS Policy Propagation via BGP, on page 178
• Configuration Examples for QoS Policy Propagation via BGP, on page 185
• Additional References, on page 187
• Feature Information for QoS Policy Propagation via BGP, on page 188

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Prerequisites for QoS Policy Propagation via BGP
• Enable the Border Gateway Protocol (BGP) and Cisco Express Forwarding (CEF) or distributed CEF
(dCEF) on the device. Subinterfaces on an ATM interface that have the bgp-policy command enabled
must use CEF mode because dCEF is not supported. dCEF uses the Versatile Interface Processor (VIP)
rather than the Route Switch Processor (RSP) to perform forwarding functions.
• Define the policy.
• Apply the policy through BGP.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
177


QoS Policy Propagation via BGP
Information About QoS Policy Propagation via BGP

• Configure the BGP community list, BGP autonomous system path, or access list and enable the policy
on an interface.
• Enable committed access rate (CAR) or Weighted Random Early Detection (WRED) to use the policy.

Information About QoS Policy Propagation via BGP
Benefits of QoS Policy Propagation via BGP
The QoS Policy Propagation via BGP feature allows you to classify packets by IP precedence based on Border
Gateway Protocol (BGP) community lists, BGP autonomous system paths, and access lists. After a packet
has been classified, you can use other quality of service (QoS) features such as committed access rate (CAR)
and Weighted Random Early Detection (WRED) to specify and enforce policies to fit your business model.

How to Configure QoS Policy Propagation via BGP
Configuring QoS Policy Propagation via BGP Based on Community Lists
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
route-map map-tag [permit | deny] [sequence-number] [
match community {standard-list-number | expanded-list-number | community-list-name [exact]}
set ip precedence [number | name]
exit
router bgp autonomous-system
table-map route-map-name
exit
ip community-list standard-list-number {permit | deny} [community-number]
interface type number
bgp-policy {source | destination} ip-prec-map
exit
ip bgp-community new-format
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

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
178


QoS Policy Propagation via BGP
Configuring QoS Policy Propagation via BGP Based on Community Lists

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. .
[
Example:
Device(config)# route-map alpha permit
ordering-seq

Step 4

match community {standard-list-number |
expanded-list-number | community-list-name [exact]}

Matches a Border Gateway Protocol (BGP) community
list.

Example:
Device(config-route-map)# match community 1

Step 5

set ip precedence [number | name]

Sets the IP Precedence field when the community list
matches.

Example:

Note
Device(config-route-map)# set ip precedence 5

Step 6

You can specify either a precedence number or
a precedence name.

Exits route-map configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-route-map)# exit

Step 7

Enables a BGP process and enters router configuration
mode.

router bgp autonomous-system
Example:
Device(config)# router bgp 45000

Step 8

Modifies the metric and tag values when the IP routing
table is updated with BGP learned routes.

table-map route-map-name
Example:
Device(config-router)# table-map rm1

Step 9

exit
Example:

Exits router configuration mode and returns to global
configuration mode.

Device(config-router)# exit

Step 10

ip community-list standard-list-number {permit | deny} Creates a community list for BGP and controls access to
it.
[community-number]
Example:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
179


QoS Policy Propagation via BGP
Configuring QoS Policy Propagation via BGP Based on the Autonomous System Path Attribute

Command or Action

Purpose

Device(config)# ip community-list 1 permit 2

Step 11

interface type number
Example:

Specifies the interface (or subinterface) and enters interface
configuration mode.

Device(config)# interface gigabitethernet 0/0/0

Step 12

bgp-policy {source | destination} ip-prec-map

Classifies packets using IP precedence.

Example:
Device(config-if)# bgp-policy source ip-prec-map

Step 13

Exits interface configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-if)# exit

Step 14

ip bgp-community new-format
Example:

(Optional) Displays the BGP community number in
AA:NN (autonomous system:community number/4-byte
number) format.

Device(config)# ip bgp-community new-format

Step 15

Exits global configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config)# end

Configuring QoS Policy Propagation via BGP Based on the Autonomous System
Path Attribute
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
named-ordering-route-map enable ]
route-map map-tag [permit | deny] [sequence-number] [ ordering-seq sequence-name
match as-path path-list-number
set ip precedence [number | name]
exit
router bgp autonomous-system
table-map route-map-name
exit
ip as-path access-list access-list-number {permit | deny} as-regular-expression
interface type number

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
180


QoS Policy Propagation via BGP
Configuring QoS Policy Propagation via BGP Based on the Autonomous System Path Attribute

13.
14.

bgp-policy {source | destination} ip-prec-map
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

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

named-ordering-route-map enable ]
Example:

Enables ordering of route-maps based on a string provided
by the user.

Device(config)# named-ordering-route-map enable

Step 4

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. ordering-seq indicates the sequence that
[ ordering-seq sequence-name
is to be used for ordering of route-maps.
Example:
Device(config)# route-map alpha permit
ordering-seq sequence1

Step 5

Matches a Border Gateway Protocol (BGP) autonomous
system path access list.

match as-path path-list-number
Example:
Device(config-route-map)# match as-path 2

Step 6

set ip precedence [number | name]

Sets the IP Precedence field when the autonomous-system
path matches.

Example:

Step 7

You can specify either a precedence number or
a precedence name.

Device(config-route-map)# set ip precedence 5

Note

exit

Exits route-map configuration mode and returns to global
configuration mode.

Example:
Device(config-route-map)# exit

Step 8

Enables a BGP process and enters router configuration
mode.

router bgp autonomous-system
Example:
Device(config)# router bgp 45000

Step 9

table-map route-map-name
Example:

Modifies the metric and tag values when the IP routing
table is updated with BGP learned routes.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
181


QoS Policy Propagation via BGP
Configuring QoS Policy Propagation via BGP Based on an Access List

Command or Action

Purpose

Device(config-router)# table-map rm1

Step 10

Exits router configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-router)# exit

Step 11

ip as-path access-list access-list-number {permit | deny} Defines an autonomous system path access list.
as-regular-expression
Example:
Device(config)# ip as-path access-list 500 permit
45000

Step 12

interface type number
Example:

Specifies the interface (or subinterface) and enters interface
configuration mode.

Device(config)# interface gigabitethernet 0/0/0

Step 13

bgp-policy {source | destination} ip-prec-map

Classifies packets using IP precedence.

Example:
Device(config-if)# bgp-policy source ip-prec-map

Step 14

Exits interface configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-if)# end

Configuring QoS Policy Propagation via BGP Based on an Access List
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
named-ordering-route-map enable ]
route-map map-tag [permit | deny] [sequence-number] [ ordering-seq sequence-name
match ip address access-list-number
set ip precedence [number | name]
exit
router bgp autonomous-system
table-map route-map-name
exit
access-list access-list-number {permit | deny} source
interface type number
bgp-policy {source | destination} ip-prec-map
end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
182


QoS Policy Propagation via BGP
Configuring QoS Policy Propagation via BGP Based on an Access List

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

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

named-ordering-route-map enable ]
Example:

Enables ordering of route-maps based on a string provided
by the user.

Device(config)# named-ordering-route-map enable

Step 4

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. ordering-seq indicates the sequence that
[ ordering-seq sequence-name
is to be used for ordering of route-maps.
Example:
Device(config)# route-map alpha permit
ordering-seq sequence1

Step 5

match ip address access-list-number

Matches an access list.

Example:
Device(config-route-map)# match ip address 69

Step 6

set ip precedence [number | name]

Sets the IP precedence field when the autonomous system
path matches.

Example:
Device(config-route-map)# set ip precedence
routine

Step 7

Exits route-map configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-route-map)# exit

Step 8

Enables a Border Gateway Protocol (BGP) process and
enters router configuration mode.

router bgp autonomous-system
Example:
Device(config)# router bgp 45000

Step 9

Modifies the metric and tag values when the IP routing
table is updated with BGP learned routes.

table-map route-map-name
Example:
Device(config-router)# table-map rm1

Step 10

exit
Example:

Exits router configuration mode and returns to global
configuration mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
183


QoS Policy Propagation via BGP
Monitoring QoS Policy Propagation via BGP

Command or Action

Purpose

Device(config-router)# exit

Step 11

access-list access-list-number {permit | deny} source

Defines an access list.

Example:
Device(config)# access-list 69 permit 10.69.0.0

Step 12

interface type number
Example:

Specifies the interfaces (or subinterface) and enters
interface configuration mode.

Device(config)# interface gigabitethernet 0/0/0

Step 13

bgp-policy {source | destination} ip-prec-map

Classifies packets using IP Precedence.

Example:
Device(config-if)# bgp-policy source ip-prec-map

Step 14

Exits interface configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-if)# end

Monitoring QoS Policy Propagation via BGP
To monitor the QoS Policy Propagation via the BGP feature configuration, use the following optional
commands.
Command or Action

Purpose

show ip bgp

Displays entries in the Border
Gateway Protocol (BGP)
routing table to verify whether
the correct community is set on
the prefixes.

show ip bgp community-list community-list-number

Displays routes permitted by the
BGP community to verify
whether correct prefixes are
selected.

show ip cef network

Displays entries in the
forwarding information base
(FIB) table based on the
specified IP address to verify
whether Cisco Express
Forwarding has the correct
precedence value for the prefix.

show ip interface

Displays information about the
interface.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
184


QoS Policy Propagation via BGP
Configuration Examples for QoS Policy Propagation via BGP

Command or Action

Purpose

show ip route prefix

Displays the current status of
the routing table to verify
whether correct precedence
values are set on the prefixes.

Configuration Examples for QoS Policy Propagation via BGP
Example: Configuring QoS Policy Propagation via BGP
The following example shows how to create route maps to match access lists, Border Gateway Protocol (BGP)
community lists, and BGP autonomous system paths, and apply IP precedence to routes learned from neighbors.
In the figure below, Device A learns routes from autonomous system 10 and autonomous system 60. The
quality of service (QoS) policy is applied to all packets that match defined route maps. Any packets from
Device A to autonomous system 10 or autonomous system 60 are sent the appropriate QoS policy, as the
numbered steps in the figure indicate.
Figure 8: Device Learning Routes and Applying QoS Policy

Device A Configuration
interface serial 5/0/0/1:0
ip address 10.28.38.2 255.255.255.0
bgp-policy destination ip-prec-map
no ip mroute-cache
no cdp enable
frame-relay interface-dlci 20 IETF
router bgp 30
table-map precedence-map
neighbor 10.20.20.1 remote-as 10
neighbor 10.20.20.1 send-community
!
ip bgp-community new-format
!
! Match community 1 and set the IP precedence to priority
route-map precedence-map permit 10
match community 1
set ip precedence priority
!
! Match community 2 and set the IP precedence to immediate
route-map precedence-map permit 20

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
185


QoS Policy Propagation via BGP
Example: Configuring QoS Policy Propagation via BGP

match community 2
set ip precedence immediate
!
! Match community 3 and set the IP precedence to flash
route-map precedence-map permit 30
match community 3
set ip precedence flash
!
! Match community 4 and set the IP precedence to flash-override
route-map precedence-map permit 40
match community 4
set ip precedence flash-override
!
! Match community 5 and set the IP precedence to critical
route-map precedence-map permit 50
match community 5
set ip precedence critical
!
! Match community 6 and set the IP precedence to internet
route-map precedence-map permit 60
match community 6
set ip precedence internet
!
! Match community 7 and set the IP precedence to network
route-map precedence-map permit 70
match community 7
set ip precedence network
!
! Match ip address access list 69 or match autonomous system path 1
! and set the IP precedence to critical
route-map precedence-map permit 75
match ip address 69
match as-path 1
set ip precedence critical
!
! For everything else, set the IP precedence to routine
route-map precedence-map permit 80
set ip precedence routine
!
! Define community lists
ip community-list 1 permit 60:1
ip community-list 2 permit 60:2
ip community-list 3 permit 60:3
ip community-list 4 permit 60:4
ip community-list 5 permit 60:5
ip community-list 6 permit 60:6
ip community-list 7 permit 60:7
!
! Define the AS path
ip as-path access-list 1 permit ^10_60
!
! Define the access list
access-list 69 permit 10.69.0.0

Device B Configuration
router bgp 10
neighbor 10.30.30.1 remote-as 30
neighbor 10.30.30.1 send-community
neighbor 10.30.30.1 route-map send_community out
!
ip bgp-community new-format
!

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
186


QoS Policy Propagation via BGP
Additional References

! Match prefix 10 and set community to 60:1
route-map send_community permit 10
match ip address 10
set community 60:1
!
! Match prefix 20 and set community to 60:2
route-map send_community permit 20
match ip address 20
set community 60:2
!
! Match prefix 30 and set community to 60:3
route-map send_community permit 30
match ip address 30
set community 60:3
!
! Match prefix 40 and set community to 60:4
route-map send_community permit 40
match ip address 40
set community 60:4
!
! Match prefix 50 and set community to 60:5
route-map send_community permit 50
match ip address 50
set community 60:5
!
! Match prefix 60 and set community to 60:6
route-map send_community permit 60
match ip address 60
set community 60:6
!
! Match prefix 70 and set community to 60:7
route-map send_community permit 70
match ip address 70
set community 60:7
!
! For all others, set community to 60:8
route-map send_community permit 80
set community 60:8
!
! Define access lists
access-list 10 permit 10.61.0.0
access-list 20 permit 10.62.0.0
access-list 30 permit 10.63.0.0
access-list 40 permit 10.64.0.0
access-list 50 permit 10.65.0.0
access-list 60 permit 10.66.0.0
access-list 70 permit 10.67.0.0

Additional References
Related Documents
Related Topic

Document Title

IP routing protocol-independent commands

Cisco IOS IP Routing:
Protocol-Independent Command
Reference

BGP configuration

BGP Configuration Guide

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
187


QoS Policy Propagation via BGP
Feature Information for QoS Policy Propagation via BGP

Related Topic

Document Title

Cisco Express Forwarding configuration

Cisco Express Forwarding
Configuration Guide

Committed access rate configuration

“Configuring Committed Access
Rate” module in the QoS:
Classification Configuration Guide
(part of the Quality of Service
Solutions Configuration Guide
Library)

Weighted Random Early Detection configuration

“Configuring Weighted Random
Early Detection” module in the
QoS: Congestion Avoidance
Configuration Guide (part of the
Quality of Service Solutions
Configuration Guide Library)

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

Feature Information for QoS Policy Propagation via BGP
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
188


QoS Policy Propagation via BGP
Feature Information for QoS Policy Propagation via BGP

Table 18: Feature Information for QoS Policy Propagation via BGP

Feature Name

Releases

Feature Information

QoS Policy Propagation via BGP

The QoS Policy Propagation via
BGP feature allows you to classify
packets by IP precedence based on
Border Gateway Protocol (BGP)
community lists, BGP autonomous
system paths, and access lists. After
a packet has been classified, you
can use other quality of service
(QoS) features such as committed
access rate (CAR) and Weighted
Random Early Detection (WRED)
to specify and enforce policies to
fit your business model.

Policy Routing Infrastructure

The Policy Routing Infrastructure
feature provides full support of IP
policy-based routing with Cisco
Express Forwarding (CEF). As
CEF gradually obsoletes fast
switching, policy routing is
integrated with CEF to increase
customer performance
requirements. When policy routing
is enabled, redundant processing is
avoided.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
189


QoS Policy Propagation via BGP
Feature Information for QoS Policy Propagation via BGP

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
190
