---
title: "BGP—Support for iBGP Local-AS"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-support-for-ibgp-local-as
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 73 BGP—Support for iBGP Local-AS Prior to the BGP—Support for iBGP Local-AS feature, the neighbor local-as command was used on a BGP speaker to change the AS negotiated for an eBGP neighbor and to modify the AS_PATH sent and/or received. The neighbor local-as command can now be used to do the same on an iBGP session. AS negotiation creates an iBGP session and we enable sending iBGP attri"
---

# BGP—Support for iBGP Local-AS

CHAPTER

73

BGP—Support for iBGP Local-AS
Prior to the BGP—Support for iBGP Local-AS feature, the neighbor local-as command was used on a BGP
speaker to change the AS negotiated for an eBGP neighbor and to modify the AS_PATH sent and/or received.
The neighbor local-as command can now be used to do the same on an iBGP session. AS negotiation creates
an iBGP session and we enable sending iBGP attributes (LOCAL_PREF, ORIGINATOR_ID, and
CLUSTER_LIST) over it, and accept this attributes when received from this session. This functionality is
useful when merging two autonomous systems into one.
• Finding Feature Information, on page 1047
• Restrictions for Support for iBGP Local-AS, on page 1047
• Information About Support for iBGP Local-AS, on page 1048
• Support for iBGP Local-AS, on page 1048
• Benefits of iBGP Local-AS, on page 1049
• How to Configure iBGP Local-AS, on page 1049
• Configuring iBGP Local-AS, on page 1049
• Configuration Examples for iBGP Local-AS, on page 1052
• Example: Configuring iBGP Local-AS, on page 1052
• Additional References for Support for iBGP Local-AS, on page 1052
• Feature Information for BGP—Support for iBGP Local-AS, on page 1053

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Restrictions for Support for iBGP Local-AS
• This feature is not supported for a peer that belongs to a confederation.
• Nonlocal-AS iBGP neighbors that are in a single AS are put into a separate update group from iBGP
neighbors that are configured with the iBGP Local-AS feature.

IP Routing: BGP Configuration Guide
1047


BGP—Support for iBGP Local-AS
Information About Support for iBGP Local-AS

• Two iBGP neighbors that are in two different autonomous systems and that are configured as iBGP
Local-AS neighbors are put into separate update groups.

Information About Support for iBGP Local-AS
Support for iBGP Local-AS
Prior to the Support for iBGP Local-AS feature, when a peer (or peer group) was configured with the neighbor
local-as command and the neighbor remote-as command that specified the same AS number, the session
would be negotiated as an iBGP session (this happens when the advertised ASes in both OPEN messages are
the same). However, updates were propagated as in an eBGP session (LOCAL_PREF, ORIGINATOR_ID
and CLUSTER_LIST were not propagated), and could cause errors if they were received via this session.
Thus, iBGP local-AS was not fully supported.
The Support for iBGP Local-AS feature means all those iBGP attributes are propogated. Additionally, as in
any iBGP session, the AS is not prepended in AS_PATH attribute when advertising routes to an iBGP local-as
session.
The figure below illustrates a scenario where this feature is being used to facilitate the merging of two
autonomous systems. The route reflector R3 and R4 belong to AS 1000; R1 and R6 belong to AS 3000. The
RR is configured with neighbor local-as 3000 and neighbor remote-as 3000 commands. Even though the
routers belong to two different autonomous systems, attributes like the LOCAL_PREF are preserved in the
updates from R6 to R4 and R6 to R1 (as show in the figure), and also in the updates from R4 to R1 and R4
to R6 (not shown in the figure).
Figure 91: Support for iBGP Local-AS to Preserve iBGP Policies Between Two Autonomous Systems

IP Routing: BGP Configuration Guide
1048


BGP—Support for iBGP Local-AS
Benefits of iBGP Local-AS

Benefits of iBGP Local-AS
This feature is used when merging two ISPs that have different autonomous system numbers. It is desirable
to preserve attributes that are considered internal (LOCAL_PREF, ORIGINATOR_ID, and CLUSTER_LIST)
in the routes that are being propogated to other autonomous system.

