---
title: "BGP PIC Edge for IP and MPLS-VPN"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-pic-edge-for-ip-and-mpls-vpn
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 46 BGP PIC Edge for IP and MPLS-VPN The BGP PIC Edge for IP and MPLS-VPN feature improves BGP convergence after a network failure. This convergence is applicable to both core and edge failures and can be used in both IP and MPLS networks. The BGP PIC Edge for IP and MPLS-VPN feature creates and stores a backup/alternate path in the routing information base (RIB), forwarding information b"
---

# BGP PIC Edge for IP and MPLS-VPN

CHAPTER

46

BGP PIC Edge for IP and MPLS-VPN
The BGP PIC Edge for IP and MPLS-VPN feature improves BGP convergence after a network failure. This
convergence is applicable to both core and edge failures and can be used in both IP and MPLS networks. The
BGP PIC Edge for IP and MPLS-VPN feature creates and stores a backup/alternate path in the routing
information base (RIB), forwarding information base (FIB), and Cisco Express Forwarding so that when a
failure is detected, the backup/alternate path can immediately take over, thus enabling fast failover.

Note

In this document, the BGP PIC Edge for IP and MPLS-VPN feature is called BGP PIC.
• Finding Feature Information, on page 739
• Prerequisites for BGP PIC, on page 739
• Restrictions for BGP PIC, on page 740
• About BGP PIC, on page 740
• How to Configure BGP PIC, on page 749
• Configuration Examples for BGP PIC, on page 752
• Additional References, on page 755
• Feature Information for BGP PIC, on page 757

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for BGP PIC
• Ensure that the Border Gateway Protocol (BGP) and the IP or Multiprotocol Label Switching (MPLS)
network is up and running with the customer site connected to the provider site by more than one path
(multihomed).

IP Routing: BGP Configuration Guide
739


BGP PIC Edge for IP and MPLS-VPN
Restrictions for BGP PIC

• Ensure that the backup/alternate path has a unique next hop that is not the same as the next hop of the
best path.
• Enable the Bidirectional Forwarding Detection (BFD) protocol to quickly detect link failures of directly
connected neighbors.

Restrictions for BGP PIC
The following restrictions apply to the BGP PIC feature:
• With BGP Multipath, the BGP Prefix-Independent Convergence (PIC) feature is already supported.
• In MPLS VPNs, the BGP PIC feature is not supported with MPLS VPN Inter-Autonomous Systems
Option B.
• The BGP PIC feature supports prefixes only for IPv4, IPv6, VPNv4, and VPNv6 address families.
• The BGP PIC feature cannot be configured with Multicast or L2VPN Virtual Routing and Forwarding
(VRF) address families.
• If the route reflector is only in the control plane, then you do not need BGP PIC, because BGP PIC
addresses data plane convergence.
• When two PE devices become each other’s backup/alternate path to a CE device, traffic might loop if
the CE device fails. Neither device will reach the CE device, and traffic will continue to be forwarded
between the PE devices until the time-to-live (TTL) timer expires.
• The BGP PIC feature does not support Nonstop Forwarding with Stateful Switchover (NSF/SSO).
However, ISSU is supported if both Route Processors have the BGP PIC feature configured.
• The BGP PIC feature solves the traffic forwarding only for a single network failure at both the edge and
the core.
• The BGP PIC feature does not work with the BGP Best External feature. If you try to configure the BGP
PIC feature after configuring the BGP Best External feature, you receive an error.

About BGP PIC
In the following sections, we describe the BGP PIC feature in details, how to detect a failure, a scenario and
how to configure it.

Benefits
• An extra path for failover allows faster restoration of connectivity when a primary path is invalid or
withdrawn.
• Reduction of traffic loss.
• Constant convergence time so that the switching time is the same for all prefixes.

IP Routing: BGP Configuration Guide
740


BGP PIC Edge for IP and MPLS-VPN
BGP Convergence

BGP Convergence
Under normal circumstances, BGP can take several seconds to a few minutes to converge after a change in
the network. At a high level, BGP goes through the steps of the following process:
1. BGP learns of failures through either Interior Gateway Protocol (IGP) or BFD events or interface events.
2. BGP withdraws the routes from the routing information base (RIB), and the RIB withdraws the routes
from the forwarding information base (FIB) and distributed FIB (dFIB). This process clears the data path
for the affected prefixes.
3. BGP sends withdrawn messages to its neighbors.
4. BGP calculates the next best path to the affected prefixes.
5. BGP inserts the next best path for affected prefixes into the RIB, and the RIB installs them in the FIB and
dFIB.
This process may take from few seconds to a few minutes to complete. It depends on, the latency of the
network, the convergence time across the network, and the local load on the devices. The data plane converges
only after the control plane converges.

