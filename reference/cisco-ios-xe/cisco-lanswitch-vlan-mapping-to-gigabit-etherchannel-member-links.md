---
title: "VLAN Mapping to Gigabit EtherChannel Member Links"
type: reference
domain: cisco-ios-xe
slug: cisco-lanswitch-vlan-mapping-to-gigabit-etherchannel-member-links
tier: reference
source: "Cisco IOS XE 16 — LAN Switching Configuration Guide"
version: ios-xe-16
family: lan-switching
documentKind: "Documentation"
abstract: "CHAPTER 5 VLAN Mapping to Gigabit EtherChannel Member Links The VLAN Mapping to Gigabit EtherChannel (GEC) Member Links feature allows you to configure static assignment of user traffic, as identified by a VLAN ID, to a given member link of a GEC bundle. You can manually assign virtual LAN (VLAN) subinterfaces to a primary and secondary link. This feature allows load balancing to downstream equi"
---

# VLAN Mapping to Gigabit EtherChannel Member Links

CHAPTER

5

VLAN Mapping to Gigabit EtherChannel Member
Links
The VLAN Mapping to Gigabit EtherChannel (GEC) Member Links feature allows you to configure static
assignment of user traffic, as identified by a VLAN ID, to a given member link of a GEC bundle. You can
manually assign virtual LAN (VLAN) subinterfaces to a primary and secondary link. This feature allows load
balancing to downstream equipment regardless of vendor equipment capabilities, and provides failover
protection by redirecting traffic to the secondary member link if the primary link fails. Member links are
supported with up to 64 GEC interfaces and 14 member links per GEC interface.
• Prerequisites for VLAN Mapping to GEC Member Links, on page 39
• Restrictions for VLAN Mapping to GEC Member Links, on page 39
• Information About VLAN Mapping of GEC Member Links, on page 40
• How to Configure VLAN Mapping to GEC Links, on page 44
• Configuration Examples for VLAN Mapping to GEC Member Links, on page 46
• Additional References, on page 49
• Feature Information for VLAN Mapping to GEC Member Links, on page 49

Prerequisites for VLAN Mapping to GEC Member Links
• Each VLAN must have IEEE 802.1Q encapsulation configured.
• One primary and one secondary link must be associated with each VLAN.
• Configure per VLAN load balancing either on the main port-channel interface or enable it globally.

Restrictions for VLAN Mapping to GEC Member Links
The following restrictions are applicable for IPv6 load balancing on Gigabit EtherChannel (GEC) links:
• IPv6 traffic distribution is enabled only on port channels with flow load balancing.
• Multiprotocol Label Switching (MPLS) Traffic Engineering (TE) is not supported on port channels.
• For Cisco ASR 1000 Series Aggregation Services Routers, the minimum number of member links per
GEC interface is 1 and the maximum number is 14.

LAN Switching Configuration Guide
39


VLAN Mapping to Gigabit EtherChannel Member Links
Information About VLAN Mapping of GEC Member Links

• 10 Gigabit, 40 Gigabit, 100 Gigabit Ethernet supported as a member link in VLAN mapping.
• The port-channel QinQ subinterface is not supported.
• The quality of service (QoS) policy can be applied to a port-channel subinterface when the following
conditions are met:
• Manual virtual LAN (VLAN) load balancing is supported.
• A policy map has the appropriate service-fragment policy configured on a physical member link.

