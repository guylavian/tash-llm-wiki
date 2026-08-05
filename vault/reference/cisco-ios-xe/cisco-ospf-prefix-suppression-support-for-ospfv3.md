---
title: "Prefix Suppression Support for OSPFv3"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-prefix-suppression-support-for-ospfv3
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 48 Prefix Suppression Support for OSPFv3 This feature enables Open Shortest Path First version 3 (OSPFv3) to hide the IPv4 and IPv6 prefixes of connected networks from link-state advertisements (LSAs). When OSPFv3 is deployed in large networks, limiting the number of IPv4 and IPv6 prefixes that are carried in the OSPFv3 LSAs can speed up OSPFv3 convergence. This feature can also be utili"
---

# Prefix Suppression Support for OSPFv3

CHAPTER

48

Prefix Suppression Support for OSPFv3
This feature enables Open Shortest Path First version 3 (OSPFv3) to hide the IPv4 and IPv6 prefixes of
connected networks from link-state advertisements (LSAs). When OSPFv3 is deployed in large networks,
limiting the number of IPv4 and IPv6 prefixes that are carried in the OSPFv3 LSAs can speed up OSPFv3
convergence.
This feature can also be utilized to enhance the security of an OSPFv3 network by allowing the network
administrator to prevent IP routing toward internal nodes.
• Finding Feature Information, page 453
• Prerequisites for Prefix Suppression Support for OSPFv3, page 453
• Information About Prefix Suppression Support for OSPFv3, page 454
• How to Configure Prefix Suppression Support for OSPFv3, page 455
• Configuration Examples for Prefix Suppression Support for OSPFv3, page 460
• Additional References for Prefix Suppression Support for OSPFv3, page 460
• Feature Information for Prefix Suppression Support for OSPFv3, page 461

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for Prefix Suppression Support for OSPFv3
Before you can use the mechanism to exclude IPv4 and IPv6 prefixes from LSAs, the OSPFv3 routing protocol
must be configured.

IP Routing: OSPF Configuration Guide
453


Prefix Suppression Support for OSPFv3
Information About Prefix Suppression Support for OSPFv3

Information About Prefix Suppression Support for OSPFv3
OSPFv3 Prefix Suppression Support
The OSPFv3 Prefix Suppression Support feature allows you to hide IPv4 and IPv6 prefixes that are configured
on interfaces running OSPFv3.
In OSPFv3, addressing semantics have been removed from the OSPF protocol packets and the main LSA
types, leaving a network-protocol-independent core. This means that Router-LSAs and network-LSAs no
longer contain network addresses, but simply express topology information. The process of hiding prefixes
is simpler in OSPFv3 and suppressed prefixes are simply removed from the intra-area-prefix-LSA. Prefixes
are also propagated in OSPFv3 via link LSAs
The OSPFv3 Prefix Suppression feature provides a number of benefits.The exclusion of certain prefixes from
adverstisements means that there is more memory available for LSA storage, bandwidth and buffers for LSA
flooding, and CPU cycles for origination and flooding of LSAs and for SPF computation. Prefixes are also
filtered from link LSAs. A device only filters locally configured prefixes, not prefixes learnt via link LSAs.
In addition, security has been improved by reducing the possiblity of remote attack with the hiding of
transit-only networks.

Globally Suppress IPv4 and IPv6 Prefix Advertisements by Configuring the
OSPFv3 Process
You can reduce OSPFv3 convergence time by configuring the OSPFv3 process on a device to prevent the
advertisement of all IPv4 and IPv6 prefixes by using the prefix-suppression command in router configuration
mode or address-family configuration mode.

Note

Prefixes that are associated with loopbacks, secondary IP addresses, and passive interfaces are not
suppressed by the router mode or the address-family configuration commands because typical network
designs require prefixes to remain reachable.

Suppress IPv4 and IPv6 Prefix Advertisements on a Per-Interface Basis
You can explicitly configure an OSPFv3 interface not to advertise its IP network to its neighbors by using
the ipv6 ospf prefix-suppression command or the ospfv3 prefix-suppression command in interface
configuration mode.