Improve Convergence
The BGP PIC functionality is achieved by an extra functionality in the BGP, RIB, Cisco Express Forwarding,
and MPLS.
• BGP Functionality
BGP PIC affects prefixes under IPv4 and VPNv4 address families. For those prefixes, BGP calculates an
extra second best path, along with the primary best path. (The second best path is called the backup or alternate
path.) BGP installs the best and backup or alternate paths for the affected prefixes into the BGP RIB. The
backup or alternate path provides a fast reroute mechanism to counter a singular network failure. BGP also
includes the alternate or backup path in its application programming interface (API) to the IP RIB.
• RIB Functionality
For BGP PIC, RIB installs an alternate path per route if one is available. If the RIB selects a BGP route
containing a backup or alternate path, it installs the backup or alternate path with the best path. The RIB also
includes the alternate path in its API with the FIB.
• Cisco Express Forwarding Functionality
With BGP PIC, Cisco Express Forwarding stores an alternate path per prefix. When the primary path goes
down, Cisco Express Forwarding searches for the backup or alternate path in a prefix-independent manner.
Cisco Express Forwarding also listens to BFD events to rapidly detect local failures.
• MPLS Functionality
MPLS Forwarding is similar to Cisco Express Forwarding in that it stores alternate paths and switches to an
alternate path if the primary path goes down.
When the BGP PIC feature is enabled, BGP calculates a backup or alternate path per prefix and installs it into
BGP RIB, IP RIB, and FIB. This improves convergence after a network failure. There are two types of network
failures that the BGP PIC feature detects:

IP Routing: BGP Configuration Guide
741


BGP PIC Edge for IP and MPLS-VPN
BGP Fast Reroute

• Core node or link failure (internal Border Gateway Protocol [iBGP] node failure): If a PE node or link
fails, then the failure is detected through IGP convergence. IGP conveys the failure through the RIB to
the FIB.
• Local link or immediate neighbor node failure (external Border Gateway Protocol [eBGP] node or link
failure): To detect a local link failure or eBGP single-hop peer node failure in less than a second, you
must enable BFD. Cisco Express Forwarding looks for BFD events to detect a failure of an eBGP
single-hop peer.
Convergence in the Data Plane
Upon detecting a failure, Cisco Express Forwarding detects the alternate next hop for all prefixes that are
affected by the failure. The data plane convergence is achieved in subseconds depending on whether the BGP
PIC implementation exists in the software or hardware.
Convergence in the Control Plane
Upon detecting a failure, BGP learns about the failure through IGP convergence or BFD events and sends
withdrawn messages for the prefixes, recalculating the best and backup or alternate paths, and advertising the
next best path across the network.

BGP Fast Reroute
BGP Fast Reroute (FRR) provides a best path and a backup or alternate path in BGP, RIB, and Cisco Express
Forwarding. BGP FRR provides a fast reroute mechanism into the RIB and Cisco Express Forwarding (CEF)
on the backup BGP next hop to reach a destination when the current best path is not available.
BGP FRR precomputes a second best path in BGP and gives it to the RIB and Cisco Express Forwarding as
a backup or alternate path, and CEF programs it into line cards.
The BGP PIC feature provides the ability for CEF to quickly switch the traffic to the other egress ports if the
current next hop or the link to this next hop goes down.

IP Routing: BGP Configuration Guide
742


BGP PIC Edge for IP and MPLS-VPN
Detect a Failure

Figure 67: BGP PIC Edge and BGP FRR

Detect a Failure
IGP detects a failure in the iBGP (remote) peer; it may take a few seconds to detect the failure. Convergence
can occur in subseconds or seconds, depending on whether PIC is enabled on the line cards.
If the failure is among the directly connected neighbors (eBGP), and if you use BFD to detect when a neighbor
has gone down. Depending on whether PIC is enabled on the line cards, the detection may happen within
subseconds and the convergence can occur in subseconds or few seconds.

