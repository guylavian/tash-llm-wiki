---
title: "VLANs over IP Unnumbered SubInterfaces"
type: reference
domain: cisco-ios-xe
slug: cisco-lanswitch-vlans-over-ip-unnumbered-subinterfaces
tier: reference
source: "Cisco IOS XE 16 — LAN Switching Configuration Guide"
version: ios-xe-16
family: lan-switching
documentKind: "Documentation"
abstract: "CHAPTER 9 VLANs over IP Unnumbered SubInterfaces The VLANs over IP Unnumbered Subinterfaces feature allows IP unnumbered interface support to be configured on Ethernet VLAN subinterfaces. This feature also provides support for DHCP on VLAN subinterfaces. Configuring Ethernet VLANs on IP unnumbered subinterfaces can save IPv4 address space and simplify configuration management, address management"
---

# VLANs over IP Unnumbered SubInterfaces

CHAPTER

9

VLANs over IP Unnumbered SubInterfaces
The VLANs over IP Unnumbered Subinterfaces feature allows IP unnumbered interface support to be configured
on Ethernet VLAN subinterfaces. This feature also provides support for DHCP on VLAN subinterfaces.
Configuring Ethernet VLANs on IP unnumbered subinterfaces can save IPv4 address space and simplify
configuration management, address management, and migration for DSL providers from ATM networks to
IP.
• Finding Feature Information, on page 139
• Prerequisites for VLANs over IP Unnumbered Subinterfaces, on page 139
• Restrictions for VLANs over IP Unnumbered Subinterfaces, on page 140
• Information About VLANs over IP Unnumbered Subinterfaces, on page 140
• How to Configure VLANs over IP Unnumbered Subinterfaces, on page 142
• Configuration Examples for VLANs over IP Unnumbered Subinterfaces, on page 145
• Additional References for VLANs over IP Unnumbered Subinterfaces, on page 145
• Feature Information for VLANs over IP Unnumbered Subinterfaces, on page 146

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.

Prerequisites for VLANs over IP Unnumbered Subinterfaces
Configure DHCP and ensure that it is operational.

LAN Switching Configuration Guide
139


VLANs over IP Unnumbered SubInterfaces
Restrictions for VLANs over IP Unnumbered Subinterfaces

Restrictions for VLANs over IP Unnumbered Subinterfaces
• Only Ethernet VLAN subinterfaces, in addition to serial interfaces, can be configured as IP unnumbered
interfaces.
• Interface ranges (the interface range command) are not supported in Cisco IOS Release 12.2(18)SXE.
• A physical interface cannot be used for Layer 3 services (no IP address configurations are supported on
the physical interface) if one of the subinterface is configured as native.

Information About VLANs over IP Unnumbered Subinterfaces
Support for VLANs over IP Unnumbered Subinterfaces
The VLANs over IP Unnumbered Subinterfaces feature enables Ethernet VLANs to be configured on IP
unnumbered subinterfaces. The IP unnumbered interface configuration enables IP processing on an interface
without assigning an IP address to the interface. The IP unnumbered interface borrows an IP address from
another interface that is already configured on the device to conserve network and address space.
Figure 1 shows the implementation of the VLANs over IP Unnumbered Subinterfaces feature in a sample
network topology. In this topology, the aggregation services routers dynamically establish IP routes when the
DHCP server assigns IP addresses to hosts.
Figure 24: Sample Network Topology Using VLANs over IP Unnumbered Subinterfaces Feature

The VLANs over IP Unnumbered Subinterfaces feature supports the following functions:
• Allocating peer IP address through DHCP.
• Configuring IP unnumbered interface support for a range of VLAN subinterfaces.
• Configuring service selection gateway support for VLANs over IP unnumbered subinterfaces.

LAN Switching Configuration Guide
140


VLANs over IP Unnumbered SubInterfaces
DHCP Option 82

• Supporting DHCP relay agent information feature (Option 82).

