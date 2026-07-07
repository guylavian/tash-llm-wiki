---
title: "BGP per Neighbor SoO Configuration"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-per-neighbor-soo-configuration
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 40 BGP per Neighbor SoO Configuration The BGP per Neighbor SoO Configuration feature simplifies the configuration of the site-of-origin (SoO) value. Per neighbor SoO configuration introduces two new commands that can be configured in submodes under router configuration mode to set the SoO value. • Finding Feature Information, on page 647 • Prerequisites for BGP per Neighbor SoO Configura"
---

# BGP per Neighbor SoO Configuration

CHAPTER

40

BGP per Neighbor SoO Configuration
The BGP per Neighbor SoO Configuration feature simplifies the configuration of the site-of-origin (SoO)
value. Per neighbor SoO configuration introduces two new commands that can be configured in submodes
under router configuration mode to set the SoO value.
• Finding Feature Information, on page 647
• Prerequisites for BGP per Neighbor SoO Configuration, on page 647
• Restrictions for BGP per Neighbor SoO Configuration, on page 647
• Information About Configuring BGP per Neighbor SoO, on page 648
• How to Configure BGP per Neighbor SoO, on page 650
• Configuration Examples for BGP per Neighbor SoO Configuration, on page 659
• Where to Go Next, on page 661
• Additional References, on page 661
• Feature Information for BGP per Neighbor SoO Configuration, on page 662

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP per Neighbor SoO Configuration
This feature assumes that a Border Gateway Protocol (BGP) network is configured and that Cisco Express
Forwarding is enabled in your network.

Restrictions for BGP per Neighbor SoO Configuration
A BGP neighbor or peer policy template-based SoO configuration takes precedence over the SoO value
configured in an inbound route map.

IP Routing: BGP Configuration Guide
647


BGP per Neighbor SoO Configuration
Information About Configuring BGP per Neighbor SoO

Information About Configuring BGP per Neighbor SoO
Site of Origin BGP Community Attribute
The site-of-origin (SoO) extended community is a BGP extended community attribute that is used to identify
routes that have originated from a site so that the readvertisement of that prefix back to the source site can be
prevented. The SoO extended community uniquely identifies the site from which a router has learned a route.
BGP can use the SoO value associated with a route to prevent routing loops.

Route Distinguisher
A route distinguisher (RD) creates routing and forwarding tables and specifies the default route distinguisher
for a VPN. The RD is added to the beginning of an IPv4 prefix to change it into a globally unique VPN-IPv4
prefix. An RD can be composed in one of two ways: with an autonomous system number and an arbitrary
number or with an IP address and an arbitrary number.
You can enter an RD in either of these formats:
• Enter a 16-bit autonomous system number, a colon, and a 32-bit number. For example:
45000:3
• Enter a 32-bit IP address, a colon, and a 16-bit number. For example:
192.168.10.15:1

BGP per Neighbor Site of Origin Configuration
There are three ways to configure an SoO value for a BGP neighbor:
• BGP peer policy template--A peer policy template is created, and an SoO value is configured as part of
the peer policy. Under address family IPv4 VRF, a neighbor is identified and is configured to inherit the
peer policy that contains the SoO value.
• BGP neighbor command--Under address family IPv4 VRF, a neighbor is identified, and an SoO value
is configured for the neighbor.
• BGP peer group--Under address family IPv4 VRF, a BGP peer group is configured, an SoO value is
configured for the peer group, a neighbor is identified, and the neighbor is configured as a member of
the peer group.

Note

A BGP neighbor or peer policy template-based SoO configuration takes precedence over the SoO value
configured in an inbound route map.
The configuration of SoO values for BGP neighbors is performed on a provider edge (PE) router, which is
the VPN entry point. When SoO is enabled, the PE router forwards prefixes to the customer premises equipment
(CPE) only when the SoO tag of the prefix does not match the SoO tag configured for the CPE.

IP Routing: BGP Configuration Guide
648


BGP per Neighbor SoO Configuration
Benefits of BGP per Neighbor Site of Origin

