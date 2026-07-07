---
title: "BGP NSR Support for iBGP Peers"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-nsr-support-for-ibgp-peers
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 58 BGP NSR Support for iBGP Peers BGP NSR provides BGP nonstop routing (NSR) and nonstop forwarding (NSF) in the event of a switchover from an Active RP to the Standby RP. The BGP NSR Support for iBGP Peers feature provides NSR support for iBGP peers configured under the IPv4 unicast or IPv4 + label address family. • Finding Feature Information, on page 895 • Restrictions on BGP NSR Supp"
---

# BGP NSR Support for iBGP Peers

CHAPTER

58

BGP NSR Support for iBGP Peers
BGP NSR provides BGP nonstop routing (NSR) and nonstop forwarding (NSF) in the event of a switchover
from an Active RP to the Standby RP. The BGP NSR Support for iBGP Peers feature provides NSR support
for iBGP peers configured under the IPv4 unicast or IPv4 + label address family.
• Finding Feature Information, on page 895
• Restrictions on BGP NSR Support for iBGP Peers, on page 895
• Information About BGP NSR Support for iBGP Peers, on page 896
• How to Configure BGP NSR Support for iBGP Peers, on page 896
• Configuration Examples for BGP NSR Support for an iBGP Peer, on page 900
• Additional References, on page 900
• Feature Information for BGP NSR Support for iBGP Peers, on page 901

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions on BGP NSR Support for iBGP Peers
This feature applies to iBGP peers configured under IPv4 unicast or IPv4 + label address families.

IP Routing: BGP Configuration Guide
895


BGP NSR Support for iBGP Peers
Information About BGP NSR Support for iBGP Peers

Information About BGP NSR Support for iBGP Peers
Benefit of BGP NSR Support for iBGP Peers
Nonstop routing is beneficial for iBGP peers because it reduces the likelihood of dropped packets during
switchover from the Active RP to the Standby RP. Switchover occurs when the Active RP fails for some
reason, and the Standby RP takes control of Active RP operations.

How to Configure BGP NSR Support for iBGP Peers
Making an iBGP Peer NSR-Capable for the IPv4 Address Family
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.

enable
configure terminal
router bgp autonomous-system-number
address-family ipv4 [unicast | vrf vrf-name]
neighbor ip-address remote-as as-number
neighbor ip-address activate
neighbor ip-address ha-mode sso
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

Enters router configuration mode for the specified routing
process.

Device(config)# router bgp 4000

Step 4

address-family ipv4 [unicast | vrf vrf-name]
Example:

IP Routing: BGP Configuration Guide
896

Specifies the IPv4 address family and enters address family
configuration mode.


BGP NSR Support for iBGP Peers
Making an iBGP Peer NSR-Capable for the VPNv4 Address Family

Command or Action

Purpose
• The unicast keyword specifies the IPv4 unicast address
family.

Device(config-router)# address-family ipv4 unicast

• The vrf keyword and vrf-name argument specify the
name of the virtual routing and forwarding (VRF)
instance to associate with subsequent IPv4 address
family configuration mode commands.
Step 5

neighbor ip-address remote-as as-number

Specifies the autonomous system of the neighbor.

Example:
Device(config-router-af)# neighbor 192.168.1.1
remote-as 4000

Step 6

neighbor ip-address activate

Activates the specified peer.

Example:
Device(config-router-af)# neighbor 192.168.1.1
activate

Step 7

neighbor ip-address ha-mode sso
Example:

Configures a BGP neighbor to support BGP NSR with
stateful switchover (SSO).

Device(config-router-af)# neighbor 192.168.1.1
ha-mode sso

Step 8

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Making an iBGP Peer NSR-Capable for the VPNv4 Address Family
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.

enable
configure terminal
router bgp autonomous-system-number
neighbor ip-address remote-as as-number
neighbor ip-address ha-mode sso
address-family vpnv4 [unicast]
neighbor ip-address activate
end

IP Routing: BGP Configuration Guide
897