How BGP PIC Can Achieve Subsecond Convergence
The BGP PIC feature works at the Cisco Express Forwarding level, and Cisco Express Forwarding can be
processed in both hardware line cards and in the software.
• For platforms that support Cisco Express Forwarding processing in the line cards, the BGP PIC feature
can converge in subseconds.
• For platforms that do not use Cisco Express Forwarding in hardware line cards, Cisco Express Forwarding
is achieved in the software. The BGP PIC feature works with the Cisco Express Forwarding through the
software and achieves convergence within seconds.

IP Routing: BGP Configuration Guide
743


BGP PIC Edge for IP and MPLS-VPN
How BGP PIC Improves Upon the Functionality of MPLS VPN BGP Local Convergence

How BGP PIC Improves Upon the Functionality of MPLS VPN BGP Local
Convergence
The BGP PIC feature is an enhancement to the "MPLS VPN--BGP Local Convergence" feature, which
provides a failover mechanism that recalculates the best path and installs the new path in forwarding after a
link failure. The feature maintains the local label for 5 minutes to ensure that the traffic uses the backup/alternate
path, thus minimizing traffic loss.
The BGP PIC feature improves the LoC time to under a second by calculating a backup/alternate path in
advance. When a link failure occurs, the traffic is sent to the backup/alternate path.
When you configure the BGP PIC feature, it will override the functionality of the "MPLS VPN--BGP Local
Convergence" feature. You do not have to remove the protection local-prefixes command from the
configuration.

Enable BGP PIC
Because many service provider networks contain many VRFs, the BGP PIC allows you to configure, at a
time, the BGP PIC feature for all VRFs.
• VPNv4 address family configuration mode protects all VRFs.
• VRF-IPv4 address family configuration mode protects only IPv4 VRFs.
• Router configuration mode protects prefixes in the global routing table.

BGP PIC Scenario
You can configure the BGP PIC functionality to achieve fast convergence.

IP PE-CE Link and Node Protection on the CE Side (Dual PEs)
The figure below shows a network that uses the BGP PIC feature. The network includes the following
components:
• eBGP sessions exist between the PE and CE devices.
• Traffic from CE1 uses PE1 to reach network 192.168.9.0/24 through device CE3.
• CE1 has two paths:
• PE1 as the primary path.
• PE2 as the backup/alternate path.
CE1 is configured with the BGP PIC feature. BGP computes PE1 as the best path and PE2 as the
backup/alternate path and installs both routes into the RIB and Cisco Express Forwarding plane. When the
CE1-PE1 link goes down, Cisco Express Forwarding detects the link failure and points the forwarding object
to the backup/alternate path. Traffic is quickly rerouted due to local fast convergence in Cisco Express
Forwarding.

IP Routing: BGP Configuration Guide
744


BGP PIC Edge for IP and MPLS-VPN
IP PE-CE Link and Node Protection on the CE Side (Dual CEs and Dual PE Primary and Backup Nodes)

Figure 68: Using BGP PIC to Protect the PE-CE Link

IP PE-CE Link and Node Protection on the CE Side (Dual CEs and Dual PE Primary and Backup
Nodes)
The figure below shows a network that uses the BGP PIC feature on CE1. The network includes the following
components:
• eBGP sessions exist between the PE and CE devices.
• Traffic from CE1 uses PE1 to reach network 192.168.9.0/24 through device CE3.
• CE1 has two paths:
• PE1 as the primary path.
• PE2 as the backup/alternate path.
• An iBGP session exists between the CE1 and CE2 devices.
In this example, CE1 and CE2 are configured with the BGP PIC feature. BGP computes PE1 as the best path
and PE2 as the backup/alternate path and installs both the routes into the RIB and Cisco Express Forwarding
plane.
There should not be any policies set on CE1 and CE2 for the eBGP peers PE1 and PE2. Both CE devices
must point to the eBGP route as next hop. On CE1, the next hop to reach CE3 is through PE1, so PE1 is the
best path to reach CE3. On CE2, the best path to reach CE3 is PE2. CE2 advertises itself as the next hop to
CE1, and CE1 does the same to CE2. As a result, CE1 has two paths for the specific prefix and it usually
selects the directly connected eBGP path over the iBGP path according to the best path selection rules.
Similarly, CE2 has two paths--an eBGP path through PE2 and an iBGP path through CE1-PE1.
When the CE1-PE1 link goes down, Cisco Express Forwarding detects the link failure and points the forwarding
object to the backup/alternate node CE2. Traffic is quickly rerouted due to local fast convergence in Cisco
Express Forwarding.
If the CE1-PE1 link or PE1 goes down and BGP PIC is enabled on CE1, BGP recomputes the best path,
removing the next hop PE1 from RIB and reinstalling CE2 as the next hop into the RIB and Cisco Express
Forwarding. CE1 automatically gets a backup/alternate repair path into Cisco Express Forwarding and the
traffic loss during forwarding is now in subseconds, thereby achieving fast convergence.