For example, in the figure below, an SoO tag is set as 65000:1 for the customer site that includes routers CPE1
and CPE2 with an autonomous system number of 65000. When CPE1 sends prefixes to PE1, PE1 tags the
prefixes with 65000:1, which is the SoO tag for CPE1 and CPE2. When PE1 sends the tagged prefixes to
PE2, PE2 performs a match against the SoO tag from CPE2. Any prefixes with the tag value of 65000:1 are
not sent to CPE2 because the SoO tag matches the SoO tag of CPE2, and a routing loop is avoided.
Figure 62: Network Diagram for SoO Example

Benefits of BGP per Neighbor Site of Origin
In releases prior to the introduction of this feature, the SoO extended community attribute is configured using
an inbound route map that sets the SoO value during the update process. With the introduction of the BGP
per Neighbor Site of Origin feature, two new commands configured in submodes under router configuration
mode simplify the SoO value configuration.

BGP Peer Policy Templates
Peer policy templates are used to configure BGP policy commands that are configured for neighbors that
belong to specific address families. Peer policy templates are configured once and then applied to many
neighbors through the direct application of a peer policy template or through inheritance from peer policy
templates. The configuration of peer policy templates simplifies the configuration of BGP policy commands
that are applied to all neighbors within an autonomous system.
Peer policy templates support inheritance. A directly applied peer policy template can directly or indirectly
inherit configurations from up to seven peer policy templates. So, a total of eight peer policy templates can
be applied to a neighbor or neighbor group.
The configuration of peer policy templates simplifies and improves the flexibility of BGP configuration. A
specific policy can be configured once and referenced many times. Because a peer policy supports up to eight
levels of inheritance, very specific and very complex BGP policies can be created.

IP Routing: BGP Configuration Guide
649


BGP per Neighbor SoO Configuration
How to Configure BGP per Neighbor SoO

For more details about BGP peer policy templates, see the "Configuring a Basic BGP Network" module.

How to Configure BGP per Neighbor SoO
Enabling Cisco Express Forwarding and Configuring VRF Instances
Perform this task on both of the PE routers in the figure above to configure Virtual Routing and Forwarding
(VRF) instances to be used with the per-VRF assignment tasks. In this task, Cisco Express Forwarding is
enabled, and a VRF instance named SOO_VRF is created. To make the VRF functional, a route distinguisher
is created, and the VRF is associated with an interface. When the route distinguisher is created, the routing
and forwarding tables are created for the VRF instance named SOO_VRF. After associating the VRF with
an interface, the interface is configured with an IP address.
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

enable
configure terminal
ip cef
ip vrf vrf-name
rd route-distinguisher
route-target {export | both} route-target-ext-community
route-target {import | both} route-target-ext-community
exit
interface type number
ip vrf forwarding vrf-name [downstream vrf-name2]
ip address ip-address mask [secondary]
end
show ip vrf [brief | detail | interfaces | id] [vrf-name] [output-modifiers]

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

ip cef
Example:
Device(config)# ip cef

IP Routing: BGP Configuration Guide
650

Enables Cisco Express Forwarding on the route processor.


BGP per Neighbor SoO Configuration
Enabling Cisco Express Forwarding and Configuring VRF Instances

Step 4

Command or Action

Purpose

ip vrf vrf-name

Defines a VRF instance and enters VRF configuration
mode.

Example:
Device(config)# ip vrf SOO_VRF

Step 5

rd route-distinguisher
Example:
Device(config-vrf)# rd 1:1

Creates routing and forwarding tables for a VRF and
specifies the default RD for a VPN.
• Use the route-distinguisher argument to specify the
default RD for a VPN. There are two formats that you
can use to specify an RD:
• A 16-bit autonomous system number, a colon,
and a 32-bit number, for example: 65000:3
• A 32-bit IP address, a colon, and a 16-bit
number, for example: 192.168.1.2:51
• In this example, the RD uses an autonomous system
number with the number 1 after the colon.

Step 6

route-target {export | both} route-target-ext-community Creates a route-target extended community for a VRF.
Example:
Device(config-vrf)# route-target export 1:1

• Use the export keyword to export routing information
to the target VPN extended community.
• Use the both keyword to both import routing
information from, and export routing information to,
the target VPN extended community.
• Use the route-target-ext-community argument to
specify the VPN extended community.
Note

Step 7

Only the syntax applicable to this step is
displayed. For a different use of this syntax, see
Step 7.

route-target {import | both} route-target-ext-community Creates a route-target extended community for a VRF.
Example:
Device(config-vrf)# route-target import 1:1

