---
title: "OSPF Support for Fast Hello Packets"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-support-for-fast-hello-packets
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 25 OSPF Support for Fast Hello Packets The OSPF Support for Fast Hello Packets feature provides a way to configure the sending of hello packets in intervals less than 1 second. Such a configuration results in faster convergence in an Open Shortest Path First (OSPF) network. Note It is recommended to use Bidirectional Forwarding Detection (BFD) instead of Fast Hello Packets. • Finding F"
---

# OSPF Support for Fast Hello Packets

CHAPTER

25

OSPF Support for Fast Hello Packets
The OSPF Support for Fast Hello Packets feature provides a way to configure the sending of hello packets
in intervals less than 1 second. Such a configuration results in faster convergence in an Open Shortest Path
First (OSPF) network.

Note

It is recommended to use Bidirectional Forwarding Detection (BFD) instead of Fast Hello Packets.
• Finding Feature Information, page 251
• Prerequisites for OSPF Support for Fast Hello Packets, page 251
• Information About OSPF Support for Fast Hello Packets, page 252
• How to Configure OSPF Fast Hello Packets, page 253
• Configuration Examples for OSPF Support for Fast Hello Packets, page 254
• Additional References, page 255
• Feature Information for OSPF Support for Fast Hello Packets, page 256

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPF Support for Fast Hello Packets
OSPF must be already configured in the network or must be configured at the same time as the OSPF Support
for Fast Hello Packets feature.

IP Routing: OSPF Configuration Guide
251


OSPF Support for Fast Hello Packets
Information About OSPF Support for Fast Hello Packets

Information About OSPF Support for Fast Hello Packets
OSPF Hello Interval and Dead Interval
OSPF hello packets are packets that an OSPF process sends to its OSPF neighbors to maintain connectivity
with those neighbors. The hello packets are sent at a configurable interval (in seconds). The defaults are 10
seconds for an Ethernet link and 30 seconds for a non broadcast link. Hello packets include a list of all neighbors
for which a hello packet has been received within the dead interval. The dead interval is also a configurable
interval (in seconds), and defaults to four times the value of the hello interval. The value of all hello intervals
must be the same within a network. Likewise, the value of all dead intervals must be the same within a network.
These two intervals work together to maintain connectivity by indicating that the link is operational. If a router
does not receive a hello packet from a neighbor within the dead interval, it will declare that neighbor to be
down.

OSPF Fast Hello Packets
OSPF fast hello packets refer to hello packets being sent at intervals of less than 1 second. To understand fast
hello packets, you should already understand the relationship between OSPF hello packets and the dead
interval. See the section OSPF Hello Interval and Dead Interval, on page 252.
OSPF fast hello packets are achieved by using the ip ospf dead-interval command. The dead interval is set
to 1 second, and the hello-multiplier value is set to the number of hello packets you want to send during that
1 second, thus providing subsecond or "fast" hello packets.
When fast hello packets are configured on the interface, the hello interval advertised in the hello packets that
are sent out this interface is set to 0. The hello interval in the hello packets received over this interface is
ignored.
The dead interval must be consistent on a segment, whether it is set to 1 second (for fast hello packets) or set
to any other value. The hello multiplier need not be the same for the entire segment as long as at least one
hello packet is sent within the dead interval.

Benefits of OSPF Fast Hello Packets
The benefit of the OSPF Support for Fast Hello Packets feature is that your OSPF network will experience
faster convergence time than it would without fast hello packets. This feature allows you to detect lost neighbors
within 1 second. It is especially useful in LAN segments, where neighbor loss might not be detected by the
Open System Interconnection (OSI) physical layer and data-link layer.

IP Routing: OSPF Configuration Guide
252


OSPF Support for Fast Hello Packets
How to Configure OSPF Fast Hello Packets

How to Configure OSPF Fast Hello Packets
Configuring OSPF Fast Hello Packets
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. ip ospf dead-interval minimal hello-multiplier multiplier
5. end
6. show ip ospf interface [interface-type interface-number]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged EXEC mode.
Enter your password if prompted.

