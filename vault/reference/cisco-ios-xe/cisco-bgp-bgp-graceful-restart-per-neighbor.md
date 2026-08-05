---
title: "BGP Graceful Restart per Neighbor"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-graceful-restart-per-neighbor
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 27 BGP Graceful Restart per Neighbor The BGP graceful restart feature is already available on a global basis. The BGP Graceful Restart per Neighbor feature allows BGP graceful restart to be enabled or disable for an individual neighbor, providing greater network flexibility and service. • Finding Feature Information, on page 513 • Information About BGP Graceful Restart per Neighbor, on p"
---

# BGP Graceful Restart per Neighbor

CHAPTER

27

BGP Graceful Restart per Neighbor
The BGP graceful restart feature is already available on a global basis. The BGP Graceful Restart per Neighbor
feature allows BGP graceful restart to be enabled or disable for an individual neighbor, providing greater
network flexibility and service.
• Finding Feature Information, on page 513
• Information About BGP Graceful Restart per Neighbor, on page 513
• How to Configure BGP Graceful Restart per Neighbor, on page 514
• Configuration Examples for BGP Graceful Restart per Neighbor, on page 524
• Additional References, on page 526
• Feature Information for BGP Graceful Restart per Neighbor, on page 527

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Graceful Restart per Neighbor
BGP Graceful Restart per Neighbor
The ability to enable or disable BGP graceful restart for every individual BGP neighbor was introduced. Three
new methods of configuring BGP graceful restart for BGP peers, in addition to the existing global BGP
graceful restart configuration, are now available. Graceful restart can be enabled or disabled for a BGP peer
or a BGP peer group using the neighbor ha-mode graceful-restart command, or a BGP peer can inherit a
graceful restart configuration from a BGP peer-session template using the ha-mode graceful-restart command.
Although BGP graceful restart is disabled by default, the existing global command enables graceful restart
for all BGP neighbors regardless of their capabilities. The ability to enable or disable BGP graceful restart
for individual BGP neighbors provides a greater level of control for a network administrator.

IP Routing: BGP Configuration Guide
513


BGP Graceful Restart per Neighbor
BGP Peer Session Templates

When the BGP graceful restart capability is configured for an individual neighbor, each method of configuring
graceful restart has the same priority, and the last configuration instance is applied to the neighbor. For example,
if global graceful restart is enabled for all BGP neighbors but an individual neighbor is subsequently configured
as a member of a peer group for which the graceful restart is disabled, graceful restart is disabled for that
neighbor.
The configuration of the restart and stale-path timers is available only with the global bgp graceful-restart
command, but the default values are set when the neighbor ha-mode graceful-restart or ha-mode
graceful-restart commands are configured. The default values are optimal for most network deployments,
and these values should be adjusted only by an experienced network operator.

BGP Peer Session Templates
Peer session templates are used to group and apply the configuration of general BGP session commands to
groups of neighbors that share session configuration elements. General session commands that are common
for neighbors that are configured in different address families can be configured within the same peer session
template. Peer session templates are created and configured in peer session configuration mode. Only general
session commands can be configured in a peer session template.
General session commands can be configured once in a peer session template and then applied to many
neighbors through the direct application of a peer session template or through indirect inheritance from a peer
session template. The configuration of peer session templates simplifies the configuration of general session
commands that are commonly applied to all neighbors within an autonomous system.
Peer session templates support direct and indirect inheritance. A BGP neighbor can be configured with only
one peer session template at a time, and that peer session template can contain only one indirectly inherited
peer session template. A BGP neighbor can directly inherit only one session template and can indirectly inherit
up to seven additional peer session templates.
Peer session templates support inheritance. A directly applied peer session template can directly or indirectly
inherit configurations from up to seven peer session templates. So, a total of eight peer session templates can
be applied to a neighbor or neighbor group.
Peer session templates support only general session commands. BGP policy configuration commands that are
configured only for a specific address family or NLRI configuration mode are configured with peer policy
templates.
To use a BGP peer session template to enable or disable BGP graceful restart, see the “Enabling and Disabling
BGP Graceful Restart Using BGP Peer Session Templates” section.

