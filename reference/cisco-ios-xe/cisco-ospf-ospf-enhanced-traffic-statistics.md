---
title: "OSPF Enhanced Traffic Statistics"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-enhanced-traffic-statistics
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 36 OSPF Enhanced Traffic Statistics This document describes new and modified commands that provide enhanced OSPF traffic statistics for OSPFv2 and OSPFv3. The ability to collect and display more detailed traffic statistics increases high availability for the OSPF network by making the troubleshooting process more efficient. New OSPF traffic statistics are collected and displayed to inclu"
---

# OSPF Enhanced Traffic Statistics

CHAPTER

36

OSPF Enhanced Traffic Statistics
This document describes new and modified commands that provide enhanced OSPF traffic statistics for
OSPFv2 and OSPFv3. The ability to collect and display more detailed traffic statistics increases high
availability for the OSPF network by making the troubleshooting process more efficient.
New OSPF traffic statistics are collected and displayed to include the following information:
• OSPF Hello input queue and OSPF process queue status and statistics.
• Global OSPF traffic statistics.
• Per-OSPF-interface traffic statistics.
• Per-OSPF-process traffic statistics.
• Finding Feature Information, page 339
• Prerequisites for OSPF Enhanced Traffic Statistics, page 340
• Information About OSPF Enhanced Traffic Statistics, page 340
• How to Display and Clear OSPF Enhanced Traffic Statistics, page 340
• Configuration Examples for OSPF Enhanced Traffic Statistics, page 342
• Additional References, page 345
• Feature Information for OSPF Enhanced Traffic Statistics, page 346

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
339


OSPF Enhanced Traffic Statistics
Prerequisites for OSPF Enhanced Traffic Statistics

Prerequisites for OSPF Enhanced Traffic Statistics
OSPFv2 or OSPFv3 must be configured on the router.

Information About OSPF Enhanced Traffic Statistics
The OSPF enhanced traffic statistics are enabled by default and cannot be disabled.
The detailed OSPF traffic statistics are especially beneficial for troubleshooting the following types of OSPF
instabilities:
• OSPF process queue status and statistical information can help the network administrator determine if
an OSPF process can handle the amount of traffic sent to OSPF.
• OSPF packet header errors and LSA errors statistics keep a record of different errors found in received
OSPF packets.
OSPF enhanced traffic control statistics also monitor the amount of traffic control exchanged between OSPF
processes--an important consideration in network environments with slow links and frequent topology changes.

How to Display and Clear OSPF Enhanced Traffic Statistics
Displaying and Clearing OSPF Traffic Statistics for OSPFv2
SUMMARY STEPS
1. enable
2. show ip ospf [process-id] traffic[interface-type interface-number]
3. clear ip ospf traffic

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

show ip ospf [process-id] traffic[interface-type
interface-number]
Example:
Router# show ip ospf 10 traffic gigabitethernet 0/0/0

IP Routing: OSPF Configuration Guide
340

Displays OSPFv2 traffic statistics.


OSPF Enhanced Traffic Statistics
Displaying and Clearing OSPF Traffic Statistics for OSPFv3

Step 3

Command or Action

Purpose

clear ip ospf traffic

Clears OSPFv2 traffic statistics.

Example:
Router# clear ip ospf traffic

Displaying and Clearing OSPF Traffic Statistics for OSPFv3
SUMMARY STEPS
1. enable
2. show ipv6 ospf [process-id] traffic[interface-type interface-number]
3. clear ipv6 ospf traffic

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

show ipv6 ospf [process-id] traffic[interface-type
interface-number]

Displays OSPFv3 traffic statistics.

Example:
Router# show ipv6 ospf traffic

Step 3

clear ipv6 ospf traffic

Clears OSPFv3 traffic statistics.

Example:
Router# clear ipv6 ospf traffic

IP Routing: OSPF Configuration Guide
341


OSPF Enhanced Traffic Statistics
Configuration Examples for OSPF Enhanced Traffic Statistics

