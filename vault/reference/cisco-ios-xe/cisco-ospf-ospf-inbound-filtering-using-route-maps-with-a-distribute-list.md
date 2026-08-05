---
title: "OSPF Inbound Filtering Using Route Maps with a Distribute List"
type: reference
domain: cisco-ios-xe
slug: cisco-ospf-ospf-inbound-filtering-using-route-maps-with-a-distribute-list
tier: reference
source: "Cisco IOS XE 16 — IP Routing: OSPF Configuration Guide"
version: ios-xe-16
family: ip-routing-ospf
documentKind: "Documentation"
abstract: "CHAPTER 22 OSPF Inbound Filtering Using Route Maps with a Distribute List The OSPF Inbound Filtering Using Route Maps with a Distribute List feature allows users to define a route map to prevent Open Shortest Path First (OSPF) routes from being added to the routing table. In the route map, the user can match on any attribute of the OSPF route. • Finding Feature Information, page 229 • Prerequisi"
---

# OSPF Inbound Filtering Using Route Maps with a Distribute List

CHAPTER

22

OSPF Inbound Filtering Using Route Maps with
a Distribute List
The OSPF Inbound Filtering Using Route Maps with a Distribute List feature allows users to define a route
map to prevent Open Shortest Path First (OSPF) routes from being added to the routing table. In the route
map, the user can match on any attribute of the OSPF route.
• Finding Feature Information, page 229
• Prerequisites OSPF Inbound Filtering Using Route Maps with a Distribute List, page 229
• Information About OSPF Inbound Filtering Using Route Maps with a Distribute List, page 230
• How to Configure OSPF Inbound Filtering Using Route Maps, page 231
• Configuration Examples for OSPF Inbound Filtering Using Route Maps with a Distribute List, page
232
• Additional References, page 233
• Feature Information for OSPF Inbound Filtering Using Route Maps with a Distribute List, page 234

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Prerequisites OSPF Inbound Filtering Using Route Maps with
a Distribute List
It is presumed that you have OSPF configured in your network.

IP Routing: OSPF Configuration Guide
229


OSPF Inbound Filtering Using Route Maps with a Distribute List
Information About OSPF Inbound Filtering Using Route Maps with a Distribute List

Information About OSPF Inbound Filtering Using Route Maps
with a Distribute List
Benefits of OSPF Route-Map-Based-Filtering
Users can define a route map to prevent OSPF routes from being added to the routing table. This filtering
happens at the moment when OSPF is installing the route in the routing table. This feature has no effect on
LSA flooding. In the route map, the user can match on any attribute of the OSPF route. That is, the route map
could be based on the following match options:
• match interface
• match ip address
• match ip next-hop
• match ip route-source
• match metric
• match route-type
• match tag
This feature can be useful during redistribution if the user tags prefixes when they get redistributed on ASBRs
and later uses the tag to filter the prefixes from being installed in the routing table on other routers.
Filtering Based on Route Tag
Users can assign tags to external routes when they are redistributed to OSPF. Then the user can deny or permit
those routes in the OSPF domain by identifying that tag in the route-map and distribute-list in commands.
Filtering Based on Route Type
In OSPF, the external routes could be Type 1 or Type 2. Users can create route maps to match either Type 1
or Type 2 and then use the distribute-list in command to filter certain prefixes. Also, route maps can identify
internal routes (interarea and intra-area) and then those routes can be filtered.
Filtering Based on Route Source
When a match is done on the route source, the route source represents the OSPF Router ID of the LSA
originator of the LSA in which the prefix is advertised.
Filtering Based on Interface
When a match is done on the interface, the interface represents the outgoing interface for the route that OSPF
is trying to install in the routing table.
Filtering Based on Next-Hop
When a match is done on the next hop, the next hop represents the next hop for the route that OSPF is trying
to install in the routing table.

IP Routing: OSPF Configuration Guide
230


OSPF Inbound Filtering Using Route Maps with a Distribute List
How to Configure OSPF Inbound Filtering Using Route Maps

