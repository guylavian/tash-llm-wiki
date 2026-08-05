---
title: "BGP Monitoring Protocol"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-monitoring-protocol
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 79 BGP Monitoring Protocol The BGP Monitoring Protocol (BMP) feature supports the following functionality to monitor Border Gateway Protocol (BGP) neighbors, also called BMP clients: • Configure devices to function as BMP servers, and set up parameters on the servers, that are required for monitoring of the BGP neighbors. • Establish connectivity of the BMP servers with BGP neighbors for"
---

# BGP Monitoring Protocol

CHAPTER

79

BGP Monitoring Protocol
The BGP Monitoring Protocol (BMP) feature supports the following functionality to monitor Border Gateway
Protocol (BGP) neighbors, also called BMP clients:
• Configure devices to function as BMP servers, and set up parameters on the servers, that are required
for monitoring of the BGP neighbors.
• Establish connectivity of the BMP servers with BGP neighbors for monitoring.
• Generate statistics report from monitoring the BGP neighbors.
• Perform appropriate error handling on the BGP neighbors.
• Graceful scale up and degradation to the point of closing connectivity between the BMP servers and
BGP neighbors.
• Finding Feature Information, on page 1083
• Prerequisites for BGP Monitoring Protocol, on page 1084
• Information About BGP Monitoring Protocol, on page 1084
• How to Configure BGP Monitoring Protocol, on page 1085
• Verifying BGP Monitoring Protocol, on page 1089
• Monitoring BGP Monitoring Protocol, on page 1090
• Configuration Examples for BGP Monitoring Protocol, on page 1091
• Additional References for BGP Monitoring Protocol, on page 1095
• Feature Information for BGP Monitoring Protocol, on page 1096

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
1083


BGP Monitoring Protocol
Prerequisites for BGP Monitoring Protocol

Prerequisites for BGP Monitoring Protocol
Before you configure BGP Monitoring Protocol (BMP) servers, you must configure Border Gateway Protocol
(BGP) neighbors, which function as BMP clients, and establish a session with its peers using either IPv4/IPv6
or VPNv4/VPNv6 address-family identifiers.

Information About BGP Monitoring Protocol
BGP Monitoring Protocol Overview
The BGP Monitoring Protocol (BMP) feature enables monitoring of BGP neighbors (called BMP clients).
You can configure a device to function as a BMP server, which monitors either one or several BMP clients,
which in turn, has several active peer sessions configured. You can also configure a BMP client to connect
to one or more BMP servers. The BMP feature enables configuration of multiple BMP servers (configured
as primary servers) to function actively and independent of each other, simultaneously to monitor BMP clients.
Each BMP server is specified by a number and you can use command-line interface (CLI) to configure
parameters such as IP address, port number, and so on. Upon activation of a BMP server, it attempts to connect
to BMP clients by sending an initiation message. The CLI enables multiple—independent and
asynchronous—BMP server connections.
BGP neighbors, called BMP clients, are configured to send data to specific BMP servers for monitoring
purposes. These clients are configured in a queue. When a request for a connection arrives from BMP clients
to BMP servers, the connection is established based on the order in which the requests arrived. Once the BMP
server connects with the first BMP neighbor, it sends out refresh requests to monitor the BMP clients and
starts monitoring those BMP clients with whom the connection is already established.
The session connection requests from the other BMP clients in queue to the BMP servers initiates after an
initial delay that you can configure using the initial-delay command. If a connection establishes but fails
later, due to some reason, the connection request is retried after a delay, which you can configure using
failure-retry-delay command. If there is repeated failure in connection establishment, the connection retries
are delayed based on the delay configured using the flapping-delay command. Configuring the delay for such
requests becomes significant because the route refresh requests that are sent to all connected BMP clients
causes considerable network traffic and load on the device.
To avoid excessive load on the device, the BMP servers sends route refresh requests to individual BMP clients
at a time, in the order in which connections are established in the queue. Once a BMP client that is already
connected is in the “reporting” state, it sends a “peer-up” message to the BMP server. After the client receives
a route-refresh request, route monitoring begins for that neighbor. Once the route refresh request ends, the
next neighbor in the queue is processed. This cycle continues until all “reporting” BGP neighbors are reported
and all routes sent by these “reporting” BGP neighbors are continuously monitored. If a neighbor establishes
after BMP monitoring has begun, it does not require a route-refresh request. All received routes from that
client is sent to BMP servers.
It is advantageous to batch up refresh requests from BMP clients, if several BMP servers are activated in
quick succession. Use the bmp initial-refresh delay command to configure a delay in triggering the refresh
mechanism when the first BMP server comes up. If other BMP servers come online within this time-frame,
only one set of refresh requests is sent to the BMP clients. You can also configure the bmp initial-refresh
skip command to skip all refresh requests from BMP servers and just monitor all incoming messages from
the peers.

