---
title: "BGP Restart Neighbor Session After Max-Prefix Limit Reached"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-restart-neighbor-session-after-max-prefix-limit-reached
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 20 BGP Restart Neighbor Session After Max-Prefix Limit Reached The BGP Restart Session After Max-Prefix Limit Reached feature adds the restart keyword to the neighbor maximum-prefix command. This allows a network operator to configure the time interval at which a peering session is reestablished by a device when the number of prefixes that have been received from a peer has exceeded the"
---

# BGP Restart Neighbor Session After Max-Prefix Limit Reached

CHAPTER

20

BGP Restart Neighbor Session After Max-Prefix
Limit Reached
The BGP Restart Session After Max-Prefix Limit Reached feature adds the restart keyword to the neighbor
maximum-prefix command. This allows a network operator to configure the time interval at which a peering
session is reestablished by a device when the number of prefixes that have been received from a peer has
exceeded the maximum prefix limit.
• Finding Feature Information, on page 435
• Information About BGP Neighbor Session Restart After Max-Prefix Limit Reached, on page 435
• How to Configure a Device to Reestablish a Neighbor Session After the Maximum Prefix Limit Has
Been Exceeded, on page 437
• Configuration Example for BGP Restart Neighbor Session After Max-Prefix Limit Reached, on page
441
• Additional References for BGP Restart Neighbor Session After Max-Prefix Limit Reached, on page 441
• Feature Information for BGP Restart Neighbor Session after Max-Prefix Limit, on page 442

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Neighbor Session Restart After
Max-Prefix Limit Reached
Prefix Limits and BGP Peering Sessions
Use the neighbor maximum-prefix command to limit the maximum number of prefixes that a device running
BGP can receive from a peer. When the device receives too many prefixes from a peer and the maximum-prefix

IP Routing: BGP Configuration Guide
435


BGP Restart Neighbor Session After Max-Prefix Limit Reached
BGP Neighbor Session Restart with the Maximum Prefix Limit

limit is exceeded, the peering session is disabled or brought down. The session stays down until the network
operator manually brings the session back up by entering the clear ip bgp command, which clears stored
prefixes.

BGP Neighbor Session Restart with the Maximum Prefix Limit
The restart keyword was added to the neighbor maximum-prefix command so that a network operator can
configure a device to automatically reestablish a BGP neighbor peering session when the peering session has
been disabled or brought down. The time interval at which peering can be reestablished automatically is
configurable. The restart-interval for the restart keyword is specified in minutes; range is from 1 to 65,535
minutes.

Subcodes for BGP Cease Notification
Border Gateway Protocol (BGP) imposes maximum limits on the maximum number of prefixes that are
accepted from a peer for a given address family. This limitation safeguards the device from resource depletion
caused by misconfiguration, either locally or on the remote neighbor. To prevent a peer from flooding BGP
with advertisements, a limit is placed on the number of prefixes that are accepted from a peer for each supported
address family. The default limits can be overridden through configuration of the maximum-prefix limit
command for the peer for the appropriate address family.
The following subcodes are supported for the BGP cease notification message:
• Maximum number of prefixes reached
• Administrative shutdown
• Peer de-configured
• Administrative reset
A cease notification message is sent to the neighbor and the peering with the neighbor is terminated when the
number of prefixes received from the peer for a given address family exceeds the maximum limit (either set
by default or configured by the user) for that address family. It is possible that the maximum number of
prefixes for a neighbor for a given address family has been configured after the peering with the neighbor has
been established and a certain number of prefixes have already been received from the neighbor for that
address family. A cease notification message is sent to the neighbor and peering with the neighbor is terminated
immediately after the configuration if the configured maximum number of prefixes is fewer than the number
of prefixes that have already been received from the neighbor for the address family.

IP Routing: BGP Configuration Guide
436


BGP Restart Neighbor Session After Max-Prefix Limit Reached
How to Configure a Device to Reestablish a Neighbor Session After the Maximum Prefix Limit Has Been Exceeded

