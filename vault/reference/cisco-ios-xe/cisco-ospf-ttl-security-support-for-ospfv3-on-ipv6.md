---
title: "TTL Security Support for OSPFv3 on IPv6"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ttl-security-support-for-ospfv3-on-ipv6
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 37 TTL Security Support for OSPFv3 on IPv6 The Time To Live (TTL) Security Support for Open Shortest Path First version 3 (OSPFv3) on IPv6 feature increases protection against OSPFv3 denial of service attacks. • Finding Feature Information, page 349 • Restrictions for TTL Security Support for OSPFv3 on IPv6, page 349 • Prerequisites for TTL Security Support for OSPFv3 on IPv6, page 350 •"
---

# TTL Security Support for OSPFv3 on IPv6

CHAPTER

37

TTL Security Support for OSPFv3 on IPv6
The Time To Live (TTL) Security Support for Open Shortest Path First version 3 (OSPFv3) on IPv6 feature
increases protection against OSPFv3 denial of service attacks.
• Finding Feature Information, page 349
• Restrictions for TTL Security Support for OSPFv3 on IPv6, page 349
• Prerequisites for TTL Security Support for OSPFv3 on IPv6, page 350
• Information About TTL Security Support for OSPFv3 on IPv6, page 350
• How to Configure TTL Security Support for OSPFv3 on IPv6, page 351
• Configuration Examples for TTL Security Support for OSPFv3 on IPv6, page 353
• Additional References, page 354
• Feature Information for TTL Security Support for OSPFv3 on IPv6, page 355

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions for TTL Security Support for OSPFv3 on IPv6
• OSPFv3 TTL security can be configured for virtual and sham links only.
• OSPFv3 TTL security must be configured in IPv6 address family configuration mode (config-router-af).
To enter IPv6 address family configuration mode you use the address-family ipv6 command.
• Sham links must not be configured on the default Virtual Routing and Forwarding (VRF).

IP Routing: OSPF Configuration Guide
349


TTL Security Support for OSPFv3 on IPv6
Prerequisites for TTL Security Support for OSPFv3 on IPv6

Prerequisites for TTL Security Support for OSPFv3 on IPv6
The TTL Security Support for OSPFv3 on IPv6 feature is available only on platforms with OSPFv3 routing
capabilities.

Information About TTL Security Support for OSPFv3 on IPv6
OSPFv3 TTL Security Support for Virtual and Sham Links
In OSPFv3, all areas must be connected to a backbone area. If there is a break in backbone continuity, or the
backbone is purposefully partitioned, you can establish a virtual link. The virtual link must be configured in
the two devices you want to use to connect the partitioned backbone. The configuration information in each
device consists of the other virtual endpoint (the other Area Border Router [ABR]) and the nonbackbone area
that the two devices have in common (called the transit area.) Note that virtual links cannot be configured
through stub areas. Sham links are similar to virtual links in many ways, but sham links are used in Layer 3
Multiprotocol Label Switching (MPLS) VPN networks to connect provider edge (PE) routers across the MPLS
backbone.

Note

Multihop adjacencies such as virtual links and sham links use global IPv6 addresses that require you to
configure TTL security to control the number of hops that a packet can travel.
If TTL security is enabled, OSPFv3 sends outgoing packets with an IP header TTL value of 255 and discards
incoming packets that have TTL values less than the configurable threshold. Because each device that forwards
an IP packet decreases the TTL value, packets received via a direct (one-hop) connection will have a value
of 255. Packets that cross two hops will have a value of 254, and so on. The receive threshold is configured
in terms of the maximum number of hops that a packet may have traveled. The value for this hop-count
argument is a number from 1 to 254, with a default of 1.
To establish a virtual link or a sham link, use the area virtual-link or area sham-link cost commands
respectively. To configure TTL security on a virtual link or a sham link, configure the ttl-security keyword
and the hop-count argument in either command. Note that the hop-count argument value is mandatory in this
case.

Note

OSPFv3 TTL Security can be configured for virtual and sham links only, and must be configured in address
family configuration (config-router-af) mode for IPv6 address families.

IP Routing: OSPF Configuration Guide
350


TTL Security Support for OSPFv3 on IPv6
How to Configure TTL Security Support for OSPFv3 on IPv6

How to Configure TTL Security Support for OSPFv3 on IPv6
Configuring TTL Security Support on Virtual Links for OSPFv3 on IPv6
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. address-family ipv6 unicast vrf vrf-name
5. area area-ID virtual-link router-id ttl-security hops hop-count
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

router ospfv3 [process-id]

Enables router configuration mode for the IPv4 or IPv6
address family.

Example:
Device(config)# router ospfv3 1

Step 4

address-family ipv6 unicast vrf vrf-name
Example:

Enters address family configuration mode for OSPFv3,
specifies IPv6 unicast address prefixes, and specifies the
name of the VRF instance to associate with subsequent
address family configuration mode commands.

