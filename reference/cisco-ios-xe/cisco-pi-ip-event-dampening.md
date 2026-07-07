---
title: "IP Event Dampening"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-ip-event-dampening
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 4 IP Event Dampening The IP Event Dampening feature introduces a configurable exponential decay mechanism to suppress the effects of excessive interface flapping events on routing protocols and routing tables in the network. This feature allows the network operator to configure a router to automatically identify and selectively dampen a local interface that is flapping. • Finding Feature"
---

# IP Event Dampening

CHAPTER

4

IP Event Dampening
The IP Event Dampening feature introduces a configurable exponential decay mechanism to suppress the
effects of excessive interface flapping events on routing protocols and routing tables in the network. This
feature allows the network operator to configure a router to automatically identify and selectively dampen a
local interface that is flapping.
• Finding Feature Information, on page 51
• Restrictions for IP Event Dampening, on page 51
• Information About IP Event Dampening, on page 52
• How to Configure IP Event Dampening, on page 55
• Configuration Examples for IP Event Dampening, on page 57
• Additional References, on page 58
• Feature Information for IP Event Dampening, on page 59
• Glossary, on page 59

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Restrictions for IP Event Dampening
Subinterface Restrictions
Only primary interfaces can be configured with this feature. The primary interface configuration is applied
to all subinterfaces by default. IP Event Dampening does not track the flapping of individual subinterfaces
on an interface.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
51


IP Event Dampening
Information About IP Event Dampening

Virtual Templates Not Supported
Copying a dampening configuration from virtual templates to virtual access interfaces is not supported because
dampening has limited usefulness to existing applications that use virtual templates. Virtual access interfaces
are released when an interface flaps, and new connections and virtual access interfaces are acquired when the
interface comes up and is made available to the network. Since dampening states are attached to the interface,
the dampening states would not survive an interface flap.
IPX Routing Protocols Not Supported
Internetwork Packet Exchange (IPX) protocols are not supported by the IP Event Dampening feature. However,
IPX variants of these protocols will still receive up and down state event information when this feature is
enabled. This should not create any problems or routing issues.

Information About IP Event Dampening
IP Event Dampening Overview
Interface state changes occur when interfaces are administratively brought up or down or if an interface
changes state. When an interface changes state or flaps, routing protocols are notified of the status of the
routes that are affected by the change in state. Every interface state change requires all affected devices in the
network to recalculate best paths, install or remove routes from the routing tables, and then advertise valid
routes to peer routers. An unstable interface that flaps excessively can cause other devices in the network to
consume substantial amounts of system processing resources and cause routing protocols to lose synchronization
with the state of the flapping interface.
The IP Event Dampening feature introduces a configurable exponential decay mechanism to suppress the
effects of excessive interface flapping events on routing protocols and routing tables in the network. This
feature allows the network operator to configure a router to automatically identify and selectively dampen a
local interface that is flapping. Dampening an interface removes the interface from the network until the
interface stops flapping and becomes stable. Configuring the IP Event Dampening feature improves convergence
times and stability throughout the network by isolating failures so that disturbances are not propagated. This,
in turn, reduces the utilization of system processing resources by other devices in the network and improves
overall network stability.

Interface State Change Events
This section describes the interface state change events of the IP Event Dampening features. This feature
employs a configurable exponential decay mechanism that is used to suppress the effects of excessive interface
flapping or state changes. When the IP Event Dampening feature is enabled, flapping interfaces are dampened
from the perspective of the routing protocol by filtering excessive route updates. Flapping interfaces are
identified, assigned penalties, suppressed if the necessary, and made available to the network when the interface
stabilizes.

Suppress Threshold
The suppress threshold is the value of the accumulated penalty that triggers the router to dampen a flapping
interface. The flapping interface is identified by the router and assigned a penalty for each up and down state
change, but the interface is not automatically dampened. The router tracks the penalties that a flapping interface

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
52


IP Event Dampening
Half-Life Period

accumulates. When the accumulated penalty reaches the default or preconfigured suppress threshold, the
interface is placed in a dampened state.

