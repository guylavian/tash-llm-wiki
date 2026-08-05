---
title: "Enabling OSPFv2 on an Interface Basis"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-enabling-ospfv2-on-an-interface-basis
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 43 Enabling OSPFv2 on an Interface Basis This document describes how to enable Open Shortest Path First version 2 (OSPFv2) on a per-interface basis to simplify the configuration of unnumbered interfaces. The ip ospf area command allows you to enable OSPFv2 explicitly on an interface. The ip ospf area command is an alternative to enabling OSPFv2 through the address of the interface that m"
---

# Enabling OSPFv2 on an Interface Basis

CHAPTER

43

Enabling OSPFv2 on an Interface Basis
This document describes how to enable Open Shortest Path First version 2 (OSPFv2) on a per-interface basis
to simplify the configuration of unnumbered interfaces. The ip ospf area command allows you to enable
OSPFv2 explicitly on an interface. The ip ospf area command is an alternative to enabling OSPFv2 through
the address of the interface that matches the address range specified by the network area command.
• Finding Feature Information, page 409
• Prerequisites for Enabling OSPFv2 on an Interface Basis, page 409
• Restrictions on Enabling OSPFv2 on an Interface Basis, page 410
• Information About Enabling OSPFv2 on an Interface Basis, page 410
• How to Enable OSPFv2 on an Interface Basis, page 411
• Configuration Example for Enabling OSPFv2 on an Interface, page 412
• Additional References, page 413
• Feature Information for Enabling OSPFv2 on an Interface Basis, page 414

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for Enabling OSPFv2 on an Interface Basis
OSPFv2 must be running on your network.

IP Routing: OSPF Configuration Guide
409


Enabling OSPFv2 on an Interface Basis
Restrictions on Enabling OSPFv2 on an Interface Basis

Restrictions on Enabling OSPFv2 on an Interface Basis
The ip ospf area command is supported only for OSPFv2.

Information About Enabling OSPFv2 on an Interface Basis
Benefits of Enabling OSPFv2 on an Interface Basis
OSPF is enabled on an interface when the network address for the interface matches the range of addresses
that is specified by the network area command, which is entered in router configuration mode. Alternatively,
you can enable OSPFv2 explicitly on an interface by using the ip ospf area command, which is entered in
interface configuration mode. This capability simplifies the configuration of unnumbered interfaces with
different areas.
Because the ip ospf area command is configured explicitly for an interface, it supersedes the effects of the
network areacommand, which is entered at the network level to affect the interfaces whose addresses fall
within the address range specified for the network area command.
If you later disable the ip ospf area command, the interface still will run OSPFv2 as long as its network
address matches the range of addresses that is specified by the network areacommand.

Implications of Configuring OSPFv2 On a Router Basis or an Interface Basis
Before you use the ip ospf area command to enable OSPFv2 on an interface, we recommend that you
understand the following scenarios and command behavior. There are implications to using the network
areacommand (configuring OSPFv2 in router configuration mode) versus using the ip ospf area command
(configuring OSPFv2 in interface configuration mode).
Interface Is Already OSPFv2-Enabled by network area Command with Same Area and Process
If you enter the ip ospf area command on an interface that is enabled in OSPFv2 by the network areacommand,
the process ID or area ID of the interface does not change, and the interface status will not be changed.
However, the interface will be flagged as being configured from interface configuration mode, and the
configuration data will be saved in the interface description block (IDB).
Interface Is Already Configured by network area Command with Different Area or Process
If you enter the ip ospf area command on an interface that is enabled in OSPFv2 by the network areacommand,
but you change the configuration by changing the process ID and area ID of the interface, after the new
configuration information is stored in the IDB, the interface will be removed and reattached. Therefore, the
interface will be removed from the original area and process and be added to the new ones. The state of the
interface will also be reset.
Interface Is Not Configured by network area Command
If the interface is not enabled in OSPFv2 by the network area command, the area and OSPF router instance
will be created if needed. When the router is reloaded, the OSPF process will not begin running until system

IP Routing: OSPF Configuration Guide
410


Enabling OSPFv2 on an Interface Basis
How to Enable OSPFv2 on an Interface Basis

initialization is complete. To remove an OSPF router instance, enter the no router ospf command. Removing
the ip ospf area command in interface mode will not result in removing an OSPF router instance.
Removing an ip ospf area Command
When the ip ospf areacommand is removed, the interface will be detached from the area. The area will be
removed if it has no other attached interfaces. If the interface address is covered by the network area command,
the interface will be enabled once again in the area for the network that it is in.
New Processes
If an OSPF process does not already exist, and a router ID cannot be chosen when either the router ospf
command or the interface command is configured, a Proximity Database (PDB) and a process will be created,
but the process will be inactive. The process will become active when a router ID is chosen, either when it is
explicitly configured using the router-id command or when an IP address becomes available. Note that the
router ospf command will now be accepted even if a router ID cannot be chosen, putting the command-line
interface (CLI) into the OSPF configuration context. Therefore, the router-id command is to be entered before
an IP address is available. If the process is not active and the show ip ospfcommand is entered, the message
"%OSPF: Router process X is not running, please provide a router-id" will be displayed.
Link-State Advertisements and Shortest Path First
If a state change occurs as a result of the ip ospf areacommand, new router link-state advertisements (LSAs)
will be generated (also for the old area, if the interface is changing areas) and shortest path first (SPF) will be
scheduled to run in both the old and new areas.

