---
title: "OSPF SNMP ifIndex Value for Interface ID in Data Fields"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-snmp-ifindex-value-for-interface-id-in-data-fields
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 40 OSPF SNMP ifIndex Value for Interface ID in Data Fields This feature allows you to configure the interface ID value Open Shortest Path First version 2 (OSPFv2) and Open Shortest Path First version 3 (OSPFv3) data fields. You can choose to use either the current interface number or the Simple Network Management Protocol (SNMP) MIB-II interface index (ifIndex) value for the interface ID"
---

# OSPF SNMP ifIndex Value for Interface ID in Data Fields

CHAPTER

40

OSPF SNMP ifIndex Value for Interface ID in Data
Fields
This feature allows you to configure the interface ID value Open Shortest Path First version 2 (OSPFv2)
and Open Shortest Path First version 3 (OSPFv3) data fields. You can choose to use either the current interface
number or the Simple Network Management Protocol (SNMP) MIB-II interface index (ifIndex) value for
the interface ID. The advantage to using the SNMP MIB-II ifIndex value is that this number corresponds to
the number that the user will see reported by SNMP.
• Finding Feature Information, page 381
• Prerequisites for SNMP ifIndex Value for Interface ID in Data Fields, page 382
• Information About SNMP ifIndex Value for Interface ID in Data Fields, page 382
• How to Configure SNMP ifIndex Value for Interface ID in Data Fields, page 383
• Configuration Examples for SNMP ifIndex Value for Interface ID in Data Fields, page 384
• Additional References, page 388
• Feature Information for OSPF SNMP ifIndex Value for Interface ID, page 389

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
381


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Prerequisites for SNMP ifIndex Value for Interface ID in Data Fields

Prerequisites for SNMP ifIndex Value for Interface ID in Data
Fields
Before you can use the SNMP ifIndex value for interface identification, OSPF must be configured on the
router.

Information About SNMP ifIndex Value for Interface ID in Data
Fields
Benefits of Choosing to Identify Interfaces by the SNMP MIB-II ifIndex Value
If you use SNMP for your OSPF network, configuring the OSPF: SNMP ifIndex Value for Interface ID in
OSPFv2 and OSPFv3 Data Fields feature can be beneficial for the following reasons:
• Using the SNMP MIB-II ifIndex identification numbers to identify OSPF interfaces makes it easier for
network administrators to identify interfaces because the numbers will correspond to the numbers that
they will see reported by SNMP.
• In the link-state advertisements (LSAs), the value used in fields that have the interface ID will be the
same as the value that is reported by SNMP.
• In the output from the show ipv6 ospf interface command, the interface ID number will have the same
value that is reported by SNMP.
• Using the SNMP MIB-II IfIndex is also suggested, but not required, by the OSPF RFC 2328 for OSPFv2
and the RFC 2740 for OSPFv3.

How OSPFv2 and OSPFv3 Use the SNMP MIB-II ifIndex Value
The user chooses for OSPF interfaces to use the SNMP MIB-II ifIndex number by entering the interface-id
snmp-if-index command for a specific OSPF process. If an interface under the specific OSPF process does
not have an SNMP ifIndex number, OSPF will not be enabled on that interface.
For OSPFv2, the ifIndex number is used for the Link Data field in the Router LSA for unnumbered
point-to-point interfaces and sham links. When the interface-id snmp-if-index command is entered, the
affected LSAs will immediately be reoriginated.
For OSPFv3, the ifIndex number is used for the interface ID in router LSAs, as the LSID in Network and
Link LSAs, and also as the interface ID in Hello packets. Intra-Area-Prefix LSAs that reference Network
LSAs have the Network LSAs LSID in the Referenced LSID field, so they will also be updated when the
interface-id snmp-if-index command is entered. The old Network, Link, and Intra-Area-Prefix LSAs that
are associated with a Network LSA will be flushed.
For both OSPFv2 and OSPFv3, adjacencies are not flapped, except for affected OSPFv3 demand circuits
(including virtual links) with full adjacencies.

IP Routing: OSPF Configuration Guide
382


OSPF SNMP ifIndex Value for Interface ID in Data Fields
How to Configure SNMP ifIndex Value for Interface ID in Data Fields

For both OSPFv2 and OSPFv3, if an interface does not have an SNMP ifIndex number and an interface ID
is needed (for OSPFv2 this applies only to unnumbered interfaces and sham links), an error message will be
generated and the interface will be disabled. The interface will be reenabled if the no interface-id snmp-if-index
command is entered.

