---
title: "BGP Attribute Filter and Enhanced Attribute Error Handling"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-attribute-filter-and-enhanced-attribute-error-handling
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 63 BGP Attribute Filter and Enhanced Attribute Error Handling The BGP Attribute Filter feature allows you to “treat-as-withdraw” updates that contain specific path attributes. The prefixes contained in the update are removed from the routing table. The feature also allows you to remove specific path attributes from incoming updates. Both behaviors provide an increased measure of security"
---

# BGP Attribute Filter and Enhanced Attribute Error Handling

CHAPTER

63

BGP Attribute Filter and Enhanced Attribute Error
Handling
The BGP Attribute Filter feature allows you to “treat-as-withdraw” updates that contain specific path attributes.
The prefixes contained in the update are removed from the routing table. The feature also allows you to remove
specific path attributes from incoming updates. Both behaviors provide an increased measure of security. The
BGP Enhanced Attribute Error Handling feature prevents peer sessions from flapping due to errors from any
malformed update, thereby saving resources.
• Finding Feature Information, on page 943
• Information About BGP Attribute Filtering, on page 943
• How to Filter BGP Path Attributes, on page 945
• Configuration Examples for BGP Attribute Filter, on page 948
• Additional References, on page 949
• Feature Information for BGP Attribute Filter and Enhanced Attribute Error Handling, on page 949

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP Attribute Filtering
BGP Attribute Filter and Enhanced Attribute Error Handling
The BGP Attribute Filter feature provides two ways to achieve an increased measure of security:
• The feature allows you to treat-as-withdraw an Update coming from a specified neighbor if the Update
contains a specified attribute type. When an Update is treat-as-withdraw, the prefixes in the Update are
removed from the BGP routing table (if they existed in the routing table).

IP Routing: BGP Configuration Guide
943


BGP Attribute Filter and Enhanced Attribute Error Handling
BGP Attribute Filter and Enhanced Attribute Error Handling

• The feature also allows you to drop specified path attributes from an Update, and then the system processes
the rest of the Update as usual.
The BGP Enhanced Attribute Error Handling feature prevents peer sessions from flapping due to a malformed
Update. The malformed Update is treat-as-withdraw and does not cause the BGP session to be reset. This
feature is enabled by default, but can be disabled.
The features are implemented in the following order:
1. Received Updates that contain user-specified path attributes are treat-as-withdraw (as long as the NLRI
can be parsed successfully). If there is an existing prefix in the BGP routing table, it will be removed. The
neighbor path-attribute treat-as-withdraw command configures this feature.
2. User-specified path attributes are discarded from received Updates, and the rest of the Update is processed
normally. The neighbor path-attribute discard command configures this feature.
3. Received Updates that are malformed are treat-as-withdraw. This feature is enabled by default; it can be
disabled by configuring the no bgp enhanced-error command.
Details About Specifying Attributes as Treat-as-Withdraw
Attribute types 1, 2, 3, 4, 8, 14, 15, and 16 cannot be configured for path attribute treat-as-withdraw.
Attribute type 5 (localpref), type 9 (Originator,) and type 10 (Cluster-id) can be configured for treat-as-withdraw
for eBGP neighbors only.
Configuring path attributes to be treated as withdrawn will trigger an inbound Route Refresh to ensure that
the routing table is up to date.
Details About Specifying Attributes as Discard
Attribute types 1, 2, 3, 4, 8, 14, 15, and 16 cannot be configured for path attribute discard.
Attribute type 5 (localpref), type 9 (Originator), and type 10 (Cluster-id) can be configured for discard for
eBGP neighbors only.
Configuring path attributes to be discarded will trigger an inbound Route Refresh to ensure that the routing
table is up to date.
Details About Enhanced Attribute Error Handling
If a malformed Update is received, it is treat-as-withdraw to prevent peer sessions from flapping due to the
processing of BGP path attributes. This feature applies to eBGP and iBGP peers. This feature is enabled by
default; it can be disabled.
If the BGP Enhanced Attribute Error Handling feature is enabled or disabled, BGP places the MP_REACH
attribute (attribute 14) at the beginning of an attribute list while formatting an update. Enhanced attribute error
handling functions more easily when the MP_REACH attribute is at the beginning of the attribute list.

