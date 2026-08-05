---
title: "PBR Support for Multiple Tracking Options"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-pbr-support-for-multiple-tracking-options
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 6 PBR Support for Multiple Tracking Options The PBR Support for Multiple Tracking Options feature extends the capabilities of object tracking using Cisco Discovery Protocol (CDP) to allow the policy-based routing (PBR) process to verify object availability by using additional methods. The verification method can be an Internet Control Message Protocol (ICMP) ping, a User Datagram Protoco"
---

# PBR Support for Multiple Tracking Options

CHAPTER

6

PBR Support for Multiple Tracking Options
The PBR Support for Multiple Tracking Options feature extends the capabilities of object tracking using Cisco
Discovery Protocol (CDP) to allow the policy-based routing (PBR) process to verify object availability by
using additional methods. The verification method can be an Internet Control Message Protocol (ICMP) ping,
a User Datagram Protocol (UDP) ping, or an HTTP GET request.
• Finding Feature Information, on page 69
• Information About PBR Support for Multiple Tracking Options, on page 69
• How to Configure PBR Support for Multiple Tracking Options, on page 70
• Configuration Examples for PBR Support for Multiple Tracking Options, on page 76
• Additional References, on page 78
• Command Reference, on page 78
• Feature Information for PBR Support for Multiple Tracking Options, on page 79

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Information About PBR Support for Multiple Tracking Options
Object Tracking
Object tracking is an independent process that monitors objects such as the following:
• State of the line protocol of an interface
• Existence of an entry in the routing table
• Results of a Service Assurance Agent (SAA) operation, such as a ping

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
69


PBR Support for Multiple Tracking Options
PBR Support for Multiple Tracking Options Feature Design

Clients such as Hot Standby Router Protocol (HSRP), Virtual Router Redundancy Protocol (VRRP), Gateway
Load Balancing Protocol (GLBP), and (with this feature) PBR can register their interest in specific, tracked
objects and then take action when the state of the objects changes.

PBR Support for Multiple Tracking Options Feature Design
The PBR Support for Multiple Tracking Options feature gives PBR access to all the objects that are available
through the tracking process. The tracking process provides the ability to track individual objects--such as
ICMP ping reachability, routing adjacency, an application running on a remote device, a route in the Routing
Information Base (RIB)--or to track the state of an interface line protocol.
Object tracking functions in the following manner. PBR will inform the tracking process that a certain object
should be tracked. The tracking process will in turn notify PBR when the state of that object changes.

How to Configure PBR Support for Multiple Tracking Options
The tasks in this section are divided according to the Cisco IOS release that you are running because Cisco
IOS Release 12.3(14)T introduced new syntax for IP Service Level Agreements (SLAs). To use this feature,
you must be running Cisco IOS Release 12.3(4)T, 12.2(25)S, or a later release. This section contains the
following tasks:

Cisco IOS Release 12.3(11)T 12.2(25)S and Earlier
Perform this task to configure PBR support for multiple tracking options. In this task, a route map is created
and configured to verify the reachability of the tracked object.
Before you begin
This task requires the networking device to be running Cisco IOS Release 12.3(11)T, 12.2(25)S, or prior
releases.
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.

enable
configure terminal
rtr operation-number
type echo protocol protocol-type target [source-ipaddr ip-address]
exit
rtr schedule operation-number [life {forever | seconds}] [start-time {hh : mm[: ss] [month day |
day month] | pending | now | after hh : mm : ss}] [ageout seconds]
track object-number rtr entry-number [reachability]
delay {up seconds [down seconds] | [up seconds] down seconds}
exit
interface type number
ip address ip-address mask [secondary]
ip policy route-map map-tag
exit
route-map map-tag [permit | deny] [sequence-number]

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
70


PBR Support for Multiple Tracking Options
Cisco IOS Release 12.3(11)T 12.2(25)S and Earlier

15.
16.

set ip next-hop verify-availability [next-hop-address sequence track object]
end

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

Enters SAA RTR configuration mode and configures an
SAA operation.

rtr operation-number
Example:
Router(config)# rtr 1

Step 4

type echo protocol protocol-type target [source-ipaddr Configures an SAA end-to-end echo response time probe
operation.
ip-address]
Example:
Router(config-rtr)# type echo protocol ipicmpecho
10.1.1.10

Step 5

Exits SAA RTR configuration mode and returns the router
to global configuration mode.

exit
Example:
Router(config-rtr)# exit

Step 6

