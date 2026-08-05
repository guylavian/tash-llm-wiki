---
title: "Configuring OSPF TTL Security Check and OSPF Graceful Shutdown"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-configuring-ospf-ttl-security-check-and-ospf-graceful-shutdown
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 38 Configuring OSPF TTL Security Check and OSPF Graceful Shutdown This module describes configuration tasks to configure various options involving Open Shortest Path First (OSPF). This module contains tasks that use commands to configure a lightweight security mechanism to protect OSPF sessions from CPU-utilization-based attacks and to configure a router to shut down a protocol temporari"
---

# Configuring OSPF TTL Security Check and OSPF Graceful Shutdown

CHAPTER

38

Configuring OSPF TTL Security Check and OSPF
Graceful Shutdown
This module describes configuration tasks to configure various options involving Open Shortest Path First
(OSPF). This module contains tasks that use commands to configure a lightweight security mechanism to
protect OSPF sessions from CPU-utilization-based attacks and to configure a router to shut down a protocol
temporarily without losing the protocol configuration.
• Finding Feature Information, page 357
• Information About OSPF TTL Security Check and OSPF Graceful Shutdown, page 358
• How to Configure OSPF TTL Security Check and OSPF Graceful Shutdown, page 359
• Configuration Examples for OSPF TTL Security Check and OSPF Graceful Shutdown, page 363
• Additional References, page 364
• Feature Information for Configuring OSPF TTL Security Check and OSPF Graceful Shutdown, page
365

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
357


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Information About OSPF TTL Security Check and OSPF Graceful Shutdown

Information About OSPF TTL Security Check and OSPF Graceful
Shutdown
TTL Security Check for OSPF
When the TTL Security Check feature is enabled, OSPF sends outgoing packets with an IP header Time to
Live (TTL) value of 255 and discards incoming packets that have TTL values less than a configurable threshold.
Since each device that forwards an IP packet decrements the TTL, packets received via a direct (one-hop)
connection will have a value of 255. Packets that cross two hops will have a value of 254, and so on. The
receive threshold is configured in terms of the maximum number of hops that a packet may have traveled.
The value for this hop-count argument is a number from 1 to 254, with a default of 1.
The TTL Security Check feature may be configured under the OSPF router submode, in which case it applies
to all the interfaces on which OSPF runs, or it may be configured on a per-interface basis.

Transitioning Existing Networks to Use TTL Security Check
If you currently have OSPF running in your network and want to implement TTL security on an
interface-by-interface basis without any network interruptions, use the ip ospf ttl-security command and set
the hop-count argument to 254. This setting causes outgoing packets to be sent with a TTL value of 255, but
allows any value for input packets. Later, once the device at the other end of the link has had TTL security
enabled you can start enforcing the hop limit for the incoming packets by using the same ip ospf ttl-security
command with no hop count specified. This process ensures that OSPF packets will not be dropped because
of a temporary mismatch in TTL security.

TTL Security Check for OSPF Virtual and Sham Links
In OSPF, all areas must be connected to a backbone area. If there is a break in backbone continuity, or the
backbone is purposefully partitioned, you can establish a virtual link. The virtual link must be configured in
both devices. The configuration information in each device consists of the other virtual endpoint (the other
area border router [ABR]) and the nonbackbone area that the two devices have in common (called the transit
area.) Note that virtual links cannot be configured through stub areas. Sham links are similar to virtual links
in many ways, but sham links are used in Layer 3 Multiprotocol Label Switching (MPLS) Virtual Private
Network (VPN) networks to connect Provider Edge (PE) routers across the MPLS backbone.
To establish a virtual link or a sham link, use the area virtual-link or area sham-link cost commands,
respectively, in router configuration mode. To configure the TTL Security Check feature on a virtual link or
a sham link, configure the ttl-security keyword and the hop-count argument in either command. Note that
the hop-count argument value is mandatory in this case.

Benefits of the OSPF Support for TTL Security Check
The OSPF Support for TTL Security Check feature provides an effective and easy-to-deploy solution to protect
OSPF neighbor sessions from CPU utilization-based attacks. When this feature is enabled, a host cannot attack
an OSPF session if the host is not a member of the local or remote OSPF network, or if the host is not directly

IP Routing: OSPF Configuration Guide
358


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
OSPF Graceful Shutdown