How to Configure OSPF Inbound Filtering Using Route Maps
Configuring OSPF Inbound Filtering Using a Route Map
SUMMARY STEPS
1. enable
2. configure terminal
3. route-map map-tag [permit | deny] [sequence-number]
4. match tag tag-name
5. Repeat Steps 3 and 4 with other route-map and match commands if you choose.
6. exit
7. router ospf process-id
8. distribute-list route-map map-tag in
9. end

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

route-map map-tag [permit | deny] [sequence-number] Defines a route map to control filtering.
Example:
Router(config)# route-map tag-filter deny 10

Step 4

match tag tag-name
Example:

Example:
or other match commands

Matches routes with a specified name, to be used as the
route map is referenced.
• At least one match command is required, but it need
not be this matchcommand. This is just an example.
• The list of match commands available to be used in
this type of route map appears on the distribute-list
in command reference page.

IP Routing: OSPF Configuration Guide
231


OSPF Inbound Filtering Using Route Maps with a Distribute List
Configuration Examples for OSPF Inbound Filtering Using Route Maps with a Distribute List

Command or Action

Purpose
• This type of route map will have no set commands.

Example:
Router(config-router)# match tag 777

Step 5

Repeat Steps 3 and 4 with other route-map and match -commands if you choose.

Step 6

exit

Exits router configuration mode.

Example:
Router(config-router)# exit

Step 7

router ospf process-id

Configures an OSPF routing process.

Example:
Router(config)# router ospf 1

Step 8

distribute-list route-map map-tag in

Enables filtering based on an OSPF route map.

Example:
Router(config-router)# distribute-list route-map
tag-filter in

Step 9

Exits router configuration mode.

end
Example:
Router(config-router)# end

Configuration Examples for OSPF Inbound Filtering Using Route
Maps with a Distribute List
Example OSPF Route-Map-Based Filtering
In this example, OSPF external LSAs have a tag. The value of the tag is examined before the prefix is installed
in the routing table. All OSPF external prefixes that have the tag value of 777 are filtered (prevented from
being installed in the routing table). The permit statement with sequence number 20 has no match conditions,
and there are no other route-map statements after sequence number 20, so all other conditions are permitted.
route-map tag-filter deny 10
match tag 777
route-map tag-filter permit 20

IP Routing: OSPF Configuration Guide
232


OSPF Inbound Filtering Using Route Maps with a Distribute List
Additional References

!
router ospf 1
router-id 10.0.0.2
log-adjacency-changes
network 172.16.2.1 0.0.0.255 area 0
distribute-list route-map tag-filter in

Additional References
The following sections provide references related to configuring the OSPF Inbound Filtering Using Route
Maps with a Distribute List feature.
Related Documents
Related Topic

Document Title

OSPF commands

Cisco IOS IP Routing: OSPF Command Reference

Configuring OSPF

"Configuring OSPF"

Cisco IOS master command list, all releases

Cisco IOS Master Command List, All Releases

Standards
Standard

Title

No new or modified standards are supported by this -feature, and support for existing standards has not
been modified by this feature.

MIBs
MIB

MIBs Link

No new or modified MIBs are supported by this
feature, and support for existing MIBs has not been
modified by this feature.

To locate and download MIBs for selected platforms,
Cisco IOS XE software releases, and feature sets, use
Cisco MIB Locator found at the following URL:
http://www.cisco.com/go/mibs

RFCs
RFC

Title

No new or modified RFCs are supported by this
feature, and support for existing RFCs has not been
modified by this feature.

--

IP Routing: OSPF Configuration Guide
233


OSPF Inbound Filtering Using Route Maps with a Distribute List
Feature Information for OSPF Inbound Filtering Using Route Maps with a Distribute List

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

Feature Information for OSPF Inbound Filtering Using Route
Maps with a Distribute List
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 25: Feature Information for OSPF Inbound Filtering Using Route Maps with a Distribute List

Feature Name

Releases

OSPF Inbound Filtering Using
Cisco IOS XE Release 2.1
Route Maps with a Distribute List

Feature Information
The OSPF Inbound Filtering Using
Route Maps with a Distribute List
feature allows users to define a
route map to prevent OSPF routes
from being added to the routing
table.
The following commands are
introduced or modified in the
feature documented in this module:
• distribute-list in (IP)

IP Routing: OSPF Configuration Guide
234