How to Configure BGP Graceful Restart per Neighbor
Enabling BGP Graceful Restart for an Individual BGP Neighbor
Perform this task on Router B in the figure above to enable BGP graceful restart on the internal BGP peer at
Router C in the figure above. Under the IPv4 address family, the neighbor at Router C is identified, and BGP
graceful restart is enabled for the neighbor at Router C with the IP address 172.21.1.2. To verify that BGP
graceful restart is enabled, the optional show ip bgp neighbors command is used.

IP Routing: BGP Configuration Guide
514


BGP Graceful Restart per Neighbor
Enabling BGP Graceful Restart for an Individual BGP Neighbor

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

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 [unicast | multicast | vrf vrf-name]
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address activate
neighbor ip-address ha-mode graceful-restart [disable]
end
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

address-family ipv4 [unicast | multicast | vrf vrf-name]
Example:
Device(config-router)# address-family ipv4 unicast

Specifies the IPv4 address family and enters address family
configuration mode.
• The unicast keyword specifies the IPv4 unicast address
family. By default, the router is placed in address
family configuration mode for the IPv4 unicast address
family if the unicast keyword is not specified.
• The multicast keyword specifies IPv4 multicast
address prefixes.
• The vrf keyword and vrf-name argument specify the
name of the VRF instance to associate with subsequent
IPv4 address family configuration mode commands.

Step 5

neighbor ip-address remote-as
autonomous-system-number
Example:

Configures peering with a BGP neighbor in the specified
autonomous system.
• In this example, the BGP peer at 172.21.1.2 is an
internal BGP peer because it has the same autonomous

IP Routing: BGP Configuration Guide
515


BGP Graceful Restart per Neighbor
Enabling BGP Graceful Restart for an Individual BGP Neighbor

Command or Action
Device(config-router-af)# neighbor 172.21.1.2
remote-as 45000

Step 6

neighbor ip-address activate
Example:
Device(config-router-af)# neighbor 172.21.1.2
activate

Step 7

Purpose
system number as the router where the BGP
configuration is being entered (see Step 3).
Enables the neighbor to exchange prefixes for the IPv4
address family with the local router.
• In this example, the internal BGP peer at 172.21.1.2
is activated.

neighbor ip-address ha-mode graceful-restart [disable] Enables the BGP graceful restart capability for a BGP
neighbor.
Example:
• Use the disable keyword to disable BGP graceful
Device(config-router-af)# neighbor 172.21.1.2
restart capability.
ha-mode graceful-restart

• If you enter this command after the BGP session has
been established, you must restart the session in order
for the capability to be exchanged with the BGP
neighbor.
• In this example, the BGP graceful restart capability is
enabled for the neighbor at 172.21.1.2.
Step 8

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Step 9

(Optional) Displays information about TCP and BGP
show ip bgp neighbors [ip-address [received-routes |
connections to neighbors.
routes | advertised-routes | paths [regexp] |
dampened-routes | flap-statistics | received prefix-filter
• “Graceful Restart Capability: advertised” will be
| policy [detail]]]
displayed for each neighbor that has exchanged
graceful restart capabilities with this router.
Example:
Device# show ip bgp neighbors 172.21.1.2

• In this example, the output is filtered to display
information about the BGP peer at 172.21.1.2.

Examples
The following example shows partial output from the show ip bgp neighbors command for the BGP
peer at 172.21.1.2. Graceful restart is shown as enabled. Note the default values for the restart and
stale-path timers. These timers can be set using only the global bgp graceful-restart command.
Device# show ip bgp neighbors 172.21.1.2
BGP neighbor is 172.21.1.2, remote AS 45000, internal link
BGP version 4, remote router ID 172.22.1.1
BGP state = Established, up for 00:01:01
Last read 00:00:02, last write 00:00:07, hold time is 180, keepalive intervals

IP Routing: BGP Configuration Guide
516


BGP Graceful Restart per Neighbor
Enabling and Disabling BGP Graceful Restart Using BGP Peer Session Templates

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
Connection state is ESTAB, I/O status: 1, unread input bytes: 0

Enabling and Disabling BGP Graceful Restart Using BGP Peer Session
Templates
Perform this task to enable and disable BGP graceful restart for BGP neighbors using peer session templates.
In this task, a BGP peer session template is created, and BGP graceful restart is enabled. A second peer session
template is created, and this template is configured to disable BGP graceful restart.
In this example, the configuration is performed at Router B in the figure below, and two external BGP
neighbors—Router A and Router E—are identified. The first BGP peer at Router A is configured to inherit
the first peer session template, which enables BGP graceful restart, whereas the second BGP peer at Router
E inherits the second template, which disables BGP graceful restart. Using the optional show ip bgp neighbors
command, the status of the BGP graceful restart capability is verified for each BGP neighbor configured in
this task.
Figure 44: Network Topology Showing BGP Neighbors