• Use the import keyword to import routing
information from the target VPN extended
community.
• Use the both keyword to both import routing
information from, and export routing information to,
the target VPN extended community.
• Use the route-target-ext-community argument to
specify the VPN extended community.

Step 8

exit
Example:

Exits VRF configuration mode and returns to global
configuration mode.

IP Routing: BGP Configuration Guide
651


BGP per Neighbor SoO Configuration
Configuring a per Neighbor SoO Value Using a BGP Peer Policy Template

Command or Action

Purpose

Device(config-vrf)# exit

Step 9

interface type number

Configures an interface type and enters interface
configuration mode.

Example:
Device(config)# interface GigabitEthernet 1/0/0

Step 10

ip vrf forwarding vrf-name [downstream vrf-name2] Associates a VRF with an interface or subinterface.
Example:

• In this example, the VRF named SOO_VRF is
associated with Gigabit Ethernet interface 1/0/0.

Device(config-if)# ip vrf forwarding SOO_VRF

Note

Step 11

ip address ip-address mask [secondary]

Executing this command on an interface
removes the IP address, so the IP address should
be reconfigured.

Configures an IP address.

Example:

• In this example, Gigabit Ethernet interface 1/0/0 is
configured with an IP address of 192.168.1.2.

Device(config-if)# ip address 192.168.1.2
255.255.255.0

Step 12

Exits interface configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-if)# end

Step 13

show ip vrf [brief | detail | interfaces | id] [vrf-name]
[output-modifiers]

Displays the configured VRFs.

Example:

• Use this command to verify the configuration of this
task.

Device# show ip vrf

Examples
The following output of the show ip vrf command displays the VRF named SOO_VRF configured
in this task.
Device# show ip vrf
Name
SOO_VRF

Default RD
1:1

Interfaces
GE1/0/0

Configuring a per Neighbor SoO Value Using a BGP Peer Policy Template
Perform this task on router PE1 in the figure above to configure an SoO value for a BGP neighbor at the router
CPE1 in the figure above using a peer policy template. In this task, a peer policy template is created, and the

IP Routing: BGP Configuration Guide
652


BGP per Neighbor SoO Configuration
Configuring a per Neighbor SoO Value Using a BGP Peer Policy Template

SoO value is configured for the peer policy. Under address family IPv4 VRF, a neighbor is identified and is
configured to inherit the peer policy that contains the SoO value.
If a BGP peer inherits from several peer policy templates that specify different SoO values, the SoO value in
the last template applied takes precedence and is applied to the peer. However, direct configuration of the
SoO value on the BGP neighbor overrides any inherited template configurations of the SoO value.
Before you begin
This task assumes that the task described in the Enabling Cisco Express Forwarding and Configuring VRF
Instances, on page 650 has been performed.

Note

A BGP peer cannot inherit from a peer policy or session template and be configured as a peer group member
at the same. BGP templates and BGP peer groups are mutually exclusive.
>

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
router bgp autonomous-system-number
template peer-policy policy-template-name
soo extended-community-value
exit-peer-policy
address-family ipv4 [unicast | multicast| vrf vrf-name]
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address activate
neighbor ip-address inherit peer-policy policy-template-name
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

IP Routing: BGP Configuration Guide
653


BGP per Neighbor SoO Configuration
Configuring a per Neighbor SoO Value Using a BGP Peer Policy Template

Command or Action

Purpose

Router(config)# router bgp 50000

Step 4

template peer-policy policy-template-name
Example:

Creates a peer policy template and enters policy-template
configuration mode.

Router(config-router)# template peer-policy
SOO_POLICY

Step 5

soo extended-community-value
Example:
Router(config-router-ptmp)# soo 65000:1

Sets the SoO value for a BGP peer policy template.
• Use the extended-community-value argument to
specify the VPN extended community value. The
value takes one of the following formats:
• A 16-bit autonomous system number, a colon,
and a 32-bit number, for example: 45000:3
• A 32-bit IP address, a colon, and a 16-bit
number, for example: 192.168.10.2:51
• In this example, the SoO value is set at 65000:1.

Step 6

exit-peer-policy
Example:

Exits policy-template configuration mode and returns to
router configuration mode.

Router(config-router-pmtp)# exit-peer-policy

Step 7

