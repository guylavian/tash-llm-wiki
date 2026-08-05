---
title: "VRF Aware BGP Translate-Update"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-vrf-aware-bgp-translate-update
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 80 VRF Aware BGP Translate-Update The VRF aware BGP translate-update feature enables multicast forwarding on those customer-edge (CE) devices, which have an older version of Cisco software that does not support multicast BGP (mBGP) routing. The provider-edge (PE) devices establish a virtual routing and forwarding (VRF) session with the neighbor CE devices, and configure the translate-upd"
---

# VRF Aware BGP Translate-Update

CHAPTER

80

VRF Aware BGP Translate-Update
The VRF aware BGP translate-update feature enables multicast forwarding on those customer-edge (CE)
devices, which have an older version of Cisco software that does not support multicast BGP (mBGP) routing.
The provider-edge (PE) devices establish a virtual routing and forwarding (VRF) session with the neighbor
CE devices, and configure the translate-update feature under an IPv4/IPv6 VRF address family. The PE
devices translate the updates from unicast to multicast on CE devices and put them as multicast updates in
the Border Gateway Protocol (BGP) VRF routing table of the PE devices for processing.
• Finding Feature Information, on page 1101
• Prerequisites for VRF Aware BGP Translate-Update, on page 1101
• Restrictions for VRF Aware BGP Translate-Update, on page 1102
• Information About VRF Aware BGP Translate-Update, on page 1102
• How To Configure VRF Aware BGP Translate-Update, on page 1103
• Configuration Examples for VRF Aware BGP Translate-Update, on page 1106
• Additional References for VRF Aware BGP Translate-Update, on page 1110
• Feature Information for VRF Aware BGP Translate-Update, on page 1110

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites for VRF Aware BGP Translate-Update
• The VRF aware translate-update feature applies only to IPv4/IPv6 virtual routing and forwarding (VRF)
address-families.
• You must use peer-group for the configuration of the neighbor under IPv4/IPv6 VRF address families.
• BGP neighbors that are only capable of unicast routing, must be activated under both unicast and multicast
address families.

IP Routing: BGP Configuration Guide
1101


VRF Aware BGP Translate-Update
Restrictions for VRF Aware BGP Translate-Update

• BGP neighbors must also be enabled under the compatible multicast address family for the VRF aware
translate-update feature to function as designed.
• The provider-edge (PE) devices must have multicast VRF enabled and must have a session established
with the customer-edge (CE) devices.

Restrictions for VRF Aware BGP Translate-Update
• You must not configure (nonVRF) IPv4/IPv6 address families for the VRF aware BGP translate-update
feature. The IPv4/IPv6 address family must be configured for multicast routing using the Subsequent
Address Family Identifier (SAFI) feature.
• The VRF aware BGP translate-update feature does not support configuration of BGP neighbor using
peer-template.

