---
title: "BGP Support for BFD"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-bfd
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 28 BGP Support for BFD Bidirectional Forwarding Detection (BFD) is a detection protocol designed to provide fast forwarding path failure detection times for all media types, encapsulations, topologies, and routing protocols. In addition to fast forwarding path failure detection, BFD provides a consistent failure detection method for network administrators. Because the network administrat"
---

# BGP Support for BFD

CHAPTER

28

BGP Support for BFD
Bidirectional Forwarding Detection (BFD) is a detection protocol designed to provide fast forwarding path
failure detection times for all media types, encapsulations, topologies, and routing protocols. In addition to
fast forwarding path failure detection, BFD provides a consistent failure detection method for network
administrators. Because the network administrator can use BFD to detect forwarding path failures at a uniform
rate, rather than the variable rates for different routing protocol hello mechanisms, network profiling and
planning will be easier, and reconvergence time will be consistent and predictable. The main benefit of
implementing BFD for BGP is a significantly faster reconvergence time.
• Finding Feature Information, on page 529
• Information About BGP Support for BFD, on page 529
• How to Decrease BGP Convergence Time Using BFD, on page 530
• Additional References, on page 533
• Feature Information for BGP Support for BFD, on page 534

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Support for BFD
BFD for BGP
Bidirectional Forwarding Detection (BFD) is a detection protocol designed to provide fast forwarding path
failure detection times for all media types, encapsulations, topologies, and routing protocols. In addition to
fast forwarding path failure detection, BFD provides a consistent failure detection method for network
administrators. Because the network administrator can use BFD to detect forwarding path failures at a uniform
rate, rather than the variable rates for different routing protocol hello mechanisms, network profiling and

IP Routing: BGP Configuration Guide
529


BGP Support for BFD
How to Decrease BGP Convergence Time Using BFD

planning will be easier, and reconvergence time will be consistent and predictable. The main benefit of
implementing BFD for BGP is a marked decrease in reconvergence time.
See also the “Configuring BGP Neighbor Session Options” chapter, the section “Configuring BFD for BGP
IPv6 Neighbors.”
For more details about BFD, see the Cisco IOS IP Routing: BFD Configuration Guide.

How to Decrease BGP Convergence Time Using BFD
Prerequisites
• Cisco Express Forwarding (CEF) and IP routing must be enabled on all participating routers.
• BGP must be configured on the routers before BFD is deployed. You should implement fast convergence
for the routing protocol that you are using. See the IP routing documentation for your version of Cisco
IOS software for information on configuring fast convergence.

Restrictions
• For the Cisco implementation of BFD Support for BGP in Cisco IOS Release15.1(1)SG, only asynchronous
mode is supported. In asynchronous mode, either BFD peer can initiate a BFD session.
• IPv6 encapsulation is supported.
• BFD multihop is supported.

Decreasing BGP Convergence Time Using BFD
You start a BFD process by configuring BFD on the interface. When the BFD process is started, no entries
are created in the adjacency database, in other words, no BFD control packets are sent or received. The
adjacency creation takes places once you have configured BFD support for the applicable routing protocols.
The first two tasks must be configured to implement BFD support for BGP to reduce the BGP convergence
time. The third task is an optional task to help monitor or troubleshoot BFD.
See also the “Configuring BFD for BGP IPv6 Neighbors” section in the “Configuring BGP Neighbor Session
Options” module.

Configuring BFD Session Parameters on the Interface
The steps in this procedure show how to configure BFD on the interface by setting the baseline BFD session
parameters on an interface. Repeat the steps in this procedure for each interface over which you want to run
BFD sessions to BFD neighbors.
SUMMARY STEPS
1. enable
2. configure terminal

IP Routing: BGP Configuration Guide
530


BGP Support for BFD
Configuring BFD Support for BGP

3. interface type number
4. bfd interval milliseconds min_rx milliseconds multiplier interval-multiplier
5. end
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

interface type number

Enters interface configuration mode.

Example:
Router(config)# interface FastEthernet 6/0

Step 4

bfd interval milliseconds min_rx milliseconds
multiplier interval-multiplier

Enables BFD on the interface.

Example:
Router(config-if)# bfd interval 50 min_rx 50
multiplier 5

Step 5

Exits interface configuration mode.

end
Example:
Router(config-if)# end

