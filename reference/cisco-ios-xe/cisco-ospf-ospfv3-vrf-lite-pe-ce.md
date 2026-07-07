---
title: "OSPFv3 VRF-Lite/PE-CE"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospfv3-vrf-lite-pe-ce
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 49 OSPFv3 VRF-Lite/PE-CE The OSPFv3 VRF-Lite/PE-CE feature adds Open Shortest Path First version 3 (OSPFv3) support for nondefault VPN routing and forwarding (VRF) instances. OSPFv3 can be used as a provider-edge-customer-edge (PE-CE) routing protocol as specified in RFC 6565, OSPFv3 as a Provider Edge to Customer Edge (PE-CE) Routing Protocol. OSPFv3 in a nondefault VRF instance support"
---

# OSPFv3 VRF-Lite/PE-CE

CHAPTER

49

OSPFv3 VRF-Lite/PE-CE
The OSPFv3 VRF-Lite/PE-CE feature adds Open Shortest Path First version 3 (OSPFv3) support for
nondefault VPN routing and forwarding (VRF) instances. OSPFv3 can be used as a
provider-edge-customer-edge (PE-CE) routing protocol as specified in RFC 6565, OSPFv3 as a Provider
Edge to Customer Edge (PE-CE) Routing Protocol. OSPFv3 in a nondefault VRF instance supports routing
of IPv4 and IPv6 address families.
• Finding Feature Information, page 463
• Restrictions for OSPFv3 VRF-Lite/PE-CE, page 463
• Information About OSPFv3 VRF-Lite/PE-CE, page 464
• How to Configure VRF-Lite/PE-CE, page 465
• Configuration Examples for OSPFv3 VRF-Lite/PE-CE, page 473
• Additional References for OSPFv3 VRF-Lite/PE-CE, page 475
• Feature Information for OSPFv3 VRF-Lite/PE-CE, page 476

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions for OSPFv3 VRF-Lite/PE-CE
In Cisco IOS Release 15.2(2)S and later releases, OSPFv3 interface commands in the ipv6 ospf format are
no longer supported in VRF interface configuration mode. You must configure them in the new format, ospfv3.
The ospfv3 commands can have one of following formats:
• ospfv3 —Applies to all OSPFv3 processes and address families on a given interface.

IP Routing: OSPF Configuration Guide
463


OSPFv3 VRF-Lite/PE-CE
Information About OSPFv3 VRF-Lite/PE-CE

• ospfv3 process-id —Applies to an OSPFv3 process with the configured process ID and to both IPv4
and IPv6 address families.
• ospfv3 process-id address-family-ID —Applies to an OSPFv3 process with the configured process ID
and the configured address family.
More specific commands take precedence over less specific commands, as shown in the following descending
order:
1 Commands that specify a process ID and an address family.
2 Commands that specify only a process ID.
3 Commands that specify neither a process ID nor an address family.
In Cisco IOS Release 15.2(2)S and later releases, you cannot use the ipv6 ospf router process-id command
to configure OSPFv3 VRF instances. You must configure the router ospfv3 process-id command in global
configuration mode and specify the address family for the configured VRF in router configuration mode.

Information About OSPFv3 VRF-Lite/PE-CE
Support for OSPFv3 VRF-Lite and PE-CE
Open Shortest Path First version 3 (OSPFv3) operates in nondefault VPN routing and forwarding (VRF)
instances for both IPv6 and IPv4 address families and, transports the routes across a Border Gateway Protocol
(BGP) or a Multiprotocol Label Switching (MPLS) backbone. On the provider edge (PE) device, customer
routes are installed together by OSPFv3 and BGP in a common VRF or address family and each protocol is
configured to redistribute the routes of the other. BGP combines the prefixes redistributed into it with a
route-distinguisher value defined for the VRF and advertises them to other MPLS-BGP speakers in the same
autonomous system using the VPNv4 or VPNv6 address family as appropriate.
The OSPFv3 route selection algorithm prefers intra-area routes across the back-door link over inter-area routes
through the MPLS backbone. Sham-links are a type of virtual link across the MPLS backbone that connect
OSPFv3 instances on different PEs. OSPFv3 instances tunnel protocol packets through the backbone and
form adjacencies. Because OSPFv3 considers the sham-link as an intra-area connection, sham-link serves as
a valid alternative to an intra-area back-door link.
Domain IDs are used to determine whether the routes are internal or external. They describe the administrative
domain of the OSPFv3 instance from which the route originates. Every PE has a 48-bit primary domain ID
(which may be NULL) and zero or more secondary domain IDs.

