---
title: "OSPF Shortest Path First Throttling"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-shortest-path-first-throttling
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 24 OSPF Shortest Path First Throttling The OSPF Shortest Path First Throttling feature makes it possible to configure shortest path first (SPF) scheduling in millisecond intervals and to potentially delay SPF calculations during network instability. SPF is scheduled to calculate the Shortest Path Tree (SPT) when there is a change in topology. One SPF run may include multiple topology cha"
---

# OSPF Shortest Path First Throttling

CHAPTER

24

OSPF Shortest Path First Throttling
The OSPF Shortest Path First Throttling feature makes it possible to configure shortest path first (SPF)
scheduling in millisecond intervals and to potentially delay SPF calculations during network instability. SPF
is scheduled to calculate the Shortest Path Tree (SPT) when there is a change in topology. One SPF run may
include multiple topology change events.
The interval at which the SPF calculations occur is chosen dynamically and is based on the frequency of
topology changes in the network. The chosen interval is within the boundary of the user-specified value
ranges. If the network topology is unstable, SPF throttling calculates SPF scheduling intervals to be longer
until the topology becomes stable.
• Finding Feature Information, page 245
• Information About OSPF SPF Throttling, page 245
• How to Configure OSPF SPF Throttling, page 247
• Configuration Example for OSPF SPF Throttling, page 248
• Additional References, page 248
• Feature Information for OSPF Shortest Path First Throttling, page 250

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPF SPF Throttling
SPF calculations occur at the interval set by the timers throttle spfcommand. The wait interval indicates the
amount of time to wait until the next SPF calculation occurs. Each wait interval after that calculation is twice
as long as the previous one until the wait interval reaches the maximum wait time specified.

IP Routing: OSPF Configuration Guide
245


OSPF Shortest Path First Throttling
Information About OSPF SPF Throttling

The SPF timing can be better explained using an example. In this example the start interval is set at 5
milliseconds (ms), the wait interval at 1000 milliseconds, and the maximum wait time is set at 90,000
milliseconds.
timers throttle spf 5 1000 90000

The figure below shows the intervals at which the SPF calculations occur so long as at least one topology
change event is received in a given wait interval.
Figure 10: SPF Calculation Intervals Set by the timers throttle spf Command

Notice that the wait interval between SPF calculations doubles when at least one topology change event is
received during the previous wait interval. Once the maximum wait time is reached, the wait interval remains
the same until the topology stabilizes and no event is received in that interval.
If the first topology change event is received after the current wait interval, the SPF calculation is delayed by
the amount of time specified as the start interval. The subsequent wait intervals continue to follow the dynamic
pattern.
If the first topology change event occurs after the maximum wait interval begins, the SPF calculation is again
scheduled at the start interval and subsequent wait intervals are reset according the parameters specified in
the timers throttle spfcommand. Notice in the figure below that a topology change event was received after
the start of the maximum wait time interval and that the SPF intervals have been reset.
Figure 11: Timer Intervals Reset After a Topology Change Event

IP Routing: OSPF Configuration Guide
246


OSPF Shortest Path First Throttling
How to Configure OSPF SPF Throttling

How to Configure OSPF SPF Throttling
Configuring OSPF SPF Throttling
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. timers throttle spf spf-start spf-hold spf-max-wait
5. end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables higher privilege levels, such as privileged
EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router ospf process-id

Configures an OSPF routing process.

Example:
Router(config)# router ospf 1

Step 4

timers throttle spf spf-start spf-hold spf-max-wait

Sets OSPF throttling timers.

Example:
Router(config-router)# timers throttle spf 10 4800
90000

Step 5

end

Exits configuration mode.

Example:
Router(config-router)# end

IP Routing: OSPF Configuration Guide
247


OSPF Shortest Path First Throttling
Verifying SPF Throttle Values

Verifying SPF Throttle Values
To verify SPF throttle timer values, use the show ip ospf command. The values are displayed in the lines that
begin, "Initial SPF schedule delay...," "Minimum hold time between two consecutive SPFs...," and "Maximum
wait time between two consecutive SPFs...."
Router# show ip ospf
Routing Process "ospf 1" with ID 10.10.10.2 and Domain ID 0.0.0.1
Supports only single TOS(TOS0) routes
Supports opaque LSA
It is an autonomous system boundary router
Redistributing External Routes from,
static, includes subnets in redistribution
Initial SPF schedule delay 5 msecs
Minimum hold time between two consecutive SPFs 1000 msecs
Maximum wait time between two consecutive SPFs 90000 msecs
Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs
LSA group pacing timer 240 secs
Interface flood pacing timer 33 msecs
Retransmission pacing timer 66 msecs
Number of external LSA 4. Checksum Sum 0x17445
Number of opaque AS LSA 0. Checksum Sum 0x0
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 1. 1 normal 0 stub 0 nssa
External flood list length 0
Area BACKBONE(0)
Number of interfaces in this area is 2
Area has no authentication
SPF algorithm last executed 19:11:15.140 ago
SPF algorithm executed 28 times
Area ranges are
Number of LSA 4. Checksum Sum 0x2C1D4
Number of opaque link LSA 0. Checksum Sum 0x0
Number of DCbitless LSA 0
Number of indication LSA 0
Number of DoNotAge LSA 0
Flood list length 0

Configuration Example for OSPF SPF Throttling
Example Throttle Timers
This example shows a router configured with the start, hold, and maximum interval values for the timers
throttle spf command set at 5, 1,000, and 90,000 milliseconds, respectively.
router ospf 1
router-id 10.10.10.2
log-adjacency-changes
timers throttle spf 5 1000 90000
redistribute static subnets
network 21.21.21.0 0.0.0.255 area 0
network 22.22.22.0 0.0.0.255 area 00

Additional References
The following sections provide references related to OSPF Shortest Path First Throttling.

IP Routing: OSPF Configuration Guide
248


OSPF Shortest Path First Throttling
Additional References

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
Standards

Title

None

--

MIBs
MIBs

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS XE releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFCs

Title

None

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

IP Routing: OSPF Configuration Guide
249


OSPF Shortest Path First Throttling
Feature Information for OSPF Shortest Path First Throttling

Feature Information for OSPF Shortest Path First Throttling
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 27: Feature Information for OSPF Shortest Path First Throttling

Feature Name

Releases

OSPF Shortest Path First Throttling Cisco IOS XE Release 2.1

Feature Information
The OSPF Shortest Path First
Throttling feature makes it possible
to configure SPF scheduling in
millisecond intervals and to
potentially delay shortest path first
(SPF) calculations during network
instability. SPF is scheduled to
calculate the Shortest Path Tree
(SPT) when there is a change in
topology.
The following commands are
introduced or modified in the
feature documented in this module:
• timer spf-interval
• timers throttle spf

IP Routing: OSPF Configuration Guide
250
