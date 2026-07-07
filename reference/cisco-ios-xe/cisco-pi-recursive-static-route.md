---
title: "Recursive Static Route"
type: reference
domain: cisco-ios-xe
slug: cisco-pi-recursive-static-route
tier: reference
source: "Cisco IOS XE 3S — IP Routing: Protocol-Independent Configuration Guide"
version: ios-xe-3s
family: ip-routing-protocol-independent
documentKind: "Documentation"
abstract: "CHAPTER 19 Recursive Static Route The Recursive Static Route feature enables you to install a recursive static route into the Routing Information Base (RIB) even if the next-hop address of the static route or the destination network itself is already available in the RIB as part of a previously learned route. This module explains recursive static routes and how to configure the Recursive Static"
---

# Recursive Static Route

CHAPTER

19

Recursive Static Route
The Recursive Static Route feature enables you to install a recursive static route into the Routing Information
Base (RIB) even if the next-hop address of the static route or the destination network itself is already available
in the RIB as part of a previously learned route. This module explains recursive static routes and how to
configure the Recursive Static Route feature.
• Finding Feature Information, on page 195
• Restrictions for Recursive Static Route, on page 195
• Information About Recursive Static Route, on page 196
• How to Install Recursive Static Route, on page 196
• Configuration Examples for Recursive Static Route, on page 200
• Additional References for Recursive Static Route, on page 201
• Feature Information for Recursive Static Routes, on page 201

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to https://cfnng.cisco.com/. An account on Cisco.com is not required.

Restrictions for Recursive Static Route
When recursive static routes are enabled using route maps, only one route map can be entered per virtual
routing and forwarding (VRF) instance or topology. If a second route map is entered, the new map will
overwrite the previous one.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
195


Recursive Static Route
Information About Recursive Static Route

Information About Recursive Static Route
How to Install Recursive Static Route
Installing Recursive Static Routes in a VRF
Perform these steps to install recursive static routes in a specific virtual routing and forwarding (VRF) instance.
You can configure the recursive-static-route functionality on any number of VRFs. Installing recursive static
routes in specific VRFs allows you to retain the default RIB behavior (of removing recursive static routes)
for the rest of the network.
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

enable
configure terminal
vrf definition vrf-name
rd route-distinguisher
address-family {ipv4 | ipv6}
exit
exit
ip route [vrf vrf-name] prefix mask ip-address
ip route static install-routes-recurse-via-nexthop [vrf vrf-name]
end
show running-config | include install
show ip route vrf vrf-name

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
Example:

Creates a virtual routing and forwarding (VRF) routing
table instance and enters VRF configuration mode.

Device(config)# vrf definition vrf1

Step 4

rd route-distinguisher

Specifies a route distinguisher for a VRF instance.

Example:

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
196


Recursive Static Route
Installing Recursive Static Routes Using a Route Map

Command or Action

Purpose

Device(config-vrf)# rd 100:1

Step 5

address-family {ipv4 | ipv6}

Enters VRF address family configuration mode to specify
an IPv4 or IPv6 address family for a VRF.

Example:
Device(config-vrf)# address-family ipv4

Step 6

Exits VRF address family configuration mode.

exit
Example:
Device(config-vrf-af)# exit

Step 7

Exits VRF configuration mode.

exit
Example:
Device(config-vrf)# exit

Step 8

ip route [vrf vrf-name] prefix mask ip-address

Configures a static route for a specific VRF instance.

Example:
Device(config)# ip route vrf vrf1 10.0.2.0
255.255.255.0 10.0.1.1

Step 9

ip route static install-routes-recurse-via-nexthop [vrf
vrf-name]

Enables recursive static routes to be installed in the RIB
of a specific VRF instance.

Example:
Device(config)# ip route static
install-routes-recurse-via-nexthop vrf vrf1

Step 10

Exits global configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config)# end

Step 11

show running-config | include install

Displays all recursive static route configurations.

Example:
Device# show running-config | inc install

Step 12

Displays the IP routing table associated with a specific
VRF.

show ip route vrf vrf-name
Example:
Device# show ip route vrf vrf1

Installing Recursive Static Routes Using a Route Map
Perform this task to install recursive static routes in a virtual routing and forwarding (VRF) instance defined
by a route map. You can perform this task if you want to install recursive static routes for only a certain range
of networks. If the route-map keyword is used without the vrf keyword, recursive static routes defined by
the route map will be applicable for the global VRF or topology.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
197


Recursive Static Route
Installing Recursive Static Routes Using a Route Map

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

enable
configure terminal
vrf definition vrf-name
rd route-distinguisher
address-family {ipv4 | ipv6}
exit
exit
ip route [vrf vrf-name] prefix mask ip-address
access-list access-list-number permit source [source-wildcard]
route-map map-tag
match ip address access-list-number
exit
ip route static install-routes-recurse-via-nexthop [vrf vrf-name] [route-map map-name]
end
show running-config | include install
show ip route vrf vrf-name

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
Example:

Creates a virtual routing and forwarding (VRF) routing
table instance and enters VRF configuration mode.

Device(config)# vrf definition vrf1

Step 4

rd route-distinguisher

Specifies a route distinguisher for a VRF instance.

Example:
Device(config-vrf)# rd 100:1

Step 5

address-family {ipv4 | ipv6}
Example:

Enters VRF address family configuration mode to specify
an IPv4 or an IPv6 address-family type for a VRF.

Device(config-vrf)# address-family ipv4

Step 6

Exits VRF address family configuration mode.