IP Routing: BGP Configuration Guide
745


BGP PIC Edge for IP and MPLS-VPN
IP MPLS PE-CE Link Protection for the Primary or Backup Alternate Path

Figure 69: Using BGP PIC in a Dual CE, Dual PE Network

IP MPLS PE-CE Link Protection for the Primary or Backup Alternate Path
The figure above shows a network that uses the BGP PIC feature on CE1 and CE2. The network includes the
following components:
• eBGP sessions exist between the PE and CE devices.
• The PE devices are VPNv4 iBGP peers with reflect devices in the MPLS network.
• Traffic from CE1 uses PE1 to reach network 192.168.9.0/24 through device CE3.
• CE3 is dual-homed with PE3 and PE4.
• PE1 has two paths to reach CE3 from the reflect routers:
• PE3 is the primary path with the next hop as a PE3 address.
• PE4 is the backup/alternate path with the next hop as a PE4 address.
In this example, all the PE devices can be configured with the BGP PIC feature under IPv4 or VPNv4 address
families.
For BGP PIC to work in BGP for PE-CE link protection, set the policies on PE3 and PE4 for prefixes received
from CE3 so that one of the PE devices acts as the primary and the other as the backup/alternate. Usually,
this is done using local preference and giving better local preference to PE3. In the MPLS cloud, traffic
internally flows through PE3 to reach CE3. Thus, PE1 has PE3 as the best path and PE4 as the second path.
When the PE3-CE3 link goes down, Cisco Express Forwarding detects the link failure, and PE3 recomputes
the best path, selects PE4 as the best path, and sends a withdraw message for the PE3 prefix to the reflect
routers. Some of the traffic goes through PE3-PE4 until BGP installs PE4 as the best path route into the RIB
and Cisco Express Forwarding. PE1 receives the withdraw, recomputes the best path, selects PE4 as the best
path, and installs the routes into the RIB and Cisco Express Forwarding plane.
Thus, with BGP PIC enabled on PE3 and PE4, Cisco Express Forwarding detects the link failure and does
in-place modification of the forwarding object to the backup/alternate node PE4 that already exists in Cisco
Express Forwarding. PE4 knows that the backup/alternate path is locally generated and routes the traffic to
the egress port connected to CE3. This way, traffic loss is minimized and fast convergence is achieved.

IP Routing: BGP Configuration Guide
746


BGP PIC Edge for IP and MPLS-VPN
IP MPLS PE-CE Node Protection for Primary or Backup Alternate Path

IP MPLS PE-CE Node Protection for Primary or Backup Alternate Path
The figure below shows a network that uses the BGP PIC feature on all the PE devices in an MPLS network.
Figure 70: Enabling BGP PIC on all PEs devices in the MPLS Network

The network includes the following components:
• eBGP sessions exist between the PE and CE devices.
• The PE devices are VPNv4 iBGP peers with reflect routers in the MPLS network.
• Traffic from CE1 uses PE1 to reach network 192.168.9.0/24 through device CE3.
• CE3 is dual-homed with PE3 and PE4.
• PE1 has two paths to reach CE3 from the reflect routers:
• PE3 is the primary path with the next hop as a PE3 address.
• PE4 is the backup/alternate path with the next hop as a PE4 address.
In this example, all the PE devices are configured with the BGP PIC feature under IPv4 and VPNv4 address
families.
For BGP PIC to work in BGP for the PE-CE node protection, set the policies on PE3 and PE4 for the prefixes
received from CE3 such that one of the PE devices acts as primary and the other as backup/alternate. Usually,
this is done using local preference and giving better local preference to PE3. In the MPLS cloud, traffic
internally flows through PE3 to reach CE3. So, PE1 has PE3 as the best path and PE4 as the second path.
When PE3 goes down, PE1 knows about the removal of the host prefix by IGPs in subseconds, recomputes
the best path, selects PE4 as the best path, and installs the routes into the RIB and Cisco Express Forwarding
plane. Normal BGP convergence will happen while BGP PIC is redirecting the traffic through PE4, and
packets are not lost.
Thus, with BGP PIC enabled on PE3, Cisco Express Forwarding detects the node failure on PE3 and points
the forwarding object to the backup/alternate node PE4. PE4 knows that the backup/alternate path is locally
generated and routes the traffic to the egress port using the backup/alternate path. This way, traffic loss is
minimized.

