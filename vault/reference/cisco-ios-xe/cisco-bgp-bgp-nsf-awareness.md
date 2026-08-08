---
title: "BGP NSF Awareness"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-nsf-awareness
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 26 BGP NSF Awareness Nonstop Forwarding (NSF) awareness allows a router to assist NSF-capable neighbors to continue forwarding packets during a Stateful Switchover (SSO) operation. The BGP Nonstop Forwarding Awareness feature allows an NSF-aware router that is running BGP to forward packets along routes that are already known for a router that is performing an SSO operation. This capabil"
---

# BGP NSF Awareness

CHAPTER

26

BGP NSF Awareness
Nonstop Forwarding (NSF) awareness allows a router to assist NSF-capable neighbors to continue forwarding
packets during a Stateful Switchover (SSO) operation. The BGP Nonstop Forwarding Awareness feature
allows an NSF-aware router that is running BGP to forward packets along routes that are already known for
a router that is performing an SSO operation. This capability allows the BGP peers of the failing router to
retain the routing information that is advertised by the failing router and continue to use this information until
the failed router has returned to normal operating behavior and is able to exchange routing information. The
peering session is maintained throughout the entire NSF operation.
• Finding Feature Information, on page 503
• Information About BGP NSF Awareness, on page 503
• How to Configure BGP NSF Awareness, on page 505
• Configuration Examples for BGP NSF Awareness, on page 511
• Additional References, on page 511
• Feature Information for BGP NSF Awareness, on page 512

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP NSF Awareness
Cisco NSF Routing and Forwarding Operation
Cisco NSF is supported by the BGP, EIGRP, OSPF, and IS-IS protocols for routing and by Cisco Express
Forwarding (CEF) for forwarding. Of the routing protocols, BGP, EIGRP, OSPF, and IS-IS have been enhanced
with NSF capability and awareness, which means that devices running these protocols can detect a switchover
and take the necessary actions to continue forwarding network traffic and to recover route information from
the peer devices.

IP Routing: BGP Configuration Guide
503


BGP NSF Awareness
Cisco Express Forwarding for NSF

In this module, a networking device is said to be NSF-aware if it is running NSF-compatible software. A
device is said to be NSF-capable if it has been configured to support NSF; therefore, it rebuilds routing
information from NSF-aware or NSF-capable neighbors.
Each protocol depends on CEF to continue forwarding packets during switchover while the routing protocols
rebuild the Routing Information Base (RIB) tables. Once the routing protocols have converged, CEF updates
the Forwarding Information Base (FIB) table and removes stale route entries. CEF then updates the line cards
with the new FIB information.

Cisco Express Forwarding for NSF
A key element of NSF is packet forwarding. In a Cisco networking device, packet forwarding is provided by
CEF. CEF maintains the FIB and uses the FIB information that was current at the time of the switchover to
continue forwarding packets during a switchover. This feature reduces traffic interruption during the switchover.
During normal NSF operation, CEF on the active RP synchronizes its current FIB and adjacency databases
with the FIB and adjacency databases on the standby RP. Upon switchover of the active RP, the standby RP
initially has FIB and adjacency databases that are mirror images of those that were current on the active RP.
For platforms with intelligent line cards, the line cards will maintain the current forwarding information over
a switchover; for platforms with forwarding engines, CEF will keep the forwarding engine on the standby RP
current with changes that are sent to it by CEF on the active RP. In this way, the line cards or forwarding
engines will be able to continue forwarding after a switchover as soon as the interfaces and a data path are
available.
As the routing protocols start to repopulate the RIB on a prefix-by-prefix basis, the updates in turn cause
prefix-by-prefix updates for CEF, which it uses to update the FIB and adjacency databases. Existing and new
entries will receive the new version (epoch) number, indicating that they have been refreshed. The forwarding
information is updated on the line cards or forwarding engine during convergence. The RP signals when the
RIB has converged. The software removes all FIB and adjacency entries that have an epoch older than the
current switchover epoch. The FIB now represents the newest routing protocol forwarding information.
The routing protocols run only on the active RP, and they receive routing updates from their neighbor routers.
Routing protocols do not run on the standby RP. After a switchover, the routing protocols request that the
NSF-aware neighbor devices send state information to help rebuild the routing tables.

Note

For NSF operation, the routing protocols depend on CEF to continue forwarding packets while the routing
protocols rebuild the routing information.