IP Routing: BGP Configuration Guide
944


BGP Attribute Filter and Enhanced Attribute Error Handling
How to Filter BGP Path Attributes

How to Filter BGP Path Attributes
Treat-as-Withdraw BGP Updates Containing a Specified Path Attribute
Note

Performing this task will trigger an inbound Route Refresh to ensure that the routing table is up to date.

SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
router bgp as-number
neighbor {ip-address | ipv6-address} path-attribute treat-as-withdraw {attribute-value | range
start-value end-value} in
5. Repeat Step 4 to configure other attributes not in a range or to configure a different neighbor.
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

router bgp as-number
Example:

Configures a BGP routing process and enters router
configuration mode.

Device(config)# router bgp 65000

Step 4

neighbor {ip-address | ipv6-address} path-attribute
treat-as-withdraw {attribute-value | range start-value
end-value} in
Example:
Device(config-router)# neighbor 2001:DB8:1::1
path-attribute treat-as-withdraw 100 in

Treat-as-withdraw any incoming Update messages that
contain the specified path attribute or range of path
attributes.
• Any prefixes in an Update that is treat-as-withdraw
are removed from the BGP routing table.
• The specific attribute value and the range of attribute
values are independent of each other.

IP Routing: BGP Configuration Guide
945


BGP Attribute Filter and Enhanced Attribute Error Handling
Discarding Specific Path Attributes from an Update Message

Command or Action
Step 5

Repeat Step 4 to configure other attributes not in a range
or to configure a different neighbor.

Step 6

end

Purpose

Exits to privileged EXEC mode.

Example:
Device(config-router)# end

Discarding Specific Path Attributes from an Update Message
Note

Performing this task will trigger an inbound Route Refresh to ensure that the routing table is up to date.

SUMMARY STEPS
1.
2.
3.
4.

enable
configure terminal
router bgp as-number
neighbor {ip-address | ipv6-address} path-attribute discard {attribute-value | range start-value
end-value} in
5. Repeat Step 4 to configure other attributes not in a range or to configure a different neighbor.
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

router bgp as-number
Example:

Configures a BGP routing process and enters router
configuration mode.

Device(config)# router bgp 6500

Step 4

Drops specified path attributes from Update messages from
neighbor {ip-address | ipv6-address} path-attribute
discard {attribute-value | range start-value end-value} in the specified neighbor.
Example:

IP Routing: BGP Configuration Guide
946


BGP Attribute Filter and Enhanced Attribute Error Handling
Displaying Withdrawn or Discarded Path Attributes

Command or Action

Purpose

Device(config-router)# neighbor 2001:DB8:1::1
path-attribute discard 128 in

Step 5

Repeat Step 4 to configure other attributes not in a range
or to configure a different neighbor.
Example:

Step 6

Exits to privileged EXEC mode.

end
Example:
Device(config-router)# end

Displaying Withdrawn or Discarded Path Attributes
Perform any of these steps in any order to display information about treat-as-withdraw, discarded, or unknown
path attributes. You can use the show ip bgp command with any address family that BGP supports, such as
show ip bgp ipv4 multicast, show ip bgp ipv6 unicast, etc.
SUMMARY STEPS
1.
2.
3.
4.
5.
6.

enable
show ip bgp neighbor [ip-address | ipv6-address]
show ip bgp path-attribute unknown
show ip bgp path-attribute discard
show ip bgp vpnv4 all prefix
show ip bgp neighbors prefix

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

show ip bgp neighbor [ip-address | ipv6-address]
Example:
Device# show ip bgp neighbor 2001:DB8:1::1

Step 3

show ip bgp path-attribute unknown
Example:

(Optional) Displays the configured discard and
treat-as-withdraw attribute values for the neighbor, counts
of Updates with such attributes discarded or
treat-as-withdraw, and the count of malformed
treat-as-withdraw Updates.
(Optional) Displays all prefixes that have an unknown
attribute.

Device# show ip bgp path-attribute unknown

IP Routing: BGP Configuration Guide
947


BGP Attribute Filter and Enhanced Attribute Error Handling
Configuration Examples for BGP Attribute Filter

Step 4

Command or Action

Purpose

show ip bgp path-attribute discard

(Optional) Displays all prefixes for which an attribute has
been discarded.

Example:
Device# show ip bgp path-attribute discard

Step 5

show ip bgp vpnv4 all prefix
Example:

(Optional) Displays the unknown attributes and discarded
attributes associated with a prefix.

Device# show ip bgp vpnv4 all 192.168.1.0

Step 6

show ip bgp neighbors prefix
Example:

(Optional) Displays the configured discard and
treat-as-withdraw attributes associated with a prefix.

Device# show ip bgp neighbors 192.168.1.0

Configuration Examples for BGP Attribute Filter
Examples: Withdraw Updates Based on Path Attribute
The following example shows how to configure the device to treat-as-withdraw any Update messages
from the specified neighbor that contain the unwanted path attribute 100 or 128:
router bgp 65600
neighbor 2001:DB8:1::2 path-attribute treat-as-withdraw 100 in
neighbor 2001:DB8:1::2 path-attribute treat-as-withdraw 128 in

The following example shows how to configure the device to treat-as-withdraw any Update messages
from the specified neighbor that contain the unwanted path attributes in the range from 21 to 255:
router bgp 65600
neighbor 2001:DB8:1::2 path-attribute treat-as-withdraw 21 255 in

Examples: Discard Path Attributes from Updates
The following example shows how to configure the device to discard path attributes 100 and 128
from incoming Update messages from the specified neighbor. The rest of the Update message will
be processed as usual.
router bgp 65600
neighbor 2001:DB8:1::1 path-attribute discard 100 in
neighbor 2001:DB8:1::1 path-attribute discard 128 in

IP Routing: BGP Configuration Guide
948


BGP Attribute Filter and Enhanced Attribute Error Handling
Additional References

The following example shows how to configure the device to discard path attributes in the range
from 17 to 255 from incoming Update messages from the specified neighbor. The rest of the Update
message will be processed as usual.
router bgp 65600
neighbor 2001:DB8:1::1 path-attribute discard 17 255 in

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Commands List, All Releases

BGP commands

Cisco IOS IP Routing: BGP Command Reference

Standards and RFCs
Standard/RFC

Title

draft-ietf-idr-error-handling Revised Error Handling for BGP Updates from External Neighbors
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

Feature Information for BGP Attribute Filter and Enhanced
Attribute Error Handling
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
949


BGP Attribute Filter and Enhanced Attribute Error Handling
Feature Information for BGP Attribute Filter and Enhanced Attribute Error Handling

Table 83: Feature Information for BGP Attribute Filter and Enhanced Attribute Error Handling

Feature Name

Releases

BGP Attribute Filter and Enhanced Cisco IOS XE Release 3.7S
Attribute Error Handling

Feature Information
The BGP Attribute Filter allows
you to “treat-as-withdraw” updates
that contain specific path attributes.
The prefixes contained in the
update are removed from the
routing table. The feature also
allows you to remove specific path
attributes from incoming updates.
Both behaviors provide an
increased measure of security. The
BGP Enhanced Attribute Error
Handling feature prevents peer
sessions from flapping due to errors
from any malformed update,
thereby saving resources.
The following commands were
introduced: bgp enhanced-error,
neighbor path-attribute discard,
neighbor path-attribute
treat-as-withdraw, show ip bgp
path-attribute discard, and show
ip bgp path-attribute unknown.
The following commands were
modified: show ip bgp, show ip
bgp neighbor, and show ip bgp
vpnv4 all.

IP Routing: BGP Configuration Guide
950
