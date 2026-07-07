---
title: "OSPF Limiting Adjacency Formations"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-limiting-adjacency-formations
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 54 OSPF Limiting Adjacency Formations The OSPF: Limit Simultaneous Adjacency Formations feature allows you to limit to the number of adjacencies in an OSPF area. • Finding Feature Information, page 505 • Information About OSPF Limiting Adjacency Formations, page 505 • How to Configure OSPF Limiting Adjacency Formations, page 507 • Configuration Examples for OSPF Limiting Adjacency Format"
---

# OSPF Limiting Adjacency Formations

CHAPTER

54

OSPF Limiting Adjacency Formations
The OSPF: Limit Simultaneous Adjacency Formations feature allows you to limit to the number of adjacencies
in an OSPF area.
• Finding Feature Information, page 505
• Information About OSPF Limiting Adjacency Formations, page 505
• How to Configure OSPF Limiting Adjacency Formations, page 507
• Configuration Examples for OSPF Limiting Adjacency Formations, page 512
• Additional References for OSPF Limiting Adjacency Formations, page 512
• Feature Information for OSPF Limiting Adjacencies Formations, page 513

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPF Limiting Adjacency Formations
Overview of Limiting Adjacencies
The OSPF: Limit Simultaneous Adjacency Formations feature allows you to limit to the number of adjacencies
that are in “exchange” or “loading” state at the same time. A process limit (PL) determines the number of
“forming” adjacencies and applies to all adjacencies for the entire process. The term “forming” refers to
adjacencies that are in “exchange” or “loading” state. Adjacencies form in an OSPF area during the initial
period after the area is created. The Initial Limit applies when no adjacencies have reached the “full” state in
an OSPF area. If there are any “full” adjacencies in the area, the new adjacencies are governed by the Process

IP Routing: OSPF Configuration Guide
505


OSPF Limiting Adjacency Formations
Configuring Adjacency Formations

Limit. At a given point of time, process limit and initial limit are effective in an OSPF area. When there are
no adjacencies “forming” in an area, at least one adjacency is allowed to form regardless of the maximum
limit specified for it. In other words, the maximum number of adjacencies can be exceeded before adjacencies
form in one or more areas. The maximum limit can be exceeded by the number of areas minus one.
When a limit is reached, adjacencies in a state less than EXCHANGE are terminated. To terminate the
adjacency, a hello packet is sent to the neighbor which does not have the neighbor’s device ID. This causes
the neighbor to put the adjacency in the INIT state. This prevents a deadlock with the neighbor, which could
otherwise happen if the neighbor is blocking an adjacency from forming on a different interface. By causing
the neighbor to bring the adjacency to INIT, it allows the neighbor to form an adjacency on a different interface.
Packets from unknown neighbors are ignored when the limit has been reached or exceeded.
If graceful restart or Cisco nonstop forwarding is configured, the hello packets must be accepted from every
neighboring device The restarting device must include the neighbors’ device IDs in its hello packets to prevent
the adjacency from being dropped by the neighbor. If graceful restart is in configured, the grace link-state
advertisements (LSAs) must be sent in a normal mode and not in a throttling mode. When the device is
performing graceful restart and if the limit is reached, new adjacencies are allowed to remain in 2-WAY or
EXSTART. However, they are prevented from proceeding to EXCHANGE until the number of forming
adjacencies is less than the limit.

Configuring Adjacency Formations
Use the adjacency stagger command to configure the maximum limit and the initial limit for an area in the
router or address-family configuration modes. The initial limit must not be greater than the process limit. The
default value is 300 and the minimum is 1. If the none keyword is used, the maximum limit is only effective.
The none keyword also disables the initial limit for areas. If an initial limit is reached in an area and no
adjacencies are forming, no adjacencies will be allowed to form in the area until global number of adjacencies
forming is less than the PL.
Use the ip ospf adjacency stagger disable or the ospfv3 adjacency stagger disable command to disable
staggering on an interface. Adjacencies forming on a disabled interface are counted towards throttling limits.
Disabling the throttling on an interface allows exceeding the maximum limit when the maximum limit is
reached and a new adjacency forms on an interface where throttling is disabled.