connected to a network segment between the local and remote OSPF networks. This solution greatly reduces
the effectiveness of Denial of Service (DoS) attacks against an OSPF autonomous system.

OSPF Graceful Shutdown
The OSPF Graceful Shutdown feature provides the ability to temporarily shut down the OSPF protocol in the
least disruptive manner and notify its neighbors that it is going away. All traffic that has another path through
the network will be directed to that alternate path. A graceful shutdown of the OSPF protocol can be initiated
using the shutdown command in router configuration mode.
This feature also provides the ability to shut down OSPF on a specific interface. In this case, OSPF will not
advertise the interface or form adjacencies over it; however, all of the OSPF interface configuration will be
retained. To initiate a graceful shutdown of an interface, use the ip ospf shutdown command in interface
configuration mode.

How to Configure OSPF TTL Security Check and OSPF Graceful
Shutdown
Configuring TTL Security Check on All OSPF Interfaces
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospf process-id
4. ttl-security all-interfaces [ hops

hop-count ]

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

IP Routing: OSPF Configuration Guide
359


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Configuring TTL Security Check on a Per-Interface Basis

Step 3

Command or Action

Purpose

router ospf process-id

Enables OSPF routing, which places the device in router
configuration mode.

Example:
Device(config)# router ospf 109

Step 4

ttl-security all-interfaces [ hops
]

hop-count Configures TTL security check on all OSPF interfaces.
Note

Example:
Device(config-router)# ttl-security
all-interfaces

Step 5

This configuration step applies only to normal OSPF
interfaces. This step does not apply to virtual links or
sham links that require TTL security protection. Virtual
links and sham links must be configured independently.

Returns to privileged EXEC mode.

end
Example:
Device(config-router)# end

Configuring TTL Security Check on a Per-Interface Basis
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. ip ospf ttl-security [hops

hop-count | disable]

5. end
6. show ip ospf [process-id] interface [interface type interface-number] [brief] [multicast] [topology
topology-name | base}]
7. show ip ospf neighbor interface-type interface-number [neighbor-id][detail]
8. show ip ospf [process-id] traffic [interface-type interface-number]
9. debug ip ospf adj

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: OSPF Configuration Guide
360


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Configuring TTL Security Check on a Per-Interface Basis

Command or Action

Purpose
• Enter your password if prompted.

Example:
Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

interface type number

Configures an interface type and enters interface configuration
mode.

Example:
Device(config)# interface GigabitEthernet
0/0/0

Step 4

ip ospf ttl-security [hops

hop-count | disable] Configures TTL security check feature on a specific interface.

Example:
Device(config-if)# ip ospf ttl-security

• The hop-countargument range is from 1 to 254.
• The disable keyword can be used to disable TTL security
on an interface. It is useful only if the ttl-security
all-interfaces comand initially enabled TTL security on all
OSPF interfaces, in which case disable can be used as an
override or to turn off TTL security on a specific interface.
• In the example, TTL security is being disabled on
GigabitEthernet interface 0/0/0.

Step 5

end

Returns to privileged EXEC mode.

Example:
Device(config-if)# end

Step 6

show ip ospf [process-id] interface [interface
type interface-number] [brief] [multicast]
[topology topology-name | base}]

(Optional) Displays OSPF-related interface information.

Example:
Device# show ip ospf interface
gigabitethernet 0/0/0

Step 7

show ip ospf neighbor interface-type
interface-number [neighbor-id][detail]
Example:

(Optional) Displays OSPF neighbor information on a per-interface
basis.
• If one side of the connection has TTL security enabled, the
other side shows the neighbor in the INIT state.

Device# show ip ospf neighbor 10.199.199.137

IP Routing: OSPF Configuration Guide
361


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Configuring OSPF Graceful Shutdown on a Per-Interface Basis

Step 8

Command or Action

Purpose

show ip ospf [process-id] traffic [interface-type
interface-number]

(Optional) Displays OSPF traffic statistics.

Example:

• The number of times a TTL security check failed is included
in the output.

Device# show ip ospf traffic

Step 9

debug ip ospf adj
Example:
Device# debug ip ospf adj

(Optional) Initiates debugging of OSPF adjacency events.
• Information about dropped packets, including interface type
and number, neighbor IP address, and TTL value, is included
in the command output.