The restart and stale-path timers can be modified only using the global bgp graceful-restart command. The
restart and stale-path timers are set to the default values when BGP graceful restart is enabled for BGP neighbors
using peer session templates.

IP Routing: BGP Configuration Guide
517


BGP Graceful Restart per Neighbor
Enabling and Disabling BGP Graceful Restart Using BGP Peer Session Templates

Note

A BGP peer cannot inherit from a peer policy or session template and be configured as a peer group member
at the same. BGP templates and BGP peer groups are mutually exclusive.

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

enable
configure terminal
router bgp autonomous-system-number
template peer-session session-template-name
ha-mode graceful-restart [disable]
exit-peer-session
template peer-session session-template-name
ha-mode graceful-restart [disable]
exit-peer-session
bgp log-neighbor-changes
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address inherit peer-session session-template-number
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address inherit peer-session session-template-number
end
show ip bgp template peer-session [session-template-number]
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

Device(config)# router bgp 45000

Step 4

template peer-session session-template-name
Example:

IP Routing: BGP Configuration Guide
518

Enters session-template configuration mode and creates a
peer session template.


BGP Graceful Restart per Neighbor
Enabling and Disabling BGP Graceful Restart Using BGP Peer Session Templates

Command or Action
Device(config-router)# template peer-session S1

Step 5

ha-mode graceful-restart [disable]
Example:
Device(config-router-stmp)# ha-mode
graceful-restart

Purpose
• In this example, a peer session template named S1 is
created.
Enables the BGP graceful restart capability and BGP NSF
awareness.
• Use the disable keyword to disable BGP graceful
restart capability.
• If you enter this command after the BGP session has
been established, you must restart the session in order
for the capability to be exchanged with the BGP
neighbor.
• In this example, the BGP graceful restart capability
is enabled for the peer session template named S1.

Step 6

exit-peer-session
Example:

Exits session-template configuration mode and returns to
router configuration mode.

Device(config-router-stmp)# exit-peer-session

Step 7

template peer-session session-template-name
Example:
Device(config-router)# template peer-session S2

Step 8

ha-mode graceful-restart [disable]
Example:
Device(config-router-stmp)# ha-mode
graceful-restart disable

Enters session-template configuration mode and creates a
peer session template.
• In this example, a peer session template named S2 is
created.
Enables the BGP graceful restart capability and BGP NSF
awareness.
• Use the disable keyword to disable BGP graceful
restart capability.
• If you enter this command after the BGP session has
been established, you must restart the session in order
for the capability to be exchanged with the BGP
neighbor.
• In this example, the BGP graceful restart capability
is disabled for the peer session template named S2.

Step 9

exit-peer-session
Example:

Exits session-template configuration mode and returns to
router configuration mode.

Device(config-router-stmp)# exit-peer-session

Step 10

bgp log-neighbor-changes
Example:
Device(config-router)# bgp log-neighbor-changes

Enables logging of BGP neighbor status changes (up or
down) and neighbor resets.
• Use this command for troubleshooting network
connectivity problems and measuring network

IP Routing: BGP Configuration Guide
519


BGP Graceful Restart per Neighbor
Enabling and Disabling BGP Graceful Restart Using BGP Peer Session Templates

Command or Action

Purpose
stability. Unexpected neighbor resets might indicate
high error rates or high packet loss in the network and
should be investigated.

Step 11

neighbor ip-address remote-as
autonomous-system-number
Example:
Device(config-router)# neighbor 192.168.1.2
remote-as 40000

Step 12

neighbor ip-address inherit peer-session
session-template-number
Example:

Configures peering with a BGP neighbor in the specified
autonomous system.
• In this example, the BGP peer at 192.168.1.2 is an
external BGP peer because it has a different
autonomous system number from the router where
the BGP configuration is being entered (see Step 3).
Inherits a peer session template.
• In this example, the peer session template named S1
is inherited, and the neighbor inherits the enabling of
BGP graceful restart.

Device(config-router)# neighbor 192.168.1.2
inherit peer-session S1

Step 13

