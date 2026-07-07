---
title: "OSPFv3 MIB"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-mib
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 47 OSPFv3 MIB The OSPFv3 MIB feature enables remote monitoring and troubleshooting of Open Shortest Path First version 3 (OSPFv3) processes using standard Simple Network Management Protocol (SNMP) management workstations. The protocol information collected by the OSPFv3 MIB objects and trap objects can be used to derive statistics that helps monitor and improve overall network performanc"
---

# OSPFv3 MIB

CHAPTER

47

OSPFv3 MIB
The OSPFv3 MIB feature enables remote monitoring and troubleshooting of Open Shortest Path First version
3 (OSPFv3) processes using standard Simple Network Management Protocol (SNMP) management
workstations. The protocol information collected by the OSPFv3 MIB objects and trap objects can be used
to derive statistics that helps monitor and improve overall network performance.
• Finding Feature Information, page 447
• Prerequisites for OSPFv3 MIB , page 447
• Restrictions for OSPFv3 MIB Support, page 448
• Information About OSPFv3 MIB, page 448
• How to Configure OSPFv3 MIB, page 448
• Configuration Examples for OSPFv3 MIB, page 451
• Additional References for OSPFv3 MIB, page 451
• Feature Information for OSPFv3 MIB , page 452

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for OSPFv3 MIB
• Ensure that Open Shortest Path First version 3 (OSPFv3) is configured on the device.
• Ensure that Simple Network Management Protocol (SNMP) is enabled on the device before notifications
(traps) can be configured or before SNMP GET operations can be performed.

IP Routing: OSPF Configuration Guide
447


OSPFv3 MIB
Restrictions for OSPFv3 MIB Support

Restrictions for OSPFv3 MIB Support
• To monitor multiple Open Shortest Path First version 3 (OSPFv3) processes, each process must be
associated with a Simple Network Management Protocol (SNMP) context.
• To monitor multiple VRFs, each VRF must be associated with an SNMP context.

Information About OSPFv3 MIB
OSPFv3 MIB
Open Shortest Path First version 3 (OSPFv3) is the IPv6 implementation of OSPF. The OSPFv3 MIB is
documented in RFC 5643 and defines a MIB for managing OSPFv3 processes through Simple Network
Management Protocol (SNMP).
Users can constantly monitor the changing state of an OSPF network by using MIB objects. The MIB objects
gather information relating to protocol parameters and trap notification objects that can signal the occurrence
of significant network events such as transition state changes.

OSPFv3 TRAP MIB
The ospfv3Notifications MIB object contains the OSPFv3 trap MIB objects that enable and disable OSPF
traps in the Cisco IOS CLI. These OSPFv3 trap MIB objects are provided by the RFC 5643 standard OSPFv3
MIB.

How to Configure OSPFv3 MIB
Enabling Specific OSPFv3 Traps
SUMMARY STEPS
1. enable
2. configure terminal
3. snmp-serverhost {hostname | ip-address} [vrf vrf-name] [traps | informs] [version {1 | 2c | 3 [auth |
noauth | priv]}] community-string [udp-port port] [notification-type]
4. snmp-server enable traps ospfv3 errors [bad-packet] [config-error] [virt-bad-packet]
[virt-config-error]
5. snmp-server enable traps ospfv3 rate-limit seconds trap-number
6. snmp-server enable traps ospfv3 state-change [if-state-change] [neighbor-restart-helper-status-change]
[neighbor-state-change] [nssa-translator-status-change] [restart-status-change] [virtif-state-change]
[virtneighbor-restart-helper-status-change] [virtneighbor-state-change]
7. end

IP Routing: OSPF Configuration Guide
448


OSPFv3 MIB
Enabling Specific OSPFv3 Traps

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

