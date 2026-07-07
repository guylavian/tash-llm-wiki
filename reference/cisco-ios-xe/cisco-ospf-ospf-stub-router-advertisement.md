---
title: "OSPF Stub Router Advertisement"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-stub-router-advertisement
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 9 OSPF Stub Router Advertisement The OSPF Stub Router Advertisement feature allows you to bring a new router into a network without immediately routing traffic through the new router and allows you to gracefully shut down or reload a router without dropping packets that are destined for other networks. • Finding Feature Information, page 111 • Information About OSPF Stub Router Advertise"
---

# OSPF Stub Router Advertisement

CHAPTER

9

OSPF Stub Router Advertisement
The OSPF Stub Router Advertisement feature allows you to bring a new router into a network without
immediately routing traffic through the new router and allows you to gracefully shut down or reload a router
without dropping packets that are destined for other networks.
• Finding Feature Information, page 111
• Information About OSPF Stub Router Advertisement, page 111
• How to Configure OSPF Stub Router Advertisement, page 113
• Configuration Examples of OSPF Stub Router Advertisement, page 117
• Additional References, page 118
• Feature Information for OSPF Stub Router Advertisement, page 119

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPF Stub Router Advertisement
OSPF Stub Router Advertisement Functionality
The OSPF Stub Router Advertisement feature allows you to bring a new router into a network without
immediately routing traffic through the new router and allows you to gracefully shut down or reload a router
without dropping packets that are destined for other networks. This feature introduces three configuration

IP Routing: OSPF Configuration Guide
111


OSPF Stub Router Advertisement
Maximum Metric Allows Routing Tables to Converge

options that allow you to configure a router that is running the Open Shortest Path First (OSPF) protocol to
advertise a maximum or infinite metric to all neighbors.
When any of these three configuration options are enabled on a router, the router will originate link-state
advertisements (LSAs) with a maximum metric (LSInfinity: 0xFFFF) through all nonstub links. The
advertisement of a maximum metric causes other routers to assign a cost to the new router that is higher than
the cost of using an alternate path. Because of the high cost assigned to paths that pass through the new router,
other routers will not use a path through the new router as a transit path to forward traffic that is destined for
other networks, which allows switching and routing functions to be up and running and routing tables to
converge before transit traffic is routed through this router.

Note

Directly connected links in a stub network are not affected by the configuration of a maximum or infinite
metric because the cost of a stub link is always set to the output interface cost.

Maximum Metric Allows Routing Tables to Converge
Two configuration options introduced by the OSPF Stub Router Advertisement feature allow you to bring a
new router into a network without immediately routing traffic through the new router. These configuration
options are useful because Interior Gateway Protocols (IGPs) converge very quickly upon a router during
startup or after a reload, often before Border Gateway Protocol (BGP) routing tables have completely converged.
If neighbor routers forward traffic through a router while that router is building BGP routing tables, packets
that have been received for other destinations may be dropped. Advertising a maximum metric during startup
will allow routing tables to converge before traffic that is destined for other networks is sent through the
router.
The following two configuration options enable a router to advertise a maximum metric at startup:
• You can configure a timer to advertise a maximum metric when the router is started or reloaded. When
this option is configured, the router will advertise a maximum metric, which forces neighbor routers to
select alternate paths until the timer expires. When the timer expires, the router will advertise accurate
(normal) metrics, and other routers will send traffic to this router depending on the cost. The configurable
range of the timer is from 5 to 86,400 seconds.
• You can configure a router to advertise a maximum metric at startup until BGP routing tables converge
or until the default timer expires (600 seconds). Once BGP routing tables converge or the default timer
expires, the router will advertise accurate (normal) metrics and other routers will send traffic to this
router, depending on the cost.