Configuring BFD Support for BGP
Perform this task to configure BFD support for BGP, so that BGP is a registered protocol with BFD and will
receive forwarding path detection failure messages from BFD.
Before you begin
• BGP must be running on all participating routers.
• The baseline parameters for BFD sessions on the interfaces over which you want to run BFD sessions
to BFD neighbors must be configured. See "Configuring BFD Session Parameters on the Interface" for
more information.

IP Routing: BGP Configuration Guide
531


BGP Support for BFD
Configuring BFD Support for BGP

SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.

enable
configure terminal
router bgp autonomous-system-number
neighbor ip-address fall-over bfd
end
show bfd neighbors [details]
show ip bgp neighbors [ip-address [received-routes | routes | advertised-routes | paths [regexp] |
dampened-routes | flap-statistics | received prefix-filter | policy [detail]]]

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

Enters global configuration mode.

configure terminal
Example:
Router# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Specifies a BGP process and enters router configuration
mode.

Router(config)# router bgp tag1

Step 4

neighbor ip-address

fall-over bfd

Enables BFD support for fallover.

Example:
Router(config-router)# neighbor 172.16.10.2
fall-over bfd

Step 5

Returns the router to privileged EXEC mode.

end
Example:
Router(config-router)# end

Step 6

show bfd neighbors [details]
Example:

Verifies that the BFD neighbor is active and displays the
routing protocols that BFD has registered.

Router# show bfd neighbors detail

Step 7

Displays information about BGP and TCP connections to
show ip bgp neighbors [ip-address [received-routes |
neighbors.
routes | advertised-routes | paths [regexp] |
dampened-routes | flap-statistics | received prefix-filter
| policy [detail]]]

IP Routing: BGP Configuration Guide
532


BGP Support for BFD
Monitoring and Troubleshooting BFD

Command or Action

Purpose

Example:
Router# show ip bgp neighbors

Monitoring and Troubleshooting BFD
To monitor or troubleshoot BFD, perform one or more of the steps in this section.
SUMMARY STEPS
1. enable
2. show bfd neighbors [details]
3. debug bfd [event | packet | ipc-error | ipc-event | oir-error | oir-event]
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

show bfd neighbors [details]
Example:

(Optional) Displays the BFD adjacency database.
• The details keyword shows all BFD protocol
parameters and timers per neighbor.

Router# show bfd neighbors details

Step 3

debug bfd [event | packet | ipc-error | ipc-event | oir-error (Optional) Displays debugging information about BFD
packets.
| oir-event]
Example:
Router# debug bfd packet

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

BFD commands

Cisco IOS IP Routing: Protocol Independent Command
Reference

IP Routing: BGP Configuration Guide
533


BGP Support for BFD
Feature Information for BGP Support for BFD

Related Topic

Document Title

Configuring BFD support for another routing
protocol

IP Routing: BFD Configuration Guide

Technical Assistance
Description

Link

The Cisco Support and Documentation website provides http://www.cisco.com/cisco/web/support/index.html
online resources to download documentation, software,
and tools. Use these resources to install and configure
the software and to troubleshoot and resolve technical
issues with Cisco products and technologies. Access to
most tools on the Cisco Support and Documentation
website requires a Cisco.com user ID and password.

Feature Information for BGP Support for BFD
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.

IP Routing: BGP Configuration Guide
534


BGP Support for BFD
Feature Information for BGP Support for BFD

Table 44: Feature Information for BGP Support for BFD

Feature Name

Releases

Feature Information

BGP Support for BFD

12.2(33)SRA

Bidirectional Forwarding Detection
(BFD) is a detection protocol
designed to provide fast forwarding
path failure detection times for all
media types, encapsulations,
topologies, and routing protocols.
In addition to fast forwarding path
failure detection, BFD provides a
consistent failure detection method
for network administrators. Because
the network administrator can use
BFD to detect forwarding path
failures at a uniform rate, rather
than the variable rates for different
routing protocol hello mechanisms,
network profiling and planning will
be easier, and reconvergence time
will be consistent and predictable.
The main benefit of implementing
BFD for BGP is a significantly
faster reconvergence time.

12.2(33)SB
15.1(1)SG
Cisco IOS XE Release 2.1
Cisco IOS XE Release 3.5S

The following commands were
introduced or modified by this
feature: bfd, neighbor fall-over,
show bfd neighbors, and show ip
bgp neighbors.

IP Routing: BGP Configuration Guide
535


BGP Support for BFD
Feature Information for BGP Support for BFD

IP Routing: BGP Configuration Guide
536