Information About VRF Aware BGP Translate-Update
VRF Aware BGP Translate-Update Overview
The VRF aware BGP translate-update feature enables multicast forwarding on those customer-edge (CE)
devices, which have an older version of Cisco software that does not support multicast BGP (mBGP) routing.
This feature is analogous to the Subsequent Address Family Identifier (SAFI), which provides the capability
to support multicast routing in the service provider's core IPv4 network, but is limited in support to IPv4/IPv6
address families. In the case of the virtual routing and forwarding (VRF) aware BGP translate-update feature,
provider-edge (PE) devices establish a VRF session with the neighbor CE devices, and have the translate-update
feature configured under an IPv4/IPv6 VRF address family.
When the neighbor translate-update command is configured on a PE device under the (IPv4 VRF)
address-family configuration mode or the (IPv6 VRF) address-family configuration mode, the PE devices
translate the updates from unicast to multicast on CE devices and put them in the Border Gateway Protocol
(BGP) VRF routing table of the PE devices, as multicast updates, for processing. If you also configure the
optional keyword unicast, the updates that are not translated, are placed in the PE device's unicast queue and
populates the unicast VRF BGP table. The translation from unicast to multicast routes occurs from CE devices
to PE devices only, and the multicast and unicast prefixes are only advertised from the CE device to the PE
device's multicast neighbors.
For example, when you configure the VRF aware BGP translate-update feature under a VRF (v1) for a neighbor
CE device (CE1), a neighbor topology under the IPv4-multicast-VRF or IPv6-multicast-VRF address-family
is added to CE1's session with a PE device (PE1). The multicast-VRF neighbor topology does not actively
participate in these multicast sessions and only forwards announcements that arrive from CE1. Once such
announcements arrive, they are translated into multicast and placed in the nonactive multicast VRF neighbor's
routing table. The Cisco software ensures that the routes advertised by CE1 configured under the IPv4/IPv6
VRF address-family are available on PE1's IPv4/IPv6 multicast VRF v1 address-family BGP table. These
routes, along with PE1's IPv4/IPv6 multicast VRF v1 address-family BGP table, are advertised to PE1's
multicast peers if you have configured the neighbor translate-update command . The routes are also advertised
to PE1's unicast peers if you have also configured the optional keyword unicast.

IP Routing: BGP Configuration Guide
1102


VRF Aware BGP Translate-Update
How To Configure VRF Aware BGP Translate-Update

The unicast keyword is optional, yet significant, as it enables the PE devices to place unicast advertisements
from the CE devices in the unicast BGP table of the PE devices. Therefore, route advertisements from CE
devices populates both unicast and multicast BGP tables, else CE device's routes only populate the PE device's
multicast BGP table.

Note

You must also enable address-family under the compatible multicast address-family for VRF aware BGP
translate-update feature to function as designed.

How To Configure VRF Aware BGP Translate-Update
Configuring VRF Aware BGP Translate-Update
Perform this task to configure VRF aware BGP translate-update feature:
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.

enable
configure terminal
router bgp as-number
address-family ipv4 [mdt | tunnel | {multicast | unicast} [vrf vrf-name] | vrf vrf-name]
neighbor peer-group-name peer-group
neighbor {ipv4-addr | ipv6-addr | peer-group-name} remote-as autonomous-system-number
neighbor {ipv4-addr | ipv6-addr} peer-group peer-group-name
neighbor {ipv4-addr | ipv6-addr | peer-group-name} activate
neighbor {ipv4-address | ipv6-address} translate-update multicast [unicast]
end
show bgp vpnv4 multicast {all | vrf vrf-name | rd route-distinguisher}
show ip route multicast vrf vrf-name
show running-config

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

IP Routing: BGP Configuration Guide
1103


VRF Aware BGP Translate-Update
Configuring VRF Aware BGP Translate-Update

Step 3

Command or Action

Purpose

router bgp as-number

Enters router configuration mode and creates a BGP
routing process.

Example:
Device(config)# router bgp 65000

Step 4

address-family ipv4 [mdt | tunnel | {multicast |
unicast} [vrf vrf-name] | vrf vrf-name]
Example:

Enters address family configuration mode to configure a
routing session using standard IP Version 4 (IPv4) address
prefixes.

Device(config)# address-family ipv4 vrf v1

Step 5

neighbor peer-group-name peer-group

Creates a BGP or multiprotocol BGP peer group.

Example:
Device(config-af)# neighbor n2 peer-group

Step 6

neighbor {ipv4-addr | ipv6-addr | peer-group-name}
remote-as autonomous-system-number

Adds an entry to the BGP or multiprotocol BGP neighbor
table.

Example:
Device(config-af)# neighbor n2 remote-as 4

Step 7

neighbor {ipv4-addr | ipv6-addr} peer-group
peer-group-name

Configures a BGP neighbor to be a member of a peer
group.

Example:
Device(config-af)# neighbor 10.1.1.1 peer-group
n2

Step 8

neighbor {ipv4-addr | ipv6-addr | peer-group-name}
activate

