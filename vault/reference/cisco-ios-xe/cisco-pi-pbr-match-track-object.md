---
title: "PBR Match Track Object"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-pbr-match-track-object
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 7 PBR Match Track Object The PBR Match Track Object feature enables a device to track the stub object during Policy Based Routing (PBR). • Finding Feature Information, on page 81 • Restrictions for PBR Match Track Object, on page 81 • Information About PBR Match Track Object, on page 82 • How to Configure PBR Match Track Object, on page 83 • Verifying PBR Match Track Object, on page 83 •"
---

# PBR Match Track Object

CHAPTER

7

PBR Match Track Object
The PBR Match Track Object feature enables a device to track the stub object during Policy Based Routing
(PBR).
• Finding Feature Information, on page 81
• Restrictions for PBR Match Track Object, on page 81
• Information About PBR Match Track Object, on page 82
• How to Configure PBR Match Track Object, on page 83
• Verifying PBR Match Track Object, on page 83
• Configuration Examples for PBR Match Track Object, on page 84
• Additional References for PBR Match Track Object, on page 85
• Feature Information for PBR Match Track Object, on page 85

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Restrictions for PBR Match Track Object
• You can use only one match track variable at a time in a route map sequence.
• You must remove the existing match track object configuration before configuring another match track
object. The match track object is unregistered from the tracking component when you remove the match
track object number configuration.
• Route-map for PBR, does not take ‘track-object’ into consideration when used under the ‘Match clause’.
Match track-object is used for route distribution protocol (for example, BGP) only during the route
distribution. Track object cannot be used in route-map, when that route-map is used in PBR.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
81


PBR Match Track Object
Information About PBR Match Track Object

Information About PBR Match Track Object
PBR Match Track Object Overview
You refer to the stub object that you track as the match track object. The device checks for the existence of
the match track object and issues an error message if there is none. Then registration with the tracking
component is done to track this object. The device issues an error in case the registration fails.
Figure 5: Match track object registration

During redistribution, the routing protocols check the route map for matches with existing routes. This provides
an exact route map that corresponds to the specific match criteria. When you apply this route map with the
match track object, the device checks the status of the match track object and provides a specific route map.
Figure 6: Route map on redistribution using routing protocols

The device uses Border Gateway Protocol (BGP) for route-filtering and distribution. The device uses the
existing notification mechanism to notify the routing protocols about the new match clause and also notifies
the routing protocols about any change in the match track object status depending upon the Policy-Based
Routing (PBR) query on redistribution.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
82


PBR Match Track Object
How to Configure PBR Match Track Object

How to Configure PBR Match Track Object
Configuring PBR Match Track Object
SUMMARY STEPS
1.
2.
3.
4.
5.

enable
configure terminal
route-map map-tag
match track track-object-number
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

Enables policy routing and enters route-map configuration
mode.

route-map map-tag
Example:
Device(config)# route-map abc

Step 4

match track track-object-number

Tracks the stub object. Value ranges from 1 to 1000.

Example:

Note

Device(config-route-map)# match track 2

Step 5

This command is effective only when the track
object specified is available on the device.

Returns to privileged EXEC mode.

end
Example:
Device(config-route-map)# end

Verifying PBR Match Track Object
SUMMARY STEPS
1. enable
2. show route-map map-name

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
83


PBR Match Track Object
Configuration Examples for PBR Match Track Object

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

show route-map map-name

Displays brief information about a specific route-map.

Example:
Device# show route-map abc

Configuration Examples for PBR Match Track Object
Example: PBR Match Track Object Configuration
Device> enable
Device# configure terminal
Device(config)# route-map abc
Device(config-route-map)# match track 2
Device(config-route-map)# end

Example: Verifying PBR Match Track Object
Sample output for the show route-map map-name command
To display information about a specific route-map, use the show route-map map-name command in privileged
EXEC mode.
Device> enable
Device# show route-map abc
route-map abc, permit, sequence 10
Match clauses:
track-object 2
Set clauses:
Policy routing matches: 0 packets, 0 bytes

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
84


PBR Match Track Object
Additional References for PBR Match Track Object

Additional References for PBR Match Track Object
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

Feature Information for PBR Match Track Object
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Feature Name
PBR Match Track Object

Releases

Feature Information
The PBR Match Track Object
feature enables a device to track the
stub object during Policy Based
Routing.
The following command was
introduced: match track
track-object-number

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
85


PBR Match Track Object
Feature Information for PBR Match Track Object

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
86
