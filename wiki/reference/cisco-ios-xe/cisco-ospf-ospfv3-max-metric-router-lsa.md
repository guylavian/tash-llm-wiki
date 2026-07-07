---
title: "OSPFv3 Max-Metric Router LSA"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-max-metric-router-lsa
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 29 OSPFv3 Max-Metric Router LSA The Open Shortest Path First version 3 (OSPFv3) max-metric router link-state advertisement (LSA) feature enables OSPFv3 to advertise its locally generated router LSAs with a maximum metric. The feature allows OSPFv3 processes to converge but not attract transit traffic through the device if there are better alternate paths. • Finding Feature Information, p"
---

# OSPFv3 Max-Metric Router LSA

CHAPTER

29

OSPFv3 Max-Metric Router LSA
The Open Shortest Path First version 3 (OSPFv3) max-metric router link-state advertisement (LSA) feature
enables OSPFv3 to advertise its locally generated router LSAs with a maximum metric. The feature allows
OSPFv3 processes to converge but not attract transit traffic through the device if there are better alternate
paths.
• Finding Feature Information, page 279
• Information About OSPFv3 Max-Metric Router LSA, page 279
• How to Configure OSPFv3 Max-Metric Router LSA, page 280
• Configuration Examples for OSPFv3 Max-Metric Router LSA, page 281
• Additional References for OSPF Nonstop Routing, page 282
• Feature Information for OSPFv3 Max-Metric Router LSA, page 282

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPFv3 Max-Metric Router LSA
OSPFv3 Max-Metric Router LSA
The OSPFv3 max-metric router LSA feature enables OSPFv3 to advertise its locally generated router LSAs
with a maximum metric. The feature allows OSPFv3 processes to converge but not attract transit traffic through

IP Routing: OSPF Configuration Guide
279


OSPFv3 Max-Metric Router LSA
How to Configure OSPFv3 Max-Metric Router LSA

the device if there are better alternate paths. After a specified timeout or a notification from Border Gateway
Protocol (BGP), OSPFv3 advertises the LSAs with normal metrics.
The max-metric LSA control places the OSPFv3 router into the stub router role using its LSA advertisement.
A stub router only forwards packets destined to go to its directly connected links. In OSPFv3 networks, a
device could become a stub router by advertising large metrics for its connected links, so that the cost of a
path through this device becomes larger than that of an alternative path. OSPFv3 stub router advertisement
allows a device to advertise the infinity metric (0xFFFF) for its connected links in router LSAs and advertise
the normal interface cost if the link is a stub network.

How to Configure OSPFv3 Max-Metric Router LSA
Configuring the OSPFv3 Max-Metric Router LSA
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 process-id
4. address-family ipv6 unicast
5. max-metric router-lsa [external-lsa [max-metric-value]] [include-stub] [inter-area-lsas
[max-metric-value]] [on-startup {seconds | wait-for-bgp}] [prefix-lsa] [stub-prefix-lsa
[max-metric-value]] [summary-lsa [max-metric-value]]
6. end
7. show ospfv3 [process-id] max-metric

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

router ospfv3 process-id
Example:
Device(config)# router ospfv3 1

IP Routing: OSPF Configuration Guide
280

Enables OSPFv3 router configuration mode.


OSPFv3 Max-Metric Router LSA
Configuration Examples for OSPFv3 Max-Metric Router LSA

Step 4

Command or Action

Purpose

address-family ipv6 unicast

Configures an instance of the OSPFv3 process in the
IPv6 address family.

Example:
Device(config)# address-family ipv6 unicast

Step 5

max-metric router-lsa [external-lsa [max-metric-value]] Configures a device that is running the OSPFv3 protocol
to advertise a maximum metric so that other devices do
[include-stub] [inter-area-lsas [max-metric-value]]
not prefer the device as an intermediate hop in their SPF
[on-startup {seconds | wait-for-bgp}] [prefix-lsa]
calculations.
[stub-prefix-lsa [max-metric-value]] [summary-lsa
[max-metric-value]]
Example:
Device(config-router-af)# max-metric router-lsa
on-startup wait-for-bgp

Step 6

Exits address family configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Step 7

show ospfv3 [process-id] max-metric

Displays OSPFv3 maximum metric origination
information.

Example:
Device# show ospfv3 1 max-metric

Configuration Examples for OSPFv3 Max-Metric Router LSA
Example: Verifying the OSPFv3 Max-Metric Router LSA
Router# show ipv6 ospf max-metric
OSPFv3 Router with ID (192.1.1.1) (Process ID 1)
Start time: 00:00:05.886, Time elapsed: 3d02h
Originating router-LSAs with maximum metric
Condition: always, State: active

IP Routing: OSPF Configuration Guide
281


OSPFv3 Max-Metric Router LSA
Additional References for OSPF Nonstop Routing

Additional References for OSPF Nonstop Routing
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Configuring IETF NSF or Cisco NSF

“Configuring NSF-OSPF” module in the Cisco IOS
High Availability Configuration Guide

Standard and RFCs
Standard/RFC

Title

RFC 2328

OSPF Version 2

RFC 3623

Graceful OSPF Restart

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

Feature Information for OSPFv3 Max-Metric Router LSA
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: OSPF Configuration Guide
282


OSPFv3 Max-Metric Router LSA
Feature Information for OSPFv3 Max-Metric Router LSA

Table 32: Feature Information for OSPFv3 Max-Metric Router LSA

Feature Name

Releases

Feature Information

OSPFv3 Max-Metric Router LSA Cisco IOS XE Release 3.4S

The OSPFv3 max-metric router
LSA feature enables OSPF to
advertise its locally generated
router LSAs with a maximum
metric.
The following commands were
introduced or modified:
max-metric router-lsa, show ipv6
ospf max-metric, show ospfv3
max-metric.

IP Routing: OSPF Configuration Guide
283


OSPFv3 Max-Metric Router LSA
Feature Information for OSPFv3 Max-Metric Router LSA

IP Routing: OSPF Configuration Guide
284
