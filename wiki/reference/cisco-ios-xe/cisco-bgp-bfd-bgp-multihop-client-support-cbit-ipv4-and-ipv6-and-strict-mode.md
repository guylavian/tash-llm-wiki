---
title: "BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bfd-bgp-multihop-client-support-cbit-ipv4-and-ipv6-and-strict-mode
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 62 BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode The BFD—BGP Multihop Client Support feature enables Border Gateway Protocol (BGP) to use multihop Bidirectional Forwarding Detection (BFD) support, which improves BGP convergence as BFD detection and failure times are faster than the Interior Gateway Protocol (IGP) convergence times in most network topologies. The"
---

# BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode

CHAPTER

62

BFD—BGP Multihop Client Support, cBit (IPv4
and IPv6), and Strict Mode
The BFD—BGP Multihop Client Support feature enables Border Gateway Protocol (BGP) to use multihop
Bidirectional Forwarding Detection (BFD) support, which improves BGP convergence as BFD detection and
failure times are faster than the Interior Gateway Protocol (IGP) convergence times in most network topologies.
The BFD—BGP cBIT feature allows BGP to determine if BFD failure is dependent or independent of the
Control Plane. This allows BGP greater flexibility in handling BFD down events.
• Finding Feature Information, on page 935
• Restrictions for BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode, on page
936
• Information About BFD - BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode, on page
936
• How to Configure BFD - BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode, on page
937
• Configuration Examples for BFD - BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode,
on page 939
• Additional References, on page 941
• Feature Information for BFD—BGP Multihop Client Support, cBit (IPv4/IPv6), and Strict Mode, on
page 941

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
935


BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
Restrictions for BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode

Restrictions for BFD—BGP Multihop Client Support, cBit (IPv4
and IPv6), and Strict Mode
• For BGP IPv4 and BGP IPv6 peering sessions only, multihop BFD support is available for BGP for
address-family IPv4 and IPv6 unicast.
• For multihop BGP sessions using IPv6 Link Local addresses, BFD multihop support is not available.
• Currently BFD Hardware offload is not supported for multihop BFD sessions and so C-bit will not be
set for multihop sessions.
• Multihop BFD for IPv6 Virtual Routing and Forwarding (VRF) is not supported.
• BGP session attribute for BFD does not change dynamically when BGP session changes from single-hop
to multihop, hence you need to clear the existing BGP session to reinitiate multihop BFD session.

Information About BFD - BGP Multihop Client Support, cBit (IPv4
and IPv6), and Strict Mode
BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
BFD is a detection protocol that is designed to provide fast forwarding path failure detection times for all
media types, encapsulations, topologies, and routing protocols. In addition to fast forwarding path failure
detection, BFD provides a consistent failure detection method for network administrators. Because the network
administrator can use BFD to detect forwarding path failures at a uniform rate, rather than the variable rates
for different routing protocol hello mechanisms, network profiling and planning is easier, and reconvergence
time is consistent and predictable. The main benefit of implementing BFD for BGP is a significantly faster
reconvergence time. For internal BGP (iBGP) sessions and external BGP (eBGP) sessions that are either
single hop or multihop, BGP can use of the multihop BFD support to help improve the BGP convergence
because BFD detection and failure times are faster than the IGP convergence times in most of the network
topologies. BGP needs the support of multihop BFD as described in RFC5882, Generic Application of
Bidirectional Forwarding Detection (BFD).
BGP by default will purge the routes received from a specific peer when a BFD down event occurs and BFD
informs BGP about it. The cBit in BFD determines whether BFD is dependent or independent of the Control
Plane. Clients like BGP, whose peers are enabled with fast fall over feature with BFD support, can use this
BFD cBit support to provide a more deterministic mechanism to do nonstop forwarding (NSF) when BGP
graceful restart is enabled along with BFD fast-fallover support for BGP sessions.
When BGP is using BFD for the fast fallover feature for remote connectivity detection, BFD can detect some
of those failures. If BFD is independent of the control plane, a BFD session failure means that data cannot be
forwarded anymore (due to link control failures) and so the BGP graceful restart procedures should be aborted
to avoid traffic black holes. On the other hand, when BFD is dependent on the control plane, a BFD failure
cannot be separated out from the other events taking place in the control plane. When the control plane crashes,
a switchover happens and BFD restarts. It is best for the clients (like BGP) to avoid any aborts due to the
graceful restart taking place.

