---
title: "EtherChannel Flow-Based Limited 1 1 Redundancy"
type: reference
domain: cisco-ios-xe
slug: cisco-lanswitch-etherchannel-flow-based-limited-1-1-redundancy
tier: reference
source: "Cisco IOS XE 16 — LAN Switching Configuration Guide"
version: ios-xe-16
family: lan-switching
documentKind: "Documentation"
abstract: "CHAPTER 7 EtherChannel Flow-Based Limited 1 1 Redundancy EtherChannel flow-based limited 1:1 redundancy provides MAC, or layer 2, traffic protection to avoid higher layer protocols from reacting to single link failures and re-converging. To use EtherChannel flow-based limited 1:1 redundancy, you configure an EtherChannel with two ports (one active and one standby). If the active link goes down,"
---

# EtherChannel Flow-Based Limited 1 1 Redundancy

CHAPTER

7

EtherChannel Flow-Based Limited 1 1
Redundancy
EtherChannel flow-based limited 1:1 redundancy provides MAC, or layer 2, traffic protection to avoid higher
layer protocols from reacting to single link failures and re-converging. To use EtherChannel flow-based limited
1:1 redundancy, you configure an EtherChannel with two ports (one active and one standby). If the active
link goes down, the EtherChannel stays up and the system performs fast switchover to the hot-standby link.
Depending on how you have the priorities set, when the failed link becomes operational again, the EtherChannel
performs another fast switchover to revert to the original active link. if all port-priorities are the same, it will
not revert, but remain on the current active link.
With 1:1 redundancy configured, only one link is active at any given time so all flows are directed over the
active link.
• Restrictions for EtherChannel Flow-based Limited 1:1 Redundancy, on page 119
• Information About EtherChannel Flow-Based Limited 1 1 Redundancy, on page 120
• How to Configure EtherChannel Flow-Based Limited 1 1 Redundancy, on page 120
• Configuration Examples for EtherChannel Flow-Based Limited1 1 Redundancy, on page 125
• Additional References, on page 126
• Feature Information for EtherChannel Flow-based Limited 1 1 Redundancy, on page 127

Restrictions for EtherChannel Flow-based Limited 1:1
Redundancy
When you are using the Cisco ASR 1001-X, the following restrictions apply for collecting traffic statistics
for VLAN egress on sub-interfaces. Obtaining input/output counters using SNMP is unsupported. This is
because the Cisco ASR 1001-X has a built-in SPA.
Restrictions that apply when obtaining traffic statistics for two types of interfaces are shown below:
• Physical sub-interfaces
For the Cisco ASR 1001-X, statistics for the VLAN egress are available for physical sub-interfaces. The
output counter is used from cpp, not from the built-in SPA hardware. To show VLAN egress statistics,
use the show vlans vlan id command.
Example

LAN Switching Configuration Guide
119


EtherChannel Flow-Based Limited 1 1 Redundancy
Information About EtherChannel Flow-Based Limited 1 1 Redundancy

# show vlans 10
VLAN ID: 10 (IEEE 802.1Q Encapsulation)
>
>
Protocols Configured:
Received:
>
IP
133

Transmitted:
104

• Port Channel sub-interfaces
For the Cisco ASR 1001-X, showing traffic statistics for the VLAN egress is not supported for port
channel sub-interfaces.
cpp or the built-in SPA can not be used to give an output counter value for port channel sub-interfaces.

Information About EtherChannel Flow-Based Limited 1 1
Redundancy
EtherChannel Flow-Based Limited 1 1 Redundancy
EtherChannel flow-based limited 1:1 redundancy provides an EtherChannel configuration with one active
link and fast switchover to a hot standby link. To use EtherChannel flow-based limited 1:1 redundancy, you
configure a Link Aggregation Control Protocol (LACP) EtherChannel with two ports (one active and one
standby). If the active link goes down, the EtherChannel stays up and the system performs fast switchover to
the hot standby link. Depending on how the priorities of the links are set, when the failed link becomes
operational again, the EtherChannel performs another fast switchover to revert to the original active link, or
to the link with the higher priority.
For EtherChannel flow-based limited 1:1 redundancy to work correctly (especially the fast switchover
capability) the feature must be enabled at both ends of the link.

How to Configure EtherChannel Flow-Based Limited 1 1
Redundancy
Configuring EtherChannel Flow-Based Limited 1 1 Redundancy with
Fast-Switchover
To configure an LACP EtherChannel with two ports (one active and one standby), perform the following
steps. This feature must be enabled at both ends of the link.
You can control which link is the primary active link by setting the port priority on the links used for the
redundancy. To configure a primary link and enable the EtherChannel to revert to the original link, one link
must have a higher port priority than the other and the LACP max-bundle must be set to 1. This configuration
results in link 1 being active and link 2 being in hot standby state.
To prevent the switchover to revert, you can assign both links the same priority.

LAN Switching Configuration Guide
120