Information About VLAN Mapping of GEC Member Links
VLAN-Manual Load Balancing
When load balancing is configured for GEC links, traffic flows are mapped to different buckets as dictated
by the load balancing algorithm. For each EtherChannel, a set of 16 buckets are created. The EtherChannel
module decides how the buckets are distributed across member links. Each bucket has an active link associated
with it that represents the interface to be used for all flows that are mapped to the same bucket.
All packets to be forwarded over the same VLAN subinterface are considered to be part of the same flow that
is mapped to one bucket. Each bucket is associated with a primary and secondary pair, and the buckets point
to the active interface in the pair. Only one pair is active at a time. Multiple VLAN flows can be mapped to
the same bucket if their (primary and secondary) mapping is the same.
The buckets are created when VLAN manual load balancing is enabled. When VLAN load balancing is
removed, the buckets are deleted. All port channels use either VLAN manual load balancing or dynamic
flow-based load balancing. For information about flow-based load balancing, see the “Flow-Based Per
Port-Channel Load Balancing” module.
One primary and one secondary link must be associated with a given VLAN. The primary and secondary
options are available only if VLAN manual load balancing is enabled. If the following conditions are met,
the load balancing information is downloaded in the forwarding plane. If any of these conditions are not met
, the load balancing information is removed from the forwarding plane.
• VLAN load balancing must be enabled globally.
• IEEE 802.1Q encapsulation must be configured on each VLAN.
• One primary and one secondary member link must be enabled to manually map the VLAN traffic to the
EtherChannel links.
• The primary and secondary links must be part of the port channel for traffic to use these links.
If only a primary link is specified, a secondary link is selected as the default. If neither a primary nor a
secondary link is explicitly configured, the primary and secondary links are selected by default. There is no
attempt to perform equal VLAN distribution across links when default links are chosen.
If the interfaces specified as primary or secondary links are not configured as part of the port channel, or if
the global VLAN load balancing is not enabled, warning messages are displayed.

LAN Switching Configuration Guide
40


VLAN Mapping to Gigabit EtherChannel Member Links
VLAN-to-Port Channel Member Link Mapping

Warning
VLAN 500's main interface is not the channel group of primary=GigabitEthernet 4/0/1 Per-VLAN manual
load-balancing will not take effect until channel-group is configured under the primary interface.
VLAN 500's main interface is not the channel group of secondary=GigabitEthernet 1/0/0 Per-VLAN manual
load-balancing will not take effect until channel-group is configured under the primary interface.

VLAN-to-Port Channel Member Link Mapping
The figure below illustrates the traffic flow for the VLAN-to-port channel mapping.
Figure 3: VLAN-to-Port Channel Member Link Mapping

The black lines represent the physical 1 Gigabit Ethernet interfaces connecting the MCP router with the Layer
2 (L2) switch. These interfaces are bundled together in port-channels, shown in green.
In the figure below, subscriber VLAN subinterfaces, shown in shades of orange and red, are configured as
Layer 3 (L3) interfaces on top of EtherChannel interfaces. Mapping of the VLAN to the member link (shown
with the dotted black arrow) is done through configuration and downloaded in the dataplane so that the
outgoing VLA traffic (shown with orange and red arrows) is sent over the associated active primary or
secondary member link. The QoS configuration in this model is applied at the VLAN subinterface and member
link interface level, implying that QoS queues are created at both levels.
Figure 4: Mapping of VLAN to Member Links

VLAN Primary and Secondary Link Association
In a port-channel traffic distribution, a member link can have either a configured primary state or a secondary
state, and an operational active or standby state. When the interface is up, the primary link is active. If the

LAN Switching Configuration Guide
41


VLAN Mapping to Gigabit EtherChannel Member Links
VLAN Primary and Secondary Link Association

primary link is down, the interface is in primary standby state while the secondary interface is in secondary
active state. If the primary link is up, the secondary link is in secondary standby even if the interface is
operationally up.
The primary and secondary member links are each associated with a routed VLAN configured on a port-channel
main interface. When forwarding traffic for this VLAN, the primary interface is used as the outgoing interface
when this interface is up; the secondary interface, if operational, is used when the primary interface is down.
If all the conditions for per-VLAN traffic distribution are not met, the mapping is not downloaded in the
forwarding plane. If all the conditions are met, the dataplane is updated with this mapping.
The table below describes the primary and secondary link configuration status and the resulting function of
each configuration.
Table 6: VLAN Primary and Secondary Link Mapping Status

Primary Status

Secondary Status

Description

Configured

Configured

Both primary and secondary links are specified with the
encapsulation dot1q command.
encapsulation dot1Q vlan-id primary

Defaulted

Defaulted

Neither a primary nor a secondary link is specified.
encapsulation dot1Q vlan-id