snmp-serverhost {hostname | ip-address} [vrf vrf-name] Specifies a recipient (target host) for Simple Network
[traps | informs] [version {1 | 2c | 3 [auth | noauth | priv]}] Management Protocol (SNMP) notification operations.
community-string [udp-port port] [notification-type]
• If the notification-type is not specified, all enabled
notifications (traps or informs) are sent to the
Example:
specified host.
Device(config)# snmp-server host 172.20.2.162
version 2c public ospfv3

Step 4

snmp-server enable traps ospfv3 errors [bad-packet]
[config-error] [virt-bad-packet] [virt-config-error]

• If you want to send only the Open Shortest Path First
version 3 (OSPFv3) notifications to the specified
host, you can use the optional ospfv3 keyword as
the notification-types . Entering the ospfv3 keyword
enables the ospfv3Notifications MIB object.
Enables SNMP notifications for OSPFv3 errors.

Example:
Device(config)# snmp-server enable traps ospfv3
errors

Step 5

snmp-server enable traps ospfv3 rate-limit seconds
trap-number

Sets the rate limit for the number of SNMP OSPFv3
notifications that are sent in each OSPFv3 SNMP
notification rate-limit window.

Example:
Device(config)# snmp-server enable traps ospfv3
rate-limit 20 20

Step 6

snmp-server enable traps ospfv3 state-change
Enables SNMP OSPFv3 notifications for OSPFv3
[if-state-change] [neighbor-restart-helper-status-change] transition state changes.
[neighbor-state-change] [nssa-translator-status-change]
[restart-status-change] [virtif-state-change]
[virtneighbor-restart-helper-status-change]
[virtneighbor-state-change]

IP Routing: OSPF Configuration Guide
449


OSPFv3 MIB
Verifying OSPFv3 MIB Traps on the Device

Command or Action

Purpose

Example:
Device(config)# snmp-server enable traps ospfv3
state-change

Step 7

Exits global configuration mode and enters privileged
EXEC mode.

end
Example:
Device(config)# end

Verifying OSPFv3 MIB Traps on the Device
SUMMARY STEPS
1. enable
2. show running-config [options]

DETAILED STEPS
Step 1

enable
Example:
Device> enable

Enables privileged EXEC mode.
• Enter your password if prompted.
Step 2

show running-config [options]
Example:
Device# show running-config | include traps

Displays the contents of the currently running configuration file and includes information about enabled traps.
• Verifies which traps are enabled.

IP Routing: OSPF Configuration Guide
450


OSPFv3 MIB
Configuration Examples for OSPFv3 MIB

Configuration Examples for OSPFv3 MIB
Example: Enabling and Verifying OSPFv3 MIB Traps
The following example shows how to enable all OSPFv3 error traps:
Device> enable
Device# configure terminal
Device(config)# snmp-server enable traps ospfv3 errors
Device(config)# end

The following example shows how to verify that the traps are enabled:
Device> enable
Device# show running-config | include traps
snmp-server enable traps ospfv3 errors

Additional References for OSPFv3 MIB
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

OSPF configuration tasks

“Configuring OSPF” module in IP Routing: OSPF
Configuration Guide

Standards and RFCs
Standard

Title

RFC 5643

Management Information Base for OSPFv3

MIBs
MIB

MIBs Link

OSPFv3-MIB

To locate and download MIBs for selected platforms,
Cisco IOS releases, and feature sets, use Cisco MIB
Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: OSPF Configuration Guide
451


OSPFv3 MIB
Feature Information for OSPFv3 MIB

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

Feature Information for OSPFv3 MIB
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 53: Feature Information for OSPFv3 MIB

Feature Name

Releases

Feature Information

OSPFv3 MIB

Cisco IOS XE Release 3.7S

The OSPFv3 MIB feature enables
remote monitoring and
troubleshooting of OSPFv3
processes using standard SNMP
management workstations.
The following commands were
introduced or modified:
snmp-server host, snmp-server
enable traps ospfv3 errors,
snmp-server enable traps ospfv3
rate-limit, snmp-server enable
traps ospfv3 state-change.

IP Routing: OSPF Configuration Guide
452
