---
title: "BGP NSR Auto Sense"
type: reference
domain: cisco-ios-xe
slug: cisco-bgp-bgp-nsr-auto-sense
tier: reference
source: "Cisco IOS XE 16 — IP Routing: BGP Configuration Guide"
version: ios-xe-16
family: ip-routing-bgp
documentKind: "Documentation"
abstract: "CHAPTER 57 BGP NSR Auto Sense The BGP NSR Auto Sense feature is the default behavior implemented to reduce unnecessary churn in the event of a Route Processor (RP) failover. Prior to this feature, when an Active RP went down, the new Active RP that was taking over to provide Border Gateway Protocol (BGP) nonstop routing (NSR) would send a route-refresh request to all peers configured with NSR. H"
---

# BGP NSR Auto Sense

CHAPTER

57

BGP NSR Auto Sense
The BGP NSR Auto Sense feature is the default behavior implemented to reduce unnecessary churn in the
event of a Route Processor (RP) failover. Prior to this feature, when an Active RP went down, the new Active
RP that was taking over to provide Border Gateway Protocol (BGP) nonstop routing (NSR) would send a
route-refresh request to all peers configured with NSR. However, the new Active RP had already received all
the incoming updates while acting as the Standby RP. Sending route-refresh requests caused unnecessary
BGP churn during switchover; this feature prevents such route-refresh requests by default. This feature also
provides NSR support to peers that lack route-refresh capability. If you want to revert to the old behavior of
sending route-refresh requests, a new command is available to make that happen.
• Finding Feature Information, on page 889
• Information About BGP NSR Auto Sense, on page 889
• How to Disable the BGP NSR Auto Sense Feature, on page 890
• Configuration Example for BGP NSR Auto Sense, on page 891
• Additional References, on page 892
• Feature Information for BGP NSR Auto Sense, on page 892

Finding Feature Information
Your software release may not support all the features documented in this module. For the latest caveats and
feature information, see Bug Search Tool and the release notes for your platform and software release. To
find information about the features documented in this module, and to see a list of the releases in which each
feature is supported, see the feature information table at the end of this module.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

Information About BGP NSR Auto Sense
Benefits of BGP NSR Auto Sense
The BGP NSR Auto Sense feature has the following benefits:
• This feature is a default behavior that reduces unnecessary churn in the event of a Route Processor (RP)
failover. Prior to this feature, when an Active RP went down, the new Active RP that was taking over
to provide BGP nonstop routing (NSR) would send a route-refresh request to all peers configured with

IP Routing: BGP Configuration Guide
889


BGP NSR Auto Sense
Consequence of Reverting to NSR Without Auto Sense

NSR. However, the Active RP had already received all the incoming updates while acting as the Standby
RP. Sending route-refresh requests caused unnecessary BGP churn during switchover; this feature prevents
such route-refresh requests by default.
• This feature also provides NSR support to peers that lack route-refresh capability. Prior to this feature,
NSR was not supported for peers that lack route-refresh capability.
• There is no need to configure this feature; it is the default behavior in releases where this feature is
implemented.
• If you want to revert to the former behavior of a new Active RP sending route-refresh requests when an
RP goes down, you can use the bgp sso route-refresh-enable command.

Consequence of Reverting to NSR Without Auto Sense
You might have a reason not to want the default behavior of the BGP NSR Auto Sense feature. If you want
to revert to the former behavior of a new Active RP sending route-refresh requests when an RP goes down,
you can use the bgp sso route-refresh-enable command. This action causes peers that did not exchange
route-refresh capability in the received OPEN message to have NSR support disabled.

How to Disable the BGP NSR Auto Sense Feature
Disabling the BGP NSR Auto Sense Feature
The BGP NSR Auto Sense feature is enabled by default. Perform this task only if you want to disable the
feature, for example, if routes that were being advertised at the point of switchover did not get processed by
the Standby RP (new Active RP) for some reason. In that case, sending a route-refresh to request all the routes
that the peer had ever advertised would be helpful. After performing this task, in the event of a failover, a new
Active RP will send route-refresh requests to peers configured with NSR.
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
bgp sso route-refresh-enable
end
show ip bgp vpnv4 all neighbor [ip-address]
show ip bgp vpnv4 all sso summary

DETAILED STEPS

Step 1

Command or Action

Purpose

enable

Enables privileged EXEC mode.

Example:
Router> enable

IP Routing: BGP Configuration Guide
890

• Enter your password if prompted.


BGP NSR Auto Sense
Configuration Example for BGP NSR Auto Sense

Step 2

Command or Action

Purpose

configure terminal

Enters global configuration mode.

Example:
Router# configure terminal

Step 3

router bgp as-number
Example:
Router(config)# router bgp 6500

Configures a BGP routing process and enters router
configuration mode.
• The as-number argument indicates the number of an
autonomous system that identifies the router to other
BGP routers and tags the routing information passed
along. Valid numbers are from 0 to 65535. Private
autonomous system numbers that can be used in
internal networks range from 64512 to 65535.
• Regarding the 4-byte AS configuration, please see the
bgp asnotation dot command in the IP Routing: BGP
Command Reference.

Step 4

bgp sso route-refresh-enable

Disables the BGP NSR Auto Sense feature.

Example:
Router(config-router)# bgp sso route-refresh-enable

Step 5

Exits to privileged EXEC mode.

end
Example:
Router(config-router)# end

Step 6

show ip bgp vpnv4 all neighbor [ip-address]

(Optional) Displays information about BGP peers.

Example:
Router# show ip bgp vpnv4 all neighbor 10.0.0.2

Step 7

show ip bgp vpnv4 all sso summary
Example:

(Optional) Displays the number of BGP peers that support
BGP nonstop routing (NSR) with stateful switchover (SSO).

Router# show ip bgp vpnv4 all sso summary

Configuration Example for BGP NSR Auto Sense
Example: Disabling the BGP NSR Auto Sense Feature
router bgp 65600

IP Routing: BGP Configuration Guide
891


BGP NSR Auto Sense
Additional References

bgp sso route-refresh-enable

Additional References
Related Documents
Related Topic

Document Title

Cisco IOS commands

Cisco IOS Master Command List,
All Releases

BGP commands

Cisco IOS IP Routing: BGP
Command Reference

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

Feature Information for BGP NSR Auto Sense
The following table provides release information about the feature or features described in this module. This
table lists only the software release that introduced support for a given feature in a given software release
train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support.
To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.

IP Routing: BGP Configuration Guide
892


BGP NSR Auto Sense
Feature Information for BGP NSR Auto Sense

Table 76: Feature Information for BGP NSR Auto Sense

Feature Name

Releases

Feature Information

BGP NSR Auto Sense

15.2(2)S

The BGP NSR Auto Sense feature
is implemented by default to reduce
unnecessary churn in the event of
an RP failover. This feature also
provides NSR support to peers that
lack route-refresh support.

Cisco IOS XE Release 3.6S

The following command was
introduced: bgp sso
route-refresh-enable.

IP Routing: BGP Configuration Guide
893


BGP NSR Auto Sense
Feature Information for BGP NSR Auto Sense

IP Routing: BGP Configuration Guide
894