In a stable system, defaults for both primary and secondary
links are selected in the same manner for all VLANs. The
first link up that is added to the EC is selected as primary,
and the second link up as secondary. If there are no links
up, the primary and secondary links are selected from the
down links.
Configured

Defaulted

Only the primary link is specified.
encapsulation dot1Q vlan-id primary

A secondary link that is different than the primary link is
internally selected.
Configured

–

Only a primary link is specified and only one link is
defined.
encapsulation dot1Q vlan-id primary

No secondary link can be selected as default when only
one link is defined in the EC.
Defaulted

–

Neither a primary nor secondary link is specified, and
only one link is defined.
encapsulation dot1Q vlan-id

A default for a primary link is selected. However, no
default link can be selected for a secondary link if only
one link is defined in the EC.

LAN Switching Configuration Guide
42


VLAN Mapping to Gigabit EtherChannel Member Links
Adding Channel Member Links

Primary Status

Secondary Status

Description

–

–

Neither a primary nor secondary link is specified, and no
links are defined.
encapsulation dot1Q vlan-id

Defaults cannot be selected and no links are defined in
the EC.

Note

Default mappings do not override user-configured mappings even if the user-configured mappings are defined
incorrectly. Once the (VLAN, primary, and secondary) association is performed (either through the CLI,
default or a combination of both), the system validates the mapping and downloads it to the dataplane. If there
are no VLANs configured, all traffic forwarded over the port channel is dropped.

Adding Channel Member Links
When a new member link is added, new buckets are created and downloaded in the dataplane. For all VLANs
that have the interface as either primary or secondary, new VLAN-to-bucket mappings are downloaded in the
dataplane. For all VLANs that need a default for primary and secondary, the default selection algorithm is
triggered, and if QoS validation passes, the VLAN-to-bucket mappings are downloaded. QoS policies create
VLAN queues on the newly added link.

Deleting Member Links
When a member link is removed, a warning message is displayed. All VLAN queues from the member link,
VLAN-to-bucket mappings, and all affected buckets are removed.

Port Channel Link Down Notification
When a link goes down, all traffic for VLANs that have the Port Channel link assigned as primary link must
be switched to secondary link if the secondary is up. The traffic for the VLANs with the Port Channel link
assigned as secondary, is not affected. The Port Channel Link Down notification causes all buckets associated
with a primary-secondary pair (where the primary link is down and the secondary link is up) to be updated
with the secondary link. This change is communicated to the dataplane.
All buckets associated with a primary-secondary pair (and the secondary link is the down link and where
primary link is up) are updated so that the primary link is now the active link. This change is communicated
to the dataplane.

Port Channel Link Up Notification
When a link goes up, all traffic for VLANs that have this link assigned as primary is switched to this link.
The traffic for VLANs that have this link assigned as secondary is not affected. The Port Channel Link Up
notification causes all buckets associated with a primary-secondary pair, where the primary link is the link
that came up, and the secondary link is up, to be notified that the primary link is up. The change is
communicated to the dataplane.

LAN Switching Configuration Guide
43


VLAN Mapping to Gigabit EtherChannel Member Links
Disabling Load Balancing on the EtherChannel

All buckets associated with a primary-secondary pair, where the secondary link is the link that came up and
the primary link is down are notified that the secondary link is now the primary link. The change is
communicated to the dataplane.

Disabling Load Balancing on the EtherChannel
To disable load balancing on the EtherChannel, use the no port-channel load-balancing vlan-manual
command. The following warning message is displayed if any VLAN subinterfaces exist:
Warning: Removing the Global VLAN LB command will affect traffic
c for all dot1Q VLANs

Removing a Member Link from the EtherChannel
To remove a member link from the EtherChannel (EC), use the no channel-group command
When a member link is removed from the EC is included in a VLAN mapping, the following warning message
is displayed:
Warning: Removing GigabitEthernet 4/0/0 from the port-channel will affect traffic for the
dot1Q VLANs that include this link in their mapping.

