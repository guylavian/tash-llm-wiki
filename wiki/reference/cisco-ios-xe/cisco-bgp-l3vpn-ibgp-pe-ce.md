---
title: "L3VPN iBGP PE-CE"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-l3vpn-ibgp-pe-ce
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 75 L3VPN iBGP PE-CE The L3VPN iBGP PE-CE feature enables the provider edge (PE) and customer edge (CE) devices to exchange Border Gateway Protocol (BGP) routing information by peering as iBGP instead of as external BGP peering between the PE and CE. • Finding Feature Information, on page 1059 • Restrictions for L3VPN iBGP PE-CE, on page 1059 • Information About L3VPN iBGP PE-CE, on page"
---

# L3VPN iBGP PE-CE

CHAPTER

75

L3VPN iBGP PE-CE
The L3VPN iBGP PE-CE feature enables the provider edge (PE) and customer edge (CE) devices to exchange
Border Gateway Protocol (BGP) routing information by peering as iBGP instead of as external BGP peering
between the PE and CE.
• Finding Feature Information, on page 1059
• Restrictions for L3VPN iBGP PE-CE, on page 1059
• Information About L3VPN iBGP PE-CE, on page 1060
• How to Configure L3VPN iBGP PE-CE, on page 1060
• Configuration Examples for L3VPN iBGP PE-CE, on page 1061
• Additional References for L3VPN iBGP PE-CE, on page 1061
• Feature Information for L3VPN iBGP PE-CE, on page 1062

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions for L3VPN iBGP PE-CE
We recommend not using the soft-reconfiguration inbound or BGP soft-reconfig-backup feature with the
iBGP PE CE.

IP Routing: BGP Configuration Guide
1059


L3VPN iBGP PE-CE
Information About L3VPN iBGP PE-CE

Information About L3VPN iBGP PE-CE
L3VPN iBGP PE-CE
When BGP is used as the provider edge (PE) or customer edge (CE) routing protocol, the peering sessions
are configured as an external peering between the VPN provider autonomous system (AS) and the customer
network autonomous system. The L3VPN iBGP PE-CE feature enables the PE and CE devices to exchange
Border Gateway Protocol (BGP) routing information by peering as internal Border Gateway Protocol (iBGP)
instead of the widely used external BGP peering between the PE and the CE. This mechanism applies at each
PE device where a VRF-based CE is configured as iBGP. This eliminates the need for service providers (SPs)
to configure autonomous system override for the CE. With this feature enabled, there is no need to configure
the virtual private network (VPN) sites using different autonomous systems.
The introduction of the neighbor internal-vpn-client command enables PE devices to make an entire VPN
cloud act like an internal VPN client to the CE devices. These CE devices are connected internally to the VPN
cloud through the iBGP PE-CE connection inside the VRF. After this connection is established, the PE device
encapsulates the CE-learned path into an attribute called ATTR_SET and carries it in the iBGP-sourced path
throughout the VPN core to the remote PE device. At the remote PE device, this attribute is assigned with
individual attributes and the source CE path is extracted and sent to the remote CE devices. ATTR_SET is
an optional transitive attribute that carries a set of BGP path attributes. It can include any BGP attribute that
can occur in a BGP update message as received from the source CE device.

How to Configure L3VPN iBGP PE-CE
Configuring L3VPN iBGP PE-CE
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
router bgp as-number
address-family ipv4 vrf name
neighbor ip-address internal-vpn-client

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device> enable

Step 2

configure terminal
Example:
Device(config)# configure terminal

IP Routing: BGP Configuration Guide
1060

Enters global configuration mode.


L3VPN iBGP PE-CE
Configuration Examples for L3VPN iBGP PE-CE

Step 3

Command or Action

Purpose

router bgp as-number

Enters router configuration mode and creates a BGP routing
process.

Example:
Device(config)# router bgp 100

Step 4

address-family ipv4 vrf name

Enters address family configuration mode and configures
VPN routing and forwarding.

Example:
Device(config-router)# address-family ipv4 vrf blue

Step 5

neighbor ip-address internal-vpn-client
Example:
Device(config-router-af)# neighbor 10.0.0.1
internal-vpn-client

Defines a neighboring device with which to exchange
routing information. The neighbor internal-vpn-client
command stacks the iBGP-CE neighbor path in the VPN
attribute set .

Configuration Examples for L3VPN iBGP PE-CE
Example: Configuring L3VPN iBGP PE-CE
The following example shows how to configure L3VPN iBGP PE-CE:
Device# enable
Device(config)# configure terminal
Device(config)# router bgp 100
Device(config-router)# address-family ipv4 vrf blue
Device(config-router-af)# neighbor 10.0.0.1 internal-vpn-client

Additional References for L3VPN iBGP PE-CE
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Routing: BGP Configuration Guide
1061


L3VPN iBGP PE-CE
Feature Information for L3VPN iBGP PE-CE

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

Feature Information for L3VPN iBGP PE-CE
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 95: Feature Information for L3VPN iBGP PE-CE

Feature Name

Releases

L3VPN iBGP PE-CE Cisco IOS XE
Release 3.10S

Feature Information
The L3VPN iBGP PE-CE feature enables the provider edge
(PE) and customer edge (CE) devices to exchange Border
Gateway Protocol (BGP) routing information by peering as
iBGP instead of as external BGP between the PE and CE.
The neighbor internal-vpn-client command was introduced.

IP Routing: BGP Configuration Guide
1062
