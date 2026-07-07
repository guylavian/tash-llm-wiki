---
title: "OSPF Link-State Advertisement Throttling"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-link-state-advertisement-throttling
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 30 OSPF Link-State Advertisement Throttling The OSPF Link-State Advertisement Throttling feature provides a dynamic mechanism to slow down link-state advertisement (LSA) updates in Open Shortest Path First (OSPF) during times of network instability. It also allows faster OSPF convergence by providing LSA rate limiting in milliseconds. • Finding Feature Information, page 285 • Prerequisit"
---

# OSPF Link-State Advertisement Throttling

CHAPTER

30

OSPF Link-State Advertisement Throttling
The OSPF Link-State Advertisement Throttling feature provides a dynamic mechanism to slow down
link-state advertisement (LSA) updates in Open Shortest Path First (OSPF) during times of network instability.
It also allows faster OSPF convergence by providing LSA rate limiting in milliseconds.
• Finding Feature Information, page 285
• Prerequisites for OSPF LSA Throttling, page 285
• Information About OSPF LSA Throttling, page 286
• How to Customize OSPF LSA Throttling, page 286
• Configuration Examples for OSPF LSA Throttling, page 291
• Additional References, page 291
• Feature Information for OSPF Link-State Advertisement Throttling, page 293

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPF LSA Throttling
It is presumed that you have OSPF configured in your network.

IP Routing: OSPF Configuration Guide
285


OSPF Link-State Advertisement Throttling
Information About OSPF LSA Throttling

Information About OSPF LSA Throttling
Benefits of OSPF LSA Throttling
Prior to the OSPF LSA Throttling feature, LSA generation was rate-limited for 5 seconds. That meant that
changes in an LSA could not be propagated in milliseconds, so the OSPF network could not achieve millisecond
convergence.
The OSPF LSA Throttling feature is enabled by default and allows faster OSPF convergence (in milliseconds).
This feature can be customized. One command controls the generation (sending) of LSAs, and another
command controls the receiving interval. This feature also provides a dynamic mechanism to slow down the
frequency of LSA updates in OSPF during times of network instability.

How OSPF LSA Throttling Works
The timers throttle lsa all command controls the generation (sending) of LSAs. The first LSA is always
generated immediately upon an OSPF topology change, and the next LSA generated is controlled by the
minimum start interval. The subsequent LSAs generated for the same LSA are rate-limited until the maximum
interval is reached. The "same LSA" is defined as an LSA instance that contains the same LSA ID number,
LSA type, and advertising router ID.
The timers lsa arrival command controls the minimum interval for accepting the same LSA. If an instance
of the same LSA arrives sooner than the interval that is set, the LSA is dropped. It is recommended that the
arrival interval be less than or equal to the hold-time interval of the timers throttle lsa all command.

How to Customize OSPF LSA Throttling
Customizing OSPF LSA Throttling
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. timers throttle lsa all start-interval hold-interval max-interval
5. timers lsa arrival milliseconds
6. end
7. show ip ospf timers rate-limit
8. show ip ospf

IP Routing: OSPF Configuration Guide
286


OSPF Link-State Advertisement Throttling
Customizing OSPF LSA Throttling

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

timers throttle lsa all start-interval hold-interval max-interval
Example:
Router(config-router)# timers throttle lsa all 100 10000
45000

(Optional) Sets the rate-limiting values (in
milliseconds) for LSA generation.
• The default values are as follows:
• start-intervalis 0 milliseconds.
• hold-intervalis 5000 milliseconds.
• max-intervalis 5000 milliseconds.

Step 5

timers lsa arrival milliseconds
Example:
Router(config-router)# timers lsa arrival 2000

(Optional) Sets the minimum interval (in
milliseconds) between instances of receiving the
same LSA.
• The default value is 1000 milliseconds.
• We suggest you keep the millisecondsvalue of
the LSA arrival timer less than or equal to the
neighbors’ hold-interval value of the timers
throttle lsa all command.

Step 6

end

Exits router configuration mode.

Example:
Router(config-router)# end

IP Routing: OSPF Configuration Guide
287


OSPF Link-State Advertisement Throttling
Customizing OSPF LSA Throttling

Step 7

Command or Action

Purpose

show ip ospf timers rate-limit

(Optional) Displays a list of the LSAs in the rate
limit queue (about to be generated).

Example:
Router# show ip ospf timers rate-limit

Example:

• The example shows two LSAs in the queue.
Each LSA is identified by LSA ID number,
Type (of LSA), Advertising router ID, and the
time in hours:minutes:seconds (to the
milliseconds) when the LSA is due to be
generated.

Example:
LSAID: 10.1.1.1
00:00:00.028

Type: 1

Adv Rtr: 172.16.2.2 Due in:

Example:
LSAID: 192.168.4.1
in: 00:00:00.028

