---
title: "Removing Private AS Numbers from the AS Path in BGP"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-removing-private-as-numbers-from-the-as-path-in-bgp
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 15 Removing Private AS Numbers from the AS Path in BGP Private autonomous system numbers (ASNs) are used by ISPs and customer networks to conserve globally unique AS numbers. Private AS numbers cannot be used to access the global Internet because they are not unique. AS numbers appear in eBGP AS paths in routing updates. Removing private ASNs from the AS path is necessary if you have bee"
---

# Removing Private AS Numbers from the AS Path in BGP

CHAPTER

15

Removing Private AS Numbers from the AS Path
in BGP
Private autonomous system numbers (ASNs) are used by ISPs and customer networks to conserve globally
unique AS numbers. Private AS numbers cannot be used to access the global Internet because they are not
unique. AS numbers appear in eBGP AS paths in routing updates. Removing private ASNs from the AS path
is necessary if you have been using private ASNs and you want to access the global Internet.
• Finding Feature Information, on page 357
• Restrictions on Removing and Replacing Private ASNs from the AS Path, on page 357
• Information About Removing and Replacing Private ASNs from the AS Path, on page 358
• How to Remove and Replace Private ASNs from the AS Path, on page 359
• Configuration Examples for Removing and Replacing Private ASNs from the AS Path, on page 362
• Additional References, on page 365
• Feature Information for Removing and Replacing Private ASNs from the AS Path, on page 366

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions on Removing and Replacing Private ASNs from the
AS Path
• The feature applies to eBGP neighbors only.
• The feature applies to routers in a public AS only. The workaround to this restriction would be to apply
the neighbor local-as command on a per-neighbor basis, with the local AS number being a public AS
number.

IP Routing: BGP Configuration Guide
357


Removing Private AS Numbers from the AS Path in BGP
Information About Removing and Replacing Private ASNs from the AS Path

Information About Removing and Replacing Private ASNs from
the AS Path
Public and Private AS Numbers
Public AS numbers are assigned by InterNIC and are globally unique. They range from 1 to 64511. Private
AS numbers are used to conserve globally unique AS numbers, and they range from 64512 to 65535. Private
AS numbers cannot be leaked to a global BGP routing table because they are not unique, and BGP best path
calculations require unique AS numbers. Therefore, it might be necessary to remove private AS numbers from
an AS path before the routes are propagated to a BGP peer.

Benefit of Removing and Replacing Private ASNs from the AS Path
External BGP requires that globally unique AS numbers be used when routing to the global Internet. Using
private AS numbers (which are not unique) would prevent access to the global Internet. This feature allows
routers that belong to a private AS to access the global Internet. A network administrator configures the routers
to remove private AS numbers from the AS path contained in outgoing update messages and optionally, to
replace those numbers with the ASN of the local router, so that the AS Path length remains unchanged.

Former Restrictions to Removing Private ASNs from the AS Path
The ability to remove private AS numbers from the AS path has been available for a long time. Prior to Cisco
IOS XE Release 3.1S, this feature had the following restrictions:
• If the AS path included both private and public AS numbers, using the neighbor remove-private-as
command would not remove the private AS numbers.
• If the AS path contained confederation segments, using the neighbor remove-private-as command
would remove private AS numbers only if the private AS numbers followed the confederation portion
of the autonomous path.
• If the AS path contained the AS number of the eBGP neighbor, the private AS numbers would not be
removed.

Enhancements to Removing Private ASNs from the AS Path
The ability to remove and replace private AS numbers from the AS path is enhanced in the following ways:
• The neighbor remove-private-as command will remove private AS numbers from the AS path even if
the path contains both public and private ASNs.
• The neighbor remove-private-as command will remove private AS numbers even if the AS path contains
only private AS numbers. There is no likelihood of a 0-length AS path because this command can be
applied to eBGP peers only, in which case the AS number of the local router is appended to the AS path.
• The neighbor remove-private-as command will remove private AS numbers even if the private ASNs
appear before the confederation segments in the AS path.

IP Routing: BGP Configuration Guide
358


Removing Private AS Numbers from the AS Path in BGP
How to Remove and Replace Private ASNs from the AS Path

• The replace-as keyword is available to replace the private AS numbers being removed from the path
with the local AS number, thereby retaining the same AS path length.
• The feature can be applied to neighbors per address family (address family configuration mode). Therefore,
you can apply the feature for a neighbor in one address family and not on another, affecting update
messages on the outbound side for only the address family for which the feature is configured.
• The feature can be applied in peer group template mode.
• When the feature is configured, output from the show ip bgp update-group and show ip bgp neighbor
commands indicates that private AS numbers were removed or replaced.