How to Configure iBGP Local-AS
Configuring iBGP Local-AS
Configure the iBGP Local-AS feature on a BGP speaker for a given neighbor when you want that session to
behave as a full iBGP session. This configuration is typically performed on a route reflector, but not exclusively
on it. In a route reflector you can optionally configure changing iBGP attributes sent to a neighbor via the
command allow-policy (this command is not exclusive for this feature and can be used on any RR).
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

enable
configure terminal
ipv6 unicast-routing
router bgp autonomous-system-number
neighbor peer-group-name peer-group
neighbor {ip-address | ipv6-address} peer-group peer-group-name
neighbor {ip-address | ipv6-address | peer-group} remote-as as-number
neighbor {ip-address | ipv6-address | peer-group} local-as as-number
neighbor {ip-address | ipv6-address | peer-group} route-reflector-client
address-family vpnv4
neighbor {ip-address | ipv6-address | peer-group} allow-policy
exit
address-family vpnv6
neighbor {ip-address | ipv6-address | peer-group} allow-policy
end
show ip bgp vpnv4 all neighbors {ip-address | ipv6-address} policy
show ip bgp vpnv4 all update-group update-group
show ip bgp vpnv4 all neighbors {ip-address | ipv6-address}

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:

• Enter your password if prompted.

Device> enable

IP Routing: BGP Configuration Guide
1049


BGP—Support for iBGP Local-AS
Configuring iBGP Local-AS

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Device# configure terminal

Step 3

ipv6 unicast-routing

Enables the forwarding of IPv6 unicast datagrams.

Example:
Device(config)# ipv6 unicast-routing

Step 4

router bgp autonomous-system-number
Example:

Enters router configuration mode to create or configure a
BGP routing process.

Device(config)# router bgp 1000

Step 5

neighbor peer-group-name peer-group

(Optional) Identifies a peer group.

Example:
Device(config-router)# neighbor rr-client-ab
peer-group

Step 6

neighbor {ip-address | ipv6-address} peer-group
peer-group-name

(Optional) Configures a BGP neighbor to be a member of
a peer group.

Example:
Device(config-router)# neighbor 192.168.3.3
peer-group rr-client-ab

Step 7

neighbor {ip-address | ipv6-address | peer-group}
remote-as as-number

Identifies the AS of the neighbor or peer group.

Example:
Device(config-router)# neighbor rr-client-ab
remote-as 3000

Step 8

neighbor {ip-address | ipv6-address | peer-group} local-as Configures the local-AS feature for the neighbor or peer
group.
as-number
Example:
Device(config-router)# neighbor rr-client-ab
local-as 3000

Step 9

neighbor {ip-address | ipv6-address | peer-group}
route-reflector-client

Configures the local device to be a route reflector and
configures the neighbor or peer group to be its client.

Example:
Device(config-router)# neighbor rr-client-ab
route-reflector-client

Step 10

address-family vpnv4
Example:
Device(config-router)# address-family vpnv4

IP Routing: BGP Configuration Guide
1050

(Optional) Places the router in VPNv4 address family
configuration mode.


BGP—Support for iBGP Local-AS
Configuring iBGP Local-AS

Step 11

Command or Action

Purpose

neighbor {ip-address | ipv6-address | peer-group}
allow-policy

(Optional) Allows the RR to be configured to change iBGP
attributes for the specified neighbor or peer group.

Example:
Device(config-router-af)# neighbor rr-client-ab
allow-policy

Step 12

exit
Example:

Exits address family configuration mode and enters router
configuration mode.

Device(config-router-af)# exit

Step 13

address-family vpnv6
Example:

(Optional) Places the router in VPNv6 address family
configuration mode.

Device(config-router)# address-family vpnv6

Step 14

neighbor {ip-address | ipv6-address | peer-group}
allow-policy

(Optional) Allows the RR to be configured to change iBGP
attributes for the specified neighbor or peer group.

Example:
Device(config-router-af)# neighbor rr-client-ab
allow-policy

Step 15

end
Example:

Exits address family configuration mode, and enters
privileged EXEC mode.

Device(config-router-af)# end

Step 16

show ip bgp vpnv4 all neighbors {ip-address |
ipv6-address} policy
Example:
Device# show ip bgp vpnv4 all neighbors
192.168.3.3 policy

Step 17

show ip bgp vpnv4 all update-group update-group
Example:
Device# show ip bgp vpnv4 all update-group 2