EtherChannel Flow-Based Limited 1 1 Redundancy
Configuring EtherChannel Flow-Based Limited 1 1 Redundancy with Fast-Switchover

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
interface port-channel channel -number
lacp fast-switchover
lacp max-bundle
1
exit
interface tengigabitethernet
slot / port / number
channel-group 1 mode mode
lacp port-priority priority
exit
interface tengigabitethernet
slot / port / number
channel-group 1 mode mode
lacp port-priority priority
end

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

Enters global configuration mode.

configure terminal
Example:
Router# configure terminal

Step 3

interface port-channel channel -number

Selects an LACP port channel interface.

Example:
Router(config)# interface port-channel 1

Step 4

Enables the fast switchover feature for this EtherChannel.

lacp fast-switchover
Example:
Router(config-if)# lacp fast-switchover

Step 5

lacp max-bundle

1

Sets the maximum number of active member ports to 14.

Example:

Note

Router(config-if)# lacp max-bundle 14

For Cisco ASR 1000 Series Aggregation Services Routers,
the minimum number of active member ports is 1 and the
maximum number is 14.

LAN Switching Configuration Guide
121


EtherChannel Flow-Based Limited 1 1 Redundancy
Configuring EtherChannel Flow-Based Limited 1 1 Redundancy with Fast-Switchover

Step 6

Command or Action

Purpose

exit

Exits interface configuration mode and returns to global
configuration mode.

Example:
Router(config-if)# exit

Step 7

interface tengigabitethernet

slot / port / number Selects the first interface to add to the port channel.

Example:
Router(config)# interface tengigabitethernet 0/0/0

Step 8

Adds the member link to the port-channel and actively
participates in LACP negotiation.

channel-group 1 mode mode
Example:
Router(config-if)# channel-group 1 mode active

Step 9

Sets the priority on the port-channel. This priority is set to
the default value.

lacp port-priority priority
Example:
Router(config-if)# lacp port-priority 32768

Step 10

Exits interface configuration mode and returns to global
configuration mode.

exit
Example:
Router(config-if)# exit

Step 11

interface tengigabitethernet

slot / port / number Selects the interface to add to the port channel.

Example:
Router(config)# interface tengigabitethernet 1/0/0

Step 12

channel-group 1 mode mode
Example:

Adds the member link to the port-channel and actively
participates in LACP negotiation.

Router(config-if)# channel-group 1 mode active

Step 13

lacp port-priority priority
Example:
Router(config-if)# lacp port-priority 32767

Step 14

Exits interface configuration mode.

end
Example:
Router(config-if)# end

LAN Switching Configuration Guide
122

Sets the port priority higher than the other link by using a
value lower than the default value of 32768. This forces
this link to be the active link whenever it is capable of
carrying traffic.


EtherChannel Flow-Based Limited 1 1 Redundancy
Setting the Switchover Rate with Carrier Delay

Setting the Switchover Rate with Carrier Delay
Optionally, you can control the speed of the switchover between the active and standby links by setting the
carrier delay on each link. The carrier-delay command controls how long it takes for Cisco IOS to propagate
the information about the links status to other modules.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
interface tengigabitethernet
carrier-delay msec msec
end

slot / port / number

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

Enters global configuration mode.

configure terminal
Example:
Router# configure terminal

Step 3

interface tengigabitethernet
Example:

slot / port / number Enters interface configuration mode and opens the
configuration for the specified interface.

Router(config)# interface tengigabitethernet 0/1/0

Step 4

carrier-delay msec msec
Example:

Sets how long it takes to propagate the link status to other
modules.

Router(config-if)# carrier-delay msec 11

Step 5

Exits interface configuration mode.

end
Example:
Router(config-if)# end

Verifying EtherChannel Flow-Based Limited 1 1 Redundancy
Use these show commands to verify the configuration and to display information about the port channel.

LAN Switching Configuration Guide
123


EtherChannel Flow-Based Limited 1 1 Redundancy
Verifying EtherChannel Flow-Based Limited 1 1 Redundancy

SUMMARY STEPS
1.
2.
3.
4.
5.

enable
show running-config interface type slot / port / number
show interfaces port-channel channel-number etherchannel
show etherchannel channel-number port-channel
end

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

show running-config interface type slot / port /
number

Verifies the configuration.
• type --gigabitethernet or tengigabitethernet.

Example:
Router# show running-config interface
tengigabitethernet 0/0/0

Step 3

show interfaces port-channel channel-number
etherchannel

Displays the bucket distribution currently in use.

Example:
Router# show interfaces port-channel 1 etherchannel

Step 4

show etherchannel channel-number port-channel

Displays the port channel fast-switchover feature capability.

Example:
Router# show etherchannel 1 port-channel

Step 5

Exits privileged EXEC mode.

end
Example:
Router# end

LAN Switching Configuration Guide
124


EtherChannel Flow-Based Limited 1 1 Redundancy
Configuration Examples for EtherChannel Flow-Based Limited1 1 Redundancy