IP Routing: OSPF Configuration Guide
464


OSPFv3 VRF-Lite/PE-CE
How to Configure VRF-Lite/PE-CE

How to Configure VRF-Lite/PE-CE
Configuring a VRF in an IPv6 Address Family for OSPFv3
SUMMARY STEPS
1. enable
2. configure terminal
3. vrf definition vrf-name
4. rd route-distinguisher
5. exit
6. router ospfv3 [process-id]
7. address-family ipv6 [unicast] [vrf vrf-name]
8. end

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

vrf definition vrf-name

Configures a VRF routing table and enters VRF configuration
mode.

Example:
Device(config)# vrf definition vrfsample

Step 4

rd route-distinguisher

Creates routing and forwarding tables for a VRF.

Example:
Device(config-vrf)# rd 10:1

Step 5

exit

Exists VRF configuration mode and returns to global
configuration mode.

Example:
Device(config-vrf)# exit

IP Routing: OSPF Configuration Guide
465


OSPFv3 VRF-Lite/PE-CE
Enabling an OSPFv3 IPv6 Address Family on a VRF Interface

Step 6

Command or Action

Purpose

router ospfv3 [process-id]

Configures an OSPF routing process and enters router
configuration mode.

Example:
Device(config)# router ospfv3 2

Step 7

address-family ipv6 [unicast] [vrf vrf-name]
Example:

Configures an instance of the OSPFv3 process in the VRF
routing table for the IPv6 address family and enters router
address family configuration mode.

Device(config-router)# address-family ipv6
unicast vrf vrfsample

Step 8

Exists router address family configuration mode and returns
to privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Enabling an OSPFv3 IPv6 Address Family on a VRF Interface
SUMMARY STEPS
1. enable
2. configure terminal
3. interface type number
4. vrf forwarding vrf-name [downstream vrf-name2]
5. ipv6 enable
6. ospfv3 process-id {ipv4 | ipv6} area area-id [instance instance-id]
7. end

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Device# enable

IP Routing: OSPF Configuration Guide
466

• Enter your password if prompted.


OSPFv3 VRF-Lite/PE-CE
Configuring a Sham-Link for OSPFv3 PE-CE

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

interface type number

Specifies an interface type and number and enters
interface configuration mode.

Example:
Device(config)# interface Serial6/0

Step 4

vrf forwarding vrf-name [downstream vrf-name2]

Associates an interface with a VRF.

Example:
Device(config-if)# vrf forwarding v1

Step 5

ipv6 enable

Enables IPv6 processing on the interface that is
associated with the VRF.

Example:
Device(config-if)# ipv6 enable

Step 6

ospfv3 process-id {ipv4 | ipv6} area area-id [instance Enables the OSPFv3 IPv6 address family on the VRF
interface.
instance-id]
Example:
Device(config-if)# ospfv3 1 ipv6 area 0

Step 7

Exits interface configuration mode and returns to
privileged EXEC mode.

end
Example:
Device(config-if)# end

Configuring a Sham-Link for OSPFv3 PE-CE
Before You Begin
The OSPFv3 PE-CE feature supports direct forwarding on Border Gateway Protocol (BGP) routes.
Before you configure a sham-link, you must create a Multiprotocol Label Switching (MPLS) backbone,
configure a device as an MPLS VPN PE device, and configure OSPFv3 as the provider-edge-customer-edge
(PE-CE) protocol in a virtual routing and forwarding (VRF) instance.