IP Routing: BGP Configuration Guide
747


BGP PIC Edge for IP and MPLS-VPN
Cisco Express Forwarding Recursion

No Local Policies Set on the PE Devices
PE1 and PE2 point to the eBGP CE paths as the next hop with no local policy. Each of the PE devices receives
the other’s path, and BGP calculates the backup/alternate path and installs it into Cisco Express Forwarding,
along with its own eBGP path towards CE as the best path. The limitation of the MPLS PE-CE link and node
protection solutions is that you cannot change BGP policies. They should work without the need for a
best-external path.
Local Policies Set on the PE Devices
Whenever there is a local policy on the PE devices to select one of the PE devices as the primary path to reach
the egress CE, the bgp advertise-best-external command is needed on the backup/alternate node PE3 to
propagate the external CE routes with a backup/alternate label into the route reflectors and the far-end PE
devices.

Cisco Express Forwarding Recursion
Recursion is the ability to find the next longest matching path when the primary path goes down.
If BGP PIC is not installed, and if the next hop to a prefix fails, Cisco Express Forwarding finds the next path
to reach the prefix by recursing through the FIB to find the next longest matching path to the prefix. This
recurstion mechanism is useful when the next hop is multiple hops away and there is more than one way of
reaching the next hop.
However, with the BGP PIC feature, you may want to disable Cisco Express Forwarding recursion for the
following reasons:
• Recursion slows down convergence when Cisco Express Forwarding searches all the FIB entries.
• BGP PIC Edge already precomputes an alternate path. It therefore eliminates the need for Cisco Express
Forwarding recursion.
When the BGP PIC functionality is enabled, Cisco Express Forwarding recursion is disabled by default for
two conditions:
• For next hops learned with a /32 network mask (host routes)
• For next hops that are directly connected.
For all other cases, Cisco Express Forwarding recursion is enabled.
You can issue the bgp recursion host command to disable or enable Cisco Express Forwarding recursion for
BGP host routes. This provision is part of the BGP PIC functionality.

Note

When the BGP PIC feature is enabled, by default, bgp recursion host is configured for VPNv4 and VPNv6
address families and disabled for IPv4 and IPv6 address families.
To disable or enable Cisco Express Forwarding recursion for BGP directly connected next hops, run the
disable-connected-check command.

IP Routing: BGP Configuration Guide
748


BGP PIC Edge for IP and MPLS-VPN
How to Configure BGP PIC

How to Configure BGP PIC
Configuring BGP PIC
Because many service provider networks contain many VRFs, the BGP PIC feature allows you to configure
the BGP PIC feature for all VRFs at once.
• VPNv4 address family configuration mode protects all the VRFs.
• VRF-IPv4 address family configuration mode protects only IPv4 VRFs.
• Router configuration mode protects prefixes in the global routing table.
For a full configuration example that includes configuring multiprotocol VRFs and shows output to verify
that the feature is enabled, see the Example: Configuring BGP PIC, on page 752.
Before you begin
• If you are implementing the BGP PIC feature in an MPLS VPN, ensure that the network is working
properly before configuring the BGP PIC feature. See “Configuring MPLS Layer 3 VPNs” for more
information.
• If you are implementing the BGP PIC feature in an MPLS VPN, configure multiprotocol VRFs, which
allow you to share route-target policies (import and export) between IPv4 and IPv6 or to configure
separate route-target policies for IPv4 and IPv6 VPNs. For information about configuring multiprotocol
VRFs, see “MPLS VPN—VRF CLI for IPv4 and IPv6 VPNs”.
• Ensure that the CE device is connected to the network by at least two paths.
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
router bgp autonomous-system-number
Do one of the following:
• address-family ipv4 [unicast | vrf vrf-name]
• address-family vpnv4 [unicast]

5.
6.
7.
8.
9.
10.

bgp additional-paths install
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address activate
bgp recursion host
neighbor ip-address fall-over [bfd |route-map map-name]
end

IP Routing: BGP Configuration Guide
749


BGP PIC Edge for IP and MPLS-VPN
Configuring BGP PIC

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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 40000

Step 4