Enables exchange of information with a BGP neighbor.

Example:
Device(config-af)# neighbor 10.1.1.1 activate

Step 9

neighbor {ipv4-address | ipv6-address} translate-update Enables multicast routing on devices, which are not capable
of multicast BGP (mBGP) routing.
multicast [unicast]
Example:
Device(config-af)# neighbor 10.1.1.1
translate-update multicast unicast

Step 10

Returns to privileged EXEC mode.

end
Example:
Device(config-af)# end

IP Routing: BGP Configuration Guide
1104


VRF Aware BGP Translate-Update
Removing the VRF Aware BGP Translate-Update Configuration

Step 11

Command or Action

Purpose

show bgp vpnv4 multicast {all | vrf vrf-name | rd
route-distinguisher}

Displays Virtual Private Network Version 4 (VPNv4)
multicast entries in a BGP table.

Example:
Device# show bgp vpnv4 mul vrf v1 summary

Step 12

show ip route multicast vrf vrf-name
Example:

Displays the IP routing table associated with a specific
multicast VPN routing and forwarding (VRF) instance.

Device# show ip route multicast vrf v1

Step 13

show running-config

Displays the running configuration on the device.

Example:
Device# show running-config

Removing the VRF Aware BGP Translate-Update Configuration
Perform this task to disable the VRF aware BGP translate-update feature:
SUMMARY STEPS
1.
2.
3.
4.
5.
6.
7.

enable
configure terminal
router bgp as-number
address-family ipv4 [mdt | tunnel | {multicast | unicast} [vrf vrf-name] | vrf vrf-name]
no neighbor {ipv4-address | ipv6-address} translate-update multicast [unicast]
end
show running-config

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

router bgp as-number
Example:

Enters router configuration mode and creates a BGP routing
process.

IP Routing: BGP Configuration Guide
1105


VRF Aware BGP Translate-Update
Configuration Examples for VRF Aware BGP Translate-Update

Command or Action

Purpose

Device(config)# router bgp 65000

Step 4

address-family ipv4 [mdt | tunnel | {multicast | unicast} Enters address family configuration mode to configure a
routing session using standard IP Version 4 (IPv4) address
[vrf vrf-name] | vrf vrf-name]
prefixes.
Example:
Device(config)# address-family ipv4 vrf v1

Step 5

no neighbor {ipv4-address | ipv6-address}
translate-update multicast [unicast]

Disables multicast routing on devices, which are not capable
of multicast BGP (mBGP) routing.

Example:
Device(config-af)# no neighbor 10.1.1.1
translate-update multicast unicast

Step 6

Returns to privileged EXEC mode.

end
Example:
Device(config-af)# end

Step 7

show running-config

Displays the running configuration on the device.

Example:
Device# show running-config

Configuration Examples for VRF Aware BGP Translate-Update
Example: Configuring VRF aware BGP Translate-Update
The following example shows how to configure the translate-update feature for an IPv4 VRF
address-family named v1 and BGP neighbor n2 peer-group for VRF configuration:

Note

Peer-template configuration for BGP neighbor is not supported for this feature due to conflicts with
the earlier versions of Cisco software.

Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# address-family ipv4 vrf v1
Device(config-router-af)# neighbor n2 peer-group
Device(config-router-af)# neighbor n2 remote-as 4
Device(config-router-af)# neighbor 10.1.1.1 peer-group n2
Device(config-router-af)# neighbor 10.1.1.1 activate

IP Routing: BGP Configuration Guide
1106


VRF Aware BGP Translate-Update
Example: Configuring VRF aware BGP Translate-Update

Device(config-router-af)# neighbor 10.1.1.1 translate-update multicast unicast
Device(config-router-af)# end