Device(config-router)# address-family ipv6
unicast vrf vrf1

IP Routing: OSPF Configuration Guide
351


TTL Security Support for OSPFv3 on IPv6
Configuring TTL Security Support on Sham Links for OSPFv3 on IPv6

Command or Action
Step 5

Purpose

area area-ID virtual-link router-id ttl-security hops Defines an OSPFv3 virtual link and configures TTL security
on the virtual link.
hop-count
Example:
Device(config-router-af)# area 1 virtual-link
10.1.1.1 ttl-security hops 10

Step 6

(Optional) Returns to privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuring TTL Security Support on Sham Links for OSPFv3 on IPv6
SUMMARY STEPS
1. enable
2. configure terminal
3. router ospfv3 [process-id]
4. address-family ipv6 unicast vrf vrf-name
5. area area-id sham-link source-address destination-address ttl-security hops hop-count
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
Example:
Device# configure terminal

IP Routing: OSPF Configuration Guide
352

Enters global configuration mode.


TTL Security Support for OSPFv3 on IPv6
Configuration Examples for TTL Security Support for OSPFv3 on IPv6

Step 3

Command or Action

Purpose

router ospfv3 [process-id]

Enables OSPFv3 router configuration mode for the IPv4
or IPv6 address family.

Example:
Device(config)# router ospfv3 1

Step 4

address-family ipv6 unicast vrf vrf-name
Example:

Enters address family configuration mode for OSPFv3,
specifies IPv6 unicast address prefixes, and specifies the
name of the VRF instance to associate with subsequent
address family configuration mode commands.

Device(config-router)# address-family ipv6
unicast vrf vrf1

Step 5

area area-id sham-link source-address
destination-address ttl-security hops hop-count

Defines an OSPFv3 sham link and configures TTL security
on the sham link.

Example:
Device(config-router-af)# area 1 sham-link
2001:DB8:1::1 2001:DB8:0:A222::2 ttl-security
hops 10

Step 6

(Optional) Returns to privileged EXEC mode.

end
Example:
Device(config-router-af)# end

Configuration Examples for TTL Security Support for OSPFv3 on
IPv6
Example: TTL Security Support on Virtual Links for OSPFv3 on IPv6
The following example shows how to configure TTL virtual link security:
Device> enable
Device# configure terminal
Device(config)# router ospfv3 1
Device(config-router)# address-family ipv6 unicast vrf vrf1
Device(config-router-af)# area 1 virtual-link 10.1.1.1 ttl-security hops 10
Device(config-router-af)# end
Device# show ospfv3 virtual-links
OSPFv3 1 address-family ipv6 (router-id 10.1.1.7)
Virtual Link OSPFv3_VL0 to router 10.1.1.2 is down
Interface ID 23, IPv6 address ::
Run as demand circuit
DoNotAge LSA allowed.
Transit area 1, Cost of using 65535
Transmit Delay is 1 sec, State DOWN,

IP Routing: OSPF Configuration Guide
353


TTL Security Support for OSPFv3 on IPv6
Example: TTL Security Support on Sham Links for OSPFv3 on IPv6

Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
Strict TTL checking enabled, up to 10 hops allowed

Example: TTL Security Support on Sham Links for OSPFv3 on IPv6
The following example shows how to configure TTL sham link security:
Device> enable
Device# configure terminal
Device(config)# router ospfv3 1
Device(config-router)# address-family ipv6 unicast vrf vrf1
Device(config-router-af)# area 1 sham-link 2001:DB8:1::1 2001:DB8:0:A222::2 ttl-security
hops 10
Device(config-router-af)# end
Device#

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

OSPF commands

Cisco IOS IP Routing: OSPF
Command Reference

IPv6 routing: OSPFv3

"IPv6 Routing: OSPFv3" module

MIBs
MIB

MIBs Link

No new or modified MIBs are supported, and support To locate and download MIBs for selected platforms,
for existing MIBs has not been modified.
Cisco software releases, and feature sets, use Cisco
MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

IP Routing: OSPF Configuration Guide
354


TTL Security Support for OSPFv3 on IPv6
Feature Information for TTL Security Support for OSPFv3 on IPv6

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

Feature Information for TTL Security Support for OSPFv3 on IPv6
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 44: TTL Security Support for OSPFv3 on IPv6

Feature Name

Software Releases

Feature Information

TTL Security Support for OSPFv3 Cisco IOS XE Release 3.7S
on IPv6

The TTL Security Support for
OSPFv3 on IPv6 feature increases
protection against OSPFv3 denial
of service attacks.
The following commands were
introduced or modified by this
feature: area sham-link, area
virtual-link.

IP Routing: OSPF Configuration Guide
355


TTL Security Support for OSPFv3 on IPv6
Feature Information for TTL Security Support for OSPFv3 on IPv6

IP Routing: OSPF Configuration Guide
356
