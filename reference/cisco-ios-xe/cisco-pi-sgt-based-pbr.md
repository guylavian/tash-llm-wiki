---
title: "SGT Based PBR"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-sgt-based-pbr
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 13 SGT Based PBR The SGT Based PBR feature supports classification of packets based on Security Group for grouping the traffic into roles to match the defined policies in Policy-Based Routing (PBR). • Finding Feature Information, on page 143 • Restrictions for SGT Based PBR, on page 143 • Information About SGT Based PBR, on page 144 • How to Configure SGT Based PBR, on page 144 • Configu"
---

# SGT Based PBR

CHAPTER

13

SGT Based PBR
The SGT Based PBR feature supports classification of packets based on Security Group for grouping the
traffic into roles to match the defined policies in Policy-Based Routing (PBR).
• Finding Feature Information, on page 143
• Restrictions for SGT Based PBR, on page 143
• Information About SGT Based PBR, on page 144
• How to Configure SGT Based PBR, on page 144
• Configuration Examples for SGT Based PBR, on page 147
• Additional References for SGT Based PBR, on page 148
• Feature Information for SGT Based PBR, on page 148

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Restrictions for SGT Based PBR
• SGT Based PBR feature supports policy configuration using number based tagging and does not support
name based tagging.
• SGT Based PBR feature is not supported for IPV6 traffic on IOS XE.
• Dynamic route-map overrides static route-map when both are associated with the same interface. A
warning message is issued during an override. The static route-map is enabled when the dynamic route-map
is deleted.
• We recommend disassociating the route-map before it is deleted. You cannot configure static PBR if the
route-map is deleted before disassociating it from the interface.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
143


SGT Based PBR
Information About SGT Based PBR

Information About SGT Based PBR
Cisco TrustSec
Cisco TrustSec assigns a Security Group Tag, (SGT) to the user’s or device’s traffic at ingress and applies
the access policy based on the assigned tag. SGT Based PBR feature allows you to configure PBR based on
Security Group classification enabling you to group users or devices into a role to match the defined policies.

SGT Based PBR
Security Group classification includes both Source and Destination Group, which is specified by source SGT
and DGT. SGT Based PBR feature provides the PBR route-map match clause for SGT/DGT based packet
classification. SGT Based PBR feature supports configuration of unlimited number of tags, but it is
recommended to configure the tags based on memory available in the platform. SGT Based PBR supports
VPN routing and forwarding (VRF) selection match criteria which can be used for policy based classification
and forwarding of Virtual Private Network (VPN) traffic.

How to Configure SGT Based PBR
Configuring Match Security Group Tag
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
route-map map-tag
match security-group source tag sgt-number
set ip next-hop ip-address
match security-group destination tag sgt-number
set ip next-hop ip-address
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

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
144


SGT Based PBR
Assigning Route-Map to an Interface

Step 3

Command or Action

Purpose

route-map map-tag

Specifies the route-map and enters route-map configuration
mode.

Example:
Device(config)# route-map policy_security

Step 4

match security-group source tag sgt-number

Configures the value for security-group source security tag.

Example:
Device(config-route-map)# match security-group
source tag 100

Step 5

Specifies the next hop for routing packets.

set ip next-hop ip-address
Example:
Device(config-route-map)# set ip next-hop
71.71.71.6

Step 6

match security-group destination tag sgt-number
Example:

Configures the value for security-group destination security
tag.

Device(config-route-map)# match security-group
destination tag 150

Step 7

Specifies the next hop for routing packets.

set ip next-hop ip-address
Example:
Device(config-route-map)# set ip next-hop
72.72.72.6

Step 8

Exits route-map configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-route-map)# end

Assigning Route-Map to an Interface
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
interface typeslot/ subslot/ port[. subinterface-number]
ip policy route-map map-tag

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
145


SGT Based PBR
Displaying and Verifying SGT Based PBR Configuration

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

interface typeslot/ subslot/ port[. subinterface-number]
Example:

Specifies the interface information and enters interface
configuration mode.

Device(config)#interface gigabitEthernet0/0/0

Step 4

ip policy route-map map-tag
Example:

Assigns the route-map configured in the previous task to
the interface.

Device(config-if)#ip policy route-map
policy_security

Displaying and Verifying SGT Based PBR Configuration
SUMMARY STEPS
1.
2.
3.
4.

enable
show ip policy
show route-map map-tag
show route-map dynamic

DETAILED STEPS

Step 1

enable
Example:
Device> enable

Enables privileged EXEC mode.
• Enter your password if prompted.
Step 2

show ip policy
Example:
Device# show ip policy
Interface
Gi0/0/1.77

Route map
test

Displays IP policy information.
Step 3

show route-map map-tag
Example:
Device# show route-map test
route-map test, permit, sequence 10

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
146


SGT Based PBR
Configuration Examples for SGT Based PBR

Match clauses:
security-group source tag 100 111
Set clauses:
ip next-hop 71.71.71.6
Policy routing matches: 0 packets, 0 bytes
route-map test, permit, sequence 20
Match clauses:
security-group destination tag 200 222
Set clauses:
ip next-hop 72.72.72.6
Policy routing matches: 0 packets, 0 bytes

Displays route-map configuration.
Step 4

show route-map dynamic
Example:
Device# show route-map dynamic
route-map AAA-02/11/15-12:32:52.955-1-test, permit, sequence 0, identifier 2818572289
Match clauses:
Security-group source tag 100 300
Set clauses:
ip next-hop 3.3.3.2
Nexthop tracking current: 3.3.3.2
3.3.3.2, fib_nh:7FDE41661370,oce:7FDE4C540AD0,status:1
Policy routing matches: 1012 packets, 83458 bytes
Current active dynamic routemaps = 1

Displays information about dynamic PBR route-map.

Configuration Examples for SGT Based PBR
Example: SGT Based PBR
The following example shows how to configure SGT Based PBR:
Example: SGT Based PBR
enable
configure terminal
route-map policy_security
match security-group source tag 100
match security-group source tag 111
set ip next-hop 71.71.71.6
match security-group destination tag 200
match security-group destination tag 222
set ip next-hop 72.72.72.6
end
interface gigabitEthernet0/0/0
ip policy route-map policy_security

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
147


SGT Based PBR
Additional References for SGT Based PBR

Additional References for SGT Based PBR
Related Documents
Related Topic

Document Title

Cisco IOS IP Routing Protocol Independent
commands

Cisco IOS IP Routing Protocol Independent Command
Reference

Cisco TrustSec Overview

Understanding Cisco TrustSec

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

Feature Information for SGT Based PBR
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
148


SGT Based PBR
Feature Information for SGT Based PBR

Table 14: Feature Information for SGT Based PBR

Feature Name

Releases Feature Information

SGT Based PBR

This feature is supported on Cisco 4000 Series ISRs.

SGT Based
PBR

The SGT Based PBR feature supports classification of packets based on Security
Group Tag (SGT) for grouping the traffic into roles to match the defined policies
in PBR.
The following commands were introduced or modified: interface, ip policy
route-map, match security-group destination tag, match security-group
source tag, route-map, show ip policy, show route-map, show route-map
dynamic, show platform hardware qfp active classification
class-group-manager class-group client pbr, show platform hardware qfp
active classification feature-manager class-group tcam pbr global details,
match security-group source tag, show platform hardware qfp active feature
pbr class-group, show platform software pbr fp interface all, show platform
software pbr rp ac statistics, show platform software route-map fp active
map, show platform software route-map rp active map.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
149


SGT Based PBR
Feature Information for SGT Based PBR

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
150