address-family ipv4 [unicast | multicast| vrf vrf-name] Specifies the IPv4 address family and enters address family
configuration mode.
Example:
• Use the unicast keyword to specify the IPv4 unicast
Router(config-router)# address-family ipv4 vrf
address family. By default, the router is placed in
SOO_VRF
configuration mode for the IPv4 unicast address
family if the unicast keyword is not specified with
the address-family ipv4 command.
• Use the multicast keyword to specify IPv4 multicast
address prefixes.
• Use the vrf keyword and vrf-name argument to
specify the name of the VRF instance to associate
with subsequent IPv4 address family configuration
mode commands.

Step 8

neighbor ip-address remote-as
autonomous-system-number
Example:
Router(config-router-af)# neighbor 192.168.1.1
remote-as 65000

IP Routing: BGP Configuration Guide
654

Adds the IP address of the neighbor in the specified
autonomous system to the IPv4 multiprotocol BGP
neighbor table of the local router.


BGP per Neighbor SoO Configuration
Configuring a per Neighbor SoO Value Using a BGP neighbor Command

Step 9

Command or Action

Purpose

neighbor ip-address activate

Enables the neighbor to exchange prefixes for the IPv4
VRF address family with the local router.

Example:
Router(config-router-af)# neighbor 192.168.1.1
activate

Step 10

neighbor ip-address inherit peer-policy
policy-template-name
Example:
Router(config-router-af)# neighbor 192.168.1.1
inherit peer-policy SOO_POLICY

Step 11

Sends a peer policy template to a neighbor so that the
neighbor can inherit the configuration.
• In this example, the router is configured to send the
peer policy template named SOO_POLICY to the
192.168.1.1 neighbor to inherit. If another peer policy
template is indirectly inherited from SOO_POLICY,
the indirectly inherited configuration will also be
applied. Up to seven additional peer policy templates
can be indirectly inherited from SOO_POLICY.
Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Router(config-router-af)# end

Configuring a per Neighbor SoO Value Using a BGP neighbor Command
Perform this task on router PE2 in the figure above to configure an SoO value for the BGP neighbor at router
CPE2 in the figure above using a neighbor command. For the IPv4 VRF address family, a neighbor is
identified, and an SoO value is configured for the neighbor.
Direct configuration of the SoO value on a BGP neighbor overrides any inherited peer policy template
configurations of the SoO value.
Before you begin
This task assumes that the task described in the “Verifying CEF and Configuring VRF Instances” section has
been performed with appropriate changes to interfaces and IP addresses.
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
address-family ipv4 [unicast | multicast | vrf vrf-name]
neighbor {ip-address | peer-group-name} remote-as autonomous-system-number
neighbor ip-address activate
neighbor {ip-address | peer-group-name} soo extended-community-value
end

IP Routing: BGP Configuration Guide
655


BGP per Neighbor SoO Configuration
Configuring a per Neighbor SoO Value Using a BGP neighbor Command

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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 50000

Step 4

address-family ipv4 [unicast | multicast | vrf vrf-name] Specifies the IPv4 address family and enters address family
configuration mode.
Example:
• Use the unicast keyword to specify the IPv4 unicast
Device(config-router)# address-family ipv4 vrf
address family. By default, the router is placed in
SOO_VRF
configuration mode for the IPv4 unicast address family
if the unicast keyword is not specified with the
address-family ipv4 command.
• Use the multicast keyword to specify IPv4 multicast
address prefixes.
• Use the vrf keyword and vrf-name argument to specify
the name of the VRF instance to associate with
subsequent IPv4 address family configuration mode
commands.

Step 5

neighbor {ip-address | peer-group-name} remote-as
autonomous-system-number
Example:

Adds the IP address of the neighbor in the specified
autonomous system to the IPv4 multiprotocol BGP neighbor
table of the local router.

Device(config-router-af)# neighbor 192.168.2.1
remote-as 65000

Step 6

neighbor ip-address activate
Example:
Device(config-router-af)# neighbor 192.168.2.1
activate

IP Routing: BGP Configuration Guide
656

Enables the neighbor to exchange prefixes for the IPv4 VRF
address family with the local router.
• In this example, the external BGP peer at 192.168.2.1
is activated.


BGP per Neighbor SoO Configuration
Configuring a per Neighbor SoO Value Using a BGP Peer Group

Command or Action

Purpose
Note

Step 7