The following is sample output from the show bgp vpnv4 multicast vrf command. As the VRF
aware BGP translate-update feature is configured, the state of the neighbor displays “NoNeg”:
Device# show bgp vpnv4 multicast vrf v1 summary
BGP router identifier 10.1.3.1, local AS number 65000
BGP table version is 8, main routing table version 8
7 network entries using 1792 bytes of memory
8 path entries using 960 bytes of memory
5/3 BGP path/bestpath attribute entries using 1280 bytes of memory
3 BGP AS-PATH entries using 88 bytes of memory
2 BGP extended community entries using 48 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 4168 total bytes of memory
BGP activity 23/2 prefixes, 33/9 paths, scan interval 60 secs
Neighbor
10.1.1.1

V
4

AS MsgRcvd MsgSent
4
5
10

10.1.3.2

4

2

12

10

TblVer
1
8

InQ OutQ Up/Down State/PfxRcd
0
0 00:01:10 (NoNeg)
0

0 00:01:33

The following is sample output from the show ip route multicast vrf command:

Note

The routes configured using the translate-update feature does not have the “+” symbol against the
prefixes in the Routing Information Base (RIB) table. Appearance of the symbol in the first entry
indicates that the unicast route has leaked into the multicast table. However, the second entry is a
translate-update route, which appears to be a multicast route.

Device# show ip route multicast vrf v1
B
B

+

10.1.1.0/24 [20/0] via 10.1.1.1 (v1), 00:00:08
10.1.1.0/24 [20/0] via 10.1.1.1 (v1), 00:00:42

The following is sample output from the show running-config command:

Note

The provider-edge (PE) device must activate its BGP neighbor under the multicast address-family
even though the neighbor is not capable of multicast routing. If the unicast address-family identifier
has the route-map configured and multicast address-family identifier has no route-map configured,
the unicast route-map controls the route under the unicast table but not the route under multicast
table.

Device# show running-config
address-family ipv4 vrf v1
redistribute connected
redistribute static
neighbor 10.1.1.1 remote-as 4
neighbor 10.1.1.1 activate

IP Routing: BGP Configuration Guide
1107


VRF Aware BGP Translate-Update
Example: Configuring VRF aware BGP Translate-Update

neighbor 10.1.1.1 translate-update multicast unicast
neighbor 10.1.1.1 remote-as 4
neighbor 10.1.1.1 activate
exit-address-family
!
address-family ipv4 multicast vrf v1
redistribute connected
redistribute static
neighbor 10.1.1.1 remote-as 4
neighbor 10.1.1.1 activate
neighbor 10.1.1.1 soft-reconfiguration inbound
neighbor 10.1.1.1 route-map x in
exit-address-family

Note

The “neighbor 10.1.1.1 soft-reconfiguration inbound” and the “ neighbor 10.1.1.1 route-map x in”
field in the output indicate that only the routes in the BGP multicast table are affected.
The following is sample output from the show running-config command when you configure a
neighbor under different address-families:

Note

Configuring the BGP neighbor under different address-families manipulates the unicast routes and
multicast routes advertised to the neighbor.
Configuration for IPv4/IPv6 unicast address-family:
Device# show running-config
address-family ipv4
neighbor 20.2.2.1 activate
neighbor 20.2.2.1 translate-update multicast unicast
exit-address-family
!
address-family ipv4 multicast
neighbor 20.2.2.1 activate
exit-address-family
!

Configuration for IPv4/IPv6 VRF unicast address-family:
Device# show running-config
address-family ipv4 vrf v1
neighbor 20.2.2.1 remote-as 4
neighbor 20.2.2.1 activate
neighbor 20.2.2.1 translate-update multicast unicast
exit-address-family
!
address-family ipv4 multicast vrf v1
neighbor 20.2.2.1 remote-as 4
neighbor 20.2.2.1 activate
exit-address-family
!

IP Routing: BGP Configuration Guide
1108


VRF Aware BGP Translate-Update
Example: Removing VRF aware BGP Translate-Update Configuration