How to Configure VLAN Mapping to GEC Links
Configuring VLAN-Based Manual Load Balancing
Perform this task to link VLAN port-channel and to enable VLAN load balancing on port channels.
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
port-channel load-balancing vlan-manual
interface port-channel channel-number
ip address ip-address address-mask
exit
interface type subinterface-number
channel-group
channel-number
exit
interface port-channel interface-number.subinterface-number
encapsulation dot1Q vlan-id primary interface-type slot/port secondary interface-type slot/port
ip address ip-address address-mask
end

LAN Switching Configuration Guide
44


VLAN Mapping to Gigabit EtherChannel Member Links
Configuring VLAN-Based Manual Load Balancing

DETAILED STEPS
Procedure

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

port-channel load-balancing vlan-manual

Enables port-channel load balancing on the router.

Example:
Router(config)# port-channel load-balancing
vlan-manual

Step 4

interface port-channel channel-number
Example:

Enters interface configuration mode and defines the
interface as a port channel.

Router(config)# interface port-channel 1

Step 5

ip address ip-address address-mask

Specifies the IP address and mask.

Example:
Router(config-if)# ip address 172.16.2.3
255.255.0.0

Step 6

Exits interface configuration mode and returns to global
configuration mode.

exit
Example:
Router(config-if)# exit

Step 7

interface type subinterface-number
Example:

Enters interface configuration mode on the Gigabit Ethernet
interface.

Router(config)# interface gigbabitethernet 1/1/0

Step 8

channel-group

channel-number

Example:
Router(config-if)# channel-group 1

Step 9

exit
Example:

Assigns the Gigabit Ethernet interface to the specified
channel group.
• The channel number is the same channel number that
you specified when you created the port-channel
interface.
Exits interface configuration mode and returns to global
configuration mode.

Device(config-if)# exit

LAN Switching Configuration Guide
45


VLAN Mapping to Gigabit EtherChannel Member Links
Troubleshooting Tips

Step 10

Command or Action

Purpose

interface port-channel
interface-number.subinterface-number

Specifies the interface type, interface number, and
subinterface number.

Example:
Device(config)# interface port-channel 1.100

Step 11

encapsulation dot1Q vlan-id primary interface-type Enables IEEE 802.1Q encapsulation on the interface.
slot/port secondary interface-type slot/port
Example:
Device(config-if)# encapsulation dot1Q 100 primary
GigabitEthernet 1/1/1 secondary GigabitEthernet
1/2/1

Step 12

ip address ip-address address-mask

Specifies the port channel IP address and mask.

Example:
Device(config-if)# ip address 172.16.2.100
255.255.255.0

Step 13

Exits interface configuration mode, and returns to
privileged EXEC mode.

end
Example:
Device(config-if)# end

Troubleshooting Tips
• Use the show etherchannel load-balancing command to display the current port channel load balancing
method.
• Use the show interfaces port-channel etherchannel command to display the current traffic distribution.

Configuration Examples for VLAN Mapping to GEC Member
Links
Example: Configuring VLAN Manual Load Balancing
This example shows how the load balancing configuration can be globally applied to define policies for
handling traffic by using the port-channel load-balancing command. Note that IEEE 802.1Q encapsulation
is configured on each port-channel interface. The figure below illustrates the port channel bundle with three
VLANs used in the following configuration example:

LAN Switching Configuration Guide
46


VLAN Mapping to Gigabit EtherChannel Member Links
Example: Configuring VLAN Manual Load Balancing

Figure 5: Port Channel Bundle

port-channel load-balancing vlan-manual
!
class-map match-all BestEffort
!
class-map match-all video
!
class-map match-all voice
!
policy-map subscriber
class voice
priority level 1
class video
priority level 2
class class-default service-fragment BE
shape average 10000
bandwidth remaining percent 80
policy-map aggregate-member-link
class BestEffort service-fragment BE
shape average 100000
!
interface Port-channel1
ip address 172.16.2.3 255.255.0.0
!
interface Port-channel1.100
encapsulation dot1Q 100 primary GigabitEthernet 1/1/1
secondary GigabitEthernet 1/2/1
ip address 172.16.2.100 255.255.255.0
service-policy output subscriber
!
interface Port-channel1.200
encapsulation dot1Q 200 primary GigabitEthernet 1/2/1
ip address 172.16.2.200 255.255.255.0
service-policy output subscriber
!
interface Port-channel1.300
encapsulation dot1Q 300
ip address 172.16.2.300 255.255.255.0
service-policy output subscriber
!
interface GigabitEthernet 1/1/1
no ip address
channel-group 1 mode on