Half-Life Period
The half-life period determines how fast the accumulated penalty can decay exponentially. When an interface
is placed in a dampened state, the router monitors the interface for additional up and down state changes. If
the interface continues to accumulate penalties and the interface remains in the suppress threshold range, the
interface will remain dampened. If the interface stabilizes and stops flapping, the penalty is reduced by half
after each half-life period expires. The accumulated penalty will be reduced until the penalty drops to the
reuse threshold. The configurable range of the half-life period timer is from 1 to 30 seconds. The default
half-life period timer is 5 seconds.

Reuse Threshold
When the accumulated penalty decreases until the penalty drops to the reuse threshold, the route is unsuppressed
and made available to the other devices on the network. The range of the reuse value is from 1 to 20,000
penalties. The default value is 1000 penalties.

Maximum Suppress Time
The maximum suppress time represents the maximum amount of time an interface can remain dampened
when a penalty is assigned to an interface. The maximum suppress time can be configured from 1 to 20,000
seconds. The default of the maximum penalty timer is 20 seconds or four times the default half-life period (5
seconds). The maximum value of the accumulated penalty is calculated, based on the maximum suppress
time, reuse threshold, and half-life period.

Affected Components
When an interface is not configured with dampening, or when an interface is configured with dampening but
is not suppressed, the routing protocol behavior as a result of interface state transitions is not changed by the
IP Event Dampening feature. However, if an interface is suppressed, the routing protocols and routing tables
are immune to any further state transitions of the interface until it is unsuppressed.

Route Types
The following interfaces are affected by the configuration of this feature:
• Connected routes:
• The connected routes of dampened interfaces are not installed into the routing table.
• When a dampened interface is unsuppressed, the connected routes will be installed into the routing
table if the interface is up.
• Static routes:
• Static routes assigned to a dampened interface are not installed into the routing table.
• When a dampened interface is unsuppressed, the static route will be installed into the routing table
if the interface is up.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
53


IP Event Dampening
Supported Protocols

Note

Only the primary interface can be configured with this feature, and all subinterfaces are subject to the same
dampening configuration as the primary interface. IP Event Dampening does not track the flapping of individual
subinterfaces on an interface.

Supported Protocols
The IP Event Dampening feature supports Routing Information Protocol (RIP), Open Shortest Path First
(OSPF), Enhanced Interior Gateway Routing Protocol (EIGRP), Intermediate System-to-Intermediate System
(IS-IS), Border Gateway Protocol (BGP), Connectionless Network Services (CLNS), and Hot Standby Routing
Protocol (HSRP). The following list provides some general information about the operation of this feature
with these protocols.
• RIP, OSPF, EIGRP, IS-IS, and BGP:
• When an interface is dampened, the interface is considered to be down by the routing protocol. The
routing protocol will not hold any adjacencies with this peer router over the dampened interface or
generate advertisements of any routes related to this interface to other peer routers.
• When the interface is unsuppressed and made available to the network, the interface will be considered
by the routing protocols to be up. The routing protocols will be notified that the interface is in an
up state and routing conditions will return to normal.
• HSRP:
• When an interface is dampened, it is considered to be down by HSRP. HSRP will not generate
HSRP messages out of the dampened interface or respond to any message received by the dampened
interface. When the interface is unsuppressed and made available to the network, HSRP will be
notified of the up state and will return to normal operations.
• CLNS:
• When an interface is dampened, the interface is dampened to both IP and CLNS routing equally.
The interface is dampened to both IP and CLNS because integrated routing protocols like IS-IS, IP,
and CLNS routing are closely interconnected, so it is impossible to apply dampening separately.

Note

The IP Event Dampening feature has no effect on any routing protocols if it is not enabled or an interface is
not dampened.