Configuration Examples for EtherChannel Flow-Based Limited1
1 Redundancy
EtherChannel 1 1 Active Standby Example
This example shows how to configure a port channel for 1:1 link redundancy for equal priority ports so there
is no preference which port is active.
Router# enable
Router# configure terminal
Router(config)# interface port-channel 2
Router(config-if)# ip address 10.1.1.1 255.255.0.0
Router(config-if)# negotiation auto
Router(config-if)# lacp max-bundle 1
Router(config-if)# lacp fast-switchover
Router(config)# interface Tengigabitethernet0/1/0
Router(config-if)# channel-group 2 mode active
Router(config-if)# negotiation auto
Router(config)# interface Tengigabitethernet 2/1/0
Router(config-if)# channel-group 2 mode active
Router(config-if)# negotiation auto
Router(config)# interface GigabitEthernet0/1/6
Router(config-if)# negotiation auto
Router(config-if)# channel-group 19 mode active
Router(config)# interface GigabitEthernet0/1/7
Router(config-if)# negotiation auto
Router(config-if)# channel-group 19 mode active
Router(config-if)# interface Port-channel19
Router(config-if)# ip address 10.19.1.1 255.255.255.0
Router(config-if)# no negotiation auto
Router(config-if)# lacp fast-switchover
Router(config-if)# lacp max-bundle 1
Router(config-if)# end

Notice in the show command display the priorities are the same value.
Router# show lacp internal
Flags: S - Device is requesting Slow LACPDUs
F - Device is requesting Fast LACPDUs
A - Device is in Active mode P - Device is in Passive mode
Channel group 19
LACP port Admin Oper Port Port
Port Flags State Priority Key Key Number State
Gi0/1/6 SA bndl 32768 0x13 0x13 0x47 0x3D
Gi0/1/7 FA hot-sby 32768 0x13 0x13 0x48 0x7

Setting Priority for 1 1 Redundancy Using LACP Example
This example shows how to configure an LACP EtherChannel with 1:1 redundancy. GigabitEthernet 0/1/7
is the active link, because it is configured with a lower number which give it a higher port priority.
Router# configure terminal
Router(config)# interface GigabitEthernet0/1/6

LAN Switching Configuration Guide
125


EtherChannel Flow-Based Limited 1 1 Redundancy
Additional References

Router(config-if)# lacp port-priority 32767
Router(config-if)# exit
Router(config)# interface GigabitEthernet0/1/7
Router(config-if)# lacp fast-switchover
Router(config-if)# lacp max-bundle 1
Router(config-if)# negotiation auto
Router(config-if)# channel-group 19 mode active

In this show display, notice that the bundled link is set at a higher priority. This will ensure that the bundled
link is used as the first active link in the standby configuration.
Router# show lacp internal
Flags: S - Device is requesting Slow LACPDUs
F - Device is requesting Fast LACPDUs
A - Device is in Active mode P - Device is in Passive mode
Channel group 19
LACP port Admin Oper Port Port
Port Flags State Priority Key Key Number State
Gi0/1/6 FA hot-sby 32768 0x13 0x13 0x47 0x7
Gi0/1/7 SA bndl 32767 0x13 0x13 0x48 0x3D

Additional References
The following sections provide references related to the EtherChannel Flow-based Limited1:1 Redundancy
feature.
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

LAN Switching commands Cisco IOS LAN Switching Command Reference
Standards
Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not -been modified by this feature.
MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this To locate and download MIBs for selected platforms, Cisco
feature, and support for existing MIBs has not IOS XE software releases, and feature sets, use Cisco MIB
been modified by this feature.
Locator found at the following URL:
http://www.cisco.com/go/mibs

LAN Switching Configuration Guide
126


EtherChannel Flow-Based Limited 1 1 Redundancy
Feature Information for EtherChannel Flow-based Limited 1 1 Redundancy

RFCs
RFC

Title

No new or modified RFCs are supported by this feature, and support for existing standards has not
been modified by this feature.

--

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

Feature Information for EtherChannel Flow-based Limited 1 1
Redundancy
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

LAN Switching Configuration Guide
127


EtherChannel Flow-Based Limited 1 1 Redundancy
Feature Information for EtherChannel Flow-based Limited 1 1 Redundancy

Table 12: Feature Information for EtherChannel Flow-based Limited 1:1 Redundancy

Feature Name

Releases

Feature Information

EtherChannel
Flow-Based
Limited 1:1
Redundancy

Cisco IOS XE EtherChannel flow-based limited 1:1 redundancy provides MAC, or
Release 2.4
layer 2, traffic protection to avoid higher layer protocols from reacting
to single link failures and re-converging. To use EtherChannel
flow-based limited 1:1 redundancy, you configure an EtherChannel
with two ports (one active and one standby). If the active link goes
down, the EtherChannel stays up and the system performs fast
switchover to the hot-standby link. Depending on how you have the
priorities set, when the failed link becomes operational again, the
EtherChannel performs another fast switchover to revert to the original
active link. if all port-priorities are the same, it will not revert, but
remain on the current active link.
No commands were modified or created to support this feature.

LAN Switching Configuration Guide
128