How to Remove and Replace Private ASNs from the AS Path
Removing and Replacing Private ASNs from the AS Path (Cisco IOS XE Release
3.1S and Later)
To remove private AS numbers from the AS path on the outbound side of an eBGP neighbor, perform the
following task. To also replace private AS numbers with the local router’s AS number, include the all replace-as
keywords in Step 17.
The examples in this task reflect the configuration for Router 2 in the scenario in the figure below.
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

enable
configure terminal
interface type number
ip address ip-address mask
exit
interface type number
ip address ip-address mask
exit
interface type number
ip address ip-address mask
exit
router bgp autonomous-system-number
network network-number
network network-number
neighbor {ip-address | ipv6-address[%]| peer-group-name} remote-as autonomous-system-number
neighbor {ip-address | ipv6-address[%]| peer-group-name} remote-as autonomous-system-number
neighbor {ip-address | peer-group-name} remove-private-as [all [replace-as]]
end
show ip bgp update-group
show ip bgp neighbors

IP Routing: BGP Configuration Guide
359


Removing Private AS Numbers from the AS Path in BGP
Removing and Replacing Private ASNs from the AS Path (Cisco IOS XE Release 3.1S and Later)

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Router> enable

Step 2

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

interface type number

Configures an interface.

Example:
Router(config)# interface gigabitethernet 0/0

Step 4

ip address ip-address mask

Sets a primary or secondary IP address for an interface.

Example:
Router(config-if)# ip address 172.30.1.1
255.255.0.0

Step 5

Returns to the next highest configuration mode.

exit
Example:
Router(config-if)# exit

Step 6

interface type number

Configures an interface.

Example:
Router(config)# interface serial 0/0

Step 7

ip address ip-address mask

Sets a primary or secondary IP address for an interface.

Example:
Router(config-if)# ip address 172.16.0.2
255.255.255.0

Step 8

Returns to the next highest configuration mode.

exit
Example:
Router(config-if)# exit

Step 9

interface type number
Example:
Router(config)# interface serial 1/0

IP Routing: BGP Configuration Guide
360

Configures an interface.


Removing Private AS Numbers from the AS Path in BGP
Removing and Replacing Private ASNs from the AS Path (Cisco IOS XE Release 3.1S and Later)

Step 10

Command or Action

Purpose

ip address ip-address mask

Sets a primary or secondary IP address for an interface.

Example:
Router(config-if)# ip address 192.168.0.1
255.255.255.0

Step 11

exit

Returns to the next highest configuration mode.

Example:
Router(config-if)# exit

Step 12

router bgp autonomous-system-number

Specifies a BGP instance.

Example:
Router(config)# router bgp 5

Step 13

network network-number

Specifies a network to be advertised by BGP.

Example:
Router(config-router)# network 172.30.0.0

Step 14

network network-number

Specifies a network to be advertised by BGP.

Example:
Router(config-router)# network 192.168.0.0

Step 15

Adds an entry to the routing table.
neighbor {ip-address | ipv6-address[%]|
peer-group-name} remote-as autonomous-system-number
• This example configures Router 3 as an eBGP
neighbor in private AS 65000.
Example:
Router(config-router)# neighbor 172.16.0.1
remote-as 65000

Step 16

Adds an entry to the routing table.
neighbor {ip-address | ipv6-address[%]|
peer-group-name} remote-as autonomous-system-number
• This example configures Router 1 as an eBGP
neighbor in public AS 1.
Example:
Router(config-router)# neighbor 192.168.0.2
remote-as 1

Step 17

neighbor {ip-address | peer-group-name}
remove-private-as [all [replace-as]]
Example:
Router(config-router)# neighbor 192.168.0.2
remove-private-as all replace-as

Removes private AS numbers from the AS Path in
outgoing updates.
• This example removes the private AS numbers from
the AS path in outgoing eBGP updates and replaces
them with 5, which is the public AS number of the
local router.

IP Routing: BGP Configuration Guide
361


Removing Private AS Numbers from the AS Path in BGP
Configuration Examples for Removing and Replacing Private ASNs from the AS Path

Step 18

Command or Action

Purpose

end

Ends the current configuration mode and returns to
privileged EXEC mode.

Example:
Router(config-router)# end

Step 19

show ip bgp update-group

(Optional) Displays information about BGP update groups.