Configuring OSPF Graceful Shutdown on a Per-Interface Basis
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. ip ospf shutdown
5. end
6. show ip ospf [ process-id ] interface [ interface type interface-number ] [ brief ] [multicast]
[topology topology-name | base}]
7. show ip ospf [ process-id ]

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
362

Enters global configuration mode.


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Configuration Examples for OSPF TTL Security Check and OSPF Graceful Shutdown

Step 3

Command or Action

Purpose

interface type number

Configures an interface type and number and enters interface
configuration mode.

Example:
Device(config)# interface GigabitEthernet 0/1/0

Step 4

ip ospf shutdown
Example:
Device(config-if)# ip ospf shutdown

Step 5

Initiates an OSPF protocol graceful shutdown at the interface
level.
• When the ip ospf shutdown interface command is
entered, the interface on which it is configured sends a
link-state update advising its neighbors that is going
down, which allows those neighbors to begin routing
OSPF traffic around this router.
Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Step 6

show ip ospf [ process-id ] interface [ interface
type interface-number ] [ brief ] [multicast]
[topology topology-name | base}]

(Optional) Displays OSPF-related interface information.

Example:
Device# show ip ospf interface GigabitEthernet

0/1/0
Step 7

show ip ospf [ process-id ]

(Optional) Displays general information about OSPF routing
processes.

Example:
Device# show ip ospf

Configuration Examples for OSPF TTL Security Check and OSPF
Graceful Shutdown
Example: Transitioning an Existing Network to Use TTL Security Check
The following example shows how to enable TTL security in an existing OSPF network on a per-interface
basis.

IP Routing: OSPF Configuration Guide
363


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Additional References

Configuring TTL security in an existing network is a three-step process:
1 Configure TTL security with a hop count of 254 on the OSPF interface on the sending side device.
2 Configure TTL security with no hop count on the OSPF interface on the receiving side device.
3 Reconfigure the sending side OSPF interface with no hop count.
configure terminal
! Configure the following command on the sending side router.
interface gigabitethernet 0/1/0
ip ospf ttl-security hops 254
! Configure the next command on the receiving side router.
interface gigabitethernet 0/1/0
ip ospf ttl-security
! Reconfigure the sending side with no hop count.
ip ospf ttl-security
end

Additional References
The following sections provide references related to the OSPF TTL Security Check and OSPF Graceful
Shutdown features.
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

No new or modified standards are supported and
-support for existing standards has not been modified.

MIBs
MIB

MIBs Link

No new or modified MIBs are supported and support To locate and download MIBs for selected platforms,
for existing MIBs has not been modified.
software releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: OSPF Configuration Guide
364


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Feature Information for Configuring OSPF TTL Security Check and OSPF Graceful Shutdown

RFCs
RFC

Title

No new or modified RFCs are supported and support -for existing RFCs has not been modified.

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

Feature Information for Configuring OSPF TTL Security Check
and OSPF Graceful Shutdown
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
365


Configuring OSPF TTL Security Check and OSPF Graceful Shutdown
Feature Information for Configuring OSPF TTL Security Check and OSPF Graceful Shutdown

Table 45: Feature Information for Configuring OSPF TTL Security Check and OSPF Graceful Shutdown

Feature Name

Releases

Feature Information

OSPF Graceful Shutdown

Cisco IOS XE Release 2.1

This feature provides the ability to
temporarily shut down a protocol
in the least disruptive manner and
to notify its neighbors that it is
going away.
A graceful shutdown of a protocol
can be initiated on all OSPF
interfaces or on a specific interface.
The following commands were
introduced or modified:
• ip ospf shutdown
• show ip ospf
• show ip ospf interface
• shutdown (router OSPF)

OSPF TTL Security Check

Cisco IOS XE Release 2.1

This feature increases protection
against OSPF denial of service
attacks, enables checking of TTL
values on OSPF packets from
neighbors, and allows users to set
TTL values sent to neighbors.
The following commands were
introduced or modified:
• area sham-link cost
• area virtual-link
• debug ip ospf adj
• ip ospf ttl-security
• show ip ospf interface
• show ip ospf neighbor
• show ip ospf traffic
• ttl-security all-interfaces

IP Routing: OSPF Configuration Guide
366
