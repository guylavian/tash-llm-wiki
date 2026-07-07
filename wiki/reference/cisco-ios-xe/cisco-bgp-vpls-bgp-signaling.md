---
title: "VPLS BGP Signaling"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-vpls-bgp-signaling
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 68 VPLS BGP Signaling The two primary functions of the Virtual Private LAN Service (VPLS) control plane are autodiscovery and signaling. The VPLS BGP Signaling feature enables you to use BGP as both an autodiscovery and a signaling protocol for VPLS, in accordance with RFC 4761. • Finding Feature Information, on page 1007 • Prerequisites for VPLS BGP Signaling, on page 1007 • Information"
---

# VPLS BGP Signaling

CHAPTER

68

VPLS BGP Signaling
The two primary functions of the Virtual Private LAN Service (VPLS) control plane are autodiscovery and
signaling. The VPLS BGP Signaling feature enables you to use BGP as both an autodiscovery and a signaling
protocol for VPLS, in accordance with RFC 4761.
• Finding Feature Information, on page 1007
• Prerequisites for VPLS BGP Signaling, on page 1007
• Information About VPLS BGP Signaling, on page 1008
• How to Configure VPLS BGP Signaling, on page 1009
• Configuration Examples for VPLS BGP Signaling, on page 1011
• Additional References for VPLS BGP Signaling, on page 1012
• Feature Information for VPLS BGP Signaling, on page 1013

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for VPLS BGP Signaling
You are familiar with the concepts in the “Configuring Virtual Private LAN Services” and the “VPLS
Autodiscovery BGP Based” modules of the .

IP Routing: BGP Configuration Guide
1007


VPLS BGP Signaling
Information About VPLS BGP Signaling

Information About VPLS BGP Signaling
Overview of VPLS BGP Signaling
Prior to the VPLS BGP Signaling feature, BGP was used for autodiscovery and Label Distribution Protocol
(LDP) for signaling in accordance with RFC 6074. The VPLS BGP Signaling feature enables you to use BGP
as the control plane protocol for both autodiscovery and signaling in accordance with RFC 4761.
As specified in RFC 4761, internal BGP (iBGP) peers will exchange update messages of the L2VPN AFI/SAFI
with L2VPN information to perform both autodiscovery and signaling. The BGP multiprotocol Network Layer
Reachability Information (NLRI) consists of a Route Distinguisher (RD), VPLS Endpoint ID (VE ID), VE
Block Offset (VBO), VE Block Size (VBS), and Label Base (LB).
The figure below shows the format of the NLRI for RFC 4761.
Figure 87: RFC 4761 NLRI

Additional information, such as next-hop, route target (specified for a VPLS instance), and other Layer 2 data
are carried in the BGP extended community attributes. A route target-based import/export mechanism similar
to L3VPN is performed by BGP to filter L2VPN NLRIs of a particular VPLS instance.
Whether you use BGP signaling (RFC 4761) or LDP signaling (RFC 6074) depends on the commands you
specify. To enable the VPLS BGP Signaling feature, use the autodiscovery bgp signaling bgp command in
L2 VFI configuration mode. This command is supported on a per VPLS instance basis.
If a BGP session receives an invalid (that is, not matching the configuration) BGP update advertisement
(update or withdraw), it is ignored.
BGP’s main task in supporting VPLS is route distribution via the L2VPN address family and interactions
with L2VPN. Interactions between BGP and other components remain the same. Basic BGP functionalities
like best-path selection, next-hop handling, and update generation, continue to operate in the same manner
with VPLS BGP signaling. BGP RT constraint works seamlessly with the BGP VPLS Signaling feature.

IP Routing: BGP Configuration Guide
1008


VPLS BGP Signaling
How to Configure VPLS BGP Signaling

How to Configure VPLS BGP Signaling
Configuring VPLS BGP Signaling
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
l2vpn vfi context name
vpn id vpn-id
autodiscovery bgp signaling {bgp | ldp} [template template-name]
ve id ve-id
ve range ve-range
exit
exit
router bgp autonomous-system-number
bgp graceful-restart
neighbor ip-address remote-as autonomous-system-number
address-family l2vpn [vpls]
neighbor ip-address activate
neighbor ip-address send-community [both | standard | extended]
neighbor ip-address suppress-signaling-protocol ldp
end
show bgp l2vpn vpls {all | rd route-distinguisher}

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

l2vpn vfi context name
Example:

Establishes a L2VPN virtual forwarding interface (VFI)
between two or more separate networks and enters Layer
2 VFI configuration mode.

Device(config)# l2vpn vfi context vfi1

IP Routing: BGP Configuration Guide
1009


VPLS BGP Signaling
Configuring VPLS BGP Signaling

Step 4

Command or Action

Purpose

vpn id vpn-id

Configures a VPN ID for the VPLS domain.

Example:
Device(config-vfi)# vpn id 100

Step 5

autodiscovery bgp signaling {bgp | ldp} [template
template-name]

Enables BGP signaling and discovery or LDP signaling
and enters L2VPN VFI autodiscovery configuration mode.

Example:

Note

For the VPLS BGP Signaling feature use the
autodiscovery bgp signaling bgp command.

Device(config-vfi)# autodiscovery bgp signaling
bgp

Step 6

ve id ve-id
Example:

Specifies the VPLS endpoint (VE) device ID value. The
VE ID identifies a VFI within a VPLS service. The VE
device ID value is from 1 to 16384.