How to Configure a Device to Reestablish a Neighbor Session
After the Maximum Prefix Limit Has Been Exceeded
Configuring a Router to Reestablish a Neighbor Session After the Maximum
Prefix Limit Reached
Perform this task to configure the time interval at which a BGP neighbor session is reestablished by a device
when the number of prefixes that have been received from a BGP peer has exceeded the maximum prefix
limit.
The network operator can configure a device running BGP to automatically reestablish a neighbor session
that has been brought down because the configured maximum-prefix limit has been exceeded. No intervention
from the network operator is required when this feature is enabled.

Note

This task attempts to reestablish a disabled BGP neighbor session at the configured time interval that is
specified by the network operator. However, the configuration of the restart timer alone cannot change or
correct a peer that is sending an excessive number of prefixes. The network operator will need to reconfigure
the maximum-prefix limit or reduce the number of prefixes that are sent from the peer. A peer that is configured
to send too many prefixes can cause instability in the network, where an excessive number of prefixes are
rapidly advertised and withdrawn. In this case, the warning-only keyword of the neighbor maximum-prefix
command can be configured to disable the restart capability while the network operator corrects the underlying
problem.

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

enable
configure terminal
router bgp autonomous-system-number
neighbor {ip-address | ipv6-address | peer-group-name} peer-group
neighbor {ip-address | ipv6-address% | peer-group-name} peer-group peer-group-name
neighbor {ip-address | ipv6-address% | peer-group-name} remote-as autonomous-system-number [
alternate-as autonomous-system-number...]
neighbor {ip-address | ipv6-address% | peer-group-name} remote-as autonomous-system-number [
alternate-as autonomous-system-number...]
neighbor {ip-address | ipv6-address% | } maximum-prefix maximum [threshold] [restart minutes]
[warning-only]
end
show ip bgp neighbors ip-address

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

IP Routing: BGP Configuration Guide
437


BGP Restart Neighbor Session After Max-Prefix Limit Reached
Configuring a Router to Reestablish a Neighbor Session After the Maximum Prefix Limit Reached

Command or Action
Example:

Purpose
• Enter your password if prompted.

Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

router bgp autonomous-system-number
Example:

Enters router configuration mode and creates a BGP
routing process.

Device(config)# router bgp 101

Step 4

neighbor {ip-address | ipv6-address | peer-group-name} Creates a BGP or multiprotocol BGP peer group.
peer-group
Example:
Device(config-router)# neighbor internal
peer-group

Step 5

neighbor {ip-address | ipv6-address% | peer-group-name} Configures a BGP neighbor to member of a peer group.
peer-group peer-group-name
• % keyword is the IPv6 link-local address identifier.
This keyword needs to be added whenever a link-local
Example:
IPv6 address is used outside the context of its
Device(config-router)# neighbor 10.4.9.5
interface.
peer-group internal

Step 6

neighbor {ip-address | ipv6-address% | peer-group-name} Adds a peer group to the BGP or multiprotocol BGP
neighbor table.
remote-as autonomous-system-number [ alternate-as
autonomous-system-number...]
Example:
Device(config-router)# neighbor internal remote-as
100

Step 7

neighbor {ip-address | ipv6-address% | peer-group-name} Adds an entry to the BGP or multiprotocol BGP neighbor
table.
remote-as autonomous-system-number [ alternate-as
autonomous-system-number...]
Example:
Device(config-router)# neighbor 10.4.9.5 remote-as
100

Step 8

Configures the maximum-prefix limit on a router that is
neighbor {ip-address | ipv6-address% | }
maximum-prefix maximum [threshold] [restart minutes] running BGP.
[warning-only]
• Use the restart keyword and minutes argument to
configure the router to automatically reestablish a
Example:
neighbor session that has been disabled because the

IP Routing: BGP Configuration Guide
438


BGP Restart Neighbor Session After Max-Prefix Limit Reached
Configuring a Router to Reestablish a Neighbor Session After the Maximum Prefix Limit Reached

Command or Action