Configuration Examples for OSPF Enhanced Traffic Statistics
Example Displaying and Clearing Enhanced Traffic Statistics for OSPFv2
The following example shows display output for the show ip ospf traffic command for OSPFv2:
Router# show ip ospf traffic
OSPF statistics:
Rcvd: 55 total, 0 checksum errors
22 hello, 7 database desc, 2 link state req
6 link state updates, 6 link state acks
Sent: 68 total
45 hello, 7 database desc, 2 link state req
10 link state updates, 4 link state acks
OSPF Router with ID (10.1.1.1) (Process ID 8)
OSPF queues statistic for process ID 8:
OSPF Hello queue size 0, no limit, drops 0, max size 0
OSPF Router queue size 0, limit 200, drops 0, max size 0
Interface statistics:
Interface GigabitEthernet0/0/1
OSPF packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
0
0
RX DB des
0
0
RX LS req
0
0
RX LS upd
0
0
RX LS ack
0
0
RX Total
0
0
TX Failed
0
0
TX Hello
16
1216
TX DB des
0
0
TX LS req
0
0
TX LS upd
0
0
TX LS ack
0
0
TX Total
16
1216
OSPF header errors
Length 0, Checksum 0, Version 0, Bad Source 0,
No Virtual Link 0, Area Mismatch 0, No Sham Link 0,
Self Originated 0, Duplicate ID 0, Hello 0,
MTU Mismatch 0, Nbr Ignored 0, LLS 0,
Authentication 0,
OSPF LSA errors
Type 0, Length 0, Data 0, Checksum 0,
Summary traffic statistics for process ID 8:
OSPF packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
0
0
RX DB des
0
0
RX LS req
0
0
RX LS upd
0
0
RX LS ack
0
0
RX Total
0
0
TX Failed
0
0
TX Hello
16
1216
TX DB des
0
0
TX LS req
0
0
TX LS upd
0
0
TX LS ack
0
0
TX Total
16
1216
OSPF header errors
Length 0, Checksum 0, Version 0, Bad Source 0,
No Virtual Link 0, Area Mismatch 0, No Sham Link 0,
Self Originated 0, Duplicate ID 0, Hello 0,
MTU Mismatch 0, Nbr Ignored 0, LLS 0,

IP Routing: OSPF Configuration Guide
342


OSPF Enhanced Traffic Statistics
Example Displaying and Clearing Enhanced Traffic Statistics for OSPFv2

Authentication 0,
OSPF LSA errors
Type 0, Length 0, Data 0, Checksum 0,
OSPF Router with ID (10.1.1.4) (Process ID 1)
OSPF queues statistic for process ID 1:
OSPF Hello queue size 0, no limit, drops 0, max size 2
OSPF Router queue size 0, limit 200, drops 0, max size 2
Interface statistics:
Interface Serial2/0/0
OSPF packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
11
528
RX DB des
4
148
RX LS req
1
60
RX LS upd
3
216
RX LS ack
2
128
RX Total
21
1080
TX Failed
0
0
TX Hello
14
1104
TX DB des
3
252
TX LS req
1
56
TX LS upd
3
392
TX LS ack
2
128
TX Total
23
1932
OSPF header errors
Length 0, Checksum 0, Version 0, Bad Source 0,
No Virtual Link 0, Area Mismatch 0, No Sham Link 0,
Self Originated 0, Duplicate ID 0, Hello 0,
MTU Mismatch 0, Nbr Ignored 0, LLS 0,
Authentication 0,
OSPF LSA errors
Type 0, Length 0, Data 0, Checksum 0,
Interface GigabitEthernet0/0/0
OSPF packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
13
620
RX DB des
3
116
RX LS req
1
36
RX LS upd
3
228
RX LS ack
4
216
RX Total
24
1216
TX Failed
0
0
TX Hello
17
1344
TX DB des
4
276
TX LS req
1
56
TX LS upd
7
656
TX LS ack
2
128
TX Total
31
2460
OSPF header errors
Length 0, Checksum 0, Version 0, Bad Source 13,
No Virtual Link 0, Area Mismatch 0, No Sham Link 0,
Self Originated 0, Duplicate ID 0, Hello 0,
MTU Mismatch 0, Nbr Ignored 0, LLS 0,
Authentication 0,
OSPF LSA errors
Type 0, Length 0, Data 0, Checksum 0,
Summary traffic statistics for process ID 1:
OSPF packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
24
1148
RX DB des
7
264
RX LS req
2
96
RX LS upd
6
444
RX LS ack
6
344
RX Total
45
2296
TX Failed
0
0
TX Hello
31
2448
TX DB des
7
528
TX LS req
2
112

IP Routing: OSPF Configuration Guide
343


OSPF Enhanced Traffic Statistics
Example Displaying and Clearing Enhanced Traffic Statistics for OSPFv3

TX LS upd
10
1048
TX LS ack
4
256
TX Total
54
4392
OSPF header errors
Length 0, Checksum 0, Version 0, Bad Source 13,
No Virtual Link 0, Area Mismatch 0, No Sham Link 0,
Self Originated 0, Duplicate ID 0, Hello 0,
MTU Mismatch 0, Nbr Ignored 0, LLS 0,
Authentication 0,
OSPF LSA errors
Type 0, Length 0, Data 0, Checksum 0,

The network administrator can issue the clear ip ospf traffic command to reset all counters and restart all
statistics collections:
Router# clear ip ospf traffic