exit
Example:
Device(config-vrf-af)# exit

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
198


Recursive Static Route
Installing Recursive Static Routes Using a Route Map

Step 7

Command or Action

Purpose

exit

Exits VRF configuration mode.

Example:
Device(config-vrf)# exit

Step 8

ip route [vrf vrf-name] prefix mask ip-address

Configures a static route for a specific VRF instance.

Example:
Device(config)# ip route vrf vrf1 10.0.2.0
255.255.255.0 10.0.1.1

Step 9

access-list access-list-number permit source
[source-wildcard]

Defines a standard access list permitting addresses that
need to be translated.

Example:
Device(config)# access-list 10 permit 10.0.2.0
255.255.255.0

Step 10

Defines a route map to control route redistribution and
enters route-map configuration mode.

route-map map-tag
Example:
Device(config)# route-map map1

Step 11

match ip address access-list-number
Example:

Matches routes that have a destination network address
that is permitted by a standard or extended access list.

Device(config-route-map)# match ip address 10

Step 12

Exits route-map configuration mode.

exit
Example:
Device(config-route-map)# exit

Step 13

ip route static install-routes-recurse-via-nexthop [vrf
vrf-name] [route-map map-name]

Enables installation of recursive static routes defined by
a route map into the RIB of a specific VRF.

Example:
Device(config)# ip route static
install-routes-recurse-via-nexthop vrf vrf1
route-map map1

Step 14

Exits global configuration mode and returns to privileged
EXEC mode.

end
Example:
Device(config)# end

Step 15

show running-config | include install

Displays all recursive static route configurations.

Example:
Device# show running-config | inc install

Step 16

Displays the IP routing table associated with a specific
VRF.

show ip route vrf vrf-name
Example:
Device# show ip route vrf vrf1

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
199


Recursive Static Route
Configuration Examples for Recursive Static Route

Configuration Examples for Recursive Static Route
•

Example: Installing Recursive Static Routes in a VRF
The following example shows how to install recursive static routes into a specific virtual routing and
forwarding instance. By using the vrf keyword, you can ensure that recursive static routes are installed
in the Routing Information Base (RIB) of only the specified VRF. The rest of the network retains
the default behavior of not installing recursive static routes in the RIB. This example is based on the
assumption that a 10.0.0.0/8 route is already installed dynamically or statically in the RIB of vrf1.
Device> enable
Device# configure terminal
Device(config)# vrf definition vrf1
Device(config-vrf)# rd 1:100
Device(config-vrf)# address-family ipv4
Device(config-vrf-af)# exit
Device(config-vrf)# exit
Device(config)# ip route vrf vrf1 10.0.2.0 255.255.255.0 10.0.1.1
Device(config)# ip route static install-routes-recurse-via-nexthop vrf vrf1
Device(config)# end

Example: Installing Recursive Static Routes using a Route Map
You can use the route-map keyword to install recursive static routes defined by the route map into
the Routing Information Base (RIB). You can also specify a route map for a specific virtual routing
and forwarding (VRF) instance to ensure that the route map is applied to only the specified VRF. In
the example given below, a route map is specified for a specific VRF. This example is based on the
assumption that a 10.0.0.0/8 route is already installed statically or dynamically in the RIB of vrf1.
Device> enable
Device# configure terminal
Device(config)# vrf definition vrf1
Device(config-vrf)# rd 100:2
Device(config-vrf)# address-family ipv4
Device(config-vrf-af)# exit
Device(config-vrf)# exit
Device(config)# access-list 10 permit 10.0.2.0 255.255.255.0
Device(config)# route-map map1
Device(config-route-map)# match ip address 10
Device(config-route-map)# exit
Device(config)# ip route static install-routes-recurse-via-nexthop vrf vrf1 route-map map1
Device(config)# ip route vrf vrf1 10.0.2.0 255.255.255.0 10.0.1.1
Device(config)# ip route vrf vrf1 10.0.3.0 255.255.255.0 10.0.1.1
Device(config)# end

In the example above, route 10.0.2.0 255.255.255.0 10.0.1.1 will be installed in the RIB, but the
route 10.0.3.0 255. 255.255.0 10.0.1.1 will not be installed in the RIB because this route does not
match the network defined in the route map.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
200


Recursive Static Route
Additional References for Recursive Static Route

Additional References for Recursive Static Route
Related Documents
Related Topic

Document Title

IP routing protocol-independent commands Cisco IOS IP Routing: Protocol-Independent Command
Reference
Technical Assistance
Description

Link

The Cisco Support and Documentation website provides http://www.cisco.com/cisco/web/support/index.html
online resources to download documentation, software,
and tools. Use these resources to install and configure
the software and to troubleshoot and resolve technical
issues with Cisco products and technologies. Access to
most tools on the Cisco Support and Documentation
website requires a Cisco.com user ID and password.

Feature Information for Recursive Static Routes
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 20: Feature Information for Recursive Static Routes

Feature Name

Releases

Feature Information

Recursive Static Routes

Cisco IOS XE Release 3.9S

The Recursive Static Route feature
enables you to install a recursive
static route into the Routing
Information Base (RIB) even if the
next-hop address of the static route
or the destination network itself is
already available in the RIB as part
of a previously learned route.
The following command was
introduced: ip route static
install-recurse-via-nexthop.

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
201


Recursive Static Route
Feature Information for Recursive Static Routes

IP Routing: Protocol-Independent Configuration Guide, Cisco IOS XE Release 3S
202
