---
title: "BGP VPLS Auto Discovery Support on Route Reflector"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-vpls-auto-discovery-support-on-route-reflector
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 23 BGP VPLS Auto Discovery Support on Route Reflector BGP Route Reflector was enhanced to be able to reflect BGP VPLS prefixes without having VPLS explicitly configured on the route reflector. • Finding Feature Information, on page 475 • Information About BGP VPLS Auto Discovery Support on Route Reflector, on page 475 • Configuration Example for BGP VPLS Auto Discovery Support on Route R"
---

# BGP VPLS Auto Discovery Support on Route Reflector

CHAPTER

23

BGP VPLS Auto Discovery Support on Route
Reflector
BGP Route Reflector was enhanced to be able to reflect BGP VPLS prefixes without having VPLS explicitly
configured on the route reflector.
• Finding Feature Information, on page 475
• Information About BGP VPLS Auto Discovery Support on Route Reflector, on page 475
• Configuration Example for BGP VPLS Auto Discovery Support on Route Reflector, on page 476
• Additional References, on page 476
• Feature Information for BGP VPLS Auto Discovery Support on Route Reflector, on page 477

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP VPLS Auto Discovery Support on Route
Reflector
BGP VPLS Autodiscovery Support on Route Reflector
In Cisco IOS Release 12.2(33)SRE, BGP VPLS Autodiscovery Support on Route Reflector was introduced.
On the Cisco 7600 and Cisco 7200 series routers, BGP Route Reflector was enhanced to be able to reflect
BGP VPLS prefixes without having VPLS explicitly configured on the route reflector. The route reflector
reflects the VPLS prefixes to other provider edge (PE) routers so that the PEs do not need to have a full mesh
of BGP sessions. The network administrator configures only the BGP VPLS address family on the route
reflector.

IP Routing: BGP Configuration Guide
475


BGP VPLS Auto Discovery Support on Route Reflector
Restrictions for BGP VPLS Auto Discovery Support on Route Reflector

For an example of a route reflector configuration that can reflect VPLS prefixes, see the “Example: BGP
VPLS Autodiscovery Support on Route Reflector” section. For more information about VPLS Autodiscovery,
see the “VPLS Autodiscovery BGP Based” module in the MPLS Layer 2 VPNs Configuration Guide .

Restrictions for BGP VPLS Auto Discovery Support on Route Reflector
• VPLS BGP Auto Discovery with BGP Signaling in inter-AS Option C is not supported in IOS XE for
route reflector.

Configuration Example for BGP VPLS Auto Discovery Support
on Route Reflector
Example: BGP VPLS Autodiscovery Support on Route Reflector
In the following example, a host named PE-RR (indicating Provider Edge Route Reflector) is configured as
a route reflector capable of reflecting VPLS prefixes. The VPLS address family is configured by address-family
l2vpn vpls command.
hostname PE-RR
!
router bgp 1
bgp router-id 1.1.1.3
no bgp default route-target filter
bgp log-neighbor-changes
neighbor iBGP_PEERS peer-group
neighbor iBGP_PEERS remote-as 1
neighbor iBGP_PEERS update-source Loopback1
neighbor 1.1.1.1 peer-group iBGP_PEERS
neighbor 1.1.1.2 peer-group iBGP_PEERS
!
address-family l2vpn vpls
neighbor iBGP_PEERS send-community extended
neighbor iBGP_PEERS route-reflector-client
neighbor 1.1.1.1 peer-group iBGP_PEERS
neighbor 1.1.1.2 peer-group iBGP_PEERS
exit-address-family
!

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Routing: BGP Configuration Guide
476


BGP VPLS Auto Discovery Support on Route Reflector
Feature Information for BGP VPLS Auto Discovery Support on Route Reflector

Standards and RFCs
Standard/RFC Title
RFC 2918

Route Refresh Capability for BGP-4

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

Feature Information for BGP VPLS Auto Discovery Support on
Route Reflector
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.
Table 39: Feature Information for BGP VPLS Auto Discovery Support on Route Reflector

Feature Name

Releases

Feature Information

BGP VPLS Auto Discovery
Support on Route Reflector

12.2(33)SRE

BGP Route Reflector was enhanced
to be able to reflect BGP VPLS
prefixes without having VPLS
explicitly configured on the route
reflector.

Cisco IOS XE Release 2.5

This feature was introduced on the
Cisco 7600 and Cisco 7200 series
routers.

IP Routing: BGP Configuration Guide
477


BGP VPLS Auto Discovery Support on Route Reflector
Feature Information for BGP VPLS Auto Discovery Support on Route Reflector

IP Routing: BGP Configuration Guide
478
