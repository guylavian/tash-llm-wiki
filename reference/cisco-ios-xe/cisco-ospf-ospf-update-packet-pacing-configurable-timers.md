---
title: "OSPF Update Packet-Pacing Configurable Timers"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-update-packet-pacing-configurable-timers
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 10 OSPF Update Packet-Pacing Configurable Timers This module describes the OSPF Update Packet-Pacing Configurable Timers feature, which allows you to configure the rate at which OSPF LSA flood pacing, retransmission pacing, and group pacing updates occur. • Finding Feature Information, page 121 • Restrictions on OSPF Update Packet-Pacing Configurable Timers, page 121 • Information About"
---

# OSPF Update Packet-Pacing Configurable Timers

CHAPTER

10

OSPF Update Packet-Pacing Configurable Timers
This module describes the OSPF Update Packet-Pacing Configurable Timers feature, which allows you to
configure the rate at which OSPF LSA flood pacing, retransmission pacing, and group pacing updates occur.
• Finding Feature Information, page 121
• Restrictions on OSPF Update Packet-Pacing Configurable Timers, page 121
• Information About OSPF Update Packet-Pacing Configurable Timers, page 122
• How to Configure OSPF Packet-Pacing Timers, page 122
• Configuration Examples of OSPF Update Packet-Pacing, page 125
• Additional References, page 126
• Feature Information for OSPF Update Packet-Pacing Configurable Timers, page 127

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions on OSPF Update Packet-Pacing Configurable
Timers
Do not change the packet-pacing timers unless all other options to meet OSPF packet flooding requirements
have been exhausted. Specifically, network operators should prefer summarization, stub area usage, queue
tuning, and buffer tuning before changing the default timers. Furthermore, there are no guidelines for changing
timer values; each OSPF deployment is unique and should be considered on a case-by-case basis. The network
operator assumes risks that are associated with changing the default timer values.

IP Routing: OSPF Configuration Guide
121


OSPF Update Packet-Pacing Configurable Timers
Information About OSPF Update Packet-Pacing Configurable Timers

Information About OSPF Update Packet-Pacing Configurable
Timers
Functionality of the OSPF Update Packet-Pacing Timers
In rare situations, you might need to change Open Shortest Path First (OSPF) packet-pacing default timers to
mitigate CPU or buffer utilization issues associated with flooding very large numbers of link-state
advertisements (LSAs). The OSPF Update Packet-Pacing Configurable Timers feature allows you to configure
the rate at which OSPF LSA flood pacing, retransmission pacing, and group pacing updates occur.
• Configuring OSPF flood pacing timers allows you to control interpacket spacing between consecutive
link-state update packets in the OSPF transmission queue.
• Configuring OSPF retransmission pacing timers allows you to control interpacket spacing between
consecutive link-state update packets in the OSPF retransmission queue.
• Cisco IOS XE software groups the periodic refresh of LSAs to improve the LSA packing density for
the refreshes in large topologies. The group timer controls the interval that is used for group LSA
refreshment; however, this timer does not change the frequency at which individual LSAs are refreshed
(the default refresh occurs every 30 minutes).

Caution

The default settings for OSPF packet-pacing timers are suitable for the majority of OSPF deployments.
You should change the default timers only as a last resort.

Benefits of OSPF Update Packet-Pacing Configurable Timers
The OSPF Update Packet-Pacing Configurable Timers feature provides the administrator with a mechanism
to control the rate at which LSA updates occur in order to reduce high CPU or buffer utilization that can occur
when an area is flooded with a very large number of LSAs.

How to Configure OSPF Packet-Pacing Timers
The tasks in this section describe how to configure and verify three OSPF update packet-pacing timers.

Configuring OSPF Packet-Pacing Timers
Caution

The default settings for OSPF packet-pacing timers are suitable for the majority of OSPF deployments.
You should change the default timers only as a last resort.

IP Routing: OSPF Configuration Guide
122


OSPF Update Packet-Pacing Configurable Timers
Configuring a Retransmission Packet-Pacing Timer

To configure a flood packet-pacing timer, use the following commands beginning in global configuration
mode:

SUMMARY STEPS
1. Router(config)# router ospf process-id
2. Router(config-router)# timers pacing flood milliseconds

DETAILED STEPS
Command or Action

Purpose

Step 1

Router(config)# router ospf process-id

Places the router in router configuration mode and enables an
OSPF routing process.

Step 2

Router(config-router)# timers pacing flood
milliseconds

Configures a flood packet-pacing timer delay (in milliseconds).

Configuring a Retransmission Packet-Pacing Timer
To configure a retransmission packet-pacing timer, use the following commands beginning in global
configuration mode:

SUMMARY STEPS
1. Router(config)# router ospf process-id
2. Router(config-router)# timers pacing retransmission milliseconds

DETAILED STEPS
Command or Action

Purpose

Step 1

Router(config)# router ospf process-id

Places the router in router configuration mode and enables an
OSPF routing process.

Step 2

Router(config-router)# timers pacing retransmission Configures a retransmission packet-pacing timer delay (in
milliseconds).
milliseconds

Configuring a Group Packet-Pacing Timer
To configure a group packet-pacing timer, use the following commands beginning in router configuration
mode:

IP Routing: OSPF Configuration Guide
123


OSPF Update Packet-Pacing Configurable Timers
Verifying OSPF Packet-Pacing Timers

SUMMARY STEPS
1. Router(config)# router ospf process-id
2. Router(config-router)# timers pacing lsa-group seconds

DETAILED STEPS
Command or Action

Purpose

Step 1

Router(config)# router ospf process-id

Places the router in router configuration mode and enables an
OSPF routing process.

Step 2

Router(config-router)# timers pacing lsa-group
seconds

Configures an LSA group packet-pacing timer delay (in
seconds).

Verifying OSPF Packet-Pacing Timers
To verify that OSPF packet pacing has been configured, use the show ip ospf privileged EXEC command.
The output of the show ip ospf command will display the type and delay time of the configurable pacing
timers (flood, retransmission, group). The following sample output is from the show ip ospf command:
Router# show ip ospf
Routing Process "ospf 1" with ID 10.0.0.1 and Domain ID 10.20.0.1
Supports only single TOS(TOS0) routes
Supports opaque LSA
SPF schedule delay 5 secs, Hold time between two SPFs 10 secs
Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs
LSA group pacing timer 100 secs
Interface flood pacing timer 55 msecs
Retransmission pacing timer 100 msecs
Number of external LSA 0. Checksum Sum 0x0
Number of opaque AS LSA 0. Checksum Sum 0x0
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 2. 2 normal 0 stub 0 nssa
External flood list length 0
Area BACKBONE(0)
Number of interfaces in this area is 2
Area has message digest authentication
SPF algorithm executed 4 times
Area ranges are
Number of LSA 4. Checksum Sum 0x29BEB
Number of opaque link LSA 0. Checksum Sum 0x0
Number of DCbitless LSA 3
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0
Area 172.16.26.0
Number of interfaces in this area is 0
Area has no authentication
SPF algorithm executed 1 times
Area ranges are
192.168.0.0/16 Passive Advertise
Number of LSA 1. Checksum Sum 0x44FD
Number of opaque link LSA 0. Checksum Sum 0x0
Number of DCbitless LSA 1
Number of indication LSA 1

IP Routing: OSPF Configuration Guide
124


OSPF Update Packet-Pacing Configurable Timers
Monitoring and Maintaining OSPF Packet-Pacing Timers

Number of DoNotAge LSA 0
Flood list length 0

Troubleshooting Tips
If the number of OSPF packet retransmissions rapidly increases, increase the value of the packet-pacing timers.
The number of OSPF packet retransmissions is displayed in the output of the show ip ospf neighbor command.

Monitoring and Maintaining OSPF Packet-Pacing Timers
Command

Purpose

Router# show ip ospf

Displays general information about OSPF routing
processes.

router# show ip ospf neighbor

Displays OSPF neighbor information on a
per-interface basis.

Router# clear ip ospf redistribution

Clears route redistribution based on the OSPF routing
process ID.

Configuration Examples of OSPF Update Packet-Pacing
Example LSA Flood Pacing
The following example configures LSA flood pacing updates to occur in 50-millisecond intervals for OSPF
routing process 1:
Router(config)# router ospf 1
Router(config-router)# timers pacing flood 50

Example LSA Retransmission Pacing
The following example configures LSA retransmission pacing updates to occur in 100-millisecond intervals
for OSPF routing process 1:
Router(config)# router ospf 1
Router(config-router)# timers pacing retransmission 100

IP Routing: OSPF Configuration Guide
125


OSPF Update Packet-Pacing Configurable Timers
Example LSA Group Pacing

Example LSA Group Pacing
The following example configures OSPF group pacing updates between LSA groups to occur in 75-second
intervals for OSPF routing process 1:
Router(config)# router ospf 1
Router(config-router)# timers pacing lsa-group 75

Additional References
For additional information related to the OSPF Update Packet-Pacing Configurable Timers feature, see the
following references:
Related Documents
Related Topic

Document Title

Configuring OSPF

"Configuring OSPF"

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standard

Title

No new or modified standards are supported by this -feature, and support for existing standards has not
been modified by this feature.

MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS XE software releases , and feature sets,
use Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: OSPF Configuration Guide
126


OSPF Update Packet-Pacing Configurable Timers
Feature Information for OSPF Update Packet-Pacing Configurable Timers

RFCs
RFC

Title

No new or modified RFCs are supported by this
feature, and support for existing RFCs has not been
modified by this feature.

--

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

Feature Information for OSPF Update Packet-Pacing
Configurable Timers
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
127


OSPF Update Packet-Pacing Configurable Timers
Feature Information for OSPF Update Packet-Pacing Configurable Timers

Table 13: Feature Information for OSPF Update Packet-Pacing Configurable Timers

Feature Name

Releases

Feature Information

OSPF Update Packet-Pacing
Configurable Timers

Cisco IOS XE Release 2.1

The OSPF Update Packet-Pacing
Configurable Timers feature allows
you to configure the rate at which
OSPF LSA flood pacing,
retransmission pacing, and group
pacing updates occur.
The following commands are
introduced or modified in the
feature documented in this module:
• timers pacing flood
• timers pacing lsa-group
• timers pacing
retransmission
• show ip ospf

IP Routing: OSPF Configuration Guide
128