IP Routing: OSPF Configuration Guide
467


OSPFv3 VRF-Lite/PE-CE
Configuring a Sham-Link for OSPFv3 PE-CE

SUMMARY STEPS
1. enable
2. configure terminal
3. interface loopback interface-number
4. description string
5. vrf forwarding vrf-name
6. ipv6 address ipv6-address/prefix-length
7. ipv6 enable
8. end
9. router ospfv3 process-id
10. address-family {ipv4 | ipv6} [unicast | multicast] [vrf vrf-name]
11. redistribute process-id [options]
12. area area-id sham-link source-address destination-address [cost number] [ttl-security hops hop-count]
13. end

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

interface loopback interface-number
Example:

Creates a loopback interface to be used as an endpoint of
the sham-link on a provider edge device and enters
interface configuration mode.

Device(config)# interface loopback 0

Step 4

description string

Provides a description of the interface to help you track
its status.

Example:
Device(config-if)# description Sham-link endpoint

Step 5

vrf forwarding vrf-name
Example:
Device(config-if)# vrf forwarding vrf1

IP Routing: OSPF Configuration Guide
468

Associates the loopback interface with a VRF.


OSPFv3 VRF-Lite/PE-CE
Configuring a Sham-Link for OSPFv3 PE-CE

Step 6

Command or Action

Purpose

ipv6 address ipv6-address/prefix-length

Configures an IPv6 address of the loopback interface on
a provider edge device.

Example:
Device(config-if)# ipv6 address
2001:DB8:0:ABCD::1/48

Step 7

ipv6 enable

Enables IPv6 processing on the loopback interface.

Example:
Device(config-if)# ipv6 enable

Step 8

end

Exits interface configuration mode and returns to global
configuration mode.

Example:
Device# end

Step 9

router ospfv3 process-id

Enters router configuration mode.

Example:
Device(config)# router ospfv3 1

Step 10

address-family {ipv4 | ipv6} [unicast | multicast] [vrf Enters IPv6 address family configuration mode for
OSPFv3.
vrf-name]
Example:
Device(config-router)# address-family ipv6
unicast vrf vrf1

Step 11

redistribute process-id [options]
Example:
Device(config-router-af)# redistribute bgp 2

Step 12

area area-id sham-link source-address
destination-address [cost number] [ttl-security hops
hop-count]

Redistributes IPv6 routes from the specified source BGP
routing domain into the specified destination routing
domain.
Note
PE-CE redistribution is always from
BGP.
Enables the sham-link and specifies its source and
destination addresses.

Example:
Device(config-router-af)# area 0 sham-link
2001:DB8:0:ABCD::1 2001:DB8:0:ABCD::2 cost 100

Step 13

end

Exits address family configuration mode and returns to
privileged EXEC mode.

Example:
Device(config-router-af)# end

IP Routing: OSPF Configuration Guide
469


OSPFv3 VRF-Lite/PE-CE
Configuring a Domain ID for an OSPFv3 PE-CE

Configuring a Domain ID for an OSPFv3 PE-CE
SUMMARY STEPS
1. enable
2. configure terminal
3. vrf definition vrf-name
4. rd route-distinguisher
5. exit
6. router ospfv3 [process-id]
7. address-family ipv6 [unicast] [vrf vrf-name]
8. domain-id type type value hex-value
9. end

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

vrf definition vrf-name

Configures a VRF routing table and enters VRF configuration
mode.

Example:
Device(config)# vrf definition vrfsample

Step 4

rd route-distinguisher
Example:
Device(config-vrf)# rd 10:1

IP Routing: OSPF Configuration Guide
470

Creates routing and forwarding tables for a VRF.


OSPFv3 VRF-Lite/PE-CE
Configuring VRF-Lite Capability for OSPFv3

Step 5

Command or Action

Purpose

exit

Exists VRF configuration mode and returns to global
configuration mode.

Example:
Device(config-vrf)# exit

Step 6

router ospfv3 [process-id]