Maximum Metric Allows Graceful Shutdown of a Router
The third configuration option introduced by the OSPF Stub Router Advertisement feature allows you to
gracefully remove a router from the network by advertising a maximum metric through all links, which allows
other routers to select alternate paths for transit traffic to follow before the router is shut down. There are
many situations where you may need to remove a router from the network. If a router is removed from a
network and neighbor routers cannot detect that the physical interface is down, neighbors will need to wait
for dead timers to expire before the neighbors will remove the adjacency and routing tables will reconverge.
This situation may occur when there is a switch between other routers and the router that is shut down. Packets
may be dropped while the neighbor routing tables reconverge.

IP Routing: OSPF Configuration Guide
112


OSPF Stub Router Advertisement
Benefits of OSPF Stub Router Advertisement

When this third option is configured, the router advertises a maximum metric, which allows neighbor routers
to select alternate paths before the router is shut down. This configuration option could also be used to remove
a router that is in a critical condition from the network without affecting traffic that is destined for other
networks.

Note

You should not save the running configuration of a router when it is configured for a graceful shutdown
because the router will continue to advertise a maximum metric after it is reloaded.

Benefits of OSPF Stub Router Advertisement
Improved Stability and Availability
Advertising a maximum metric through all links at startup or during a reload will prevent neighbor routers
from using a path through the router as a transit path, thereby reducing the number of packets that are dropped
and improving the stability and availability of the network.
Graceful Removal from the Network
Advertising a maximum metric before shutdown allows other routers to select alternate paths before the transit
path through a router becomes inaccessible.

How to Configure OSPF Stub Router Advertisement
The following tasks configure OSPF to advertise a maximum metric. This feature has three different
configuration options. All tasks are optional and should be individually configured.

Configuring Advertisement on Startup
SUMMARY STEPS
1. Router(config)# router ospf process-id
2. Router(config-router)# max-metric router-lsa on-startup announce-time

DETAILED STEPS
Command or Action

Purpose

Step 1

Router(config)# router ospf process-id

Places the router in router configuration mode and enables an OSPF routing
process.

Step 2

Router(config-router)# max-metric
router-lsa on-startup announce-time

Configures OSPF to advertise a maximum metric during startup for a
configured period of time. The announce-time argument is a configurable
timer that must follow the on-startup keyword to be configured. There is

IP Routing: OSPF Configuration Guide
113


OSPF Stub Router Advertisement
Configuring Advertisement Until Routing Tables Converge

Command or Action

Purpose
no default timer value. The configurable time range is from 5 to 86,400
seconds.

Configuring Advertisement Until Routing Tables Converge
SUMMARY STEPS
1. Router(config)# router ospf process-id
2. Router(config-router)# max-metric router-lsa on-startup wait-for-bgp

DETAILED STEPS
Command or Action

Purpose

Step 1

Router(config)# router ospf process-id

Places the router in router configuration mode and enables an OSPF
routing process.

Step 2

Router(config-router)# max-metric
router-lsa on-startup wait-for-bgp

Configures OSPF to advertise a maximum metric until BGP routing tables
have converged or until the default timer has expired. The wait-for-bgp
keyword must follow the on-startup keyword to be configured. The
default timer value is 600 seconds.

Configuring Advertisement for a Graceful Shutdown
SUMMARY STEPS
1. Router(config)# router ospfprocess-id
2. Router(config-router)# max-metric router-lsa
3. Router(config-router)# end
4. Router# show ip ospf

DETAILED STEPS

Step 1

Command or Action

Purpose

Router(config)# router ospfprocess-id

Places the router in router configuration mode and enables an OSPF
routing process.

IP Routing: OSPF Configuration Guide
114


OSPF Stub Router Advertisement
Verifying the Advertisement of a Maximum Metric

Command or Action

Purpose

Step 2

Router(config-router)# max-metric
router-lsa

Configures OSPF to advertise a maximum metric until the router is shut
down.

Step 3

Router(config-router)# end

Ends configuration mode and places the router in privileged EXEC mode.

Step 4