neighbor ip-address remote-as
autonomous-system-number
Example:
Device(config-router)# neighbor 192.168.3.2
remote-as 50000

Step 14

neighbor ip-address inherit peer-session
session-template-number
Example:

Configures peering with a BGP neighbor in the specified
autonomous system.
• In this example, the BGP peer at 192.168.3.2 is an
external BGP peer because it has a different
autonomous system number from the router where
the BGP configuration is being entered (see Step 3).
Inherits a peer session-template.
• In this example, the peer session template named S2
is inherited, and the neighbor inherits the disabling
of BGP graceful restart.

Device(config-router)# neighbor 192.168.3.2
inherit peer-session S2

Step 15

end
Example:

Exits router configuration mode and enters privileged
EXEC mode.

Device(config-router)# end

Step 16

show ip bgp template peer-session
[session-template-number]
Example:
Device# show ip bgp template peer-session

Step 17

show ip bgp neighbors [ip-address [received-routes |
routes | advertised-routes | paths [regexp] |

IP Routing: BGP Configuration Guide
520

(Optional) Displays locally configured peer session
templates.
• The output can be filtered to display a single peer
policy template by using the session-template-name
argument. This command also supports all standard
output modifiers.
(Optional) Displays information about TCP and BGP
connections to neighbors.


BGP Graceful Restart per Neighbor
Enabling and Disabling BGP Graceful Restart Using BGP Peer Session Templates

Command or Action
dampened-routes | flap-statistics | received prefix-filter
| policy [detail]]]
Example:
Device# show ip bgp neighbors 192.168.1.2

Purpose
• “Graceful Restart Capability: advertised” will be
displayed for each neighbor that has exchanged
graceful restart capabilities with this router.
• In this example, the output is filtered to display
information about the BGP peer at 192.168.1.2.

Examples
The following example shows partial output from the show ip bgp neighbors command for the BGP
peer at 192.168.1.2 (Router A in the figure above). Graceful restart is shown as enabled. Note the
default values for the restart and stale-path timers. These timers can be set only by using the bgp
graceful-restart command.
Device# show ip bgp neighbors 192.168.1.2
BGP neighbor is 192.168.1.2, remote AS 40000, external link
Inherits from template S1 for session parameters
BGP version 4, remote router ID 192.168.1.2
BGP state = Established, up for 00:02:11
Last read 00:00:23, last write 00:00:27, hold time is 180, keepalive intervals
Neighbor sessions:
1 active, is multisession capable
Neighbor capabilities:
Route refresh: advertised and received(new)
Address family IPv4 Unicast: advertised and received
Graceful Restart Capability: advertised
Multisession Capability: advertised and received
!
Address tracking is enabled, the RIB does have a route to 192.168.1.2
Connections established 1; dropped 0
Last reset never
Transport(tcp) path-mtu-discovery is enabled
Graceful-Restart is enabled, restart-time 120 seconds, stalepath-time 360 secs
Connection state is ESTAB, I/O status: 1, unread input bytes: 0

The following example shows partial output from the show ip bgp neighbors command for the BGP
peer at 192.168.3.2 (Router E in the figure above). Graceful restart is shown as disabled.
Device# show ip bgp neighbors 192.168.3.2
BGP neighbor is 192.168.3.2, remote AS 50000, external link
Inherits from template S2 for session parameters
BGP version 4, remote router ID 192.168.3.2
BGP state = Established, up for 00:01:41
Last read 00:00:45, last write 00:00:45, hold time is 180, keepalive intervals
Neighbor sessions:
1 active, is multisession capable
Neighbor capabilities:
Route refresh: advertised and received(new)
Address family IPv4 Unicast: advertised and received
!
Address tracking is enabled, the RIB does have a route to 192.168.3.2
Connections established 1; dropped 0
Last reset never
Transport(tcp) path-mtu-discovery is enabled

IP Routing: BGP Configuration Guide
521


BGP Graceful Restart per Neighbor
Disabling BGP Graceful Restart for a BGP Peer Group

Graceful-Restart is disabled
Connection state is ESTAB, I/O status: 1, unread input bytes: 0

