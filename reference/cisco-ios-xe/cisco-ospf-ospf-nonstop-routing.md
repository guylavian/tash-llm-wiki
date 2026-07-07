---
title: "OSPF Nonstop Routing"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-nonstop-routing
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 44 OSPF Nonstop Routing The OSPF Nonstop Routing feature allows a device with redundant Route Processors (RPs) to maintain its Open Shortest Path First (OSPF) state and adjacencies across planned and unplanned RP switchovers. The OSPF state is maintained by checkpointing the state information from OSPF on the active RP to the standby RP. After a switchover to the standby RP, OSPF uses th"
---

# OSPF Nonstop Routing

CHAPTER

44

OSPF Nonstop Routing
The OSPF Nonstop Routing feature allows a device with redundant Route Processors (RPs) to maintain its
Open Shortest Path First (OSPF) state and adjacencies across planned and unplanned RP switchovers. The
OSPF state is maintained by checkpointing the state information from OSPF on the active RP to the standby
RP. After a switchover to the standby RP, OSPF uses the checkpointed information to continue operations
without interruption.
• Finding Feature Information, page 417
• Prerequisites for OSPF NSR, page 417
• Restrictions for OSPF NSR, page 418
• Information About OSPFv3 Authentication Trailer, page 418
• How to Configure OSPF Nonstop Routing, page 418
• Configuration Examples for OSPF Nonstop Routing, page 420
• Additional References, page 421
• Feature Information for OSPF NSR, page 422

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPF NSR
• OSPF NSR is available for platforms with redundant RPs or Cisco IOS software redundancy running
Cisco IOS Release XE 3.3S or later releases.

IP Routing: OSPF Configuration Guide
417


OSPF Nonstop Routing
Restrictions for OSPF NSR

Restrictions for OSPF NSR
• OSPF nonstop routing (NSR) can significantly increase the memory used by OSPF during certain phases
of its operation. CPU usage also can be increased. You should be aware of router memory capacity and
estimate the likely memory requirements of OSPF NSR. For more information see Configuring OSPF
NSR. For routers where memory and CPU are constrained you might want to consider using OSPF NSF
instead. For more information, see OSPF RFC 3623 Graceful Restart Helper Mode.
• A switchover from the active to the standby RP can take several seconds, depending on the hardware
platform, and during this time OSPF is unable to send Hello packets. As a result, configurations that use
small OSPF dead intervals might not be able to maintain adjacencies across a switchover.

Information About OSPFv3 Authentication Trailer
OSPF NSR Functionality
Although OSPF Nonstop Routing (NSR) serves a similar function to OSPF Nonstop Forwarding (NSF), it
works differently. With NSF, OSPF on the newly active standby RP initially has no state information. OSPF
uses extensions to the OSPF protocol to recover its state from neighboring OSPF devices. For the recovery
to work, the neighbors must support the NSF protocol extensions and be willing to act as “helpers” to the
device that is restarting. The neighbors must also continue forwarding data traffic to the device that is restarting
while protocol state recovery takes place.
With NSR, by contrast, the device that performs the switchover preserves its state internally, and in most
cases the neighbors are unaware of the switchover. Because assistance is not needed from neighboring devices,
NSR can be used in situations where NSF cannot be used; for example, in networks where not all neighbors
implement the NSF protocol extensions, or where network topology changes during the recovery making NSF
unreliable, use NSR instead of NSF.

How to Configure OSPF Nonstop Routing
Configuring OSPF NSR
Perform this task to configure OSPF NSR.
NSR adds a single new line, "nsr," to the OSPF router mode configuration. Routers that do not support NSR,
for whatever reason, will not accept this command.

IP Routing: OSPF Configuration Guide
418


OSPF Nonstop Routing
Configuring OSPF NSR

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf
4. nsr

process-id

5. end
6. show ip ospf [ process-id ] nsr [[ objects ]|[ statistics ]]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospf

process-id

Places the router in router configuration mode and
configures an OSPF routing process.

Example:
Router(config)# router ospf 109

Step 4

nsr

Configures NSR.

Example:
Router(config-router)# nsr

Step 5

end

Exits router configuration mode and returns to privileged
EXEC mode.

Example:
Router(config-router)# end

Step 6

show ip ospf [ process-id ] nsr [[ objects ]|[ statistics Displays OSPF NSR status information.
]]
Example:
Router# show ip ospf 109 nsr

IP Routing: OSPF Configuration Guide
419


OSPF Nonstop Routing
Configuration Examples for OSPF Nonstop Routing

Troubleshooting Tips
OSPF NSR can increase the amount of memory used by the OSPF device process. To determine how much
memory OSPF is currently using without NSR, you can use the show processes and show processes memory
commands:
Device# show processes|include OSPF
276 Mwe
296 Mwe

133BE14
133A824

1900
10

1792
971

1060 8904/12000
10 8640/12000

0 OSPF-1 Router
0 OSPF-1 Hello

Process 276 is the OSPF device process that is to be checked. Use the show processes memory command to
display its current memory use:
Device# show processes memory 276
Process ID: 276
Process Name: OSPF-1 Router
Total Memory Held: 4454800 bytes

In the above example, OSPF is using 4,454,800 bytes, or approximately 4.5 megabytes (MB). Because OSPF
NSR can consume double this memory for brief periods, ensure that the device has at least 5 MB of free
memory before enabling OSPF NSR.

Configuration Examples for OSPF Nonstop Routing
Example: Configuring OSPF NSR
The following example shows how to configure OSPF NSR:
Device> enable
Device# configure terminal
Device(config)# router ospf 1
Device(config-router)# nsr
Device(config-router)# end
Device# show ip ospf 1 nsr
Standby RP
Operating in duplex mode
Redundancy state: STANDBY HOT
Peer redundancy state: ACTIVE
ISSU negotation complete
ISSU versions compatible
Routing Process "ospf 1" with ID 10.1.1.100
NSR configured
Checkpoint message sequence number: 3290
Standby synchronization state: synchronized
Bulk sync operations: 1
Last sync start time: 15:22:48.971 UTC Fri Jan 14 2011
Last sync finish time: 15:22:48.971 UTC Fri Jan 14 2011
Last sync lost time:
Last sync reset time: LSA Count: 2, Checksum Sum 0x00008AB4

The output shows that OSPF NSR is configured and that OSPF on the standby RP is fully synchronized and
ready to continue operation should the active RP fail or if a manual switchover is performed.

IP Routing: OSPF Configuration Guide
420


OSPF Nonstop Routing
Additional References

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

OSPF commands: complete command syntax, command mode, defaults, Cisco IOS IP Routing: OSPF
command history, usage guidelines, and examples
Command Reference
Configuring OSPF

“Configuring OSPF” in the IP
Routing: OSPF Configuration
Guide.

OSPFv2 loop-free alternate fast reroute

“OSPFv2 Loop-Free Alternate Fast
Reroute” in the IP Routing: OSPF
Configuration Guide

Standards and RFCs
Standard/RFC

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

IP Routing: OSPF Configuration Guide
421


OSPF Nonstop Routing
Feature Information for OSPF NSR

Feature Information for OSPF NSR
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 50: Feature Information for OSPF NSR

Feature Name

Releases

Feature Information

OSPF NSR

XE 3.3S

The OSPF NSR feature allows a
router with redundant route
processors to maintain its OSPF
state and adjacencies across
planned and unplanned RP
switchovers.

Cisco IOS Release 15.1(1)SY

In Cisco IOS Release XE 3.3S, this
feature was introduced.
The following commands were
introduced or modified: nsr, show
ip ospf nsr.

IP Routing: OSPF Configuration Guide
422
