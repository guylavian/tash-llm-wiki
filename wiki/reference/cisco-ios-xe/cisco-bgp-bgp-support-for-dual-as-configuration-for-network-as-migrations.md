---
title: "BGP Support for Dual AS Configuration for Network AS Migrations"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-dual-as-configuration-for-network-as-migrations
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 21 BGP Support for Dual AS Configuration for Network AS Migrations The BGP Support for Dual AS Configuration for Network AS Migrations feature extended the functionality of the BGP Local-AS feature by providing additional autonomous system path customization configuration options. The configuration of this feature is transparent to customer peering sessions, allowing the provider to merg"
---

# BGP Support for Dual AS Configuration for Network AS Migrations

CHAPTER

21

BGP Support for Dual AS Configuration for
Network AS Migrations
The BGP Support for Dual AS Configuration for Network AS Migrations feature extended the functionality
of the BGP Local-AS feature by providing additional autonomous system path customization configuration
options. The configuration of this feature is transparent to customer peering sessions, allowing the provider
to merge two autonomous systems without interrupting customer peering arrangements. Customer peering
sessions can later be updated during a maintenance window or during other scheduled downtime.
• Finding Feature Information, on page 443
• Information About BGP Support for Dual AS Configuration for Network AS Migrations, on page 443
• How to Configure BGP Support for Dual AS Configuration for Network AS Migrations, on page 445
• Configuration Examples for Dual-AS Peering for Network Migration, on page 447
• Additional References, on page 449
• Feature Information for BGP Support for Dual AS Configuration for Network AS Migrations, on page
449

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Support for Dual AS Configuration for
Network AS Migrations
Autonomous System Migration for BGP Networks
Autonomous system migration can be necessary when a telecommunications or Internet service provider
purchases another network. It is desirable for the provider to be able to integrate the second autonomous

IP Routing: BGP Configuration Guide
443


BGP Support for Dual AS Configuration for Network AS Migrations
Dual Autonomous System Support for BGP Network Autonomous System Migration

system without disrupting existing customer peering arrangements. The amount of configuration required in
the customer networks can make this a cumbersome task that is difficult to complete without disrupting service.

Dual Autonomous System Support for BGP Network Autonomous System
Migration
In Cisco IOS Release 12.0(29)S, 12.3(14)T, 12.2(33)SXH, and later releases, support was added for dual BGP
autonomous system configuration to allow a secondary autonomous system to merge under a primary
autonomous system, without disrupting customer peering sessions. The configuration of this feature is
transparent to customer networks. Dual BGP autonomous system configuration allows a router to appear, to
external peers, as a member of secondary autonomous system during the autonomous system migration. This
feature allows the network operator to merge the autonomous systems and then later migrate customers to
new configurations during normal service windows without disrupting existing peering arrangements.
The neighbor local-as command is used to customize the AS_PATH attribute by adding and removing
autonomous system numbers for routes received from eBGP neighbors. This feature allows a router to appear
to external peers as a member of another autonomous system for the purpose of autonomous system number
migration. This feature simplifies this process of changing the autonomous system number in a BGP network
by allowing the network operator to merge a secondary autonomous system into a primary autonomous system
and then later update the customer configurations during normal service windows without disrupting existing
peering arrangements.
BGP Autonomous System Migration Support for Confederations, Individual Peering Sessions, and Peer
Groupings
This feature supports confederations, individual peering sessions, and configurations applied through peer
groups and peer templates. If this feature is applied to group peers, the individual peers cannot be customized.
Ingress Filtering During BGP Autonomous System Migration
Autonomous system path customization increases the possibility that routing loops can be created if such
customization is misconfigured. The larger the number of customer peerings, the greater the risk. You can
minimize this possibility by applying policies on the ingress interfaces to block the autonomous system number
that is in transition or routes that have no local-as configuration.

Caution

BGP prepends the autonomous system number from each BGP network that a route traverses to maintain
network reachability information and to prevent routing loops. This feature should be configured only for
autonomous system migration and should be deconfigured after the transition has been completed. This
procedure should be attempted only by an experienced network operator, as routing loops can be created with
improper configuration.

BGP Network Migration to 4-Byte Autonomous System Numbers
The BGP Support for 4-Byte ASN feature introduced support for 4-byte autonomous system numbers. Because
of increased demand for autonomous system numbers, in January 2009 the IANA started to allocate 4-byte
autonomous system numbers in the range from 65536 to 4294967295.
The Cisco implementation of 4-byte autonomous system numbers supports RFC 4893. RFC 4893 was developed
to allow BGP to support a gradual transition from 2-byte autonomous system numbers to 4-byte autonomous