neighbor {ip-address | peer-group-name} soo
extended-community-value
Example:

If a peer group has been configured in Step 5 ,
do not use this step because BGP peer groups
are activated when any parameter is configured.
For example, a BGP peer group is activated when
an SoO value is configured using the neighbor
soo command in Step 7.

Sets the site-of-origin (SoO) value for a BGP neighbor or
peer group.
• In this example, the neighbor at 192.168.2.1 is
configured with an SoO value of 65000:1.

Device(config-router-af)# neighbor 192.168.2.1 soo
65000:1

Step 8

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuring a per Neighbor SoO Value Using a BGP Peer Group
Perform this task on router PE1 in the figure above to configure an SoO value for the BGP neighbor at router
CPE1 in the figure above using a neighbor command with a BGP peer group. Under address family IPv4
VRF, a BGP peer group is created and an SoO value is configured using a BGP neighbor command, and a
neighbor is then identified and added as a peer group member. A BGP peer group member inherits the
configuration associated with a peer group, which in this example, includes the SoO value.
Direct configuration of the SoO value on a BGP neighbor overrides any inherited peer group configurations
of the SoO value.
Before you begin
This task assumes that the task described in “Enabling Cisco Express Forwarding and Configuring VRF
Instances” has been performed.

Note

A BGP peer cannot inherit from a peer policy or session template and be configured as a peer group member
at the same. BGP templates and BGP peer groups are mutually exclusive.

SUMMARY STEPS
1.
2.
3.
4.
5.
6.

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 [unicast | multicast | vrf vrf-name]
neighbor peer-group-name peer-group
neighbor {ip-address | peer-group-name} soo extended-community-value

IP Routing: BGP Configuration Guide
657


BGP per Neighbor SoO Configuration
Configuring a per Neighbor SoO Value Using a BGP Peer Group

7.
8.
9.
10.

neighbor ip-address remote-as autonomous-system-number
neighbor ip-address activate
neighbor ip-address peer-group peer-group-name
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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 50000

Step 4

address-family ipv4 [unicast | multicast | vrf vrf-name] Specifies the IPv4 address family and enters address family
configuration mode.
Example:
• Use the unicast keyword to specify the IPv4 unicast
Device(config-router)# address-family ipv4 vrf
address family. By default, the router is placed in
SOO_VRF
configuration mode for the IPv4 unicast address
family if the unicast keyword is not specified with
the address-family ipv4 command.
• Use the multicast keyword to specify IPv4 multicast
address prefixes.
• Use the vrf keyword and vrf-name argument to
specify the name of the VRF instance to associate
with subsequent IPv4 address family configuration
mode commands.

Step 5

neighbor peer-group-name peer-group

Creates a BGP peer group.

Example:
Device(config-router-af)# neighbor SOO_group
peer-group

Step 6

neighbor {ip-address | peer-group-name} soo
extended-community-value
Example:

IP Routing: BGP Configuration Guide
658

Sets the site-of-origin (SoO) value for a BGP neighbor or
peer group.
• In this example, the BGP peer group, SOO_group, is
configured with an SoO value of 65000:1.


BGP per Neighbor SoO Configuration
Configuration Examples for BGP per Neighbor SoO Configuration

Command or Action

Purpose

Device(config-router-af)# neighbor SOO_group soo
65000:1

Step 7

neighbor ip-address remote-as
autonomous-system-number
Example:

Adds the IP address of the neighbor in the specified
autonomous system to the IPv4 multiprotocol BGP
neighbor table of the local router.

Device(config-router-af)# neighbor 192.168.1.1
remote-as 65000

Step 8

neighbor ip-address activate
Example:

Enables the neighbor to exchange prefixes for the IPv4
VRF address family with the local router.

Device(config-router-af)# neighbor 192.168.1.1
activate

Step 9

neighbor ip-address peer-group peer-group-name

Assigns the IP address of a BGP neighbor to a peer group.

Example:
Device(config-router-af)# neighbor 192.168.1.1
peer-group SOO_group

Step 10

end
Example:

Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