Step 18

show ip bgp vpnv4 all neighbors {ip-address |
ipv6-address}
Example:
Device# show ip bgp vpnv4 all neighbors
192.168.3.3

(Optional) Displays the locally configured policies of the
neighbor.
• The output includes the phrase “allow-policy” if the
neighbor allow-policy command was configured for
that neighbor.
(Optional) Displays the information for the update group.
• The output includes the phrase “Allow-policy” if the
neighbor allow-policy command was configured for
neighbors in the update group.
(Optional) Displays information about the neighbor.
• The output includes the remote AS and local AS,
which will indicate the same AS number when the
Support for iBGP Local-AS feature is configured.

IP Routing: BGP Configuration Guide
1051


BGP—Support for iBGP Local-AS
Configuration Examples for iBGP Local-AS

Configuration Examples for iBGP Local-AS
Example: Configuring iBGP Local-AS
The example configures a route reflector (RR) in AS 4000 to treat BGP sessions with the peer group rr-client-2
in AS 2500 as iBGP sessions. That is, iBGP attributes (LOCAL_PREF, ORIGINATOR_ID, and
CLUSTER_LIST) will not be dropped from routes in advertisements to and from the neighbors belonging to
the peer group; the attributes will be passed unmodified. AS 2500 will not be prepended to the AS_PATH
attribute in routes to or from the peer group.
Additionally, the neighbor allow-policy command configures that the network administrator can configure
iBGP policies on the RR. That is, an outbound route map can be configured to change attributes that are sent
to the downstream peers. In this example, the command is applied to VPNv4 and VPNv6 address families.
router bgp 4000
neighbor rr-client-2 peer-group
neighbor 192.168.1.1 peer-group rr-client-2
neighbor 192.168.4.1 peer-group rr-client-2
neighbor rr-client-2 remote-as 2500
neighbor rr-client-2 local-as 2500
neighbor rr-client-2 route-reflector-client
address-family vpnv4
neighbor rr-client-2 allow-policy
!
address-family vpnv6
neighbor rr-client-2 allow-policy

Additional References for Support for iBGP Local-AS
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List,
All Releases

BGP commands

Cisco IOS IP Routing: BGP
Command Reference

Migration of autonomous systems

“BGP Support for Dual AS
Configuration for Network AS
Migrations” module in the IP
Routing: BGP Configuration
Guide, Cisco IOS XE Release 3S

IP Routing: BGP Configuration Guide
1052


BGP—Support for iBGP Local-AS
Feature Information for BGP—Support for iBGP Local-AS

Technical Assistance
Description

Link

The Cisco Support and Documentation website provides online resources to http://www.cisco.com/cisco/
download documentation, software, and tools. Use these resources to install web/support/index.html
and configure the software and to troubleshoot and resolve technical issues
with Cisco products and technologies. Access to most tools on the Cisco
Support and Documentation website requires a Cisco.com user ID and
password.

Feature Information for BGP—Support for iBGP Local-AS
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 93: Feature Information for BGP—Support for iBGP Local-AS

Feature Name

Releases

Feature Information

BGP—Support
for iBGP
Local-AS

Cisco IOS XE Prior to the BGP—Support for Local-AS feature, the neighbor local-as
Release 3.9S command was used on a route reflector to customize AS_PATH attributes
for routes received from an eBGP neighbor. The neighbor local-as
command can now be used to enable the sending of the iBGP attributes
(LOCAL_PREF, ORIGINATOR_ID, CLUSTER_ID, and
CLUSTER_LIST) over an iBGP local-AS session. This functionality is
useful when merging two autonomous systems, when it is advantageous
to keep the iBGP attributes in routes.
Prior to the BGP—Support for iBGP Local-AS feature, the RR should not
have been configured to change iBGP attributes. With the introduction of
this feature, the RR can be configured to change iBGP attributes, providing
more flexibility.
The following command was introduced:
• neighbor allow-policy
The following commands were modified:
• neighbor local-as
• show ip bgp vpnv4

IP Routing: BGP Configuration Guide
1053


BGP—Support for iBGP Local-AS
Feature Information for BGP—Support for iBGP Local-AS

IP Routing: BGP Configuration Guide
1054