BGP Graceful Restart for NSF
When an NSF-capable router begins a BGP session with a BGP peer, it sends an OPEN message to the peer.
Included in the message is a declaration that the NSF-capable or NSF-aware router has graceful restart
capability. Graceful restart is the mechanism by which BGP routing peers avoid a routing flap after a switchover.
If the BGP peer has received this capability, it is aware that the device sending the message is NSF-capable.
Both the NSF-capable router and its BGP peer(s) (NSF-aware peers) need to exchange the graceful restart
capability in their OPEN messages, at the time of session establishment. If both peers do not exchange the
graceful restart capability, the session will not be graceful restart capable.
If the BGP session is lost during the RP switchover, the NSF-aware BGP peer marks all the routes associated
with the NSF-capable router as stale; however, it continues to use these routes to make forwarding decisions

IP Routing: BGP Configuration Guide
504


BGP NSF Awareness
BGP NSF Awareness

for a set period of time. This functionality means that no packets are lost while the newly active RP is waiting
for convergence of the routing information with the BGP peers.
After an RP switchover occurs, the NSF-capable router reestablishes the session with the BGP peer. In
establishing the new session, it sends a new graceful restart message that identifies the NSF-capable router
as having restarted.
At this point, the routing information is exchanged between the two BGP peers. Once this exchange is complete,
the NSF-capable device uses the routing information to update the RIB and the FIB with the new forwarding
information. The NSF-aware device uses the network information to remove stale routes from its BGP table.
Following that, the BGP protocol is fully converged.
If a BGP peer does not support the graceful restart capability, it will ignore the graceful restart capability in
an OPEN message but will establish a BGP session with the NSF-capable device. This functionality will allow
interoperability with non-NSF-aware BGP peers (and without NSF functionality), but the BGP session with
non-NSF-aware BGP peers will not be graceful restart capable.

BGP NSF Awareness
BGP support for NSF requires that neighbor routers are NSF-aware or NSF-capable. NSF awareness in BGP
is also enabled by the graceful restart mechanism. A router that is NSF-aware functions like a router that is
NSF-capable with one exception: an NSF-aware router is incapable of performing an SSO operation. However,
a router that is NSF-aware is capable of maintaining a peering relationship with an NSF-capable neighbor
during an NSF SSO operation, as well as holding routes for this neighbor during the SSO operation.
The BGP Nonstop Forwarding Awareness feature provides an NSF-aware router with the capability to detect
a neighbor that is undergoing an SSO operation, maintain the peering session with this neighbor, retain known
routes, and continue to forward packets for these routes. The deployment of BGP NSF awareness can minimize
the effects of Route Processor (RP) failure conditions and improve the overall network stability by reducing
the amount of resources that are normally required for reestablishing peering with a failed router.
NSF awareness for BGP is not enabled by default. The bgp graceful-restart command is used to globally
enable NSF awareness on a router that is running BGP. NSF-aware operations are also transparent to the
network operator and to BGP peers that do not support NSF capabilities.

Note

NSF awareness is enabled automatically in supported software images for Interior Gateway Protocols, such
as EIGRP, IS-IS, and OSPF. In BGP, global NSF awareness is not enabled automatically and must be started
by issuing the bgp graceful-restart command in router configuration mode.

How to Configure BGP NSF Awareness
Configuring BGP Nonstop Forwarding Awareness Using BGP Graceful Restart
The tasks in this section show how configure BGP Nonstop Forwarding (NSF) awareness using the BGP
graceful restart capability.
• The first task enables BGP NSF globally for all BGP neighbors and suggests a few troubleshooting
options.

IP Routing: BGP Configuration Guide
505


BGP NSF Awareness
Enabling BGP Global NSF Awareness Using BGP Graceful Restart

• The second task describes how to adjust the BGP graceful restart timers, although the default settings
are optimal for most network deployments.
• The next three tasks demonstrate how to enable or disable BGP graceful restart for individual BGP
neighbors, including peer session templates and peer groups.
• The final task verifies the local and peer router configurations of BGP NSF.

Enabling BGP Global NSF Awareness Using BGP Graceful Restart
Perform this task to enable BGP NSF awareness globally for all BGP neighbors. BGP NSF awareness is part
of the graceful restart mechanism and BGP NSF awareness is enabled by issuing the bgp graceful-restart
command in router configuration mode. BGP NSF awareness allows NSF-aware routers to support NSF-capable
routers during an SSO operation. NSF-awareness is not enabled by default and should be configured on all
neighbors that participate in BGP NSF.

Note

The configuration of the restart and stale-path timers is not required to enable the BGP graceful restart
capability. The default values are optimal for most network deployments, and these values should be adjusted
only by an experienced network operator.

Note

Configuring both Bidirectional Forwarding Detection (BFD) and BGP graceful restart for NSF on a device
running BGP may result in suboptimal routing.

SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp autonomous-system-number
bgp graceful-restart [restart-time seconds] [stalepath-time seconds]
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
Example:
Device# configure terminal

IP Routing: BGP Configuration Guide
506

Enters global configuration mode.


BGP NSF Awareness
Troubleshooting Tips