Device(config-vfi-autodiscovery)# ve id 1001

Step 7

ve range ve-range
Example:
Device(config-vfi-autodiscovery)# ve range 12

Step 8

exit
Example:

Specifies the VE device ID range value. The VE range
overrides the minimum size of VE blocks. The default
minimum size is 10. Any configured VE range must be
higher than 10.
Exits L2VPN VFI autodiscovery configuration mode and
enters L2VPN VFI configuration mode.

Device(config-vfi-autodiscovery)# exit

Step 9

exit
Example:

Exits L2VPN VFI configuration mode and enters global
configuration mode.

Device(config-vfi)# exit

Step 10

router bgp autonomous-system-number
Example:

Enters router configuration mode to create or configure a
BGP routing process.

Device(config)# router bgp 100

Step 11

bgp graceful-restart
Example:

Enables the BGP graceful restart capability and BGP
nonstop forwarding (NSF) awareness.

Device(config-router)# bgp graceful-restart

Step 12

neighbor ip-address remote-as
autonomous-system-number
Example:
Device(config-router)# neighbor 10.10.10.1
remote-as 100

IP Routing: BGP Configuration Guide
1010

Configures peering with a BGP neighbor in the specified
autonomous system.


VPLS BGP Signaling
Configuration Examples for VPLS BGP Signaling

Step 13

Command or Action

Purpose

address-family l2vpn [vpls]

Specifies the L2VPN address family and enters address
family configuration mode.

Example:
Device(config-router)# address-family l2vpn vpls

• The optional vpls keyword specifies that VPLS
endpoint provisioning information is to be distributed
to BGP peers.
In this example, an L2VPN VPLS address family session
is created.

Step 14

neighbor ip-address activate
Example:

Enables the neighbor to exchange information for the
L2VPN VPLS address family with the local device.

Device(config-router-af)# neighbor 10.10.10.1
activate

Step 15

neighbor ip-address send-community [both | standard Specifies that a communities attribute should be sent to a
BGP neighbor.
| extended]
Example:

• In this example, an extended communities attribute
is sent to the neighbor at 10.10.10.1.

Device(config-router-af)# neighbor 10.10.10.1
send-community extended

Step 16

neighbor ip-address suppress-signaling-protocol ldp
Example:
Device(config-router-af)# neighbor 10.10.10.1
suppress-signaling-protocol ldp

Step 17

end
Example:

Suppresses LDP signaling and enables BGP signaling.
• In this example LDP signaling is suppressed (and
BGP signaling enabled) for the neighbor at
10.10.10.1.
Exits address family configuration mode and returns to
privileged EXEC mode.

Device(config-router-af)# end

Step 18

show bgp l2vpn vpls {all | rd route-distinguisher}
Example:

(Optional) Displays information about the L2VPN VPLS
address family.

Device# show bgp l2vpn vpls all

Configuration Examples for VPLS BGP Signaling
Example: Configuring and Verifying VPLS BGP Signaling
l2vpn vfi context vfi1
vpn id 100

IP Routing: BGP Configuration Guide
1011


VPLS BGP Signaling
Additional References for VPLS BGP Signaling

autodiscovery bgp signaling bgp
ve id 1001
ve range 10
!
!
router bgp 100
bgp graceful-restart
neighbor 209.165.200.224 remote-as 100
neighbor 209.165.200.224 update-source Loopback1
!
address-family l2vpn vpls
neighbor 209.165.200.224 activate
neighbor 209.165.200.224 send-community extended
neighbor 209.165.200.224 suppress-signaling-protocol ldp
exit-address-family
!
show bgp l2vpn vpls all
Network
Route Distinguisher: 100:100
*>100:100:VEID-1001:Blk-1001/136

Next Hop

*>i 100:100:VEID-1003:Blk-1000/136

209.165.200.224

Metric LocPrf Weight Path

0.0.0.0

32768
0

100

?
0

?

Additional References for VPLS BGP Signaling
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

BGP commands: complete command syntax, command mode, defaults, Cisco IOS IP Routing: BGP
command history, usage guidelines, and examples.
Command Reference
Configuring Virtual Private LAN Services
Configuring Access Port

Configuring Virtual Private LAN
Services,

VPLS Autodiscovery BGP Based
Standards and RFCs
Standard/RFC Title
RFC 4761

Virtual Private LAN Service (VPLS) Using BGP for Auto-Discovery and Signaling

RFC 6074

Provisioning, Auto-Discovery, and Signaling in Layer 2 Virtual Private Networks (L2VPNs)

IP Routing: BGP Configuration Guide
1012


VPLS BGP Signaling
Feature Information for VPLS BGP Signaling

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

Feature Information for VPLS BGP Signaling
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 88: Feature Information for VPLS BGP Signaling

Feature Name

Releases

Feature Information

VPLS BGP Signaling

Cisco IOS XE Release 3.8S

The VPLS BGP Signaling feature
enables you to use BGP as both an
autodiscovery and signaling
protocol for VPLS, in accordance
with RFC 4761.
The following commands were
introduced or modified:
autodiscovery (MPLS), neighbor
suppress-signaling-protocol, show
bgp l2vpn vpls, and ve.

IP Routing: BGP Configuration Guide
1013


VPLS BGP Signaling
Feature Information for VPLS BGP Signaling

IP Routing: BGP Configuration Guide
1014