IP Routing: BGP Configuration Guide
444


BGP Support for Dual AS Configuration for Network AS Migrations
How to Configure BGP Support for Dual AS Configuration for Network AS Migrations

system numbers. A new reserved (private) autonomous system number, 23456, was created by RFC 4893 and
this number cannot be configured as an autonomous system number in the Cisco IOS CLI.
Migrating your BGP network to 4-byte autonomous system numbers requires some planning. If you are
upgrading to an image that supports 4-byte autonomous system numbers, you can still use 2-byte autonomous
system numbers. The show command output and regular expression match are not changed and remain in
asplain (decimal value) format for 2-byte autonomous system numbers regardless of the format configured
for 4-byte autonomous system numbers.
To ensure a smooth transition, we recommend that all BGP speakers within an autonomous system that is
identified using a 4-byte autonomous system number be upgraded to support 4-byte autonomous system
numbers.
For details about steps to perform to upgrade a BGP network to full 4-byte autonomous system support, see
the Migration Guide for Explaining 4-Byte Autonomous System white paper.

How to Configure BGP Support for Dual AS Configuration for
Network AS Migrations
Configuring Dual AS Peering for Network Migration
Perform this task to configure a BGP peer router to appear to external peers as a member of another autonomous
system for the purpose of autonomous system number migration. When the BGP peer is configured with dual
autonomous system numbers then the network operator can merge a secondary autonomous system into a
primary autonomous system and update the customer configuration during a future service window without
disrupting existing peering arrangements.
The show ip bgp and show ip bgp neighbors commands can be used to verify autonomous system number
for entries in the routing table and the status of this feature.

Note

• The BGP Support for Dual AS Configuration for Network AS Migrations feature can be configured for
only true eBGP peering sessions. This feature cannot be configured for two peers in different
subautonomous systems of a confederation.
• The BGP Support for Dual AS Configuration for Network AS Migrations feature can be configured for
individual peering sessions and configurations applied through peer groups and peer templates. If this
command is applied to a peer group, the peers cannot be individually customized.

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
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address local-as [autonomous-system-number [no-prepend [replace-as [dual-as]]]]
neighbor ip-address remove-private-as
end

IP Routing: BGP Configuration Guide
445


BGP Support for Dual AS Configuration for Network AS Migrations
Configuring Dual AS Peering for Network Migration

8. show ip bgp [network] [network-mask] [longer-prefixes] [prefix-list prefix-list-name | route-map
route-map-name] [shorter-prefixes mask-length]
9. show ip bgp neighbors [neighbor-address] [received-routes | routes | advertised-routes | paths regexp
| dampened-routes | received prefix-filter]
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

Enters router configuration mode, and creates a BGP routing
process.

Router(config)# router bgp 40000

Step 4

neighbor ip-address remote-as
autonomous-system-number

Establishes a peering session with a BGP neighbor.

Example:
Router(config-router)# neighbor 10.0.0.1 remote-as
45000

Step 5

neighbor ip-address local-as
[autonomous-system-number [no-prepend [replace-as
[dual-as]]]]
Example:
Router(config-router)# neighbor 10.0.0.1 local-as
50000 no-prepend replace-as dual-as

Customizes the AS_PATH attribute for routes received
from an eBGP neighbor.
• The replace-as keyword is used to prepend only the
local autonomous system number (as configured with
the ip-address argument) to the AS_PATH attribute.
The autonomous system number from the local BGP
routing process is not prepended.
• The dual-as keyword is used to configure the eBGP
neighbor to establish a peering session using the real
autonomous-system number (from the local BGP
routing process) or by using the autonomous system
number configured with the ip-address argument
(local-as).
• The example configures the peering session with the
10.0.0.1 neighbor to accept the real autonomous system
number and the local-as number.

IP Routing: BGP Configuration Guide
446


BGP Support for Dual AS Configuration for Network AS Migrations
Configuration Examples for Dual-AS Peering for Network Migration

Command or Action
Step 6

neighbor ip-address

Purpose
remove-private-as

Example:
Router(config-router)# neighbor 10.0.0.1
remove-private-as

(Optional) Removes private autonomous system numbers
from outbound routing updates.
• This command can be used with the replace-as
functionality to remove the private autonomous system
number and replace it with an external autonomous
system number.
• Private autonomous system numbers (64512 to 65535)
are automatically removed from the AS_PATH
attribute when this command is configured.

Step 7