How to Enable OSPFv2 on an Interface Basis
Enabling OSPFv2 on an Interface
SUMMARY STEPS
1. enable
2. configure terminal
number
3. interface type
ip
ospf
process-id
area area-id [secondaries none]
4.
5. end
6. show ip ospf interface [type -number]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: OSPF Configuration Guide
411


Enabling OSPFv2 on an Interface Basis
Configuration Example for Enabling OSPFv2 on an Interface

Command or Action

Purpose
• Enter your password if prompted.

Example:
Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

interface type

number

Configures an interface type and enters interface configuration
mode.

Example:
Device(config)# interface GigabitEthernet
0/2/1

Step 4

ip ospf process-id area area-id [secondaries
none]

Enables OSPFv2 on an interface.
• To prevent secondary IP addresses on the interface from
being advertised, you must enter the optional secondaries
keyword followed by the none keyword.

Example:
Device(config-if)# ip ospf 1 area 0
secondaries none

Step 5

Exits interface configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-if)# end

Step 6

show ip ospf interface [type -number]

Displays OSPF-related interface information.

Example:
Device# show ip ospf interface
GigabitEthernet 0/2/1

• Once you have enabled OSPFv2 on the interface, you can
enter the show ip ospf interfacecommand to verify the
configuration.

Configuration Example for Enabling OSPFv2 on an Interface
Example Enabling OSPFv2 on an Interface
In the following example, OSPFv2 is configured explicitly on GigabitEthernet interface 0/0/0:
Device(config)# interface GigabitEthernet 0/2/1
Device(config-if)# bandwidth 10000

IP Routing: OSPF Configuration Guide
412


Enabling OSPFv2 on an Interface Basis
Additional References

Device(config-if)# ip address 172.16.1.1 255.255.255.0
Device(config-if)# ip ospf hello-interval 1
Device(config-if)# ip ospf 1 area 0

When the show ip ospf interface command is entered, the following output shows that GigabitEthernet
interface 0/0/0 was configured in interface configuration mode to run OSPFv2. The secondary IP addresses
on the interface will also be advertised:
Device# show ip ospf interface GigabitEthernet 0/2/1
GigabitEthernet0/0/0 is up, line protocol is up
Internet Address 172.16.1.1/24, Area 0
Process ID 1, Router ID 172.16.11.11, Network Type BROADCAST, Cost: 10
Enabled by interface config, including secondary ip addresses
Transmit Delay is 1 sec, State DR, Priority 1
Designated Router (ID) 172.16.11.11, Interface address 172.16.1.1
Backup Designated router (ID) 172.16.22.11, Interface address 172.16.1.2
Timer intervals configured, Hello 1, Dead 4, Wait 4, Retransmit 5
oob-resync timeout 40
Hello due in 00:00:00
Supports Link-local Signaling (LLS)
Index 2/2, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 172.26.22.11 (Backup Designated Router)
Suppress hello for 0 neighbor(s)

Additional References
The following sections provide references related to enabling OSPFv2 on an interface.
Related Documents
Related Topic

Document Title

Configuring OSPF

Configuring OSPF

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standard

Title

No new or modified standards are supported by this -feature, and support for existing standards has not
been modified by this feature.

IP Routing: OSPF Configuration Guide
413


Enabling OSPFv2 on an Interface Basis
Feature Information for Enabling OSPFv2 on an Interface Basis

MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS XE releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

RFC 2328

OSPF Version 2

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

Feature Information for Enabling OSPFv2 on an Interface Basis
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
414


Enabling OSPFv2 on an Interface Basis
Feature Information for Enabling OSPFv2 on an Interface Basis

Table 49: Feature Information for Enabling OSPFv2 on an Interface Basis

Feature Name

Releases

Enabling OSPFv2 on an Interface Cisco IOS XE Release 2.1
Basis
Note

This feature was
originally named "Area
Command in Interface
Mode for OSPFv2."

Feature Information
This document describes how to
enable OSPFv2 on a per-interface
basis to simplify the configuration
of unnumbered interfaces. The ip
ospf area command allows you to
enable OSPFv2 explicitly on an
interface. The ip ospf area
command is an alternative to
enabling OSPFv2 through the
address of the interface that
matches the address range specified
by the network area command.
The following commands are
introduced or modified in the
feature documented in this module:
• ip ospf area.

IP Routing: OSPF Configuration Guide
415


Enabling OSPFv2 on an Interface Basis
Feature Information for Enabling OSPFv2 on an Interface Basis

IP Routing: OSPF Configuration Guide
416