The following is sample configuration of the translate-update feature from a device with the old
version of Cisco Software. The neighbor, in this case, is configured for IPv4/IPv6 unicast
address-family, without running the address-family command:
Configuration in the old format, without an address-family configured:
Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# neighbor 20.2.2.1 remote-as 4
Device(config-router)# neighbor 20.2.2.1 translate-update nlri ipv4 multicast unicast
Device(config-router-af)# end

Configuration in the new format, without an address-family configured:
Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# neighbor 20.2.2.1 remote-as 4
Device(config-router)# neighbor 20.2.2.1 translate-update nlri multicast unicast
Device(config-router-af)# end

Example: Removing VRF aware BGP Translate-Update Configuration
The following example shows how to disable the VRF aware BGP translate-update feature for an
IPv4 VRF address-family named v1 and BGP neighbor n2 peer-group for VRF:

Note

Disabling the translate-update configuration for a neighbor deletes the pseudo multicast neighbor
and flaps the session, similar to removing the neighbor from a multicast session:

Device> enable
Device# configure terminal
Device(config)# router bgp 65000
Device(config-router)# address-family ipv4 vrf v1
Device(config-router-af)# no neighbor 10.1.1.1 translate-update multicast unicast
Device(config-router-af)# end

The following output displays the debug logs after you disable the translate-update feature on the
neighbor:
*Nov 20 07:09:15.902: %BGP_SESSION-5-ADJCHANGE:
neighbor 2.2.2.1 IPv4 Multicast vpn vrf v1 topology base removed from session Neighbor
deleted
*Nov 20 07:09:15.902: %BGP-5-ADJCHANGE:
neighbor 2.2.2.1 vpn vrf v1 Down Neighbor deleted
*Nov 20 07:09:15.902: %BGP_SESSION-5-ADJCHANGE:
neighbor 2.2.2.1 IPv4 Unicast vpn vrf v1 topology base removed from session Neighbor deleted
*Nov 20 07:09:16.877: %BGP-5-ADJCHANGE:
neighbor 2.2.2.1 vpn vrf v1 Up

The following is sample output from the show running-config command:

IP Routing: BGP Configuration Guide
1109


VRF Aware BGP Translate-Update
Additional References for VRF Aware BGP Translate-Update

Note

The associated neighbor 10.1.1.1 is removed even from the nonvolatile generation (NVGEN) after
translate-update is disabled on that neighbor.

Device# show running-config
address-family ipv4 vrf v1
redistribute connected
redistribute static
neighbor 10.1.1.1 remote-as 4
neighbor 10.1.1.1 activate
exit-address-family
!
address-family ipv4 multicast vrf v1
redistribute connected
redistribute static
exit-address-family

Additional References for VRF Aware BGP Translate-Update
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Command List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

Technical Assistance
Description

Link

The Cisco Support website provides extensive online resources, including
documentation and tools for troubleshooting and resolving technical issues
with Cisco products and technologies.

http://www.cisco.com/support

To receive security and technical information about your products, you can
subscribe to various services, such as the Product Alert Tool (accessed from
Field Notices), the Cisco Technical Services Newsletter, and Really Simple
Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website requires a Cisco.com user
ID and password.

Feature Information for VRF Aware BGP Translate-Update
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.

IP Routing: BGP Configuration Guide
1110


VRF Aware BGP Translate-Update
Feature Information for VRF Aware BGP Translate-Update

Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 100: Feature Information for VRF Aware BGP Translate-Update

Feature Name

Releases

Feature Information

VRF aware BGP
Translate-Update

Cisco IOS XE Release 3.11S

The VRF aware BGP
translate-update feature
enables multicast forwarding
on those customer-edge (CE)
devices, which have an older
version of Cisco software that
does not support multicast
BGP (mBGP) routing.
The following command was
introduced:
neighbor translate-update

IP Routing: BGP Configuration Guide
1111


VRF Aware BGP Translate-Update
Feature Information for VRF Aware BGP Translate-Update

IP Routing: BGP Configuration Guide
1112