DHCP Option 82
DHCP provides a framework for passing configuration information to hosts on a TCP/IP network. Configuration
parameters and other control information are carried in tagged data items (also called options) that are stored
in the options field of the DHCP message. Option 82 is organized as a single DHCP option that contains
information known by the relay agent.
The DHCP Relay Agent Information feature communicates information to the DHCP server using a suboption
of the DHCP relay agent information option called agent remote ID. The information sent in the agent remote
ID includes an IP address identifying the relay agent and information about the interface and the connection
over which the DHCP request was received. The DHCP server uses this information to assign IP addresses
to interfaces and to form security policies.
Figure 2 shows the agent remote ID suboption format that is used with the VLANs over IP Unnumbered
Subinterfaces feature.
Figure 25: Format of the Agent Remote ID Suboption

Field

Description

Type

Format type (1 byte). Value 2 specifies the format for
use with this feature.

Length

Length of the agent remote ID suboption (1 byte). The
type field and the remaining bytes of the length field
are not included.

Reserved

Reserved (2 bytes).

NAS IP Address

Network-attached storage (NAS) IP address (4 bytes)
of the interface specified by the ip unnumbered
command.

Interface

Physical interface (1 byte). This field has the
following format:
slot (4 bits) | module (1 bit) | port (3 bits).
For example, if the interface is Ethernet 2/1/1, the slot
is 2, the module is 1, and the port is 1.

Reserved

Reserved (1 byte).

VLAN ID

VLAN identifier (2 bytes) for the Ethernet
subinterface.

LAN Switching Configuration Guide
141


VLANs over IP Unnumbered SubInterfaces
Benefits of VLANs over IP Unnumbered Subinterfaces

Benefits of VLANs over IP Unnumbered Subinterfaces
The VLANs over IP Unnumbered Subinterfaces feature provides the following benefits:
• Migration from other interfaces to Gigabit Ethernet uplinks and IP core becomes easier for DSL providers.
• All ports share the same subnet, therefore saving the IPv4 address space.
• Each user is on a separate VLAN. DHCP communicates routing information, and there is no Address
Resolution Protocol (ARP) or MAC address spoofing, which leads to enhancement in security layers.
• IP address management with DHCP becomes simpler.
• Configuring interface ranges with Ethernet VLAN subinterfaces leads to easier NVRAM configuration
and saves overall memory.

How to Configure VLANs over IP Unnumbered Subinterfaces
Configuring IP Unnumbered Interface Support on an Ethernet VLAN
Subinterface
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
interface type number [name-tag]
encapsulation dot1q vlan-id [native]
ip unnumbered type number
end
show running-config

DETAILED STEPS
Procedure

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
Example:
Device# configure terminal

LAN Switching Configuration Guide
142

Enters global configuration mode.


VLANs over IP Unnumbered SubInterfaces
Configuring IP Unnumbered Interface Support on a Range of Ethernet VLAN Subinterfaces

Step 3

Command or Action

Purpose

interface type number [name-tag]

Configures an interface type and enters interface or
subinterface configuration mode.

Example:
Device(config)# interface fastethernet 1/0.1

Step 4

encapsulation dot1q vlan-id [native]
Example:

Enables IEEE 802.1Q encapsulation of traffic on a specified
subinterface in a VLAN.

Device(config-subif)# encapsulation dot1q 10

Step 5

ip unnumbered type number
Example:
Device(config-subif)# ip unnumbered ethernet 3/0

Step 6

Enables IP processing on an interface without assigning an
explicit IP address to the interface.
• The type and number arguments specify an interface
with a predefined IP address on the device. Do not
specify an unnumbered interface, if one already exists.
Exits subinterface configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-subif)# end

Step 7

show running-config
Example:

Displays contents of the current running configuration file
on the device including the configuration of the IP
unnumbered support feature.

Device# show running-config

Configuring IP Unnumbered Interface Support on a Range of Ethernet VLAN
Subinterfaces
Note

The interface range command is not supported in Cisco IOS Release 12.2(18)SXE.

SUMMARY STEPS
1. enable
2. configure terminal
3. interface range {{ethernet | fastethernet | gigabitethernet | vlan vlan} slot/interface.subinterface {ethernet | fastethernet | gigabitethernet | vlan vlan} slot/interface.subinterface | macro macro-name}
4. encapsulation dot1q vlan-id [native]
5. ip unnumbered type number
6. end
7. show running-config

LAN Switching Configuration Guide
143


VLANs over IP Unnumbered SubInterfaces
Configuring IP Unnumbered Interface Support on a Range of Ethernet VLAN Subinterfaces