Step 3

Command or Action

Purpose

router bgp autonomous-system-number

Enters router configuration mode and creates a BGP routing
process.

Example:
Device(config)# router bgp 45000

Step 4

bgp graceful-restart [restart-time seconds]
[stalepath-time seconds]
Example:
Device(config-router)# bgp graceful-restart

Enables the BGP graceful restart capability and BGP NSF
awareness.
• If you enter this command after the BGP session has
been established, you must restart the session for the
capability to be exchanged with the BGP neighbor.
• Use this command on the restarting router and all of
its peers (NSF-capable and NSF-aware).

Step 5

Exits router configuration mode and enters privileged EXEC
mode.

end
Example:
Device(config-router)# end

Troubleshooting Tips
To troubleshoot the NSF feature, use the following commands in privileged EXEC mode, as needed:
• debug ip bgp —Displays open messages that advertise the graceful restart capability.
• debug ip bgp event —Displays graceful restart timer events, such as the restart timer and the stalepath
timer.
• debug ip bgp updates —Displays sent and received EOR messages. The EOR message is used by the
NSF-aware router to start the stalepath timer, if configured.
• show ip bgp —Displays entries in the BGP routing table. The output from this command displays routes
that are marked as stale by displaying the letter “S” next to each stale route.
• show ip bgp neighbor —Displays information about the TCP and BGP connections to neighbor devices.
When enabled, the graceful restart capability is displayed in the output of this command.
What to Do Next
If the bgp graceful-restart command has been issued after the BGP session has been established, you must
reset by issuing the clear ip bgp * command or by reloading the router before graceful restart capabilities
will be exchanged. For more information about resetting BGP sessions and using the clear ip bgp command,
see the “Configuring a Basic BGP Network” module.

Configuring BGP NSF Awareness Timers
Perform this task to adjust the BGP graceful restart timers. There are two BGP graceful restart timers that can
be configured. The optional restart-time keyword and seconds argument determine how long peer routers
will wait to delete stale routes before a BGP open message is received. The default value is 120 seconds. The
optional stalepath-time keyword and seconds argument determine how long a router will wait before deleting

IP Routing: BGP Configuration Guide
507


BGP NSF Awareness
Configuring BGP NSF Awareness Timers

stale routes after an end of record (EOR) message is received from the restarting router. The default value is
360 seconds.

Note

The configuration of the restart and stale-path timers is not required to enable the BGP graceful restart
capability. The default values are optimal for most network deployments, and these values should be adjusted
only by an experienced network operator.

SUMMARY STEPS
1.
2.
3.
4.
5.
6.

enable
configure terminal
router bgp autonomous-system-number
bgp graceful-restart [restart-time seconds]
bgp graceful-restart [stalepath-time seconds]
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

router bgp autonomous-system-number
Example:

Enters router configuration mode and creates a BGP routing
process.

Device(config)# router bgp 45000

Step 4

bgp graceful-restart [restart-time seconds]
Example:
Device(config-router)# bgp graceful-restart
restart-time 130

Enables the BGP graceful restart capability and BGP NSF
awareness.
• The restart-time argument determines how long peer
routers will wait to delete stale routes before a BGP
open message is received.
• The default value is 120 seconds. The range is from 1
to 3600 seconds.
Note

IP Routing: BGP Configuration Guide
508

Only the syntax applicable to this step is used in
this example. For more details, see the Cisco IOS
IP Routing: BGP Command Reference.


BGP NSF Awareness
What to Do Next

Step 5

Command or Action

Purpose

bgp graceful-restart [stalepath-time seconds]

Enables the BGP graceful restart capability and BGP NSF
awareness.

Example:
Device(config-router)# bgp graceful-restart
stalepath-time 350

• The stalepath-time argument determines how long a
router will wait before deleting stale routes after an
end of record (EOR) message is received from the
restarting router.
• The default value is 360 seconds. The range is from 1
to 3600 seconds.
Note

Step 6

Only the syntax applicable to this step is used in
this example. For more details, see the Cisco IOS
IP Routing: BGP Command Reference.

Exits router configuration mode and enters privileged EXEC
mode.

end
Example:
Device(config-router)# end

What to Do Next
If the bgp graceful-restart command has been issued after the BGP session has been established, you must
reset the peer sessions by issuing the clear ip bgp * command or by reloading the router before graceful restart
capabilities will be exchanged. For more information about resetting BGP sessions and using the clear ip bgp
command, see the “Configuring a Basic BGP Network” module.

Verifying the Configuration of BGP Nonstop Forwarding Awareness
Use the following steps to verify the local configuration of BGP NSF awareness on a router and to verify the
configuration of NSF awareness on peer routers in a BGP network.
SUMMARY STEPS
1. enable
2. show running-config [options]
3. show ip bgp neighbors [ip-address [received-routes | routes | advertised-routes | paths [regexp] |
dampened-routes | flap-statistics | received prefix-filter | policy [detail]]]
DETAILED STEPS