IP Routing: BGP Configuration Guide
936


BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
How to Configure BFD - BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode

The table below describes the handling of BFD down events by BGP.
Table 81: BGP handling of BFD Down Event

BFD Down Event

Failure—Control Plane
Independent?

BGP Action for NSF (when GR and
BFD are enabled)

BGP control plane detection failure Yes
enabled

Purge Routes

BGP control plane detection failure No
enabled

Carry on NSF and keep stale routes
in Routing Information Base (RIB)

BGP control plane detection failure Yes
disabled (the default behavior)

Purge Routes

BGP control plane detection failure No
disabled (the default behavior)

Purge Routes

BGP session establishment works independently from BFD state change, except for fast fall-over detection,
that is, inaccessible next-hop and cause best path re-calculation. This means that the BGP session could be
established while BFD state is down or dampened, even with neighbor fail-over bfd configured.
From the XE 3.17S release the new optional keyword strict-mode is introduced, which does not allow BGP
session to become established, if BFD is in down state. When BFD is dampened or down the routing protocol
states or sessions cannot come up.

How to Configure BFD - BGP Multihop Client Support, cBit (IPv4
and IPv6), and Strict Mode
Configuring BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict
Mode
Before you begin

Note

The multihop BFD minimum detection time should be higher than IGP convergence times in your network
to ensure that down events are not mistakenly identified during reconvergences, causing multihop BGP sessions
to flap.

Note

For the BFD strict mode to work, configure BFD on both the neighboring devices.

IP Routing: BGP Configuration Guide
937


BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
Configuring BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode

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
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address update-source interface-type interface-number
neighbor ip-address remote-as autonomous-system-number
neighbor ip-address ebgp-multihop ttl
neighbor ip-address fall-over bfd [multi-hop] [check-control-plane-failure] [ strict-mode]
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

Configures the Border Gateway Protocol (BGP) routing
process and enters router configuration mode.

Device(config)# router bgp 50000

Step 4

neighbor ip-address remote-as
autonomous-system-number

Adds an entry to the BGP or multiprotocol BGP neighbor
table.

Example:
Device(config-router)# neighbor 10.0.0.2 remote-as
100

Step 5

neighbor ip-address update-source interface-type
interface-number

Allows BGP sessions to use any operational interface for
TCP connections.

Example:
Device(config-router)# neighbor 10.0.0.2
update-source GigabitEthernet 0/0/0

Step 6

neighbor ip-address remote-as
autonomous-system-number
Example:

IP Routing: BGP Configuration Guide
938

Adds an entry to the BGP or multiprotocol BGP neighbor
table.


BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
Configuration Examples for BFD - BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode

Command or Action

Purpose

Device(config-router)# neighbor 10.0.0.2 remote-as
100

Step 7

neighbor ip-address ebgp-multihop ttl
Example:

Accepts and attempts BGP connections to external peers
residing on networks that are not directly connected.

Device(config-router)# neighbor 10.0.0.2
ebgp-multihop 4

Step 8

neighbor ip-address fall-over bfd [multi-hop]
[check-control-plane-failure] [ strict-mode]

• Enables BGP to monitor the peering session of a
specified neighbor for adjacency changes and to
deactivate the peering session.

Example:

• Configures BGP BFD with control plane independence
enabled for BFD cBit support.

Device(config-router)# neighbor 10.0.0.2 fall-over
bfd multi-hop check-control-plane-failure
strict-mode

Step 9

Exits router configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router)# end

Configuration Examples for BFD - BGP Multihop Client Support,
cBit (IPv4 and IPv6), and Strict Mode
Example: Configuring BFD—BGP Multihop Client Support, cBit (IPv4/IPv6),
and Strict Mode
R1 e0/0 ---------------e0/0 R2
Router 1 configuration
hostname R1
!
bfd map ipv4 2.2.2.2/32 1.1.1.1/32 mh1
!
bfd-template multi-hop mh1
interval min-tx 50 min-rx 50 multiplier 3
!
interface Loopback1
ip address 1.1.1.1 255.255.255.255
ip ospf 1 area 0
!
interface Ethernet0/0
ip address 10.0.0.1 255.255.255.0
ip ospf 1 area 0
!

