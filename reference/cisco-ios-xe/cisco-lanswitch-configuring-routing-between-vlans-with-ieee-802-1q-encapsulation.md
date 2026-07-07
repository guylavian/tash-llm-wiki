---
title: "Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation"
type: reference
domain: cisco-ios-xe
slug: cisco-lanswitch-configuring-routing-between-vlans-with-ieee-802-1q-encapsulation
tier: reference
source: "Cisco IOS XE 16 — LAN Switching Configuration Guide"
version: ios-xe-16
family: lan-switching
documentKind: "Documentation"
abstract: "CHAPTER 3 Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation This chapter describes the required and optional tasks for configuring routing between VLANs with IEEE 802.1Q encapsulation. • Restrictions for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation, on page 19 • Information About Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation, on page 19 • How"
---

# Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation

CHAPTER

3

Configuring Routing Between VLANs with IEEE
802.1Q Encapsulation
This chapter describes the required and optional tasks for configuring routing between VLANs with IEEE
802.1Q encapsulation.
• Restrictions for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation, on page 19
• Information About Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation, on page
19
• How to Configure Routing Between VLANs with IEEE 802.1Q Encapsulation, on page 20
• Configuration Examples for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation,
on page 24
• Additional References, on page 24
• Feature Information for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation, on
page 25

Restrictions for Configuring Routing Between VLANs with IEEE
802.1Q Encapsulation
Shared port adapters (SPAs) on Cisco ASR 1000 Series Aggregation Services Router have a limit of 8,000
TCAM entries, which limits the number of VLANs you can create on a single SPA.

Information About Configuring Routing Between VLANs with
IEEE 802.1Q Encapsulation
Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
The IEEE 802.1Q protocol is used to interconnect multiple switches and routers, and for defining VLAN
topologies. The IEEE 802.1Q standard is extremely restrictive to untagged frames. The standard provides
only a per-port VLANs solution for untagged frames. For example, assigning untagged frames to VLANs
takes into consideration only the port from which they have been received. Each port has a parameter called

LAN Switching Configuration Guide
19


Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
How to Configure Routing Between VLANs with IEEE 802.1Q Encapsulation

a permanent virtual identification (Native VLAN) that specifies the VLAN assigned to receive untagged
frames.
The main characteristics of IEEE 802.1Q are as follows:
• Assigns frames to VLANs by filtering.
• The standard assumes the presence of a single spanning tree and of an explicit tagging scheme with
one-level tagging.

How to Configure Routing Between VLANs with IEEE 802.1Q
Encapsulation
Configuring IP Routing over IEEE 802.1Q
IP routing over IEEE 802.1Q extends IP routing capabilities to include support for routing IP frame types in
VLAN configurations using the IEEE 802.1Q encapsulation.
To route IP over IEEE 802.1Q between VLANs, you need to customize the subinterface to create the
environment in which it will be used. Perform the tasks described in the following sections in the order in
which they appear:

Enabling IP Routing
IP routing is automatically enabled in the Cisco IOS XE software for routers. To reenable IP routing if it has
been disabled, perform the following steps.
Once you have IP routing enabled on the router, you can customize the characteristics to suit your environment.
If necessary, refer to the IP configuration chapters in the Cisco IOS XE IP Routing Protocols Configuration
Guide , Release 2, for guidelines on configuring IP.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
ip routing
end

DETAILED STEPS
Procedure

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Router> enable

LAN Switching Configuration Guide
20

• Enter your password if prompted.


Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
Defining the VLAN Encapsulation Format

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

Enables IP routing on the router.

ip routing
Example:
Router(config)# ip routing

Step 4

Exits privileged EXEC mode.

end
Example:
Router(config)# exit

Defining the VLAN Encapsulation Format
To define the encapsulation format as IEEE 802.1Q, perform the following steps.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
interface gigabitethernet card / spaslot / port . subinterface-number
encapsulation dot1q vlanid
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

interface gigabitethernet
subinterface-number

card / spaslot / port . Specifies the subinterface on which IEEE 802.1Q will be
used, and enters interface configuration mode.

Example:

LAN Switching Configuration Guide
21


Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
Assigning an IP Address to Network Interface

Command or Action

Purpose

Router(config)# interface gigabitethernet 0/0/0.101

Step 4

Defines the encapsulation format as IEEE 802.1Q (dot1q),
and specifies the VLAN identifier

encapsulation dot1q vlanid
Example:
Router(config-subif)# encapsulation dot1q 101

Step 5

Exits subinterface configuration mode.

end
Example:
Router(config-subif)# end

Assigning an IP Address to Network Interface
An interface can have one primary IP address. To assign a primary IP address and a network mask to a network
interface, perform the following steps.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
interface gigabitethernet card / spaslot / port . subinterface-number
ip address ip-address mask
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

interface gigabitethernet
subinterface-number

card / spaslot / port . Specifies the subinterface on which IEEE 802.1Q will be
used, and enters interface configuration mode.

Example:
Router(config)# interface gigabitethernet 0/0/0.101

LAN Switching Configuration Guide
22


Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
Monitoring and Maintaining VLAN Subinterfaces

Step 4

Command or Action

Purpose

ip address ip-address mask

Sets a primary IP address for an interface.

Example:

• Enter the primary IP address for an interface.

Router(config-subif)# ip address 10.0.0.0 255.0.0.0 Note

A mask identifies the bits that denote the network number
in an IP address. When you use the mask to subnet a
network, the mask is then referred to as a subnet mask.
Step 5

Exits subinterface configuration mode.

end
Example:
Router(config-subif)# end

Monitoring and Maintaining VLAN Subinterfaces
To indicate whether a VLAN is a native VLAN, perform the following steps.
SUMMARY STEPS
1. enable
2. show vlans
3. end
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

show vlans

Displays VLAN information.

Example:
Router# show vlans

Step 3

end

Exits privileged EXEC mode.

Example:
Router# end

LAN Switching Configuration Guide
23


Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
Configuration Examples for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation

Configuration Examples for Configuring Routing Between VLANs
with IEEE 802.1Q Encapsulation
Configuring IP Routing over IEEE 802.1Q Example
This configuration example shows IP being routed on VLAN 101:
!
ip routing
!
interface gigabitethernet 4/1/1.101
encapsulation dot1q 101
ip addr 10.0.0.0 255.0.0.0
!

Additional References
Related Documents
Related Topic

Document Title

IP LAN switching commands: complete command syntax,
command mode, defaults, usage guidelines, and examples

Cisco IOS LAN Switching Services Command
Reference

Standards
Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not -been modified by this feature.
MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this To locate and download MIBs for selected platforms, Cisco
feature, and support for existing MIBs has not IOS releases, and feature sets, use Cisco MIB Locator
been modified by this feature.
found at the following URL:
http://www.cisco.com/go/mibs

LAN Switching Configuration Guide
24


Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
Feature Information for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation

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

Feature Information for Configuring Routing Between VLANs
with IEEE 802.1Q Encapsulation
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.
Table 2: Feature Information for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation

Feature Name

Releases

Configuring Routing Between VLANs Cisco IOS XE Release
with IEEE 802.1Q Encapsulation
2.1

Feature Information
This feature was introduced on the Cisco
ASR 1000 Series Aggregation Services
Routers.

LAN Switching Configuration Guide
25


Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation
Feature Information for Configuring Routing Between VLANs with IEEE 802.1Q Encapsulation

LAN Switching Configuration Guide
26
