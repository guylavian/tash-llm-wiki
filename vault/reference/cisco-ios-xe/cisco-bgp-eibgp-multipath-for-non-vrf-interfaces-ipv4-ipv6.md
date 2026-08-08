---
title: "eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-eibgp-multipath-for-non-vrf-interfaces-ipv4-ipv6
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 74 eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6) The eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6) feature allows you to configure multipath load sharing among native IPv4 and IPv6 external Border Gateway Protocol (eBGP) and internal BGP (iBGP) paths for improved load balancing in deployments. This module explains the feature and how to configure it. • Finding Feature Informati"
---

# eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)

CHAPTER

74

eiBGP Multipath for Non-VRF Interfaces
(IPv4/IPv6)
The eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6) feature allows you to configure multipath load
sharing among native IPv4 and IPv6 external Border Gateway Protocol (eBGP) and internal BGP (iBGP)
paths for improved load balancing in deployments. This module explains the feature and how to configure it.
• Finding Feature Information, on page 1055
• Information About eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6), on page 1055
• How to Configure eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6), on page 1056
• Configuration Examples for eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6), on page 1057
• Feature Information for eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6), on page 1057

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About eiBGP Multipath for Non-VRF Interfaces
(IPv4/IPv6)
eiBGP Multipath for Non-VRF Interfaces Overview
The Border Gateway Protocol (BGP) path-selection algorithm prefers external BGP (eBGP) paths over internal
BGP (iBGP) paths. With the eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6) feature, this algorithm is
modified to allow multipath load sharing among native IPv4 and IPv6 eBGP and iBGP paths. Prior to the
eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6) feature, this functionality was only available on VPN
routing and forwarding (VRF) instances. With this feature, the functionality is extended to non-VRF interfaces.
The maximum-paths command allows you to configure BGP to install multiple paths in the Routing

IP Routing: BGP Configuration Guide
1055


eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)
How to Configure eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)

Information Base (RIB) for multipath load sharing. The BGP best path algorithm selects a single multipath
as the best path and advertises the path to BGP peers. Other multipaths are inserted into both the BGP table
and the RIB, and these multipaths are used by Cisco Express Forwarding to perform load balancing, which
is performed either on a per-packet basis or on a per-source or per-destination basis.
This feature can be configured on a customer provider edge (PE) device. However, the feature should be
configured only on one PE device at the customer site. If this feature is configured on more than one PE
device, some parts of the traffic may loop between the PE devices at the customer site. Therefore, it is important
to set up the feature appropriately to avoid traffic loops. This feature is enabled by default.

How to Configure eiBGP Multipath for Non-VRF Interfaces
(IPv4/IPv6)
Enabling IPv4/IPv6 Multipaths for Non-VRF Interfaces
SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
router bgp autonomous-system-number
Enter one of the following:
• address-family ipv4 unicast
• address-family ipv6 unicast

5. maximum-paths eibgp number
6. end
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

Enters router configuration mode to create or configure a
Border Gateway Protocol (BGP) routing process.

Device(config)# router bgp 64496

Step 4

Enter one of the following:
• address-family ipv4 unicast

IP Routing: BGP Configuration Guide
1056

Enters IPv4 or IPv6 address family configuration mode.


eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)
Configuration Examples for eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)

Command or Action

Purpose

• address-family ipv6 unicast
Example:
Device(config-router)# address-family ipv4 unicast
Device(config-router)# address-family ipv6 unicast

Step 5

maximum-paths eibgp number
Example:

Forwards packets over multiple external BGP (eBGP) and
internal BGP (iBGP) paths.

Device(config-router-af)# maximum-paths eibgp 3

Step 6

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuration Examples for eiBGP Multipath for Non-VRF
Interfaces (IPv4/IPv6)
Example: Enabling IPv4/IPv6 Multipaths in Non-VRF Interfaces
The following example shows how to enable IPv4 multipaths on non-VRF interfaces.
Device> enable
Device# configure terminal
Device(config)# router bgp 64496
Device(config-router)# address-family ipv4 unicast
Device(config-router-af)# maximum-paths eibgp 4
Device(config-router-af)# end

The following example shows how to enable IPv6 multipaths on non-VRF interfaces.
Device> enable
Device# configure terminal
Device(config)# router bgp 64497
Device(config-router)# address-family ipv6 unicast
Device(config-router-af)# maximum-paths eibgp 4
Device(config-router-af)# end

Feature Information for eiBGP Multipath for Non-VRF Interfaces
(IPv4/IPv6)
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.

IP Routing: BGP Configuration Guide
1057


eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)
Feature Information for eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)

Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 94: Feature Information for eiBGP Multipath for Non-VRF Interfaces (IPv4/IPv6)

Feature Name
eiBGP Multipath for Non-VRF
Interfaces (IPv4/IPv6)

Releases

Feature Information
The eiBGP Multipath for NonVRF Interfaces (IPv4/IPv6) feature
allows you to configure multipath
load sharing among native IPv4 and
IPv6 external Border Gateway
Protocol (eBGP) and internal BGP
(iBGP) paths for improved load
balancing in deployments.
The following command was
modified: maximum-paths eibgp.

IP Routing: BGP Configuration Guide
1058
