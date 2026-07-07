---
title: "OSPFv3 NSR"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-nsr
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 45 OSPFv3 NSR The OSPFv3 NSR feature allows a router with redundant Route Processors (RPs) to maintain its Open Shortest Path First (OSPF) state and adjacencies across planned and unplanned RP switchovers. It does this by checkpointing state information from OSPFv3 on the active RP to the standby RP. Later, following a switchover to the standby RP, OSPFv3 can use this checkpointed inform"
---

# OSPFv3 NSR

CHAPTER

45

OSPFv3 NSR
The OSPFv3 NSR feature allows a router with redundant Route Processors (RPs) to maintain its Open
Shortest Path First (OSPF) state and adjacencies across planned and unplanned RP switchovers. It does this
by checkpointing state information from OSPFv3 on the active RP to the standby RP. Later, following a
switchover to the standby RP, OSPFv3 can use this checkpointed information to continue operation without
interruption.
• Finding Feature Information, page 423
• Information About OSPFv3 NSR, page 423
• How to Configure OSPFv3 NSR, page 424
• Configuration Examples for OSPFv3 NSR, page 427
• Additional References, page 430
• Feature Information for OSPFv3 NSR, page 431

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPFv3 NSR
OSPFv3 NSR Functionality
Although OSPFv3 NSR serves a similar function to the OSPFv3 graceful restart feature, it works differently.
With graceful restart, OSPFv3 on the newly active standby RP initially has no state information, so it uses

IP Routing: OSPF Configuration Guide
423


OSPFv3 NSR
How to Configure OSPFv3 NSR

extensions to the OSPFv3 protocol to recover its state from neighboring OSPFv3 devices. For this to work,
the neighbors must support the graceful restart protocol extensions and be able to act as helpers to the restarting
device. They must also continue forwarding data traffic to the restarting device while this recovery is taking
place.
With NSR, by contrast, the device performing the switchover preserves its state internally, and in most cases
the neighbors are unaware that anything has happened. Because no assistance is needed from neighboring
devices, NSR can be used in situations where graceful restart cannot; for example, graceful restart is unreliable
in networks where not all the neighbors implement the graceful restart protocol extensions or where the
network topology changes during the recovery.

Note

When NSR is enabled, the responsiveness and scalability of OSPF is degraded. The performance degradation
happens because OSPF uses cpu and memory to checkpoint data to the standby Route Processor (RP).

How to Configure OSPFv3 NSR
Configuring OSPFv3 NSR
Perform this task to configure OSPFv3 NSR.

Note

Devices that do not support NSR will not accept the nsr (OSPFv3) command.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 process-id
4. nsr
5. end
6. show ospfv3 [process-id] [address-family] nsr

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device> enable

IP Routing: OSPF Configuration Guide
424

• Enter your password if prompted.


OSPFv3 NSR
Configuring OSPFv3 NSR for an Address Family

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router ospfv3 process-id

Places the device in router configuration mode and
configures an OSPFv3 routing process.

Example:
Device(config)# router ospfv3 109

Step 4

Configures NSR.

nsr
Example:
Device(config-router)# nsr

Step 5

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Step 6

show ospfv3 [process-id] [address-family] nsr

Displays OSPFv3 NSR status information.

Example:
Device# show ospfv3 109 nsr

Configuring OSPFv3 NSR for an Address Family
In address family configuration mode you can configure NSR for a particular address family. Perform this
task to enable OSPFv3 NSR for an address family.

Note

Devices that do not support NSR will not accept the nsr (OSPFv3) command.

SUMMARY STEPS
1. router ospfv3 process-id
2. address-family {ipv4 | ipv6} unicast [vrf vrf-name]
3. nsr [disable]

IP Routing: OSPF Configuration Guide
425


OSPFv3 NSR
Configuring OSPFv3 NSR for an Address Family

DETAILED STEPS

Step 1

Command or Action

Purpose

router ospfv3 process-id

Places the device in router configuration mode and
configures an OSPFv3 routing process.

Example:
Device(config)# router ospfv3 109

Step 2

address-family {ipv4 | ipv6} unicast [vrf vrf-name]

Enters IPv4 or IPv6 address family configuration mode
for OSPFv3 router configuration mode.

Example:
Device(config-router)# address-family ipv4
unicast

Step 3

nsr [disable]

Enables NSR for the address family that is configured.

Example:
Device(config-router-af)# nsr

Disabling OSPFv3 NSR for an Address Family
In address family configuration mode the optional disable keyword is available for the nsr command. Perform
this task to disable OSPFv3 NSR for an address family.

SUMMARY STEPS
1. router ospfv3 process-id
2. address-family {ipv4 | ipv6} unicast [vrf vrf-name]
3. nsr [disable]

DETAILED STEPS

Step 1

Command or Action

Purpose

router ospfv3 process-id

Places the device in router configuration mode and
configures an OSPFv3 routing process.

Example:
Device(config)# router ospfv3 109

IP Routing: OSPF Configuration Guide
426


OSPFv3 NSR
Configuration Examples for OSPFv3 NSR

Step 2

Command or Action

Purpose

address-family {ipv4 | ipv6} unicast [vrf vrf-name]

Enters IPv4 or IPv6 address family configuration mode
for OSPFv3 router configuration mode.

Example:
Device(config-router)# address-family ipv6
unicast

Step 3

nsr [disable]

Disables NSR for the address family that is configured.

Example:
Device(config-router-af)# nsr disable

Troubleshooting Tips
OSPFv3 NSR can increase the amount of memory used by the OSPFv3 device process. To determine how
much memory OSPFv3 is currently using without NSR, you can use the show processes and show processes
memory commands:
Device# show processes
| include OSPFv3
276 Mwe 133BE14
296 Mwe 133A824

