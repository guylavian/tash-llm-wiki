---
title: "Graceful Shutdown Support for OSPFv3"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-graceful-shutdown-support-for-ospfv3
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 8 Graceful Shutdown Support for OSPFv3 This feature provides the ability to temporarily shut down an Open Shortest Path First version 3 (OSPFv3) process or interface in the least disruptive manner, and to notify its neighbors that it is going away. A graceful shutdown of a protocol can be initiated on all OSPFv3 interfaces or on a specific interface. • Finding Feature Information, page 1"
---

# Graceful Shutdown Support for OSPFv3

CHAPTER

8

Graceful Shutdown Support for OSPFv3
This feature provides the ability to temporarily shut down an Open Shortest Path First version 3 (OSPFv3)
process or interface in the least disruptive manner, and to notify its neighbors that it is going away. A graceful
shutdown of a protocol can be initiated on all OSPFv3 interfaces or on a specific interface.
• Finding Feature Information, page 103
• Information About Graceful Shutdown Support for OSPFv3, page 103
• How to Configure Graceful Shutdown Support for OSPFv3, page 104
• Configuration Examples for Graceful Shutdown Support for OSPFv3, page 108
• Additional References for Graceful Shutdown Support for OSPFv3, page 109
• Feature Information for Graceful Shutdown Support for OSPFv3, page 110

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About Graceful Shutdown Support for OSPFv3
OSPFv3 Graceful Shutdown
The Graceful Shutdown for OSPFv3 feature provides the ability to temporarily shut down the OSPFv3 protocol
in the least disruptive manner and to notify its neighbors that it is going away. All traffic that has another path
through the network will be directed to that alternate path. A graceful shutdown of the OSPFv3 protocol can
be initiated using the shutdown command in router configuration mode or in address family configuration
mode.

IP Routing: OSPF Configuration Guide
103


Graceful Shutdown Support for OSPFv3
How to Configure Graceful Shutdown Support for OSPFv3

This feature also provides the ability to shut down OSPFv3 on a specific interface. In this case, OSPFv3 will
not advertise the interface or form adjacencies over it; however, all of the OSPFv3 interface configuration
will be retained. To initiate a graceful shutdown of an interface, use the ipv6 ospf shutdown or the ospfv3
shutdown command in interface configuration mode.

How to Configure Graceful Shutdown Support for OSPFv3
Configuring Graceful Shutdown of the OSPFv3 Process
SUMMARY STEPS
1. enable
2. configure terminal
3. Do one of the following:
• ipv6 router ospf process-id
• router ospfv3 process-id
4. shutdown
5. end
6. Do one of the following:
• show ipv6 ospf [process-id]
• show ospfv3 [process-id]

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

Do one of the following:
• ipv6 router ospf process-id
• router ospfv3 process-id

IP Routing: OSPF Configuration Guide
104

Enables OSPFv3 routing and enters router
configuration mode.


Graceful Shutdown Support for OSPFv3
Configuring Graceful Shutdown of the OSPFv3 Process in Address-Family Configuration Mode

Command or Action

Purpose

Example:
Device(config)# ipv6 router ospf 1

Example:
Device(config)# router ospfv3 101

Step 4

shutdown

Shuts down the selected interface.

Example:
Device(config-router)# shutdown

Step 5

Returns to privileged EXEC mode.

end
Example:
Device(config-router)# end

Step 6

Do one of the following:
• show ipv6 ospf [process-id]

(Optional) Displays general information about
OSPFv3 routing processes.

• show ospfv3 [process-id]

Example:
Device# show ipv6 ospf

Example:
Device# show ospfv3

Configuring Graceful Shutdown of the OSPFv3 Process in Address-Family
Configuration Mode
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. address-family ipv6 unicast [vrf vrf-name]
5. shutdown
6. end
7. show ospfv3 [process-id]

IP Routing: OSPF Configuration Guide
105


Graceful Shutdown Support for OSPFv3
Configuring Graceful Shutdown of the OSPFv3 Process in Address-Family Configuration Mode

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

router ospfv3 [process-id]

Enables router configuration mode for the IPv6 address
family.

Example:
Device(config)# router ospfv3 1

Step 4

address-family ipv6 unicast [vrf vrf-name]

Enters IPv6 address family configuration mode for
OSPFv3.

Example:
Device(config-router)#address-family ipv6

Step 5

shutdown