Example Displaying and Clearing Enhanced Traffic Statistics for OSPFv3
The following example shows display output for the show ipv6 ospf traffic command for OSPFv3:
Router# show ipv6 ospf traffic
OSPFv3 statistics:
Rcvd: 32 total, 0 checksum errors
10 hello, 7 database desc, 2 link state req
9 link state updates, 4 link state acks
0 LSA ignored
Sent: 45 total, 0 failed
17 hello, 12 database desc, 2 link state req
8 link state updates, 6 link state acks
OSPFv3 Router with ID (10.1.1.4) (Process ID 6)
OSPFv3 queues statistic for process ID 6
Hello queue size 0, no limit, max size 2
Router queue size 0, limit 200, drops 0, max size 2
Interface statistics:
Interface Serial2/0/0
OSPFv3 packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
5
196
RX DB des
4
172
RX LS req
1
52
RX LS upd
4
320
RX LS ack
2
112
RX Total
16
852
TX Failed
0
0
TX Hello
8
304
TX DB des
3
144
TX LS req
1
52
TX LS upd
3
252
TX LS ack
3
148
TX Total
18
900
OSPFv3 header errors
Length 0, Checksum 0, Version 0, No Virtual Link 0,
Area Mismatch 0, Self Originated 0, Duplicate ID 0,
Instance ID 0, Hello 0, MTU Mismatch 0,
Nbr Ignored 0, Authentication 0,
OSPFv3 LSA errors
Type 0, Length 0, Data 0, Checksum 0,
Interface GigabitEthernet0/0/0
OSPFv3 packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
6
240
RX DB des
3
144
RX LS req
1
52
RX LS upd
5
372

IP Routing: OSPF Configuration Guide
344


OSPF Enhanced Traffic Statistics
Additional References

RX LS ack
2
152
RX Total
17
960
TX Failed
0
0
TX Hello
11
420
TX DB des
9
312
TX LS req
1
52
TX LS upd
5
376
TX LS ack
3
148
TX Total
29
1308
OSPFv3 header errors
Length 0, Checksum 0, Version 0, No Virtual Link 0,
Area Mismatch 0, Self Originated 0, Duplicate ID 0,
Instance ID 0, Hello 0, MTU Mismatch 0,
Nbr Ignored 0, Authentication 0,
OSPFv3 LSA errors
Type 0, Length 0, Data 0, Checksum 0,
Summary traffic statistics for process ID 6:
OSPFv3 packets received/sent
Type
Packets
Bytes
RX Invalid
0
0
RX Hello
11
436
RX DB des
7
316
RX LS req
2
104
RX LS upd
9
692
RX LS ack
4
264
RX Total
33
1812
TX Failed
0
0
TX Hello
19
724
TX DB des
12
456
TX LS req
2
104
TX LS upd
8
628
TX LS ack
6
296
TX Total
47
2208
OSPFv3 header errors
Length 0, Checksum 0, Version 0, No Virtual Link 0,
Area Mismatch 0, Self Originated 0, Duplicate ID 0,
Instance ID 0, Hello 0, MTU Mismatch 0,
Nbr Ignored 0, Authentication 0,
OSPFv3 LSA errors
Type 0, Length 0, Data 0, Checksum 0,

The network administrator can issue the clear ipv6 ospf traffic command to reset all counters and restart all
statistics collections:
Router# clear ipv6 ospf traffic

Additional References
The following sections provide references related to the OSPF Sham-Link MIB Support feature.
Related Documents
Related Topic

Document Title

Configuring OSPF sham-links

OSPF Sham-Link Support for MPLS VPN

SNMP configuration

Cisco IOS Network Management Configuration
Guide.

SNMP commands

Cisco IOS Network Management Command
Reference.

IP Routing: OSPF Configuration Guide
345


OSPF Enhanced Traffic Statistics
Feature Information for OSPF Enhanced Traffic Statistics

Standards
Standard

Title

None

--

MIBs
MIB
• CISCO-OSPF-MIB
• CISCO-OSPF-TRAP-MIB

MIBs Link
To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

None

--

Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/techsupport
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies. Access to most tools
on the Cisco Support website requires a Cisco.com
user ID and password. If you have a valid service
contract but do not have a user ID or password, you
can register on Cisco.com.

Feature Information for OSPF Enhanced Traffic Statistics
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
346


OSPF Enhanced Traffic Statistics
Feature Information for OSPF Enhanced Traffic Statistics

Table 43: Feature Information for OSPF Enhanced Traffic Statistics for OSPFv2 and OSPFv3

Feature Name

Releases

OSPF Enhanced Traffic Statistics Cisco IOS XE Release 2.1
for OSPFv2 and OSPFv3

Feature Information
This document describes the
detailed OSPF traffic statistics that
are provided when the user enters
the new and modified show
commands for OSPFv2 and
OSPFv3.
The following commands are
introduced or modified in the
feature documented in this module:
• clear ipv6 ospf traffic
• show ip ospf traffic
• show ipv6 ospf traffic

IP Routing: OSPF Configuration Guide
347


OSPF Enhanced Traffic Statistics
Feature Information for OSPF Enhanced Traffic Statistics

IP Routing: OSPF Configuration Guide
348
