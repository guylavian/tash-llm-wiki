---
title: "PBR Next-Hop Verify Availability for VRF"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-pbr-next-hop-verify-availability-for-vrf
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 16 PBR Next-Hop Verify Availability for VRF The PBR Next-Hop Verify Availability for VRF feature enables verification of next-hop availability for IPv4/IPv6 packets in virtual routing and forwarding (VRF) instances. • Finding Feature Information, on page 163 • Information About PBR Next-Hop Verify Availability for VRF, on page 163 • How to Configure PBR Next-Hop Verify Availability for V"
---

# PBR Next-Hop Verify Availability for VRF

CHAPTER

16

PBR Next-Hop Verify Availability for VRF
The PBR Next-Hop Verify Availability for VRF feature enables verification of next-hop availability for
IPv4/IPv6 packets in virtual routing and forwarding (VRF) instances.
• Finding Feature Information, on page 163
• Information About PBR Next-Hop Verify Availability for VRF, on page 163
• How to Configure PBR Next-Hop Verify Availability for VRF, on page 164
• Configuration Examples for PBR Next-Hop Verify Availability for VRF, on page 173
• Additional References for PBR Next-Hop Verify Availability for VRF, on page 175
• Feature Information for PBR Next-Hop Verify Availability for VRF, on page 175

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Information About PBR Next-Hop Verify Availability for VRF
PBR Next-Hop Verify Availability for VRF Overview
Cisco IOS policy-based routing (PBR) defines packet matching and classification specifications, sets action
policies, which can modify the attributes of IP packets, and overrides normal destination IP address-based
routing and forwarding. PBR can be applied on global interfaces and under multiple routing instances. The
PBR Next-Hop Verify Availability for VRF feature enables verification of next-hop availability for IPv4/IPv6
packets under virtual routing and forwarding (VRF) instances.
In case of an inherited VRF, the VRF instance is based on the ingress interface. Inter VRF refers to forwarding
of packets from one VRF to another VRF; for example, from VRFx to VRFy. An IPv4/IPv6 packet received
from VRFx is forwarded to VRFy and the availability of the next hop is verified in the VRFy instance.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
163


PBR Next-Hop Verify Availability for VRF
How to Configure PBR Next-Hop Verify Availability for VRF

How to Configure PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inherited IP VRF
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
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.

enable
configure terminal
ip vrf vrf-name
rd vpn-route-distinguisher
route-target export route-target-ext-community
route-target import route-target-ext-community
exit
ip sla operation-number
icmp-echo destination-ip-address
vrf vrf-name
exit
ip sla schedule operation-number life forever start-time now
track object-number ip sla operation-number
interface type number
ip vrf forwarding vrf-name
ip address ip-address subnet-mask
exit
route-map map-tag [permit | deny] [sequence-number] [
set ip vrf vrf-name next-hop verify-availability next-hop-address sequence track object
exit
interface type number
ip vrf forwarding vrf-name
ip policy route-map map-tag
ip address ip-address subnet-mask
end

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

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
164


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inherited IP VRF

Step 3

Command or Action

Purpose

ip vrf vrf-name

Configures an IP VPN routing and forwarding instance
and enters VRF configuration mode.

Example:
Device(config)# ip vrf RED

Step 4

Specifies the route distinguisher. The route distinguisher
is either an autonomous system (AS) number or an IP
address.

rd vpn-route-distinguisher
Example:
Device(config-vrf)# rd 100:1

Step 5

route-target export route-target-ext-community
Example:
Device(config-vrf)# route-target export 100:1

Step 6

route-target import route-target-ext-community
Example:
Device(config-vrf)# route-target import 100:1

Step 7

Creates a route-target extended community for a VRF and
exports routing information from the target VPN extended
community. The route-target-ext-community argument is
either an AS number or an IP address.
Creates a route-target extended community for a VRF and
imports routing information from the target VPN extended
community. The route-target-ext-community argument is
either an AS number or an IP address.
Exits VRF configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-vrf)# exit

Step 8

Configures a Cisco IOS IP Service Level Agreements
(SLAs) operation and enters IP SLA configuration mode.

ip sla operation-number
Example:
Device(config)# ip sla 1

Step 9

Configures an IP SLAs Internet Control Message Protocol
(ICMP) echo operation and enters ICMP echo
configuration mode.

icmp-echo destination-ip-address
Example:
Device(config-ip-sla)# icmp-echo 10.0.0.4

Step 10