How to Configure SNMP ifIndex Value for Interface ID in Data
Fields
Configuring OSPF interfaces to use SNMP MIB-II ifIndex Numbers
SUMMARY STEPS
1. enable
2. configure terminal
3. Do one of the following:
• router ospf process-id [vrf vpn-name]
•
• ipv6 router ospf process-id
4. interface-id snmp-if-index
5. end
6. show snmp mib ifmib ifindex [type number] [detail][free-list]

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

Do one of the following:
• router ospf process-id [vrf vpn-name]
•
• ipv6 router ospf process-id

Configures an OSPFv2 routing process and enters router
configuration mode.
Configures an OSPFv3 routing process and enters router
configuration mode.

IP Routing: OSPF Configuration Guide
383


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Configuration Examples for SNMP ifIndex Value for Interface ID in Data Fields

Command or Action

Purpose
Note

Example:

If you configure an OSPFv3 routing process, that uses
IPv6, you must have already enabled IPv6.

Device(config)# router ospf 4

Example:

Example:
Device(config)# ipv6 router ospf 4

Step 4

interface-id snmp-if-index

Configures OSPF interfaces with the SNMP interface index
identification numbers (ifIndex values).

Example:
Device(config-router)# interface-id
snmp-if-index

Step 5

end

Returns to privileged EXEC mode.

Example:

Repeat this task for each OSPF process for which you want the
interfaces to use the SNMP MIB-II ifIndex numbers.

Device(config-router)# end

Step 6

show snmp mib ifmib ifindex [type number]
[detail][free-list]

Displays SNMP interface index identification numbers (ifIndex
values) for all the system interfaces or the specified system
interface.

Example:
Device# show snmp mib ifmib ifindex
GigabitEtherent 0/0

Configuration Examples for SNMP ifIndex Value for Interface
ID in Data Fields
Example Configuring SNMP ifIndex Value for Interface ID for OSPFv2
The following example configures the OSPF interfaces to use the SNMP ifIndex values for the interfaces IDs.
The show snmp mib ifmib ifindex command confirms that the SNMP MIB-II ifIndex values are used for
the interface ID values in the OSPFv2 data fields.
Device# configure terminal

IP Routing: OSPF Configuration Guide
384


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Example Configuring SNMP ifIndex Value for Interface ID for OSPFv3

Enter configuration commands, one per line. End with CNTL/Z.
Device(config)# router ospf 1
Device(config-router)# interface-id snmp-if-index
Device(config-router)# ^Z
Device# show ip ospf 1 1 data router self
OSPF Router with ID (172.16.0.1) (Process ID 1)
Router Link States (Area 1)
LS age: 6
Options: (No TOS-capability, DC)
LS Type: Router Links
Link State ID: 172.16.0.1
Advertising Router: 172.16.0.1
LS Seq Number: 80000007
Checksum: 0x63AF
Length: 48
Area Border Router
Number of Links: 2
Link connected to: another Router (point-to-point)
(Link ID) Neighboring Router ID: 172.17.0.1
(Link Data) Router Interface address: 0.0.0.53
Number of TOS metrics: 0
TOS 0 Metrics: 64
Link connected to: a Stub Network
(Link ID) Network/subnet number: 192.168.0.11
(Link Data) Network Mask: 255.255.255.255
Number of TOS metrics: 0
TOS 0 Metrics: 1
Device# show snmp mib ifmib ifindex serial 13/0
Serial13/0: Ifindex = 53

Example Configuring SNMP ifIndex Value for Interface ID for OSPFv3
The following example configures the OSPFv3 interfaces to use the SNMP ifIndex values for the interface
IDs:
Device# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)# ipv6 router ospf 1
Device(config-router)# interface-id snmp-if-index

The output from the show snmp mib ifmib ifindex command confirms that the SNMP MIB-II ifIndex values
are being used for the interface ID values in the OSPFv2 data fields:
Device# show snmp mib ifmib ifindex GigabitEthernet 0/0/0
0/0/0: Ifindex = 5
Device# show ipv6 ospf interface
OSPF_VL0 is up, line protocol is up
Interface ID 71
Area 0, Process ID 1, Instance ID 0, Router ID 172.16.0.1
Network Type VIRTUAL_LINK, Cost: 10
Configured as demand circuit.
Run as demand circuit.
DoNotAge LSA allowed.
Transmit Delay is 1 sec, State POINT_TO_POINT,
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:02
Index 1/2/3, flood queue length 0
Next 0x0(0)/0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 1
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.0.0.1 (Hello suppressed)
Suppress hello for 1 neighbor(s)
GigabitEthernet is up, line protocol is up
Link Local Address FE80::A8BB:CCFF:FE00:6F02, Interface ID 10
Area 0, Process ID 1, Instance ID 0, Router ID 172.16.0.1
Network Type BROADCAST, Cost: 10