Note

If you have globally suppressed IPv4 and IPv6 prefixes from connected IP networks by configuring the
prefix-suppression router configuration command, the interface configuration command takes precedence
over the router configuration command.

IP Routing: OSPF Configuration Guide
454


Prefix Suppression Support for OSPFv3
How to Configure Prefix Suppression Support for OSPFv3

How to Configure Prefix Suppression Support for OSPFv3
Configuring Prefix Suppression Support of the OSPFv3 Process
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 process-id
4. prefix-suppression

[vrf vpn-name]

5. end
6. show ospfv3

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

router ospfv3 process-id

[vrf vpn-name]

Configures an OSPFv3 routing process and enters router
configuration mode.

Example:
Device(config)# router ospfv3 23

Step 4

prefix-suppression
Example:

Prevents OSPFv3 from advertising all IPv4 and IPv6 prefixes,
except prefixes that are associated with loopbacks, secondary IP
addresses, and passive interfaces.

Device(config-router)# prefix-suppression

Step 5

end

Returns to privileged EXEC mode.

Example:
Device(config-router)# end

Step 6

show ospfv3

Displays general information about OSPFv3 routing processes.

IP Routing: OSPF Configuration Guide
455


Prefix Suppression Support for OSPFv3
Configuring Prefix Suppression Support of the OSPFv3 Process in Address-Family Configuration Mode

Command or Action

Purpose
Note

Example:

Use this command to verify that IPv4 and IPv6 prefix
suppression has been enabled.

Device# show ospfv3

Configuring Prefix Suppression Support of the OSPFv3 Process in
Address-Family Configuration Mode
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 process-id [vrf vpn-name]
4. address-family ipv6 unicast
5. prefix-suppression
6. end
7. show ospfv3

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.
• Enter your password if prompted.

Example:
Device> enable

Step 2

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

router ospfv3 process-id

[vrf vpn-name]

Example:
Device(config)# router ospfv3 23

IP Routing: OSPF Configuration Guide
456

Configures an OSPFv3 routing process and enters router
configuration mode.


Prefix Suppression Support for OSPFv3
Configuring Prefix Suppression Support on a Per-Interface Basis

Step 4

Command or Action

Purpose

address-family ipv6 unicast

Enters IPv6 address family configuration mode for OSPFv3.

Example:
Device(config-router)# address-family ipv6
unicast

Step 5

prefix-suppression
Example:

Prevents OSPFv3 from advertising all IPv4 and IPv6 prefixes,
except prefixes that are associated with loopbacks, secondary
IP addresses, and passive interfaces.

Device(config-router-af)# prefix-suppression

Step 6

Returns to privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Step 7

Displays general information about OSPFv3 routing processes.

show ospfv3

Note

Example:

Use this command to verify that IPv4 and IPv6 prefix
suppression has been enabled.

Device# show ospfv3

Configuring Prefix Suppression Support on a Per-Interface Basis
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. Do one of the following:
• ipv6 ospf prefix-suppression [disable]
• ospfv3 prefix-suppression disable
5. end
6. show ospfv3 interface

IP Routing: OSPF Configuration Guide
457


Prefix Suppression Support for OSPFv3
Configuring Prefix Suppression Support on a Per-Interface Basis

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

Configures an interface type and enters interface configuration
mode.

Example:
Device(config)# interface serial 0/0

Step 4

Do one of the following:
• ipv6 ospf prefix-suppression [disable]
• ospfv3 prefix-suppression disable

Example:

Prevents OSPFv3 from advertising IPv4 and IPv6 prefixes that
belong to a specific interface, except those that are associated with
secondary IP addresses.
• When you enter the ipv6 ospf prefix-suppression command
or the ospfv3 prefix-suppression command in interface
configuration mode, it takes precedence over the
prefix-suppression command that is entered in router
configuration mode.