Configures IP SLAs for a VRF instance.

vrf vrf-name
Example:
Device(config-ip-sla-echo)# vrf RED

Step 11

Exits ICMP echo configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-ip-sla-echo)# exit

Step 12

ip sla schedule operation-number life forever start-time Configures the scheduling parameters for a single Cisco
IOS IP SLAs operation.
now
Example:
Device(config)# ip sla schedule 1 life forever
start-time now

Step 13

track object-number ip sla operation-number
Example:

Tracks the state of a Cisco IOS IP SLAs operation and
enters tracking configuration mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
165


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inherited IP VRF

Command or Action

Purpose

Device(config)# track 1 ip sla 1

Step 14

interface type number
Example:

Specifies the interface type and number and enters interface
configuration mode.

Device(config-track)# interface Ethernet1/0

Step 15

ip vrf forwarding vrf-name

Configures the forwarding table.

Example:
Device(config-if)# ip vrf forwarding RED

Step 16

ip address ip-address subnet-mask

Specifies the IP address and subnet mask for the interface.

Example:
Device(config-if)# ip address 10.0.0.2 255.0.0.0

Step 17

exit
Example:

Exits interface configuration mode and returns to global
configuration mode.

Device(config-if)# exit

Step 18

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. .
[
Example:
Device(config)# route-map alpha permit
ordering-seq

Step 19

set ip vrf vrf-name next-hop verify-availability
next-hop-address sequence track object
Example:

Configures policy routing to verify the reachability of the
next hop of a route map before the router performs policy
routing to that next hop.

Device(config-route-map)# set ip vrf RED next-hop
verify-availability 192.168.23.2 1 track 1

Step 20

exit
Example:

Exits route-map configuration mode and returns to global
configuration mode.

Device(config-route-map)# exit

Step 21

interface type number
Example:

Specifies the interface type and number and enters interface
configuration mode.

Device(config)# interface Ethernet0/0

Step 22

ip vrf forwarding vrf-name

Configures the forwarding table.

Example:
Device(config-if)# ip vrf forwarding RED

Step 23

ip policy route-map map-tag
Example:

Identifies a route map to use for policy routing on an
interface.

Device(config-if)# ip policy route-map test02

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
166


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inherited IPv6 VRF

Step 24

Command or Action

Purpose

ip address ip-address subnet-mask

Specifies the IP address and subnet mask for the interface.

Example:
Device(config-if)# ip address 192.168.10.2
255.255.255.0

Step 25

Returns to privileged EXEC mode.

end
Example:
Device(config-if)# exit

Configuring PBR Next-Hop Verify Availability for Inherited IPv6 VRF
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
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.
26.
27.

enable
configure terminal
ip vrf vrf-name
rd vpn-route-distinguisher
route-target export route-target-ext-community
route-target import route-target-ext-community
exit
ip sla operation-number
icmp-echo destination-ip-address
vrf vrf-name
exit
ip sla schedule operation-number life forever start-time now
track object-number ip sla operation-number
interface type number
ip vrf forwarding vrf-name
ip address ip-address subnet-mask
ipv6 address ipv6-prefix
exit
route-map map-tag [permit | deny] [sequence-number] [
set ipv6 vrf vrf-name next-hop verify-availability next-hop-address sequence track object
exit
interface type number
ip vrf forwarding vrf-name
ipv6 policy route-map map-tag
ip address ip-address subnet-mask
ipv6 address ipv6-prefix
end

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
167


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inherited IPv6 VRF

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

ip vrf vrf-name
Example:

Configures an IP VPN routing and forwarding instance
and enters VRF configuration mode.

Device(config)# ip vrf RED

Step 4

rd vpn-route-distinguisher
Example:

Specifies the route distinguisher. The route distinguisher
is either an autonomous system (AS) number or an IP
address.

Device(config-vrf)# rd 100:1

Step 5

route-target export route-target-ext-community
Example:
Device(config-vrf)# route-target export 100:1

Step 6

route-target import route-target-ext-community
Example:
Device(config-vrf)# route-target import 100:1

Step 7

exit
Example:

Creates a route-target extended community for a VRF and
exports routing information from the target VPN extended
community. The route-target-ext-community argument is
either an AS number or an IP address.
Creates a route-target extended community for a VRF and
imports routing information from the target VPN extended
community. The route-target-ext-community argument is
either an AS number or an IP address.
Exits VRF configuration mode and returns to global
configuration mode.

Device(config-vrf)# exit

Step 8

ip sla operation-number
Example:

Configures a Cisco IOS IP Service Level Agreements
(SLAs) operation and enters IP SLA configuration mode.

Device(config)# ip sla 1

Step 9

icmp-echo destination-ip-address
Example:

Configures an IP SLAs Internet Control Message Protocol
(ICMP) echo operation and enters ICMP echo
configuration mode.

Device(config-ip-sla)# icmp-echo 10.0.0.4

Step 10

vrf vrf-name

Configures IP SLAs for a VRF instance.

Example:
Device(config-ip-sla-echo)# vrf RED

Step 11

exit
Example:

Exits ICMP echo configuration mode and returns to global
configuration mode.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
168


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inherited IPv6 VRF

Command or Action

Purpose

Device(config-ip-sla-echo)# exit

Step 12

ip sla schedule operation-number life forever start-time Configures the scheduling parameters for a single Cisco
IOS IP SLAs operation.
now
Example:
Device(config)# ip sla schedule 1 life forever
start-time now

Step 13

track object-number ip sla operation-number
Example:

Tracks the state of a Cisco IOS IP SLAs operation and
enters tracking configuration mode.

Device(config)# track 1 ip sla 1

Step 14

Specifies the interface type and number and enters interface
configuration mode.

interface type number
Example:
Device(config-track)# interface Ethernet1/0

Step 15

Configures the forwarding table.

ip vrf forwarding vrf-name
Example:
Device(config-if)# ip vrf forwarding RED

Step 16

ip address ip-address subnet-mask

Specifies the IP address and subnet mask for the interface.

Example:
Device(config-if)# ip address 10.0.0.2 255.0.0.0

Step 17

Specifies the IPv6 prefix.

ipv6 address ipv6-prefix
Example:
Device(config-if)# ipv6 address 2001:DB8::/48

Step 18

Exits interface configuration mode and returns to global
configuration mode.

exit
Example:
Device(config-if)# exit

Step 19

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed. .
[
Example:
Device(config)# route-map alpha permit
ordering-seq

Step 20

set ipv6 vrf vrf-name next-hop verify-availability
next-hop-address sequence track object
Example:

Configures policy routing to verify the reachability of the
next hop of a route map before the router performs policy
routing to that next hop.

Device(config-route-map)# set ipv6 vrf RED
next-hop verify-availability 2001:DB8:1::1 1 track
1

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
169


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inter VRF

Step 21

Command or Action

Purpose

exit

Exits route-map configuration mode and returns to global
configuration mode.

Example:
Device(config-route-map)# exit

Step 22

interface type number
Example:

Specifies the interface type and number and enters interface
configuration mode.

Device(config)# interface Ethernet0/0

Step 23

ip vrf forwarding vrf-name

Configures the forwarding table.

Example:
Device(config-if)# ip vrf forwarding RED

Step 24

ipv6 policy route-map map-tag
Example:

Identifies a route map to use for policy routing on an
interface.

Device(config-if)# ipv6 policy route-map test02

Step 25

ip address ip-address subnet-mask

Specifies the IP address and subnet mask for the interface.

Example:
Device(config-if)# ip address 192.168.10.2
255.255.255.0

Step 26

ipv6 address ipv6-prefix

Specifies the IPv6 prefix.

Example:
Device(config-if)# ipv6 address 2001:DB8::/32

Step 27

Returns to privileged EXEC mode.

end
Example:
Device(config-if)# end

Configuring PBR Next-Hop Verify Availability for Inter VRF
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

enable
configure terminal
ip vrf vrf-name
rd vpn-route-distinguisher
route-target export route-target-ext-community
ip vrf vrf-name
no rd vpn-route-distinguisher
rd vpn-route-distinguisher
route-target export route-target-ext-community
interface type number

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
170


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inter VRF

11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.

ip vrf forwarding vrf-name
ip address ip-address subnet-mask
ip policy route-map map-tag
interface type number
ip vrf forwarding vrf-name
ip address ip-address subnet-mask
exit
ip route vrf vrf-name prefix mask interface-type interface-number ip-address
ip route vrf vrf-name prefix mask ip-address
Repeat Step 19 to establish additional static routes.
route-map map-tag [permit | deny] [sequence-number] [ sequence-name
match interface interface-type interface-number
set ip vrf vrf-name next-hop verify-availability next-hop-address sequence track object
end

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

Enters global configuration mode.

configure terminal
Example:
Device# configure terminal

Step 3

Configures an IP VPN routing and forwarding instance
and enters VRF configuration mode.

ip vrf vrf-name
Example:
Device(config)# ip vrf BLUE

Step 4

Specifies the route distinguisher. The route distinguisher
is either an autonomous system (AS) number or an IP
address.

rd vpn-route-distinguisher
Example:
Device(config-vrf)# rd 800:1

Step 5

route-target export route-target-ext-community
Example:
Device(config-vrf)# route-target export 800:1

Step 6

Creates a route-target extended community for a VRF and
exports routing information from the target VPN extended
community. The route-target-ext-community argument is
either an AS number or an IP address.
Configures an IP VPN routing and forwarding instance.

ip vrf vrf-name
Example:
Device(config-vrf)# ip vrf BLUE

Step 7

Removes the specified route distinguisher.

no rd vpn-route-distinguisher
Example:
Device(config-vrf)# no rd 800:1

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
171


PBR Next-Hop Verify Availability for VRF
Configuring PBR Next-Hop Verify Availability for Inter VRF

Step 8

Command or Action

Purpose

rd vpn-route-distinguisher

Specifies the route distinguisher. The route distinguisher
is either an AS number or an IP address.

Example:
Device(config-vrf)# rd 900:1

Step 9

route-target export route-target-ext-community
Example:
Device(config-vrf)# route-target export 900:1

Step 10

interface type number
Example:

Creates a route-target extended community for a VRF and
exports routing information from the target VPN extended
community. The route-target-ext-community argument is
either an AS number or an IP address.
Specifies the interface type and number and enters interface
configuration mode.

Device(config-vrf)# interface Ethernet0/0

Step 11

ip vrf forwarding vrf-name

Configures the forwarding table.

Example:
Device(config-if)# ip vrf forwarding RED

Step 12

ip address ip-address subnet-mask

Specifies the IP address and subnet mask for the interface.

Example:
Device(config-if)# ip address 192.168.10.2
255.255.255.0

Step 13

ip policy route-map map-tag
Example:

Identifies a route map to use for policy routing on an
interface.

Device(config-if)# ip policy route-map test00

Step 14

interface type number

Specifies the interface type and number.

Example:
Device(config-if)# interface Ethernet0/1

Step 15

ip vrf forwarding vrf-name

Configures the forwarding table.

Example:
Device(config-if)# ip vrf forwarding BLUE

Step 16

ip address ip-address subnet-mask

Specifies the IP address and subnet mask for the interface.

Example:
Device(config-if)# ip address 192.168.21.1
255.255.255.0

Step 17

exit
Example:

Exits interface configuration mode and returns to global
configuration mode.

Device(config-if)# exit

Step 18

ip route vrf vrf-name prefix mask interface-type
interface-number ip-address

Establishes static routes.

Example:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
172


PBR Next-Hop Verify Availability for VRF
Configuration Examples for PBR Next-Hop Verify Availability for VRF

Command or Action

Purpose

Device(config)# ip route vrf BLUE 192.168.10.1
255.255.255.255 Ethernet0/0 192.168.10.1

Step 19

ip route vrf vrf-name prefix mask ip-address

Establishes static routes.

Example:
Device(config)# ip route vrf BLUE 192.168.23.0
255.255.255.0 192.168.21.2

Step 20

Repeat Step 19 to establish additional static routes.

Step 21

route-map map-tag [permit | deny] [sequence-number] Configures a route map and specifies how the packets are
to be distributed..
[ sequence-name

—

Example:
Device(config)# route-map alpha permit
ordering-seq

Step 22

match interface interface-type interface-number
Example:

Distributes any routes that have their next hop as one of
the specified interfaces.

Device(config-route-map)# match interface
Ethernet0/0

Step 23

set ip vrf vrf-name next-hop verify-availability
next-hop-address sequence track object
Example:

Configures policy routing to verify the reachability of the
next hop of a route map of a VRF instance before the router
performs policy routing to that next hop.

Device(config-route-map)# set ip vrf BLUE next-hop
verify-availability 192.168.23.2 1 track 1

Step 24

Returns to privileged EXEC mode.

end
Example:
Device(config-route-map)# end

Configuration Examples for PBR Next-Hop Verify Availability
for VRF
Example: Configuring PBR Next-Hop Verify Availability for Inherited IP VRF
Device> enable
Device# configure terminal
Device(config)# ip vrf RED
Device(config-vrf)# rd 100:1
Device(config-vrf)# route-target export 100:1
Device(config-vrf)# route-target import 100:1
Device(config-vrf)# exit
Device(config)# ip sla 1
Device(config-ip-sla)# icmp-echo 10.0.0.4

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
173


PBR Next-Hop Verify Availability for VRF
Example: Configuring PBR Next-Hop Verify Availability for Inherited IPv6 VRF

Device(config-ip-sla-echo)# vrf RED
Device(config-ip-sla-echo)# exit
Device(config)# ip sla schedule 1 life forever start-time now
Device(config)# track 1 ip sla 1
Device(config-track)# interface Ethernet0/0
Device(config-if)# ip vrf forwarding RED
Device(config-if)# ip address 10.0.0.2 255.0.0.0
Device(config-if)# exit
Device(config)# route-map test02 permit 10
Device(config-route-map)# set ip vrf RED next-hop verify-availability 192.168.23.2 1 track
1
Device(config-route-map)# interface Ethernet0/0
Device(config-if)# ip vrf forwarding RED
Device(config-if)# ip policy route-map test02
Device(config-if)# ip address 192.168.10.2 255.255.255.0
Device(config-if)# end

Example: Configuring PBR Next-Hop Verify Availability for Inherited IPv6 VRF
Device> enable
Device# configure terminal
Device(config)# ip vrf RED
Device(config-vrf)# rd 100:1
Device(config-vrf)# route-target export 100:1
Device(config-vrf)# route-target import 100:1
Device(config-vrf)# exit
Device(config)# ip sla 1
Device(config-ip-sla)# icmp-echo 10.0.0.4
Device(config-ip-sla-echo)# vrf RED
Device(config-ip-sla-echo)# exit
Device(config)# ip sla schedule 1 life forever start-time now
Device(config)# track 1 ip sla 1
Device(config-track)# interface Ethernet0/0
Device(config-if)# ip vrf forwarding RED
Device(config-if)# ip policy route-map test02
Device(config-if)# ip address 192.168.10.2 255.255.255.0
Device(config-if)# ipv6 address 2001:DB8::/32
Device(config-if)# interface Ethernet1/0
Device(config-if)# ip vrf forwarding RED
Device(config-if)# ip address 10.0.0.2 255.0.0.0
Device(config-if)# ipv6 address 2001:DB8::/48
Device(config-if)# exit
Device(config)# route-map test02 permit 10
Device(config-route-map)# set ipv6 vrf RED next-hop verify-availability 2001:DB8:1::1 1
track 1
Device(config-route-map)# end

Example: Configuring PBR Next-Hop Verify Availability for Inter VRF
Device> enable
Device# configure terminal
Device(config)# ip vrf BLUE
Device(config-vrf)# rd 800:1
Device(config-vrf)# route-target export 800:1
Device(config-vrf)# ip vrf BLUE
Device(config-vrf)# no rd 800:1
Device(config-vrf)# rd 900:1

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
174


PBR Next-Hop Verify Availability for VRF
Additional References for PBR Next-Hop Verify Availability for VRF

Device(config-vrf)# route-target export 900:1
Device(config-vrf)# interface Ethernet0/0
Device(config-if)# ip vrf forwarding RED
Device(config-if)# ip address 192.168.10.2 255.255.255.0
Device(config-if)# ip policy route-map test00
Device(config-if)# interface Ethernet0/1
Device(config-if)# ip vrf forwarding BLUE
Device(config-if)# ip address 192.168.21.1 255.255.255.0
Device(config-if)# exit
Device(config)# ip route vrf blue 192.168.10.1 255.255.255.255 Ethernet0/0 192.168.10.1
Device(config)# ip route vrf blue 192.168.23.0 255.255.255.0 192.168.21.2
Device(config)# route-map test00 permit 10
Device(config-route-map)# match interface Ethernet0/0
Device(config-route-map)# set ip vrf blue next-hop verify-availability 192.168.23.2 1 track
1
Device(config-route-map)# end

Additional References for PBR Next-Hop Verify Availability for
VRF
Related Documents
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

Feature Information for PBR Next-Hop Verify Availability for
VRF
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
175


PBR Next-Hop Verify Availability for VRF
Feature Information for PBR Next-Hop Verify Availability for VRF

Feature Name

Releases

PBR Next-Hop Verify Availability
for VRF

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
176

Feature Information
The PBR Next-Hop Verify
Availability for VRF feature
enables verification of next-hop
availability for IPv4/IPv6 packets
in virtual routing and forwarding
(VRF) instances.