Step 1

enable
Enables privileged EXEC mode. Enter your password if prompted.
Example:
Router> enable

Step 2

show running-config [options]

IP Routing: BGP Configuration Guide
509


BGP NSF Awareness
Verifying the Configuration of BGP Nonstop Forwarding Awareness

Displays the running configuration on the local router. The output will display the configuration of the bgp graceful-restart
command in the BGP section. Repeat this command on all BGP neighbor routers to verify that all BGP peers are configured
for BGP NSF awareness. In this example, BGP graceful restart is enabled globally and the external neighbor at 192.168.1.2
is configured to be a BGP peer and will have the BGP graceful restart capability enabled.
Example:
Router# show running-config
.
.
.
router bgp 45000
bgp router-id 172.17.1.99
bgp log-neighbor-changes
bgp graceful-restart restart-time 130
bgp graceful-restart stalepath-time 350
bgp graceful-restart
timers bgp 70 120
neighbor 192.168.1.2 remote-as 40000
neighbor 192.168.1.2 activate
.
.
.

Step 3

show ip bgp neighbors [ip-address [received-routes | routes | advertised-routes | paths [regexp] | dampened-routes
| flap-statistics | received prefix-filter | policy [detail]]]
Displays information about TCP and BGP connections to neighbors. “Graceful Restart Capability: advertised” will be
displayed for each neighbor that has exchanged graceful restart capabilities with this router. In Cisco IOS Releases
12.2(33)SRC, 12.2(33)SB, or later releases, the ability to enable or disable the BGP graceful restart capability for an
individual BGP neighbor, peer group or peer session template was introduced and output was added to this command to
show the BGP graceful restart status.
The following partial output example using a Cisco IOS Release 12.2(33)SRC image, displays the graceful restart
information for internal BGP neighbor 172.21.1.2 at Router C in the figure above. Note the “Graceful-Restart is enabled”
message.
Example:
Router# show ip bgp neighbors 172.21.1.2
BGP neighbor is 172.21.1.2, remote AS 45000, internal link
BGP version 4, remote router ID 172.22.1.1
BGP state = Established, up for 00:01:01
Last read 00:00:02, last write 00:00:07, hold time is 180, keepalive intervals
Neighbor sessions:
1 active, is multisession capable
Neighbor capabilities:
Route refresh: advertised and received(new)
Address family IPv4 Unicast: advertised and received
Graceful Restart Capability: advertised
Multisession Capability: advertised and received
!
Address tracking is enabled, the RIB does have a route to 172.21.1.2
Connections established 1; dropped 0
Last reset never
Transport(tcp) path-mtu-discovery is enabled
Graceful-Restart is enabled, restart-time 120 seconds, stalepath-time 360 secs

IP Routing: BGP Configuration Guide
510


BGP NSF Awareness
Configuration Examples for BGP NSF Awareness

Configuration Examples for BGP NSF Awareness
Example: Enabling BGP Global NSF Awareness Using Graceful Restart
The following example enables BGP NSF awareness globally on all BGP neighbors. The restart time is set
to 130 seconds, and the stale path time is set to 350 seconds. The configuration of these timers is optional,
and the preconfigured default values are optimal for most network deployments.
configure terminal
router bgp 45000
bgp graceful-restart
bgp graceful-restart restart-time 130
bgp graceful-restart stalepath-time 350
end

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

MIBs
MIB MIBs Link
None To locate and download MIBs for selected platforms, Cisco software releases, and feature sets, use
Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs
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

IP Routing: BGP Configuration Guide
511


BGP NSF Awareness
Feature Information for BGP NSF Awareness

Feature Information for BGP NSF Awareness
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 42: Feature Information for BGP NSF Awareness

Feature Name

Releases

Feature Information

BGP NSF Awareness

Cisco IOS XE Release 2.1

Nonstop Forwarding (NSF)
awareness allows a device to assist
NSF-capable neighbors to continue
forwarding packets during a
Stateful Switchover (SSO)
operation. The BGP Nonstop
Forwarding Awareness feature
allows an NSF-aware device that is
running BGP to forward packets
along routes that are already known
for a device that is performing an
SSO operation. This capability
allows the BGP peers of the failing
device to retain the routing
information that is advertised by
the failing device and continue to
use this information until the failed
device has returned to normal
operating behavior and is able to
exchange routing information. The
peering session is maintained
throughout the entire NSF
operation.
The following commands were
introduced or modified: bgp
graceful-restart, show ip bgp,
show ip bgp neighbors.

IP Routing: BGP Configuration Guide
512