DETAILED STEPS
Procedure

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

interface range {{ethernet | fastethernet | gigabitethernet Executes commands on multiple subinterfaces
simultaneously. The device prompt changes to configuration
| vlan vlan} slot/interface.subinterface - {ethernet |
interface range mode after the commands are executed.
fastethernet | gigabitethernet | vlan vlan}
slot/interface.subinterface | macro macro-name}
• Separate the interface range with a hyphen and space
as shown in the example.
Example:
Device(config)# interface range fastethernet 1/0.1
- fastethernet 1/0.100

Step 4

encapsulation dot1q vlan-id [native]
Example:
Device(config-if-range)# encapsulation dot1q 10

Step 5

ip unnumbered type number
Example:
Device(config-if-range)# ip unnumbered ethernet
3/0

Step 6

end
Example:

Applies a unique VLAN ID to each subinterface within the
range.
• The VLAN ID specified by the vlan-id argument is
applied to the first subinterface in the range. Each
subsequent interface is assigned a VLAN ID, which
is the specified vlan-id including the subinterface
number and excluding the first subinterface number
(VLAN ID + subinterface number - first subinterface
number).
Enables IP processing on an interface without assigning an
explicit IP address to the interface.
• The type and number arguments specify an interface
with a predefined IP address on the device. Do not
specify an unnumbered interface, if one already exists.
Exits interface-range configuration mode and returns to
privileged EXEC mode.

Device(config-if-range)# end

Step 7

show running-config
Example:
Device# show running-config

LAN Switching Configuration Guide
144

Displays contents of the current running configuration file
on the device including the configuration of the IP
unnumbered support feature.


VLANs over IP Unnumbered SubInterfaces
Configuration Examples for VLANs over IP Unnumbered Subinterfaces

Configuration Examples for VLANs over IP Unnumbered
Subinterfaces
Example: VLAN Configuration on a Single IP Unnumbered Subinterface
The following example shows how to configure IP unnumbered subinterface using Ethernet VLAN subinterface
3/0.2:
interface ethernet 3/0.2
encapsulation dot1q 200
ip unnumbered ethernet 3/1

Example: VLAN Configuration on a Range of IP Unnumbered Subinterfaces
The following example shows how to configure IP unnumbered subinterfaces using Fast Ethernet subinterfaces
in the range from 5/1.1 to 5/1.4:
interface range fastethernet 5/1.1 - fastethernet 5/1.4
ip unnumbered ethernet 3/1

Additional References for VLANs over IP Unnumbered
Subinterfaces
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

IP Addressing commands

Cisco IOS IP Addressing Services Command
Reference

IP Addressing Services configuration tasks

Cisco IOS IP Addressing Services Configuration
Guide

VLAN configuration tasks

Cisco IOS LAN Switching Configuration Guide

VLAN configuration commands

Cisco IOS LAN Switching Command Reference

RFCs
RFCs

Title

RFC 1812

Requirements for IP Version 4 Routers, June 1995

LAN Switching Configuration Guide
145


VLANs over IP Unnumbered SubInterfaces
Feature Information for VLANs over IP Unnumbered Subinterfaces

Technical Assistance
Description

Link

The Cisco Support and Documentation website
http://www.cisco.com/cisco/web/support/index.html
provides online resources to download documentation,
software, and tools. Use these resources to install and
configure the software and to troubleshoot and resolve
technical issues with Cisco products and technologies.
Access to most tools on the Cisco Support and
Documentation website requires a Cisco.com user ID
and password.

Feature Information for VLANs over IP Unnumbered
Subinterfaces
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.
Table 17: Feature Information for VLANs over IP Unnumbered Subinterfaces

Feature Name

Releases

Feature Information

VLANs over IP Unnumbered
Subinterfaces

Cisco IOS XE Release 3.9S

The VLANs over IP Unnumbered
Subinterfaces feature allows IP
unnumbered interface support to be
configured on Ethernet VLAN
subinterfaces. This feature also
provides support for DHCP on
VLAN subinterfaces. Configuring
Ethernet VLANs on IP unnumbered
subinterfaces can save IPv4 address
space and simplify configuration
management, address management,
and migration for DSL providers
from ATM networks to IP.
The following command was
modified:
ip unnumbered

LAN Switching Configuration Guide
146