rtr schedule operation-number [life {forever | seconds}] Configures the time parameters for the SAA operation.
[start-time {hh : mm[: ss] [month day | day month] |
pending | now | after hh : mm : ss}] [ageout seconds]
Example:
Router(config)# rtr schedule 1 life forever
start-time now

Step 7

track object-number rtr entry-number [reachability] Tracks the reachability of a Response Time Reporter (RTR)
object and enters tracking configuration mode.
Example:
Router(config)# track 123 rtr 1 reachability

Step 8

delay {up seconds [down seconds] | [up seconds] down (Optional) Specifies a period of time (in seconds) to delay
communicating state changes of a tracked object.
seconds}
Example:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
71


PBR Support for Multiple Tracking Options
Cisco IOS Release 12.3(11)T 12.2(25)S and Earlier

Command or Action

Purpose

Router(config-track)# delay up 60 down 30

Step 9

exit
Example:

Exits tracking configuration mode and returns the router
to global configuration mode.

Router(config-track)# exit

Step 10

interface type number
Example:

Specifies an interface type and number and enters interface
configuration mode.

Router(config)# interface ethernet 0

Step 11

ip address ip-address mask [secondary]
Example:
Router(config-if)# ip address 10.1.1.11 255.0.0.0

Step 12

ip policy route-map map-tag
Example:

Specifies a primary or secondary IP address for an
interface.
• See the "Configuring IPv4 Addresses" chapter of the
Cisco IOS IP Addressing Services Configuration
Guide for information on configuring IPv4 addresses.
Enables policy routing and identifies a route map to be
used for policy routing.

Router(config-if)# ip policy route-map alpha

Step 13

exit
Example:

Exits interface configuration mode and returns the router
to global configuration mode.

Router(config-if)# exit

Step 14

route-map map-tag [permit | deny] [sequence-number] Specifies a route map and enters route-map configuration
mode.
Example:
Router(config)# route-map alpha

Step 15

set ip next-hop verify-availability [next-hop-address
sequence track object]

Configures the route map to verify the reachability of the
tracked object.

Example:
Router(config-route-map)# set ip next-hop
verify-availability 10.1.1.1 10 track 123

Step 16

end
Example:

Exits route-map configuration mode and returns the router
to privileged EXEC mode.

Router(config-route-map)# end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
72


PBR Support for Multiple Tracking Options
Configuring PBR Support for Multiple Tracking Options

Configuring PBR Support for Multiple Tracking Options
Perform this task to configure PBR support for multiple tracking options. In this task, a route map is created
and configured to verify the reachability of the tracked object.
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.