Enters router configuration mode.

Example:
Device(config)# router ospfv3 2

Step 7

address-family ipv6 [unicast] [vrf vrf-name]
Example:

Configures an instance of the OSPFv3 process in the VRF
routing table for the IPv6 address family and enters address
family configuration mode..

Device(config-router)# address-family ipv6
unicast vrf vrfsample

Step 8

domain-id type type value hex-value

Configures the BGP domain ID.
• The value for type can be 0005, 0105, 0205, or 8005.

Example:

• The value for value is an arbitrary 48-bit number
encoded as 12 hexadecimal digits.

Device(config-router-af)# domain-id type 0205
value 800EFFFF12AB

Step 9

Exists router address family mode and returns to privileged
EXEC mode.

end
Example:
Device(config-router-af)# end

Configuring VRF-Lite Capability for OSPFv3
SUMMARY STEPS
1. enable
2. configure terminal
3. vrf definition vrf-name
4. rd route-distinguisher
5. exit
6. router ospfv3 [process-id]
7. address-family ipv6 [unicast] [vrf vrf-name]
8. capability vrf-lite
9. end

IP Routing: OSPF Configuration Guide
471


OSPFv3 VRF-Lite/PE-CE
Configuring VRF-Lite Capability for OSPFv3

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

vrf definition vrf-name

Configures a VRF routing table and enters VRF
configuration mode.

Example:
Device(config)# vrf definition vrfsample

Step 4

rd route-distinguisher

Creates routing and forwarding tables for a VRF.

Example:
Device(config-vrf)# rd 10:1

Step 5

exit

Exists VRF configuration mode and returns to global
configuration mode.

Example:
Device(config-vrf)# exit

Step 6

router ospfv3 [process-id]

Enables router configuration mode for the IPv4 or IPv6
address family.

Example:
Device(config)# router ospfv3 2

Step 7

address-family ipv6 [unicast] [vrf vrf-name]
Example:

Configures an instance of the OSPFv3 process in the VRF
routing table for the IPv6 address family and enters address
family configuration mode.

Device(config-router)# address-family ipv6
unicast vrf vrfsample

Step 8

capability vrf-lite
Example:
Device(config-router-af)# capability vrf-lite

IP Routing: OSPF Configuration Guide
472

Applies the multi-VRF capability to the OSPF process.


OSPFv3 VRF-Lite/PE-CE
Configuration Examples for OSPFv3 VRF-Lite/PE-CE

Step 9

Command or Action

Purpose

end

Exists router address family mode and returns to privileged
EXEC mode.

Example:
Device(config-router-af)# end

Configuration Examples for OSPFv3 VRF-Lite/PE-CE
Example: Configuring a Provider Edge Device to Provide IPv6 and IPv4 Routing
The following example shows how to configure a provider edge (PE) device to provide IPv6 and IPv4 routing
for a user on VRF “v1” and IPv6 routing for a user on VRF “v2”:
vrf definition v1
rd 1:1
route-target export 100:1
route-target import 100:1
!
address-family ipv4
exit-address-family
!
address-family ipv6
exit-address-family
!
vrf definition v2
rd 2:2
route-target export 200:2
route-target import 200:2
!
address-family ipv6
exit-address-family
!
interface Loopback1
vrf forwarding v1
ipv6 address 2001:DB8:0:ABCD::1/48
!
interface Serial5/0
vrf forwarding v2
no ip address
ipv6 address 2001:DB8:0:ABCD::3/48
ospfv3 1 ipv6 area 1
!
interface Serial6/0
vrf forwarding v1
ip address 10.0.0.1 255.255.255.0
ipv6 enable
ospfv3 1 ipv6 area 0
ospfv3 1 ipv4 area 10.1.1.1
!
router ospfv3
!
log-adjacency-changes detail
!
address-family ipv4 unicast vrf v1
router-id 10.2.2.2
redistribute bgp 1

IP Routing: OSPF Configuration Guide
473