IP Routing: OSPF Configuration Guide
385


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Example Configuring SNMP ifIndex Value for Interface ID for OSPFv3

Transmit Delay is 1 sec, State DR, Priority 1
Designated Router (ID) 172.16.0.1, local address FE80::A8BB:CCFF:FE00:6F02
No backup designated router on this network
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:06
Index 1/1/2, flood queue length 0
Next 0x0(0)/0x0(0)/0x0(0)
Last flood scan length is 0, maximum is 0
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 0, Adjacent neighbor count is 0
Suppress hello for 0 neighbor(s)
GigabitEthernet is up, line protocol is up
Link Local Address FE80::A8BB:CCFF:FE00:6F01, Interface ID 6
Area 1, Process ID 1, Instance ID 2, Router ID 172.16.0.1
Network Type BROADCAST, Cost: 10
Transmit Delay is 1 sec, State DR, Priority 1
Designated Router (ID) 172.16.0.1, local address FE80::A8BB:CCFF:FE00:6F01
Backup Designated router (ID) 10.0.0.1, local address FE80::A8BB:CCFF:FE00:6E01
Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Hello due in 00:00:06
Index 1/1/1, flood queue length 0
Next 0x0(0)/0x0(0)/0x0(0)
Last flood scan length is 1, maximum is 2
Last flood scan time is 0 msec, maximum is 0 msec
Neighbor Count is 1, Adjacent neighbor count is 1
Adjacent with neighbor 10.0.0.1 (Backup Designated Router)
Suppress hello for 0 neighbor(s)
Device# show ipv6 ospf database network adv-router 172.16.0.1
OSPFv3 Router with ID (172.16.0.1) (Process ID 1)
Net Link States (Area 1)
LS age: 144
Options: (V6-Bit E-Bit R-bit DC-Bit)
LS Type: Network Links
Link State ID: 6 (Interface ID of Designated Router)
Advertising Router: 172.16.0.1
LS Seq Number: 80000001
Checksum: 0x1FC0
Length: 32
Attached Router: 172.16.0.1
Attached Router: 10.0.0.1
Device# show ipv6 ospf database prefix adv-router 172.16.0.1
OSPFv3 Router with ID (172.16.0.1) (Process ID 1)
Intra Area Prefix Link States (Area 0)
Routing Bit Set on this LSA
LS age: 196
LS Type: Intra-Area-Prefix-LSA
Link State ID: 0
Advertising Router: 172.16.0.1
LS Seq Number: 80000001
Checksum: 0x6F11
Length: 44
Referenced LSA Type: 2001
Referenced Link State ID: 0
Referenced Advertising Router: 172.16.0.1
Number of Prefixes: 1
Prefix Address: 2002:0:2::
Prefix Length: 64, Options: None, Metric: 10
Intra Area Prefix Link States (Area 1)
Routing Bit Set on this LSA
LS age: 161
LS Type: Intra-Area-Prefix-LSA
Link State ID: 0
Advertising Router: 172.16.0.1
LS Seq Number: 80000001
Checksum: 0xB6E7
Length: 52
Referenced LSA Type: 2001
Referenced Link State ID: 0
Referenced Advertising Router: 172.16.0.1
Number of Prefixes: 1
Prefix Address: 2002:0:2:0:A8BB:CCFF:FE00:6F02
Prefix Length: 128, Options: LA , Metric: 0
Routing Bit Set on this LSA

IP Routing: OSPF Configuration Guide
386


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Example Configuring SNMP ifIndex Value for Interface ID for OSPFv3