Do one of the following:
• address-family ipv4 [unicast | vrf vrf-name]
• address-family vpnv4 [unicast]
Example:
Device(config-router)# address-family ipv4 unicast

Example:

Specifies the IPv4 or VPNv4 address family and enters
address family configuration mode.
• The unicast keyword specifies the IPv4 or VPNv4
unicast address family.
• The vrf keyword and vrf-name argument specify the
name of the virtual routing and forwarding (VRF)
instance to associate with subsequent IPv4 address
family configuration mode commands.

Device(config-router)# address-family vpnv4

Step 5

bgp additional-paths install
Example:

Calculates a backup/alternate path and installs it into the
RIB and Cisco Express Forwarding.

Device(config-router-af)# bgp additional-paths
install

Step 6

neighbor ip-address remote-as
autonomous-system-number
Example:
Device(config-router-af)# neighbor 192.168.1.1
remote-as 45000

Step 7

neighbor ip-address activate
Example:

IP Routing: BGP Configuration Guide
750

Adds the IP address of the neighbor in the specified
autonomous system to the IPv4 multiprotocol BGP
neighbor table of the local router.
• By default, neighbors that are defined using the
neighbor remote-as command in router configuration
mode exchange only IPv4 unicast address prefixes.
To exchange other address prefix types, neighbors
must also be activated using the neighbor activate
command in address family configuration mode for
the other prefix types.
Enables the neighbor to exchange prefixes for the IPv4
unicast address family with the local router.


BGP PIC Edge for IP and MPLS-VPN
Disabling BGP PIC Core

Command or Action

Purpose

Device(config-router-af)# neighbor 192.168.1.1
activate

Step 8

bgp recursion host
Example:
Device(config-router-af)# bgp recursion host

Step 9

neighbor ip-address fall-over [bfd |route-map
map-name]

(Optional) Enables the recursive-via-host flag for IPv4,
VPNv4, and VRF address families.
• When the BGP PIC feature is enabled, Cisco Express
Forwarding recursion is disabled. Under most
circumstances, you do not want to enable recursion
when BGP PIC is enabled.
Enables BFD protocol support to detect when a neighbor
has gone away, which can occur within a subsecond.

Example:
Device(config-router-af)# neighbor 192.168.1.1
fall-over bfd

Step 10

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Disabling BGP PIC Core
BGP PIC core feature is enabled by default. Use the following configuration to disable the BGP PIC core
feature.

Note

Use the cef table output-chain build favor convergence-speed command in global configuration mode to
re-enable the BGP PIC core feature.

SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
cef table output-chain build favor memory-utilization
end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

IP Routing: BGP Configuration Guide
751


BGP PIC Edge for IP and MPLS-VPN
Configuration Examples for BGP PIC

Command or Action

Purpose

Device> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

cef table output-chain build favor memory-utilization
Example:

Configures memory characteristics for Cisco Express
Forwarding table output chain building for the forwarding
of packets through the network.

Device(config)# cef table output-chain build favor
memory-utilization

Step 4

Exits global configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config)# end

Configuration Examples for BGP PIC
Example: Configuring BGP PIC
The following example shows how to configure the BGP PIC feature in VPNv4 address family configuration
mode, which enables the feature on all VRFs. In the following example, there are two VRFs defined: blue
and green. All the VRFs, including those in VRFs blue and green, are protected by backup/alternate paths.
vrf definition test1
rd 400:1
route-target export 100:1
route-target export 200:1
route-target export 300:1
route-target export 400:1
route-target import 100:1
route-target import 200:1
route-target import 300:1
route-target import 400:1
address-family ipv4
exit-address-family
exit
!
vrf forwarding test1
ip address 10.0.0.1 255.0.0.0
exit
router bgp 3
no synchronization
bgp log-neighbor-changes
redistribute static
redistribute connected
neighbor 10.6.6.6 remote-as 3

IP Routing: BGP Configuration Guide
752


BGP PIC Edge for IP and MPLS-VPN
Example: Displaying Backup Alternate Paths for BGP PIC