Disabling BGP Graceful Restart for a BGP Peer Group
Perform this task to disable BGP graceful restart for a BGP peer group. In this task, a BGP peer group is
created and graceful restart is disabled for the peer group. A BGP neighbor, Router D at 172.16.1.2 in the
figure above, is then identified and added as a peer group member. It inherits the configuration associated
with the peer group, which, in this example, disables BGP graceful restart.
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
address-family ipv4 [unicast | multicast | vrf vrf-name]
neighbor peer-group-name peer-group
neighbor peer-group-name remote-as autonomous-system-number
neighbor peer-group-name ha-mode graceful-restart [disable]
neighbor ip-address peer-group peer-group-name
end
show ip bgp neighbors [ip-address [received-routes | routes | advertised-routes | paths [regexp] |
dampened-routes | flap-statistics | received prefix-filter | policy [ detail]]]

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

Enters router configuration mode and creates a BGP
routing process.

Device(config)# router bgp 45000

Step 4

address-family ipv4 [unicast | multicast | vrf vrf-name] Specifies the IPv4 address family and enters address family
configuration mode.
Example:
• The unicast keyword specifies the IPv4 unicast
Device(config-router)# address-family ipv4 unicast
address family. By default, the router is placed in
address family configuration mode for the IPv4

IP Routing: BGP Configuration Guide
522


BGP Graceful Restart per Neighbor
Disabling BGP Graceful Restart for a BGP Peer Group

Command or Action

Purpose
unicast address family if the unicast keyword is not
specified.
• The multicast keyword specifies IPv4 multicast
address prefixes.
• The vrf keyword and vrf-name argument specify the
name of the VRF instance to associate with
subsequent IPv4 address family configuration mode
commands.

Step 5

neighbor peer-group-name peer-group
Example:

Creates a BGP peer group.
• In this example, the peer group named PG1 is created.

Device(config-router-af)# neighbor PG1 peer-group

Step 6

neighbor peer-group-name remote-as
autonomous-system-number
Example:
Device(config-router-af)# neighbor PG1 remote-as
45000

Step 7

Configures peering with a BGP peer group in the specified
autonomous system.
• In this example, the BGP peer group named PG1 is
added to the IPv4 multiprotocol BGP neighbor table
of the local router.

neighbor peer-group-name ha-mode graceful-restart Enables the BGP graceful restart capability for a BGP
neighbor.
[disable]
Example:
Device(config-router-af)# neighbor PG1 ha-mode
graceful-restart disable

• Use the disable keyword to disable BGP graceful
restart capability.
• If you enter this command after the BGP session has
been established, you must restart the session for the
capability to be exchanged with the BGP neighbor.
• In this example, the BGP graceful restart capability
is disabled for the BGP peer group named PG1.

Step 8

neighbor ip-address peer-group peer-group-name
Example:
Device(config-router-af)# neighbor 172.16.1.2
peer-group PG1

Step 9

end
Example:

Assigns the IP address of a BGP neighbor to a peer group.
• In this example, the BGP neighbor peer at 172.16.1.2
is configured as a member of the peer group named
PG1.
Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

Step 10

show ip bgp neighbors [ip-address [received-routes | (Optional) Displays information about TCP and BGP
connections to neighbors.
routes | advertised-routes | paths [regexp] |
dampened-routes | flap-statistics | received prefix-filter
| policy [ detail]]]

IP Routing: BGP Configuration Guide
523


BGP Graceful Restart per Neighbor
Configuration Examples for BGP Graceful Restart per Neighbor

Command or Action
Example:
Device# show ip bgp neighbors 172.16.1.2

Purpose
• In this example, the output is filtered to display
information about the BGP peer at 172.16.1.2 and the
“Graceful-Restart is disabled” line shows that the
graceful restart capability is disabled for this neighbor.

Examples
The following example shows partial output from the show ip bgp neighbors command for the BGP
peer at 172.16.1.2. Graceful restart is shown as disabled. Note the default values for the restart and
stale-path timers. These timers can be set using only the global bgp graceful-restart command.
Device# show ip bgp neighbors 172.16.1.2
BGP neighbor is 172.16.1.2, remote AS 45000, internal link
Member of peer-group PG1 for session parameters
BGP version 4, remote router ID 0.0.0.0
BGP state = Idle
Neighbor sessions:
0 active, is multisession capable
!
Address tracking is enabled, the RIB does have a route to 172.16.1.2
Connections established 0; dropped 0
Last reset never
Transport(tcp) path-mtu-discovery is enabled
Graceful-Restart is disabled