Purpose
maximum-prefix limit has been exceeded. The
configurable range of minutes is from 1 to 65535
minutes.

Device(config-router)# neighbor 10.4.9.5
maximum-prefix 1000 90 restart 60

• Use the warning-only keyword to configure the
device to disable the restart capability to allow you
to adjust a peer that is sending too many prefixes.
Note

Step 9

end
Example:

If the minutes argument is not configured, the
disabled session will stay down after the
maximum-prefix limit is exceeded. This is the
default behavior.

Exits router configuration mode and enters privileged
EXEC mode.

Device(config-router)# end

Step 10

show ip bgp neighbors ip-address
Example:
Device# show ip bgp neighbors 10.4.9.5

(Optional) Displays information about the TCP and BGP
connections to neighbors.
• In this example, the output from this command will
display the maximum prefix limit for the specified
neighbor and the configured restart timer value.

Examples
The following sample output from the show ip bgp neighbors command verifies that a device has
been configured to automatically reestablish disabled neighbor sessions. The output shows that the
maximum prefix limit for neighbor 10.4.9.5 is set to 1000 prefixes, the restart threshold is set to 90
percent, and the restart interval is set at 60 minutes.
Device# show ip bgp neighbors 10.4.9.5
BGP neighbor is 10.4.9.5, remote AS 101, internal link
BGP version 4, remote router ID 10.4.9.5
BGP state = Established, up for 2w2d
Last read 00:00:14, hold time is 180, keepalive interval is 60 seconds
Neighbor capabilities:
Route refresh: advertised and received(new)
Address family IPv4 Unicast: advertised and received
Message statistics:
InQ depth is 0
OutQ depth is 0
Sent
Rcvd
Opens:
1
1
Notifications:
0
0
Updates:
0
0
Keepalives:
23095
23095
Route Refresh:
0
0
Total:
23096
23096
Default minimum time between advertisement runs is 5 seconds

IP Routing: BGP Configuration Guide
439


BGP Restart Neighbor Session After Max-Prefix Limit Reached
Troubleshooting Tips

For address family: IPv4 Unicast
BGP table version 1, neighbor versions 1/0 1/0
Output queue sizes : 0 self, 0 replicated
Index 2, Offset 0, Mask 0x4
Member of update-group 2
Sent
Rcvd
Prefix activity:
------Prefixes Current:
0
0
Prefixes Total:
0
0
Implicit Withdraw:
0
0
Explicit Withdraw:
0
0
Used as bestpath:
n/a
0
Used as multipath:
n/a
0
Outbound
Inbound
Local Policy Denied Prefixes:
-------------Total:
0
0
!Configured maximum number of prefixes and restart interval information!
Maximum prefixes allowed 1000
Threshold for warning message 90%, restart interval 60 min
Number of NLRIs in the update sent: max 0, min 0
Connections established 1; dropped 0
Last reset never
Connection state is ESTAB, I/O status: 1, unread input bytes: 0
Local host: 10.4.9.21, Local port: 179
Foreign host: 10.4.9.5, Foreign port: 11871
Enqueued packets for retransmit: 0, input: 0 mis-ordered: 0 (0 bytes)
Event Timers (current time is 0x5296BD2C):
Timer
Starts
Wakeups
Next
Retrans
23098
0
0x0
TimeWait
0
0
0x0
AckHold
23096
22692
0x0
SendWnd
0
0
0x0
KeepAlive
0
0
0x0
GiveUp
0
0
0x0
PmtuAger
0
0
0x0
DeadWait
0
0
0x0
iss: 1900546793 snduna: 1900985663 sndnxt: 1900985663
sndwnd: 14959
irs: 2894590641 rcvnxt: 2895029492 rcvwnd:
14978 delrcvwnd:
1406
SRTT: 300 ms, RTTO: 607 ms, RTV: 3 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 316 ms, ACK hold: 200 ms
Flags: passive open, nagle, gen tcbs
Datagrams (max data segment is 1460 bytes):
Rcvd: 46021 (out of order: 0), with data: 23096, total data bytes: 438850
Sent: 46095 (retransmit: 0, fastretransmit: 0), with data: 23097, total data by9