neighbor 10.6.6.6 update-source Loopback0
neighbor 10.7.7.7 remote-as 3
neighbor 10.7.7.7 update-source Loopback0
no auto-summary
!
address-family vpnv4
bgp additional-paths install
neighbor 10.6.6.6 activate
neighbor 10.6.6.6 send-community both
neighbor 10.7.7.7 activate
neighbor 10.7.7.7 send-community both
exit-address-family
!
address-family ipv4 vrf blue
import path selection all
import path limit 10
no synchronization
neighbor 10.11.11.11 remote-as 1
neighbor 10.11.11.11 activate
exit-address-family
!
address-family ipv4 vrf green
import path selection all
import path limit 10
no synchronization
neighbor 10.13.13.13 remote-as 1
neighbor 10.13.13.13 activate
exit-address-family

The following show vrf detail command output shows that the BGP PIC feature is enabled:
Router# show vrf detail
VRF test1 (VRF Id = 1); default RD 400:1; default VPNID <not set>
Interfaces:
Se4/0
Address family ipv4 (Table ID = 1 (0x1)):
Export VPN route-target communities
RT:100:1
RT:200:1
RT:300:1
RT:400:1
Import VPN route-target communities
RT:100:1
RT:200:1
RT:300:1
RT:400:1
No import route-map
No export route-map
VRF label distribution protocol: not configured
VRF label allocation mode: per-prefix
Prefix protection with additional path enabled
Address family ipv6 not active.