1900
10

1792
971

1060 8904/12000
10 8640/12000

0 OSPFv3-1 Router
0 OSPFv3-1 Hello

Process 276 is the OSPFv3 device process that is to be checked. The show processes memory command is
used to display its current memory use:
Device# show processes memory 276
Process ID: 276
Process Name: OSPFv3-1 Router
Total Memory Held: 4454800 bytes

In this case OSPFv3 is using 4,454,800 bytes or approximately 4.5 megabytes (MB). OSPFv3 NSR could
double this for brief periods, so you should make sure the device has at least 5 MB of free memory before
enabling OSPFv3 NSR.

Configuration Examples for OSPFv3 NSR
Example Configuring OSPFv3 NSR
The following example shows how to configure OSPFv3 NSR and verify that it is enabled:
Device(config)# router ospfv3 1
Device(config-router)# nsr
Device(config-router)# end
Device# show ospfv3 1
OSPFv3 1 address-family ipv4
Router ID 10.0.0.1
Supports NSSA (compatible with RFC 3101)

IP Routing: OSPF Configuration Guide
427


OSPFv3 NSR
Example Configuring OSPFv3 NSR

Event-log enabled, Maximum number of events: 1000, Mode: cyclic
It is an area border and autonomous system boundary router
Redistributing External Routes from,
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
Number of external LSA 0. Checksum Sum 0x000000
Number of areas in this router is 3. 2 normal 0 stub 1 nssa
Non-Stop Routing enabled
Graceful restart helper support enabled
Reference bandwidth unit is 100 mbps
RFC1583 compatibility enabled
Area BACKBONE(0) (Inactive)
Number of interfaces in this area is 1
SPF algorithm executed 3 times
Number of LSA 6. Checksum Sum 0x03C938
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0
Area 1
Number of interfaces in this area is 3
SPF algorithm executed 3 times
Number of LSA 6. Checksum Sum 0x024041
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0
Area 3
Number of interfaces in this area is 1
It is a NSSA area
Perform type-7/type-5 LSA translation
SPF algorithm executed 4 times
Number of LSA 5. Checksum Sum 0x024910
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0
OSPFv3 1 address-family ipv6
Router ID 10.0.0.1
Supports NSSA (compatible with RFC 3101)
Event-log enabled, Maximum number of events: 1000, Mode: cyclic
It is an area border and autonomous system boundary router
Redistributing External Routes from,
ospf 2
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
Number of external LSA 0. Checksum Sum 0x000000
Number of areas in this router is 3. 2 normal 0 stub 1 nssa
Non-Stop Routing enabled
Graceful restart helper support enabled
Reference bandwidth unit is 100 mbps
RFC1583 compatibility enabled
Area BACKBONE(0) (Inactive)
Number of interfaces in this area is 2
SPF algorithm executed 2 times
Number of LSA 6. Checksum Sum 0x02BAB7

IP Routing: OSPF Configuration Guide
428


OSPFv3 NSR
Example Verifying OSPFv3 NSR

Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0
Area 1
Number of interfaces in this area is 4
SPF algorithm executed 2 times
Number of LSA 7. Checksum Sum 0x04FF3A
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0
Area 3
Number of interfaces in this area is 1
It is a NSSA area
Perform type-7/type-5 LSA translation
SPF algorithm executed 3 times
Number of LSA 5. Checksum Sum 0x011014
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0

The output shows that OSPFv3 NSR is configured.

Example Verifying OSPFv3 NSR
The following example shows how to verify OSPFv3 NSR status:
Device# show ospfv3 1 nsr
Active RP
Operating in duplex mode
Redundancy state: ACTIVE
Peer redundancy state: STANDBY HOT
Checkpoint peer ready
Checkpoint messages enabled
ISSU negotiation complete
ISSU versions compatible
OSPFv3 1 address-family ipv4 (router-id 10.0.0.1)
NSR configured
Checkpoint message sequence number: 29
Standby synchronization state: synchronized
Bulk sync operations: 1
Next sync check time: 12:00:14.956 PDT Wed Jun 6 2012
LSA Count: 17, Checksum Sum 0x00085289
OSPFv3 1 address-family ipv6 (router-id 10.0.0.1)
NSR configured
Checkpoint message sequence number: 32
Standby synchronization state: synchronized
Bulk sync operations: 1
Next sync check time: 12:00:48.537 PDT Wed Jun 6 2012
LSA Count: 18, Checksum Sum 0x0008CA05

The output shows that OSPFv3 NSR is configured and that OSPFv3 on the standby RP is fully synchronized
and ready to continue operation if the active RP fails or if a manual switchover is performed.

IP Routing: OSPF Configuration Guide
429


OSPFv3 NSR
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

OSPFv3 Address Families

OSPFv3 Address Families module

Standards
Standards

Title

No new or modified standards are supported by this —
feature, and support for existing standards has not
been modified by this feature.

MIBs
MIBs

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco software releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFCs

Title

RFC 5187.

OSPFv3 Graceful Restart

IP Routing: OSPF Configuration Guide
430


OSPFv3 NSR
Feature Information for OSPFv3 NSR

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

Feature Information for OSPFv3 NSR
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 51: Feature Information for OSPFv3 NSR

Feature Name

Releases

Feature Information

OSPFv3 NSR

15.1(2)SY

The OSPFv3 NSR feature allows
a router with redundant RPs to
maintain its OSPFv3 state and
adjacencies across planned and
unplanned RP switchovers.

15.2(4)S

The following commands were
introduced or modified: clear
ospfv3 nsr, nsr (OSPFv3), show
ospfv3 nsr.

IP Routing: OSPF Configuration Guide
431


OSPFv3 NSR
Feature Information for OSPFv3 NSR

IP Routing: OSPF Configuration Guide
432