ConfigurationExamplesforBGPperNeighborSoOConfiguration
Example: Configuring a per Neighbor SoO Value Using a BGP Peer Policy
Template
The following example shows how to create a peer policy template and configure an SoO value as part of the
peer policy. After enabling Cisco Express Forwarding and configuring a VRF instance named SOO_VRF, a
peer policy template is created and an SoO value is configured as part of the peer policy. Under the IPv4 VRF
address family, a neighbor is identified and configured to inherit the peer policy that contains the SoO value.
ip cef
ip vrf SOO_VRF
rd 1:1
route-target export 1:1
route-target import 1:1
exit
interface GigabitEthernet 1/0/0
ip vrf forwarding SOO_VRF
ip address 192.168.1.2 255.255.255.0
exit

IP Routing: BGP Configuration Guide
659


BGP per Neighbor SoO Configuration
Example: Configuring a per Neighbor SoO Value Using a BGP neighbor Command

router bgp 50000
template peer-policy SOO_POLICY
soo 65000:1
exit-peer-policy
address-family ipv4 vrf SOO_VRF
neighbor 192.168.1.1 remote-as 65000
neighbor 192.168.1.1 activate
neighbor 192.168.1.1 inherit peer-policy SOO_POLICY
end

Example: Configuring a per Neighbor SoO Value Using a BGP neighbor
Command
The following example shows how to configure an SoO value for a BGP neighbor. After enabling Cisco
Express Forwarding and configuring a VRF instance named SOO_VRF, a neighbor is identified in the IPv4
VRF address family and an SoO value is configured for the neighbor.
ip cef
ip vrf SOO_VRF
rd 1:1
route-target export 1:1
route-target import 1:1
exit
interface GigabitEthernet 1/0/0
ip vrf forwarding SOO_VRF
ip address 192.168.2.2 255.255.255.0
exit
router bgp 50000
address-family ipv4 vrf SOO_VRF
neighbor 192.168.2.1 remote-as 65000
neighbor 192.168.2.1 activate
neighbor 192.168.2.1 soo 65000:1
end

Example: Configuring a per Neighbor SoO Value Using a BGP Peer Group
The following example shows how to configure an SoO value for a BGP peer group. After enabling Cisco
Express Forwarding and configuring a VRF instance named SOO_VRF, a BGP peer group is configured in
the IPv4 VRF address family, an SoO value is configured for the peer group, a neighbor is identified, and the
neighbor is configured as a member of the peer group.
ip cef
ip vrf SOO_VRF
rd 1:1
route-target export 1:1
route-target import 1:1
exit
interface GigabitEthernet 1/0/0
ip vrf forwarding SOO_VRF
ip address 192.168.1.2 255.255.255.0
exit
router bgp 50000
address-family ipv4 vrf SOO_VRF
neighbor SOO_GROUP peer-group
neighbor SOO_GROUP soo 65000:65
neighbor 192.168.1.1 remote-as 65000
neighbor 192.168.1.1 activate

IP Routing: BGP Configuration Guide
660


BGP per Neighbor SoO Configuration
Where to Go Next

neighbor 192.168.1.1 peer-group SOO_GROUP
end

Where to Go Next
• To read an overview of BGP, proceed to the "Cisco BGP Overview" module.
• To perform basic BGP feature tasks, proceed to the "Configuring a Basic BGP Network" module.
• To perform advanced BGP feature tasks, proceed to the "Configuring Advanced BGP Features" module.
• To configure BGP neighbor session options, proceed to the "Configuring BGP Neighbor Session Options"
module.
• To perform internal BGP tasks, proceed to the "Configuring Internal BGP Features" module.

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Switching commands Cisco IOS IP Switching Command Reference
MIBs
MIB MIBs Link
—

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco
MIB Locator found at the following URL:
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
661


BGP per Neighbor SoO Configuration
Feature Information for BGP per Neighbor SoO Configuration

Feature Information for BGP per Neighbor SoO Configuration
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 56: Feature Information for BGP per Neighbor SoO Configuration

Feature Name

Releases

Feature Information

BGP per Neighbor
SoO Configuration

Cisco IOS XE
Release 2.1

The BGP per neighbor SOO configuration feature simplifies the
configuration of the site-of-origin (SoO) parameter. The per
neighbor SoO configuration introduces two new commands that
can be configured in submodes under router configuration mode
to set the SoO value.
This feature was introduced on the Cisco ASR 1000 Series
Aggregation Services Routers.
The following commands were introduced by this feature:
neighbor soo, soo.

IP Routing: BGP Configuration Guide
662