Example:
Router# show ip bgp update-group

Step 20

show ip bgp neighbors

(Optional) Displays information about BGP neighbors.

Example:
Router# show ip bgp neighbors

Configuration Examples for Removing and Replacing Private
ASNs from the AS Path
Example Removing Private ASNs (Cisco IOS XE Release 3.1S)
In the example below, Router A has the neighbor remove-private-as command configured, which removes
private AS numbers in updates sent to the neighbor at 172.30.0.7. The subsequent show command asks for
information about the route to host 1.1.1.1. The output includes private AS numbers 65200, 65201, 65201 in
the AS path of 1001 65200 65201 65201 1002 1003 1003.
To prove that the private AS numbers were removed from the AS path, the show command on Router B also
asks for information about the route to host 1.1.1.1. The output indicates a shorter AS path of 100 1001 1002
1003 1003, which excludes private AS numbers 65200, 65201, and 65201. The 100 prepended in the path is
Router B’s own AS number.
Router A
router bgp 100
bgp log-neighbor-changes
neighbor 19.0.101.1 remote-as 1001
neighbor 172.30.0.7 remote-as 200
neighbor 172.30.0.7 remove-private-as all
no auto-summary
RouterA# show ip bgp 1.1.1.1
BGP routing table entry for 1.1.1.1/32, version 2
Paths: (1 available, best #1, table default)
Advertised to update-groups:
1
2
1001 65200 65201 65201 1002 1003 1003
19.0.101.1 from 19.0.101.1 (19.0.101.1)
Origin IGP, localpref 100, valid, external, best RouterA#

IP Routing: BGP Configuration Guide
362


Removing Private AS Numbers from the AS Path in BGP
Example Removing and Replacing Private ASNs (Cisco IOS XE Release 3.1S)

Router B (All Private ASNs Have Been Removed)
RouterB# show ip bgp 1.1.1.1
BGP routing table entry for 1.1.1.1/32, version 3
Paths: (1 available, best #1, table default)
Not advertised to any peer
100 1001 1002 1003 1003
172.30.0.6 from 172.30.0.6 (19.1.0.1)
Origin IGP, localpref 100, valid, external, best RouterB#

Example Removing and Replacing Private ASNs (Cisco IOS XE Release 3.1S)
In the following example, when Router A sends prefixes to the peer 172.30.0.7, all private ASNs in the AS
path are replaced with the router’s own ASN, which is 100.
Router A
router bgp 100
bgp log-neighbor-changes
neighbor 172.16.101.1 remote-as 1001
neighbor 172.16.101.1 update-source Loopback0
neighbor 172.30.0.7 remote-as 200
neighbor 172.30.0.7 remove-private-as all replace-as
no auto-summary

Router A receives 1.1.1.1 from peer 172.16.101.1 which has some private ASNs (65200, 65201, and 65201)
in the AS path list, as shown in the following output:
RouterA# show ip bgp 1.1.1.1
BGP routing table entry for 1.1.1.1/32, version 2
Paths: (1 available, best #1, table default)
Advertised to update-groups:
1
2
1001 65200 65201 65201 1002 1003 1003
172.16.101.1 from 172.16.101.1 (172.16.101.1)
Origin IGP, localpref 100, valid, external, best RouterA#

Because Router A is configured with neighbor 172.30.0.7 remove-private-as all replace-as, Router A sends
prefix 1.1.1.1 with all private ASNs replaced with 100:
Router B
RouterB# show ip bgp 1.1.1.1
BGP routing table entry for 1.1.1.1/32, version 3
Paths: (1 available, best #1, table default)
Not advertised to any peer
100 1001 100 100 100 1002 1003 1003
172.30.0.6 from 172.30.0.6 (192.168.1.2)
Origin IGP, localpref 100, valid, external, best RouterB#

Router B
router bgp 200
bgp log-neighbor-changes
neighbor 172.30.0.6 remote-as 100
no auto-summary

IP Routing: BGP Configuration Guide
363


Removing Private AS Numbers from the AS Path in BGP
Example Removing Private ASNs (Cisco IOS XE Release 2)

Example Removing Private ASNs (Cisco IOS XE Release 2)
In this example, Router 3 uses private ASN 65000. Router 1 and Router 2 use public ASNs AS 1 and AS 5
respectively.
The figure below illustrates Router 2 belonging to a service provider, with Router 1 and Router 3 as its clients.
Figure 35: Removing Private AS Numbers

In this example, Router 2, belonging to the Service Provider, removes private AS numbers as follows.
1. Router 3 advertises the network 10.0.0.0/24 with the AS path attribute 65000 to Router 2.
2. Router 2 receives the update from Router 3 and makes an entry for the network 10.0.0.0/24 in its routing
table with the next hop as 172.16.0.1 (serial interface S0 on Router 3).
3. Router 2 (service provider device), when configured with the neighbor 192.168.0.2 remove-private-as
command, strips off the private AS number and constructs a new update packet with its own AS number
as the AS path attribute for the 10.0.0.0/24 network and sends the packet to Router 1.
4. Router 1 receives the eBGP update for network 10.0.0.0/24 and makes an entry in its routing table with
the next hop as 192.168.0.1 (serial interface S1 on Router 2). The AS path attribute for this network as
seen on Router 1 is AS 5 (Router 2). Thus, the private AS numbers are prevented from entering the BGP
tables of the Internet.
The configurations of Router 3, Router 2, and Router 1 follow.
Router 3
interface gigabitethernet 0/0
ip address 10.0.0.1 255.255.255.0
!
interface Serial 0
ip address 172.16.0.1 255.255.255.0
!
router bgp 65000
network 10.0.0.0 mask 255.255.255.0

IP Routing: BGP Configuration Guide
364


Removing Private AS Numbers from the AS Path in BGP
Additional References

neighbor 172.16.0.2 remote-as 5
!---Configures Router 2 as an eBGP neighbor in public AS 5.
!
end

Router 2
interface gigabitethernet 0/0
ip address 172.30.1.1 255.255.0.0
!
interface Serial 0
ip address 172.16.0.2 255.255.255.0
!
interface Serial 1
ip address 192.168.0.1 255.255.255.0
!
router bgp 5
network 172.30.0.0
network 192.168.0.0
neighbor 172.16.0.1 remote-as 65000
!---Configures Router 3 as an eBGP neighbor in private AS 65000.
neighbor 192.168.0.2 remote-as 1
!---Configures Router 1 as an eBGP neighbor in public AS 1.
neighbor 192.168.0.2 remove-private-as
!---Removes the private AS numbers from outgoing eBGP updates.
!
end

Router 1
version 12.2
!
!
interface Serial 0
ip address 192.168.0.2 255.255.255.0
!
router bgp 1
neighbor 192.168.0.1 remote-as 5
!---Configures Router 2 as an eBGP neighbor in public AS 5.
!
end

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands Cisco IOS Master Commands List, All Releases
BGP commands

Cisco IOS IP Routing: BGP Command Reference

IP Routing: BGP Configuration Guide
365


Removing Private AS Numbers from the AS Path in BGP
Feature Information for Removing and Replacing Private ASNs from the AS Path

Standards
Standard Title
None

--

MIBs
MIB MIBs Link
None To locate and download MIBs for selected platforms, Cisco software releases, and feature sets, use
Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs
Technical Assistance
Description

Link

The Cisco Support website provides extensive online http://www.cisco.com/cisco/web/support/index.html
resources, including documentation and tools for
troubleshooting and resolving technical issues with
Cisco products and technologies.
To receive security and technical information about
your products, you can subscribe to various services,
such as the Product Alert Tool (accessed from Field
Notices), the Cisco Technical Services Newsletter, and
Really Simple Syndication (RSS) Feeds.
Access to most tools on the Cisco Support website
requires a Cisco.com user ID and password.

Feature Information for Removing and Replacing Private ASNs
from the AS Path
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn. An account on Cisco.com is not
required.

IP Routing: BGP Configuration Guide
366


Removing Private AS Numbers from the AS Path in BGP
Feature Information for Removing and Replacing Private ASNs from the AS Path

Table 31: Feature Information for BGP--Remove/Replace Private AS

Feature Name

Releases

BGP--Remove/Replace Cisco IOS XE
Private AS Filter
Release 3.1S

Feature Information
Private autonomous system (AS) numbers are used by ISPs and
customer networks to conserve globally unique AS numbers.
Private AS numbers cannot be used to access the globalInternet
because they are not unique. AS numbers appear in eBGP AS
paths in routing tables. Removing private AS numbers from the
AS path is necessary if you have been using private AS numbers
and you want to access the global Internet.
The following command is modified:
• neighbor remove-private-as

IP Routing: BGP Configuration Guide
367


Removing Private AS Numbers from the AS Path in BGP
Feature Information for Removing and Replacing Private ASNs from the AS Path

IP Routing: BGP Configuration Guide
368