Example:
Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

interface type number

Configures an interface type and enters interface configuration mode.

Example:
Router(config)# interface
gigabitethernet 0/0/1

Step 4

ip ospf dead-interval minimal
hello-multiplier multiplier
Example:
Router(config-if)# ip ospf dead-interval
minimal hello-multiplier 5

Sets the interval during which at least one hello packet must be
received, or else the neighbor is considered down.
• In the example, OSPF Support for Fast Hello Packets is enabled
by specifying the minimal keyword and the hello-multiplier
keyword and value. Because the multiplier is set to 5, five hello
packets will be sent every second.

IP Routing: OSPF Configuration Guide
253


OSPF Support for Fast Hello Packets
Configuration Examples for OSPF Support for Fast Hello Packets

Step 5

Command or Action

Purpose

end

(Optional) Saves configuration commands to the running configuration
file, exits configuration mode, and returns to privileged EXEC mode.

Example:
Router(config-if)# end

Step 6

show ip ospf interface [interface-type
interface-number]
Example:

• Use this command when you are ready to exit configuration mode
and save the configuration to the running configuration file.
(Optional) Displays OSPF-related interface information.
• The relevant fields that verify OSPF fast hello packets are
indicated in the sample output following this table.

Router# show ip ospf interface
gigabitethernet 0/0/1

Examples
The following sample output verifies that OSPF Support for Fast Hello Packets is configured. In the line that
begins with "Timer intervals configured," the hello interval is 200 milliseconds, the dead interval is 1 second,
and the next hello packet is due in 76 milliseconds.
Router# show ip ospf interface gigabitethernet 0/0/1
GigabitEthernet0/0/1 is up, line protocol is up
Internet Address 172.16.1.2/24, Area 0
Process ID 1, Router ID 172.17.0.2, Network Type BROADCAST, Cost:1
Transmit Delay is 1 sec, State DR, Priority 1
Designated Router (ID) 172.17.0.2, Interface address 172.16.1.2
Backup Designated router (ID) 172.16.0.1, Interface address 172.16.1.1
Timer intervals configured, Hello 200 msec, Dead 1, Wait 1, Retransmit 5
Hello due in 76 msec
Index 2/2, flood queue length 0
Next 0x0(0)/0x0(0)
Last flood scan length is 2, maximum is 3
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 172.16.0.1 (Backup Designated Router)
Suppress hello for 0 neighbor(s)

Configuration Examples for OSPF Support for Fast Hello Packets
Example OSPF Fast Hello Packets
The following example configures OSPF fast hello packets; the dead interval is 1 second and 5 hello packets
are sent every second:
interface gigabitethernet 0/0/1
ip ospf dead-interval minimal hello-multiplier 5

IP Routing: OSPF Configuration Guide
254


OSPF Support for Fast Hello Packets
Additional References

Additional References
Related Documents
Related Topic

Document Title

IPv6 addressing and connectivity

IPv6 Configuration Guide

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

IPv6 commands

Cisco IOS IPv6 Command
Reference

Cisco IOS IPv6 features

Cisco IOS IPv6 Feature Mapping

OSPFv3 External Path Preference Option

“Configuring OSPF” module

Standards and RFCs
Standard/RFC

Title

RFCs for IPv6

IPv6 RFCs

MIBs
MIB

MIBs Link
To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

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

IP Routing: OSPF Configuration Guide
255


OSPF Support for Fast Hello Packets
Feature Information for OSPF Support for Fast Hello Packets

Feature Information for OSPF Support for Fast Hello Packets
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 28: Feature Information for OSPF Support for Fast Hello Packets

Feature Name

Releases

Feature Information

OSPF Support for Fast Hello
Packets

Cisco IOS XE Release 2.1

The OSPF Support for Fast Hello
Packets feature provides a way to
configure the sending of hello
packets in intervals less than 1
second. Such a configuration
results in faster convergence in an
Open Shortest Path First (OSPF)
network.

IP Routing: OSPF Configuration Guide
256