IP Routing: BGP Configuration Guide
1084


BGP Monitoring Protocol
How to Configure BGP Monitoring Protocol

In a client-server configuration, it is recommended that the resource load of the devices be kept minimal and
adding excessive network traffic must be avoided. In the BMP configuration, you can configure various delay
timers on the BMP server to avoid flapping during connection between the server and client. To avoid excessive
message throughput or high usage of system resources, you can configure the maximum buffer limit for the
BMP session.

How to Configure BGP Monitoring Protocol
Configuring a BGP Monitoring Protocol Session
Perform this task to configure BGP Monitoring Protocol (BMP) session parameters for the BMP servers to
establish connectivity with BMP clients.
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp as-number
bmp {buffer-size buffer-bytes | initial-refresh {delay refresh-delay | skip} | server server-number-n
end

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

Step 3

router bgp as-number
Example:

Enters router configuration mode and creates a BGP routing
process.

Device(config)# router bgp 65000

Step 4

bmp {buffer-size buffer-bytes | initial-refresh {delay
refresh-delay | skip} | server server-number-n

Configures BMP parameters for BGP neighbors and enters
BMP server configuration mode to configure BMP servers.

Example:
Device(config-router)# bmp initial-refresh delay
30

IP Routing: BGP Configuration Guide
1085


BGP Monitoring Protocol
Configuring BGP Monitoring Protocol on BGP Neighbors

Step 5

Command or Action

Purpose

end

Returns to privileged EXEC mode.

Example:
Device(config-router)# end

Configuring BGP Monitoring Protocol on BGP Neighbors
Perform this task to activate BGP Monitoring Protocol (BMP) on BGP neighbors (also called BMP clients)
so that the client activity is monitored by the BMP server configured on the neighbor.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
router bgp as-number
neighbor {ipv4-addr | neighbor-tag | ipv6-addr} bmp-activate {all | server server-number-1 [server
server-number-2 . . . [server server-number-n]]}
• Repeat Steps 1 to 4 to configure other BMP clients in the session.

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

Step 3

router bgp as-number
Example:

Enters router configuration mode and creates a BGP routing
process.

Device(config)# router bgp 65000

Step 4

neighbor {ipv4-addr | neighbor-tag | ipv6-addr}
bmp-activate {all | server server-number-1 [server
server-number-2 . . . [server server-number-n]]}
• Repeat Steps 1 to 4 to configure other BMP clients in
the session.
Example:

IP Routing: BGP Configuration Guide
1086

Activates BMP monitoring on a BGP neighbor.


BGP Monitoring Protocol
Configuring BGP Monitoring Protocol Servers

Command or Action

Purpose

Device(config-router)# neighbor 30.1.1.1
bmp-activate server 1 server 2

Step 5

Returns to privileged EXEC mode.

end
Example:
Device(config-router)# end

Configuring BGP Monitoring Protocol Servers
Perform this task to configure BGP Monitoring Protocol (BMP) servers and its parameters in BMP server
configuration mode.
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
router bgp as-number
bmp {buffer-size buffer-bytes | initial-refresh {delay refresh-delay | skip} | server server-number-n
activate
address {ipv4-addr | ipv6-addr} port-number port-number
description LINE server-description
failure-retry-delay failure-retry-delay
flapping-delay flap-delay
initial-delay initial-delay-time
set ip dscp dscp-value
stats-reporting-period report-period
update-source interface-type interface-number
exit-bmp-server-mode
• Repeat Steps 1 to 14 to configure other BMP servers in the session.

15.

end

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

IP Routing: BGP Configuration Guide
1087


BGP Monitoring Protocol
Configuring BGP Monitoring Protocol Servers

Step 3

Command or Action

Purpose

router bgp as-number

Enters router configuration mode and creates a BGP
routing process.

Example:
Device(config)# router bgp 65000

Step 4

bmp {buffer-size buffer-bytes | initial-refresh {delay
refresh-delay | skip} | server server-number-n

Enters BMP server configuration mode to configure BMP
servers.

Example:
Device(config-router)# bmp server 1

Step 5

activate
Example:

Initiates a connection between BMP server and BGP
neighbors.

Device(config-router-bmpsrvr)# activate

Step 6

address {ipv4-addr | ipv6-addr} port-number
port-number

Configures IP address and port number to a specific BMP
server.

Example:
Device(config-router-bmpsrvr)# address 10.1.1.1
port-number 8000

Step 7

description LINE server-description

Configures a textual description of a BMP server.

Example:
Device(config-router-bmpsrvr)# description LINE
SERVER1

Step 8

failure-retry-delay failure-retry-delay
Example:

Configures delay in the retry requests during failures when
sending BMP server updates.

Device(config-router-bmpsrvr)# failure-retry-delay
40

Step 9

flapping-delay flap-delay
Example:

Configures delays in flapping when sending BMP server
updates.

Device(config-router-bmpsrvr)# flapping-delay 120

Step 10

initial-delay initial-delay-time
Example:

Configures delays in sending initial requests for updates
from the BMP servers.

Device(config-router-bmpsrvr)# initial-delay 20

Step 11

set ip dscp dscp-value
Example:

IP Routing: BGP Configuration Guide
1088

Configures the IP Differentiated Services Code Point
(DSCP) values for BMP servers.


BGP Monitoring Protocol
Verifying BGP Monitoring Protocol

Command or Action

Purpose

Device(config-router-bmpsrvr)# set ip dscp 5

Step 12

stats-reporting-period report-period
Example:

Configures the time interval in which the BMP server
receives the statistics report from BGP neighbors.

Device(config-router-bmpsrvr)#
stats-reporting-period 30

Step 13

update-source interface-type interface-number
Example:

Configures the interface source for routing updates on the
BMP servers.

Device(config-router-bmpsrvr)# update-source
ethernet 0/0

Step 14

exit-bmp-server-mode
• Repeat Steps 1 to 14 to configure other BMP servers
in the session.

Exits from BMP server configuration mode and returns to
router configuration mode.

Example:
Device(config-router-bmpsrvr)#
exit-bmp-server-mode

Step 15

Returns to privileged EXEC mode.

end
Example:
Device(config-router)# end

Verifying BGP Monitoring Protocol
Perform the following steps to verify the configuration for the BGP Monitoring Protocol (BMP) servers and
BMP clients:
SUMMARY STEPS
1. enable
2. show ip bgp bmp
3. show running-config
DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

IP Routing: BGP Configuration Guide
1089


BGP Monitoring Protocol
Monitoring BGP Monitoring Protocol

Step 2

Command or Action

Purpose

show ip bgp bmp

Displays information about BMP servers and neighbors.

Example:
Device# show ip bgp bmp neighbors

Step 3

show running-config

Displays information about BMP servers and neighbors.

Example:
Device# show running-config | section bmp

Monitoring BGP Monitoring Protocol
Perform the following steps to enable debugging and monitor the BGP Monitoring Protocol (BMP) servers.
SUMMARY STEPS
1. enable
2. debug ip bgp bmp
3. show debugging
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

debug ip bgp bmp

Enables debugging of the BMP attributes.

Example:
Device# debug ip bgp bmp server

Step 3

show debugging
Example:
Device# show debugging

IP Routing: BGP Configuration Guide
1090

Displays information about the types of debugging that are
enabled on a device.


BGP Monitoring Protocol
Configuration Examples for BGP Monitoring Protocol

Configuration Examples for BGP Monitoring Protocol
Examples for Configuring, Verifying, and Monitoring BGP Monitoring Protocol
Examples: Configuring BGP Monitoring Protocol

Note

There are two levels of configuration required for the BGP Monitoring Protocol (BMP) to function
as designed. You must enable BMP monitoring on each BGP neighbor (also called BMP client) to
which several peers are connected in a network, and establish connectivity between the BMP servers
and clients. Then, configure each BMP server in BMP server configuration mode for a specific server
with the parameters required for monitoring the associated BMP clients.
The following example shows how to activate BMP on a neighbor with IP address 30.1.1.1, which
is monitored by BMP servers (in this case, server 1 and 2):
Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# neighbor 30.1.1.1 bmp-activate server 1 server 2
Device(config-router)# end

The following example shows how to configure initial refresh delay of 30 seconds for BGP neighbors
on which BMP is activated using the neighbor bmp-activate command:
Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# bmp initial-refresh delay 30
Device(config-router)# bmp buffer-size 2048
Device(config-router)# end

The following example show how to enter BMP server configuration mode and initiate connection
between a specific BMP server with the BGP BMP neighbors. In this example, connection to clients
is initiated from BMP servers 1 and 2 along with configuration of the monitoring parameters:
Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# bmp server 1
Device(config-router-bmpsrvr)# activate
Device(config-router-bmpsrvr)# address 10.1.1.1 port-number 8000
Device(config-router-bmpsrvr)# description LINE SERVER1
Device(config-router-bmpsrvr)# failure-retry-delay 40
Device(config-router-bmpsrvr)# flapping-delay 120
Device(config-router-bmpsrvr)# initial-delay 20
Device(config-router-bmpsrvr)# set ip dscp 5
Device(config-router-bmpsrvr)# stats-reporting-period 30
Device(config-router-bmpsrvr)# update-source ethernet 0/0
Device(config-router-bmpsrvr)# exit-bmp-server-mode
Device(config-router)# bmp server 2

IP Routing: BGP Configuration Guide
1091


BGP Monitoring Protocol
Examples for Configuring, Verifying, and Monitoring BGP Monitoring Protocol

Device(config-router-bmpsrvr)# activate
Device(config-router-bmpsrvr)# address 20.1.1.1 port-number 9000
Device(config-router-bmpsrvr)# description LINE SERVER2
Device(config-router-bmpsrvr)# failure-retry-delay 40
Device(config-router-bmpsrvr)# flapping-delay 120
Device(config-router-bmpsrvr)# initial-delay 20
Device(config-router-bmpsrvr)# set ip dscp 7
Device(config-router-bmpsrvr)# stats-reporting-period 30
Device(config-router-bmpsrvr)# update-source ethernet 2/0
Device(config-router-bmpsrvr)# exit-bmp-server-mode
Device(config-router)# end

Examples: Verifying BGP Monitoring Protocol
The following is sample output from the show ip bgp bmp server command for server number 1.
The attributes displayed are configured in the BMP server configuration mode:
Device# show ip bgp bmp server 1
Print detailed info for 1 server number 1.
bmp server 1
address: 10.1.1.1
port 8000
description SERVER1
up time 00:06:22
session-startup route-refresh
initial-delay 20
failure-retry-delay 40
flapping-delay 120
activated

The following is sample output from the show ip bgp bmp server command for server number 2.
The attributes displayed are configured in the BMP server configuration mode:
Device# show ip bgp bmp server 2
Print detailed info for 1 server number 2.
bmp server 2
address: 20.1.1.1
port 9000
description SERVER2
up time 00:06:23
session-startup route-refresh
initial-delay 20
failure-retry-delay 40
flapping-delay 120
activated

The following is sample output from the show ip bgp bmp server summary command after
deactivating the BMP server 1 and 2 connections:
Device# show ip bgp bmp server summary
Number of BMP servers configured: 2
Number of BMP neighbors configured: 10
Number of neighbors on TransitionQ: 0, MonitoringQ: 0, ConfigQ: 0
Number of BMP servers on StatsQ: 0
BMP Refresh not in progress, refresh not scheduled
Initial Refresh Delay configured, refresh value 30s
BMP buffer size configured, buffer size 2048 MB, buffer size bytes used 0 MB

IP Routing: BGP Configuration Guide
1092


BGP Monitoring Protocol
Examples for Configuring, Verifying, and Monitoring BGP Monitoring Protocol

ID Host/Net
1 10.1.1.1
2 20.1.1.1

Port
8000
9000

TCB
0x0
0x0

Status
Down
Down

Uptime

MsgSent
0
0

LastStat

The following is sample output from the show ip bgp bmp neighbors command, which shows the
status of the BGP BMP neighbors after reactivating the BMP server 1 and 2 connections:
Device# show ip bgp bmp server neighbors
Number of BMP neighbors configured: 10
BMP Refresh not in progress, refresh not scheduled
Initial Refresh Delay configured, refresh value 30s
BMP buffer size configured, buffer size 2048 MB, buffer size bytes used 0 MB
Neighbor
30.1.1.1
2001:DB8::2001
40.1.1.1
2001:DB8::2002
50.1.1.1
60.1.1.1
2001:DB8::2002
70.1.1.1
Neighbor
80.1.1.1
2001:DB8::2002

PriQ
0
0
0
0
0
0
0
0
PriQ
0
0

MsgQ
0
0
0
0
0
0
0
0
MsgQ
0
0

CfgSvr#
1 2
1 2
1 2
1 2
1 2
1 2
1
2
CfgSvr#
1
1 2

ActSvr#
1 2
1 2
1 2
1 2
1 2
1 2
1
2
ActSvr#
1
1 2

RM Sent
16
15
26
15
16
26
9
12
RM Sent
10
16

The following is sample output from the show ip bgp bmp server command for BMP server number
1 and 2. The statistics reporting interval on BMP server 1 and 2 has been set to 30 seconds, therefore
each server receives statistics messages from its connected BGP BMP neighbor in each cycle of 30
seconds:
Device# show ip bgp bmp server summary
Number of BMP servers configured: 2
Number of BMP neighbors configured: 10
Number of neighbors on TransitionQ: 0, MonitoringQ: 0, ConfigQ: 0
Number of BMP servers on StatsQ: 0
BMP Refresh not in progress, refresh not scheduled
Initial Refresh Delay configured, refresh value 30s
BMP buffer size configured, buffer size 2048 MB, buffer size bytes used 0 MB
ID Host/Net
1 10.1.1.1
2 20.1.1.1

Port
8000
9000

TCB
0x2A98B07138
0x2A98E17C88

Status
Up
Up

Uptime
00:38:49
00:38:49

MsgSent
162
46

LastStat
00:00:09
00:00:04

Device# show ip bgp bmp server summary
Number of BMP servers configured: 2
Number of BMP neighbors configured: 10
Number of neighbors on TransitionQ: 0, MonitoringQ: 0, ConfigQ: 0
Number of BMP servers on StatsQ: 0
BMP Refresh not in progress, refresh not scheduled
Initial Refresh Delay configured, refresh value 30s
BMP buffer size configured, buffer size 2048 MB, buffer size bytes used 0 MB
ID Host/Net
1 10.1.1.1
2 20.1.1.1

Port
8000
9000

TCB
0x2A98B07138
0x2A98E17C88

Status
Up
Up

Uptime
00:40:19
00:40:19

MsgSent
189
55

LastStat
00:00:07
00:00:02

IP Routing: BGP Configuration Guide
1093


BGP Monitoring Protocol
Examples for Configuring, Verifying, and Monitoring BGP Monitoring Protocol

Note

If we configure several BGP BMP neighbors to be monitored by the BMP servers, for example 10,
then 10 statistics messages are received by both servers in each periodic cycle that is configured.
The following is sample output from the show running-config command, which shows the running
configuration on the device:
Device# show running-config | section bmp
bmp server 1
address 10.1.1.1 port-number 8000
description SERVER1
initial-delay 20
failure-retry-delay 40
flapping-delay 120
update-source Ethernet0/0
set ip dscp 3
activate
exit-bmp-server-mode
bmp server 2
address 20.1.1.1 port-number 9000
description SERVER2
initial-delay 20
failure-retry-delay 40
flapping-delay 120
update-source Ethernet2/0
set ip dscp 5
activate
exit-bmp-server-mode
bmp initial-refresh delay 30
bmp-activate all

Examples: Monitoring BGP Monitoring Protocol
The following example shows how to enable debugging of the various BMP attributes:
Device# debug ip bgp bmp event
BGP BMP events debugging is on
Device# debug ip bgp bmp neighbor
BGP BMP neighbor debugging is on
Device# debug ip bgp bmp server
BGP BMP server debugging is on

The following is sample output from the show debugging command after you enable the BGP BMP
server debugging:
Device# show debugging
IP routing:
BGP BMP server debugging is on
Device#

IP Routing: BGP Configuration Guide
1094


BGP Monitoring Protocol
Additional References for BGP Monitoring Protocol

*Apr 8 21:04:13.164: BGPBMP: BMP server connection attempt timer expired for server 1 10.1.1.1/8000
*Apr 8 21:04:13.165: BGPBMP: BMP server 1 active open process success - 10.1.1.1/8000
*Apr 8 21:04:13.165: BGPBMP: TCP KA interval is set to 15
Device#
*Apr 8 21:04:15.171: BGPBMP: Register read/write notification callbacks with BMP server 1
TCB - 10.1.1.1/8000
*Apr 8 21:04:15.171: BGPBMP: Initiation msg sent to BMP server 1 - 10.1.1.1/8000
*Apr 8 21:04:15.171: BGPBMP: BMP server 1 connection - 10.1.1.1/8000 up, invoke refresh
event
Device#
*Apr 8 21:04:16.249: BGPBMP: BMP server connection attempt timer expired for server 2 20.1.1.1/9000
*Apr 8 21:04:16.249: BGPBMP: BMP server 2 active open process success - 20.1.1.1/9000
*Apr 8 21:04:16.249: BGPBMP: TCP KA interval is set to 15
*Apr 8 21:04:16.250: BGPBMP: Register read/write notification callbacks with BMP server 2
TCB - 20.1.1.1/9000
*Apr 8 21:04:16.250: BGPBMP: Initiation msg sent to BMP server 2 - 20.1.1.1/9000
*Apr 8 21:04:16.250: BGPBMP: BMP server 2 connection - 20.1.1.1/9000 up, invoke refresh
event

Additional References for BGP Monitoring Protocol
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.

http://www.cisco.com/support

To receive security and technical information about your products, you can
subscribe to various services, such as the Product Alert Tool (accessed from
Field Notices), the Cisco Technical Services Newsletter, and Really Simple
Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com user
ID and password.

IP Routing: BGP Configuration Guide
1095


BGP Monitoring Protocol
Feature Information for BGP Monitoring Protocol

Feature Information for BGP Monitoring Protocol
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
1096


BGP Monitoring Protocol
Feature Information for BGP Monitoring Protocol

Table 99: Feature Information for BGP Monitoring Protocol

Feature Name

Releases

Feature Description

BGP Monitoring Protocol

Cisco IOS XE Release 3.11S

IP Routing: BGP Configuration Guide
1097


BGP Monitoring Protocol
Feature Information for BGP Monitoring Protocol

Feature Name

Releases

Feature Description
The BMP feature supports the
following functionality to enable
monitoring of the Border Gateway
Protocol (BGP) neighbors, which
become BMP clients:
• Configure devices to function
as BMP servers, and set up
parameters on the servers, that
are required for monitoring of
the BGP neighbors.
• Establish connectivity of the
BMP servers with BGP
neighbors for monitoring.
• Generate statistics report from
monitoring the BGP
neighbors.
• Perform appropriate error
handling on the BGP
neighbors.
• Graceful scale up and
degradation to the point of
closing connectivity between
the BMP servers and BGP
neighbors.
The following commands were
introduced or modified:
bmp
debug ip bgp bmp
neighbor bmp-activate
show ip bgp bmp
The following commands were
introduced in BMP server
configuration mode, to configure
specific BMP servers:
activate
address
default
description
exit-bmp-server-mode
failure-retry-delay
flapping-delay

IP Routing: BGP Configuration Guide
1098


BGP Monitoring Protocol
Feature Information for BGP Monitoring Protocol

Feature Name

Releases

Feature Description
initial-delay
set ip dscp
stats-reporting-period
update-source

IP Routing: BGP Configuration Guide
1099


BGP Monitoring Protocol
Feature Information for BGP Monitoring Protocol

IP Routing: BGP Configuration Guide
1100
