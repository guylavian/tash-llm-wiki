---
title: "OSPFv2 Local RIB"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv2-local-rib
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 41 OSPFv2 Local RIB With the OSPFv2 Local RIB feature, each OSPF protocol instance has its own local Routing Information Base (RIB). The OSPF local RIB serves as the primary state for OSPF SPF route computation. The global RIB is not updated with intermediate results during the SPF. Instead, the global RIB is updated only when routes are added, deleted, or changed, thereby reducing globa"
---

# OSPFv2 Local RIB

CHAPTER

41

OSPFv2 Local RIB
With the OSPFv2 Local RIB feature, each OSPF protocol instance has its own local Routing Information
Base (RIB). The OSPF local RIB serves as the primary state for OSPF SPF route computation. The global
RIB is not updated with intermediate results during the SPF. Instead, the global RIB is updated only when
routes are added, deleted, or changed, thereby reducing global RIB computation. This reduced update activity
may result in fewer dropped packets.
This feature is enabled by default and does not need to be configured. This document describes some optional
configuration tasks to modify how the global and local RIBs function, although it is recommended to keep
the default settings.
• Finding Feature Information, page 391
• Prerequisites for OSPFv2 Local RIB, page 392
• Restrictions for OSPFv2 Local RIB, page 392
• Information About OSPFv2 Local RIB, page 392
• How to Configure OSPFv2 Local RIB, page 392
• Configuration Examples for OSPFv2 Local RIB, page 396
• Additional References, page 397
• Feature Information for OSPFv2 Local RIB, page 398

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
391


OSPFv2 Local RIB
Prerequisites for OSPFv2 Local RIB

Prerequisites for OSPFv2 Local RIB
Before this feature is configured, the OSPF routing protocol must be configured.

Restrictions for OSPFv2 Local RIB
This feature is available only for IP Version 4 networks.

Information About OSPFv2 Local RIB
A router that is running OSPFv2 maintains a local RIB in which it stores all routes to destinations that it has
learned from its neighbors. At the end of each SPF, OSPF attempts to install the best (that is, the least-cost)
routes to a destination present in the local RIB into the global IPv4 routing table. The global RIB will be
updated only when routes are added, deleted, or changed. Routes in the local RIB and Forwarding Information
Base (FIB) will not compute when intermediate results are computed during SPF, resulting in fewer dropped
packets in some circumstances.
By default, the contents of the global RIB are used to compute inter-area summaries, NSSA translation, and
forwarding addresses for type-5 and type-7 LSAs. Each of these functions can be configured to use the contents
of the OSPF local RIB instead of the global RIB for their computation. Using the local RIB for the computation
may be slightly faster in some circumstances, but because the local RIB has information for only a particular
instance of OSPF, using it for the computation may yield incorrect results. Potential problems that may occur
include routing loops and black-hole routes. It is recommended that you not change the default values because
they are conservative and preserve the current global RIB behavior.
By default, OSPF installs discard routes to null0 for any area range (internal) or summary-address (external)
prefixes that it advertises to other routers. Installation of a discard route can prevent routing loops in cases
where portions of a summary do not have a more specific route in the RIB. Normally, internal discard routes
are installed with an administrative distance of 110, while external discard routes have an administrative
distance of 254.
There may be rare circumstances, however, when some other values are needed. For example, if one OSPF
process installs a route that exactly matches an area range configured on another OSPF process, the internal
discard routes for the second OSPF process could be given a higher (less desirable) administrative distance.

How to Configure OSPFv2 Local RIB
Although it is recommended to keep the default settings for the commands described in the following sections,
it is optional to change the defaults settings.

IP Routing: OSPF Configuration Guide
392


OSPFv2 Local RIB
Changing the Default Local RIB Criteria

Changing the Default Local RIB Criteria
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id [vrf vpn-name]
4. local-rib-criteria [forwarding-address] [inter-area-summary] [nssa-translation]
5. end
6. show ip ospf process-id

rib [redistribution] [network-prefix] [network-mask] [detail]

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

router ospf process-id

[vrf vpn-name]

Configures an OSPFv2 routing process and enters
router configuration mode.

Example:
Device(config)# router ospf 23

Step 4

local-rib-criteria [forwarding-address]
[inter-area-summary] [nssa-translation]

Specifies that the OSPF local RIB will be used for
route validation.

Example:
Device(config-router)# local-rib-criteria
forwarding-address

Step 5

end

Returns to privileged EXEC mode.

Example:
Device(config-router)# end

IP Routing: OSPF Configuration Guide
393


OSPFv2 Local RIB
Changing the Administrative Distance for Discard Routes

Step 6

Command or Action

Purpose

show ip ospf process-id rib [redistribution]
[network-prefix] [network-mask] [detail]

Displays information for the OSPF local RIB or
locally redistributed routes.

Example:
Device# show ip ospf 23 rib

Changing the Administrative Distance for Discard Routes
Note

It is recommended that you keep the default settings. However, you can follow the steps in this section to
change the administrative distance for discard routes.

SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id [vrf vpn-name]
4. discard-route [external [distance]] [internal [distance]]
5. end
6. show ip route [ip-address [mask] [longer-prefixes] | protocol [process-id] | list [access-list-number |
access-list-name] | static download]

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
Example:
Device# configure terminal

IP Routing: OSPF Configuration Guide
394

Enters global configuration mode.


OSPFv2 Local RIB
Changing the Administrative Distance for Discard Routes

Command or Action
Step 3

router ospf process-id

Purpose
[vrf vpn-name]

Configures an OSPFv2 routing process and enters router
configuration mode.

Example:
Device(config)# router ospf 23

Step 4

discard-route [external [distance]] [internal
[distance]]

Reinstalls either an external or internal discard route that was
previously removed.
Note

Example:

You can now specify the administrative distance
for internal and external discard routes.

Device(config-router)# discard-route external
150

Step 5

Returns to privileged EXEC mode.

end
Example:
Device(config-router)# end

Step 6

show ip route [ip-address [mask] [longer-prefixes] | Displays the current state of the routing table.
protocol [process-id] | list [access-list-number |
Note
Entering the show ip route command will verify
access-list-name] | static download]
the changed administrative distance values for
external and internal discard routes.
Example:
Device# show ip route ospf 23

Example
The sample output displayed for the show ip route command confirms that the administrative distance for
the IP route 192.168.0.0/24 is 110.
Device# show ip route 192.168.0.0 255.255.255.0
Routing entry for 192.168.0.0/24

Known via "ospf 1", distance 110, metric 0, type intra area
Routing Descriptor Blocks:
* directly connected, via Null0
Route metric is 0, traffic share count is 1

IP Routing: OSPF Configuration Guide
395


OSPFv2 Local RIB
Configuration Examples for OSPFv2 Local RIB

Troubleshooting Tips
You can research the output from the debug ip ospf rib command to learn about the function of the local RIB
and the interaction between the route redistribution process and the global RIB. For example, you can learn
why the routes that OSPF placed in the global RIB are not the same ones that you anticipated.

Configuration Examples for OSPFv2 Local RIB
Example: Changing the Default Local RIB Criteria
In the following example, the local-rib-criteria command is entered without any keywords to specify that
the local RIB will be used as criteria for all of the following options: forwarding address, inter-area summary,
and NSSA translation.
router ospf 1
router-id 10.0.0.6
local-rib-criteria

Example: Changing the Administrative Distance for Discard Routes
In the following example, the administrative distance for external and internal discard routes is set to 25 and
30, respectively.
router ospf 1
router-id 10.0.0.6
log-adjacency-changes
discard-route external 25 internal 30
area 4 range 10.2.0.0 255.255.0.0
summary-address 192.168.130.2 255.255.255.0
redistribute static subnets
network 192.168.129.2 0.255.255.255 area 0
network 192.168.130.12 0.255.255.255 area 0

The output from the show ip route command verifies that the administrative distance for the internal route
10.2.0.0/16 is set to 30.
Device# show ip route 10.2.0.0 255.255.0.0
Routing entry for 10.2.0.0/16
Known via "ospf 1", distance 30, metric 1, type intra area
Routing Descriptor Blocks:
* directly connected, via Null0
Route metric is 1, traffic share count is 1

The output from the show ip route command verifies that the administrative distance for the external route
192.168.130.2/24 is set to 25.
Device# show ip route 192.168.130.2 255.255.255.0
Routing entry for 192.168.130.2/24
Known via "ospf 1", distance 25, metric 20, type intra area
Routing Descriptor Blocks:
* directly connected, via Null0
Route metric is 20, traffic share count is 1

IP Routing: OSPF Configuration Guide
396


OSPFv2 Local RIB
Additional References

Additional References
The following sections provide references related to OSPFv2 Local RIB.
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
397


OSPFv2 Local RIB
Feature Information for OSPFv2 Local RIB

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

Feature Information for OSPFv2 Local RIB
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
398


OSPFv2 Local RIB
Feature Information for OSPFv2 Local RIB

Table 48: Feature Information for the OSPFv2 Local RIB

Feature Name

Releases

Feature Information

OSPFv2 Local RIB

Cisco IOS XE Release 2.1

With the OSPFv2 Local RIB
feature, each OSPF protocol
instance has its own local Routing
Information Base (RIB). The OSPF
local RIB serves as the primary
state for OSPF SPF route
computation. The global RIB is not
updated with intermediate results
during the SPF. Instead, the global
RIB is updated only when routes
are added, deleted, or changed,
thereby reducing global RIB
computation. This reduced update
activity may result in fewer
dropped packets.
This feature is enabled by default
and does not need to be configured.
This document describes some
optional configuration tasks to
modify how the global and local
RIBs function, although it is
recommended to keep the default
settings.
The following commands were
introduced or modified: debug ip
ospf rib, discard-route,
local-rib-criteria, show ip ospf
rib.

IP Routing: OSPF Configuration Guide
399


OSPFv2 Local RIB
Feature Information for OSPFv2 Local RIB

IP Routing: OSPF Configuration Guide
400
