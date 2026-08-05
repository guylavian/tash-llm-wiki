---
title: "OSPFv3 Demand Circuit Ignore"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-demand-circuit-ignore
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 51 OSPFv3 Demand Circuit Ignore This feature enables you to prevent an interface from accepting demand-circuit requests from other devices by specifying the ignore keyword in the ipv6 ospf demand-circuit command. • Finding Feature Information, page 483 • Information About OSPFv3 Demand Circuit Ignore, page 483 • How to Configure OSPFv3 Demand Circuit Ignore, page 484 • Configuration Exam"
---

# OSPFv3 Demand Circuit Ignore

CHAPTER

51

OSPFv3 Demand Circuit Ignore
This feature enables you to prevent an interface from accepting demand-circuit requests from other devices
by specifying the ignore keyword in the ipv6 ospf demand-circuit command.
• Finding Feature Information, page 483
• Information About OSPFv3 Demand Circuit Ignore, page 483
• How to Configure OSPFv3 Demand Circuit Ignore, page 484
• Configuration Examples for OSPFv3 Demand Circuit Ignore, page 485
• Additional References for OSPFv3 Demand Circuit Ignore, page 485
• Feature Information for OSPFv3 Demand Circuit Ignore, page 486

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About OSPFv3 Demand Circuit Ignore
Demand Circuit Ignore Support
Demand Circuit Ignore Support enables you to prevent an interface from accepting demand-circuit requests
from other devices by specifying the ignore keyword in the ipv6 ospf demand-circuit command. Demand
circuit ignore instructs the router not to accept Demand Circuit (DC) negotiation and is a useful configuration
option on the point-to-multipoint interface of the Hub router.

IP Routing: OSPF Configuration Guide
483


OSPFv3 Demand Circuit Ignore
How to Configure OSPFv3 Demand Circuit Ignore

How to Configure OSPFv3 Demand Circuit Ignore
Configuring Demand Circuit Ignore Support for OSPFv3
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. Enter one of the following commands:
• ipv6 ospf demand-circuit ignore
• ospfv3 demand-circuit ignore
5. end
6. show ospfv3 process-id [ area-id ] [ address-family ] [vrf {vrf-name |* }] interface [type number]
[brief]

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

interface type number

Configures an interface type and number and enters
interface configuration mode.

Example:
Device(config)# interface GigabitEthernet 0/1/0

Step 4

Enter one of the following commands:
• ipv6 ospf demand-circuit ignore
• ospfv3 demand-circuit ignore

IP Routing: OSPF Configuration Guide
484

Prevents an interface from accepting demand-circuit
requests from other devices.


OSPFv3 Demand Circuit Ignore
Configuration Examples for OSPFv3 Demand Circuit Ignore

Command or Action

Purpose

Example:
Device(config-if)# ipv6 ospf demand-circuit ignore

Example:
Device(config-if)# ospfv3 demand-circuit ignore

Step 5

Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Step 6

show ospfv3 process-id [ area-id ] [ address-family ] [vrf (Optional) Displays OSPFv3-related interface
information.
{vrf-name |* }] interface [type number] [brief]
Example:
Device# show ospfv3 interface GigabitEthernet 0/1/0

Configuration Examples for OSPFv3 Demand Circuit Ignore
Example: Demand Circuit Ignore Support for OSPFv3
The following example shows how to configure demand circuit ignore support for OSPFv3:
interface Serial0/0
ip address 6.1.1.1 255.255.255.0
ipv6 enable
ospfv3 network point-to-multipoint
ospfv3 demand-circuit ignore
ospfv3 1 ipv6 area 0

Additional References for OSPFv3 Demand Circuit Ignore
The following sections provide references related to the OSPFv3 Demand Circuit Ignore feature.
Related Documents
Related Topic

Document Title

OSPF configuration tasks

“Configuring OSPF”

IP Routing: OSPF Configuration Guide
485


OSPFv3 Demand Circuit Ignore
Feature Information for OSPFv3 Demand Circuit Ignore

Related Topic

Document Title

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS commands

Cisco IOS Master Command List, All Releases

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

Feature Information for OSPFv3 Demand Circuit Ignore
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 57: Feature Information for OSPFv3 Demand Circuit Ignore

Feature Name

Releases

Feature Information

OSPFv3 Demand Circuit Ignore

Cisco IOS XE Release 3.8

The OSPFv3 Demand Circuit
Ignore feature enables you to
prevent an interface from accepting
demand-circuit requests from other
devices by specifying the ignore
keyword in the ipv6 ospf
demand-circuit command.
The following commands were
introduced or modified:
• ipv6 ospf demand-circuit
• ospfv3 demand-circuit

IP Routing: OSPF Configuration Guide
486