IP Routing: BGP Configuration Guide
939


BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
Verifying BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode

router ospf 1
!
router bgp 1
neighbor 2.2.2.2 remote-as 1
neighbor 2.2.2.2 update-source Loopback1
neighbor 2.2.2.2 fall-over bfd multi-hop check-control-plane-failure strict-mode
!
address-family ipv4
neighbor 2.2.2.2 activate
exit-address-family
!
Router 2 configuration:
hostname R2
!
bfd map ipv4 1.1.1.1/32 2.2.2.2/32 mh1
bfd-template multi-hop mh1
interval min-tx 50 min-rx 50 multiplier 3
!
interface Loopback1
ip address 2.2.2.2 255.255.255.255
ip ospf 1 area 0
!
interface Ethernet0/0
ip address 10.0.0.2 255.255.255.0
ip ospf 1 area 0
!
router ospf 1
!
router bgp 1
neighbor 1.1.1.1 remote-as 1
neighbor 1.1.1.1 update-source Loopback1
neighbor 1.1.1.1 fall-over bfd multi-hop check-control-plane-failure strict-mode
!
address-family ipv4
neighbor 1.1.1.1 activate
exit-address-family
!

Verifying BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict
Mode
The following examples show how to verify if BFD is enabled on the neighbor, peer-group.
R801-ASBR#sh ip bgp neighbor 11.1.0.2
BGP neighbor is 11.1.0.2, remote AS 65000, external link
Fall over configured for session
BFD is configured. BFD peer is Up. Using BFD to detect fast fallover (single-hop)
in strict-mode.
BGP version 4, remote router ID 10.10.10.10
BGP state = Established, up for 00:04:12
Last read 00:00:49, last write 00:00:24, hold time is 180, keepalive interval
is 60 seconds
…

If BFD is up and running, the following is displayed:

IP Routing: BGP Configuration Guide
940


BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
Additional References

Fall over configured for session
BFD is configured. BFD peer is Up. Using BFD to detect fast fallover (single-hop)
in strict-mode (will be verified).
…

If BFD is not up and running, the following is displayed:
Fall over configured for session
BFD is configured. BFD peer is Down. Using BFD to detect fast fallover
(single-hop) in strict-mode.

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

Feature Information for BFD—BGP Multihop Client Support,
cBit (IPv4/IPv6), and Strict Mode
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
941


BFD—BGP Multihop Client Support, cBit (IPv4 and IPv6), and Strict Mode
Feature Information for BFD—BGP Multihop Client Support, cBit (IPv4/IPv6), and Strict Mode

Table 82: Feature Information for BFD—BGP Multihop Client Support, cBit (IPv4/IPv6), and Strict Mode

Feature Name

Releases

Feature Information

BFD—BGP Multihop Client
Support and cBit (IPv4/IPv6)

15.2(4)S

The BFD—BGP Multihop Client
Support feature enables Border
Gateway Protocol (BGP) to use
multihop Bidirectional Forwarding
Detection (BFD) support, which
improves BGP convergence as BFD
detection and failure times are
faster than the Interior Gateway
Protocol (IGP) convergence times
in most of network topologies.

Cisco IOS XE Release 3.6S
Cisco IOS XE Release 3.7S

The BFD—BGP cBIT feature
allows BGP to determine if BFD
failure is dependent or independent
of the Control Plane. This allows
BGP greater flexibility in handling
BFD down events.
In Cisco IOS XE Release 3.7S,
support was added for the Cisco
ASR 903 router.
The following commands were
modified: neighbor fall-over and
show ip bgp neighbors.
BFD—BGP Multihop Client
Support, cBit (IPv4/IPv6), and
Strict Mode

Cisco IOS XE Release 3.17S

In Cisco IOS XE Release 3.17S,
the following command was
modified:
neighbor ip-address fall-over
bfd [multi-hop|single-hop]
[check-control-plane-failure] [
strict-mode] .

IP Routing: BGP Configuration Guide
942