Device(config-if)# ipv6 ospf
prefix-suppression

Example:
Device(config-if)# ospfv3 1
prefix-suppression disable

Step 5

end

Returns to privileged EXEC mode.

Example:
Device(config-if)# end

Step 6

show ospfv3 interface

Displays OSPFv3-related interface information.
Note

Example:
Device# show ospfv3 interface

IP Routing: OSPF Configuration Guide
458

Use this command to verify that IPv4 and IPv6 prefix
suppression has been enabled for a specific interface.


Prefix Suppression Support for OSPFv3
Troubleshooting IPv4 and IPv6 Prefix Suppression

Troubleshooting IPv4 and IPv6 Prefix Suppression
SUMMARY STEPS
1. enable
2. debug ospfv3 lsa-generation
3. debug condition interface interface-type interface-number [dlci dlci] [vc {vci | vpi | vci}]
4. show debugging
5. show logging [slot slot-number | summary]

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

debug ospfv3 lsa-generation

Displays informations about each OSPFv3 LSA that is
generated.

Example:
Device# debug ospfv3 lsa-generation

Step 3

debug condition interface interface-type
interface-number [dlci dlci] [vc {vci | vpi | vci}]

Limits output for some debug commands on the basis of
the interface or virtual circuit.

Example:
Device# debug condition interface serial 0/0

Step 4

show debugging

Displays information about the types of debugging that are
enabled for your device.

Example:
Device# show debugging

Step 5

show logging [slot slot-number | summary]

Displays the state of syslog and the contents of the standard
system logging buffer.

Example:
Device# show logging

IP Routing: OSPF Configuration Guide
459


Prefix Suppression Support for OSPFv3
Configuration Examples for Prefix Suppression Support for OSPFv3

Configuration Examples for Prefix Suppression Support for
OSPFv3
Example: Configuring Prefix Suppression Support for OSPFv3
The following example shows how to configure prefix suppression support for OSPFv3 in router configuration
mode:
router ospfv3 1
prefix-suppression
!
address-family ipv6 unicast
router-id 0.0.0.6
exit-address-family

The following example shows how to configure prefix suppression support for OSPFv3 in address-family
configuration mode:
router ospfv3 1
!
address-family ipv6 unicast
router-id 10.0.0.6
prefix-suppression
exit-address-family

The following example shows how to configure prefix suppression support for OSPFv3 in interface
configuration mode:
interface Ethernet0/0
ip address 10.0.0.1 255.255.255.0
ipv6 address 2001:201::201/64
ipv6 enable
ospfv3 prefix-suppression
ospfv3 1 ipv4 area 0
ospfv3 1 ipv6 area 0
end

Additional References for Prefix Suppression Support for
OSPFv3
Related Documents
Related Topic

Document Title

Configuring OSPF

“Configuring OSPF”

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Cisco IOS commands

Cisco IOS Master Command List, All Releases

IP Routing: OSPF Configuration Guide
460


Prefix Suppression Support for OSPFv3
Feature Information for Prefix Suppression Support for OSPFv3

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

Feature Information for Prefix Suppression Support for OSPFv3
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 54: Feature Information for Prefix Suppression Support for OSPFv3

Feature Name

Releases

Feature Information

Prefix Suppression Support for
OSPFv3

Cisco IOS XE Release 3.8S

This feature enables Open Shortest
Path First version 3 (OSPFv3) to
hide the IPv4 and IPv6 prefixes of
connected networks from link-state
advertisements (LSAs).
This feature can also be used to
enhance the security of an OSPFv3
network by allowing the network
administrator to prevent IP routing
toward internal nodes.
The following commands were
introduced or modified:
• ipv6 ospf
prefix-suppression
• ospfv3 prefix-suppression
• prefix-suppression
(OSPFv3)

IP Routing: OSPF Configuration Guide
461


Prefix Suppression Support for OSPFv3
Feature Information for Prefix Suppression Support for OSPFv3

IP Routing: OSPF Configuration Guide
462