enable
configure terminal
ip sla monitor operation-number
type echo protocol ipIcmpEcho {destination-ip-address| destination-hostname}[source-ipaddr
{ip-address| hostname} | source-interface interface-name]
exit
ip sla monitor schedule operation-number [life {forever | seconds}] [start-time {hh : mm[: ss]
[month day | day month] | pending | now | after hh : mm : ss}] [ageout seconds] [recurring]
track object-number rtr entry-number [reachability| state]
delay {up seconds [down seconds] | [up seconds] down seconds}
exit
interface type number
ip address ip-address mask [secondary]
ip policy route-map map-tag
exit
route-map map-tag [permit | deny] [sequence-number] [
set ip next-hop verify-availability [next-hop-address sequence track object]
end
show track object-number
show route-map [map-name| all| dynamic]

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

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

Starts a Cisco IOS IP Service Level Agreement (SLA)
operation configuration and enters IP SLA monitor
configuration mode.

ip sla monitor operation-number
Example:
Device(config)# ip sla monitor 1

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
73


PBR Support for Multiple Tracking Options
Configuring PBR Support for Multiple Tracking Options

Command or Action
Step 4

Purpose

type echo protocol ipIcmpEcho {destination-ip-address| Configures an IP SLA Internet Control Message Protocol
(ICMP) echo probe operation.
destination-hostname}[source-ipaddr {ip-address|
hostname} | source-interface interface-name]
Example:
Device(config-sla-monitor)# type echo protocol
ipIcmpEcho 10.1.1.1

Step 5

exit
Example:

Exits IP SLA monitor configuration mode and returns the
device to global configuration mode.

Device(config-sla-monitor)# exit

Step 6

ip sla monitor schedule operation-number [life {forever Configures the scheduling parameters for a single Cisco
| seconds}] [start-time {hh : mm[: ss] [month day | day IOS IP SLA operation.
month] | pending | now | after hh : mm : ss}] [ageout
• In this example, the time parameters for the IP SLA
seconds] [recurring]
operation are configured.
Example:
Device(config)# ip sla monitor schedule 1 life
forever start-time now

Step 7

track object-number rtr entry-number [reachability| Tracks the reachability of a Response Time Reporter (RTR)
object and enters tracking configuration mode.
state]
Example:
Device(config)# track 123 rtr 1 reachability

Step 8

delay {up seconds [down seconds] | [up seconds] down (Optional) Specifies a period of time, in seconds, to delay
communicating state changes of a tracked object.
seconds}
Example:
Device(config-track)# delay up 60 down 30

Step 9

exit
Example:

Exits tracking configuration mode and returns the device
to global configuration mode.

Device(config-track)# exit

Step 10

interface type number
Example:

Specifies an interface type and number and enters interface
configuration mode.

Device(config)# interface serial 2/0

Step 11

ip address ip-address mask [secondary]
Example:

Specifies a primary or secondary IP address for an
interface.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
74


PBR Support for Multiple Tracking Options
Configuring PBR Support for Multiple Tracking Options

Command or Action

Purpose

Device(config-if)# ip address 192.168.1.1
255.255.255.0

• See the "Configuring IPv4 Addresses" chapter of the
Cisco IOS IP Addressing Services Configuration
Guide for information on configuring IPv4 addresses.
• In this example, the IP address of the incoming
interface is specified. This is the interface on which
policy routing is to be enabled.

Step 12

Enables policy routing and identifies a route map to be
used for policy routing.

ip policy route-map map-tag
Example:
Device(config-if)# ip policy route-map alpha

Step 13

Exits interface configuration mode and returns the device
to global configuration mode.

exit
Example:
Device(config-if)# exit

Step 14

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed.
[
Example:
Device(config)# route-map alpha permit
ordering-seq

Step 15

set ip next-hop verify-availability [next-hop-address
sequence track object]
Example:
Device(config-route-map)# set ip next-hop
verify-availability 10.1.1.1 10 track 123

Step 16

Configures the route map to verify the reachability of the
tracked object.
• In this example, the policy is configured to forward
packets received on serial interface 2/0 to 10.1.1.1 if
that device is reachable.
Exits route-map configuration mode and returns the device
to privileged EXEC mode.

end
Example:
Device(config-route-map)# end

Step 17

(Optional) Displays tracking information.

show track object-number
Example:

• Use this command to verify the configuration. See
the display output in the "Examples" section of this
task.

Device# show track 123

Step 18

show route-map [map-name| all| dynamic]
Example:
Device# show route-map alpha

(Optional) Displays route map information.
• In this example, information about the route map
named alpha is displayed. See the display output in
the "Examples" section of this task.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
75


PBR Support for Multiple Tracking Options
Configuration Examples for PBR Support for Multiple Tracking Options

Examples
The following output from the show track command shows that the tracked object 123 is reachable.
Device# show track 123
Track 123
Response Time Reporter 1 reachability
Reachability is Up
2 changes, last change 00:00:33
Delay up 60 secs, down 30 secs
Latest operation return code: OK
Latest RTT (millisecs) 20
Tracked by:
ROUTE-MAP 0

The following output from the show route-map command shows information about the route map
named alpha that was configured in the task.
Device# show route-map alpha
route-map alpha, permit, sequence 10
Match clauses:
Set clauses:
ip next-hop verify-availability 10.1.1.1 10 track 123
Policy routing matches: 0 packets, 0 bytes

[up]

Configuration Examples for PBR Support for Multiple Tracking
Options
Cisco IOS Release 12.3(11)T 12.2(25)S and Earlier
In the following example, object tracking is configured for PBR on routers that are running Cisco IOS Release
12.3(11)T, 12.2(25)S, or earlier releases.
The configured policy is that packets received on Ethernet interface 0, should be forwarded to 10.1.1.1 only
if that device is reachable (responding to pings). If 10.1.1.1 is not up, then the packets should be forwarded
to 10.2.2.2. If 10.2.2.2 is also not reachable, then the policy routing fails and the packets are routed according
to the routing table.
Two Response Time Reporters (RTRs) are configured to ping the remote devices. The RTRs are then tracked.
Policy routing will monitor the state of the tracked RTRs and make forwarding decisions based on their state.
! Define and start the RTRs.
rtr 1
type echo protocol ipicmpecho 10.1.1.1
rtr schedule 1 start-time now life forever
!
rtr 2
type echo protocol ipicmpecho 10.2.2.2
rtr schedule 2 start-time now life forever
!
! Track the RTRs.
track 123 rtr 1 reachability

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
76


PBR Support for Multiple Tracking Options
Example: Configuring PBR Support for Multiple Tracking Options

track 124 rtr 2 reachability
!
! Enable policy routing on the incoming interface.
interface ethernet 0
ip address 10.4.4.4 255.255.255.0
ip policy route-map beta
!
! 10.1.1.1 is via this interface.
interface ethernet 1
ip address 10.1.1.254 255.255.255.0
!
! 10.2.2.2 is via this interface.
interface ethernet 2
ip address 10.2.2.254 255.255.255.0
!
! Define a route map to set the next-hop depending on the state of the tracked RTRs.
route-map beta
set ip next-hop verify-availability 10.1.1.1 10 track 123
set ip next-hop verify-availability 10.2.2.2 20 track 124

Example: Configuring PBR Support for Multiple Tracking Options
The following example shows how to configure PBR support for multiple tracking options.
The configured policy is that packets received on Ethernet interface 0, should be forwarded to 10.1.1.1 only
if that device is reachable (responding to pings). If 10.1.1.1 is not up, then the packets should be forwarded
to 10.2.2.2. If 10.2.2.2 is also not reachable, then the policy routing fails and the packets are routed according
to the routing table.
Two RTRs are configured to ping the remote devices. The RTRs are then tracked. Policy routing will monitor
the state of the tracked RTRs and make forwarding decisions based on their state.
! Define and start the RTRs.
ip sla monitor 1
type echo protocol ipicmpecho 10.1.1.1
ip sla monitor schedule 1 start-time now life forever
!
ip sla monitor 2
type echo protocol ipicmpecho 10.2.2.2
ip sla monitor schedule 2 start-time now life forever
!
! Track the RTRs.
track 123 rtr 1 reachability
track 124 rtr 2 reachability
!
! Enable policy routing on the incoming interface.
interface ethernet 0
ip address 10.4.4.4 255.255.255.0
ip policy route-map beta
!
! 10.1.1.1 is via this interface.
interface ethernet 1
ip address 10.1.1.254 255.255.255.0
!
! 10.2.2.2 is via this interface.
interface ethernet 2
ip address 10.2.2.254 255.255.255.0
!
! Define a route map to set the next-hop depending on the state of the tracked RTRs.
route-map beta

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
77


PBR Support for Multiple Tracking Options
Additional References

set ip next-hop verify-availability 10.1.1.1 10 track 123
set ip next-hop verify-availability 10.2.2.2 20 track 124

Additional References
The following sections provide references related to the PBR Support for Multiple Tracking Options feature.
Related Documents
Related Topic

Document Title

Object tracking within Cisco IOS
software

Configuring Enhanced Object Tracking" chapter of the Cisco IOS
IP Application Services Configuration Guide

Configuring IP addresses

"Configuring IPv4 Addresses" chapter of the Cisco IOS IP
Addressing Services Configuration Guide

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

Command Reference
The following commands are introduced or modified in the feature or features documented in this module.
For information about these commands, see the Cisco IOS IP Routing: Protocol-Independent Command
Reference. For information about all Cisco IOS commands, use the Command Lookup Tool at
http://tools.cisco.com/Support/CLILookup or the Cisco IOS Master Command List, All Releases , at
http://www.cisco.com/en/US/docs/ios/mcl/allreleasemcl/all_book.html.
• set ip next-hop verify-availability

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
78


PBR Support for Multiple Tracking Options
Feature Information for PBR Support for Multiple Tracking Options

Feature Information for PBR Support for Multiple Tracking
Options
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 7: Feature Information for PBR Support for Multiple Tracking Options

Feature Name
PBR Support for
Multiple Tracking
Options

Releases Feature Information
The PBR Support for Multiple Tracking Options feature extends the
capabilities of object tracking using Cisco Discovery Protocol (CDP) to
allow the policy-based routing (PBR) process to verify object availability
by using additional methods. The verification method can be an Internet
Control Message Protocol (ICMP) ping, a User Datagram Protocol (UDP)
ping, or an HTTP GET request.
The following commands were introduced or modified by this feature:
set ip next-hop verify-availability.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
79


PBR Support for Multiple Tracking Options
Feature Information for PBR Support for Multiple Tracking Options

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
80