Troubleshooting Tips
Use the clear ip bgp command to reset a BGP connection using BGP soft reconfiguration. This command
can be used to clear stored prefixes to prevent a device that is running BGP from exceeding the maximum-prefix
limit.
Display of the following error messages can indicate an underlying problem that is causing the neighbor
session to become disabled. You should check the values configured for the neighbor maximum-prefix
command and the configuration of any peers that are sending an excessive number of prefixes. The following
sample error messages are similar to the error messages that may be displayed:
00:01:14:%BGP-5-ADJCHANGE:neighbor 10.10.10.2 Up
00:01:14:%BGP-4-MAXPFX:No. of unicast prefix received from 10.10.10.2 reaches 5, max 6
00:01:14:%BGP-3-MAXPFXEXCEED:No.of unicast prefix received from 10.10.10.2:7 exceed limit6

IP Routing: BGP Configuration Guide
440


BGP Restart Neighbor Session After Max-Prefix Limit Reached
Configuration Example for BGP Restart Neighbor Session After Max-Prefix Limit Reached

00:01:14:%BGP-5-ADJCHANGE:neighbor 10.10.10.2 Down - BGP Notification sent
00:01:14:%BGP-3-NOTIFICATION:sent to neighbor 10.10.10.2 3/1 (update malformed) 0 byte

The bgp dampening command can be used to configure the dampening of a flapping route or interface when
a peer is sending too many prefixes and causing network instability. Use this command only when
troubleshooting or tuning a device that is sending an excessive number of prefixes. For more details about
BGP route dampening, see the “Configuring Advanced BGP Features” module.

Configuration Example for BGP Restart Neighbor Session After
Max-Prefix Limit Reached
Example: Configuring a Router to Reestablish a Neighbor Session After the
Maximum Prefix Limit Reached
The following example sets the maximum number of prefixes allowed from the neighbor at 192.168.6.6 to
2000 and configures the device to reestablish a peering session after 30 minutes if one has been disabled:
Device(config)# router bgp 101
Device(config-router)# neighbor internal peer-group
Device(config-router)# neighbor 10.4.9.5 peer-group internal
Device(config-router)# neighbor internal remote-as 100
Device(config-router)# neighbor 10.4.9.5 remote-as 100
Device(config-router)# neighbor 10.4.9.5 maximum-prefix 2000 90 restart 30
Device(config-router)# end

Additional References for BGP Restart Neighbor Session After
Max-Prefix Limit Reached
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

BGP commands

Cisco IOS IP Routing: BGP
Command Reference

Standards and RFCs
Standard/RFC Title
RFC 2918

Route Refresh Capability for BGP-4

RFC 4486

Subcodes for BGP Cease Notification Message

IP Routing: BGP Configuration Guide
441


BGP Restart Neighbor Session After Max-Prefix Limit Reached
Feature Information for BGP Restart Neighbor Session after Max-Prefix Limit

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

Feature Information for BGP Restart Neighbor Session after
Max-Prefix Limit
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 36: Feature Information for BGP Restart Session After Max-Prefix Limit

Feature Name

Releases

Feature Information

BGP Restart Session After
Max-Prefix Limit

Cisco IOS XE Release 2.1

The BGP Restart Session After
Max-Prefix Limit Reached feature
adds the restart keyword to the
neighbor maximum-prefix
command. This allows a network
operator to configure the time
interval at which a peering session
is reestablished by a device when
the number of prefixes that have
been received from a peer has
exceeded the maximum prefix
limit.
This feature was introduced on the
Cisco ASR 1000 Series
Aggregation Services Routers.
The following commands were
modified: neighbor
maximum-prefix and show ip bgp
neighbors.

BGP—Subcodes for BGP Cease
Notification

IP Routing: BGP Configuration Guide
442

Cisco IOS XE Release 3.13S

Support for subcodes for BGP
cease notification has been added.
