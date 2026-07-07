---
title: "OSPFv3 ABR Type 3 LSA Filtering"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-abr-type-3-lsa-filtering
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 50 OSPFv3 ABR Type 3 LSA Filtering This feature extends the ability of an Area Border Router (ABR) that is running the Open Shortest Path First version 3 (OSPFv3) protocol to filter type 3 link-state advertisements (LSAs) that are sent between different OSPFv3 areas. This feature allows only packets with specified prefixes to be sent from one area to another area and restricts all packet"
---

# OSPFv3 ABR Type 3 LSA Filtering

CHAPTER

50

OSPFv3 ABR Type 3 LSA Filtering
This feature extends the ability of an Area Border Router (ABR) that is running the Open Shortest Path First
version 3 (OSPFv3) protocol to filter type 3 link-state advertisements (LSAs) that are sent between different
OSPFv3 areas. This feature allows only packets with specified prefixes to be sent from one area to another
area and restricts all packets with other prefixes. This type of area filtering can be applied out of a specific
OSPFv3 area, into a specific OSPFv3 area, or into and out of the same OSPFv3 areas at the same time.
• Finding Feature Information, page 477
• OSPFv3 ABR Type 3 LSA Filtering , page 477
• Information About OSPFv3 ABR Type 3 LSA Filtering, page 478
• How to Configure OSPFv3 ABR Type 3 LSA Filtering, page 478
• Configuration Examples for OSPFv3 ABR Type 3 LSA Filtering, page 479
• Additional References for OSPFv3 ABR Type 3 LSA Filtering , page 480
• Feature Information for OSPFv3 ABR Type 3 LSA Filtering, page 481

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

OSPFv3 ABR Type 3 LSA Filtering
Only type 3 LSAs that originate from an ABR are filtered.

IP Routing: OSPF Configuration Guide
477


OSPFv3 ABR Type 3 LSA Filtering
Information About OSPFv3 ABR Type 3 LSA Filtering

Information About OSPFv3 ABR Type 3 LSA Filtering
Area Filter Support
OSPFv3 area filters allow the filtering of inter-area prefix LSAs on the ABRs. The filter, based on IPv6 prefix
lists, can be applied in both directions. In the “in” direction, it filters out the LSAs coming from all other areas
when sending the inter-area prefix LSAs into the specified area. In the “out” direction, it filters out the inter-area
prefix LSAs generated for the specified area.
The Area Filter Support feature gives the administrator improved control of route distribution between OSPFv3
areas.

How to Configure OSPFv3 ABR Type 3 LSA Filtering
Configuring Area Filter Support for OSPFv3
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 process-id
4. area area-id filter-list prefix prefix-list-name {in | out}
5. end
6. ipv6 prefix-list list-name [seq seq-number] {deny ipv6-prefix/prefix-length | permit
ipv6-prefix/prefix-length | description text} [ge ge-value] [le le-value]

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

IP Routing: OSPF Configuration Guide
478

Enters global configuration mode.


OSPFv3 ABR Type 3 LSA Filtering
Configuration Examples for OSPFv3 ABR Type 3 LSA Filtering

Step 3

Command or Action

Purpose

router ospfv3 process-id

Configures the router to run an OSPFv3 process.

Example:
Device(config)# router ospfv3 1

Step 4

area area-id filter-list prefix prefix-list-name {in | out}

Configures the router to filter interarea routes out
of the specified area.

Example:
Device(config-router)# area 1 filter-list prefix
test_ipv6 out

Step 5

Returns to global configuration mode.

end
Example:
Device(config-router)# end

Step 6

ipv6 prefix-list list-name [seq seq-number] {deny
ipv6-prefix/prefix-length | permit ipv6-prefix/prefix-length |
description text} [ge ge-value] [le le-value]

Creates a prefix list with the name specified for the
list-name argument.

Example:
Device(config)# ipv6 prefix-list test_ipv6 seq 5
permit 2011::1/128

Configuration Examples for OSPFv3 ABR Type 3 LSA Filtering
Example: Area Filter Support for OSPFv3
The following example shows how to configure Area Filter Support for OSPFv3:
router ospfv3 1
!
address-family ipv4 unicast
area 2 filter-list prefix test_ipv4 in
exit-address-family
!
address-family ipv6 unicast
area 2 filter-list prefix test_ipv6 in
exit-address-family
!
ip prefix-list test_ipv4 seq 5 permit 2.2.2.2/32
!
!
ipv6 prefix-list test_ipv6 seq 5 deny 2011::1/128

IP Routing: OSPF Configuration Guide
479


OSPFv3 ABR Type 3 LSA Filtering
Additional References for OSPFv3 ABR Type 3 LSA Filtering

Additional References for OSPFv3 ABR Type 3 LSA Filtering
Related Documents
Related Topic

Document Title

Configuring OSPF

“Configuring OSPF”

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standard

Title

No new or modified standards are supported and
—
support for existing standards has not been modified.

RFCs
RFC

Title

No new or modified RFCs are supported and support —
for existing RFCs has not been modified.

Technical Assistance
Description

Link

The Cisco Support and Documentation website
http://www.cisco.com/cisco/web/support/index.html
provides online resources to download documentation,
software, and tools. Use these resources to install and
configure the software and to troubleshoot and resolve
technical issues with Cisco products and technologies.
Access to most tools on the Cisco Support and
Documentation website requires a Cisco.com user ID
and password.

IP Routing: OSPF Configuration Guide
480


OSPFv3 ABR Type 3 LSA Filtering
Feature Information for OSPFv3 ABR Type 3 LSA Filtering

Feature Information for OSPFv3 ABR Type 3 LSA Filtering
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 56: Feature Information for OSPFv3 ABR Type 3 LSA Filtering

Feature Name

Releases

Feature Information

OSPFv3 ABR Type 3 LSA
Filtering

Cisco IOS XE Release 3.8

The OSPFv3 ABR Type 3 LSA
Filtering feature extends the ability
of an ABR that is running the
OSPFv3 protocol to filter type 3
LSAs that are sent between
different OSPFv3 areas. This
feature allows only packets with
specified prefixes to be sent from
one area to another area and
restricts all packets with other
prefixes. This type of area filtering
can be applied out of a specific
OSPFv3 area, into a specific
OSPFv3 area, or into and out of the
same OSPFv3 areas at the same
time.

15.3(1)S
15.2(1)E

IP Routing: OSPF Configuration Guide
481


OSPFv3 ABR Type 3 LSA Filtering
Feature Information for OSPFv3 ABR Type 3 LSA Filtering

IP Routing: OSPF Configuration Guide
482