Note

When using the no adjacency stagger command to disable the feature, the command is displayed in the
running configuration. To return to the default values, use the default adjacency stagger command. After
using this command, the adjacency stagger command does not appear in the running configuration.

IP Routing: OSPF Configuration Guide
506


OSPF Limiting Adjacency Formations
How to Configure OSPF Limiting Adjacency Formations

How to Configure OSPF Limiting Adjacency Formations
Configuring Adjacency Formations Globally
Configuring Adjacency Limit in the Router Configuration Mode
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. adjacency stagger {initial-limit | none} maximum-limit
5. end

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

router ospf process-id

Enables OSPF routing and enters router configuration mode.

Example:
Device(config)# router ospf 109

Step 4

adjacency stagger {initial-limit | none}
maximum-limit
Example:
Device(config-router)# adjacency stagger
10 50

Controls the number of adjacencies forming in an area.
• initial-limit—Minimum number of adjacencies allowed in
an area.
• maximum-limit—Maximum number of adjacencies allowed
in an area.
• none—No minimum number for adjacencies allowed in an
area.

IP Routing: OSPF Configuration Guide
507


OSPF Limiting Adjacency Formations
Configuring Adjacency Formations Globally

Step 5

Command or Action

Purpose

end

Exits router configuration mode and returns to privileged EXEC
mode.

Example:
Device(config-router)# end

Configuring Adjacency Limit in the Address Family Configuration Mode
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. Do one of the following:
• address-family ipv4 unicast
• address-family ipv6 unicast
5. adjacency stagger {initial-limit | none} {maximum-limit| disable}
6. end

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

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for the IPv4 or
IPv6 address family.

Example:
Device(config)# router ospfv3 1

Step 4

Do one of the following:
• address-family ipv4 unicast
• address-family ipv6 unicast

IP Routing: OSPF Configuration Guide
508

Enters IPv4 or IPv6 address family configuration mode for
OSPFv3.


OSPF Limiting Adjacency Formations
Disabling Adjacency Staggering in the Interface Configuration Mode

Command or Action

Purpose

Example:
Device(config-router)# address-family ipv4
unicast

Example:
Device(config-router)# address-family ipv6
unicast

Step 5

adjacency stagger {initial-limit | none}
{maximum-limit| disable}
Example:
Device(config-router-af)# adjacency stagger
10 50

Controls the number of adjacencies forming in an area.
• initial-limit—Minimum number of adjacencies allowed
in an area.
• none—No minimum number for adjacencies allowed
in an area.
• maximum-limit—Maximum number of adjacencies
allowed in an area.
• disable—Disable adjacency formations.

Step 6

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Disabling Adjacency Staggering in the Interface Configuration Mode
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. Do one of the following:
• ip ospf adjacency stagger disable
• ospfv3 adjacency stagger disable
5. end

IP Routing: OSPF Configuration Guide
509


OSPF Limiting Adjacency Formations
Verifying Adjacency Staggering

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

interface type number

Specifies the interface and enters interface
configuration mode.

Example:
Device(config)# interface serial 2/0

Step 4

Do one of the following:

Disables adjacency staggering on the interface.

• ip ospf adjacency stagger disable
• ospfv3 adjacency stagger disable

Example:
Device(config-if)# ip ospf adjacency stagger disable

Example:
Device(config-if)# ospfv3 adjacency stagger disable

Step 5

Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Verifying Adjacency Staggering
SUMMARY STEPS
1. enable
2. show ip ospf
3. show ospfv3

DETAILED STEPS
Step 1

enable

IP Routing: OSPF Configuration Guide
510


OSPF Limiting Adjacency Formations
Verifying Adjacency Staggering

Example:
Device> enable

Enables privileged EXEC mode.
• Enter your password if prompted.
Step 2