Configuration Examples for BGP Graceful Restart per Neighbor
Examples: Enabling and Disabling BGP Graceful Restart per Neighbor
The ability to enable or disable the BGP graceful restart capability for an individual BGP neighbor, peer group,
or peer session template was introduced. The following example is configured on Router B in the figure below
and enables the BGP graceful restart capability for the BGP peer session template named S1 and disables the
BGP graceful restart capability for the BGP peer session template named S2. The external BGP neighbor at
Router A (192.168.1.2) inherits peer session template S1, and the BGP graceful restart capability is enabled
for this neighbor. Another external BGP neighbor at Router E (192.168.3.2) is configured with the BGP
graceful restart capability disabled after inheriting peer session template S2.

IP Routing: BGP Configuration Guide
524


BGP Graceful Restart per Neighbor
Examples: Enabling and Disabling BGP Graceful Restart per Neighbor

Figure 45: Network Topology Showing BGP Neighbors for BGP Graceful Restart

The BGP graceful restart capability is enabled for an individual internal BGP neighbor, Router C at 172.21.1.2,
whereas the BGP graceful restart is disabled for the BGP neighbor at Router D, 172.16.1.2, because it is a
member of the peer group PG1. The disabling of BGP graceful restart is configured for all members of the
peer group, PG1. The restart and stale-path timers are modified, and the BGP sessions are reset.
router bgp 45000
template peer-session S1
remote-as 40000
ha-mode graceful-restart
exit-peer-session
template peer-session S2
remote-as 50000
ha-mode graceful-restart disable
exit-peer-session
bgp log-neighbor-changes
bgp graceful-restart restart-time 150
bgp graceful-restart stalepath-time 400
address-family ipv4 unicast
neighbor PG1 peer-group
neighbor PG1 remote-as 45000
neighbor PG1 ha-mode graceful-restart disable
neighbor 172.16.1.2 peer-group PG1
neighbor 172.21.1.2 remote-as 45000
neighbor 172.21.1.2 activate
neighbor 172.21.1.2 ha-mode graceful-restart
neighbor 192.168.1.2 remote-as 40000
neighbor 192.168.1.2 inherit peer-session S1
neighbor 192.168.3.2 remote-as 50000
neighbor 192.168.3.2 inherit peer-session S2
end
clear ip bgp *

To demonstrate how the last configuration instance of the BGP graceful restart capability is applied, the
following example initially enables the BGP graceful restart capability globally for all BGP neighbors. A
BGP peer group, PG2, is configured with the BGP graceful restart capability disabled. An individual external
BGP neighbor, Router A at 192.168.1.2 in the figure above, is then configured to be a member of the peer

IP Routing: BGP Configuration Guide
525


BGP Graceful Restart per Neighbor
Additional References

group, PG2. The last graceful restart configuration instance is applied, and, in this case, the neighbor,
192.168.1.2, inherits the configuration instance from the peer group PG2, and the BGP graceful restart
capability is disabled for this neighbor.
router bgp 45000
bgp log-neighbor-changes
bgp graceful-restart
address-family ipv4 unicast
neighbor PG2 peer-group
neighbor PG2 remote-as 40000
neighbor PG2 ha-mode graceful-restart disable
neighbor 192.168.1.2 peer-group PG2
end
clear ip bgp *

Additional References
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
RFC 4724

Graceful Restart Mechanism for BGP

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
526


BGP Graceful Restart per Neighbor
Feature Information for BGP Graceful Restart per Neighbor

Feature Information for BGP Graceful Restart per Neighbor
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 43: Feature Information for BGP Graceful Restart per Neighbor

Feature Name

Releases

BGP Graceful Restart per Neighbor 12.2(33)SRC
12.2(33)SB
Cisco IOS XE 3.8S

Feature Information
The BGP Graceful Restart per
Neighbor feature enables or
disables the BGP graceful restart
capability for an individual BGP
neighbor, including using peer
session templates and BGP peer
groups.
In Cisco IOS Release 12.2(33)SB,
platform support includes the Cisco
10000 series routers.
The following commands were
introduced by this feature: ha-mode
graceful-restart, andneighbor
ha-mode graceful-restart.
The following command was
modified by this feature: show ip
bgp neighbors.

IP Routing: BGP Configuration Guide
527


BGP Graceful Restart per Neighbor
Feature Information for BGP Graceful Restart per Neighbor

IP Routing: BGP Configuration Guide
528