Router# show ip ospf

Displays general information about OSPF routing processes.
• Use the show ip ospf command to verify that the max-metric
router-lsa command has been enabled before the router is shut
down or reloaded.

What to Do Next

Note

Do not save the running configuration of a router when it is configured for a graceful shutdown because
the router will continue to advertise a maximum metric after it is reloaded.

Verifying the Advertisement of a Maximum Metric
To verify that the advertisement of a maximum metric has been configured correctly, use the show ip ospfor
show ip ospf databasecommand.
The output of the show ip ospfcommand will display the condition, state, and remaining time delay of the
advertisement of a maximum metric, depending on which options were configured with the max-metric
router-lsa command.
The following sample output is similar to the output that will be displayed when the on-startupkeyword and
announce-time argument are configured with the max-metric router-lsa command:
Router# show ip ospf
Routing Process "ospf 1998" with ID 10.18.134.155
Supports only single TOS(TOS0) routes
Supports opaque LSA
It is an area border and autonomous system boundary router
Redistributing External Routes from,
static, includes subnets in redistribution
Originating router-LSAs with maximum metric, Time remaining: 00:01:18
Condition: on startup for 300 seconds, State: active
SPF schedule delay 5 secs, Hold time between two SPFs 10 secs
Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs
Number of external LSA 7. Checksum Sum 0x47261
Number of opaque AS LSA 0. Checksum Sum 0x0
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 2. 1 normal 0 stub 1 nssa
External flood list length 0
Area BACKBONE(0)
Number of interfaces in this area is 1
Area has no authentication
SPF algorithm executed 3 times
Area ranges are

IP Routing: OSPF Configuration Guide
115


OSPF Stub Router Advertisement
Verifying the Advertisement of a Maximum Metric

Number of LSA 8. Checksum Sum 0x474AE
Number of opaque link LSA 0. Checksum Sum 0x0

The following sample output is similar to the output that will be displayed when the on-startupand wait-for-bgp
keywords are configured with the max-metric router-lsa command:
Router# show ip ospf
Routing Process "ospf 1998" with ID 10.18.134.155
Supports only single TOS(TOS0) routes
Supports opaque LSA
It is an area border and autonomous system boundary router
Redistributing External Routes from,
static, includes subnets in redistribution
Originating router-LSAs with maximum metric, Time remaining: 00:01:18
Condition: on startup while BGP is converging, State: active
SPF schedule delay 5 secs, Hold time between two SPFs 10 secs
Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs
Number of external LSA 7. Checksum Sum 0x47261
Number of opaque AS LSA 0. Checksum Sum 0x0
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 2. 1 normal 0 stub 1 nssa
External flood list length 0
Area BACKBONE(0)
Number of interfaces in this area is 1
Area has no authentication
SPF algorithm executed 3 times
Area ranges are
Number of LSA 8. Checksum Sum 0x474AE
Number of opaque link LSA 0. Checksum Sum 0x0

The following sample output is similar to the output that will be displayed when the max-metric router-lsa
command is configured without any keywords or arguments:
Router# show ip ospf
Routing Process "ospf 1998" with ID 10.18.134.155
Supports only single TOS(TOS0) routes
Supports opaque LSA
It is an area border and autonomous system boundary router
Redistributing External Routes from,
static, includes subnets in redistribution
Originating router-LSAs with maximum metric
Condition: always, State: active
SPF schedule delay 5 secs, Hold time between two SPFs 10 secs
Minimum LSA interval 5 secs. Minimum LSA arrival 1 secs
Number of external LSA 7. Checksum Sum 0x47261
Number of opaque AS LSA 0. Checksum Sum 0x0
Number of DCbitless external and opaque AS LSA 0
Number of DoNotAge external and opaque AS LSA 0
Number of areas in this router is 2. 1 normal 0 stub 1 nssa
External flood list length 0
Area BACKBONE(0)
Number of interfaces in this area is 1
Area has no authentication
SPF algorithm executed 3 times
Area ranges are
Number of LSA 8. Checksum Sum 0x474AE
Number of opaque link LSA 0. Checksum Sum 0x0