Shuts down the selected interface.

Example:
Device(config-router-af)# shutdown

Step 6

end

Returns to privileged EXEC mode.

Example:
Device(config-router-af)# end

Step 7

show ospfv3 [process-id]
Example:
Device# show ospfv3

IP Routing: OSPF Configuration Guide
106

(Optional) Displays general information about OSPFv3
routing processes.


Graceful Shutdown Support for OSPFv3
Configuring OSPFv3 Graceful Shutdown of the OSPFv3 Interface

Configuring OSPFv3 Graceful Shutdown of the OSPFv3 Interface
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. Do one of the following:
• ipv6 ospf shutdown
• ospfv3 shutdown
5. end
6. show ospfv3 process-id [ area-id ] [ address-family ] [ vrf {vrf-name | * }] interface [type number]
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

Configures an interface type and number and enters interface
configuration mode.

Example:
Device(config)# interface GigabitEthernet

Step 4

Do one of the following:
• ipv6 ospf shutdown
• ospfv3 shutdown

Example:

Initiates an OSPFv3 protocol graceful shutdown at the
interface level.
• When the ipv6 ospf shutdown interface command is
entered, the interface on which it is configured sends a
link-state update advising its neighbors that is going
down, which allows those neighbors to begin routing
OSPFv3 traffic around this device.

Device(config-if)# ipv6 ospf shutdown

IP Routing: OSPF Configuration Guide
107


Graceful Shutdown Support for OSPFv3
Configuration Examples for Graceful Shutdown Support for OSPFv3

Command or Action

Purpose

Example:
Device(config-if)# ospfv3 process-id ipv6
shutdown

Step 5

Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Step 6

show ospfv3 process-id [ area-id ] [ address-family ] (Optional) Displays OSPFv3-related interface information.
[ vrf {vrf-name | * }] interface [type number] [brief]
Example:
Device# show ospfv3 1 interface

Configuration Examples for Graceful Shutdown Support for
OSPFv3
Example: Configuring Graceful Shutdown of the OSPFv3 Process
The following example shows how to configure graceful shutdown of the OSPFv3 process in IPv6 router
OSPF configuration mode configuration mode:
ipv6 router ospf 6
router-id 10.10.10.10
shutdown

The following example shows how to configure graceful shutdown of the OSPFv3 process in router OSPFv3
configuration mode:
!
router ospfv3 1
shutdown
!
address-family ipv6 unicast
exit-address-family

The following example shows how to configure graceful shutdown of the OSPFv3 process in address-family
configuration mode:
!
router ospfv3 1
!
address-family ipv6 unicast
shutdown
exit-address-family

IP Routing: OSPF Configuration Guide
108


Graceful Shutdown Support for OSPFv3
Example: Configuring Graceful Shutdown of the OSPFv3 Interface

Example: Configuring Graceful Shutdown of the OSPFv3 Interface
The following example shows how to configure graceful shutdown of the OSPFv3 interface using the ipv6
ospf shutdown command:
!
interface Serial2/1
no ip address
ipv6 enable
ipv6 ospf 6 area 0
ipv6 ospf shutdown
serial restart-delay 0
end

The following example shows how to configure graceful shutdown of the OSPFv3 interface using the ospfv3
shutdown command:
!
interface Serial2/0
ip address 10.10.10.10 255.255.255.0
ip ospf 1 area 0
ipv6 enable
ospfv3 shutdown
ospfv3 1 ipv6 area 0
serial restart-delay 0
end

Additional References for Graceful Shutdown Support for
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
109


Graceful Shutdown Support for OSPFv3
Feature Information for Graceful Shutdown Support for OSPFv3

Feature Information for Graceful Shutdown Support for OSPFv3
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 11: Feature Information for Graceful Shutdown Support for OSPFv3

Feature Name

Releases

Feature Information

Graceful Shutdown Support for
OSPFv3

Cisco IOS XE Release 3.8

This feature provides the ability to
temporarily shut down an Open
Shortest Path First version 3
(OSPFv3) process or interface in
the least disruptive manner, and to
notify its neighbors that it is going
away.
A graceful shutdown of a protocol
can be initiated on all OSPFv3
interfaces or on a specific interface.
The following commands were
introduced:
• ipv6 ospf shutdown
• ospfv3 shutdown
• shutdown (router ospfv3)

IP Routing: OSPF Configuration Guide
110