LS age: 151
LS Type: Intra-Area-Prefix-LSA
Link State ID: 1006
Advertising Router: 172.16.0.1
LS Seq Number: 80000001
Checksum: 0x6E24
Length: 44
Referenced LSA Type: 2002
Referenced Link State ID: 6
Referenced Advertising Router: 172.16.0.1
Number of Prefixes: 1
Prefix Address: 2002:0:1::
Prefix Length: 64, Options: None, Metric: 0
Device# show ipv6 ospf database router
OSPFv3 Router with ID (10.0.0.1) (Process ID 1)
Router Link States (Area 0)
Routing Bit Set on this LSA
LS age: 5 (DoNotAge)
Options: (V6-Bit E-Bit R-bit DC-Bit)
LS Type: Router Links
Link State ID: 0
Advertising Router: 10.0.0.1
LS Seq Number: 80000004
Checksum: 0xEE5C
Length: 40
Area Border Router
Number of Links: 1
Link connected to: a Virtual Link
Link Metric: 10
Local Interface ID: 70
Neighbor Interface ID: 71
Neighbor Router ID: 172.16.0.1
LS age: 162
Options: (V6-Bit E-Bit R-bit DC-Bit)
LS Type: Router Links
Link State ID: 0
Advertising Router: 172.16.0.1
LS Seq Number: 80000004
Checksum: 0xCE7C
Length: 40
Area Border Router
Number of Links: 1
Link connected to: a Virtual Link
Link Metric: 10
Local Interface ID: 71
Neighbor Interface ID: 70
Neighbor Router ID: 10.0.0.1
Router Link States (Area 1)
Routing Bit Set on this LSA
LS age: 176
Options: (V6-Bit E-Bit R-bit DC-Bit)
LS Type: Router Links
Link State ID: 0
Advertising Router: 10.0.0.1
LS Seq Number: 80000003
Checksum: 0xC807
Length: 40
Area Border Router
Number of Links: 1
Link connected to: a Transit Network
Link Metric: 10
Local Interface ID: 6
Neighbor (DR) Interface ID: 6
Neighbor (DR) Router ID: 172.16.0.1
LS age: 175
Options: (V6-Bit E-Bit R-bit DC-Bit)
LS Type: Router Links
Link State ID: 0
Advertising Router: 172.16.0.1
LS Seq Number: 80000004
Checksum: 0xBD10
Length: 40
Area Border Router

IP Routing: OSPF Configuration Guide
387


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Additional References

Number of Links: 1
Link connected to: a Transit Network
Link Metric: 10
Local Interface ID: 6
Neighbor (DR) Interface ID: 6
Neighbor (DR) Router ID: 172.16.0.1
Device# show ipv6 ospf database link adv-router 172.16.0.1
OSPFv3 Router with ID (172.16.0.1) (Process ID 1)
Link (Type-8) Link States (Area 0)
LS age: 245
Options: (V6-Bit E-Bit R-bit DC-Bit)
LS Type: Link-LSA (Interface: GigabitEthernet2/0)
Link State ID: 10 (Interface ID)
Advertising Router: 172.16.0.1
LS Seq Number: 80000002
Checksum: 0xA0CB
Length: 56
Router Priority: 1
Link Local Address: FE80::A8BB:CCFF:FE00:6F02
Number of Prefixes: 1
Prefix Address: 2002:0:2::
Prefix Length: 64, Options: None
Link (Type-8) Link States (Area 1)
LS age: 250
Options: (V6-Bit E-Bit R-bit DC-Bit)
LS Type: Link-LSA (Interface: GigabitEthernet1/0)
Link State ID: 6 (Interface ID)
Advertising Router: 172.16.0.1
LS Seq Number: 80000001
Checksum: 0x4F94
Length: 44
Router Priority: 1
Link Local Address: FE80::A8BB:CCFF:FE00:6F01
Number of Prefixes: 0

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Protecting TE tunnel interfaces

MPLS Traffic Engineering--Fast Reroute Link and
Node Protection section in the Cisco IOS
Multiprotocol Label Switching Configuration Guide

Standards
Standard

Title

No new or modified standards are supported, and
-support for existing standards has not been modified.

IP Routing: OSPF Configuration Guide
388


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Feature Information for OSPF SNMP ifIndex Value for Interface ID

MIBs
MIB
• None

MIBs Link
To locate and download MIBs for selected platforms,
Cisco software releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

RFC 5286

Basic Specification for IP Fast Reroute: Loop-Free
Alternates

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

Feature Information for OSPF SNMP ifIndex Value for Interface
ID
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
389


OSPF SNMP ifIndex Value for Interface ID in Data Fields
Feature Information for OSPF SNMP ifIndex Value for Interface ID

Table 47: Feature Information for OSPF: SNMP ifIndex Value for Interface ID in OSPFv2 and OSPFv3 Data Fields

Feature Name

Releases

Feature Information

OSPF: SNMP ifIndex Value for
Interface ID in OSPFv2 and
OSPFv3 Data Fields

Cisco IOS XE Release 2.6

This allows you to choose either
the current interface number or the
SNMP ifIndex value for the
interface ID in OSPFv2 and
OSPFv3 data fields. The advantage
to using the SNMP MIB-II ifIndex
value is that this number
corresponds to the number that the
user will see reported by SNMP.
The following command is
introduced or modified by the
feature documented in this module:
interface-id snmp-if-index

IP Routing: OSPF Configuration Guide
390