BGP NSR Support for iBGP Peers
Making an iBGP Peer NSR-Capable for the VPNv4 Address Family

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

Device(config)# router bgp 4000

Step 4

neighbor ip-address remote-as as-number

Specifies the autonomous system of the neighbor.

Example:
Device(config-router)# neighbor 192.168.1.1
remote-as 4000

Step 5

neighbor ip-address ha-mode sso
Example:

Configures a BGP neighbor to support BGP NSR with
stateful switchover (SSO).

Device(config-router)# neighbor 192.168.1.1 ha-mode
sso

Step 6

address-family vpnv4 [unicast]
Example:

Specifies the VPNv4 address family and enters address
family configuration mode.

Device(config-router)# address-family VPNv4 unicast

Step 7

neighbor ip-address activate

Activates the specified peer.

Example:
Device(config-router-af)# neighbor 192.168.1.1
activate

Step 8

end
Example:
Device(config-router-af)# end

IP Routing: BGP Configuration Guide
898

Exits address family configuration mode and returns to
privileged EXEC mode.


BGP NSR Support for iBGP Peers
Making an iBGP Peer NSR Capable at the Router Level

Making an iBGP Peer NSR Capable at the Router Level
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.

enable
configure terminal
router bgp autonomous-system-number
neighbor ip-address remote-as as-number
neighbor ip-address activate
neighbor ip-address ha-mode sso
end
show ip bgp sso summary

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

Device(config)# router bgp 4000

Step 4

neighbor ip-address remote-as as-number

Specifies the autonomous system of the neighbor.

Example:
Device(config-router)# neighbor 192.168.1.1
remote-as 4000

Step 5

neighbor ip-address activate

Activates the specified neighbor.

Example:
Device(config-router)# neighbor 192.168.1.1
activate

Step 6

neighbor ip-address ha-mode sso
Example:

Configures the specified peer to be NSR capable in all of
the NSR-supported address families under which that peer
has been activated.

Device(config-router)# neighbor 192.168.1.1 ha-mode
sso

IP Routing: BGP Configuration Guide
899


BGP NSR Support for iBGP Peers
Configuration Examples for BGP NSR Support for an iBGP Peer

Step 7

Command or Action

Purpose

end

Exits configuration mode and returns to privileged EXEC
mode.

Example:
Device(config-router)# end

Step 8

show ip bgp sso summary
Example:

(Optional) Displays information about stateful switchover
(sso) and whether a peer has NSR enabled or disabled.

Device# show ip bgp sso summary

Configuration Examples for BGP NSR Support for an iBGP Peer
Example: Configuring an iBGP Peer To Be NSR Capable
Configuring an iBGP Peer to Be NSR Capable at the Address Family Level
router bgp 4000
address-family ipv4 unicast
neighbor 192.168.1.1 remote-as 4000
neighbor 192.168.1.1 activate
neighbor 192.168.1.1 ha-mode sso

Configuring an iBGP Peer to Be NSR Capable at the Router Level
router bgp 4000
neighbor 192.168.1.1 remote-as 4000
neighbor 192.168.1.1 activate
neighbor 192.168.1.1 ha-mode sso

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
900


BGP NSR Support for iBGP Peers
Feature Information for BGP NSR Support for iBGP Peers

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

Feature Information for BGP NSR Support for iBGP Peers
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 77: Feature Information for BGP NSR Support for iBGP Peers

Feature Name

Releases

Feature Information

BGP NSR Support for iBGP Peers Cisco IOS XE Release 3.6S
Cisco IOS XE Release 3.7S

BGP NSR provides BGP nonstop
routing and nonstop forwarding in
the event of a switchover from an
active RP to the standby RP.
The following commands were
modified: neighbor ha-mode sso
and show ip bgp vpnv4 all sso
summary.

IP Routing: BGP Configuration Guide
901


BGP NSR Support for iBGP Peers
Feature Information for BGP NSR Support for iBGP Peers

IP Routing: BGP Configuration Guide
902