Exits router configuration mode and enters privileged EXEC
mode.

end
Example:
Router(config-router)# end

Step 8

show ip bgp [network] [network-mask] [longer-prefixes] Displays entries in the BGP routing table.
[prefix-list prefix-list-name | route-map route-map-name]
• The output can be used to verify if the real autonomous
[shorter-prefixes mask-length]
system number or local-as number is configured.
Example:
Router# show ip bgp

Step 9

Displays information about TCP and BGP connections to
show ip bgp neighbors [neighbor-address]
[received-routes | routes | advertised-routes | paths regexp neighbors.
| dampened-routes | received prefix-filter]
• The output will display local AS, no-prepend,
replace-as, and dual-as with the corresponding
Example:
autonomous system number when these options are
Router# show ip bgp neighbors
configured.

Configuration Examples for Dual-AS Peering for Network
Migration
Example: Dual AS Configuration
The following examples shows how this feature is used to merge two autonomous systems without interrupting
peering arrangements with the customer network. The neighbor local-as command is configured to allow
Router 1 to maintain peering sessions through autonomous system 40000 and autonomous system 45000.
Router 2 is a customer router that runs a BGP routing process in autonomous system 50000 and is configured
to peer with autonomous-system 45000.

IP Routing: BGP Configuration Guide
447


BGP Support for Dual AS Configuration for Network AS Migrations
Example: Dual AS Confederation Configuration

Router 1 in Autonomous System 40000 (Provider Network)
interface Serial3/0
ip address 10.3.3.11 255.255.255.0
!
router bgp 40000
no synchronization
bgp router-id 10.0.0.11
neighbor 10.3.3.33 remote-as 50000
neighbor 10.3.3.33 local-as 45000 no-prepend replace-as dual-as

Router 1 in Autonomous System 45000 (Provider Network)
interface Serial3/0
ip address 10.3.3.11 255.255.255.0
!
router bgp 45000
bgp router-id 10.0.0.11
neighbor 10.3.3.33 remote-as 50000

Router 2 in Autonomous System 50000 (Customer Network)
interface Serial3/0
ip address 10.3.3.33 255.255.255.0
!
router bgp 50000
bgp router-id 10.0.0.3
neighbor 10.3.3.11 remote-as 45000

After the transition is complete, the configuration on router 50000 can be updated to peer with autonomous
system 40000 during a normal maintenance window or during other scheduled downtime:
neighbor 10.3.3.11 remote-as 100

Example: Dual AS Confederation Configuration
The following example can be used in place of the Router 1 configuration in the "Example: Dual AS
Configuration" example. The only difference between these configurations is that Router 1 is configured to
be part of a confederation.
interface Serial3/0/0
ip address 10.3.3.11 255.255.255.0
!
router bgp 65534
no synchronization
bgp confederation identifier 100
bgp router-id 10.0.0.11
neighbor 10.3.3.33 remote-as 50000
neighbor 10.3.3.33 local-as 45000 no-prepend replace-as dual-as

Example: Replace an AS with Another AS in Routing Updates
The following example strips private autonomous system 64512 from outbound routing updates for the
10.3.3.33 neighbor and replaces it with autonomous system 50000:

IP Routing: BGP Configuration Guide
448


BGP Support for Dual AS Configuration for Network AS Migrations
Additional References

router bgp 64512
neighbor 10.3.3.33 local-as 50000 no-prepend replace-as

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

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

Feature Information for BGP Support for Dual AS Configuration
for Network AS Migrations
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.

IP Routing: BGP Configuration Guide
449


BGP Support for Dual AS Configuration for Network AS Migrations
Feature Information for BGP Support for Dual AS Configuration for Network AS Migrations

Table 37: Feature Information for BGP Support for Dual AS Configuration for Network AS Migrations

Feature Name

Releases

Feature Information

BGP Support for Dual AS
Configuration for Network AS
Migrations

12.2(33)SRA

The BGP Support for Dual AS
Configuration for Network AS
Migrations feature extended the
functionality of the BGP Local-AS
feature by providing additional
autonomous system path
customization configuration
options. The configuration of this
feature is transparent to customer
peering sessions, allowing the
provider to merge two autonomous
systems without interrupting
customer peering arrangements.
Customer peering sessions can later
be updated during a maintenance
window or during other scheduled
downtime.

Cisco IOS XE Release 2.1

This feature was introduced on the
Cisco ASR 1000 Series Routers.
The following command was
modified by this feature: neighbor
local-as.

IP Routing: BGP Configuration Guide
450