LAN Switching Configuration Guide
47


VLAN Mapping to Gigabit EtherChannel Member Links
Example: Troubleshooting

service-policy output aggregate-member-link
!
interface GigabitEthernet 1/2/1
no ip address
channel-group 1 mode on
service-policy output aggregate-member-link

Example: Troubleshooting
Example 1:
Device# show etherchannel load-balancing
EtherChannel Load-Balancing Configuration: vlan-manual

Example 2:
Device# show etherchannel load-balancing
EtherChannel Load-Balancing Configuration: not configured

Use the show interfaces port-channel command to display the traffic distribution currently in use.
Device# show interfaces port-channel 1 etherchannel
Active Member List contains 0 interfaces
Passive Member List contains 2 interfaces
Port: GigabitEthernet 4/0/0
VLAN 1 (Pri, Ac, D, P)
VLAN 100 (Pri, Ac, C, P)
VLAN 200 (Sec, St, C, P)
Port: GigabitEthernet 1/0/0
VLAN 1 (Sec, St, D, P)
VLAN 100 (Sec, St, C, P)
VLAN 200 (Pri, Ac, C, P)
Bucket Information for VLAN Manual LB:
Bucket 0
(p=GigabitEthernet 4/0/0, s=GigabitEthernet 4/0/0) active GigabitEthernet
4/0/0
Bucket 1
(p=Gigabitthernet 4/0/0, s=GigabitEthernet 1/0/0) active GigabitEthernet
4/0/0
Bucket 4
(p=GigabitEthernet 1/0/0, s=GigabitEthernet 4/0/0) active GigabitEthernet
1/0/0
Bucket 5
(p=GigabitEthernet 1/0/0, s=GigabitEthernet 1/0/0) active GigabitEthernet
1/0/0

To see the mapping of a VLAN to primary and secondary links, use the show vlans command.
Device# show vlans 100
VLAN ID: 100 (IEEE 802.1Q Encapsulation)
Protocols Configured:
Received:
Transmitted:
VLAN trunk interfaces for VLAN ID 100:
Port-channel1.1 (100)
Mapping for traffic load-balancing using bucket 1:
primary
= GigabitEthernet 4/0/0 (active, C, P)
secondary = GigabitEthernet 1/0/0 (standby, C, P)
Total 0 packets, 0 bytes input
Total 0 packets, 0 bytes output
No subinterface configured with ISL VLAN ID 100

LAN Switching Configuration Guide
48


VLAN Mapping to Gigabit EtherChannel Member Links
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

LAN Switching commands Cisco IOS LAN Switching Command Reference
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

Feature Information for VLAN Mapping to GEC Member Links
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.
Table 7: Feature Information for VLAN Mapping to Gigabit EtherChannel Member Links

Feature Name

Releases

Feature Information

VLAN Mapping to
Gigabit
EtherChannel
Member Links

Cisco IOS XE The VLAN Mapping to Gigabit EtherChannel Member Links feature
Release 2.1
allows you to configure static assignment of user traffic as identified
by a VLAN ID to a given member link of a GEC bundle. You can
manually assign VLAN subinterfaces to a primary and secondary link.
This feature allows load balancing to downstream equipment,
regardless of vendor equipment capabilities, and provides failover
protection by redirecting traffic to the secondary member link if the
primary link fails. Member links are supported with up to 16 bundles
per chassis.
The following commands were modified by this feature: encapsulation
dot1q, port-channel load-balancing vlan-manual, show
etherchannel load-balancing, and show interfaces port-channel
vlan mapping.

LAN Switching Configuration Guide
49


VLAN Mapping to Gigabit EtherChannel Member Links
Feature Information for VLAN Mapping to GEC Member Links

LAN Switching Configuration Guide
50