Network Deployments
In real network deployments, some routers may not be configured with interface dampening, and all routers
may not even support this feature. No major routing issues are expected, even if the router at the other end of
a point-to-point interface or routers of the same multicast LAN do not have interface dampening turned on
or do not have this feature implemented. On the router, where the interface is dampened, routes associated
with the interface will not be used. No packets will be sent out of this interface, and no routing protocol activity
will be initiated with routers on the other side of the interface. However, routers on the other side can still
install some routes, in their routing tables, that are associated with this subnet because the routers recognize
that their own interfaces are up and can start forwarding packets to the dampened interface. In such situations,

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
54


IP Event Dampening
Benefits of IP Event Dampening

the router with the dampened interface will start forwarding these packets, depending on the routes in its
routing table.
The IP Event Dampening feature does not introduce new information into the network. In fact, the effect of
dampening is to subtract a subset of routing information from the network. Therefore, looping should not
occur as a result of dampening.

Benefits of IP Event Dampening
Reduced Processing Load
The IP Event Dampening Feature employs a configurable exponential decay mechanism to suppress the effects
of excessive interface flapping events on routing protocols. Excessive interface up and down state changes
that are received in a short period of time are not processed and do not consume system resources. Other
routers in the network need not waste system resources because of a flapping route.
Faster Convergence
The IP Event Dampening feature improves convergence times and stability throughout the network by isolating
failures so that disturbances are not propagated. Routers that are not experiencing link flap reach convergence
sooner, because routing tables are not rebuilt each time the offending router leaves and enters the service
Improved Network Stability
The IP Event Dampening feature provides increased network stability. A router with a flapping interface
removes the flapping interface from the network until the interface stabilizes, so other routers simply redirect
traffic around the affected router until the interface becomes stable, which ensures that the router loses no
data packets.

How to Configure IP Event Dampening
Enabling IP Event Dampening
The dampening command is entered in interface configuration mode to enable the IP Event Dampening
feature. If this command is applied to an interface that already has dampening configured, all dampening
states are reset and the accumulated penalty will be set to 0. If the interface has been dampened, the accumulated
penalty will fall into the reuse threshold range, and the dampened interface will be made available to the
network. The flap counts, however, are retained.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
interface type number
dampening [half-life-period reuse-threshold] [suppress-threshold max-suppress [restart-penalty]]
end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
55


IP Event Dampening
Verifying IP Event Dampening

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
Example:

Enters interface configuration mode and configures the
specified interface.

Router(config)# interface type number

Step 4

dampening [half-life-period reuse-threshold]
[suppress-threshold max-suppress [restart-penalty]]
Example:
Router(config-if)# dampening

Step 5

Enables interface dampening.
• Entering the dampening command without any
arguments enables interface dampening with the
default configuration parameters.
• When manually configuring the timer for the
restart-penalty argument, the values must be manually
entered for all arguments.
Exits interface configuration mode and enters privileged
EXEC mode.

end
Example:
Router(config-if)# end

Verifying IP Event Dampening
Use the show dampening interface or show interface dampening commands to verify the configuration of
the IP Event Dampening feature.
The clear counters command may be used to clear the flap count and reset it to zero. All other parameters
and status, including dampening states and accumulated penalties, are not affected by this command.
SUMMARY STEPS
1. enable
2. show dampening interface
3. show interface dampening

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
56


IP Event Dampening
Configuration Examples for IP Event Dampening

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

Displays dampened interfaces.

show dampening interface
Example:
Router# show dampening interface

Step 3

Displays dampened interfaces on the local router.

show interface dampening
Example:
Router# show interface dampening

Configuration Examples for IP Event Dampening
Configuring IP Event Dampening Example
The following example configures interface dampening on Gigabit Ethernet interface 0/0/0 and sets the half
life to 30 seconds, the reuse threshold to 1500, the suppress threshold to 10000, and the maximum suppress
time to 120 seconds:
interface GigabitEthernet 0/0/0
dampening 30 1500 10000 120

The following example configures interface dampening on ATM interface 2/0/0 and uses the default interface
dampening values:
interface atm 2/0/0
dampening