Step 8

Type: 3

Adv Rtr: 172.17.2.2 Due

show ip ospf
Example:
Router# show ip ospf

Example:

Example:
Routing Process "ospf 4" with ID 10.10.24.4

Example:
Supports only single TOS(TOS0) routes

Example:
Supports opaque LSA

Example:
Supports Link-local Signaling (LLS)

Example:
Initial SPF schedule delay 5000 msecs

IP Routing: OSPF Configuration Guide
288

(Optional) Displays information about OSPF.
• The output lines that specify initial throttle
delay, minimum hold time for LSA throttle,
and maximum wait time for LSA throttle
indicate the LSA throttling values.


OSPF Link-State Advertisement Throttling
Customizing OSPF LSA Throttling

Command or Action

Purpose

Example:
Minimum hold time between two consecutive SPFs 10000
msecs

Example:
Maximum wait time between two consecutive SPFs 10000
msecs

Example:
Incremental-SPF disabled

Example:

Initial LSA throttle delay 100 msecs
Example:
Minimum hold time for LSA throttle 10000 msecs

Example:
Maximum wait time for LSA throttle 45000 msecs

Example:
Minimum LSA arrival 1000 msecs

Example:
LSA group pacing timer 240 secs

Example:
Interface flood pacing timer 33 msecs

Example:
Retransmission pacing timer 66 msecs

Example:
Number of external LSA 0. Checksum Sum 0x0

IP Routing: OSPF Configuration Guide
289


OSPF Link-State Advertisement Throttling
Customizing OSPF LSA Throttling

Command or Action
Example:
Number of opaque AS LSA 0. Checksum Sum 0x0

Example:
Number of DCbitless external and opaque AS LSA 0

Example:
Number of DoNotAge external and opaque AS LSA 0

Example:
Number of areas in this router is 1. 1 normal 0 stub 0
nssa

Example:
External flood list length 0

Example:
Area 24

Example:
Number of interfaces in this area is 2

Example:
Area has no authentication

Example:
SPF algorithm last executed 04:28:18.396 ago

Example:
SPF algorithm executed 8 times

Example:
Area ranges are

IP Routing: OSPF Configuration Guide
290

Purpose


OSPF Link-State Advertisement Throttling
Configuration Examples for OSPF LSA Throttling

Command or Action

Purpose

Example:
Number of LSA 4. Checksum Sum 0x23EB9

Example:
Number of opaque link LSA 0. Checksum Sum 0x0

Example:
Number of DCbitless LSA 0

Example:
Number of indication LSA 0

Example:
Number of DoNotAge LSA 0

Example:
Flood list length 0

Configuration Examples for OSPF LSA Throttling
Example OSPF LSA Throttling
This example customizes OSPF LSA throttling so that the start interval is 200 milliseconds, the hold interval
is 10,000 milliseconds, and the maximum interval is 45,000 milliseconds. The minimum interval between
instances of receiving the same LSA is 2000 milliseconds.
router ospf 1
log-adjacency-changes
timers throttle lsa all 200 10000 45000
timers lsa arrival 2000
network 10.10.4.0 0.0.0.255 area 24
network 10.10.24.0 0.0.0.255 area 24

Additional References
The following sections provide references related to OSPF LSA throttling.

IP Routing: OSPF Configuration Guide
291


OSPF Link-State Advertisement Throttling
Additional References

Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Configuring OSPF

"Configuring OSPF"

OSPFv3 Fast Convergence: LSA and SPF Throttling “OSPFv3 Fast Convergence: LSA and SPF Throttling”
module
OSPFv3 Max-Metric Router LSA

“OSPFv3 Max-Metric Router LSA” module

Standards
Standard

Title

None

--

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

None

--

IP Routing: OSPF Configuration Guide
292


OSPF Link-State Advertisement Throttling
Feature Information for OSPF Link-State Advertisement Throttling

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

Feature Information for OSPF Link-State Advertisement
Throttling
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
293


OSPF Link-State Advertisement Throttling
Feature Information for OSPF Link-State Advertisement Throttling

Table 33: Feature Information for OSPF Link-State Advertisement Throttling

Feature Name

Releases

Feature Information

OSPF Link-State Advertisement
Throttling

Cisco IOS XE Release 2.1 Cisco
IOS XE Release 2.6

The OSPF Link-State
Advertisement Throttling feature
provides a dynamic mechanism to
slow down link-state advertisement
(LSA) updates in OSPF during
times of network instability. It also
allows faster OSPF convergence
by providing LSA rate limiting in
milliseconds.
The following commands are
introduced or modified in the
feature documented in this module:
• debug ip ospf
database-timer rate-limit
• show ip ospf
• show ip ospf timers
rate-limit
• timers lsa arrival
• timers throttle lsa all

IP Routing: OSPF Configuration Guide
294