The output of the show ip ospf databasecommand will display information about OSPF LSAs and indicate
if the router is announcing maximum cost links. The following sample output is similar to the output that will
be displayed when any form of the max-metric router-lsa command is configured:
Router# show ip ospf database
Exception Flag: Announcing maximum link costs
LS age: 68
Options: (No TOS-capability, DC)
LS Type: Router Links
Link State ID: 172.18.134.155
Advertising Router: 172.18.134.155
LS Seq Number: 80000002

IP Routing: OSPF Configuration Guide
116


OSPF Stub Router Advertisement
Monitoring and Maintaining OSPF Stub Router Advertisement

Checksum: 0x175D
Length: 60
Area Border Router
AS Boundary Router
Number of Links: 3
Link connected to: a Transit Network
(Link ID) Designated Router address: 192.168.1.11
(Link Data) Router Interface address: 192.168.1.14
Number of TOS metrics: 0
TOS 0 Metrics: 65535 (metric used for local calculation: 10)
Link connected to: a Transit Network
(Link ID) Designated Router address: 10.1.145.11
(Link Data) Router Interface address: 10.1.145.14
Number of TOS metrics: 0
TOS 0 Metrics: 65535 (metric used for local calculation: 10)
Link connected to: a Stub Network
(Link ID) Network/subnet number: 10.11.12.0
(Link Data) Network Mask: 255.255.255.0
Number of TOS metrics: 0
TOS 0 Metrics: 1

Monitoring and Maintaining OSPF Stub Router Advertisement
Command
Router# show ip ospf

Router# show ip ospf database router

Purpose
Displays general information about OSPF routing
processes and provides information about the
configuration settings and status of the OSPF Stub
Router Advertisement feature.
Displays information about router LSAs, and indicates
if a router is announcing maximum link costs.

Configuration Examples of OSPF Stub Router Advertisement
Example Advertisement on Startup
In the following example, a router that is running OSPF is configured to advertise a maximum metric at startup
for 300 seconds:
Router(config)# router ospf 100
Router(config-router)# max-metric router-lsa on-startup 300

IP Routing: OSPF Configuration Guide
117


OSPF Stub Router Advertisement
Example Advertisement Until Routing Tables Converge

Example Advertisement Until Routing Tables Converge
In the following example, a router that is running OSPF is configured to advertise a maximum metric until
BGP routing tables converge or until the default timer expires (600 seconds):
Router(config)# router ospf 100
Router(config-router)# max-metric router-lsa on-startup wait-for-bgp

Example Graceful Shutdown
In the following example, a router that is running OSPF is configured to advertise a maximum metric until
the router is shut down:
Router(config)# router ospf 100
Router(config-router)# max-metric router-lsa
Router(config-router)# end
Router# show ip ospf

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

IP Routing: OSPF Configuration Guide
118


OSPF Stub Router Advertisement
Feature Information for OSPF Stub Router Advertisement

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

Feature Information for OSPF Stub Router Advertisement
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 12: Feature Information for OSPF Stub Router Advertisement

Feature Name

Releases

OSPF Stub Router Advertisement Cisco IOS XE Release 2.1

Feature Information
The OSPF Stub Router
Advertisement feature allows you
to bring a new router into a
network without immediately
routing traffic through the new
router and allows you to gracefully
shut down or reload a router
without dropping packets that are
destined for other networks.
The following commands are
introduced or modified in the
feature documented in this module:
• max-metric router-lsa
• show ip ospf

IP Routing: OSPF Configuration Guide
119


OSPF Stub Router Advertisement
Feature Information for OSPF Stub Router Advertisement

IP Routing: OSPF Configuration Guide
120