The following example configures the router to apply a penalty of 500 on Gigabit Ethernet interface 0/0/0
when the interface comes up for the first time after the router is reloaded:
interface GigabitEthernet 0/0/0
dampening 5 500 1000 20 500

Verifying IP Event Dampening Example
The output of the show dampening interfacecommand displays a summary of interface dampening.
Router# show dampening interface
3 interfaces are configured with dampening.
No interface is being suppressed.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
57


IP Event Dampening
Additional References

Features that are using interface dampening:
IP Routing

The output of the show interface dampening command displays the summary of the dampening parameters
and the status of interfaces on the local router. The following is sample output from the show interface
dampening command.
Router# show interface dampening
GigabitEthernet0/0/0
Flaps Penalty
Supp ReuseTm
0
0
FALSE
0
ATM2/0/0
Flaps Penalty
Supp ReuseTm
0
0
FALSE
0
POS2/0/0
Flaps Penalty
Supp ReuseTm
0
0
FALSE
0

HalfL
5

ReuseV
1000

SuppV
2000

MaxSTm
20

MaxP Restart
16000
0

HalfL
5

ReuseV
1000

SuppV
2000

MaxSTm
20

MaxP Restart
16000
0

HalfL
5

ReuseV
1000

SuppV
2000

MaxSTm
20

MaxP Restart
16000
0

Additional References
The following sections provide references related to the IP Event Dampening feature.
Related Documents
Related Topic

Document Title

IP Routing Protocol-Independent commands Cisco IOS IP Routing: Protocol-Independent Command
Reference
Standards
Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not -been modified by this feature.
MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this To locate and download MIBs for selected platforms, Cisco
feature, and support for existing MIBs has not IOS XE software releases, and feature sets, use Cisco MIB
been modified by this feature.
Locator found at the following URL:
http://www.cisco.com/go/mibs
RFCs
RFC

Title

No new or modified RFCs are supported by this feature, and support for existing standards has not
been modified by this feature.

--

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
58


IP Event Dampening
Feature Information for IP Event Dampening

Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including http://www.cisco.com/techsupport
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.
To receive security and technical information about your products, you
can subscribe to various services, such as the Product Alert Tool (accessed
from Field Notices), the Cisco Technical Services Newsletter, and Really
Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com
user ID and password.

Feature Information for IP Event Dampening
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 5: Feature Information for IP Event Dampening

Feature Name

Releases

Feature Information

IP Event
Dampening

Cisco IOS XE
Release 2.1

The IP Event Dampening feature introduces a configurable exponential
decay mechanism to suppress the effects of excessive interface flapping
events on routing protocols and routing tables in the network. This
feature allows the network operator to configure a router to automatically
identify and selectively dampen a local interface that is flapping.
This feature was introduced on the Cisco ASR 1000 Series Aggregation
Services Routers.
The following commands were introduced by this feature: dampening,
debug dampening, show dampening interface, show interface
dampening.

Glossary
event dampening --The process in which a router dampens a flapping interface from the perspective of the
routing tables and routing protocols of IP by filtering the excessive route adjust message because of the
interface state change.
Flap --Rapid interface state changes from up to down and down to up within a short period of time.
half life --The rate of the exponential decay of the accumulated penalty is determined by this value.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
59


IP Event Dampening
Glossary

maximum penalty --The maximum value beyond which the penalty assigned does not increase. It is derived
from the maximum suppress time.
maximum suppress time --The maximum amount of time the interface can stay suppressed at the time a
penalty is assigned.
penalty --A value assigned to an interface when it flaps. This value increases with each flap and decreases
over time. The rate at which it decreases depends on the half life.
reuse threshold --The threshold value after which the interface will be unsuppressed and can be used again.
suppress threshold --Value of the accumulated penalty that triggers the router to dampen a flapping interface.
When the accumulated penalty exceeds this value, the interface state is considered to be down from the
perspective of the routing protocol.
suppressed --Suppressing an interface removes an interface from the network from the perspective of the
routing protocol. An interface enters the suppressed state when it has flapped frequently enough for the penalty
assigned to it to cross a threshold limit.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
60