show ip ospf
Example:
Device# show ip ospf
Routing Process "ospf 10" with ID 10.8.3.3
Start time: 2w0d, Time elapsed: 00:16:43.033
Supports only single TOS(TOS0) routes
Supports opaque LSA
Supports Link-local Signaling (LLS)
Supports area transit capability
Supports NSSA (compatible with RFC 3101)
Supports Database Exchange Summary List Optimization (RFC 5243)
Event-log enabled, Maximum number of events: 1000, Mode: cyclic
Router is not originating router-LSAs with maximum metric
Initial SPF schedule delay 5000 msecs
Minimum hold time between two consecutive SPFs 10000 msecs
Maximum wait time between two consecutive SPFs 10000 msecs
Incremental-SPF disabled
Minimum LSA interval 5 secs
Minimum LSA arrival 1000 msecs
LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
Number of external LSA 0. Checksum Sum 0x000000
Number of opaque AS LSA 0. Checksum Sum 0x000000
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 0. 0 normal 0 stub 0 nssa
Number of areas transit capable is 0
External flood list length 0
IETF NSF helper support enabled
Cisco NSF helper support enabled
Reference bandwidth unit is 100 mbps

Displays information about OSPF routing processes.
Step 3

show ospfv3
Example:
Device# show ospfv3
OSPFv3 12 address-family ipv6
Router ID 10.8.3.3
Supports NSSA (compatible with RFC 3101)
Supports Database Exchange Summary List Optimization (RFC 5243)
Event-log enabled, Maximum number of events: 1000, Mode: cyclic
Router is not originating router-LSAs with maximum metric
Initial SPF schedule delay 5000 msecs
Minimum hold time between two consecutive SPFs 10000 msecs
Maximum wait time between two consecutive SPFs 10000 msecs
Minimum LSA interval 5 secs
Minimum LSA arrival 1000 msecs
LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
Retransmission limit dc 24 non-dc 24
EXCHANGE/LOADING adjacency limit: initial 10, process maximum 50

IP Routing: OSPF Configuration Guide
511


OSPF Limiting Adjacency Formations
Configuration Examples for OSPF Limiting Adjacency Formations

Number of external LSA 0. Checksum Sum 0x000000
Number of areas in this router is 0. 0 normal 0 stub 0 nssa
Graceful restart helper support enabled
Reference bandwidth unit is 100 mbps
RFC1583 compatibility enabled

Displays information about OSPFv3 routing processes.

ConfigurationExamplesforOSPFLimitingAdjacencyFormations
Example: Configuring Adjacency Limit in the Router Configuration Mode
Device> enable
Device# configure terminal
Device(config)# router ospf 109
Device(config-router)# adjacency stagger 10 50
Device(config-router)# end

Example: Configuring Adjacency Limit in the Address Family Configuration
Mode
Device> enable
Device# configure terminal
Device(config)# router ospfv3 1
Device(config-router)# address-family ipv6 unicast
Device(config-router-af)# adjacency stagger 10 50
Device(config-router-af)# end

Example: Disabling Adjacency in the Interface Configuration Mode
Device> enable
Device# configure terminal
Device(config)# interface serial 2/0
Device(config-if)# ospfv3 adjacency stagger disable
Device(config-if)# end

Additional References for OSPF Limiting Adjacency Formations
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Configuring OSPF

Configuring OSPF

IP Routing: OSPF Configuration Guide
512


OSPF Limiting Adjacency Formations
Feature Information for OSPF Limiting Adjacencies Formations

Related Topic

Document Title

Multiarea Adjacency

• OSPFv2 Multiarea Adjacency
• OSPFv3 Multiarea Adjacency

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

Feature Information for OSPF Limiting Adjacencies Formations
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 59: Feature Information for OSPF Limiting Adjacencies Formations

Feature Name

Releases

Feature Information

OSPF: Limit Simultaneous
Adjacency Formations

Cisco IOS XE Release
3.15S

The OSPF: Limit Simultaneous Adjacency
Formations feature allows you to limit to
the number of adjacencies in an OSPF
area.
The following commands were introduced
or modified: adjacency stagger, ip ospf
adjacency stagger disable, ip ospfv3
adjacency stagger disable, show ip ospf,
show ip ospfv3.

IP Routing: OSPF Configuration Guide
513


OSPF Limiting Adjacency Formations
Feature Information for OSPF Limiting Adjacencies Formations

IP Routing: OSPF Configuration Guide
514