Example: Displaying Backup Alternate Paths for BGP PIC
The command output in the following example shows that the VRFs in VRF blue have backup/alternate paths:
Device# show ip bgp vpnv4 vrf blue 10.0.0.0
BGP routing table entry for 10:12:12.0.0.0/24, version 88
Paths: (4 available, best #1, table blue)
Additional-path
Advertised to update-groups:
6
1, imported path from 12:23:12.0.0.0/24

IP Routing: BGP Configuration Guide
753


BGP PIC Edge for IP and MPLS-VPN
Example: Displaying Backup Alternate Paths for BGP PIC

10.3.3.3 (metric 21) from 10.6.6.6 (10.6.6.6)
Origin incomplete, metric 0, localpref 200, valid, internal, best
Extended Community: RT:12:23
Originator: 10.3.3.3, Cluster list: 10.0.0.1 , recursive-via-host
mpls labels in/out nolabel/37
1, imported path from 12:23:12.0.0.0/24
10.13.13.13 (via green) from 10.13.13.13 (10.0.0.2)
Origin incomplete, metric 0, localpref 100, valid, external
Extended Community: RT:12:23 , recursive-via-connected
1, imported path from 12:23:12.0.0.0/24
10.3.3.3 (metric 21) from 10.7.7.7 (10.7.7.7)
Origin incomplete, metric 0, localpref 200, valid, internal
Extended Community: RT:12:23
Originator: 10.3.3.3, Cluster list: 10.0.0.1 , recursive-via-host
mpls labels in/out nolabel/37
1
10.11.11.11 from 10.11.11.11 (1.0.0.1)
Origin incomplete, metric 0, localpref 100, valid, external, backup/repair
Extended Community: RT:11:12 , recursive-via-connected

The command output in the following example shows that the VRFs in VRF green have backup/alternate
paths:
Device# show ip bgp vpnv4 vrf green 12.0.0.0
BGP routing table entry for 12:23:12.0.0.0/24, version 87
Paths: (4 available, best #4, table green)
Additional-path
Advertised to update-groups:
5
1, imported path from 11:12:12.0.0.0/24
10.11.11.11 (via blue) from 10.11.11.11 (1.0.0.1)
Origin incomplete, metric 0, localpref 100, valid, external
Extended Community: RT:11:12 , recursive-via-connected
1
10.3.3.3 (metric 21) from 10.7.7.7 (10.7.7.7)
Origin incomplete, metric 0, localpref 200, valid, internal
Extended Community: RT:12:23
Originator: 10.3.3.3, Cluster list: 10.0.0.1 , recursive-via-host
mpls labels in/out nolabel/37
1
10.13.13.13 from 10.13.13.13 (10.0.0.2)
Origin incomplete, metric 0, localpref 100, valid, external, backup/repair
Extended Community: RT:12:23 , recursive-via-connected
1
10.3.3.3 (metric 21) from 10.6.6.6 (10.6.6.6)
Origin incomplete, metric 0, localpref 200, valid, internal, best
Extended Community: RT:12:23
Originator: 10.3.3.3, Cluster list: 10.0.0.1 , recursive-via-host
mpls labels in/out nolabel/37

The command output in the following example shows the BGP routing table entries for the backup and alternate
paths:
Device# show ip bgp 10.0.0.0 255.255.0.0
BGP routing table entry for 10.0.0.0/16, version 123
Paths: (4 available, best #3, table default)
Additional-path
Advertised to update-groups:
2
3
Local
10.0.101.4 from 10.0.101.4 (10.3.3.3)

IP Routing: BGP Configuration Guide
754


BGP PIC Edge for IP and MPLS-VPN
Example: Disabling BGP PIC Core

Origin IGP, localpref 100, weight 500, valid, internal
Local
10.0.101.3 from 10.0.101.3 (10.4.4.4)
Origin IGP, localpref 100, weight 200, valid, internal
Local
10.0.101.2 from 10.0.101.2 (10.1.1.1)
Origin IGP, localpref 100, weight 900, valid, internal, best
Local
10.0.101.1 from 10.0.101.1 (10.5.5.5)
Origin IGP, localpref 100, weight 700, valid, internal, backup/repair

The command output in the following example shows the routing information base entries for the backup and
alternate paths:
Device# show ip route repair-paths 10.0.0.0 255.255.0.0
Routing entry for 10.0.0.0/16
Known via "bgp 10", distance 200, metric 0, type internal
Last update from 10.0.101.2 00:00:56 ago
Routing Descriptor Blocks:
* 10.0.101.2, from 10.0.101.2, 00:00:56 ago
Route metric is 0, traffic share count is 1
AS Hops 0
MPLS label: none
[RPR]10.0.101.1, from 10.0.101.1, 00:00:56 ago
Route metric is 0, traffic share count is 1
AS Hops 0
MPLS label: none

The command output in the following example shows the Cisco Express Forwarding/forwarding information
base entries for the backup and alternate paths:
Device# show ip cef 10.0.0.0 255.255.0.0 detail
10.0.0.0/16, epoch 0, flags rib only nolabel, rib defined all labels
recursive via 10.0.101.2
attached to
recursive via 10.0.101.1, repair
attached to

Example: Disabling BGP PIC Core
The following example shows how to disable the BGP PIC core in global configuration mode.
Device> enable
Device# configure terminal
Device(config)# cef table output-chain build favor memory-utilization
Device(config)# end

Additional References
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

IP Routing: BGP Configuration Guide
755


BGP PIC Edge for IP and MPLS-VPN
Additional References

Related Topic

Document Title

BGP commands

Cisco IOS IP Routing: BGP Command Reference

Basic MPLS VPNs

“Configuring MPLS Layer 3 VPNs” module in the MPLS: Layer
3 VPNs Configuration Guide

A failover feature that creates a new path “MPLS VPN—BGP Local Convergence” module in the MPLS:
after a link or node failure
Layer 3 VPNs Configuration Guide
Configuring multiprotocol VRFs

“MPLS VPN—VRF CLI for IPv4 and IPv6 VPNs” module in
the MPLS: Layer 3 VPNs Configuration Guide

Related Documents
Standards
Standard

Title

draft-walton-bgp-add-paths-04.txt Advertisement of Multiple Paths in BGP
MIBs
MIB MIBs Link
—

To locate and download MIBs for selected platforms, Cisco software releases, and feature sets, use
Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

RFC 1771 A Border Gateway Protocol 4 (BGP-4)
RFC 2547 BGP/MPLS VPNs
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
756


BGP PIC Edge for IP and MPLS-VPN
Feature Information for BGP PIC

Feature Information for BGP PIC
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 62: Feature Information for BGP PIC

Feature Name

Releases

Feature Information

BGP PIC Edge
for IP and
MPLS-VPN

Cisco IOS XE
Release 3.2S

The BGP PIC Edge for IP and MPLS-VPN feature improves BGP
convergence after a network failure. This convergence is applicable
to both core and edge failures and can be used in both IP and MPLS
networks. The BGP PIC Edge for IP and MPLS-VPN feature creates
and stores a backup/alternate path in the routing information base
(RIB), forwarding information base (FIB), and Cisco Express
Forwarding so that when a failure is detected, the backup/alternate
path can immediately take over, thus enabling fast failover.

Cisco IOS XE
Release 3.7S

In Cisco IOS XE Release 3.2S, this feature was introduced.
The following commands were introduced or modified: bgp
additional-paths install, bgp recursion host, show ip bgp, show
ip cef, show ip route, show vrf.

IP Routing: BGP Configuration Guide
757


BGP PIC Edge for IP and MPLS-VPN
Feature Information for BGP PIC

IP Routing: BGP Configuration Guide
758