OSPFv3 VRF-Lite/PE-CE
Example: Configuring a Provider Edge Device for VRF-Lite

exit-address-family
!
address-family ipv6 unicast vrf v1
router-id 2001:DB8:1::1
domain-id type 0205 value 111111222222
area 0 sham-link 2001:DB8:0:ABCD::5 2001:DB8:0:ABCD::7
redistribute bgp 1
exit-address-family
address-family ipv6 unicast vrf v2
router-id 2001:DB8:1::3
redistribute bgp 1
exit
!
router bgp 1
bgp router-id 10.3.3.3
no bgp default ipv4-unicast
neighbor 10.0.0.4 remote-as 1
neighbor 10.0.0.4 update-source-Loopback0
!
address-family ipv4
exit-address-family
!
address-family vpnv4
neighbor 10.0.0.4
neighbor 10.0.0.4 send-community extended
exit-address-family
!
address-family vpnv6
neighbor 10.0.0.4 activate
neighbor 10.0.0.4 send-community extended
exit-address-family
!
address-family ipv4 vrf v1
redistribute ospfv3 1
exit-address-family
!
address-family ipv6 vrf v1
redistribute ospf 1
exit-address-family
!
address-family ipv6 vrf v2
redistribute ospf 1
exit-address-family
!

Example: Configuring a Provider Edge Device for VRF-Lite
vrf definition v1
rd 1:1
!
address-family ipv4
exit-address-family
!
address-family ipv6
exit-address-family
!
vrf definition v2
rd 2:2
!
address-family ipv6
exit-address-family
!
interface FastEthernet0/0
no ip address
!
interface FastEthernet0/0.100
encapsulation dot1Q 100
vrf forwarding v1
ip address 192.168.1.1 255.255.255.0

IP Routing: OSPF Configuration Guide
474


OSPFv3 VRF-Lite/PE-CE
Additional References for OSPFv3 VRF-Lite/PE-CE

ipv6 enable
ospfv3 1 ipv6 area 0
ospfv3 1 ipv4 area 0
!
interface FastEthernet0/0.200
encapsulation dot1Q 200
vrf forwarding v2
ipv6 enable
ospfv3 1 ipv6 area 0
!
interface FastEthernet0/1
rf forwarding v1
ip address 10.1.1.1 255.255.255.0
ipv6 enable
ospfv3 1 ipv6 area 1
ospfv3 1 ipv4 area 0
no keepalive
!
interface FastEthernet0/2
vrf forwarding v2
no ip address
ipv6 address 2001:DB8:1::1
ipv6 enable
ospfv3 1 ipv6 area 1
!
router ospfv3 1
!
address-family ipv6 unicast vrf v2
router-id 192.168.2.1
capability vrf-lite
exit-address-family
!
address-family ipv4 unicast vrf v1
router-id 192.168.1.4
capability vrf-lite
exit-address-family
!
address-family ipv6 unicast vrf v1
router-id 192.168.1.1
capability vrf-lite
exit-address-family
!

Additional References for OSPFv3 VRF-Lite/PE-CE
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List, All Releases

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

RFCs
RFC

Title

RFC 5838

Support of Address Families in OSPFv3

IP Routing: OSPF Configuration Guide
475


OSPFv3 VRF-Lite/PE-CE
Feature Information for OSPFv3 VRF-Lite/PE-CE

RFC

Title

RFC 6565

OSPFv3 as a Provider Edge to Customer Edge
(PE-CE) Routing Protocol

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

Feature Information for OSPFv3 VRF-Lite/PE-CE
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 55: Feature Information for OSPFv3 VRF-Lite/PE-CE

Feature Name

Releases

Feature Information

OSPFv3 VRF-Lite/PE-CE

Cisco IOS XE Release 3.6S

The OSPFv3 VRF-Lite/PE-CE
feature adds OSPFv3 support for
nondefault VRF instances.
The following commands were
introduced or modified: area
sham-link (OSPFv3), capability
vrf-lite (OSPFv3).

IP Routing: OSPF Configuration Guide
476
